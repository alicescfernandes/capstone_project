const esbuild = require('esbuild');
const fg = require('fast-glob');
const fs = require('fs');
const path = require('path');
const postcss = require('postcss');
const postcssConfig = require('./postcss.config');
const sass = require('sass');
const { platform } = require('os');

const isWatchMode = process.argv.includes('--watch');

async function buildCSS() {
  const cssFiles = await fg(['src/css/**/*.css', 'src/css/**/*.scss']);

  const processAll = async () => {
    await Promise.all(cssFiles.map(async (inputPath) => {
      const outputPath = inputPath
        .replace(/^src/, './dashboard/static')
        .replace(/\.scss$/, '.css');

      let css;

      if (inputPath.endsWith('.scss')) {
        const result = sass.compile(inputPath, { style: 'expanded' });
        css = result.css;
      } else {
        css = fs.readFileSync(inputPath, 'utf8');
      }

      const result = await postcss(postcssConfig.plugins).process(css, {
        from: inputPath,
        to: outputPath
      });

      fs.mkdirSync(path.dirname(outputPath), { recursive: true });
      fs.writeFileSync(outputPath, result.css);
      console.log('CSS compilado:', outputPath);
    }));
  };

  await processAll();

  if (isWatchMode) {
    fs.watch('src/css', { recursive: true }, async (eventType, filename) => {
      if (filename.endsWith('.css') || filename.endsWith('.scss')) {
        console.log('Alteração detetada em CSS/SCSS:', filename);
        await processAll();
      }
    });
    console.log('A ver ficheiros CSS/SCSS...');
  }
}

async function buildJS() {
  const entryPoints = await fg('src/js/*.js');


  const ctx = await esbuild.context({
    entryPoints,
    outdir: './dashboard/static/js',
    bundle: true,
    target: ['es2015'],
    // minify: true,
    sourcemap: true,
    // format: 'iife',
    platform: "browser"
  });


  if (isWatchMode) {
    await ctx.watch();
    console.log('A ver ficheiros JS...');
  } else {
    await ctx.rebuild();
    ctx.dispose();
    console.log('JS transpiled', entryPoints);
  }
}

(async () => {
  await buildCSS();
  await buildJS();
})();
