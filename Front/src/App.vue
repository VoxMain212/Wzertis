<template>
  <div id="app">
    <Header />
    <HeroSection />
    <FeaturedCarousel 
      :featured-works="featuredWorks" 
      @open-modal="openArtworkModal" 
    />
    <GallerySection 
      :artworks="artworks" 
      :categories="categories" 
      @open-modal="openArtworkModal" 
    />
    <AboutSection />
    <ContactSection @form-submitted="handleFormSubmit" />
    <Footer />
    
    <ArtworkModal 
      :is-open="isModalOpen" 
      :artwork="selectedArtwork" 
      :categories="categories"
      @close="closeModal" 
    />
  </div>
</template>

<script>
import Header from './components/Header.vue';
import HeroSection from './components/HeroSection.vue';
import FeaturedCarousel from './components/FeaturedCarousel.vue';
import GallerySection from './components/GallerySection.vue';
import AboutSection from './components/AboutSection.vue';
import ContactSection from './components/ContactSection.vue';
import Footer from './components/Footer.vue';
import ArtworkModal from './components/ArtworkModal.vue';

export default {
  name: 'App',
  components: {
    Header,
    HeroSection,
    FeaturedCarousel,
    GallerySection,
    AboutSection,
    ContactSection,
    Footer,
    ArtworkModal
  },
  data() {
    return {
      isModalOpen: false,
      selectedArtwork: null,
      featuredWorks: [],
      artworks: [],
      categories: []
    };
  },
  async created() {
    // Загружаем все данные при старте
    await this.loadAllData();
  },
  methods: {
    async loadAllData() {
      try {
        const categoriesRes = await fetch('http://127.0.0.1:8000/groups/');
        this.categories = await categoriesRes.json();
        console.log('Категории:', this.categories); // ← добавьте это

        const artworksRes = await fetch('http://127.0.0.1:8000/artworks/');
        this.artworks = await artworksRes.json();
        console.log('Работы:', this.artworks);

        const featuredRes = await fetch('http://127.0.0.1:8000/fav_works/');
        this.featuredWorks = await featuredRes.json();
        console.log('Избранные:', this.featuredWorks);
      } catch (err) {
        console.error('Ошибка загрузки данных:', err);
      }
    },
    openArtworkModal(artwork) {
      this.selectedArtwork = artwork;
      this.isModalOpen = true;
    },
    closeModal() {
      this.isModalOpen = false;
      this.selectedArtwork = null;
    },
    handleFormSubmit() {
      alert('Сообщение отправлено! Спасибо за ваше обращение.');
    }
  }
};
</script>

<style>
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

@keyframes blob {
  0% { transform: translate(0px, 0px) scale(1); }
  33% { transform: translate(30px, -70px) scale(1.1); }
  66% { transform: translate(-20px, 20px) scale(0.9); }
  100% { transform: translate(0px, 0px) scale(1); }
}
</style>