Now I have sufficient calibration. Let me write the final consolidated review.

**Initial bracket (Round 1):** Between 2.0 and 3.5 based on the weak anchors (CURATE at 2.80, Rule-Based GridWorld at 3.00, 3D Curriculum at 2.50).

**Narrowing (Round 2):** Comparing against anchors in the 2.0–4.5 range places this paper at 3.0. It is better written than CURATE (2.80) and has a clearer conceptual contribution, but its experiments are significantly weaker than Concrete-to-Abstract Goals (4.00) or Test-time Offline RL (5.00), both of which were still rejected. The paper is most comparable to "All Life is Problem Creation" (3.00) — a conceptually interesting paper with insufficient experimental support.

**Final score: 3.0 — Reject**

---

## Summary

This paper proposes a conceptual reframing of curriculum learning in goal-conditioned RL: curricula should be understood not merely as exploration heuristics, but as "selective data acquisition" mechanisms that reshape the training distribution. The authors illustrate this perspective by comparing uniform goal sampling to edge-biased curricula in a GridWorld environment with UVFAs, showing modest improvements in edge-goal success rates.

## Strengths

1. **Clear conceptual reframing.** The paper explicitly articulates an underexplored perspective: curricula as structural mechanisms for biasing training distributions rather than purely exploration aids (Section 1). This framing is well-motivated and connects curriculum design to questions of function approximation and open-ended learning.

2. **Tunable effect demonstrated.** The weighted curriculum variant (Section 3.2) increases the edge-goal sampling bias and produces larger gains (Δ_edge ≈ +0.18 in Figure 3, and +0.083 in Table 1), providing evidence that the effect scales with distributional bias. This supports the claim that curricula are tunable data-acquisition mechanisms.

3. **Clean writing and straightforward experimental setup.** The paper is well-organized and the experimental pipeline (data collection → UVFA training → zero-shot evaluation) is easy to follow. The isolation of goal-sampling distribution as the sole manipulated variable is methodologically sound in principle.

## Weaknesses

### Major

1. **The experiments do not adequately support the core claims.** The reported improvements are small and not statistically significant. At H=16, the baseline curriculum achieves overall success 0.370±0.151 vs. uniform 0.361±0.060, and edge success 0.217±0.125 vs. 0.183±0.131 — all error bars overlap substantially. With only three seeds and no statistical tests, the paper's claim of "consistent improvements on harder edge goals" (Section 3.1) is not supported by the evidence presented.

2. **The paper claims to measure mechanisms it does not actually measure.** The central thesis is that curricula improve learning by reshaping the training distribution and reducing approximation error. Yet the paper never quantifies the training distribution (e.g., empirical frequency of each goal in the dataset), never measures value approximation error (e.g., MSE against a ground-truth value function), and never shows that distribution shift mediates success-rate improvements. Figure 2's caption asserts it shows "Training distributions" but the figure only reports success rates. The mechanism story is therefore asserted, not demonstrated.

3. **No comparison to standard GCRL baselines.** The problem of sparse reward for hard goals in GCRL is precisely what Hindsight Experience Replay (HER, Andrychowicz et al., 2017, cited in the paper) was designed to address. Without any comparison to HER or other standard GCRL methods, it is unclear what new insight the "data selection" lens provides beyond existing understanding. The paper frames this as a conceptual contribution, but some empirical anchoring against known methods is needed to ground the claims.

### Minor

4. **Experimental details are underspecified, harming reproducibility.** The grid size and number of cells are not stated (Section 2.1). The exact sampling probabilities for edge vs. interior cells in the curriculum are not specified (Section 2.4). The mechanism for "greedy action selection under PBRS shaping" during data collection (line 84) is ambiguous — it is not explained how greedy actions are selected without a learned value function (the PBRS potential φ(s,g) = -d(s,g) can provide a proxy, but this is not clarified). How the "weighted curriculum" adjusts sampling proportions based on "empirical difficulty" (line 119) is described only qualitatively.

5. **Potential-based reward shaping (PBRS) confounds the curriculum effect.** PBRS with φ(s,g) = -d(s,g) already provides a dense reward signal that strongly correlates with task difficulty (Section 2.3). This may substantially reduce the need for curricula and could explain the small observed effects. The paper does not discuss this interaction or test the curriculum without PBRS.

