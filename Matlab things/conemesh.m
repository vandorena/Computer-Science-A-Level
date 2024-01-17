[X,Y] = meshgrid(-500:.5:500);
R = sqrt(X.^2 + Y.^2) +eps;
Z = sin(R)./R;
figure(2)
surf(X,Y,Z)

figure(1)
mesh(X,Y,Z)
