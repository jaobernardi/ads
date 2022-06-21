const processData = (data, callback) => {
    if (!data.success) {
        callback(false, data.error_message)
        return;
    }
    callback(true, data.session)
}

const queryDatabase = (username, password, callback) => {
    $.post('/api/login', {username: username, password: password})
    .done((data) => {
        processData(data, callback);
    })
}

$(document).ready(e => {
    let toastElList = document.querySelectorAll('.toast')
    let toastList = [...toastElList].map(toastEl => new bootstrap.Toast(toastEl, {}))
    $("#login_form").submit(e => {
        e.preventDefault();
        let username = $("#username").val();
        let password = $("#password").val();
        queryDatabase(username, password, (status, data) => {
            if (!status) {
                toastElList.forEach(e => e.innerText = data);
                toastList.forEach(e => e.show())
            } else {
                window.location = '..'
            }
        })
        e.preventDefault();
        
    })
})