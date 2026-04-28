# Separate and Diffuse: Using a Pretrained Diffusion Model for Better Source Separation

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
The problem of speech separation, also known as the cocktail party problem,
refers to the task of isolating a single speech signal from a mixture of speech
signals. Previous work on source separation derived an upper bound for the
source separation task in the domain of human speech. This bound is derived for
deterministic models. Recent advancements in generative models challenge this
bound. We show how the upper bound can be generalized to the case of random
generative models. Applying a diffusion model Vocoder that was pretrained to
model single-speaker voices on the output of a deterministic separation model leads
to state-of-the-art separation results. It is shown that this requires one to combine
the output of the separation model with that of the diffusion model. In our method,
a linear combination is performed, in the frequency domain, using weights that are
inferred by a learned model. We show state-of-the-art results on 2, 3, 5, 10, and 20
speakers on multiple benchmarks. In particular, for two speakers, our method is
able to surpass what was previously considered the upper performance bound.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a diffusion-based post-processing module for single-channel speech enhancement. The authors present a mathematical derivation of the upper-bound of the source-to-distortion for generative methods, proving an improvement over the bound derived for deterministic models in prior work. They also present an architecture that combines the discriminative estimation and the generative estimation in the Fourier domain, which consists of a separation module, a generative module, and a mixing weights prediction module. Empirical results on a number of popular speech separation architectures on two speech separation datasets with multiple speaker numbers demonstrate the effectiveness of the proposed approach.

### Strengths
The idea of diffusion-based separation has been applied in speech separation, but the primary novelty of this work lies in the mathematical perspective of improving the SDR upper-bound with the generative approach by combining the output of the discriminative and generative estimations.

The experiments are conducted across several different separation architectures and for two popular source separation datasets (with several speaker-number settings), and an ablation study of the mixing network is performed. The empirical results demonstrate the improvement of the proposed method with deterministic SOTA on speech separation.

### Weaknesses
My major concern about the current version of this manuscript is the clarity of the writing. There are a number of notations (e.g., $v_r, v_{gr}, v_{dr}$) that are used across multiple sections of the paper, but these notations are not easy to follow and the consistency could be improved. In particular:

- Introduction could be clearer with all variables properly defined with types (real vs complex), and dimensions. Additionally, I suggest beginning with some motivation (reiterating parts of Section 2) but focusing on the bottleneck of the existing (deterministic and discriminative) approaches.

- Please make sure to define the acronyms at the first usage (e.g., SDE in Section 2, GM in Section 3.1).

