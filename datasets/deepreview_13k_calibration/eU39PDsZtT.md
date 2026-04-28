# GraphRouter: A Graph-based Router for LLM Selections

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
The rapidly growing number and variety of Large Language Models (LLMs) present significant challenges in efficiently selecting the appropriate LLM for a given query, especially considering the trade-offs between performance and computational cost. Current LLM selection methods often struggle to generalize across new LLMs and different tasks because of their limited ability to leverage contextual interactions among tasks, queries, and LLMs, as well as their dependence on a transductive learning framework. To address these shortcomings, we introduce a novel inductive graph framework, named as \method, which fully utilizes the contextual information among tasks, queries, and LLMs to enhance the LLM selection process. \method constructs a heterogeneous graph comprising task, query, and LLM nodes, with interactions represented as edges, which efficiently captures the contextual information between the query's requirements and the LLM's capabilities. Through an innovative edge prediction mechanism, \method is able to predict attributes (the effect and cost of LLM response) of potential edges, allowing for optimized recommendations that adapt to both existing and newly introduced LLMs without requiring retraining. Comprehensive experiments across three distinct effect-cost weight scenarios have shown that \method substantially surpasses existing routers, delivering a minimum performance improvement of 12.3\%. In addition, it achieves enhanced generalization across new LLMs settings and supports diverse tasks with at least a 9.5\% boost in effect and a significant reduction in computational demands. This work endeavors to apply a graph-based approach for the contextual and adaptive selection of LLMs, offering insights for real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of LLM selection for specific tasks and proposes a graph-based routing framework to select suitable LLM for the input query. By modeling the contextual information among tasks, queries, and LLMs as a heterogeneous graph, query, and LLM nodes, with interactions represented as edges, which efficiently captures the contextual information between the query’s requirements and the LLM’s capabilities. From the experiments, the authors compared the proposed method with different baselines and show that it can outperform regarding the reward. However, there are some issues that need to be addressed for better quality.

### Strengths
1. This paper studies the challenging LLM model selection problem, which has been well addressed.

2. This paper considers leveraging graph learning to incorporate more contextual information for LLM model selection.

3. The experiments show that the proposed method achieves good performance compared to baselines.

### Weaknesses
1. The studied setting is not quite realistic. The proposed method constructs a graph with task, query, and LLM nodes. For each query, it may select a different LLM to answer the query, which is quite unrealistic in practice. Specifically, in real-world scenarios, it's often necessary to maintain a consistent model for a given user session or application context, rather than switching models on a per-query basis due to the overhead of loading different models and maintaining their state. This frequent switching also introduces latency and complexity that are not accounted for in the current evaluation.

2. The model performance especially cost may vary a lot on different hardware settings. It is also unrealistic to make sure the real hardware used can align with the numbers in the training data. And we cannot curate the training data for different hardware settings. The reported cost metrics, which are likely based on API pricing or token counts, may not accurately reflect the actual computational cost on different hardware configurations. For example, the inference time and memory usage of different LLMs can vary significantly depending on the underlying hardware (e.g., CPU vs. GPU, different GPU models), which is not captured by the current cost definition. This makes it difficult to generalize the results to real-world deployments where hardware constraints are a major factor.

3. Some details are unclear. For example, in table 5, what is the specific reward used for evaluation? And what is the purpose of adding task nodes? Can we just incorporate the information of task nodes into the query nodes? The reward function used in the experiments is not clearly defined, making it difficult to reproduce the results or compare them with other methods. Furthermore, the rationale behind including task nodes as separate entities in the graph is not fully justified. It is unclear why task information cannot be effectively encoded within the query node features, which would simplify the graph structure and potentially reduce computational overhead.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces GraphRouter, a novel graph-based approach for selecting appropriate LLMs for different queries. The authors construct a heterogeneous graph comprising task, query, and LLM nodes, with interactions represented as edges to capture contextual relationships. Through an innovative edge prediction mechanism, GraphRouter can adapt to both existing and newly introduced LLMs without requiring retraining. The work demonstrates significant performance improvements over baseline methods across multiple experimental settings, achieving at least 12.3% improvement in standard scenarios and 9.5% improvement in new LLM scenarios. The framework is evaluated on four distinct tasks (Alpaca, GSM8K, SQUAD, Multi-News) using ten different LLMs under various performance-cost tradeoff conditions.

