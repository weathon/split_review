# Geometry of Lightning Self-Attention: Identifiability and Dimension

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We consider function spaces defined by self-attention networks without normalization, and theoretically analyze their geometry. Since these networks are polynomial, we rely on tools from algebraic geometry. In particular, we study the identifiability of deep attention by providing a description of the generic fibers of the parametrization for an arbitrary number of layers and, as a consequence, compute the dimension of the function space. Additionally, for a single-layer model, we characterize the singular and boundary points. Finally, we formulate a conjectural extension of our results to normalized self-attention networks, prove it for a single layer, and numerically verify it in the deep case.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper provides a theoretical analysis of the geometry of the function spaces corresponding to self-attention networks. The core of the work concentrates on the “lightning” variant of self-attention (for which forward computation computation is linear in the sequence length) since it is amenable to an algebraic analysis. The authors calculate the dimension of the hypothesis space (“neuromanifold”) through an analysis of the (generic) fibers of the model’s parametrization. The submission provides an extension to normalized attention modules, provably for the case of a single layer, and conjecturally for deep networks.

### Strengths
S1. The paper exposition is quite clear, striking a balance between the lingo of algebraic geometry and the context of the ICLR audience.

S2. The empirical popularity of attention-based networks, and the relative lack of understanding on the properties of said architectures (with respect to fully connected and convolutional ones, as the authors point out in L51-53) sufficiently justifies the theoretical exploration presented in this submission.

S3. The authors identify lightning self-attention as a fruitful compromise that is both (1) amenable to their algebraic-geometric analysis and (2) a reasonably realistic neural network module. I believe the presented implicit hierarchy of modules (single-layer lightning self-attention, deep lightning self-attention, single-layer normalized self-attention, deep normalized self-attention) can be of use in further theoretical analyses of attention networks.

S4. The authors introduce a “virtual weights” parametrization which enables an elegant analysis of deep lightning self-attention networks.

S5. The submission poses a conjecture on the fibers for deep normalized self-attention networks (under their virtual weights parametrization). This conjecture is theoretically validated in the case of a single layer and empirically tested for deep networks. The communication of this conjecture to the relevant communities within the context of the ICLR conference can be beneficial towards advancing on its resolution.

### Weaknesses
While S2 can warrant sufficient interest from the ICLR community, I think the submission falls short of adequately examining the implications of its findings. I think the authors could have expanded more on the “so what?” question after reaching their (interesting!) core theoretical goals.

W1. For example, in L416-419, the authors are quite descriptive about the dimension of the neuromanifold for a contemporary language model being ~8.2B vs the crude parameter dimension of ~8.6B. Yet, there is not even a high-level attempt to prescribe how to exploit this information. The authors could have explored, even speculatively, how this difference in dimensionality might be leveraged in practical scenarios. For instance, could this gap suggest avenues for more efficient parameterizations, or indicate inherent redundancies that could be pruned without significant performance loss?

W2. The authors partially justify the importance of the analysis of the dimension of the neuromanifold via an appeal to learning theory (L58-61) and its connection with sample complexity. (Although this may be considered outside of the scope!) The submission does not present a tangible demonstration of the implications of the knowledge of the neuromanifold’s dimension on the sample complexity, not even in a very simple toy-ish experimental setting. Even a basic experiment, such as training the same model with varying amounts of data and observing the correlation between the neuromanifold dimension and generalization performance, could have provided a more concrete link to the theoretical claims.

### Questions
Q1 & Q2. What is the authors’ position on W1 and W2?

Q3. In the (much appreciated!) anonymized code for the verification of Conjecture 3.16, L19 instantiates `n_iter_array = [5, 5, 5, 5, 5, 5, 5, 8]`. These iterations are used as “trials” out of which the maximum rank Jacobian is extracted in L41 `dim_vec.append(max(ranks))`. Could the authors explain why such multiple “trials” are needed? And also why is this component left out of the experimental description in L472-484?

Q4. Could the authors elaborate on the implications of the non-smoothness of the $\mathcal{M}_{d, d’, a}$ manifold from an optimization standpoint?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the geometry of lighting attention models by characterizing their fibers (redundant parameterizations of a neural network) and neuromanifolds (the function spaces induced by all possible parameterizations). Critically, they assume for most of the paper that (1) the attention matrix has no normalization (i.e. no softmax); (2) there are no MLP layers of the transformer; and (3) there are no residual connections. They prove the following:
* From Theorem 3.2, in most cases, the fibers are 1-dimensional (identifiable functions up to rescaling), except under certain rank-1 cases, where the fiber has higher-dimensional symmetries. The dimensionality of these fibers can be used to exactly capture the neuromanifold dimension in Corollary 3.3.
* Theorem 3.4 shows that the neuromanifold is closed in Euclidean space and that its boundaries are defined by networks with rank-1 matrices.
* Theorem 3.15 shows that self-attention layers have singleton fibers, and Conjecture 3.16 predicts that deeper self-attention models also have singleton fibers. The conjecture is backed up with experiments that estimate the dimensionality of the neuromanifold dimension and shows a tight alignment to the conjecture.

