# Towards Precise Prediction Uncertainty in GNNs: Refining GNNs with Topology-grouping Strategy

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The calibration of model predictions has recently gained increasing attention in the domain of graph neural networks (GNNs), with a particular emphasis on the underconfidence exhibited by these networks. Among the critical factors identified to be associated with GNN calibration, the concept of neighborhood prediction similarity has been recognized as a pivotal component. Building upon this insight, modern GNN calibration techniques adapt GNNs by smoothing the confidence of individual nodes with those of adjacent nodes. However, these approaches often engage in superficial learning across varying affinity levels, thereby failing to effectively accommodate diverse local topologies. Through an in-depth analysis, we unveil that calibrated logits from preceding research significantly contradict their foundational assumption of nearby affinity, necessitating a re-evaluation of the existing GNN-founded calibration strategies. To address this, we introduce Simi-Mailbox, which categorizes nodes based on both neighborhood representational similarity and their own confidence, irrespective of proximity or connectivity. Our method effectively mitigates miscalibration for nodes exhibiting analogous similarity levels by adjusting their predictions with group-specific temperatures. This encourages a more sophisticated calibration, where each group-wise temperature is tailored to address affiliated nodes with similar topology. Extensive experiments demonstrate the effectiveness of Simi-Mailbox across diverse datasets on different GNN architectures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper points out the problems with GNN calibration and proposes a new calibration method to improve them. This method focuses on the correlation between the similarity of neighboring nodes and calibration performance, and uses this information to make corrections. Experiments on multiple baselines with multiple data sets show that the proposed method has good performance.

### Strengths
- Experimentally finding heuristically that conventional GNN calibration methods have biased performance from node to node and the conditions under which they do so.
- Based on the characteristics found, a method to solve those problems is proposed.
- Experiments have shown that the proposed method is effective for multiple data sets and baselines

### Weaknesses
 - The problems with conventional methods are heuristic. I don't deny that in itself, and the experimental results suggest that the finding is correct. However, it would be better to have an algorithmic point of view, even if not proven. Specifically, a more detailed analysis of why existing methods fail in the context of varying node similarity would be beneficial. For instance, it's not clear why methods that adjust temperature based on neighborhood information do not inherently account for similarity differences. A deeper dive into the mathematical formulations of existing methods, highlighting their limitations with respect to node similarity, would strengthen the paper.
- Some parts are not reader friendly, for example, Fig.1 and Fig.3 look like similar tables but show different information.

### Questions
The results are likely to change depending on the setting of the number of clusters in K-means, the scaling of $\hat{p}_i$,$\bar{M}^{simi}(i)$ and the setting of $\lambda$ in equation (10). What is the impact of these different settings? If the sensitivity is high and they are not easy to set up, it is not sufficient to say that the proposed method is as effective as claimed. Because of this concern, I withhold my rating.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the miscalibration issue in graph learning. Different from general deep models, GNNs are often underconfident about their predictions. Previous GNN calibration techniques adapt node-wise temperature scaling by smoothing the confidence of individual nodes with those of adjacent nodes. However, the authors find that calibrated logits from preceding research significantly contradict their foundational assumption of nearby affinity. As a remedy, they introduce SIMI-MAILBOX, which categorizes nodes based on
both neighborhood representational similarity and their own confidence. The extensive experiments verify the effectiveness of their proposed method.

### Strengths
[+] The manuscript is well-presented. The authors clearly present the motivations, the methods and the experiments.  
[+] The paper is motivated by valid empricial study.       
[+] Extensive experiments are performed to verify the effectiveness of the proposed method.

### Weaknesses
[-] The pioneering work (CaGCN) [1] in this field (GNN calibration) verify the the Accuracy-Preserving property through theoretical analysis and empirical study. Does the method proposed in this manuscript possess such property? It is an important property for calibration methods. More theoretical justifications and experimental results are expected.            
[-] The contribution of the proposed method is somewhat limited. Specifically, the authors utilize KMeans clustering to classify nodes based on analogous neighborhood prediction similarity and their own confidence. And then, analogous nodes within each cluster is rectified via group-specific temperatures. This is incremental compared to previous temperature-tunning methods [1,2].             
[-] Many graph calibration methods are built on the concept of neighborhood prediction similarity. Hence, they can achieve superior performance in homophilous graphs. So, can the proposed method work in heterophilous graphs?                          
[-] The codes for reproducing the results are not provided.                   
[-] Minor issue: The scarlar (probability) value $p$ in Eq. (1) is bolded while it ($\textbf{p}$) often denotes a vector.

### Questions
1. Does the method proposed in this manuscript possess the Accuracy-Preserving property?             
2. Can the proposed method work in heterophilous graphs?          
3. Will the code for reproducing the results be released?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses the issue of graph neural networks (GNNs) calibration by introducing SIMI-MAILBOX, a novel method that categorizes nodes based on neighborhood similarity and confidence levels, effectively mitigating miscalibration across diverse local topologies. The study highlights limitations in current GNN calibration techniques, particularly in relation to neighborhood prediction affinity, and offers valuable insights into improving the reliability of GNN predictions through group-specific temperature adjustments. Experimental validation demonstrates the effectiveness of the proposed approach.

### Strengths
1. The paper is well-structured, easy to understand, and presents a straightforward, implementable method.

2. The motivation behind the paper is compelling, and it provides experimental evidence to support the existence of the discussed phenomenon, along with proposing a viable solution.

3. The paper extensively validates the effectiveness of the proposed method through a large number of experiments and visualizations, demonstrating significant improvements compared to baseline approaches.

### Weaknesses
1. The paper lacks essential citations to highly relevant works, which significantly diminishes its actual contributions. For instance, [1] introduces a calibration loss based on grouping, and [2] presents the concept of multicalibration, akin to grouping. While these papers do not directly address graphs, they offer universal methods applicable to graphs, and this paper should reference these works, highlighting the similarities and differences between them.

2. The most closely related research is [3], which was first published on June 8, 2023, on Arxiv. In [3], a similar approach of grouping samples and applying temperature scaling to each group is proposed. [3] also raises concerns about potential miscalibration post-grouping. Moreover, [3] defines a general grouping function, and it's worth noting that the grouping in this paper, obtained through k-means clustering, is a specific (human-defined) grouping function. [3] offers a learning-based method in this regard.

3. Based on these two points, the primary contribution of this paper appears to be the discovery of an effective grouping function in the context of GNNs, accompanied by some experimental analysis. While this discovery holds practical significance, its novelty may not be sufficient for acceptance by ICLR.

### Questions
Please address the weaknesses identified in the review.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
