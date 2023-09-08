#primeira questão da lista
class node:
    def __init__(self, valor):
        self.value = valor
        self.left = None
        self.right = None
    
    def __repr__(self):
        return '%s <- %s -> %s' % (self.left and self.left.value, self.value, self.right and self.right.value)

#segunda questão da lista
class tree:
    def __init__(self, valor=None):
        self.raiz = node(valor)
        self.count = 0
        
    def insert(self, value):
        def _inserir(value, no):
            if no.left is None:
                no.left = node(value)
            elif no.right is None:
                no.right = node(value)
            else:
                if no.left.right is None:
                    _inserir(value, no.left)
                else:
                    _inserir(value, no.right)
        if self.raiz is None:
            self.raiz = node(value)
        else:
            _inserir(value, self.raiz)

    #terceira questão da lista
    def binary_search(self, value):
        def binary_search_recursive(value, no):
            if no is None:
                return False
            elif value == no.value: 
                return True
            elif value < no.value:
                return binary_search_recursive(value, no.left) 
            elif value > no.value:
                return binary_search_recursive(value, no.right)  
        if self.raiz is None:
            return False
        else:
            return binary_search_recursive(value, self.raiz) 

    #quarta questão da lista
    def tree_height(self):
        def tree_height_recursive(no):
            if no is None:
                return 0

            left_height = tree_height_recursive(no.left)
            right_height = tree_height_recursive(no.right)

            return max(left_height, right_height) + 1
        return tree_height_recursive(self.raiz) - 1

    #quinta questão
    def in_order(self):
        def _inorder(no):
            if no is not None:
                _inorder(no.left)
                print(no.value, end=" -> ")
                _inorder(no.right)
        _inorder(self.raiz)
        print()

    #sexta questão
    def pre_order(self):
        def _preorder(no):
            if no:
                print(no.value, end=" - ")
                if no.left is not None:
                    _preorder(no.left)
                if no.right is not None:
                    _preorder(no.right)
        _preorder(self.raiz)
        print()

    #sétima questão
    def post_order(self):
        def _postorder(no):
            if no:
                _postorder(no.left)
                _postorder(no.right)
                print(no.value, end=" -> ")
        _postorder(self.raiz)
        print()

    #oitava questão
    def level_order(self):
        if self.raiz is None:
            return
        
        nos = [self.raiz]
        while nos:
            no = nos.pop(0)
            print(no.value, end=" <-> ")
            if no.left:
                nos.append(no.left)
            if no.right:
                nos.append(no.right)
        print()

    def represent(self):
        def _reper(no):
            s = ''
            if no is not None:
                s += '%s <- %s -> %s \n' % (no.left and no.left.value, no.value, no.right and no.right.value)
                s += self._reper(no.left)
                s += self._reper(no.right)
            return s
        return _reper(self.raiz)

    #nona questão
    def count_nos(self):
        def count_nos_recursive(no):
            if no.left:
                self.count += 1
                count_nos_recursive(no.left)
            if no.right:
                self.count += 1
                count_nos_recursive(no.right)
            
            return self.count + 1
        return count_nos_recursive(self.raiz)

    #décima questão
    def max_value(self):
        def max_value_recusive(no):
            if no is None:
                return 0
            current_level = [no]
            values = []
            while current_level:
                next_level = []
                for no in current_level:
                    if no.left is None:
                        values.append(no.value)
                    else:
                        values.append(no.value)
                    if no.left:
                        next_level.append(no.left)
                    if no.right:
                        next_level.append(no.right)
                current_level = next_level
            return max(values)
        return max_value_recusive(self.raiz)

    #décima primeira questão
    def is_valid_bst(self):
        def is_valid_bst_recursive(no, min_value=float('-inf'), max_value=float('inf')):
            if no is None:
                return True

            if not (min_value < no.value < max_value):
                return False

            #verifica-se apenas um lado, pois se um lado da árvore não está organizado
            #já não serve como uma árvore de busca
            left_valid = is_valid_bst_recursive(no.left, min_value, no.value)

            return left_valid
        return is_valid_bst_recursive(self.raiz)

    #décima segunda
    def remove_value(self,value):
        def find_min(node):
            aux = node
            while aux.left is not None:
                aux = aux.left
            return aux

        def delete_recursive(no, value):
            if no is None:
                return no

            if value < no.value:
                no.left = delete_recursive(no.left, value)
            elif value > no.value:
                no.right = delete_recursive(no.right, value)
            else:
                if no.left is None:
                    return no.right
                elif no.right is None:
                    return no.left

                temp = find_min(no.right)
                no.value = temp.value
                no.right = delete_recursive(no.right, temp.value)

            return no

        self.raiz = delete_recursive(self.raiz, value)

    #décima terceira
    def nivel_node_descendent(self,nivel):
        def nivel_node_descendent_recursive(no):
            if no is None:
                return 0
            current_level = [no]
            nodes = []
            while current_level:
                next_level = []
                for no in current_level:
                    if no.left is None:
                        nodes.append(no.value)
                    else:
                        nodes.append(no.value)
                    if no.left:
                        next_level.append(no.left)
                    if no.right:
                        next_level.append(no.right)
                current_level = next_level
            return nodes
        nos = nivel_node_descendent_recursive(self.raiz)
        level = 1
        if nivel == 0:
            return nos[level:]
        elif nivel == 1:
            level += 2
            return nos [level:]
        else:
            level = 2
            j = 2
            for i in range(nivel):
                j = j * 2
            return nos[j-level:]
    
    # décima quarta
    def root_node(self,no):
        def find_node_recursive(no, value, path):
            if no is None:
                return None

            path.append(no.value)

            if no.value == value:
                return path

            left_path = find_node_recursive(no.left, value, path.copy())
            if left_path:
                return left_path

            right_path = find_node_recursive(no.right, value, path.copy())
            if right_path:
                return right_path

            return None

        path_value = find_node_recursive(self.raiz, no, [])
        if path_value:
            return path_value
        else:
            return []

    #décima quinta
    def descendant_node(self,no):
        def find_node(no, value):
            if no is None:
                return None
            if no.value == value:
                return no
            left_result = find_node(no.left, value)
            if left_result:
                return left_result
            return find_node(no.right, value)

        def find_children(no):
            children = []
            if no is not None:
                if no.left is not None:
                    children.append(no.left.value)
                if no.right is not None:
                    children.append(no.right.value)
            return children

        nodo = find_node(self.raiz, no)
        if nodo:
            children = find_children(nodo)
            return children
        else:
            return []

