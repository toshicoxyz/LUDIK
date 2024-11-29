<template>
    <div>
        <h2 class="text-2xl font-semibold text-gray-600 mb-4">Lista de Tareas</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            <div v-for="task in tasks" :key="task.id" class="bg-white p-4 rounded shadow-md">
                <h3 class="text-lg font-bold text-gray-700">{{ task.title }}</h3>
                <p class="text-gray-600 mb-4">{{ task.description }}</p>
                <span :class="getStatusBadgeClass(task.status)"
                    class="inline-block px-3 py-1 rounded text-sm font-semibold">
                    {{ task.status }}
                </span>
                <div class="flex justify-between mt-4">
                    <button class="text-blue-500 hover:underline" @click="$emit('start-editing', task)">
                        Editar
                    </button>
                    <button class="text-red-500 hover:underline" @click="$emit('delete-task', task.id)">
                        Eliminar
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
const props = defineProps({
    tasks: { type: Array, required: true },
});

const getStatusBadgeClass = (status: string) => {
    switch (status) {
        case 'Pendiente':
            return 'bg-yellow-100 text-yellow-700';
        case 'En Proceso':
            return 'bg-blue-100 text-blue-700';
        case 'Completada':
            return 'bg-green-100 text-green-700';
        default:
            return 'bg-gray-100 text-gray-700';
    }
};
</script>
