Now I have sufficient calibration data. Let me write the consolidated review.

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), a dataless regularizer for weight disentanglement in task arithmetic. The key insight is that representation-drift regularization simplifies to a quadratic form of the Jacobian Gramian under model linearization, which is identified as an instance of the generalized Gauss-Newton (GGN) matrix. This connection enables the use of KFAC (Kronecker-Factored Approximate Curvature) to tractably approximate the regularizer without requiring external task data. The paper further proposes a Kronecker accumulation heuristic that merges per-task curvature factors into a single surrogate, achieving O(1) memory and runtime complexity in the number of tasks. Experiments on vision (CLIP ViT backbones on 8 Vision benchmark) and language (T5-base on 6 NLP tasks) demonstrate SOTA performance on task addition and negation, robustness to task-vector rescaling, and practical efficiency.

## Strengths

1. **Dataless regularization that matches or exceeds data-dependent methods.** The derivation (Eq. 3) shows that under linearization, representation drift reduces to a quadratic form of the pre-computed Jacobian Gramian, eliminating the need for external task data during fine-tuning. Tables 1 and 2 confirm that TAK achieves SOTA results on both task addition and negation while being dataless (✓), unlike τ‑Jp which requires data from other tasks (✗). For example, on ViT-L/14, TAK achieves 99.3 normalized accuracy vs. τ‑Jp's 98.5 (Table 1), and on task negation, TAK achieves lower target accuracy (3.4–3.5 vs. 3.7–6.7) while better preserving control accuracy (Table 2).

2. **Constant complexity in the number of tasks.** The Kronecker accumulation heuristic (Eq. 8) merges per-task KFAC factors into a single Kronecker product, yielding O(1) memory and runtime. Table 3 shows this heuristic closely matches (and in some cases slightly exceeds) the naïve O(T) multi-task formulation across both ViT-B/16 and T5-base.

3. **Robustness to task-vector rescaling, eliminating held-out tuning.** Figure 4a shows TAK maintains high accuracy across α ∈ [0, 2], while other merging strategies (TA, TSV, ISO, TIES) degrade sharply. Table 1 shows TAK with α=1 is nearly indistinguishable from tuned α, a significant practical advantage.

4. **Sound theoretical connection between representation drift and curvature.** Sections 3.1–3.2 cleanly derive that the drift regularizer is identical to the generalized Gauss‑Newton matrix under squared loss, enabling the import of decades of curvature-approximation research (KFAC) into the task-arithmetic setting.

5. **Empirical validation of task localization.** Figure 5 shows that for TAK-regularized task vectors, the quantity ‖Jθ f(x,θ₀)τt‖₂² concentrates near zero for out-of-distribution inputs, providing direct evidence of weight disentanglement.

6. **Practical efficiency and low overhead.** KFAC estimation for all 8 Vision tasks takes only 3.9 minutes (MC=1, Figure 6b). Block-compression reduces KFAC storage by 87% (550 MB → 70 MB) with only ∼1-point accuracy drop (Figure 7b). The regularizer adds only about one-third the overhead of τ‑Jp.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Kronecker accumulation heuristic lacks theoretical characterization.** The approximation in Eq. 8 — ∑_t B_t ⊗ A_t ≈ (∑_t B_t) ⊗ (∑_t λ_t A_t) — is not generally correct, and the paper provides no analysis of the conditions under which it holds or fails. While Table 3 provides strong empirical evidence that it works across the tested settings, a reader cannot assess whether it would remain reliable in regimes with highly heterogeneous factors (e.g., tasks with very different Jacobian structures). The authors should at minimum discuss when the approximation might degrade.

2. **Non-linear regime extension is empirically motivated but lacks theoretical grounding.** The derivation (Eq. 3) depends on model linearization, yet TAK is applied to attention-only fine-tuning (a non-linear regime). The paper acknowledges this ("our regularization is not theoretically exact in the non-linear regime") and appeals to "kernel-like" behavior of attention-only FT, but provides no formal argument or bound on the approximation error. This limits the reader's ability to predict when the method would break down for architectures or tasks where attention-only FT does not produce near-linear dynamics.

3. **No standard deviations or confidence intervals for main results.** Tables 1, 2, and 3 report point estimates without variance across runs. Given the known variability in fine-tuning outcomes (especially for smaller backbones like ViT-B/32), it is impossible to assess whether the reported gaps between TAK and τ‑Jp, or between TAK and the diagonal GGN, are statistically significant. The paper should report results across multiple seeds.

4. **Language results presented via radar charts rather than tabular summaries.** Figure 3 uses radar charts which show relative trends but make precise quantitative comparison difficult. The paper states that full tables are in the appendix, which is acceptable for supplementary material, but including a compact tabular summary in the main text would strengthen the language-domain evidence.

### Trivial
None.

## Nice-to-Haves

