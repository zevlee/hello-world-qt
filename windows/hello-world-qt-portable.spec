# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
	['../helloworldqt.py'],
	pathex=[],
	binaries=[],
	datas=[
		('../helloworldqt', 'helloworldqt'),
		('../org.example.HelloWorldQt.svg', '.'),
		('../LICENSE', '.'),
		('../VERSION', '.')
	],
	hiddenimports=[],
	hookspath=[],
	runtime_hooks=[],
	excludes=[],
	win_no_prefer_redirects=False,
	win_private_assemblies=False,
	cipher=block_cipher,
	noarchive=False
)

pyz = PYZ(
	a.pure,
	a.zipped_data,
	cipher=block_cipher
)

exe = EXE(
	pyz,
	a.scripts,
	a.binaries,
	a.zipfiles,
	a.datas,
	[],
	name='hello-world-qt',
	icon='hello-world-qt.ico',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	console=False
)
