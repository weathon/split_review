# FL-GNN: A Fuzzy-logic Graph Neural Network

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
This paper presents a novel hybrid fuzzy-logic Graph Neural Network (FL-GNN) by combining Fuzzy Neural network (FNN) with GNN (Graph Neural Network) to effectively capture and aggregate local information flows within graph structural data. FL-GNN by design has three novel features. First, we introduce a specific structure fuzzy rule to boost the graph inference capability of FL-GNN to be on par with the representative GNN models. Second, we enhance the interpretability of FL-GNN by adding the analytic exploration methods to its graph inference ability from two perspectives: Fuzzy Inference System and Message Passing Algorithm (MPA). Finally, we ameliorate the structure of FL-GNN based on MPA to address the inherent limitations of FL-GNN. This optimization can reduce the calculation complexity of FL-GNN and further improve its learning efficiency. Extensive experiments are conducted to validate the graph inference capability of FL-GNN and report the performance comparison against other widely used GNN models. The results demonstrate that FL-GNN can outperform existing representative graph neural networks for graph inference tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a combination of Takagi-Sugeno Fuzzy Neural Networks (TS-FNNs) and Graph Neural Networks (GNNs), which they call a Fuzzy-Logic Graph Neural Network (FL-GNN).
The FL-GNN architecture consists of five layers: A fuzzification layer and a rule layer, followed by normalization, defuzzification and output layers.
First, the fuzzification layer assigns multiple fuzzy set membership degrees to each vertex feature of a given input graph.
Then, in the rule layer, the features of neighboring vertices are combined via learned fuzzy-logic rules whose firing strength depends on the degree to which features of adjacent vertices are members of the same fuzzy sets; the structure of those fuzzy rules is inspired by the message passing algorithm (MPA), that is typically used in GNNs.
The following three layers then transform the results of the fuzzy rules into a final prediction for each vertex.

Since the proposed architecture for FL-GNNs turns out to be computationally expensive, the authors also propose a simplified variant, called FL-GNN-A, which uses sliding windows and max pooling to significantly reduce the number of rules.

In the conducted experiments, the FL-GNN-A model was compared against multiple other state-of-the-art GNN architecture on a selection of seven common node-level and graph-level benchmark datasets.
Overall FL-GNN-A appears to perform similarly to the models it was compared against.
In the conclusion the authors state that the proposed combination of fuzzy inference and GNNs can improve interpretability and offer new insights into graph inference.

### Strengths
First, the paper is well structured and provides a good introduction to fuzzy neural networks, without assuming an in-depth knowledge about fuzzy logic and fuzzy inference.
The language is clear and the provided figures support the written explanations well and are easy to understand.

Second, the idea of combining fuzzy logic with message passing and the potential to improve model interpretability via fuzzy rules is interesting.
The example in appendix C, showing that meaningful rules can be learned via FL-GNNs, is promising.

### Weaknesses
I see the following four weaknesses, ordered descendingly by importance:

