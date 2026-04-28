# Simple mechanisms for representing, indexing and manipulating concepts

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 3, 8

## Abstract
Deep networks typically learn concepts via classifiers, which involves setting up a model and training it via gradient descent to fit the concept-labeled data. We will argue instead that learning a concept could be done by looking at its moment statistics matrix to generate a concrete representation or signature of that concept. These signatures can be used to discover structure across the set of concepts and could recursively produce higher-level concepts by learning this structure from those signatures. When the concepts are `intersected', signatures of the concepts can be used to find a common theme across a number of related `intersected' concepts. This process could be used to keep a dictionary of concepts so that inputs could correctly identify and be routed to the set of concepts involved in the (latent) generation of the input.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose to formalize concepts to be a shared set of properties defined by a polynomial manifold. Such manifold can be identified by the null-space of moment statistics of points in the manifold, which makes these statistics serve as the signature of the manifold, or concept. The strengths of such signatures are that the structure of concepts can be reflected in the signature of concepts and the lower-level signature can be used to derive higher-level signatures. The authors also analyze the transformer network on how it captures the concepts defined in this paper.

### Strengths
1. The authors provide a novel formalism of "concepts", which facilitates further studies on "concepts";
2. The authors provide proof for every statement they propose. They also provide examples to illustrate some abstract ideas;

### Weaknesses
Although the analyses and demonstrations are comprehensive, the authors do not provide any experiments to support their theories or how their theories can be applied to existing models. I suggest authors may conduct a few experiments to show the applicability of their model.

### Questions
See my suggestions above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
*Note that mathematical claims were not checked in detail*

The authors propose a formalism for hierarchical concept discovery, in which concepts lie on low-dimensional polynomial manifolds whose moment statistics can be used to identify the "signatures" of concepts. They show that in such a setting, the inner product between points on the same concept manifold will be lower than those on different manifolds, such that concept membership can, in principle, be performed with an inner product check. Furthermore, they show that random projections can be used to lower the sample complexity of membership checks to be quadratic in the effective number of dimensions of a manifold.

These theoretical results are then applied to a (theoretical) modification of the transformer architecture, in which the polynomial manifolds correspond to distinct conceptual subspaces (in much the same way the Mechanistic Interpretability community have conceptualized the transformers in the "residual stream view" [1]). In this proposed architecture the attention operation associates points lying on the same manifold most strongly (as per the inner-product findings above), and the MLPs are responsible for computing the signatures of each point (i.e. the separate concepts). Applied across multiple layers this amounts to a hierarchical computation of signature, and thus concepts, associated with the inputs.

The authors make their theoretical framework somewhat more concrete by providing examples of signatures corresponding to circles, moving objects and rotation-invariant point clouds.

[1] Elhage et al. 2021 - A Mathematical Framework for Transformer Circuits

### Strengths
The mathematical treatment of the proposed framework for concept discovery is thorough, and the examples aid in understanding. Additionally, the proposed architecture appears promising from a theoretical perspective. To the best of our knowledge, formalising concept discovery as membership on learned polynomial manifolds is novel.

### Weaknesses
There are two primary weaknesses of the paper, though these may easily reflect a lack of understanding on the part of the reviewer:
1) It is very dense, though this is somewhat expected of a theoretical paper and,
2) It is unclear whether this framework is particularly useful, either for understanding concept acquisition on currently-used transformer architectures, or for learning in their proposed architecture. For example, there are good reasons to believe that Capsule-Nets should learn to hierarchically decompose complex objects into re-usable parts, but most of the existing literature on Part-Whole hierarchies has encountered great difficulties in being applied to non-toy datasets when training with e.g. gradient descent. As such, the lack of experiments makes it unclear that a reader is well-served to work through this theoretical paper, as it is not immediately obvious that theoretical guarantees around inner-product proximity and signature computation will reflect the learning of disentangled concept manifolds in practice.

Nitpick:
1. The first sentence of section 3.1 is missing "*can be used* to group points"

### Questions
We have one high-level question regarding the practical applicability of this framework: Which constraints, if any, does the assumption of a polynomial manifold impose on the form of the input vectors which this framework could model? In particular, are there reasons to expect the assumption of linear manifolds associated with concepts to hold in practical settings, where e.g. the inputs, $x_{t}$, might be features from a complex neural network?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a new mathematics to represent and learn concepts. Learning a concept is carried out by its moment statistics matrix, which generates a concrete representation or signature of that concept. Authors also show how higher-level concepts can be developed and how relations to Transformer is also presented.

