function mylocomotive() {
  gsap.registerPlugin(ScrollTrigger);

  // Using Locomotive Scroll from Locomotive https://github.com/locomotivemtl/locomotive-scroll

  const locoScroll = new LocomotiveScroll({
    el: document.querySelector(".main"),
    smooth: true,
    
  });
  // each time Locomotive Scroll updates, tell ScrollTrigger to update too (sync positioning)
  locoScroll.on("scroll", ScrollTrigger.update);

  // tell ScrollTrigger to use these proxy methods for the ".main" element since Locomotive Scroll is hijacking things
  ScrollTrigger.scrollerProxy(".main", {
    scrollTop(value) {
      return arguments.length
        ? locoScroll.scrollTo(value, 0, 0)
        : locoScroll.scroll.instance.scroll.y;
    }, // we don't have to define a scrollLeft because we're only scrolling vertically.
    getBoundingClientRect() {
      return {
        top: 0,
        left: 0,
        width: window.innerWidth,
        height: window.innerHeight,
      };
    },
    // LocomotiveScroll handles things completely differently on mobile devices - it doesn't even transform the container at all! So to get the correct behavior and avoid jitters, we should pin things with position: fixed on mobile. We sense it by checking to see if there's a transform applied to the container (the LocomotiveScroll-controlled element).
    pinType: document.querySelector(".main").style.transform
      ? "transform"
      : "fixed",
  });

  // each time the window updates, we should refresh ScrollTrigger and then update LocomotiveScroll.
  ScrollTrigger.addEventListener("refresh", () => locoScroll.update());

  // after everything is set up, refresh() ScrollTrigger and update LocomotiveScroll because padding may have been added for pinning, etc.
  ScrollTrigger.refresh();
}

function slider1() {
  var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    pagination: {
      el: ".swiper-pagination",
    },
  });
}
function slider2() {
  var swiper = new Swiper(".mySwiper2", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
      rotate: 50,
      stretch: 0,
      depth: 100,
      modifier: 1,
      slideShadows: true,
    },
    pagination: {
      el: ".swiper-pagination",
    },
  });
}
function myowl_crosol() {
  $(".owl-carousel").owlCarousel({
    loop: true,
    margin: 10,
    nav: false,
    autoplay: false,
    autoplayTimeout: 3000,
    dots: true,
    responsive: {
      0: {
        items: 1.5,
      },
      600: {
        items: 2.5,
      },
      1024: {
        items: 3.5,
      },
      2000: {
        items: 4.5,
      },
      2560: {
        items: 5.5,
      },
    },
  });
}
function front_page_Animation() {
  Shery.imageEffect(".back", {
    style: 6,
    config: {
      noiseDetail: { value: 7.44, range: [0, 100] },
      distortionAmount: { value: 2.21, range: [0, 10] },
      scale: { value: 35.88, range: [0, 100] },
      speed: { value: 0.50, range: [0, 1] },
      zindex: { value: -9996999, range: [-9999999, 9999999] },
      aspect: { value: 2.136478510252749 },
      ignoreShapeAspect: { value: true },
      shapePosition: { value: { x: 0, y: 0 } },
      shapeScale: { value: { x: 0.5, y: 0.5 } },
      shapeEdgeSoftness: { value: 0, range: [0, 0.5] },
      shapeRadius: { value: 0, range: [0, 2] },
      currentScroll: { value: 0 },
      scrollLerp: { value: 0.07 },
      gooey: { value: true },
      infiniteGooey: { value: true },
      growSize: { value: 1, range: [1, 15] },
      durationOut: { value: 1, range: [0.1, 5] },
      durationIn: { value: 1.5, range: [0.1, 5] },
      displaceAmount: { value: 0.5 },
      masker: { value: true },
      maskVal: { value: 1, range: [1, 5] },
      scrollType: { value: 0 },
      geoVertex: { range: [1, 64], value: 1 },
      noEffectGooey: { value: true },
      onMouse: { value: 0 },
      noise_speed: { value: 1.83, range: [0, 10] },
      metaball: { value: 0.05, range: [0, 2], _gsap: { id: 3 } },
      discard_threshold: { value: 0.5, range: [0, 1] },
      antialias_threshold: { value: 0, range: [0, 0.1] },
      noise_height: { value: 0.27, range: [0, 2] },
      noise_scale: { value: 100, range: [0, 100] },
    },
    debug: false,
    gooey: true,
  });
}
function front_page() {
  gsap.from(".page1 .row2 .col1", {
    duration: 3,
    scale: 0.4,
  });
  gsap.from(".page1 .top .heading ", {
    duration: 2,
    scale: 0.6,
  });

  gsap.from(".page1 .row2 .col2 .mod ",{
    x:1500,
    stagger: 0.5,
    duration: 1,
    ease:"power1.in",
  })

}

function secondpage() {
  gsap.from(".page2 .row1 .col1 h5", {
    x: -400,
    duration: 1,
    rotate: 360,
    scrollTrigger: {
      trigger: ".page2",
      scroller: ".main",
      markers: false,
      start: "top 400px",
      end: "top 500px",
    },
  });
  gsap.from(".page2 .row1 .col2 h1", {
    y: -300,
    duration: 2,
    // rotate: 360,
    ease: "bounce.out",
    scrollTrigger: {
      trigger: ".page2",
      scroller: ".main",
      markers: false,
      start: "top 500px",
      end: "top 50px",
    },
  });
}

