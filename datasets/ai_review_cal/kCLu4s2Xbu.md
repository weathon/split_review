- Decision: Reject
- Avg Score: 3.60
- Scores: 1, 3, 6, 3, 5
Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes TDGBA, an offline imitation learning method that uses Wasserstein distance to compute a **trajectory-level alignment measure** between unlabeled trajectories and expert demonstrations, treats this alignment as an "implicit expert preference," and feeds it into a trajectory diffuser (borrowed from FTB) to generate high-quality trajectories for behavior cloning. The key idea is to replace expensive human preference data with a cheap geometric proxy while retaining the preference-guided generation pipeline. Experiments on D4RL locomotion and antmaze tasks show strong performance against BC-based and reward-based offline IL baselines.

## Strengths

1. **Strong empirical results on D4RL benchmarks.** Table 2 shows TDGBA outperforms all compared BC-based offline IL methods (DemoDICE, SMODICE, LobsDICE, SQIL, BC, 10%BC) on all 9 locomotion tasks, with an average normalized score 18.74% ahead of the second-best. Table 3 shows competitive or leading results against reward-based methods (ORIL, UDS, OTR, SEABO) in 7 of 11 tasks — notable because TDGBA is a BC-based method that avoids reward learning entirely. These results are consistent across multiple seeds and are reported with standard deviations.

2. **Trajectory-level alignment as a proxy for preferences, removing the need for human annotation.** The alignment measure computed from a single expert trajectory (Figure 2) correlates with ground-truth returns as well as or better than a preference model trained on 15 human-labeled trajectory pairs (FTB). Table 1 further shows that FTB's preference model accuracy fluctuates non-monotonically with more data. This provides empirical justification for using the geometric proxy in place of expensive human preference data.

3. **Effective trajectory generation with demonstrated diversity and accuracy.** Section 5.3 shows that TDGBA-generated trajectories have larger L2 distances from the dataset (indicating diversity) while exhibiting lower mean absolute error (dynamic accuracy) than even minimal Gaussian augmentation (Figure 4b,c). This demonstrates that the diffusion-based generation, guided by alignment preferences, produces both novel and physically plausible trajectories.

4. **Robustness to key hyperparameters.** Tables 5 and 6 show that performance is stable across the scaling coefficient β (5–30) and number of blocks K (3–7), suggesting the method is not brittle.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguity in the alignment measure definition (Eq. 4 vs. textual description).** The paper states (line 16): *"Trajectories with small distances are referred to as high-alignment trajectories."* However, Eq. 4 defines the alignment measure as m(τ^u,τ^e) = Σ_i Σ_j f(c(s_i^u,s_j^e) μ*_{i,j}) with the example f(x) = exp(βx). If f is increasing (as exp(βx) with β>0 is), then m *increases* with the Wasserstein distance — i.e., trajectories farther from the expert receive *larger* values of m. This is the opposite of what "alignment" should mean under the paper's own definition. The paper never clarifies whether the actual implementation uses a decreasing function (e.g., f(x)=exp(-βx)), or whether m is interpreted as a misalignment measure and the ordering is flipped downstream. Since m is the quantity used for clustering into blocks (which determines diffusion conditioning), and the paper repeatedly references "high-alignment" vs. "low-alignment" trajectories, this ambiguity affects the interpretability of the entire pipeline. The strong empirical results suggest the implementation works correctly, but the paper must state the unambiguous formula actually used and reconcile it with the textual description.

### Minor

2. **No explicit justification or ablation for state-only alignment.** The cost function in Eq. 3 uses only state vectors c(s_i^u, s_j^e). The paper does not discuss why actions are excluded from the alignment computation, nor does it ablate state-only vs. state-action alignment. Section 5.4 compares against OTR and PWIL in both state-only and state-action variants, and TDGBA (state-only) still wins — which suggests the choice may be benign — but a direct controlled ablation on TDGBA itself would strengthen the evidence and provide a practical insight.

