const findMyLocation = () => {
    const status = document.querySelector('.location');
  
    const success = (position) => {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
  
      const geoApiUrl = `https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en`;
  
      fetch(geoApiUrl)
        .then(res => res.json())
        .then(data => {
          const localityValue = data.locality;
          status.textContent = `Location: ${localityValue}`;
  
          var locationInput = document.getElementById("locationInput");
          locationInput.value = localityValue
          
        
        })
        .catch(error => {
          console.error('Error:', error);
        });
    };
  
    const error = () => {
      status.textContent = 'Unable to retrieve your location';
    };
  
    navigator.geolocation.getCurrentPosition(success, error);
  };
  
  
  
  // Attach event listener to the "Find Location" button
  document.querySelector('.find-location').addEventListener('click', findMyLocation);
  