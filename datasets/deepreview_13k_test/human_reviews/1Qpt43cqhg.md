# Fully-inductive Node Classification on Arbitrary Graphs

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
One fundamental challenge in graph machine learning is generalizing to new graphs. Many existing methods following the inductive setup can generalize to test graphs with new structures, but assuming the feature and label spaces remain the same as the training ones. 
This paper introduces the fully-inductive setup, where models should perform inference on arbitrary test graphs with new structures, feature and label spaces. We propose GraphAny as the first attempt to this challenging setup. GraphAny models inference on a new graph as an analytical solution to a LinearGNN, which can be naturally applied to graphs with any feature and label spaces. To further build a stronger model with learning capacity, we fuse multiple LinearGNN predictions with a learned inductive attention. Specifically, the attention module is carefully parameterized as a function of the entropy-normalized distance features between pairs of LinearGNN predictions to ensure generalization to new graphs. Empirically, GraphAny trained on a single Wisconsin dataset with only 120 labeled nodes can generalize to 30 new graphs with an average accuracy of 67.26%, surpassing not only all inductive baselines, but also strong transductive methods trained separately on each of the 30 test graphs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the problem of fully inductive node classification, where limited parameters are learned from one small graph, and inference other unseen graphs.  The authors propose GraphAny, which consists of two components, one is a set of linearGNNs, and the other is a learnable attention MLP function. Using pseudo-inverse, LinearGNNs directly compute the node embeddings of corresponding linearGNN channels. Then a sophisticated attention technique which has properties of permutation-invariant and robust dimension generalization is used to combine these embeddings. The extensive experiments show that GraphAny gains significant improvements over the state-of-the-art methods in many datasets.

### Strengths
1. This paper proposes a novel problem setting seemingly impractical, and provides a reasonable solution to it. Previously, I was doubtful about the feasibility of graph foundation models, since unlike in NLP and CV, graph data is more universal and diverse. The information heterogeneity between different graphs may make this fully inductive setting impossible, i.e., I didn't think the knowledge in different graphs has much in common. However, the authors provide an impressive and valid solution to this problem, which is a good contribution to the community.

2. The proposed method is well-motivated and well-designed. The attention module that tackles dimensionality and permutation issues is particularly novel and interesting, with strong intuition. 

3. The experiments are extensive and convincing. An impressive number (31) of datasets are involved in this fully-inductive setting, and the good average score of GraphAny demonstrates its effectiveness.

4. The ablation study is comprehensive and insightful. The authors provide a clear understanding of the importance of each component in GraphAny.

### Weaknesses
1. (Explainability) I didn't see any explanation of one very important question: why could the knowledge learned from one graph be transferred to another unseen and unrelated graph? The authors should provide more intuitive insights on this point. From my point of view, LinearGNNs with different graph operations may serve as probes to extract different types of intrinsic knowledge from the graph, then the permutation and dimension invariant attention module could combine this knowledge in a semantic space where the common knowledge of graphs is shared. The authors should provide more insights on this point, i.e., why it works well.

2. (Experiments) Although the proposed AnyGraph shows a high average performance, it is not the best in all datasets, especially in some large datasets such as Arxiv, Reddit and Products. I don't think homophily could explain this, since AnyGraph (Arxiv) also performs poorly. The authors could provide more insights on why AnyGraph fails in these datasets, and how to possibly improve it.

3. (Experiments) The transductive baselines (GCN, GAT) are not strong enough. Since the benchmark contains so many datasets ranging from highly homophily to highly heterophily, baselines [1,2,3] that could fit both homophilous and heterophilous graphs should be compared. I highly recommend the authors to add some of these baselines to make the results more convincing.


[1] Luan, S., Hua, C., Lu, Q., Zhu, J., Zhao, M., Zhang, S., ... & Precup, D. (2022). Revisiting heterophily for graph neural networks. Advances in neural information processing systems, 35, 1362-1375.

[2] Lim, D., Hohne, F., Li, X., Huang, S. L., Gupta, V., Bhalerao, O., & Lim, S. N. (2021). Large scale learning on non-homophilous graphs: New benchmarks and strong simple methods. Advances in Neural Information Processing Systems, 34, 20887-20902.

