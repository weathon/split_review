# Phase-aware Training Schedule Simplifies Learning in Flow-Based Generative Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 3, 5

## Abstract
We analyze the training of a two-layer autoencoder used to parameterize a flow-based generative model for sampling from a high-dimensional Gaussian mixture. Building on the work of Cui et al. (2024), we find that the phase where the high-level features are learnt during training disappears as the dimension goes to infinity without an appropriate time schedule. We introduce a time dilation that solves this problem. This enables us to characterize the learnt velocity field, finding a first phase where the high-level feature (asymmetry between modes) is learnt and a second phase where the low-level feature (distribution of each mode) is learnt. We find that the autoencoder representing the velocity field learns to simplify by estimating only the parameters relevant to the feature for each phase. Turning to real data, we propose a method that, for a given feature, finds intervals of time where training improves accuracy the most on that feature, and we provide an experiment on MNIST validating this approach.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
2

### Summary
This paper presents a new training approach for flow-based generative models designed to overcome the challenge of learning high-level features in high-dimensional spaces. The authors introduce phase-aware strategy combined with a time dilation mechanism to provide an appropriate time schedule for the model to capture high-level structures. Using a two layer autoencoder and a two-mode Gaussian Mixture Model, they show that the neural network representing the velocity field learns to simplify only phase-relevant parameters. Validation using the MNIST dataset indicates that their method identifies a time interval during which additional training significantly enhances accuracy for specific features.

### Strengths
1. The paper has explained in depth the mathematical background of the method.
2. It showed an interesting idea.

### Weaknesses
1. The standalone paper does not show any experiments or proof of them. 
2. The paper does not include a comparison with other state-of-the-art methods. 
3. The paper should include clear picture with network architecture.
4. It is almost only theoretical without clearly presenting the necessary experiments or methods that would be expected.
5. The paper is hard to follow and has some weirdly written sentences, i.e. “”Sample complexity for Gaussian Mixtures Cui et al. (2024) study the learning problem for the Gaussian mixture in high dimensions demonstrate n = Θd(1) samples are sufficient to sample the in the balanced case where (the two modes have the same probability.)”
6. The paper lacks quantitative and qualitative comparisons. Two graphs included show more of an ablation study and not the comparison. 
7. It has a well-written theoretical side but without any visual or quantitative results, it is not sufficient to defend the theory.

### Questions
1. Do you have a visual comparison of the MNIST dataset? If so, can you include it in the main paper? 
2. Did you do a comparison with state-of-the-art methods? Can you please include it in the tables and figures in the main paper?
3. Could you please check the grammatical correctness of the paper? Some sentences have unnecessary brackets and overall the paper is hard to follow and understand.
4. Could you please include a figure showcasing your proposed method? It would enhance the readability of your paper.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a novel approach to training and analysing diffusion models by splitting the process into two distinct phases. The first phase focuses on determining the mass assignments of clusters to the data, while the second phase is dedicated to learning the structure of each individual cluster. The authors provide explicit calculations for a bimodal Gaussian, which indicate the change point between these two phases. Additionally, experiments are conducted on the MNIST dataset to demonstrate the approach in practice.

### Strengths
This paper provides explicit formulas for identifying the phase transition between the two phases described by the authors in a diffusion process. These formulas, although cumbersome to derive, are valuable in the context of the standard bimodal Gaussian example used for sampling. By offering a precise mathematical framework to describe this phase transition, the authors make a contribution for the bimodal Gaussian.

### Weaknesses
The main weakness lies in the lack of generalisability of the analysis, and further overall contribution of this work. While the authors provide a detailed investigation of a bimodal example, it remains unclear how this extends to more complex, multimodal data. For datasets with more than two modes, it is not obvious that there are always two phases along the diffusion path, as suggested by the authors. In such cases, there may be multiple occurrences of cluster splitting, and without prior knowledge of the underlying probability density, it is difficult to derive explicit formulas. This limits the broader applicability of the approach to more general probability distributions.

Furthermore, the use of the MNIST dataset, although a recognised benchmark, does not sufficiently demonstrate the generalisability of the authors' claims. To support their conclusions, a more diverse set of examples, ideally involving a variety of multimodal distributions, would provide stronger evidence.

From my current understanding, the presented framework may struggle to accommodate general Gaussian mixtures. If such formulas could indeed be extended, one would expect to see multiple phases emerging during training that cannot be easily identified computationally. This raises questions about the practical utility of the method in more complex settings. Additionally, it is unclear why the phase transitions along the diffusion path are not evident from the mollification process described by the Ornstein-Uhlenbeck SDE, especially for multimodal data well studied in the annealed Langevin literature.

I would encourage the authors to clarify whether the paper aims to claim that, in general, there are two phases to be considered during training for multimodal data, or if this only holds true for bimodal Gaussian mixtures. A clearer articulation of this distinction would significantly aid in understanding the broader relevance of the work. Further elaboration on how these results might generalise to more complex probability densities would also help assess the robustness of the proposed approach.

### Questions
Could the authors comment on the expected behaviour for a Gaussian mixture with three clusters? Specifically, if the cluster means are centred at vectors $(-1,...,-1)$, $(0,...,0)$, and $(100,...,100)$, with unit variances and equal weighting across the clusters, would we still observe two distinct phases as described for the bimodal case? 

