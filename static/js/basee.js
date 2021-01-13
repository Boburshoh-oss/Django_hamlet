var x = document.getElementById("indexx");
var y = document.getElementById("agents");
var z = document.getElementById("blog");
var k = document.getElementById("properties");
var u = document.getElementById("about");
var i = document.getElementById("contact");
function myFunction() {
    x.classList.add("active");
    z.classList.remove("active");
    k.classList.remove("active");
    y.classList.remove("active"); 
    u.classList.remove("active");  
    i.classList.remove("active");         
}
function youFunction() {
    x.classList.remove("active");
    z.classList.add("active");
    k.classList.remove("active");
    y.classList.remove("active");  
    u.classList.remove("active");  
    i.classList.remove("active");      
}
function weFunction() {
    x.classList.remove("active");
    z.classList.remove("active");
    k.classList.add("active");
    y.classList.remove("active");
    u.classList.remove("active");  
    i.classList.remove("active");     
}
function areFunction() {
    x.classList.remove("active");
    z.classList.remove("active");
    k.classList.remove("active");
    y.classList.add("active");  
    u.classList.remove("active");  
    i.classList.remove("active");       
}
function isFunction() {
    x.classList.remove("active");
    z.classList.remove("active");
    k.classList.remove("active");
    y.classList.remove("active");  
    u.classList.add("active");  
    i.classList.remove("active");       
}
function amFunction() {
    x.classList.remove("active");
    z.classList.remove("active");
    k.classList.remove("active");
    y.classList.remove("active");  
    u.classList.remove("active");  
    i.classList.add("active");       
}