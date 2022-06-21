const parseCookie = str =>
  str
  .split(';')
  .map(v => v.split('='))
  .reduce((acc, v) => {
    acc[decodeURIComponent(v[0].trim())] = decodeURIComponent(v[1].trim());
    return acc;
  }, {});

$(document).ready(e => {
    let { SessionNAME } = document.cookie ? parseCookie(document.cookie) : {}
    $("body")[0].innerHTML = $("body")[0].innerHTML.replaceAll('${username}', SessionNAME ? SessionNAME : 'Visitante')
})