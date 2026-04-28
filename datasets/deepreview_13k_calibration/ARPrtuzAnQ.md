# On the hardness of learning under symmetries

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 6, 8

## Abstract
We study the problem of learning equivariant neural networks via gradient descent. The incorporation of known symmetries (``equivariance'') into neural nets has empirically improved the performance of learning pipelines, in domains ranging from biology to computer vision. However, a rich yet separate line of learning theoretic research has demonstrated that actually learning shallow, fully-connected (i.e. non-symmetric) networks has exponential complexity in the correlational statistical query (CSQ) model, a framework encompassing gradient descent. In this work, we ask: are known problem symmetries sufficient to alleviate the fundamental hardness of learning neural nets with gradient descent? We answer this question in the negative. In particular, we give lower bounds for shallow graph neural networks, convolutional networks, invariant polynomials, and frame-averaged networks for permutation subgroups, which all scale either superpolynomially or exponentially in the relevant input dimension. Therefore, in spite of the significant inductive bias imparted via symmetry, actually learning the complete classes of functions represented by equivariant neural networks via gradient descent remains hard.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the hardness of learning certain two-layer or one-hidden-layer neural networks under symmetrized architecture/algorithmic designs on Gaussian inputs, via the Statistical Query (SQ) lower bound techniques. It provides several results characterizing the hardness of learning GNNs and CNNs via leveraging correlational SQ (CSQ) lower bounds for learning boolean functions and by connecting them with learning parity functions. It also discussed when CSQ lower bounds can be different than SQ lower bounds.

### Strengths
1. The question studied in this paper is closely related to a core question in understanding deep learning, that is: can deep learning benefit from symmetry-inspired algorithmic designs? In this sense I deem the question studied in the paper valuable and this paper's attempt to deal with it respectful.
2. The technical contribution of this paper, although still depended on some prior works, is novel enough to my understanding to be nontrivial. This paper constructed function classes that were not studied before to specifically deal with their problems, and proved hardness of learning these classes, which is a notable effort. 
3. This paper covers both GNN and CNNs, and discussed the difference between CSQ and SQ in certain scenarios, which is good for completeness.

### Weaknesses
The weaknesses listed below are, in my opinion, secondary to the contributions of this paper.
The approach of this paper in studying the hardness of learning symmetry-enhanced neural networks has certain limitations. It cannot account for all neural architectures at once and requires specific construction whenever the problem formulation changes by a little bit. For instance, the specific hard function classes constructed, while effective for the proofs, lack intuitive connections to practical scenarios. The reliance on carefully crafted, non-standard function classes makes it difficult to generalize the findings to more commonly used architectures or learning tasks. The paper does not provide sufficient justification for why these specific function classes are representative of the challenges faced in learning with symmetric architectures beyond the immediate proof context. Furthermore, the paper's analysis could be strengthened by a more detailed discussion of how the derived lower bounds relate to the practical performance of these networks, especially given that SQ lower bounds can sometimes be loose in practice. A more thorough discussion of the limitations of the SQ framework in the context of neural network learning would also be beneficial.

### Questions
None

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work considers the problem of learning symmetric Neural Networks.  The
authors provide hardness results for Statistical Query (SQ) and Correlational
Statistical Query (CSQ) algorithms (and an NP-Hardness result for properly
learning Graph Neural Networks (GNNs)).  An example of a symmetric neural
network is a 2-layer GNN that maps an input graph $A$ to $g(f(A))$, where
$f:\{0, 1\}^{n \times n} \mapsto R^k$ first aggregates $k$ permutation
invariant features of the input graph $A$ and $g$ is a one-hidden layer MLP.

The first result is an SQ hardness result for two-layer GNNs showing that for
the above class of GNNs $\tau^2 2^{n^{\Omega(1)}}$ queries of tolerance $\tau$
are required.  The result follows by designing a 2-layer GNN where the
$i$-output of the first layer counts how many nodes have $i-1$ outgoing edges
and the second layer selects a subset of those counts and computes its parity.
By using properties of GNP graphs, the authors reduce the problem to the
well-known hard problem of learning parity functions over the uniform
distribution on the $n$-dimensional Boolean hypercube.

The second result considers GNNs that take as input a $n \times d$ feature
matrix $X$ and then compute $1_n^T \sigma(A(G) X W) a$, for an adjacency matrix
$A(G) \in \{0,1\}^n$,a weight $d \times 2 k$ matrix $W$ and a $2k$-dimensional
weight vector $a$.  They give a $d^k$ CSQ lower bound for this problem.  This
result follows from adapting the hard instances of the CSQ lower bound
construction of [2].

