
function enviarForm() {
    form_data = JSON.stringify({
        "nickname" : document.getElementById("nickname").value,
        "passkey" : document.getElementById("passkey").value,
    })

    try {
        //remplazar url con el host que se esté usando actualmente
        //IMPORTANTE, USAR HTTPS
        fetch("https://lcs1423.pythonanywhere.com/login_usuario", {
            method : "POST",
            body : form_data,
            headers : {"Content-type" : "application/json"}
        })
    } catch(error) {
        alert(error)
    }
}