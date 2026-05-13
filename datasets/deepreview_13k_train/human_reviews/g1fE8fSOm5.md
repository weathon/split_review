# Graph Neural Networks Provably Benefit from Structural Information: A Feature Learning Perspective

- Decision: Reject
- Scores: 5, 5, 6, 6, 3

## Abstract
Graph neural networks (GNNs) have pioneered advancements in graph representation learning, exhibiting superior feature learning and performance over multilayer perceptrons (MLPs) when handling graph inputs. However, understanding the feature learning aspect of GNNs is still in its initial stage. This study aims to bridge this gap by investigating the role of graph convolution within the context of feature learning theory in neural networks using gradient descent training. We provide a distinct characterization of signal learning and noise memorization in two-layer graph convolutional networks (GCNs), contrasting them with two-layer convolutional neural networks (CNNs). Our findings reveal that graph convolution significantly augments the benign overfitting regime over the counterpart CNNs, where signal learning surpasses noise memorization, by approximately factor $\sqrt{D}^{q-2}$, with $D$ denoting a node's expected degree and $q$ being the power of the ReLU activation function where $q > 2$. These findings highlight a substantial discrepancy between GNNs and MLPs in terms of feature learning and generalization capacity after gradient descent training, a conclusion further substantiated by our empirical simulations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper provides grounded theoretical exploration to analyze the characteristics, effectiveness, and superbness of GCNs (compared with other common modules), revealing the role that graph convolution plays. It has several interesting findings, especially the ones about test erros.

### Strengths
(placeholder for future edit, please allow me extra hours to finish the writing.)

### Weaknesses
The practical significance of the theoretical results is unclear. While the study provides a comparison between GCNs and CNNs, the implications for real-world applications are not adequately addressed. For instance, how do these theoretical findings translate into tangible improvements in GCN design or training? Furthermore, the theoretical results do not fully capture the essence of graph structure information. The study mentions the adjacency matrix A and the Laplacian matrix L as key differentiators between GCNs and CNNs. However, the derived results do not explicitly incorporate these matrices in a way that clearly demonstrates their impact on the observed differences in generalization. A more concrete connection between the theoretical framework and the specific graph structures is needed to strengthen the conclusions.

### Questions
(placeholder for future edit, please allow me extra hours to finish the writing.)

### Soundness
4 excellent

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
This study aims to address the knowledge gap by investigating the role of graph convolution in feature learning theory under a specific data generative model. They conduct a comparative analysis of optimization and generalization between two-layer graph convolutional networks (GCNs) and their convolutional neural network (CNN) counterparts. They indicate that graph convolution significantly improves the range of low test errors compared to CNNs. This highlights a significant discrepancy in generalization capacity between GNNs and MLPs, a conclusion further supported by our empirical simulations on both synthetic and real-world datasets.

### Strengths
Several theoretical results about two-layer GCNs are obtained to compare with CNNs.

### Weaknesses
 - I fully agree that it is a theoretical paper that sufficient assumptions are necessary, while the node feature part is somehow far from the reality, as there are no such golden methods to divide any feature into such two orthogonal groups. Therefore, more connection of the applicability of this node feature model to the real-world setting is demanded, e.g. by showing some repression/clustering results of some real-world node features on such two orthogonal part, which is not required to be identifiable.
- Homophily is considered to be a key factor for GNNs, especially unavoidable for those analytical works based on SBM, where the interclass and intraclass connections are explicitly modeled. However, this paper does not include such a discussion, but rather focuses on the distribution of the node features.
- For Figure 3 and 4, it is better to provide variance bars by repeating the experiments of several times to show the stability of the results.

### Questions
1. I am confused with the significance of the theoretical results provided in this work. What's the purpose? Guide to improve GCN's training efficiency? or explain why GCNs better than CNNs?

2. The main difference between GCNs and CNNs is the introduction of graph structure information, such as adjacency matrix A and Laplacian matrix L, where the theoretical results in this work have not entirely reflected the structure information (A or L), please explain this in detail.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel angle to view the training set and generalization ability of GNNs compared to CNNs. It is based on a data model that combines both the signal-to-noise for the node feature part and the stochastic block model for the graph structure. For the analysis, it introduces a signal-to-noise ratio quantity to better describe the shape of the dataset, which is closer to the utility of GNNs. Experiments on simulation datasets coincide with the theoretical analysis.

### Strengths
- The whole paper is well-structured and problem is well formulated, especially both the training phases and generalization ability are discussed.
- Detailed and quantitative explanation are entailed along with the arguments of this paper, also the explanation of the numbers are helpful in understanding such proofs with practical impressions.
- Proof stretches are friendly to readers.

