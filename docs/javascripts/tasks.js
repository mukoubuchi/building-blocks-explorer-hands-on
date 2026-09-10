/** Persist completion checkboxes for each page across instant navigation. */
document$.subscribe(function() {
    document.querySelectorAll('.task-list-item').forEach(function(item) {
        const checkbox = item.querySelector('.task-list-control input[type="checkbox"]');
        if (!checkbox) return;
        const key = 'task-' + window.location.pathname + '-' + item.textContent.trim();
        checkbox.addEventListener('change', function() {
            localStorage.setItem(key, checkbox.checked);
        });
        const savedState = localStorage.getItem(key);
        if (savedState !== null) checkbox.checked = savedState === 'true';
    });
});
