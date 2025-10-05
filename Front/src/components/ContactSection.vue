<template>
  <section id="contact" class="contact-section">
    <div class="container">
      <h2 class="section-title">Связаться со мной</h2>
      <div class="contact-content">
        <!-- Контактная информация -->
        <div class="contact-info">
          <h3>Контактная информация</h3>
          <p>Я буду рада услышать от вас! Ответ обычно приходит в течение 24 часов.</p>

          <div class="contact-links">
            <a
              v-if="authorInfo.email"
              :href="'mailto:' + authorInfo.email"
              class="contact-link"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                <polyline points="22,6 12,13 2,6"></polyline>
              </svg>
              <span>{{ authorInfo.email }}</span>
            </a>

            <a
              v-if="authorInfo.ig"
              :href="authorInfo.ig"
              target="_blank"
              rel="noopener noreferrer"
              class="contact-link"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
              </svg>
              <span>Instagram</span>
            </a>

            <a
              v-if="authorInfo.vk"
              :href="authorInfo.vk"
              target="_blank"
              rel="noopener noreferrer"
              class="contact-link"
            >
              <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>VK</title><path d="m9.489.004.729-.003h3.564l.73.003.914.01.433.007.418.011.403.014.388.016.374.021.36.025.345.03.333.033c1.74.196 2.933.616 3.833 1.516.9.9 1.32 2.092 1.516 3.833l.034.333.029.346.025.36.02.373.025.588.012.41.013.644.009.915.004.98-.001 3.313-.003.73-.01.914-.007.433-.011.418-.014.403-.016.388-.021.374-.025.36-.03.345-.033.333c-.196 1.74-.616 2.933-1.516 3.833-.9.9-2.092 1.32-3.833 1.516l-.333.034-.346.029-.36.025-.373.02-.588.025-.41.012-.644.013-.915.009-.98.004-3.313-.001-.73-.003-.914-.01-.433-.007-.418-.011-.403-.014-.388-.016-.374-.021-.36-.025-.345-.03-.333-.033c-1.74-.196-2.933-.616-3.833-1.516-.9-.9-1.32-2.092-1.516-3.833l-.034-.333-.029-.346-.025-.36-.02-.373-.025-.588-.012-.41-.013-.644-.009-.915-.004-.98.001-3.313.003-.73.01-.914.007-.433.011-.418.014-.403.016-.388.021-.374.025-.36.03-.345.033-.333c.196-1.74.616-2.933 1.516-3.833.9-.9 2.092-1.32 3.833-1.516l.333-.034.346-.029.36-.025.373-.02.588-.025.41-.012.644-.013.915-.009ZM6.79 7.3H4.05c.13 6.24 3.25 9.99 8.72 9.99h.31v-3.57c2.01.2 3.53 1.67 4.14 3.57h2.84c-.78-2.84-2.83-4.41-4.11-5.01 1.28-.74 3.08-2.54 3.51-4.98h-2.58c-.56 1.98-2.22 3.78-3.8 3.95V7.3H10.5v6.92c-1.6-.4-3.62-2.34-3.71-6.92Z"/></svg>
              </svg>
              <span>VK</span>
            </a>
          </div>

          <div class="order-info">
            <h4>Информация о заказах</h4>
            <p>Индивидуальные заказы доступны по запросу. Расскажите о вашем проекте — и я пришлю коммерческое предложение.</p>
          </div>
        </div>

        <!-- Форма -->
        <div class="contact-form-wrapper">
          <div class="contact-form" :class="{ 'form-success': isSubmitted }">
            <div v-if="isSubmitting" class="form-overlay">
              <div class="spinner"></div>
            </div>

            <form v-if="!isSubmitted" @submit.prevent="submitForm">
              <div class="form-row">
                <div class="form-group">
                  <label for="name">Имя</label>
                  <input
                    type="text"
                    id="name"
                    v-model="formData.name"
                    class="form-control"
                    placeholder="Ваше имя"
                    required
                  />
                </div>
                <div class="form-group">
                  <label for="email">Email</label>
                  <input
                    type="email"
                    id="email"
                    v-model="formData.email"
                    class="form-control"
                    placeholder="your@email.com"
                    required
                  />
                </div>
              </div>

              <div class="form-group">
                <label for="subject">Тема</label>
                <input
                  type="text"
                  id="subject"
                  v-model="formData.theme"
                  class="form-control"
                  placeholder="О чём это?"
                  required
                />
              </div>

              <div class="form-group">
                <label for="message">Сообщение</label>
                <textarea
                  id="message"
                  v-model="formData.message"
                  class="form-control"
                  rows="5"
                  placeholder="Расскажите мне о вашем проекте..."
                  required
                ></textarea>
              </div>

              <button type="submit" class="submit-btn" :disabled="isSubmitting">
                {{ isSubmitting ? 'Отправка...' : 'Отправить сообщение' }}
              </button>
            </form>

            <div v-else class="form-success-content">
              <div class="success-icon">
                <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                  <polyline points="22,4 12,14.01 9,11.01"></polyline>
                </svg>
              </div>
              <h3>Сообщение отправлено!</h3>
              <p>Спасибо за обращение. Я свяжусь с вами в ближайшее время.</p>
              <button @click="resetForm" class="reset-btn">Отправить ещё</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  data() {
    return {
      authorInfo: {},
      formData: {
        name: '',
        email: '',
        theme: '',
        message: ''
      },
      isSubmitting: false,
      isSubmitted: false
    };
  },
  methods: {
    async get_author_profile() {
      try {
        const response = await fetch('http://127.0.0.1:8000/author/profile/');
        if (response.ok) {
          this.authorInfo = await response.json();
        }
      } catch (error) {
        console.error('Ошибка загрузки профиля:', error);
      }
    },
    async submitForm() {
      this.isSubmitting = true;
      try {
        const response = await fetch('http://127.0.0.1:8000/appeal/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.formData)
        });

        if (response.ok) {
          this.isSubmitted = true;
        } else {
          alert('Ошибка отправки. Попробуйте позже.');
        }
      } catch (error) {
        alert('Ошибка сети. Проверьте подключение.');
        console.error('Ошибка:', error);
      } finally {
        this.isSubmitting = false;
      }
    },
    resetForm() {
      this.formData = { name: '', email: '', theme: '', message: '' };
      this.isSubmitted = false;
    }
  },
  mounted() {
    this.get_author_profile();
  }
};
</script>

