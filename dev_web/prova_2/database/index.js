/* Considerando que, em momento algum, exigiu-se a implementação de databases 
*  junto com node na disciplina, não utilizarei SQL. 
*/
const { User } = require('../structures')
const _data = {
    users: {'admin': 'password'},
    tokens: {'username': 'token'}
}

module.exports["getUser"] = (username) => {
    return _data.users[username] ? new User(username, _data.users[username]) : undefined
};

module.exports["getUserFromToken"] = (token) => {
    return _data.tokens[token] ? new User(_data.tokens[token], _data.users[_data.tokens[token]]) : undefined
}

module.exports["concedeToken"] = (username) => {
    var token           = '';
    var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for ( var i = 0; i < length; i++ ) {
        token += characters.charAt(Math.floor(
        Math.random() * 
        charactersLength
        ));
    }
    _data.tokens[token] = username;
    return token;
}