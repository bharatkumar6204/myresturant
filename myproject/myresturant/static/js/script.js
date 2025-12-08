function toggleMenu(){
        document.getElementById("menuList").classList.toggle("show");
    }

    console.log("Restaurant Website Loaded Successfully!");


    let buttons = document.querySelectorAll(".filter-btn");
let items = document.querySelectorAll(".menu-card");

buttons.forEach(btn => {
    btn.addEventListener("click", () => {

        // Active Button Style
        buttons.forEach(b => b.classList.remove("active"));
        btn.classList.add("active");

        let category = btn.getAttribute("data-category");

        items.forEach(item => {
            if (category === "all" || item.getAttribute("data-category") === category) {
                item.style.display = "block";
            } else {
                item.style.display = "none";
            }
        });

    });
});

// Smooth Scroll for buttons
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth",
        });
    });
});

// Book table form submit message
/*
document.querySelector(".book-form").addEventListener("submit", function (e) {
    e.preventDefault();

    alert("🎉 Your table has been booked successfully!\nWe are waiting to serve you ❤️");
});
*/

// Newsletter submit message
/*
document.querySelector(".newsletter-form").addEventListener("submit", function (e) {
    e.preventDefault();
    alert("🎉 Thank you for subscribing to our newsletter!");
});
*/


