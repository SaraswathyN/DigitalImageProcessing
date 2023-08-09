
                          // Brightness enhancement , Contrast Manipulation and  Image Negative 

clc
close
clear all
warning off
a = imread('F:\SCILAB (20337)\images\micky.png');
figure(1);
subplot(2,2,1);
imshow(a);
title('original image');

b=a+50;
subplot(2,2,2);
imshow(b);
title('Intensity increased image');

c = a*5;
subplot(2,2,3);
imshow(c);
title('contrast increased image');

d=255-a;
subplot(2,2,4);
imshow(d);
title('Negative image');

figure(2);
subplot(2,2,1)
g = rgb2gray(a);
imshow(g);
title('Gray image');

b = g+50;
subplot(2,2,2);
imshow(b);
title('intensity increased image');

c = g*5;
subplot(2,2,3);
imshow(c);
title('contrast increased image');

n =255-g
subplot(2,2,4);
imshow(n);
title('Negative image');
size(a);
