Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper introduces Dig-DEC (dual information gain DEC), a new model-free decision-estimation coefficient that replaces the optimism principle of prior work (optimistic E2D [FGQ+23]) with pure information-gain-driven exploration. The key contributions are: (1) Dig-DEC is always no larger than optimistic DEC and can be strictly smaller in constructed instances; (2) removing optimism enables the first model-free regret bounds for hybrid MDPs (stochastic transitions, adversarial rewards) with bandit feedback, resolving an open problem from [LWZ25]; (3) refined online estimation procedures that improve regret rates for average estimation error and achieve √T for Bellman-complete MDPs. The framework unifies and generalizes the AIR approach of [XZ23, LWZ25] with a new divergence-based analysis.

## Strengths

1. **First model-free regret bounds for hybrid MDPs with bandit feedback (resolves open problem)**. The paper explicitly states this as the main open problem from [LWZ25] (Section 2.2), and the removal of optimism is the enabling mechanism because it "avoids explicit construction of the reward estimator" (Section 6), which is the core difficulty in the bandit setting. This is a genuine advance.

2. **Dig-DEC provably subsumes optimistic DEC and can be strictly smaller**. Theorem 13 shows dig-dec ≤ o-dec + η, meaning any setting handled by optimistic E2D is also covered. Theorem 14 provides a concrete 3-armed bandit instance where optimistic DEC suffers Ω(√T) but Dig-DEC achieves O(1) regret, demonstrating strict improvement. The decomposition into KL regularization + information gain (Section 6) provides a clean conceptual explanation.

3. **Achieves √T for Bellman-complete MDPs for the first time in a DEC framework**. The abstract reports improving the prior DEC bound from T^{5/6} to √T, matching optimism-based approaches [JLM21, XFB+23]. This is enabled by the refined two-timescale posterior update (Section 4.2.2) that bounds Est to O(log²|Φ|) (Theorem 11).

4. **Generalizes the AIR framework with a more flexible analysis**. Section 4 introduces a divergence-based analysis that "nicely connects to the standard analysis of mirror descent," moving beyond the restrictive "constructive minimax theorem" of prior work. Appendix C shows the framework recovers previous results without additional complexity.

5. **Novel unbiased estimator improves concentration for average estimation error**. Section 4.2.1 contrasts the paper's unbiased estimator (using sample splitting) with the biased estimator of [FGQ+23], demonstrating a clear algorithmic refinement that reduces the Est bound from T^{1/2}·(larger factor) to N log|Φ| T^{1/2} (Theorem 7).

## Weaknesses

### Major

1. **Contradictory exponent claims across abstract, introduction, and Table 1.** The abstract reports improving FGQ+23's bounds from T^{3/4} to T^{3/5} (on-policy) and from T^{5/6} to T^{7/8} (off-policy). However, Table 1 — the paper's own summary for the same D_av (average estimation error) setting — gives T^{2/3} for both on-policy and off-policy bilinear classes. Three different exponent pairs appear for what should be the same result (abstract: T^{3/5}/T^{7/8}; Table 1: T^{2/3}/T^{2/3}; introduction line 39: T^{3/2}/T^{5/6} after garbled rendering). Moreover, T^{7/8} ≈ 0.875 is *worse* than T^{5/6} ≈ 0.833, so the claimed off-policy "improvement" is mathematically a deterioration. These inconsistencies are verifiable from the extracted text (abstract line 19, Table 1 lines 268–269, intro line 39) and must be resolved before the paper can be properly evaluated.

2. **The "improvement in Est's rate" is tautological.** Section 4.2.1 (line 219) states: "our construction of the estimator improves their rate of Est from √T to T^{1/2}." Since √T = T^{1/2}, this claims an improvement with no change in the T-exponent. The improvement is in the *unbiasedness* and the *N log|Φ|* factor, not the T-exponent, so the wording is incorrect as written and misleads about the nature of the contribution.

### Minor

