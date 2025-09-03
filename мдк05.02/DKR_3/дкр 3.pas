program pri;
uses crt;
var n,choice:integer;
a,b,x,h,s,g,otn,absl:real;
function f(x:real):real;
begin
  f:=1*x*x*x+(1)*x*x+(5)*x+(16);
end;
procedure integral(a,b:real; n:integer);
var i:integer;
begin
  h := ((b - a) / n);
  s := 0;
  h := (b - a) / N;  
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
  clrscr;
  repeat
    writeln('Выберите:');
    writeln('1. Рассчитать интеграл');
    writeln('2. Выход');
    write('Ваш выбор: ');
    readln(choice);
    case choice of
      1: begin
           write('Нижний предел (a): ');
           readln(a);
           write('Верхний предел (b): ');
           readln(b);
           write('Количество разбиений (n): ');
           readln(n);
           integral(a, b, n);
         end;
      2: writeln('Выход из программы.');
      else writeln('такого варианта нет!!!');
    end;
  until choice = 2;
end.
 