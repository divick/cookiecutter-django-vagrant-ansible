var gulp = require('gulp');
var exec = require('child_process').exec;
var spawn = require('child_process').spawn;
var debug = require('gulp-debug');
var gutil = require('gulp-util');
var bower = require('bower');
var sass = require('gulp-sass');
var sh = require('shelljs');
require('shelljs/global');
var rename = require('gulp-rename');
var preprocess = require('gulp-preprocess');
var runSequence = require('run-sequence');
var argv = require('yargs')
    .default({port: 8080})
    .argv;
//var jshint = require('gulp-jshint');
var stylish = require('jshint-stylish');
var changed = require('gulp-changed');
var open = require("gulp-open");
var clean = require('gulp-clean');
var rename = require("gulp-rename");
var moment = require("moment");
var replace = require('gulp-replace');
var bump = require('gulp-bump');
var semver = require('semver');
var git = require('gulp-git');
var filter = require('gulp-filter');
var tag_version = require('gulp-tag-version');
var Q = require('q');
var merge = require('merge-stream');

// If BUILD_TARGET is not defined then we assume it to be development
var build_target = process.env.BUILD_TARGET || 'development';

// the source paths
var source_paths = {
  sass: ['./static/scss/**/*.scss'],
  sass_out: './static/css/**/*.min.css',
  scripts: ['./static/js/**/*.js'],
  js_config: ['./static/js/config.in'],
  js_config_out: './static/js/config.js',
};

// the destination paths
var dest_paths = {
  tmp: './www/css/',
  css: './static/css/',
  scripts: './static/js/',
  js_config: './static/js/',
};

gulp.task('default', function(){
    runSequence('compile', 'serve');
});

///////////////////////////////////////////////////////
// COMPILATION TASKS
///////////////////////////////////////////////////////
gulp.task('compile-sass', function() {
  console.log("Inside compile-scss");
  return gulp.src(source_paths.sass)
    .pipe(changed(dest_paths.tmp))
    .pipe(sass())
    .pipe(gulp.dest(dest_paths.tmp))
    .pipe(gulp.dest(dest_paths.css));
});

gulp.task('preprocess-js-config', function() {
  console.log("Inside preprocess-js-scripts");
  console.log(build_target);
  return gulp.src(source_paths.js_config)
    .pipe(changed(dest_paths.tmp))
    .pipe(preprocess({context: { BUILD_TARGET: build_target}}))
    .pipe(rename({ extname: '.js' }))
    .pipe(gulp.dest(dest_paths.js_config));
});

gulp.task('compile-all', [
                          //'lint',
                          'preprocess-js-config',
                          'compile-sass'
                          ]);

// compile everything after cleaning the build
gulp.task('compile', ['clean', 'clean-js-config'], function(){
  console.log("Inside task compile...");
  var deferred = Q.defer();

  runSequence('compile-all', function(){
    console.log("Calling deferred.resolve..");
    deferred.resolve();
  });

  return deferred.promise;
});

///////////////////////////////////////////////////////
// CLEAN TASKS
///////////////////////////////////////////////////////

gulp.task('clean', function() {
  return gulp.src(dest_paths.tmp, {read: false})
         .pipe(clean());
});

gulp.task('clean-js-config', function() {
  return gulp.src(source_paths.js_config_out, {read: false})
         .pipe(clean());
});

///////////////////////////////////////////////////////
// WATCH TASKS
///////////////////////////////////////////////////////

gulp.task('watch-sass', function(){
  return gulp.watch(source_paths.sass, ['compile-sass']);
});

gulp.task('watch-js-config', function(){
  return gulp.watch(source_paths.js_config, ['preprocess-js-config']);
});

gulp.task('watch', function() {
  runSequence([ 'watch-sass',
                'watch-js-config'
              ]);
});

///////////////////////////////////////////////////////
// LOCAL SERVER TASKS
///////////////////////////////////////////////////////

// migrate django
gulp.task('migrate', [], function() {
    console.log('Running migrations...');
    return exec('pythong manage.py migrate');
});


// start django dev server
gulp.task('run-server', [], function() {
    var port = argv.port;
    console.log('Running django dev server on port ' + port);

    var cmd = spawn('python',
                    ['manage.py', 'runserver', '0.0.0.0:' + port],
                    {stdio: 'inherit'});
    cmd.on('close', function (code) {
      console.log('my-task exited with code ' + code);
    });
    return;
});

