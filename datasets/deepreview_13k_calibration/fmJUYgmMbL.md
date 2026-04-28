# Learned Reference-based Diffusion Sampler for multi-modal distributions

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 3, 6, 8

## Abstract
Over the past few years, several approaches utilizing score-based diffusion have been proposed to sample from probability distributions, that is without having access to exact samples and relying solely on evaluations of unnormalized densities. The resulting samplers approximate the time-reversal of a noising diffusion process, bridging the target distribution to an easy-to-sample base distribution. In practice, the performance of these methods heavily depends on key hyperparameters that require ground truth samples to be accurately tuned. Our work aims to highlight and address this fundamental issue, focusing in particular on multi-modal distributions, which pose significant challenges for existing sampling methods. Building on existing approaches, we introduce \emph{Learned Reference-based Diffusion Sampler} (LRDS), a methodology specifically designed to leverage prior knowledge on the location of the target modes in order to bypass the obstacle of hyperparameter tuning. LRDS proceeds in two steps by (i) learning a \emph{reference} diffusion model on samples located in high-density space regions and tailored for multimodality, and (ii) using this reference model to foster the training of a diffusion-based sampler. We experimentally demonstrate that LRDS best exploits prior knowledge on the target distribution compared to competing algorithms on a variety of challenging distributions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a new approach to sampling from multi-modal distributions called Learned Reference-based Diffusion Sampler (LRDS). The proposed method is an extension of previous variational diffusion-based samplers and tries to address their limitations related to their sensitivity to small perturbations of hyperparameters. The authors propose two approaches. The first one GMM-LRDS is based on Gaussian Mixture Models, a more lightweight approach targeting simpler target distributions. The second one EBM-LRDS uses a more computationally expensive Energy-Based Model, allowing one to sample from harder target distributions.

### Strengths
1. The paper's structure is logical and well-organized, and the writing is clear and concise, making it easy to follow and understand.
2. The paper demonstrates a strong mathematical foundation that supports the authors' claims. The inclusion of detailed mathematical proofs in the appendix adds to the paper's technical depth.
3. In contrast to previous methods, which rely on hyperparameter tuning for reference distributions, the proposed approach learns these hyperparameters.

### Weaknesses
1. While the figures are generally well-presented, some may benefit from additional context or explanation in the main text. For example, the importance of parameter $h$ in Figure 4 is not obvious without checking the appendix. Specifically, the connection between $h$ and the imbalance of the modes in the $\phi^4$ potential is not clearly articulated, making it difficult to understand the experimental setup and results without referring to supplementary material. This lack of clarity hinders the accessibility of the paper.
2. The authors present the experiments only on the synthetic datasets. The paper would greatly benefit from the inclusion of experiments on real-world datasets (e.g., images), which would help to demonstrate the practical applicability. The current experiments, while useful for demonstrating the method's behavior on controlled distributions, do not sufficiently establish its effectiveness in more complex, real-world scenarios where the underlying distributions are often unknown and high-dimensional. The absence of such experiments limits the paper's impact and practical relevance.
3. The authors provide the computational complexity of the overall sampling procedure for different methods in the appendix; however, the memory complexity and exact timings might help the reader. While asymptotic complexity is useful, it does not provide a complete picture of the computational cost. Practical considerations such as memory usage and wall-clock time are crucial for assessing the feasibility of the proposed method in real-world applications. The lack of this information makes it difficult to evaluate the practical efficiency of the proposed approach compared to existing methods.

### Questions
I would like to suggest authors to 
1. add the comparison on real-world datasets.
2. add the exact timing comparison of the discussed methods for training and sampling stages.
3. expand the experiments section with an ablation study of the LRDS limitations.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a sampling method (named as LRDS) which extends existing works to sample from a probability density under the assumptions that they know the location of modes of the distribution while do not have access to the ground truth samples. Inspired by the observations that the existing works are sensitive to hyperparameters, the authors propose two methods (GMM-LRDS and EBM-LRDS) that surpasses the performance of the baselines on sampling from multimodal distributions.

### Strengths
- Trying to solve interesting and fundamental problems.
- Performance improvement over the baselines for estimating mode weight is shown.

