
<p align="center">
    <img src="https://github.com/TheGreatestShoaib/MathSeq/blob/master/logo/finalmathseqlogo.png" alt="logo">
    <br/>
    <img src="https://img.shields.io/github/license/TheGreatestShoaib/MathSeq?color=blue&style=flat-square" alt="license">
    <img src="https://img.shields.io/github/stars/TheGreatestShoaib/mathseq?style=flat-square" alt="GitHub Repo stars">
    <img src="https://img.shields.io/github/forks/TheGreatestShoaib/mathseq?style=flat-square" alt="GitHub forks">
    <img src="https://img.shields.io/pypi/v/mathseq?style=flat-square" alt="PyPI">
</p>



<div align="center">
<h1> Mathseq </h1>
<br/>

<p>Mathseq is python library that helps to generate inifinite sequences real quick ..</p>

</div>
  
## Supported Sequences

- Fibonacci

- Lucas Number

- Prime Number
    - end (Positional Argument)

- Catalan Number

- Vaneck's sequence

- Composite Numbers

- Pronic Numbers

- Random sequence
    - seed
    - type

- Look and say
    - inverse

<br>

## Installation
<br>

**Using pip** 

    $ pip install mathseq

<br>

## Usage
<br>

**Imports**

```python

>>>from mathseq import seq

```
<br>

**Create Objects**

```python

>>>from mathseq import seq
>>>
>>>fibonacci = seq.fibonacci()
>>>fibonacci
<generator object fibonacci at 0x0000020F83BEC648>
>>>

```
<br>

**Iteration**


```python

from mathseq import seq

fibonacci = seq.fibonacci()

#printing through desired range
desired_range = 10
for _ in range(desired_range):
    fib = next(fibonacci)
    print(fib)


#keep generating to the infinity
for fib in fibonacci:
    print(fib)

```

<br>

**Use List Comprehension**
<br>

```python


from mathseq import seq

fibonacci = seq.fibonacci()
catalan = seq.catalan_numbers()

fib_list = [next(fibonacci) for _ in range(10)]
cat_list = [next(catalan) for _ in range(10)]

print("List of Fibonacci Numbers",fib_list)
print("List of Catalan Numbers",cat_list)

```
<br>


## License

[MIT](https://choosealicense.com/licenses/mit/)

## Authors

- [@Shoaib Islam](https://www.github.com/TheGreatestShoaib)

<br>

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

  


  
