const parseCookie = str =>
  str
  .split(';')
  .map(v => v.split('='))
  .reduce((acc, v) => {
    acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
    return acc;
  }, {});

const getSession = () => {
  let { SessionNAME, SessionID, SessionUNAME } = document.cookie ? parseCookie(document.cookie) : {}
  if (!SessionID) {
    return;
  }
  return {name: SessionNAME, username: SessionUNAME, id: SessionID}
}

const clickHome = () => {
  if (getSession()) {
    window.location = '/home'
  } else {
    alert("Efetue login para acessar a página home.");
  }
}

$(document).ready(e => {
    let { SessionNAME } = document.cookie ? parseCookie(document.cookie) : {}
    $("body")[0].innerHTML = $("body")[0].innerHTML.replaceAll('${username}', SessionNAME ? SessionNAME : 'Visitante')
})