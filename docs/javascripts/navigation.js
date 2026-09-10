/** Keep page controls working after Material's instant navigation updates. */
(function() {
    const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    const tabs = document.querySelector('.md-tabs');

    function updateBackToTop() {
        const button = document.querySelector('.md-top');
        if (button) button.hidden = window.scrollY <= 300;
    }

    function centerActiveTab() {
        const active = document.querySelector('.md-tabs__item--active');
        if (!active || !tabs || window.innerWidth > 1220) return;
        const box = tabs.getBoundingClientRect();
        const item = active.getBoundingClientRect();
        tabs.scrollTo({
            left: tabs.scrollLeft + item.left - box.left - (box.width - item.width) / 2,
            behavior: reducedMotion.matches ? 'instant' : 'smooth'
        });
    }

    window.addEventListener('scroll', updateBackToTop, { passive: true });
    window.addEventListener('resize', centerActiveTab, { passive: true });
    document$.subscribe(() => {
        updateBackToTop();
        // The selector updates the active item synchronously in this emission.
        requestAnimationFrame(centerActiveTab);
    });
})();
