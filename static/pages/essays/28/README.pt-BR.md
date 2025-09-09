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

from collections import deque
from collections.abc import Callable, Generator, Iterator, Mapping, Sequence, Set
from functools import partial
from typing import Any


class pipe:
    def __init__(self, func: Callable[..., Any]) -> None:
        self._func = func
        self._name = func.__name__ if hasattr(func, "__name__") else func.__class__.__name__

    def __rshift__(self, other: Any) -> Any:
        result = self._func
        if callable(result) and not isinstance(result, (pipe, partial)):
            result = result()
        self._func = other._func
        self._name = other._name
        return self.__rrshift__(result)

    def __rrshift__(self, other: Any) -> Generator[Any, None, None] | Any:
        if (
            (isinstance(other, (Iterator, Sequence)) and self.__not_str_bytes(other))
            or isinstance(other, Mapping)
            or isinstance(other, Set)
        ) and not hasattr(self._func, "_materialize"):
            return self.__stream__(other)
        return self._func(other)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        return self._func(*args, **kwargs)

    @staticmethod
    def filter(func: Callable[..., bool]) -> pipe:
        def __filter(data: Any) -> Generator[Any, None, None]:
            result = func(data)
            result = next(result) if isinstance(result, Generator) else result
            if result:
                yield data

        return pipe(__filter)

    @staticmethod
    def reduce(
        func: Callable[..., Any] | None = None,
        *,
        initializer: Any = None,
    ) -> Callable[[Callable[..., Any]], pipe]:
        _initializer = initializer

        def __reduce_dec(func: Callable[..., Any]) -> pipe:
            def __reduce(data: Any) -> Any:
                nonlocal _initializer
                if _initializer is None:
                    _initializer = data
                    yield data
                else:
                    result = func(_initializer, data)
                    _initializer = next(result) if isinstance(result, Generator) else result
                    yield _initializer

            return pipe(__reduce)

        if func is not None:
            return __reduce_dec(func)
        return __reduce_dec

    def __stream__(self, other: Any) -> Generator[Any, None, None]:
        def __generator_result(item: Any) -> Generator[Any, None, None]:
            result = self._func(item)
            if isinstance(result, Generator):
                yield from result
            else:
                yield result

        if isinstance(other, Mapping):
            yield from __generator_result(other)
        elif getattr(self._func, "__name__", None) == "__reduce":
            yield deque((next(__generator_result(item)) for item in other), maxlen=1).pop()
        else:
            for item in other:
                yield from __generator_result(item)

    def __not_str_bytes(self, item: Any) -> bool:
        return not isinstance(item, (str, bytes, bytearray))
```

Sim, eu sei: muito código, gigante... muita coisa para desenrolar.

Mas tudo bem, a implementação também está longe de ser perfeita ou de funcionar para todos os tipos de casos, e não me atrevo a fazer uma implementação perfeita que também nunca seria usada.

Entretanto, funciona, e funciona muito bem para algumas coisas bem interessantes.

Um detalhe importante é que precisamos envelopar todas as nossas funções com essa classe, para que possamos “empilhar” umas às outras.

Para alguns casos, já criei alguns helpers para facilitar.

```python
from collections.abc import ItemsView, Iterator, Mapping, Sequence
from collections.abc import Set as _Set
from functools import partial
from typing import Any

from src.pipe import pipe
from src.support.utils import from_generator, materialize

STRUCTURAL_TYPES = (Sequence, Iterator, Mapping, _Set, ItemsView)

Parcial = lambda func, *args, **kwargs: pipe(partial(func, *args, **kwargs))
Print = pipe(print)


@materialize
def to_value(data: Any) -> Any:
    return from_generator(data)


class List:
    @materialize
    @staticmethod
    def to_value(data: Any) -> list:
        if isinstance(data, list):
            return data
        elif not isinstance(data, STRUCTURAL_TYPES):
            return [data]
        return list(data)


class Dict:
    @materialize
    @staticmethod
    def to_value(data: Any) -> dict:
        data = from_generator(data)
        if isinstance(data, dict):
            return data
        elif isinstance(data, (Sequence, Iterator)):
            return dict(data)
        else:
            return {data: data}


class Set:
    @materialize
    @staticmethod
    def to_value(data: Any) -> set:
        if isinstance(data, set):
            return data
        elif not isinstance(data, STRUCTURAL_TYPES):
            return {data}
        return set(data)


class String:
    @materialize
    @staticmethod
    def to_value(data: Any) -> str:
        return str(from_generator(data))


