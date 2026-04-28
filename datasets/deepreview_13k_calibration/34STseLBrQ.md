# Polynomial Width is Sufficient for Set Representation with High-dimensional Features

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
Set representation has become ubiquitous in deep learning for modeling the inductive bias of neural networks that are insensitive to the input order.
DeepSets is the most widely used neural network architecture for set representation. It involves embedding each set element into a latent space with dimension $L$, followed by a sum pooling to obtain a whole-set embedding, and finally mapping the whole-set embedding to the output. In this work, we investigate the impact of the dimension $L$ on the expressive power of DeepSets.
Previous analyses either oversimplified high-dimensional features to be one-dimensional features or were limited to complex analytic activations, thereby diverging from practical use or resulting in $L$ that grows exponentially with the set size $N$ and feature dimension $D$.
To investigate the minimal value of $L$ that achieves sufficient expressive power, we present two set-element embedding layers: (a) linear + power activation (LP) and (b) linear + exponential activations (LE).
We demonstrate that $L$ being $\poly(N, D)$ is sufficient for set representation using both embedding layers. We also provide a lower bound of $L$ for the LP embedding layer. Furthermore, we extend our results to permutation-equivariant set functions and the complex field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
## High level summary 
This paper delves into the question of representations of sets as continuous functions in vector spaces. The work builds up on the ideas proposed in DeepSet, which shows that proves any permutation-invariant continuous function, can be restated by mapping each element to a vector, summing those vectors, and then mapping them to a scalar again. This paper addresses the unresolved question, whether sets over high-dimensional vectors can be represented efficiently, i.e., polynomially wrt to the set and feature size. 

