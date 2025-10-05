<template>
  <section id="featured" class="featured-section" v-if="featuredWorks.length">
    <div class="container">
      <h2 class="section-title">Избранные работы</h2>
      <div class="carousel-container">
        <div class="carousel">
          <div
            class="carousel-slide"
            :style="{ transform: `translateX(-${currentSlide * 100}%)` }"
          >
            <div
              v-for="(work, index) in featuredWorks"
              :key="index"
              class="slide-item"
              @click="openModal(work)"
            >
              <div class="slide-wrapper">
                <img
                  :src="'http://127.0.0.1:8000' + work.image"
                  :alt="work.title"
                  class="slide-image"
                />
                <div class="slide-overlay"></div>
                <div class="slide-caption">
                  <h3>{{ work.title }}</h3>
                  <p>{{ work.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Навигация -->
        <div class="carousel-nav">
          <button @click.stop="prevSlide" aria-label="Предыдущая работа">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="15 18 9 12 15 6"></polyline>
            </svg>
          </button>
          <button @click.stop="nextSlide" aria-label="Следующая работа">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
        </div>

        <!-- Доты -->
        <div class="carousel-dots">
          <div
            v-for="(dot, index) in featuredWorks"
            :key="index"
            class="carousel-dot"
            :class="{ active: currentSlide === index }"
            @click.stop="goToSlide(index)"
            :aria-label="`Перейти к слайду ${index + 1}`"
          ></div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'FeaturedCarousel',
  props: {
    featuredWorks: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      currentSlide: 0,
      autoSlideInterval: null
    };
  },
  methods: {
    nextSlide() {
      this.currentSlide = (this.currentSlide + 1) % this.featuredWorks.length;
    },
    prevSlide() {
      this.currentSlide =
        (this.currentSlide - 1 + this.featuredWorks.length) %
        this.featuredWorks.length;
    },
    goToSlide(index) {
      this.currentSlide = index;
    },
    openModal(work) {
      this.$emit('open-modal', work);
    }
  },
  mounted() {
    this.autoSlideInterval = setInterval(() => {
      this.nextSlide();
    }, 6000); // чуть дольше — 6 сек
  },
  beforeUnmount() {
    if (this.autoSlideInterval) {
      clearInterval(this.autoSlideInterval);
    }
  }
};
</script>

<style scoped>
.featured-section {
  padding: 80px 20px 100px;
  background: linear-gradient(180deg, var(--gray-900) 0%, #0a0a12 100%);
  position: relative;
  overflow: hidden;
}

.featured-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at center, rgba(30, 124, 255, 0.05) 0%, transparent 70%);
  pointer-events: none;
  z-index: 0;
}

.container {
  position: relative;
  z-index: 2;
}

.section-title {
  text-align: center;
  font-size: 2.8rem;
  margin-bottom: 2.5rem;
  font-weight: 800;
  background: linear-gradient(to right, #ffffff, #a0a0ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: -0.5px;
}

.carousel-container {
  position: relative;
  max-width: 1100px;
  margin: 0 auto;
}

.carousel {
  overflow: visible; /* чтобы тени не обрезались */
  border-radius: 16px;
  position: relative;
}

.carousel-slide {
  display: flex;
  transition: transform 0.6s cubic-bezier(0.22, 0.61, 0.36, 1);
}

.slide-item {
  min-width: 100%;
  position: relative;
  cursor: pointer;
  padding: 0 10px;
  display: flex;
  justify-content: center;
}

.slide-wrapper {
  width: 100%;
  max-width: 900px;
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow:
    0 20px 50px rgba(0, 0, 0, 0.6),
    0 0 0 1px rgba(255, 255, 255, 0.05);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.slide-wrapper:hover {
  transform: scale(1.02);
  box-shadow:
    0 25px 60px rgba(0, 0, 0, 0.7),
    0 0 0 1px rgba(30, 124, 255, 0.3);
}

.slide-image {
  width: 100%;
  height: 500px;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.slide-wrapper:hover .slide-image {
  transform: scale(1.03);
}

.slide-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.7), transparent 60%);
  pointer-events: none;
}

.slide-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2rem;
  color: white;
  z-index: 2;
  transform: translateY(20px);
  opacity: 0;
  transition: all 0.4s ease;
}

.slide-wrapper:hover .slide-caption {
  transform: translateY(0);
  opacity: 1;
}

.slide-caption h3 {
  font-size: 1.8rem;
  margin-bottom: 0.75rem;
  font-weight: 700;
  letter-spacing: -0.5px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.slide-caption p {
  color: var(--gray-300);
  font-size: 1.1rem;
  line-height: 1.5;
  max-width: 600px;
  opacity: 0.9;
}

/* Навигация */
.carousel-nav {
  position: absolute;
  top: 50%;
  width: 100%;
  display: flex;
  justify-content: space-between;
  padding: 0 20px;
  transform: translateY(-50%);
  z-index: 3;
}

.carousel-nav button {
  background: rgba(10, 10, 10, 0.7);
  color: white;
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.carousel-nav button:hover {
  background: rgba(30, 124, 255, 0.3);
  transform: scale(1.1);
  color: white;
}

/* Доты */
.carousel-dots {
  display: flex;
  justify-content: center;
  margin-top: 2rem;
  gap: 8px;
}

.carousel-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  cursor: pointer;
  background-color: rgba(255, 255, 255, 0.3);
  transition: all 0.3s ease;
}

.carousel-dot:hover {
  background-color: rgba(255, 255, 255, 0.6);
  transform: scale(1.2);
}

.carousel-dot.active {
  background-color: var(--accent-color);
  transform: scale(1.3);
  box-shadow: 0 0 0 3px rgba(30, 124, 255, 0.3);
}

/* Адаптив */
@media (max-width: 768px) {
  .section-title {
    font-size: 2.2rem;
  }

  .slide-image {
    height: 350px;
  }

  .slide-caption h3 {
    font-size: 1.5rem;
  }

  .slide-caption p {
    font-size: 1rem;
  }

  .carousel-nav button {
    width: 40px;
    height: 40px;
  }
}

@media (max-width: 480px) {
  .slide-image {
    height: 280px;
  }

  .slide-caption {
    padding: 1.25rem;
  }
}
</style>