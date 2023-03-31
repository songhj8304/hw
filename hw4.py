def rep_char(c,n):
  print(c*n)
 
def draw_line_string(nstr):
  msg1=f' Hello {nstr},'
  msg2= ' \n Welcome to Seoul.'
  nstr=len(msg1)if(len(msg1)>len(msg2))else len(msg2)

  rep_char('-',nstr)
  print( msg1,msg2 )
  rep_char('-',nstr)

inputname=input('input his/her name: ')
draw_line_string(inputname)
