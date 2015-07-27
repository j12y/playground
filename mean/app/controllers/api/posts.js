
var router = require('express').Router();
var Post = require('../../models/post');

router.get('/', function(req, res, next) {
    Post.find()
        .sort('-date')
        .exec(function(err, posts) {
            if (err) { return next(err); }
            res.json(posts);
        });
});

router.post('/', function(req, res, next) {
    console.log('username', req.body.username);
    console.log('body', req.body.body);
    var post = new Post({
        username: req.body.username,
        body: req.body.body,
    });
    post.save(function(err, post) {
        if (err) { return next(err); }
        res.status(201).send(post);
    });
});

module.exports = router;
