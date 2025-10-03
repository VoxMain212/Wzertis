<template>
  <header>
    <div class="header-container">
      <div class="logo">WZERTIS</div>
      <nav v-if="!isMobile">
        <ul>
          <li><a href="#home">Главная</a></li>
          <li><a href="#gallery">Галерея</a></li>
          <li><a href="#about">Обо мне</a></li>
          <li><a href="#contact">Контакты</a></li>
        </ul>
      </nav>
      <button class="mobile-menu-btn" @click="toggleMobileMenu" v-if="isMobile">☰</button>
    </div>
    <div class="mobile-menu" v-show="isMobileMenuOpen && isMobile">
      <a href="#home" @click="closeMobileMenu">Главная</a>
      <a href="#gallery" @click="closeMobileMenu">Галерея</a>
      <a href="#about" @click="closeMobileMenu">Обо мне</a>
      <a href="#contact" @click="closeMobileMenu">Контакты</a>
    </div>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

const isMobileMenuOpen = ref(false);
const isMobile = ref(window.innerWidth <= 768);

const toggleMobileMenu = () => isMobileMenuOpen.value = !isMobileMenuOpen.value;
const closeMobileMenu = () => isMobileMenuOpen.value = false;

const handleResize = () => {
  isMobile.value = window.innerWidth <= 768;
  if (!isMobile.value) isMobileMenuOpen.value = false;
};

onMounted(() => window.addEventListener('resize', handleResize));
onUnmounted(() => window.removeEventListener('resize', handleResize));
</script>

<style scoped>
/* Скопировать стили header из оригинала */
header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 50;
  background-color: var(--primary-color);
  border-bottom: 1px solid var(--gray-800);
  padding: 1rem 0;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  letter-spacing: 1px;
}

nav ul {
  display: flex;
  list-style: none;
}

nav li {
  margin-left: 2rem;
}

nav a {
  color: var(--text-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

nav a:hover {
  color: var(--accent-color);
}

.mobile-menu-btn {
  display: none;
  cursor: pointer;
}

.mobile-menu {
  display: none;
  background-color: var(--primary-color);
  border-top: 1px solid var(--gray-800);
  padding: 1rem 0;
}

.mobile-menu a {
  display: block;
  color: var(--text-color);
  text-decoration: none;
  padding: 0.5rem 1rem;
  transition: color 0.3s ease;
}

.mobile-menu a:hover {
  color: var(--accent-color);
}

@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
    gap: 1rem;
  }

  nav ul {
    display: none;
  }

  .mobile-menu-btn {
    display: block;
  }

  .mobile-menu {
    display: block;
  }
}
</style>