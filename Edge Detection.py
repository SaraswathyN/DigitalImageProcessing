
                                                      // Edge Detection
clc
close
clear all
warning off
disp('1.Original Image');
disp('2.Gray Image');
disp('3.Prewitt Image');
disp('4.Canny Image');
disp('5.Sobel Image');
disp('6.Log Image');
disp('7.Exit');
while(1)
    h=input('Enter your choice:');
    select h
    case 1
        r = imread('F:\SCILAB (20337)\images\starfish.jpeg');
        subplot(4,3,1);
imshow(r);
        title('Original Image');
    case 2
        subplot(4,3,2);
        a=rgb2gray(r);
imshow(a);
        title('GrayImage');
    case 3
        subplot(4,3,3);
        b=edge(a,'prewitt');
imshow(b);
        title('Prewitt Image');
    case 4
        subplot(4,3,4);
        c=edge(a,'canny');
imshow(c);
        title('Canny Image');
    case 5
        subplot(4,3,5);
        d=edge(a,'sobel');
imshow(d);
        title('Sobel Image');
    case 6
        subplot(4,3,6);
        f=edge(a,'log');
imshow(f);
        title('Log Image');
    case 7
disp('Exit');
        break;
    end
 end
