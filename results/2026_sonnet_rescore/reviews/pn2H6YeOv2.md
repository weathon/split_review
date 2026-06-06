## Summary

PI-CCA introduces a replay-free continual learning framework for vision-language models that reframes catastrophic forgetting as alignment-geometry drift. Rather than distilling proxy signals (logits, similarities), it maintains a compact, constant-memory certificate of the top-*k* canonical correlations and canonical subspaces of the whitened image-text cross-covariance via EMA-updated streaming estimates and random sketch projectors. A prompt-invariance loss averages canonical subspace projectors over prompt perturbations to reduce sensitivity to phrasing. Evaluated on MTIL, X-TAIL, VLCL, and ConStruct-VL, PI-CCA achieves state-of-the-art performance among replay-free methods and surpasses a synthetic-replay competitor (GIFT) on retrieval and structured concept tasks.

---

## Strengths

- **State-of-the-art on all four benchmarks under replay-free constraint.** Tables 1 and 2 show PI-CCA attains the highest step-averaged accuracy on MTIL (76.8 vs. 75.2 for C-CLIP), X-TAIL (68.1 vs. 67.4 for RAIL), best VLCL I2T R@1 (48.6±1.0), and best ConStruct-VL FA/AF (75.2±1.3 / 2.7±0.2). Notably, it surpasses GIFT (47.3±1.2 I2T R@1), a synthetic-replay method using diffusion-generated pairs, while remaining generator-free.

- **Ablation establishes that both spectral and subspace alignment terms are necessary.** Table 3 shows that removing $\mathcal{L}_\text{spec}$ costs 2.5 pp on MTIL Avg and 2.3 on VLCL R@1; removing $\mathcal{L}_\text{sub}$ costs 2.2 pp and 2.7 pp respectively. These are the two largest individual drops in the ablation, directly supporting the claim that both the spectrum and subspace dimensions of the CCA geometry need to be preserved.

- **Prompt-invariance mechanism demonstrably improves robustness.** Fig. 4 shows that $\mathcal{L}_\text{pi}$ flattens the accuracy decay curve under increasing perturbation strength $s$. At $s=1.0$, R@1 is +2.44 pp (ID) / +2.51 pp (OOD) higher with $\mathcal{L}_\text{pi}$, and AF is reduced by ~1.1 / 0.96 points. The OOD template curves show similar trends, validating the projector-averaging mechanism beyond its training distribution.

- **Thorough task-order sensitivity analysis.** Fig. 5 evaluates 20 independently shuffled MTIL sequences (11 domains, 3 seeds each) and reports narrow interquartile ranges (Avg span ~76.0–77.4%, Last span ~74.5–76.0%). This analysis is frequently omitted in competing papers and significantly strengthens confidence in the generality of the results.

- **Efficient Pareto profile.** Fig. 2 maps memory, step time, and MTIL Avg over a grid of $(k, h)$ configurations and identifies a stable Pareto ridge around $k \in [48, 96]$, $h \in [192, 320]$, with $(k,h)=(64,256)$ near the knee of the efficient frontier, confirming practical deployability.

---

## Weaknesses

### Fatal
None.

### Major

- **The geometry → performance correlation (Fig. 3) is self-referential, not cross-method evidence.** Section 4.3 states: "We sweep realistic perturbations (certificate size, EMAs, invariance strength, whitening, pairing, LoRA capacity/LR, sketch type)." All of these are PI-CCA's own hyperparameters, and PI-CCA's training objectives ($\mathcal{L}_\text{spec}$ and $\mathcal{L}_\text{sub}$) directly minimize $D_\text{ang}$ and $D_\rho$. Consequently, configurations where the regularization is weaker will simultaneously exhibit higher geometry drift and lower performance — not because geometry drift causally governs performance, but because both are downstream effects of the same regularization strength. A Pearson $r = 1.00$ from an internal hyperparameter sweep of one's own method is an indication of this circularity, not an empirical law. To support the causal claim that "stability of the canonical subspace/spectrum reliably predicts downstream performance" (§5), the paper would need to measure geometry drift on diverse *baselines* (ZSCL, C-CLIP, Mod-X, etc.) under a common measurement protocol and show that methods with lower geometry drift rank higher in performance regardless of mechanism. The current analysis cannot distinguish "CCA geometry drift predicts performance" from "stronger regularization of any kind reduces forgetting." The framing in Fig. 3 and the conclusion in §5 therefore overstate what the data can support.

### Minor

- **No confidence intervals or seeds for MTIL and X-TAIL results (Tables 1).** Table 2 (VLCL, ConStruct-VL) includes ±s.d. across seeds, but Table 1 reports single numbers for all classification-track baselines. Margins over the second-best method on MTIL (1.6 pp) and X-TAIL (0.7 pp) are small enough that variance information matters for the state-of-the-art claim. This is standard to report.

- **Memory cost of streaming covariance EMAs is not explicitly accounted for in the efficiency analysis.** Section 3.4 (Eq. 12) maintains three full covariance matrices $\Sigma_{vv} \in \mathbb{R}^{d_v \times d_v}$, $\Sigma_{tt} \in \mathbb{R}^{d_t \times d_t}$, $\Sigma_{vt} \in \mathbb{R}^{d_v \times d_t}$. For CLIP ViT-L/14 with $d_v = d_t = 768$, this amounts to roughly three 768×768 matrices (~14M floats, ~56 MB in FP32), substantially exceeding the sketch cost itself. The paper's "constant-memory" claim is technically correct (memory does not grow with tasks), but the Pareto efficiency narrative in Fig. 2 accounts for certificate size while leaving this dominant background cost implicit.

