# Image Segmentation

image segmentation is the process of partitioning a digital image into multiple segments. The goal of segmentation is to simplify and/or change the representation of an image into something that is more meaningful and easier to analyze.
Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images.

## [Contour](https://docs.opencv.org/3.3.1/d4/d73/tutorial_py_contours_begin.html)
Contours can be explained simply as a curve joining all the continuous points (along the boundary), having same color or intensity. The contours are a useful tool for shape analysis and object detection and recognition

For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.

Contour Are Basically used for
- Shape Analysis
- Object Detections


### Edge Detection Vs Contour

These two terms are often used interchangeably. Still, the term 'edge' is mostly used to denote image points where intensity difference between pixels are significant. On the other hand, the term contour is used to denote object boundary. Thus, in many cases contour detection is performed  by processing the detected edges further.

