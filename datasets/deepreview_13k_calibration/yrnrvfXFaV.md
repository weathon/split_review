# Low-cost Enhancer for Text Attributed Graph Learning via Graph Alignment

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 6, 3, 3

## Abstract
Many graphs can be represented as Text-attributed Graphs (TAGs). Due to the rich textual information present in each node of TAGs, traditional graph neural networks (GNNs) often struggle to deliver satisfactory performance. Recent advancements leveraging large language models (LLMs) to augment new node text features have notably enhanced node representations, resulting in significant performance improvements. However, these methods typically require extensive annotations or fine-tuning on all nodes, which are both time-consuming and expensive. To address this challenge, we propose GAGA, a novel and lightweight framework for TAG representation learning. GAGA employs a more efficient strategy by annotating only representative nodes and edges, thereby reducing both annotation time and cost. It further capitalizes on these annotations by constructing an annotation graph that captures the topological relationships among them. Additionally, GAGA introduces a two-level alignment module to integrate the annotation graph with the TAG, ensuring effective alignment of their underlying structures. Experiments demonstrate that GAGA achieves classification accuracies comparable to or exceeding state-of-the-art methods while requiring only 1\% of the data to be annotated, making it highly efficient.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Summary

This paper studies how to leverage the textual information for improved performance for node classification and link prediction. It inherits the idea from existing works that utilize LLMs as data enhancers by prompting the LLMs for explainations and broader knowledge, with a special focus on reducing the costs of both training and inference time. The experimental results demonstrated the effectivenss of the proposed method.

### Strengths
Pros:

1. The combination of LLMs and TAGs are important topics for graph research which establishes new benchmarks and poses new challenges.

2. I like the idea of prompting LLMs for broader knowledge and the rationale behind the observed graph, e.g., edge formation.

2. The experiments were comprehensive and covered most important baselines for the two tasks evaluated.

### Weaknesses
The presentation needs to be improved. Several critical designs of the framework lacks motivation. Please see the Questions part for details.




### Questions
Questions:

1. The authors need to provide a detailed motivation&discussion on the use of vector quantization (VQ) in the framework. Based on the manuscript,  I feel like a lot of things are missing regarding this part. For example, how to learn the prototype matrix $Z_a$ during training? 


2. During inference on downstream tasks, the final node representations are generated as a weighted sum of the prototype matrix learnt from the alignment stage. Could the authors explain the rationale behind this design? I understand that the authors provide a subsection 'Effect Visualization of Annotation Prototype.', yet I'm still quite confused. 


3. Does the alignment stage need to be performed for any given graph, or can it be pretrained on some datasets and directly apply to unseen graphs?

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
3

### Summary
The paper introduces GAGA, a framework for enhancing Text-Attributed Graphs by incorporating annotations efficiently. GAGA addresses this by annotating only a small set of representative nodes and edges based on information density, which significantly reduces time and cost compared with the traditional method. A two-level alignment module then integrates these annotations into the TAG structure, facilitating high-quality graph representation learning. Experiments demonstrate that GAGA achieves comparable or superior classification accuracies with little data annotated, proving its efficiency.

### Strengths
1. **Efficiency and Scalability**: Reducing both time and cost associated with LLM-based enhancements for TAG, making it scalable for large datasets.The experiment on the correlation between the amount of labeled data and performance in the ablation paper is also very interesting.

2. **Two-Level Alignment Module**: The innovative two-level alignment module, which integrates annotations with TAG structure, allows GAGA to achieve strong generalization with limited annotations.

3. **Experimental Validation**: Comprehensive experiments across six datasets validate GAGA’s efficiency and accuracy.

### Weaknesses
See Questions.

### Questions
1. How does the performance of GAGA vary with different values of the hyper-parameter 𝛼 in the loss function? Are there any guidelines for tuning it?

2. How does GAGA choose which nodes (edges) to be annotated. Is there any consideration about it?

3. While large language models (LLMs) are crucial to the proposed method, the experiments are solely conducted on GPT-3.5. I am curious about the method's compatibility with other open-source LLMs, such as Llama 3.2 or Qwen 2.5. Could you clarify which specific characteristics of LLMs are most impactful for GAGA? Additionally, how might one select an appropriate or potentially more advanced LLM to further enhance GAGA's performance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a lightweight framework for representation learning on text-attributed graphs. The proposed model only annotate representative nodes and edges, and introduces a two-level alignment module for structure alignment.

### Strengths
Experiments on both node classification and link prediction taks show the effectiveness of the proposed methods.

The research topic is promising in graph representation learning.

### Weaknesses
The novelty of this paper is incremental. Specifically, regarding low-cost annotation, the approach of annotating only representative nodes via LLMs is not new. Previous work [1] has already applied this method for TAG representation learning. For model explanations, the idea of considering the annotation given by LLMs as an explanation (line 169) is similarly well-explored in [2].

The writing and presentation need refinement. For instance, the Introduction is overly lengthy and should be shortened. Figure 2 is difficult to interpret.

The usage and description of mathematical symbols are chaotic; for example, see line 340.

It is unclear how Figure 3 demonstrates the effect of annotation prototype projection.

### Questions
For the two-level contrastive learning, does it introduce additional training of the language models?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the challenges faced by traditional graph neural networks (GNNs) when working with Text-attributed Graphs (TAGs), which contain rich textual information. While recent methods leveraging large language models (LLMs) have improved node representations, they often necessitate extensive annotations and fine-tuning, which can be costly and time-consuming. This paper propose a lightweight framework for TAG representation learning model which innovatively annotates only representative nodes and edges, significantly reducing annotation time and costs.

### Strengths
The method explores a new aspect by examining the issues related to large language models from both the perspectives of time expenditure and cost.

### Weaknesses
1. The motivation for the model is not strong enough. The article points out that an important limitation of other methods is the requirement to enhance the attributes of all nodes. This assumption is not necessarily reasonable; enhancing all nodes is not mandatory, and enhancing only a subset of nodes is also a viable option. While the impact of this approach on model performance does require further experimentation, I do not believe it constitutes a limitation of the other methods.
2. The code is not publicly available.
3. From the experimental results (Table 2), the improvement of this method is quite limited and not very significant.
4. The core contribution claimed by this article is the selection of representative nodes for labeling, aimed at reducing time and cost while maintaining effectiveness. Therefore, I focused on this aspect. However, I regret to say that the methods employed in the article do not convince me. The first assumption in the paper equates information density with node density, positing that areas with denser nodes have higher information density, suggesting that representative nodes should originate from such areas. In my view, nodes in low-density areas can also result in significant information loss, and defining high and low density is highly dependent on later parameter tuning. Secondly, the article employs k-means to obtain central nodes as a metric for selecting representative nodes. The algorithmic complexity of k-means is very high, and I do not believe this method can be particularly efficient, especially when dealing with large datasets. Overall, while the motivation behind this idea is appealing, the specific implementation fails to satisfy me.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
1