### Strengths
The paper seems to be the first to reformulate LLM selection as a graph-based edge prediction problem, providing a fresh perspective on router design. The heterogeneous graph structure effectively captures the complex relationships between tasks, queries, and LLMs. The framework addresses real-world challenges in LLM deployment, particularly the ability to handle new LLMs without retraining and balance performance with computational costs. The evaluation across three different cost-performance scenarios demonstrates practical utility. The authors conduct thorough experiments using multiple datasets, LLMs, and evaluation metrics. The ablation studies on GNN layer count and size provide useful insights for implementation.

### Weaknesses
1.	Authors only provide intuitive explanations for why graph structure should help with LLM selection, lacking analysis on why edge prediction correlates with routing performance. Also, the paper fails to explain why the heterogeneous graph structure (Figure 5) is optimal for capturing LLM-query relationships. Specifically, the paper does not provide a rigorous justification for why predicting edges between query and LLM nodes directly translates to optimal LLM selection. The connection between the predicted edge weights and the actual performance of the selected LLM is not clearly established, and the assumption that higher edge weights correspond to better LLM choices needs more theoretical backing.
2.	In L. 219, task-query edges are initialized uniformly to 1, which seems overly simplistic given the rich task-query relationships that could be captured. LLM-query edge features only use performance and cost concatenation, ignoring other potentially valuable signals like response length or generation time. The lack of exploration into alternative edge features is a significant oversight. The paper does not justify why the chosen features are sufficient and fails to consider how other features might improve the model's ability to capture the nuances of LLM-query interactions. For example, response length could indicate verbosity, while generation time could reflect computational efficiency, both of which are relevant to LLM selection.
3.	The ablation studies in Section 4.3 don't explore alternative edge feature designs Example: In Table 4, some performance variations could potentially be explained by inadequate edge features, but this is not analyzed. The ablation study focuses on GNN layers and embedding size but neglects the impact of different edge feature combinations. This is a critical omission, as the quality of edge features directly impacts the GNN's ability to learn meaningful representations. Without exploring alternative edge features, it's difficult to ascertain whether the performance gains are due to the graph structure or simply the chosen edge features.
4.	L. 327 present results across different LLMs but don't analyze how model architectures affect routing decisions. There is no discussion of how to efficiently update the graph structure when new LLMs are added Example: The experiments in Table 5 show impressive few-shot performance but don't evaluate beyond 10 LLMs, leaving questions about larger-scale deployments. The paper lacks an analysis of how different LLM architectures (e.g., transformer-based vs. other architectures) influence the routing decisions made by GraphRouter. The framework's scalability is also questionable, as the experiments are limited to only ten LLMs, and there is no discussion on how the graph structure would be updated when new LLMs are introduced, particularly in a dynamic environment where LLMs are constantly evolving.
5.	While GNN layer count is analyzed, other hyperparameters and embedding dimension are not thoroughly explored, but I think this is a minor problem.

### Questions
1．	How does the performance of GraphRouter change when handling LLMs with similar architectures but different sizes (e.g., different versions of LLaMA)? Is the framework able to effectively distinguish between such similar models?
2．	Could you elaborate on how the framework would handle dynamic updates to LLM capabilities, such as when models are fine-tuned or updated? Would this require rebuilding the entire graph?
3．	Have you considered incorporating more sophisticated edge features, particularly for task-query relationships? How might this affect the framework's performance?

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
4

### Summary
This paper studies the LLM-Selection task, i.e., given a user query, selecting the appropriate LLM for execution that achieves the balance between performance and cost. Motivated by the contextual relationships between tasks, queries and LLMs, this paper utilizes a graph structure to represent these information and reformulates the LLM-Selection problem as a link-prediction task within graph. The proposed GraphRouter framework leverages a GNN to perform this task and can easily adapt to an inductive setting, accommodating the rapid evolution of LLMs. Extensive experiments in both transductive and inductive settings demonstrate the effectiveness of GraphRouter.

### Strengths
*S1* This paper is well-motivated and addresses an important problem. The rapid evolution of LLMs necessitates effective LLM selection, yet existing methods often over-simplify this task as failing to consider the contextual information between tasks, queries, and LLMs, and they struggle to accommodate newly emerged LLMs. The graph-based LLM selection method not only offers a new and effective approach to the LLM selection task but also contributes a novel application in LLM + GNN research. 

*S2* The proposed method, GraphRouter, is both reasonable and intuitive. Extensive experiments demonstrate its effectiveness across different settings.

*S3* The paper is easy to follow, with illustrative figures that facilitate comprehension.

### Weaknesses
*W1* The evaluation setting is simplified. On one hand, the experimental tasks primarily focus on reasoning and question answering, overlooking specialized areas such as code generation and complex multi-hop question answering, which are critical for evaluating the generalizability of LLM selection methods. On the other hand, the available LLMs are quite limited, with nearly half originating from the same series (i.e., LLaMA), which does not fully represent the diverse landscape of available LLMs with varying architectures and capabilities. This narrow selection of LLMs might lead to biased results that do not generalize well to other LLMs.

