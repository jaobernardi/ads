// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    const forms = document.querySelectorAll('.needs-validation')
  
    // Loop over them and prevent submission
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {

        form.classList.add('was-validated')

        if (form.checkValidity()) {
            const toastLiveExample = document.getElementById('toast')
            const toast = new bootstrap.Toast(toastLiveExample)
            toast.show()
            form.reset()
            form.classList.remove('was-validated')
        }

        window.scrollTo(0, document.body.scrollHeight);
        
        event.preventDefault()
        event.stopPropagation()
      }, false)
    })
  })()