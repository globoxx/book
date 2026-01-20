document.querySelector('.cta-button').addEventListener('click', () => {
    document.querySelector('.milestones').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.mil-1').addEventListener('click', (e) => {
    e.preventDefault(); 
    document.querySelector('.milestones').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.logo img').addEventListener('click', () => {
    document.querySelector('.hero').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.car').addEventListener('click', (e) => {
    e.preventDefault(); 
    document.querySelector('.career-history').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.acc').addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelector('.hero').scrollIntoView({ behavior: 'smooth' });
});

document.querySelector('.con').addEventListener('click', (e) => {
    e.preventDefault();
    document.querySelector('.contact').scrollIntoView({ behavior: 'smooth' });
});


const scrollContainer = document.querySelector('.career-scroll-container');
const scrollLeftButton = document.getElementById('scroll-left');
const scrollRightButton = document.getElementById('scroll-right');

scrollLeftButton.addEventListener('click', () => {
    scrollContainer.scrollBy({ left: -300, behavior: 'smooth' });
});

scrollRightButton.addEventListener('click', () => {
    scrollContainer.scrollBy({ left: 300, behavior: 'smooth' });
});


