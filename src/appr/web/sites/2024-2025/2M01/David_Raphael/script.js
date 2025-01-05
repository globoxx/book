document.getElementById('toggleButton').addEventListener('click', function () {
    const content = document.getElementById('toggleContent');
    const button = this;
  
    if (content.style.display === 'none' || content.style.display === '') {
      content.style.display = 'block';
     
    } else {
      content.style.display = 'none';
     
    }
  });
<script src="script.js"></script>
  