[3] Zhu, J., Rossi, R. A., Rao, A., Mai, T., Lipka, N., Ahmed, N. K., & Koutra, D. (2021, May). Graph neural networks with heterophily. In Proceedings of the AAAI conference on artificial intelligence (Vol. 35, No. 12, pp. 11168-11176).

### Questions
Most of the questions and suggestions are already mentioned in the weaknesses section. I would like to mention some minor points here.

1. I would like to see more graph operations used in LinearGNN instead of just X, AX, A^2X, (I-A)X, (I-A)^2X. For example, the Chebyshev polynomial operation, the PageRank operation, normalized Laplacian operation, etc. I think more operations could provide more diverse perspectives of the graph, and thus improve the performance of GraphAny at a little extra cost.

2. I doubt the time complexity in Table 1, since pseudo-inverse is used in LinearGNN, which is computationally expensive up to O(n^2d), could the authors explain this?

### Soundness
3

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
This paper tackles the issue of fully inductive graph learning by introducing GraphAny. The proposed method consists of LinearGNN to preprocess the features following the idea of SGC and attention module to transform the feature.

### Strengths
1. This paper tackles a great challenging fully-inductive graph learning task.
2. This paper introduces an inductive attention module that satisfies permutation invariance properties and generalizes to new graphs.

### Weaknesses
1. The presentation of this paper needs improvement. Many details are missing in the section of methodology. 
- The authors conduct the experimental on motivating the entropy normalization, while the experimental setup in figure 5 is not explicit. It's not suggested to specify what these methods are until the section 4.1. The authors should provide more explicit explanation of the experimental setup for Figure 5.
- It's not clear what is the learnable parameters in the attention module and how to get the attention vector $\alpha$. A clear description of the learnable parameters in the attention module should be added.
- It's weird to call $y_u^{(i)}$ in equations 9 and 10 as node feature and it's more proper to describe it as label vector considering its dimensionality. 

2. In figure 3, the authors mention that LinearGNN is non-parametric, but LinearGNN involves the learnable weight matrix W in equation 1. It's improper to claim that LInearGNN is a non-parametric solution. The authors should revise their description of LinearGNN to avoid confusion.

3. This paper mentions that it is always possible to cheat the fully-inductive setup by training a separate instance of existing models for each test dataset (in Line 75). However, the proposed LinearGNN operates like what it just said by training a linear layer with a graph convolution operation for a test graph and the authors called this LinearGNN a non-parametric solution, or preprocessing step (in Table 1). It's hard to convince the readers that the proposed method is a fully-inductive graph learning method. 

4. Though the authors show that GraphAny has better average performance in total 31 graphs in Table 2. However, the experimental results in Table 5 shows that GAT outperforms GraphAny in 18 out of 31 graphs, which means that the proposed method does not have advantage in the fully inductive learning setting. In addition, GAT is a baseline proposed in 2018, and many recent methods can outperform GAT in most of these graphs. 

5. How does the different values of t influence the performance of GraphAny on different datasets? It's better to include an ablation study on the effect of t.

### Questions
1. How do you get the attention score in equation 5? Do you just sum all elements in matrix $P_u^{i}$ in equation 10? What is the learnable weight in the attention module as shown in figure 3?

2. Can you further explain the experimental setting in figure 5? What does the density mean? Since the value is in the range of [0, 1], is this value normalized?

3. This paper mentions that it is always possible to cheat the fully-inductive setup by training a separate instance of existing models for each test dataset (in Line 75). However, the proposed LinearGNN operates like what it just said by training a linear layer with a graph convolution operation for a test graph and the authors called this LinearGNN a non-parametric solution, or preprocessing step (in Table 1). It's hard to convince the readers that the proposed method is a fully-inductive graph learning method. Can the authors clearly differentiate your approach from the "cheating" setup?

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
4

### Summary
The authors focus on addressing a challenging problem: enabling GNNs to be fully-inductive across diverse datasets. They propose a model called GraphAny. Specifically, the authors employed multiple encoders (LinearGNNs) whose parameters can be obtained analytically, allowing it to generalize across datasets with different feature and label spaces. Additionally, the authors design an attention-based, learnable MLP to capture transferable graph patterns. Extensive experiments demonstrate the model's effectiveness.

### Strengths
S1. The authors are ambitious, tackling a highly challenging and valuable problem: designing a foundational GNN model that can generalize across diverse datasets. 

