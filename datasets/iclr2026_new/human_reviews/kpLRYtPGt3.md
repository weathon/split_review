## Human Reviewer 1

### Summary
The authors propose Neon, a self-training method that fine-tunes a base model using its own self-synthesized data with reversed gradient updates. Remarkably, Neon is effective even with as few as 1,000 synthetic samples. Its performance is validated across a wide range of architectures and datasets.

### Strengths
* Neon is simple to implement and effectively addresses common self-training challenges such as model autophagy disorder (MAD) and model collapse.

* The method is evaluated across a wide range of architectures—including diffusion, flow-matching, autoregressive, and momentum-matching models—and diverse datasets such as ImageNet, CIFAR, and FFHQ.

### Weaknesses
* The effectiveness of Neon hinges on the assumption that s < 0 (negative gradient alignment). However, this condition may not consistently hold in practice, raising concerns about the robustness of the approach.

* The hyperparameter configuration—particularly the training budget and negative extrapolation strength w —could introduce additional tuning complexity. Ablation studies in Figures 3 and 4 suggest that Neon is sensitive to these hyperparameters, which may impact its ease of deployment.

### Questions
* The key idea behind Neon—"synthetic degradation and real-data improvement point in opposite directions"—is intriguing. However, the current derivation of the supporting theorems appears loosely structured. Could you provide a clearer logical overview of how these derivations are organized? Additionally, how should this statement be interpreted intuitively in the context of model training? 

* In Figure 3, the FID increases as the self-training budget B grows. Does this suggest that extended training with Neon may lead to performance degradation? If so, does it challenge the assumption that s < 0 (negative gradient alignment) consistently holds?

* In the images presented in Appendices E through I, are these generated samples from the Neon self-trained models, or are they the synthesized images used during the self-training process? Could you clarify this distinction and provide an analysis of the synthesized images used for self-training? Additionally, a visual interpretation explaining why these images are effective in contributing to the self-training process would be highly valuable.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
The paper proposes NEON (Negative Extrapolation from self-traiNing): briefly self-train a generative model on its own samples to obtain degraded weights , then extrapolate backward from the degradation direction via a simple parameter merge . The authors give a theoretical account showing that common mode-seeking samplers create anti-alignment between synthetic and population gradients, so reversing the self-training direction reduces true data risk. Empirically, NEON improves diffusion, flow-matching, autoregressive, and few-step models on CIFAR-10, FFHQ, and ImageNet, often with <1% extra compute; notably it pushes xAR-L on ImageNet-256 from FID 1.28 → 1.02 with only 0.36% additional training compute.

### Strengths
Simple, general, post-hoc procedure that requires no extra real data, no auxiliary models, and no inference changes; just a short self-training run and a weight merge. 

Clear theory: formalizes sampler-induced anti-alignment and gives conditions where negative extrapolation lowers population risk; also analyzes failure cases (diversity-seeking samplers). 

Broad empirical coverage across diffusion, flow matching, AR, and few-step models with consistent FID gains; includes precision/recall analysis explaining NEON’s recall-boosting mechanism. 

Strong results with tiny cost (often ≤2% of base training compute; sometimes as low as 0.36%), and improvements with as few as 1k synthetic samples. 

SOTA highlight: ImageNet-256 xAR-L FID 1.02, plus useful studies on (w, γ) co-tuning and cross-architecture transfer of the degradation signal.

### Weaknesses
Positioning vs. simple weight merges: needs stronger comparisons to generic weight interpolation/extrapolation baselines (e.g., linear checkpoint merges/SWA-style extrapolation) to isolate NEON’s specific benefit beyond “negative LR step”. 

Benchmark scope: focuses on standard class-conditional/unconditional image generation; lacks large-scale text-to-image or broader modalities, and relies mainly on FID + P/R without human eval. 

Hyperparameter sensitivity: performance depends on w (and γ for AR/CFG); while grids are shown, guidance on automatic selection or stability across training checkpoints could be expanded.

### Questions
see weakness

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
Usually training/retraining generative models on synthetic data can degrade performance metrics. On the opposite, this paper proposed a technique to leverage (bad) synthetic data from generative models, and improve generation. This work is in the direct line of work following Karras 2024 and Alemohammad 2024.