Additionally, could the authors provide further experimental results for multimodal distributions with more than three clusters? A detailed description of the diffusion schedule used in these experiments would also be valuable for better understanding the behaviour of the model in more complex settings.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates the training dynamics of a two-layer autoencoder in a flow-based generative model for high-dimensional Gaussian mixtures. The authors identify and address a phase loss issue in high-dimensional settings, introducing a time dilation technique to ensure sequential learning of high-level and low-level features. This approach enables the model to focus on relevant parameters in each training phase, with experiments on MNIST demonstrating the effectiveness of feature-specific time intervals for improving accuracy.

### Strengths
***Relevance of Topic***: The paper addresses a highly relevant and popular topic within the field, focusing on a new approach to velocity field learning in generative models. 

***Potentially Valuable Theoretical Contributions***: The theoretical considerations presented in the paper have promise for advancing the understanding of velocity field modeling. If better supported by clear explanations and experimental validation, these theoretical insights could offer a substantial contribution to the committee’s knowledge and help guide future research.

### Weaknesses
1)
The paper misses some very important references on phase transitions in generative diffusion. The cited analysis of speciation times in Biroli (2024) was partially based on prior work on spontaneous symmetry breaking (Raya, 2023), which should be properly discussed. In fact, this was the first work to characterize symmetry-breaking phenomena as a function of the time variable and to suggest the separation in qualitatively different generative phases, which is fundamental to the approach the authors are proposing. The authors should also discuss the further developments in (Ambrogioni, 2023), and the more mathematical related work in (Li, 2024). Note that, while these results are not stated in terms of stochastic interpolants, they all translate directly to the setting considered in this submission.

2) The time dilation formula in Eq.10 can only be calibrated on a single symmetry-breaking point. This means that the proposed method can only improve the probabilistic calibration of a specific class separation. While I do think that this is a valid starting point, it would be more useful to have a formula that can recalibrate the sampling of data with multiple decision points and a more complex class structure. 

3) The experiments on real image datasets are rather weak for the standard of a top international conference. It would be useful to see the analysis repeated on other datasets such as Cifar10, CelebA and ImageNet and on other class divisions. It would also be useful to compare the results with other noise scheduling methods commonly used in the literature.

### Questions
Please refer to the weakness section.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper deals with an important issue with flow-based and diffusion models, namely that the generative process is highly non-stationary, with certain phases of diffusion being almost 'trivial' and with short 'critical' time windows that have an overwhelming importance in the final generation. These decision points are also known as spontaneous symmetry breaking points or speciation points and are strongly connected with the theory of critical phase transitions in statistical physics (Raya, 2023; Ambrogioni, 2023; Biroli, 2024; Li, 2024). 

The paper offers a thorough theoretical analysis of flow-based generative models under a mixture of Gaussian data in high dimension, which results in a time-dilation formula that optimizes the training process by a non-linear transformation of the time variable. The formula is designed to 'push' the symmetry breaking point that divide two predefined classes at infinity, which results in a more homogeneous training and in more balanced generation.

While the formulas have been derived for mixture of Gaussian data, the author also provides experiments that suggest their usefulness in real image datasets.

### Strengths
To my knowledge, this is one of the first papers to deal with this important problem. Most existing work on time and noise scheduling are only based on features of the forward process or on empirical performance by trial-and-error. Given the insights from statistical physics, the time is ripe for a more principled approach to noise scheduling and I highly appreciate the effort of the authors in providing a principled solution.

The paper is generally well-written and its results are relatively easy to read. while I did not check the details of the proofs, the theoretical analysis appears to be rigorous and well-motivated. The basic idea of removing the trivial phase of diffusion by changing the time axis is well-principled and it seems to lead to performance gains in simple models and to promising results in real image datasets.

### Weaknesses
1)
The paper misses some very important references on phase transitions in generative diffusion. The cited analysis of speciation times in Biroli (2024) was partially based on prior work on spontaneous symmetry breaking (Raya, 2023), which should be properly discussed. In fact, this was the first work to characterize symmetry-breaking phenomena as a function of the time variable and to suggest the separation in qualitatively different generative phases, which is fundamental to the approach the authors are proposing. The authors should also discuss the further developments in (Ambrogioni, 2023), and the more mathematical related work in (Li, 2024). Note that, while these results are not stated in terms of stochastic interpolants, they all translate directly to the setting considered in this submission.

2) The time dilation formula in Eq.10 can only be calibrated on a single symmetry-breaking point. This means that the proposed method can only improve the probabilistic calibration of a specific class separation. While I do think that this is a valid starting point, it would be more useful to have a formula that can recalibrate the sampling of data with multiple decision points and a more complex class structure. 

3) The experiments on real image datasets are rather weak for the standard of a top international conference. It would be useful to see the analysis repeated on other datasets such as Cifar10, CelebA and ImageNet and on other class divisions. It would also be useful to compare the results with other noise scheduling methods commonly used in the literature.

References:
I) Raya, Gabriel, and Luca Ambrogioni. "Spontaneous Symmetry Breaking in Generative Diffusion Models." arXiv preprint arXiv:2305.19693 (2023).
II) Ambrogioni, Luca. "The statistical thermodynamics of generative diffusion models." arXiv preprint arXiv:2310.17467 (2023).
III) Li, Marvin, and Sitan Chen. "Critical windows: non-asymptotic theory for feature emergence in diffusion models." arXiv preprint arXiv:2403.01633 (2024).

### Questions
1) Could you connect your result to the theory of spontaneous symmetry breaking in generative diffusion models?

2) Could you offer some suggestions on how to extend your formula to the case with multiple classes that separate at different critical times?

### Soundness
3

### Presentation
2

### Contribution
2
