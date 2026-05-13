# CFD: Learning Generalized Molecular Representation via Concept-Enhanced Feedback Disentanglement

- Decision: Accept
- Scores: 6, 6, 8, 6

## Abstract
To accelerate biochemical research, e.g., drug and protein discovery, molecular representation learning (MRL) has attracted much attention. However, most existing methods follow the closed-set assumption that training and testing data share identical distribution, which limits their generalization abilities in out-of-distribution (OOD) cases. In this paper, we explore designing a new disentangled mechanism for learning generalized molecular representation that exhibits robustness against distribution shifts. And an approach of Concept-Enhanced Feedback Disentanglement (CFD) is proposed, whose goal is to exploit the feedback mechanism to learn distribution-agnostic representation. Specifically, we first propose two dedicated variational encoders to separately decompose distribution-agnostic and spurious features. Then, a set of molecule-aware concepts are tapped to focus on invariant substructure characteristics. By fusing these concepts into the disentangled distribution-agnostic features, the generalization ability of the learned molecular representation could be further enhanced. Next, we execute iteratively the disentangled operations based on a feedback received from the previous output. Finally, based on the outputs of multiple feedback iterations, we construct a self-supervised objective to promote the variational encoders to possess the disentangled capability. In the experiments, our method is verified on multiple real-world molecular datasets. The significant performance gains over state-of-the-art baselines demonstrate that our method can effectively disentangle generalized molecular representation in the presence of various distribution shifts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper, titled "CFD: Learning Generalized Molecular Representation via Concept-Enhanced Feedback Disentanglement," addresses the challenge of out-of-distribution (OOD) generalization in molecular representation learning. The proposed approach, called Concept-Enhanced Feedback Disentanglement (CFD), aims to enhance the robustness of molecular representations against distribution shifts. CFD incorporates a novel feedback mechanism and a concept mining module to disentangle molecular representations into distribution-agnostic generalized features and spurious features.

The method uses two dedicated variational encoders: one to extract invariant (distribution-agnostic) features and the other for spurious features. A set of molecule-aware concepts is introduced to capture critical substructures. The iterative feedback mechanism allows multiple stages of representation disentanglement, progressively refining the generalized features over iterations. The approach also utilizes a self-supervised objective to further enhance the disentangling process, making it effective in capturing important molecular substructures.

Extensive experiments conducted on multiple real-world datasets, including GOOD and DrugOOD, demonstrate the proposed method’s superior OOD generalization performance compared to state-of-the-art baselines. CFD shows significant improvements, particularly in tasks involving distribution shifts related to scaffold and molecule size, as well as in predicting molecular ground-state conformations. The paper positions its contribution as a robust solution to learn generalized molecular representations that perform well under diverse distribution conditions.

### Strengths
The proposed Concept-Enhanced Feedback Disentanglement (CFD) introduces an iterative feedback mechanism that allows for progressively refining the disentangled representations across multiple iterations. This is a novel application within the molecular representation domain and effectively addresses a significant challenge in learning generalized representations—namely, how to handle complex structures and high variability in molecular data. This feedback mechanism enables the model to overcome the limitations of traditional one-step disentanglement methods, which often fail for biomacromolecules or other complex molecular structures.

The integration of concept mining to identify invariant substructures is a key strength. By incorporating domain-relevant substructures into the generalized features, CFD not only enhances the model's generalization ability but also improves interpretability. This combination of disentanglement and concept-aware enhancement represents a thoughtful fusion of representation learning techniques, where each step complements the other to strengthen the robustness of the final representation.

### Weaknesses
There is insufficient analysis to quantify the specific contribution of this feedback mechanism compared to a one-step or non-feedback approach. Although there are qualitative claims about the benefits of the iterative process, including an ablation study that explicitly compares different iteration counts or contrasts the feedback approach against standard one-step disentanglement would be crucial to substantiate the claims regarding its effectiveness. Such analysis would provide a clearer understanding of when and how the feedback mechanism truly enhances generalization, particularly in the presence of highly complex molecular structures.

The paper does not explore how well the learned representations generalize to domains outside of those used for training. Given the emphasis on out-of-distribution generalization, it would be beneficial to evaluate CFD's effectiveness across other molecular tasks beyond those in the current dataset, such as predicting drug toxicity or protein-ligand binding affinity, which require different structural knowledge.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a concept-enhanced disentanglement feedback mechanism for molecular representation learning. The authors innovatively introduce the feedback mechanism to learn distribution-agnostic representation and validate the method’s effectiveness through comprehensive experimental evaluations.

### Strengths
1. Extensive evaluation across multiple datasets demonstrates the method’s robustness and generalizability.
2. The method achieves strong results on both classification and regression tasks, indicating its versatility.

