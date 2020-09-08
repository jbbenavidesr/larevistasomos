const { dest, src } = require('gulp');

// Grabs all css, runs them through css min
// and plops them in the dist folder
const js = () => {
    return src('./js/**/*')
        .pipe(dest('../static_compiled/js'));
};

module.exports = js;
