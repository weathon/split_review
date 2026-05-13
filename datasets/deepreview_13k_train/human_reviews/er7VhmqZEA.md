# NOISY MULTI-VIEW CONTRASTIVE LEARNING FRAMEWORK FOR ENHANCING TOP-K RECOMMENDATION

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
Recommender systems have become an essential component of various online plat-
forms, providing personalized recommendations to users. Collaborative filtering-
based methods, such as matrix factorization, have been widely used to capture
latent user-item preferences. Recently, graph-based methods have shown promising
results by modeling the interactions between users and items as a graph and lever-
aging knowledge graphs (KG) to learn the user and item embeddings. Motivated
by the recent success of contrastive learning in mining supervised signals from data
itself, in this paper, we focus on establishing a noisy contrastive learning framework
in Knowledge-aware recommendation systems and propose a self-supervised novel
noisy multi-view contrastive learning framework for improving top-K recommen-
dation. In this paper, we propose a novel recommendation system architecture that
generates three different views of user-item interactions for improved recommenda-
tion along with a noise addition module. The global-level structural view leverages
attention-based aggregation network Wang et al. (2019d) to capture collaborative
information in the entity-item-user graph. In the item-item semantic view, we
use a K-nearest Neighbour item-item semantic module to incorporate semantic
relations among items. In the local view, we apply LightGCN He et al. (2020)
with noisy perturbations to generate robust user-item representations. We then use
two more signals such as representation loss and uniformity loss in positive pairs
to improve the quality of the representations and ensure uniform representations
in the representational space. Experimental results on two benchmark datasets
demonstrate that our proposed method achieves superior performance compared
to state-of-the-art methods. Additionally, we conducted extensive experiments
on CTR task-based datasets to demonstrate the robustness of our framework’s
generalization in learning better user-item representations which can be seen in the
supplementary material. All the codes to generate reproducible results are available
in this anonymous repository.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to utilize multi-view contrastive learning to enhance the recommender system. The proposed model based on self-supervised learning can aggregate the information from item knowledge graph, item similarity and historic records. Extensive experiments verify the effectiveness of the proposed model.

### Strengths
1.	The writing quality of this paper is high.
2.	This paper introduces a novel contrastive learning model to enhance the CTR recommendation task.

### Weaknesses
1.	This paper lacks theoretical analysis to clarify how each contrastive learning module benefits the final CTR task.
2.	It would be beneficial to test the proposed model in various datasets across different domains, not just in the movie domain.
3.	A comprehensive ablation study is necessary to clarify the effectiveness of each proposed module, including the contrastive module and the feature alignment module.
4.	There is a citation format error below Equation (2): "Inspired by SimGCL (simgcl) and Noisytune wu2022noisytune papers' additions."

### Questions
See weaknesses.

### Soundness
2 fair

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
This paper presents a novel Noisy Multi-view Contrastive Learning framework for Knowledge-aware recommender systems (NMCLK). NMCLK generates three different views over user-item interactions and knowledge graphs, and further introduces a noise addition module to improve model robustness. The three views include a global-level structural view, a local-level user-item view, and an item-item semantic view. NMCLK also utilizes representation loss and uniformity loss to enhance the quality of the learned user-item representations. Experimental results on two movie recommendation datasets demonstrate that the proposed method outperforms state-of-the-art approaches.

### Strengths
- NMCLK is able to outperform a number of baseline approaches on two movie recommendation datasets.

### Weaknesses
- The novelty of the paper is limited. The authors should derive more insights in the alignment and uniformity constraints in contrastive learning, and maybe design a better contrastive module.
- The design choice of the contrastive module is not explained. In addition, the readers cannot know how and why the multi-view framework works, and cannot see the performance improvement after using the multi-view framework.
- The model is only evaluated on NMCLK on two movie recommendation datasets, and it is questionable whether the performance of NMCLK will generalize to other recommendation domains.
- No ablation study is conducted to verify the effectiveness of the introduced modules, e.g., the noise module and the contrastive learning module.

