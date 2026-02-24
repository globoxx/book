const toggleBtn = document.getElementById("menu-toggle");
const sideMenu = document.getElementById("side-menu");
const overlay = document.getElementById("menu-overlay");
toggleBtn.addEventListener("click", () => {
    const isOpen = sideMenu.classList.toggle("open");
        overlay.classList.toggle("show");
        toggleBtn.textContent = isOpen ? "✖" : "☰";
    });
    overlay.addEventListener("click", () => {
        sideMenu.classList.remove("open");
        overlay.classList.remove("show");
        toggleBtn.textContent = "☰";
    });
    const links = document.querySelectorAll("#side-menu a");
    const currentPage = location.pathname.split("/").pop();
    links.forEach(link => {
        if (link.getAttribute("href") === currentPage) {
        link.classList.add("active");
        }
    });