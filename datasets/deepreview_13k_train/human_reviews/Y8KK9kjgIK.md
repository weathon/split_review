# SigDiffusions: Score-Based Diffusion Models for Time Series via Log-Signature Embeddings

- Decision: Accept
- Scores: 6, 6, 1

## Abstract
Score-based diffusion models have recently emerged as state-of-the-art generative models for a variety of data modalities. Nonetheless, it remains unclear how to adapt these models to generate long multivariate time series. Viewing a time series as the discretization of an underlying continuous process, we introduce  \texttt{SigDiffusion}, a novel diffusion model operating on log-signature embeddings of the data. The forward and backward processes gradually perturb and denoise log-signatures preserving their algebraic structure. To recover a signal from its log-signature, we provide new closed-form inversion formulae expressing the coefficients obtained by expanding the signal in a given basis (e.g. Fourier or orthogonal polynomials) as explicit polynomial functions of the log-signature. Finally, we show that combining \texttt{SigDiffusion} with these inversion formulae results in highly realistic time series generation, competitive with the current state-of-the-art on various datasets of synthetic and real-world examples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors propose a generative model for multivariate time-series data, SigDiffusion. The diffusion processes generates samples from a distribution in a (latent truncated) log-signature space (coming from Rough Path theory), which serves as an efficient embedding of a time series. The authors discuss improved methods for recover from the log-signature to time-series path space — namely they propose some new closed-form inversion formulas to recover the time-series trajectories from the log-signature as polynomial series. 

The two main contributions are:
1. Application of score-based generative diffusion model to space of truncated log-signatures, which is 
2. Improvements to signature inversion algorithm going from the log-signature space to trajectory space. 
    1. This is done by path as expressed as a series in different polynomial bases, which can be shown to converge.

These two claims are backed up by empirical experiments:
- For the signature inversion: synthetic evaluation using example paths random sine waves + gaussian noise,
- For the diffusion model application time-series: Two synthetic data (sines, Lotka–Volterra system) and three real data: Household Electric Power Consumption, Exchange Rates, and Weather.

### Strengths
- The paper is clear, well organized, and well written (see later comments on section 2)
- The overall scheme using log-signature is grounded in sound mathematical theory from rough path theory and signature method literature. The claims in Theorems 3.1 and 3.2 seem reasonable (though I did not check in high detail) and appear to be new contributions that address a known problem in literature.
- Efficacy of doing diffusion in log-signature space backed up by empirical evidence
    - Per Table 2. The speedup by doing the generative process in the truncated log-signature is an advantage with comparable or better performance to other diffusion method for continuous-time paths.

### Weaknesses
### Contribution, Theory, and Experiments:

- Doing the diffusion in log-signature (or the space of any integral transform/transformed feature or embedding) is a relatively straightforward idea (similar ideas are discussed in related literature of section 4). Primary contribution seems to me to the closed form signature inversion formula, which then enables one to do the diffusion processes in the log-signature space. I am more or less convinced that the presented polynomial series would approximate the original signal. But all numerical illustrations done in this aspect are only with synthetic data, and not using real data (though the synthetic illustrations are quite extensive, they seem to mostly cover of the case of a low frequency signal + noise).
    - Since the signature inversion is a primary claim, it may be useful to provide some illustrations using the real datasets about reconstruction quality (e.g., in terms of $\ell_2$ error akin to Fig 8.) from log signature (e.g., number of basis, type of basis, properties of the data analogous to Appendix D.)
    - The runtime to recover using the closed form inversion formula in terms of number of basis and number of truncated signatures is not explicitly stated.
- It may be useful to have at least a comparison to one non-diffusion baed generative time series model (i.e., pick one from section 4, following from TimeGAN paper).

### Organization and Writing:

- Disclaimer: I not an expert in signature method or rough path theory:
    - Not coming from this background, I think presentation in full generality of Section 2 is, in my opinion, not very accessible.
    - The present development may be more suitable for an appendix. The exposition in provided references (e.g., Fermanian et al. 2023) was more clear to me.

### Errata: 
- Line 213: acronym ST is not defined, assume it refers to (log)-Signature Transform.

### Questions
- Could authors provide some results on signal recovery for real signals? (e.g. some signals have non-noise high frequency characteristics that may not be well captured without higher order terms of polynomial series, you could back this with up with some synthetic signals as well).
- In Appendix E of experimental details could authors provide some discussion about which inversion scheme (and how many basis authors used) authors chose for the real data and why?
- Why is the order of the log-signature order chosen to be 4 in your experiment? Since the runtime growth is highly unfavorable in the order $\mathcal{O}[(d^{n+1}-1)/(d-1)]$ and mildly unfavorable in the dimension of the signal.
- On the runtime aspect, to make work self contained, could authors provide some discussion (extending Figure 1) about how much runtime is required to transform between the truncated log-signature space (extending discussion in lines 198-205), and go from the log-signature space to the path space using Theorems in 3.1 and 3.2 (i.e., extending Table 2) and comment on runtime as compared to previous method (e.g., Inversion method).
- Connection to long sequences specifically is unclear to me, could you elaborate on why SigDiffusion is more suitable for long sequences?

