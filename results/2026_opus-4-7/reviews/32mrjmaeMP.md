## Summary
The paper proposes TAK, a regularizer for weight disentanglement in Task Arithmetic that recasts the representation-drift penalty as a quadratic form in the Generalized Gauss-Newton (GGN) matrix and approximates it with KFAC, so per-task curvature factors can be precomputed once and shared without raw data. A Kronecker-merge heuristic combines per-task factors into a single surrogate, giving constant cost in the number of tasks T. On 8 Vision (CLIP ViT-B/32, B/16, L/14) TAK matches or beats the data-using τJp baseline with α=1 (no tuning) and shows α-robustness; results extend to T5-base NLI with a remaining gap to τJp.

## Strengths
- Clean conceptual mapping (§3.1–3.2): under linearization the drift regularizer collapses to a quadratic form in the Jacobian Gram matrix, identified exactly as the squared-loss GGN, unlocking mature curvature-approximation tooling (KFAC) for a problem that was previously framed as data-dependent.
- Strong vision task-addition results (Table 1): with α=1, TAK reaches 85.8/97.6 (ViT-B/32), 88.3/97.9 (B/16), 91.6/99.3 (L/14), matching the data-using τJp and decisively beating the only other dataless baseline (Diag. GGN at 80.1/92.3 on B/32).
- Robustness to the rescaling coefficient α (Fig. 4): TAK stays flat over α∈[0.5, 2.0] while TA and post-hoc merging methods peak sharply and collapse — removes the held-out-tuning step, a real practical pain point.
- Task negation (Table 2): lowest target accuracy (3.4% on ViT-B/32) with best preserved control accuracy (62.4%), better than τJp without needing control-task data.
- Task-localization evidence (Fig. 5): Jacobian-norm distributions show inlier/outlier separation under KFAC regularization that is absent in unregularized Linear FT — concrete visualization of the disentanglement mechanism.
- Efficiency analysis (Fig. 6) and KFAC compression (Fig. 7b: ~87% memory reduction at ~1pt accuracy cost) give actionable deployment numbers.

## Weaknesses

### Fatal
None.

### Major
- **The multi-task Kronecker merge (Eq. 8) is presented as a heuristic with no error analysis, yet it underpins the headline "O(1) in T" claim.** A sum of Kronecker products is not generally a Kronecker product, and the λ_t weighting is asymmetric (inside the A sum but not the B sum) without justification. Empirical support is Table 3 on T=8 vision and T=6 language, with no study of how the approximation degrades as T grows or as tasks diverge. For ViT-B/32 the merged version already lags the un-merged one by 0.5–0.7 pts; the paper attributes this to "smaller architectures being more sensitive," which is exactly where one would worry the heuristic begins to break.
- **Scope of the derivation vs. scope of the headline non-linear results.** §3.1 strictly requires the linearization in Eq. (1); the best non-linear numbers ("Attn. Only FT + TAK" in Table 1) are justified only by appealing to Jin et al. (2025)'s "approximately linear" claim, with no quantitative check that ||f − f_lin|| is small in this setup. The empirical wins are real but the analysis stops short of the regime that produces the strongest reported numbers.

### Minor
- **"Dataless / inherently privacy-preserving" framing.** KFAC factors are derived from training data and aggregate per-example gradients; the paper does not analyze whether they leak information. The accurate statement is "data-free at composition time," not privacy-preserving in any formal sense. §4's "inherently privacy-preserving" overstates what is shown.
- **Squared-loss GGN vs. cross-entropy mismatch (§3.2).** Identifying the Jacobian Gram matrix as GGN requires the squared-loss criterion, discarding ∇²c. On T5-base TAK trails τJp 78.7 vs. 81.3 (Abs.) — a 2.6-pt gap. Whether a Fisher / training-criterion KFAC variant would close this is not tested, despite being a small change directly motivated by the analysis.
- **Cross-paper comparison for TaLoS (†) in Table 1.** The non-linear headline ("we beat TaLoS") relies in part on numbers transcribed from Iurada et al. 2025 rather than a controlled head-to-head, so matched training budgets are not verifiable.
- **Task-localization claim (Fig. 5) is only qualitative.** Only histogram shapes are shown; no AUROC or separation metric against simple baselines (e.g., MSP, energy score, TaLoS-mask agreement), yet the paper "suggests OOD detection" use.

### Trivial
None substantive.

