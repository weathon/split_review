# An Information Criterion for Controlled Disentanglement of Multimodal Data

- Decision: Accept
- Avg Score: 6.25
- Scores: 5, 8, 6, 6

## Abstract
Multimodal representation learning seeks to relate and decompose information inherent in multiple modalities. By disentangling modality-specific information from information that is shared across modalities, we can improve interpretability and robustness and enable downstream tasks such as the generation of counterfactual outcomes. Separating the two types of information is challenging since they are often deeply entangled in many real-world applications. We propose \textbf{Disentangled} \textbf{S}elf-\textbf{S}upervised \textbf{L}earning (\algo), a novel self-supervised approach for learning disentangled representations. We present a comprehensive analysis of the optimality of each disentangled representation, particularly focusing on the scenario not covered in prior work where the so-called \textit{Minimum Necessary Information} (MNI) point is not attainable. We demonstrate that \algo successfully learns shared and modality-specific features on multiple synthetic and real-world datasets and consistently outperforms baselines on various downstream tasks, including prediction tasks for vision-language data, as well as molecule-phenotype retrieval tasks for biological data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a self-supervised learning approach to disentangle shared and modality-specific information in multimodal data. The authors also explain that the optimal case in prior work is not doable based on Minimum Necessary Information (MNI), as the comprehensive analysis of the optimality. The experiments on vision-language and molecule-phenotype retrieval tasks demonstrate its effectiveness.

### Strengths
1. The paper presents a rigorous, information-theoretic framework for disentangling data for different domains and modalities under conditions where MNI is unattainable.

2. Based on the theoretical analysis, the authors designed a two-step training algorithm, and provided an optimality guarantee for this proposed method theoretically.

### Weaknesses
Weakness:
For the experiments on synthetic data, they only contain the data for unattainable MNI. The synthetic experiments for attainable MNI are also essential here to demonstrate the reliability of the theoretical bound. My suggestion is to add Gaussian noise produced by different variances as the degrees of MNI attainable or unattainable.


1. In Figure 4 (b), the superiority of DISENTANGLEDSSL is not significant compared to other baselines, such as JointOPT. The hyperparameter front of JointOPT is closer to the front of DISENTANGLEDSSL.

2. Table 1 shows the three versions of DISENTANGLEDSSL are unstable. For example, DISENTANGLEDSSL (shared) can achieve promising performance on MOSI while failing on MUSTARD. It would be better to explain why such a phenomenon exists, probably focusing on the main difference between these three versions and properties of multi-modal data. 

3. The performance gain shown in Table 2 is quite limited. Could the author explain if small improvements might be important in this domain? In addition, it would be better if the authors could provide the reason for this tiny improvement. 

4. The paper does not satisfy the page limitation.

### Questions
Please check the weakness section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
In this paper, the authors proposed a novel self-supervised representation learning method for multimodal representation learning. The proposed method disentangles the representation of multimodal information into shared information and modality-specific information, and uses a separate neural network to learn each representation. The authors supported their proposed method through extensive theoretical analysis and proofs. The proposed method was evaluated on both synthetic datasets and real-world multimodal datasets, where the proposed method achieved top performance over baselines in most tasks.

### Strengths
1. The paper introduces a new perspective in how to perform effective multimodal representation learning. Specifically, the paper demonstrated that disentanglement of modality-specific and shared information into 2 separate representations can be effective in improving downstream task performance, which seems to be original and novel.

2. The authors provided extensive theoretical justifications and proofs for their proposed approach.

3. The experiments are quite comprehensive. They include both synthetic and real-world datasets, and the proposed method is evaluated against several multimodal SSL baselines on different tasks from drastically different domains. The proposed method achieved top performance in almost all tasks.

4. All experiment details are presented in the Appendix (high reproducibility).

### Weaknesses
While the extensive use of information-theory notations allowed rigorous proof of the proposed approach, it isn't really easy for readers who isn't interested in the proofs and just want to learn about the concrete algorithm/methodology. Perhaps the authors should consider including a Pseudocode/Alg block either in the main text or in Appendix to clearly demonstrate the training process.

### Questions
Although in most cases DisentangledSSL-both achieves highest performance, there are also several tasks where either  DisentangledSSL-shared or  DisentangledSSL-specific alone achieves top performance (and sometimes by quite a large margin over  DisentangledSSL-both, such as Mustard). Do you observe any trend / suggest any guidelines for when it is best to use each configuration?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors believe that "shared information between modalities is precisely what is relevant for downstream tasks" and "the modality gap ... results in misalignment between modalities, restricting the application of these methods in numerous real-world multimodal scenarios." Hence they motivate "the need for a disentangled representation space that captures both shared and modality-specific information". To address this need, they propose DISENTANGLEDSSL, an information-theoretic framework designed to learn disentangled shared and modality-specific representations of multimodal data. The authors have conducted a theoretical analysis to evaluate the quality of disentanglement, which can be applied even in cases where Minimum Necessary Information (MNI) is unattainable. The efficacy of DISENTANGLEDSSL is demonstrated across a range of synthetic and real-world multimodal datasets and tasks, including prediction tasks for vision-language data and molecule-phenotype retrieval tasks for biological data.

### Strengths
It makes sense to learn disentangled shared and modality-specific representations of multimodal data. 

The theoretical analysis to evaluate the quality of disentanglement, which can be applied even in cases where Minimum Necessary Information (MNI) is unattainable, is provided.

The efficacy of DISENTANGLEDSSL is demonstrated across a range of synthetic and real-world multimodal datasets and tasks, including prediction tasks for vision-language data and molecule-phenotype retrieval tasks for biological data.

