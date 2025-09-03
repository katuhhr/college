program dkr;
var x,y,l: real;
begin
  x := -9;
  l := 0.1;
  while x <= -2 do
  begin
    if (x <= (-7)) then 
      begin
        y := cos(2*x)/sin(x)+ln(abs(x));
        writeln('x=',x:2:1,', y=',y:2:3);
      end;
    if (x <= -4) and (x >= -7) then 
      begin
        y:=sin(x) / cos(2*x); 
        writeln('x=',x:2:1,', y=',y:2:3);
      end;
    if x>= -4 then
      begin
        y:=(tan(x) * (x * x));
        writeln('x=',x:2:1,', y=',y:2:3);
      end;
       x:=x+l;
end;
end.