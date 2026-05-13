# Open-Set Graph Anomaly Detection via Normal Structure Regularisation

- Decision: Accept
- Scores: 6, 3, 6, 6

## Abstract
This paper considers an important Graph Anomaly Detection (GAD) task, namely open-set GAD, which aims to train a detection model using a small number of normal and anomaly nodes (referred to as \textit{seen anomalies}) to detect both seen anomalies and \textit{unseen anomalies} (\ie, anomalies that cannot be illustrated the training anomalies). Those labelled training data provide crucial prior knowledge about abnormalities for GAD models, enabling substantially reduced detection errors. However, current supervised GAD methods tend to over-emphasise fitting the seen anomalies, leading to many errors of
detecting the unseen anomalies as normal nodes.
Further, existing open-set AD models were introduced to handle Euclidean data, failing to effectively capture discriminative features from graph structure and node attributes for GAD.
In this work, we propose a novel 
open-set GAD approach, namely \textit{\underline{n}ormal \underline{s}tructure \underline{reg}ularisation} (\textbf{NSReg}),
to achieve generalised detection ability to unseen anomalies, while maintaining its effectiveness on detecting seen anomalies.
The key idea in NSReg is to introduce a regularisation term that enforces the learning of compact, semantically-rich representations of normal nodes based on their structural relations to other nodes. When being optimised with supervised anomaly detection losses, the regularisation term helps incorporate strong normality into the modelling, and thus, it effectively avoids overfitting the seen anomalies and learns a better normality decision boundary, largely reducing the false negatives of detecting unseen anomalies as normal. Extensive empirical results on seven real-world datasets show that NSReg significantly outperforms state-of-the-art competing methods by at least 14\% AUC-ROC on the unseen anomaly classes and by 10\% AUC-ROC on all anomaly classes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper tackles the challenge of open-set graph anomaly detection, where the detection model is trained to detect both known and previously unseen anomalies. The authors introduce NSReg, a method that utilizes auxiliary relational information around normal nodes to regularize the model's training. NSReg works by distancing unseen anomalies from normal nodes, aiding in their detection. The paper also includes a theoretical analysis of the proposed method. Comprehensive experiments evaluate the model's effectiveness and the individual contributions of its components.

### Strengths
1. The paper tackles an important and impactful problem—open-set graph anomaly detection—with significant potential for real-world applications.
2. The writing is clear, and the paper is well-organized, making it easy to follow.
3. A theoretical analysis is provided, adding depth to the proposed approach.
4. The paper includes thorough experiments that demonstrate the proposed method's effectiveness, along with ablation studies that evaluate the contribution of each component.

### Weaknesses
1. The core idea of using neighborhood information to enhance anomaly detection is not entirely novel, as similar approaches have been explored in prior works [1], [2], [3]. A comparison between NSReg and these previous methods is necessary to better contextualize its contributions.

2. I have some concerns about the effectiveness of the Normal-node-oriented Relation Generation component. Specifically, the unconnected relation $R_{(n,u,u)}$ between normal nodes and other nodes may include a large number of connections to unlabeled normal nodes, given the predominance of normal nodes in the dataset, as the authors also note. If most $R_{(n,u,u)}$ relations are between labeled and unlabeled normal nodes, distancing these pairs may not meaningfully enhance model training. At the same time, if there are very few $R_{(n,u,u)}$ relations involving labeled normal nodes and unlabeled unseen anomalies, the regularization term may have minimal impact on detecting unseen anomalies. I suggest that the authors conduct an empirical analysis on the distribution of different types of relations within the sampled $R_{(n,u,u)}$ set and discuss how this distribution affects the regularization term's effectiveness.

3. In Eq. (3), the meaning of symbols $\cdot$ and $\circ$ are unclear. Also, in Eq. (2) and (5), the supervised training loss should sum over all training nodes, not the entire node set $V$.

4. Could the authors provide justifications for updating the three components $\eta$, $F$ and $E$, and $\phi$ separately as stated in the pseudo-code?

