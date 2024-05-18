// MainButton
// .isVisible
// .hide()
// .show()
// rg.MainButton.

let tg = window.Telegram.webApp;
tg.expand();

let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");


btn5.addEventListener('click', function(){
    if(tg.MainButton.isVisble){
        tg.mainButton.hide();
    }
    else{
        tg.MainButton.setText("Вы вывбрали товар 5!")
        item = "5";
        tg.MainButton.show();
    }
})

btn6.addEventListener('click', function(){
    if(tg.MainButton.isVisible){
        item = '6';
        tg.mainButton.show();
    }
});




Telegram.WebApp.onEvent("mainButtonCLicked", function(){
    tg.sendData(item); 
})

let usercard = document.getElementById("usercard");

let p = document.createElement("p");

p.innerText = `${tg.initDataUnsafe.first_name}
${th.initDataUnsafe.last_name}`;

usercard.appendChild(p);