// the options used by gulp-open when booting the test server
var open_options = {
  uri: "http://localhost:8000",
};

// open browser after starting server
gulp.task('open-browser', ['run-server'], function() {
  console.log("Running open-browser...");
  return gulp.src('')
  .pipe(open(open_options));
});

// compile then boot up the ionic site in a browser
gulp.task('serve', ['migrate', 'run-server', 'watch']);

///////////////////////////////////////////////////////
// MISC TASKS
///////////////////////////////////////////////////////

// used for bumping versions and getting the version info
// `fs` is used instead of require to prevent caching in watch
// (require caches)
var fs = require('fs');
var getPackageJson = function () {
  return JSON.parse(fs.readFileSync('./package.json', 'utf8'));
};

/**
 * Bumping version number and tagging the repository with it.
 *
 * Semantic versioning bump
 * Please read http://semver.org/
 * **************************************************
 * MAJOR ("major") version when you make incompatible API changes --
 *    major: 1.0.0
 * MINOR ("minor") version when you add functionality in a
 *    backwards-compatible manner -- minor: 0.1.0
 * PATCH ("patch") version when you make backwards-compatible bug
 *    fixes. -- patch: 0.0.2
 * PRERELEASE ("prerelease") a pre-release version --
 *    prerelease: 0.0.1-2
 * **************************************************
 *
 * You can use the commands
 *
 *     gulp patch     # makes v0.1.0 → v0.1.1
 *     gulp feature   # makes v0.1.1 → v0.2.0
 *     gulp release   # makes v0.2.1 → v1.0.0
 *     gulp prerelease # makes v0.2.1-2 → v1.0.0-2
 *
 * To bump the version numbers accordingly after you did a patch,
 * introduced a feature or made a backwards-incompatible release.
 */

function inc(importance) {
  // reget package
  var pkg = getPackageJson();
  // get existing version
  var oldVer = pkg.version;
  // increment version
  var newVer = semver.inc(oldVer, importance);
  // json filter
  var jsonFilter = filter('**/*.json');

  // Also in the common_settings.py which is read by server
  // to keep track of api version
  var settingsPy = gulp.src(['{{cookiecutter.project_slug}}/common_settings.py'])
      .pipe(replace(/(APP_VERSION\s*=\s*\")(\d+\.)+(\d+)+(-\d+)*\"/g,
                    '$1' + newVer + '"'))
      .pipe(gulp.dest('{{cookiecutter.project_slug}}/'));

  var merged = merge(configJs, settingsPy);

  // bump version in json files and git commit rest of the changed
  // files
  var all = gulp.src(['./package.json', './bower.json',
                      './{{cookiecutter.project_slug}}/common_settings.py'])
      // filter only the json files
      .pipe(jsonFilter)
      // bump the version number in the json files
      .pipe(bump({version: newVer}))
      // save json files back to filesystem
      .pipe(gulp.dest('./'))
      // restore full stream
      .pipe(jsonFilter.restore())
      // commit the changed version number
      .pipe(git.commit('bump api version to ' + newVer));
      // read only one file to get the version number
      //.pipe(filter('package.json'))
      // **tag it in the repository**
      //.pipe(tag_version());

  merged.add(all);
  return merged;
}

gulp.task('patch', function() {
  return inc('patch');
});

gulp.task('feature', function() {
  return inc('minor');
});

gulp.task('release', function() {
  return inc('major');
});

// In case of prerelease we do not want to increment the android
// release version
gulp.task('prerelease', function() {
  return inc('prerelease');
});

// run source scripts through JSHint
gulp.task('lint', function() {
  return gulp.src(source_paths.scripts)
    .pipe(jshint())
    .pipe(jshint.reporter(stylish));
});

gulp.task('install', function() {
  return bower.commands.install()
    .on('log', function(data) {
      gutil.log('bower', gutil.colors.cyan(data.id), data.message);
    });
});

gulp.task('git-check', function(done) {
  if (!which('git')) {
    console.log(
      '  ' + gutil.colors.red('Git is not installed.'),
      '\n  Git, the version control system, is required.',
      '\n  Download git here:', gutil.colors.cyan(
        'http://git-scm.com/downloads') + '.',
      '\n  Once git is installed, run \'' + gutil.colors.cyan(
        'gulp install') + '\' again.'
    );
    process.exit(1);
  }
  done();
});