The third result shows that for CNNs (and more general frame-averaged networks)
of the form $f(X) = 1/|G| \sum_{g \in G} a^T \sigma (W^T g^{-1} X) 1_d$ where
$X$ is a $n \times d$ input matrix, $G$ is a group acting on $R^n$ (e.g., could
be cyclic shifts) either requires $2^{n^{\Omega(1)}}/ |G|^2$ queries or a query
with precision $|G| 2^{-n^{\Omega(1)}} + \sqrt{|G|} n^{-\Omega(k)}$.  The proof
of this results also adapts the construction of [2] For more general
frame-averaged networks, the authors use the techniques developed in [1] to
show a super-polynomial CSQ lower-bound (for any constant c either $n^{\log n}$
queries are needed or a query with accuracy $n^{-c}$).


[1] Surbhi Goel, Aravind Gollakota, Zhihan Jin, Sushrut Karmalkar, and Adam Klivans. Superpolynomial lower bounds for learning one-layer neural networks using gradient descent.
ICML 2020.

[2] Ilias Diakonikolas, Daniel M Kane, Vasilis Kontonis, and Nikos Zarifis. Algorithms and sq lower bounds for pac learning one-hidden-layer relu networks. COLT 2020.

### Strengths
1. The problem considered in this work is interesting and well-motivated. Most theoretical prior works on learning neural networks focused on fully connected shallow networks; investigating the learnability of popular and practically relevant classes of neural networks such as GNNs and CNNs (that have more restricted symmetric structure) is a natural
next step.

2. The paper provides hardness results for various classes of ``symmetric'' neural networks in the SQ and CSQ models that are general models of computation capturing, for example, stochastic gradient descent algorithms.

3. I found the paper to be well-organized and written. The authors clearly state what results of prior works they rely on to get their results.

### Weaknesses
1. The novelty of the technics and arguments used in the lower bounds provided in this work may be limited in the sense that most of the claimed results rely heavily on machinery developed in the prior works [1,2]. Specifically, the adaptation of the techniques from [2] for the CSQ lower bounds, while non-trivial, does not introduce fundamentally new proof strategies. The core ideas of constructing hard instances and leveraging the properties of parity functions are largely inherited, with modifications primarily focused on adapting to the specific symmetric network architectures considered in this paper.

2. While the authors clearly state which lemmas and proofs of the prior works they are using, I think a more detailed high-level explanation of the arguments and the differences from prior work should appear in the main body of the paper. For instance, when adapting the construction from [2] for frame-averaged networks, the specific challenges and modifications required to handle the group averaging operation are not sufficiently highlighted. A more in-depth discussion of how the group structure interacts with the hard instance construction would be beneficial.

### Questions
1. See weaknesses. 

2. While the authors clearly state which lemmas and proofs of the prior works they are using, I think a more detailed high-level explanation of the arguments and the differences from prior work should appear in the main body of the paper.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the computational hardness of learning equivariant networks using gradient descent.  They show that enforcing symmetries like permutation invariance does not make learning any substantially easier, and that their hardness results hold even for shallow 1-layer GNNs and CNNs.  They provide statistical query (SQ) lower bounds that scale exponentially with feature dimensions for various architectures.  Additionally, the authors provide an efficient non-gradient based algorithm for learning sparse invariant polynomials, separating SQ and correlational SQ complexity.  Lastly, they perform numerous experiments to verify their results.

### Strengths
Originality:

The authors prove numerous new results on the sample complexity of learning in neural networks, and provide ample empirical support for their work.

Quality/clarity:

The authors sketch their proofs using careful, clear technical arguments.  Additionally, their experiments are simple, but clear demonstrations of the practical difficulty of learning networks within the families they authors study.

Significance:

The author's work significantly advances progress on the hardness of learning symmetric networks, opening the door to clear avenues of future, follow-up work.

### Weaknesses
I would've liked a _slightly_ more thorough empirical treatment, if only to make sure that the failure to learn was not due to poor hyperparameter choices / poor initialization etc.

### Questions
Could the authors comment more on the applicability of "worst-case" reasoning re: the likelihood of these function classes to well-describe nature?  It seems plausible that the worst case could be significantly harder than the typical case for problems that we care about.  In practice, these sorts of hardness results don't seem to impact practitioner's usage of these model classes much at all!

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
