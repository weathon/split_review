# Temporal Generalization Estimation in Evolving Graphs

- Decision: Accept
- Scores: 6, 5, 6, 8, 5

## Abstract
Graph Neural Networks (GNNs) are widely deployed in vast fields, but they often struggle to maintain accurate representations as graphs evolve. 
We theoretically establish a lower bound, proving that under mild conditions, representation distortion inevitably occurs over time.
To estimate the temporal distortion without human annotation after deployment, one naive approach is to pre-train a recurrent model (e.g., RNN) before deployment and use this model afterwards, but the estimation is far from satisfactory.
In this paper, we analyze the representation distortion from an information theory perspective, and attribute it primarily to inaccurate feature extraction during evolution.
Consequently, we introduce \textsc{Smart}, a straightforward and effective baseline enhanced by an adaptive feature extractor through self-supervised graph reconstruction.
In synthetic random graphs, we further refine the former lower bound to show the inevitable distortion over time and empirically observe that \textsc{Smart} achieves good estimation performance.  
Moreover, we observe that \textsc{Smart} consistently shows outstanding generalization estimation on four real-world evolving graphs. The ablation studies underscore the necessity of graph reconstruction. For example, on OGB-arXiv dataset, the estimation metric MAPE deteriorates from 2.19\% to 8.00\% without reconstruction.

\iffalse

Graph Neural Networks (GNNs) find broad application across various domains, but they often struggle to maintain accurate representations as graphs evolve. We theoretically establish that, under mild conditions, representation distortion inevitably occurs over time, leading to unreliable performance post-deployment. To proactively estimate generalization degradation without human annotation, one approach is to pre-train a recurrent model (e.g., RNN) on partially observed labels before deployment, but this method falls short of providing satisfactory estimates.

In this paper, we analyze representation distortion from an information loss perspective and attribute it primarily to inaccurate feature extraction during evolution. Consequently, we introduce \textsc{Smart}, a straightforward and effective baseline enhanced by augmented graph reconstruction. In synthetic random graphs, we refine the form

a closed-form generalization error after deployment, with \textsc{Smart} achieving a maximum of 9.11\% MAPE over 180 timesteps of evolution. Moreover, \textsc{Smart} consistently demonstrates exceptional generalization estimation on four real-world evolving graphs. Ablation studies underscore the importance of graph reconstruction, as seen with the Pharmabio dataset, where the estimation MAPE deteriorates from 1.34% to 87.38% without reconstruction
\fi

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This study investigates the representation distortion of graphs during evolution. The authors proposed SMART to estimate the temporal generalization performance of GNN. The authors provided theoretical proofs as well as numerical experiments, showing the distortion of representation is inevitable and providing a way of estimating generalization loss.

### Strengths
This is a novel study trying to analyze the representation distortion from an information theory perspective, which I think is an important and interesting question.  The authors theoretically establish a lower bound and conducted various numerical experiments using both synthetic datasets and real world datasets. Introduction is straightforward. The results seem promising. The ablation study is convincing and sufficient.

### Weaknesses
The authors mainly compared their results with linear regression. The authors may add more model comparisons to make the results more convincing.

Figure 1 is a bit confusing: what’s the x axis? And what are the nodes at each year?

For the information loss, the authors considered the loss from RNN as well as from representation distortion. Can the authors comment on the loss of information from graphs to their low dimensional representations and their effects on the model.

More evaluation metrics besides MAPE should be considered for the synthetic datasets.

Interestingly GCN seems achieved the best performance in the three compared GNNs, can the authors comment on the contribution of different GNN structures to the performance?

### Questions
Figure 1 is a bit confusing: what’s the x axis? And what are the nodes at each year?

For the information loss, the authors considered the loss from RNN as well as from representation distortion. Can the authors comment on the loss of information from graphs to their low dimensional representations and their effects on the model.

More evaluation metrics besides MAPE should be considered for the synthetic datasets.

Interestingly GCN seems achieved the best performance in the three compared GNNs, can the authors comment on the contribution of different GNN structures to the performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies the problem of estimating the generalization performance of GNNs on evolving graphs. The authors propose SMART, which estimates the generalization performance of GNNs without the need for manual annotation post-deployment. SMART employs self-supervised contrastive graph reconstruction to update the feature extractor, minimizing information loss during the dynamic evolution process.

