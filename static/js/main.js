/* ============================================================
    main.js - El cerebro interactivo de PlantApp
    Optimizado: Prevención de dobles peticiones y bloqueos de interfaz
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

    if (fileInput && dropZone) {
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    const promptText = dropZone.querySelector('.prompt-text'); 
                    if (promptText) promptText.classList.add('hidden');

                    let previewImg = dropZone.querySelector('.preview-img');
                    if (!previewImg) {
                        previewImg = document.createElement('img');
                        previewImg.className = 'preview-img max-w-full max-h-full object-contain rounded-2xl z-0 transition-all duration-300 shadow-sm';
                        dropZone.appendChild(previewImg);
                    }
                    previewImg.src = event.target.result;
                    
                    dropZone.classList.remove('border-dashed', 'border-green-200');
                    dropZone.classList.add('border-solid', 'border-green-600', 'bg-green-50/10', 'p-2');
                }
                reader.readAsDataURL(file);
            }
        });
    }

    // Centralizamos el submit aquí de forma limpia para evitar duplicidad
    if (formIA) {
        formIA.addEventListener('submit', analizarimagen);
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
    // 4. ACTUALIZACIÓN DE DATOS (POLLING DE SENSORES SIMULADOS)
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

// Función de análisis corregida: procesa de manera segura y única la petición
async function analizarimagen(e) {
    e.preventDefault(); 
    
    const form = e.target;
    const formData = new FormData(form);
    
    const btnAnalizar = document.getElementById('btn-analizar');
    const resultadoDiv = document.getElementById('resultado-ia');

    if (btnAnalizar) {
        btnAnalizar.disabled = true;
        btnAnalizar.innerHTML = `
            <div class="flex items-center justify-center gap-3">
                <svg class="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                <span class="text-sm">Analizando...</span>
            </div>`;
    }

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Respuesta inválida del servidor: ${response.status}`);
        }

        const data = await response.json();
        console.log("Datos limpios recibidos del backend:", data);

        if (data) {
            document.getElementById('res-planta-nombre').innerText = data.nombre || "Indeterminado";
            document.getElementById('res-planta-alias').innerText = data.alias || "Ninguno";
            
            const certeza = data.certeza || 0;
            document.getElementById('res-planta-certeza').innerText = `${certeza}%`;
            document.getElementById('res-planta-barra').style.width = `${certeza}%`;

            // Renderizar la URL de la imagen devuelta
            const imgElement = document.getElementById('res-planta-img');
            if (imgElement) imgElement.src = data.img;

            if (resultadoDiv) {
                resultadoDiv.classList.remove('hidden');
            }
        }

    } catch (error) {
        console.error("Error en el flujo del Frontend:", error);
        alert("Ocurrió un error al procesar el análisis de la planta.");
    } finally {
        if (btnAnalizar) {
            btnAnalizar.disabled = false;
            btnAnalizar.innerHTML = `<span>Analizar Imagen</span>`;
        }
    }
}