### Questions
- wu2022noisytune and simgcl are not properly cited.
- Section 5.1.1 says "Table 1 displays the statistics of the three datasets mentioned above", while only two datasets are used.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript proposes to use contrastive learning for enhancing top-k recommendation. Alignment and uniformity constraint module are introduced to both the global and local parts. Experimental results on two datasets show that the proposed NMCLK outperforms previous methods.

### Strengths
This paper is written clearly and easily understandable.
The experimental results seem to be good on two datasets.

### Weaknesses
The main contribution of this manuscript is introducing self-supervised learning methods which are commonly used in CV and NLP to the recommendation field. I think the novelty is not enough for an ICLR paper.
The contrastive learning is to make features from the same field similar and in contrast, with large distances for disparate ones. Is that always true in recommendation?
The ablation studies are not convincing, the authors should conduct experiments with and without each proposed component.

### Questions
See the weakness part.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To improve the data sparsity issue, this paper proposes a multi-view contrastive learning framework for knowledge-aware recommendation. The proposed model generates multiple modeling views including a collaborative view, a semantic view, and a structural view. The three views are constructed by utilizing part of the heterogeneous data combining the user-item interaction information and the item-entity knowledge information. Then two contrastive learning losses, and an alignment and uniformity loss is applied for supervision enhancement. Experiments on ML-100K and ML-1M validate the effectiveness of the proposed approach.

### Strengths
- Clear presentation. The paper is well-writen with good illustration figures. The introduction clearly highlights the major research motivation and key contributions of this paper. And it has a clear structure to introduce the view generation part and the contrastive learning part, respectively. I find it easy to follow.
- Important research topic. The paper targets an important research topic, namely self-supervised learning for knowledge-aware recommender systems.
- Technical design. The contrastive learning method adopted in this paper is conducted from multiple dimensions, including the cross-view contrastive learning, and the alignment and uniformity constraints.

### Weaknesses
- Limited novelty. There have already been some self-supervised learning approaches proposed for knowledge-aware recommendation (e.g. KGCL [1], KGIC [2], KACL [3]). In terms of view generation and contrastive constraints, this paper does not make sufficiently innovative contribution to this topic compared to the existing works.
- Insufficient experiments. i) The empirical study is conducted on two small-size datasets that are not aligned with the recent studies on knowledge-aware recommendation. ii) The paper does not involve the existing contrastive KG recommendation methods as baselines. iii) There is only the overall performance comparison. There lack other experiments such as ablation study, hyperparameter study, anti-noise investigation, for a comprehensive empirical study.
- Important part of methodology is not clearly explained. I cannot find the specific definitions for some of the self-supervised learning loss terms, such as $\mathcal{L}_u^g$, $\mathcal{L}_i^g$, $\mathcal{L}_u^l$, $\mathcal{L}_i^l$, and $L_{local}$. Please correct me if I am wrong.

Minor mistakes: 
- In the task formulation section, there should be braces in the definitions for user/item sets, the knowledge graph, and so on.
- LightGCN is the original model name. Adding a hyphen in the name (Light-GCN) may cause confusion. If the used GCN architecture is not exactly LightGCN, using other expressions like light-weight GCN would be better.
- The paper utilizes $\mathcal{L}$ for loss terms in most cases, but sometimes $L$ is used. The notations could be better if unified.
- Typo: "This results ..." in page 5

[1] Knowledge Graph Contrastive Learning for Recommendation

[2] Improving Knowledge-aware Recommendation with Multi-level Interactive Contrastive Learning

[3] Knowledge-Adaptive Contrastive Learning for Recommendation

### Questions
- What are the major improvements brought by the proposed method, in comparison to the existing CL methods for KG recommendation listed above?
- How to calculate the CL loss terms in detail?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
