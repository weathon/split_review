Here is my final consolidated review.

---

## Summary

This paper proposes MT-Diffusion, a generalization of DDPM to multi-modal/multi-task settings. The core contribution is a multi-task variational lower bound (Theorem 1) that extends the standard DDPM ELBO to handle heterogeneous modality data via a shared diffusion space with modality-specific encoders and decoders. Experiments on masked-image training, joint image-label generation, image transition, and joint image-representation generation are presented.

## Strengths

1. **Principled multi-modal ELBO that reduces to standard DDPM (Theorem 1, Eq. 4–6, Remark 1):** The paper derives a multi-task variational lower bound with four explicit terms. Remark 1 correctly notes that when N=1 (single modality), the L₂ term vanishes and the loss reduces to standard DDPM. This is a clean, principled generalization, not a heuristic combination of losses.

2. **Closed-form posterior with tractable multi-modal aggregation (Theorem 2, Eq. 11–14):** The posterior q(z_{t-1}|z₀,z_t,X) retains the Gaussian form of standard DDPM while incorporating an explicit aggregation term Σᵢ w_t⁽ⁱ⁾Eᵢ(xᵢ). This is a non-trivial theoretical property that keeps training tractable.

3. **MT-Diffusion-X shows large training efficiency gains on ImageNet-64 (Table tab:scores):** At 1M iterations, MT-Diffusion-X achieves FID=9.85 vs. ADM (class-cond) FID=16.35, both trained from scratch with identical hyperparameters. This is a substantial improvement, demonstrating that multi-task masked-image training can accelerate convergence for the conditional variant.

4. **Constrained image restoration achieves near-perfect LPIPS scores (Table tab:recovery):** MT-Diffusion achieves LPIPS 0.035–0.133 across masking levels vs. SDEdit- at 0.400–0.513 and the Clean-Masked baseline at 0.311–0.491. This demonstrates a concrete new capability — inpainting that preserves unmasked regions — enabled by the multi-task formulation.

5. **Practical encoder-decoder design framework (Section 3.2.3, Figure 3):** The paper specifies three encoder scenarios (identity mapping, pretrained generator, U-Net cross attention) and explicit decoder designs (MLP head for labels, convolutional head for images), following a principle of reusing existing components. This makes the framework directly implementable.

6. **Classifier accuracy benefit from joint generative training (Figure 4, lines 261–266):** In the joint image-label experiment, the classifier from MT-Diffusion-E consistently outperforms the baseline classifier finetuned from the released ADM checkpoint, showing that the generative multi-task objective also improves discriminative performance.

## Weaknesses

### Major

1. **Central claim contradicted by key evidence.** The paper's headline claim (abstract, line 36) is that MT-Diffusion can "achieve simultaneous generation without hurting individual task performance." The cleanest controlled comparison — MT-Diffusion-U vs. ADM (un-cond) on ImageNet-64 (Table tab:scores) — shows MT-Diffusion-U achieves FID 26.00 vs. ADM's 23.22, which is *worse*. The paper states "both the two variants significantly outperform the unconditioned ADM" (line 256), which is factually incorrect for MT-Diffusion-U on FID, sFID, and recall. Similarly, without finetuning, MT-Diffusion-M (FID 33.92) and MT-Diffusion-E (FID 41.00) are dramatically worse than single-task ADM (16.35). On ImageNet-128 with classifier guidance (Table tab:convergence_com), MT-Diffusion_g achieves FID 8.06 vs. ADM_g* at 3.56 — a factor of ~2 worse. The competitive results (FID 3.51, 11.28, 13.48) all require *post-hoc single-task finetuning*, which undercuts the claim that multi-task training itself preserves performance. This is the most serious weakness: the paper's core claim is not supported by the evidence.

2. **Weak baseline for the constrained image restoration task (Table tab:recovery).** The paper compares MT-Diffusion against SDEdit- and acknowledges SDEdit- "is not specifically designed for such a task" (line 257). Meaningful baselines would be dedicated inpainting methods such as RePaint (Lugmayr et al., 2022), LaMa, or diffusion-based inpainting that conditions on unmasked regions. The comparison against a method acknowledged as unsuitable for the task is uninformative and does not establish superiority over reasonable alternatives.

3. **Missing results for a claimed contribution.** Joint image-representation generation (item 4 in the introduction, line 32) is listed as a contribution, but no results — not even the promised qualitative results — are presented in the paper. The experiments section (line 153) only describes image transition and defers to "mostly qualitative" results, but Figure 3 shows image transition (night2day/cityscape), not image-representation generation. This claimed experiment is absent.

