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


    const searchInput = document.getElementById('sectionSearch');
    const sectionContainers = document.querySelectorAll('.section-container');

    function highlightText(text, searchTerm) {
        if (!searchTerm) return text;
        const regex = new RegExp(searchTerm, 'gi');
        return text.replace(regex, match => `<span class="bg-yellow-200">${match}</span>`);
    }

    function resetHighlights(element) {
        const originalText = element.getAttribute('data-original-text') || element.textContent;
        element.innerHTML = originalText;
    }

    //
    searchInput.addEventListener('input', function(e) {
        const searchTerm = e.target.value.toLowerCase();

        sectionContainers.forEach(container => {
            const sectionLink = container.querySelector('.section-item a');
            const chartItems = container.querySelectorAll('.chart-item');
            let hasMatch = false;

            // Store original text if not already stored
            if (!sectionLink.getAttribute('data-original-text')) {
                sectionLink.setAttribute('data-original-text', sectionLink.textContent);
            }
            chartItems.forEach(chart => {
                if (!chart.getAttribute('data-original-text')) {
                    chart.setAttribute('data-original-text', chart.textContent);
                }
            });

            // Check if section title matches
            const sectionTitle = sectionLink.textContent.toLowerCase();
            if (sectionTitle.includes(searchTerm)) {
                hasMatch = true;
                sectionLink.innerHTML = highlightText(sectionLink.getAttribute('data-original-text'), searchTerm);
            } else {
                resetHighlights(sectionLink);
            }

            // Check if any chart titles match
            chartItems.forEach(chart => {
                const chartTitle = chart.textContent.toLowerCase();
                if (chartTitle.includes(searchTerm)) {
                    hasMatch = true;
                    chart.innerHTML = highlightText(chart.getAttribute('data-original-text'), searchTerm);
                } else {
                    resetHighlights(chart);
                }
            });

            // Show/hide section based on matches
            if (hasMatch) {
                container.style.display = '';
                // If there's a search term, expand sections with matches
                if (searchTerm) {
                    const subSections = container.querySelector('.sub-sections');
                    if (subSections) {
                        subSections.classList.remove('hidden');
                    }
                }
            } else {
                container.style.display = 'none';
            }
        });
    });
});


