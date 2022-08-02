function create_element(text) {
    let child = document.createElement("p");
    child.innerHTML = text;
    return child;
}

function append_data(data_text) {
    let child = create_element(data_text);
    document.getElementById("data").appendChild(child)
}

function demo() {
    let now = new Date();
    let hour = now.getHours();
    if (hour <= 12) {
        append_data(`Bom dia! Agora são ${hour} horas`)
    } else if (hour > 12 && hour < 20) {
        append_data(`Boa tarde! Agora são ${hour} horas`)
    } else {
        append_data(`Boa noite! Agora são ${hour} horas`)
    }
}