- Please resolve the inconsistency
  - notations between the opening paragraph ([$\alpha_i, \beta_i$] = F($\bar{v}_d^i, \bar{v}_g^i$) vs ([$\alpha_i, \beta_i$] = F($\bar{V}_d^i, \bar{V}_g^i$) in (4).
  - $I(m_r, v_r)$ --> $I(m_r; v_r)$ in (6).
  - $p(v_{d}r) --> p(v_{dr})$ in Section 3.1.
  - The notations of $v_{gr}, \bar{v}_{gr}$ and $v_{dr}, \bar{v}_{dr}$ in Section 3.

- In (10): it seems there is overloading of the notation $p(v_{gr})$ on LHS and RHS of the equation.

- The font size of the equations and figure labels could be improved.
  - In Figure 4 (a), the x-label "MSE" is in italics, whereas for (b) it is not.
  - I would recommend disabling the italics for function names such as "argmax", "ELBO", "SDR", "log", etc.

### Questions
- I'm uncertain on how the two inequalities in (11) are derived. For the first inequality, how is $I(v_r; v_{gr})$ related to $I(v_r; v_{dr},v_{gr})$ in (9)? The necessary condition for the second inequality is $I(v_r; v_{gr}, v_{dr}) \leq I(v_r; m_r)$, but this is not implied from (7) or (9). It would be helpful if the authors could clarify the steps. Also, it'll be helpful to explain how the "3.0" db is obtained in (21).

- Any reason for transposing the horizontal and vertical axes for the visualizations in Figure 5? It is conventional to display the spectral information in the vertical axis and temporal dimension horizontally.

Update after rebuttal: I'd like to thank the authors for addressing the questions. The scores have been updated.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method for the source separation problem. First, a discriminative model is used to produce output sources. Then a generative model is used to refine those signals conditioned on the output of the discriminative model. Finally, a learned mixing coefficient is used to blend between the generative and discriminative outputs.

### Strengths
Overall I appreciate the method and the author's approach to using generative models. Generative models have shown strong performance in many areas and their use in source separation has been somewhat limited. I also appreciate the theoretical analysis which provides solid justification for the choices and results.

The ablation study shows that the the mixing network is in fact helpful, since the naive approach would be to just use the generative output v_g directly.

It is also nice that the authors use a variety of discriminative models and compare them, which shows that the method is general. 

The output audio examples provide a good sense to the listener of the model's performance

### Weaknesses
The main issue I have is the usefulness of the theoretical bounds given the underlying assumptions. The paper build heavily on the analysis in Lutati et al. where the bounds were derived by making assumptions on the context used. These assumptions provide a bound that is not realistic, as evidenced by the fact that the bound for WSJ2 mix is 23.1dB but TF-Gridnet achieved 23.4dB gain using purely a discriminative complex valued model. This is something that should be discussed in the paper more. The theoretical analysis relies on a chunking approach with assumptions of uncorrelated chunks, which does not align with the time-frequency processing of models like TF-GridNet. This discrepancy undermines the practical relevance of the derived bounds, as they do not reflect the performance of state-of-the-art methods. The paper should explicitly acknowledge this limitation and discuss the implications for the applicability of the theoretical results. Furthermore, the analysis does not seem to account for the non-stationarity of real-world audio signals, which is a significant factor in source separation performance. The assumption of uncorrelated chunks is a strong simplification that may not hold in practice, especially for speech signals with temporal dependencies.

### Questions
I would like to see an ablation where only the generative output is used after conditioning on the discriminative output (not a simple average like the current ablation). Have you done those experiments and how did they perform?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a single-channel speech separation method using a combination of deterministic and generative models. An upper bound on the signal distortion ratio (SDR) of this combined method is derived, suggesting that it has the potential to be better than the deterministic model alone.

### Strengths
1. The authors innovatively integrate deterministic models with generative models for speech separation and theoretically demonstrate the performance boundaries of this approach.
2. To address the phase shift issue between the output estimates of the deterministic and generative models, an alignment network is employed to estimate two parameters for the fusion of the outputs from both models.
3. Results across multiple datasets and models indicate that this method can further improve the performance of existing models.

### Weaknesses
1. **Generative Model Selection:** The authors' choice of utilizing only one diffusion-based generative model to validate the performance enhancement brought by noise introduction appears to be limiting. Although the theoretical incapacity of deterministic generative models to achieve performance enhancement has been demonstrated, the naturalness in generation by HiFiGAN is inherently lower than that of DiffWave. This raises concerns about whether this disparity is the reason for HiFiGAN's lack of improvement. I would recommend the authors consider incorporating other diffusion-based generative models, such as FastDiff [1], or superior deterministic models like UnivNet [2], to bolster the robustness of their results. Specifically, the authors should investigate whether the observed lack of improvement with HiFiGAN is due to its deterministic nature or its lower generation quality compared to diffusion models. A more comprehensive evaluation across a range of generative models with varying architectures and generation capabilities is needed to isolate the impact of the generative model's characteristics on the overall performance.
2. **Deterministic Model Upper Bound:** I disagree with the notion that deterministic models possess an upper bound. Recently, TF-GridNet results surpassed the so-called upper bound of deterministic models, attaining an SI-SDRi of 23.4, which is strikingly close to the SepFormer + DiffWave model. It would be prudent for the authors to include results on TF-GridNet to underscore the necessity of noise introduction in diffusion-based generative models. Training a generative model alone can be computationally demanding, and might not be the optimal solution just for a marginal performance gain. The claim of a deterministic upper bound needs further scrutiny, particularly given the recent advancements in time-frequency domain methods. The authors should clarify the specific conditions under which this upper bound is applicable and acknowledge the limitations of this assumption in light of recent results.
3. **Alignment Network Concerns:** Regarding the alignment network, the authors utilize the relative phase difference between $V_g$ and $V_d$ as well as the phase of $V_d$ as inputs to align the phase of the fused output with $V_d$. This poses a question: Is the observed enhancement in model performance a result of the phase alignment between $V_g$ and $V_d$, or is it due to the introduction of additional parameters, i.e., the alignment network? Another hypothesis worth considering is if the alignment network, when directly using the phase of $V_g$ and $V_d$ as inputs, would produce a similar effect. The authors need to provide a more detailed analysis of the alignment network's contribution. It is crucial to determine whether the performance gain is genuinely due to the phase alignment or simply a consequence of increased model complexity. Ablation studies, varying the inputs to the alignment network, should be conducted to isolate the effect of each input component.
4. **Testing on Noisy Datasets:** One notable observation from the manuscript is its primary focus on clean datasets for evaluation. It would be beneficial to see how the proposed combined model performs on noisy datasets, such as WHAM! or the noisy version of Librimix. Evaluating on these datasets can provide insights into the model's robustness in more realistic scenarios, where environmental noise might significantly impact the performance of the generative model. Such an evaluation will offer a more comprehensive understanding of the model's real-world applicability and its ability to tackle inherent challenges posed by noisy environments. The evaluation should include a range of noise levels and types to thoroughly assess the model's robustness under diverse conditions.
5. **Training Concerns:** The manuscript should clearly specify whether the separation and generative models were involved in the training of the alignment network $F$.
6. **Symbol Representation:** Please ensure a consistent and standardized representation of symbols throughout the paper. Conventionally, vectors are denoted in boldface.

### Questions
My detailed questions are as described above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