### Weaknesses
The model of the data is very specific and limited, even for a two class model. The two classes are modeled as some template signal and its negative, without noise that directly affects the signal, e.g., additive noise. The noise is supported on indices which are disjoint from the signal. It is ok to consider simplistic models when doing mathematical analysis, but this should be clear for the reader. The fact that the model is simplistic should be clarified better in the text. The motivation for choosing such a simplistic model can be explained better. Namely, to be able to clearly decouple the signal learning aspect from the noise memorization aspect of learning.



### Questions
- For the signal-noise model of the data model part, $x^{(1)}$ means the most ``informative'' node features. And does it imply that a binary classification setting according to $y$ is sampled from $\{-1,1\}.$ Is it possible that some parts of the conclusion of the paper can be influenced in a multi-classification setting, or just for the sake of proof?
- Should the subsection of 3.4 be part of 3.3? This is a minor issue. Another small suggestion is to standardize the use of the names MLP or CNN.
- For verification on real data, how is the graph of points 1 and 2 of MNIST constructed? By the same possibility of interclass and intraclass connections?
- It would be greatly appreciated if the authors could provide some intuition behind the dimensionality of the two parts of the node features in the data model.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper compares GCN to MLP/CNN when learning on graph data. The paper sets out to show the benefits of using the graph structure in GCNs vs learning a MLP on the node features with no diffusion of features along the edges (which is called CNN in this paper). This is done by proposing a simple generative model for graphs and considering a two layer GCN model, providing exact formulas for gradient descent training, and proving theorems about the accuracy of the trained model. The results of this GCN model are compared to equivalent results of a MLP/CNN model. This way, GCN is shown theoretically to be superior to MLPs/CNNs.

### Strengths
The paper treats all aspects of learning with regard to the proposed model. Namely, they derive a formula for the training process and for the resulting accuracy. Hence, the paper provides a complete theoretical analysis, which rigorously proves the benefits of GCN over CNNs (for the proposed data model). The paper is clearly written.

### Weaknesses
1. (I am not an expert in deep learning theory, so my assessment of this might be less confident.) The novelty of the proposed method seems to be limited. According to my preliminary check, the main theory and proof of this work follow the prior feature learning theory paper closely [1]. It seems to be directly adapted from [1]. Could the authors summarize the main difference/contributions of this submission, compared to [1]?

2. The main results of why GNNs work are not surprising and not adding new insights to the community. It is well-known that GNNs can help smooth the node features corresponding to the same class, thus making the classification tasks easier [2]. In this sense, the results from this paper do not add new insights or provide potential future topics in the field.

3. The experimental results are also widely observed by previous work in the community.

### Questions
In section 3.3, why do you call this model a CNN and not a MLP? You apply a MLP on each node separately, and there is no diffusion/mixing between the features of the different nodes. It is only equivalent to a 1x1 standard CNN. I would call it a MLP that treats each node as a separate data point.

Page 8, Verification via real-world data: In your model, the two features come from one template with positive and negative sign, while in the experiment you have two features that come from two different templates. Can you explain in the paper how the experiment differs from the theoretical setting (if I am not missing something)? Can you run an experiment fully modeled as the proposed data model?

Since the experiment synthetically builds graph data that corresponds to the proposed data model, it does not show that the proposed model can describe real data. Is there some real data that can be approximated by your model? Namely, can you fit the parameters of the model to data, and check its accuracy/ability to represent real data? Or is there no real data that corresponds to your mode?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies why GNNs work from the perspective of feature learning theory, which is proposed by recent work to analyze why CNNs work. This paper identifies the convergence conditions for GNNs under the defined specific data generation model, i.e., SNM-SBM. Overall, this work justifies why GNNs can achieve better generalization ability than CNNs on graph data from the perspective of feature learning theory.

### Strengths
1. The motivation for analyzing why GNNs work theoretically is important and potentially inspiring for better GNN designs.

2. The formulation of the feature learning theory in GNNs is grounded and well-presented.

3. The simple simulation experiments are clearly shown.

### Weaknesses
1. (I am not an expert in deep learning theory, so my assessment of this might be less confident.) The novelty of the proposed method seems to be limited. According to my preliminary check, the main theory and proof of this work follow the prior feature learning theory paper closely [1]. It seems to be directly adapted from [1]. Could the authors summarize the main difference/contributions of this submission, compared to [1]?

2. The main results of why GNNs work are not surprising and not adding new insights to the community. It is well-known that GNNs can help smooth the node features corresponding to the same class, thus making the classification tasks easier [2]. In this sense, the results from this paper do not add new insights or provide potential future topics in the field.

3. The experimental results are also widely observed by previous work in the community.

[1] Cao, Yuan, et al. "Benign overfitting in two-layer convolutional neural networks." Advances in neural information processing systems 35 (2022): 25237-25250.

[2] Li, Qimai, Zhichao Han, and Xiao-Ming Wu. "Deeper insights into graph convolutional networks for semi-supervised learning." Proceedings of the AAAI conference on artificial intelligence. Vol. 32. No. 1. 2018.

### Questions
N/A

Typo: "by" above Eq. (3)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
