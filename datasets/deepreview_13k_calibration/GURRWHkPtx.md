# Language Models are Graph Learners

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Language Models (LMs) are increasingly challenging the dominance of domain-specific models, including Graph Neural Networks (GNNs) and Graph Transformers (GTs), in graph learning tasks. Following this trend, we propose a novel approach that empowers off-the-shelf LMs to achieve performance comparable to state-of-the-art GNNs on node classification tasks, without requiring any architectural modification. By preserving the LM's original architecture, our approach retains a key benefit of LM instruction tuning: the ability to jointly train on diverse datasets, fostering greater flexibility and efficiency. To achieve this, we introduce two key augmentation strategies: (1) Enriching LMs' input using topological and semantic retrieval methods, which provide richer contextual information, and (2) guiding the LMs' classification process through a lightweight GNN classifier that effectively prunes class candidates. Our experiments on real-world datasets show that backbone Flan-T5 models equipped with these augmentation strategies outperform state-of-the-art text-output node classifiers and are comparable to top-performing vector-output node classifiers. By bridging the gap between specialized task-specific node classifiers and general LMs, this work paves the way for more versatile and widely applicable graph learning models. We will open-source the code upon publication.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel framework for leveraging language models (LMs) in graph learning tasks. The key contributions include: (1) a dual-similarity node retrieval mechanism that integrates both topological and semantic features to identify relevant nodes, and (2) an innovative label space pruning technique that incorporates inductive biases derived from pre-trained graph neural networks (GNNs). The proposed approach demonstrates competitive performance across four diverse node classification benchmarks, suggesting its effectiveness as a general-purpose solution for graph-based learning tasks.

### Strengths
1. The paper presents an innovative approach to encoding graph structural information into a text format that is directly consumable by language models; This bridge between graph and textual domains enables leveraging the powerful capabilities of pre-trained LMs for graph-based tasks without requiring architectural modifications.



2. The proposed dual-similarity node retrieval system effectively captures both structural and semantic relationships; By considering both topology and semantics, the method provides richer contextual information to the LM compared to purely structure-based or content-based approaches


3. The integration of GNN-derived inductive biases through label space pruning represents a theoretically well-grounded approach; This technique effectively reduces the complexity of the classification task while preserving model performance.

### Weaknesses
1. The choice of Personalized PageRank (PPR) for topological similarity computation needs stronger justification. Modern GNNs with link prediction objectives could potentially provide more sophisticated structural representations. A comparative analysis between PPR and alternative approaches (e.g., GNN-based methods) would strengthen the methodological choices. 


2. The title ``Language Models are Graph Learners'' suggests a broader scope than the actual focus on node classification. The method's generalizability claims would be more convincing with evaluation on: a). Link prediction tasks; b). Graph question-answering (GraphQA) scenarios. A discussion of potential adaptations needed for other graph learning tasks would be valuable. 


3. The experimental evaluation lacks comprehensive comparisons with recent LLM-based graph learning methods[1-5]. A thorough comparison with these baselines would better contextualize the method's contributions and advantages.

### Questions
1. The performance metrics for GraphSAGE are absent from Table 2. There is a discrepancy between the methodology description and experimental results regarding GraphSAGE (line 420)

2. The paper claims to "retain the versatility of the original LM" (line 160) while requiring LM parameter tuning (line 372). How does the training process affect the LM's general capabilities? Is there evidence of catastrophic forgetting on the original LM tasks? Can the model generalize across different node classification domains (e.g., Arxiv to Products) without multi-task learning?


3. The experimental section would benefit from detailed efficiency metrics beside section 4.5. The metrics include FLOPs comparison with baseline methods, particularly InstructGLM, Memory usage analysis across different dataset scales, Convergence time comparisons, End-to-end runtime analysis including retrieval and inference phases. 

4. Have the authors considered using GNNs with link-prediction objectives as an alternative to PPR?


5. For prototypical semantic retrieval, how is the performance of only relying on the semantic information (e.g. sentence representation based on SimCSE)?

### Soundness
2

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
The paper presents a novel approach named AUGGLM that leverages off-the-shelf Language Models for node classification tasks on Text-Attributed Graphs (TAGs) without requiring any architectural modifications. The key contributions include: (1) Relevant Node Retrieval which utilizes topological and semantic retrieval methods to enrich the input of LMs with contextual information from relevant nodes. (2) Candidate Label Pruning which employs a lightweight GNN to prune class candidates, guiding the LMs' classification process. The approach maintains the original architecture of LMs, preserving their flexibility and efficiency in multi-task learning and personalized fine-tuning. The experiments on real-world datasets demonstrate that AUGGLM-equipped LMs outperform state-of-the-art text-output node classifiers and are comparable to top-performing vector-output node classifiers.

### Strengths
The approach creatively repurposes LMs for graph learning tasks, bridging the gap between specialized node classifiers and general LMs. This makes it more convenient for real-world applications as it does not require modifications to the LLM architecture. By maintaining the original architecture of LMs, the method preserves their versatility and compatibility with multi-task learning and personalized fine-tuning services.
The proposed topological and semantic retrieval methods effectively enhance the contextual information available to LMs, improving their performance on node classification tasks.
The paper provides thorough experimental validation on multiple datasets, showing consistent performance improvements.

