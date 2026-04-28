# Classifier-Free Guidance is a Predictor-Corrector

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
We investigate the theoretical foundations of
classifier-free guidance (CFG).
CFG is the dominant method of conditional sampling for text-to-image diffusion models, yet
unlike other aspects of diffusion, it remains on shaky theoretical footing. In this paper, we first disprove common misconceptions,
by showing that CFG interacts differently with
DDPM~\citep{ho2020denoising} and DDIM~\citep{song2021denoising},
and neither sampler with CFG generates the gamma-powered distribution $p(x|c)^\gamma p(x)^{1-\gamma}$. 
Then, we clarify the behavior of CFG by showing that it is a kind of
predictor-corrector method \citep{song2020score} that alternates between denoising and sharpening, which we call predictor-corrector guidance (PCG).
We prove that in the SDE limit,
CFG is actually equivalent to
combining a DDIM predictor for the conditional distribution
together with a Langevin dynamics corrector
for a gamma-powered distribution
(with a carefully chosen gamma).
Our work thus provides a lens to theoretically understand CFG
by embedding it in a broader design space
of principled sampling methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper attempts to understand classifier-free guidance from a theoretical perspective. A special characteristic of classifier-free guidance is that it introduces a strength parameter $\gamma$ so that the plug-in score function is not precisely $\nabla \log p_t(x | y)$. Although practical results demonstrate promises of this methodology, its theoretical analysis is still largely missing. This paper presents new understanding of classifier-free guidance by first pointing out that the terminal distribution is hard to find. From my reading, this result is relatively a minor contribution. More interesting results come when connecting classifier-free guidance to predictor-corrector algorithm.

### Strengths
This paper is well written and the results appear to be correct and sound.

I am particularly appreciative of the discussions in Section 5, not only introduces relevant literature, but also touches on limitations and future directions.

Understanding classifier-free guidance from a theoretical perspective is an important direction.

### Weaknesses
Practical implication of the study may be limited.

### Questions
The following two recent works are related to guidance in diffusion models; they focus on mixture models. "What does guidance do? A fine-grained analysis in a simple setting" and "Theoretical Insights for Diffusion Guidance: A Case Study for Gaussian Mixture Models".

Algorithm 1 states that Line 4 is a DDIM step. From my understanding, DDIM (as well as DDPM) uses an exponential integrator to discretize the backward ODE (SDE). Line 4 is a Euler discretization. Some discussion might be needed.

What do we gain from writing out the SDE limit of PCG?

Are there practical reasons to sample from the gamma-powered distribution? I believe the gamma-powered distribution comes from the classifier-free guidance. In practice, people only aim to promote label alignment and keep high sample fidelity. Is it possible to go beyond the gamma-powered distribution?

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
This paper provides a comprehensive, well-founded exploration of classifier-free guidance, establishing it as a viable, efficient alternative to classifier-based guidance methods. By grounding CFG in a predictor-corrector framework, the paper not only enhances understanding of diffusion models but also opens new paths for controlling generative models with minimal complexity.

### Strengths
### 1. Theoretical Foundation: By framing CFG within a mathematical context, the paper provides a rigorous basis for understanding its behavior and optimizing its use in diffusion models.

### 2. Experiment Validation: The paper provides the experiments to support its methodology.

### Weaknesses
### 1. The paper explains the classifier-free guidance, but I did not see whether your method can boost the performance of the diffusion model compared to DDPM, DDIM, or the consistency model.

### 2. I do not see the benefit of your understanding of CFG. Whether your understanding of CFG can benefit the theory results of CFG?

### Questions
### 1. Whether your method can boost the performance of the diffusion model compared to DDPM, DDIM, or the consistency model.

### 2. What's the benefit of your understanding of CFG? Whether your understanding of CFG can benefit the theory results of CFG in [Fu24]?

[Fu24] Unveil Conditional Diffusion Models with Classifier-free Guidance: A Sharp Statistical Theory

### Soundness
3

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
3

### Summary
The paper aims to investigate the theoretical foundations of classifier-free guidance (CFG). It disproves common misconcepts by  using counterexamples to show that CFG does not generate gamma-powered distribution, and CFG interacts differently with DDPM and DDIM. The  paper shows that CFG is equivalent to a particular kind of predictor-corrector that combines one step of DDIM denoiser with one step of Langevin dynamics in the gamma-powered distribution.

