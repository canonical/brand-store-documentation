document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);

    // 1. Helper to find and replace text across all nodes (including code blocks)
    function replaceTextInNodes(node, paramName, value) {
        const marker = `__VAR_${paramName}__`;
        
        if (node.nodeType === Node.TEXT_NODE) {
            if (node.nodeValue.includes(marker)) {
                node.nodeValue = node.nodeValue.replace(new RegExp(marker, 'g'), value);
            }
        } else {
            for (let child of node.childNodes) {
                replaceTextInNodes(child, paramName, value);
            }
        }
    }

    // 2. Process every parameter found in the URL
    urlParams.forEach((value, key) => {
        const decodedValue = decodeURIComponent(value);

        // Replace in standard roles (the <span> tags)
        document.querySelectorAll(`.dynamic-param[data-param="${key}"]`).forEach(el => {
            el.innerText = decodedValue;
        });

        // Replace in code blocks and the rest of the body
        // We target 'pre' tags specifically for performance
        document.querySelectorAll('pre, code').forEach(block => {
            replaceTextInNodes(block, key, decodedValue);
        });
    });

    // 3. Pre-fill form inputs
    document.querySelectorAll('.dynamic-form input').forEach(input => {
        const val = urlParams.get(input.name);
        if (val) input.value = decodeURIComponent(val);
    });
});