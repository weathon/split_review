# Adversarially Robust Out-of-Distribution Detection Using Lyapunov-Stabilized Embeddings

- Decision: Accept
- Scores: 8, 6, 5, 6

## Abstract
Despite significant advancements in out-of-distribution (OOD) detection, existing methods still struggle to maintain robustness against adversarial attacks, compromising their reliability in critical real-world applications. Previous studies have attempted to address this challenge by exposing detectors to auxiliary OOD datasets alongside adversarial training. However, the increased data complexity inherent in adversarial training, and the myriad of ways that OOD samples can arise during testing, often prevent these approaches from establishing robust decision boundaries. To address these limitations, we propose AROS, a novel approach leveraging neural ordinary differential equations (NODEs) with Lyapunov stability theorem in order to obtain robust embeddings for OOD detection.
By incorporating a tailored loss function, we apply Lyapunov stability theory to ensure that both in-distribution (ID) and OOD data converge to stable equilibrium points within the dynamical system. 
This approach encourages any perturbed input to return to its stable equilibrium, thereby enhancing the model’s robustness against adversarial perturbations. 
To not use additional data, we generate fake OOD embeddings by sampling from low-likelihood regions of the ID data feature space, approximating the boundaries where OOD data are likely to reside. To then further enhance robustness, we propose the use of an orthogonal binary layer following the stable feature space, which maximizes the separation between the equilibrium points of ID and OOD samples. We validate our method through extensive experiments across several benchmarks, demonstrating superior performance, particularly under adversarial attacks. Notably, our approach improves robust detection performance from 37.8\% to \textbf{80.1\%} on CIFAR-10 vs. CIFAR-100 and from 29.0\% to \textbf{67.0\%} on CIFAR-100 vs. CIFAR-10.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a new out-of-distribution detector that is robust against adversarial attacks. Specifically, the authors point out the problems of adversarial training with auxiliary datasets and propose a novel approach based on neural ordinary differential equation (ODE) and Lyapunov stability. The authors force the neural ODE model’s dynamical system to have stable equilibrium points on both in-distribution (ID) and out-of-distribution (OOD) samples. The authors also present a theoretical background that supports the proposed method. With experiments, the authors present the performance of the proposed method and some ablation studies.

### Strengths
1. The proposed method's theoretical background is solid, and the main trick (i.e., the Levy-Desplanques Theorem) seems useful for other neural ODE models.
2. With an orthogonal layer, the authors effectively overcame practical problems, such as exploding gradients and vanishing gradients.
3. The experiments are well done. The authors used very strong attacks and many baseline models to compare. The proposed method's performance is really impressive.

### Weaknesses
1. The proposed method generates fake OOD data in the embedding space, which might expose other vulnerabilities in ID embedding extraction. For example, the adversary can try poisoning the training ID data by injecting OOD samples so that the crafted OOD data does not include those injected OOD samples. This could lead to a scenario where the model is robust against the generated OOD samples but vulnerable to real, poisoned OOD samples.
2. If I understand correctly, the fake OOD embedding is sampled from the low-likelihood space. This makes sense because OOD samples will be embedded in the low-likelihood part. However, this could be an ineffective method to generate embeddings of “realistic” OOD samples because even random noise would be mapped to the low-likelihood part. The method does not guarantee that the generated OOD samples will resemble real-world OOD data, potentially limiting its effectiveness in practical scenarios. Furthermore, the low-likelihood space might be too broad, leading to the generation of OOD samples that are not challenging enough for the model.

### Questions
1. I’m curious about the sampling methods. Do you have some justification that the low-likelihood part would represent the embeddings of the realistic OOD samples, or do you just not care about the realisticness of the embeddings?

### Soundness
4

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
This paper introduces a novel adversarially robust out-of-distribution (OOD) detection method, AROS, which leverages Neural Ordinary Differential Equations (NODE) and Lyapunov stability theory to enhance model stability against adversarial perturbations. AROS employs a pseudo-OOD data generation strategy, sampling low-likelihood regions in the embedding space to create pseudo-OOD samples, thereby improving the model's generalization capability. Additionally, it incorporates an orthogonal binary layer to strengthen the separation between in-distribution (ID) and OOD samples. Experiments on CIFAR-10, CIFAR-100, and ImageNet-1k demonstrate that AROS maintains high detection accuracy across various attacks, including strong adversarial PGD and adaptive AutoAttack. Ablation studies indicate that Lyapunov stability regularization and pseudo-OOD embedding generation are particularly important for enhancing robustness.