### Strengths
Representing or grounding concepts in the form of geometric manifolds is a promising approach to machine learning and artificial intelligence.

### Weaknesses
Unfortunately, this work in the current presented version is still too early for a formal publication. Some mathematical formulas are not clear. The major limitation is the missing of experiments. If the relation to Transformer can be established, can the new method outperform Transformers in some tasks?

The writing of "Proposition 1.1. (Informal summary of results)" is strange. By "Proposition" we expect formal results, but followed by "(Informal summary of results)". The lack of clarity in the mathematical formulations makes it difficult to assess the soundness of the proposed approach. For instance, the definition of the kernel signature and its relation to the moment statistics matrix needs more rigorous explanation. The paper introduces several concepts without sufficient justification or examples, making it hard to grasp their practical implications. The connection to Transformer architectures, while mentioned, is not clearly demonstrated, and it remains unclear how the proposed method could be integrated or compared with existing Transformer models. The absence of experimental validation is a significant drawback, as it is impossible to verify the effectiveness and efficiency of the proposed method in real-world scenarios. Without empirical evidence, the theoretical contributions remain speculative and lack practical relevance.

### Questions
1. in Definition 2.1, is there any restriction between d and m? For example, d > m or d < M.
2. think of the character recognition (MNIST). There are ten concepts: 0, 1, 2, ..., 9.  Given images of characters x_1, x_2, ..., Each image has the size of 28X28 pixels. How should the kernel signature be defined?  
3. in Definition 2.3, P is a mapping from R^m to R^{d-k}, but, P(X) = 0 means mapping x in R^m to R^1.  What does \mathtt{S} mean?
4. In the mechanism behind the learning method. The attention is simply based on the cosine similarity. Does this have enough representation power to distinguish manifolds located at the same orientation but different distances to a reference manifold?
5. Have you ever done any experiments with your new methods?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an approach for concept learning, that is based on the idea of generating concept signature from the matrix of moment statistics. Such signatures can be recursively combined in order to hierarchically construct higher-level concepts. The methodology is based on manifold learning via an attention mechanism, and a dictionary of concept signatures can be exploited as a sort of memory of already learned concepts.

### Strengths
+ Concept learning is a very important and challenging problem, still far from being solved. Advances in this area are crucial for the development of AI.

+ The paper presents a theoretical methodology grounded on manifold learning. The formalization is sound, as far as I could check.

### Weaknesses
- The work is mostly theoretical, with neither experiments nor examples that could drive the reader through the methodology. While the concept of combining signatures is introduced, a more concrete illustration of how this translates into learning higher-level concepts would significantly enhance understanding. For instance, an example demonstrating the transition from recognizing individual shapes to understanding spatial relationships between them would be beneficial.

- The paper does not describe how the proposed approach could be implemented in practice, i.e., for example illustrating how and whether it could scale up to a large number of concepts and manifolds, or to what extent it would be possible to associate symbols to the learned concepts. The proposed architecture of a "concept discovery unit" and a "concept dictionary" is mentioned only conceptually. A more detailed architectural diagram, outlining the data flow and the interaction between these components, would be helpful. Additionally, the paper should elaborate on how the "concept dictionary" stores and retrieves concepts, and how the "nullspace concept signatures" contribute to interpretability.

- Section 6 very briefly explains a link between the proposed approach and transformer architectures, due to the use of an attention mechanism within the manifold. This connection with transformers should probably be made more explicit, as it is not easy to grasp from Section 6. Specifically, the paper should clarify how the proposed signature generation and combination relate to the attention mechanism and subsequent feedforward network in transformers. A more detailed comparison, perhaps with a table highlighting the similarities and differences in the processing steps, would greatly improve clarity.

- The paper is well-written, but also not very easy to follow due to the complex formalism. The authors should consider simplifying the language where possible, and providing more intuitive explanations alongside the mathematical formulations. For example, the concept of "moment statistics" and their role in generating concept signatures could be explained in simpler terms.

### Questions
- Pag. 5, please check the use of $l$ vs. $\ell$.
- Pag. 6, Figure 2: "Points lies" -> "Points lie"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
