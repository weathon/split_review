Here is my final consolidated review:

## Summary

This paper extends the phenomenon of training loss curve (TLC) collapse — where normalized loss curves from different model sizes align onto a single trajectory — from small-scale settings (Qiu et al., 2025) to practical LLM training with AdamW, weight decay, and μP. The authors identify three controls governing collapse: the AdamW timescale τ, the tokens-per-parameter ratio (TPP), and the LR schedule. They show that fixing τ and TPP yields collapse across a 30× parameter range (111M–3.9B). They then demonstrate two applications: using deviation-from-collapse as an early diagnostic for training pathologies, and fitting a parametric surrogate on small-scale runs to enable early stopping in hyperparameter tuning. The paper also introduces the Celerity model family, trained at fixed TPP bands with optimally-chosen τ.

## Strengths

- **Identifies and validates the three controls for TLC collapse at LLM scale.** The paper experimentally demonstrates that τ (jointly determined by η, λ, and B) modulates TLC shape in a predictable way, and that fixing τ and TPP yields collapse across model sizes. Figure 3 convincingly shows that different hyperparameter combinations yielding the same τ produce nearly identical normalized curves. Figure 4 shows collapse across a 30× parameter range (111M to 3.3B) when both τ and TPP are matched. This is a genuine extension of Qiu et al. (2025) to practical LLM settings with AdamW, weight decay, and co-scaling of width/depth/batch size.

- **Demonstrates collapse in a practical LLM family (Celerity) at multiple TPP bands.** The Celerity models at 20 TPP and 80 TPP (Figure 6, left and middle) show tight collapse across 300M–3.9B parameters, confirming that the phenomenon persists at realistic scales and is not a small-scale artifact.

- **Collapse residuals provide a sensitive, quantitative diagnostic for training pathologies.** The 1.8B, 234 TPP run case study (Figure 1 right vs. Figure 6 right) is compelling: deviation-from-collapse pinpointed a numerical issue near 60% of training, whereas the raw loss only showed a visible blip after 90%. This demonstrates practical utility for monitoring large-scale runs where human inspection of raw loss trajectories is unreliable.

- **The early stopping method is well-motivated and shows promising results.** The insight that fixing τ during tuning preserves curve ordering (Figure 7) — enabling early stopping — is practically useful. The parametric surrogate model (Eq. 4–5) fit on 111M-scale runs produces reasonable predictions at 3.3B scale (Figure 8), and the "predicted best" selection outperforms "current best" at 10–30% of training (Figure 9).

## Weaknesses

### Major

