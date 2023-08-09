                               // Discrete Fourier Transform
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
a1=imresize(a,[40 40]);
subplot(2,2,2);
imshow(a1);
title('Resized image');
[m n p]= size(a1);
disp(m,n,p);

subplot(2,2,3);
g = rgb2gray(a1);
imshow(g);
title('Gray image');

subplot(2,2,4);
f=fft2(double(g));
imshow(f);
title('Fourier Transfrom image');

figure(2);
subplot(2,2,1);
f1=fftshift(f);
imshow(f1);
title('Centered image');

f2=ifftshift(f1);
subplot(2,2,2);
imshow(f2);
title('Inversed image');

f3=ifft(f2);
subplot(2,2,3);
imshow(uint8(f3));
title('Result image');
