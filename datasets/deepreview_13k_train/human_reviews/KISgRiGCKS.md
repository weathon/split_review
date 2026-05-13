# Optimal Transport-Based Domain Alignment as a Preprocessing Step for Federated Learning

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Federated learning is a subfield of machine learning that avoids sharing local data with a central server, which can enhance privacy and scalability. The inability to consolidate data in a central server leads to a unique problem called dataset imbalance, which is where agents in a network do not have equal representation of the labels one is trying to learn to predict. In FL, fusing locally-trained models with unbalanced datasets may deteriorate the performance of global model aggregation; this further reduces the quality of updated local models and the accuracy of the distributed agents' decisions. In this work, we introduce an Optimal Transport-based preprocessing algorithm that aligns the datasets by minimizing the distributional discrepancy of data along the edge devices without breaking privacy concerns. We accomplish this by leveraging Wasserstein barycenters when computing channel-wise averages. These barycenters are collected in a trusted central server where they collectively generate a target RGB space. By projecting our dataset towards this target space, we minimize the distributional discrepancy on a global level, which facilitates the learning process due to a minimization of variance across the samples in the analyzed network. We demonstrate the capabilities of the proposed approach over the CIFAR-10 dataset, where we show its capability of reaching higher degrees of generalization in fewer communication rounds.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a preprocessing step for federated learning aimed to reduce distributional discrepancy between clients via optimal transport. It computes the channel-wise Wasserstein barycenters on each client and sends them to a trusted server where global Wasserstein barycenters are then computed as the target space and broadcasted to clients. Each client projects their data on the target space. Projected client data are fed into any FL learning algorithm. Experiments demonstrate that this preprocessing step pairing with FedAvg outperforms a number of baseline algorithms.

### Strengths
The proposed preprocessing step is interesting, simple yet effective in boosting FL learning performance.

### Weaknesses
Some concerns are as follows:
1) technical exposition in Section 3.2 is poor. For example, I have no idea what Lines 184-185 mean. There is no definition for $\mathcal{L}_{d^P}(\cdot,\cdot)$ in Eq. (4), $\Sigma_n$ in Eq.(5), $W_{reg}$ in Eq. (7). Why $\lambda_{s}\in\Sigma_{n}$ in Line 215? Furthermore, the description of the channel-wise barycenter calculation is unclear. It's not specified how the optimal transport is performed for each channel, and what the ground metric is. The notation $\mathcal{L}_{d^P}$ is not standard and needs to be defined clearly, including the metric $d^P$ itself. The meaning of $\Sigma_n$ as a set of weights is not clear from the context, nor is the role of $\lambda_s$ as a specific weight within that set.
2) I feel confusing in Lines 339-350 regarding the number of epochs when the number of clients is small. In Lines 339-341, it seems to use a large number of epochs when P is small. But in Line 345 it seems to use a small number of epochs when P is small and in Line 349 it says that more agents less data. The relationship between the number of participating clients (P), the total number of clients (N), and the number of local epochs is not clearly explained. The text implies contradictory relationships, making it difficult to understand the experimental setup and its implications.
3) In Line 469, could you explain why "we do so with a model of fewer parameters"? The rationale behind using a smaller model in the experiments is not well-justified. It's unclear whether this choice was made for computational efficiency or if there's a specific reason related to the proposed method. The impact of model size on the results needs to be clarified.
4) it would be better if more experiments are presented where the preprocessing step pairs with more FL algorithms other than FedAvg. The evaluation is limited to FedAvg, which is a basic FL algorithm. It's unclear how the proposed preprocessing step would perform with more advanced FL algorithms, such as those incorporating momentum or adaptive learning rates. This limits the generalizability of the findings.
5) The exposition of the proposed preprocessing step is instantiated with image data which has RGB channels. What if other data is given? The method's reliance on channel-wise processing is a limitation. It's not clear how the method would be applied to data without a clear channel structure, such as time-series data or tabular data. The applicability of the method to diverse data types is not addressed.
6) This preprocessing step relies on a trusted central server for privacy, which doesn't seem like a rigorous privacy guarantee. The reliance on a trusted central server raises privacy concerns. The method does not provide any formal privacy guarantees, and the assumption of a trusted server is not always realistic in practical FL scenarios.