- **The "signature of compute-efficient training" framing overreaches.** The paper claims that collapse "emerges as a signature of compute-efficient pre-training" (abstract, line 36). However, collapse is shown at 20 TPP, 80 TPP, *and* 234 TPP — three very different efficiency regimes. 234 TPP is explicitly *not* compute-optimal (it requires 67% more compute for iso-loss, per the paper's own analysis in Figure 5). Collapse occurs whenever τ and TPP are fixed, regardless of whether the TPP is on the Chinchilla frontier. The claim conflates "τ selected optimally for a given TPP" with "compute-efficient training" in the standard scaling-laws sense. This framing appears designed to inflate the contribution and is not supported by the evidence. The core scientific finding (collapse conditions) does not depend on this framing, but the paper would be stronger if the claims were scoped to match the evidence.

- **The Celerity compute-efficiency frontier comparison lacks controlled experiments.** Figure 2 shows Celerity models on the accuracy/compute Pareto frontier, but the comparison has several confounds: (1) different models use different data mixes, and Celerity uses a curated mix (educational, math, code) while many baselines use general web data; (2) some baselines use task-specific annealing or mid-training that Celerity avoids; (3) the "frontier" dashed line in Figure 2 is a power law fit to Celerity points *alone*, not an empirical Pareto envelope — it primarily shows that Celerity models follow a smooth trend, not that they dominate all comparators. Without a controlled experiment (e.g., training the same architecture at TPP=20 with standard τ and comparing loss vs. compute), it is impossible to attribute Celerity's position to the collapse methodology versus data quality or architecture choices.

- **No quantitative collapse metric or variance estimation across seeds.** The paper assesses collapse visually and via residual plots for a single run. There is no formal measure (e.g., maximum normalized deviation, RMSE across scale pairs, inter-run variance as in Qiu et al.). Without this, claims about "tightness" of collapse are subjective, and it is unclear how robust the phenomenon is across random seeds. This makes the contribution harder to verify and compare against future work.

### Minor

- **The early stopping method is validated only on λ sweeps at two scales (1.7B and 3.3B).** The paper claims generality for hyperparameter tuning, but only weight decay (λ) is swept. Learning rate η, batch size B, and schedule shape are not tested. While the paper argues that τ-fixing generalizes (Figure 7), the actual early stopping experiments only demonstrate the method for λ. Additionally, the "current best" baseline (picking the best at the stopping point) is reasonable but the paper would benefit from comparison to more principled alternatives like power-law extrapolation or multi-fidelity optimization methods.

- **The theoretical model (Eq. 3) assumes constant LR, but all experiments use linear decay-to-zero.** The paper acknowledges this gap (lines 134, 138) and argues that LR schedule deformations are scale-invariant under μP, citing Noci et al. (2024). However, this assumption is not empirically validated here — there are no curvature plots or ablations with different schedules. The theory is best understood as a useful intuition rather than a rigorous explanation of the observed behavior.

- **Celerity evaluation metrics are limited to average accuracy on seven commonsense reasoning tasks.** No language modeling perplexity or held-out loss is reported for the Celerity models. Given that the paper's main phenomenon concerns training loss, reporting held-out loss would strengthen the connection between collapse and generalization. The absence of perplexity is particularly noticeable since many works in this area report it.

### Trivial

- None.

## Nice-to-Haves

- A quantitative collapse metric (e.g., maximum pairwise deviation across scales) and 2–3 seeded runs per model size would substantially strengthen the core claim.
- A controlled experiment comparing Celerity with a baseline trained at TPP=20 with matched data and architecture, reporting loss vs. compute, would clarify whether the collapse methodology itself drives efficiency gains.
- Testing the early stopping method on η sweeps or schedule shape would broaden the validation.

## Removed Points

- **Criticism that collapse claims are about different TPP regimes (Harsh Critic Point 1, part about "conflates two distinct phenomena"):** Kept with modified framing. The critic's claim that the paper is "unsubstantiated" is overly strong — the paper does provide evidence that collapse occurs at optimal τ for given TPP. However, the "compute-efficient" framing is indeed overblown. Retained as a major weakness but with modified wording.

- **Criticism about the frontier line being "not an empirical frontier" (Harsh Critic Point 2):** Retained as part of the major weakness, but the claim that the evaluation is "cherry-picked" is removed as speculative. The paper includes all Celerity models in the plot and does not selectively omit unfavorable comparisons.

- **Criticism that "current best" baseline is a "straw man" (Harsh Critic Point 3):** Removed. The paper's description ("Almazrouei et al. (2023) used the best run after warmup") matches the implementation of picking the best at the stop point. This is a reasonable baseline, not a straw man.

- **Criticism about missing related works on multi-fidelity optimization:** Removed per guidelines (do not mention missing related works without external sources to verify).

- **Criticism about "computational cost of fitting the surrogate not reported":** Removed as a nitpick — the paper focuses on method, not cost analysis, and cost information is not standard for this type of contribution.

- **Strength from Strength Finder about Celerity being "compute-efficient":** Weakened. The Celerity models are on the frontier, but the controlled experiment gap weakens this claim significantly.

## Novel Insights

None beyond the paper's own contributions. The calibration anchors did not surface a perspective that meaningfully reframes the paper.

## Suggestions

1. **Reframe the "compute-efficient training" narrative.** Replace the broad claim with a more precise statement: collapse signals that τ is well-tuned for a given TPP, not that the training is on the Chinchilla frontier. This would better align the paper's language with its evidence and eliminate the main source of overclaiming.

2. **Add a quantitative collapse metric.** Report, e.g., the maximum normalized deviation and RMSE across all model-size pairs at each TPP band, including variance estimates across 2–3 seeds. This would solidify the core contribution.

3. **Add a controlled comparison for Celerity.** Train a baseline model with the same architecture and data at TPP=20 with a standard τ (not tuned via collapse principles), and compare training loss vs. compute and downstream accuracy. This would isolate the effect of the collapse-based methodology.

4. **Extend early stopping validation to at least one other hyperparameter** (η or B) at one model scale to demonstrate generality beyond λ sweeps.

## Score and Decision

**Calibration anchors used** (all from human reviews corpus):

| Path | Avg Score | Comparison to this paper |
|------|-----------|------------------------|
| `PvTxIdZc1E.md` (Weight Decay vs µP) | 5.50 | Similar topic (hyperparameter transfer), similar experimental scale. This paper's core finding (collapse conditions) is arguably more novel, but its overclaiming is worse. |
| `T985gm4sDA.md` (Scaling Laws for DiT) | 5.50 | Solid empirical work with clear claims. Our paper has more practical applications but less controlled evaluation. |
| `qBAV2DEvAC.md` (Implicit bias scaling laws) | 5.50 | Good theory-experiment connection. Our paper has stronger practical relevance but weaker theory-experiment link. |
| `NbdCwOgk4m.md` (Trajectory Invariance) | 4.00 | Similar type of contribution (empirical invariance principle) but our paper is much stronger: tested across 30× parameter range vs. single model size. |
| `kFcP5facrQ.md` (Charting the Frontier) | 4.50 | Both have evaluation issues, but our paper's core phenomenon is clearly demonstrated. |
| `FMjeC9Msws.md` (Scaling RL Compute) | 7.50 | Much more extensive study (400K GPU-hours), cleaner claims. Our paper has comparable practical relevance but significantly less experimental rigor. |
| `dnuIoVjeGR.md` (Unified Neural Scaling Laws) | 3.00 | Both propose scaling-related functional forms, but our paper provides users with practical diagnostics and tools rather than just a parametric form. |

The paper's core empirical contribution — demonstrating the conditions for TLC collapse at LLM scale with AdamW and weight decay — is solid and extends prior work in a practically meaningful direction. The monitoring and early stopping applications are genuine use cases. However, the paper's framing inflates the significance of the Celerity model family's position on the compute-efficiency frontier and makes an unsupported equivalence between τ-optimality and compute-efficiency. These issues are addressable but in their current form weaken the manuscript.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept (Poster)</orange>