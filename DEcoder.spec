# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['DEcoder.py'],
             pathex=['/Users/admin/Documents/Code/项目/DEcoder'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='DEcoder',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='DEcoder')
app = BUNDLE(coll,
             name='DEcoder.app',
             icon=None,
             bundle_identifier=None,
               info_plist={
                'NSHighResolutionCapable': True,
                'NSHumanReadableCopyright': u"Copyright © 2020, UINOTE, All Rights Reserved"
            })
