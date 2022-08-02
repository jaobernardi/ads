const express = require('express');
const app = express();
const bodyParser = require('body-parser');
var cookieParser = require('cookie-parser')
var multer = require('multer');
var upload = multer();


// for parsing application/json
app.use(bodyParser.json()); 

// for parsing application/xwww-
app.use(bodyParser.urlencoded({ extended: true })); 
//form-urlencoded

// for parsing multipart/form-data
app.use(upload.array()); 

// Parse user's cookies
app.use(cookieParser())


const { html_router, assets_router, api_router } = require('./routes');

app.use('/', html_router)
app.use('/assets', assets_router)
app.use('/api', api_router)

app.listen(3000, '0.0.0.0')