function bhaskara(a, b, c) {
    let delta = (b*b)-4*a*c;
    let root_1 = ((b*-1)-Math.sqrt(delta))/(2*a);
    let root_2 = ((b*-1)+Math.sqrt(delta))/(2*a);
    return [root_1, root_2]
}


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
    let bhask = bhaskara(2, 12, -14)
    append_data(`Raizes para a equação 2x - 12x² - 14: ${bhask.join(', ')}`)
}

