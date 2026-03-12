import os
import subprocess

# 获取当前目录下所有 docx
files = [f for f in os.listdir('.') if f.endswith('.docx')]

for f in files:
    output_name = os.path.splitext(f)[0] + '.md'
    print(f"正在转换: {f} -> {output_name}")
    
    # 构造命令
    cmd = [
        'pandoc', f, 
        '-o', output_name,
        '--extract-media', f'./media/{os.path.splitext(f)[0]}'
    ]
    subprocess.run(cmd)

print("全部转换完成！")