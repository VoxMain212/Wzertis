<template>
  <section id="gallery" class="gallery-section">
    <div class="container">
      <h2 class="section-title">Галерея</h2>
      <div class="category-filter">
        <button
          :class="['category-btn', { active: selectedCategory === 'all' }]"
          @click="selectCategory('all')"
        >
          Все работы
        </button>
        <button
          v-for="category in categories"
          :key="category.id"
          :class="['category-btn', { active: selectedCategory === category.id }]"
          @click="selectCategory(category.id)"
        >
          {{ category.title }}
        </button>
      </div>
      <div class="gallery-grid" :class="{ animated: isAnimated }">
        <div
          v-for="(artwork, index) in filteredArtworks"
          :key="artwork.id"
          class="gallery-item"
          @click="openModal(artwork)"
        >
          <div class="gallery-card">
            <img
              :src="'http://127.0.0.1:8000' + artwork.image"
              :alt="artwork.title"
              class="gallery-image"
              loading="lazy"
            />
            <div class="gallery-overlay"></div>
            <div class="gallery-info">
              <h3>{{ artwork.title }}</h3>
              <p>
                <span v-if="artwork.collection">{{ artwork.collection }} • </span>
                {{ artwork.year }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'GallerySection',
  props: {
    artworks: {
      type: Array,
      default: () => []
    },
    categories: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      selectedCategory: 'all',
      isAnimated: false
    };
  },
  computed: {
    filteredArtworks() {
      if (this.selectedCategory === 'all') {
        return this.artworks;
      }
      return this.artworks.filter(art => art.group === this.selectedCategory);
    }
  },
  methods: {
    selectCategory(category) {
      this.selectedCategory = category;
      // После смены фильтра — перезапускаем анимацию
      this.isAnimated = false;
      this.$nextTick(() => {
        this.isAnimated = true;
      });
    },
    openModal(artwork) {
      this.$emit('open-modal', artwork);
    }
  },
  mounted() {
    // Запускаем анимацию после первого рендера
    this.$nextTick(() => {
      this.isAnimated = true;
    });
  }
};
</script>

<style scoped>
.gallery-section {
  padding: 80px 20px 100px;
  background: var(--primary-color);
  position: relative;
}

.gallery-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--accent-color);
  border-radius: 2px;
  opacity: 0.3;
}

.section-title {
  text-align: center;
  font-size: 2.6rem;
  margin-bottom: 2.5rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

/* Фильтры */
.category-filter {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-bottom: 2.5rem;
  padding: 0 10px;
}

.category-btn {
  padding: 0.6rem 1.4rem;
  border-radius: 30px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  background: var(--gray-800);
  color: var(--text-color);
  position: relative;
  overflow: hidden;
}

.category-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--accent-color);
  opacity: 0;
  z-index: -1;
  transition: opacity 0.3s ease;
}

.category-btn.active {
  color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(30, 124, 255, 0.3);
}

.category-btn.active::before {
  opacity: 1;
}

.category-btn:hover:not(.active) {
  background: var(--gray-700);
  transform: translateY(-2px);
}

/* Сетка галереи */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 32px;
  padding: 0 10px;
}

.gallery-section {
  padding: 80px 20px 100px;
  background: var(--primary-color);
  position: relative;
}

.gallery-section::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--accent-color);
  border-radius: 2px;
  opacity: 0.3;
}

.section-title {
  text-align: center;
  font-size: 2.6rem;
  margin-bottom: 2.5rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  position: relative;
  display: inline-block;
  left: 50%;
  transform: translateX(-50%);
}

.category-filter {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-bottom: 2.5rem;
  padding: 0 10px;
}

.category-btn {
  padding: 0.6rem 1.4rem;
  border-radius: 30px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  font-size: 1rem;
  transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  background: var(--gray-800);
  color: var(--text-color);
  position: relative;
  overflow: hidden;
}

.category-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: var(--accent-color);
  opacity: 0;
  z-index: -1;
  transition: opacity 0.3s ease;
}

.category-btn.active {
  color: var(--primary-color);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(30, 124, 255, 0.3);
}

.category-btn.active::before {
  opacity: 1;
}

.category-btn:hover:not(.active) {
  background: var(--gray-700);
  transform: translateY(-2px);
}

/* Сетка галереи */
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 32px;
  padding: 0 10px;
}

/* Анимация применяется ТОЛЬКО когда класс .animated есть */
.gallery-grid.animated .gallery-item {
  opacity: 0;
  transform: translateY(20px);
  animation: fadeInUp 0.6s ease-out forwards;
  animation-delay: calc(var(--index) * 0.05s);
}

/* Чтобы animation-delay работал, передаём index через CSS-переменную */
.gallery-grid.animated .gallery-item:nth-child(1) { --index: 0; }
.gallery-grid.animated .gallery-item:nth-child(2) { --index: 1; }
.gallery-grid.animated .gallery-item:nth-child(3) { --index: 2; }
.gallery-grid.animated .gallery-item:nth-child(4) { --index: 3; }
.gallery-grid.animated .gallery-item:nth-child(5) { --index: 4; }
.gallery-grid.animated .gallery-item:nth-child(6) { --index: 5; }
.gallery-grid.animated .gallery-item:nth-child(7) { --index: 6; }
.gallery-grid.animated .gallery-item:nth-child(8) { --index: 7; }
.gallery-grid.animated .gallery-item:nth-child(9) { --index: 8; }
.gallery-grid.animated .gallery-item:nth-child(10) { --index: 9; }
/* Можно добавить больше, если нужно, или использовать JS для динамической установки --index */

@keyframes fadeInUp {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Остальной стиль карточек — без изменений */
.gallery-item {
  cursor: pointer;
}

.gallery-card {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  box-shadow:
    0 10px 25px rgba(0, 0, 0, 0.4),
    0 0 0 1px rgba(255, 255, 255, 0.03);
  transition: transform 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275),
              box-shadow 0.4s ease;
}

.gallery-card:hover {
  transform: translateY(-8px) scale(1.01);
  box-shadow:
    0 20px 40px rgba(0, 0, 0, 0.6),
    0 0 0 2px rgba(30, 124, 255, 0.2);
}

.gallery-image {
  width: 100%;
  height: 320px;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.gallery-card:hover .gallery-image {
  transform: scale(1.05);
}

.gallery-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.6), transparent 70%);
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.gallery-card:hover .gallery-overlay {
  opacity: 1;
}

.gallery-info {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 1.5rem;
  color: white;
  z-index: 2;
  transform: translateY(10px);
  opacity: 0;
  transition: all 0.4s ease;
}

.gallery-card:hover .gallery-info {
  transform: translateY(0);
  opacity: 1;
}

.gallery-info h3 {
  font-size: 1.35rem;
  margin-bottom: 0.4rem;
  font-weight: 700;
  letter-spacing: -0.3px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.gallery-info p {
  color: var(--gray-300);
  font-size: 0.95rem;
  opacity: 0.9;
}

/* Адаптив */
@media (max-width: 768px) {
  .section-title {
    font-size: 2.1rem;
  }

  .gallery-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }

  .gallery-image {
    height: 280px;
  }

  .category-btn {
    padding: 0.5rem 1.2rem;
    font-size: 0.95rem;
  }
}

@media (max-width: 480px) {
  .gallery-image {
    height: 240px;
  }

  .gallery-info h3 {
    font-size: 1.2rem;
  }
}
</style>