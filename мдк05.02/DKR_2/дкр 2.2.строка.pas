program Re;
var
  s, s1,r: string;
  i, count: integer;
begin
  readln(s);
  readln(s1); 
  r := '';
  for i := 1 to Length(s1) do
  begin
      if i mod 2=1 then 
        r := r + s1[i]
  end;
  WriteLn('Результат: ', r);
end.
