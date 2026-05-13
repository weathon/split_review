# The ubiquity of 2-homogeneity, how its implicit bias selects features, and other stories

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
This work studies the optimization and generalization consequences of a seemingly
  innocuous design choice in many modern architectures:
  they end with a composition of affine parameters belonging to a normalization layer and a linear layer,
  resulting in a fundamentally $2$-homogeneous architecture.
  The first set of results are abstract, showing how any architecture satisfying this type of 2-homogeneity and a
  few regularity conditions on the gradients of the inner layers obtain large margins
  and low test error. As technical byproducts, this part of the story provides an implicitly
  biased gradient flow guarantee and also a nondecreasing margin lemma for inhomogeneous networks. The second set of results instantiate this framework for shallow normalized ReLU networks,
  establishing large margin and low test error via feature selection
  purely from random initialization and standard
  gradient flow. As a corollary, the paper obtains good test error for $k$-bit parity problems,
  in particular passing
  below sample complexity lower bounds from linearized analyses such as the  Neural Tangent Kernel.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an expansion of theoretical results about homogeneous networks to those that only *end* in a 2-homogeneous network (with inhomogeneous layers before that). This includes the majority of common present-day architectures, which end in the combination of a normalization layer with learnable scales and shifts by another linear layer. Under certain assumptions, the paper uses a correspondence of gradient descent on these parameters to mirror descent in a re-parameterized space, showing that gradient flow yields large margins, for a certain definition of margin mostly aligning with prior work.

### Strengths
The problem addressed by the paper is important. Identifying that the combination of a normalization layer with a linear layer at the end of these networks might be important to their optimization seems like it might be an important observation. The framing of the particular approach with the connection to mirror descent is clever.

Unfortunately I did not have time to carefully follow the proofs in the supplementary material, but the proof sketches in the main body are clear and the approaches seem reasonable to me.

