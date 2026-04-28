# Knowledge Benchmark Graph: Assisting Large Language Models in Designing Models by Retrieving Benchmark Knowledge

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
In recent years, the design and transfer of neural network models have been widely studied due to their exceptional performance and capabilities. However, the complex nature of datasets and the vast architecture space pose significant challenges for both manual and automated algorithms in creating high-performance models. Inspired by researchers who design, train, and document the performance of various models across different datasets, this paper introduces a novel schema that transforms the benchmark data into a Knowledge Benchmark Graph (KBG), which primarily stores the facts in the form of performance(data, model). Constructing the KBG facilitates the structured storage of design knowledge, aiding subsequent model design and transfer. However, it is a non-trivial task to retrieve or design suitable neural networks based on the KBG, as real-world data are often off the records. To tackle this challenge, we propose transferring existing models stored in KBG by establishing correlations between unseen and previously seen datasets. Given that measuring dataset similarity is a complex and open-ended issue, we explore the potential for evaluating the correctness of the similarity function. Then, we further integrate the KBG with Large Language Models (LLMs), assisting LLMs to think and retrieve existing model knowledge in a manner akin to humans when designing or transferring models. We demonstrate our method specifically in the context of Graph Neural Network (GNN) architecture design, constructing a KBG (with 26,206 models, 211,669 performance records, and 2,540,064 facts) and validating the effectiveness of leveraging the KBG to promote GNN architecture design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a graph dataset that helps connect datasets, models, and model performance, making it easier for machine learning systems to automatically find the best model architecture for a specific dataset. Since real-world datasets are often new and unseen, the authors create a method to measure how relevant different datasets are to each other, which helps in sharing knowledge between them. This method allows the system to use information from existing benchmark data, ensuring that high-performing models can still be applied to new datasets. Additionally, the authors present a new metric that focuses on the most useful insights, which makes the model selection process even better. In their experiments, they test this approach on various datasets to show how effective and efficient it is, highlighting its potential to improve model design and performance in real-world situations.

### Strengths
This paper has several notable strengths that enhance its contribution to the field of automated machine learning.

1. The introduction of a comprehensive graph dataset models the relationships between datasets, models, and performance. This structured resource simplifies the model selection process for researchers and practitioners.
2. The theoretical framework is well-articulated and provides a solid basis for the proposed methods. This enhances the credibility of the approach and demonstrates a deep understanding of the principles involved.
3. The experiments conducted are thorough and well-executed, testing the methods across various datasets. These results provide strong empirical support for the authors’ theoretical claims.
4. The research has significant implications for automated machine learning (AutoML), allowing for the automatic identification of optimal model architectures. This capability can reduce the time and expertise required for model design, making machine learning more accessible.

Overall, the paper effectively combines a valuable dataset, strong theoretical foundations, and solid experimental validation, positioning it as a promising contribution to AutoML. Its findings could lead to further advancements in automated processes for model development.

### Weaknesses
The theoretical explanations in the paper could be improved with additional background to aid reader comprehension. 
1. For example, in Definition 1, it would be useful for the authors to provide an overview of existing problem formulations in model transfer or AutoML to better contextualize their approach. 
2. Explaining the motivation for using a probability lower bound in Definition 1 and its relevance to practical model transfer would clarify this choice. 
3. It would also be helpful to indicate whether this problem formulation is novel or based on existing methods, and if it is novel, to discuss the advantages it brings over previous formulations.

In Section 4.3, the intuition behind the transferability score could be further clarified. 
1. A conceptual explanation of what the transferability score represents in practical terms would be beneficial, along with a small example or illustration to demonstrate how it is calculated and interpreted. 
2. Additionally, comparing this score with existing metrics for evaluating model transfer effectiveness could further clarify its utility.

Furthermore, the paper’s discussion on integrating Large Language Models (LLMs) into the proposed framework could be more comprehensive, as it is currently quite brief. 
1. The authors might expand on the specific role of LLMs in their approach, detailing how they interact with the Knowledge Benchmark Graph and contribute to model selection or adaptation. 
2. Examples illustrating the LLMs' role in the process would be helpful, as well as a discussion of any potential challenges in integrating LLMs and how these are addressed. 
3. Lastly, comparing this approach to other recent methods that incorporate LLMs for AutoML or model selection would provide a useful context for the reader.

### Questions
please refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors proposes a new solution for AutoML. The authors design a knowledge graph that contains information on data, model and performance. With the knowledge graph, the method uses similarity score of data and relevance score of model to suggest best model on unseen data. 

