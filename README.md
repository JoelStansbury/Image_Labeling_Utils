# Image_Labeling_Utils
Simple functions which assist in hand labeling images for machine learning purposes

## multipoint()
```
>>import image_labeling_utils as ilu
>>coords = ilu.multipoint(path/to/image.jpg)
```
[image]: [capture.png]

LEFT CLICK: add coordinate at pointer location
RIGHT CLICK: remove last coordinate
RETURN: close window and return list of coords
```
RETURNS:
[[632, 867], [2101, 879], [2070, 2816], [731, 2859], [2635, 1131]]
```
