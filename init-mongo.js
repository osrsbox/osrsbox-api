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
