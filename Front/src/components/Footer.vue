<script>
export default {
  data() {
    return {
      authorInfo: {},
      currentYear: new Date().getFullYear()
    };
  },
  async beforeMount() {
    await this.get_author_profile();
  },
  methods: {
    async get_author_profile() {
      try {
        const response = await fetch('http://127.0.0.1:8000/author/profile/', {
          method: 'GET'
        });
        if (response.ok) {
          this.authorInfo = await response.json();
        }
      } catch (error) {
        console.error('Ошибка загрузки профиля:', error);
      }
    }
  }
};
</script>

<template>
  <footer>
    <div class="container">
      <div class="footer-content">
        <div class="footer-logo">WZERTIS</div>
        <div class="footer-social">
          <a
            v-if="authorInfo.tg"
            :href="authorInfo.tg"
            target="_blank"
            rel="noopener noreferrer"
            class="social-link"
            aria-label="Telegram"
          >
            <svg 
              width="18" 
              height="18" 
              viewBox="0 0 24 24" 
              fill="currentColor" 
              xmlns="http://www.w3.org/2000/svg"
              aria-hidden="true"
            >
              <path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>
            </svg>
          </a>
          <a
            v-if="authorInfo.vk"
            :href="authorInfo.vk"
            target="_blank"
            rel="noopener noreferrer"
            class="social-link"
            aria-label="VK"
          >
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                <svg role="img" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><title>VK</title><path d="m9.489.004.729-.003h3.564l.73.003.914.01.433.007.418.011.403.014.388.016.374.021.36.025.345.03.333.033c1.74.196 2.933.616 3.833 1.516.9.9 1.32 2.092 1.516 3.833l.034.333.029.346.025.36.02.373.025.588.012.41.013.644.009.915.004.98-.001 3.313-.003.73-.01.914-.007.433-.011.418-.014.403-.016.388-.021.374-.025.36-.03.345-.033.333c-.196 1.74-.616 2.933-1.516 3.833-.9.9-2.092 1.32-3.833 1.516l-.333.034-.346.029-.36.025-.373.02-.588.025-.41.012-.644.013-.915.009-.98.004-3.313-.001-.73-.003-.914-.01-.433-.007-.418-.011-.403-.014-.388-.016-.374-.021-.36-.025-.345-.03-.333-.033c-1.74-.196-2.933-.616-3.833-1.516-.9-.9-1.32-2.092-1.516-3.833l-.034-.333-.029-.346-.025-.36-.02-.373-.025-.588-.012-.41-.013-.644-.009-.915-.004-.98.001-3.313.003-.73.01-.914.007-.433.011-.418.014-.403.016-.388.021-.374.025-.36.03-.345.033-.333c.196-1.74.616-2.933 1.516-3.833.9-.9 2.092-1.32 3.833-1.516l.333-.034.346-.029.36-.025.373-.02.588-.025.41-.012.644-.013.915-.009ZM6.79 7.3H4.05c.13 6.24 3.25 9.99 8.72 9.99h.31v-3.57c2.01.2 3.53 1.67 4.14 3.57h2.84c-.78-2.84-2.83-4.41-4.11-5.01 1.28-.74 3.08-2.54 3.51-4.98h-2.58c-.56 1.98-2.22 3.78-3.8 3.95V7.3H10.5v6.92c-1.6-.4-3.62-2.34-3.71-6.92Z"/></svg>
            </svg>
          </a>
          <a
            v-if="authorInfo.ig"
            :href="authorInfo.ig"
            target="_blank"
            rel="noopener noreferrer"
            class="social-link"
            aria-label="Instagram"
          >
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
              <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
              <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
            </svg>
          </a>
        </div>
      </div>
      <div class="footer-copyright">
        &copy; {{ currentYear }} WZERTIS. Все права защищены.
      </div>
    </div>
  </footer>
</template>

<style scoped>
footer {
  background: linear-gradient(to top, var(--primary-color), #0f0f0f);
  border-top: 1px solid var(--gray-800);
  padding: 2.5rem 20px 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

footer::before {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 60px;
  height: 2px;
  background: var(--accent-color);
  opacity: 0.2;
}

.container {
  position: relative;
  z-index: 2;
}

.footer-content {
  display: flex;
  flex-direction: column;
  gap: 1.2rem;
  align-items: center;
}

@media (min-width: 768px) {
  .footer-content {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
}

.footer-logo {
  font-size: 1.6rem;
  font-weight: 800;
  letter-spacing: -0.5px;
  background: linear-gradient(to right, #ffffff, #a0a0ff);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.footer-social {
  display: flex;
  gap: 1.2rem;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  color: var(--gray-400);
  text-decoration: none;
  transition: all 0.3s ease;
}

.social-link:hover {
  color: var(--accent-color);
  transform: translateY(-2px);
}

.footer-copyright {
  margin-top: 1.5rem;
  color: var(--gray-500);
  font-size: 0.85rem;
  letter-spacing: 0.5px;
}
</style>