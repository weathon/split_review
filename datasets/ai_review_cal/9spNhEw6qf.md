- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3
Here is the consolidated review.

---

## Summary

This paper investigates whether knowledge distillation (KD) from a grokked teacher can enable grokking below the critical data regime — the data threshold below which standard training fails to generalize. Using 1-layer Transformers on modular arithmetic tasks (addition, subtraction), the authors show that (a) KD from a teacher grokked on one prime modulus P₁ enables a student to grok on a different P₂ even at 20% data, where standard training yields chance-level accuracy; (b) distilling from multiple small grokked models lets a larger model generalize across joint distributions when any sub-distribution is data-poor; and (c) KD mitigates catastrophic forgetting during continual pretraining from one distribution to another. The paper also presents weight-norm and optimizer comparisons intended to challenge prior claims about weight decay and decreasing weight norms being necessary for grokking.

## Strengths

- **KD enables grokking below the critical data threshold (Fig. 4).** At 20% training data, standard training (both Adam and AdamW) produces no generalization within 30K iterations. Under KD from a grokked teacher on a different prime, the student achieves perfect generalization — with or without weight decay. This is the paper's clearest and most original empirical contribution, directly supporting the claim that a grokked teacher can unlock generalization in data regimes where standard training fails entirely.

- **Transfer of grokking across distinct modular arithmetic distributions (Fig. 2b).** A teacher grokked on prime P₁ enables a student trained from scratch on a different prime P₂ to grok, using only 30% of the P₂ data. The student groks under both Adam and AdamW, while the non-KD baseline at 30% with Adam fails within the same iteration budget. This demonstrates practical reuse of grokked representations under distribution shift.

- **Multi-distillation scales to joint distributions (Figs. 5 & 6).** A larger model tasked with learning both P₁ and P₂ fails under joint cross-entropy training when either sub-distribution falls below the critical threshold, but succeeds when trained solely via KD from the two small grokked models. This extends the utility of the approach to multi-distribution scenarios with heterogeneous data availability.

- **KD mitigates catastrophic forgetting in continual pretraining (Fig. 7).** When a grokked model on P₁ is continually pretrained on P₂, KD preserves near-perfect accuracy on P₁ while maintaining rapid generalization on P₂, in contrast to rapid forgetting without KD. This is a practically useful demonstration.

## Weaknesses

### Fatal

None.

### Major

- **The paper's claim to "refute" prior theories about weight decay and decreasing weight norms as drivers of grokking is over-extended.** The weight-norm and weight-decay experiments (Figs. 2b, 3, 4b) are conducted **under KD**, not standard training. Prior works (Nanda et al., 2023; Liu et al., 2022b; Varma et al., 2023) analyzed the dynamics of standard (non-KD) training, where weight decay plays a mechanistic role in a "cleanup" phase. The paper's own Figure 2a shows that under **standard training without KD**, Adam (no weight decay) does **not** grok within 30K iterations — consistent with the prior work. The paper shows that KD *circumvents* the weight-decay dependency, which is an interesting finding, but the claim of "refuting" the mechanistic explanations of standard-training grokking conflates two different training regimes. The conclusion (Section 6) reiterates "refuting" without this caveat. The paper should clarify that its results challenge the *necessity* of weight decay for grokking *in general* (by showing an alternative path), not that the prior mechanistic accounts of standard training are incorrect.

- **No multiple runs or variance reporting.** All experiments appear to be single-seed runs. The paper reports no error bars, confidence intervals, or seed-averaged learning curves. This is a serious omission for an empirical paper: the reader cannot assess whether the reported grokking curves, especially the "short of unity" case in Fig. 5b at 10% data, are reproducible or reflect a single favorable initialization. The paper should report at least 3–5 seeds with shaded variance bands.

- **Missing baseline: KD from a non-grokked teacher.** To isolate whether the *grokking* property of the teacher (structured internal representations, Fourier circuits, etc.) is what enables the student's success, a control experiment with KD from a non-grokked teacher (e.g., one trained on the same P₁ data but stopped before grokking, or one trained on a different random sample) is essential. Without this, the advantage could simply come from any well-trained teacher's soft labels, not from the grokking phenomenon specifically.

- **Missing baseline: comparison to other low-data regularization techniques.** The paper shows KD enables grokking where standard training fails at 20% data, but does not compare with other methods that improve generalization in low-data settings (e.g., label smoothing, data augmentation, stronger weight decay scheduling, or a larger model trained from scratch with more iterations). Such comparisons would help attribute the effect to KD's specific properties rather than to generic regularization benefits.