### Weaknesses
 - Please revise the introduction entirely from the high-level perspective. Currently, Introduction is written as if sort of a problem definition and preliminary knowledge (which are usually put in related works or method section).
    1. What is the task to solve?     
    2. What are the real-world applications?
    3. What other baselines have been proposed? And what are the limitations of them?
    4. What is the proposed method concisely and what is the improvement that is theoretically and empirically shown in the paper?
    - It should be understandable to some extent for non-expert readers in this domain.
    - I believe this is a basic rule of thumb in paper writing.
- Weak motivation
    - Why do we need to care about this paper’s assumptions (L40-L41)? Is it a realistic scenario? What are the examples in practice?
    - Why do we need to sample from multi modal distributions? (L35-L36) Why not simply sampling from a single-mode distribution?
- Weak experiments
    - Higher dimensional dataset experiments are needed (e.g., MNIST or Cifar10) to show that the proposed methods can be applicable beyond the toy-level experiments.
    - Quantitative experiments
        - The measure for computing the distance/divergence with the target distribution is required.
        - How is Table 2 (mode weight estimation error) connected to the actual task which is approximating the target distribution?
        - It seems like each column of Table 2 is almost identical. Is there something meaningful to report? 

- Overall, the proposed method itself is interesting. However, its presentation (paper writing) needs to be significantly revised and the experiments are not good enough to show the performance improvements in sampling and to verify that the proposed method can be applicable in the real world applications.

### Questions
1. Fig. 4. Is GMM-LRDS as fast as the Laplace approximations?
2. It is very difficult to find strengths of the proposed methods in Fig. 5. LV-DDS looks better, actually.

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
2

### Summary
This paper introduces the Learned Reference-based Diffusion Sampler (LRDS), a novel approach for sampling from multi-modal distributions. The authors identify a fundamental issue with existing variational diffusion-based methods (their high sensitivity to hyperparameters) and address this by proposing a methodology that leverages prior knowledge of target mode locations. LRDS is implemented in two variants: (1) GMM-LRDS, which is well-suited for a variety of target distributions while being relatively lightweight, and (2) EBM-LRDS, a more computationally intensive approach for harder sampling problems. Through extensive experiments on challenging multi-modal settings, the authors demonstrate that LRDS outperforms previous diffusion-based samplers.

### Strengths
1. The paper demonstrates a critical limitation in existing diffusion-based sampling methods. To solve the hyperparameter sensitivity issues in previous approaches, the authors provide a well-grounded theoretical method for their solution. The mathematical framework is developed and presented clearly, making their contributions theoretically sound and academically valuable.

2. The experimental evaluation is encompassing a diverse range of challenging distributions. The authors' comparative analysis against multiple baseline methods across different settings provides evidence for their method's superiority.

3. The paper offers two complementary approaches (GMM-LRDS and EBM-LRDS) that provide flexibility in handling different types of multi-modal distributions. These two versions of the method demonstrate the validity of the reference-based sampling approach proposed in this paper. Figures 5 and 6 show that the proposed method generally works well for various distributions.

### Weaknesses
1. A limitation of the proposed method lies in its computational overhead, particularly in the pre-training phase of the reference process models. The authors could have provided a more detailed analysis of the computational costs, specifically detailing the time complexity of the MCMC sampling, GMM/EBM training, and the diffusion model training, and how these scale with the dimensionality of the target distribution and the number of modes. Furthermore, the authors should discuss optimization strategies, such as parallelization or approximations, to mitigate the computational burden as the complexity and scale of the target distribution increases.

2. The method's reliance on prior knowledge of mode locations (target distribution) represents a substantial practical limitation. While the authors acknowledge this requirement, the authors could address how the method might be adapted for scenarios where such information is incomplete or inaccurate. For example, the authors could explore strategies for automatically detecting modes or incorporating uncertainty about mode locations into the reference distribution. The current approach assumes perfect knowledge of mode locations, which is unrealistic in many real-world applications.

