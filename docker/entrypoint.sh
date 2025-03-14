#!/bin/sh
#!/bin/bash

# Start the Docker daemon (if not started externally)
/usr/bin/docker &

# Give Docker daemon some time to start
sleep 10

# Start jenkins
exec /usr/local/bin/jenkins.sh

# Install plugins
if [  -f /usr/share/jenkins/plugins.txt ]; then
  jenkins-plugin-cli --plugins $(cat /usr/share/jenkins/plugins.txt)
fi

# Start jenkins
exec /usr/local/bin/jenkins.sh "$@