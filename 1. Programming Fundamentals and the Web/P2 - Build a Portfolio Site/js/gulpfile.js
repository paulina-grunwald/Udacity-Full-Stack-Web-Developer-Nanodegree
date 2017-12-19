//this scrit will minify javascript file and after 
//that it will also rename the file
///require is like import and will import gulp
var gulp =  require('gulp')
	//uglify module
	uglify = require('gulp-uglify')
	//rename module
	rename = require('gulp-rename')
	minifyCSS = require('gulp-minify-css')

///create new tasks in gulp named scripts
gulp.task('scripts', function(){
	//specify src (source file)
	//look in js folder for all the files that are .js
	//if you want to look in any subdirectory you can use 'js/**/*.js'
	//pipe links two element in input(source) to output(pipe) way
	gulp.src('js/*.js')
		//if you have more than one js file you need to use concat module
		//so both of them will be uglify and renamed
		.pipe(concat())
		.pipe(uglify())
		.pipe(rename('app.min.js'))
		.pipe(gulp.dest('js/'));
	});

gulp.task('styles', function(){
	gulp.src('css/*.css')
		.pipe(minifyCSS())
		.pipe(gulp.dest('minCSS'));

});

//watch function that will detect changes in js and css files
gulp.task('watch', function(){
	gulp.watch('js/*.js', ['scripts']);
	gulp.watch('css/*.css', ['styles']);

});

gulp.task('deafult', ['script', 'styles']);