<style scoped>
.contact-section {
  padding: 100px 20px;
  background: linear-gradient(180deg, var(--primary-color) 0%, var(--gray-900) 100%);
  position: relative;
  overflow: hidden;
}

.contact-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 80% 20%, rgba(30, 124, 255, 0.05) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}

.container {
  position: relative;
  z-index: 2;
}

.section-title {
  text-align: center;
  font-size: 2.6rem;
  margin-bottom: 3rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  color: white;
}

.contact-content {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
}

@media (min-width: 768px) {
  .contact-content {
    flex-direction: row;
    gap: 3rem;
  }
}

/* Контактная информация */
.contact-info {
  flex: 0 0 320px;
}

.contact-info h3 {
  font-size: 1.6rem;
  margin-bottom: 1rem;
  color: white;
}

.contact-info p {
  margin-bottom: 1.8rem;
  color: var(--gray-400);
  line-height: 1.6;
}

.contact-links {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 2rem;
}

.contact-link {
  display: flex;
  align-items: center;
  gap: 12px;
  color: var(--text-color);
  text-decoration: none;
  padding: 0.6rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.contact-link:hover {
  background: rgba(30, 124, 255, 0.1);
  color: var(--accent-color);
  transform: translateX(4px);
}

.contact-link svg {
  flex-shrink: 0;
}

.order-info {
  background: var(--gray-800);
  padding: 1.5rem;
  border-radius: 12px;
  border-left: 3px solid var(--accent-color);
}

.order-info h4 {
  margin-bottom: 0.8rem;
  color: white;
}

.order-info p {
  margin-bottom: 0;
  font-size: 0.95rem;
  color: var(--gray-400);
}

/* Форма */
.contact-form-wrapper {
  flex: 1;
  max-width: 650px;
}

.contact-form {
  position: relative;
  background: var(--gray-800);
  padding: 2.5rem;
  border-radius: 16px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  transition: all 0.4s ease;
}

.contact-form.form-success {
  background: rgba(30, 124, 255, 0.1);
  border: 1px solid rgba(30, 124, 255, 0.3);
}

.form-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(10, 10, 10, 0.7);
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10;
}

.spinner {
  width: 32px;
  height: 32px;
  border: 3px solid rgba(255, 255, 255, 0.3);
  border-top: 3px solid var(--accent-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.form-row {
  display: flex;
  gap: 1rem;
  margin-bottom: 1rem;
}

.form-group {
  flex: 1;
  margin-bottom: 1.2rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: white;
  font-weight: 500;
}

.form-control {
  width: 100%;
  padding: 0.85rem;
  border: 1px solid var(--gray-600);
  border-radius: 8px;
  background-color: var(--gray-700);
  color: var(--text-color);
  transition: all 0.3s ease;
  font-size: 1rem;
}

.form-control:focus {
  outline: none;
  border-color: var(--accent-color);
  box-shadow: 0 0 0 3px rgba(30, 124, 255, 0.2);
}

.form-control::placeholder {
  color: var(--gray-400);
}

.submit-btn {
  width: 100%;
  padding: 0.9rem;
  background: linear-gradient(135deg, var(--accent-color), #1a6cd4);
  color: var(--primary-color);
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
  font-size: 1.05rem;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(30, 124, 255, 0.3);
}

.submit-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(30, 124, 255, 0.4);
}

.submit-btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
}

/* Успех */
.form-success-content {
  text-align: center;
  padding: 2rem 1rem;
}

.success-icon {
  color: var(--accent-color);
  margin-bottom: 1.5rem;
}

.form-success-content h3 {
  font-size: 1.8rem;
  margin-bottom: 1rem;
  color: white;
}

.form-success-content p {
  color: var(--gray-400);
  margin-bottom: 1.5rem;
  line-height: 1.6;
}

.reset-btn {
  background: var(--gray-700);
  color: var(--text-color);
  border: 1px solid var(--gray-600);
  padding: 0.6rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.reset-btn:hover {
  background: var(--gray-600);
  transform: translateY(-2px);
}

/* Адаптив */
@media (max-width: 768px) {
  .form-row {
    flex-direction: column;
    gap: 0;
  }

  .contact-info {
    flex: 0 0 100%;
  }

  .section-title {
    font-size: 2.2rem;
  }
}
</style>