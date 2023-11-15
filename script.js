document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contactForm');
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        // You can add additional validation here if needed

        // Submit the form using Formspree
        const url = 'https://formspree.io/k.gandhi@reply.com';
        const formData = new FormData(this);

        fetch(url, {
            method: 'POST',
            body: formData,
            headers: {
                Accept: 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            alert('Thank you for your submission!');
            form.reset();
        })
        .catch(error => {
            alert('Error submitting the form. Please try again later.');
        });
    });
});
