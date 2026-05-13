# Rethinking Neural Multi-Objective Combinatorial Optimization via Neat Weight Embedding

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Recent decomposition-based neural multi-objective combinatorial optimization (MOCO) methods struggle to achieve desirable performance. Even equipped with complex learning techniques, they often suffer from significant optimality gaps in weight-specific subproblems. To address this challenge, we propose a neat weight embedding method to learn weight-specific representations, which captures weight-instance interaction for the subproblems and was overlooked by most current methods. We demonstrate the potentials of our method in two instantiations. First, we introduce a succinct addition model to learn weight-specific node embeddings, which surpassed most existing neural methods. Second, we design an enhanced conditional attention model to simultaneously learn the weight embedding and node embeddings, which yielded new state-of-the-art performance. Experimental results on classic MOCO problems verified the superiority of our method. Remarkably, our method also exhibits favorable generalization performance across problem sizes, even outperforming the neural method specialized for boosting size generalization.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel but simple neural multi-objective combinatorial optimization (MOCO) method. Specifically, the paper proposes a single-model method which can effectively solve MOCO problems (such as the multi-objective variants of the Traveling Salesman Problem or Capacitated Vehicle Routing Problem). This model is capable of learning the interaction of the problem instances with the weight vectors that are provided to decompose the problem into smaller, scalarized subproblems. At inference time, this allows the user to specify N weight vectors along with the problem instance, thereby producing a Pareto front of solutions. The authors introduce two variations of their method. In the first approach, named WE-Add, the interaction of the weight vectors and the node features is captured by simply adding their linear projections to get the node embeddings in the encoder of the model. In the second approach, WE-CA, the authors leverage a conditional attention model to capture the interaction of the instance and the weight vector. First, node embeddings conditioned on the weight vectors are derived through feature-wise affine transformations of the linear projections of the node features and weight vectors. Then, these embeddings are passed through standard transformer encoder layers, with multi-headed attention, instance normalization and feed forward networks. The authors demonstrate that this model not only reduces the optimality gaps of the subproblems but can also generalize well to problems of different sizes.

### Strengths
### Originality
The method of deploying "conditional attention" as proposed in the paper is simple and novel.

### Quality
With the exception of the points discussed in the Weaknesses Section, the paper is of good quality.
1. The paper features a comprehensive list of experiments. It discusses variations of several important problems, such as 20, 50, and 100 node variants of the bi- and tri-objective Traveling Salesman Problem (Bi-TSP and Tri-TSP), bi-objective Capacitated Vehicular Routing Problem (Bi-CVRP), and bi-objective Knapsack Problem (Bi-KP). The paper also demonstrates the out-of-distribution generalization for 150 and 200 node variants of Bi-TSP.
2. The authors justify their method which uses *conditional attention* by running ablation studies for its important components, such as *conditional embeddings* and *attention*. The experiments show that the combination of both these ideas work better than either one in isolation.


### Clarity

The paper is well-written. The ideas are communicated clearly. For example, Section 4.1 explains the base model that is used, and then builds on it in Section 4.2 to explain the model with conditional attention, making it easy to follow.

### Significance
The contributions of the paper are significant:
1. The simplicity of the method is commendable.
2. The proposed method shows strong performance compared to the baselines, showing smaller optimality gaps for the subproblems and higher hypervolumes, with comparable or faster solving times.
3. Also interesting is the finding that a unified model trained this way generally performs better than models trained for problems of specific sizes.

### Weaknesses
1. The authors could a clear definition of what they mean by "neat" in the context of their work, and highlight specific sections where they could elaborate on how their method contrasts with the complexity of existing approaches.
2. In the Methods section, while the structure of the proposed architecture is described, I would like to see a more detailed explanation of why each component is expected to improve performance. Specifically, theoretical justifications for key components such as the addition-based weight embedding and the conditional attention mechanism would be helpful. Some discussion of how the proposed components address specific limitations of previous approaches would also strengthen the work.
3. It would be valuable to see more ablation studies that isolate the contributions of each architectural component. For example, a fair experiment design that solely isolates the effect of the addition-based weight embedding.

### Questions
Can the authors justify the reference points that were chosen for the experiments?

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
This paper introduced a new way for directly learning weight-specific representations, thereby improving the handling of decomposed subproblems. The authors designed two models for weight embedding: one is an additive embedding model, which performs embedding through simple addition operations; the other is a conditional attention model, which more accurately captures the interaction between weights and instance information through a conditional attention mechanism.

### Strengths
The weight embedding method proposed in this paper directly learns weight-specific representations, avoiding tedious adjustments and high computational costs, while improving performance without increasing model complexity.

