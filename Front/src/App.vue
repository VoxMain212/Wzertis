<template>
  <Header />
  <HeroSection />
  <FeaturedCarousel :featured-works="featuredWorks" />
  <GallerySection :artworks="artworks" :categories="categories" />
  <AboutSection />
  <ContactSection @form-submitted="handleFormSubmit" />
  <Footer />
  <ArtworkModal 
    :is-open="isModalOpen" 
    :artwork="selectedArtwork" 
    :categories="categories"
    @close="closeModal" 
  />
</template>

<script setup>
import { ref } from 'vue';
import Header from './components/Header.vue';
import HeroSection from './components/HeroSection.vue';
import FeaturedCarousel from './components/FeaturedCarousel.vue';
import GallerySection from './components/GallerySection.vue';
import AboutSection from './components/AboutSection.vue';
import ContactSection from './components/ContactSection.vue';
import Footer from './components/Footer.vue';
import ArtworkModal from './components/ArtworkModal.vue';

// Данные
const featuredWorks = ref([
  {
    title: "Космическая каллиграфия",
    image: "https://placehold.co/1200x800/0a0a0a/ffffff?text=Космическая+каллиграфия",
    description: "Слияние космических элементов и сложных буквенных форм."
  },
  {
    title: "Синие мечты",
    image: "https://placehold.co/1200x800/1e3c5f/ffffff?text=Синие+мечты",
    description: "Сюрреалистическая композиция, сочетающая аниме-эстетику с каллиграфическими элементами."
  },
  {
    title: "Синий змей",
    image: "https://placehold.co/1200x800/0a0a0a/1e7cff?text=Синий+змей",
    description: "Мистическое существо, возникающее из космических узоров."
  }
]);

const artworks = ref([
  {
    id: 1,
    title: "Космическая каллиграфия",
    description: "Слияние космических элементов и сложных буквенных форм.",
    image: "https://placehold.co/800x600/0a0a0a/ffffff?text=Космическая+каллиграфия",
    category: "calligraphy",
    date: "2023",
    technique: "Акрил на холсте"
  },
  {
    id: 2,
    title: "Исследование готического алфавита",
    description: "Исследование темной элегантности готических буквенных форм.",
    image: "https://placehold.co/800x600/1e1e1e/ffffff?text=Готический+алфавит",
    category: "calligraphy",
    date: "2023",
    technique: "Чернила на бумаге"
  },
  {
    id: 3,
    title: "Синие мечты",
    description: "Сюрреалистическая композиция, сочетающая аниме-эстетику с каллиграфическими элементами.",
    image: "https://placehold.co/800x600/1e3c5f/ffffff?text=Синие+мечты",
    category: "illustration",
    date: "2023",
    technique: "Цифровая иллюстрация"
  },
  {
    id: 4,
    title: "Темная элегантность",
    description: "Монохромное исследование в черно-белых тонах с драматическими контрастами.",
    image: "https://placehold.co/800x600/0d0d0d/ffffff?text=Темная+элегантность",
    category: "illustration",
    date: "2023",
    technique: "Перо и чернила"
  },
  {
    id: 5,
    title: "Синий змей",
    description: "Мистическое существо, возникающее из космических узоров.",
    image: "https://placehold.co/800x600/0a0a0a/1e7cff?text=Синий+змей",
    category: "illustration",
    date: "2023",
    technique: "Смешанная техника"
  },
  {
    id: 6,
    title: "Абстрактные буквенные формы",
    description: "Деконструкция традиционного письма в абстрактные композиции.",
    image: "https://placehold.co/800x600/1a1a1a/ffffff?text=Абстрактные+формы",
    category: "calligraphy",
    date: "2023",
    technique: "Маркер на картоне"
  }
]);

const categories = ref([
  { id: 'all', name: 'Все работы' },
  { id: 'calligraphy', name: 'Каллиграфия' },
  { id: 'illustration', name: 'Иллюстрация' }
]);

// Модальное окно
const isModalOpen = ref(false);
const selectedArtwork = ref(null);

const openArtworkModal = (artwork) => {
  selectedArtwork.value = artwork;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  selectedArtwork.value = null;
};

// Эмиттеры
const handleFormSubmit = () => {
  alert('Сообщение отправлено! Спасибо за ваше обращение.');
};

// Экспортируем методы для дочерних компонентов
defineExpose({
  openArtworkModal,
  closeModal
});
</script>

<style>
/* Здесь оставляем только глобальные стили из :root и * */
:root {
  --primary-color: #0a0a0a;
  --secondary-color: #1e3c5f;
  --accent-color: #1e7cff;
  --text-color: #ffffff;
  --gray-800: #1e1e1e;
  --gray-900: #121212;
  --gray-700: #2d2d2d;
  --gray-600: #444444;
  --gray-400: #999999;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: var(--primary-color);
  color: var(--text-color);
  line-height: 1.6;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Анимации */
@keyframes blob {
  0% { transform: translate(0px, 0px) scale(1); }
  33% { transform: translate(30px, -70px) scale(1.1); }
  66% { transform: translate(-20px, 20px) scale(0.9); }
  100% { transform: translate(0px, 0px) scale(1); }
}
</style>