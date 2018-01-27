# Geometric Calculations
Let's get some hand Dirty with Some Geometry, Before understanding this Chapter [Geometrical Transformations](https://github.com/Kartikkh/OpenCv-Starter/blob/master/GeometricTransformations.ppt)

# Image Manipulation
Transformation simply means Geometric distortion inacted upon the image Like Rotation, Translation, Scale
So, We generally use transformation to correct the problem of image capturing from different points and Angles

Types of Transformations are -
- Affine Transformation
- Non Affine Transformation



## Affine Transformation

 Affine transform is a combination of rotation, translation ( shift ), scale, and shear.
 This transform has six parameters. When a square undergoes an Affine transformation, parallel lines remain parallel,
 but lines meeting at right angles no longer remain orthogonal.

- Scaling
- Rotation
- Transformation


#### Note-
- Line which are parallel in the original image will always be parallel in transformed image
- Parallelism is always maintained

##### For More Information Please check these Links
- [Geometrical Transformation](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html)
- [Affine Transformation Example](https://www.learnopencv.com/warp-one-triangle-to-another-using-opencv-c-python/)


## Non Affine Transformation

- In Non Affine Transformation Collinearity is maintained !
- They does not preserve Parallelism , Angle and Length
- Very common in Computer vision
- And it arises due to the way of image is being captured !