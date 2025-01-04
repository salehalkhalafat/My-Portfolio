document.addEventListener("DOMContentLoaded", function () {
    const sections = document.querySelectorAll(".section-content");

    function isInViewport(element) {
        const rect = element.getBoundingClientRect();
        return rect.top >= 0 && rect.bottom <= (window.innerHeight || document.documentElement.clientHeight);
    }

    function checkSections() {
        sections.forEach((section) => {
            if (isInViewport(section)) {
                section.classList.add("visible");
            }
        });
    }

    window.addEventListener("scroll", checkSections);
    checkSections();
});