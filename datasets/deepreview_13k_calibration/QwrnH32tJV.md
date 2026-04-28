# Provably Learning Concepts by Comparison

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 3, 6

## Abstract
We are born with the ability to learn concepts by comparing diverse observations. This helps us to understand the new world in a compositional manner and facilitates extrapolation, as objects naturally consist of multiple concepts. In this work, we argue that the cognitive mechanism of comparison, fundamental to human learning, is also vital for machines to recover true concepts underlying the data. This offers correctness guarantees for the field of concept learning, which, despite its impressive empirical successes, still lacks general theoretical support. Specifically, we aim to develop a theoretical framework for the identifiability of concepts with multiple classes of observations. We show that with sufficient diversity across classes, hidden concepts can be identified without assuming specific concept types, functional relations, or parametric generative models. Interestingly, even when conditions are not globally satisfied, we can still provide alternative guarantees for as many concepts as possible based on local comparisons, thereby extending the applicability of our theory to more flexible scenarios. Moreover, the hidden structure between classes and concepts can also be identified nonparametrically. We validate our theoretical results in both synthetic and real-world settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper studies learning of a certain type of non-parametric hidden variable model. Theorems are given showing statistical identifiability, and some experiments are preformed.

The family of non-parametric hidden variable models is described on pp 2-3. In brief:
- There are concept-dependent hidden variables $Z_A$ and concept-independent hidden variables $Z_B$. The distributions of $Z_A$ and $Z_B$ are not constrained to come from a specific distribution such as Gaussian. The concept-dependent variables $Z_A$ depend on the class $c$ of a given datapoint.
- The hidden variables $(Z_A, Z_B)$ are mapped to the observed variable $X$ via some smooth function $g$. 
- It is further assumed that the Jacobian of $g$ satisfies certain full-rank assumptions in order to ensure an ability to recover the model based on observations.
- Some sparsity assumptions are made on how many concept-dependent hidden variables correspond to each class $c$.
- A "structural diversity" assumption is made stating roughly that each class has at least one hidden variable unique to this class and not shared with other classes.

The paper proves theorems that under the assumption listed above it is possible to recover the model (up to some transformation). 

Experiments are performed on synthetic datasets, as well as Fashion-MNIST, EMNIST, AnimalFace, and Flower102 datasets and model is fitted using a regularized maximum-likelihood method. Robustness of the recovered concept is tested by comparing the same concept across different angles and environments. 

The paper also compares the performance of regularized maximum-likelihood method that encorporates the aforementioned assumptions vs the base method that does not incorporate the assumptions above. It is shown that the former achieves a better performance in terms of Mean Correlation Coefficient (MCC).

### Strengths
- Non-parametric models of the type studied in this work have their uses and can be important if one is working with relatively low-dimensional data and needs high degree of interpretability.
- The paper is carefully written and includes an appendix listing all notation, figures are well-made.

### Weaknesses
 - The paper does clearly articulate how exactly it improves on a number of closely-related papers such as [Zheng et al., 2022], [Zheng & Zhang, 2023] and [Kong et al. 2022] among others. These works study non-parametric models that look quite similar to the ones given in this work in terms of assumptions on the Jacobian and structural sparsity. They also use very similar mathematical tools to analyze identifyability. The paper does not articulate clearly what exactly it believes are some specific shortcomings of these earlier works, and how the current work overcomes such shortcomings. I think it is important that this is done, and it is also convincingly argued that the current paper indeed overcomes such limitations. (Update: added experiments partially address this objections, I raise my score but lower the confidence score)

### Questions
(See above)

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper models and studies the problem of concept learning. Suppose that we are given observations $x$s from $k$ classes that are generated based on their concept vectors $z$, furthermore, each class has a set of associated indices of the concept vectors and a concept vector is generated according to the class, we want to recover the corresponding set of concept indices for each class. The paper tries to build a theoretic framework that can explain under certain assumptions, which kind of concept can be recovered. Besides the theoretic framework, the paper also performs experiments on both synthetic and real-world datasets based on their theoretic framework.

### Strengths
Concept learning is an important topic in machine learning. This paper builds a mathematical framework to help understand what concepts can be reliably recovered. Experiments are also provided to help justify the theory in this paper.

### Weaknesses
1. 
The main weakness of the paper is its presentation. I list several issues about the presentation as follows.

The definition of the problem is not complete in the preliminary section. In the preliminary section, the paper only defines how observations are generated but does not give a clear definition of what a learner is expected to output and how to measure the performance of a learner.
Furthermore, the statements of the main theorems are not mathematically formal enough. For example, the statement of Theorem 1 mentions "estimated latent concepts"
> the estimated latent concepts for the set difference $\hat{z}_{\pi(A_i \backslash A_j)}$...,

I understand that the estimated latent concepts should be the output of a learner. However, before the statement of Theorem 1, the paper does not define the definition of estimated latent concepts. It is confusing what algorithm/estimator a learner uses to get such an estimation. Another example is the statement of Theorem 2. In the statement of Theorem 2, the paper mentions 
>$z_B$ is identifiable up to a subspace-wise invertible transformation.

I think subspace-wise invertible transformation is an informal mathematical term. Furthermore, as the definition of identifiable is also not formally presented in the preliminary section, it is unclear the exact result that the theorem would like to convey.

2. I think some of the assumptions made by the paper are not natural enough. For example, in equation (3), the paper assumes that the entries of the class-dependent concepts $z_A$ are conditionally independent. This seems to be a very strong assumption, but the paper does not provide natural examples to justify that the assumption is reasonable.

