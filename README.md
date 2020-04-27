# ngrok-scp-uploader
Just some code snippets to share some files with a another remote desktop

**Problem:** Software that is developed must be tested on another host. Booth are not in the same network.

**Solution:** Use ngrok to open a ssh tunnel and use scp command to send files to the remote host.


More about **[ngrok](https://ngrok.com/product)**
> You download and run a program on your machine and provide it the port of a network service, usually a web server.
> It connects to the ngrok cloud service which accepts traffic on a public address and relays that traffic through to the ngrok > process running on your machine and then on to the local address you specified.

Required cli-tools:

On working host: `sshpass`, `scp`, `python`
On remote host: `ngrok`

# Walktrough

On remote host machine type: `ngrok tcp 22`

Note the url. e.g. 0.tcp.ngrok.io:141592


On local machine:

use the port from the remote machine.

python copy_to_office.py 141592
