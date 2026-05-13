# DSPO: Direct Score Preference Optimization for Diffusion Model Alignment

- Decision: Reject
- Scores: 8, 6, 6

## Abstract
Diffusion-based Text-to-Image (T2I) models have achieved impressive success in generating high-quality images from textual prompts. While large language models (LLMs) effectively leverage Direct Preference Optimization (DPO) for fine-tuning on human preference data without the need for reward models, diffusion models have not been extensively explored in this area. Current preference learning methods applied to T2I diffusion models immediately adapt existing techniques from LLMs. However, this direct adaptation introduces an estimated loss specific to T2I diffusion models. This estimation can potentially lead to suboptimal performance through our empirical results.  In this work, we  propose Direct Score Preference Optimization (DSPO), a novel algorithm that aligns the pretraining and fine-tuning objectives of diffusion models by leveraging score matching, the same objective used during pretraining. It introduces a new perspective on preference learning for diffusion models. Specifically, DSPO distills the score function of human-preferred image distributions into pretrained diffusion models, fine-tuning the model to generate outputs that align with human preferences. We theoretically show that DSPO shares the same optimization direction as reinforcement learning algorithms in diffusion models under certain conditions. Our experimental results demonstrate that DSPO outperforms preference learning baselines for T2I diffusion models in human preference evaluation tasks and enhances both visual appeal and prompt alignment of generated images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The authors propose the first method to fine-tune text-to-image models on human preference that aligns pertaining and fine-tuning objectives, the benefit of which is shown by outperforming preference learning baselines on human preference tasks. The method is also shown to be equivalent with RLHF objectives in diffusion models under certain conditions.

### Strengths
1. The first method that fine-tunes diffusion models on human preferences using a score-matching, thus aligning with pretraining objectives, and the benefits are apparent through the baselines.
2. Clear presentation of related works provides the reader with ample context.
3. Comprehensive experiments covering supervised finetuning, diffusion-DPO, diffusion-KTO, and MaPO as baselines, evaluated with multiple scoring metrics, and includes evaluations on a recent model (SDXL).
4. The proposed method outperforms baseline methods across multiple datasets and scoring metrics.

### Weaknesses
1. Figure 3 looks cramped; the equations are pitted against other visual elements, making them hard to read

### Questions
1. In table 2, Diff.-DPO seems to have a higher score in the PickV2 dataset with the Pick Score Metric, but it’s not highlighted.
2. The paper shows the equivalence between the proposed method and RLHF, but it seems like the evaluation does not contain a direct comparison with a model that has been fine-tuned with RLHF.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new direct score preference optimization method for diffusion model alignment that utilizes a target human-preferred score function, thereby aligning the fine-tuning objective with the pretraining objective.

### Strengths
- The paper takes a different approach to aligning text-to-image diffusion models, motivated by score matching, which sets this method apart from the others.
- In terms of multiple open-source reward scores, DSPO demonstrates effectiveness in increasing reward values.

### Weaknesses
- In general, I find that many claims are too vague and ambiguous. When we examine the final loss of Diffusion-DPO and DSPO, how can we definitively say that one aligns with the pretrained loss of Stable Diffusion more clearly than the other? Additionally, why is aligning the diffusion model with direct reward optimization or RL considered suboptimal due to a mismatch in pretraining and fine-tuning objectives? Is there any theoretical justification beyond the win rates?
- In my opinion, since the method is based on human preference, a human evaluation should be conducted to confirm whether it truly increases the reward aligned with human preference. Relying solely on open-source reward model scores seems unreliable, as these models can carry inherent biases.
- Furthermore, why does the Diffusion-KTO result differ so significantly from the original paper? I think the authors should provide detailed explanations of their evaluation settings, including the seeds used, the number of images generated per method, and other relevant factors. Without this information, the results may appear unreliable.

### Questions
- In Figure 2, what baseline models were used to calculate the win rate? Is it the pretrained SD1.5 model?
- During evaluation, did the authors generate images from multiple fixed seeds and average the results over them, or do the results come from a single specific seed?

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
5

### Summary
The paper introduces DSPO, presenting a score-matching formulation for fine-tuning pre-trained diffusion models on human preference data. The authors argue that since existing preference alignment fine-tuning methods have a different objective than the pre-training objective, it can lead to sub-optimal results, and they demonstrate this with empirical evidence.

### Strengths
* The score-matching formulation for alignment fine-tuning of diffusion models hasn't been explored before, and the paper does a good job of exploring this direction. 
* The connection between the objective covered by the RLHF methods for diffusion models and DSPO.

### Weaknesses
* The paper misses out on using MaPO [1] as a reasonable baseline even though it considers contemporary works like Diffusion KTO. The reason why I think MaPO is important here to consider is because it has similar motivations and also either performs on par with Diffusion DPO or outperforms it under various settings. 
* Lack of experimental results on models like SDXL makes it unclear as to how scalable DSPO is and if it works for models other than SD v1.5. 
* The ablations lack experiments on some of the design choices the authors make to arrive at the final objective of DSPO. For example, they use the direct score function of the underlying data distribution as opposed to using that of $p_{ref}$, but they don't justify it with sufficient experimental results. 
* Pick-a-Pic v2 contains duplicate prompts. Did the authors perform any de-duplication? If not, I think it might be better to run at least a few experiments with de-duplication to check if this improves the results.

**References**

[1] Margin-aware Preference Optimization for Aligning Diffusion Models without Reference; Hong et al.; 2024.

### Questions
* Figure 2 could mention the base model on which the respective methods were applied.

* L099 - L101: The authors mention "... with existing baselines for preference learning in T2I diffusion models." However, Figure 2 compares the performance of a single base model on which the respective methods were applied. So, I think it's better to be specific and mention the base model in the statement.

* Equation 12 could benefit from an expansion of the notations used. For example, I don't know where $\lambda$ is coming from. Furthermore, it'd be beneficial to highlight the score function of the data distribution replacing $p_{ref}$.

* It's not clear how DSPO incorporates $\mathbf{x}_t^w$. Under Section 4.2, $\mathbf{x}_t^w$ only appears in Equation 14. 

* L091: Typo on "constraints". 

* SD1.5 is a relatively old model. Since DSPO doesn't consider other recent models like SDXL, SD3, Flux, etc., it's unclear as to how well DSPO generalizes. I can understand that providing further results on SD3 or Flux might be computationally challenging, but I request that the authors at least consider SDXL experiments. Additionally, LoRA fine-tuning (similar to how DPOK [1] does it) when doing DSPO for larger models like SD3 and Flux might help them quickly evaluate its potential better. 

* Are there any sample-efficient aspects of DSPO? More specifically, I am interested to see if using the score-matching perspective of alignment fine-tuning like DSPO does can improve alignment with fewer samples than other methods.

* The authors could also consider using human-benchmark arenas such as imgsys [2] for evaluation. 

* To assess the practical aspects of DSPO, it would be useful to report the wall-clock time and memory requirements of DSP and compare them against the existing methods. 

**References**

[1] DPOK: Reinforcement Learning for Fine-tuning Text-to-Image Diffusion Models; Fan et al.; 2023.

[2] imgsys; fal.ai team.

### Soundness
3

### Presentation
2

### Contribution
3