### Weaknesses
1. Missing details: Some critical details are insufficiently explained. For instance, how are $\mu_c$ and $\sigma_c$ of the concept learned? What is the motivation for the residual term? How does the residual operation assigns molecular substructure features to the corresponding concept. Also, the invariance mentioned in Eq.1 lacks further explanation of the association with the methodology herein.
2. Limited in-depth analysis: The effectiveness of KAN needs further comparison with other methods. It's essential to include ablation studies to explore the sensitivity of the proposed method to variations in this hyper-parameter.
3. High computational complexity: In the feedback disentanglement iterations, each step treats disentangled features as independent feature. However, there may be overlaps among these features. And concatenating the disentangled features from each iteration step can lead to dimensional growth, introducing high redundancy.
4. Unclear motivation: The rationale behind the disentanglement and subsequent concatenation approach is not fully substantiated. It remains unclear whether this method effectively demonstrates decoupling, as no concrete evidence is provided. The multi-step disentanglement process may still retain spurious correlations, and the concatenation of these features may not lead to a truly invariant representation. The authors should provide a comparison experiment that considers only the features from the final step of disentanglement.

### Questions
1. How is the environment $e$ in Eq. 1 obtained? Does it require spurious labels?
2. Does “concept” represent the environment  in Eq. 1? Are $f(·)$ in Eq. 1 and $\varphi(·)$ in Line 305 the same?
3. In Line 251-252: “we explore mining a series of concepts that do not specialize to one particular type or class of molecule.” What does that mean?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
(1) The article presents an iterative model based on an encoding-then-separation scheme, designed to be robust against distribution shifts.

(2) The model employs a concept-mining module that focuses on critical substructures with invariant characteristics, aiming for superior performance on out-of-distribution (OOD) data.

(3)The authors conducted experiments on a diverse set of real-world molecular datasets, demonstrating significant performance gains over multiple baselines. Additionally, they evaluated the model on an unseen task, proving its effectiveness.

Although there are some curiosities about the algorithm, overall it seems to be novel and effective for representation learning for molecules.

### Strengths
(1) The method is novel and has demonstrated superiority over conventional models.

(2) The method also performs well on out-of-distribution (OOD) data prediction tasks.

### Weaknesses
(1) The algorithm appears somewhat complicated. --> Question (2)

(2) It is unclear how the contrastive loss contributes to the usefulness of the general latent representations, as it only enforces similarity between the GNN latent vector and the general latent vectors. --> Question (1), (3) and (4)

(3) The model is complex and iterative, suggesting it may consume a significant amount of computational power. However, no analysis of this aspect has been conducted. --> Question (5)

### Questions
(1) In the contrastive loss, the first term aims to maximize the similarity between the latent representations of the general encoder and the GNN encoder initially. However, given that there is no direct link between the GNN latent space and downstream tasks, it is unclear how the authors ensure that this high similarity will make the general embedding latent useful in the end.

(2) Why is KAN used instead of conventional deep learning models? The article states:

"Unlike MLPs, which have fixed activation functions on neurons, KANs feature learnable activation functions (Liu et al., 2024), which enhances the flexibility of the learned concepts."

But what is the specific rationale behind this choice?

(3) The molecular concept is a critical factor in the algorithm. Are there experiments, such as visualizations, that examine the importance of this concept across iterations?

(4) Is there any analysis involving a decoder to determine if the molecular concept aligns with known scaffolds for the input molecules?

(5) The algorithm appears rather complex. Is there any analysis of the computational costs for training and inference?

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
This article introduces a "First-Encoding-Then-Separation" paradigm-based framework for out-of-distribution (OOD) molecular representation learning. The authors have designed an iterative disentanglement module that utilizes a feedback mechanism to gradually decompose molecular representations into spurious features and invariant features. The effectiveness of the proposed framework has been validated by the authors across multiple datasets and various tasks.

### Strengths
- The writing is clear, and the paper is easy to follow.
- The experimental results are very comprehensive, with ample ablation studies demonstrating the effectiveness of each module. There is also an exploration of the impact of various hyperparameters on the model.

### Weaknesses
 - The article lacks chemical interpretability or inspiration. The methodology presented could be generalized to any graph-based out-of-distribution generalization problem, but the authors have limited the scope of the paper to molecular representation learning. Specifically, the learned concepts are not tied to any established chemical principles or properties. For instance, the concepts do not seem to correlate with known molecular features like polarity, hydrogen bonding capacity, or specific functional groups, which are crucial for understanding molecular behavior. This lack of connection to chemical reality makes the method less insightful for chemists and limits its practical applicability in drug discovery or materials science.
- One of the core contributions of this article, concept mining, shows a high degree of similarity to the idea in another paper. See questions for details.
- The article lacks theoretical support. See questions for details.

### Questions
1. Could the authors elaborate on the distinction between the Concept Mining presented in this work and the Residual Vector Quantization found in iMoLD[1]? The Concept Mining in this work appears to be simply a weighted sum of the vectors from the codebook of iMoLD.
2. Could the authors supplement the manuscript with a proof analogous to the proofs of Theorem 1 and Theorem 2 in MoleOOD[2], demonstrating that minimizing the loss function presented in this article can help the model acquire invariant features capable of providing sufficient predictive power across various environments?
3. Could the author clarify why the baselines CIGA, DisC, and CAL fail to adapt on the datasets GOOD-ZINC and GOOD-PCBA?

### Soundness
2

### Presentation
4

### Contribution
3
