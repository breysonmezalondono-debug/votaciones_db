document.addEventListener("DOMContentLoaded", function(){

const form = document.querySelector("form");
const input = document.querySelector("input[name='numero']");

if(form){

form.addEventListener("submit", function(e){

let cedula = input.value.trim();

if(cedula === ""){

alert("Ingrese su número de identificación");
e.preventDefault();
return;

}

if(isNaN(cedula)){

alert("La identificación solo debe contener números");
e.preventDefault();
return;

}

if(cedula.length < 6){

alert("Número de identificación inválido");
e.preventDefault();
return;

}

let boton = document.querySelector("button");

boton.innerHTML = "Consultando...";
boton.style.background = "#777";

});

}

});