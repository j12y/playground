
var express = require('express');
var router = express.Router();

router.use(express.static(__dirname + '/../assets'));
router.use(express.static(__dirname + '/../templates'));

var path = require('path');
router.get('/', function(req, res) {
    res.sendFile('layouts/app.html', {
        root: path.join(__dirname, '..'),
        });
});

module.exports = router;
