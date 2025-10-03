<template>
  <section id="featured" class="featured-section">
    <div class="container">
      <h2 class="section-title">Избранные работы</h2>
      <div class="carousel-container">
        <div class="carousel">
          <div class="carousel-slide" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
            <div v-for="(work, index) in featuredWorks" :key="index" class="slide-item">
              <img :src="work.image" :alt="work.title" class="slide-image" />
              <div class="slide-caption">
                <h3>{{ work.title }}</h3>
                <p>{{ work.description }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="carousel-nav">
          <button @click="prevSlide">←</button>
          <button @click="nextSlide">→</button>
        </div>
        <div class="carousel-dots">
          <div
            v-for="(dot, index) in featuredWorks"
            :key="index"
            class="carousel-dot"
            :class="{ active: currentSlide === index }"
            @click="goToSlide(index)"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const props = defineProps({
  featuredWorks: {
    type: Array,
    required: true
  }
});

const currentSlide = ref(0);

const nextSlide = () => {
  currentSlide.value = (currentSlide.value + 1) % props.featuredWorks.length;
};

const prevSlide = () => {
  currentSlide.value = (currentSlide.value - 1 + props.featuredWorks.length) % props.featuredWorks.length;
};

const goToSlide = (index) => {
  currentSlide.value = index;
};

onMounted(() => {
  const interval = setInterval(() => {
    nextSlide();
  }, 5000);
  //onUnmounted(() => clearInterval(interval));
});
</script>

<style scoped>
/* Скопировать стили featured-section и карусели */
.featured-section {
  padding: 60px 20px;
  background-color: var(--gray-900);
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  margin-bottom: 2rem;
}

.carousel-container {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
}

.carousel {
  overflow: hidden;
  border-radius: 10px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
}

.carousel-slide {
  display: flex;
  transition: transform 0.5s ease;
}

.slide-item {
  min-width: 100%;
  position: relative;
}

.slide-image {
  width: 100%;
  height: 400px;
  object-fit: cover;
}

.slide-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
  padding: 1.5rem;
}

.slide-caption h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
}

.slide-caption p {
  color: var(--gray-400);
}

.carousel-nav {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
}

.carousel-nav button {
  background-color: rgba(0, 0, 0, 0.5);
  color: white;
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background-color 0.3s ease;
}

.carousel-nav button:hover {
  background-color: rgba(0, 0, 0, 0.7);
}

.carousel-dots {
  display: flex;
  justify-content: center;
  margin-top: 1rem;
}

.carousel-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin: 0 5px;
  cursor: pointer;
  background-color: var(--gray-600);
  transition: background-color 0.3s ease;
}

.carousel-dot.active {
  background-color: var(--accent-color);
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }
}
</style>