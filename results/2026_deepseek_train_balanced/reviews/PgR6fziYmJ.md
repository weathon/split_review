## Summary

HP3O proposes a hybrid-policy variant of PPO that augments on-policy updates with a FIFO trajectory replay buffer containing recent policies' trajectories. Each training batch mixes the best-return trajectory with randomly sampled prior trajectories. The paper provides policy improvement bounds (Theorems 1 and 2) for this non-chronological sampling scheme and evaluates the method on four MuJoCo continuous-control tasks against several baselines.

## Strengths

1. **Theorem 1 extends policy improvement bounds to non-chronologically sampled prior policies.** The paper derives a bound (Eq. 4) where reference policies are randomly sampled from a replay buffer rather than required to be chronologically ordered as in Queeney et al. (2021). Remark 3 explicitly identifies this distinction, and Lemma 2 (whose core idea is clear from Remark 2 even if the equation was lost to the parser) provides the technical foundation that removes the temporal-ordering requirement.

2. **Theorem 2 introduces a value-penalty term in the lower bound for HP3O+.** The extra term (γ C^{π_k} ε)/(1-γ)² in Eq. 5 represents a value gap between the current state value and the best trajectory's value, which Remark 4 describes as a regularization mechanism — a theoretically grounded addition absent in vanilla PPO.

3. **Empirical runtime advantage over SAC is demonstrated.** Section 6.2 shows that HP3O/HP3O+ "take approximately the same training time as PPO" while SAC requires substantially more runtime (Figure 3b), making this a practical contribution for applications where wall-clock time matters.

4. **FIFO buffer design with explicit distribution-drift motivation.** Section 4 clearly motivates why a FIFO eviction strategy is used rather than a standard replay buffer, and Section 6.3 honestly discusses the tradeoffs (good trajectories may only be learned once).

## Weaknesses

### Major

1. **The "ablation study" (Section 6.2) does not actually ablate any component of HP3O.** Despite being labeled "Ablation Study," the section compares variance and runtime across *different algorithms* (HP3O/HP3O+ vs. SAC vs. baselines) and reports explained variance. There is no ablation of the FIFO buffer size, no comparison of including vs. excluding the best trajectory, no comparison of FIFO vs. standard replay, and no isolation of the HP3O+ baseline effect. For a method paper whose algorithm has multiple interacting design decisions (buffer sizing, FIFO eviction vs. alternatives, best-trajectory selection, the new baseline in HP3O+), this is a significant evidential gap. The reader cannot tell which component drives the reported improvements or whether they interact positively.

2. **The claimed variance reduction from the random-sampling framework is asserted without formal or empirical support.** Remark 3 states that Theorem 1's extra expectation operator over multiple trajectories "leads to the smaller variance" compared to Lemma 1. However, no variance analysis is provided — no derivation of how the expectation over v reduces variance, no empirical measurement of gradient variance, and no comparison of variance between single-trajectory and multi-trajectory bounds. Similarly, Remark 4's claim that the value-penalty term "reduces the variance" is intuitive but unsupported by any formal analysis or isolated experiment. These are central claims of the paper (the title itself promises variance reduction).

### Minor

3. **No comparison against TRPO.** The paper compares against A2C (known to perform poorly on continuous control) but omits TRPO, which is a more natural on-policy baseline with a trust-region mechanism directly related to the theoretical framework. This makes the on-policy comparison set weaker than it should be.

4. **Empirical results are reported qualitatively without statistical grounding.** Comparisons in Section 6.1 rely on visual inspection of learning curves ("sharper average slope," "more flattened curve") without statistical tests, effect sizes, or the raw numerical values behind the figures. With only 5 random seeds per condition, the strength of comparative claims ("our proposed methods learn more stably than all baselines") is not commensurate with the evidence.

5. **The connection between the theoretical bound and the empirical gains is not established.** Theorem 1 gives a lower bound on policy improvement, not a bound on sample efficiency or variance. The paper's primary empirical claims (sample efficiency, variance reduction) are not directly connected to the theoretical results shown. The sampling efficiency argument in Remark 5 is hand-wavy ("there exist multiple updates compared to the vanilla PPO").

### Trivial

None of note beyond formatting artifacts introduced by the PDF parser.

## Nice-to-Haves

- A proper ablation study isolating: (a) FIFO vs. standard replay, (b) best-trajectory inclusion vs. random-only sampling, (c) HP3O vs. HP3O+ to isolate the baseline effect.
- Comparison against TRPO as an on-policy baseline.
- Reporting of key hyperparameters (buffer size, learning rates, network architecture, clipping ε) in a table.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Missing Algorithm 1 and Lemma 2 equation (harsh critic's fatal points #1 and #2):** Removed. The paper ends Section 4 mid-sentence with "Algorithm 1 shows" and Lemma 2 is stated without its inequality. However, these are consistent with PDF-parser failures to extract formatted algorithm blocks and equations — the original ICLR submission would have contained both. The instruction explicitly states that parser-induced missing content should not be treated as author errors.

- **Missing experimental hyperparameters (harsh critic's point #3):** Removed per the instruction classifying "undisclosed hyperparameters" as nitpicks about reproducibility that should be removed. Standard RL hyperparameters are typically reported in appendices which are stripped by the parser.

- **Code availability criticism:** Removed. "Code is available here" is a standard placeholder in submissions; code is typically released upon acceptance.

- **Harsh critic's point about Queeney et al. comparison being unsupported:** Downgraded and merged into Major weakness #2 (variance reduction claim unsupported). The paper does identify the technical difference and provides Lemma 2 to ground it. The remaining concern is the unsubstantiated variance-reduction claim, not the novelty of the bound itself.

- **Missing broader impacts section:** Removed. The section title exists ("CONCLUSION AND BROADER IMPACTS") and likely contains content that was not extracted.

- **Strength Finder's generic strengths ("important problem," "reasonable research question"):** Removed as superficial observations that add no evaluative weight.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface genuinely novel observations that the paper itself does not already claim or discuss.

## Suggestions

1. Rename Section 6.2 from "Ablation Study" to "Additional Analysis" and add a genuine ablation study that isolates: (a) FIFO vs. standard replay, (b) best-trajectory sampling vs. random-only, (c) HP3O vs. HP3O+ to isolate the baseline effect. This is the single most important improvement for the paper.

2. Provide either a formal variance analysis or an empirical measurement of gradient variance across the sampling distribution to support the variance-reduction claim in Remark 3. Without this, a central advertised benefit rests on intuition alone.

3. Add TRPO as an on-policy baseline for completeness.

4. Include a table of key hyperparameters (buffer size, learning rates, network architecture, clipping ε) and report numerical results (final mean return with standard deviation across seeds) in a table so the reader need not estimate from figures.

5. Clarify in the theoretical section how the bound in Theorem 1 relates to sample efficiency or variance — the current framing presents the bound without connecting it to the paper's main empirical claims.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>