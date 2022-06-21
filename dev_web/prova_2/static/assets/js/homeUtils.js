$(document).ready(e => {
    window.cookieStore.get('SessionNAME')
    .then(cookie => {
        $("body")[0].innerHTML = $("body")[0].innerHTML.replaceAll('${username}', cookie ? cookie.value : 'Visitante')
    })
    
})