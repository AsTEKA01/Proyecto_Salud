document.getElementById("loginForm").addEventListener("submit", function(event) {
    // Muestra la pantalla de carga
    document.getElementById("loadingScreen").classList.remove("d-none");

    // Para propósitos de prueba, previene el envío inmediato del formulario
    event.preventDefault();

    // Simula una espera antes de enviar el formulario para ver la pantalla de carga
    setTimeout(() => {
      this.submit();  // Envía el formulario después de 2 segundos
    }, 500);  // Espera de 0.5 segundos
});
