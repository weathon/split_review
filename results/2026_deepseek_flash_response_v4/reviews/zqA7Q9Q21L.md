Now I have solid calibration anchors. Let me write the final consolidated review.

**Round 1 bracket:** Between the weak anchors (2.50–3.40) and the strong anchors (8.00), I initially bracketed the paper in the 4.0–6.5 range.

**Round 2 narrowing:** Calibration against 5.33–6.33 anchors shows this paper is comparable to papers scoring 5.50–5.75 — it has stronger theoretical contributions than most but a more significant empirical gap than some. The accepted anchor at 5.75 (MORL generalization) had no major methodological gaps, while the rejected anchors at similar scores typically had one significant weakness.

**Final score:** 5.5.

---

## Summary

This paper introduces R2PS, an approach for worst-case robust real-time pursuit strategies under partial observability in graph-based pursuit-evasion games (PEGs). The contributions are threefold: (1) proving that a dynamic programming (DP) algorithm for Markov PEGs maintains optimality under asynchronous moves (Theorem 2, Corollary 1); (2) proposing a belief preservation mechanism (Equations 4–7) to handle partial observability with Õ(|V|) per-timestep complexity, with a guarantee that it reduces to the optimal perfect-information policy when the evader's position is known (Lemma 2); and (3) embedding this mechanism into the EPG cross-graph RL framework to train a GNN-based pursuer policy with O(n²m) inference time, demonstrated on real-world maps with zero-shot generalization.

## Strengths

1. **Theoretical extension of DP optimality to asynchronous moves.** Theorem 2 and Lemma 1 (Section 3.1) prove that the distance table D from Algorithm 1 induces strictly optimal policies for both pursuer and evader under asynchronous-move settings where the evader observes the pursuers' action before moving. This extends the prior DP analysis (Lu et al., 2025a) beyond synchronous moves.

2. **Belief preservation mechanism with provable reduction guarantee.** The belief-averaged policy (Equation 6) and update rule (Equation 7) are shown in Lemma 2 to reduce to the provably optimal perfect-information policy when Pos is a singleton. Table 1 validates this empirically: DP_belief consistently outperforms DP_Pos across all 10 test graphs (e.g., 0.78 vs 0.59 on Grid Map, 0.90 vs 0.73 on Downtown Map), with 49–115% relative improvement on graphs with large diameter.

3. **Real-time feasibility rigorously demonstrated.** Section 4.2 derives O(n²m) RL inference complexity vs. Õ(n^{m+1}) for DP recomputation. Table 3 shows concrete gaps: on Sagrada Familia (2065 nodes), RL inference takes 0.0099s while DP takes 139s — over 14,000× faster. All large-graph inferences are below 0.01s, supporting the real-time claim in the title and abstract.

4. **Zero-shot generalization to unseen real-world graphs.** Table 2 shows the cross-graph RL policy (trained on 300 graphs never seen during evaluation) achieves substantial success rates against the strong DP_async evader on unseen maps (0.76 on Scotland-Yard, 0.95 on Times Square), where a PSRO policy trained directly on those test graphs achieves 0.00 and 0.04 respectively.

5. **Informative ablation of the belief mechanism.** Table 4 systematically varies belief update frequency (every 1/2/3 steps) and compares against a known-opponent oracle. Success rates drop monotonically with less frequent updates (e.g., Scotland-Yard: 0.73→0.34→0.28), providing direct causal evidence that the belief mechanism drives performance.

6. **Observation range generalization.** Section 5.3 (Table 7 referenced) reports that the RL policy trained with minimum observability (range 2) monotonically improves when given larger observation ranges at inference, demonstrating generalization along the sensing-capability axis.

## Weaknesses

### Major

- **Underspecified PSRO training opponent undermines the headline empirical comparison.** The paper's central empirical claim is that R2PS "consistently outperforms the PSRO policy directly trained on the test graphs" (Section 5.2, Table 2). However, the paper never states what opponent the PSRO policy trains against. R2PS explicitly trains against ν* —the optimal DP evader (Section 4.1, line 177: "use ν* = ν_i^* as the adversarial policy"). If PSRO was run in standard self-play (its typical mode), it would never encounter the optimal DP evader during training, which would trivially explain its poor performance against DP_async in Table 2 (e.g., 0.00 on Scotland-Yard, 0.00 on Hollywood Walk of Fame). The comparison may reflect a training-condition mismatch rather than architectural superiority. The paper should (a) specify the PSRO training opponent, and ideally (b) include a variant where PSRO is also trained against the DP evader to create a fair comparison.

### Minor

- **Missing statistical significance / error bars.** Tables 1–4 report success rates averaged over 500 or fewer episodes without confidence intervals, standard deviations, or error bars. Since these are Monte Carlo estimates, variance could be substantial, especially on harder graphs where success rates are low (e.g., Hollywood Walk of Fame at 0.38). Adding error bars or confidence intervals would strengthen the reliability of the reported comparisons.

