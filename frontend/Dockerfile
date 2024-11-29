# Usa una imagen basada en Alpine
FROM node:18-alpine AS base

RUN npm install -g pnpm

# Fase de dependencias
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json package-lock.json ./
RUN pnpm install

# Fase de construcción
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN pnpm run build

# Fase de ejecución (producción)
FROM base AS runner
WORKDIR /app
COPY --from=builder /app ./
USER node
EXPOSE 3000
CMD ["pnpm", "run", "preview"]
