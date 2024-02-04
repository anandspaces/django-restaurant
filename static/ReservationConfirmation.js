function generateRandomIntRID() {
    function getRandomInt(min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min;
    }

    const randomNum = getRandomInt(100000000, 999999999);

    document.getElementById("RID").textContent = randomNum;
}

document.addEventListener('DOMContentLoaded',()=>{
    generateRandomIntRID();
})

const goBackHome = document.getElementById("goBackHomeButton");
goBackHome.addEventListener('click',()=>{
    window.location.href = "restaurantweb";
});