4. **The best FID scores (2.15, 2.02) come from a different task and should not anchor the same comparison table.** In Table tab:convergence_com, MT-Diffusion* and MT-Diffusion_g* report FID 2.15 and 2.02. The caption acknowledges these are from "the constrained image restoration task with 10% random masking" and are "not directly comparable." These results use 90% of the ground-truth image as input — a fundamentally different (and easier) problem than unconditional or class-conditional generation. Including them in the same table as unconditional generation numbers (where the best ADM gets 8.46–3.56) is misleading regardless of the footnote, as it visually implies superiority.

### Minor

5. **Forward aggregation weights w_t⁽ⁱ⁾ are never specified.** Equation (4) introduces weights w_t⁽ⁱ⁾ for each modality at each timestep, and the entire forward aggregation mechanism (Theorem 2, Eq. 6) depends on them. The paper never states whether these weights are learned, fixed to a constant, time-dependent, or how they are set in experiments. This makes the forward aggregation underspecified and the method not reproducible as described.

6. **No variance or statistical significance reported.** All tables report single point estimates with no error bars, no information about number of runs, and no indication of statistical significance. Given that several comparisons hinge on modest differences (e.g., MT-Diffusion FID 8.42 vs. ADM FID 9.62 at 128×128), this is a meaningful omission.

7. **The paper overclaims scope.** Line 146 states "all the tasks considered in the literature can be accomplished with our MT-Diffusion framework." This is an unsupported overstatement given the paper only tests two-modality settings on a subset of possible multi-modal configurations.

8. **Image transition and image-representation experiments lack quantitative evaluation.** The night2day and cityscape results are purely qualitative with no quantitative metrics. For a paper submitted to a top venue, qualitative-only results for claimed contributions are insufficient.

### Trivial

9. Line 256: "It is observed both the two variants significantly outperform the unconditioned ADM" — as noted above, this is inaccurate for MT-Diffusion-U on FID. The wording should be corrected.

## Nice-to-Haves

- A controlled experiment isolating single-task vs. multi-task training as the only variable (keeping architecture, hyperparameters, and compute identical) would directly test the paper's central claim. Currently, MT-Diffusion-U (the closest to this ideal) shows worse FID.
- Separating the constrained restoration results (starred entries in Table tab:convergence_com) into their own table with proper inpainting baselines would improve clarity and fairness.
- Comparison against latent diffusion models with conditioning mechanisms (which also handle heterogeneous data) would strengthen the positioning.

## Removed Points

The following points raised by reviewers were filtered out:

- **"The theoretical generalization collapses to adding auxiliary losses"** — This is an interpretive opinion, not a verifiable weakness. The paper derives a genuine multi-modal ELBO, and reducing to simpler components under specific assumptions is standard practice.
- **"No comparison against other multi-modal generative frameworks"** — The paper scopes itself as an initial investigation on multi-modal diffusion. Requesting comparisons with all multi-modal frameworks is scope creep.
- **"The heterogeneous setting is not very heterogeneous"** — Image+label is genuinely heterogeneous (discrete label space vs. continuous image space). The critic's dismissal of this is not accurate.
- **Missing related works concerns** — I cannot verify the existence of missing references.
- **Formatting, typos, and presentation style concerns** — These are parser artifacts, not author errors.
- **Reproducibility nitpicks about undisclosed hyperparameters beyond w_t⁽ⁱ⁾** — The paper provides substantial implementation details; only w_t⁽ⁱ⁾ is a genuine specification gap.
- **"Classifier accuracy baseline is weak"** — While comparing against a finetuned checkpoint rather than a state-of-the-art classifier from scratch is not ideal, this is a comparison against the same classifier used in the ADM codebase, which is standard practice. Demoting to Nice-to-Have territory.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a consistent pattern: the theoretical framework is legitimate, but the experimental evidence is significantly weaker than the claims made for it, and several design choices inflate the apparent performance.

## Suggestions

1. Correct or remove the claim that "both variants significantly outperform the unconditioned ADM" — it is false for MT-Diffusion-U on FID.
2. Run a controlled experiment where the only variable is single-task vs. multi-task training, keeping architecture, compute, and hyperparameters identical, and report results honestly.
3. Replace SDEdit- with proper inpainting baselines (RePaint, LaMa, conditioned diffusion inpainting) for the constrained restoration task.
4. Specify how w_t⁽ⁱ⁾ is set in experiments — learned, fixed, time-dependent, or constant.
5. Move the starred entries (constrained restoration results) out of Table tab:convergence_com into their own table with appropriate task notation and baselines.
6. Either provide the promised qualitative results for joint image-representation generation or clearly state that this experiment is deferred to future work.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>