- **The abstract's claim of "resilience to style shifts" is broader than what the prompt invariance stress test measures.** Section 4.3 uses "token-level synonym swap / back-translation / template jitter" as perturbations. These are in-distribution variations of the same caption style. Genuine style shifts (medical reports vs. web captions, VQA phrasing vs. descriptive captions) are meaningfully harder and more application-relevant. The abstract and conclusion should qualify this claim to match the actual evaluation scope.

### Trivial

- **Code is unavailable during review** (stated explicitly in the reproducibility section). Given the method's multiple interacting components (EMA stop-gradient, differentiable SVD via block power iteration, prompt perturbation sampling, sketch normalization), reviewers cannot verify implementation matches the description. This is a stated constraint, not an oversight, but it is a real limitation.

---

## Nice-to-Haves

- The single most impactful analysis to strengthen the paper's theoretical narrative would be to measure $D_\text{ang}$ and $D_\rho$ on saved checkpoints from the baselines (ZSCL, C-CLIP, Mod-X, etc.) and plot them in the same scatter plot as Fig. 3. This requires only inference passes and would transform the geometry→performance correlation from an internal consistency check into genuine cross-method evidence.

- The prompt-invariance story would be substantially stronger with a domain involving genuine style variation (e.g., medical captions vs. web captions for the same images, or VQA-style descriptions vs. CLIP-style templates), even in a small-scale pilot, rather than perturbations confined to synonym/template variation within one caption style.

- Reporting the exact covariance EMA memory cost alongside the sketch cost in Fig. 2 would make the efficiency comparison more transparent and honest.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Framing of prior work as 'regularizing outcomes' is overstated" (Harsh Critic, Introduction note):** The distinction is a matter of degree and the paper acknowledges that methods like Mod-X are "geometry-inspired." However, the characterization is a reasonable rhetorical framing in an introduction and not a factual error. Removed as a Minor nitpick on framing rather than a substantive weakness.

- **"GIFT comparison fairness / does GIFT's additional access imply different task difficulty":** The paper explicitly footnotes GIFT as "synthetic replay" (Table 2 footnote †), making the asymmetry transparent. Since the unfair comparison, if any, favors GIFT (it has extra generative access), and PI-CCA still wins, this is intentionally asymmetric to prove a stronger point. Per hard rules, removed.

- **"Requesting theoretical proofs for why CCA invariants are the 'right' invariants":** The paper is an empirical systems paper. Demanding formal guarantees goes beyond the community standard for this type of contribution. The paper defers to §A.4 for theoretical supporting material. Removed per soft rules (moved to nice-to-have territory regarding cross-method evidence).

---

## Novel Insights

The most genuinely novel observation is that *projector averaging* over prompt perturbations (Eq. 5–6) eliminates sign and rotation ambiguity within the canonical subspace without needing Procrustes alignment — a neat, practically motivated solution to a subtle problem in CCA-based continual learning. Additionally, the paper demonstrates that a replay-free method operating at constant memory can outperform diffusion-augmented synthetic replay (GIFT) on retrieval tasks, which suggests that the quality of the alignment invariant maintained — rather than data diversity — is the binding constraint in this regime. The task-order robustness analysis over 20 shuffled MTIL sequences (Fig. 5) is unusually thorough and sets a reproducibility standard worth highlighting.

---

## Suggestions

1. **Reframe or replace Fig. 3.** Either (a) add geometry drift measurements for at least three baselines (ZSCL, C-CLIP, Mod-X) to show the correlation holds cross-method, or (b) explicitly label the current scatter plots as "within-PI-CCA hyperparameter sweep" and weaken the causal language in §4.3 and §5 ("predicts" → "correlates with, within the PI-CCA family").

2. **Add seed-level variance to Table 1.** Report mean ± s.d. over at least 3 random seeds for MTIL and X-TAIL, matching the standard used in Table 2. Even if confidence intervals slightly change the picture, they are expected at this venue.

3. **Account for covariance EMA memory in the Pareto analysis.** Add a horizontal annotation or footnote to Fig. 2 indicating the fixed ~56 MB background cost from the three full covariance EMAs, so the memory axis is fully interpretable.

4. **Qualify the "style shift" claim in the abstract.** Change "resilience to style shifts" to "resilience to prompt/template variations" to match the actual scope of the stress test in §4.3.

---

## Evaluation on Key Axes

- **Originality:** High — applying CCA-geometry preservation as a first-class invariant in VL-CL is a principled and underexplored direction. The prompt-invariant projector-averaging mechanism is novel.
- **Importance of research question:** High — replay-free continual learning for VLMs is a pressing practical problem with clear deployment implications.
- **Claims well-supported:** Mostly — empirical performance claims are well-supported across four benchmarks with thorough ablation. The causal geometry→performance claim is overstated relative to the evidence.
- **Soundness of experiments:** Good — four benchmarks, component-wise ablation, efficiency Pareto, 20-order sensitivity sweep. Main gap is lack of confidence intervals in Table 1.
- **Clarity of writing:** Good — the method section is technical but precise; the certificate construction is clearly described.
- **Value to research community:** High — delivers SOTA on standard benchmarks, provides a clean geometry-first framework that future work can build on, and includes unusually thorough robustness analyses.

---

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>