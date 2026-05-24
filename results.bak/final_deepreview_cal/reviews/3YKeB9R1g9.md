Now I have all the information I need to produce the final consolidated review. Let me synthesize everything.

**Round 1 bracket**: Based on the calibration anchors, I place this paper in the [5.5, 6.5] range. It's clearly above the weak papers (score 2-3) and below the very strong papers (score 8). It's comparable to accepted papers at ~6.0-6.5 like "Scaling Optimal LR Across Token Horizons" and "PolyPythias," and better than rejected papers with weak evidence like "Time Transfer" (5.25). The rejected "Scaling Law with LR Annealing" (6.75) had serious methodological flaws that this paper does not have.

**Round 2 narrowing**: Comparing to the accepted papers at 6.0-6.5:
- "Scaling Optimal LR Across Token Horizons" (6.00, accepted) — similar empirical rigor, similar scope (one central finding + practical implications)
- "PolyPythias" (6.50, accepted) — released resources + analyses, similar contribution level
- "Multi-Power Law" (6.00, accepted) — similar in having an empirical law with practical implications, similar validation concerns

The paper under review is slightly stronger than "Multi-Power Law" because the τ-based analysis provides a principled explanation rather than a purely empirical fit, and the noisy-quadratic model grounds the observations theoretically. It's comparable to "Scaling Optimal LR" which was also a clean empirical study with a clear practical message. I think 6.0 is the right score — not so high that it implies comprehensive validation of all applications, but solid for its well-supported core contribution.

Let me also verify the harsh critic's "missing limitations section" claim by checking the paper once more.

The paper does not have a dedicated limitations section. The harsh critic flags this as a weakness. I'll note it as a minor point.

Now let me produce the final review.## Summary

This paper demonstrates that normalized training loss curves (TLCs) collapse across LLM model sizes (300M–3.9B parameters) when three controls are matched: the AdamW timescale τ, tokens-per-parameter ratio (TPP), and learning-rate schedule. It shows that τ modulates TLC shape via a bias–variance trade-off, provides a noisy-quadratic model formalizing this, and identifies TPP as a second scale-invariant control. The paper introduces the Celerity model family, trained in a fixed-TPP/τ regime where collapse occurs and Celerity sits on the compute-efficiency frontier. Two applications are proposed: (1) using deviation-from-collapse as a training-monitoring diagnostic, and (2) early stopping in hyperparameter tuning via a surrogate model fit on small-scale runs.

## Strengths

- **Extends collapse from small-scale µP experiments to practical LLM training.** Prior work (Qiu et al., 2025) demonstrated TLC collapse only for small models with vanilla Adam and no weight decay. This paper shows the phenomenon persists with AdamW, weight decay, and co-scaled width/depth/batch size at scales up to 3.9B parameters (Figure 1 middle, Figure 6). This is a non-trivial extension that addresses an explicit call from the prior work.

- **Identifies and explains the three controls governing collapse.** Section 3 systematically isolates τ (via sweeps of η, λ, and B in Figure 3) and TPP (Figure 4) as the determinants of normalized TLC shape, with the LR schedule phasing early bias vs. late variance. The noisy-quadratic model (Appendix B.3, Eq. 3) provides a principled theoretical grounding for why τ controls the bias–variance trade-off, going beyond purely empirical curve-fitting.

- **Celerity is a concrete, competitive model family trained in the collapse regime.** Celerity models sit on the accuracy-vs-compute Pareto frontier (Figure 2) and are released as open resources, providing a reproducible benchmark for future work on collapse-aware training. The compute-vs-compression trade-off analysis (Figure 5, Appendix C.1) motivating the 234 TPP choice is clearly reasoned.

## Weaknesses

### Major
None.

### Minor

- **The monitoring application is demonstrated on a single case.** The paper shows one compelling example (1.8B 234 TPP run with numerical instability, Figure 1 right) where collapse residuals flagged divergence near 60% while raw loss only showed a blip near 90%. This is a convincing illustration, but the claim in the abstract that "deviation-from-collapse provides a sensitive, early diagnostic of training pathologies" overstates what a single anecdote supports. The monitoring method is not systematically evaluated on additional runs (e.g., simulated issues, different seeds, other natural failure modes). This is an evidential gap in a claimed contribution, though it does not undermine the paper's core finding about collapse itself.

- **Early-stopping validation is limited to λ sweeps at two model sizes.** The early-stopping procedure (Section 5, Figure 9) is tested only on weight-decay tuning for 1.7B/20TPP and 3.3B/30TPP models. It is not demonstrated for other hyperparameters (η, B) or other TPP regimes. The surrogate model (Eq. 4-5) is designed to handle τ and TPP variation, but the experimental validation of early stopping only covers λ sweeps. The paper acknowledges this scope indirectly ("Further experiments are in Appendix D.2") but does not hedge the claims enough.

- **No quantitative collapse metric.** The paper evaluates collapse visually through normalized curve overlays and residual plots. It does not report a formal quantitative measure of collapse quality (e.g., average absolute residual, RMSE across models, maximum deviation compared to inter-run noise). This makes it hard to compare collapse tightness across TPP bands or to set objective alarm thresholds for the monitoring application. Since collapse is the central phenomenon, a simple quantitative metric would strengthen the paper.

- **The surrogate model fit (Eq. 4-5) is empirically motivated but somewhat ad-hoc.** The functional form combines a power-law term and a schedule-modulation term with several free parameters. The alternating fit procedure (b then q, iteratively) is described as reducing the grid-search cost, but the robustness of the resulting fits to different data subsets or initialization is not explored. Appendix Table 11 reports MAE but without uncertainty or per-curve breakdown.

