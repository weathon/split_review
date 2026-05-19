Now I have all the information needed to produce the consolidated review.

---

## Summary

CONCORD introduces a training-free method for injecting instance-level semantic control into diffusion-based dataset distillation. The approach (1) retrieves fine-grained, discriminative concepts via LLMs for each category, (2) filters them through CLIP-based validity evaluation on real images, and (3) guides the denoising process with a contrastive objective that matches positive concepts while repelling negatives from similar categories. Applied to Minimax and unCLIP Img2Img baselines, the method shows consistent accuracy gains across ImageNet-1K, ImageNet-100, ImageWoof, and Food-101.

## Strengths

1. **Fine-grained concepts outperform class-name and classifier guidance (Table 6, Figure 3).** The contrastive objective with LLM-retrieved concepts achieves 67.7±0.9 (IPC=10) versus 66.4±0.8 for classifier guidance and 65.3±0.5 for the cosine-only objective. Figure 3 visually demonstrates that descriptive concepts (e.g., "legs covered in thick fur") control specific image details while class-name guidance collapses under increasing weight.

2. **Training-free and classifier-agnostic design.** The guidance is derived entirely from text concepts and a frozen CLIP encoder — no classifier training or fine-tuning is needed. This is validated in Table 6, where classifier guidance requires careful weight tuning (λ=0.05) and still underperforms the proposed approach.

3. **Consistent improvements across multiple baselines, datasets, and architectures (Tables 1–3).** CONCORD improves both Minimax and unCLIP baselines on ImageNet-1K (+3.4 points at IPC=1, ConvNet), ImageWoof, ImageNet-100, and Food-101 (+2–6 points across IPC settings). Results are reported with 3-run means and variances, and improvements hold across ConvNet, ResNet-18, and ResNet-101.

4. **Rigorous ablation of key design choices (Tables 5–6, Figure 4).** Negative concept selection (random vs. similarity-limited vs. weighted sampling), objective form (cosine vs. contrastive vs. classifier guidance), and hyperparameters (λ, number of negatives) are all systematically evaluated, providing practical deployment guidelines.

## Weaknesses

### Fatal

None.

### Major

1. **The λ hyperparameter value is stated inconsistently between the implementation and the parameter analysis.** Section 4.1 (Implementation Details) states: "The informing weight λ in Eq. 9 is set as 1." Section 4.4 (Parameter Analysis) concludes: "Through comparison, we set the value of λ as 2.0 for balance between sufficient control and stable denoising." This contradiction makes it unclear which value was used for the main results (Tables 1–3). If λ=1 was used, the paper's own analysis suggests the main results could be improved by switching to λ=2. If λ=2 was used, Section 4.1 is wrong. This must be clarified for the results to be reproducible and trustworthy.

2. **The use of CLIP embeddings on noisy diffusion latents is neither justified nor ablated.** The concept matching objective (Eq. 12) computes ψ(x^(t)) — CLIP embeddings of the *noisy* latent at arbitrary denoising steps. CLIP was trained on clean images, and its embedding space is not calibrated for the heavy noise present at early/intermediate timesteps. The paper already computes the clean estimate x̂^(0) (Eq. 8) as part of the DDIM sampler, but does not compare guidance on x^(t) versus guidance on x̂^(0). This omission weakens the mechanistic claim that "fine-grained concepts are being informed" — the observed improvements could partially stem from the gradient acting as an implicit regularizer on the denoising trajectory rather than from semantic concept matching. An ablation varying the guidance start step or substituting x̂^(0) for x^(t) in the objective would substantially strengthen the paper.

### Minor

3. **"State-of-the-art" claim is broader than the comparison set supports.** The paper claims SOTA performance on ImageNet-1K (abstract, Section 4.2) but compares only against diffusion-based methods (MTT, SRe²L, RDED, DiT, Minimax, Img2Img) and one non-diffusion method (MTT, which is meta-learning-based). Well-established non-diffusion distillation methods with strong ImageNet results are not included. Qualifying the claim as "state-of-the-art among diffusion-based methods" would be more precise and avoid overclaiming.

4. **No ablation on the number of concepts |C|.** The paper fixes |C|=5 without examining how performance changes with 1, 3, 5, or 10 concepts. Since the method's effectiveness depends on concept quantity and quality, this is a notable gap in the analysis.

