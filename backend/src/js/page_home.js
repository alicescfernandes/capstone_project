document.addEventListener("DOMContentLoaded", () => {
    const tocLinks = document.querySelectorAll("#floating-toc a");
    const sections = Array.from(tocLinks).map(link =>
        document.querySelector(link.getAttribute("href"))
    );

    const observerOptions = {
        root: null,
        rootMargin: "10px",
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            const id = entry.target.id;
            const link = document.querySelector(`#floating-toc a[href="#${id}"]`);
            if (entry.isIntersecting) {
                tocLinks.forEach(l => l.classList.remove("active"));
                if (link) link.classList.add("active");
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        if (section) observer.observe(section);
    });
});