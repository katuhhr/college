program jkg;
var
  i, min, k: integer;
  a: array [1..10]  of integer;
  begin
    for i:=1 to 10 do
    begin
      read(a[i]);
    end;
    k:=0;
    min:=100;
  for i := 1 to 10 do
  begin
    if a[i] < min then
    begin
   min:=a[i];
    end;
    if a[i] = min then
    begin
      k+=1; 
      end;
    end;
    writeln(a,' ', k);
  end.