The weight embedding method not only performs well across various problem scales but also shows strong generalization across different scales (such as varying numbers of nodes or task complexity). This capability allows the model to maintain good optimization performance when encountering problems of different scales or new challenges, demonstrating high adaptability. The additive weight embedding and conditional attention weight embedding models designed in the paper are not only straightforward but also adaptable to various MOCO tasks.

The authors also provides a lot of experiments for validation, showing the superority for their performance.

### Weaknesses
I think it would be beneficial to include more theoretical discussions. For example, the paper mentions that the weighted approach can improve generalization; adding a proof for the generalization bound would make the results more convincing. Additionally, when the number of classes approaches infinity, will this weighting approach converge to the average weight?

### Questions
For larger-scale problems, such as those with a large number of objective functions or high dimensions, how efficient is weight embedding? If the number of variables is quite large, could this impact the precision of weight learning? Will it still lead to improvements in training results?

Do the authors plan to release the code for validation? I believe that such a detailed comparison could be a great contribution to the community.

### Soundness
3

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
The paper presents a method for solving Neural Multi-Objective Combinatorial Optimization (MOCO) using a "neat" weight embedding approach. The authors argue that existing MOCO models are limited in their ability to effectively optimize weight-specific subproblems due to complex learning techniques and significant optimality gaps. Their proposed method learns weight-specific representations through a simpler weight embedding technique, capturing weight-instance interactions. Two models instantiate this approach: one with addition-based weight embedding and another with conditional attention. Experimental results demonstrate the method’s performance on benchmark MOCO problems, showing significant improvements in generalization across different problem sizes.

### Strengths
This work has extensive experiments that show the effectiveness of the proposed method and show strong cross-size generalization capabilities.

### Weaknesses
1. The authors could a clear definition of what they mean by "neat" in the context of their work, and highlight specific sections where they could elaborate on how their method contrasts with the complexity of existing approaches.
2. In the Methods section, while the structure of the proposed architecture is described, I would like to see a more detailed explanation of why each component is expected to improve performance. Specifically, theoretical justifications for key components such as the addition-based weight embedding and the conditional attention mechanism would be helpful. Some discussion of how the proposed components address specific limitations of previous approaches would also strengthen the work.
3. It would be valuable to see more ablation studies that isolate the contributions of each architectural component. For example, a fair experiment design that solely isolates the effect of the addition-based weight embedding.

### Questions
1. In Fig. 1, what is the input to get $h_c$ when $t=1$ in the decoder?
2. In Table 2, the proposed method appears to be slower than PMOCO. Does this indicate that the efficiency is worse compared to the baseline (given the 'neatness')?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel weight embedding approach for neural multi-objective combinatorial optimization (MOCO) to address the optimality challenges observed in current decomposition-based methods. It focuses on capturing weight-instance interaction through a weight-specific representation learned directly within the neural model. Two model variations—Weight Embedding with Addition (WE-Add) and Weight Embedding with Conditional Attention (WE-CA)—are introduced. These models simplify MOCO by avoiding complex auxiliary techniques and showcase state-of-the-art performance across several MOCO problems, specifically the multi-objective traveling salesman, capacitated vehicle routing, and knapsack problems.

### Strengths
- Direct weight embedding is a fresh perspective in MOCO, addressing a gap in existing neural approaches that often require complex multi-model techniques.
- The paper provides thorough experimental results, comparing its models with state-of-the-art baselines (including multi-model, single-model, and heuristic-based methods) on three classic MOCO problems across different scales.
- The proposed WE-CA model achieves superior performance in terms of hypervolume (HV) and execution time, particularly highlighting its generalization capabilities across problem sizes.
- The models eliminate the need for size-aware embedding mechanisms, thus simplifying the optimization process.

### Weaknesses
- Real-world applications with complex constraints are acknowledged as challenging for this approach. Further exploration into handling such constraints would enhance the paper's practical relevance.

- The paper’s unified training model, WE-CA-U, provides promising generalization across problem sizes, but more discussion on its failure cases (where applicable) would improve understanding of its limitations.

### Questions
1-  In cases where the unified model fails to generalize effectively to certain sizes, could you provide more details on why this happens? Are there specific problem characteristics or settings that lead to these limitations?

2- Could you elaborate on how the conditional attention layer facilitates weight-instance interaction? While the paper describes the feature-wise linear projection mechanism, more insight into its layer-wise influence on embeddings would clarify how it improves optimality across subproblems.

### Soundness
3

### Presentation
4

### Contribution
4
