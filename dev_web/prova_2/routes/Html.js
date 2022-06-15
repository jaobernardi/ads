const path = require('path')
const express = require('express');
const html_router = express.Router();

html_router.get("/", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'home.html'
    )))
})


html_router.get("/login", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'login.html'
    )))
})


html_router.get("/cadastro", (req, res) => {
    res.sendFile(path.resolve(path.join(
        'static',
        'cadastro.html'
    )))
})

module.exports['html_router'] = html_router