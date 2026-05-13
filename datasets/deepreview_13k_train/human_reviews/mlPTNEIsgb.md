# Solving Blind Non-linear Forward and Inverse Problem for Audio Applications

- Decision: Reject
- Scores: 1, 6, 5, 1

## Abstract
We propose a unified framework to address the blind forward and inverse problems in audio domain, where the objective is to estimate either the function or the input signal solely from the observed output, without access to the other.
We formally define forward operators ---mapping input to output signals --- and formulate both problems within a probabilistic framework.
For the blind forward problem, we design an architecture that utilizes a reference encoder to extract features from the reference signal, enabling the main operator to approximate arbitrary forward operators systematically composed via algebraic representations. 
For the blind inverse problem, we employ a conditional diffusion model conditioned on features from the pretrained reference encoder and augment the generation process using twisted particle filtering technique leveraging the approximated operator in the forward problem.
We validate our framework on zero-shot audio effect modeling and speech enhancement. The experiments show that our approach replicates both simple and complex audio effects, generalizes under distribution mismatches, and effectively enhances noisy full-band audio across diverse effects and real-world scenarios. 
Codes are available at  https://t.ly/n11uk , with audio samples at https://t.ly/dBUhF

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes a framework for blind estimation of a forward operator and solving the corresponding inverse problem with application in audio signal transformation. The forward operator is estimated using a neural model consisting of a reference encoder and a “main” neural operator. The inverse problem is solved using a score-matching diffusion model. The authors show results on audio effect learning and speech enhancement.

### Strengths
Training pipeline including creating a DAG for the forward operator is interesting, and appears to model more complex forward operators than used in the previous work, e.g., (Rice, 2023).

### Weaknesses
The paper proposes a model for estimating the forward operator, and a score-based model for solving the corresponding inverse problem.
The most relevant existing work is (Rice, 2023). However, that is mentioned only in passing, and the difference or the advantages of the proposed model are not clearly presented. Furthermore, there's not a single baseline system used in the experimental section.
This reviewer would suggest, at minimum, to include (Rice, 2023) as a baseline. Furthermore, it would be helpful to include some of the recent diffusion-based speech enhancement models as baselines in the speech enhancement experiment (for example, score-matching based SGMSE).

Surprisingly, for a paper dealing with estimating audio, the authors found not provide a single audio example.
At minimum, the authors should provide randomly-sampled test example pairs of input and output audio (for different processing setups).
A link to the examples should be provided in the paper.

The paper is unfinished and clearly not well prepared for peer review.
For examples, Tables {2,3,4} are not referred to in the paper.
Footnote 2 on page 10 is particularly interesting, where the authors claim that:
"The numbers of the table are relying on the model with insufficient training iteration, thus will be updated during reviewing process."
In this reviewer's opinion, submitting incomplete results is unacceptable.
The authors should have completed the experiments before the initial submission, and all tables should have been properly referenced.

Based on the results in Table 3, there is some inconsistency in codec results.
In particular, both PESQ and SQUIM-MOS are quite high for the input signals ("Mix"), and the proposed model is significantly degrading the quality. At the same time, the proposed model is significantly improving SI-SDR and eSTOI. The differences are so large, that they do not look convincing without audio examples.

### Questions
"Dry and wet signals" naming is used on page 1, but never formally introduced. While that's a common naming used in audio effects, it's not the ideal choice when handling, for example, speech enhancement. The authors could change that to make it more clear. Using general terminology, such as model input and model output or estimated signal, would be more appropriate.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a framework for solving blind nonlinear forward and inverse problems with applications to audio. Specifically, the authors propose using a reference encoder module to approximate an arbitrary forward function for the forward nonlinear problem. Then, based on the estimated forward operator, they propose solving the inverse problem using guidance from the estimated forward function to train the diffusion model for recovering the input signal. Improvements to the main framework are also discussed by using a particle filter-based approach for the inverse problem. Experimental results on audio effects modeling for the forward problem and speech enhancement for the inverse problem are presented to demonstrate the effectiveness of the proposed method, with both objective and subjective evaluations.

### Strengths
- The proposed framework is theoretically grounded and can be applied to solving both nonlinear forward and inverse problems.

- Robust performance to distribution shift and recording environment mismatch of the training and test audio data; enabling zero-shot audio effect learning.

- Effectiveness of the proposed method across a wide range of audio effects and manipulations, supported by both objective metrics and subjective listening testing scores.