S2. The proposed method is ingenious. The authors introduce a LinearGNN that does not require training, enabling the model to adapt to different datasets.

S3. The experimental results are powerful and impressive. 

S4. The authors provide the complete code, along with a well-organized README file, to support their views.

### Weaknesses
W1. In fact, the proposed LinearGNNs seem to me more like a data preprocessing method which requires no learning to unify the feature and label spaces through analytical solutions.

W2. Regarding W1, the authors’ statement in the Introduction that GraphAny is the first fully-inductive method seems somewhat over-claimed. According to the views in this paper, any model that can be solved analytically (i.e., without training) could also be seem as fully-inductive. Nonetheless, this point does not negate the contribution of the attention-based component to knowledge transfer.

W3. The paper does not mention some recent methods capable of achieving the fully-inductive as described, such as GraphControl [1]. 

W4. I suggest that the author should provide the data split ratio for downstream test datasets (it is vaguely mentioned only in the appendix). This is a crucial setting, as if my understanding is correct, the proposed method requires a certain amount of ground-truth labels to analytically solve the parameters of LinearGNNs on test datasets.

W5. Based on W4, the approach in this paper seems to be semi-supervised (or fine-tuned) on downstream tasks, meaning it has access to the same amount of labeled data as other semi-supervised algorithms like GCN. Moreover, GraphAny benefits from additional prior knowledge from other datasets (i.e., the pre-training phase), making it seemingly more advantageous compared to other algorithms in experimental settings. This stands in contrast to the authors' claim that other semi-supervised algorithms have an additional advantage over GraphAny in the experimental settings.

If LinearGNNs do not require any test dataset labels to solve the parameters (i.e. completely zero-shot scenario), then W4 and W5 would not hold. I strongly recommend that the authors add further explanations in the paper to improve reader comprehension.

[1] GraphControl: Adding Conditional Control to Universal Graph Pre-trained Models for Graph Domain Transfer Learning, WWW24.

### Questions
Please see above.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces GraphAny, a model designed for fully-inductive graph learning, where models must infer on new graphs with varying structures, features, and labels. GraphAny leverages LinearGNN for analytical graph inference, adaptable to diverse graph types. By integrating multiple LinearGNN predictions using learned inductive attention, GraphAny ensures robust generalization to new graphs. Empirical results demonstrate GraphAny's effectiveness, achieving a 67.26% average accuracy on 30 new graphs with minimal training data, outperforming both inductive and transductive baselines.

### Strengths
1. this paper raises a more general and challenging task for graph ood, that is the fully inductive node classification, which requires the model can generalize to arbitrary graphs, involving new structures, new dimensions, and semantics for their feature and label spaces.

2. this paper designs a novel method GraphAny, that integrates the multiple LinearGNN predictions and learned inductive attention, which satisfies the permutation invariant and robust to dimension changes

3.  the paper gives comprehensive experiments and evaluation of various datasets, showing the effectiveness of their methods.

### Weaknesses
1. The lack of baseline. This paper seems only to compare with the test-adapted GNN models as the baselines (GCN, GAT, MLP), I am not very certain if any other GNN baselines trained on the one dataset while generalizing to more datasets, such as the LLM-based GFM[1]. 

2. Since your method is based on the combination of 5 different linearGNNs ($ F = X$ (Linear), $F = AX$ (LinearSGC1), $F = A^2X $(LinearSGC2), $F = (I − A)X$ (LinearHGC1) and $F = (I − A)^2X$ (LinearHGC2) ), have you ever compared your method with the random coefficients combination of them? I suggest comparing GraphAny to a baseline that uses random or fixed coefficients to combine the 5 LinearGNN components. This would help isolate the benefit of the learned inductive attention mechanism.

[1] One for All: Towards Training One Graph Model for All Classification Tasks

### Questions
1.  Could you compare your method with the random coefficients combination of 5 different linearGNNs?

2. According to your Table 2 and Figure 7, it seems that SGC1 and SGC2 occupy a dominant position( high weight and high accuracy). Could you discuss why this happens more? Could you analyze why SGC1 and SGC2 tend to get higher weights and accuracy? Does this suggest that simpler graph convolutions are more transferable? How might this insight inform future designs of inductive graph models?

### Soundness
3

### Presentation
3

### Contribution
4
