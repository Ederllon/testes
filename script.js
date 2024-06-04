
const jokeElement = document.getElementById('joke');
const getJokeBtn = document.getElementById('getJokeBtn');

getJokeBtn.addEventListener('click', getJoke);

function getJoke() {
    fetch('https://api.chucknorris.io/jokes/random')
    .then(response => response.json())
    .then(data => {
        jokeElement.textContent = data.value;
    })
    .catch(error => {
        console.error('Error fetching joke:', error);
    });
}
