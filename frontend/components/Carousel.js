import React from 'react';

const Carousel = () => {
  return (
    <div id="carouselExampleSlidesOnly" class="carousel slide" data-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img class="d-block w-100" src="/images/img-1.jpg" alt="Primeiro Slide"/>
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src="images/" alt="Segundo Slide"/>
        </div>
        <div class="carousel-item">
          <img class="d-block w-100" src=".../800x400?auto=yes&bg=555&fg=333&text=Terceiro Slide" alt="Terceiro Slide"/>
        </div>
      </div>
    </div>
  )
}

export default Carousel;
