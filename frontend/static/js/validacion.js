function validarFormularioSumate() {
    //Obtener los valores
    var nombre = document.getElementById("nombre").value.trim()
    var apellido = document.getElementById("apellido").value.trim()
    var mail = document.getElementById("mail").value.trim()
    var nac = document.getElementById("nac").value.trim()

    //Verificar si hay campos vacios
    if(nombre==="" || apellido==="" || mail==="" || nac===""){
        alert("Complete todos los campos del formulario.")
        return false
    }

    // Verificar si el nombre contiene solo caracteres alfabéticos (incluidos tildes del español) o espacios
    var nombreTest = /^[a-zA-ZÁÉÍÓÚáéíóúñ ]+$/.test(nombre);
    if(nombreTest===false){
      alert("ingrese un nombre válido con las letras del abecedario.")
      return false
    }

    // Verificar si el apellido contiene solo caracteres alfabéticos (incluidos tildes del español) o espacios
    var apellidoTest = /^[a-zA-ZÁÉÍÓÚáéíóúñ ]+$/.test(apellido);
    if(apellidoTest===false){
      alert("ingrese un apellido válido con las letras del abecedario.")
      return false
    }

    //Verificar si tiene al menos 18 años
    const currentDate = new Date()
    const birthdate =  new Date(nac)
    const age = currentDate.getFullYear() - birthdate.getFullYear()
    if (age < 18){
        alert("Debe ser mayor de edad para unirse.") /*si tiene 17 y fraccion, puede fallar*/
        return false
    }

    //Si supera las validaciones
    alert("Formulario enviado con éxito! Revise su correo para obtener la contraseña.")
    return true
}

/* //Aun no sabemos como enviar una contraseña al mail del usuario :c
function validarFormularioContraseña() {
    //Obtener los valores
    var codigoIngresado = document.getElementById("codigo").value.trim()

    //Verificar si la contraseña es correcta
    if(codigoIngresado===codigoEnviado){
        alert("Se ha registrado con éxito!")        
        return true
    }

    return false
}
*/

function validarFormularioContacto() {
    //Obtener los valores
    var mail_contacto = document.getElementById("mail_contacto").value.trim()
    var comentario = document.getElementById("comentario").value.trim()

    //Verificar si hay campos vacios
    if(mail_contacto==="" || comentario===""){
        alert("Complete todos los campos del formulario.")
        return false
    }

    //Si supera las validaciones
    alert("Consulta enviada con éxito!")
    return true
}