let textOne = document.querySelector('.text-one')
let textTwo = document.querySelector('.text-two')
let textThree = document.querySelector('.text-three')

let oneBtn = document.querySelector('.oneBtn')
let twoBtn = document.querySelector('.twoBtn')
let threeBtn = document.querySelector('.threeBtn')


const btnOne = () => {
    textOne.style.display = "Block"
    textTwo.style.display = "none"
    textThree.style.display = "none"
    oneBtn.classList.add("active")
    twoBtn.classList.remove("active")
    threeBtn.classList.remove("active")
}

const btnTwo = () => {
    textOne.style.display = "none"
    textTwo.style.display = "Block"
    textThree.style.display = "none"
    oneBtn.classList.remove("active")
    twoBtn.classList.add("active")
    threeBtn.classList.remove("active")
}
const btnThree = () => {
    textOne.style.display = "none"
    textTwo.style.display = "none"
    textThree.style.display = "Block"
    oneBtn.classList.remove("active")
    twoBtn.classList.remove("active")
    threeBtn.classList.add("active")
}