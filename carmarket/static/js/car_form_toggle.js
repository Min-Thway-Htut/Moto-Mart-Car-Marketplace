 console.log("car_form_toggle.js loaded");
 
 document.addEventListener("DOMContentLoaded", function () {
            const darkModeToggle = document.getElementById("darkModeToggle");
            const currentMode = localStorage.getItem("theme");
        
            if (currentMode === "dark") {
              document.body.classList.remove("light-mode");
              document.body.classList.add("dark-mode");
              darkModeToggle.checked = true;
            }
        
            darkModeToggle.addEventListener("change", function () {
              if (this.checked) {
                document.body.classList.remove("light-mode");
                document.body.classList.add("dark-mode");
                localStorage.setItem("theme", "dark");
              } else {
                document.body.classList.remove("dark-mode");
                document.body.classList.add("light-mode");
                localStorage.setItem("theme", "light");
              }
            });
          });