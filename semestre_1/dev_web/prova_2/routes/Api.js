const path = require('path')
const express = require('express');
const { getUser, concedeToken } = require('../database/')
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
        let token = concedeToken(user.username);
        res.cookie('SessionID', token, { maxAge: 900000 })
        res.cookie('SessionNAME', user.name, { maxAge: 900000 })
        res.cookie('SessionUNAME', username, { maxAge: 900000 })
        res.send({
            success: true,
            session: {
                username: username,
                token: token,
                name: user.name
            }
        });
    } else {
        res.send({success: false, error_message: 'Usuário e/ou senha não constam no banco de dados.'})
    }
})


api_router.param('token', (req, res) => {
    req.user_session = ''
})


module.exports['api_router'] = api_router