5. In the Yelp dataset, NSReg displays less sensitivity to the hyper-parameter $\lambda$ compared to other datasets (such as Photo, Computers, and CS). Could the authors provide an explanation for this? Additionally, G. SMOTE performs better on unseen anomalies for this dataset, as shown in Table 1. An explanation for this would also be necessary.

6. The source code for this work is not provided for review.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studied the unsupervised graph anomaly detection problem under the lack of prior knowledge setting. In particular, it proposes an approach focusing on learning normality using supervised signals to distinguish unseen anomalies from normal nodes. The proposed method, NSReg, models three types of normal-node-oriented relations as a discriminative task, enhancing representation learning with enriched normality semantics. The authors argue that this approach effectively disentangles unseen anomalous nodes from normal nodes in the representation space. The paper also discusses the plug-and-play design of the method, which allows for its application in various scenarios.

### Strengths
1. The problem studied in the paper is interesting. Due to the lack of prior knowledge, unsupervised graph anomaly detection often suffers from high error rates. The authors focus on learning normality to enhance the model's ability to detect unseen anomalies, potentially improving the performance of existing methods in this area.
2.  The Plug-and-Play design is a notable strength, as it allows the method to be easily integrated into existing frameworks and applied to various scenarios.
3. The experiments conducted are comprehensive, covering the performance on all anomalies and unseen anomalies, ablation study, and the performance as a plug module, which evaluates the proposed method's effectiveness well.

### Weaknesses
1. There are some unsupervised graph anomaly detection works that achieve considerable inductive performance. The author did not point out why these methods cannot meet the requirements. There should be a more thorough comparison of these existing methods and an analysis of the deeper reasons behind them.
2. The description of the proposed method did not clarify the innovation of this paper. One innovation of this paper is the focus on learning normality on structure. This differentiates this work from existing one-class classification/anomaly detection methods, but this point is unclear.
3. The presentation of the paper needs to be improved.

### Questions
1. Aegis (Inductive anomaly detection on attributed networks) is an unsupervised graph anomaly detection using GAN to strengthen the generalization ability of the model. The authors should discuss how their method compares with this work.
2. Line 271, why is the $aplha$ set to 0.8? What is the significance of this value? The author should discuss this in detail and provide some experiment results to support this choice.
3. Figure 3 is hard to understand.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel open-set Graph Anomaly Detection (GAD) approach called Normal Structure Regularization (NSReg). The method aims to achieve generalized detection capabilities for unseen anomalies while retaining effectiveness in identifying known anomalies. It introduces a regularization term that encourages the learning of compact, semantically rich representations of normal nodes, informed by their structural relationships with other nodes. Extensive empirical evaluations on seven real-world datasets demonstrate that NSReg significantly outperforms state-of-the-art competing methods.

### Strengths
1. The experiments are comprehensive and yield strong results.
2. The paper provides some theoretical proofs.
3. It introduces a novel open-set approach to Graph Anomaly Detection (GAD).

### Weaknesses
1. The paper's structure is disorganized, and the context of the paragraph is stiff. For instance, the three types of 'Normal-node-oriented Relations' are not clearly explained. Additionally, in lines 225-228, the authors mention analyzing the effects of enforcing structural normality in the representation space and its advantages for enhancing generalization to unseen anomalies. However, it is difficult to connect this to the later explanations, and the concept of structural normality even is not defined.
2. The wording in the paper is imprecise. For example, in the caption of Figure 2, the term "The green teal dashed box" does not clearly indicate which part of the figure it corresponds to. Furthermore, it is unclear whether "a discriminative graph anomaly detector" refers to "a graph anomaly detector with a discriminator," as the term "detector" itself implies a discriminative function.
3. The paper does not provide information about the hardware used for running experiments, nor does it include the experimental code and datasets. This raises concerns about the reproducibility of the results. Moreover, the novelty of the paper is questionable. The Normal-node-oriented Relation Modelling section relies on simplistic relational labels C(r) for supervised training. The impact of isolated anomalous nodes connected to multiple normal nodes in C(r) is not discussed. Also, the calculation of C(r) does not consider other factors such as node degree or average features.

