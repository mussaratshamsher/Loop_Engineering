function greet(user) {
    if (!user) {
        return "Hello, guest!";
    }
    return "Hello, " + user.name + "!";
}

module.exports = greet;
