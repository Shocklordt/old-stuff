function validation(form) {
    event.preventDefault()
    if (form.full_name.value === "") {
        alert("Name can not be empty!")
        form.full_name.focus()
        return false;
    }
    if (form.password1.value !== "" && form.password1.value === form.password2.value) {
        if (!checkPassword(form.password1.value)) {
            alert("The password you have entered is not valid!");
            return false;
        }
    } else {
        alert("Error: Please check that you have entered and confirmed your password.")
        return false;
    }
    return send();
}

function checkPassword(str) {
    var re = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
    return re.test(str)
}

function send() {
    event.preventDefault()
    let name = document.getElementById("full_name").value
    let password1 = document.getElementById("password1").value
    let password2 = document.getElementById("password2").value
    let birthdate = document.getElementById("birthdate").value
    let height = document.getElementById("number").value;
    let color = document.getElementById("favorite_color").value
    let country = document.getElementById("country")
    let profession = document.getElementById("myProfession").value
    let message = document.getElementById("message").value

    name_send(name)
    password_send(password1, password2)
    hobbies_send()
    date_send(birthdate)
    gender_send()
    height_send(height)
    color_send(color)
    country_send(country)
    pro_send(profession)
    msg_send(message)
}

function name_send(name) {
    if (name.length === 0) {
        alert("Name empty!")
    } else if (name && name) {
        console.log(`Full Name: ${name}`);
        document.getElementById("output_name").innerHTML = "Name: " + name
    }
}

function password_send(password1, password2) {
    /* Password processing */
    if (password1 === password2) {
        console.log(`Password1: ${password1}`);
        console.log(`Password2: ${password1}`);
        document.getElementById("output_pass1").innerHTML = "Password1: " + password1
        document.getElementById("output_pass2").innerHTML = "Password2: " + password2

    } else {
        alert("Invalid password")
    }

}

function hobbies_send() {
    let hobbies = ["sports", "games", "TV", "music"];
    let myHobbies = [];
    /* Hobbies processing */
    for (let choice of document.getElementsByName("hobbies")) {
        if (choice.checked && hobbies.findIndex((x) => x === choice.value) !== -1) {
            myHobbies.push(choice.value);
        }
    }
    if (myHobbies.length) {
        console.log(`Your hobbies are: ${myHobbies.join(", ")}`);
        document.getElementById("output_hobbies").innerHTML = `Hobbies: ${myHobbies.join(", ")}`
    } else {
        console.log("You have no hobbies");
    }

}

function date_send(birthdate) {
    if (birthdate.length == 0) {

    } else if (birthdate) {
        document.getElementById("output_date").innerHTML = "Date of Birth: " + birthdate
    }
}

function gender_send() {
    /* Gender radio button processing */
    gender = document.getElementsByName("gender")
    let genders = ["male", "female", "other"]
    let myGender = []

    for (let choice1 of gender) {
        if (choice1.checked && genders.findIndex((x) => x == choice1.value) != -1) {
            myGender.push(choice1.value)
        }
    }
    if (myGender.length) {
        console.log(`Your gender is : ${myGender.join(", ")}`);
        document.getElementById("output_date").innerHTML = `Gender: ${myGender.join(", ")}`
    } else {
        alert("Gender is not selected!")
    }
}

function height_send(height) {
    /* Height processing */
    if (height.length === 0) {

    } else if (height) {
        console.log("Height is: " + height)
        document.getElementById("output_height").innerHTML = "Height: " + height
    }
}

function color_send(color) {
    /* Color processing */
    if (color.length === 0) {

    } else if (color) {
        document.getElementById("output_color").innerHTML = "Favorite color: " + color
    }
}

function country_send(country) {
    /* Country processing */
    if (country.length === 0) {

    } else if (country) {
        let sCountry = document.getElementById("country")
        document.getElementById("output_country").innerHTML = "Country: " + sCountry[sCountry.selectedIndex].text
    }
}

function pro_send(profession) {
    /* Profession processing */
    if (profession.length === 0) {

    } else if (profession) {
        document.getElementById("output_prof").innerHTML = "profession: " + profession

    }
}

function msg_send(message) {
    /* Message processing */
    if (message.length === 0) {
        alert("No message entered!")
    } else if (message) {
        document.getElementById("output_msg").innerHTML = "Message: " + message
    }
}