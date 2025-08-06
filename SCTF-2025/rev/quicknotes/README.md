# quicknotes

## description

Just bought a new note-taking app! Uhm... what does it even do?

[download here](https://drive.google.com/file/d/18YxjodcP70PiccFDnJGeOKMYqs5-r6Gn/view)

author: `kairos`

files provided: `quicknotes.AppImage`

```
> file quicknotes.AppImage
quicknotes.AppImage: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.18, stripped
```

## solve

this is my first time doing `.AppImage` rev but i extracted the files from it using `--appimage-extract`.

```
> ./quicknotes.AppImage --appimage-extract
squashfs-root/.DirIcon
squashfs-root/AppRun
squashfs-root/LICENSE.electron.txt
squashfs-root/LICENSES.chromium.html
...
squashfs-root/resources/app.asar
...
squashfs-root/v8_context_snapshot.bin
squashfs-root/vk_swiftshader_icd.json
```

usually the main logic of such files is in `app.asar`, which is in `squashfs-root/resources`.

```
> asar extract squashfs-root/resources/app.asar quicknotes_app
> tree quicknotes_app/
quicknotes_app/
├── main.js
├── __package.json
└── package.json

0 directories, 3 files
```

```
> cat quicknotes_app/main.js
const { app, BrowserWindow, ipcMain, net } = require('electron');
const path   = require('path');
const os     = require('os');
const crypto = require('crypto');

function createMainWindow () {
  const win = new BrowserWindow({
    width: 820,
    height: 600,
    title: 'QuickNotes',
    webPreferences: {
      contextIsolation: true,
      nodeIntegration: false
    }
  });

  win.loadFile(path.join(__dirname, 'index.html'));
}


const cfg = {
  endpoint : 'https://updates.quicknotes.local/api/ping',
  digest   : Buffer.from([
    0x26,0x36,0x21,0x33,0x2e,0x3b,0x65,0x22,0x0a,0x2c,
    0x65,0x00,0x0a,0x3e,0x1b,0x65,0x02,0x0a,0x3d,0x65,
    0x22,0x0a,0x21,0x65,0x0a,0x27,0x30,0x23,0x74,0x28
  ])
};

function decrypt (buf) {
  return Buffer.from(buf.map(b => b ^ 0x55)).toString('utf8');
}

function pingSilent () {
  const payload = JSON.stringify({
    host : os.hostname(),
    user : os.userInfo().username,
    ver  : app.getVersion(),
    ts   : Date.now(),
    data : crypto.createHash('sha256').update(cfg.digest).digest('hex') // looks legit
  });

  const req = net.request({ method: 'POST', url: cfg.endpoint, timeout: 1500 });
  req.on('abort', () => {});
  req.end(payload);
  req.abort();
}

app.whenReady().then(() => {
  createMainWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createMainWindow();
  });
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
```

ah yes looks legit.

```
> python3
Python 3.13.5 (main, Jun 11 2025, 15:36:57) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> flag = [0x26,0x36,0x21,0x33,0x2e,0x3b,0x65,0x22,0x0a,0x2c,0x65,0x00,0x0a,0x3e,0x1b,0x65,0x02,0x0a,0x3d,0x65,0x22,0x0a,0x21,0x65,0x0a,0x27,0x30,0x23,0x74,0x28]
>>> ''.join(chr(a ^ 0x55) for a in flag)
'sctf{n0w_y0U_kN0W_h0w_t0_rev!}'
```

flag: `sctf{n0w_y0U_kN0W_h0w_t0_rev!}`

## afterthoughts

life is roblox