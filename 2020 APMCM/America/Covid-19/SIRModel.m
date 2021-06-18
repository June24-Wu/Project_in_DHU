function y=SIRModel(t,x,lambda,mu,de)
y=[-lambda*x(1)*x(2),lambda*x(1)*x(2)-mu*x(2)-de*x(2),mu*x(2),de*x(2)]';

 ts=1:1:365;
 lambda=0.2; 
 mui=0.18;
 de=0.00005;
 x0=[0.971990864,0.0280091,0.017272109,0.000565839];
 [t,x] = ode45(@(t,x) SIRModel(t,x,lambda,mui,de), ts, x0);
 plot(t,x(:,1),t,x(:,2),'.',t,x(:,3),'*',t,x(:,4),'-');
 xlabel('Time/Day');
 ylabel('Rate');
 legend('S','I','R','D');
 title('America');
