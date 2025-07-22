// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger && navMenu) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // Close mobile menu when clicking on a link
        document.querySelectorAll('.nav-menu li a').forEach(link => {
            link.addEventListener('click', function() {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }
    
    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Функция для инициализации обработчиков кликов по артистам
    initArtistCardClickHandlers();
    
    // Анимация заголовка страницы
    initTitleAnimation();
});

// Функция для инициализации обработчиков кликов по артистам
function initArtistCardClickHandlers() {
    const artistCards = document.querySelectorAll('.artist-card');
    
    artistCards.forEach(card => {
        // Удаляем старые обработчики если есть
        const oldHandler = card._clickHandler;
        if (oldHandler) {
            card.removeEventListener('click', oldHandler);
        }
        
        // Создаем новый обработчик
        const clickHandler = function(e) {
            // Получаем данные об артисте из DOM
            const rank = this.querySelector('.artist-rank')?.textContent;
            const artistName = this.querySelector('.artist-info h4')?.textContent;
            const artistTime = this.querySelector('.artist-time')?.textContent;
            const artistIcon = this.querySelector('.artist-icon')?.textContent;
            
            // Создаем объект с данными артиста
            const artistData = {
                rank: rank,
                name: artistName,
                time: artistTime,
                icon: artistIcon
            };
            
            // Логируем клик в консоль
            console.log('Клик по артисту:', artistData);
            
            // Добавляем визуальный эффект клика
            this.classList.add('clicked');
            setTimeout(() => {
                this.classList.remove('clicked');
            }, 600);
            
            handleArtistClick(artistData);
        };
        
        // Сохраняем ссылку на обработчик для последующего удаления
        card._clickHandler = clickHandler;
        card.addEventListener('click', clickHandler);
        
        // Добавляем стиль курсора для указания кликабельности
        card.style.cursor = 'pointer';
    });
}

// Функция обработки клика по артисту
function handleArtistClick(artistData) {
    // Здесь можно добавить дополнительную логику:
    // - отправить аналитику
    // - открыть модальное окно с информацией об артисте
    // - воспроизвести музыку
    // - перейти на страницу артиста
    
    console.log(`Выбран артист: ${artistData.name} с ${artistData.time} прослушивания`);
}

// Функция для показа уведомлений
function showNotification(message) {
    // Создаем элемент уведомления
    const notification = document.createElement('div');
    notification.className = 'artist-notification';
    notification.textContent = message;
    
    document.body.appendChild(notification);
    
    // Показываем уведомление
    setTimeout(() => {
        notification.style.opacity = '1';
    }, 100);
    
    // Скрываем через 3 секунды
    setTimeout(() => {
        notification.style.opacity = '0';
        setTimeout(() => {
            if (notification.parentNode) {
                document.body.removeChild(notification);
            }
        }, 300);
    }, 3000);
}

// Анимация заголовка страницы
function initTitleAnimation() {
    const baseTitle = "BIO";
    const phrases = [
        "| " + namePage,
        "| Python Developer",
        "| Django Developer",
        "| Backend Developer",
        "| Web Developer",
        "| Software Engineer",
        "| Programmer",
        "| Coder",
        "| Developer",
        "| Full Stack Developer",
    ];
    
    let currentPhrase = 0;
    let currentChar = 0;
    let isDeleting = false;
    let isEnd = false;
    
    function typeTitle() {
        const phraseText = phrases[currentPhrase];
        const fullText = phraseText.substring(0, currentChar);
        
        document.title = baseTitle + " " + fullText;
        
        // печать
        if (!isDeleting && currentChar <= phraseText.length) {
            currentChar++;
            
            if (currentChar > phraseText.length) {
                isEnd = true;
                isDeleting = true;
                setTimeout(typeTitle, 1500);
                return;
            }
        }
        
        // удаление
        if (isDeleting && currentChar >= 0) {
            currentChar--;
            
            if (currentChar === 0) {
                isDeleting = false;
                currentPhrase = (currentPhrase + 1) % phrases.length;
            }
        }
        
        // скорость анимации
        const typingSpeed = isDeleting ? 50 : 200;
        const nextStep = isEnd ? 0 : typingSpeed;
        isEnd = false;
        
        setTimeout(typeTitle, nextStep);
    }
    
    typeTitle();
}