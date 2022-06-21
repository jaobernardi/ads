const path = require('path')
const express = require('express');
const html_router = express.Router();
const { getUserFromToken } = require('../database/')

html_router.get("/", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'index.html'
    )))
})

html_router.get("/index", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'index.html'
    )))

})
html_router.get("/index.html", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'index.html'
    )))

})

html_router.get("/home", (req, res) => {
    let { SessionID } = req.cookies
    if (SessionID && getUserFromToken(SessionID)) {
        res.sendFile(path.resolve(path.join(
            'static',
            'home.html'
        )))
    } else {
        res.redirect('/login')
    }

})

html_router.get("/home.html", (req, res) => {
    let { SessionID } = req.cookies
    if (SessionID && getUserFromToken(SessionID)) {
        res.sendFile(path.resolve(path.join(
            'static',
            'home.html'
        )))
    } else {
        res.redirect('/login')
    }

})


html_router.get("/login", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'login.html'
    )))
})

html_router.get("/login.html", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'login.html'
    )))
})

html_router.get("/auto-cadastro", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'auto-cadastro.html'
    )))
})

html_router.get("/auto-cadastro.html", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'auto-cadastro.html'
    )))
})

module.exports['html_router'] = html_router