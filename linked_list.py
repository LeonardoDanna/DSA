# head = cabeça
# tail = cauda
# node = nó

# Classe que representa um nó da lista duplamente ligada
class Node:  # Inicializando um nó da linked list
    def __init__(self, value):
        self.value = value  # Valor armazenado no nó
        self.next = None  # Ponteiro para o próximo nó
        self.prev = None  # Ponteiro para o nó anterior

# Classe que representa a lista duplamente ligada
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Ponteiro para o primeiro nó (cabeça)
        self.tail = None  # Ponteiro para o último nó (cauda)

    # Método para adicionar um novo nó no início da lista
    def add_to_front(self, value):
        new_node = Node(value)  # Criando um novo nó
        if not self.head:  # Se a lista estiver vazia
            self.head = self.tail = new_node  # O novo nó é tanto a cabeça quanto a cauda
        else:
            new_node.next = self.head  # O próximo nó do novo nó será a antiga cabeça
            self.head.prev = new_node  # A antiga cabeça aponta de volta para o novo nó
            self.head = new_node  # O novo nó se torna a nova cabeça

    # Método para adicionar um novo nó no final da lista
    def add_to_end(self, value):
        new_node = Node(value)  # Criando um novo nó
        if not self.tail:  # Se a lista estiver vazia
            self.head = self.tail = new_node  # O novo nó é tanto a cabeça quanto a cauda
        else:
            new_node.prev = self.tail  # O nó anterior do novo nó será a antiga cauda
            self.tail.next = new_node  # A antiga cauda aponta para o novo nó
            self.tail = new_node  # O novo nó se torna a nova cauda

    # Método para remover um nó do início da lista
    def remove_from_front(self):
        if not self.head:  # Se a lista estiver vazia, retorna None
            return None
        removed_value = self.head.value  # Armazena o valor da cabeça antes de removê-la
        if self.head == self.tail:  # Se a lista tiver apenas um elemento
            self.head = self.tail = None  # A lista fica vazia
        else:
            self.head = self.head.next  # A nova cabeça passa a ser o próximo nó
            self.head.prev = None  # Remove a referência ao nó removido
        return removed_value  # Retorna o valor removido

    # Método para remover um nó do final da lista
    def remove_from_end(self):
        if not self.tail:  # Se a lista estiver vazia, retorna None
            return None
        removed_value = self.tail.value  # Armazena o valor da cauda antes de removê-la
        if self.head == self.tail:  # Se a lista tiver apenas um elemento
            self.head = self.tail = None  # A lista fica vazia
        else:
            self.tail = self.tail.prev  # A nova cauda passa a ser o nó anterior
            self.tail.next = None  # Remove a referência ao nó removido
        return removed_value  # Retorna o valor removido
