const { dest, src } = require('gulp');
const cssmin = require('gulp-minify-css');

// Grabs all css, runs them through css min
// and plops them in the dist folder
const css = () => {
    return src('./css/**/*')
        .pipe(
            cssmin()
        )
        .pipe(dest('../static_compiled/css'));
};

module.exports = css;
