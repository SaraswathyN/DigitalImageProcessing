              //Separating the RGB image into Red , Green and Blue channels
clc
close
clear all
warning off
figure(1);
a = imread('F:\SCILAB (20337)\images\flower.jpg');
imshow(a);
title('original image');
redchannel=a(:,:,1);
greenchannel=a(:,:,2);
bluechannel=a(:,:,3);
black=zeros(size(a,1),size(a,2),'uint8');
red=cat(3,redchannel,black,black);
green=cat(3,black,greenchannel,black);
blue=cat(3,black,black,bluechannel);
figure(2);
imshow(red);
title('redchannel');
figure(3);
imshow(green);
title('greenchannel');
figure(4);
imshow(blue);
title('bluechannel');