function thirdpage() {
  gsap.from(".page3 .row2 h1", {
    y: -260,
    duration: 2,
    ease: "bounce.out",
    scrollTrigger: {
      trigger: ".page3",
      scroller: ".main",
      markers: false,
      start: "top 400px",
      end: "top 100px",
    },
  });

  gsap.from(".page3 .row3 h6", {
    x: 1800,
    ease: "power1.inout",
    stagger: 0.2,
    scrollTrigger: {
      trigger: ".page3",
      scroller: ".main",
      markers: false,
      start: "top 100px",
      end: "top 200px",
    },
  });
}

function fifthpage() {
  var t1 = gsap.timeline({
    scrollTrigger: {
      trigger: ".page5div1",
      scroller: ".main",
      markers: false,
      start: "top 500px",
      end: "top 100px",
      onEnter: showrandom,
    },
  });

  function showrandom() {
    let num1 = document.querySelector("#num1");
    let num2 = document.querySelector("#num2");
    let num3 = document.querySelector("#num3");
    let myInterval = setInterval(myTimer, 30);
    setTimeout(myStopFunction, 1500);

    function myTimer() {
      num1.innerHTML = Math.floor(Math.random() * 10);
      num2.innerHTML = Math.floor(Math.random() * 1000);
      num3.innerHTML = Math.floor(Math.random() * 100);
    }

    function myStopFunction() {
      num1.innerHTML = "10";
      num2.innerHTML = "300";
      num3.innerHTML = "70";
      clearInterval(myInterval);
    }
  }
}

function sixthpage() {
  // var tl = gsap.timeline()
  gsap.from(".page6 .row1 .part1 h1", {
    x: "-80vw",
    ease: "power1.inout",
    duration: 1,
    scrollTrigger: {
      trigger: ".page6 .row1 .part1",
      scroller: ".main",
      markers: false,
      start: "top 300px",
      end: "bottom 200px",
    },
  });
  gsap.from(".page6 .row1 .part2 p", {
    x: "-45vw",
    duration: 1,
    scrollTrigger: {
      trigger: ".page6 .row1 .part1",
      scroller: ".main",
      markers: false,
      start: "top 300px",
      end: "bottom 200px",
    },
  });
}

function seventhpage() {
  gsap.from(".page7 .middlerow .col1 .writeen h3", {
    y: "45vw",
    stagger: 0.1,
    duration: 1,

    scrollTrigger: {
      trigger: ".page7 .middlerow .col1",
      scroller: ".main",
      markers: false,
      start: "top 500px",
      end: "bottom 200px",
    },
  });
  gsap.to(".page7 .middlerow .col1 .writeen #students", {
    delay: 1.2,
    x: "6vw",
    scrollTrigger: {
      trigger: ".page7 .middlerow .col1",
      scroller: ".main",
      markers: false,
      start: "top 500px",
      end: "bottom 200px",
    },
  });
  gsap.to(".page7 .middlerow .col1 .writeen #feedback", {
    delay: 1.5,
    x: "10vw",
    scrollTrigger: {
      trigger: ".page7 .middlerow .col1",
      scroller: ".main",
      markers: false,
      start: "top 500px",
      end: "bottom 200px",
    },
  });
}

function eightpage() {
  gsap.to(".page8 .col1 .part1 h4", {
    // x:"-45vw",
    scale: 1.5,
    duration: 1,
    scrollTrigger: {
      trigger: ".page8 .col1 .part1",
      scroller: ".main",
      markers: false,
      start: "top 300px",
      end: "bottom 200px",
    },
  });
  gsap.from(".page8 .col1 .part2 h6", {
    x: "-45vw",
    stagger: 0.3,
    // duration:1,
    scrollTrigger: {
      trigger: ".page8 .col1 .part1",
      scroller: ".main",
      markers: false,
      start: "top 300px",
      end: "bottom 200px",
    },
  });
}

function hamburger() {
  console.log("hellp")
  var profileisopen = false
  var page1 = document.querySelector(".page1");
  var profile = document.querySelector(".profile1");
  var box = document.querySelector(".hamburger-menu");

  profile.addEventListener("click", () => {

    if (profileisopen == false) {
      box.style.left = "78vw";
      box.style.display = "block";
      page1.style.transform = "ease-in-out" ;
      profileisopen = true;
    }
    else {
      box.style.left = "100vw";
      box.style.display = "none";
      profileisopen = false;
    }
  });
}

function signuppage(){
  const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = () => {
  loginForm.style.marginLeft = "-50%";
  loginText.style.marginLeft = "-50%";
};
loginBtn.onclick = () => {
  loginForm.style.marginLeft = "0%";
  loginText.style.marginLeft = "0%";
};
signupLink.onclick = () => {
  signupBtn.click();
  return false;
};
}

mylocomotive();
slider1();
slider2();
myowl_crosol();
front_page();
front_page_Animation();
secondpage();
thirdpage();
fifthpage();
sixthpage();
seventhpage();
eightpage();
hamburger();
signuppage();