Happy to adjust my score if these concerns are addressed

### Soundness
3

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
3

### Summary
This paper proposes an algorithm for generating particularly long multi-series time series. The proposed method, SigDiffusion, embeds time series into a Lie algebra and is a diffusion model constructed from the perspective of Lie algebra structure.

### Strengths
- This paper proposes a new method for constructing a time series generation model for multiple series. The model method is score-based diffusion, but it is a method that is theoretically robust because it is constructed based on Lie algebra analysis.
- The proposed method is also very useful for objects with long series lengths.
- It is constructed with theoretical proof, so I think it will be useful in terms of leading to a wide range of future expansion. Personally, I am very interested in the possibility of applying it to texts and leading to the construction of an LLM.

### Weaknesses
This paper is strong in the theoretical part, and that is important, but on the other hand, the description of the experimental part is poor. It is not clear what the experiment proves in relation to the paper's claim. It is unclear whether it is showing that it is excellent as a generative model for time series, or whether it is showing that it is excellent in score-based diffusion, but since it is being compared with TS-Diffusion, I think it is showing that it is excellent in the overall generative model for multiple series. Since time series generation models are being actively developed, it is necessary to compare the most advanced methods, and it should be explained that appropriate methods have been selected for comparison. There are so many different new methods, and the evaluation metrics and data sets are all different, that it is impossible to judge whether they are producing sufficient results. Also, the Discriminative Score is generally a better indicator when the value is larger, and this can be recognized even by reading the explanation, but it seems that a smaller value is better. I think it would be better to clarify the definition. It seems that the predictive score is defined in the same way as the loss used in training, but the loss in training does not always match the loss in prediction performance, so the definition should be clearly stated.

### Questions
- What is the claim you want to prove in Table 1, and after looking again at the most advanced methods, please tell us why the comparison you have chosen is appropriate as a way of proving your claim. There may be cases where you change the comparison. Table 1 in [1] will be useful for a list of cutting-edge methods.

[1] Y. Yang et al., A Survey on Diffusion Models for Time Series and Spatio-Temporal Data, arXiv:2404.18886

- Please clarify the definitions of the evaluation indicators in Table 1.
If the above points are clarified, I will raise the score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper presents a new score-based diffusion modeling trick for long multivariate time series.
Their motivation is to recover the underlying dynamics of the discretized time series data via log-signature embeddings.
Here, log-signature embeddings corresponds to some algebraic structure of time underlying continuous time dynamics.
The key contribution is the derivation of a closed-form for signal recovery.
They support their theory and proposal with numerical experiments.

### Strengths
This work suggests a new approach to time series generation from signature inversion algorithms. The problem of interest is important. The method employed is refreshing, at least in ML.

### Weaknesses
## **Updated after rebuttal: Changed to strong rejection due to claiming non-original results as their own.**

---

I don't believe I'm the best person to judge this work, as I'm not well-versed in log-signature. However, I am familiar with Lie algebra, group theory, and some algebraic and topological algebra. I find this paper challenging to read and understand, even with my background. The paper feels more like a math paper than an ML paper, especially in the first half. While I appreciate the mathematics, I believe there are valuable insights here, but I suggest the authors polish the presentation to better engage the general ML community.

* Are Thm 2.1 and Thm 2.2 original results? If not, consider treating them as lemmas and specifying the reference in the title. For example, "Lemma 2.1 (Shuffle Identity, Ree 1958)."

* Poor motivation. For theory-heavy papers, motivation and intuition are important to communicate with a broader audience, including non-theorists and mathematicians. For example, in Appendix A, while the authors provide some examples, they remain very dry and don't help the reader appreciate the connection between log-signature and ML.

* As a background section, Sec. 2 is very dry and difficult to learn from, beyond memorizing definitions.

* As a methodology paper, the experiments are somewhat limited.
  -  Ablation. The paper does not include enough ablation studies. Additional ablation studies are needed to support the findings.
  - For common time series data, why only use exchange rates and weather? Why not include electricity and traffic data?

Given above, I find this paper not ready for publication. I encourage the authors to improve its accessibility for the broader ML community.

### Questions
Per my understanding, log signature is path integral. A few clarification questions are in order:

* Is log-signature deterministic or stochastic path?

* If it's deterministic, please justify why it's a good idea to use deterministic dynamics in stochastic diffusion process?

* How to justify the robustness of the algebraic structure against noise? Especially it's well-known time series is one of the most noisy data type.

* In `line 182`, why you describe the score function as it's not continuous? In score-based DMs, while the time is discretized for implementation purposes,  score function is continuous.

From above, I find it difficult to see the connection between DMs and log-signature embedding in Sec. 2.3.

### Soundness
2

### Presentation
1

### Contribution
1
