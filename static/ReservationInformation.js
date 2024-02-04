const nameSpan = document.getElementById('name_');
const date_timeSpan = document.getElementById('date_time_');
const emailSpan = document.getElementById('email_');
const phoneNoSpan = document.getElementById('phoneNo_');
const noOfDinersSpan = document.getElementById('noOfDiners_');

const dateOfArrival = sessionStorage.getItem('dateOfArrival');
const timeOfArrival = sessionStorage.getItem('timeOfArrival');
const firstName = sessionStorage.getItem('firstName');
const lastName = sessionStorage.getItem('lastName');
const emailID = sessionStorage.getItem('emailID');
const phoneNo = sessionStorage.getItem('phoneNo');
const noOfDiners = sessionStorage.getItem('noOfDiners');

nameSpan.textContent = `${firstName} ${lastName}`;
date_timeSpan.textContent = `${dateOfArrival} ${timeOfArrival}`;
emailSpan.textContent = emailID;
phoneNoSpan.textContent = phoneNo;
noOfDinersSpan.textContent = noOfDiners;

function generateRandomInt() {
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    document.getElementById("tableNo_").textContent = getRandomInt(100, 999);
}

document.addEventListener('DOMContentLoaded', () => {
    generateRandomInt();
});

const inform = document.getElementById("informButton");
inform.addEventListener('click',()=>{
    window.location.href = "confirmation"
})

const informBack = document.getElementById("informBackButton");
informBack.addEventListener('click',()=>{
    window.location.href = "restaurantweb";
})
