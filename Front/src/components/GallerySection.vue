<template>
  <section id="gallery" class="gallery-section">
    <div class="container">
      <h2 class="section-title">Галерея</h2>
      <div class="category-filter">
        <button
          v-for="category in categories"
          :key="category.id"
          :class="['category-btn', { active: selectedCategory === category.id }]"
          @click="selectCategory(category.id)"
        >
          {{ category.name }}
        </button>
      </div>
      <div class="gallery-grid">
        <div
          v-for="artwork in filteredArtworks"
          :key="artwork.id"
          class="gallery-item"
          @click="openModal(artwork)"
        >
          <img :src="artwork.image" :alt="artwork.title" class="gallery-image" />
          <div class="gallery-info">
            <h3>{{ artwork.title }}</h3>
            <p>{{ artwork.technique }} • {{ artwork.date }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  artworks: {
    type: Array,
    required: true
  },
  categories: {
    type: Array,
    required: true
  }
});

const emit = defineEmits(['open-artwork']);

const selectedCategory = ref('all');

const filteredArtworks = computed(() => {
  if (selectedCategory.value === 'all') return props.artworks;
  return props.artworks.filter(art => art.category === selectedCategory.value);
});

const selectCategory = (id) => {
  selectedCategory.value = id;
};

const openModal = (artwork) => {
  emit('open-artwork', artwork);
};
</script>

<style scoped>
/* Скопировать стили gallery-section */
.gallery-section {
  padding: 60px 20px;
}

.category-filter {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 2rem;
}

.category-btn {
  padding: 0.5rem 1rem;
  border-radius: 20px;
  border: none;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s ease;
}

.category-btn.active {
  background-color: var(--accent-color);
  color: var(--primary-color);
}

.category-btn:not(.active) {
  background-color: var(--gray-800);
  color: var(--text-color);
}

.category-btn:hover {
  transform: translateY(-2px);
}

.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
}

.gallery-item {
  cursor: pointer;
  transition: transform 0.3s ease;
}

.gallery-item:hover {
  transform: scale(1.03);
}

.gallery-image {
  width: 100%;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
}

.gallery-info {
  padding: 1rem 0;
}

.gallery-info h3 {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}

.gallery-info p {
  color: var(--gray-400);
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .gallery-grid {
    grid-template-columns: 1fr;
  }
}
</style>