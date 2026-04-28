# Improved Sample Access for Quantum-Inspired Algorithms

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
We have withdrawn our paper.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the topic of the quantum-inspired classical algorithm design, where in this field we usually analyze the speedups of the quantum ML algorithms by developing classical counterparts, and show that previous quantum algorithms do not give an exponential speedup. The paper analyzes two major subroutines: inner product estimation and sampling from a linear combination of vectors, which are based on the binary tree data structures proposed in Tang (2019). In particular, the paper extends to the $\ell_2$ guarantee to the $\ell_p$ guarantee in the sampling probability or the error dependence and shows the $\ell_1$ case has a better runtime than the $\ell_2$ case. Next, the paper gives a proof-of-concept example of downstream applications from the presented new subroutines.

### Strengths
1. The paper gives a new insight into the quantum-inspired ML algorithm design, which suggests considering the other $\ell_p$ norm subroutines might give faster such algorithms. This is interesting to me. The paper also gives a proof-of-concept example of the downstream applications.

### Weaknesses
1. From a technical perspective, the analysis of the new proposed subroutines seems to be straightforward, based on some variance argument. And despite the paper giving a proof-of-concept example, it is still not very clear the new subroutine can give a better bound for the downstream quantum-inspired ML algorithm. It will make the paper stronger if the authors can have more discussion about this.

### Questions
1. It seems the Proposition 4 (or Corollary 2) gives a constant improvement for the subroutine. From a complexity perspective, would it be possible for these new subroutines indeed improve the complexity of the previous quantum-inspired ML algorithms?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers quantum-inspired classical algorithms, presenting improved bounds for inner product estimation and sampling from linear combinations of vectors using a quantum-inspired classical data structure, SQ. Additionally, it discusses the applications of quantum-inspired algorithms in various specific settings.

### Strengths
This paper presents example-driven numerical experiments that demonstrate the effectiveness of quantum-inspired classical algorithms. This is intuitive and is uncommon in previous work on quantum-inspired algorithms.

### Weaknesses
1. My main concern is about the correctness of the optimality claim in Proposition 4 and Proposition 6. In particular, in the proof the authors only show that, for a specific kind of algorithm, $SQ_1$ input yields an optimal bound. However, the authors fail to argue that this specific kind of algorithm is optimal, i.e., ruling out the possibility that there might be some totally different algorithm that achieves the same task using $SQ_p$ for some $p\neq 1$ that has better bound.
2. The title seems a bit too vague, as quantum-inspired algorithms is a broad class of algorithms, but the authors only discussed a few examples among them.
3. I did not fully get the connection between Section 3 and later sections discussing the applications of quantum-inspired classical algorithms. It would be good for the authors to add some connecting paragraphs in between.
4. There are a good amount of typos in the paper. Examples: line 107, $L^p$ -> $L^p$-norm; line 125, vector -> a vector/the vector; line 170: should it be SQ(y) instead of Q(y)?; Wrong format for author middle names in references: Andrew J Baldwin -> Andrew J. Baldwin.

### Questions
I don't have more questions other than the ones above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The article studies the quantum-inspired classical algorithms for linear algebra and machine learning tasks. These algorithms are based on a data structured involving  binary search tree (BST), inspired by the QRAMs proposed for quantum data loading and computing. In this paper, generalization of this data structure is studied, where the tree nodes are pth norms of the columns of the data matrix. It is shown that under certain settings, $p=1$ norm based BST will be advantageous in terms of sampling complexity required for $\epsilon$ approximations. Two applications are  discussed for the new data structure and  optimal sample access is established. 
Numerical simulations are presented to illustrate the results.

### Strengths
Strengths:
1. Generalization  of the data structure used for  quantum-inspired classical algorithms is presented. 
2. Optimal sample access is established for certain type of vectors.
3. Two potential applications are studied for the generalized data structure.

### Weaknesses
Weakness:
1. Certain aspects of the study are unclear, making it hard to understand the contributions.
2. Significance of the study and results are unclear.

For details, see questions below.

### Questions
I have the following comments about the paper:

1.  Certain aspects of the study are unclear, and should be clarified.

i. The optimalilty/advantage for inner products estimation using the proposed SQ_p data structure seem to apply only when the vectors $x$ and $y$ have zero mean i.i.d random (Gaussian) entries. 
However, it is not obvious as to why the  elements of $x$ and $y$ have zero mean. We know that typically  these vectors represent quantum states, i..e, the entries are probabilities, and so  will be in [0,1]. So, these typically cannot be i.i.d zero mean Gaussian (uniform) random variables. Authors should discuss situations where such settings will occur. 

ii. Certain aspects of the optimality results established are not clear. The additive error guarantees (bounds) presented for SQ and SQ_p for the inner product estimation are different. When we set $p=1$, the additive error we obtain for SQ_p from Proposition 3 will be worse than the bound we have for SQ in Proposition 1. So, the sampling complexity comparison is not for the same error guarantee, it appears. Is this correct? Authors can clarify this.
 Similarly, for sampling from a linear combination of vectors, the output we obtain from SQ and  SQ_p  are different, ie.e, $D_{Ax}$ and $D^{(p)}_{Ax}$, respectively. We do not obtain samples for the same quantity using these two data structures. Therefore, it is not clear how do we compare the sample complexity for these two approaches, and claim that SQ_p  with p=1 has a better sample complexity, when the outputs or the error guarantees are different.  Authors can clarify these.

iii. Similar to the inner product case, for sampling from a linear combination of vectors too, it is not obvious as to why would the matrix  $A$ and the vector $x$  have i.i.d entries. Will this be the case for the two applications discussed.  Typically, data matrices $A$, do not have i.i.d entries. Authors can discuss settings where we encounter such i.i.d matrices and vectors.

iv. Motivation to use  a dequantized quantum classifiers can be further discussed. A discussion on why using such a classifier over existing (powerful) classical methods will be helpful. The quantum classifier such as the ones based on the parametrized quantum circuits  (PQC) are useful when the data is quantum in nature (e.g., comes from a quantum computation). Authors can discuss why using a classical algorithm for inner product estimation, within a quantum classifier will be beneficial.

2. Given the above, the significance of the proposed approach and results are not clear.  Authors can provide more details on these in order to improve the paper. 


3. Minor Comment:
i. In line 253, what is x? This variable is not defined.

### Soundness
2

### Presentation
3

### Contribution
2
