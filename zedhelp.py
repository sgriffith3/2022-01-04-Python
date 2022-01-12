img01 = """
             088
            ;8@@t             
           .8@@@@8,            
             0@C.             
             0@f              
             0@f              
             0@f              
             0@f            ,,
08;          0@f          .0C 
 L@8:        0@f        .G@1  
  .C@81      0@f      i8@f.   
     :G@@8Ct;8@CitG8@@0:      
         ,1L0@@@0Cf;.         
             0@f              
             0@f              
             G@t
"""

img02 = """
             ,G0L        			 
           .G@C.         
         ,0@C.           
       .G@C.             
     ,0@L.    L8@8t      
   ,G@L.     ;@@@@8,     
  :0@@0i.     ;08C,      
     .10@@G1             
         .i0@@0i.        
             .10@@Gi     
                 .10@@0i.
                 .if0@@@f
          .:L8@@@80f:.   
    ;tG8@@@8Li,          
 0@@0Ci,. 
G0L@
"""

print(img01, img02)

def img_splitter(img: str) -> list:
    img_lines = img.splitlines()
    longest = 0
    for ind, line in enumerate(img_lines):
        if line == "":
            img_lines.pop(ind)
        if len(line) > longest:
            longest = len(line)
    for line in img_lines:
        if len(line) < longest:
            line.format(n=longest, c=" ")
    return img_lines

new_01 = img_splitter(img01)
new_02 = img_splitter(img02)

x = zip(new_01, new_02)
for line in x:
    print(line[0], line[1])