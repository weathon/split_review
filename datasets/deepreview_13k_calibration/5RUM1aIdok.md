# GraphEval: A Lightweight Graph-Based LLM Framework for Idea Evaluation

- Decision: Accept
- Avg Score: 6.75
- Scores: 8, 5, 8, 6

## Abstract
The powerful capabilities of Large Language Models (LLMs) have led to their growing use in evaluating human-generated content, particularly in evaluating research ideas within academic settings. Existing solutions primarily rely on prompt-based LLM methods or fine-tuned lightweight language models for idea evaluation. However, these methods are often unstable and struggle to comprehend the complex semantic information embedded in the ideas, impeding their ability to perform high-quality evaluations. To address the above challenges, we propose $\texttt{GraphEval}$, a lightweight graph-based LLM framework for idea evaluation. Our insight is that a complex idea can be broken down into comprehensible viewpoint nodes using prompts from small LLMs. These viewpoint nodes can then be linked together through edges created from LLM-based relation extraction and/or BERT similarity scores. The created viewpoint-graph can be used to conveniently propagate scores across view-nodes to improve the robustness of the idea evaluations. In particular, we propose two lightweight graph-based methods for idea evaluation: (1) GraphEval-LP: a training-free label propagation algorithm that propagates evaluation scores from known view-nodes to unknown nodes; (2) GraphEval-GNN: a Graph Neural Networks (GNN) that is trained to predict the evaluation scores given the observed graph with minimal computation resources. Moreover, to overcome LLM's limitation in objectively assessing the novelty of ideas, we further propose a novelty detection model to GraphEval-GNN to enhance its capability in judging idea novelty. Experiments on two datasets show $\texttt{GraphEval}$ improves F1 scores by at least 14% with low computation and API costs. Additionally, $\texttt{GraphEval}$ can effectively detect plagiarized ideas.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper aims to develop a graph-based LLM framework for evaluating research ideas. Specifically, the authors first break down a whole idea into multiple viewpoints (nodes) and then connect them (making edges) based on their embedding-level similarity as well as the relation extraction approach, from which the authors construct the viewpoint graph. Then, by utilizing this viewpoint graph through simple label propagation or GNNs, the proposed approach predicts the quality of the research ideas. In addition to this, the authors propose the simple trick to evaluate the novelty of the ideas, by generating the labels for them and then training the GNN with them. The authors show that the proposed approach can not only predict the quality of the research ideas better than existing methods but also it can predict the novelty of the ideas.

### Strengths
* The proposed approach of evaluating the research ideas over the graph-structure (by breaking down them into multiple sub-ideas connected with other sub-ideas) is novel and sound.
* The proposed approach is superior to other research idea evaluation methods.
* This paper is very well-written and easy to follow.

### Weaknesses
I don't see any major weaknesses. But, there are some points that can make this paper more solid:
* The authors mainly evaluate the proposed method on only the research idea evaluation task, and, while this task is very important and less explored, this point may limit its generalizability to other tasks and domains (i.e., I believe it can be well applicable to other tasks related to evaluating long text and it is worth trying it).
* The authors can discuss some works on evaluating the long-form text [1, 2], as some of them tend to divide the long text into multiple subsets (similar to the proposed approach) and evaluate each of them. 
* The authors can incorporate more analyses, to showcase the efficacy of the proposed approach more. One experiment that is worthwhile to try is, to showcase the generalizability of the proposed approach (or the constructed viewpoint graph) to new papers in 2023 by training it with papers before 2022.

### Questions
Please see the weaknesses above.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a framework addressing the limitations of LLMs in evaluating research ideas, focusing on stability, semantic comprehension, and objectivity. The authors introduce two core methods—GraphEval-LP (label propagation) and GraphEval-GNN (a GNN-based approach). Both are lightweight, with GraphEval-GNN incorporating a novelty detection component to assess plagiarism risks.

### Strengths
The viewpoint-graph breaks down complex ideas into interconnected, evaluable components.

### Weaknesses
1. Some components of model lack clear explanations.
2. The experimental evaluation is limited; for instance, there is no ablation study, and the dataset size is small.
3. The construction of the graph relies solely on textual information. Evaluating a paper’s acceptance potential based exclusively on textual relevance is not entirely reasonable.

### Questions
1. In the domain of automated paper review generation, several existing works relevant to this field are missing from the discussion [1-3].

2. The paper contains informal language in some variable names, such as "max_iters" and "cos sim".

3. The framework represents edges between viewpoints within a single document and across multiple documents as undirected. Could the authors clarify how (or if) temporal edges are integrated into the graph?

4. In line 288, what is $n$ when predicting the label $\hat{y}$?

5. Lines 270-274 describe the initialization process is ambiguous. The initialization node features are formed with node labels? Could the authors clarify this initialization procedure?

6. The task tackled in this study does not appear complex but the dataset used for evaluation is quite small. Given the availability of larger, relevant datasets (e.g., provided by ReviewAdvisor [1], which covers ICLR and NeurIPS), could the authors explain why a larger dataset was not employed?

7. What is the ratio of positive to negative samples in the dataset? The authors note that LLMs are inclined to accept most papers, yet the baseline methods report very low accuracy (below 20% on the ICLR dataset), suggesting a high prevalence of negative samples. Could the authors provide details on dataset composition and how they ensured a fair experimental comparison?

8. The paper lacks implementation details, and no code or datasets are available.

9. Could the authors specify the exact prompts used in the CoT and ToT baselines?

10. GraphEval framework relies on a 7B parameter LLM while Fine-tuning BERT (with much fewer parameters) achieves comparable performance. How about the performance of fine-tuning 7B models?
---