- **Standard deviations** for main accuracy numbers across multiple seeds would substantially increase confidence in the results.
- **A brief discussion of privacy implications** of sharing KFAC factors: while the method avoids sharing raw data, the KFAC factors (input covariance matrices) could potentially leak information about the training distribution. This would strengthen the "dataless" framing's intellectual honesty.
- A **theoretical bound or approximation-error analysis for the accumulation heuristic** (Eq. 8), even a simple covariance-diagonalization argument, would make the heuristic less ad hoc.

## Removed Points

These points were flagged by reviewers but are removed as they do not constitute valid weaknesses:

1. **"Comparison with 'no regularization' in the non-linear regime"** — The paper already shows this: Table 1 reports Attn. Only FT (80.4 on ViT-B/16) vs. Attn. Only FT + TAK (84.3), which is a direct comparison with and without regularization in the non-linear regime.
2. **"Data-free claim requires nuance about privacy risks"** — Moved to Nice-to-Have above. The paper's claim is about avoiding *data access during regularization*, which is accurate; the privacy implication is a reasonable discussion point but not a flaw in the methodology.
3. **Generic concerns about "unfair comparison"** — The paper's comparisons are fair and standard for the task arithmetic literature. No asymmetry favoring the author's method was found.
4. **Style/formatting nitpicks** — Parser artifacts, not author errors.

## Novel Insights

The harsh critic and strength finder together surface a clear insight that neither captures alone: the paper's central intellectual contribution is the *parallel* it draws between two previously separate literatures — representation-drift regularization in task arithmetic and generalized Gauss-Newton curvature approximation in optimization. This parallel is not merely analogical; it is exact under the squared loss, meaning the paper can directly import decades of KFAC research. The accumulation heuristic (Eq. 8), while theoretically crude, is made practically viable by the empirical observation that KFAC factors are sufficiently similar across tasks (implied by the small gap in Table 3). This suggests a deeper property: the pre-trained Jacobian's structure constrains the GGN factors across tasks more than one might expect, which could be a research direction in itself.

## Suggestions

1. Report all main results (at least Tables 1 and 2) with means and standard deviations across 3–5 random seeds.
2. Add a paragraph discussing the limitations of the Kronecker accumulation heuristic and the conditions under which it might fail (e.g., highly heterogeneous task Jacobians).
3. Include a concise tabular summary of language results in the main text alongside (or replacing) the radar charts.
4. Strengthen the non-linear regime narrative by framing it explicitly as an empirical finding rather than a core claim, or provide a more rigorous justification (e.g., a bound on the regularization error under attention-only FT).

## Score and Decision

### Calibration Protocol

**Round 1 — Bracketing.**
- Weak anchors (avg < 3.5): Task Vector Bases (3.33), Orthogonal Updates for Continual Learning (3.00). These papers have significant flaws or very limited contributions.
- Middle anchors (3.5–7.5): EWC-LoRA (6.00, Accept Poster), Curvature-Informed Model Merging / OTA (6.00, Reject), Neural Collapse in MTL (6.50, Accept Poster), KeepLoRA (5.50, Accept Poster), GMF-Mean (5.33, Reject), Taming Curvature (6.00, Accept Poster).
- Strong anchors (> 7.5): Off-topic (RL, rotation estimation, text-to-3D).

Initial bracket: between ~5.5 and ~7.5.

**Round 2 — Narrowing.**
I compared the paper in detail against the most relevant anchors:

- **vs. EWC-LoRA (6.00, Accept Poster)**: The current paper has stronger novelty (connecting representation drift to GGN is a new insight, whereas EWC-LoRA applies an existing method to a new setting), more comprehensive evaluation (vision + language, task addition + negation, extensive ablations), and clearer theoretical grounding. The current paper is clearly stronger.

- **vs. Curvature-Informed Model Merging / OTA (6.00, Reject)**: That paper requires Adam optimizer statistics (a training artifact) and was criticized for limited architecture scope. The current paper operates without training artifacts, tests multiple architectures (ViT-B/32, B/16, L/14, T5-base), and has stronger theoretical foundations. It also avoids the key practical limitations flagged in that paper's reviews.

- **vs. GMF-Mean (5.33, Reject)**: That paper's reviews identified significant theoretical concerns about the assumptions underlying its formulation and insufficient empirical validation of its central claims. The current paper's claims are better supported.

- **vs. Neural Collapse in MTL (6.50, Accept Poster)**: The current paper has a similar level of theoretical soundness but greater practical impact (directly useful for model merging practitioners rather than primarily theoretical).

The paper under review is stronger than all the 6.0-range anchors. However, it does not reach the 8.0+ level of the strongest papers (which tend to introduce fundamentally new paradigms or solve long-standing open problems). The missing standard deviations and limited theoretical analysis of the accumulation heuristic prevent it from being an exceptionally strong paper.

**Final score: 7.0** — corresponding to a solid Accept (Poster). This places it above EWC-LoRA and Neural Collapse in MTL (both ~6.0), and well above the rejected curvature-informed merging paper. The score reflects strong theoretical grounding, convincing empirical results, practical efficiency, and appropriate acknowledgement of limitations — offset by the absence of statistical variance reporting and the heuristic nature of the Kronecker accumulation.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>