CREATE TABLE scores (
    userID INTEGER,
    based INTEGER DEFAULT 0,
    cringe INTEGER DEFAULT 0,
    pog INTEGER DEFAULT 0,
    shieldTimeLeft INTEGER DEFAULT 0,
    primary key(userID)
);

CREATE TABLE servers (
    serverID INTEGER,
    prefix TEXT DEFAULT '&',
    reaction TEXT,
    primary key(serverID)
);

INSERT INTO scores (userID) VALUES (0)