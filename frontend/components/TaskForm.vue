<template>
    <div class="bg-white p-6 rounded shadow-md max-w-md mx-auto">
        <h2 class="text-xl font-semibold text-gray-600 mb-4">
            {{ isEditing ? 'Edit Task' : 'New Task' }}
        </h2>
        <form @submit.prevent="handleSubmit">
            <div class="mb-4">
                <label class="block text-gray-600 mb-1">Title</label>
                <input v-model="localTask.title" type="text" class="w-full border rounded px-3 py-2"
                    placeholder="Task title" required />
            </div>
            <div class="mb-4">
                <label class="block text-gray-600 mb-1">Description</label>
                <textarea class="w-full border rounded px-3 py-2" rows="3" v-model="localTask.description"
                    placeholder="Task description"></textarea>
            </div>
            <div class="mb-4">
                <label class="block text-gray-600 mb-1">Status</label>
                <select v-model="localTask.status" class="w-full border rounded px-3 py-2">
                    <option value="Pendiente">Pendiente</option>
                    <option value="En Proceso">En Proceso</option>
                    <option value="Completada">Completada</option>
                </select>
            </div>
            <button type="submit" class="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition">
                {{ isEditing ? 'Update Task' : 'Create Task' }}
            </button>
        </form>
    </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';

const props = defineProps({
    newTask: { type: Object, required: true },
    isEditing: { type: Boolean, required: true },
});

const emit = defineEmits(['create-task', 'update-task']);

// Sincroniza la tarea local con las props
const localTask = ref({ ...props.newTask });

watch(
    () => props.newTask,
    (newVal) => {
        localTask.value = { ...newVal };
    },
    { immediate: true }
);

const handleSubmit = () => {
    if (props.isEditing) {
        emit('update-task', localTask.value); // Emitimos la tarea actualizada
    } else {
        emit('create-task', localTask.value);
    }
};
</script>
