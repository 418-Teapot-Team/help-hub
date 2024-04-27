<template>
  <span class="loader"></span>
</template>
<style scoped lang="scss">
.loader {
  border: 24px solid;
  border-color: rgba(255, 255, 255, 0.15) rgba(255, 255, 255, 0.25) rgba(255, 255, 255, 0.35)
    rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  display: inline-block;
  box-sizing: border-box;
  animation: animloader 1s linear infinite;
}

@keyframes animloader {
  0% {
    border-color: rgba(46, 196, 182, 0.15) rgba(46, 196, 182, 0.25) rgba(46, 196, 182, 0.35)
      rgba(46, 196, 182, 0.75);
  }
  33% {
    border-color: rgba(46, 196, 182, 0.75) rgba(46, 196, 182, 0.15) rgba(46, 196, 182, 0.25)
      rgba(46, 196, 182, 0.35);
  }
  66% {
    border-color: rgba(46, 196, 182, 0.35) rgba(46, 196, 182, 0.75) rgba(46, 196, 182, 0.15)
      rgba(46, 196, 182, 0.25);
  }
  100% {
    border-color: rgba(46, 196, 182, 0.25) rgba(46, 196, 182, 0.35) rgba(46, 196, 182, 0.75)
      rgba(46, 196, 182, 0.15);
  }
}
</style>