- **Asymmetric BR_async reporting.** Table 2 includes BR_async (best-responding evader trained against the R2PS pursuer) only for "Ours" with no PSRO column. Training a best-responding evader against the PSRO pursuer as well would provide a more complete picture of each pursuer's robustness under its own worst-case opponent.

- **Non-monotonic success rates in scalability tests require commentary.** Table 3 shows some success rates against DP_async that are higher than the corresponding rates on smaller versions in Table 2 (e.g., Hollywood: 0.38→0.46, Sagrada: 0.20→0.33, The Bund: 0.25→0.46). Since these are discretizations at different resolutions rather than strictly scaled versions of the same graphs, the paper should comment on whether this reflects topological differences or discretization effects.

- **"Worst-case robust" language is stronger than what is formally demonstrated.** The paper uses "worst-case" throughout but evaluates against specific opponent policies (DP_async, BR_async). While these are strong opponents, a formal worst-case guarantee against any evader policy is not provided. Qualifying this to "empirically robust against provably strong evader policies" would better match the evidence.

### Trivial

- **PSRO citation typo.** Referenced as "Lancet et al., 2017" (line 240) but the correct spelling is "Lanctot et al., 2017" (used correctly on line 31 in the contributions list but misspelled in the evaluation section).

## Nice-to-Haves

- Training a PSRO variant against the DP evader (matching R2PS's training condition) would provide the fairest comparison.
- Reporting success rates with confidence intervals.

## Removed Points

- **No EPG comparison.** The harsh critic demanded comparison against EPG (the paper's foundation). Removed because EPG requires perfect information and does not handle partial observability — comparing against a method that cannot operate in the paper's setting is not meaningful. The paper's contribution is extending EPG to partial observability, and it already compares against PSRO as a general RL alternative.

- **"Transitivity argument is hand-wavy."** This argument (Section 4.1) is presented as conceptual motivation following Czarnecki et al. (2020), not as a formal claim. It does not constitute a methodological weakness.

- **"Strong evader assumption not acknowledged."** The paper repeatedly acknowledges this asymmetric setup (Section 1: "the evader may have stronger observation capabilities than the pursuers"; Section 2.1), making this a deliberate design choice for security scenarios.

- **Critique of "worst-case robust" terminology.** The paper's language is somewhat ambitious but the evaluation against DP_async (provably optimal) and BR_async (trained best response) provides reasonable empirical grounding. This is weakened to a Minor point rather than removed entirely.

## Novel Insights

The most operationally useful insight from the reviews is that the PSRO baseline training condition is underspecified — this is a concrete gap that, if resolved, would either substantially validate or weaken the paper's central empirical claim. The strength finder's observation that the monotonic improvement under larger observation ranges is noteworthy (it suggests the trained representation captures more than just the specific sensing condition used during training) is also a genuine insight not fully emphasized in the paper itself.

## Suggestions

1. **Specify the PSRO training opponent.** State whether PSRO used self-play, a fixed opponent, or the DP evader. If self-play was used, add a variant trained against DP_async for a fair comparison. This is the single most impactful improvement to the paper.
2. Add confidence intervals or error bars to all reported success rates (Tables 1–4).
3. Briefly discuss the non-monotonic success rates in Table 3 vs. Table 2 — acknowledge whether graph topology or discretization explains the pattern.
4. Qualify the "worst-case" language to better reflect the empirical (rather than formal) nature of the robustness claim.
5. Fix the PSRO citation spelling (Lancet → Lanctot).

## Score and Decision

**Round 1 bracket (initial):** 4.0–6.5. The paper is clearly stronger than the 2.50–3.40 weak anchors (rejected GNN+RL papers with basic flaws) and clearly weaker than 8.00 strong anchors (accepted papers with comprehensive contributions).

**Round 2 narrowing (anchors read in full or partially):**
- *tuEP424UQ5* (5.75, Accept): MORL benchmark paper; limited theory, accepted despite evaluation concerns. The current paper has stronger theoretical contributions but a more significant empirical gap.
- *TyZhiK6fDf* (5.60, Reject): Dyna-PSRO; similar structure of comparing against PSRO but had presentation issues and missing baselines. The current paper is better presented but has a similar-caliber empirical gap.
- *5btqauRdz0* (5.50, Reject): Zero-shot GNN generalization. Mixed reviews (6,5,5,6), accepted-style paper but rejected. Comparable in overall quality.
- *Q00CO1Tm6M* (5.75, Reject): Theoretical POMDP paper. Strong theory but rejected due to niche applicability. The current paper is more applied.
- *99tKiMVJhY* (6.33, Accept): Dec-POMFC. Strong theory+experiments. The current paper is weaker than this anchor.
- *Yx7TnC6AAp* (5.75, Reject): IIEFGs with linear function approximation. Pure theory paper. The current paper has more practical validation.

**Final score:** 5.5 — The paper presents a sound method and genuine theoretical contributions (DP optimality under async moves, belief mechanism), but the main empirical claim is weakened by an underspecified PSRO baseline. The core ideas are promising and the theoretical analysis is solid, but the experimental evidence for the headline result is incomplete in its current form. The paper falls slightly below the acceptance bar due to this gap, but the weaknesses are addressable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>