First, the paper does not provide convincing evidence that the proposed FL-GNN architecture has consistent, measurable advantages over existing GNN architectures. The experimental results show that FL-GNNs are on-par with previously proposed approaches. While the authors allude to potential insights into graph inference and improved model interpretability in the conclusion, the anecdotal evidence provided in appendix C is, by itself, not sufficient to claim that FL-GNNs provide interpretable predictions. Here, a more comprehensive evaluation and a comparison with general gradient-based approaches, such as [GradCAM](https://arxiv.org/abs/1610.02391), or graph-specific approaches, such as [GnnExplainer](https://arxiv.org/abs/1903.03894) would have been interesting. As it stands, the relevance of the proposed architecture is unclear to me.

Second, the definition of the FL-GNN architecture in section 3 is, in parts, lacking formal accuracy. Here are a few examples:
- Section 3.1: The signatures of $\phi$ and $\psi$, as well as those of $\rho$ and $\sigma$ are unclear. The authors state that the signature of $\phi$ is $V \to F_v$ but also that $\phi(v_i) \subset F_v$. Similarly, supposedly $\rho(\phi(v_i)) \subset A_v$, even though the target domain of $\rho$ is $A_v$, not $2^{A_v}$.
- Section 3.2, eq. 10: Why is the "AND" in the condition taken over all $A_m \in \{ A_{m_{1,i}},\dots, A_{m_{D,j}} \}$? Since $i$ is used to denote the feature index and $j$ to denote the index of a fuzzy  subset, $A_{m_{1,j}}$ was probably meant here. Is this correct?
- Section 3.2: $S$ is defined as the Cartesian product of $D$ sets of size $M$, therefore $|S| = M^D$; in the last line on page 4 the authors do however state that $S$ has $M^D$ subsets.
Even though each of those examples can be considered to be minor formal mistakes, the repeated unclear usage of "element" and "subset" of a set make it difficult to understand the precise meaning of the provided formal definitions.

Third, the proposed approach only considers the direct neighbors of a vertex in each rule. Indirect interactions between vertices therefore are not captured by FL-GNNs, as also alluded to by the authors at the end of appendix C.
The authors do not discuss if and how meaningful interpretations could be provided in problem domains where such indirect interactions are important.

Last, I noticed a number of minor typos, that could have easily been prevented by proofreading. A few examples: Consistently used "Coar" instead of "Cora" in section 4, "fields such as medical image process" (page 1), "information are ubiquitous" (page 2).

### Questions
1. Is there additional evidence supporting the claim that FL-GNNs can provide meaningful interpretations? Is the quality of those interpretations/explanations better than that of other XAI approaches?
2. Concerning the formal definitions, can you clarify the intended meaning of the mentioned formulas?
3. Can FL-GNNs be adapted to also capture indirect vertex interactions and, if so, how?

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a hybrid fuzzy-logic graph neural network by combining fuzzy neural network with GNN to effectively capture and aggregate local information flows within graph structural data. FL-GNN by design has three novel features. The structure fuzzy rule is to boost the graph inference capability. The interpretability is enhanced by adding the analytic exploration methods to its graph inference. The experiments show the improvements over several baselines.

### Strengths
1. This paper focuses on an interesting problem to the graph machine learning community, which is to combine fuzzy neural network with GNN.
2. The paper is well written. The framework is clear to present the details of the proposed method, especially Figure 1 and 2.
3. The experiments are conducted on real-world datasets such as OGB.

### Weaknesses
1. Some claims need to be further validated. The authors argue that the interpretability of FL-GNN is good while they ignore the experiments to compare with some graph interpretability baselines (please refer to [1]). Specifically, the paper lacks a quantitative comparison demonstrating how the fuzzy rules provide better interpretability compared to methods like GNNExplainer, which directly identifies important edges or subgraphs for a prediction. The current analysis is limited to a qualitative discussion of the fuzzy rules, which is insufficient to claim superior interpretability.
2. The experiments in terms of node-level predictions should consider more large-scale datasets from OGB, just as the authors have done in graph-level predictions. The current node-level experiments are limited in scale and do not fully demonstrate the scalability of the proposed method. It is important to evaluate the performance on datasets with a larger number of nodes and edges to validate the practical applicability of the model.
3. Typos: dataset name Coar -> Cora in section 4.1.

### Questions
See weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces the FL-GNN, a fusion of Fuzzy Neural Network (FNN) and Graph Neural Network (GNN), aiming to harness the benefits of fuzzy logic in graph inference. The proposed model addresses key challenges in GNN, boosting its inference capabilities, enhancing interpretability, and improving efficiency by reducing computational complexity.

### Strengths
* Novel Approach: The amalgamation of FNN and GNN is an innovative step, seeking to combine the strengths of both paradigms for improved graph inference.

* Enhanced Interpretability: One significant contribution is the enhancement in model interpretability, a challenge with many machine learning models, especially neural networks.

### Weaknesses
 * While the paper claims that FL-GNN outperforms other GNN models, it could benefit from a more rigorous benchmarking, including challenges faced, methodologies adopted, and potential pitfalls.

* It would benefit the paper to clearly outline the limitations of the proposed FL-GNN, and how these have been addressed, to provide a comprehensive perspective.

### Questions
* In addition to benchmarking performance, a detailed comparative analysis on how FL-GNN overcomes the limitations of standard GNNs would be insightful.

* The introduction of terms such as Type-2 fuzzy sets and intuitionistic fuzzy sets, which are mentioned as future work, might be unfamiliar to some readers. A brief description or reference would be helpful.

* Please provide more discussion on the related works [1,2]

[1] Fuzzy Representation Learning on Graph (https://ieeexplore.ieee.org/document/10061283)

[2] Graph Fuzzy System for the Whole Graph Prediction: Concepts, Models and Algorithms (https://ieeexplore.ieee.org/document/10287583)"

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
