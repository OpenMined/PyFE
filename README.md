# PyFE

A library for running Functional Encryption on tensors

## What is Functional Encryption?

Functional encryption (FE) is a generalization of public-key encryption in which possessing a secret key allows one to learn a function of what the ciphertext is encrypting. Functional encryption extends the notion of public key encryption where one uses a public key `pk` and a secret key `sk` to respectively encrypt and decrypt some data. More precisely, `pk` is still used to encrypt data, but for a given function f, `sk` can be used to derive a functional decryption key `dkf`
which will be shared to users so that, given a ciphertext of `x`, they can decrypt `f(x)` but not `x`. In
particular, someone having access to `dkf` cannot learn anything about `x` other than `f(x)`. Note also
that functions cannot be composed, since the decryption happens within the function evaluation.
Hence, only single quadratic functions can be currently securely evaluated.

**Perfect correctness**: Perfect correctness is achieved in functional encryption: ∀x ∈ X , f ∈ F,
Pr[Dec(dkf , ct) = f(x)] = 1, where dkf ← KeyGen(msk, f) and ct ← Enc(pk, x). Note that this
property is a very strict condition, which is not satisfied by exisiting fully homomorphic encryption
schemes (FHE),


## How it helps in deep learning ?

It will mask the private data and allow to evaluate a pre-trained model thanks to its decryption key `dkf`

## Installation

```
pip install PyFE
```

# Usage

[] to do
