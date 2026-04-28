# Presto! Distilling Steps and Layers for Accelerating Music Generation

- Decision: Accept
- Avg Score: 7.25
- Scores: 8, 5, 8, 8

## Abstract
Despite advances in diffusion-based text-to-music (TTM) methods, efficient, high-quality generation remains a challenge. 
We introduce \textbf{\textit{Presto!}}, an approach to inference acceleration for score-based diffusion transformers via reducing both sampling steps and cost per step. 
To reduce steps, we develop a new score-based distribution matching distillation (DMD) method for the EDM-family of diffus ion models, the first GAN-based distillation method for TTM. 
To reduce the cost per step, we develop a simple, but powerful improvement to a recent layer distillation method 
that improves learning 
via better preserving hidden state variance. 
Finally, we combine our step and layer distillation methods together for a dual-faceted approach.
We evaluate our step and layer distillation methods independently and show each yield best-in-class performance. 
Our combined distillation method can generate high-quality outputs with improved diversity, accelerating our base model by 10-18x (230/435ms latency for 32 second mono/stereo 44.1kHz, 15x faster than comparable SOTA)
--- the fastest high-quality TTM to our knowledge.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes "Presto!" for effective and efficient music generation. More specificly, Presto! is a set of model distillation techniques that aims at improving the inference efficiency of continuous diffusion models from two aspects:
1. overall inference steps,
2. runtime of each inference step.

The motivations and approaches are sound, and the results on the demo page are extremely convincing. Huge efforts have been done to applying latest SOTA methods to their own DNN architecture. Experiments are well designed to support the claims and motivations.

It is unfortunate that the authors do not plan to open their method, as I feel the framework is a little bit complex: it invovles extensive grid seearch for a better stability in adversarial training.

### Strengths
1. Very solid target: enhancing efficiency from both the number of steps and the runtime of a single ste.
2. novel to audio community to combine both step distillation and layer distillation, on top of the successful usage of an adversarial loss.
3. Clear presentation. The origin of the proposed techniques, and the differences between Presto! and prior arts are well explained. Related works are very up-to-date hence informative.
4. Great objective measurements. Presto! could outperform or keep on-par with the teacher model, while reducing the sampling steps to as few as 4, for the first time in audio community. The proposed continuous step distillation offers a more predictable performance gain when more inference budget is given.
5. Excellent subjective quality. The violin plot shows that Presto! outperforms Stable Audio Open and SoundCTM, two works published earlier this year, which is impressive. The samples in demo page sound great.

### Weaknesses
The ablation study indicates quite high complexity if we want to stably and effectively use Presto!. I am interested in how well the framework could be when applied to other VAEs or generator backbones, especially if no resource is open. The reliance on extensive grid search for stable adversarial training is a significant practical hurdle. The paper does not provide sufficient detail on the specific hyperparameter ranges explored during this grid search, making it difficult to assess the robustness of the method. Furthermore, the lack of information on the computational resources required for this search raises concerns about the accessibility of the proposed approach. It is also unclear how sensitive the performance is to variations in these hyperparameters, which could limit its practical applicability.

### Questions
Is it possible to open the implementation without sharing pretrained model weights? Or open a part of key tricks or components in the work?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an innovative approach to improve text-to-music generative models by significantly reducing inference time. Focusing on score-based diffusion models, the authors present two main contributions: first, a reformulated few-step synthesis approach utilizing online GAN-based adversarial distillation, adapted specifically for continuous time diffusion through the DMD2 framework; and second, a layer distillation technique, inspired by ASE, which uses a layer-budgeting module to prioritize layers based on noise levels.

They further explore the combination of step and layer distillation, demonstrating cases where the methods complement each other effectively. Their experiments, conducted on latent diffusion models with VAE and DiT blocks, use internal datasets for training and Song Describer for evaluation. Comparative analysis on the CLAP-LAION dataset with FAD scores shows that each method, independently and in combination, improves upon alternatives while maintaining real-time factor (RTF) performance.

### Strengths
This paper marks an important step toward a unified approach for faster generative models by bridging adversarial and diffusion methods for text-to-music tasks. In particular, Section 3.1 demonstrates this by applying GAN-based distillation to continuous-time score-based diffusion models. 

