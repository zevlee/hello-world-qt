# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
	['../hello-world-qt'],
	pathex=[],
	binaries=[],
	datas=[
		('../lib', 'lib'),
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
	[],
	exclude_binaries=True,
	name='hello-world-qt',
	icon='hello-world-qt.icns',
	debug=False,
	bootloader_ignore_signals=False,
	strip=False,
	upx=True,
	console=False,
	codesign_identity='',
	entitlements_file='entitlements.plist'
)

coll = COLLECT(
	exe,
	a.binaries,
	a.zipfiles,
	a.datas,
	strip=False,
	upx=True,
	upx_exclude=[],
	name='hello-world-qt'
)

app = BUNDLE(
	coll,
	name='Hello World.app',
	icon='hello-world-qt.icns',
	bundle_identifier='org.example.HelloWorldQt',
	version='VERSION'
)
