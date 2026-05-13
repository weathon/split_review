# GraphBridge: Towards Arbitrary Transfer Learning in GNNs

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Graph neural networks (GNNs) are conventionally trained on a per-domain, per-task basis. It creates a significant barrier in transferring the acquired knowledge to different, heterogeneous data setups. This paper introduces **GraphBridge**, a novel framework to enable knowledge transfer across disparate tasks and domains in GNNs, circumventing the need for modifications to task configurations or graph structures. Specifically, GraphBridge allows for the augmentation of any pre-trained GNN with prediction heads and a bridging network that connects the input to the output layer. This architecture not only preserves the intrinsic knowledge of the original model but also supports outputs of arbitrary dimensions. To mitigate the negative transfer problem, GraphBridg merges the source model with a concurrently trained model, thereby reducing the source bias when applied to the target domain. Our method is thoroughly evaluated across diverse transfer learning scenarios, including Graph2Graph, Node2Node, Graph2Node, and graph2point-cloud. Empirical validation, conducted over 16 datasets representative of these scenarios, confirms the framework's capacity for task- and domain-agnostic transfer learning within graph-like data, marking a significant advancement in the field of GNNs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, a novel GraphBridge framework is proposed. This framework introduces a resource-efficient approach for enabling versatile graph transfer learning across diverse tasks and domains, designed to fully leverage pre-trained Graph Neural Networks (GNNs) without necessitating data restructuring or task redefinition. It outlines four transfer learning scenarios of varying complexity and employs two novel tuning techniques, GSST and GMST, to navigate specific challenges in each. Experimental results across multiple domains, covering tasks like graph and node classification as well as 3D object recognition, validate GraphBridge's effectiveness in achieving domain-agnostic transfer learning with greater resource efficiency. Future work will expand the framework's applicability by addressing more extensive benchmarks.

### Strengths
GraphBridge offers a versatile framework for efficient graph transfer learning, enabling pre-trained GNNs to tackle diverse tasks and domains without extensive reorganization. It achieves resource efficiency through two novel tuning methods, GSST and GMST. The framework supports both cross-level and cross-domain tasks, allowing scalable application across simple to complex scenarios. Extensive experiments demonstrate its adaptability and robustness.

### Weaknesses
Although the paper represents a good novel contribution, there are some issues, which are as follows:

1. The framework relies on high-quality pre-trained GNNs, which may not always be available or easy to obtain. This dependence introduces a potential bottleneck, as the performance of GraphBridge is intrinsically tied to the quality of the pre-trained model. The paper does not adequately explore the implications of using pre-trained models of varying quality or how the framework might perform with less robust pre-trained GNNs. Furthermore, the computational cost and data requirements for obtaining such high-quality pre-trained models are not discussed, which could limit the practical applicability of the framework.

2. Some domain-specific nuances might still require additional adaptation, potentially limiting GraphBridge’s effectiveness in highly specialized applications. The paper acknowledges this limitation but does not provide a thorough analysis of how the framework handles diverse data characteristics or how much manual intervention is required for different domains. For instance, the feature space and graph structure can vary significantly across domains, and the framework's ability to adapt to these variations needs further investigation. The paper should include a more detailed discussion on the limitations of the proposed approach in handling highly heterogeneous data.

3. Baselines are very less and not that recent may be due to the scope of the work. The lack of a comprehensive comparison with state-of-the-art methods makes it challenging to assess the true performance and advantages of GraphBridge. The paper should include a wider range of baselines, including more recent and competitive methods, to provide a more robust evaluation of the proposed framework.

### Questions
The work covers nearly all aspects which should be taken care for the study. However, there are following question which may arise:
1. Hypergraphs are also a way which considers information with their context for downstream tasks. Can the framework be adapted for hypergraphs as well or can it be comapred with hypergraphs?
2. How can it be compared statistically with the given baselines?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes GraphBridge, a framework for knowledge transfer across different tasks and domains in Graph Neural Networks (GNNs). The main contributions include 1) An end-to-end pre-training-tuning framework, 2) Two parameter-efficient transfer methods (GSST and GMST) based on side-tuning, 3) A "Task Pyramid" defining different difficulty levels and validation on 16 datasets.

