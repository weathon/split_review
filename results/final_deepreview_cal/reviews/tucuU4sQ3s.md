Now I have all the information I need. Let me synthesize the final consolidated review.

**Round 1 Bracket:** Based on my initial calibration search, the paper clearly falls in the middle band — far above the weak anchors (2.00–2.50) and below the strong anchors (8.00–9.00). The plausible range is 5.5 to 7.5.

**Round 2 Narrowing:** Reading C-CLIP (6.50, Accept), PROOF (5.67, Reject), and TiC-CLIP (6.25, Accept) in full shows that NuSA-CL compares favorably to these anchors. It has a cleaner method than C-CLIP (single elegant idea vs. LoRA+CKC+distillation), better analysis (spectral dynamics in Figure 2), and stronger theoretical motivation. The main weakness (no variance) is shared with these anchors, but NuSA-CL compensates with more thorough ablations and analysis.

**Final Score:** 7.0 — solid Accept. The paper is positioned above C-CLIP (6.50) due to clearer methodology and better analytical depth, but below the exceptional 8+ papers which introduce paradigms or solve fundamentally harder problems.

---

## Summary

This paper introduces NuSA-CL, a memory-free continual learning method for vision-language models. The core idea is elegant: before each task, SVD is used to identify a low-energy (null) subspace of the current weight matrix, and all task-specific updates are persistently constrained to lie within this subspace via a frozen basis formulation ($\Delta W = U_n M V_n^\top$). After learning, the update is merged into the backbone, maintaining a fixed parameter budget. The method is evaluated on the MTIL benchmark (11-dataset sequence) and CIFAR-100 class-incremental learning, demonstrating strong performance with only 1.5M trainable parameters and zero additional storage — outperforming other storage-free methods (LoRA, MiLoRA) and rivaling storage-based approaches at a fraction of the cost.

## Strengths

- **Elegant and well-motivated method with clear theoretical grounding.** The null-space-constrained update is formalized through Lemma 1 and Theorem 2, which bound parameter-space interference. The persistent constraint (freezing $U_n, V_n$ and learning only $M$) is a clean design that the paper rigorously validates through ablation (Table 4a: removing the constraint drops Transfer from 68.58% to 62.60%).

- **Superior efficiency-performance tradeoff demonstrated across multiple benchmarks.** On the MTIL benchmark (Table 1), NuSA-CL uses 1.5M params (vs. LoRA's 15.7M, MoE-Adapters' 59.8M), zero storage, 6.6 GB peak GPU memory, and 1.21 GPU-hours, while achieving 68.6% Transfer, 75.1% Avg., and 82.8% Last — outperforming all other storage-free methods and rivaling storage-based ones. On 50-step CIFAR-100 CIL (Table 3), NuSA-CL achieves 71.85% Last accuracy, outperforming ZSCL by 4.4%.

- **Insightful analysis of learning dynamics.** Figure 2 provides direct quantitative evidence that NuSA-CL *accumulates* knowledge in underutilized spectral directions (effective rank increases across tasks), while LoRA and Full-FT merely overwrite existing structure. This turns a conceptual claim into a measurable phenomenon.

- **Thorough ablation study validating key design choices.** The paper methodically ablates: (a) subspace selection strategy (Tail vs. Top vs. Random across 5 ranks, Figure 3a), (b) persistent constraint vs. initialization-only (Table 4a), (c) multimodal vs. unimodal adaptation (Table 4a), (d) energy cutoff robustness across $\rho = 0.80$ to $0.999$ (Table 4b), and (e) maximum update rank (Figure 3b). These collectively demonstrate that each design choice is evidence-based.

