import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_soma():
    #given two values 
    valor_1 = 5 
    valor_2 = 3

    # when we calculate the soma
    output = methods.soma(valor_1, valor_2)
    
    # then the perimeter should be 14
    assert output == 8


def test_subtracao():
    #given two values 
    valor_1 = 10
    valor_2 = 4

    # when we calculate the subtracao
    output = methods.subtracao(valor_1, valor_2)
    
    # then the subtracao should be 6
    assert output == 6

def test_multiplicacao():
    #given two values 
    valor_1 = 5
    valor_2 = 7

    # when we calculate the multiplicacao
    output = methods.multiplicacao(valor_1, valor_2)
    
    # then the multiplicacao should be 35
    assert output == 35

def test_divisao():
    #given two values 
    valor_1 = 20
    valor_2 = 5

    # when we calculate the divisao
    output = methods.divisao(valor_1, valor_2)
    
    # then the divisao should be 4
    assert output == 4