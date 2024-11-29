FROM node:18-alpine AS base

# Fase de dependencias
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci  # Instala las dependencias

# Fase de construcción
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules 
COPY . .  
RUN npm run build  # Ejecuta el build para generar los archivos de producción

# Comando de depuración: Verifica si el archivo nitro.json está presente
RUN ls -l /app/.output/

# Fase de ejecución (producción)
FROM base AS runner
WORKDIR /app
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nitro
COPY --from=builder /app .
USER nitro
EXPOSE 3000
ENV PORT 3000

# Verifica si el archivo nitro.json está presente en la fase de ejecución
RUN ls -l /app/.output/

CMD ["npm", "run", "preview"]  # Ejecuta nuxt preview
