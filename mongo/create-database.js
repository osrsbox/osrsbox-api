db.getSiblingDB("osrsbox-db").runCommand(
    { createUser: "someusername",
      pwd: "somepassword",
      roles: [
          {
              role: "userAdmin",
              db: "osrsbox-db"
          },
          "readWrite"
        ]
    }
)

db.temp.insertOne(
    { 
        random: "JIfxp2mVSz61ZF7qzgmF4vBDd2eHjKSiZV6WzUXr24E=", 
    }
);