### Strengths
The contributions reveal interesting properties of the geometry of lightning attention models and provide a rigorous characterization of the resulting functional space. The results are well-described and relatively straight-forward to follow.

As far as I can tell (although I am no expert in algebraic geometry), the claims are clearly stated and the mathematics are correct.

### Weaknesses
There are several key gaps between the models studied in this paper and practical models:
* The lack of non-linearities in the attention unit (in particular, the lack of softmax). This is a critical omission, as the softmax function introduces a crucial normalization step that ensures the attention weights sum to one, which is fundamental for the proper functioning of attention mechanisms. Without it, the behavior of the attention mechanism is significantly altered, and the analysis might not be directly applicable to real-world scenarios.
* The lack of residual connections between layers. Residual connections are essential for training deep networks, as they mitigate the vanishing gradient problem and allow for the effective propagation of information across layers. Their absence in the analyzed model raises concerns about the relevance of the findings to practical deep transformer architectures.
* The lack of element-wise multi-layer perceptrons between layers. MLPs introduce non-linear transformations that are crucial for learning complex representations. The absence of these layers in the model limits its expressive power and makes it unclear whether the geometrical properties observed in this simplified model would generalize to more realistic transformers. As far as I am aware, all three components are important for practical transformers, and that a lack of residual connections or MLPs tend to lead to degeneracy in training. While the manifold analysis in the paper is interesting, it's unclear how it would extend to cases where the model does not have such clear polynomial behavior.

While the theory is interesting in its own right, it's somewhat unclear to me what can be inferred about realistic models based on this theory, especially because the softmax results point to no parameter redundancy.

### Questions
While the results are certainly mathematically interesting, it's unclear to me what practical guidance can be gleaned from this line of work. What are the consequences of understanding the dimensionality of the neuromanifold for the model's expressivity and generalization? 

I think parameter redundancy is an interesting angle, but this work seems to suggest that existing models have little room for improvement on that front. Are there modifications to this work (or questions to be pursued by future work) that might look at notions of fibers that pertain to parameters that map to _approximately_ the same output, rather than exactly the same output?  

I appreciate the section that extends this analysis to self-attention layers. Can this analysis be modified to account for the inclusion of residual connections or MLPs?

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
2

### Summary
This paper studies the geometry of self-attention networks, focusing on "lightning" self-attention mechanisms. The paper offers a theoretical analysis of lightening attention using algebraic geometry, focusing on dimension of the neurmoanifold and the identifiability of deep attention. Key contributions include a description of the fibers of the parametrization map and the computation of neuromanifold dimensions. Additionally, the authors extend their findings to traditional, normalized self-attention networks (essentially with softmax activation) and present a conjecture, supported by empirical evidence, regarding their fibers of parametrization.

### Strengths
The paper presents a novel and rigorous theoretical analysis of undoubtedly important topics, i.e., attention mechanisms. The authors use algebraic geometry to develop a solid theoretical understanding of the neuromanifold of neural networks using attention mechanisms. Although the analysis is offered in a simplified context, that is standard and inevitable for a rigorous theoretical analysis and does not reduce the importance of their contribution. I believe the introduction motivates the study quite well (though it could be improved). Understanding the dimension and the topology of the neuromanifold is a consequential result, as it relates to the learning dynamics of transformers in the overparameterized regime (as authors point out, e.g., lines 246-248), and it could enable a series of future studies. The paper could potentially provide foundational insights with a potentially wide range of applications in understanding the mathematical properties of attention mechanisms in deep learning (though, whether this is achieved or not is not fully clear, as I discuss under weaknesses).

### Weaknesses
 **Key weakness:** The main weakness of the paper which is present throughout the paper is that the ultimate goal of the theoretical results as well as their implications tend to seem lost and poorly explained. I believe many among the ML audience of this paper might raise the objection that “this paper belongs to a math journal, not ICLR”. I take the liberty to clarify that that is not my objection, and I believe even a paper that solely focuses on deriving results and developing mathematical tools from a purely theoretical perspective could be valuable and could very well belong to ICLR. That being said, I expect such a paper to clarify the implications of their results for the wider community, or at least for future theoretical research on foundations of deep learning. I regret to see that this paper does not meet this criteria. As I mentioned among the strengths, I understand the results are foundational with potentially important consequences, but they are highly (perhaps overly) mathematicized, without proper explanations that clarify what these mathematicized observations entail for the ML applications, e.g., how transformers learn their representation, or how these result allow us to develop a better understand of the convergence of GD-based optimization on transformers (which I think they could do).



