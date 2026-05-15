Now I have thoroughly read and verified the paper against both reviews. Let me produce the consolidated review.

---

## Summary

This paper proposes a geometric explanation for why adversarial training is less effective for certain data points: the authors argue that the "least robust" points lie in high-curvature regions of the data manifold, where the model perceives pixel distances as encoding disproportionately large semantic changes. They formalize this via a sensitivity measure (point-wise Lipschitz constant of the label map) and attempt to link it to the Finsler-Haantjes curvature. Empirically, they show that (i) diffusion models generate more semantically varied clones from non-robust images, and (ii) focusing stronger PGD-40 adversarial training on just the 1024 least robust points (≈0.005% of data) yields a small (~0.2 pp) improvement in test-set AutoAttack accuracy, which together with learning-rate adjustments produces marginal gains over the Wang et al. (2023) baseline.

## Strengths

- **Margin-based explanations are empirically insufficient**: The paper convincingly demonstrates (Section 1, Fig. 1b) that the minimal l∞ distance between non-robust CIFAR-10 images (≈0.2118) is over 6× the perturbation radius (≈0.0314), proving that margin alone cannot explain the ×2 gap in adversarial accuracy between robust and non-robust regions. This motivates the need for an alternative explanation.

- **Diffusion-model experiments provide qualitative evidence connecting robustness to semantic variation**: Figure 3 and Table 1 show that clones of the least robust images exhibit larger semantic changes despite smaller pixel differences (average l2 distance 0.0388 vs. 0.0687 for most robust), while clones of robust images show mainly color/background shifts. This is a genuinely interesting qualitative observation, even if it measures the generative model's manifold rather than the data manifold directly.

- **Targeted adversarial training on non-robust points yields a signal**: The paper shows that focusing stronger PGD-40 training on only 1024 points (≈0.005% of the dataset) produces a consistent (if small) improvement across multiple settings (CIFAR-10 l∞, l2; CIFAR-100 l∞). The ablations comparing random sets vs. the least-robust set (Table 2, rows 1–5) help isolate the effect, and the fact that doubling/quadrupling the focus set offers no further benefit (suggesting the 1024 least robust points are special) is an interesting finding.

- **Sensitivity measure is well-motivated and local behavior is guaranteed**: The sensitivity functional (Eq. 1) naturally captures data-point vulnerability, and Theorem 1 provides a Lipschitz continuity guarantee that ensures sensitivity information is locally consistent—a useful property even if the link to curvature is imperfect.

## Weaknesses

### Major

- **The core mathematical step linking sensitivity order to curvature order is unjustified and likely incorrect as stated.**  
  The paper claims (Section 3, line 77) that because Δ₁ = {1/d}, Δ₂ = {λ−d}, and Δ₃ = {1/d³} admit the same order (all monotonically decreasing in d), "the same holds for Δ₄ := {(λ−d)/d³}."  This is **not generally true**.  The function f(d) = (λ−d)/d³ has derivative f′(d) = (2d−3λ)/d⁴, which changes sign at d = 3λ/2.  When d > 3λ/2 the function increases with d, reversing the order relative to Δ₁.  The paper provides **no condition** (e.g., d < 3λ/2 for all pairs) under which order is preserved, and no argument that such a condition holds for the actual data.  Since this step is the mechanism that connects the computable sensitivity s_y(p_i) to the uncomputable perceived curvature κ_perc, the claimed theoretical link is unsupported.  This does **not** invalidate the paper's empirical findings, but it means the "new and rigorous explanation" (claim i in the introduction) is not rigorous as presented.

- **The constant-perceived-manifold-distance assumption is a non sequitur.**  
  The paper argues (Section 3) that because neural networks can fit random labels, the model perceives the manifold distance between *any* two differently labeled points as a constant δ(y).  This leaps from "the empirical observation that models can memorize arbitrary label assignments" to "the geometry of the model's learned representation treats all between-class distances as equal."  No evidence is provided that this holds for the actual models, data, and training pipeline used in the experiments.  Because this assumption is the bridge between sensitivity and curvature, the gap between the paper's theory and its experiments is significant.

- **The empirical robustness improvements are small, reported with minimal statistical verification, and partly confounded.**  
  The central practical result is a ≈0.2 pp improvement on CIFAR-10 l∞ (Table 2).  This is small relative to typical run-to-run variance in adversarial training, yet the paper reports only 2 random seeds per setting (Table 3) with no confidence intervals, error bars, or statistical significance tests.  The "800 epochs" comparison is based on Wang et al. (2023)'s published results rather than a controlled rerun.  The CIFAR-10 l∞ extension (Table 4) actually *decreases* performance, which the paper attributes to overfitting, but this non-monotonic behavior raises questions about reliability.  Additionally, the practical recipe involves a learning-rate schedule change, a "glitch" circumvention with unclear effect, and stronger PGD-40 on a subset — these are not fully ablated, so the cause of the small gains is uncertain.

