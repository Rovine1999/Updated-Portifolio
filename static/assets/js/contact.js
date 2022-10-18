const form_ = document.getElementById('php-email-form')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');


const sendMessage = () => {

    const url = form_.getAttribute('action');

    const form = {
        subject: document.getElementById('subject').value,
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        message: document.getElementById('email').value
    }
    fetch(url,{
        method: 'POST',
        headers: {
           'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({form: form})
    })
    .then(response => {
        response.json().then(resolved => {
            form_.querySelector('.sent-message').classList.add('d-block');
            form_.reset();
        })
    })
    .catch(error => {

    })


}

form_.addEventListener('submit', (e) => {
    e.preventDefault();
    sendMessage();
})