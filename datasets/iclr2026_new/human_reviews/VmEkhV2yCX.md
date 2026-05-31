## Human Reviewer 1

### Summary
This paper challenges the conventional practice of adding reasoning data only during fine-tuning. Through controlled experiments, it demonstrates that front-loading diverse reasoning data into pretraining creates an advantage that cannot be matched by later stages.

Their key findings are:

1. Pretraining benefits most from scale and diversity of reasoning data, building broad and robust foundational capabilities.
2. SFT is dominated by data quality, where small amounts of high-quality, long chain-of-thought data are vastly more effective than large, diverse but lower-quality mixtures. Naively scaling SFT data with mixed quality can even be detrimental.
3. High-quality pretraining data has a latent effect, where its full benefit is "unlocked" only after the subsequent SFT phase.

The study concludes that a strategic, asymmetric data strategy—prioritizing diversity in pretraining and quality in SFT—is essential for building more capable and efficient reasoning models.

### Strengths
1. The authors present a systematic and thorough experimental setup, including baseline comparisons, multiple data regimes (scale, quality, diversity), and evaluation across a broad suite of reasoning benchmarks and domains (math, science, code, general reasoning). This breadth of empirical evidence is a clear strength.
2. The central finding—that diversity in reasoning data benefits pretraining most, while data quality dominates SFT effectiveness—is supported by clear quantitative results (e.g., Tables 1, 2, and 3), providing a practical guideline for future LLM training recipes.
3. The paper performs extensive ablation studies (Section 5), specifically investigating scaling strategies, catch-up hypotheses, and the latent effects of high-quality data. For example, Table 4 rigorously compares the effects of doubling SFT data versus diverse pretraining.

### Weaknesses
1. The description of data volume is highly unclear. In Section 2.2, $D_{LDQ}$ is described as containing 336B tokens, while $D_{SHQ}$ is described as containing 1.2M samples. It is also unclear exactly how much base data and reasoning data each model used during the pretraining phase, especially for the $M_{SHQ}$ model. 
2. The results in Tables 2, 3, and 5 only report the average scores of the three models pretrained with reasoning data. However, Table 1 has already demonstrated significant performance differences between the base models of LDQ and SHQ. The authors should provide the complete results for each individual model group across all tables.
3. The experimental results in this work lack validation across different model scales and on the more widely adopted Transformer architecture.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Summary
This paper investigates the stage to introduce reasoning data into the training process of Large Language Models (LLMs). The authors challenge the conventional approach of adding reasoning skills during the post-training stage and  argue for incorporating it early on, during pretraining.

### Strengths
1. This paper provides a detailed comparison of pretraining with $\mathcal{M_{LDQ}}$, $\mathcal{M_{SHQ}}$, and a mixture of both, thoroughly evaluating their impact on the model's performance across different reasoning tasks after pretrain and SFT. 
2. This paper shows that introducing reasoning data in pretrain stage can improve model performance in both pretrain stage and SFT stage 
3. This paper demonstrates that the SFT stage should leverage higher-quality data with greater reasoning depth to significantly enhance the model's final performance.

### Weaknesses
1. All the performances are evaluated in reasoning tasks, the performance on the memry task are not evaluated.
2. The paper does not clearly specify how the $\mathcal{M_{LDQ}}$ and $\mathcal{M_{SHQ}}$ datasets were mixed to create $\mathcal{M_{LMQ}}$ (especially ratio). It would be important to investigate whether different mixing ratios significantly impact the model's performance, and specifically, whether an optimal ratio exists that would allow $\mathcal{M_{LMQ}}$ to outperform $\mathcal{M_{LDQ}}$.

### Questions
1. The objective in Equation 1 requires clarification. The notation $E_{t \sim \mathcal{T}}$ is ambiguous as to whether a single fine-tuned model is evaluated across all tasks in $\mathcal{T}$, or if a unique model is fine-tuned specifically for each task $t$.
2. Why choosing a hybrid model, is the conclusion the same for Decoder-only transformer?

### Soundness
2

### Presentation
2

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper investigates the benefits of adding reasoning data earlier during pretraining. The authors vary the scale, diversity and quality of the reasoning data and show that front-loading reasoning data into pretraining stage not only builds better pretrained models but also synergies with subsequent post-training. They also show that diversity of the reasoning data is crucial for pretraining, whereas quality is important for SFT stage.

