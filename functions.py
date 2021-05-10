def substituicao(A, B, C):
    if A == B:
        return C
    else:
        if len(A) == 1:
            return A
        if A[0] == '¬':
            return ('¬', substituicao(A[1], B, C))
        if type(A[1]) == str:
            return (substituicao(A[0], B, C), A[1], substituicao(A[2], B, C))


formula1 = ('¬', ('p', '∨', 'q'))
formula2 = ('o', '∨', 'r')
formula3 = ('p', '∧', 'q')
formula4 = ('s', '→', 't')

interpretacao = ('q', 'F')


def truth_value(formula, partial_interpretation):
    if formula[0] == '¬':
        if partial_interpretation[1] == 'T':
            return formula, '= F'
        else:
            return formula, '= T'

    if formula[1] == '→':
        if formula[0] == partial_interpretation[0] and partial_interpretation[1] == 'F':
            return formula, '=', partial_interpretation[1]
        if formula[2] == partial_interpretation[0] and partial_interpretation[1] == 'T':
            return formula, '=', partial_interpretation[1]
        else:
            return formula, '= F'

    if formula[0] == partial_interpretation[0] or formula[2] == partial_interpretation[0]:
        if formula[1] == '∧' or formula[1] == '∨':
            return formula, '=', partial_interpretation[1]


def get_domain(email):
    aux = email
    i = len(email) - 1
    aux2 = ''
    while(aux[i] != '@'):
        aux2 += email[i]
        i -= 1
    print(aux2[::-1])


def truth_value2(formula, partial_interpretation):
    if formula[1] == '>':
        if formula[0] == partial_interpretation[0] and partial_interpretation[1] == 'F':
            return formula, "= F"
        if formula[2] == partial_interpretation[0] and partial_interpretation[1] == 'T':
            return formula, "= T"
        else:
            return "Não é possível descobrir um valor-verdade"

    if formula[0] == partial_interpretation[0] or formula[2] == partial_interpretation[0]:
        if formula[1] == 'v' and partial_interpretation[1] == 'T':
            return formula, "= T"
        if formula[1] == '^' and partial_interpretation[1] == 'F':
            return formula, "= F"
        else:
            return "Não é possível descobrir o valor-verdade"
    else:
        return "Não é possível descobrir o valor-verdade"


outra_formula = ('o', 'v', 'r')
form = ('p', '^', 'q')
subs = ('s', '>', 't')

interpretacao = ('o', 'F')

print(truth_value(outra_formula, interpretacao))
