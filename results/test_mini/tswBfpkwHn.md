Now I have a thorough understanding of the paper and all the reviews. Let me write the final consolidated review.

---

## Summary

This paper presents the first theoretical analysis of training dynamics and in-context learning (ICL) generalization for a one-layer Mamba model on binary classification tasks where prompts may contain additive outliers. The key contribution is a rigorous characterization of how Mamba's gating mechanism enables robustness to outlier-contaminated prompts. The paper derives an exact closed-form expression for one-layer Mamba as a linear attention layer followed by nonlinear gating (Equation 3), proves convergence and sample complexity bounds (Theorem 1), and shows that Mamba can maintain accurate ICL generalization even when the fraction of outlier-containing context examples approaches 1 (Theorem 2), while a comparable linear Transformer fails beyond a 1/2 outlier fraction threshold (Theorem 4). The mechanism is further elucidated through Corollaries 1 and 2, which show that the learned attention focuses on same-pattern examples while the gating suppresses outliers and induces an exponential locality bias. Experiments on synthetic data validate the theoretical predictions.

## Strengths

- **First theoretical analysis of Mamba training dynamics for ICL with outliers.** The paper explicitly contrasts with prior work (Li et al., 2024b; 2025b) that only analyzes global minima, and with Transformer-focused ICL theory (Huang et al., 2023; Zhang et al., 2023; Li et al., 2024a), establishing concrete novelty. The closed-form derivation in Equation (3) decomposing one-layer Mamba into linear attention + nonlinear gating is the foundation for the whole analysis.

- **Provable robustness advantage over linear Transformers, with a clean theoretical threshold contrast.** Theorems 2 and 4 deliver a crisp quantitative comparison: Mamba tolerates outlier fraction α < min(1, p_a·l_tr/l_ts) which can approach 1, while a one-layer linear Transformer requires α < 1/2. This theoretical gap is directly validated by experiments in Figure 2, where Mamba's error stays below 0.01 for α up to 0.8 while the linear Transformer's error jumps sharply past α = 0.5 across three outlier labeling schemes (flipped, targeted, random).

- **Mechanistic characterization verified by experiments.** Corollary 1 shows the linear attention concentrates on same-pattern examples (verified in Figure 3). Corollary 2 shows the gating suppresses outlier examples (gating near zero) and decays exponentially with index distance for clean examples (verified in Figure 4). This provides a complete and testable account of how Mamba implements robust ICL.

- **Honest treatment of limitations.** The paper explicitly acknowledges in Remark 6 that the comparison is against linear attention only, that large Transformers can achieve robustness, and discusses the CQ sensitivity in Section 4 (Table 1). This intellectual honesty strengthens the contribution.

## Weaknesses

### Major

None.

### Minor

- **The comparison with Transformers is limited to linear attention.** The paper compares a one-layer Mamba with a one-layer *linear* Transformer (no softmax, no multi-head attention). While Remark 6 acknowledges this caveat, the abstract and contributions section's framing ("Mamba maintains accurate predictions even when the proportion of outliers exceeds the threshold that a linear Transformer can tolerate") could mislead casual readers into thinking the comparison is against standard Transformers. The practical implication of the α < 1/2 threshold for real Transformer models (which use softmax attention and multiple heads) is unclear. The paper's own experiments confirm Mamba works mostly with one-layer linear Transformers; the 3-layer results in Table 1 and Appendix B.1 partially address this but the core theoretical comparison remains restricted.

