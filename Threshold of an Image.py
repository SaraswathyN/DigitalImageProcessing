
                                    // Threshold of an Image
clc
close
clear all
warning off
figure(1);
a = imread('F:\SCILAB (20337)\images\micky.png');
a=rgb2gray(a);
imshow(a);
title('original image');
s=size(a);
for i=1:s(1)
    for j=1: s(2)
        if a(i,j)>150 then
            a(i,j)=255;
        else
            a(i,j)=0;
        end
    end
end    
figure(2);
imshow(a);
title("Thershold Image");
