# WATERMARKING GRAPH NEURAL NETWORKS VIA EXPLANATIONS FOR OWNERSHIP PROTECTION

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Graph Neural Networks (GNNs) are the mainstream method to learn pervasive graph data and are widely deployed in industry, making their intellectual property valuable. However, protecting GNNs from unauthorized use remains a challenge. Watermarking, which embeds ownership information into a model, is a potential solution. However, existing watermarking methods have two key limitations: First, almost all of them focus on non-graph data, with watermarking GNNs for complex graph data largely unexplored. Second, the de facto backdoor-based watermarking methods pollute training data and induce ownership ambiguity through intentional misclassification. Our explanation-based watermarking inherits the strengths of backdoor-based methods (e.g., robust to watermark removal attacks), but avoids data pollution and eliminates intentional misclassification. In particular, our method learns to embed the watermark in GNN explanations such that this unique watermark is statistically distinct from other potential solutions, and ownership claims must show statistical significance to be verified.  We theoretically prove that, even with full knowledge of our method, locating the watermark is an NP-hard problem.  Empirically, our method manifests robustness to removal attacks like fine-tuning and pruning.  By addressing these challenges, our approach marks a significant advancement in protecting GNN intellectual property.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
In this paper, the authors propose to watermarking GNNs via the explanations of GNNs. Their theory indicates that locating the watermark is an NP-hard problem and the experiments demonstrate that the proposed attack is robust to current defenses.

### Strengths
1 This motivation of the paper is clear.

2 The experiments are quite solid.

3 The soundness of the proposed method is good.

### Weaknesses
1 Although the authors claim that the proposed method can avoid data pollution and eliminates intentional misclassification. However, compared to the traditional methods, it requires a more tight threat model: the training process of target models. It is not always accessible to all scenarios.

2 In Figure 2, the results indicate that fine-tuning fails to remove the effectiveness of the embedded watermark. However, as far as I know, the effectiveness of the fine-tuning attack is closely related to the detailed setting of the learning rate, A larger learning rate might attack the proposed method.

3 In this paper, the authors only narrows the attack in the node classfication. It is only a sub-task in the graph community. I am not sure whether the attack is general enough to be applied to another task, such as edge classification.

### Questions
1 As far as I know, GNNs is only one type of models for node classification, how about more powerful models such as graph transformers?

2 In Table 1, the authors only show the accuracy after inserting watermark. How about accuracy with performing watermarking? Those data is needed to demonstrate the stealthiness of the attack.

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
This paper proposes a graph explanation-based watermarking method. The watermarks are set as specific explanations and are trained into the protected model by backdoor techniques. During verification, explanations of watermarked data will be compared with the ground-truth explanations to determine the ownership. In empirical evaluations, authors demonstrate the performance of the proposed watermarking method from different views, e.g., effectiveness, uniqueness, robustness, and undetectability.

### Strengths
It is novel to utilize explanation as 'poisoned labels' of watermarked data, which will not negatively influence the performance of GNNs.

### Weaknesses
The major concern is how verifiers could get the explanations via black-box access to the protected model during the black-box verification. If I read carefully enough, the explanation of GraphLIME can only be obtained under white-box settings with node embeddings or other model parameters. How is the query efficient if they can be obtained via black-box access? I welcome discussion from authors and will consider raising the score if the answer is appropriate.

### Questions
Please refer to weaknesses.

### Soundness
3

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
3

### Summary
This paper aims to inject watermarks to graph neural networks, in order to serve as a verification strategy to protect the ownership of the graph neural network. In order to achieve the goal, the authors investigate a new methodology of graph model explanation.

### Strengths
1. The paper studies a novel problem for GNN ownership verification. 
2. The proposed method is interesting and the empirical results demonstrate the effectiveness. 
3. The authors conduct serious robustness evaluation of the proposed methodology.

### Weaknesses
 **Concerns Regarding the Presentation**
From Section 3, the paper uses too many math notations and equations, but didn't provide sufficient explanation and clarification. This make the paper not very easy to follow. For example, the GNN explanation part in Section 3.2, it is hard to see how someone can use it to explain the GNN prediction. Moreover, the switch from Lasso to Ridge Regression will make the give weights to all features. I am not sure how to find important features based on the Ridge Regression output. 

**Concerns Regarding the Threat Model**
The threat model discussed in this paper appears to lack sufficient justification. Specifically:
1. It is unclear why or under what circumstances “the adversary does not know the location of the watermarked subgraphs, but knows the shape and number of the subgraphs.” In practice, if the adversary is not the model trainer, they may have limited knowledge about the watermark.
2. The authors also mention that the model ownership verifier cannot access the protected model. It’s not immediately clear why the verifier would be unable to access the model parameters. Try to imagine, if an artist who owns a painting work sues another party for copyright infringement, it would be unusual for the artist to prevent the judges from examining their original artworks.

### Questions
Plz see the weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a graph neural network watermarking method that embeds ownership information into the explanations of predictions. During the training process, the node classification loss maintains the model's classification accuracy, while the watermark embedding loss ensures that the feature explanations of the watermarked subgraphs align with the watermark pattern. After training, the model owner can claim its ownership by the similarity between the explanations and the watermark pattern. The author proves that it is an NP-hard problem for attackers to find the watermarked subgraphs. The method mitigates the impact of intentional misclassification compared to traditional backdoor-based watermarking techniques. Experiments on three datasets in node classification task illustrate the effectiveness of ownership verification and its robustness to pruning and fine-tuning.

### Strengths
The paper first introduces node feature explanations into GNN watermarking and demonstrates the potential of model explanations for applications in the GNN watermarking domain. By embedding the watermark within GNN prediction explanations rather than in the training data, the method mitigates risks associated with data pollution and misclassification.

### Weaknesses
1. Several prior methods have been proposed in the area of GNN watermarking, such as [1] and [2]. It is important to consider experiments that compare the watermark accuracy and downstream task performance of these methods. Specifically, a comparison should be made on metrics such as the false positive rate of watermark detection, the impact of the watermark on classification accuracy, and the robustness of the watermark to removal attempts. The current paper lacks a clear benchmark against existing techniques, making it difficult to assess the relative performance and advantages of the proposed method.

2. The paper highlights the robustness of the method against pruning and fine-tuning. Given that adversaries may attempt model extraction attacks, as described in [3], it is advisable to address the robustness against such extraction attacks. The paper should consider scenarios where an adversary attempts to extract the model's parameters or functionality through techniques like knowledge distillation or model inversion. Evaluating the resilience of the watermark against these attacks is crucial for practical application, as an easily extracted model would render the watermarking scheme ineffective.

### Questions
1. How does the model perform without watermarking? It would be helpful to compare the classification accuracy on downstream tasks before and after embedding the watermark.
2. The explanation method GraphLIME is applied only to the node classification task in the paper. Can this watermarking method be extended to other downstream tasks in graph-based applications?

### Soundness
2

### Presentation
3

### Contribution
2
