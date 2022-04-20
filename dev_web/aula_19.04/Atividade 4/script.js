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
    (true) ? append_data("Condição verdadeira.") : append_data("Condição false (impossível).")
}
