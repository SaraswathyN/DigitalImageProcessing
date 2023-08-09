
                                    // Opening and Closing of an Image
clc
close
clear all
warning off
figure(1);
a = imread('F:\SCILAB (20337)\images\ball.jpg');
imshow(a);
title('original image');
figure(2);
se=imcreatese('ellipse',15,15);
op=imopen(a,se);
imshow(op);
title('Open image Output');
figure(3);
se=imcreatese('ellipse',15,15);
op1=imclose(a,se);
imshow(op1);
title('Close image Output');
