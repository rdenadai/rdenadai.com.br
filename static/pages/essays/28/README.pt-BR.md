## Introduction

Eu não sou um desses fanáticos por paradigmas de programação ou nada do gênero, mas sinto que tenho um ímpeto constante de buscar coisas novas e interessantes que possam atiçar minha curiosidade.

Recentemente rolou uma discussão no Bluesky, quando uma pessoa que acompanho postou uma imagem de código em F#. Dentre as discussões, foi levantada a questão de operações encadeadas usando algum tipo de operador.

Para quem está acostumado com linguagens funcionais (eu diria), esse operador faz parte do ferramental disponível para o programador. Entretanto, em muitas linguagens “clássicas” (vou me dar essa liberdade aqui, mas colocando aspas), isso é algo desconhecido pelos programadores ou, se existe, é pouco explorado devido ao mindset gerado ao longo de anos pelo denominado Paradigma Orientado a Objetos.

Somente fazendo um parêntese aqui: não culpo o Paradigma Orientado a Objetos por isso, mas talvez a área como um todo tenha prestado menos atenção a esse tipo de possibilidade e a como isso poderia gerar pipelines interessantes.

Dito isso, muitos acabam se “perdendo” na Orientação a Objetos ou ainda estão presos a uma codificação mais procedural. Não que isso seja um problema, muito pelo contrário: código funcionando é o que importa, mas, como escrevi no meu blog post anterior [The Last Programming Language you will Learn](https://www.rdenadai.com.br/essay/last-programming-language-you-will-learn), pode ser que eventualmente você acabe perdendo algo e tendo a oportunidade de mudar/melhorar o modo como você pensa e resolve um problema.

## The pipe operator

Bom, voltando ao tópico principal, o operador que foi discutido naquele post no Bluesky foi o conhecido pipeline operator.

Esse operador tem diversas formas de uso. Entretanto, F#, Elixir e OCaml utilizam os caracteres `|>`. Alguns exemplos para ilustrar.

```elixir
"Elixir rocks" |> String.upcase() |> String.split()
# ["ELIXIR", "ROCKS"]
```

```ocaml
"OCaml rocks" |> String.uppercase_ascii |> String.split_on_char ' '
(* - : string list = ["OCAML"; "ROCKS"] *)
```

Você pode consultar tanto a documentação do Elixir quanto a do OCaml a respeito do operador pipe:

- [Elixir: The pipe operator](https://hexdocs.pm/elixir/enumerable-and-streams.html#the-pipe-operator)
- [OCaml: The Pipe Operator](https://ocaml.org/docs/values-and-functions#the-pipe-operator)

Veja que, em linguagens em que o operador pipe não existe, teríamos duas formas de fazer isso.

### Encadeamento de funções

Muito parecido com o exemplo acima, porém mais agrupado. Vamos colocar a chamada de uma função como parâmetro da outra.

> Por favor, ignore o fato de eu estar escrevendo funções em Python que não fazem sentido; é apenas para ilustrar.

```python
def upper(s: str) -> str:
    return s.upper()

def split(s: str, char: str = " ") -> str:
    return s.split(char)

print(split(upper("Python rocks")))
# ["PYTHON", "ROCKS"]
```

### Method chaining

Muitas linguagens orientadas a objetos acabam adotando essa sintaxe para encadear métodos usando a notação de ponto (`.`), a fim de permitir operações semelhantes às que vemos com o operador pipe.

```python
print("Python Rocks".upper().split())
# ['PYTHON', 'ROCKS']
```

Dessa forma, temos algo muito parecido com o pipe operator, mas trabalhando com objetos.

## Why pipe operator matters?

Essa necessidade de uso do operador pipe aparece principalmente quando estamos trabalhando no primeiro caso acima (encadeamento de funções) e, no segundo, quando criamos um objeto que agrupa elementos e precisamos operar sobre eles.

Não que seja impossível não usar o pipe, mas, no fim, o código pode acabar ficando extenso e difícil de ler, principalmente em momentos em que criamos algum tipo de pipeline, em que vamos realizar diversas chamadas a diferentes funções para operar em um conjunto de dados.

Vamos a um exemplo em Python, relativamente simples e cheio de viés.

```python
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items: Any = []

    def add_item(self, item: Any):
        self.items.append(item)


shopping_cart = ShoppingCart()
shopping_cart.add_item(Product("Apple", 1.0))
shopping_cart.add_item(Product("Banana", 0.5))
shopping_cart.add_item(Product("Avocado", 2.0))
shopping_cart.add_item(Product("Pineapple", 3.0))
shopping_cart.add_item(Product("Grapes", 2.5))
```

Calma. Primeiro, estou apenas criando um exemplo bem simples. Agora, vamos filtrar todos os produtos com valores maiores que um, retornar seus nomes e imprimi-los.

```python
print(
    list(
        map(
            lambda p: p.name,
            filter(
                lambda p: p.price > 1.0,
                shopping_cart.items
            )
        )
    )
)
# ['Avocado', 'Pineapple', 'Grapes']
```

Eu coloquei de forma mais aberta aí de propósito, mas conseguimos ver o problema que o encadeamento de funções pode ocasionar: a ordem é do último para o primeiro.

Mas você, alguém que trabalha com Python, pode estar pensando: “mas eu posso fazer isso com compreensões de lista”, e, sim, você pode E DEVE, na verdade. Compreensões de lista (e, consequentemente, de dicionários e conjuntos) são sensacionais!

```python
print(
    [
        p.name
        for p in shopping_cart.items
        if p.price > 1.0
    ]
)
# ['Avocado', 'Pineapple', 'Grapes']
```

> P.S.: Gostaria que mais linguagens tivessem essa sintaxe de compreensões; elas são muito legais.

Apesar de tudo isso, há algo que me incomoda um pouco nas compreensões em Python (nada grave; só acho chato mesmo).

Se quisermos colocar um `else`, a estrutura da compreensão muda de forma mais drástica e passamos a usá-la como um ternário.

```python
print(
    [
        p.name if p.price > 1.0 else "Não encontrado"
        for p in shopping_cart.items
    ]
)
# ['Não encontrado', 'Não encontrado', 'Avocado', 'Pineapple', 'Grapes']
```

## Implementing a "pipe" operator

Ok, muito legal tudo isso, mas o exercício aqui é: seria possível criar algo parecido com o pipe operator em Python?

Bom, poderíamos modificar o CPython e acrescentar esse operador, o que seria algo bem trabalhoso, e já existiram diversas tentativas de adicionar tal operador (ou discussões em torno do mesmo) com suporte direto no Python e todas, por enquanto, não foram para frente. Eis alguns exemplos:

- https://discuss.python.org/t/pipe-operator/94333
- https://discuss.python.org/t/introduce-funnel-operator-i-e-to-allow-for-generator-pipelines/67701
- https://discuss.python.org/t/functools-pipe-function-composition-utility/69744

Mas nem por isso não podemos explorar e pensar se seria possível implementar tal operador na linguagem.

## Dunder methods

Uma grande peculiaridade que existe em Python são os conhecidos _dunder methods_ (ou **dunder**, como você pode encontrar por aí).

São métodos que existem em todos os objetos Python e respeitam o [Data Model](https://docs.python.org/3/reference/datamodel.html) da linguagem.

**_"Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects."_**

Isso implica que qualquer objeto que criamos possui uma abundância de _dunder methods_ que podemos implementar, e essa pode ser uma ideia interessante.

Se você procurar agora (sair do blog e ir na internet) por “pipe operator in Python”, você com certeza irá encontrar algum blog em que o autor implementou, usando classes e _dunder methods_, esse pipe com o caractere `|` (que também usamos como “ou” lógico).

Exemplo:

```python
result = (
  Pipe("data.csv")
  | load_csv
  | filter_data
  | summarize
).result()
```

A minha ideia vai nessa linha também: usar um dunder method para replicar isso; entretanto, apesar de o código acima ser possível, eu não o entendo como algo que seja o pipe operator.

Vimos acima como o operador funciona em Elixir e OCaml, e a minha ideia é tentar se aproximar ao máximo do mesmo funcionamento. Outra questão, para mim, seria o uso do | como operador.

## Implementation

Bom, outro operador que podemos usar e que, no caso, tem uso mais restrito seria o `>>`. Esse é um operador bit a bit (bitwise) e, com toda a certeza, seu uso é bem restrito, dependendo do tipo de projeto.

Escolhi-o por ter pouco uso e, consequentemente, ser visualmente melhor em comparação com o `|` (você pode discordar sem problemas).

Dito isso, ao olhar o Data Model do Python, encontramos o _dunder method_ `__rshift__` e seu par “oposto”, `__rrshift__`.

Perfeito, portanto, temos a seguinte classe:

```python
from __future__ import annotations

import inspect
from collections.abc import Callable, Iterator, Mapping, Sequence, Set
from functools import partial, reduce
from inspect import isclass
from typing import Any


class pipe:
    def __init__(self, func: Callable[..., Any]) -> None:
        self._func: Callable[..., Any] = func
        self._name: str = func.__name__ if hasattr(func, "__name__") else func.__class__.__name__

    def __rshift__(self, other: Any) -> Any:
        result = self._func
        if callable(result) and not isinstance(result, (pipe, partial)):
            result = result()
        return other._func(result)

    def __rrshift__(self, other: Any) -> Any:
        if isinstance(other, Iterator):
            return self._func(other)

        if isinstance(other, partial):
            return self._func(other())  # type: ignore

        if isclass(self._func):
            if issubclass(self._func, Sequence):
                return self._func(  # type: ignore
                    other
                    if isinstance(other, (Iterator, Sequence)) and not isinstance(other, (str, bytes, bytearray))
                    else [other]  # type: ignore
                )
            elif issubclass(self._func, Mapping):
                return self._func(other if isinstance(other, Mapping) else {other: other})  # type: ignore
            elif issubclass(self._func, Set):
                return self._func(other if isinstance(other, Set) or isinstance(other, Iterator) else {other})  # type: ignore
        try:
            signature = inspect.signature(self._func)
            if len(signature.parameters) > 1 and not inspect.isbuiltin(self._func):
                if isinstance(other, (Iterator, Sequence)):
                    return self._func(*other)
                elif isinstance(other, Mapping):
                    return self._func(**other)
        except ValueError:
            ...

        return self._func(other)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        if not args and not kwargs:
            return self._func()

        def partial_func(data: Any) -> Callable[..., Any]:
            if (
                isinstance(data, (Iterator, Sequence, Set, Mapping)) and not isinstance(data, (str, bytes, bytearray))
            ) or self._func is partial:
                if self._func is reduce:
                    return self._func(args[0], data, *args[1:])
                return self._func(*args, data, **kwargs)
            return self._func(*args, [data], **kwargs)

        return pipe(partial_func)
```

Sim, eu sei: muito código, gigante... muita coisa para desenrolar.

Mas tudo bem, a implementação também está longe de ser perfeita ou de funcionar para todos os tipos de casos, e não me atrevo a fazer uma implementação perfeita que também nunca seria usada.

Entretanto, funciona, e funciona muito bem para algumas coisas bem interessantes.

Um detalhe importante é que precisamos envelopar todas as nossas funções com essa classe, para que possamos “empilhar” umas às outras. Como talvez queiramos usar funções como `map`, `filter` etc., você precisaria fazer algo como:

```python
from functools import partial, reduce

from .pipe import pipe

map = pipe(map)
filter = pipe(filter)
reduce = pipe(reduce)
partial = pipe(partial)
to_list = pipe(list)
to_dict = pipe(dict)
to_set = pipe(set)
to_tuple = pipe(tuple)
pprint = pipe(print)
```

Com toda a certeza, qualquer programador Python, ao olhar as linhas acima, irá me amaldiçoar e a toda a minha linhagem, mas calma: isso são apenas “toy examples”; eu não espero que você faça isso em produção.

Mas, feito isso, podemos brincar à vontade com nosso novo operador!

```python
@pipe
def add_one(x: int) -> int:
    return x + 1

@pipe
def multiply_by_two(x: int) -> int:
    return x * 2

_ = (
    3
    >> add_one
    >> multiply_by_two
    >> map(lambda x: (x, x * 10))
    >> to_dict
    >> pprint
)
# {8: 80}
```

```python
_ = (
    [1, 2, 3, 4]
    >> map(lambda x: pow(x, 2))
    >> to_list
    >> pprint
)
# [1, 4, 9, 16]
```

Muito interessante, não? Mas calma: essa classe acaba utilizando um conceito bem interessante que temos em Python.

## Doing crazy with Generators

Eu não sei quantas foram as vezes em que eu estava escrevendo algum tipo de pipeline, ou modificando algum, em que eu precisava esperar por todos os dados em cada uma das etapas do pipeline para seguir para a próxima.

Um dia eu aprendi sobre _Generators_ e isso, com toda a certeza, mudou minha visão de como um processamento em sequência poderia ser parcial.

Não vou entrar em detalhes técnicos de como _Generators_ funcionam; você pode consultar o excelente livro do Luciano Ramalho, [Python Fluente](https://pythonfluente.com/2/#ch_generators), para entender como funcionam.

Mas, do modo como implementamos a classe _pipe_, ganhamos gratuitamente a execução parcial que um pipeline de _streaming_ com geradores nos proporcionaria!

```python
@pipe
def generator_func() -> Generator[int, None, None]:
    for i in range(6):
        print(">>>", i)
        yield i

def filter_divisible_by_3(x: int) -> bool:
    print(x % 2 == 0)
    return x % 2 == 0

def multiply_by_10(x: int) -> int:
    print(x * 10)
    return x * 10

print(">>> Start pipeline")
_ = (
    generator_func
    >> filter(filter_divisible_by_3)
    >> map(multiply_by_10)
    >> to_list
    >> pprint
)
# >>> Start pipeline
# >>> 0
# True
# 0
# >>> 1
# False
# >>> 2
# True
# 20
# >>> 3
# False
# >>> 4
# True
# 40
# >>> 5
# False
# [0, 20, 40]
```

É claro que a implementação é básica e isso não nos permite ir muito a fundo em como aninhamos nossas funções, principalmente quando usamos `map` e `filter`.

Em casos assim, você precisaria envelopar as funções dentro de um `lambda`, por exemplo:

```python
@pipe
def generator_func() -> Generator[int, None, None]:
    for i in range(6):
        print(">>>", i)
        yield i

def filter_divisible_by_3(x: int) -> bool:
    print(x % 2 == 0)
    yield x % 2 == 0

def multiply_by_10(x: int) -> int:
    print(x * 10)
    yield x * 10

print(">>> Start pipeline")
_ = (
    generator_func
    >> filter(lambda x: next(filter_divisible_by_3(x))) # Generators of generators
    >> map(lambda x: next(multiply_by_10(x)))
    >> to_list
    >> pprint
)
```

## Conclusion

Acredito que, como pequena prova de conceito de que seria possível escrever um operador de pipe para a linguagem Python, essa brincadeira foi de alguma valia, se não foi, caro leitor, tudo bem, me serviu para aprender algo.

A partir daqui não há muito o que fazer, exceto, talvez, melhorar a implementação para cobrir casos mais complexos e os buracos que deixei pelo caminho. Talvez até mudar o modo como estou relacionando cada chamada para evitar que a _stack_ fique sobrecarregada.

Penso que esse post foi mais um exercício de curiosidade para mim e espero que possa ter atiçado a sua curiosidade para tentar implementar um operador de pipe na sua linguagem, ou mesmo ir aprender mais sobre Elixir ou OCaml.

No mais, é isso. Happy coding 😆!
