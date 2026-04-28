# Graph Inference Acceleration by Bridging GNNs and MLPs with Self-Supervised Learning

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 3, 6, 3, 5

## Abstract
Graph Neural Networks (GNNs) have demonstrated their effectiveness in a variety of graph learning tasks such as node classification and link prediction. However, GNN inference mainly relies on neighborhood aggregation, which limits the deployment in latency-sensitive (i.e., real-time) applications such as financial fraud detection. To solve this problem, recent works have proposed to distill knowledge from teacher GNNs to student Multi-Layer Perceptrons (MLPs) trained on node content for inference acceleration. Despite the progress, these studies still suffer insufficient exploration of structural information when inferring unseen nodes. To address this issue, we propose a new method (namely {\bf SSL-GM}) to fully integrate rich structural information into MLPs by bridging \textbf{G}NNs and \textbf{M}LPs with Self-Supervised Learning (\textbf{SSL}) for graph inference acceleration while improving model generalization capability. A key new insight of SSL-GM is that, without fetching their neighborhoods, the structural information of unseen nodes can be inferred solely from the nodes themselves with SSL. Specifically, SSL-GM employs self-supervised contrastive learning to align the representations encoded by graph context-aware GNNs and neighborhood dependency-free MLPs, fully integrating the structural information into MLPs. In particular, SSL-GM approximates the representations of GNNs using a non-parametric aggregator to avoid potential model collapse and exploits augmentation to facilitate the training; additionally, SSL-GM further incorporates reconstruction regulation to prevent representation shift caused by augmentation. Theoretically, we interpret our proposed SSL-GM through the principle of information bottleneck, demonstrating its generalization capability; we also analyze model capacity in incorporating structural information from the perspective of mutual information maximization and graph smoothness. Empirically, we demonstrate the superiority of SSL-GM over existing state-of-the-art models in both efficiency and effectiveness. In particular, SSL-GM obtains significant performance gains {\bf (7$\sim$26\%)} in comparison to MLPs, and a remarkable acceleration of GNNs {\bf (90$\sim$126$\times$)} on large-scale graph datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new method called SSL-GM, which integrates structural information into MLPs by connecting GNNs and MLPs using SSL. This method can accelerate graph inference and improve the generalization capability, resulting in a favorable balance between accuracy and inference time. Experimental results show that the method performs well in node classification tasks and is effective in accelerating inference. In addition, many theoretical analyses and corresponding experiments flesh out the work.

### Strengths
1. This paper propose a new method, which can accelerate GNN inference and performs well in node classification tasks over the state-of-art models.
2. There are detailed theoretical analyses and corresponding experiments of SSL-GM ,which fleshes out the article and provides inspiration for the innovations that follow.
3. This work has comprehensive and detailed experiments, which validates the performance and efficiency of SSL-GM.

### Weaknesses
1. The article lacks sufficient innovation and is merely a combination and application of existing methods, such as Bootstrap loss, SGC, graph augmentation, and reconstruction. The novelty of combining these techniques is not sufficiently justified, and the paper does not clearly articulate why this specific combination is superior to other possible combinations or existing approaches. The paper should provide a more in-depth discussion of the limitations of the existing methods and how the proposed combination specifically addresses these limitations, rather than simply presenting a collection of existing techniques.
2. In section 4.3, there is only 'Figure 3' to demonstrate the capability of SSL-GM for inference acceleration. However, it is necessary to provide detailed experimental results regarding accuracy and inference time. These results should be obtained from a wider range of datasets and classification settings. The current presentation lacks sufficient quantitative evidence to support the claim of inference acceleration, and the lack of detailed results makes it difficult to assess the practical significance of the proposed method. The paper should include tables with specific values for accuracy and inference time, and these results should be presented across diverse datasets and classification tasks to demonstrate the generalizability of the method.
3. In section 3.3, it would be better to introduce representation shift in detail and explain how reconstruction helps in mitigating representation shift.  The explanation of representation shift is currently too high-level and lacks a concrete discussion of how data augmentation leads to changes in the learned representations. Furthermore, the paper does not provide a clear explanation of how the reconstruction regularizer specifically addresses the issue of representation shift. A more detailed explanation, possibly with a mathematical formulation, is necessary to clarify the underlying mechanism and justify the use of the reconstruction regularizer.

