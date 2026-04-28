# Shapley-Guided Utility Learning for Effective Graph Inference Data Valuation

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 5, 6

## Abstract
Graph Neural Networks (GNNs) have demonstrated remarkable performance in various graph-based machine learning tasks, yet evaluating the importance of neighbors of testing nodes remains largely unexplored due to the challenge of assessing data importance without test labels. To address this gap, we propose Shapley-Guided Utility Learning (SGUL), a novel framework for graph inference data valuation. SGUL innovatively combines transferable data-specific and modelspecific features to approximate test accuracy without relying on ground truth labels. By incorporating Shapley values as a preprocessing step and using feature Shapley values as input, our method enables direct optimization of Shapley value prediction while reducing computational demands. SGUL overcomes key limitations of existing methods, including poor generalization to unseen test-time structures and indirect optimization. Experiments on diverse graph datasets demonstrate that SGUL consistently outperforms existing baselines in both inductive and transductive settings. SGUL offers an effective, efficient, and interpretable approach for quantifying the value of test-time neighbors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper has studied the graph inference data valuation problem by developing a new data-driven utility function and providing theoretical insights to enable direct optimization through the Shapley value decomposition. Extensive experiments on public datasets were provided in terms of multiple evaluation protocols.

### Strengths
- A new definition of the structure-aware Shapley value has been introduced to facilitate graph data valuation. 
- The paper has extensively discussed the limitations of applying Shapley values on graph-structured data from the utility estimation and indirect optimization perspectives, resulting in the proposed SGUL framework. 
- The experiment is well designed to comprehensively access both utility estimation and data valuation, covering different graph structures, downstream tasks, and multiple evaluation protocols.

### Weaknesses
 - While the proposed method seems novel and technically sound to me, it would be better to involve a more detailed comparison and discussion with existing works (e.g., [Chi et al., 2024]) in the main text and experimental analysis. 
- It remains unclear if the proposed SGUL is scalable to large graph benchmarks, such as Open Graph Benchmark (Hu et al., 2020), due to the introduction of an $\ell_1$ penalty in eq (3).
- The methodology is somewhat hard to follow and less self-contained. An illustration framework or outline algorithm would be much helpful.

### Questions
While it is interesting and novel to connect utility learning and Shapley value prediction through a linear projection, the training process of the data-driven utility function and how to obtain feature Shapley values ($\psi_i$) remain unclear to me. 
- How to obtain/initialize $\psi_i$?
- Can `Theorem 1` be applied to general domains other than graph-structured data? 
- Is there any limitation or assumption for `Theorem 1`?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel framework called Shapley-Guided Utility Learning for the graph-structured data valuation problem. The proposed method tackle with two problems associated with graph-structured data valuation: lack of test labels and indirect optimizaiton of utility function.

### Strengths
1. The paper is well written and organized.
2. The method is well motivated and justified.
3. The experimental results shows promising performance.

### Weaknesses
 1. The details of permuation sampling process is not clear. Could authors elaborate on the sampling process?
2. The proposed data-specific features, such as edge cosine similarity, appear to favor graph homophily. When applying this framework to heterophilous graphs, it raises the question of whether these features would still be effective.  How is edge cosine similarity adapted for both homophilous and heterophilous graphs? Additional discussion on this point could be valuable.
3. It seems that the ablation study on the investigation of the seperate contribution of data-specific features and model-specific feature is missisng.

### Questions
see weakness

### Soundness
3

### Presentation
3

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
In this paper, the authors design a shapely-guided unility learning framework for graph inference data valuation, which termed SGUL. SGUL combines transferable data-specific and model-specific features to test data without relying on labels.

### Strengths
1. The author has provided the code to ensure the reproducibility of the paper’s results.

2. The author has supplied partial theoretical proofs to support the claims made in the study.

### Weaknesses
1.  In Figure 1, the author has chosen a comparison method that only includes one paper from 2024. Please incorporate more recent comparative experimental methods.


2. The results of the comparative experiments by the author are perplexing. Why does SGUL consistently perform the worst across all datasets? The author explains that SGUL can identify important nodes in the graph structure. However, could it be that the design methodology is ineffective, leading to the model’s poor performance?


3. In the field of graph neural networks, test-time training methods are widely used to address distribution shift issues in test data[1,2,3,4]. These methods also do not require labels. How does your approach compare to test-time training-based graph methods, and what advantages does it offer?


4. In Theorem 1, why is the variable U suddenly linear when it was previously described in exponential form (as in Equation 1)? The transition lacks a clear explanation, even though the author provides a proof based on the linear function.

5. There are typographical errors, such as consecutive “for instance” phrases in line 206.

6. The advantages in terms of time and space efficiency are not clearly demonstrated and need to be supported by experimental evidence.

### Questions
Please see weakness.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper is well-written. It combines transferable data-specific and modelspecific features to approximate test accuracy without relying on G-T labels.

### Strengths
1. This work introduces a transferable feature extraction method that transforms player-dependent inputs into general features.

2. Authors claim that they are the first to formulate the graph inference data valuation problem.

3. Code is open-source and readable.

### Weaknesses
1. Lack of comparison with other works. GNNEvaluator, DoC, ATC are the compared baseline in your experiment, but readers are not yet clear about the main differences between these baselines and your method. I noticed that there is an introduction in the appendix, but there is a lack of comparison.

2. The method in this work has special optimization in structure(Sec 3.2), but lacks experimental verification of this optimization.

### Questions
1. Is there any experiment to show the importance of  the structure-aware Shapley value?


2. Since you are the first to formulate the graph inference data valuation problem, what's the main different between your work and GNNEvaluator[1]?It seems that both of you are methods for verifying GNN performance without  labels.

3. In your code, Which part of the paper does 'data_without_edges' correspond to? Why remove the graph structure for testing？



[1] GNNEvaluator: Evaluating GNN Performance On Unseen Graphs Without Labels, arxiv 2310.14586

### Soundness
3

### Presentation
3

### Contribution
2
