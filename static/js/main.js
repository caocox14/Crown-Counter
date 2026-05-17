/* ============================================================
   main.js - El cerebro interactivo de PlantApp
   Corregido: Gestión de vista previa e identificación IA
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
    
    console.log("🌱 PlantApp: Sistema frontend iniciado.");

    // ============================================================
    // 1. GESTIÓN DE NAVEGACIÓN (CAMBIO DE PESTAÑAS)
    // ============================================================
    const btnDashboard = document.getElementById('btn-dashboard');
    const btnInfo = document.getElementById('btn-info');
    const sectionDashboard = document.getElementById('section-dashboard');
    const sectionInfo = document.getElementById('section-info');

    function showSection(sectionToShow, sectionToHide, activeBtn, inactiveBtn) {
        sectionToShow.classList.remove('hidden');
        sectionToHide.classList.add('hidden');
        activeBtn.classList.add('bg-white/20', 'text-white');
        activeBtn.classList.remove('text-white/80');
        inactiveBtn.classList.remove('bg-white/20', 'text-white');
        inactiveBtn.classList.add('text-white/80');
    }

    if(btnInfo && btnDashboard) {
        btnInfo.addEventListener('click', () => showSection(sectionInfo, sectionDashboard, btnInfo, btnDashboard));
        btnDashboard.addEventListener('click', () => showSection(sectionDashboard, sectionInfo, btnDashboard, btnInfo));
    }

    // ============================================================
    // 2. VISTA PREVIA Y CONTROL DE FORMULARIO (IA)
    // ============================================================
    const fileInput = document.getElementById('file-input'); 
    const dropZone = document.getElementById('drop-zone');
    const formIA = document.getElementById('upload-form');
    const btnAnalizar = document.getElementById('btn-analizar');

    if (fileInput && dropZone) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    // Ocultamos el texto e icono original
                    const promptText = dropZone.querySelector('.prompt-text'); 
                    if (promptText) promptText.classList.add('hidden');

                    // Buscamos si ya existe una preview para no duplicarla
                    let previewImg = dropZone.querySelector('.preview-img');
                    if (!previewImg) {
                        previewImg = document.createElement('img');
                        // 'z-0' para que quede detrás del input invisible y puedas cambiar la foto si quieres
                        previewImg.className = 'preview-img absolute inset-0 h-full w-full object-cover rounded-3xl p-1 animate-fade-in z-0';
                        dropZone.appendChild(previewImg);
                    }
                    previewImg.src = event.target.result;
                    
                    // Cambiamos el borde para dar feedback de que ya hay algo
                    dropZone.classList.remove('border-dashed');
                    dropZone.classList.add('border-solid', 'border-green-500');
                }
                reader.readAsDataURL(file);
            }
        });
    }

    if (formIA && btnAnalizar) {

    formIA.addEventListener('submit', async (e) => {
        btnAnalizar.disabled = true;
        // Mantenemos la altura para evitar que la página se mueva
        btnAnalizar.style.height = `${btnAnalizar.offsetHeight}px`; 
        btnAnalizar.innerHTML = `
            <div class="flex items-center justify-center gap-3">
                <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span class="text-sm">Analizando...</span>
            </div>`;
        await analizarimagen(e);
    });
}

    // ============================================================
    // 3. CONFIGURACIÓN DE LA GRÁFICA (Chart.js)
    // ============================================================
    const chartCanvas = document.getElementById('soilChart');
    if (chartCanvas) {
        const ctx = chartCanvas.getContext('2d');
        let gradient = ctx.createLinearGradient(0, 0, 0, 400);
        gradient.addColorStop(0, 'rgba(22, 163, 74, 0.4)');
        gradient.addColorStop(1, 'rgba(22, 163, 74, 0)');

        window.humidityChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['12:00', '12:05', '12:10', '12:15', '12:20', '12:25'],
                datasets: [{
                    label: 'Humedad %',
                    data: [50, 55, 48, 65, 62, 65],
                    borderColor: '#16a34a',
                    backgroundColor: gradient,
                    fill: true,
                    tension: 0.4,
                    borderWidth: 3,
                    pointRadius: 5,
                    pointBackgroundColor: '#fff',
                    pointBorderColor: '#16a34a'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: {
                    y: { beginAtZero: true, max: 100, ticks: { callback: v => v + '%' } },
                    x: { grid: { display: false } }
                }
            }
        });
    }

    // ============================================================
    // 4. ACTUALIZACIÓN DE DATOS (POLLING)
    // ============================================================
    async function fetchSensorData() {
        try {
            const simulatedData = {
                actual: 65 + Math.floor(Math.random() * 5),
                hora: new Date().toLocaleTimeString('es-CO', { hour: '2-digit', minute: '2-digit' })
            };

            const humidityElement = document.getElementById('current-humidity');
            if (humidityElement) humidityElement.innerText = simulatedData.actual + '%';

            if (window.humidityChart) {
                window.humidityChart.data.labels.push(simulatedData.hora);
                window.humidityChart.data.datasets[0].data.push(simulatedData.actual);
                if (window.humidityChart.data.labels.length > 10) {
                    window.humidityChart.data.labels.shift();
                    window.humidityChart.data.datasets[0].data.shift();
                }
                window.humidityChart.update('none');
            }

            const tableBody = document.getElementById('humidity-logs');
            if (tableBody) {
                const newRow = `<tr><td class="py-2 text-gray-600">${simulatedData.hora}</td><td class="py-2 text-right font-bold text-blue-600">${simulatedData.actual}%</td></tr>`;
                tableBody.insertAdjacentHTML('afterbegin', newRow);
                if (tableBody.children.length > 5) tableBody.lastElementChild.remove();
            }
        } catch (e) { console.error("Error en polling:", e); }
    }

    setInterval(fetchSensorData, 10000);
});
async function analizarimagen(e){
    e.preventDefault();
        const form = e.target;
        // Obtiene todos los datos del formulario
        const formData = new FormData(form);
        try {
            const response = await fetch("/upload", {
                method: "POST",
                body: formData
            });
            // Si Flask devuelve texto HTML
            const resultado = await response.text();
            // Inserta el resultado en la página
            //document.getElementById("resultado").innerHTML = resultado;
            console.log("Respuesta del servidor2:", resultado);
        } catch (error) {
            console.error(error);
        }
}