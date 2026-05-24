Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper presents the first systematic evaluation of adversarial example transferability across Multimodal Large Language Models (MLLMs) and proposes the Typography Augment Transferability Method (TATM), a data augmentation technique that adds typographic text to images during adversarial generation. TATM is motivated by two principles: increasing information diversity and editing across vision-language modalities. The method is evaluated across 13 victim MLLMs (5 model families) using 2 surrogate models on MS-COCO, compared against 8 augmentation baselines, and tested under single-prompt, cross-prompt, ensemble, multi-prompt, and Gaussian defense settings. Consistently across settings, TATM achieves the highest or near-highest Attack Success Rate / CLIPScore on the majority of victim models.

## Strengths

- **First systematic evaluation of cross-MLLM adversarial transferability with extensive baselines**: The paper evaluates 9 data augmentation methods (pixel-level and semantic-level) across 13 victim MLLMs spanning 5 distinct architectures (BLIP2, InstructBLIP, MiniGPT-4, LLaVA-v1.5, LLaVA-v1.6) with 2 surrogate models. This goes substantially beyond the sporadic validations noted in prior work.

- **TATM consistently ranks top-3 across most victim models**: In Table 1 (single-prompt, "suicide" target, InstructBLIP surrogate), TATM achieves the highest ASR on 9 of 13 victim models and is always top-3. Under the LLaVA surrogate it is top-3 on 10 of 13 models. The color-coded tables make this pattern clear and reproducible from the reported numbers. This directly supports the claim that TATM boosts transferability.

- **Quantitative metric (MADS) to justify information diversity**: Equation (1) defines the Multi-semantic Angular Deviation Score, and Figure 2(b) shows TATM yields the highest MADS among Admix, AIP, and Typo relative to pixel-level methods. This provides a principled, measurable rationale for why TATM is expected to work beyond just empirical results.

- **TATM extensions (ensemble and multi-prompt) consistently outperform baselines**: Figures 3 and 4 show that TATM combined with ensemble training and multi-prompt training outperforms the corresponding baselines across all 13 victim models (e.g., TATM+Ensemble beats base ensemble on 12 of 13 models), demonstrating flexibility in realistic black-box scenarios.

- **Strong performance under Gaussian defenses**: Table 3 shows TATM maintains top-tier ASR/CLIPScore under Gaussian noise and blur, often achieving the highest ASR across multiple victim models (VM1–VM8). This suggests the transferability gain is not fragile to simple input-level defenses.

## Weaknesses

### Fatal
None.

### Major

- **The ASR metric for the "Harmful Word Insertion" scenario conflates successful attacks with safe refusals.** The paper defines Attack Success Rate as the target word "suicide" appearing anywhere in the model's response (line 218). A model that responds "I cannot discuss suicide" or "If you are considering suicide, please seek help" is counted as a successful attack. This is a genuine confound. The paper frames the scenario as a jailbreak-like task (line 43: "similar to a Jailbreak in the context of Harmful Word Insertion"), but the metric does not distinguish between generating harmful content and safely mentioning the word. While the ASR metric is standard for *targeted attacks* (forcing the model to output a specific token), its framing as revealing "real-world harm" is not supported without supplementary analysis — e.g., manual inspection of a sample of successful outputs, or a stricter metric that also requires the absence of refusal language. This does not invalidate the transferability comparison (TATM still forces the word more often), but the paper's claims about real-world safety threats are overstated.

- **No ablation testing whether the *semantic content* of the typographic text matters.** The paper argues (lines 104, 129) that typography works because it causes "semantic distraction" and enables "meaningful augmentation of the language modality." However, the experiments never ablate this mechanism. Random character strings (e.g., "XXXXX"), non-word text, or text in a language unknown to the model would isolate whether the benefit comes from the visual presence of text (a high-salience visual pattern) versus the semantic content of the words. Without this control, the paper's mechanistic explanation is speculative — the consistent TATM advantage could simply reflect that adding rendered text is a stronger visual perturbation (like high-contrast texture), not a semantic one. This is fixable with a straightforward experiment and would substantially strengthen the paper.

### Minor

- **The algorithm description and the experimental setup are inconsistent on prompt selection.** Algorithm 1 (line 178) randomly samples a prompt from set *P* at each PGD iteration. However, the experimental setup (line 215) states "the prompt 'describe the image' is used by default during the optimization process of TATM." This ambiguity matters because the algorithm may appear to describe TATM-MultiP rather than default TATM, but the caption says "Typography Augment Transferability Method (TATM)" without qualification. The relationship between the default method, the algorithm, and the multi-prompt extension needs clarification.

- **The evidence for "cross-modal editing" is indirect.** The paper motivates TATM using the principle of "editing across vision-language modality information" (lines 88–98) and claims that TATM "achieves true semantic augmentation." However, the supporting analyses (PCA in Figure 2a, Grad-CAM in Figure 1c) both examine the *vision encoder's* representations, not the language model's internal states or the language output directly. The semantic similarity matching (Figure 2c) is more relevant but still operates through the vision encoder's embedding. The paper never directly measures whether the language side is being edited in a way that goes beyond what any visual perturbation would cause. This gap weakens the explanatory story but does not affect the empirical finding that TATM works.

