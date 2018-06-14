var JsonInfluxDbStream = require('json-to-line-protocol').JsonInfluxDbStream;

var jsonToLine = new JsonInfluxDBLineStream();

// Get JSON (stringified objects), convert to line format, write to influxdb
getJsonStream()
  .pipe(jsonToLine)
  .pipe(influxApiStream);