Aligning most distributions with the training distribution, as shown in Table 1, empirically improves all metrics, underscoring the robustness of their approach.

The authors also navigate the task of combining layer and step distillation, finding a highly effective recipe that substantially enhances generation speed. 

Achieving a 10-18x speedup in audio generation is a noteworthy accomplishment, positioning this collection of methods as a valuable resource for practical applications in the field.

### Weaknesses
While the paper is well-structured in a general sense, certain sections are hard to follow due to the level of detail. For example, Figure 1 is dense and, despite a detailed caption, remains challenging to interpret. The figure also uses various notations that lack prior explanation, making it difficult for readers to follow the intended process. Specifically, the lack of clarity around the precise mathematical operations and data flow within the distillation process makes it difficult to grasp the core mechanics of the proposed method. The use of terms like 'online GAN-based adversarial distillation' without explicitly defining the GAN architecture or the adversarial loss function further complicates understanding. The reader is left to infer these details, which hinders a clear comprehension of the methodology.

Additionally, the models are trained on internally licensed data, so the results cannot be easily referenced in future work. With no indication that the code will be released, reproducing this complex setup—including multiple models, distributions, and training phases—would be exceptionally difficult. This limitation means future researchers may be restricted to evaluating audio examples alone rather than building upon this work directly. The absence of publicly available datasets and code significantly restricts the ability to validate and extend the findings presented in the paper. This lack of transparency undermines the potential impact and reproducibility of the research.

### Questions
In line 35, does 5-20 seconds latency refer to 32 seconds audio? If yes, please clarify because it's mentioned in the abstract but not in the introduction.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a distillation method to develop a fast music generation model. The authors modify the [DMD2](https://arxiv.org/abs/2405.14867) and [ASE](https://proceedings.mlr.press/v235/moon24a.html) frameworks to improve the model performance. The proposed method not only enables a model to generate music signals with a few NFEs but also makes the model size smaller. The authors demonstrated that their trained model outperforms models trained/equipped with previous methods in terms of multiple evaluation metrics, using their in-house data for training and the Song Describer dataset for evaluation. They also conducted comprehensive ablation studies to show that their choices are reasonable.

### Strengths
1. The paper is well written. I could understand their motivation, the proposed method, and the experimental results.
2. The authors modified the existing DMD2 and ASE frameworks while conducting ablation studies. As ablation studies are comprehensive, readers can understand the reasons for the modifications/choices.
3. The authors demonstrated that the proposed distillation method works well in several aspects (AD, MMD, CLAP scores, and subjective evaluation) despite its fast generation.

### Weaknesses
I do not think that the paper has a critical weak point, but let me mention some weaknesses.

- Although the paper is well-written, some readers would struggle to reproduce the results without their code public. (I understand some institutes/companies do not make their code publicly available due to their policy.)
- Since the proposed training framework is general, I thought I would like to see experimental results in the text-to-audio generation task evaluated on AudioCaps. Furthermore, if we have a DiT-based baseline model for text-to-image or text-to-video generation, we can apply the proposed method to them. I thought I would like to see the performance in those tasks as well.
- The explanation of baselines in Section 4.1 is a little unclear to me. My understanding is that the authors trained the teacher model and applied the proposed technique and previous ones (CM, SoundCTM, DITTO-CTM, DMD-GAN, and ASE). For MusicGen and Stable Audio Open, they just downloaded and evaluated the official distributed models. Whether my understanding is correct or not, a clearer description would be appreciated.

### Questions
I would appreciate the authors' response to my comment in "Weaknesses".

### Soundness
4

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
5

### Summary
The authors propose Presto, a distilled diffusion-based text-to-music model. Specifically, they introduce Presto-S, a model that applies DMD2 to a text-to-music generative model, and Presto-L, a model that performs layer-based distillation by extending ASE. Additionally, they propose Presto-LS, which combines these two distillation techniques. Experimental evaluations demonstrate that all three models achieve high-quality and efficient text-to-music generation.

