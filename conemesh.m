[X,Y] = meshgrid(-100:.5:100);
R = sqrt(X.^2 + Y.^2) +eps;
Z = sin(R)./R;
figure(2)
surf(X,Y,Z)

figure(1)
mesh(X,Y,Z)
