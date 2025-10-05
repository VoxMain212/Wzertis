<template>
  <section id="home" class="hero">
    <!-- Blob-фоны -->
    <div 
      class="blob" 
      style="top: 10%; left: 10%; width: 250px; height: 250px; background-color: #1e7cff;"
    ></div>
    <div 
      class="blob" 
      style="top: 20%; right: 10%; width: 250px; height: 250px; background-color: #6633ff;"
    ></div>
    <div 
      class="blob" 
      style="bottom: 10%; left: 50%; width: 250px; height: 250px; background-color: #3366ff;"
    ></div>

    <!-- Тонкие звёзды / частицы (для глубины) -->
    <div class="stars"></div>

    <div class="hero-content">
      <h1 class="hero-title">
        Где <span class="highlight">Буквы</span> Встречают <span class="highlight">Мечты</span>
      </h1>
      <p class="hero-subtitle">
        Исследование пересечения каллиграфии, иллюстрации и космического воображения
      </p>
      <div class="hero-buttons">
        <a href="#gallery" class="btn btn-primary">
          Посмотреть галерею <span class="arrow">→</span>
        </a>
        <a href="#contact" class="btn btn-secondary">Связаться со мной</a>
      </div>
    </div>

    <!-- Плавная прокрутка вниз -->
    <a href="#about" class="scroll-down-indicator">
      <span class="scroll-icon"></span>
    </a>
  </section>
</template>

<style scoped>
.hero {
  padding: 0;
  position: relative;
  overflow: hidden;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background-color: var(--primary-color);
}

/* Усиленные blob-анимации */
.blob {
  position: absolute;
  border-radius: 50%;
  mix-blend-mode: multiply;
  filter: blur(80px);
  opacity: 0.25;
  animation: blob 12s infinite ease-in-out;
  z-index: 0;
}

.blob:nth-child(2) {
  animation-delay: 3s;
}
.blob:nth-child(3) {
  animation-delay: 6s;
}

/* Звёзды для глубины фона */
.stars {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: 
    radial-gradient(white, rgba(255,255,255,.1) 1px, transparent 2px),
    radial-gradient(white, rgba(255,255,255,.15) 1px, transparent 2px);
  background-size: 50px 50px, 70px 70px;
  background-position: 0 0, 25px 25px;
  opacity: 0.15;
  pointer-events: none;
  z-index: 0;
}

.hero-content {
  max-width: 800px;
  z-index: 2;
  padding: 0 20px;
}

/* Анимация заголовка */
.hero-title {
  font-size: 3.2rem;
  margin-bottom: 1.2rem;
  line-height: 1.15;
  font-weight: 800;
  letter-spacing: -0.5px;
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 1s ease-out 0.3s forwards;
}

.hero-title .highlight {
  color: var(--accent-color);
  position: relative;
  display: inline-block;
}

/* Подчёркивание при наведении (опционально, можно убрать) */
.hero-title .highlight::after {
  content: '';
  position: absolute;
  bottom: -8px;
  left: 0;
  width: 100%;
  height: 3px;
  background: var(--accent-color);
  opacity: 0;
  transform: scaleX(0);
  transition: all 0.4s ease;
}

.hero-title:hover .highlight::after {
  opacity: 1;
  transform: scaleX(1);
}

.hero-subtitle {
  font-size: 1.25rem;
  margin-bottom: 2.5rem;
  color: var(--gray-400);
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  opacity: 0;
  transform: translateY(15px);
  animation: fadeInUp 1s ease-out 0.6s forwards;
}

.hero-buttons {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 1s ease-out 0.9s forwards;
  display: flex;
  justify-content: center;
  gap: 24px;
  flex-wrap: wrap;
}

.btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 0.85rem 2rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.btn-primary {
  background-color: var(--accent-color);
  color: var(--primary-color);
}

.btn-primary:hover {
  background-color: #1a6cd4;
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 8px 20px rgba(30, 124, 255, 0.4);
}

.btn-secondary {
  border: 2px solid var(--gray-600);
  color: var(--text-color);
  background: transparent;
}

.btn-secondary:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
  transform: translateY(-4px) scale(1.03);
  box-shadow: 0 8px 20px rgba(30, 124, 255, 0.2);
}

/* Анимация стрелки в кнопке */
.arrow {
  display: inline-block;
  transition: transform 0.3s ease;
}

.btn-primary:hover .arrow {
  transform: translateX(4px);
}

/* Индикатор прокрутки вниз */
.scroll-down-indicator {
  position: absolute;
  bottom: 40px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  color: var(--gray-400);
  text-decoration: none;
  z-index: 2;
  opacity: 0;
  animation: fadeIn 1s ease-out 1.4s forwards;
}

.scroll-icon {
  width: 24px;
  height: 24px;
  border-left: 2px solid var(--gray-400);
  border-bottom: 2px solid var(--gray-400);
  transform: rotate(-45deg);
  margin-bottom: 8px;
  animation: bounce 2s infinite 1.6s;
}

/* Анимации */
@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes fadeIn {
  to {
    opacity: 1;
  }
}

@keyframes bounce {
  0%, 20%, 50%, 80%, 100% {
    transform: translateY(0) rotate(-45deg);
  }
  40% {
    transform: translateY(-10px) rotate(-45deg);
  }
  60% {
    transform: translateY(-5px) rotate(-45deg);
  }
}

/* Адаптив */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.2rem;
    line-height: 1.2;
  }

  .hero-subtitle {
    font-size: 1.1rem;
    padding: 0 10px;
  }

  .hero-buttons {
    gap: 16px;
    flex-direction: column;
    align-items: center;
  }

  .btn {
    width: 100%;
    max-width: 300px;
    justify-content: center;
  }

  .scroll-down-indicator {
    display: none; /* или оставить, если нужно */
  }
}
</style>