const esbuild = require('esbuild');
const fg = require('fast-glob');
const fs = require('fs');
const path = require('path');
const postcss = require('postcss');
const postcssConfig = require('./postcss.config');

const isWatchMode = process.argv.includes('--watch');

async function buildCSS() {
  const cssFiles = await fg('src/css/**/*.css');

  const processAll = async () => {
    await Promise.all(cssFiles.map(async (inputPath) => {
      const outputPath = inputPath.replace(/^src/, './dashboard/static');
      const css = fs.readFileSync(inputPath, 'utf8');

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
      if (filename.endsWith('.css')) {
        console.log('Alteração detetada em CSS:', filename);
        await processAll();
      }
    });
    console.log('A ver ficheiros CSS...');
  }
}

async function buildJS() {
  const entryPoints = await fg('src/js/*.js');

  
  const ctx = await esbuild.context({
    entryPoints,
    outdir: './dashboard/static/js',
    bundle: true,
    minify: true,
    sourcemap: true,
    format: 'iife',
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