- **Test-time outlier condition is restrictive.** Theorem 2 requires each test outlier pattern to be a linear combination of training outlier patterns whose coefficients sum to a positive value L > 0 (plus an orthogonal component). This means test outliers must have a positive projection onto the training outlier subspace. While the paper is transparent about this condition (explicitly stated in Theorem 2 and emphasized in Section 3.1's P1), this excludes test outliers that are entirely orthogonal to the training outlier subspace or those with equal positive and negative coefficients. The paper claims this "captures a wide range of possible outlier patterns at test time" (Remark 3), but the scope is narrower than the robustness framing might suggest.

- **Interdependence of theoretical conditions.** The sufficient conditions in Theorem 1 involve several interdependent constraints on κ_a, l_tr, V, β, p_a, and ε. For example, κ_a must satisfy both a lower bound (Vβ^{-4}) and an upper bound (Vβ(1-p_a)p_a^{-1}ε^{-1}) simultaneously. The prompt length l_tr is bounded above by a term involving poly(M_1^{κ_a}), making it extremely sensitive to κ_a. It is not obvious that feasible parameter settings exist for all regimes, especially small ε. The experiments (Section 4) provide an existence proof for one parameter setting (β=3, κ_a=2, p_a=0.6, etc.), but no theoretical feasibility analysis is given. This is a common issue in this style of analysis but worth noting.

- **Positional sensitivity (CQ setting) is a genuine architectural limitation.** Corollary 2 shows gating values decay exponentially with distance from the query. Table 1 shows that when outliers are placed closest to the query (CQ setting), Mamba's accuracy drops to 82.73% — far below the linear Transformer's 93.96%. The paper discusses this honestly, but this is a structural limitation of the gating mechanism, not just a sensitivity. The theoretical robustness guarantee (Theorem 2) does not incorporate positional effects, so a practitioner relying on the α < min(1, p_a·l_tr/l_ts) bound might be misled if outliers are positioned near the query. The paper could more prominently flag this as a failure mode of the architecture.

### Trivial

None. The paper is competently written and organized.

## Nice-to-Haves

- A concrete worked example demonstrating all conditions of Theorem 1 are simultaneously satisfiable (e.g., specific numeric values for each parameter). While the experiments provide empirical existence, a table or paragraph showing the feasible region would help readers assess the theory's practicality.
- A theoretical characterization of how robustness degrades as outliers move closer to the query, extending Corollary 2 to bound test error in the CQ regime.
- Discussion of whether the Σ λ_i ≥ L > 0 condition is an artifact of the proof or a genuine barrier, with an informal argument for what happens when L ≤ 0.

## Removed Points

**These points were removed for the following reasons:**

- *Criticism about missing proof sketches for Theorems 3 and 4* — The paper states proof sketches are in the appendix; the appendix is stripped by the PDF parser.
- *Criticism about missing related works* — As per instructions, I cannot verify citation existence or assess coverage.
- *Criticism about missing discussion of hinge loss choice* — Speculative and not a substantive weakness; the choice is standard.
- *Criticism about lack of discussion of W_A and other Mamba parameters* — The paper explicitly selects A = -I (following Gu & Dao 2023) and acknowledges this simplification; criticizing a deliberate modeling choice taken for analytical tractability is scope creep.
- *Criticism about formatting, typos, and presentation* — These are PDF parser artifacts.
- *Claim from Strength Finder about "attention scores on same pattern increase during training" being a strength* — While the experiments are good, this specific strength claim is descriptive rather than evaluative; the mechanistic characterization (Corollaries 1 and 2) is already captured in Strengths.
- *Generic strengths about "addressing important problems" or "targeting interesting questions"* — Dropped as superficial per instructions.

## Novel Insights

The harsh critic raises an interesting tension that the paper does not fully resolve: Mamba's gating mechanism is simultaneously the source of its outlier robustness AND its positional vulnerability. The gating suppresses outliers by driving their gating values to near-zero (Corollary 2(i)), but this same mechanism creates an exponential locality bias (Corollary 2(ii)) that makes the model fragile when outliers are near the query. This dual nature — that the very mechanism enabling one form of robustness creates a different vulnerability — is a genuinely interesting architectural insight that could guide future SSM design. Standard "strengths and weaknesses" discussions treat these as separate issues, but they are in fact two sides of the same mechanism.

## Suggestions

1. **Sharpen the scope claim in the abstract and contributions** to consistently say "one-layer linear Transformer" rather than just "linear Transformer" in places where it could be misread. Currently the abstract says "compared to the analysis of linear Transformers under the same setting" which is precise, but the sentence "Mamba maintains accurate predictions even when the proportion of outliers exceeds the threshold that a linear Transformer can tolerate" could be misread without context as comparing against all Transformers.

2. **Add a feasibility paragraph** that discusses whether Theorem 1's conditions can be met in practice, even informally. A table showing a concrete numeric configuration that satisfies all inequalities would significantly help readers.

3. **More prominently flag the CQ limitation** in the main text where the theoretical robustness claims are stated (e.g., alongside Theorem 2 or in the contributions list), not just in the experiments section.

4. **Include experiments on small-scale real or semi-real data** (e.g., sentiment classification with flipped labels as suggested by Figure 1) to demonstrate that the theory operates beyond the exact synthetic setup used for validation. The paper mentions additional experiments in Appendix B.2; these should be highlighted in the main text if they involve non-synthetic data.

## Score and Decision

**Calibration protocol summary:**

**Round 1 (Bracketing):** Searched for theoretical Mamba ICL papers across three bands.
- Weak band (<3.5): Mamba theory papers scoring 2.67–3.33 — notably weaker, with thin results or flawed methodology.
- Middle band (3.5–7.5): Several papers scoring 4.0–7.0. Most comparable anchors: "Mamba Can Learn Low-Dimensional Targets" (5.00, Reject), "A Theoretical Analysis of Mamba's Training Dynamics" (5.00, Accept Poster), "Theory of Scaling Laws for ICL" (5.50, Accept Poster).
- Strong band (>7.5): "From Markov to Laplace" (7.50, Accept Oral) — outstanding paper with clean optimality results.
- **Initial bracket: between 5 and 7.**

**Round 2 (Narrowing):** Searched within (4.5–6.5) and (6.0–8.0) for finer anchoring.
- At 5.00: Two papers directly comparable in topic and methodology. The paper under review is stronger than both — it has more natural training (standard SGD vs. artificial two-stage), studies distribution shift (train vs. test), includes a cleaner Transformer comparison, and validates mechanism predictions (Figures 3, 4).
- At 6.50–7.50: "From Markov to Laplace" (7.50, Oral) and "Learning to Recall" (6.50, Poster). The current paper is not as strong as the 7.50 paper, which provides an optimality result (Bayes and minimax) with a cleaner analysis, but is comparable to or slightly stronger than the 6.50 paper in the target dimension of theoretical thoroughness.
- **Narrowed bracket: between 5.5 and 6.5; final score at 6.0.**

**Anchors consulted:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `3KPsog4mpy.md` | 5.00 | R1, R2 | Weaker — artificial training algorithm, weaker experiments |
| `hvpKqEYJjj.md` | 5.00 | R1, R2 | Comparable but slightly weaker — similar simplified model but less analysis of distribution shift |
| `2g8vgmyXgQ.md` | 5.00 | R2 | About Transformers, not Mamba — less directly comparable |
| `qA42mWsnbl.md` | 5.50 | R2 | ICL scaling laws for Transformers — different topic |
| `kmK3WSCOCT.md` | 7.50 | R2 | Stronger — cleaner optimality result, better writing |
| `HwCvaJOiCj.md` | 7.00 | R1, R2 | Engineering paper — different contribution type |
| `CfFj68C9Cn.md` | 6.50 | R2 | About Transformers recall — different topic |
| `8cDoHzqDXP.md` | 3.33 | R1 | Weaker — less rigorous |
| `lhvdbCiiE6.md` | 3.33 | R1 | Weaker — not clearly stated |
| `466gVY2sBQ.md` | 2.67 | R1 | Much weaker — limited scope |
| `NX6oMuoLxu.md` | 2.67 | R1 | Much weaker — different focus |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>