### Strengths
- The paper systematically studies the effects of front-loading different types of reasoning data (in terms of quality and diversity) into pretraining, which is novel and timely.

- The experiments are conducted at a large-scale and evaluated on diverse downstream tasks, which makes the conclusions more practical.

- The finding that high-quality pretraining data shows benefits only after SFT is interesting.

### Weaknesses
1. Major: 'Scale and diversity of the reasoning data are important in pretraining' is not well supported. D_{LDQ} and D_{SHQ} are from different datasets, and scale and diversity is not the only difference. The content of the dataset, as well as the quality of the dataset, are likely to be confounders. I think a more controllable comparison is to reduce the size and diversity of D_{LDQ} (-->D'_{LDQ}) and compare M_{LDQ} and M'_{LDQ}.

2. Minor: Some observations remain to be better understood, for example why exactly pretraining benefits more from diversity and SFT betnefits more from quality.

### Questions
1. Is D_{res} always 20% of the data (mentioned at Line 189)? If yes, why there are different scales of reasoning datasets (D_{SHQ} and D_{LDQ})? Can you clarify?

2. How is the ratio of reasoning data decided? Did you try other ratio (higher or lower than 20%) and does that affect your conclusions? 

3. What is D_{LLQ}? at Line 171-172? It seems not defined.

4. Line 349-350, could you explain why D_{SHQ} is mentioned, should it be D_{LMQ}?

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

## Human Reviewer 4

### Summary
The paper studies when to introduce reasoning-style data in the LLM pipeline. Using an 8B hybrid Mamba-Transformer trained from scratch for 1T tokens, the authors compare injecting reasoning data during pretraining vs. during SFT (and then RL). Core findings: (1) adding diverse reasoning data early (during pretraining) creates durable advantages that post-training cannot “catch up” to (reported ~19% average gain on expert benchmarks); (2) an asymmetric allocation principle: diversity & scale matter most in pretraining, while quality (long CoT) dominates SFT; (3) naïvely scaling mixed-quality SFT data can hurt reasoning; (4) some high-quality pretraining effects are “latent” and only unlock after SFT.

### Strengths
Comprehensive empirical study. Thorough, well-controlled experiments quantify how reasoning data affects both pretraining (PT) and post-training (SFT/RL).

Actionable principle. Clear rule of thumb: prioritize diversity and scale of reasoning signals during PT; prioritize quality (e.g., long, high-fidelity CoT) during SFT—immediately useful for practitioners.

Cross-stage validation. Systematic swaps across PT/SFT/RL (controlling data type/quality/scale) repeatedly confirm the “front-loading” thesis, with consistent gains (Tables 1–6).

Informative negative result. Simply doubling mixed-quality SFT data provides no benefit and can degrade math performance, underscoring that quantity cannot replace quality.

Latent PT benefit. A small amount of high-quality reasoning introduced in PT yields improvements that only manifest after SFT, clarifying stage interactions.

### Weaknesses
External validity & dataset specificity. The pretraining relies on NVIDIA-curated corpora (~6.2T tokens) and SFT sets such as OpenThoughts and Nemotron-Pretraining-SFT-v1. It’s unclear how well the conclusions transfer to other pretraining bases or fully open corpora.

Clarity on PT/SFT data mixing and table notation. For Tables 2–3, please spell out the exact SFT composition used during post-training for each pretraining variant and standardize the notation. In Table 4, the meaning of SFT×2 is ambiguous: is the dataset literally duplicated (two passes over identical examples) or expanded with additional unique samples? If duplicated, did the model simply see the same data twice (risking overfitting), and was the token budget controlled elsewhere?

Breadth vs. alignment trade-off. Length-filtered long-CoT SFT (DALF) appears to improve reasoning while weakening instruction-following. Any concrete hypothesis (e.g., length effects, stylistic drift, or distribution shift) plus diagnostics on this?


Pretraining mixture definition (80% D_base / 20% D_res). The paper states: “we pretrain from scratch for 1T tokens using 80% D_base and 20% D_res.”  how is that 20% constructed on different reasoning dataset settings?  If any sampling strategy is used? Please clarify this.

### Questions
see weakness

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