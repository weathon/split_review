Here is my consolidated final review.

---

## Summary

This paper proposes mirror-descent algorithms (Double-Scrible, BaBle-Scrible, MNL-Scrible) for adversarial online linear optimization with preference feedback — covering dueling (pairwise), batched, and top-*m* ranking feedback. It derives regret bounds of Õ(d√T) for the dueling case with matching lower bounds, and extends these to batched and ranking feedback with corresponding rates showing improvement factors of √min{B,d} and √m respectively. The paper claims the first gradient-descent-based approach for adversarial preference feedback, achieving O(dT) computational cost while avoiding the restrictive derivative lower-bound assumptions required by prior GLM bandit methods.

## Strengths

- **First gradient-descent algorithm for adversarial preference feedback with near-optimal regret.** Double-Scrible achieves Õ(d√T) regret (Theorem 1) using online mirror descent with self-concordant barriers, providing a computationally efficient (O(dT) per round) alternative to the intractable UCB/TS methods that dominate the RLHF literature (Remark 5). This is a genuinely novel technical contribution relative to the Scrible algorithm (which operates under value feedback) — the key innovation is constructing a gradient estimator from binary preference feedback rather than from direct function evaluations.

- **Matching lower bounds confirm near-optimality.** The paper provides lower bounds of Ω(d√T log T) (Theorem 3, dueling), Ω(d√T/√min{B,d}) (Theorem 6, batched), and Ω(d√T/√m) (Theorem 9, ranking), showing each algorithm is optimal up to logarithmic factors. Deriving these from information-theoretic first principles is non-trivial.

- **Extension to batched and ranking feedback with clean reductions.** BaBle-Scrible (Theorem 4) and MNL-Scrible (Theorem 7) extend the approach naturally, with the ranking setting exploiting a clever hypercube-structured query set (Section 5.1(i)) and Lemma 14's observation that top-*m* ranking yields *m* independent pairwise comparisons, reducing the problem to the batched setting.

- **Eliminates the derivative lower-bound assumption required by prior GLM bandit approaches.** Remark 5 explicitly notes that Double-Scrible avoids the κ-dependency (a multiplicative penalty from lower-bounding σ′(θ^T(x−y))) that afflicts prior UCB-based Logit-DB algorithms (Saha et al., 2023; Das et al., 2024), thanks to the symmetric perturbation trick (Lemma 11).

## Weaknesses

### Fatal

None. The paper's core theoretical contributions (the algorithms, regret bounds, and lower bounds) are internally coherent and represent a genuine technical advance.

### Major

1. **Abstract oversells the RLHF connection with trajectory-based policy optimization.** The abstract states: "Following this we extend our results to policy optimization in the RLHF framework with **trajectory preferences** and design **no-regret RL policies** using a variant of mirror descent." The technical body does not deliver this. Sections 3–5 remain entirely within the adversarial online linear bandit (best-arm identification) framework — there are no state transitions, no trajectory feedback, no policy gradient or value functions, and no RL component whatsoever. The paper itself acknowledges (line 20–22) that it "frame[s] the RLHF problem as a best-arm identification problem" and calls this "the first step." The abstract's wording implies a concrete extension to trajectory-based RLHF that was never carried out. This mismatch will mislead readers; the paper would be better served by framing its contribution honestly as "adversarial preference bandits with implications for RLHF" and dropping the unsupported claims about trajectory preferences and RL policies.

2. **Experimental evaluation is too weak to support the claim that it "validates our theoretical findings."** (a) No baselines are implemented — not even a random baseline or a lightweight UCB comparison on small *d*. The paper argues prior methods are computationally infeasible, which may be true for large *d*, but a small-scale comparison (e.g., *d* = 2,5) or a random policy would be straightforward and informative. (b) The experiments do not verify the predicted scaling rates: there are no log-log plots, no curve-fits, and no normalized regret plots (e.g., Regret/(d√T)) to confirm the theoretical dependencies on *d*, *T*, *B*, or *m*. The raw cumulative regret plots only show monotonic growth consistent with *any* sublinear algorithm, not specifically with the claimed rates. (c) No confidence intervals or error bars are shown despite averaging over 100 runs. For a paper that claims empirical validation of specific theoretical rates, the experiments fall short.

### Minor

