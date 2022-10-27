# Exercise 7

## Instructions

### Echo Server/Client

1. Write a TCP server:
   1. It can receive a string
   2. It returns any received string to the client.
   3. EXTRA: The server stay alive and can receive multiple messages

2. Write a TCP client:
   1. That connect to a server
   2. It can send a string
   3. It can print the response
   4. EXTRA: The client uses CMD menu
   5. EXTRA: The clients connections stay alive and can send multiple messages

### Reverse server

1. Rewrite your server:
   1. it should reverse the string sent to the client
   2. it should return the string uppercase

    ```text
    hello
    OLLEH
    ```

### Basic protocol

We will define a protocol that determines how we want our string to be modified.

1. Use the first letter in the string as a "command" to the server
   1. If the first letter is 'u' the string should be returned as upper case
   2. If the first letter is 'r' the string should be reversed
   3. If the first letter is a number 0-9 the string should be sent that many times.
2. The server should print the received command and string before returning to the client
3. The client should work as is from the previous versions

### Improve the protocol

The current solution in not good enough, since it makes u, r and 0-9 reserved to the command. I.e. if you write the string risk, it would return ksi. You should in this exercise separate the string message and the command, so you can handle command (r, u, 0-9) and strings.

1. In the client:
   1. Print sent command, and string
   2. Print the received string as previously
2. In the server:
   1. Print the received command and string
   2. Apply the command to the string and return the result to the client

### Multiple commands

1. In the server:
   1. Allow multiple commands, i.e. ru or ur will return the string reversed and upper case.
   2. Print what commands the server received
   3. EXTRA: how would you handle rru?

2. In the client:
   1. Support to send multiple commands, ie. ru

### More Commands

1. Add more commands to your server, read the python docs for inspirations [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

### Extra Word Guessing Game

Use the protocol from previous tasks but will need to rethink how you use it.

1. Write a word guessing game client
   1. The user can start a new game
   2. The user can send a guessed word
   3. The user will get the correct letters after each try

2. Write a word guessing game server
   1. The user can start the game and gets a random word from a list
   2. The user can restart the game and will then get a new word
   3. The user will get the correct letters sent back, and the wrong ones marked with a asterisk: `um*br***a`
   4. If the user successfully guesses the word, the user is notified without sending the word

## Hand in instructions

No hand in this exercise.