- **Baseline hyperparameters for Admix (mixing ratio) and AIP (patch parameters) are not reported.** The paper cites the original papers but does not specify the implementation choices for these baselines (e.g., what fraction of the image is mixed, patch size). If these were not tuned, the comparison may not reflect these methods at their strongest. This is a minor reproducibility gap.

- **The defense evaluation is too narrow to support the claim that TATM "will not be compromised by some defense methods" (line 54).** Only two Gaussian defenses with fixed parameters (noise σ=0.005, blur kernel=3, σ=0.1) are tested. These are mild transformations. The paper should either acknowledge this limitation explicitly or qualify the claim.

### Trivial

- **The MADS formula (Eq. 1) is presented in an unnecessarily complex form.** The expression uses a complex exponential ($e^{i(\mu_m - \mu_j)}$) and then takes its argument, which reduces to $|\mu_m - \mu_j| \mod 2\pi$. It is also unclear from the text how the 2D vectors from PCA are obtained (the PCA reduces to 2D but the original embeddings are high-dimensional). A simpler exposition would improve readability.

## Nice-to-Haves
- **Confidence intervals or error bars.** Adversarial generation involves randomness (random typographic words, random transformations for DIM/SIA). Without any measure of variance, it is unclear whether small gaps (e.g., TATM 0.130 vs. Admix 0.083 on VM9 in Table 1) are meaningful. However, single-run evaluation is standard for large-scale attack experiments (~24h GPU time on an A40 for the full dataset), so this is not a required fix but a desirable improvement.
- **Testing on a second dataset.** The paper uses only MS-COCO; validating on ImageNet or a domain-specific dataset would strengthen generality.
- **A discussion of computational cost.** TATM adds text rendering and 1000 PGD iterations. The paper mentions 24-hour GPU time for 300 images but does not compare per-iteration cost against pixel-level methods.

## Removed Points

- *"The evaluation is not comprehensive (only 2 surrogate models, 1 dataset)"* — Removed. 13 victim models spanning 5 architectures with 9 methods is genuinely comprehensive for the victim side. The computational cost (24h on A40 for 300 images × 1000 iterations) makes multi-dataset evaluation challenging; this criticism is disproportionate.
- *"The claim about cross-modal editing is conceptually stretched — any perturbation affects the language output"* — Weakened to Minor (see above). The reviewer's claim that "any visual perturbation affects the final language output" conflates "affects" with "edits in a semantically meaningful way." Typography adds specific word content, which is a different kind of intervention from pixel noise. However, the paper's evidence for this distinction is indeed indirect, which is why the point survives in weakened form in Minor.
- *"Goh et al. is a blog post"* — Removed per policy: cited references are assumed to exist and be valid.
- *"Radar plots are hard to read"* — Removed (formatting/style nitpick).
- *"Conclusion lacks limitations"* — Removed. Standard for conference papers; not a meaningful weakness.
- *"MADS is never used in experiments"* — Removed. MADS is computed and presented in Figure 2(b) as part of the motivation/analysis. It is not used in the transferability comparison experiments, but the paper never claims it would be.
- *"Missing related works"* — Removed per policy (cannot confirm existence of missing references without external sources).

## Novel Insights

None beyond the paper's own contributions. The reviewers' main observations (the ASR metric's weakness for the "harmful" framing and the missing semantic ablation) are valuable methodological critiques but do not constitute novel insights about adversarial transferability itself.

## Suggestions

1. **(Critical)** Add a manual inspection or stricter metric for the "suicide" scenario. Randomly sample 50–100 responses counted as "successful" and report what fraction are genuine harmful generations vs. safe refusals. Alternatively, define success as: (a) the target word appears AND (b) the response does not contain refusal phrases (e.g., "cannot", "sorry", "not appropriate").

2. **(Critical)** Run an ablation comparing TATM with meaningful words against TATM with non-semantic text (e.g., "XXXXX", random character strings, or text in a language the MLLM does not process). Report whether the ASR drops. This directly tests whether the benefit is semantic or purely visual.

3. Clarify Algorithm 1: either separate the default TATM (fixed prompt) from TATM-MultiP (random prompt), or note that prompt sampling is only used in the multi-prompt variant.

4. Report the specific mixing ratio and patch parameters used for Admix and AIP baselines.

5. Qualify the defense claim (line 54) to explicitly state "against mild Gaussian noise and blur defenses" rather than "some defense methods."

## Score and Decision

**Originality:** Good. Typography as a data augmentation for adversarial transferability across MLLMs is novel. The systematic evaluation across 13 victim models is the first of its kind.

**Importance of research question:** High. Adversarial transferability across MLLMs is an underexplored but practically important security concern.

**Are claims well supported:** Partially. The empirical claim that TATM boosts transferability is well supported by extensive experiments. However, the framing of "real-world harm" via the suicide metric is not well supported, and the mechanistic claim about "semantic distraction" lacks a critical ablation.

**Soundness of experiments:** Good in breadth (13 victim models, 9 methods, multiple scenarios). Weakened by the metric issue and missing ablation.

**Clarity of writing:** Generally clear. Some presentation issues (MADS formula complexity, algorithm/setup inconsistency).

**Value to research community:** Moderate to high. Provides a strong benchmark for cross-MLLM transferability and a simple but effective method (TATM) that can serve as a baseline for future work.

**MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>**