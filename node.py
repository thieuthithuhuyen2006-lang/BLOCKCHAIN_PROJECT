"""P8 – Full Node. Phụ trách: Network."""


class Node:
    def receive_tx(self, tx):
        raise NotImplementedError

    def receive_block(self, block):
        raise NotImplementedError

    def broadcast(self, message):
        raise NotImplementedError