More formally, $X\in R^{N\times D}$ represents $N$ feature vectors of dimension $D,$ and function $f:R^{N\times D} \to R$ is defined to be permutation-invariant if for any permutation matrix $P$ it satisfies $f(P X) = f(X).$  The main contributions of the paper can be enumerated as
- Thm 3.1 asserts that there $\phi:R^D\to R^L$ and $\rho:R^L\to R$ such that $f$ can be re-written as $f(X) = \rho(\sum_{i=1}^N \phi(x^{(i)}))$ where $L$ is at most polynomial wrt to $N$ and $D$, with two different constructions that authors refer to as "power mapping " and exponential activation". The theorem further asserts that $L$ is lower-bounded roughly by $ND$. 
- Thm 5.1 further shows that permutation equivariant functions, i.e., $f:R^{N\times D}\to R^{N\times D'}$ such that  $f(P X) = P f(X),$ then there are $\phi:R^D\to R^L$ and $\rho:R^D\times R^L\to R$ such that $f(X)_j = \rho\left(x^{(j)}, \sum_i^N \phi(x^{(i)})\right)$ where again $L$ is polynomial in $N$ and $D$. 

## Technical summary 

*Set representation for one-dimensional elements $D=1$* The previous result proves that when $D=1$ there are $\phi:R\to R^L$ and $\rho:R^L\to R$ such that $f = \rho(\sum_i^N \phi(x_i)$). This result mostly hinges on a particular function, referred to as power-mapping $\Psi_N :R^N\to R^N$, defined as  $\Psi_N(X)_k = \sum_i^N (x^{(i)} )^k.$ The paper goes on to explain that $\Psi_N$ is "bijective" in a particular sense that deviates from the standard definition, in that $\Psi_N(X) = \Psi_N(X')$ implies rows of $X$ are a permutation of $X'.$ This allows us to introduce the mapping and its inverse as an identity and conclude $ f = f \circ \Psi_N^{-1} \circ \Psi_N  = \rho(\sum_i^N \phi(X))$ where $\rho:= f\circ \Psi_N^{-1}$ and $\phi:= \psi_N$. 

*The channel alignment problem in $D\ge 2$* The first insight is explaining that the straightforward approach of representing each channel (dimension) of the high-dimensional features, will not work. This is because the mapping $\Psi_N:R^N\to R^N$ is permutation-invariant, meaning that while extending it to high dimension will preserve permutation invariance across each channel, these permutations are not going to be necessarily the same, referred to as alignment. This means that while we can ensure that while the naive approach ensures that each channel is preserved with permutation invariance, these permutations are not necessarily the same, and thus the vectors structure, where indices of vector do matter, may be lost. 

*Linearly lifting dimension to $L$ to resolve alignment* The main idea behind the proposed theory, as far as I can understand, is how to prevent this *alignment problem* by linearly lifting the $D$-dimensional elements to a much higher dimension $L$ that has lots of redundancies. Crucially, this lifting has the property channels of two different matrices after lifting can be aligned independently, then one matrix is a row-permutation of another.

Here I will summarise the more detailed theoretical insights I can draw from various parts of the paper 
- *Anchor.* The main idea for the entire theoretical construction in fact develops on top of this alignment problem, suggesting a way to "anchor" different channels. The theoretical construct. Formally, anchor $a\in R^N$ for data $X \in R^{N\times D}$, preserves the equality structure of the rows of $X$: $x^{(i)}\neq x^{(j)}\implies a_i\neq a_j$.  
- *Coupling of alignment with anchor.* If $a$ is an anchor of $X$, and $a'$ is a permutation of $a,$ and same permutation $P$ can be applied on every channel of $X$ to transform to the equivalent channel of $X'$, then rows of $X$ are a permutation of rows of $X'$. Thus, we can couple the alignment of various channels to the alignment of $a$ to $a',$ we can easily conclude that $X\sim X'$ 
-  *Linear probes for anchors. * We can pick linear probes $w_1,\dots, w_k\in R^D,$ such that for any matrix $X,$ at least one of the $X w_1,\dots, X w_k$ must be an anchor of $X$. This is achieved by picking a large enough $K$, and $w_k$'s such that every subset of size $D$ will be linearly independent, i.e., in general position, which is achievable by simply drawing from some Gaussian multivariate distribution. The claim follows from a cute pigeonhole principle. Now, if we do set representation of all $x^{(i)}$ and these linear probes $X w_k$'s, we can ensure that each of them are injective, and at least one of the $X w_k$'s is an anchor, but we still haven't coupled the alignment of the anchor to the rest of the channels. 
- *Coupling channel alignments to the anchor* Next, authors prove existence of coefficients $\gamma_1,\dots, \gamma_K$ such that if$x\sim x', y\sim y'$ and  $x - \gamma_k y$ is a permutation of $x' - \gamma_k y'$ for every $k = 1, \dots, K$, then permutation of $x\sim x'$ and $y\sim y'$ can be aligned. 
- *Lifting* Here, using the linear probes $w_k$ and coefficients $\gamma_k$'s from previous step, we can define lifting operator colums  $w_{i,j,k} = e_i - \gamma_k w_j$  for a polynomial range of $i,j,k$, and put all of them as columns of the lifting linear $W \in R^{D\times L}.$ Then each channel (column) of $Y = X W$ will be of the form $x^{(i)} - \gamma_k X w_j.$ Therefore, by previous properties, if every channel (column) of $X W$ can be aligned to (is a permutation of) $X' W$, then rows of $X$ are a permutation of $X'.$ The *set representation* of each channel will follow naturally from this step.

### Strengths
Here are the main strengths I find in the appear:
- The theory of the paper, to be best of my understanding, is sound and accurate. The statement of the theorems, lemmas, and the proofs, as much as I delved into, are sound and clearly stated. 
- The main problem that this paper focuses on, is a natural abstraction of real-world problems. 
- There are many clever and intuitive proof techniques used in this work, which may be interesting for the reader

### Weaknesses
Main issues: 
- While the paper presents a mathematically intriguing case, I am not quite sure what to draw from it from a machine learning perspective.  While theoretical contributions should certainly be welcome in the ML field, I think the theoretical works should take a few steps in demonstrating the relevance of their results for the broader community. For example, are there any concrete examples or use cases that these theoretical findings would be relevant? Specifically, while the paper demonstrates the existence of a polynomial-sized embedding, it does not provide any guidance on how this embedding can be constructed or learned in practice. The theoretical result is not tied to any practical algorithm, limiting its impact on the field.
- Following up on the previous point, despite the embedding-sum decomposition, the construction of the $\rho$ function $\rho:R^L \to R$ is still a complete black box. Again, these non-constructive arguments do not seem to add up to any "practical insight." While this is not a 100% a critical point, if authors can think of ways to make it easier for the reader to imagine applications, they would broaden their audience and enhance the impact of the paper.  The paper proves the existence of such a function, but does not provide any details on its structure, complexity, or how it can be implemented. This makes it difficult to translate the theoretical results into practical applications.
- While the paper is mathematically sound, it could benefit from more high-level idea developments both before and after the theorems. There are several places where a geometric interpretation is available, but not discussed in the main text. For example in the proof of Lemma 4.2 it becomes clear that a system of $w_k$'s in general position, if there are "enough" of them, at least one will be one that is not in the hyperplane orthogonal to difference between each two columns of $X$, perhaps this can even be visualised for some toy example with $D=2$ and $N=3.$ With the intuition that authors have built upon this case, if they are able to come up with more intuitive/visual depiction of these concepts, it would dramatically improve the paper's readability and accessibility. The lack of geometric intuition makes the proofs harder to grasp and limits the broader understanding of the core ideas.

 Minor issues:
- The notion of injectivity for functions (Def 2.7), that $f(X) = f(X')$ implies rows of $X$ are a permutation of rows of $X'$, slightly deviates from the standard notion that assumes "a function f that maps distinct elements of its domain to distinct elements." It took me quite a few iterations to notice this slight difference. Perhaps author can caution the reader before or afterwards. Most readers will be inclined to assume the "default" notion which could lead to some confusions later on. 
- The notation $[a\ x]\sim [a'\ x']$ which (for example used in Lemma 4.2) is somewhat ambiguous. Initially, I interpreted it as concatenating the two vectors along their main axis $[a\ x] \in R^{2N}$ which leads to lots of contradictions, while the authors implied stacking them along a new dimension $[a\ x]\in R^{2\times N}$ which makes sense. While this might be consistent with the papers notation elsewhere, it is still good and helpful to highlight it for the readers that this implies stacking them and not concatenation.  
- "Comparison with Prior Arts"? I'm guessing authors mean "articles" here? Is this a common shorthand for articles? While I don't want to sound authoritative, this seems like a rather informal writing style.
- (page 17) "pigeon-hold principle" I'm guessing authors refer to "pigeonhole principle" :)

### Questions
- The main results of this paper are obtained for a notion of permutation-invariance of $f,$ which is somewhat strictly defined over the entire input set $X.$ In real world applications, often the feature vectors $x$ represent learned or encoded features of a particular dataset. So in these cases, the "user" will be interested in "relaxed set preserving properties", in the sense that permutation invariance is only held over a subset (possibly even countable subset) of $R^{N\times D}$. Can authors think of any interesting relaxations  on $X$ and extend their theory for those? (assuming it has certain properties or its feature vectors are chosen from a smaller/finite set)
- Upon reading the paper, the architecture that authors propose resembles a network with depth "2" (perhaps this mysteriously encoded $\rho$ , which in reality could be a highly complex $R^L\to R$ function). In certain scenarios, there could be a hierarchical set representations, e.g., we want to embed sets of sets of sets, (or even more). Can authors comment on extendability of their theory, or in general any comments they may have for such multilevel/hierarchical sets?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a theoretical bound for the size of the embedding dimension of permutation invariant set functions which is not restricted to a single feature dimension, as some previous works.

### Strengths
- The problem is very relevant, as many works which utilize permutation invariant functions do not consider the importance of the embedding dimension.
- The derivation in the text appears thorough and rigorous

### Weaknesses
 - It took me a while to grasp the concept of anchors. In lemma 4.2 I think it needs to be stressed that the same anchor is being applied over all the channels. Although the notation states this, it would be good to state it in plain text as well.
- Under Lemma 4.2 there is a sentence which says "then once each coupled pairs are aligned, two data matrices are globally aligned." Can you elaborate on the precise meaning of this sentence? What does "aligned" and "globally aligned" signify? Specifically, it is not clear how the alignment of individual pairs implies a global alignment of the matrices. The notion of alignment itself needs more rigorous definition in the context of set functions and permutation invariance.
- Why is Lemma 4.4 necesary? I do not see the reason for this, and I do not think it is explained well in the text either. At the beginning of page 8, it is stated that: "Eq. 5 implies Eq. 6, but none of these seem to depend on Lemma 4.4 or "Contruction point #3" so I am not sure why it is necessary. I think this needs to be explained better in the text. It is unclear how the construction in Lemma 4.4, which involves mixing anchor channels with original feature channels, is crucial for the proof. The connection between the alignment of these mixed channels and the alignment of the original data matrices is not sufficiently motivated or explained.


### Questions
- Right before section 2.2, it is stated: "The obtained results for D′ = 1 can also be easily extended to D′ > 1 as
otherwise f can be written as [f1 · · · fD′ ]⊤ and each fi has single output feature channel." I assume this is referring to the previous sentence and means "the results obtained for invariance can be extended to equivariance, as.." Is this correct?

I would be curious to hear the authors opinion on the following:

According to this and prior theoretical works, a very large embedding dimension $L$ is needed to maintain the universal function approximation ability of permutation invariant functions, however, many practical works which utilize permutation invariant set functions do not use such a large embedding dimension. Therefore, what is the practical takeaway for an implementation which wishes to utilize a permutation invariant function? There seems to be quite a large disconnect between theory and practice on this topic.  

---

Overall, my biggest conflict with this work is that there is no empirical experiment to corroborate the theoretical findings presented in the paper. While I cannot find issue with any of the claims made in the paper, if there is no way to empirically verify the given bounds, then it is quite difficult to understand their practical significance. Therefore, if the authors could provide an experiment or further discussion which illuminates this topic, I would be happy to revisit my current score.

### Soundness
3 good

### Presentation
3 good

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
This work concerns the expressive power of the DeepSets architecture [Zaheer et al., 2017], which is designed to model permutation invariant functions taking as input *sets* whose elements are real vectors. The basic parameters relevant for the model are N and D; N denotes the size of the input set and D denotes the dimension of its elements. The novelty of this work is in proving a poly(N,D) upper bound on the latent dimension sufficient for DeepSets to express *any* permutation-invariant function. Previously known bounds were exponential in the relevant parameters N and D.

To elaborate, the DeepSets architecture is of the form $g(x) = \rho(\sum_{i=1}^N \phi(x^i))$, where $\phi: \mathbb{R}^D \to \mathbb{R}^L$ is a feature map for the set elements $x^i \in \mathbb{R}^D$, and $\rho: \mathbb{R}^L \to \mathbb{R}$ is an activation function. Both $\phi$ and $\rho$ are chosen by the model designer. Writing $\Phi(X) = \sum_{i=1}^N \phi(x^i)$, where $X \in \mathbb{R}^{N \times D}$ we can view $\Phi$ a “sum-pooled” feature map for the input X. A key question for the practitioner is “How large should I set the latent dimension L to model *any* permutation-invariant target function?” This work shows that L = poly(N, D) is both sufficient and necessary (the bounds are not tight, however). Previously known upper bounds on L were exponential in N and D, thus this work represents a significant improvement over the previous state-of-the-art in theory.

### Strengths
The paper presents novel ideas in designing the feature map $\Phi : \mathbb{R}^{N \times D} \to \mathbb{R}^L$ to overcome limitations of previous work which did not generalize beyond the scalar-elements case (i.e., D=1). The combinatorial argument presented in the proof of Lemma 4.4 is particularly nice, though it is somewhat difficult to follow in the current exposition. Overall, I find the proofs insightful and quite surprising (I will elaborate on this below). Hence, I am inclined to accepting this paper.

The proof of the main result can be understood in stages. Let $\Phi(X) = \sum_{i=1}^N \phi(x^i)$, where $x^i$ denotes D-dimensional vectors which are elements of the given “set” X. The ultimate goal is to design $\Phi : \mathbb{R}^{N \times D}$ such that $\Phi(X) = \Phi(X’)$ implies $X \sim X’$, where $A \sim B$ means that the two matrices are equivalent up to row permutations (the opposite implication is obvious). The key difficulty is in “surviving” the sum-pooling operation $\sum_{i=1}^N$.

Ideas from previous work, such as the degree-N polynomial mapping $\psi(z) = (z, z^2, z^3, \ldots, z^N)$, can be applied entrywise to ensure that $\Phi(X) = \Phi(X’)$ implies that the rows of X and X’ are equivalent *individually*, which is a weaker implication than $X \sim X’$. This only works only in the D=1 case and not for D > 1 since $X \sim X’$ requires the coordinates of the rows $x^i$ be *jointly* aligned. To overcome this limitation, the authors propose novel ideas in the design of $\Phi$ so that alignment between the coordinates of $x^i$ are ensured as well. Personally, I found this issue of coordinate-wise alignment quite challenging and was pleased to see its resolution here.

### Weaknesses
One shortcoming of this paper is that the exposition is quite hard to follow. It would help this paper reach a wider audience if the authors improved their exposition. I would suggest using less confusing notation and providing a more structured and detailed proof overview. Specific examples include:

- The proof of their main theorem can be presented in stages as follows “Suppose $\Phi(X) = \Phi(X’)$. The polynomial mapping ensures that the *rows* of X and X’, when viewed as multi-sets, are equal. The main technical challenge is to ensure that the coordinates of the rows are aligned as well. This step combines two ideas: the “anchors” and the set $\Gamma$, representing the additional linear mappings that ensure *pairwise* alignment …”
- The linear projections that form the coordinates of $\phi(x^i)$ are all represented as $w_j$’s. It would be more informative if different symbols were used for the different “types” of these mappings (standard basis, anchors, \gamma’s …).
- In p.7, the superscript notation for $w$ is confusing. For the samples, the superscript “(n)” was used to index elements of the set. Here it is used to denote different “types” of w. As mentioned before, simply using different symbols for different groups would avoid the use of unnecessary superscripts.

### Questions
- One of the key technical proof ideas is showing that there exists some set of real numbers $\Gamma$ s.t. for any $a,a’,b,b’ \in \mathbb{R}^N$, if $a \sim a’$, $b \sim b’$, and $(a-\gamma b) \sim (a’ - \gamma b’)$ for all $\gamma \in \Gamma$, then $[a, b] \sim [a’, b’]$ (here, we view [a b] as “row $a$ stacked on top of row $b$”). Is the idea of using such linear transformations (of the form $a - \gamma b$) to ensure alignment between the coordinates new? Or is this “linear coupling” a well-known fact in mathematics?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the representational powers of the permutation-invariant DeepSets architecture, which maps inputs $X \in \mathbb{R}^{N \times D}$ to features $\phi(X) \in \mathbb{R}^{N \times L}$, computes a sum, and then computes an output with $\rho: \mathbb{R}^L \to \mathbb{R}$. Past results have shown that the DeepSets architecture can represent any permutation-invariant continuous function when $D = 1$ as long as $L \geq D$, and that $L \geq \exp(\Omega(\min(\sqrt{N}, D)))$ is necessary under certain assumptions about the $\phi$ and $\rho$ being implementable with analytic activation functions. This work shows that without these activation restrictions, permutation-invariant continuous functions can be exactly represented using embedding dimension $L = \text{poly}(N, D)$. 

They do so by introducing a pair of positive results in Theorem 3.1, one having a power mapping activation (where each input is mapped to its powers up to degree $N$) and another having an exponential activation. The constructions use a similar proof structure, both of which involve finding $\phi$ that that the function $X \mapsto \sum_i \phi(x_i)$ is continuous and invertible, which makes it possible to invert the mapping in $\rho$ and then apply the permutation-invariant function directly. (Note that this means that, while $\phi$ is a simple construction that can be made explicit, the inversion of $\rho$ is an existential result that may correspond to a highly non-smooth function.) The feature mapping $\phi$ is constructed carefully to ensure that inputs that are element-wise permutation-invariant but *not* vector-wise permutation-invariant map to different features; the authors do so by using *anchor* vectors to distinguish each vector. The remainder of the construction is dedicated to ensuring that some anchor exists for every possible input and that the desired constraints are enforced.

They contextualize their results by including several negative results to illuminate their design decisions, including Lemma 3.4 (why $\rho$ and $\phi$ must be continuous) and Theorem 4.5 (why there must be at least $D$ candidate anchor vectors for each input to have an anchor). They run brief experiments in Appendix K that train DeepSets models to compute lexicographical medians, and find that the necessary width $L$ grows polynomially in $N$ and $D$.

### Strengths
The contrast to the Zweig and Bruna lower bound is of theoretical interest, since it shows that requiring analytic activation functions changes the minimum width cost from polynomial in $N$ and $D$ to exponential. The work, coupled with its experimental results, suggests that an impressive amount of information can be encoded in sums of relatively low-dimensional feature embeddings, and that the functions that cannot be represented by standard DeepSets architectures are likely highly pathological or discontinuous.

The results are technically impressive, and I found no major errors in the proofs. In particular, the LP and LE constructions were clever, meticulous, and well-visualized by figures.

### Weaknesses
While I don't expect this paper to solve the problem, the non-explicitness of the construction means that $\rho$ is likely to be a highly non-smooth function that is difficult to compactly approximate using a neural network architecture. In future works, I'd be interested in understanding whether feature dimensions that are larger polynomials in $N$ and $D$ make it possible to yield explicit (and ideally more smooth) $\rho$ mappings. Perhaps the work could discuss possible approaches to bounding the smoothness of inversion functions? Or perhaps the authors can discuss which kinds of permutation-invariant functions $f$ are expected to have smooth features?

## Minor issues
* I was momentary confused by the conditions on $L$ in Theorem 3.1. At first, I thought $L$ *could not* be larger than $N^5D^2$ and not that this is an upper bound on the smallest $L$. Perhaps the lower bounds could be mentioned separately, for the sake of clarity? 
* Page 17 says "pigeon-hold" instead of "pigeon-hole."
* Lemma E.1 is much easier to parse after noting Remark E.2. Perhaps the remark could be included before the proof, or maybe the lemma could just define the $\gamma_i$ values explicitly as prime numbers, since a generality in $\gamma_i$ is not necessary for any of the proofs?

### Questions
N/A

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
