var Datastore = require('nedb');
var db = new Datastore({
    filename: './data/memo',
    autoload: true
});
var querystring = require('querystring');
var url = require('url');


exports.create = function(req, res, body) {
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.write('create memo');
    res.end();
};

exports.read = function(req, res, body) {
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.write('read memo');
    res.end();
};

exports.update = function(req, res, body) {
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.write('update memo');
    res.end();
};

exports.remove = function(req, res, body) {
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.write('remove memo');
    res.end();
};

function _insertMemo(body, callback) {
    body = typeof body === 'string' ? JSON.parse(body) : body;

    var memo = {
        author: body.author,
        memo: body.memo,
        date: new Date()
    };

    db.insert(memo, callback);
}

function _findMemo(where, callback) {
    where = where || {};
    db.find(where, callback);
}

function _updateMemo(where, body, callback) {
    db.update(where, {
        $set: body
    }, {
        multi: true
    }, callback);
}

function _removeMemo(where, callback) {
    db.remove(where, {
        multi: true
    }, callback);
}