### Questions
see above

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel preprocessing step for federated learning that uses the tools of Optimal Transport. To summarize, it computes the Wasserstein barycenter of each client and collects them to compute a global barycenter. The clients then project local data to the global one in order to align the data with others. Experiments show significant improvement after the alignment compared with non-aligned baselines.

### Strengths
1. The author introduces a novel method using Optimal Transport to address the data heterogeneity in federated learning. 
2. The method is impressive overall and seems easy to apply to different FL methods.

### Weaknesses
1. Overall presentation is below average: Many of the notations in section 3.2 are not explained. Also, the authors should focus on the meaning and utility of OT, instead of the formula derivation. Section 4 is lack of description. The authors should explain the whole process in detail by bullet list or paragraphs with subtitles based on Figure 2,3.
2. Weak Experiments: The comparisons are mostly with non-aligned FL methods but only one (CCVR) baseline. More baselines should be included to demonstrate OT to be a good preprocessing step.

### Questions
1. Please clarify the concepts and notations mentioned in Weakness 1 above. For example, section 3.2 introduced OT, but how WB was calculated is still unclear.
2. As noted in Weakness 2, the author mainly chooses non-aligned FL methods as the baseline. Could other preprocessing methods, like simple regularization, be included in the comparison? If not, why are further comparisons unavailable?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose an optimal transport-based preprocessing step in federated learning to align datasets of different clients. This alignment step is run on each RGB color space separately using Wasserstein barycenters. After that, the datasets are projected toward the  target (aggregated) space. The authors show improvements over baselines empirically.

### Strengths
- The paper is well motivated and clearly written.

- As far as I know, use of optimal transport for domain alignment is novel in federated learning.

### Weaknesses
 - The paper mentions several times that the proposed preprocessing algorithm would preserve privacy. However, I could not find a clear definition of privacy notion the paper is referring to. Could the authors clarify what privacy notion they're targeting and how they compute/measure the privacy guarantees?

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes an optimal transport preprocessing step for federated learning in order to align the data distributions between the clients. The main idea is to treat the alignment as a hierarchical Wasserstein barycenters problem, where each client first summarizes their local data into an “average image” by computing a Wasserstein barycentre per image channel. These local barycenters are then communicated to the server, where new Wasserstein barycentres are computed across the local ones. These “global” barycenters are then communicated back to the clients and each one projects their data distribution onto them. After this preprocessing step, a standard federated learning algorithm such as FedAvg can be applied on top of these new input representations. The authors evaluate their method on CIFAR 10, showing improvements upon vanilla FedAvg and other baselines.

### Strengths
The main strength of this work is the simplicity of the proposed method. As it is a straightforward preprocessing step, it can be orthogonal to various other methods proposed for non-i.i.d. data in federated learning, potentially improving them even more.

### Weaknesses
I believe that this work has several axes for improvement.

# Clarity
There are quite a few instances where the manuscript is unclear and could be written better. More specifically:
- Important implementation details of the method are missing, i.e., what transport cost is used, what is the algorithm used for OT (e.g., is it Sinkhorn iterations?), what are its hyper parameters (if it is Sinkhorn iterations, what is the regularization parameter? This is important as it relates to the complexity analysis) and how is the projection to the global barycenters done. These need to be either in the main paper or in an appendix.
- The authors do not mention the dataset details in the experimental section (there is just a single mention of CIFAR-10 in the abstract) and what optimization hyper parameters where used for FedAvg. These are important for reproducibility and need to also be either in the main paper or the appendix.
- The notation in equations is a bit sloppy and needs to be improved. More specifically:
    - In Eq. 2 there is a $\sum_i$ but no index $i$ is present in the summand
    - Above Eq. 4 the definition of $(D^p_{i,j})_{i,j} \in R^{n\times n}$ is unclear; does this mean that each entry of the distance / cost matrix is itself an $n\times n$ matrix? Furthermore, there is a $diag(A) = 0$ introduced, but no mention of what $A$ is, and it is not clear what $\forall (i,j,k) [[n]]^3$ means and why it is important. 
    - After Eq. 5 the authors optimise the Wasserstein barycentre $a \in \Sigma_n$ but there is no mention of what $\Sigma_n$ is.  Also it seems that also $\lambda_s \in \Sigma_n$ later on (after Eq. 7) which is a bit counterintuitive as one is a vector and the other is a scalar. 
    - After Eq. 7 the authors mention $WB(B)$ but there is no mention of what $B$ is. 

