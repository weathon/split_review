# Editable Graph Neural Network for Node Classifications

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Despite Graph Neural Networks (GNNs) have achieved prominent success in many graph-based learning problem, such as credit risk assessment in financial networks and fake news detection in social networks.
However, the trained GNNs still make errors and these errors may cause serious negative impact on society.
\textit{Model editing}, which corrects the model behavior on wrongly predicted target samples while leaving model predictions unchanged on unrelated samples, has garnered significant interest in the fields of computer vision and natural language processing. However, model editing for graph neural networks (GNNs) is rarely explored, despite GNNs' widespread applicability. 
To fill the gap, we first observe that existing model editing methods significantly deteriorate prediction accuracy (up to $50\%$ accuracy drop) in GNNs while a slight accuracy drop in multi-layer perception (MLP). 
The rationale behind this observation is that the node aggregation in GNNs will spread the editing effect throughout the whole graph.
This propagation pushes the node representation far from its original one.
Motivated by this observation, we propose \underline{E}ditable \underline{G}raph \underline{N}eural \underline{N}etworks (EGNN), a neighbor propagation-free approach to correct the model prediction on misclassified nodes. 
Specifically, EGNN simply stitches an MLP to the underlying GNNs, where the weights of GNNs are frozen during model editing. In this way, EGNN disables the propagation during editing while still utilizing the neighbor propagation scheme for node prediction to obtain satisfactory results. 
Experiments demonstrate that EGNN outperforms existing baselines in terms of effectiveness (correcting wrong predictions with lower accuracy drop), generalizability (correcting wrong predictions for other similar nodes), and efficiency (low training time and memory) on various graph datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a work on tackling the conflict between message aggregation in GNNs and model editing by stitching a MLP as auxiliary; It also provides sufficient experiment results to support the effectiveness of their method.

### Strengths
Strength:

•	The paper claims to be the first work studying model editing on GNNs.

•	They choose to utilize loss landscape to demonstrate the reason of accuracy drops after editing, providing a visualization of the potential rationale; a theoretical analysis in appendix also offers more solid explanation.

•	Seemingly good results on benchmarks.

### Weaknesses
Weakness:

* Adding an additional MLP to compensate the original model is an interesting idea. However I have big concerns about the soundness of Algorithm 1. For example, if we require all parameters of the MLP to be zero, it is almost an optimum to make L_loc and L_task lowest, especially if the pretrained GNN model already has an MLP component (e.g. using skip connections of jumping knowledge). The concern is that the algorithm, as described, might be trivially optimized by simply setting the MLP weights to zero, which would not provide any meaningful editing capability. This is particularly concerning if the base GNN model already incorporates MLP layers, as the added MLP could become redundant and not contribute to the desired editing effect.

* The motivation of editing GNN models is not clear enough. The motivation starts from mitigating errors of GNNs in real world application; however, it does not present an example of such error or mention why the cost of wrong decision is high. It would be beneficial to provide a concrete scenario where correcting a GNN's prediction is crucial, highlighting the potential negative consequences of an incorrect prediction in a real-world context. This would strengthen the justification for the proposed editing approach.

* Lack of analysis of why there exists errors in GNNs’ classification; are GNNs only making wrong prediction with certain type of inputs? It is important to understand the nature of the errors GNNs make. Are these errors random, or are they systematic, occurring with specific types of inputs or data patterns? An analysis of the error patterns would provide valuable insights into the limitations of the GNN and the potential scope of the editing method.

* For section 5.3, it really confuses me how the described experiments help to answer R2: it corrects the flipping nodes and then test whether model makes right prediction on same class? If I get the point correctly, the flipped nodes only take 10% of the training node, so 90% of the time model should be able to learn the correct classification, then why it  can indicate the generalization ability of EGNN? The experimental setup in section 5.3 needs further clarification. It is unclear how editing a small fraction of flipped nodes can demonstrate the generalization ability of the proposed method. The connection between the experimental design and the research question is not well-established.

### Questions
Please refer to weakness.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explorea a and important problem, i.g., GNNs model editing for node classification. This paper empirically shows that the vanilla model editing method may not perform well due to node aggregation. Furthermore, this paper proposes EGNN to correct misclassified samples while preserving other intact nodes, via stitching a trainable MLP. In this way, the power of GNNs for prediction and the editing-friendly MLP can be integrated together in EGNN.

### Strengths
1. The authors can leverage the GNNs’ structure learning meanwhile avoiding the spreading edition errors to guarantee the overall node classification task.

2. The experimental results validate the solution which could address all the erroneous samples.

3.  Via freezing GNNs’ part, EGNN is scalable to address misclassified nodes in the million-size graphs.

### Weaknesses
1. The motivation is not clear. Since the authors trained the model on a subgraph containing only the training node, how node aggregation in GNNs will spread the editing effect throughout the whole graph?

2. The experiment setting is not clear. The authors trained the model on a subgraph containing only the training node, then what graph is used for editing?

### Questions
See weakness.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the graph model editing problem by inserting an MLP in GNN architecture and freezing the GNN model during the model editing phase to alleviate the propagation of misinformation by the message-passing mechanism.

### Strengths
1. The problem setting is interesting.
2. The motivation example in Section 3.1 is intuitive.

### Weaknesses
1. My major concern regarding this paper is the performance of the proposed method. Though Tables 2, 3, and 4 show great improvement compared with GD and ENN, the actual improvement is still limited. Based on the experimental results of GCN and GraphSAGE without any graph editing on these datasets (e.g., the performance of GCN reported in [SUGRL](https://ojs.aaai.org/index.php/AAAI/article/view/20748) Tables 1 and 2), GCN achieves 91.6\% accuracy on A-Photo dataset and 84.5\% accuracy on A-Computers dataset. However, in the proposed method, EGNN achieves 91.97\% accuracy on the A-Photo dataset and 82.85\% accuracy on the A-Computers dataset. Comparing these two results, if editing the graph model could not improve the performance, then why do we need it? Thus, the authors should also report the performance of GCN and GraphSAGE without any editing in the experiment. It's important to demonstrate that graph editing can indeed improve the performance of GNN. If EGNN is worse than the vanilla GCN and GraphSAGE, then the proposed method is meaningless.

2. The novelty of this paper is somehow limited. The proposed method simply incorporates the MLP into the GNN architecture to address the issue of message-passing during the graph editing.

3. In the related work, the period is missing for the sentence "This assumption might not hold well for graph data, given the fundamental node interactions that occur during neighborhood propagation".

4. The evaluation regarding the metric DrawDown is questionable. See question 2.

### Questions
1. In the experiment, the authors evaluate EGNN under the inductive setting.  As many types of GNNs benefit from leveraging the feature and the graph topology of both labeled and unlabeled nodes, can EGNN work in the transductive setting?

2. In Table 2, the authors report the DrawDown of EGNN, which is the **mean absolute difference** between test accuracy before and after performing an edit. Then, how can it be a negative value (e.g., -0.17 for EGNN with GCN and -0.01 for EGNN with GraphSAGE on the Coauthor-CS dataset)?

3. In Algorithm 1 for the EGNN edit procedure, should the condition of the while loop ($\hat{y}\neq y_v$) be $\hat{y}\neq y_e$? Correct me if I misunderstand it. 

4. Figure 2 suggests that the more editing it conducts, the worse performance it achieves shown in the last three subfigures, e.g., Figures GCN (Reddit), GraphSAGE (ogb-arxiv), and GraphSAGE (Reddit). When the number of sequential edits increases from 10 to 40 or 20 to 40, we can observe the DrawDown consistently increases. In this case, why do we need to edit the model anymore?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