### Questions
1. Although this work is a combination of existing methods, it is fascinating to introduce this model from a higher level rather than loss function level. 
2. In B.3, learning rates is misspelled where ‘5e4’ appears twice.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of Graph inference acceleration and summarizes two shortcomings in existing work: limited acceleration effectiveness and insufficient generalization performance. Based on insights from existing work, it is suggested that self-supervised learning can be used to infer structural information of unseen nodes from the nodes themselves. The paper introduces the SSL-GM algorithm, primarily aligning the consistency between GNN and MLP representations through self-supervised contrastive learning. This bridges GNN and MLP with self-supervised learning to achieve accelerated graph inference.

### Strengths
1. The problem is novel, the challenge of accelerating graph inference still persists.
2. The proposed algorithm demonstrates favorable performance in multiple experimental validations.

### Weaknesses
1. Although a significant number of experiments were conducted, the novelty and contribution of the proposed method remain limited.
2. In Section 3.1, the author introduces the Non-Parametric Aggregator to help align the representations of GNN and MLP. While the author explains the differences in the appendix, the aggregation method given in Equation 2 still resemble the form of APPNP. I did not find an explanation for this issue in the experimental section and other where of the paper. The author claims that, in contrast to SGC and APPNP, SSL-GM uses non-linear adjacency matrix aggregation instead of high-order adjacency matrices. So, from the perspective of acceleration effectiveness and improvement in generalization, what is the contribution of non-linear adjacency matrix aggregation to accelerating graph inference?
3. I cannot understand Formula 4. The author injects randomness by perturbing the structure and features of the original graph, with the expectation that the MLP encoder can capture invariant key features. However, Formula 4 is perplexing. The first part of the formula computes the mutual information between G_1 and G_2, but is it merely a distinction of whether the perturbed structure is included? Why does this part enable the encoder to obtain high-quality representations? It seems more like an optimization of the random augmentation methods q_e and q_f, but the author did not clarify whether they are learnable.
4. Given the method proposed in the paper, I believe it would be interesting to include GNN methods like SGC and APPNP in the experiments concerning acceleration effectiveness.

### Questions
Please see the comments in the weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies an important problem: how to accelerate graph inference and improve model generalization. For this paper, the authors propose SSL-GM to bridge graph context-aware GNNs and neighborhood dependency-free MLPs with SSL. In addition, the authors also provide theoretical analysis to prove the generalization capability of SSL-GM. Furthermore, the extensive experimental results show that the solution mentioned in this paper not only accelerates GNN inference but also exhibits significant performance improvements over vanilla MLPs.

### Strengths
1. The problem studied in this paper is fundamental in the graph neural network area.
2. The solution mentioned in this paper is basic and the performance of the method mentioned in this paper is great. The experimental results are extensive.
3. This paper develops a theoretical analysis.
4. The presentation of this paper is so clear that I can follow the paper easily.

### Weaknesses
1. The experimental results only contain the performance over node classification and graph classification. Is it possible to evaluate the proposed method over link prediction?
2. It seems that this paper only borrows some ideas from contrastive learning. Based on contrastive learning, this paper develops a new objective function that can be used to solve the model generalization problem. Therefore, could the authors highlight some contributions here? I think it is a good paper but the contribution of this paper is a little bit marginal. If the authors are able to emphasize their contributions here, I am willing to improve my rate.

### Questions
See Strengths and Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of accelerating GNN inference by training an MLP on the node features. It proposes to use self-supervised learning to train the MLP and achieves strong empirical results.

### Strengths
1.	The paper is well-written and easy to follow.
2.	The empirical results are rich and significantly outperform the baselines.