### Strengths
- The paper addresses the challenging issue of cross-task and cross-domain transfer in GNNs.
- The design of using side-tuning to mitigate negative transfer is rational. 
- The experiments are conducted across multiple scenarios and datasets to evaluate the performance.

### Weaknesses
 - The technical novelty seems limited. The overall framework is a straightforward application of traditional pre-train finetune paradigm but lacks graph-specific innovative designs. The use of a simple MLP as a side network, without exploring more sophisticated architectures tailored for graph data, is a missed opportunity. For instance, the paper does not consider attention mechanisms that could potentially better capture the relationships between the pre-trained GNN and the side network, which is a common practice in other transfer learning domains.
- The paper directly uses MLP as a side network without comparing it to other networks, such as co-attention used by multimodal large language models in bridging two different modalities. This is a significant oversight, as the choice of side network architecture can greatly impact the effectiveness of knowledge transfer. The lack of ablation studies on different side network architectures makes it difficult to assess the true potential of the proposed approach.
- The improvements seem quite limited in some datasets, e.g., some results in Table 1. Can the authors elaborate more on the possible reasons? The paper does not adequately address the cases where the proposed method underperforms, particularly in the Easy Scenario. It is crucial to understand why the method struggles on certain datasets, as this could reveal limitations in the approach or areas for improvement. The lack of analysis on the impact of label imbalance, for example, is a significant gap.
- The analysis of computational efficiency and memory consumption is not sufficient. It would be better to conduct a comparison from a theoretical or experimental perspective for further discussion. The paper lacks a rigorous analysis of the computational overhead introduced by the side-tuning approach. A comparison of the time and memory complexity of the proposed method with full fine-tuning, both theoretically and empirically, is necessary to fully evaluate its practical utility.
- In Loss, alpha is learnable, but there seems to be no mechanism to limit the range of alpha. Will this cause alpha of gnn to be 0 and the mlp part to dominate? The lack of constraints on the learnable alpha parameter is a concern, as it could lead to instability during training or cause the model to rely solely on the side network, effectively ignoring the pre-trained GNN.
- What are the criteria for choosing between GSST and GMST? The paper does not provide clear guidelines on when to use GSST versus GMST. The selection criteria should be more explicit, based on the characteristics of the source and target tasks and domains.

### Questions
See weaknesses.

### Soundness
3

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
3

### Summary
In this paper, a framework is introduced, which aims to realize the arbitrary transfer learning of graph neural network (GNN) between different tasks and fields.Demonstration that GraphBridge achieves high efficiency with significantly fewer parameters (5%-20% of typical models) while maintaining comparable performance.

GraphBridge incorporates Graph Side-tuning techniques—Graph-Scaff-Side-Tune (GSST) and Graph-Merge-Side-Tune (GMST)—to minimize negative transfer effects, which occur when knowledge transfer from one domain adversely impacts performance in another. GSST focuses on efficiently transferring knowledge using a side network for layer-wise fusion with the base model. GMST, designed for domains with larger gaps, merges a pretrained model with a randomly initialized model, effectively reducing bias from the source domain.

At the same time, the author created a "task pyramid" with four levels of difficulty and tested it on 16 data sets.

### Strengths
Originality:GraphBridge introduces a novel approach to arbitrary transfer learning within Graph Neural Networks (GNNs), allowing models to be reused across a variety of tasks and domains without modifying task-specific configurations or graph structures. This approach is particularly original in that it combines prediction heads and a bridging network in a way that facilitates diverse task adaptation while preserving pretrained model knowledge.