### Questions
1. What does "connected normal nodes, unconnected normal nodes, and unconnected normal nodes to unlabelled nodes" mean? It would be best to illustrate these relationships with a diagram.
2. What does the calculation symbol "$\circ$" represent in the paper?
3. In line 241, what do "these two types of relations" refer to? Are they the two types described in line 232: "the relations between only the normal nodes and the relations between normal and anomaly nodes"? Why does the relationship description in line 2—“connected normal nodes, unconnected normal nodes, and unconnected normal nodes to unlabelled nodes”—not use the same phrasing? Are there actually distinctions between them?
4. In line 238, what is the specific operation when it states, “If Z is shared with a discriminative graph anomaly detector”?
5. The equations in lines 267-269 are not labelled and should correspond to Equation 3. How is alpha determined, and why is it set to 0.8?
6. In Figure 2, is the "shared representation space" represented by the grey rectangle with dashed lines? The arrows inside have three different styles, but the authors only labelled two of them.
7. In line 277, why is g considered a mapping and how is it discriminative?
8. What is the relationship between the equation in line 282 and g? Is this equation equivalent to $g_C$?
9. How does the paper address the prediction of unseen nodes, and how does it identify unseen nodes?

### Soundness
3

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
4

### Summary
The paper proposes an approach for open-set graph anomaly detection. The authors introduce a method called Normal Structure Regularisation (NSReg) to regularize the learning process by focusing on the structural relationships among normal nodes in the graph. Experiments show that the framework outperforms baselines on datasets included in this paper.

### Strengths
S1. The authors introduce a method called Normal Structure Regularisation (NSReg) to regularize the learning process by focusing on the structural relationships among normal nodes in the graph.

S2. Experiments show that the framework outperforms baselines on datasets included in this paper.

### Weaknesses
W1. The contribution seems to be overclaimed. As stated in this paper, open-set GAD is an under-explored problem. However, the definition of open-set GAD problem is very similar to that of out-of-distribution detection, and there are several previous works in this area, such as GNNSAFE[1], EnergyDef[2], and GNSD[3]. 

W2. Experiments are not comprehensive enough. As for the supervised GAD model, there are several new baselines, such as XGBGraph[4], and CONSISGAD[5]. The authors should include them as baselines as well. Besides, as mentioned above in W1, such a task is almost the same as the out-of-distribution problem, which means the authors need to compare their framework with out-of-distribution models on out-of-distribution datasets, instead of creating synthetic datasets from T-Finance. 

W3. Some parts of the paper need to be further explained. For example, in Section 3.3, Normal-node-oriented Relation Generation, the authors set alpha = 0.8 by default but did not provide any intuition or theoretical analysis of such a value. Furthermore, the authors do not provide a clear explanation of why the range [0, 0.5] for alpha is invalid, especially given that Equation (3) does not impose such a limitation.

### Questions
Q1. Can the authors explain the differences between open-set GAD and out-of-distribution detection? 

Reference
1. Qitian Wu, Yiting Chen, Chenxiao Yang, Junchi Yan. Energy-based Out-of-Distribution Detection for Graph Neural Networks. ICLR 2023. 
2. Zheng Gong, Ying Sun. An Energy-centric Framework for Category-free Out-of-distribution Node Detection in Graphs. KDD 2024. 
3. Xixun Lin, Wenxiao Zhang, Fengzhao Shi, Chuan Zhou, Lixin Zou, Xiangyu Zhao, Dawei Yin, Shirui Pan, Yanan Cao. Graph Neural Stochastic Diffusion for Estimating Uncertainty in Node Classification. ICML 2024. 
4. Jianheng Tang, Fengrui Hua, Ziqi Gao, Peilin Zhao, Jia Li. GADBench: Revisiting and Benchmarking Supervised Graph Anomaly Detection. NeurIPS 2023. 
5. Nan Chen, Zemin Liu, Bryan Hooi, Bingsheng He, Rizal Fathony, Jun Hu, Jia Chen. Consistency Training with Learnable Data Augmentation for Graph Anomaly Detection with Limited Supervision. ICLR 2024.

### Soundness
2

### Presentation
3

### Contribution
2