### Minor

- **The diffusion-model experiments measure the diffusion model's learned manifold, not the classifier's perceived curvature.**  The claim that these experiments reveal the classifier's "perception of curvature" is indirect.  What is actually shown is that a *separate* generative model produces different outputs for robust vs. non-robust points.  This is interesting qualitative evidence, but not direct support for the paper's core theoretical claim about the *classifier's* training dynamics.

- **The MDS clustering argument (Fig. 2c,d) is partially circular.**  The paper claims that MDS clustering by sensitivity supports Theorem 1.  But MDS operates on pairwise pixel distances, and sensitivity is defined using those same distances, so some correlation is expected by construction.  This does not provide independent evidence.

- **The "glitch" in the Wang et al. pipeline is mentioned but never explained.**  The paper says it "uncovered a glitch" and "circumvented" it, but never states what the glitch was, making it impossible for readers to assess whether the comparison to the baseline is fair.

### Trivial

- The paper states "for any λ∈ℝ" when discussing the ordering of Δ₂ and Δ₄ — but λ is later set to δ(y) (a positive constant).  The "any λ" phrasing is unnecessarily broad and could mislead.

- Several citations in the experimental setup section appear truncated (e.g., line 88 ends with "., 2017" dangling).

## Nice-to-Haves

- Directly validating the constant-distance assumption (e.g., by measuring representation distances in a trained model's latent space between differently labeled points) would substantially strengthen the theory.
- Reporting results with at least 5 random seeds, including error bars or confidence intervals, would address concerns about the robustness of the claimed improvement.
- A more complete ablation isolating each modification (LR schedule, glitch circumvention, PGD-40 on subset) would clarify the source of the gains.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **The harsh critic's claim that Theorem 1 is "trivially true and provides no new insight"** — This is a judgment call, not a weakness.  Theorem 1 provides a useful local-consistency guarantee that supports the sensitivity measure's validity.  It serves its purpose in the framework.  (Removed per rule: not a genuine weakness.)
- **The harsh critic's claim that "Section 2a,b tells us nothing about curvature"** — Overstated.  The paper uses these figures as supporting, not definitive, evidence.  The point is retained in spirit but softened.  
- **The harsh critic's claim that the paper "cannot compute d̃" is a weakness** — The paper explicitly acknowledges this and explains that it is the *perceived* curvature (via sensitivity) that matters.  This is a feature of the approach, not an oversight.  (Removed as a strawman.)
- **The strength finder's claim that "careful ablations rule out all confounding factors"** — Overstated.  The ablations are present but not comprehensive.  This is resolved in the weakness section above.

## Novel Insights

The harsh critic's identification of the mathematical issue with the function (λ−d)/d³ not being monotonic is the most insightful observation across the reviews: it goes beyond "this needs more evidence" to identify a concrete logical gap in the theoretical derivation.  This issue could potentially be fixed by noting that if δ(y) > d(p_i,p_j) for all pairs (which is plausible since manifold distance ≥ pixel distance and δ(y) is a constant), and d(p_i,p_j) < 3δ(y)/2, then monotonicity holds — but the paper provides no such reasoning and the assumption would need validation.  Separately, the finding that focusing on 1024 points and not more is optimal is a surprising empirical result that deserves more attention than the paper gives it.

## Suggestions

1. **Fix the mathematical gap**: Either prove the order equivalence under explicit conditions (e.g., if d_max < 3δ(y)/2 for all pairs) and validate those conditions on the actual data, or abandon the formal link between sensitivity and curvature and instead present sensitivity as a *proxy* motivated by geometric intuition rather than a proven equivalent.

2. **Add statistical rigor**: Report means and standard deviations across at least 5 random seeds for the main robustness results (Tables 2–4).  Without this, a 0.2 pp improvement could easily be noise.

3. **Clarify the glitch**: State clearly what the training-pipeline glitch was, how it was circumvented, and why this does not affect the fairness of the comparison.

4. **Validate or weaken the constant-distance assumption**: Either provide evidence (e.g., via latent-space analysis) that differently-labeled points have approximately equal representation distance, or explicitly frame this as a working assumption / approximation rather than a conclusion from the random-labels literature.

## Score and Decision

This paper tackles an interesting question and provides some genuinely novel observations (the diffusion-model cloning results, the fact that 1024 points suffice for a signal).  However, the theoretical framework that is the paper's stated primary contribution contains a mathematical gap that undermines the claimed "rigorous" link between sensitivity and curvature.  The empirical improvements are small, statistically unverified, and partly confounded.  These weaknesses are significant enough that the paper in its current form does not convincingly support its core claims.

I assign a score of 4.5, reflecting a paper with interesting ideas but fundamental issues in both theory and experimental validation that prevent acceptance at a top venue.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>