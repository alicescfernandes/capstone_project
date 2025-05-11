document.addEventListener("DOMContentLoaded", () => {

    // Scroll to top functionality
    const scrollBtn = document.getElementById('scrollToTopBtn');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 500) {
            scrollBtn.classList.remove('hidden');
        } else {
            scrollBtn.classList.add('hidden');
        }
    });
    document.querySelectorAll('[data-toggle]').forEach(button => {
        const targetId = button.getAttribute('data-toggle');
        const target = document.querySelector(`[data-section-id="${targetId}"]`);

        button.addEventListener('click', () => {
            const isHidden = target.classList.toggle('hidden');
            button.textContent = isHidden ? '+' : '-';
        });
    });
});


