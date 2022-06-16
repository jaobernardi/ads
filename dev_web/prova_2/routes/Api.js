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
        console.info(`Usuário ${username} autenticado.`)
        let token = user.concedeToken();
        res.cookie('Session', token, { maxAge: 900000, httpOnly: true })
        res.send({
            success: true,
            session: {
                username: username,
                token: token
            }
        });
    } else {
        res.send({success: false, error_message: 'Usuário e/ou senha não constam no banco de dados.'})
    }
})


api_router.param('token', (req, res) => {
    req.user_session = 
})


api_router.post('/session/:id', (req, res) => {
    let {username, password} = req.body;
    let user = getUser(username)
    if (user && user.checkPassword(password)) {
        console.info(`Usuário ${username} autenticado.`)
        let token = user.concedeToken();
        res.cookie('Session', token, { maxAge: 900000, httpOnly: true })
        res.send({
            success: true,
            session: {
                username: username,
                token: token
            }
        });
    } else {
        res.send({success: false, error_message: 'Usuário e/ou senha não constam no banco de dados.'})
    }
})

module.exports['api_router'] = api_router