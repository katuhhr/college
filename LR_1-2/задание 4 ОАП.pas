program koordinata;
var x1, x2, y1, y2, d: real;
begin
  writeln('введите координаты двух точек (х1, у1, х2, у2)');
  readln (x1, y1, x2, y2);
  d:=sqrt((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1));
  writeln('расстояние между точками',' '  , d);
end.