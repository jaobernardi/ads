const path = require('path')
const express = require('express');
const { getUser } = require('../database/')
const api_router = express.Router();

api_router.get('/status', (req, res) => {
    res.send({
        'status': 200
    })
})

api_router.post('/login', (req, res) => {
    let {username, password} = req.body;
    let user = getUser(username)
    if (user && user.checkPassword(password)) {
        let token = makeid(64);
        res.cookie('token', token, { maxAge: 900000, httpOnly: true })
        res.send({'token': token});
        tokens[token] = username;
    } else {
        res.send({'403': true})
    }
})

module.exports['api_router'] = api_router