
var express = require('express');
var router = express.Router();

router.use(express.static(__dirname + '/../assets'));

var path = require('path');
router.get('/', function(req, res) {
    res.sendFile('layouts/posts.html', {
        root: path.join(__dirname, '..'),
        });
});

module.exports = router;
