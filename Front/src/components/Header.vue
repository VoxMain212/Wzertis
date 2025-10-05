<template>
  <header :class="{ 'header-scrolled': isScrolled, 'mobile-open': isMobileMenuOpen }">
    <div class="header-container">
      <a href="#home" class="logo" @click="closeMobileMenu">WZERTIS</a>
      <nav v-if="!isMobile">
        <ul>
          <li v-for="item in menuItems" :key="item.href">
            <a
              :href="item.href"
              :class="{ active: activeSection === item.id }"
              @click="closeMobileMenu"
            >
              {{ item.label }}
            </a>
          </li>
        </ul>
      </nav>
      <button class="mobile-menu-btn" @click="toggleMobileMenu" v-if="isMobile" aria-label="Меню">
        <span class="hamburger"></span>
      </button>
    </div>
    <transition name="slide-down">
      <div class="mobile-menu" v-show="isMobileMenuOpen && isMobile">
        <a
          v-for="item in menuItems"
          :key="item.href"
          :href="item.href"
          @click="closeMobileMenu"
          :class="{ active: activeSection === item.id }"
        >
          {{ item.label }}
        </a>
      </div>
    </transition>
  </header>
</template>

<script setup>
import { ref, onMounted, onUnmounted, onBeforeUnmount } from 'vue';

const isMobileMenuOpen = ref(false);
const isMobile = ref(window.innerWidth <= 768);
const isScrolled = ref(false);
const activeSection = ref('home');

const menuItems = [
  { id: 'home', href: '#home', label: 'Главная' },
  { id: 'gallery', href: '#gallery', label: 'Галерея' },
  { id: 'about', href: '#about', label: 'Обо мне' },
  { id: 'contact', href: '#contact', label: 'Контакты' }
];

const toggleMobileMenu = () => isMobileMenuOpen.value = !isMobileMenuOpen.value;
const closeMobileMenu = () => isMobileMenuOpen.value = false;

const handleResize = () => {
  isMobile.value = window.innerWidth <= 768;
  if (!isMobile.value) isMobileMenuOpen.value = false;
};

const handleScroll = () => {
  // Эффект тени при скролле
  isScrolled.value = window.scrollY > 20;

  // Определение активной секции
  const sections = ['home', 'gallery', 'about', 'contact'];
  const scrollPos = window.scrollY + 100;

  for (const section of sections) {
    const el = document.getElementById(section);
    if (el) {
      const top = el.offsetTop;
      const height = el.offsetHeight;
      if (scrollPos >= top && scrollPos < top + height) {
        activeSection.value = section;
        break;
      }
    }
  }
};

onMounted(() => {
  window.addEventListener('resize', handleResize);
  window.addEventListener('scroll', handleScroll);
  handleScroll(); // инициализация
});

onBeforeUnmount(() => {
  window.removeEventListener('resize', handleResize);
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background-color: rgba(10, 10, 10, 0.85);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid transparent;
  padding: 1rem 0;
  transition: all 0.4s ease;
}

header.header-scrolled {
  background-color: var(--primary-color);
  border-bottom: 1px solid var(--gray-800);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
}

header.mobile-open {
  background-color: var(--primary-color);
  border-bottom: 1px solid var(--gray-800);
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  position: relative;
}

.logo {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  text-decoration: none;
  background: linear-gradient(to right, #ffffff, #a0a0ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  transition: transform 0.3s ease;
}

.logo:hover {
  transform: scale(1.05);
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
  font-weight: 500;
  position: relative;
  padding: 0.4rem 0;
  transition: color 0.3s ease;
}

nav a::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: var(--accent-color);
  transition: width 0.3s ease;
}

nav a:hover,
nav a.active {
  color: var(--accent-color);
}

nav a:hover::after,
nav a.active::after {
  width: 100%;
}

/* Мобильное меню */
.mobile-menu-btn {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  z-index: 1001;
}

.hamburger {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--text-color);
  position: relative;
  transition: all 0.3s ease;
}

.hamburger::before,
.hamburger::after {
  content: '';
  position: absolute;
  width: 24px;
  height: 2px;
  background: var(--text-color);
  transition: all 0.3s ease;
}

.hamburger::before {
  top: -6px;
}

.hamburger::after {
  bottom: -6px;
}

.mobile-menu {
  background-color: var(--primary-color);
  border-top: 1px solid var(--gray-800);
  padding: 1.2rem 0;
  overflow: hidden;
}

.mobile-menu a {
  display: block;
  color: var(--text-color);
  text-decoration: none;
  padding: 0.8rem 1.5rem;
  font-size: 1.1rem;
  font-weight: 500;
  transition: all 0.3s ease;
  position: relative;
}

.mobile-menu a::after {
  content: '';
  position: absolute;
  left: 1.5rem;
  bottom: 0;
  width: 0;
  height: 1px;
  background: var(--gray-600);
  transition: width 0.3s ease;
}

.mobile-menu a:hover,
.mobile-menu a.active {
  color: var(--accent-color);
  padding-left: 1.8rem;
}

.mobile-menu a:hover::after,
.mobile-menu a.active::after {
  width: 30px;
}

/* Анимации */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.slide-down-enter-from,
.slide-down-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Адаптив */
@media (max-width: 768px) {
  .header-container {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 0;
  }

  nav ul {
    display: none;
  }

  .mobile-menu-btn {
    display: block;
  }
}
</style>