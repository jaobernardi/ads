/* Considerando que, em momento algum, exigiu-se a implementação de databases 
*  junto com node na disciplina, não utilizarei SQL. 
*/
const { User } = require('../structures/User')
const _data = {
    users: {'admin': 'password'},
    tokens: {'username': 'token'}
}

module.exports["getUser"] = (username) => {
    return _data.users[username] ? User(username, _data.users[username]) : undefined
};

module.exports["getUserFromToken"] = (token) => {
    return _data.tokens[token] ? User(_data.tokens[token], _data.users[_data.tokens[token]]) : undefined
}

module.exports["concedeToken"] = (username) => {
    
    return _data.tokens[token] ? User(_data.tokens[token], _data.users[_data.tokens[token]]) : undefined
}