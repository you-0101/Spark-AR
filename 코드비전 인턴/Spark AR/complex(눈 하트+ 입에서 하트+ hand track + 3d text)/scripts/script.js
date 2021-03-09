
const Scene = require('Scene');

const FaceTracking = require('FaceTracking');



// Enables async/await in JS [part 1]
(async function() {

    const textObject = await Scene.root.findFirst('3dText0');

    textObject.text = "ME!!";

    const textObject1 = await Scene.root.findFirst('3dText1');

    textObject1.text = "Hi!";



})();
