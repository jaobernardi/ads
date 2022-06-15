const path = require('path')
const express = require('express');

const assets_router = express.static('static/assets');

module.exports['assets_router'] = assets_router