### Minor

- **Architecture details are underspecified.** The paper says "1 layer Transformer" but does not report the number of attention heads, embedding dimension, feed-forward dimension, activation function, or number of parameters. This hinders reproducibility. (The paper has no appendix section.)

- **Specific primes P₁ and P₂ are not reported.** The paper states "results are consistent regardless of the choice of P₁ and P₂" but never states which primes were actually used. For reproducibility and for readers to assess the absolute number of training examples (e.g., for a given P, how many unique pairs constitute 20%?), the actual primes should be reported.

- **The practical-relevance framing is inflated relative to the experiments.** The abstract and introduction claim relevance to "continual learning, multi-task learning, domain generalization" and "efficient model training in dynamic and data-limited scenarios," but all experiments are on synthetic modular arithmetic with a single synthetic distribution shift (changing P). While this is a legitimate starting point, the framing oversells the generality.

- **At 30% data, the advantage of KD is primarily speed, not enabling generalization per se (for AdamW).** Figure 2a shows that AdamW (with weight decay) already produces grokking at 30% without KD; KD at 30% mainly accelerates it. The paper's strongest case is at 20% (Fig. 4), and this should be foregrounded more clearly. (Note: for Adam at 30%, KD does enable grokking where standard training fails, so the criticism applies only to the AdamW case.)

### Trivial

None.

## Nice-to-Haves

- Extending training to 100K+ iterations for the 20% non-KD baseline to definitively rule out that grokking would eventually emerge without KD given more steps.
- Reporting the temperature parameter *t* and the mixing coefficient *α* used in the KD loss, and whether these were tuned.

## Removed Points

The following points from the inputs were removed with justifications:

1. **"The paper does not report the actual number of training examples (e.g., for a given P, how many unique pairs are there?)"** — Moved to Minor rather than the severity implied by the harsh critic. The paper correctly cites Varma et al. for the definition of critical data size, and 20%/10% fractions on modular arithmetic are standard in the grokking literature. Reporting the absolute counts is a helpful specificity but not a structural weakness.

2. **Criticism about "the figures are not visible (likely PDF artifacts)"** — Removed as a parser artifact; the paper as submitted would have figures.

3. **"The axes are not visible" / "the axes are not visible" (Fig. 7)** — Removed as a parser artifact.

4. **Criticism about "no comparison with a single large teacher (instead of two small ones)" for multi-distillation** — Moved to Nice-to-Haves. The multi-distillation experiment already has a clear design (two task-specific small teachers vs. joint cross-entropy training). Adding a single-large-teacher baseline would be an additional control but is not critical for the main claim.

5. **Strength Finder's generic strengths** — Removed generic/superficial strengths such as "the paper investigates an important problem." Kept only concretely evidenced strengths.

6. **"The paper does not investigate the trade-off: is retained accuracy on p1 at the cost of slower learning on p2?"** — Removed. The paper does report both previous-task and current-task accuracy curves (Fig. 7a and 7b), and the caption states the KD case achieves rapid generalization on P₂ while retaining P₁ accuracy. The reported data addresses this question.

## Novel Insights

None beyond the paper's own contributions. Both reviewers largely rephrased the paper's results or raised standard empirical-rigor concerns; neither identified a pattern or implication not already present in the paper.

## Suggestions

1. **Reframe the theoretical claims.** Replace "refute" with "challenge" or "provide counterexamples to the necessity of" when discussing prior weight-decay theories, and explicitly state that the counterexamples occur under KD rather than standard training. This would not weaken the paper — it would make the claims more defensible.

2. **Add multiple seeds.** Even 3–5 seeds with shaded min/max bands on the learning curves would substantially increase confidence in the results, especially for the 10% data fraction case where generalization "falls short of unity."

3. **Add a non-grokked teacher baseline.** Train a teacher on P₁ to the same loss but stop before grokking (or train on a random subset), then distill from it. If KD from a non-grokked teacher fails while KD from a grokked teacher succeeds, the paper's causal story is much stronger.

4. **Report all key architecture and training hyperparameters** (embedding dimension, number of heads, activation, temperature, α, exact primes used) either in a short table or by adding a brief "Implementation Details" subsection.

5. **Tone down the practical-relevance framing** to match the experimental scope (modular arithmetic with synthetic distribution shifts). Claiming relevance to "continual learning" is fine; claiming the paper provides "a framework for efficient model training in dynamic and data-limited scenarios" oversells.
