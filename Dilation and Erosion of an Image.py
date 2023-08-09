                                             // Dilation and Erosion of an Image
clc
close
clear all
warning off
disp('1.Original Image');
disp('2.Binary Image');
disp('3.Dilated Image');
disp('4.Eroded Image');
disp('5.Exit');
while(1)
    h=input('Enter your choice:');
    select h
    case 1
        r = imread('F:\SCILAB (20337)\images\a.png');
        subplot(4,3,1);
imshow(r);
        title('Original Image');

    case 2
        subplot(4,3,2);
        a=rgb2gray(r);
        a=im2bw(a,0.5);
imshow(a);
        title('Binary Image');
    case 3
        subplot(4,3,4);
        se=imcreatese('ellipse',15,15);
sd=imdilate(a,se);
imshow(sd);
        title('Dilation Image');
    case 4
        subplot(4,3,5);
        se1=imcreatese('ellipse',15,15);
        sd1=imerode(a,se1);
imshow(sd1);
        title('Eroded Image');
    case 5
disp('Exit');
        break;
    end
 end
