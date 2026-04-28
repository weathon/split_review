# Holographic Node Representations: Pre-training Task-Agnostic Node Embeddings

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Large general purpose pre-trained models have revolutionized computer vision and natural language understanding. However, the development of general purpose pre-trained Graph Neural Networks (GNNs) lags behind other domains due to the lack of suitable generalist node representations. Existing GNN architectures are often tailored to specific task orders, such as node-level, link-level, or higher-order tasks, because different tasks require distinct permutation symmetries, which are difficult to reconcile within a single model. In this paper, we propose _holographic node representations_, a new blueprint for node representations capable of solving tasks of any order. Holographic node representations have two key components: (1) a task-agnostic expansion map, which produces highly expressive, high-dimensional embeddings, free from node-permutation symmetries, to be fed into (2) a reduction map that carefully reintroduces the relevant permutation symmetries to produce low-dimensional, task-specific embeddings. We show that well-constructed expansion maps enable simple and efficient reduction maps, which can be adapted for any task order. Empirical results show that holographic node representations can be effectively pre-trained and reused across tasks of varying orders, yielding up to 100% relative performance improvement, including in cases where prior methods fail entirely.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes holographic node representations that are capable of solving tasks of any order (node: 1st order and edge: 2nd order, etc). The proposed holographic node representations consist of two components: (1) a task-agnostic expansion map, which produces highly expressive, high-dimensional embeddings, and (2) a reduction map, which introduces the relevant permutation symmetries. The experimental results show that the holographic node representations show the best performance across tasks of varying order.

### Strengths
- The proposed paper is well-written.
- The research question of the paper is really interesting.
- The proposed approach is novel and interesting.

### Weaknesses
 - It would be better if the paper included experimental results on graph classification. This paper shows the effectiveness of the holistic node representations using node classification, link prediction, and meta-path prediction (UserMovieUser). But I wonder if the proposed representations perform well on graph classification.

### Questions
Please refer to the weaknesses section.

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
The paper aims to learn node embeddings capable of solving multiple graph learning tasks. It first presents the challenge of existing node embedding models in solving multiple tasks. To address this challenge, the paper proposes a holographic node representation model named HoloGNN. HoloGNN consists of two components: an expansion map that produces descriptive symmetry-free representations, and a reduction map that introduces task-specific symmetries to obtain embeddings tailored for a specific task. Experimental results on four graph datasets show that compared with baselines, the HoloGNN is more effective in adapting GNN pre-trained on one task to other tasks.

### Strengths
The idea of generating holographic node embeddings to address multiple graph learning tasks seems novel and interesting. The paper provides theoretical analyses to justify the validity of the proposed method. Experimental results show that the proposed HoloGNN can effectively adapt GNN trained on one task to other tasks.

### Weaknesses
1. There is no justification for Property (1) and Property (2).

2. Section 4.1 is difficult to follow as it lacks sufficient details on the node-breaking selectors. More elaborations about node-breaking selectors and why these selectos are needed in the expansion map should be provided to enhance clarity. Specifically, the paper does not provide a theoretical proof that these properties hold, which is necessary since they are not self-evident. The paper needs to demonstrate that the proposed node-breaking selectors satisfy these properties.

3. The proposed HoloGNN is quite complicated since it requires breaking symmetries using either sequential breaking or parallel breaking algorithms. Complexity analyses should be provided to understand the additional computational cost introduced by these algorithms and to clarify whether the parallel breaking algorithm can effectively reduce the cost. It is unclear how the computational cost scales with the number of nodes, edges, and the number of breaking operations.

4. The paper lacks discussions and comparisons with the graph transformer models. What are the advantages of the proposed HoloGNN model compared with graph transformer models? Specifically, how does HoloGNN handle positional information compared to graph transformers, and why is this approach more suitable for multi-task learning?

5. I have some major concerns regarding the experiments:

(1) The HoloGNN is designed to be pre-trained and then adapted to any graph learning tasks (line 46-47). However, in the experiments, the paper only shows the results of HoloGNN when it is pre-trained on a single task (e.g., node classification) within a single dataset and then adapted to another task (e.g., link prediction) on the same dataset. This evaluation is insufficient to validate the generalisation of HoloGNN across different datasets and tasks. A potential solution is to pre-train HoloGNN on one task across all the datasets and then evaluate its performance across different datasets and tasks, including the pre-training task. The current experimental setup only demonstrates task transferability within the same dataset, which is a significant limitation.

(2) The results in Figure 3 show that the performance of pre-trained HoloGNN is worse than that of HoloGNN trained from scratch. Is pre-training still necessary in these scenarios? The paper needs to clarify the specific scenarios where pre-training is beneficial, given that it does not seem to improve performance in the current experiments.

(3) The results and analyses on the MovieLens dataset are difficult to understand. More explanations should be provided to enhance the clarity. The paper should provide a more detailed explanation of the experimental setup and results on this dataset.

(4) The paper lacks analyses of the impacts of some hyperparameters in the HoloGNN model, such as $T$ and $L$ in equation (2). The paper should include a sensitivity analysis of these hyperparameters to understand their impact on the model's performance.

