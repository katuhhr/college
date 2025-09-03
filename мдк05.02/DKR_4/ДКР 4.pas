program hjhg;
uses graphABC;
var x0,y0,y1,x1,n,a1,b1: integer;
x2,y2,k,a,b,h:real;
function f(x:real):real;
begin
f:=1*x*x*x+(1)*x*x+(5)*x+(16);
end;
procedure integral(a,b:real; n:integer);
var i:integer;
h,s,g,otn,x,absl: real;
begin
  h := ((b - a) / n);
  s := 0; 
  for i:=1 to n do
  begin 
  x:=a+i*h;
  s:=s+f(x)*h;  
  end;
  writeln('Интеграл равен: ', s);  
  g := (((b*b*b*b)/4+((b*b*b)/3)+((5)*b*b)/2)+(16*b)) - (((a*a*a*a)/4)+((a*a*a)/3+((5)*a*a)/2)+(16*a));
  writeln('Ручной счет: ', g);  
  absl := abs(g - s);
  otn := absl / abs(g);  
  writeln('Абсолютная погрешность: ', absl:12
  :10);
  writeln('Относительная погрешность: ', otn:12:10);
end;
begin
  SetWindowSize(800,600);
  x0:=400;
  y0:=300;
  line(10,y0, 790, y0);
  line(x0,10,x0,590);
  readln(a,b);
  k:=15;
  x2:=a;
  while x2<=b do
  begin
    y2:=f(x2);
    x1:=x0+round(x2*k);// изменненые координаты
    y1:=y0-round(y2*k);// измененные координаты
    SetPixel(x1,y1,clred);
    x2+=0.001;
  end;
  
  readln(a1,b1,n);
  h:=((b1-a1)/n);
  integral(a1,b1,n);
  x2:=a1;
   while x2<=b1 do
   begin
    y2:=f(x2);
    x1:=x0+round(x2*k);// изменненые координаты
    y1:=y0-round(y2*k);// измененные координаты
    Rectangle(x1,y0,(x0+round((x2+h)*k)),(y0-round((f(x2+h))*k)));
    x2+=h;
  end;
 end.