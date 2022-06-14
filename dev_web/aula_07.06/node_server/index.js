const express = require('express');
const path = require('path')
const bodyParser = require('body-parser');
var cookieParser = require('cookie-parser')
var multer = require('multer');
var upload = multer();
const app = express();
const tokens = {};
const users = {
    "admin": "password"
}
const html_router = express.Router();
const api_router = express.Router();


function makeid(length) {
    var result           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
      result += characters.charAt(Math.floor(Math.random() * 
 charactersLength));
   }
   return result;
}

// for parsing application/json
app.use(bodyParser.json()); 

// for parsing application/xwww-
app.use(bodyParser.urlencoded({ extended: true })); 
//form-urlencoded

// for parsing multipart/form-data
app.use(upload.array()); 

// Parse user's cookies
app.use(cookieParser())


html_router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname+'/files/index.html'))
})

html_router.get('/login', (req, res) => {
    res.sendFile(path.join(__dirname+'/files/login.html'))
})

html_router.get('/pagSucesso', (req, res) => {
    let { token } = req.cookies;
    if (tokens[token]) {
        res.sendFile(path.join(__dirname+'/files/pagSucesso.html'))
    } else {
        res.sendStatus(403)
    }

})

api_router.get('/session/info', (req, res) => {
    let { token } = req.cookies ? req.cookies : req.body
    if (tokens[token]) {
        res.send({username: tokens[token]})
    } else {
        res.sendStatus(403)
    }
})

api_router.post('/login', (req, res) => {
    let {username, password} = req.body;
    if (users[username] === password) {
        let token = makeid(64);
        res.cookie('token', token, { maxAge: 900000, httpOnly: true })
        res.send({'token': token});
        tokens[token] = username;
    } else {
        res.send({'403': true})
    }
})


// Set the routers for the
app.use('/', html_router);
app.use('/api', api_router);
app.use('/static', express.static('static'))
app.listen(80)


console.log(`Server is running at localhost:80`)