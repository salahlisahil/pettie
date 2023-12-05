let animals = document.querySelector(".animals")
let doctors = document.querySelector(".doctors")

let btnAnimals = document.querySelector(".btn-animals")
let btnDoctors = document.querySelector(".btn-doctor")


const animalsFunc = () => {
    animals.style.display = "grid"
    doctors.style.display = "none"
    btnAnimals.classList.add('active')
    btnDoctors.classList.remove('active')
}

const doctorsFunc = () => {
    animals.style.display = "none"
    doctors.style.display = "grid"
    btnAnimals.classList.remove('active')
    btnDoctors.classList.add('active')
}