document.addEventListener('DOMContentLoaded', function() {
    // Your handleSearch function goes here
    function handleSearch() {
        const searchInput = document.querySelector('input[name="query"]');
        const searchQuery = searchInput.value.trim().toLowerCase();
  
        fetch(`/api/v1/dashboard?query=${searchQuery}`)
            .then(response => response.json())
            .then(pharmaciesData => {
                const carouselInner = document.querySelector('.carousel-inner');
                carouselInner.innerHTML = '';
  
                let carouselItemIndex = 0;
                pharmaciesData.forEach(pharmacy => {
                    const matchingDrugs = pharmacy.drugs.filter(drug => drug.name.toLowerCase().includes(searchQuery));
                    console.log('Matching Drugs:', matchingDrugs);
                    if (matchingDrugs.length > 0) {
                        const carouselItem = document.createElement('div');
                        console.log('Pharmacy Data:', pharmacy);
                        carouselItem.classList.add('carousel-item');
                        if (carouselItemIndex === 0) {
                            carouselItem.classList.add('active');
                        }
  
                        const card = document.createElement('div');
                        card.classList.add('card');
  
                        const cardBody = document.createElement('div');
                        cardBody.classList.add('card-body');
  
                        const cardTitle = document.createElement('h5');
                        cardTitle.classList.add('card-title');
                        cardTitle.textContent = pharmacy.name;
  
                        const cardText = document.createElement('p');
                        cardText.classList.add('card-text');
                        cardText.textContent = `Address: ${pharmacy.address}`;
  
                        const drugList = document.createElement('ul');
                        drugList.classList.add('list-group', 'list-group-flush');
  
                        matchingDrugs.forEach(drug => {
                            const drugItem = document.createElement('li');
                            drugItem.classList.add('list-group-item');
  
                            const drugName = document.createElement('span');
                            drugName.classList.add('drug-name');
                            drugName.textContent = drug.name;
  
                            const drugPrice = document.createElement('span');
                            drugPrice.classList.add('drug-price');
                            drugPrice.textContent = `Price: $${drug.price}`;
  
                            drugItem.appendChild(drugName);
                            drugItem.appendChild(drugPrice);
                            drugList.appendChild(drugItem);
                        });
  
                        cardBody.appendChild(cardTitle);
                        cardBody.appendChild(cardText);
                        cardBody.appendChild(drugList);
                        card.appendChild(cardBody);
                        carouselItem.appendChild(card);
                        carouselInner.appendChild(carouselItem);
  
                        carouselItemIndex++;
                    }
                });
  
                // Reinitialize the carousel
                $('.carousel').carousel();
            })
            .catch(error => console.error('Error fetching search results:', error));
    }
  
    // Attach the search function to the search button click event
    const searchButton = document.querySelector('button[type="submit"]');
    searchButton.addEventListener('click', function(event) {
        event.preventDefault();
        handleSearch();
    });
  });