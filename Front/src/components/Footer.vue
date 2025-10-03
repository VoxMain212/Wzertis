<template>
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-logo">WZERTIS</div>
        <div class="footer-social">
          <a href="#">TG</a>
          <a href="#">VK</a>
          <a href="#">IG</a>
        </div>
      </div>
      <div class="footer-copyright">
        &copy; {{ currentYear }} WZERTIS. Все права защищены.
      </div>
    </div>
  </footer>
</template>

<script setup>
const currentYear = new Date().getFullYear();
</script>

<style scoped>
/* Скопировать стили footer */
footer {
  background-color: var(--primary-color);
  border-top: 1px solid var(--gray-800);
  padding: 2rem 20px;
  text-align: center;
}

.footer-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

@media (min-width: 768px) {
  .footer-content {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}

.footer-logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.footer-social {
  display: flex;
  gap: 1rem;
}

.footer-social a {
  color: var(--gray-400);
  text-decoration: none;
  font-size: 1.5rem;
  transition: color 0.3s ease;
}

.footer-social a:hover {
  color: var(--accent-color);
}

.footer-copyright {
  margin-top: 1rem;
  color: var(--gray-400);
  font-size: 0.9rem;
}
</style>