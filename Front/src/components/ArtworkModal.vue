<template>
  <div class="modal" v-show="isOpen">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">{{ artwork?.title }}</h3>
        <button class="modal-close" @click="close">&times;</button>
      </div>
      <div class="modal-body">
        <img :src="artwork?.image" :alt="artwork?.title" class="modal-image" />
        <div class="modal-details">
          <div class="modal-detail">
            <div class="modal-detail-label">Описание</div>
            <div class="modal-description">{{ artwork?.description }}</div>
          </div>
          <div class="modal-detail">
            <div class="modal-detail-label">Детали</div>
            <div>Техника: {{ artwork?.technique }}</div>
            <div>Год: {{ artwork?.date }}</div>
            <div>Категория: {{ getCategoryName(artwork?.category) }}</div>
          </div>
        </div>
      </div>
      <div class="modal-footer">
        <button class="btn btn-primary" @click="close">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  isOpen: Boolean,
  artwork: Object,
  categories: Array
});

const emit = defineEmits(['close']);

const close = () => emit('close');

const getCategoryName = (categoryId) => {
  const category = props.categories.find(cat => cat.id === categoryId);
  return category ? category.name : '';
};
</script>

<style scoped>
/* Скопировать стили modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
  z-index: 1000;
  padding: 20px;
  overflow-y: auto;
}

.modal-content {
  background-color: var(--gray-900);
  border-radius: 8px;
  max-width: 800px;
  margin: 0 auto;
  max-height: 90vh;
  overflow-y: auto;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 1.5rem;
  border-bottom: 1px solid var(--gray-800);
}

.modal-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.modal-close {
  background: none;
  border: none;
  color: var(--gray-400);
  font-size: 1.5rem;
  cursor: pointer;
  transition: color 0.3s ease;
}

.modal-close:hover {
  color: var(--text-color);
}

.modal-body {
  padding: 1.5rem;
}

.modal-image {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 1rem;
}

.modal-details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-bottom: 1rem;
}

.modal-detail {
  padding: 1rem;
  background-color: var(--gray-800);
  border-radius: 4px;
}

.modal-detail-label {
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.modal-description {
  margin-bottom: 1rem;
}

.modal-footer {
  padding: 1.5rem;
  text-align: right;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  transition: all 0.3s ease;
  cursor: pointer;
}

.btn-primary {
  background-color: var(--accent-color);
  color: var(--primary-color);
}

.btn-primary:hover {
  background-color: #1a6cd4;
  transform: translateY(-2px);
}
</style>