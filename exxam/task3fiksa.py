#Initializing sender, recipient and empty list to store lines of the message
class Message:
    def __init__(self, sender: str, recipient: str) -> None:
        self._sender = sender
        self._recipient = recipient
        self._message_body = []


#Using property to define getter methods for sender and recipient
#Allowing access without directy accessing
    @property
    def sender(self) -> str:
        return self._sender

    @property
    def recipient(self) -> str:
        return self._recipient

    def append(self, line: str) -> None:
        self._message_body.append(line)

    def __str__(self) -> str:
        message_str = f"From: {self._sender}\nTo: {self._recipient}\n"
        message_str += "\n".join(self._message_body)
        return message_str


if __name__ == "__main__":
    message = Message("Harry Morgan", "Rudolf Reindeer")
    
    # Appending lines to the message body
    message.append("Dear Rudolf,")
    message.append("I hope this message finds you well.")
    message.append("Best regards,")
    message.append("Harry")
    
    print(message)  # Prints the string representation of the message
