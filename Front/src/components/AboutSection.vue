<template>
  <section id="about" class="about-section">
    <div class="container">
      <h2 class="section-title">Обо мне</h2>
      <div class="about-content">
        <div class="about-image">
          <img src="https://placehold.co/400x500/1e1e1e/ffffff?text=Портрет+художника" alt="Портрет художника" />
        </div>
        <div class="about-text">
          <p>Я визуальный художник, специализирующийся на слиянии каллиграфии, иллюстрации и космических образов...</p>
          <p>Мой путь начался с традиционных техник письма...</p>
          <p>Когда я не создаю искусство, я изучаю древние письмена...</p>
          <div class="social-links">
            <a href="#" class="social-link">IG</a>
            <a href="#" class="social-link">TW</a>
            <a href="#" class="social-link">FB</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
/* Скопировать стили about-section */
.about-section {
  padding: 60px 20px;
  background-color: var(--gray-900);
}

.about-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

@media (min-width: 768px) {
  .about-content {
    flex-direction: row;
    align-items: center;
  }
}

.about-image {
  flex: 0 0 300px;
}

.about-image img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.about-text {
  flex: 1;
}

.about-text p {
  margin-bottom: 1rem;
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.social-link {
  color: var(--accent-color);
  text-decoration: none;
  font-size: 1.5rem;
  transition: color 0.3s ease;
}

.social-link:hover {
  color: #1a6cd4;
}

@media (max-width: 768px) {
  .about-content {
    flex-direction: column;
  }

  .about-image {
    flex: 0 0 100%;
  }
}
</style>