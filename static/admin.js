fetch('/uz/users/admin-info/')
    .then(response => response.json())
    .then(data => {
        
        let img = document.querySelector('.sidebar img');
        if (data.photo) {
            img.src = data.photo;
            img.style.width = '30px';
            img.style.height = '30px';
            
        }
      let a = document.querySelector('aside a');
      a.remove()
    });