### Weaknesses
 - The main weakness of the work is the lack of comparison with existing approaches for better understanding of where the proposed method stands. For example, for the inverse problem of speech enhancement, the authors could have compared their approach to other diffusion based speech enhancement methods (e.g., *Lu et al., "Conditional Diffusion Probabilistic Model for Speech Enhancement," ICASSP, 2022*; *Tai et al., "DOSE: Diffusion Dropout with Adaptive Prior for Speech Enhancement," NeurIPS, 2023*) on more standard benchmark datasets such as VoiceBand+DEMAND (*Cassia et al., "Noisy speech database for training speech enhancement algorithms and TTS models," 2016*) and CHiME-3 (*Vincent et al., "An analysis of environment, microphone and data simulation mismatches in robust speech recognition," Computer Speech Language, 2017*). Having such comparison to prior works will help strengthen the contribution of this paper.

- Another weakness is the lack of information on the model size, computational complexity, or real-time processing performance of the proposed model. From a practical perspective, many speech and audio processing applications have certain constraints on the latency and memory requirements for the models to be deployed on edge devices (e.g., smart speakers, intelligent home appliances, hearing aids, etc). Therefore, providing relevant information would be helpful for researchers and developers to consider adopting the proposed model.

### Questions
- In Definition 1 (Forward Operator), it is assumed that both $x\in K$ and $y\in K$, where $K\subseteq X=\mathbb{R}^T$. Does it mean that the proposed framework is only applicable to the case where the input $x$ and output $y$ have the same signal length $T$? Could you provide further details on how the proposed framework can be potentially extended to other inverse problems where the input and output signals may have different dimensionality?

- In eq. (1), what does $\mathcal{A}\in\mathcal{C}(K)$ mean?

- At line 159, maybe directly using $c_g$ for $t$ and $c_l$ for $c$ makes it more clear as they refer to the same thing. This could also help the reader understand what $c_g$ and $c_l$ are in the subsequent sentence at line 161.

- In Figure 2, what are the upper-case $X$ and $Y$? It looks like they are the spectrogram representations of $x$ and $y$, respectively, but such information is missing. In addition, do you use the complex-valued spectrograms or just their magnitude components for training the model?

- In Table 3, what do "Mix", "Blind" and "Known" stand for respectively?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a framework for solving blind forward and inverse problems in audio effect modeling and speech enhancement, where the authors aim to recover the applied audio effect or remove degradations without prior knowledge of the effect chain. The approach includes a dynamic pipeline that generates paired dry and wet signals dynamically and a reference encoder that conditions the network to apply or reverse audio effects. The method is evaluated through objective metrics, with code being released to support reproducibility.

### Strengths
- The paper introduces a dynamic signal pairing pipeline that enhances the adaptability of the model across diverse audio effects and environments, a practical contribution to real-time audio processing.
- Using a reference encoder for conditioning allows the model to handle multiple unknown degradations in a versatile manner, making it potentially useful in scenarios requiring "real-time"/zero-shot  adaptability.
- Objective metrics provide an initial evaluation of performance across varied conditions.

### Weaknesses
 - Theoretical and Practical Limitations: The model employs a Directed Acyclic Graph (DAG) with a semiring-based approach to formalize audio effect chains, which could theoretically add rigor if the properties (like associativity and distributivity) were applied explicitly to audio effects. However, without clear practical benefits, the connection risks remaining overly theoretical. The paper could benefit from further exploration of how this semiring-DAG structure enhances computation or generalization in practice. Specifically, the paper does not detail how the semiring operations (addition and multiplication) map to actual audio processing steps, making it difficult to assess the practical implications of this formalism. For example, if the 'multiplication' operation corresponds to a convolution, it should be explicitly stated, and the computational benefits of using the DAG structure for this operation should be analyzed.