Quality:The paper presenting a comprehensive evaluation of GraphBridge across 16 datasets and multiple transfer scenarios, ranging from relatively straightforward graph-to-graph tasks to more complex cross-domain transfers. 

Clarity:The paper is generally clear in its exposition of both the problem and the proposed solution and the diagram of the paper is very clear and beautiful, which is pleasing to the eye.

Significance:GraphBridge is significant because it offers a flexible, task-agnostic framework for GNN transfer learning—a major advance in the field. The framework has broad implications for practical applications across various domains where graph data is prevalent, from molecular property prediction to social networks.

### Weaknesses
While the paper introduces two side-tuning techniques (GSST and GMST) to address negative transfer, it would be beneficial to delve deeper into when and why each approach is likely to succeed or fail. For instance, providing clearer conditions under which GSST vs. GMST is preferable would help practitioners select the appropriate method for specific tasks. Additionally, it might be useful to add a comparison with other common techniques for mitigating negative transfer, such as domain adaptation approaches, as this would position the side-tuning techniques more clearly within the broader context of transfer learning.

### Questions
1.How to prove the wide applicability of the task pyramid?
2.Can you provide more specific guidance on when to use GSST versus GMST?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this scholarly article, the researchers introduce a novel framework termed GraphBridge, which is designed to facilitate resource-efficient graph transfer learning for arbitrary downstream tasks and domains. The overarching objective is to establish a unified workflow that maximizes the utility of pre-trained Graph Neural Networks (GNNs) across a spectrum of cross-level and cross-domain downstream tasks, thereby eliminating the necessity for data reorganization and task reformulation. To achieve this, the authors have constructed four distinct scenarios of graph transfer learning tasks, spanning from simple to complex, and proposed two resource-efficient tuning methods, namely Graph-Scaffold Side-Tune (GSST) and Graph-Merge Side-Tune (GMST), to address the associated challenges. The experimental validation, conducted across diverse domains and tasks, including graph and node classification as well as 3D object recognition, demonstrates the effectiveness of their approach in enabling arbitrary domain transfer learning on GNNs with enhanced resource efficiency.

### Strengths
1. The paper introduces the GraphBridge framework, an innovative solution aimed at enabling arbitrary transfer learning of Graph Neural Networks (GNNs) across different tasks and domains, an area that has not been fully explored in previous research. GraphBridge, through the introduction of prediction heads and a bridging network, allows pre-trained GNNs to effectively transfer learning between inputs and outputs of different dimensions, a novel design approach.
2. The paper has conducted extensive experimental validation on multiple datasets, covering a range of transfer learning scenarios from simple to complex, demonstrating the rigor and reliability of the research methodology. 
3. The paper is structured clearly, with a tight logic, detailing the problem statement, methodology, experimental design, and result analysis, making it easy for readers to understand and follow. 
4. The paper addresses an important issue in the practical application of GNNs, that is, how to effectively transfer and reuse knowledge trained on one type of data to another different type of data, which is of great significance for promoting the widespread application of GNNs.

### Weaknesses
 1. In the research of graph neural networks, the interpretability of models is an important aspect. The paper may need to further explore how to explain the decision-making process of GraphBridge. 
2. The paper may need to provide more visualizations of the experimental results, such as confusion matrices, to help readers more intuitively understand the model's performance.


### Questions
In the realm of graph neural networks research, the interpretability of models is a crucial consideration. The paper might need to delve deeper into elucidating the decision-making mechanisms of GraphBridge. Furthermore, to aid readers in gaining a more intuitive grasp of the model's performance, the paper could benefit from incorporating additional visual representations of the experimental outcomes, such as confusion matrices. In the HARD TASK challenge, as shown in Table 3, the model's performance on the Amazon and Flickr datasets does not match the effectiveness seen with FT. Please provide an explanation considering aspects such as the structure of the datasets.

### Soundness
3

### Presentation
3

### Contribution
3