### Weaknesses
1.  Theorem 1 is possibly wrong. I check the proof in the appendix, which basically connects each term in (17) to each term in (13) and leads to two problems. (1) The authors seem that minimizing each term in (17) also minimizes the corresponding term in (13). Pls prove these conclusions rigorously instead of only using intuitively explanations. Specifically, the connection between minimizing the entropy terms in (17) and the norm and covariance terms in (13) is not rigorously established. The authors need to explicitly state any assumptions about the data distribution for these transformations to hold. For instance, if Gaussian distributions are assumed, this should be clearly stated and justified. (2) Even if the first point holds, (13) minimizes the summarization of 4 terms, and thus the minimizer may not be the minimizers of the 4 terms. Thus, there is no guarantee that (13) and (17) will have the same minimizer. Nowadays, many machine learning papers have theorems but my opinion is that theorems should be rigorous. Moreover, I failed to follow the mutual information part of Section 5, especially how the authors transform different models into mutual information forms. If this can be done, pls conduct the mathematical transformations in rigorous ways. The transformations from cross-entropy to mutual information for different models lack detailed mathematical derivations. The authors should provide step-by-step transformations, clearly showing how the mutual information terms are derived for each model (MLP, GNN, GLNN, NOSMOG, GENN, and their proposed SSL-GM). The current explanation is too high-level and lacks the necessary mathematical rigor.
2.  It is unclear what are the challenges of using self-supervised learning (SSL) to train MLP and what are the new designs of the paper. SSL is widely used for graph learning, and the author should be very specific in the challenges of using it to train MLP. Currently, descriptions of the weak points of existing works, e.g., “insufficient exploration of structural information when inferring unseen nodes”, “cannot fully model the structural information” are rather vague. In section 3, the authors propose several techniques and loss terms, e.g., alignment loss, data augmentation, and reconstruction loss. These are not new for SSL, which are also evidenced by the citations provided by the authors. The question is that what are the new things proposed by the authors. The paper will be stronger if the authors can connect the challenges and the proposed new techniques. The authors need to clearly articulate the specific challenges in applying SSL to train MLPs for graph data, beyond the general limitations of existing methods. They should detail how their approach addresses these challenges, rather than just stating that existing methods are insufficient. The novelty of the proposed techniques (alignment loss, data augmentation, reconstruction loss) needs to be explicitly justified in the context of training MLPs with SSL for graph data, highlighting what makes their approach different from standard SSL techniques.
3.  Experiments can be improved. (1) Pls provide the time for model training, which is also an important practical consideration. (2) Pls run the experiments on large practical datasets, e.g., Papers100M, MAG240M, and IGB.

### Questions
NA

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a novel method, SSL-GM, for graph inference acceleration. The primary idea is to bridge GNNs and Multi-Layer Perceptrons (MLPs) through Self-Supervised Learning (SSL) to integrate structural information into MLPs. SSL-GM employs self-supervised contrastive learning to align the representations of GNNs and MLPs. Besides, it uses non-parametric aggregation, augmentation, and reconstruction regulation to avoid potential model collapse, improve model training, and prevent representation shift, respectively. The extensive experiments demonstrate SSL-GM's empirical superiority over existing models in terms of both efficiency and effectiveness.

### Strengths
* It introduces a novel approach, SSL-GM, which integrates structural information into MLPs by contrastive learning between GNN and MLP outputs.
* The empirical results over 10 datasets demonstrate the effectiveness of SSL-GM.
* The paper is well-written and structured, with clear explanations of the methodology and theoretical insights.

### Weaknesses
 * In this paper, the structure-aware ability of SSL-GM is supported by the objective $\mathcal{L}_{cont}$. However, its success depends on the quality of the learned representations from the GNN, rather than solely on the capabilities of the student MLP. In other words, $\mathcal{L}{cont}$ enforces the student MLP to output representations similar to the aggregated representations from the GNN but does not inherently empower the student with structure-aware abilities. For unseen nodes during training, the student MLP may encounter challenges in learning structure-aware representations without the supervision provided by the GNN.
* It's worth considering whether addressing the representation shift issue is necessary. The absence of the reconstruction strategy only leads to a slight decrease in performance (as shown in Table 1, "w/o Rec." column), indicating that this strategy may not be indispensable in some cases. Furthermore, the performance drop is not consistent across datasets, suggesting that the necessity of this component is highly dependent on the specific graph structure and characteristics. For example, the performance difference on Cora is minimal, while it is more pronounced on Arxiv.
* To enhance reproducibility and ensure accurate results, it would be helpful if the authors could provide detailed information about the experimental environment used for SSL-GM.  I used the Google Colab platform to rerun the source code but obtained $83.80_{\pm0.46}$ in the Cora dataset compared to  $84.60_{\pm0.24}$ in the paper. This discrepancy raises concerns about the reproducibility of the results and the potential impact of environmental factors on the model's performance. The lack of specific details about the hardware, software versions, and random seeds used in the original experiments makes it difficult to pinpoint the source of the difference.

### Questions
Please refer to the Weaknesses section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
