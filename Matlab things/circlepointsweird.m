x = [-1000:1:1000]
y = x.^2 + 12.21321323
min(y)
figure(1)
plot(x,y,"r*")
d = roots(y)
figure(2)
plot(d,"R*")
hold on
d = d*d'
plot(d,"B*")