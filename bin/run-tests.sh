#!/opt/app-root/bin/dumb-init /bin/sh

###
# Run front-end tests
###

# Start Xvfb
test -e /tmp/.X99-lock
/usr/bin/Xvfb :99 &
xvfb=$!

export DISPLAY=:99.0
export CHROME_BIN=/usr/bin/chromium-browser

/portal/node_modules/.bin/karma start /portal/karma.conf.js --single-run

kill -TERM $xvfb
wait $xvfb