### Strengths
The paper is well-written, and the idea is clearly explained. Experiments are overall rather well presented. Figure 2 explains well the approach.

### Weaknesses
- I do not understand the novelty with respect to previous works.
Could authors explain what is the difference between their work and [1] and mostly [2]? Especially, I really would like to better understand better the difference with [2]: the idea of using negative guidance from synthetic data is already in [2], in particular, Equation (1) of the proposed manuscript resembles line 4 in algorithm 1 of [2]. Are you doing SIMS, but in the parameter space? Could authors comment on that?
- How significant do you consider the empirical results? Can you show the same plots on test set, with the Dinov2 embedding?
- in particular I would be interested to see if the minimum value on the training set correlates with the minimum value on the test set


[1] Tero Karras, Miika Aittala, Tuomas Kynkäänniemi, Jaakko Lehtinen, Timo Aila, and Samuli Laine.
Guiding a diffusion model with a bad version of itself.

[2] Sina Alemohammad, Ahmed Imtiaz Humayun, Shruti Agarwal, John Collomosse, and Richard Baraniuk. Self-improving diffusion models with synthetic data


Non-scientific comment: I would remove the following quote, "In the words of Martin Luther King, Jr., “Sometimes to move forward, we have to go backward.”, used to motivate negative parameter guidance. It does not feel appropriate

### Questions
see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
5

---

## Human Reviewer 4

### Summary
In this paper, the author proposed a new self-training algorithm for image generative models NEON. Specifically, NEON uses synthetic images generated by the generative model to finetune the model, and use the performance degredation as a learning signal. The key insight is that most inference samplers are mode-seeking, biasing samples towards high-density regions of the model distribution, resulting in model collapasing, and worsens FID. Consequently, NEON uses negative extrapolation between the reference model and briefly self-trained model, avoids mode collapsing. The author tested their NEON algorithm across different generative models and datasets and shows consistent FID improvement with little computational overhead.

### Strengths
Overall, the paper introduces Neon, a simple but effective method that interprets self-training degradation as a useful signal for improvement. The approach is theoretically grounded and empirically validated across diffusion, flow, and autoregressive models.

- The core idea of reversing the direction of self-training degradation is both simple and effective. The implementation requires only a single weight extrapolation step and no architectural or loss modifications, making the method easy to implement and apply.
- Neon adds little computational overhead and scales well across model families. Its simplicity makes it readily to deploy in large-scale training pipelines.
- The experiments are thorough, spanning multiple datasets (CIFAR-10, FFHQ, ImageNet-256/512) and model architectures. Across all cases, Neon consistently improves FID and recall. The recall and precision analysis provided nice support to the theory of Neon. It treats precision for recall, encouraging diveristy by negative extropolation. 
- Ablations show that Neon’s benefits generalize across architectures and even compensate for reduced real data availability.
- The controlled toy experiment from the appendix effectively illustrate the theoretical predictions and help readers grasp the distinction between mode-seeking and diversity-seeking regimes.

I did not verify all derivations in detail, but at an intuitive level the theoretical claims are consistent and well-motivated. I defer to other reviewers for a closer assessment of the mathematical rigor and proofs.

### Weaknesses
- The paper does not include quantitative comparisons against other self-training baselinesin the precision/recall/FID analyses. Even showing results for the simplest baseline of direct self-finetuning would help clarify how much of Neon’s gain comes from the negative extrapolation itself versus the self-training process. Moreover, comparisons in terms of data and compute efficiency would contextualize Neon’s benefits relative to prior self-improvement algorithms.
- While the quantitative results are compelling, the paper would benefit from a few qualitative visual examples to illustrate how Neon changes the generative behavior. It remains a bit unclear whether the performance gains are purely distributional (i.e., improved diversity and recall) or also reflect higher fidelity and perceptual realism compared to naive self-training.

### Questions
- Can the authors provide qualitative visual examples to illustrate how Neon changes the generative distribution? Are the observed gains primarily due to improved diversity (recall), or do they also enhance perceptual fidelity compared to naïve self-training—or possibly hurt fidelity due to the diversity–precision trade-off?
- Can the author also include some baselines for the precsion/recall/FID analysis?
- Do the authors see Neon as applicable to other domains such as NLP generation?
- For figure 9, what is the synhetic dataset used samped from for the 30k model?

### Soundness
3

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
3