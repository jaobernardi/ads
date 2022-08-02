function get_data() {
    const params = new URLSearchParams(window.location.search);
    if (!params.has("birthday")) {
        return;
    }
    return params;
}

function show_form_data(data) {
    if (data) {
        return_showback = document.getElementById("showback");
        return_showback.innerHTML = `<h1>Olá ${data.get('name')}!</h1>`;
    }
}

show_form_data(get_data())