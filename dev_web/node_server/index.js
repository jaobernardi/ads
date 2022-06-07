const express = require('express');
const path = require('path')
const app = express();
const router = express.Router();


router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname+'/files/index.html'))
})


app.use('/', router);
app.listen(80)

console.log(`Server is running at localhost:80`)