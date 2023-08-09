
                                                //DISCRETE COSINE TRANSFORM
clc
close
clear all
warning off
figure(1);
a = imread('F:\SCILAB (20337)\images\google.jpeg');
subplot(2,2,1);
imshow(a);
title('original image');
[m n p]= size(a);
disp(m,n,p);

subplot(2,2,2);
b = rgb2gray(a);
imshow(b);
title('Gray image');

subplot(2,2,3);
d=dct(double(b));
imshow(d);
title('DCT image');

d1=idct(d);
subplot(2,2,4);
imshow(uint8(d1));
title('Inversed DCT image');
