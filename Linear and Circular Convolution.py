
                                   //Linear Convolution
clear all
close
clc
x=input('enter x seq :');
h=input('enter h seq :');
m=length(x);
n=length(h);
for i=1:n+m-1
conv_sum=0;
   for j=1:i
       if(((i-j+1)<=n)&(j<=m))
conv_sum=conv_sum+x(j)*h(i-j+1);
       end;
 y(i)=conv_sum;
       end;
   end;
disp('Before using convolution funtion');
disp(y');
   y=conv(x,h);
disp('After using convolution funtion');
disp(y);


                       // Circular Convolution

clear all;
clc;
close;
x1=[1,2,3,4];
x2=[1,2,1,2];
//Computing DFT
X1=fft(x1,1)
X2=fft(x2,-1)
//Multiplication of 2DFTs
X3=X1.*X2
//Circular Convolution Result
x3=abs(fft(X3,-1))
disp('Circular convolution funtion');
disp(x3)
