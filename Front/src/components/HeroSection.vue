<template>
  <section id="home" class="hero">
    <div class="blob" style="top: 10%; left: 10%; width: 250px; height: 250px; background-color: #1e7cff;"></div>
    <div class="blob" style="top: 20%; right: 10%; width: 250px; height: 250px; background-color: #6633ff;"></div>
    <div class="blob" style="bottom: 10%; left: 50%; width: 250px; height: 250px; background-color: #3366ff;"></div>
    <div class="hero-content">
      <h1>Где <span>Буквы</span> Встречают <span>Мечты</span></h1>
      <p>Исследование пересечения каллиграфии, иллюстрации и космического воображения</p>
      <div>
        <a href="#gallery" class="btn btn-primary">Посмотреть галерею <span>→</span></a>
        <a href="#contact" class="btn btn-secondary">Связаться со мной</a>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Скопировать стили hero и кнопок */
.hero {
  padding: 100px 20px 60px;
  position: relative;
  overflow: hidden;
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.hero-content {
  max-width: 800px;
  z-index: 1;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.hero h1 span {
  color: var(--accent-color);
}

.hero p {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  color: var(--gray-400);
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  cursor: pointer;
}

.btn-primary {
  background-color: var(--accent-color);
  color: var(--primary-color);
}

.btn-primary:hover {
  background-color: #1a6cd4;
  transform: translateY(-2px);
}

.btn-secondary {
  border: 2px solid var(--gray-600);
  color: var(--text-color);
}

.btn-secondary:hover {
  border-color: var(--accent-color);
  color: var(--accent-color);
  transform: translateY(-2px);
}

.blob {
  position: absolute;
  background-color: var(--accent-color);
  border-radius: 50%;
  mix-blend-mode: multiply;
  filter: blur(80px);
  opacity: 0.2;
  animation: blob 7s infinite;
}

.blob:nth-child(2) {
  animation-delay: 2s;
}

.blob:nth-child(3) {
  animation-delay: 4s;
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }
}
</style>