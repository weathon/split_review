# Distortion-free and GPU-compatible Tree Embeddings in Hyperbolic Space

- Decision: Reject
- Scores: 8, 6, 8, 6, 6

## Abstract
Embedding tree-like data, from hierarchies to ontologies and taxonomies, forms a well-studied problem for representing knowledge across many domains. Hyperbolic geometry provides a natural solution for embedding trees, with vastly superior performance over Euclidean embeddings. Recent literature has shown that hyperbolic tree embeddings can even be placed on top of neural networks for hierarchical knowledge integration in deep learning settings. For all applications, a faithful embedding of trees is needed, with combinatorial constructions emerging as the most effective direction. This paper identifies and solves two key limitations of existing works. First, the combinatorial construction hinges on finding maximally separated points on a hypersphere, a notoriously difficult problem. Current approaches lead to poor separation, which degrades the quality of the corresponding hyperbolic embedding. As a solution, we propose maximally separated Delaunay tree embeddings (MS-DTE), where during placement, the children of a node are maximally separated through optimization, which directly leads to lower embedding distortion. Second, low distortion requires additional precision. The current approach for increasing precision is to use multiple precision arithmetic, which renders the embeddings useless on GPUs in deep learning settings. We reformulate the combinatorial construction using floating point expansion arithmetic, leading to superior embedding quality while simultaneously retaining their use on accelerated hardware.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper refines an algorithm for tree embeddings via projected stochastic descent and improved floating point arithmetic. The authors identify an issue with an algorithm for uniformly sampling points on hyperplanes in the Poincare disk, which is a crucial part of a classical tree embedding algorithm. They then compare their approach to other well-known methods and obtain consistently improved performance.

### Strengths
1. Fast implementation using projected gradient descent.
2. Empirical efficacy
3. The solution to the floating point arithmetic degeneracy ailment is crucial due to calculations of the division of small numbers. I find it to be very interesting.

### Weaknesses
1. There are no claims of empirical results for downstream tasks, despite the introduction which claims the importance of tree embeddings for downstream tasks.

2. Code isn't available.

### Questions
1. Can you explain Figure 1 (b)?

### Soundness
4

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
5

### Summary
This paper tackles two key challenges in embedding tree-structured data using hyperbolic geometry, a mathmatical concept known for effectively capturing hierarchical relationships. Traditional combinatorial methods struggle with finding maximally separated points on a hypersphere, leading to poor separation and high distortion in embeddings. The authors introduce maximally separated Delaunay tree embeddings (MS-DTE), which optimize child node placement to reduce distortion. Additionally, they address the precision requirements for low-distortion embeddings, replacing multiple-precision arithmetic with floating-point expansion to ensure compatibility with GPU acceleration. MS-DTE offers a more accurate and hardware-compatible approach for hyperbolic embeddings, facilitating their use in deep learning.

### Strengths
This paper tries to improve the hyperbolic embedding method for tree-like data in two aspects: lower distortion and higher precision. It demonstrates effectiveness through several experiments.

### Weaknesses
My primary concern with this paper lies in its limited exploration of embedding dimensions, as all experiments are confined to fixed dimensions of 8 or 10. Hyperbolic spaces are indeed well-suited for embedding tree-like structures in low dimensions with minimal distortion, as shown by prior work such as Sala et al. (2018), which evaluated dimensions from 2 to 200. The restricted range of dimensions examined here leaves questions about the method's robustness across different dimensional settings and its performance at lower dimensions, which could highlight the embedding quality and distortion more clearly.

Moreover, in the specific experiment detailed in Table 1, the authors embed an 8-depth binary tree in a 10-dimensional space. Given the remark in lines 232-233 about point generation limitations in low-dimensional spaces, this experiment does not seem sufficient to validate these claims, as a binary tree should be well-represented in 10 dimensions without encountering major separation limitations. Additionally, as the node degree is 2 in this case, the proposed MHS in Equation 14 appears equivalent to Liu et al.’s (2018) approach in Equation 13, raising concerns about the distinct advantage claimed for this setting.

To strengthen the paper, I recommend conducting experiments across a wider range of dimensions, particularly in low dimensions, which would not only enable visualization but also demonstrate the effectiveness of the proposed GPU-compatible floating-point expansion approach. This expanded experimentation would provide a more comprehensive evaluation of the proposed method’s advantages and limitations.

