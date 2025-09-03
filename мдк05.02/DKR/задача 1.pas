program dkr;
var x,y: real;

begin
    writeln('введите х: ');  
    readln(x);
    if (x <= (-7)) then 
      begin
        y := cos(2*x)/sin(x)+ln(abs(x));
        writeln('x=',x,', y=',y);
      end;
    if (x <= -4) and (x >= -7) then 
      begin
        y:=sin(x) / cos(2*x); 
        writeln('x=',x,', y=',y);
      end;
    if x>= -4 then
      begin
        y:=(tan(x) * (x * x));
        writeln('x=',x,', y=',y);
      end;     
end.