# Evaluation
In my opinion, there are quite a few ways that the evaluation can be improved:
- There seems to be only one dataset (assuming CIFAR-10 from the abstract?) and architecture used. This is not enough to get a strong signal for the usefulness of this method. Other datasets (such as TinyImagenet and CIFAR 100) and architectures (such as ResNets and ViTs) are important to provide a broader picture. 
- It is not clear what the non-i.i.d.-ness is the data is. Uniform sampling without replacement should intuitively lead to more or less i.i.d. data across the clients, thus making OT-alignment not important. Prior works (such as McMahan et al. 2017) have more elaborate ways to generate non-i.i.d. data (by e.g., having each client only observe a subset of the classes). Furthermore, as the main premise of this work is domain alignment, I would also have expected a more elaborate evaluation of various non-i.i.d. settings, ranging from covariate shift (same $p(y)$ but different $p(x|y)$), to label skew (different $p(y)$ but same $p(x|y)$) or any mixture of the two. Intuitively, preprocessing the data should mainly help for the first setting as opposed to the second, so it would be beneficial if the authors update the manuscript with such cases. 
- The final performance improvement is a bit hard to believe. The authors argue that their OT alignment step leads to ~ +28% better accuracy on their dataset against vanilla FedAvg (which is a very big improvement). If we take this claim at face value, then this would imply that this small architecture gets SoTA on CIFAR-10 (if I compare it with results shown in https://paperswithcode.com/sota/image-classification-on-cifar-10 where a much larger/deeper ViT-H/14 model gets 99.5%), which is also a bit hard to believe. 

# Novelty
While the authors do discuss quite a few related works in the related work section, they unfortunately missed what seems to be a crucial related work, FedOT [1]. There the authors do also discuss about projecting the data distributions of each of the clients to a common space and they perform this step with optimal transport. Therefore, this weakens the novelty of this work.

### Questions
The questions stem from the prior discussion of the weaknesses of this work. To reiterate:

# Clarity
- The authors should elaborate and extensively discuss the implementation details of the their method. Questions such as what transport cost are important and relevant for reproduction.
- The notation should be improved upon, with clear explanation of symbols.

# Evaluation
- The authors should increase the breadth and depth of the evaluation of their method, especially given its simplicity. Some recommendations are
    - OT-alignment combined with other federated learning methods
    - Evaluation on other datasets and architectures
    - More involved client data distribution shifts and how OT alignment improves performance
    - Perhaps a visual interpretation of what the Wasserstein barycenters look like
    - Clarification of how such a big performance improvement is possible with OT alignment. Maybe a relevant baseline is FedAvg on i.i.d. data splits, as that would highlight what is the best possible performance of OT alignment. Furthermore, are the numbers of the other baselines discussed at Table 2 taken from the respective papers or reimplemented? This is important, as hyperparameter details (especially with how the data are partitioned between the clients) can have a big impact on model behaviour. 
    - The privacy claims are a bit vacuous, given that without formal privacy guarantees, FedAvg can break (e.g., see the work at [2]). I would encourage the authors to either substantiate the privacy claims (by e.g., an empirical evaluation) or removing them from the paper altogether. 

[2] Inverting Gradients — How easy is it to break privacy in federated learning? Geiping et al., 2020, https://arxiv.org/abs/2003.14053

### Soundness
1

### Presentation
1

### Contribution
2