### Strengths
- The authors propose the first diffusion-based text-to-music distillation model to successfully incorporate GAN loss.
- They also introduce a layer-distillation method to reduce computational cost at each sampling step, which has not yet been explored in the text-to-music task.
- Additionally, they present a methodology for integrating these two orthogonal distillation techniques.
- The effectiveness of these three methods is demonstrated through extensive evaluation.

### Weaknesses
 - The explanation of Presto-L seems to assume prior knowledge of ASE, which is unfriendly for readers. For better readability and self-containment, it would be helpful to explain Presto-L more thoroughly by including an algorithm, equations, or an illustrative figure of the distillation process, as done for Presto-S. At the very least, a more detailed literature review of ASE should be provided. (ASE is a relatively new method presented at ICML 2024, and as the authors note in the last paragraph of Section 2, such layer-distillation methods have not yet been explored in text-to-music, underscoring the need for a detailed explanation)
- The contribution to the research community in terms of reproducibility is limited. Therefore, I strongly recommend either releasing the codebase or providing sufficient implementation details to facilitate straightforward replication, at least to allow future research to conduct follow-up studies (see also Questions).
    - While I understand from the reproducibility statement that the authors chose not to release checkpoints, it should still be feasible to release the codebase itself (as done in some prior works [1][2]) or to include sufficient implementation details for reproduction in the Appendix.

[1] Evans, Z., Carr, C.J., Taylor, J., Hawley, S.H. and Pons, J., 2024. Fast timing-conditioned latent audio diffusion. arXiv preprint arXiv:2402.04825.

[2] Evans, Z., Parker, J.D., Carr, C.J., Zukowski, Z., Taylor, J. and Pons, J., 2024. Long-form music generation with latent diffusion. arXiv preprint arXiv:2404.10301.

### Questions
- Around L90–L91 in Introduction, the authors mention TTA. Are there plans to conduct text-to-audio generation experiments during the rebuttal period?
   - If not, claiming it as a contribution in the Introduction is an overstatement.
- How exactly is the CFG-augmented real score, represented by $\tilde{\mu}^{w}_{\text{real}}$ in Eq (5), formulated?
     - Is it something like $\mu_{\text{real}}( \hat{x}_{\text{gen}}+\sigma\epsilon, \sigma, \varnothing) + w (\mu_{\text{real}}( \hat{x}_{\text{gen}}+\sigma\epsilon, \sigma, \bf{c}) - \mu_{\text{real}}( \hat{x}_{\text{gen}}+\sigma\epsilon, \sigma, \varnothing)$, $where $\bf{c}$ is condition?
- Section 3.1, L210–L211: Regarding “the fake score model is updated 5 times as often as the generator to stabilize the estimation of the generator’s distribution,” how robust is this to different model training setups, architectures, and datasets? For example, if the number “5” were changed to “4” or “6,” how significantly would it affect training stability and generation quality in those sense?
- Section 3.1, L212–L214: In “Specifically, a discriminator head $D_{\psi}$ is attached to the intermediate feature activations of the fake score network,” which specific part of the DiT block do the “intermediate feature activations” refer to? Also, how is the architecture of the discriminator head $D_{\psi}$ actually configured? The explanation in Section 3.2.3 is still high-level for both points. Could you provide further detail using pseudo-code or a figure illustrating the architecture?
- In Algorithm 1, $\nu_1, \nu_2, g_1, g_2$ are mentioned. What values do the authors set as $\nu_1, \nu_2$? Are both $g_1, g_2$ optimized with Adam at a learning rate of 1e-4? Also, do the authors use learning rate schedulers?
- How is Presto-L distilled? The explanation in Section 3.3 and $\mathcal{L}_{\text{st}}$ alone seem insufficient to clarify the distillation process. Could you provide a more detailed explanation using an algorithm table, pseudo-code, or a figure illustrating the distillation process?
- Since multi-step sampling uses stochastic sampling like CM, I would expect that as the number of sampling steps increases, sample quality will eventually plateau and then degrade if increased further. Have you observed such a phenomenon when increasing the number of sampling steps to around 15, for example?

### Soundness
4

### Presentation
3

### Contribution
3
