const { concedeToken } = require('../database')

class User {
    constructor(username, password, name) {
        this.username = username;
        this.password = password;
        this.name = name;
    }

    checkPassword(pass) {
        return pass === this.password
    }


}

module.exports = User