1. **The regret bound's dependence on problem-dependent constants H_{D,ψ} and ν is not fully characterized.** Theorem 1's bound scales with d√(ν log T)/H_{D,ψ}, but the paper gives only toy examples for these constants (Remark 3: H²=2 for the unit ball with one barrier, H²=d for another). The practical magnitude of these constants for typical decision sets of interest (polytopes, simplices) is not discussed, making it hard for readers to gauge what the bound means in concrete settings.

2. **The Minimal Eigenvalue Assumption (Remark 3) is a non-trivial restriction not required by the original Scrible algorithm.** The paper acknowledges this honestly and provides examples where it holds, but does not discuss what happens when it fails or whether it is always satisfiable for arbitrary decision sets. This weakens the "optimality" claim relative to the standard Scrible analysis.

3. **Hyperparameter choices for experiments not reported.** The settings of η, δ, γ_t are given symbolically in the theory but numerical values used in the experiments are not stated, hindering reproducibility.

### Trivial

None.

## Nice-to-Haves

- Log-log plots or normalized regret (Regret/(d√T), Regret·√m/(d√T)) to visually confirm the theoretical scaling rates.
- A small-scale comparison to a simple baseline (e.g., random policy, or a UCB variant on very small *d*) to substantiate the claimed efficiency advantage.
- Explicit numerical hyperparameter values used in experiments.
- A brief discussion or formal reduction showing exactly how (if at all) the bandit setting maps to trajectory-based RLHF, or an acknowledgement that this extension is left for future work.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"All algorithm pseudocode is relegated to the appendix"** — REMOVED because the appendix exists in the original submission; the main text provides a substantive textual description of each algorithm (Double-Scrible in §3, BaBle-Scrible in §4.1, MNL-Scrible with steps (i)–(iv) in §5.1). The parser strips appendix content from all papers.
- **"Garbled/incomplete lines in algorithm description"** — REMOVED as these are parser rendering artifacts, not author errors.
- **"The paper fails the minimum standard of self-contained presentation"** — REMOVED per the above two points.
- **"Incomplete specification of adversarial environments Inst-1/Inst-2"** — REMOVED because truncated sentences like "we choose θ_t" are parser artifacts; the original submission likely had complete descriptions.
- **"Missing related works"** — REMOVED per instructions (cannot independently verify existence of omitted references).
- **"The batched extension is straightforward and has limited novelty"** — REMOVED as subjective opinion insufficiently grounded; the value lies in the analysis showing √min{B,d} improvement.
- Strength about **"Empirical validation across multiple dimensions"** — REMOVED because it conflicts with the verified weakness that experiments do not validate the specific theoretical rates.

## Novel Insights

None beyond the paper's own contributions. The reviewer perspectives do not uncover a hidden novel interpretation of the paper that the paper itself does not articulate. The disconnect between RLHF framing and bandit content is a presentation issue, not a novel observation about the method.

## Suggestions

1. **Revise the abstract and introduction to accurately scope the contribution.** Frame the paper as "adversarial preference bandits with logistic feedback" and either remove the unsubstantiated "trajectory preferences" / "RL policy" claims or add a formal subsection sketching the reduction (even if preliminary). Honest framing strengthens the paper by letting readers evaluate what is actually delivered.
2. **Strengthen the experimental section.** Add at least a simple random baseline; include normalized regret plots (e.g., Regret/(d√T)) to visually confirm the scaling laws; report hyperparameter values; add error bars. This would turn the experiments from a perfunctory demonstration into genuine validation.
3. **Characterize H_{D,ψ} and ν more explicitly** for a few natural decision sets (e.g., polytope, simplex, ℓ₂ ball) so practitioners can gauge the practical tightness of the bounds.
4. **Discuss the Minimal Eigenvalue Assumption's practical implications** — when it holds, when it fails, and what alternative analyses or regularizers might circumvent it.

## Score and Decision

The paper presents a technically solid theoretical contribution — novel gradient-based algorithms with matching lower bounds for adversarial preference feedback, overcoming computational and assumption-related limitations of prior work. These results are publishable. However, the abstract overclaims scope (RLHF trajectory policy optimization that is never delivered), and the experiments do not substantiate the claim of validating the theory. These are fixable with a major revision (rescope the claims, strengthen experiments), but in its current form the mismatch between framing and content is significant enough to warrant rejection for a top venue at this stage.

**Score:** 5.0 (marginally below acceptance threshold for a top venue; the theoretical core is strong but the presentation overreaches and the empirical support is weak)

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>