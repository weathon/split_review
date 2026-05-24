## Summary

This paper demonstrates that training loss curves (TLCs) from different model sizes *collapse* onto a single normalized trajectory in large-scale LLM training, extending a phenomenon previously observed only in small μP experiments. The authors identify AdamW timescale τ, tokens-per-parameter ratio (TPP), and LR schedule as the three controls that must be matched across scales for collapse to occur. They instantiate this in the *Celerity* model family (300M–3.9B), which sits on the compute-accuracy Pareto frontier, and show two practical applications: collapse residuals as an early diagnostic of training pathologies, and a surrogate-based method enabling early stopping in hyperparameter tuning after 10–30% of training.

## Strengths

- **Empirical demonstration that τ modulates TLC shape (Fig. 3):** Sweeping η, λ, and B independently for 610M models at 80 TPP shows that normalized TLCs align whenever τ is matched. This provides controlled evidence that τ is a governing variable of curve shape, not an artifact of a single hyperparameter.

- **Scale-invariant collapse at fixed TPP and τ across a 30× parameter range (Fig. 4, right):** Models from 111M to 3.3B at TPP=20 with approximately constant τ produce normalized curves that collapse onto a single trajectory, confirming the phenomenon holds under practical width-and-depth scaling, not just width-only as in prior μP work.

- **Celerity models achieve the compute–accuracy Pareto frontier (Fig. 2):** Celerity-3.9B, 1.8B, and 900M occupy the upper-left frontier among open models on seven downstream benchmarks, tying collapse directly to compute-efficient pre-training.

- **Collapse residuals detect training issues earlier than raw loss (Fig. 1, right):** The deviation of the initial 1.8B run from the 500M reference becomes visible near 60% of training, whereas the unnormalized loss in Fig. 6 (right) does not show a clear upward trend until after 90%. This early-warning capability is a direct consequence of having a collapsed reference curve.

- **Theoretical grounding of τ's role via a noisy quadratic model (Eq. 3):** The derivation shows how τ controls the bias–variance trade-off: smaller τ yields faster initial decay but a higher variance floor ∝ 1/τ, matching the observed "fast-then-flatten" behavior. After normalization, the curvature factor cancels, explaining why normalized TLCs become scale-invariant at matched τ.

- **Addresses an explicit gap left by Qiu et al. (2025):** The prior work validated collapse only on small autoregressive tasks with vanilla Adam and no weight decay. This paper tests collapse under practical scaling ladders that co-scale width, depth, batch size, and weight decay — a substantive step toward real-world applicability.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Collapse is demonstrated only visually, without a quantitative tightness metric.** Figures 1, 4, and 6 are the primary evidence that normalized curves collapse, but no numerical measure (e.g., maximum pairwise deviation between curves, or the standard deviation across curves at each ˆt) is reported. This matters because the applications (diagnostics via residuals, early stopping via alignment) rely on the curves following the *same* trajectory to high precision. A quantitative metric would allow assessing whether collapse is tight enough for these purposes across different TPP bands and comparing collapse quality across settings. *The paper does provide MAE for the surrogate model in Section 5, but this evaluates prediction accuracy, not the tightness of empirical collapse itself.*

2. **Early stopping validation is limited to λ sweeps at two model sizes.** The central experiment (Fig. 9) tests only λ sweeps at 1.7B/20 TPP and 3.3B/30 TPP. The paper shows that the surrogate model accurately predicts normalized TLCs (Fig. 8, Table 12 in appendix), and Fig. 7 demonstrates that fixing τ preserves curve ordering in batch-size sweeps. However, the actual early stopping procedure (Steps 1–6 in Section 5) is validated only on λ. Sweeps over learning rate, batch size, or other hyperparameters at different TPP bands are not tested. The claim that collapse "enables early stopping in large-scale hyperparameter tuning" is broader than the evidence directly supports.

3. **The phrasing "collapse emerges as a signature of compute-efficient training" is slightly imprecise.** The paper shows that collapse occurs when τ is matched across scales, and that optimal τ depends only on TPP (Bergsma et al., 2025a). However, two families with the same τ and TPP would collapse regardless of whether τ is optimal. Collapse is therefore a signature of *consistent controls*, with a *correlation* to compute-efficient training (because compute-efficient training uses optimal τ, which is consistent across scales at fixed TPP). The paper's own framing in Section 3 ("Key takeaway 1") correctly identifies the three controls, so this is a presentational imprecision rather than a substantive error.

4. **No ablation comparing normalization strategies.** Section 4 mentions two strategies for normalizing when L(T) is unknown ("estimate" vs. "early-align") and states that "early-align" is used in experiments. No comparison of how the diagnostic or early-stopping results depend on this choice is provided. Since the applications hinge on accurate normalization, understanding the sensitivity to this choice would strengthen the paper.

5. **The surrogate model's alternating fitting procedure is not analyzed for robustness.** The fitting alternates between optimizing (b_const, b_exp) and (q_const, q_exp) to reduce grid-search cost (Eq. 5). The paper states this "yields stable fits" but does not show convergence behavior, sensitivity to initialization, or parameter stability under re-sampling. This is a minor concern given that the predictions match well empirically (Fig. 8), but a brief analysis would improve confidence.

### Trivial
None.

## Nice-to-Haves