- **Practical efficiency is demonstrated, not just claimed.** Table 4b shows SVD initialization takes <1 minute (vs. InLoRA's ~81 minutes), and performance is stable across a wide range of $\rho$ thresholds, showing the method does not require sensitive tuning.

## Weaknesses

### Major

- **No variance or statistical significance reported for any experiment.** All results in Tables 1–4 are single numbers without standard deviations, confidence intervals, or multiple seeds. This is especially consequential in Table 2 (5-shot MTIL), where NuSA-CL's improvements over InLoRA are often 1–3 points (e.g., Transfer 68.1 vs. 66.8, Last 75.4 vs. 74.8). Without error bars, the reader cannot assess whether these margins are statistically reliable or within run-to-run noise. The 5-shot setting is computationally light enough that 3 seeds would be standard practice, and even in the full-shot setting, reporting 2 seeds with a stability note would substantially strengthen the evidence. This is the paper's most significant weakness.

### Minor

- **The Transfer metric protocol is incompletely specified.** The paper defines Transfer as "the zero-shot accuracy on unseen tasks" (Section 5.1) but does not specify: (1) which datasets constitute the "unseen" set at each evaluation point, (2) whether evaluation happens after each individual task or only at the end, and (3) the precise aggregation procedure. While the MTIL benchmark is from prior work (ZSCL), the paper should be self-contained on this point. Additionally, NuSA-CL achieves Transfer (68.1% in Table 2) that *exceeds* zero-shot CLIP (65.3%) — a non-obvious result that the paper does not analyze or explain. This is a missed opportunity for insight rather than a flaw, but it does leave the reader wondering whether the metric might conflate seen and unseen evaluations.

- **The method's scope (attention projection matrices only) is stated late.** The paper specifies on line 292 (Section 6.3) that SVD is applied to $W_q, W_k, W_v, W_o$ matrices, but this is not mentioned in the Method section (Section 3). A reader implementing the method from Section 3 alone would not know which layers are adapted. This is a reproducibility concern that should be addressed upfront.

### Trivial

None that survive filtering.

## Nice-to-Haves

- A comparison with LoRA at a matched trainable parameter count (by reducing LoRA's rank) would help isolate whether the improvement comes from the null-space constraint or from parameter efficiency. The paper already demonstrates the efficiency advantage clearly; this would strengthen attribution of *why* NuSA-CL outperforms LoRA.

- An analysis of why Transfer improves over zero-shot CLIP (e.g., feature similarity on seen vs. unseen tasks) would turn an unexplained finding into a key insight.

- Task-order sensitivity experiments, acknowledged as future work in Section 7, would strengthen robustness claims.

## Removed Points

These are points from the input reviews that were removed with justifications:

- **"Missing discussion of prompt-based CL methods like L2P, DualPrompt"**: Removed per the rule against citing missing related work.
- **"Theoretical connection to forgetting is weak (parameter space not function space)"**: The paper explicitly acknowledges this limitation (Section 4: "should be viewed as a local stability condition rather than a full function-level guarantee"). A self-acknowledged scope limitation is not a weakness.
- **"Comparison with LoRA/MiLoRA at different parameter counts is unfair"**: Removed per the rule: the asymmetry favors NuSA-CL (fewer params, better performance), and the paper is proving a stronger point about efficiency.
- **"Zero-shot CLIP on Transfer tasks not reported"**: The zero-shot CLIP baseline on the 11 MTIL datasets IS reported in Table 2 (65.3% average). Since the Transfer metric evaluates on subsets of these same datasets, the baseline is implicitly available.
- **"Missing task order information"**: The paper acknowledges task-order sensitivity as future work (Section 7). This is a known limitation, not an oversight.
- **Various formatting, style, and typo nitpicks**: Removed per parser-artifact rules.

## Novel Insights

The paper's spectral dynamics analysis (Figure 2) provides a genuinely novel perspective on how continual learning methods interact with a model's parameter structure. The finding that LoRA and Full-FT leave the spectral footprint essentially unchanged (effective rank nearly constant) while NuSA-CL progressively fills underutilized spectral directions offers a measurable criterion for distinguishing "knowledge accumulation" from "knowledge overwriting" — a distinction that has been conceptually discussed in CL literature but rarely empirically demonstrated at the parameter level.

## Suggestions

1. Add variance estimates (at least 3 seeds) for the 5-shot MTIL experiments (Table 2) and the CIFAR-100 experiments (Table 3), where computational cost is manageable. Report mean ± std for summary metrics.
2. Document the Transfer metric protocol fully: which datasets are "unseen" at each step, when evaluation occurs, and how the aggregate is computed. Briefly analyze why Transfer exceeds zero-shot CLIP (e.g., does null-space adaptation strengthen feature representations for unseen tasks?).
3. State the scope of adaptation (attention projection matrices $W_q, W_k, W_v, W_o$) in Section 3 alongside the method description, not only in Section 6.3.

## Score and Decision

**Calibration Anchors Used:**

| Anchor ID | Avg Score | Round | Comparison |
|---|---|---|---|
| JIlIYIHMuv | 2.50 | 1 (weak) | Much weaker — rejected LVLM-CL paper with poorly motivated method |
| WM5G2NWSYC | 2.00 | 1 (weak) | Much weaker — rejected projected subnetworks paper |
| gNoqEdT2wO | 2.33 | 1 (weak) | Much weaker — rejected multimodal CIL benchmark |
| ZaudLwn0Hm | 2.50 | 1 (weak) | Much weaker — rejected prototypical evolution paper |
| k9NYnsC4Mq | 5.67 | 1 (mid) | Weaker — PROOF (LwF for VLMs), rejected due to inference mismatch and representation drift |
| 9aZ2ixiYGd | 5.00 | 1 (mid) | Weaker — Vision-Language Synergy, mixed reviews, relies on ChatGPT |
| sb7qHFYwBc | 6.50 | 1 (mid), 2 | Comparable/Weaker — C-CLIP, similar scope and approach, but NuSA-CL has cleaner method and better analysis |
| G9Ea7mlqGO | 3.80 | 1 (mid) | Weaker — rejected online CL paper |
| TLADT8Wrhn | 6.25 | 2 | Comparable — TiC-CLIP, different contribution type (benchmark paper), similar score |
| wE1I9IGqeH | 6.00 | 2 | Comparable — complementary memory systems, rejected despite 6.00 |
| 1aF2D2CPHi | 8.00 | 1 (strong) | Stronger — data-free KD, different problem scope |
| gc8QAQfXv6 | 9.00 | 1 (strong) | Stronger — function vectors for CF in instruction tuning, deeper theoretical contribution |

**Round 1 Bracket:** 5.5 – 7.5  
**Round 2 Narrowing:** The paper is strongest among the mid-band anchors. It is clearly better than PROOF (5.67, Reject) and Vision-Language Synergy (5.00, Accept), and compares favorably to C-CLIP (6.50, Accept) due to a more elegant method, stronger theoretical motivation, and more insightful analysis. The no-variance weakness is real but does not collapse the contribution. Placing the paper slightly above C-CLIP reflects these advantages.

**Final Score:** 7.0  
**Decision:** Accept

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>