- Irreversible Transformations and Restoration Quality: Certain audio effects, such as clipping and band limiting, are irreversible and introduce permanent information loss. While restoration is theoretically possible if the model learns the underlying signal distribution, the quality of restoration is critical and must be rigorously evaluated. In particular, reconstructing fine details - like distinguishing between high-frequency fricative sounds (e.g., "s" and "f") - may be inherently ambiguous after irreversible effects. This limitation should be acknowledged in the framework to set realistic boundaries on reconstruction accuracy. The paper should include an analysis of the model's performance on these irreversible transformations, detailing the specific types of errors that occur and how they relate to the information loss.
- Importance of Perceptual Validation: While the objective metrics provide quantitative insight, they are insufficient to fully assess restoration quality, especially in cases involving irreversible transformations. An actual subjective evaluation through listening tests is essential to validate whether the restored audio meets perceptual quality standards, as small deviations from the original can significantly affect listener experience. The lack of subjective tests here limits the confidence in the model’s real-world applicability. The paper should provide a clear rationale for the choice of objective metrics and explain how these metrics correlate with human perception of audio quality. Without this, the objective results are difficult to interpret in terms of real-world performance.
- Limited Comparative Evaluation and Reproducibility: The absence of task-specific baseline comparisons detracts from a clear evaluation of the method’s effectiveness. Additionally, the lack of accessible qualitative examples (e.g., audio samples) limits reproducibility and a deeper evaluation of perceptual quality. The paper should include comparisons with existing methods for similar audio processing tasks, even if those methods use different datasets or sampling rates. This would help to contextualize the performance of the proposed method and highlight its advantages and disadvantages.
- Result Interpretation: Although the results section provides metrics, a subjective evaluation is missing.

### Questions
- How does the proposed method compare to task-specific baselines in terms of objective and perceptual quality?

- Could the model incorporate assumptions about the original signal distribution to enhance the robustness of the restoration, and would this improve restoration quality?

- In the context of semiring theory, could the properties (like associativity and distributivity) of operations in the DAG be explicitly defined to enhance computation or generalization?

- To improve validation, could a listening test be added to evaluate the perceptual acceptability of restored audio, especially in cases where irreversible transformations have introduced ambiguity?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposes a novel framework for solving blind forward and inverse problems using diffusion models. The approach consists of two main steps:

1. Training an encoder network that takes a transformed signal (wet signal) as input and outputs the parameters of the transformation process (forward operator).
2. During inference, using the parameters estimated by this encoder network to solve the inverse problem, with the diffusion model serving as a prior distribution.

The framework is applied to address the following problems:

- Estimating the original signal (dry signal) from a wet signal created by audio effects with unknown parameters.
- Speech enhancement, which involves restoring the original speech signal from degraded speech that has undergone various processing.

This approach enables the solution of inverse problems where the transformation process is unknown, leveraging the power of diffusion models as priors.

### Strengths
This research topic is important both theoretically and practically as it explores new applications using diffusion models as a foundation. A particularly noteworthy aspect is the potential to solve blind inverse problems with minimal additional training.

### Weaknesses
I find it difficult to recommend this paper for acceptance due to the following reasons. Detailed comments and questions are provided in the Questions part.

1. There are several parts of insufficient explanations. For example, the meaning of 'hallucination effect' on line 57 is unclear, and the caption for Figure 1 is incomplete. Addressing these and other similar issues would improve the paper.
2. While the paper contains a lot of mathematical descriptions, many terms are undefined or seem unnecessary for the discussion. Although some meanings can be inferred, the lack of proper citations makes it challenging for readers to follow the discussion accurately. For instance, A_{\theta}^{\dagger} on line 145 and c_g, c_l on line 161 are not properly defined. Additionally, Proposition 1 and Theorem 1 are stated without proofs.
3. The problem addressed in this paper appears to be inadequately defined, and it's unclear from the paper whether the method described in section 6.2.3 actually solves this problem.
4. A major issue is that the experimental results in Section 7 do not include any comparative methods. This makes it impossible to discuss the performance advantages of the proposed method.

### Questions
I would like to request clarification from the authors on the following points:

1. Please provide evidence for the claim near line 49 “that generative models are inferior to discriminative models in terms of quality”.
2. Explain the meaning and relevance of the statement on line 57 that particle filtering techniques reduce the 'hallucination effect'.
3. In Definition 1, if a pure noise-adding operator (as might be expected in speech enhancement tasks) is unbounded, is it excluded from the forward operators considered in this paper?
4. Complete the explanation following '(Right)' in Figure 1.
5. Clarify the definition of 'forward problem' mentioned on line 129.
6. Provide the definition of A_{\theta}^{\dagger} on line 145.
7. Define c_g and c_l mentioned on line 161.
8. Explain what 'sequence length' refers to on line 188.
9. Demonstrate how the training objective in section 4.3 is derived from the objective function defined in section 3.
10. Provide the proofs for Proposition 1 and Theorem 1.
11. Explain how the results of Theorem 1 contribute to the paper's main arguments.
12. Describe the derivation method for m(x_t) and C(x_t) in equation (8) of section 6.4.
13. Can you add comparative methods to section 7?
14. Is it possible to provide audio samples in the experimental section, e.g., audio samples corresponding to the spectrograms shown in Figures 6-9?"

### Soundness
1

### Presentation
1

### Contribution
1
