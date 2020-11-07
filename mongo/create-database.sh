#!/bin/bash
set -e

mongo -- "osrsbox-db" <<EOF
    var rootUser = '$MONGO_INITDB_ROOT_USERNAME';
    var rootPassword = '$MONGO_INITDB_ROOT_PASSWORD';
    var admin = db.getSiblingDB('admin');
    admin.auth(rootUser, rootPassword);

    var user = '$PROJECT_USERNAME';
    var passwd = '$PROJECT_PASSWORD';
    db.createUser({user: user, pwd: passwd, roles: ["readWrite"]});
EOF

mongo -- "osrsbox-db" <<EOF 
    db.temp.insertOne(
        { 
            random: "JIfxp2mVSz61ZF7qzgmF4vBDd2eHjKSiZV6WzUXr24E=", 
        }
    );
EOF