### Strengths
1. The paper disproves the misconcepts about CFG using counterexamples.
2. The paper provides a new understanding of CFG from the perspective of predictor-corrector guidance.

### Weaknesses
1. In page 3, the authors state that `` This gives a principled way to interpret CFG: it is implicitly an annealed
Langevin dynamics''.  What is the exact annealing path of the associated annealed Langevin dynamics? It seems not clear to me that CFG can be directly associated with  annealed Langevin dynamics as the predictor and corrector correspond to different limiting distributions and the corrector take only one Langevin dynamics. 

2. The interpretations of Theorem 1 and 2 are not clear stated. Is CFG-DDIM always tends to be sharper than CFG-DDPM, or it just because the special construction used in Theorem 1 and 2?

3. What is the potential usefulness of the derived results in further theoretical analysis of diffusion model?

### Questions
Is it always true that  a larger $\gamma$ and more Langevin dynamic steps in the corrector can lead to sharper distribution?

### Soundness
2

### Presentation
3

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
This paper focuses on the theoretical understanding of classifier-free guidance (CFG), a widely used technique in conditional sampling with diffusion models. The authors argue that the theory of CFG has been somewhat misunderstood, presenting counterexamples using 1D toy models to support their claim. They show that CFG can be explained by a predictor-corrector (PC) sampling algorithm with different annealing distributions. In particular, they introduce the predictor-corrector guidance (PCG) and suggest that CFG with DDPM sampling is equivalent to PCG with DDIM sampling. In this framework, the predictor is set as DDIM and the corrector is set as Langevin dynamics with a gamma-powered distribution.

### Strengths
* The paper points out that the theoretical understanding of CFG is lacking, considering its widespread practical use. The analysis of how different distributions correspond to different guidance scales could be helpful for practical applications.

* The statement of CFG with DDPM through predictor-corrector sampling, where Langevin dynamics serve as the corrector, is intuitive and reasonable.

### Weaknesses
 * The paper provides only informal theorems, so it is unclear what specific statements the authors intend to make within the scope of their work.
  * The theorems are incomplete and difficult to fully understand. In particular, the notation used in the statements is not well-defined (e.g., what is meant by c=0?), and the assumptions necessary to satisfy these theorems are not properly discussed.
   * Specifically, in my opinion, the additional claim in Theorem 1 that the DDIM variant is exponentially sharper than the DDPM variant is based solely on the counterexamples, which may lead to an overstatement in its current form.
   * For Theorem 3, the analysis only covers CFG with DDPM, so a clearer statement regarding this limitation is needed.

* While the relationship between CFG and PCG is explained, the reasons why CFG works are not adequately addressed.
  * There is a lack of sufficient analysis regarding PCG. As the authors themselves note, unlike the conventional PC algorithm, PCG operates with different annealing distributions for the predictor and corrector. Thus, the effectiveness of PCG should be explained with an analysis based on these different annealing distributions. For example, the effect of different annealing distributions on the final sampled distribution is not discussed. I believe this analysis is crucial because it ties into the argument that CFG works with a sampling distribution that deviates from the conventional intuition.
  * In explaining CFG in terms of PCG, the authors assume that the difference in timesteps between the predictor and corrector tends to zero, but the implications of this assumption are not sufficiently discussed or analyzed.
  * In Line 465, the paper mentions that CFG and PCG are qualitatively similar and claims that the results are consistent with the theory. However, looking at the quantitative metrics in Table 1, there appears to be a difference, so I question whether this statement is valid.

* CFG is known to be effective for image-condition alignment. It would be beneficial to include experimental results, such as quantitative metrics for image-text alignment in text-to-image diffusion models such as Stable Diffusion.

### Questions
* Please provide the authors' responses to the points listed under "Weaknesses".
* Algorithm 2 states that the noise prediction model uses the same timestep for both the DDIM step and the Langevin dynamics step. Is this correct?
* Minor comments
  * I believe that Eq. 2 should be expressed as a proportional relationship.
  * In Line 131, the paper states that it primarily considers the VP diffusion process, but the counterexamples seem to primarily focus on the VE diffusion process.

### Soundness
3

### Presentation
2

### Contribution
2
