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


html_router.get("/login", (req, res) => {
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

module.exports['html_router'] = html_router