### Strengths
S1. The problem is of significant importance in dynamic graph learning, and the authors provide theoretical proofs to demonstrate that representation distortion is inevitable.

S2. The authors derive a closed-form expression of the generalization error bound on synthetic data and verify the effectiveness of the proposed method.

S3. The paper is well-written, and I have no complaint about the presentation of the paper.

### Weaknesses
W1. The theoretical analysis is limited to single-layer GCN models. It would be beneficial to extend the analysis to multi-layer GCNs or other more complex graph neural network architectures, as single-layer models might not fully capture the complexities of real-world graph data. The current analysis provides a good starting point, but its practical applicability could be limited if it doesn't generalize to more sophisticated models.

W2. The baseline only includes simple linear regression models. A more compelling baseline would involve a model that is continuously updated with new node labels as they become available and then retrained. This would provide a more direct comparison to the proposed method, demonstrating whether the generalization curve of such a retraining approach is close to what SMART predicts. Such a comparison is crucial to show the true advantage of the proposed method over a more standard approach.

W3. The paper primarily focuses on performance drops due to changes in graph structure (nodes and edges) in citation networks, while the category distribution remains relatively stable. However, in many real-world scenarios, label changes and concept drift are significant factors causing performance degradation. It's necessary to discuss the applicability of the proposed method in such dynamic environments where both the graph structure and the underlying label distributions are evolving. The current evaluation does not address scenarios with frequent label changes, which is a common challenge in real applications.

### Questions
See W1-W3 for details.

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
This paper proposes a method (SMART) for performing generalization error estimation on temporal node classification tasks. The authors show that representations will become increasingly distorted as time increases, and propose to use both a structure graph reconstruction and feature construction loss to improve representation quality. The adapted features are feed into an RNN that is trained to predict the loss. The authors also propose two theorems: one which shows that distortion is strictly increasing over time, and the other one is specific to the Barbasi Albert graph and is used to argue the benefits of SMART.

### Strengths
- This paper studies an interesting problem (generalization gap prediction for temporal node classification) that has not been well-studied in the graph representation learning literature before. 

- The authors conduct experiments across a variety of datasets, and conduct several ablations to demonstrate the benefits of each of the components of SMART. 

- The authors attempt to provide some theoretical bounds and use these, as well as an information theory framework, to ground the proposed method.

### Weaknesses
 - The authors only compared to a single linear regression baseline. While other methods for generalization prediction are not specific to temporal graph data, it should still be possible to consider some. Maybe some from [1] could be adapted? In this vein, I think there should be more citations to other generalization error predictors and a dedicated related works section in the main paper. 

- The theorems need to be discussed more. For example, in theorem 1, I don't think that beta has been defined. Furthermore, while the authors make the strong but acceptable assumption that the graph will only add edges, I was wondering if it was also assumed that the underlying graphs were homophilous. Do the authors expect the proposed method to work on heterophilus graphs as well? 

- The writing could be improved. For example, its not clear why the approach is referred to as "constrastive." From my understanding the authors do augment the graph, but the overall loss is purely reconstruction based.

### Questions
Please see the weaknesses above.

I'd appreciate some clarifications about the theorems and potential baselines as mentioned above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents an important question: how to ensure that GNN gives a good prediction for graphs that are rapidly evolving in time. The authors first give a theoretical proof to show that under mild conditions, as graph evolves, graph representation distortion is not avoidable (the loss is lower bounded). Secondly, the authors propose information losses in two phases: (1) information loss induced by RNN and (2) information loss induced by representation distortion. Then, the authors have proposed SMART that contains contrastive graph construction. The augmented feature graphs is randomly adding or dropping edges, and then structure reconstruction loss and feature reconstruction loss are used on the contrasted examples. The authors have verified the effectiveness of SMART on the barabasi-albert random graph, and performed extensive experiments to showcase SMART's effectiveness with evolving graphs.

### Strengths
S1. The paper targets evolving graph prediction, which is a challenging problem in the research community. It is novel to consider the evolving graph using information loss perspective, and the contrastive solution to resolve such problem is very convincing.

S2. The paper is clearly written. The authors give a clear problem definition with theoretical justification. There are several architecture and losses considerations in the methodology, yet each component is clearly addressed. The author has also provided a theoretical proof on the barabasi-albert random graph to showcase the effectiveness of SMART.