3. There are concerns about the method's applicability to real-world data distributions, despite its impressive performance on synthetic examples. While the paper demonstrates effectiveness in controlled settings, the approach of learning mode information from reference samples may not translate well to real-world scenarios where modes are less well-defined, data is high-dimensional, and data structures are more complex and noisy. The lack of validation on real-world datasets, such as image or molecular data, leaves uncertainty about the method's practical utility and generalizability beyond carefully constructed example distributions. The paper should include experiments on real-world datasets to validate the method's robustness and applicability.

### Questions
1. what the impact would be if random sampling was used to obtain reference samples rather than sampling that reflects a target distribution such as mcmc?

2. I understand that challenge mode collapse settings are rare in general real-world datasets. Although these experiments and analyzes may not be appropriate for the contribution of this paper, I wonder whether this sampling strategy can be applied to general real-world applications.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Unlike previous score-based diffusion sampling methods, this paper takes a step further by learning a reference process based on GMMs or energy-based models (EBMs) to facilitate sampling from multi-modal distributions. The energy-based models (EMMs) presented are novel compared to recent literature, enabling the learning of references for various challenging distributions that GMM-based references cannot handle. Additionally, the authors summarize the key differences and innovations of their method compared to other diffusion sampling techniques in Table 1.

The authors also compare their approach with other state-of-the-art algorithms, including LV-PIS, LV-DDS, and LV-DIS, on various challenging distributions. And the results are satisfactory.

### Strengths
1. The paper proposes using GMMs or EBMs, based on prior knowledge of the modes, as a reference for sampling multi-modal densities. The EBM framework is particularly novel, as it helps learn initial references through a neural network for sampling a range of distributions that standard GMMs reference cannot handle.

2. The paper is technically sound, presenting solid theories, lemmas, and propositions in the Appendix, which provides a good supplement and well support their algorithms.

3. The paper compares their algorithm with various other state-of-the-art algorithms, and the results are satisfactory.

### Weaknesses
1. While the paper highlights leveraging prior knowledge of mode locations to avoid hyper-parameter tuning challenges, I believe the sensitivity still depends on the choice of reference distributions. The authors may illustrate how different choices of references (e.g., varying the number, means, variances of GMM components, or EBM architectures) impact the sampling results. Specifically, for GMMs, the impact of misspecified component variances (e.g., using too narrow or too wide variances relative to the true modes) should be explored. For EBMs, the sensitivity to the choice of network architecture (number of layers, hidden units, activation functions) and training parameters (learning rate, batch size) should be investigated, as these choices can significantly affect the learned energy landscape and thus the sampling performance.

2. In the experiments, the modes of the target distributions (such as the high-dimensional Gaussian, rings, and checkerboard) are relatively close together. Have the authors tried target distributions with varying number of modes (e.g., 10, 100, 500) with increasing separation, and how does the algorithm perform in these cases? It would be beneficial to see how the method scales to scenarios with a larger number of modes and how the separation between modes affects the convergence and quality of the samples. For example, in high-dimensional spaces, the separation between modes might need to be significantly larger to avoid overlap, and it's unclear how the proposed approach would handle such cases. Furthermore, the computational cost of training and sampling should be analyzed as the number of modes increases.

3. The authors primarily evaluate mode weight recovery error, but there are other important evaluation metrics, such as Maximum Mean Discrepancy (MMD) and Wasserstein distance. Since it seems possible to obtain true samples for each of the experiments, I believe calculating MMD and Wasserstein distance would be feasible. These metrics would provide a more comprehensive assessment of the sample quality, capturing not only the mode weights but also the overall distribution shape and diversity. It would also be useful to report metrics such as the Effective Sample Size (ESS) to quantify the independence of the generated samples.

### Questions
Regarding the weaknesses, my questions are as follows:

1. How sensitive is your algorithm to the choice of different reference distributions (e.g., in GMMs, the variances/means of the modes; and in EBMs, the choice of hyper-parameters)?

2. How does the model perform when the modes of the target distributions are widely separated or when the number of modes is higher? What about the training and sampling complexities?

3. Can the authors present additional evaluation metrics to provide more straightforward assessments of sample quality?

### Soundness
4

### Presentation
3

### Contribution
3
