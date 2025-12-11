<template>
  <div class="min-h-screen bg-black">
    <!-- Transparent Header for Hero Section -->
    <header 
      v-if="isHeroVisible"
      class="fixed top-0 left-0 right-0 bg-transparent z-50 transition-all duration-300"
    >
      <nav class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-center">
          <div class="flex space-x-8">
            <a 
              v-for="link in navLinks" 
              :key="link.id"
              :href="`#${link.id}`"
              @click.prevent="scrollTo(link.id)"
              class="text-white hover:text-green-400 transition-all duration-300 hover:scale-105 font-medium drop-shadow-lg"
            >
              {{ link.label }}
            </a>
          </div>
        </div>
      </nav>
    </header>

    <!-- Dark Header for Other Sections -->
    <header 
      v-if="!isHeroVisible"
      class="fixed top-0 left-0 right-0 bg-black/95 backdrop-blur-md border-b border-green-800/50 z-50 shadow-lg transition-all duration-300"
    >
      <nav class="container mx-auto px-6 py-4">
        <div class="flex items-center justify-center">
          <div class="flex space-x-8">
            <a 
              v-for="link in navLinks" 
              :key="link.id"
              :href="`#${link.id}`"
              @click.prevent="scrollTo(link.id)"
              class="text-green-400 hover:text-white transition-all duration-300 hover:scale-105 font-medium"
            >
              {{ link.label }}
            </a>
          </div>
        </div>
      </nav>
    </header>

    <!-- Slide 1: Hero Section -->
    <section id="home" class="min-h-screen flex items-center justify-end pt-20 relative bg-contain bg-center" style="background-image: url('./main2.jpg')">
      <div class="absolute inset-0 bg-black/40"></div>
      <div class="container mx-48 px-6 max-w-4xl relative z-10 text-right animate-fade-in flex flex-col items-end">
        <h1 class="text-5xl md:text-7xl font-bold text-white mb-6 tracking-tight drop-shadow-lg">
          CTF Competition
        </h1>
        <p class="text-xl md:text-2xl text-white mb-12 font-light leading-relaxed drop-shadow-md">
          Capture The Flag соревнование по кибербезопасности.<br>
          Проверьте свои навыки и соревнуйтесь с лучшими специалистами.
        </p>
        <button
          @click="scrollTo('register')"
          class="bg-green-500 text-black px-12 py-4 text-lg font-semibold hover:bg-green-400 transition-all duration-300 rounded-full shadow-lg hover:shadow-green-500/50 hover:scale-105 transform"
        >
          Участвовать
        </button>
      </div>
    </section>

    <!-- Slide 2: Date & Time Info -->
    <section id="info" class="min-h-screen flex items-center justify-center bg-black py-20">
      <div class="container mx-auto px-6 max-w-6xl">
        <h2 class="text-4xl md:text-5xl font-light text-white mb-16 text-center animate-fade-in">
          Информация о соревновании
        </h2>
        
        <div class="grid md:grid-cols-3 gap-8 mb-16">
          <!-- Date Block -->
          <div class="bg-gradient-to-br from-black to-green-950/70 border border-green-800/50 p-8 text-center rounded-2xl shadow-2xl hover:shadow-green-500/20 transition-all duration-300 hover:-translate-y-2 transform hover:border-green-500/50">
            <div class="text-sm uppercase tracking-wider text-green-400 mb-4">Дата проведения</div>
            <div class="text-3xl font-light text-white">{{ competitionDate }}</div>
          </div>

          <!-- Time Block -->
          <div class="bg-gradient-to-br from-black to-green-950/70 border border-green-800/50 p-8 text-center rounded-2xl shadow-2xl hover:shadow-green-500/20 transition-all duration-300 hover:-translate-y-2 transform hover:border-green-500/50">
            <div class="text-sm uppercase tracking-wider text-green-400 mb-4">Время</div>
            <div class="text-3xl font-light text-white">{{ competitionTime }}</div>
          </div>

          <!-- Format Block -->
          <div class="bg-gradient-to-br from-black to-green-950/70 border border-green-800/50 p-8 text-center rounded-2xl shadow-2xl hover:shadow-green-500/20 transition-all duration-300 hover:-translate-y-2 transform hover:border-green-500/50">
            <div class="text-sm uppercase tracking-wider text-green-400 mb-4">Формат</div>
            <div class="text-3xl font-light text-white">{{ competitionFormat }}</div>
          </div>
        </div>

        <!-- Countdown Timer -->
        <div class="bg-gradient-to-br from-black to-green-950/70 border border-green-800/50 p-12 text-center rounded-2xl shadow-2xl">
          <div class="text-sm uppercase tracking-wider text-green-400 mb-6">До начала соревнования</div>
          <div class="grid grid-cols-4 gap-6 max-w-2xl mx-auto">
            <div 
              v-for="(value, key) in countdown" 
              :key="key" 
              class="border border-green-800/50 p-6 rounded-xl shadow-lg hover:shadow-green-500/30 transition-all duration-300 hover:scale-105 transform bg-green-950 hover:border-green-500/50"
            >
              <div class="text-4xl md:text-5xl font-light text-white mb-2">{{ String(value).padStart(2, '0') }}</div>
              <div class="text-xs uppercase tracking-wider text-green-400">{{ getCountdownLabel(key) }}</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 3: Categories & Details -->
    <section id="details" class="min-h-screen flex items-center justify-center bg-black py-20">
      <div class="container mx-auto px-6 max-w-4xl">
        <h2 class="text-4xl md:text-5xl font-light text-white mb-16 text-center animate-fade-in">
          Детали соревнования
        </h2>

        <div class="space-y-12">
          <!-- Categories -->
          <div class="border-b border-green-800/50 pb-12">
            <h3 class="text-2xl font-light text-white mb-8">Категории заданий</h3>
            <div class="grid md:grid-cols-2 gap-4">
              <div 
                v-for="(category, index) in categories" 
                :key="category"
                class="border border-green-800/50 p-6 text-green-300 rounded-xl shadow-lg hover:shadow-green-500/20 transition-all duration-300 hover:-translate-y-1 transform bg-gradient-to-br from-black to-green-950/70 hover:border-green-500/50"
                :style="{ animationDelay: `${index * 0.1}s` }"
              >
                {{ category }}
              </div>
            </div>
          </div>

          <!-- Prizes -->
          <div class="border-b border-green-800/50 pb-12">
            <h3 class="text-2xl font-light text-white mb-8">Призы</h3>
            <div class="grid md:grid-cols-3 gap-6">
              <div 
                v-for="(prize, index) in prizesList" 
                :key="index"
                class="bg-gradient-to-br from-black to-green-950 border border-green-800/50 p-8 rounded-2xl shadow-xl hover:shadow-green-500/20 transition-all duration-300 hover:-translate-y-2 transform hover:border-green-500/50"
              >
                <div class="text-4xl font-bold text-green-400 mb-3">{{ prize.place }}</div>
                <div class="text-xl font-semibold text-white mb-2">{{ prize.title }}</div>
                <div class="text-green-300">{{ prize.description }}</div>
              </div>
            </div>
          </div>

          <!-- Description -->
          <div>
            <h3 class="text-2xl font-light text-white mb-4">О соревновании</h3>
            <p class="text-green-200 text-lg leading-relaxed">
              {{ competitionDescription }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Slide 4: Registration Form -->
    <section id="register" class="min-h-screen flex items-center justify-center bg-black py-20">
      <div class="container mx-auto px-6 max-w-2xl">
        <h2 class="text-4xl md:text-5xl font-light text-white mb-12 text-center animate-fade-in">
          Регистрация
        </h2>

        <form @submit.prevent="submitRegistration" class="bg-gradient-to-br from-black to-green-950/50 border border-green-800/50 p-12 space-y-6 rounded-2xl shadow-2xl">
          <div>
            <label class="block text-sm uppercase tracking-wider text-green-400 mb-3" for="name">
              Имя и Фамилия
            </label>
            <input
              id="name"
              v-model="form.name"
              type="text"
              required
              class="w-full px-4 py-3 border border-green-800/50 bg-black text-white placeholder-green-300 focus:outline-none focus:border-green-500 focus:ring-2 focus:ring-green-500/50 transition-all duration-300 rounded-lg shadow-lg hover:shadow-green-500/20"
              placeholder="Иван Иванов"
            />
          </div>

          <div>
            <label class="block text-sm uppercase tracking-wider text-green-400 mb-3" for="email">
              Email
            </label>
            <input
              id="email"
              v-model="form.email"
              type="email"
              required
              class="w-full px-4 py-3 border border-green-800/50 bg-black text-white placeholder-green-300 focus:outline-none focus:border-green-500 focus:ring-2 focus:ring-green-500/50 transition-all duration-300 rounded-lg shadow-lg hover:shadow-green-500/20"
              placeholder="ivan@example.com"
            />
          </div>

          <div>
            <label class="block text-sm uppercase tracking-wider text-green-400 mb-3" for="experience">
              Уровень опыта
            </label>
            <select
              id="experience"
              v-model="form.experience"
              required
              class="w-full px-4 py-3 border border-green-800/50 bg-black text-white focus:outline-none focus:border-green-500 focus:ring-2 focus:ring-green-500/50 transition-all duration-300 rounded-lg shadow-lg hover:shadow-green-500/20"
            >
              <option value="" disabled class="bg-green-900/50">Выберите уровень</option>
              <option value="beginner" class="bg-green-900/50">Начинающий</option>
              <option value="intermediate" class="bg-green-900/50">Средний</option>
              <option value="advanced" class="bg-green-900/50">Продвинутый</option>
            </select>
          </div>

          <div>
            <label class="block text-sm uppercase tracking-wider text-green-400 mb-3" for="message">
              Дополнительная информация
            </label>
            <textarea
              id="message"
              v-model="form.message"
              rows="4"
              class="w-full px-4 py-3 border border-green-800/50 bg-black text-white placeholder-green-300 focus:outline-none focus:border-green-500 focus:ring-2 focus:ring-green-500/50 transition-all duration-300 resize-none rounded-lg shadow-lg hover:shadow-green-500/20"
              placeholder="Расскажите о себе или задайте вопросы..."
            ></textarea>
          </div>

          <button
            type="submit"
            :disabled="loading"
            class="w-full bg-gradient-to-r from-green-800 to-green-950 text-white py-4 px-6 font-semibold hover:from-green-500 hover:to-green-700 transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed rounded-full shadow-lg hover:shadow-green-500/50 hover:scale-105 transform"
          >
            <span v-if="!loading">Зарегистрироваться</span>
            <span v-else>Отправка...</span>
          </button>

          <div v-if="message" :class="messageType === 'success' ? 'text-green-400' : 'text-red-400'" class="text-center text-sm">
            {{ message }}
          </div>
        </form>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-black border-t border-green-800/50 py-8">
      <div class="container mx-auto px-6 text-center text-green-600 text-sm">
        © 2025 CTF Competition. Все права защищены.
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted, onUnmounted } from 'vue'

