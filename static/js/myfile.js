function change() {
    const heads = document.getElementById("head");
    heads.style.color = "#061020";
    const elms1=document.getElementById("int1");
    const elms2=document.getElementById("int2");
    elms1.style.border="3px solid #061020";
    elms2.style.border="3px solid #061020";
    const but = document.getElementById("btn");
    but.style.backgroundColor = "#061020";
    but.style.color = "white";
}

function noChange() {
    const heads = document.getElementById("head");
    heads.style.color = "white";
    const but = document.getElementById("btn");
    but.style.backgroundColor = "white";
    but.style.color = "#061020";
}