6. The paper mainly focuses on the node classification and link prediction tasks. I would if the proposed HoloGNN model can be applied to the graph classification task and how it might perform in that task. The paper should discuss the applicability of HoloGNN to graph classification and provide experimental results to support its claim.

7. The code is not available, which makes it difficult to reproduce the results given the proposed model is rather complicated.

### Questions
Please see the questions in the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper propose a new approach that allows node embeddings to be trained on any task (e.g. link prediction) and then easily adapted to other tasks (e.g. node classifcation).

### Strengths
1. The paper proposed an interesting approach by learning a 'holographic' node representation that contains multiple view of representations and utilized a reduce map to produce a specific embedding for specific task.
2. The authors provide thorough and interesting analysis for holoGNN from the perspective of canonical eigenvectors.

### Weaknesses
1. My major concern is about the 'pretraining' term used in the work, as it is biased from the widely accepted perspective. For the community, pretraining usually refers to an unsupervised task, e.g. language modeling or predicting next token in language models (LM); or graph reconstruction tasks in [1]. However, the proposed method and experiment setting in this paper is more like 'traditional transfer learning' which learn representations from one downstream task (task labels are necessary, e.g. node classification) and adapt them to another task (e.g. link prediction). From the perspecctive of pretraining, the experiment setting is not suitable since it solely evals one downstream task. As a result, I would like to advise the author revise the term to make this part consistent.

2. The paper's framing of 'pretraining' is further weakened by the limited scale of the datasets used. The primary experiments are conducted on datasets like Cora, which only contains a few thousand nodes. This raises concerns about whether the 'pretraining' procedure on such small datasets is truly representative of the benefits one might expect from a genuine pretraining approach on much larger graphs. The lack of experiments on larger, more complex graphs makes it difficult to assess the practical scalability and effectiveness of the proposed method as a pretraining strategy.

### Questions
1. Does the authors regard the HoloGNN as a pretraining approach? If so, it would be better if they could provide comparison analysis against other pretraining methods, e.g. [1][2]. However, from my point view, the paper is more about 'transfer learning' which learns from one downstream task and adapt to another. From this perspective, a thorough refinement of the paper is necessary.

[1] Hu, Weihua, et al. "Strategies for pre-training graph neural networks." _arXiv preprint arXiv:1905.12265_ (2019).
[2] Hu, Ziniu, et al. "Gpt-gnn: Generative pre-training of graph neural networks." Proceedings of the 26th ACM SIGKDD international conference on knowledge discovery & data mining. 2020.

### Soundness
2

### Presentation
3

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
This work investigates the ability of node embeddings to solve various graph tasks. From the preliminary results that no existing node embeddings could solve all the tasks, it proposes holographic node representations to learn symmetry-free embeddings and reintroduce the task-specific symmetries back to the model. Both theoretical analysis and empirical results are provided.

### Strengths
1. The paper is generally well structured and easy to follow.
2. In addition to extensive empirical verification, most of the designs adopted in the proposal are also theoretically justified.
3. The findings that the source of task-specific embeddings is symmetry are distinctive across different tasks is really interesting.

### Weaknesses
1. As the very first definition of the paper, Structural Representation is not very clear. For example, in line 107, 'order r' is confusing, since it was previously defined as the cardinality of a node subset S. And the explanations for the subscript S, $\pi \circ$, and permutation matrices are missing from the definitional formulation. Also, how do I understand the output format of the function f, which is not clear to me? Do the last r rows of the output matrix repeat some r rows of the previous n rows?
2. The same question appears in the formulation of the reduction map: where is the input of r for the corresponding output matrix in equation (3)? Before presenting the idea of task-agnostic node embeddings, it seems to me that a more general question should be asked: what kind of task-agnostic information can we store in node embeddings? This is because the analogy between pre-training for word embeddings and node embeddings is not perfectly aligned across different graphs. If the scenario we're focusing on in this paper is the nodes from the same graph, then it's necessary to make this point very clear.
3. It is confusing to me that in the real world, most of the graphs come with node-level distinctive features, which is fed in $V_1$, for this purpose, how significant is the necessity of breaking symmetry technique to distinguish structurally isomorphic nodes? It seems that the practical impact of this symmetry breaking is not well justified given the prevalence of node features in real-world graphs.
4. There is one point that seems counter-intuitive to me: if the downstream tasks are always embodied with certain structural symmetries, since after all they are performed in the graph domain, then whether it is a bit detour to dismiss all symmetries in the expansion map step? Why not preserve all symmetries in the first place, but fuse them without bias, and then follow the same idea of the current design of the reduction map?

### Questions
1. Line 43: It needs more explanation about "different permutation symmetries with respect to different task orders"? Same question for the first paragraph of the second section.
2. Why do the links in Figure 1 not preserve isomorphism?
3. It's kinda hard for me to understand lines 137-141. If the extra task-specific embeddings don't negatively affect the performance of another task, then what's the difference between the proposal and naively concatenating all task-specific embeddings?
4. Can you briefly explain/show what the 'single node permutation' is?
5. The isomorphism in this paper refers to the one defined by first-order neighbor?

### Soundness
4

### Presentation
3

### Contribution
3