**A list of some of the main weaknesses:**

1. The implications of the theoretical statements are often not discussed (with a small number of exceptions). For instance, the main result of the paper is stated in Theorem 3.13, but no discussion of its implication is provided. In an ML paper, all such theoretical results should follow with a discussion of the implications that are more accessible to ML researchers. 

2. Even when implications are discussed, the ultimate goal or the consequences of the implications are not discussed. e.g., the authors discuss the implications of corollary 3.5, but they can clarify what this implies for the success of the attention mechanisms, or at least remark how it could enable future studies on that.

3. The experiments lead to a conjecture, but they are from empirical relevance. I would like to clarify again that this is fine with me, as long as at least the theoretical relevance for future work that could eventually lead to an empirically relevant application is discussed.

4. There are too many technical details leading to the proofs or sketch of the proofs of the results, which I do not think belong to the main text of a machine learning paper (e.g., lines 165-173 or 227-240). These details could be move to the appendix and replaced with a more high-level discussion of the intuition behind the results and the implications of the results.



**More specific points about the weaknesses:**

a. There is almost no review of the literature. There are many interesting (and some quite relevant) recent works on developing a theoretical understanding of transformers or relevant topics (e.g. learning dynamics in overparameterized regimes). It is important to discuss this and explain the gap in the literature. This helps motivate the paper as well.

b. While the introduction motivates the paper, the abstract does not. The abstract could be improved to reflect the motivation explained in the second paragraph of the introduction. Moreover, the second paragraph of the introduction itself could mention more specific examples of the applications and the potential future direction the paper opens a door to, in order to better motivate the paper.

c. The purpose of the visualizations in figures 2 and 3 is unclear.

d. Line 297 says “we introduce yet another re-parameterization”. While I understand you later use this, I suggest you explain closer to where you introduce the reparameterization and why you are introducing it.

e. The summary of the proof of Theorem 3.13 could also be moved to the appendix. It is crucial to discuss the implications of the theorem, instead of explaining the proof in the main paper.

f. The presentation can be improved to be more accessible to ML researchers.

### Questions
1. The authors say in the conclusion that “Extending our algebra-geometric analysis to include these variations represents an interesting line for future investigation” (line 496). How? Can you be more specific? What do you think are the future direction of the research? Can you specify 2-3 specific directions?

2. What purpose do figures 2 and 3 serve?

3. What do you think are the main implications of the main theorem?

### Soundness
4

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies the neuromanifold, the image of the parametrization map that maps network weights to the corresponding input-output map of the network, of single-layer and multi-layer linear-self-attention networks. Specifically, the dimensions of these neuromanifolds are computed, and the fibers of the parametrization of these neuromanifolds are discussed.

### Strengths
Analysis of linear self-attention networks with tools from algebraic geometry

### Weaknesses
The paper computes the intrinsic dimensions of the neuromanifolds for single- and multi-layer self-attention networks, and finds them to be of the same scale as the number of parameters. For single-layer networks, the dimension is $2ad+dd'$ compared to $2ad+dd'-a^2-1$ parameters, and for multi-layer networks, the dimension is 8.2b compared to 8.6b parameters in an LLM example. While the reviewer acknowledges the research effort, these results do not offer a significantly better characterization of the function space's complexity than simply counting parameters. The small difference between the number of parameters and the dimension of the neuromanifold raises questions about the practical utility of this analysis. Specifically, it is unclear if this difference has any implications for the expressiveness or trainability of these networks, or if it is simply an artifact of the parameterization. 

This paper also delves into the fiber of the parametrization, the boundary of the neuromanifold, and critical points of the parametrization map. While these are likely important characteristics in algebraic geometry, their relevance to the deep learning community is not well-established. Most of the results lack a discussion of their implications for the training or generalization of linear self-attention networks. The sole exception is Corollary 3.5, which states that "any training trajectory that converges to an equilibrium in the ambient space will converge within the neuromanifold." However, this statement is too vague to provide any practical insights into the behavior of training algorithms or the properties of the learned models. The paper does not sufficiently connect these geometric properties to concrete aspects of training, such as convergence rates, generalization performance, or robustness to adversarial examples. Therefore, the practical impact of these findings remains unclear.

Therefore, while the results presented in this paper may be of interest to the algebraic geometry community, the reviewer does not see it getting well appreciated by the ML community in its current form.

### Questions
See "Weaknesses". The authors do not need to spend too much time responding to this review, rather, they should revise the paper to be more accessible to a broader audience and motivate the results from a more practical perspective.

### Soundness
3

### Presentation
2

### Contribution
2