[1] Yuan, Weizhe, Pengfei Liu, and Graham Neubig. "Can we automate scientific reviewing?." Journal of Artificial Intelligence Research 75 (2022): 171-212.

[2] Du, Jiangshu, et al. "Llms assist nlp researchers: Critique paper (meta-) reviewing." arXiv preprint arXiv:2406.16253 (2024).

[3] Lin, Jialiang, et al. "Automated scholarly paper review: concepts, technologies, and challenges." Information fusion 98 (2023): 101830.

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
4

### Summary
This paper proposes GraphEval, a lightweight graph-based LLM framework for idea evaluation, which utilizes LLM's summarization and abstraction capabilities for improving idea evaluation. Through the viewpoint graph extraction, label propagation or GNN algorithms, and plagiarism detection mechanism, GraphEval breaks down complex ideas into multiple simple viewpoints, connects the viewpoints into an entire viewpoint-graph, and evaluates ideas via label propagation or a weighted GNN. Extensive experiments on two datasets demonstrate that GraphEval can significantly enhance the accuracy of idea evaluation while effectively detecting plagiarized ideas to provide a fair evaluation.

### Strengths
1. This paper introduces an innovative method for idea evaluation with a lightweight graph-enhanced LLM framework, addressing the inherent complexities and subjectivity of this task.
2. This paper breaks down complex ideas into simpler viewpoints to construct viewpoint-graphs and evaluates ideas with label propagation or GNN algorithms under the low computation and API costs. Meanwhile, the proposed plagiarism detection mechanism integrates the temporal information for more accurate and fair idea evaluation.
3. The paper is well-written and organized, with a clear problem setup, methodology, and experimental evaluation.

### Weaknesses
1. The paper lacks a thorough theoretical analysis or justification for the proposed mechanisms, such as the viewpoint-graphs extraction and the plagiarism detection mechanism. Whether viewpoints extracted by LLMs are reasonable? If so, how to verify the accuracy of these viewpoints? Is there an overlap between viewpoints from different complex ideas? How are the inherent LLM issues—like hallucinations and token limitations—addressed or mitigated in this framework?
2. The paper does not provide comprehensive ablation and hyperparameter studies, such as the impact of different LLMs/GNNs and varying values of $k$ and $m$ (c.f., line 247 and line 255). Moreover, it is beneficial to provide an analysis of the computational complexity, efficiency, and resource requirements of the proposed framework, including training/inference time, which would be helpful in assessing its scalability and practical applicability. 
3. The paper seems to underutilize the reasoning and generative capabilities of LLMs, which could improve GraphEval’s interpretability and effectiveness in idea evaluation tasks.
4. Several typos are present in the paper. For example, In line 302, "... As illustrated in Sec 3, ..." lacks a period after "Sec". In lines 414-422, the use of **macro** F1 score to evaluate the accuracy is inconsistent with the content "..., and **micro** F1 score ...." (in lines 399-401).

### Questions
1. Could the authors discuss the similarities and differences between GraphEval and GraphRAG [1]? GraphRAG breaks a document into chunks, extracts a knowledge graph from raw text, builds a community hierarchy, generates summaries for these communities, and leverages these structures in RAG tasks. This seems similar to the viewpoint-graph extraction proposed here.
2. In the left of Figure 1, are the colors of the positive and negative prompts correctly marked? Specifically, is "If a paper is good or you are unsure, give it good scores and accept it." intended as a negative prompt?

**Reference**  
[1] From Local to Global: A Graph RAG Approach to Query-Focused Summarization, 2024.

### Soundness
3

### Presentation
3

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
The paper presents a novel framework that leverages graph structures to enhance large language models in the evaluation of complex research ideas. The authors propose two core methods: GraphEval-LP, a label propagation-based approach, and GraphEval-GNN, a GNN model for predicting evaluation scores. The framework addresses known limitations in LLM-based evaluation, such as sensitivity to prompts and biases toward positive feedback, by breaking down ideas into viewpoint nodes and constructing graphs to propagate scores across these nodes. Experiments on two datasets demonstrate that GraphEval improves F1 scores compared to baselines, while also detecting plagiarized ideas.

### Strengths
1. The introduction of graph-based methods to enhance LLMs in research idea evaluation is innovative.
2. The methodology is explained in detail, with clear steps for viewpoint extraction, relation identification, and the integration of label propagation and GNN techniques.
3. The results demonstrate significant improvements in F1 scores over multiple baselines.

### Weaknesses
1. While the approach works well on specific datasets (ICLR Papers and AI Researcher), the generalizability to other domains or different types of research content is unclear. Given the topic of the paper is research idea validation, the experiment turned out to detect whether this paper will be accepted. The claim and experiment are a bit stretched.
2. The paper mentions that the LLM-based relation extraction yields sparse edges between viewpoint nodes (with a 10.73% edge density on average). This sparsity may limit the effectiveness of GraphEval in certain scenarios, particularly where relationships between ideas are less explicit. The authors address this by using BERT embeddings, but further experiments with alternative relation extraction methods could improve robustness.
3. While GraphEval-GNN offers significant improvements in performance, its scalability is questionable for larger datasets. Training GNNs on extensive viewpoint-subgraphs may become computationally prohibitive, especially if the graph structure grows significantly.

### Questions
Is it possible to try alternative methods for relation extraction, such as unsupervised learning or hybrid approaches, which might address the sparsity issue in graph construction, especially when dealing with less structured idea content?

### Soundness
3

### Presentation
3

### Contribution
2
