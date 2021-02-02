// function stopwatch() {
//   let start = null,
//     end = null,
//     running = false,
//     duration = 0;
//   this.startsw = function () {
//     if (running) {
//       throw new Error("stopwatch aready running");
//     } else {
//       console.log("started");
//       running == true;
//       start = new Date();
//     }
//   };
//   this.stopsw = function () {
//     if (!running) {
//       throw new Error("stopwatch already stoped");
//     } else {
//       console.log("stoped");
//       running = false;
//       end = new Date();
//       const seconds = (end.getTime() - start.getTime()) / 1000;
//       duration += seconds;
//     }
//   };
//   this.reset = function () {
//     start = null;
//     end = null;
//     duration = 0;
//     running = false;
//   };
//   Object.defineProperty(this, "duration", {
//     get: function () {
//       return duration;
//     },
//   });
// }
// const sw = new stopwatch();
//--------------------------------------------------------------------------------------


function StopWatch() {
  var startTime = null;
  var stopTime = null;
  var running = false;

  function getTime() {
    var day = new Date();
    return day.getTime();
  }
  this.start = function () {
    if (running == true) return;
    else if (startTime != null)
       stopTime = null;
    running = true;
    startTime = getTime();
  };
  this.stop = function () {
    if (running == false) return;

    stopTime = getTime();
    running = false;
  };
  this.duration = function () {
    if (startTime == null || stopTime == null) return "Undefined";
    else return (stopTime - startTime) / 1000;
  };
}