5. **No ablation quantifying the benefit of CLIP-based concept validity filtering.** The paper retrieves an over-abundant set of concepts and filters by CLIP activation (Section 3.2), but never reports what happens if all retrieved concepts are used without filtering. This makes it impossible to attribute gains to the filtering step versus the concept set itself.

6. **Implementation detail: CLIP gradient computation is underspecified.** The paper does not state whether the gradient ∇_{x^(t)} O is computed by backpropagating through the full CLIP encoder or using a cached/stochastic approximation. The number of CLIP forward passes per denoising step and the resulting wall-clock overhead are not reported. This affects both reproducibility and the claimed practicality of the method.

7. **"Random" baseline in Table 3 is not defined.** The baseline likely means random selection from the original training set, but this is not stated. The fact that unCLIP underperforms random selection at 50 IPC is notable and unexplained — a brief discussion would strengthen the analysis.

### Trivial

None.

## Nice-to-Haves

- Ablate using random words or concepts from unrelated categories as the guidance signal to confirm that the *semantic content* of the concepts, not just the presence of a gradient, drives improvement.
- Report wall-clock time per distilled image with and without CONCORD, with a breakdown of CLIP vs. diffusion overhead.
- Analyze sensitivity of the guidance quality to the noise level (e.g., at which timestep t does CLIP-on-noisy-latent guidance become reliable?).

## Removed Points

- **"Prompt iteration concern" (Harsh Critic, Section-by-Section Notes):** The reviewer asked whether prompts were manually iterated to maximize performance. The paper already compares prompt designs (classification-style vs. their own) in Table 4 and reports using GPT-4. This concern is addressed by the existing ablation. **Removed.**
- **"The claim that 'merely imitating the real distribution' is insufficient is not supported by any experiment" (Harsh Critic):** This is a framing/rhetorical claim in the Introduction, not an experimental claim. The paper's experiments show that adding concept-informed guidance improves over distribution-matching baselines, which indirectly supports this premise. **Removed as too speculative about framing.**
- **"Missing related works" —** Not raised explicitly; not included per instructions.
- **Formatting/typography complaints —** None present in the inputs; none to remove.
- **Reproducibility concerns about unreleased models/tools —** The paper cites Minimax, unCLIP, GPT-4, CLIP. All are released/public. **Removed per hard rules.**
- **Strength Finder: generic strengths about "important problem" or "addressed important question"** — None present; all listed strengths are concrete and specific. **All kept.**
- **Strength Finder: "Parameter analysis provides practical guidelines"** — This is specific (Fig 4b, 4c) and grounded. **Kept.**

## Novel Insights

The two reviews converge on the paper's core strengths (clear idea, extensive experiments, consistent gains) and on the two dominant weaknesses (λ inconsistency and the unaddressed CLIP-on-noisy-latent design choice). A genuinely novel observation emerging from this synthesis is that the λ inconsistency creates an unusual tension: the main results may be *underestimates* (if λ=1 was used suboptimally), yet the CLIP-on-noisy-latent concern suggests the mechanism may be less semantically precise than claimed. These two issues pull in opposite directions — one suggesting the numbers could be better, the other questioning the narrative — but neither invalidates the observed empirical improvement. The paper would be significantly strengthened by resolving both, ideally in the same ablation (testing λ values with both x^(t) and x̂^(0) as the CLIP input).

## Suggestions

1. **Resolve the λ inconsistency explicitly.** State clearly which λ was used for each experiment (e.g., "All main results (Tables 1–3) use λ=2; Section 4.1 has been corrected"), or, if λ=1 was used, update the main results to λ=2 and discuss the difference.

2. **Add an ablation comparing guidance on x^(t) vs. x̂^(0) (the clean estimate from Eq. 8).** If performance is similar or better with x̂^(0), adopt it and justify the choice. If x^(t) works better, explain why (e.g., CLIP embeddings may be robust to moderate noise, or the gradient on noisy latents provides beneficial stochasticity).

3. **Qualify the "state-of-the-art" claim** to specify "among diffusion-based dataset distillation methods" unless additional non-diffusion baselines are added.

4. **Add ablations on the number of concepts |C|** (e.g., 1, 3, 5, 10) and on whether concept validity filtering helps (compare with/without filtering).

5. **Report the computational overhead** in practical terms: number of CLIP forward passes per denoising step per image, and wall-clock time per distilled image.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>