3. **Theorem 14's constant regret claim lacks sufficient intuition in the main text.** The claim that a 3-armed bandit instance yields max_a E[Reg(a)] ≤ 1 for all T is extraordinary. The paper says the proof is in Appendix J (stripped from this extract) and offers only a brief conceptual explanation (the KL information gain term captures distributional differences that mean-based D terms miss). The critic's concern about standard Ω(log T) lower bounds is misplaced — this is a constructed Φ-restricted DMSO instance, not a standard MAB — but more intuition in the main text would help readers assess the claim without chasing the appendix.

4. **Hybrid setting regret exponents in Table 2 appear superlinear.** The regret column of Table 2 reports T^{3/2} for bilinear on-policy and T^{13/8} for bilinear off-policy (D_av), both exceeding 1. T^{3/2} is superlinear and would not constitute a valid sublinear regret bound. These may be PDF-rendering artifacts (e.g., T^{2/3} misrendered as T^{3/2}), but the paper must clarify what the intended exponents are.

5. **The paper is silent on computational aspects.** Algorithm 1 requires solving an infinite-dimensional minimax optimization over Δ(Π) × Δ(Ψ) at each round. While this follows the convention of prior DEC papers [FKQR21, FGQ+23, XZ23, LWZ25] which are information-theoretic rather than algorithmic, a brief acknowledgment of this limitation would improve the paper's honesty and prevent unrealistic expectations.

### Trivial

6. The introduction (line 39) contains the string "T^{3/2}/T^{5/8}" and "T^{3/2}/T^{5/6}" which are inconsistent with the abstract and appear to be rendering errors (T^{3/2} is superlinear and would be meaningless as a regret bound). This needs correction regardless of whether it is a source typo or extraction artifact.

## Nice-to-Haves

- **Lower bound references.** Adding a discussion of known information-theoretic lower bounds for the settings considered would help readers gauge the optimality gap of the achieved rates.
- **High-probability bounds.** The paper briefly mentions (end of Section 5.1) that high-probability versions exist, but more detail would strengthen the practical relevance.
- **Main-text sketch of estimation procedures.** The posterior update procedures (Algorithms 2–4) are only mentioned by name; a one-paragraph sketch of the key ideas (e.g., the split-sample trick) would make Section 4.2 more self-contained.

## Removed Points

These points appeared in the inputs but are excluded or demoted from the main weaknesses for the reasons given:

- **Theorem 6 bound not fully justified (harsh critic).** The critic questions whether replacing ρ_t with max_ρ is valid. This is a standard worst-case bounding technique, and the paper refers to the appendix for details. This is standard practice in theoretical papers and not a genuine weakness. → Removed.