### Strengths
1. The paper proposes an OOD detection method based on Lyapunov stability and NODE, representing an innovative attempt to integrate control theory with OOD detection to improve model robustness under adversarial perturbations.
2. The proposed orthogonal binary layer is effective in enhancing the separation of ID and OOD samples.

### Weaknesses
1. In the formula for the pseudo-embedding generation strategy, $p(r | y = j)$ denotes the conditional probability of generating pseudo-OOD embeddings. Here, the conditional probability notation $p(\cdot | \cdot)$ is used to describe feature vectors that meet a given condition, but in reality, it defines an inequality rather than a complete probabilistic expression. To avoid misunderstandings, it is recommended to rewrite this as an inequality, preventing the impression that a probability density function is defined here.

2. The definition and application of the orthogonal binary layer $B_{\eta}$ are somewhat complex. This layer aims to enhance the separation of ID and OOD samples by enforcing orthogonality in specific directions of the feature space. However, in the formula $L_{SL}$, directly using $B_{\eta}$ as a layer with multiple parameters may cause confusion, especially when multiple hyperparameters are involved. The expression might be clearer if $B_{\eta}$ is decomposed or its function is clearly annotated.

3. The model architecture used in the experimental section is not clearly described in the paper. Please clarify the model architecture.

4. Most of the models used in the experiments are based on traditional CNN architectures. Could the authors consider using Transformer-based models to evaluate performance differences between different methods?

5. It seems the experiments use untargeted attacks. Has the author considered the impact of targeted attacks on OOD detection?

6. In Section A3.2, "Extended Ablation Study," the authors provide results from ablation experiments but do not analyze the reasons for choosing the default parameters in the paper or discuss how different parameters might affect the results.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes the Adversarially Robust OOD Detection through Stability (AROS) method, aimed at enhancing robustness in out-of-distribution (OOD) detection, particularly under adversarial conditions. The authors base their approach on Neural Ordinary Differential Equations (NODE) and Lyapunov stability theory, designing a time-invariant dynamic system to train the model for stability in perturbed environments. The AROS method includes adversarial training, pseudo-OOD embedding generation, Lyapunov stability regularization, and an orthogonal binary layer to construct a robust feature space that improves the separation between in-distribution (ID) and OOD samples. Experimental results demonstrate that AROS outperforms other OOD detection methods across multiple benchmark datasets (e.g., CIFAR-10, CIFAR-100, and ImageNet-1k), especially under strong adversarial attacks such as PGD, AutoAttack, and Adaptive AutoAttack.

### Strengths
1. The paper is clearly written and easy to understand.
2. The authors conducted extensive experiments to validate the effectiveness of their method.

### Weaknesses
1. The loss function $L_{SL}$ includes multiple hyperparameters, $\gamma_1$, $\gamma_2$, and $\gamma_3$. The choice of these hyperparameters affects the model's focus on different regularization terms, but directly showing them in the formula can seem verbose.
2. A detailed explanation of the elements in $[
abla h_{\phi}(X_{\text{train}})]_{ii}$ 

and $[\nabla h_{\phi}(X_{\text{train}})]_{ij}$ is needed to clarify their computation.

3. In the section on the orthogonal binary layer, the equation $z^T z = I$ expresses the orthogonalization condition. However, it is unclear if $z$ has been normalized and whether its inner product yielding $I$ is the required condition.
4. The adversarial attack methods used in experiments are not the latest. The authors are encouraged to add 2023 and 2024 adversarial attack methods, particularly those with stronger transferability and generalization. See this work [1] for reference.
5. The authors did not provide the code for the experiments.

### Questions
1. In the experiments in Table 1, the authors used different model architectures. What is the reason for this choice? Could a unified model architecture be used to ensure fairness in method comparison?
2. Tables 2, 3, and 4 do not specify the model architectures used. Only OOD detection performance on different datasets is shown, which reduces the reproducibility of the paper.
3. In the text, $\epsilon$ is set to 8/255 and 4/255, but in Table 8a, the authors set $\epsilon$ to 128/255 and 64/255. Such high perturbation rates would cause noticeable distortion in samples. Please explain the significance of this setting. Could results for perturbation rates of 16/255 and 32/255, especially 16/255 (the default parameter in most adversarial attack methods), be added?
4. The authors simply list the experimental results for $\beta$ without providing in-depth analysis. For instance, in Table 11a, why are the results for $\beta = 0.001$ identical to those for $\beta = 0.025$? The three hyperparameters $\gamma_1$, $\gamma_2$, and $\gamma_3$ in the loss function $L_{SL}$ are also listed without further analysis.
5. Could some generated pseudo-OOD data samples be provided for readers to view?
6. I am curious whether the proposed method in the paper can be applied to the detection of backdoor attack samples.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces AROS, a method for enhancing the robustness of OOD detection under adversarial attacks. Using Lyapunov-stabilized embeddings within a NODE framework, AROS aims to stabilize the decision boundaries between ID and OOD samples by promoting equilibrium convergence through adversarial training. The approach includes generating synthetic OOD data in the feature space and applying an orthogonal binary layer to maximize separation between ID and OOD samples.