6. **Figure 2 caption is misleading.** The caption states "Training distributions and success rates at horizon H=16" but the figure shows only success rate bars — no distribution information is presented. This overstates what is actually shown.

7. **Table 1 vs. main-text numbers can confuse readers.** Section 3.1 reports baseline numbers (NoCurr 0.361±0.060 overall), while Table 1 shows weighted-condition numbers (NoCurr 0.276±0.055). Section 3.3 references Table 1 without clarifying it refers to the weighted condition, not the baseline. This is disorienting.

### Trivial

- None that survive filtering.

## Nice-to-Haves

- Running the same experiment *without* PBRS (or with sparse reward) would directly test whether the curriculum's role is more pronounced when the learning signal is weaker, which would strengthen the "data selection" hypothesis.
- Reporting individual seed results or bootstrapped confidence intervals would help readers assess the reliability of the improvements.
- Quantifying the training distribution (e.g., plotting empirical goal frequencies under each condition) would directly support the distribution-shift claim.
- Adding an HER baseline would help contextualize the magnitude of the observed gains.

## Removed Points

- **"Logically circular" data collection** (Harsh Critic point 1): Removed because greedy action selection under PBRS can be implemented using the potential function φ(s,g) = -d(s,g) directly (shortest-path policy), without requiring a pre-trained value function. The protocol is underspecified but not circular.
- **"Table 1 title cut off"**: Parser artifact; removed per formatting rules.
- **"Section 2.4 curriculum detail about fixed/changing probability"**: Merged into the minor weakness about underspecified details; not a standalone point.
- **Generic strengths from Strength Finder** about "addressing an important problem": Removed per filtering rules — such strengths are superficial and not specific to this paper's contribution.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder generally recapitulate the paper's claims rather than adding interpretive depth. The one genuinely novel observation across both reviews is that the PBRS reward shaping may be a confound that reduces the observable effect of the curriculum — this interaction is not discussed in the paper.

## Suggestions

1. **Strengthen the link between mechanism and measurement.** Add a quantitative analysis of the training distribution (e.g., histogram of goal frequencies under each sampling scheme) and measure UVFA approximation error (e.g., MSE against DP-computed values per goal). Without these, the paper's core claim about distributional shifts remains speculative.

2. **Add a sparse-reward condition.** Run the same experiment without PBRS to disentangle the curriculum's effect from the dense reward signal. This would directly test whether curricula help through data selection or merely supplement existing exploration.

3. **Increase statistical rigor.** Use more seeds (10+), report per-seed results, and provide bootstrapped confidence intervals or significance tests for the success-rate differences.

4. **Add at least one standard GCRL baseline.** HER is the most natural comparison and would give context for whether the observed gains are meaningful relative to existing methods.

5. **Specify all experimental details.** Grid dimensions, exact sampling distributions for each curriculum variant, and the data-collection policy should be fully described.

## Score and Decision

**Round 1 bracket:** 2.0–3.5
- CURATE (2.80): similar-topic curriculum paper with more method but poorer writing; slightly weaker overall.
- Rule-Based GridWorld (3.00): more ambitious method but limited to grid domains; comparable.
- 3D Curriculum Design (2.50): weak experiments, rejected; our paper is slightly better.
- All Life is Problem Creation (3.00): conceptually interesting but experimentally limited; similar quality.

**Round 2 narrowing:** anchors within (2.0, 4.5) and (3.0, 5.0)
- Concrete-to-Abstract Goals (4.00, reject): more extensive experiments across multiple environments; our paper is clearly weaker.
- MOGCSL (3.50, reject): real-world datasets, comprehensive baselines; much stronger empirically.
- Test-time Offline RL (5.00, reject): comprehensive experiments across many tasks; much stronger.
- Goal-Conditioned Supervised Learning (3.50, reject): had real-data experiments; our paper is weaker.

**Final position:** Below all three rejected moderate-scoring papers (3.50–5.00). Comparable to the weakest accepted paper in the set (CURATE at 2.80). The conceptual framing is legitimate but the experimental evidence is too thin for ICLR.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>