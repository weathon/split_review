Now I have all the information needed. Let me write the final review.

## Summary

This paper proposes TAK (Task Arithmetic with KFAC regularization), which connects representation-drift regularization for weight disentanglement to curvature approximation (GGN) and then exploits KFAC to make it practical. The key insight is that under model linearization, the representation drift penalty reduces to a quadratic form of the Jacobian Gramian, which is a GGN matrix. KFAC provides a tractable approximation, and a Kronecker-factor merging heuristic (Eq. 8) keeps the method's complexity O(1) in the number of tasks. Experiments on vision (CLIP ViT-B/32, B/16, L/14) and language (T5-base) show TAK matching or exceeding the data-requiring τJp baseline on task addition while outperforming all methods on task negation.

## Strengths

- **Principled theoretical derivation (Sec. 3.1–3.2, Eq. 3).** The paper cleanly shows that representation drift regularization under linearized fine-tuning simplifies to a quadratic form of the Jacobian Gramian, and identifies this Gramian as a generalized Gauss-Newton matrix. This connection is what enables the method to avoid runtime data access — a concrete advance over τJp (Yoshida et al., 2025), which requires explicit access to other tasks' data during training.

- **O(1) Kronecker merging heuristic (Eq. 8) validated against the O(T) formulation.** Table 3 shows the gap between the accumulated regularizer and the naïve multi-task formulation is marginal (e.g., ViT-B/16: 88.3 vs. 88.1; T5-base: 78.7 vs. 78.5 at Best α). This is not merely a complexity claim — it is backed by a direct head-to-head comparison.

- **State-of-the-art task negation results (Table 2).** TAK achieves the strongest forgetting of target tasks (3.4% target accuracy across all three ViT backbones) while best preserving control-task accuracy (62.4%, 66.4%, 72.6%). These numbers beat the data-dependent τJp (6.7%/60.8% on ViT-B/32) and the dataless TaLoS (11.0%/60.7%), all without accessing external task data.

- **Robustness to α rescaling (Fig. 4a, Table 1).** On ViT-B/32, TAK with α=1 achieves 85.8% absolute accuracy, within 0.2 points of the best-tuned 86.0%. The accuracy remains nearly flat across α ∈ [0, 2], eliminating the need for held-out tuning of the mixing coefficient — a practical advantage over methods requiring cross-task validation.

- **Efficient pre-computation and practical engineering analysis (Figs. 6–8).** KFAC estimation with MC=1 takes ~4 minutes total for all 8 vision tasks (vs. ~199 minutes exact). The paper further analyzes KFAC compression (block-8 reduces storage from 550 MB to ~70 MB with ~1 point accuracy drop), scheduling, and sample efficiency — providing concrete deployment guidance.

- **Task localization evidence (Fig. 5).** The paper directly visualizes that TAK produces task vectors whose Jacobian-vector-product norms concentrate near zero for out-distribution inputs across all eight datasets, going beyond aggregate accuracy to show the mechanism.

## Weaknesses

### Major

- **No statistical uncertainty reported for any experimental result.** Every number in Tables 1–3 and the main text is a point estimate with no standard deviation, confidence interval, or indication of the number of random seeds/independent runs. The paper acknowledges that "variance across seeds increases as the number of MC samples grows" (line 318) — confirming variance exists — yet no seed-averaged results are reported. Differences between methods are often 0.2–0.6% absolute accuracy, which could easily fall within noise. This undermines the ability to evaluate which comparative claims are meaningful.

- **Regularization strength β is never specified or analyzed.** Equation (7) introduces β as the overall regularization weight, but the paper never states what value(s) of β were used, how they were chosen, or whether they require tuning per task. Since the paper's main advantage over τJp includes "eliminating the need for held-out tuning" (referring to α), it is critical to verify that β does not itself require careful tuning. A sensitivity analysis over β is missing.

### Minor

- **"Dataless" framing requires sharper delineation.** Computing the KFAC factors for a task *does* require that task's data (forward passes for activations A^l; backward passes for gradient covariances B^l, Section 3.3). What the method avoids is *runtime* access to other tasks' data during training. The paper acknowledges this (line 83: "after initial pre-computation, does not require further data access"; line 334: releasing "additional assets together with the pre-trained weights"), but the abstract and introduction frame it as simply "dataless" without this qualification, which could mislead readers about what the method actually requires.

- **Non-linear regime justification is asserted rather than demonstrated.** The paper states that Attention-Only FT "induces approximately linear fine-tuning dynamics" (line 227) and uses this to justify applying TAK in the non-linear regime. However, no evidence is provided to support this claim — no measurement of linearity, no comparison with the linearized regime's Jacobian structure. The non-linear results (e.g., Attn. Only FT + TAK: 84.3/91.0 vs. Linear FT + TAK: 88.3/98.1 on ViT-B/16) are substantially weaker than the linearized results, which aligns with the caveat that the regularizer "is not theoretically exact in the non-linear regime."

### Trivial

- The abstract claims "constant complexity in the number of tasks" — this is correct for the training phase but pre-computing KFAC factors is O(T), as shown in Algorithm 1. Minor imprecision.