## Nice-to-Haves
- A sweep over larger T (e.g. partitioned ImageNet up to ~50 tasks) to characterize where Eq. 8 degrades.
- A Fisher / training-criterion KFAC variant tested on T5 to isolate whether the language gap is a squared-loss artifact or a structural limit of being data-free.
- A quantitative check on the linearization assumption underlying attention-only fine-tuning, to back the application of TAK outside the linearized regime.
- α-robustness reported across more model scales and T (currently centered on ViT-B/32, Fig. 4).

## Removed Points
These points are flagged to be removed; treat them with caution.
- "Dataless framing is dishonest." The paper does explicitly state at training time of each task vector that no *other* task's data is needed, and Algorithm 1 makes the KFAC-computation step explicit. Kept only as a minor framing concern around the "privacy-preserving" wording, not as a major weakness.
- Reproducibility / training-budget concerns beyond what is in the paper — out of scope per submission norms.
- Generic complaints about not running additional baselines or extra datasets beyond 8 Vision and 6 NLI — paper's evaluation scope already aligns with the standard for this subfield.

## Novel Insights
None beyond the paper's own contributions. The identification of the representation-drift regularizer with the squared-loss GGN — and the resulting opening up of the entire KFAC toolkit for task-arithmetic regularization — is itself the paper's novel observation, and it is a clean one.

## Suggestions
- Add an error-analysis section (theoretical bound or synthetic sweep) for Eq. 8 as T grows and as task similarity varies.
- Test a Fisher-based KFAC on T5 to probe whether the language gap to τJp is structural or a squared-loss artifact.
- Replace "inherently privacy-preserving" with a precise statement about data access patterns; ideally add a small experiment on whether KFAC factors leak training data.
- Quantify the linearization quality of attention-only fine-tuning to justify applying the TAK derivation in that regime.
- Quantify the Fig. 5 task-localization signal (AUROC against simple OOD baselines).

## Calibration

Round 1 bracket — anchors retrieved:
- `lNtio1tdbL.md` ATM (3.00, weak) — much shallower TA analysis than TAK.
- `XVHXVdoV11.md` Compatible specialization (3.40, weak) — purely diagnostic, no method.
- `yx8bU8T5ZN.md` Delta-parameter editing (2.33, weak) — survey-style.
- `WM5G2NWSYC.md` Projected Subnetworks (2.00, weak) — much weaker.
- `1VwWi6zbxs.md` τJp (6.00, mid) — the *baseline* TAK matches without data; TAK is a step beyond it.
- `q3ztjJRQuJ.md` TA in Trust Region (5.75, mid) — comparable in maturity but less theoretically grounded.
- `lIdc5DUplq.md` SUPERMERGE (4.33, low-mid) — weaker.
- `1v7SRWsYve.md` MAP (6.33, mid) — similar caliber.
- `irPcM6X5FV.md` Submodule linearity (6.00, mid) — close in theme and quality.
- `jOmk0uS1hl.md`, `TwJrTz9cRS.md`, `SPS6HzVzyt.md`, `vf5aUZT0Fz.md` (8.00, strong) — broader scope or sharper conceptual claim than TAK.

Round-1 bracket: 5.5–7.0.

Round 2 narrowing — anchors retrieved:
- `1VwWi6zbxs.md` τJp (6.00) — TAK directly improves on it (matches without data + α-robustness): TAK is somewhat better.
- `dj0TktJcVI.md` Attn-only FT (6.25) — used as TAK's non-linear baseline; TAK adds a more general regularizer: TAK comparable/slightly better.
- `TDyE2iuvyc.md` TaLoS (5.50) — another baseline TAK beats in Table 1: TAK is better.
- `OZVTqoli2N.md` Second-order Perspective (7.50) — deeper theoretical analysis of compositionality; TAK is more practical, less conceptually broad: TAK weaker than this anchor.
- `nT2u0M0nf8.md` CAMEx (6.67) — curvature-aware merging, similar caliber: comparable.
- `D7KJmfEDQP.md` Uncertainty-based gradient matching (6.00) — comparable.
- `1v7SRWsYve.md` MAP (6.33) — comparable.

TAK sits above its direct baselines (τJp 6.00, TaLoS 5.50, Attn-only 6.25), comparable to curvature-aware merging anchors (CAMEx 6.67, MAP 6.33), and below the deeper Second-Order Perspective (7.5). The merge heuristic, overstated dataless/privacy framing, and language-task gap prevent it from clearing the 7.5 anchor.

Final score: 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>