# Explainable Graph Representation Learning via Graph Pattern Analysis

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Explainable artificial intelligence (XAI) is an important area in the AI community, and interpretability is crucial for building robust and trustworthy AI models. While previous work has explored model-level and instance-level explainable graph learning, there has been limited investigation into explainable graph representation learning.
In this paper, we focus on representation-level explainable graph learning and ask a fundamental question: What specific information about a graph is captured in graph representations? Our approach is inspired by graph kernels, which evaluate graph similarities by counting substructures within specific graph patterns. Although the pattern counting vector can serve as an explainable representation, it has limitations such as ignoring node features and being high-dimensional.
To address these limitations, we introduce a framework for learning and explaining graph representations through graph pattern analysis. We start by sampling graph substructures of various patterns. Then, we learn the representations of these patterns and combine them using a weighted sum, where the weights indicate the importance of each graph pattern's contribution.
We also provide theoretical analyses of our methods, including robustness and generalization. In our experiments, we show how to learn and explain graph representations for real-world data using pattern analysis. Additionally, we compare our method against multiple baselines in both supervised and unsupervised learning tasks to demonstrate its effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a graph representation learning method leveraging graph pattern analysis. It presents a representation learning approach applicable to both supervised and unsupervised learning, utilizing various graph kernels to provide interpretable pattern information for post hoc analysis, effectively demonstrating its utility in experiments.

### Strengths
- The notation is clearly defined, contributing to a well-articulated description of the proposed approach.
- The use of visualizations enhances the accessibility of pattern-based explanations.
- The paper effectively conveys the need to provide explanations based on graph patterns.

### Weaknesses
 - The time complexity would be significantly higher than the time complexity analysis. However, it is difficult to say it is incorrect because details about kernel usage, such as the number of graphlets employed, and preprocessing requirements are missing. In particular, efficiently identifying graphlets with more than four nodes is a challenging task.
- While the theoretical analysis is included, it lacks the intuition and analysis for understanding the proposed work.
 - The introduction mentions post-hoc interpretability methods, but the connection to the proposed approach is unclear, as they appear to address entirely different tasks.
 - As the paper addresses explanations at the representation level, comparisons with methods like UNR-Explainer [1] and MotifExplainer [2] would strengthen the related work or introduction section.
 - The paper employs graph sampling, yet details and sensitivity analysis are omitted.
 - GNNs typically struggle with modeling paths, trees, and graphlets due to limited expressive power. It remains unclear if this aspect is effectively visualized and well-learned in the training analysis.

### Questions
Please refer to the weaknesses above.

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
This paper proposes explainable AI (XAI) in the graph domain from the perspective of graph representations. Existing XAI methods in the graph domain mainly focus on model-level or instance-level explanations and lack exploration of representation-level explanations. This paper introduces two methods: 1) PXGL-EGK and 2) PXGL-GNN, which combine representations of graph patterns within the input graph. These methods provide explanations through weight parameters that combine pattern representations to construct the overall graph representation. The authors propose both supervised and unsupervised versions for each method. PXGL-GNN addresses several limitations of PXGL-EGK, such as ignoring node features, high dimensionality, time complexity, and limited expressiveness. The paper includes theoretical analysis on robustness, generality, and complexity, with experimental results and t-SNE visualizations demonstrating the superiority of the proposed methods over existing approaches.

### Strengths
1. The paper is well-written and easy to follow.

2. It explores representation-level explanations within the graph domain, an area that is not well-explored.

3. The explanation is intuitive and effectively highlights dominant graph patterns using weight parameters.

### Weaknesses
1. The theoretical analysis suggests that the robustness of the method depends on the number of layers \( L \). A performance comparison across different values of \( L \) would be beneficial, as setting \( L = 5 \) appears to be heuristic.

2. Since the representation of the input graph is directly influenced by the types of patterns used, the authors should demonstrate how different combinations of patterns affect the representation.

3. A hyperparameter analysis regarding the number of samples \( Q \) is necessary.

### Questions
1. Regarding datasets that contain node attributes, as the authors argue that PXGL-GNN can address the issue of ignoring node features present in PXGL-EGK, it would be beneficial to directly compare the two methods on a dataset with node attributes.

2. In the MUTAG dataset, each graph's label is determined by the presence of key tree-like substructures, such as \( NO_2 \) or \( NH_4 \). In other words, ring patterns do not influence the prediction of the input data. However, PXGL-GNN tends to capture dominant patterns within the input data, often assigning larger weights to cyclic structures. Given this tendency, how can PXGL-GNN outperform other baselines that focus on the critical substructures (i.e., \( NO_2 \) or \( NH_4 \)) needed to predict the label of the input graph?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
PXGL-GNN is an explainable graph representation learning method based on the analysis of graph patterns such as paths, trees, graphlets, cycles, cliques, wheels, and stars. It explicitly defines the important graph patterns of interest for analysis and learns the importance of each pattern with regard to supervised or unsupervised learning tasks.

### Strengths
The proposed method is novel in employing graph pattern analysis to introduce an explainable graph representation learning model. It reveals the importance of pre-selected graph patterns and their impact on the learned representation vector. Furthermore, this method is applicable in both supervised and unsupervised settings. While maintaining explainability, the model's accuracy in predictive tasks is comparably superior to other black-box models. Additionally, the authors provide a theoretical analysis of the proposed method in terms of robustness, generality, and complexity.