## Nice-to-Haves

- A compute-matched comparison with τJp would separate the effect of the regularizer from the effect of computational budget.
- A discussion of whether a cross-entropy-weighted GGN (rather than squared-error GGN) might yield different results would deepen the theoretical analysis.
- An explicit statement that MC=1 with 128 examples is the default setup for main experiments, placed in the experimental setup section.

## Removed Points

These points were raised by reviewers but removed after verification against the paper:

- **"Kronecker heuristic beating the idealized multi-task formulation undermines the validation logic."** Both the "naïve" O(T) and "accumulated" O(1) versions use KFAC approximations; neither is the exact GGN. The paper acknowledges the gap is "marginal." The observation that one KFAC-based approximation slightly outperforms another on a specific metric does not undermine the method — it simply reflects approximation noise. This is better attributed to the need for error bars (already covered).

- **"Missing learning rate / optimizer / epoch count in main text."** These details exist in the appendix (App. E), which the parser stripped. Per policy, missing-appendix complaints are removed.

- **"No explicit statement of which KFAC variant is used."** The paper states "With a single Monte Carlo sample" (line 302) and labels "MC=1 (ours)" in Fig. 6b/Table (line 288), providing the information even if not in a dedicated experimental-setup subsection.

## Novel Insights

The reviewers' combined analysis surfaces a compelling observation not emphasized in the paper itself: TAK's approach inverts the typical trade-off in task arithmetic. Existing methods either (a) use data at merge/regularization time to reduce interference (τJp) or (b) avoid data but accept degraded performance (naïve task arithmetic, post-hoc merging). TAK exploits the fact that the KFAC factors are *architecture-specific* rather than *task-specific* in the same way raw data is — they summarize the input-output statistics of a pre-trained model's layers. This means the one-time pre-computation cost is a form of amortization: the same KFAC factors could potentially be reused across many different task compositions, unlike data which must be re-accessed each time the task set changes. This positions KFAC factors as a new class of *model asset* alongside pre-trained weights, unlocking downstream applications (privacy-preserving merging, continual task addition) that neither data-dependent methods nor fully dataless post-hoc methods can achieve simultaneously.

## Suggestions

- Add standard deviations (3–5 seeds) to all main results in Tables 1–3.
- Report the β value(s) used and include a sensitivity analysis (sweeping β across 3–4 orders of magnitude) on at least one benchmark.
- Qualify the "dataless" framing in the abstract/introduction to clarify that data is needed for one-time KFAC pre-computation, not for runtime regularization.
- Strengthen the non-linear regime justification by either measuring the linearity of attention-only fine-tuning or softening the claims about applicability.

## Score and Decision

**Round-1 bracket**: The paper is most comparable to accepted papers in task arithmetic averaging 5.75–6.25 (τJp paper: 6.0; Attention-Only FT: 6.25; Submodule Linearity: 6.0; SAM for merging: 5.75), and clearly stronger than the rejected anchors (Interfering with Interference: 5.0; Realistic Evaluation: 5.33). Initial bracket: [5.5, 6.5].

**Round-2 narrowing**: Compared to the τJp paper (avg 6.0), the current paper has stronger theoretical grounding (explicit GGN/KFAC connection), broader experimental scope (language + vision), and addresses τJp's main weakness (requires task data). However, it shares τJp's reproducibility gaps (no error bars, β unspecified). Compared to the Attention-Only FT paper (6.25), the current paper has deeper theoretical novelty but similar empirical limitations. The paper is closest to the τJp anchor in overall quality/contribution level.

**Final calibrated score**: 6.0. The paper contributes a novel theoretical connection and a practical, well-evaluated method. The major weaknesses (no error bars, unreported β) are addressable and do not invalidate the core contribution.

**Anchors retrieved** (all rounds):
1. `1VwWi6zbxs.md` — τJp paper (avg 6.0, scores 8/5/6/5). Direct competitor; current paper has better theory and scope.
2. `irPcM6X5FV.md` — Submodule Linearity (avg 6.0, all 6s). Similar quality; different approach.
3. `eaTqsptDPL.md` — SAM merging (avg 5.75). Slightly weaker; smaller gains.
4. `4wuvmJRAU4.md` — Interfering with Interference (avg 5.0). Rejected; current paper stronger in theory and evaluation.
5. `dj0TktJcVI.md` — Attention-Only FT (avg 6.25). Accepted; similar quality, less theory but cleaner method.
6. `q3ztjJRQuJ.md` — Trust Region merging (avg 5.75). Rejected; comparable quality but narrower scope.
7. `Bq3fEAGXUL.md` — Realistic Evaluation (avg 5.33). Rejected; survey paper.
8. `g8sGBSQjYk.md` — Second-order optimization param. (avg 7.33). Higher quality; different subfield.
9. `Q0TEVKV2cp.md` — Mini-batch quadratics (avg 6.75). Higher quality; different subfield.
10. `88rjm6AXoC.md` — Optimal Brain Apoptosis (avg 6.25). Similar quality; different subfield.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>