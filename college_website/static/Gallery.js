function get_image() {
    var con = document.querySelectorAll(".ri-image-fill");
    var pic_container = document.querySelector(".col22");
    con.forEach(function (item) {
        item.addEventListener("click", function (event) {
            var imgaddress = event.target.getAttribute("data-");
            pic_container.style.backgroundImage = "url(" + imgaddress + ")";
        });
    });
}
get_image();