### Weaknesses
Some of the key assertions motivating this work are inaccurate, and the proposed graphical model is flawed, which together raise questions about the validity of the resulting framework.

For instance, the statement "shared information between modalities is precisely what is relevant for downstream tasks" is not universally accurate. What is relevant depends heavily on the specific downstream tasks. Furthermore, "shared information" is a vague term, especially when applied across modalities, making it problematic in this context. For example, in a vision-language task, the shared information might be high-level concepts, but the task might require fine-grained details unique to each modality. Consider a task that requires identifying the specific breed of a dog from an image and a textual description; the breed information might be considered 'shared', but the visual features (ear shape, fur pattern) and textual features (breed name, typical temperament) are modality-specific and crucial for the task. The paper does not adequately address how the framework handles such scenarios where modality-specific information is critical for task performance.

The assertion that "the modality gap ... results in misalignment between modalities, restricting the application of these methods in numerous real-world multimodal scenarios" is also oversimplified. The modality gap is not the sole or primary cause of misalignment; other factors such as alignment methods, distributional shifts, domain shifts, sampling biases, and more can contribute significantly. For example, even if the modality gap is minimized, a model trained on one dataset might fail on another due to distributional differences. The paper should acknowledge and discuss these other sources of misalignment, and how the proposed method might interact with them.

The graphical model in Figure 2, intended to represent the generative process (as claimed in line 128), has two major issues. First, the authors have conflated the generative and inference processes. Only the pathway from Z to X represents the generative model, while the path from X to \hat{Z} corresponds to inference, which should not be included in the data-generating graphical model. This issue is straightforward to resolve by removing the inference process from the model, which would not affect the algorithm or results, or to create separate diagrams, one for the generative process and the other for inference to clarify.

The second issue is more severe: the assumption of a shared latent variable Z_c existing between two modalities may not hold. This assumption lacks foundation, as it is more likely that the relationship takes the form of two variables Z_c^1 and Z_c^2, with potential connections between them:  (1)  Z_c^1 -> Z_c^2, (2)  Z_c^1 <- Z_c^2, or (3) or Z_c^1 <-C-> Z_c^2, depending on the modalities involved. This discrepancy significantly undermines the justification for the proposed algorithm. For instance, in a vision-language setting, the latent representation of an image and its corresponding text might not share a single common latent space but rather have distinct, albeit related, latent spaces. The paper should discuss the implications of using separate but potentially connected latent variables (Z_c^1 and Z_c^2) instead of a single shared Z_c, and how might this change affect the proposed algorithm and results. This could lead to a more nuanced and realistic model of multimodal relationships.

### Questions
Please respond to the weaknesses listed above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the disentanglement of modality-shared and modality-specific information in multi-modal self-supervised learning and proposes DisentangledSSL. From an information-theoretic perspective, the modality-shared information is optimized using a conditional entropy bottleneck (CEB). Correspondingly, the authors formulate an optimization problem to isolate modality-specific information. Theoretical analysis of the optimality of each disentangled representation, particularly when Minimum Necessary Information is unattainable, along with experimental results, demonstrates the superiority of DisentangledSSL.

### Strengths
1.The idea of applying conditional entropy bottleneck (CEB) in multi-modal self-supervised learning is novel.

2.Comprehensive theoretical analysis is conducted to prove the optimality of both modality-specific and modality-shared information.

3.DisentangledSSL demonstrates superior performance across tasks, including vision-language prediction and molecule-phenotype retrieval.

### Weaknesses
1.How does the optimization objective for the modality-shared representation change from Eq. (1) to Eq. (3)? Why is $I(X^1;X^2)$ omitted? The transition from the constrained optimization problem in Eq. (1) to the unconstrained form in Eq. (3) lacks sufficient explanation. Specifically, the justification for dropping the $I(X^1;X^2)$ term, which represents the mutual information between the two input modalities, is not clearly articulated. This omission needs further clarification, as it directly impacts the objective function being optimized. A more detailed explanation of how this term is treated as a constant with respect to the optimization variable $Z^1$ is necessary.

2.Related studies, such as CoCoNet [1] and SimMMDG [2], which also address the separation of modality-shared and modality-specific information, are recommended for inclusion and comparison. Note that SimMMDG [2] can be easily adapted to a self-supervised setting by substituting supervised contrastive learning with the original self-supervised counterpart. The current manuscript lacks a thorough comparison with existing methods that tackle similar problems. Specifically, CoCoNet [1] and SimMMDG [2] are highly relevant and should be discussed in detail, highlighting their differences and similarities with the proposed DisentangledSSL. Furthermore, an experimental comparison with SimMMDG, adapted to a self-supervised setting, would provide a more comprehensive evaluation of the proposed method's performance.

3.Ablation studies on the impact of $\beta$ and $\lambda$ in the MultiBench datasets should be provided to demonstrate the importance of separating modality-specific and modality-shared information in real-world applications. The manuscript lacks a detailed analysis of how the hyperparameters $\beta$ and $\lambda$ affect the performance of DisentangledSSL on real-world datasets such as those in MultiBench. Ablation studies are crucial to demonstrate the sensitivity of the method to these parameters and to validate the importance of disentangling modality-specific and modality-shared information in practical applications. Without these studies, the practical utility of the method remains unclear.

4.Some typos.
1)$Z^2$ should be $X^2$ in Eq.(6) and in the equation below Eq.(6).
2)$I(X^1;Z^1)$ should be $I(X^1;X^2)$ in Figure 3.

### Questions
Are there any alternative approaches for implementing the $I(Z^1;\hat{Z}_{c}^{1*})$ in $L_s^1$? If so, how does their performance compare to that of the orthogonal loss implementation?

### Soundness
4

### Presentation
3

### Contribution
4
