import postcss from 'rollup-plugin-postcss';

export default [
  {
    input: 'src/css/styles.css',
    plugins: [
      postcss({
        extract: './dist/static/styles.css', // output file
        config: './postcss.config.js',
        minimize: true,
      }),
    ]
  },
];