S3. The empirical results presented in the paper show that the proposed method SMART outperforms linear regression model, using the same GCN/GAT/GraphSage backbone structures and evaluated on four different datasets, showcasing the quality and robustness of SMART. 

S4. Given the ubiquity and increasing reliance on evolving graph in real-world applications, the capability to adapt to evolving graph is important. SMART can adapt to various graph learning architectures and has potential impact for studying the changing graphs in time.

S5.  The ablation study is well-written and consider various loss configurations and hyper-parameter configueratons.

### Weaknesses
W1. The paper does not have a related work section. There should be at least some descriptions of the previous work which showcases that GNNs performances can suffer from the representation distortion over time, and the performance degradation occurs.

W2. There appears to be an inconsistency of mentioning the information loss in Section 3.2 and introducing SMART with contrastive loss in Section 3.3. The information loss is introduced, but not used in experiment settings (MPAE and standard error are used instead) or the later contrastive loss calculation. There should at least some experiments and measurements that connect information loss to contrastive learning post deployment, and to show that SMART is able to reduce the information loss induced by representation distortion. A theoretical justification is also fine.

W3. The data augmentation in graph is too naive. The authors have only considered to randomly add or drop edges, which should only work for graphs without edge labels. While the random data augmentation technique works for barabasi-albert random graphs, it should not be effective for the cases where edge labels are also changing (for example, people change their relationship status with other people). The authors should consider more complex data augmentation techniques in graphs.

### Questions
Q1. Theorem 1 is evaluated only for one layer GNN with a Leaky ReLU activation. Is Theorem 1 adjustable to multi-layer GNN and different GNN backbone structures such as GCN/GAT/GraphSage?

Q2. Figure 3, what is the y-axis prediction loss? Why not use other evaluation metrics to showcase the GNN prediction performances deterioration?

Q3. Is there a particular reason that RNN is used instead of other time-series model to capture the temporal variation?

Q4. Will the contrastive graph reconstruction improve the feature extractor during the pre-deployment phase? Why just limit the contrastive learning and reconstruction to post-deployment?

Q5. How will the proposed algorithm be used towards more complex real-time graphs? For example, how to deal with graphs that contain changing node labels and changing edge labels? How to apply the methods to heterogeneous graphs or spatial temporal graphs?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper analyzes and tackles the challenge of temporal representation distortion in GNNs as the graph evolves over time, so as to yield better generalization estimation. Based on a few assumptions, the authors theoretically establish that such distortion is strictly increasing over time with a lower bound. Furthermore, based on the pre-trained GNN and an RNN that performs temporal generalization estimation, the authors propose a solution that incorporates an adaptive feature extractor that operates through self-supervised graph reconstruction, aiming to estimate and adjust for the distortion. Under a synthetic random graph setting,  a closed-form generalization error is also derived. Experiments on synthetic and real-world benchmarks demonstrate the effectiveness of the proposed method in terms of substantially improving estimation accuracy and generalization ability.

### Strengths
1.	The general motivation for analyzing the generalization of evolving graphs is interesting and important. It is also interesting to see the theoretical analysis with a synthetic random graph demonstration with a closed-form generalization error.
2.	The presentation quality of this paper is in general satisfactory, in terms of the organization and figure demonstration.
3.	The experiments and analysis on the proposed method itself are relatively sufficient including model component ablation and hyper-parameter study.

### Weaknesses
1. One major concern is the lack of baseline methods. The proposed method is only compared with a linear regression, which turns out to be a naive baseline. The methods mentioned in the related work D.2 are not compared. Moreover, only the MAPE with standard error is evaluated. More evaluation metrics are expected.
2. It will be better if the methods are evaluated on a few more state-of-the-art backbones to further enhance the effectiveness of the proposed method.
3. The assumptions made to conduct theoretical analysis and bound derivation could be a concern as they are often too strong. Evolving graphs also contain nodes disappearing in many cases(e.g. sensor networks with possible malfunction over time), which means the assumption of an ever-growing network can be often invalid. Moreover, the zero-mean requires a non-min-max preprocessing of features. The authors need to be specific about the claims.
4. It would be better to sketch the connection between the information loss and the form in Equation 2, section 3.2.
5. It would be better to define some notations such as the function l, and generalization error beforehand for better understanding of the idea.

### Questions
Please see the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
