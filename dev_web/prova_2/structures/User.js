class User {
    constructor(username, password) {
        this.username = username;
        this.password = password;
    }

    checkPassword(pass) {
        return pass === this.password
    }

}