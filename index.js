const os = require('os');
console.log("architecture : ",os.arch());
console.log("free RAM : ",os.freemem()/(1024*1024*1024));
console.log("total RAM : ",os.totalmem()/(1024*1024*1024));
console.log("your host name : ",os.hostname())
console.log("platform : ",os.platform())
console.log("user information  : ",os.userInfo())