### Weaknesses
Combining Figures 2 and 3 into a single figure would make it easier to understand the differences between the proposed approach and the InstructGLM method. This would provide a clearer picture of the main distinctions. Additionally, including an overall pipeline figure would help bridge the relationships among the various subsections mentioned in the methodology, offering a more cohesive understanding of the entire process.
The methods section is dense with rich content, making it challenging to follow. After reading the entire methods section, it is not easy to draw a complete picture of how the authors achieve their goal. A more streamlined presentation or a summary of key steps could improve clarity and comprehension.
The effectiveness of the retrieval-based augmentation heavily relies on the quality of the retrieved nodes. If the retrieval process fails to identify truly relevant nodes, the performance could degrade. Specifically, the paper does not provide a clear analysis of how the topological and semantic retrieval methods are evaluated for relevance, and how the quality of retrieved nodes impacts the final classification performance. Without a clear metric or evaluation of the retrieved nodes, it is difficult to assess the robustness of the proposed method.
Due to the extensive details in the methods section, the authors have allocated limited space to present the experimental results and analyses. More discussions and deeper analyses of the experimental results would provide better insights into the performance and limitations of the proposed approach. For example, a detailed ablation study on the impact of different numbers of retrieved nodes or different weighting schemes for combining topological and semantic retrieval would be beneficial.

### Questions
How does the retrieval quality (both topological and semantic) impact the overall performance? Are there any metrics or evaluations to ensure the relevance of the retrieved nodes?
Can the authors provide a detailed analysis of the computational cost associated with the retrieval and candidate pruning steps? How does this compare to traditional GNN-based methods?
Have the authors tested the method on other types of graph datasets beyond TAGs?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an approach that enables off-the-shelf Language Models (LMs) to perform node classification tasks on Text-Attributed Graphs (TAGs) with a performance comparable to state-of-the-art Graph Neural Networks (GNNs).  Authors propose two strategies for enriching LM inputs and the proposed method empowers LMs to handle graph data without altering their original architecture, thus maintaining the LMs' versatility for multi-task learning and other applications. Also, authors propose to use a GNN-based classifier to guide the training of LMs, which enhances the efficiency of model prediction.

### Strengths
* Motivation for making the model capable of processing graph data without changing the model architecture is interesting and proposes a reasonable approach
* Paper is well structured, with a clear introduction,  methodology, and experiments, making it easy for the reader to follow the author's thoughts.
* An experimental evaluation of real-world data sets proves the effectiveness of the proposed method. The use of multiple datasets increases the reliability of the results.

### Weaknesses
 * Incorporation of structural information through the addition of related nodes appears to be a well-established concept, I doubt the source of the performance improvement is, see the question section.
* The scalability of the model is limited, increasing the number of input nodes will inevitably increase the length of input text, which may be intractable in some situations, and the paper lacks discussions for this.
* Model performance is limited by the GNN model. For example, if the GNN model cannot give accurate candidate labels, then the LM model cannot give correct predictions.
* Experiments are thin and lack detailed additional experiments and analysis, such as hyperparameters. The choice of GNN model and the number of retrieved nodes are critical parameters that need further investigation to understand the method's robustness and limitations. The performance of the simple semantic retrieval is also surprisingly strong, and the paper does not adequately address why the proposed method has advantages over a simpler approach using a strong embedding model like SimTeG.

### Questions
* As mentioned in weakness, the proposed method is similar to few-shot methods, can you provide comparison between your method and some simple baselines, such as retrieval neighbor nodes or high text-similarity nodes to enhance the input?
* Whether it can provide the performance of the model related to key hyperparameters, such as the number of nodes retrieved or different GNN models, is critical to understanding the key components of the method and the scalability.
* Most LM-based methods are inductive. Is the proposed method inductive? Have you tried zero-shot experiments? For example, training on one dataset. and test on other datasets.
* Why wasn't the experiment conducted on decoder-only LLMs such as 7b model, which would have enhanced the integrity and significance of the paper.  Although it doesn't change my rating on the paper.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new methodology called 'AUGGLM (Augmented Graph Language Model)'. This approach enhances node classification performance without modifying existing language models (e.g., Flan-T5). The primary idea is to enrich the input to the language model using topological and semantic search methods, enabling better graph data processing. Additionally, a lightweight Graph Neural Network (GNN) is used to prune candidate labels, improving classification performance. Through these augmentation techniques, the model demonstrates performance that either surpasses or matches existing text-based node classifiers, with the goal of developing a model applicable to various tasks.

### Strengths
1. AUGGLM can process graph data without modifying the existing language model architecture, making it easily applicable to various tasks.
2. AUGGLM performs on par with traditional Graph Neural Networks (GNNs), and in certain datasets, it achieves even better results.

### Weaknesses
1. Although various engineering techniques were applied to contribute to performance improvement, they are merely a combination of existing, publicly available techniques, with no original or novel methods included.
2. It is unclear how the method presented in Section 4.2 differs from widely known ensemble techniques. It seems to be a simple ensemble of GNN and language models (LM), and the unique contributions of the authors are not clearly explained.
3. There is a lack of clear motivation for each module—Topological Retrieval, Prototypical Semantic Retrieval, and Classifier Guidance—and an insufficient explanation of the theoretical background for using these three modules together. It gives the impression of a system that compiles widely known techniques.

### Questions
1. The overall process is quite complex. Have diagrams been prepared for each module—Topological Retrieval, Prototypical Semantic Retrieval, and Classifier Guidance?
2. While the motivation for each module is indirectly addressed, the clear rationale for using all three modules together has not been fully explained. Could you provide additional explanation regarding the theoretical background for proposing these three modules together?
3. Classifier Guidance appears to be a simple ensemble technique rather than an attempt to effectively utilize the language model (LM). Furthermore, without the ensemble technique, it would be difficult to claim superior performance over InstructGLM. Is it merely a simple ensemble method? If not, could you explain in detail the novel aspects uniquely proposed by the authors?

### Soundness
3

### Presentation
2

### Contribution
2
