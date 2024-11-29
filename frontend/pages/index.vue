<template>
    <div class="min-h-screen bg-gray-50 p-6">
        <header class="mb-6">
            <h1 class="text-3xl font-bold text-center text-gray-700">Administrador de Tareas</h1>
        </header>

        <!-- Indicador de Carga -->
        <div v-if="loading" class="text-center text-blue-500">
            <span class="loader"></span> Cargando tareas...
        </div>

        <!-- Formulario -->
        <FormComponent v-if="!loading" :new-task="newTask" :is-editing="isEditing" @create-task="createTask"
            @update-task="updateTask" />

        <!-- Lista de Tareas -->
        <ListComponent v-if="!loading" :tasks="tasks" @start-editing="startEditing" @delete-task="deleteTask" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted, defineAsyncComponent } from 'vue';
import axios from 'axios';

const tasks = ref([]);
const apiBaseUrl = 'http://localhost:8000/api/tasks';
const newTask = ref({ title: '', description: '', status: 'Pendiente' });
const isEditing = ref(false);
const editingTaskId = ref<number | null>(null);
const loading = ref(true);

// Lazy load components
const FormComponent = defineAsyncComponent(() =>
    import('@/components/TaskForm.vue')
);
const ListComponent = defineAsyncComponent(() =>
    import('@/components/TaskList.vue')
);

const fetchTasks = async () => {
    try {
        loading.value = true;
        const { data } = await axios.get(`${apiBaseUrl}/`);
        tasks.value = data;
    } catch (error) {
        console.error('Error fetching tasks:', error);
    } finally {
        loading.value = false;
    }
};

const createTask = async (task: typeof newTask.value) => {
    try {
        await axios.post(`${apiBaseUrl}/`, task);
        fetchTasks();
    } catch (error) {
        console.error('Error creating task:', error);
    }
};

const startEditing = (task: typeof newTask.value) => {
    if (!task.id || !task.title || !task.description || !task.status) {
        console.error('Invalid task object:', task);
        return;
    }

    isEditing.value = true;
    editingTaskId.value = task.id;
    newTask.value = { ...task }; // Clonamos la tarea seleccionada
};


const updateTask = async (changeTask) => {
    if (!editingTaskId.value) {
        console.error('No task selected for editing');
        return;
    }

    console.log('Updating task:', newTask.value);

    try {
        await axios.put(
            `${apiBaseUrl}/${editingTaskId.value}`,
            changeTask
        );

        isEditing.value = false;
        editingTaskId.value = null;
        newTask.value = { title: '', description: '', status: 'Pendiente' }; // Limpia el formulario
        fetchTasks();
    } catch (error) {
        console.error('Error updating task:', error);
    }
};

const deleteTask = async (taskId: number) => {
    try {
        await axios.delete(`${apiBaseUrl}/${taskId}`);
        fetchTasks();
    } catch (error) {
        console.error('Error deleting task:', error);
    }
};

onMounted(fetchTasks);
</script>

<style>
/* Indicador de carga */
.loader {
    border: 4px solid #f3f3f3;
    border-top: 4px solid #3498db;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>