### Weaknesses
I found some of the initial discussion a little misleading in that e.g. the discussion around line 140 made me think that the analysis would apply to arbitrary homogeneous subsets of parameters $\hat w$. While this is true for the margin definition given there, almost all of the paper applies only to the doubled-linear-layer structure of equation (2). This is fine; I just found that bit of discussion confusing, particularly since taking e.g. only the last layer would also yield a 1-homogeneous structure, and I found myself wondering if it would really be true that it would increase the margin defined in terms of each possible homogeneous part of the network. (To be clear, I don't think any statements in the paper are wrong, I just found this brief discussion confusing.)

Much more importantly: if the feature map $F$ were frozen, the setting of this paper would become a "diagonal network" of depth two, for which the implicit bias of gradient descent was already determined by [Gunasekar et al. (NeurIPS 2018)](https://arxiv.org/abs/1806.00468) to be, indeed, an l1 minimizer. The difference with the present paper's results is that $F$ is not required to stay frozen, and of course a frozen $F$ would be a substantial difference from actual training. The setting of the present paper, though, requires that although $F$ can change, it must satisfy "slow-growing derivatives" and "initial good features." Together, this seems to allow the optimization on the last two layers to basically pick out the good features before they change too much to no longer be good. This is interesting, but perhaps not as interesting as it might seem without citing the (here-uncited) previous work for frozen $F$, and with the caveats about initial good features only coming several pages into the paper. The slow-growing derivatives assumption, while technically necessary, also seems to significantly constrain the applicability of the results, as it is not clear how realistic this assumption is in practice, especially in the early stages of training where feature representations can change dramatically. Furthermore, the paper does not provide any empirical evidence to support the claim that features actually exhibit this slow-growing behavior.

The paper also implicitly argues that the 2-homogeneous structure at the end of transformer-like architectures is very important to their optimization geometry. To be more convincing on this point, since the theoretical results are admittedly a "sanity check," it would be interesting to also run some experiments at least on toy problems to see if this seems to line up. That is, do people leave the learnable parameters on in their normalization layers that are immediately next to a linear layer because it actually helps, or just because they didn't think about it?

### Questions
- In the case of frozen $F$, would direct application of the results of Lyu and Li plus Gunasekar et al. give roughly the same results as you obtain?

- Is my characterization of "slow-growing derivatives" + "initial good features" -> "the features can't break before last-layer optimization finds the good ones" correct?

- I'm curious about the relationship of your "initial good features" assumption to the "initial alignment" results from the series of papers by Emmanuel Abbe and coauthors, particularly [Abbe et al. (ICML 2022)](https://arxiv.org/abs/2202.12846). It seems, without thinking about it very much, that your "initial good features" assumption implies a high "initial alignment"; as they show, this is in some sense necessary for learning, but in a stronger form than they make.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper shows how any architecture satisfying 2-homogeineity and a few regularity conditions on the gradients of the inner layers obtain large margins and low test error. Instantiating this framework to shallow normalized ReLU networks, the paper gives an end-to-end result showing that it obtains large margin and low text error. As a corollary, the paper obtains good test error for k-bit parity problems.

### Strengths
1. The instantiation of the framework to shallow normalized ReLU network is novel and interesting. This improved upon results in [Chizat and Bach 2020] to be quantitative, though the computational complexity may be double exponential. 

2. For result has concrete implications to the support-only k-parity problem, demonstrating neural networks could learn support-only k-parity much more sample-efficient than kernel methods.

### Weaknesses
The first set of results (Theorem 1.1) are a bit abstract and contain non-varifiable assumptions. It is not clear whether it is useful beyond the more concrete shallow normalized ReLU network. The assumptions in Theorem 1.1, particularly those concerning the regularity of gradients in inner layers and the 2-homogeneity requirement, are not easily checked for arbitrary architectures. This makes it difficult to assess the practical applicability of this theorem beyond the specific case of shallow ReLU networks. Furthermore, the paper does not provide clear guidance on how to verify these assumptions for other architectures, limiting the broader impact of the theoretical framework.

### Questions
See weakness

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper describes the dynamics of a network with a 2-homogeneous head and establish the margin guarantee for the models in late training phases. Under a simpler setting of adding 2-homogeneous head to a one-hidden-layer network, the paper can further establish generalization guarantees based on the margin guarantees.

### Strengths
The paper establishes theorem 3.6, a generalization of result from previous work in a clear form. The paper has clear writing that exhibits the proof ideas.

### Weaknesses
1. Theorem 3.1 & 4.1 has assumptions that are hard to verify, and I believe these assumptions should be given out more explicitly in the texts. For theorem 3.1, as the line 260 RHS bounds depends on $t$, the choice of $t$ depends on $R$ and $n$, and the LHS quantity also depends on $n, R$ and $t$, it is essentially hard to tell whether these assumptions can be satisfied. In particular, the required time $t$ for the margin bound in Theorem 3.1 to hold is doubly exponential in $n$ and $1/\gamma$, which implies that the initial condition $\Vert{\bar{p}}_0\Vert_\infty$ and the constant $C_2$ must be extremely small, raising questions about the practical relevance of the result. For theorem 4.1, $m$ depends on $t$, $t$ depends on $R$ and $R$ may depend on $m$ as $m$ changes the initialization scheme. Thus the authors should at least provide the scale estimate of $R$ to show that their assumption is reasonable.  

2. The proof technique for Theorem 3.6 is standard and may be lacking of novelty compared to former work (https://arxiv.org/abs/1906.05890) .

3. The correlation of part1 and part2 of theorem 1.1 are unclear from text. It seems like two independent results. The main claim of the current paper - selecting feature from space $F_1$ is more efficient than from $F_2$ using 2-homogeneous head - does not require a result in representation learning, thus is basically already inferred from previous work (Telgarsky 2022 + Lyu 2019, as mentioned in Example 4.1). Also it is unclear from text why 2-homogeneity is unique - from my perspective $k$-homogeneity may also be provable using similar arguments for $k>1$. Furthermore, the title of the paper should be changed in the pdf file.

### Questions
Regarding weakness 1, can the authors provide an instance of choices of the parameters such that the assumptions in theorem 3.1&4.1 are satisfied? And please provide more clarifications on the strength of these assumptions?

Also can the author further clarify weakness 2 & 3?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the gradient flow dynamics on networks where the last layer includes normalization followed by a linear transformation. Formally, it means that they consider networks where the last layers are a two-layer linear diagonal network, but the motivation for studying this architecture comes from normalization layers. They show implicit bias towards ell_1 margin maximization of the linear transformation induced by the last layer (with its normalization). This result includes abstract assumptions, but they also consider two-layer normalized ReLU networks as a concrete instantiation, obtain generalization guarantees, and use it to achieve a generalization guarantee for sparse parities which goes beyond the NTK bounds.

### Strengths
The paper considers the challenging problem of analyzing the implicit bias of non-homogenous networks. They give a general margin-maximization guarantee (under certain assumptions) and show that this general result can be used to obtain more concrete bounds for two-layer normalized ReLU networks and specifically for learning sparse parities. Unlike many existing results on the implicit bias in the rich regime, their result gives a bound on the margin rather than just showing convergence to a KKT point of the max-margin problem. The sparse parities learning problem has attracted much interest, and several prior works considered learning sparse parities using shallow neural networks, and thus the corollary (Example 4.1) is of independent interest. The technique seems interesting and non-trivial, and might also be of independent interest.

### Weaknesses
Theorem 3.1 is very hard to parse. It includes assumptions that involve the margin induced by the random features at initialization, and the KL divergence between the ell_1 max margin predictor at initialization and the last layer’s initialization. These assumptions are not intuitive and require a deeper understanding of the interplay between the initialization and the optimization dynamics. It's unclear how these assumptions would be satisfied in practice, beyond the specific case of normalized ReLU networks. The assumption called “the slow growing derivatives property” is also problematic, as it's not immediately clear how to verify this property for different activation functions or network architectures. The lack of clarity around these assumptions makes it difficult to assess the general applicability of the theoretical results. The connection between the abstract assumptions and the concrete results for two-layer normalized ReLU networks could be made more explicit. It would be helpful to see a more detailed discussion of how the assumptions of Theorem 3.1 translate into the specific properties of the normalized ReLU network, and why these properties are satisfied. 

Typos:
- Title is missing
- Line 433: xi_t —> \xi_t
- Line 479: “of of”

### Questions
Can you compare your result on two-layer networks to Theorem 3.3 in Telgarsky 2022?

### Soundness
4

### Presentation
3

### Contribution
3