- **No explicit limitations section.** Given the scope of the claims (monitoring at scale, early stopping across HPs), a brief discussion of when collapse might break (e.g., with different architectures, non-µP training, extreme TPP where data distribution shifts) would strengthen the paper.

### Trivial
- Hyperparameter details: The paper states τ = 0.05 for the 234 TPP Celerity models and reports batch sizes and peak LR, but does not explicitly list the individual η and λ values used per model size. These could be verified from the provided τ, B, D values, but reporting them explicitly would aid quick reproducibility.

## Nice-to-Haves

- Extend the monitoring validation with at least one additional case (e.g., a run with a known data ordering issue or a simulated gradient corruption) to transform it from an illustration into a reproducible methodology.
- Add a quantitative collapse metric such as the average absolute residual over ˆt ∈ [0.2, 1] across models in a TPP band.
- Test the early-stopping procedure on at least one η or B sweep to demonstrate generality beyond λ tuning.
- Include error bands on the fitted power law in Figure 2 to convey uncertainty.

## Removed Points

- *Criticism about the residual bias assumption not being verified empirically (Section 3 "Scale invariance"):* REMOVED. The paper explicitly states this as an assumption and the empirical collapse results indirectly support it. The authors do not claim to have verified it. This is a standard modeling assumption, not a weakness.
- *Criticism about "fair comparison" with baselines favoring the author's method:* REMOVED. The asymmetry favors baselines (not the author's method), so this rule excludes it.
- *Criticism about statistical significance for Figure 2 (no error bands):* DEMOTED to Nice-to-Have. Error bands are not standard for this type of frontier plot in the scaling laws literature, and the scatter is readable without them.
- *Strength Finder claim that the paper "provides a principled explanation for when collapse occurs and why it fails in families like Llama-2":* WEAKENED. While the paper does explain why Llama-2 fails to collapse (varying TPP and τ across models), this explanation is straightforward given the identified controls. The strength is real but modest.
- *Strength Finder claim about "earlier detection than raw loss":* KEPT but contextualized. The single-case demonstration supports this claim for that specific case but does not establish it as a general property.

## Novel Insights

The paper's key novel insight is that the AdamW timescale τ = B/(ηλD) is the unifying control behind TLC shape variation: sweeps of η, λ, or B produce matching curves when τ is matched (Figure 3). This reframes weight-decay tuning as timescale tuning and explains why collapse emerges in compute-efficient regimes (where τ is set optimally for the TPP) and why it fails in families like Llama-2 (where TPP and τ co-vary across sizes). This is the paper's most interesting finding and extends beyond what prior descriptive work provided.

## Suggestions

1. Add a limitations paragraph discussing the conditions under which collapse might break (e.g., different architectures, non-µP parameterizations, extremely high TPP).
2. Convert the monitoring illustration into a validated method by testing on at least one additional run with a known or simulated issue.
3. Report a simple quantitative collapse metric (e.g., mean absolute residual across models per TPP band) to replace purely visual evaluation.
4. List the individual η and λ values per Celerity model size in the appendix for completeness.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| BUpdp5gETF (Different Rates for Different Weights) | 2.50 | R1 | Much lower quality; this paper is far stronger |
| f7aWmxgSN4 (Generalization from Starvation) | 3.00 | R1 | Much lower quality |
| lZRRfupxYn (Mesoscience for generalizability) | 3.00 | R1 | Much lower quality |
| o9YC0B6P2m (Scaling Law with LR Annealing) | 6.75 | R1 | Similar empirical approach but that paper had methodological flaws not present here; this paper is comparable or slightly better |
| KnoS9XxIlK (Multi-Power Law) | 6.00 | R1, R2 | Comparable in scope and validation; both propose empirical laws with practical applications and have similar levels of validation rigor |
| WYL4eFLcxG (Scaling Optimal LR) | 6.00 | R1, R2 | Comparable; both are clean empirical studies with one central finding and practical guidance |
| xGM5shdGJD (Hitchhiker's Guide) | 5.20 | R1 | Lower; primarily methodological advice rather than novel finding |
| d8w0pmvXbZ (Small-scale Proxies) | 8.00 | R1 | Stronger; more thorough validation and clearer practical recommendations |
| MLhquJb1qN (Time Transfer) | 5.25 | R2 | Weaker; empirical evidence insufficiently supported claimed scaling laws |
| bmrYu2Ekdz (PolyPythias) | 6.50 | R2 | Comparable; both release resources and conduct thorough analyses of training dynamics |
| P7KRIiLM8T (u-µP) | 7.33 | R2 | Stronger; more principled theoretical contribution validated across scales |
| 5HCnKDeTws (When Scaling Meets Finetuning) | 6.75 | R2 | Comparable quality, different topic |

**Round 1 bracket:** [5.5, 6.5]

**Round 2 narrowing:** After reading anchors at 6.00 (Multi-Power Law, Scaling Optimal LR) and 6.50 (PolyPythias), this paper is comparable to the accepted papers at the 6.0 level but does not reach the thoroughness of the 6.5-7.5 papers like u-µP (7.33) or Small-scale Proxies (8.00). The core finding is well-supported and the noisy-quadratic derivation provides a stronger theoretical basis than purely empirical fits, but the applications are validated too narrowly to push the score higher.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>