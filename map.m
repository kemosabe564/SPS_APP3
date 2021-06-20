
clc
clear


% importdata('maplayout.txt');
I = imread('layoutpf.png');

I = im2bw(I);
% 
% store(I);


% function[] = store (A)
x=[];
y=[];
fid = fopen('maplayout.txt','a')   ;
[r,c]=size(I);
for i=1:10:r
%    fprintf(fid,'%s','{'); 
   x=[x,i];
for j=1:10:c
   fprintf(fid,'%d',I(i,j));
   y=[y,i];
if j+10<c
fprintf(fid,'%s',',');

end

end
% fprintf(fid,'%s','}'); 
% fprintf(fid,'%s',','); 

fprintf(fid,'\r\n');
end
fclose(fid); 
% end
% 