- **Additional diagnostic examples:** The 1.8B numerics issue (Fig. 1, right) is a compelling anecdote but stands alone. One or two more examples from different sizes or failure modes would demonstrate that the method is not tuned to one incident.
- **Systematic investigation of when collapse breaks down:** The 234 TPP band shows late-training divergence on training loss (attributed to training data overfitting). A broader study of when and why collapse degrades (e.g., under different data regimes, multiple epochs, or schedule variants) would clarify the method's limits.
- **Validation on at least one more hyperparameter axis for early stopping:** A batch-size sweep under fixed τ (where Fig. 7 already shows ordering is preserved) or an LR sweep would significantly strengthen the early stopping claims without requiring new methodology.

## Removed Points
- **Reference to De Vries (2023) as a blog post:** Removed per hard rules — the paper cites this reference; questioning its type is not admissible.
- **"More diagnostic examples needed"** moved to Nice-to-Haves above.
- **"Discussion of when collapse fails"** moved to Nice-to-Haves above.
- **"Comparison between 'current best' and 'predicted best' is a strawman"** — The harsh critic claimed "any practitioner would know picking best loss at 10% is unreliable." However, the paper cites Almazrouei et al. (2023) showing this exact practice is used in production (Falcon). The baseline is taken from real practice, not a strawman.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") removed per filtering instructions.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. Add a quantitative collapse metric (e.g., mean pairwise ℓ₂ distance between normalized curves over ˆt ∈ [0.1, 1]) and report it for each TPP band. This would immediately substantiate the "collapse" visual claim and enable readers to compare collapse quality across settings.
2. Validate the early stopping procedure on at least one additional hyperparameter axis — a batch-size sweep with fixed τ would directly connect to Fig. 7 and is the most natural extension.
3. Provide a brief ablation comparing "estimate" vs. "early-align" normalization strategies for at least one diagnostic or early-stopping scenario.
4. Add a sentence clarifying the relationship between collapse and compute efficiency: collapse follows from matched τ and TPP, and optimal training happens to produce matched τ — collapse and efficiency are correlated, not causally linked.

## Score and Decision

**Round 1 bracket:** The paper clearly sits above the weak-anchor band (avg 2.5–3.0) and below the very-strong band (avg 7.33–8.0). Initial bracket: **5.5–7.5**.

**Round 2 narrowing:** Compared to mid-to-high anchors:
- *A Multi-Power Law for Loss Curve Prediction* (6.00, Accept): tested only 25M–400M models, no theoretical grounding, narrower validation. Our paper is stronger in scale, theory, and practical demonstration.
- *Scaling Optimal LR Across Token Horizons* (6.00, Accept): solid empirical work on LR transfer, criticized for arbitrary functional forms. Our paper is comparable or slightly stronger.
- *How Does Critical Batch Size Scale in Pre-Training?* (6.80, Accept): well-executed mix of theory and experiments, but criticized for disabling weight decay and limited scale. Our paper is at a comparable quality level.
- *Scaling Law with Learning Rate Annealing* (6.75, Reject): had fundamental formulation flaws (zero-LR invariance). Our paper has no such flaw.

**Final score: 6.5.** This paper makes a clear and useful contribution — extending TLC collapse to practical LLM training, identifying τ and TPP as key controls, and demonstrating two concrete applications with a trained model family. The evidence is solid but not exhaustive: the core collapse claim rests on visual evidence without a quantitative metric, and the early stopping application is validated on a narrow set of conditions. These are addressable limitations that do not undermine the paper's central findings but place it below the 7+ tier where the evidence would need to be more complete.

### Anchors consulted

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| f7aWmxgSN4 | 3.00 | R1 | Much weaker — unrelated universality claim, same score by all reviewers |
| BUpdp5gETF | 2.50 | R1 | Much weaker — narrow method paper |
| q541p2YLt2 | 2.50 | R1 | Much weaker — attention stability |
| lZRRfupxYn | 3.00 | R1 | Much weaker — mesoscience application to ML, unrelated topic |
| o9YC0B6P2m | 6.75 | R1,R2 | Comparable avg score but had fundamental formulaic flaws leading to rejection. Our paper is more solid |
| KnoS9XxIlK | 6.00 | R1,R2 | Similar topic, weaker empirical scale (25M–400M vs 300M–3.9B), no theory. Our paper is stronger |
| WYL4eFLcxG | 6.00 | R1 | Similar quality, well-executed LR scaling law. Comparable |
| xGM5shdGJD | 5.20 | R1,R2 | Methodology paper on scaling law estimation, weaker contribution |
| mao3y822aM | 5.50 | R2 | Narrower in scope, weaker empirical results |
| zpBamnxyPm | 5.75 | R2 | About predicting downstream capabilities, not directly comparable |
| P7KRIiLM8T | 7.33 | R2,R3 | Stronger — theory-heavy μP extension with unit scaling. Our paper is more applied |
| 5HCnKDeTws | 6.75 | R2 | Finetuning scaling, different focus, comparable quality |
| JCiF03qnmi | 6.80 | R2,R3 | Comparable — solid mix of theory and experiments on CBS. Accepted despite weaknesses (no WD, limited scale) |
| g8sGBSQjYk | 7.33 | R3 | Stronger — second-order optimization theory |
| KZJehvRKGD | 7.50 | R3 | Stronger — depthwise hyperparameter transfer with tight theory |
| g6syfIrVuS | 7.00 | R3 | Stronger — local learning theory with μP |

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>