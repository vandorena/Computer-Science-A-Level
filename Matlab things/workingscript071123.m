% matrices and vectors

clc, clearvars, close all

x = linspace(-10,10);
y1 = (-(x-3).^2)+10;
y2 = (-(x-3).^2)+15;
y3 = (-(x-5).^2)+10;
figure(1)
plot(x,y1,'r*')
xlabel('x')
ylabel('y')
title("Y vs X")
grid on
legend("y1","y3")
hold on



plot(x,y2,"b^")
plot(x,y3,'g+')