class Tuple:
    @materialize
    @staticmethod
    def to_value(data: Any) -> tuple:
        if isinstance(data, tuple):
            return data
        elif not isinstance(data, STRUCTURAL_TYPES):
            return (data,)
        return tuple(data)
```

Mas, feito isso, podemos brincar à vontade com nosso novo operador!

```python
@pipe
def add_one(x: int) -> int:
    return x + 1

@pipe
def multiply_by_two(x: int) -> int:
    return x * 2

result = 3 >> add_one >> multiply_by_two >> Dict.to_value
assert result == {8: 8}
# {8: 8}
```

```python
class Person:
    __slots__ = ("name", "age")

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

@pipe.filter
def is_adult(person: Person) -> bool:
    return person.age >= 18

data = [Person("Alice", 17), Person("Bob", 20), Person("Charlie", 15), Person("David", 22)]
result = data >> is_adult >> List.to_value
assert [person.name for person in result] == ["Bob", "David"]
# ["Bob", "David"]
```

Muito interessante, não? Mas calma: essa classe acaba utilizando um conceito bem interessante que temos em Python.

## Doing crazy with Generators

Eu não sei quantas foram as vezes em que eu estava escrevendo algum tipo de pipeline, ou modificando algum, em que eu precisava esperar por todos os dados em cada uma das etapas do pipeline para seguir para a próxima.

Um dia eu aprendi sobre _Generators_ e isso, com toda a certeza, mudou minha visão de como um processamento em sequência poderia ser parcial.

Não vou entrar em detalhes técnicos de como _Generators_ funcionam; você pode consultar o excelente livro do Luciano Ramalho, [Python Fluente](https://pythonfluente.com/2/#ch_generators), para entender como funcionam.

Mas, do modo como implementamos a classe _pipe_, ganhamos gratuitamente a execução parcial que um pipeline de _streaming_ com geradores nos proporcionaria!

```python
class Product:
    __slots__ = ("name", "price")

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

cart = ShoppingCart()
cart.add_product(Product("Laptop", 999.99))
cart.add_product(Product("Mouse", 25.50))
cart.add_product(Product("Keyboard", 45.00))
cart.add_product(Product("Monitor", 150.75))

@pipe
def apply_discount(product: Product) -> Product:
    product.price *= 0.9  # Apply a 10% discount
    yield product

@pipe.filter
def filter_expensive_products(product: Product) -> bool:
    yield product.price > 50

@pipe.reduce(initializer=0.0)
def sum_prices(x: float, y: Product) -> float:
    yield x + y.price

discounts = cart.products >> apply_discount >> List.to_value
assert all(
    abs(p.price - original_price * 0.9) < 1e-2
    for p, original_price in zip(discounts, [999.99, 25.50, 45.00, 150.75])
)

filtered_expensive = cart.products >> apply_discount >> filter_expensive_products >> List.to_value
assert len(filtered_expensive) == 2  # Laptop and Monitor
assert all(p.price > 50 for p in filtered_expensive)

total = cart.products >> apply_discount >> filter_expensive_products >> sum_prices >> to_value

assert round(total, 2) == 838.88  # Total price after discount for Laptop and Monitor
```

É claro que a implementação é básica e isso não nos permite ir muito a fundo em como aninhamos nossas funções, principalmente quando usamos `map` e `filter`.

Em casos assim, você precisaria envelopar as funções dentro de um `lambda`, por exemplo:

```python
@pipe
def random_number(N: int) -> int:
    yield random.randint(1, 100)

numbers = range(5) >> random_number >> List.to_value
assert len(numbers) == 5
assert all(1 <= num <= 100 for num in numbers)
# [69, 34, 2, 17, 90]  # Example output, will vary each run
```

## Conclusion

Acredito que, como pequena prova de conceito de que seria possível escrever um operador de pipe para a linguagem Python, essa brincadeira foi de alguma valia, se não foi, caro leitor, tudo bem, me serviu para aprender algo.

A partir daqui não há muito o que fazer, exceto, talvez, melhorar a implementação para cobrir casos mais complexos e os buracos que deixei pelo caminho. Talvez até mudar o modo como estou relacionando cada chamada para evitar que a _stack_ fique sobrecarregada.

Penso que esse post foi mais um exercício de curiosidade para mim e espero que possa ter atiçado a sua curiosidade para tentar implementar um operador de pipe na sua linguagem, ou mesmo ir aprender mais sobre Elixir ou OCaml.

Se você quiser o código completo, ele está [AQUI](https://github.com/rdenadai/pipe)!

No mais, é isso. Happy coding 😆!
