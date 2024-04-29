<script>
    document.addEventListener('DOMContentLoaded', function () {
        var galleryTop = new Swiper('.gallery-top', {
            loop: true,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });

        var galleryThumbs = new Swiper('.gallery-thumbs', {
            spaceBetween: 10,
            slidesPerView: 4,
            loop: true,
            freeMode: true,
            loopedSlides: 5, // Adjust according to your number of images
            watchSlidesVisibility: true,
            watchSlidesProgress: true,
            autoplay: {
                delay: 3000, // Auto switch every 3 seconds
                disableOnInteraction: false,
            },
            breakpoints: {
                768: {
                    slidesPerView: 3,
                },
                576: {
                    slidesPerView: 2,
                },
            },
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
        });

        galleryTop.controller.control = galleryThumbs;
        galleryThumbs.controller.control = galleryTop;

        galleryThumbs.on('slideChange', function () {
            var index = galleryThumbs.activeIndex;
            galleryTop.slideTo(index);
        });
    });
</script>