### Weaknesses
W1. The Introduction's storyline is confusing. The authors primarily discuss post-hoc explainers, including GNN-Explainer and XGNN, in the second paragraph and set the research goal as "What specific information about a graph is captured in graph representation learning?" On first reading, this easily misleads readers into thinking the proposed method is similar to post-hoc explanations. However, this is not the case of PXGL-GNN which is a graph representation learning that incorporates explainability. The introduction should more clearly distinguish between post-hoc explanation methods and the proposed approach, which aims to learn interpretable representations directly.

W2. The authors claim the explainability of their GNN, but no evaluation of the explanations is conducted. While the method identifies the importance of pre-selected graph patterns, there is no quantitative assessment of how well these patterns explain the learned representations. It is unclear how the learned pattern importance scores relate to the actual predictive power or the underlying graph properties. The absence of metrics to quantify explanation quality is a significant weakness.

W3. The explanation method for graph representation learning is more valuable to discuss in the context of PXGL-GNN. However, the discussion of post-hoc graph explanations for supervised learning models is sufficient (in my opinion, it's excessive). Additionally, the authors omit the recent UNR-Explainer method, which explains node representation learning, in the related works section. The related work section should be more focused on methods that learn interpretable representations, rather than just post-hoc explanation techniques. The omission of UNR-Explainer is a significant oversight, given its relevance to the topic of explaining learned representations.

W4. Although PXGL-GNN is an explainable graph learning model, it lacks explicit explanations. While it provides the importance of pre-selected graph patterns, mapping these to specific subgraphs in the input graph is challenging. Users can understand the overall pattern for the output but struggle to map the insight into the real dataset. This becomes problematic when a certain graph pattern (e.g., a cycle) is important, but slight differences in its components lead to significant changes in prediction. Thus, providing only the graph pattern is insufficient to explain the prediction. The method needs to provide a way to identify *where* these important patterns occur in the input graph, not just their overall importance.

Minor: In Tables 3 and 5, the second-best results for the COLLAB dataset and REDDIT-B are not highlighted.

### Questions
Please refer to the weaknesses W1, W2, W3, and W4, as well as the minor issue mentioned.

Q1. What are the advantages of analyzing graph patterns for graph representation learning?

Q2. How does understanding important patterns in graph representation learning tasks benefit real-world scenarios?

Q3. Is it feasible to extend the proposed method to node representation learning?

Q4. Have you considered extracting explicit explanations, given that the model already possesses knowledge of important graph patterns in the input graph?


----------

 I appreciate the authors' dedicated efforts in addressing the reviewers’ concerns. As the review process has concluded, I will now present my feedback more directly for clarity.

Explaining representation $g$ is not exclusive to approaches of the model-level and instance-level explanations, for example, TAGE explains the representation vectors in view of the instance-level. Though authors point out the unique novelty compared to post-hoc explainers, in fact,  PXGL-GNN is an interpretable representation learning model or a self-explainable model that learns and explains the inherent important pattern in an integrated way. Since I appreciate the author's effort and novel work, I recommend improving the clarity of the introduction. I hope authors have a changed to consider my concerns.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel method for explainable graph representation learning based on graph pattern analysis. It aims to answer what information about a graph is captured in its representations by analyzing substructures within different graph patterns. The method includes two approaches: a graph ensemble kernel (PXGL-EGK) for explainable similarity learning and a graph neural network (PXGL-GNN) that combines learned representations from various patterns. Theoretical analyses cover aspects like robustness and generalization, and experiments demonstrate the proposed method’s effectiveness in classification and clustering tasks.

### Strengths
Novelty in Explainable Representation: By focusing on pattern-based explainability, the paper addresses a unique gap in graph representation learning, offering insights into the contributions of specific patterns.

Theoretical Rigor: Theoretical analyses on robustness and generalization bounds add depth to the paper, strengthening the credibility of the proposed method.

Experimental Validation: The method outperforms several baselines in both supervised and unsupervised learning tasks, showing its practical effectiveness and explainability in graph-based tasks.

### Weaknesses
1. Language, Formatting, and Text Issues:

There are numerous language and formatting issues throughout the manuscript. For instance, the citation formats at the beginning of Chapters 1 and 4 are incorrect. Some terms that should be consistent, such as "generality" and "generalization," are not used uniformly. Additionally, some equations end with punctuation while others do not, and line 297 redundantly uses "Eq. equation." Furthermore, the equation on line 332 exceeds the page length significantly and would benefit from a line break. While I do not typically have strict formatting requirements, the frequency of these issues greatly impacts readability. I recommend a thorough review of the entire manuscript for consistency and clarity.

2. Structure of Chapters 4 and 5:

I suggest a complete rewrite and restructuring of Chapters 4 and 5. I found Chapters 1 to 3 to be relatively clear and easy to follow, but the latter chapters are quite challenging to understand. I read through them multiple times to grasp the progression between theoretical sections, yet some parts remain obscure. I recommend the following:
1.	Emphasize the relationship between Definition 4.2 and Definition 4.3 and the subsequent sections of the manuscript, explaining why these definitions are highlighted at the beginning.
2.	After each section of theoretical derivation, include a statement summarizing the conclusions that can be drawn from that section.

3. Limited Diversity in Pattern Selection:

The experiments focus on common graph patterns but lack exploration of more complex or specialized patterns, which may affect the method's generality and adaptability to various application domains.  More diverse and application-specific patterns could be explored to enhance the method’s flexibility and relevance cross various domains. Furthermore, future work could expand on computational efficiency, providing empirical results on time and memory usage for large datasets.


4. Scalability Concerns:

Although the method discusses time and space complexity, it lacks empirical results demonstrating efficiency on large-scale graph datasets, which raises questions about its scalability.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