const competitionDate = '13 декабря 2025'
const competitionTime = '10:00 - 18:00 МСК'
const competitionFormat = 'Онлайн'
const categories = [
  'Web Security',
  'Cryptography',
  'Reverse Engineering',
  'Forensics',
  'PWN'
]
const prizesList = [
  { place: '1', title: 'Первое место', description: 'Денежный приз 50,000₽ и сертификат победителя' },
  { place: '2', title: 'Второе место', description: 'Денежный приз 30,000₽ и сертификат призера' },
  { place: '3', title: 'Третье место', description: 'Денежный приз 20,000₽ и сертификат призера' }
]

const competitionDescription = 'Присоединяйтесь к нашему CTF соревнованию и продемонстрируйте свои навыки в области кибербезопасности. Соревнование включает различные категории заданий, от веб-безопасности до криптографии и реверс-инжиниринга. Победители получат ценные призы и признание в сообществе.'

const navLinks = [
  { id: 'home', label: 'Главная' },
  { id: 'info', label: 'Информация' },
  { id: 'details', label: 'Детали' },
  { id: 'register', label: 'Регистрация' }
]

const form = reactive({
  name: '',
  email: '',
  experience: '',
  message: ''
})

const isHeroVisible = ref(true)

const loading = ref(false)
const message = ref('')
const messageType = ref('')