### Questions
1. 
In the preliminary section, the classes are defined as a vector $c=(c_1,\dots,c_u)$. It is not very clear to me whether the class vector $c$ can take continuous real values or can only take discrete values. If $c$ can only take discrete values, then in line 124, it is not reasonable to say one can take the partial derivative of $g$ with respect to $c$. Can you help clarify this?

2. 
In line 320, it says the distributional assumption in Theorem 2 necessitates the existence of at least two classes with differing conditional distributions and is highly likely to be satisfied. But it seems that the distribution assumption is much stronger because it requires the probability mass for the probabilities to be unequal for any subset $A_z$ that is not a product set of $B_{z_B} \times z_A$. Can you provide any real-world example that satisfies the assumption?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies a new model of concept learning that works roughly as follows:
- In any given setting (e.g. classifying images of animals), we have $u$ possible classes, such as "cat", "dog", "mammal", "bird" (not necessarily mutually exclusive), and $n$ possible real-valued concepts, such as "furriness", "number of legs", "age", etc. Of these, $n_A$ concepts are class-dependent (e.g. "furriness", "number of legs"), and the rest are not (e.g. "age").
- A binary "structure" matrix $M \in \\{0, 1\\}^{n_A \times u}$ describes which concepts are related to which classes.
- Data is generated as follows: we first generate a class vector $c \in \\{0, 1\\}^u$ (e.g., "cat" + "mammal"), then we generate a latent concept vector $z$ based on $c$ (via a distribution $p(z|c)$ that follows the dependence structure given by $M$), and finally generate an observed vector $x$ based on the concept vector $z$.
- It is important that no other parametric assumptions are made.
- The goal is to identify $z$ based only on the observed data $x$.

Under this data-generating process, the main results are identifiability results:
- Under some technical assumptions that essentially encode a kind of diversity and identifiability in the structure matrix (intuitively, for each concept $z_i$, there must be a set of classes such that $z_i$ is unique to one of those classes --- in a sense, each concept has a unique "class signature"), the concept vector $z$ is identifiable from the data up to permutation and invertible transformation (Theorem 2).
- Extensions / variants of this result are also given (e.g. for pairwise comparison of classes, etc).
- Some experimental results are also given.

### Strengths
**Disclaimer:** while my background is in ML theory, I have very limited familiarity with this particular area (which I see as causal discovery / structure learning), and my perspective should be taken as that of a relative outsider.

This work tackles a broad and ambitious question in "concept learning": what are the mildest structural assumptions under which we can reasonably hope to identify underlying concepts from purely observed data? To do so, the paper introduces a rather generic non-parametric data-generating process and shows basic identifiability results under certain technical assumptions.

Overall the paper scores well on ambition and originality, as this is certainly an important question to investigate, and it appears from the literature that prior work had not tackled the question in quite such generality (to my limited knowledge). Thus a nice contribution of the paper is the definition of the model and the approach to the question. It is also nice that the authors obtain results with very few parametric assumptions on the data-generating process. The result is likely of technical interest to an audience in causality and related areas.

### Weaknesses
 (See disclaimer above.)

By far the biggest weakness of the paper is that it is written in a very obscure and technical fashion, and is IMO very hard to read and understand for anyone not working in causal discovery, structure learning or related areas. Remarkably for a paper that claims to study such a broad and basic question, essentially no examples whatsoever are given of how the main data-generating process is instantiated in real-world settings. In fact it took me a while even to extract enough understanding to write the summary above.

In general the paper seems jump between very technical statements and voluminous but vague exposition. For example, the main theorems are all quite technical and tricky to parse. The few examples given are entirely synthetic and hard to interpret. The notation is quite dense. See also some concrete questions below.

I also have a lurking suspicion that the framework is so generic and the assumptions so strong that the main result is sort of tautological and primarily a mathematical exercise. Intuitively it seems quite reasonable to expect diversity assumptions of this type to lead to identifiability. Perhaps the authors could do a better job contextualizing what makes the result surprising and notable.

Overall it is not clear who the intended audience really is. As interesting as the results may be, they certainly do not seem accessible to a broad machine learning audience like at ICLR. While the authors have placed it in the primary area of "interpretability and explainable AI", I am quite sure it is out of place here, at least as written. In fact I am not sure why it has not been framed more squarely as causal discovery or structure learning, or indeed submitted to a specialized technical venue or journal in that field.

### Questions
- I strongly recommend that the authors discuss real-world examples of how the data-generating process may be instantiated (e.g. for image classification in the context of Fashion-MNIST or AnimalFace, but also others). This includes clearly specifying what the classes, concepts, and observed values are in each example.
- A high-level modeling question I am unclear on is why there is a distinction between classes and concepts. Any given observed vector is implicitly associated both with a latent vector of classes and a latent vector of concepts. Both appear to be unobserved --- unless the classes are indeed observed and this is the difference? If not it is not clear why we want to model them separately at all, and how they are playing functionally different roles.
- What is the type of each class $c_i$? What space does it take values in? This does not seem clearly specified anywhere and is very confusing. The entire meaning of the partial derivative $D_c g$ rests on this.
- Theorem 1 refers to "estimated latent concepts" --- what is the estimation procedure? If it is an identifiability result, why do we need to refer to estimated concepts at all?
- It would really great if the notation could be lightened in any way possible. The array slicing notation $D_{:n_A, :}$ in particular adds a lot of visual noise and I am not sure why it is needed if $g$ anyway maps to $\\mathbb{R}^{n_A}$. At least some shorthand could be introduced.

### Soundness
3

### Presentation
1

### Contribution
2
