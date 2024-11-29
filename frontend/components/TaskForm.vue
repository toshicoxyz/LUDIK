<template>
    <div class="bg-white p-6 rounded shadow-md max-w-md mx-auto">
        <h2 class="text-xl font-semibold text-gray-600 mb-4">
            {{ isEditing ? 'Editar Tarea' : 'Nueva Tarea' }}
        </h2>
        <form @submit.prevent="handleSubmit">
            <div class="mb-4">
                <label class="block text-gray-600 mb-1">Titulo</label>
                <input v-model="localTask.title" type="text" class="w-full border rounded px-3 py-2"
                    placeholder="Titulo de la Tarea" required />
            </div>
            <div class="mb-4">
                <label class="block text-gray-600 mb-1">Descripción</label>
                <textarea class="w-full border rounded px-3 py-2" rows="3" v-model="localTask.description"
                    placeholder="Descripcion de la tarea"></textarea>
            </div>
            <div class="mb-4">
                <label class="block text-gray-600 mb-1">Estado</label>
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
import DOMPurify from 'dompurify'; // Importar DOMPurify para sanitizar entradas

const props = defineProps({
    newTask: { type: Object, required: true },
    isEditing: { type: Boolean, required: true },
});

const emit = defineEmits(['create-task', 'update-task']);

// Sincroniza la tarea local con las props
const localTask = ref({ ...props.newTask });

// Reloj para detectar cambios en newTask y sincronizarlos con localTask
watch(
    () => props.newTask,
    (newVal) => {
        localTask.value = { ...newVal };
    },
    { immediate: true }
);

// Función para sanitizar los datos antes de enviarlos
const sanitizeInput = (input: string) => {
    return DOMPurify.sanitize(input); // Sanitiza el input para prevenir XSS
};

const handleSubmit = () => {
    // Sanitizar los campos antes de emitir los datos
    const sanitizedTitle = sanitizeInput(localTask.value.title);
    const sanitizedDescription = sanitizeInput(localTask.value.description);

    // Actualizar el objeto localTask con los valores sanitizados
    localTask.value.title = sanitizedTitle;
    localTask.value.description = sanitizedDescription;

    if (props.isEditing) {
        emit('update-task', localTask.value); // Emitimos la tarea actualizada
    } else {
        emit('create-task', localTask.value); // Emitimos la nueva tarea
    }
};
</script>
