<template>
  <div class="modal" v-show="isOpen" @click.self="close">
    <div class="modal-content">
      <div class="modal-header">
        <h3 class="modal-title">{{ artwork ? artwork.title : 'Загрузка...' }}</h3>
        <button class="modal-close" @click="close">&times;</button>
      </div>

      <div class="modal-body">
        <div class="modal-layout">
          <!-- Изображение слева -->
          <div class="modal-image-container">
            <div class="image-wrapper">
              <img 
                v-if="artwork && artwork.image" 
                :src="'http://127.0.0.1:8000' + artwork.image" 
                :alt="artwork.title || 'Работа'" 
                class="modal-image"
                loading="lazy"
              />
              <div v-else class="modal-image-placeholder">Изображение отсутствует</div>
              <div class="image-glow"></div>
            </div>
          </div>

          <!-- Информация справа -->
          <div class="modal-info">
            <div class="modal-detail">
              <div class="modal-detail-label">Описание</div>
              <div class="modal-description">
                {{ artwork && artwork.description ? artwork.description : 'Нет описания' }}
              </div>
            </div>

            <div class="modal-detail">
              <div class="modal-detail-label">Детали</div>
              <div class="detail-row">
                <span>Техника:</span> 
                <span>{{ artwork && artwork.group ? artwork.group : '—' }}</span>
              </div>
              <div class="detail-row">
                <span>Год:</span> 
                <span>{{ artwork && artwork.year ? artwork.year : '—' }}</span>
              </div>
              <div v-if="artwork && artwork.collection" class="detail-row">
                <span>Коллекция:</span> 
                <span>{{ artwork.collection }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="modal-footer">
        <button class="btn btn-primary" @click="close">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArtworkModal',
  props: {
    isOpen: Boolean,
    artwork: Object
  },
  methods: {
    close() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.9) 0%, rgba(10, 10, 10, 0.95) 100%);
  z-index: 1000;
  padding: 20px;
  overflow-y: auto;
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
}

.modal-content {
  background: var(--gray-900);
  border-radius: 16px;
  max-width: 900px;
  width: 100%;
  max-height: 90vh;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7);
  animation: fadeInUp 0.5s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  padding: 1.5rem;
  border-bottom: 1px solid var(--gray-800);
  position: relative;
}

.modal-title {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: white;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
}

.modal-close {
  background: none;
  border: none;
  color: var(--gray-400);
  font-size: 1.8rem;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0.5rem;
  border-radius: 50%;
}

.modal-close:hover {
  color: white;
  background: rgba(255, 255, 255, 0.05);
  transform: scale(1.1);
}

.modal-body {
  padding: 1.5rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.modal-layout {
  display: flex;
  gap: 2rem;
  height: 100%;
}

.modal-image-container {
  flex: 0 0 320px;
  position: relative;
}

.image-wrapper {
  position: relative;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  transition: transform 0.4s ease;
}

.image-wrapper:hover {
  transform: scale(1.02);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.6);
}

.modal-image {
  width: 100%;
  height: auto;
  border-radius: 12px;
  object-fit: cover;
  display: block;
  transition: transform 0.5s ease;
}

.image-wrapper:hover .modal-image {
  transform: scale(1.03);
}

.image-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 12px;
  background: radial-gradient(circle, rgba(30, 124, 255, 0.2) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.4s ease;
  pointer-events: none;
  z-index: -1;
}

.image-wrapper:hover .image-glow {
  opacity: 1;
}

.modal-image-placeholder {
  width: 100%;
  height: 320px;
  background: var(--gray-800);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gray-400);
  font-style: italic;
}

.modal-info {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
}

.modal-detail {
  padding: 1.2rem;
  background: var(--gray-800);
  border-radius: 8px;
  border-left: 3px solid var(--accent-color);
  transition: transform 0.3s ease;
}

.modal-detail:hover {
  transform: translateX(4px);
}

.modal-detail-label {
  font-weight: 700;
  margin-bottom: 0.8rem;
  color: var(--accent-color);
  font-size: 1.1rem;
  letter-spacing: -0.5px;
}

.modal-description {
  margin-bottom: 1rem;
  line-height: 1.6;
  color: #e0e0ff;
  font-size: 1.05rem;
}

.detail-row {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.detail-row span:first-child {
  font-weight: 600;
  color: white;
  min-width: 80px;
}

.detail-row span:last-child {
  color: var(--gray-300);
}

.modal-footer {
  padding: 1.5rem;
  text-align: right;
  border-top: 1px solid var(--gray-800);
  background: rgba(10, 10, 10, 0.3);
}

.btn {
  display: inline-block;
  padding: 0.85rem 1.8rem;
  border-radius: 50px;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.btn-primary {
  background: linear-gradient(135deg, var(--accent-color), #1a6cd4);
  color: var(--primary-color);
}

.btn-primary:hover {
  background: linear-gradient(135deg, #1a6cd4, #165cbf);
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(30, 124, 255, 0.4);
}

/* Адаптив */
@media (max-width: 768px) {
  .modal-layout {
    flex-direction: column;
  }

  .modal-image-container {
    flex: none;
  }

  .modal-image {
    height: 280px;
    object-fit: cover;
  }

  .modal-info {
    gap: 1rem;
  }

  .modal-detail {
    padding: 1rem;
  }

  .modal-title {
    font-size: 1.4rem;
  }
}

@media (max-width: 480px) {
  .modal-content {
    max-width: 95%;
  }

  .modal-image {
    height: 240px;
  }

  .modal-detail-label {
    font-size: 1rem;
  }
}
</style>