- **Theorem 14 contradicts standard bandit lower bounds (harsh critic).** The critic argues Ω(log T) or Ω(√T) lower bounds rule out constant regret. However, Theorem 14 is about a constructed Φ-restricted DMSO instance, not a standard stochastic bandit — the Φ-class structure can make the problem easier than standard MAB. The criticism relies on an incorrect analogy. → Removed; replaced with a weakened version (Minor #3 above).

- **Missing computational efficiency discussion (harsh critic).** Demanding computational solutions for the infinite-dimensional saddle-point problem is out of scope for this information-theoretic framework, following the same convention as all prior DEC papers. → Removed.

- **Missing lower bounds table (harsh critic).** This is a suggestion, not a weakness. → Moved to Nice-to-Haves.

- **Assumption 6 too technical (harsh critic).** The paper is a theoretical paper; technical assumptions are expected. → Removed.

- **Strength Finder: generic strengths about problem importance.** Removed because they lack specific evidence tied to the paper's content and are not competitive strengths.

- **Strength Finder: strength about T^{7/8} improvement.** The claimed improvement T^{5/6} → T^{7/8} is actually a deterioration, so this claimed strength is invalid. → Removed from Strengths, moved to the weakness list.

## Novel Insights

The most insightful observation emerging from the reviews is that the tension between the harsh critic's technical scrutiny and the strength finder's positive framing reveals two distinct evaluation surfaces: **(a)** the paper's core technical machinery (Dig-DEC, divergence-based AIR analysis, unbiased estimation) is sound and genuinely advances the state of the art; **(b)** the presentation of the *results of that machinery* (regret exponents, improvement claims) contains several inconsistencies that are separable from the machinery itself. The paper would benefit from adding a "Validation" paragraph that traces each claimed rate back to the specific theorem, assumption instantiation, and η-tuning calculation, making the chain from theory to reported exponents fully transparent.

## Suggestions

1. **Fix all exponent inconsistencies.** Reconcile the abstract, introduction, and Tables 1–2 so that one set of correct, consistent numbers appears throughout. In particular: (a) verify whether the D_av regret exponent for stochastic bilinear classes is T^{2/3} (as in Table 1) or something else; (b) correct the off-policy exponent if T^{7/8} is indeed wrong (it appears to be a deterioration); (c) verify and clarify the hybrid exponents in Table 2, especially the entries that appear superlinear.

2. **Fix the "Est from √T to T^{1/2}" claim.** Clarify that the improvement is in the unbiasedness and the N log|Φ| factor, not the T-exponent.

3. **Add a brief intuitive explanation for Theorem 14** in the main text — even 2–3 sentences explaining how the Φ-class structure enables constant regret despite the "3-armed bandit" framing.

4. **Include a derivation trace.** Add a short paragraph showing how a representative rate (e.g., T^{2/3} for bilinear on-policy) is obtained from T·dig-dec + Est/η by plugging in the dig-dec bound (H²dη) and Est bound (N log|Φ| T^{1/2}) and optimizing η. This would let readers verify any rate independently.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Three queries covering weak (avg < 3.5), middle (3.5–7.5), and strong (avg > 7.5) bands. Weak-band anchors (scores 2.33–3.20) were on unrelated topics. Middle-band anchors included "Horizon-free RL in Adversarial Linear Mixture MDPs" (6.00), "Optimal Strong Regret in CMDPs" (6.00), and "Model-Free BPI in CMDPs" (5.20). Strong-band anchors (scores 8.00) were on policy gradients, multi-agent RL, and applied topics — structurally different from this paper's pure theory contribution. **Initial bracket: 5.0–7.0.**

**Round 2 — Narrowing:** Queries targeting 4.5–6.5 and 5.5–7.5. Retrieved "Decoupled Actor-Critic" (5.75, empirical, less relevant), "Horizon-free Adversarial MDP" (6.00, the closest theoretical counterpart), "Stochastic Bandits Robust to Attacks" (6.50), "Private Adversarial Bandits" (5.67), "Tree Search with Delay" (5.75). The horizon-free adversarial MDP paper (score 6.00) is the best comparator: it solves an open problem, has clean presentation, and achieves near-optimal rates. The current paper has broader scope (new framework + multiple applications vs. one algorithm) and resolves a different open problem, but its presentation is less polished (exponent inconsistencies). **Final bracket: 5.5–6.5.**

**Anchor comparisons:**
- *aPNwsJgnZJ* (Horizon-free Adversarial Linear Mixture MDPs, avg 6.00): Comparable theoretical depth and contribution significance. Current paper has broader scope (new framework + multiple applications) but more presentation issues. → Similar quality.
- *8eNLKk5by4* (Optimal Strong Regret in CMDPs, avg 6.00): Similar theoretical rigor. Current paper's contributions are more structurally novel (new DEC notion) vs. algorithmic improvement. → Slightly stronger.
- *w8Zo7jACq7* (Model-Free BPI in CMDPs, avg 5.20): Current paper has stronger theoretical novelty and broader scope. → Clearly stronger.
- *2h3m61LFWL* (Value-Biased MLE for Linear MDPs, avg 4.25): Current paper is much stronger in both contribution and novelty. → Clearly stronger.

**Positioning:** The paper sits near the top of its bracket. The theoretical contributions (new DEC, first model-free hybrid bounds, improved estimation) are a genuine advance over prior DEC literature, comparable to the 6.0 anchors. The exponent errors are real but do not affect the core theoretical machinery — they are presentation issues in reporting the corollary rates. After these are fixed, the paper would be solidly in the 6.5–7.0 range.

**Final score: 6.0** — Strong accept with mandatory minor revisions to fix exponent inconsistencies.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>