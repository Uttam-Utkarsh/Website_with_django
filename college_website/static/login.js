function hamburger() {
    
    var profileisopen = false;
    var page1 = document.querySelector(".page1");
    var profile = document.querySelector(".profile1");
    var box = document.querySelector(".hamburger-menu");

    profile.addEventListener("click", () => {
        if (profileisopen == false) {
            console.log("hellp");
            box.style.left = "78vw";
            box.style.display = "block";
            page1.style.transform = "ease-in-out";
            profileisopen = true;
        } else {
            box.style.left = "100vw";
            box.style.display = "none";
            profileisopen = false;
        }
    });
}

function signuppage() {
    const loginText = document.querySelector(".title-text .login");
    const loginForm = document.querySelector("form.login");
    const loginBtn = document.querySelector("label.login");
    const signupBtn = document.querySelector("label.signup");
    const signupLink = document.querySelector("form .signup-link a");
    signupBtn.onclick = () => {
        loginForm.style.marginLeft = "-50%";
        loginText.style.marginLeft = "-50%";
    };
    loginBtn.onclick = () => {
        loginForm.style.marginLeft = "0%";
        loginText.style.marginLeft = "0%";
    };
    signupLink.onclick = () => {
        signupBtn.click();
        return false;
    };
}

hamburger();
signuppage();
