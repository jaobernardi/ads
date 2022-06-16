const { concedeToken } = require('../database')

class User {
    constructor(username, password) {
        this.username = username;
        this.password = password;
    }

    checkPassword(pass) {
        return pass === this.password
    }

    concedeToken() {
        return concedeToken(this.username);
    }

}

module.exports = User