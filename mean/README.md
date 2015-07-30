
=== Python ===

## Virtualenv

mkproject playground
workon playground

=== NODE.JS ===

## Node.js Setup ##
brew install npm
npm install -g n
n stable

=== MONGODB ===

## Installation ##
brew install mongodb
brew info mongodb
    ln -sfv /usr/local/opt/mongodb/*.plist ~/Library/LaunchAgents
    Then to load mongodb now:
        launchctl load ~/Library/LaunchAgents/homebrew.mxcl.mongodb.plist
    Or, if you don't want/need launchctl, you can just run:
        mongod --config /usr/local/etc/mongod.conf

## Basics ##

    > use playground
    > db.users.insert({...})
    > db.users.find()
    > db.users.find({...})

=== Gulp ===

npm install --global gulp
npm install --save gulp

$ gulp hello

npm install --save gulp-concat

Other plugins to investigate:
* gulp-jshint - linter over js for coding standards
* gulp-rev - appends hash of contents to filename for aggressive caching
* gulp-autoprefixer - add vendor prefixes to css automatically
* gulp-rimraf - clean out directories for fresh build
* gulp-imagemin - compress images
* gulp-livereload -- refresh browser when css/js changes

=== Stylus ===

Like Sass, Less -- a CSS preprocessor
that runs with node.js instead of ruby etc.

npm install --save gulp-stylus

http://learnboost.github.io/stylus/

=== Social App ===

## Developing App ##

npm install --save express
npm install --save mongoose

## Development Tool ##
Detect changes and reload server:
npm install --global nodemon
nodemon server.js

Also available with gulp

npm install --save gulp-nodemon

## Testing Tool ##
curl -v -H "Content-Type: application/json" -XPOST --data '{"username":"dickeyxxx"}' localhost:3000/api/posts

or Postman for Chrome

## Connecting to DB ##

mongo social
db.posts.find()

## Minimizing / Uglifier ##

Could also look into Browserify -- alternative to gulp concatenating

npm install --save gulp-uglify

angular not very uglify compatible because of $http and $scope so
gulp-ng-annotate can fix it
npm install --save gulp-ng-annotate

minified version difficult for debugging without source map
npm install --save gulp-sourcemaps

## Authentication ##

npm install --save jwt-simple

JWT -- JSON Web Token is used to sign, not encrypt

npm install --save lodash

npm install --save bcrypt
$ node
> require('bcrypt').hashSync('pass', 10)