3. **Overstated novelty framing around "preference learning."** The paper repeatedly claims (abstract, lines 4–5; line 29) to be the *"first to successfully transfer the advantages of preference learning to offline IL."* However, TDGBA does not *learn* preferences from pairwise comparisons (as in standard preference learning / RLHF); it computes a deterministic geometric distance and uses it as a preference proxy. This is a valuable practical insight — that a cheap geometric proxy can substitute for expensive human preferences in the FTB generation pipeline — but framing it as a preference-learning contribution is a stretch. The paper's actual contribution (replacing human preferences with a geometric alignment measure in the FTB framework) is solid and does not need this overclaim.

4. **Missing direct comparison to FTB.** FTB (Zhang et al., 2023) is the method from which the trajectory diffuser, block clustering, and conditioning scheme are adopted. A direct performance comparison between TDGBA (no human preferences) and FTB (with human preferences) on the same tasks would provide a clear quantification of the cost of replacing human preferences with the geometric proxy. If TDGBA matches or approaches FTB's numbers, the contribution is strengthened; if not, the gap should be discussed. Currently, FTB appears in none of the main tables.

### Trivial

- "offilne" appears in place of "offline" (e.g., line 12, 29, 36).
- The phrase "inaugural application" (line 4) is unusual; "first application" would be clearer.

## Nice-to-Haves

- **Spearman/Pearson correlation coefficients** for the alignment measure vs. ground-truth returns in Figure 2, rather than relying on visual inspection.
- **Ablation of the cost function inputs** (state-only vs. state-action) on TDGBA itself, to confirm that the state-only choice does not leave performance on the table.
- **Qualitative examples** of generated trajectories (e.g., a state-sequence comparison of low-alignment, generated, and expert trajectories) to give readers intuition for what the diffuser produces.

## Removed Points

These points were raised by reviewers but are removed after verification:

- **"Alignment measure is undefined / fatal flaw" (Critic's Issue 1 as "fatal"):** Downgraded to Major. While the naming inconsistency between m (Eq. 4) and the textual definition of "alignment" is real and must be fixed, it does not invalidate the empirical results or the method's core logic. The actual computation still produces a valid ranking of trajectories; the ambiguity is in how the scalar relates to the name. Calling it "fatal" overstates the severity.

- **"Algorithm 1 not in main text / reproducibility gap":** Removed per instruction — the parser strips appendix content from all papers. The algorithm exists in the original submission.

- **"Missing related work" references:** Removed per instruction.

- **Typo/formatting nitpicks (mixed, parser artifacts):** Removed per instruction. The parser introduces formatting errors; they are not author errors.

- **"Baseline numbers might be from original papers without re-running":** Partially removed — this is a speculative concern; the paper states it follows prior work's settings and uses D4RL standard benchmarks, and mean/std over 5 seeds is reported.

- **Strength Finder's "first demonstration of preference-learning benefits" framing:** Softened — it conflicts with the verified weakness about overstated novelty claims. The insight (geometric proxy works) is real, but the "first to bring preference learning to offline IL" framing is imprecise.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the alignment-definition ambiguity and the missing FTB comparison, but do not identify a fundamentally new angle on the problem that the paper itself misses.

## Suggestions

1. **Fix Eq. 4.** State the exact formula used in experiments (if f(x)=exp(-βx) or a similar decreasing function is used, say so explicitly; or define alignment as -W or 1/W). Reconcile the mathematical definition with the textual description so that "high alignment" unambiguously corresponds to "small Wasserstein distance."

2. **Add an FTB comparison row** to Table 2 or 3, using FTB's reported numbers on the same D4RL tasks (or re-running FTB under the same evaluation protocol). This is the most informative upper bound for the method.

3. **Add a state-only vs. state-action ablation** for the alignment computation on a subset of tasks to confirm that state-only is sufficient.

4. **Reframe the novelty claims** more precisely: e.g., "we show for the first time that a geometric alignment measure can replace human preferences in preference-guided trajectory generation for offline IL," rather than claiming to transfer "preference learning" to offline IL.
