const express = require('express');
const router = express.Router();

const test = ""


/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Hello Git!' });
});

module.exports = router;