### Questions
1. What is $s$ in Eq 13


2. In lines 250-254, you discuss the limitation of Eq. 13. Is this a mere observation or a conclusion drawn from empirical analysis? Have you experimented with using Equation 13 as an objective function, and if so, what were the results?

3. In Equation 14, is the objective minimizing the absolute angle value? Note this is equivalent to minimizing the geodesic distance between vectors. Why not instead minimize the cosine value between the angles?

4. You note that the effective number of nodes is lower in practice due to the high frequency of low-degree nodes, allowing cached hyperspherical points to be reused (lines 271-272). Could you provide more context (statistics on dataset) on how frequently these caches are applied and their impact on computational efficiency?

5. While the paper focuses on the embedding method itself, have you evaluated the utility of these embeddings in downstream tasks? For example, Nickel and Kiela (2017) demonstrated the effectiveness of their embeddings on link prediction. Any insights on potential downstream improvements would be helpful.


6. Have you evaluated the proposed model on WordNet?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors introduce maximally separated Delaunay tree embeddings to construct tree embeddings in hyperbolic spaces, particularly in the Poincaré ball model. Empirically, they show that their method improves upon existing methods. Additionally, they present a method for the arithmetic expansion of floating-point numbers in tensors, allowing for increased calculation precision without losing the benefits of hardware acceleration.

### Strengths
The authors present a series of interesting theoretical results with clear and well-written proofs. These results serve as the fundamental backbone of the work, making it well-written and cohesive.

### Weaknesses
1. Line 855 is not clearly understandable; there is likely a typo. 
2. Theorems 3 and 5 seem more straightforward than presented. It would be better to state them as propositions and briefly comment on their proofs.

### Questions
1. Could it be possible to elaborate a bit more on the third limitation (line 236)? I may have missed something, but it doesn't seem entirely clear based on the current text.
2. Can you use isometries between hyperbolic spaces to study another manifolds? I think maybe some properties will be preserved.
3. Can you derive an extension of Theorem 1 changing MHS? The proof may be similar.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
Embedding tree structures in hyperbolic space enhances knowledge representation, especially for hierarchies and ontologies. This paper addresses two key challenges: poor point separation and limited hardware compatibility. It proposes maximally separated Delaunay tree embeddings (MS-DTE) and floating-point expansion arithmetic, achieving lower distortion and efficient GPU use, which improves embedding quality in deep learning applications.

### Strengths
- The paper is well-structured.
- The proposed method is well-justified.
- The method demonstrates strong performance improvements.

### Weaknesses
- The experimental evaluation lacks comprehensiveness.

### Questions
- In the abstract, "directly leads to lower embedding distortion" is mentioned; if the method only reduces distortion, what justifies the use of "distortion-free" in the title?
- The relationship between "DISTORTION-FREE," "GPU-COMPATIBLE," and performance in downstream tasks remains unclear.
- The impact of finding maximally separated points on a hypersphere for downstream tasks needs clarification.
- Experimental details are incomplete, as MHS requires training.
- The paper should include an analysis of computational complexity and overhead.
- Parameter analysis for the scaling factor $\tau$ is needed, as different values are used across tasks.
- Why is the MAP metric omitted from Table 3 and Table 4?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a new hyperbolic embedding algorithm for tree data. The authors propose a Delaunay tree embedding with maximum separation (MS-DTE), where during placement, the child nodes of the node directly result in lower embedding distortion by optimizing the maximum separation. To solve the problem of floating point precision at the edge of Poincare-ball space, a gpu multi-precision algorithm is proposed.

### Strengths
1.The motivation of this article is very natural. The tree structure embedding in hyperbolic space does have two problems mentioned .
2.The paper is well written and is easy to understand.
The theory of the article is very solid, and the precision problem is explained very well.

### Weaknesses
1.This approach is aimed at hyperbolic embedding of tree structures, but does not seem to be able to handle general data (there is no explicit tree structure, but often there is an underlying tree structure).
2. The author lacks a discussion of algorithm complexity. Especially for the accuracy problem, whether it will cause a greater amount of calculation.

### Questions
1. Can this precision processing method be applied to general hyperbolic neural networks? As we all know, hyperbolic machine learning has two problems, precision error and difficult optimization.
2. See other questions in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
4