### Strengths
1. **Innovative Use of Stability Theory:** The integration of Lyapunov stability within NODEs for OOD detection is novel and well-motivated. The application of stability principles to mitigate adversarial perturbations shows theoretical grounding.

2. **Comprehensive Evaluation:** The method undergoes extensive testing across datasets (CIFAR, ImageNet, and medical data) under both adversarial and clean conditions. Performance metrics like AUROC and AUPR are presented alongside ablations, providing a thorough examination.

3. **Orthogonal Binary Layer:** The addition of an orthogonal layer to further separate equilibrium points of ID and OOD data adds robustness and addresses alignment issues in perturbed scenarios.

### Weaknesses
1. **Complexity of Mathematical Justifications:** The paper’s reliance on Lyapunov stability and NODEs introduces significant mathematical complexity. Equation derivations and stability proofs (such as those around equilibrium points) are not fully explained, making it challenging for readers without a control theory background. Specifically, the paper lacks a clear explanation of how the Lyapunov function is constructed within the NODE framework and how its properties guarantee convergence to stable equilibrium points, especially in high-dimensional feature spaces. The connection between the theoretical stability conditions and the practical implementation of the NODE is not sufficiently detailed, leaving the reader to infer critical steps. Furthermore, the paper does not adequately address the challenges of ensuring stability when using numerical solvers for the NODE, which can introduce approximation errors that may violate the theoretical stability guarantees.

2. **Synthetic OOD Data Generation:** While the fake OOD generation in the feature space is practical, it lacks clarity on how well it approximates real-world OOD samples. The method samples from low-likelihood regions of the ID feature space, but it is unclear if this captures the diversity and complexity of real-world OOD data, which may have different underlying structures. Further analysis or empirical validation of this approximation would strengthen the argument for its effectiveness. For example, the paper does not explore how the generated synthetic OOD samples compare to real OOD samples in terms of feature distributions or their impact on the decision boundaries. It also does not consider the potential for the synthetic OOD data to introduce biases that could affect the performance of the detector on unseen OOD data.

3. **Loss Function Ambiguity:** The custom loss function, $L_{SL}$, is somewhat ambiguous in its practical effects on training stability. The paper does not provide a clear explanation of how each term in the loss function contributes to the overall stability and robustness of the model. Further detail on parameter tuning (e.g., effects of $\gamma$-values) and ablation studies on these would clarify its role in achieving robustness. The interplay between the cross-entropy loss and the stability terms is not well-defined, and it is unclear how the different $\gamma$ parameters affect the optimization landscape and the convergence properties of the training process. The paper also lacks a discussion on the potential for the stability terms to conflict with the classification objective, which could lead to suboptimal performance.

### Questions
1. Could the authors clarify the theoretical guarantees of Lyapunov stability when applied within the NODE framework, particularly for high-dimensional embeddings? Specifically, could they expand on how the equilibrium points are stabilized across varying adversarial perturbation magnitudes, especially under different norm constraints? Additionally, the derivations and stability proofs related to Theorems 1 and 2 are complex. Would the authors consider including expanded derivations or references in the appendix to enhance understanding for readers without a control theory background?


2. The introduction of the orthogonal binary layer aims to enhance ID-OOD separation. Could the authors provide more empirical insights or visualizations to demonstrate the layer's effectiveness in maintaining separation, particularly in adversarial scenarios? Furthermore, an analysis of the sensitivity of this layer to different perturbation levels would strengthen the practical understanding of its robustness.


3. The authors propose generating synthetic OOD embeddings by sampling from low-likelihood regions in the ID feature space. However, how well does this synthetic data represent real-world OOD instances, which may be more complex in structure? Could the authors provide empirical evidence or a quantitative comparison to validate the representativeness of these synthetic OOD samples? Additionally, would the authors consider including an ablation or alternative generation methods to explore the impact of different OOD data synthesis strategies?

### Soundness
3

### Presentation
3

### Contribution
3