// Countdown timer
const countdown = reactive({
  days: 0,
  hours: 0,
  minutes: 0,
  seconds: 0
})

let countdownInterval = null

const updateCountdown = () => {
  const targetDate = new Date('2025-12-13T10:00:00')
  const now = new Date()
  const diff = targetDate - now

  if (diff > 0) {
    countdown.days = Math.floor(diff / (1000 * 60 * 60 * 24))
    countdown.hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))
    countdown.minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60))
    countdown.seconds = Math.floor((diff % (1000 * 60)) / 1000)
  } else {
    countdown.days = 0
    countdown.hours = 0
    countdown.minutes = 0
    countdown.seconds = 0
  }
}

const getCountdownLabel = (key) => {
  const labels = {
    days: 'Дней',
    hours: 'Часов',
    minutes: 'Минут',
    seconds: 'Секунд'
  }
  return labels[key] || ''
}

const scrollTo = (id) => {
  const element = document.getElementById(id)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

const submitRegistration = async () => {
  loading.value = true
  message.value = ''
  
  try {
    const payload = {
      name: form.name,
      email: form.email,
      experience: form.experience,
      extra: form.message,
    }

    const response = await fetch('/api/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload)
    })

    const text = await response.text()
    let data = {}
    
    if (text) {
      try {
        data = JSON.parse(text)
      } catch (e) {
        data = { error: 'Ошибка обработки ответа сервера' }
      }
    }

    if (response.ok) {
      message.value = 'Регистрация успешна! Проверьте вашу почту для подтверждения.'
      messageType.value = 'success'
      Object.keys(form).forEach(key => {
        form[key] = ''
      })
    } else {
      message.value = data.error || `Ошибка сервера (${response.status}). Попробуйте позже.`
      messageType.value = 'error'
    }
  } catch (error) {
    message.value = 'Ошибка соединения с сервером. Убедитесь, что сервер запущен.'
    messageType.value = 'error'
  } finally {
    loading.value = false
  }
}

const handleScroll = () => {
  const heroSection = document.getElementById('home')
  if (heroSection) {
    const rect = heroSection.getBoundingClientRect()
    // Показываем прозрачный header только если первый слайд полностью виден
    // Темный header появляется когда первый слайд скроллится вверх
    isHeroVisible.value = rect.bottom > window.innerHeight * 0.5
  }
}

onMounted(() => {
  updateCountdown()
  countdownInterval = setInterval(updateCountdown, 1000)
  window.addEventListener('scroll', handleScroll)
  handleScroll() // Initial check
})

onUnmounted(() => {
  if (countdownInterval) {
    clearInterval(countdownInterval)
  }
  window.removeEventListener('scroll', handleScroll)
})
</script>