*W2* Current methodology overlooks the inherent relationships among LLMs. For instance, some LLMs belong to the same series (e.g., LLaMA3-7B, LLaMA3-8B), and their performance characteristics might be correlated. Adding links to indicate such parent or sibling connections could provide a more comprehensive graph modeling, allowing the model to leverage shared knowledge and improve selection accuracy. Additionally, common prior knowledge could enhance the LLM descriptions: e.g., CodeLLaMA series are effective for code-related tasks, while BaiChuan performs better in Chinese contexts. Such prior knowledge could be incorporated as node features or through more sophisticated graph structures.

*W3* (Minor Points) Figures 2-4 require further explanation. In Figure 2, what does the notation $t$ represent? For Figures 3 and 4, does "effect" refer to performance, and why do some LLMs have multiple dots? Additionally, there appears to be an unfinished sentence in Line 138.

### Questions
1. Can GraphRouter be extended to a training-free version? For example, could a training-free GNN, e.g., SGC or LightGCN, be adapted to perform the link prediction task? I am curious about the capability of a training-free GNN for the LLM-selection task, as well as the percentage of training samples required to achieve satisfactory performance. 

2. Can the empirical evaluation be conducted in a more complex scenario, such as by adding more LLMs or introducing a broader variety of tasks?

3. (A Minor Point) LLM selection task is also dependent on specific querying times. For example, in June 2024, the system may recommend GPT-4o for solving a graph reasoning task, while GPT-o1 might become the best choice at a later date. Can such temporal information be incorporated into the methodology or evaluation? 

I understand that time is limited during the rebuttal phase, therefore, brief discussions would be greatly appreciated.

### Soundness
3

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
3

### Summary
This paper tackles the problem of generalizable LLM selection, which requires making performance-cost trade-offs in LLM selection for a given query while being capable of making inductive selections for new LLMs and tasks unseen during training. To address this challenging scenario, inspired by previous studies in graph machine learning and recommender systems, it proposes GraphRouter, a graph-based approach for context aware inductive LLM selection. Technically, it constructs a heterogeneous graph comprising task, query, and LLM nodes, with interactions represented as edges. Evaluating candidate LLMs and making a selection with respect to a given query can then be modeled as an edge-level prediction problem and the authors train a heterogeneous graph neural network for this purpose. Empirical studies demonstrate the effectiveness of GraphRouter for transductive and inductive settings.

### Strengths
**S1.** Compared to the baselines, the proposed graph-based approach conceptually allows better effectiveness and generalizability in LLM selection due to the incorporation of context information.

**S2.** Empirical studies demonstrate the effectiveness of the proposed approach for both transductive and inductive settings.

**S3.** Overall, the paper is easy to follow and the story is appealing and convincing.

### Weaknesses
 **W1.** The initial LLM node feature is based on text embedding, which is likely not the best strategy to model numerical information like token pricing and context length when there is a need to capture the subtlety in numerical differences. Specifically, directly embedding text descriptions of LLMs may not effectively capture the nuanced relationships between numerical attributes such as token costs or maximum context windows. For instance, a small difference in token price (e.g., $0.0001 vs $0.0002 per token) might be crucial for cost-sensitive applications, but this subtle difference could be lost when using text embeddings alone. Similarly, the context window size, a critical factor for handling long documents, is a numerical value that requires careful consideration. 

**W2.** From L245-246, the paper assumes a universally optimal LLM selection for each query, which may not be the case in practice with constraints like inference cost and latency. This assumption overlooks the fact that the optimal LLM choice can vary significantly based on user-specific constraints and preferences. For example, a user might prioritize low latency over high accuracy, or might have a strict budget for API costs. These constraints are not universally applicable and should be considered as part of the selection process. The paper should acknowledge that a single 'optimal' LLM selection is unlikely to satisfy all real-world scenarios and discuss how the proposed approach can be adapted to accommodate diverse user needs.

**W3.** The discussion of related works can be further improved for proper credit attribution. For example:

- The authors cite "Xie et al., 2022" for label propagation while the credit at least should also be properly attributed to the original work "Zhu & Ghahramani, 2002" [1].

- R-GCN is likely the first heterogeneous GNN to the best of my knowledge. It should also be cited in discussing heterogeneous graph neural networks [2].

- The authors employ an attention-based heterogeneous GNN and should also discuss the first few attention-based heterogeneous GNNs, such as [3].

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
3
