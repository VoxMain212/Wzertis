<template>
  <section id="contact" class="contact-section">
    <div class="container">
      <h2 class="section-title">Связаться со мной</h2>
      <div class="contact-content">
        <div class="contact-info">
          <h3>Контактная информация</h3>
          <p>Я буду рада услышать от вас!...</p>
          <div class="contact-detail">
            <span class="contact-icon">✉️</span>
            <span>artist@vista-artista.com</span>
          </div>
          <div class="contact-detail">
            <span class="contact-icon">📷</span>
            <span>@vista_artista</span>
          </div>
          <div class="contact-detail">
            <span class="contact-icon">🐦</span>
            <span>@vista_artista</span>
          </div>
          <div class="mt-8">
            <h4>Информация о заказах</h4>
            <p style="font-size: 0.9rem; color: var(--gray-400);">
              Индивидуальные заказы доступны по запросу...
            </p>
          </div>
        </div>
        <div class="contact-form">
          <form @submit.prevent="submitForm">
            <div class="form-group">
              <label for="name">Имя</label>
              <input type="text" id="name" v-model="formData.name" class="form-control" placeholder="Ваше имя" />
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input type="email" id="email" v-model="formData.email" class="form-control" placeholder="your@email.com" />
            </div>
            <div class="form-group">
              <label for="subject">Тема</label>
              <input type="text" id="subject" v-model="formData.subject" class="form-control" placeholder="О чем это?" />
            </div>
            <div class="form-group">
              <label for="message">Сообщение</label>
              <textarea id="message" v-model="formData.message" class="form-control" rows="5" placeholder="Расскажите мне о вашем проекте..."></textarea>
            </div>
            <button type="submit" class="submit-btn">Отправить сообщение</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const emit = defineEmits(['form-submitted']);

const formData = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
});

const submitForm = () => {
  emit('form-submitted');
  formData.value = { name: '', email: '', subject: '', message: '' };
};
</script>

<style scoped>
/* Скопировать стили contact-section */
.contact-section {
  padding: 60px 20px;
}

.contact-content {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

@media (min-width: 768px) {
  .contact-content {
    flex-direction: row;
  }
}

.contact-info {
  flex: 0 0 300px;
}

.contact-info h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.contact-info p {
  margin-bottom: 1.5rem;
  color: var(--gray-400);
}

.contact-detail {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.contact-icon {
  margin-right: 0.5rem;
  color: var(--accent-color);
}

.contact-form {
  flex: 1;
  background-color: var(--gray-800);
  padding: 2rem;
  border-radius: 8px;
}

.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
}

.form-control {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid var(--gray-600);
  border-radius: 4px;
  background-color: var(--gray-700);
  color: var(--text-color);
  transition: border-color 0.3s ease;
}

.form-control:focus {
  outline: none;
  border-color: var(--accent-color);
}

.form-control::placeholder {
  color: var(--gray-400);
}

.submit-btn {
  width: 100%;
  padding: 0.75rem;
  background-color: var(--accent-color);
  color: var(--primary-color);
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.submit-btn:hover {
  background-color: #1a6cd4;
}

@media (max-width: 768px) {
  .contact-content {
    flex-direction: column;
  }

  .contact-info {
    flex: 0 0 100%;
  }
}
</style>