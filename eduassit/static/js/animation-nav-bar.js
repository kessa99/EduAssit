/*
DEBUT GESTION NAVBAR
pour l'apparition de la barre de navigation
*/
const humbergerToggler = document.querySelector(".humberger")
const navlinksContainer = document.querySelector(".navlinks-container");
const toggleNav = () => {
    humbergerToggler.classList.toggle("open")
    navlinksContainer.classList.toggle("open")
    const ariaToggle = humbergerToggler.getAttribute("aria-expanded") === "true" ? "false" : "true ";
    humbergerToggler.setAttribute("ariaToggler", ariaToggle)
}
humbergerToggler.addEventListener("click", toggleNav)
    /*
    cette partie servira a gerer les transition NB: celle en le faisqit en css a ete enleve pour laisser le js s'en occuper
     */
new ResizeObserver(entries => {
        if (entries[0].contentRect.width <= 900) {
            navlinksContainer.style.transition = "transform 0.3s ease-out"
        } else {
            navlinksContainer.style.transition = "none"
        }
    }).observe(document.body)
    /*FIN GESTION NAVBAR*/