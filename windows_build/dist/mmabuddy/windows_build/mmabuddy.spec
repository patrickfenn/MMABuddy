# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew
block_cipher = None


a = Analysis(['C:\\Users\\patri\\PycharmProjects\\MMABuddy\\main.py'],
             pathex=[],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='mmabuddy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
coll = COLLECT(exe,Tree('dist\\share\\glew\\bin\\'),
Tree('dist\\share\\sdl2\\bin\\'),
Tree('C:\\Users\\patri\\PycharmProjects\\MMABuddy\\'),
               a.binaries,
               a.zipfiles,
               a.datas, 
*[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='mmabuddy')