In experiments, the authors construct the knowledge graph with graph datasets and GNN architectures. The result show that the method author proposes achieves the best result on 3/8 tasks. However, with the assistance of LLM, the model is able to achieve best result on 5/8 tasks.

### Strengths
The paper writing is clear. The formulation is very straight-forward. The authors use data similarity score and model relevance score to infer the best potential model on unseen data. 
The authors provide extensive experiments comparing to SOTA methods.

### Weaknesses
1. The data similarity score the authors propose is too simple. The authors focus their study on GNN, but the similarity score does not involve any relational information on the edges. Specifically, the method uses a simple L1 or L2 distance on node features, which ignores the graph structure. For example, two graphs with identical node features but different edge connections would be considered identical by the proposed similarity metric, which is a significant limitation when dealing with graph data.
2. The model relevance score is confusing. The name sounds like it look for architectural similarity between models. But in reality it's the model's historical performance. This is misleading because the term 'relevance' typically implies a measure of similarity or compatibility, not just past performance. Furthermore, using historical performance as a proxy for relevance assumes that past performance is a reliable indicator of future performance on unseen data, which may not always hold true, especially if the unseen data has different characteristics.
2. The experiment section that involves LLM is very vague to me. There's is not explanation on exactly how LLM infer or select the models. The description lacks details on the specific prompts used, how the LLM's output is processed, and whether any constraints are applied to the LLM's suggestions. This makes it difficult to reproduce the results and understand the contribution of the LLM component.

### Questions
1. LLM assisted method achieves best performance but there is no detailed explanation or design. For example, you can answer the following questions:
    (a)What prompts or instructions were given to the LLM?
    (b)How were the LLM's outputs processed or integrated into the model selection process?
    (c)Were there any constraints or filtering applied to the LLM's suggestions?
2. It's good to include more complicated design of the two scores. For example, incorporate edge-level information in data similarity score calculation and model architectural information, like the number of convolutional layers, in model relevance calculation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper attempts to construct a graph that stores all the existing datasets, models, and model performance on datasets for future research and development endeavors. Based on the constructed datasets, the authors try to propose some metrics to evaluate the similarity between datasets and the effectiveness of the models retrieved on an unseen dataset. The experimental results show that such a graph is benefical for the development of AutoML.

### Strengths
The idea is interesting and the motivation is convincing. 
The implementation of this idea is relatively complete, including the graph construction process, the design of enhancing generalization ability on incorporating unseen datasets, and the retrieval mechanism of existing model candidates.

### Weaknesses
The work is full of engingeering skills while lack some academic insights. For example, controling and varying the hyperparameters (e.g., delta, the size of datasets, epsilon, etc.) bring limited insight. Perhaps a case study is required to illustrate how the algorithm succeeds to retrieve a good model according to a given unseen-yet-similar dataset. There should be more deeper insights and factors beyond the similarity of datasets, such as the underlying common research issues. What features should the algorithm capture and consider? 
The scenario is relatively limited. Authors conduct experiments merely in GNN domain. It’s unclear whether such an effort could generlize to other ML methods, which makes the contribution of this paper vague. I suggest conducting a small amount of experimental evidence to demonstrate the generalization ability of this work, which could make it more promising and convincing.

### Questions
Please refer to the weakness.

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
- This paper proposes a novel AutoML framework with LLM for GNN design. In this paper, the authors construct a knowledge benchmark graph to inform the LLM with more domain knowledge about GNN architecture and design new metrics to guide the knowledge selection.

### Strengths
- The idea of this paper of paper is more innovative, combining Knowledge Grap, LLM and AutoML.
- The authors have done sufficient data preparation, method design and experiments around this idea.

### Weaknesses
 - There are some labeling errors in Table2, e.g., the optimal result on the Citeseer dataset appears on the GAT but is not bold.
- The experiments in the current article stop at the GNN domain and are only oriented to the node classification task, which has some limitations in the scope of application. And the title gives the impression that the authors' approach is oriented to a variety of tasks in generalized scenarios. I think KBG can be considered to be applied on top of more heterogeneous tasks, such as other tasks in the field of graph learning, or even out-of-domain experiments such as CV/NLP that require the GNN method to verify the effectiveness of the method. Further, the design of the model can also be not limited to the GNN model.

### Questions
- Which LLM do you employ in the experiments? I can not get the corresponding information after reading Section 5.1
- The naming of knowledge benchmark graph might be modified. I think the current name misleads people into thinking this is a new KG benchmark.
- See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3
