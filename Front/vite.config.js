import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      '/api': {
        target: 'http://backend:8000', // ← имя сервиса из docker-compose
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    },
    host: '0.0.0.0',
    port: 5173,
    watch: {
      usePolling: true,   // ← для Docker на Windows/macOS
      interval: 1000
    }
  }
})