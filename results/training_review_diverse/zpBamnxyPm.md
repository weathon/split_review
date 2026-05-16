Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper identifies and demonstrates a previously underexplored factor that makes modeling scaling behavior on multiple-choice benchmarks difficult: the sequence of transformations from log-likelihoods to common downstream metrics (accuracy, Brier score, choices-normalized probability) progressively degrades the per-sample correlation between scores and pretraining compute. The mechanism is that these metrics depend not only on probability mass on the correct answer but also on fluctuations of probability mass on *specific* incorrect choices. The authors provide systematic evidence across 5 model families and 12 benchmarks showing that the ordering of score-compute correlations is consistent: \(\log p_{\theta}^{\text{Vocab}}\)(correct) > \(p_{\theta}^{\text{Vocab}}\)(correct) > \(p_{\theta}^{\text{Choices}}\)(correct) / Brier Score > Accuracy.

## Strengths

1. **Novel factor identification with clear mechanism.** The paper isolates a concrete, previously unarticulated reason why downstream metrics are harder to predict than pretraining loss: downstream accuracy/Brier score require modeling probability mass on *specific* incorrect choices, not just the correct one. The scatter plots in Figure 5 convincingly show that knowing \(p_{\theta}^{\text{Vocab}}\)(correct) tells you almost nothing about \(p_{\theta}^{\text{Choices}}\)(correct) or accuracy, precisely because the denominator (sum over specific incorrect choices) is underdetermined. This is a genuine insight beyond prior work on emergence artifacts (Schaeffer et al., Hu et al.).

2. **Systematic, large-scale empirical evidence.** The analysis covers four dense model families (Pythia, Cerebras-GPT, OLMo, LLM360) plus INCITE, evaluated on 12 multiple-choice benchmarks (ARC, HellaSwag, MMLU, etc.) using three correlation metrics (Spearman, Pearson, Kendall) and four distribution statistics (mean, median, AUC, negative Wasserstein distance). Figures 3 and 4 show that the degradation ordering holds across nearly all benchmark-family combinations, demonstrating generalizability rather than being a quirk of one setup.

3. **Actionable takeaways grounded in analysis.** The recommendations (e.g., practitioners should consider using \(p_{\theta}^{\text{Vocab}}\)(correct) for scaling-predictable signals; continuous metrics do not guarantee predictability if they compare against specific incorrect choices) follow directly from the mechanism demonstrated, rather than being generic advice. Takeaway #2 — that even "continuous" metrics like \(p_{\theta}^{\text{Choices}}\)(correct) can be unpredictable — is a counterintuitive and useful contribution.

4. **Clean exposition of the transformation chain.** Figure 1's schematic and the formalization of the transformation steps (Eqns. 1–5) provide a clear, reusable framework that future work can build on when analyzing evaluation metrics.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between per-sample evidence and claims about aggregate predictability.** The paper's title, abstract, and framing ("predicting downstream capabilities") naturally read as addressing *aggregate* benchmark scores — the quantity the community cares about when fitting scaling laws. However, all empirical evidence operates at the *per-sample* level. The paper explicitly states "All the scores we discuss are per-datum" (line 92), which is transparent, but it never demonstrates that the per-sample degradation translates to aggregate unpredictability. In fact, if per-sample noise averages out, mean accuracy could still follow a smooth scaling trend. The paper argues (line 193) that predictions "must" be made per-sample because averages are insufficient, but this conflates *knowing the average mass on incorrect choices* (which is indeed insufficient per-sample) with the claim that *mean accuracy is hard to predict as a function of compute*. These are different statements, and the paper provides no aggregate-level evidence (e.g., scaling-law fits for mean accuracy vs. mean log-likelihood). This mismatch between the level of the claim and the level of the evidence weakens the paper's headline conclusion.

2. **No scaling-law fitting or extrapolation evaluation.** The paper uses "predictability" to mean "high per-sample rank correlation with compute." This is a defensible operationalization, but it is distinct from how the scaling-law literature evaluates predictability (curve fitting to aggregate metrics + held-out extrapolation error). Without demonstrating that aggregate accuracy is actually harder to fit or extrapolate than aggregate log-likelihood — and that the gap is attributable to the mechanism identified — the paper's claim that it *explains* the elusiveness of downstream prediction remains plausible but unsubstantiated at the aggregate level. The paper acknowledges this limitation (Direction 2: "do not employ backtesting"), but the acknowledgment appears in a future-work paragraph while the stronger framing persists in the title, abstract, and takeaways.

### Minor

1. **Uncertainty about whether the "might be possible" claim in Section 5 is warranted.** The scatter plots in Figure 6 show a large spread (orders of magnitude variance) between correct-choice mass and incorrect-choice mass. The paper says this suggests "fitting per-sample scaling trends for each incorrect choice might be possible" but immediately acknowledges "whether... trends can be fit and accurately extrapolated is unclear." This is appropriately cautious, but it leaves Section 5 feeling inconclusive — it documents the difficulty without demonstrating progress toward a solution.

2. **The number of choices as an unexamined modulating factor.** The degradation mechanism depends on the denominator size (number of available choices). Benchmarks with more choices (e.g., MMLU's 4-choice format vs. ARC's 4-choice format vs. others) could be differentially affected. The paper does not analyze whether the degradation severity varies with choice count, which would strengthen the mechanistic account.

3. **INCITE outlier is discussed but not analyzed.** The paper notes INCITE is an outlier due to possible benchmark contamination but still includes it in aggregate results (Figures 3, 4). Some discussion of how contamination might interact with the identified mechanism would be helpful.

### Trivial
None.

## Nice-to-Haves

- **Aggregate scaling-law fits** comparing mean log-likelihood, mean \(p_{\theta}^{\text{Vocab}}\)(correct), mean accuracy, and mean Brier Score, with goodness-of-fit or held-out prediction error metrics, would directly connect the per-sample mechanism to the aggregate-level claim. This is the single most impactful addition the paper could make.
- **Analysis by number of choices** (2-choice vs. 4-choice vs. N-choice benchmarks) to test whether the degradation magnitude scales with denominator size.
- **Sample-difficulty stratification** to see whether the degradation is concentrated on hard samples (where incorrect-choice mass fluctuates more) or is uniform.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Claim–evidence mismatch" framed as a structural/fatal flaw.** The harsh critic presents this as invalidating the paper's conclusion. However, the paper is explicit about its per-sample scope ("All the scores we discuss are per-datum") and frames its contribution as identifying *a factor*, not as definitively proving that aggregate metrics are impossible to predict. The criticism is valid as a gap but overstated in severity — this is a major weakness, not a fatal one. Moved to Major.
- **Criticism about no scaling-law fitting.** This evaluates the paper against the wrong class of expectations. The paper is an empirical diagnostic analysis, not a scaling-law modeling paper. Demanding that it fit power laws and evaluate extrapolation error is scope creep. The paper identifies a factor and demonstrates a mechanism; fitting scaling laws would strengthen but is not required for the core contribution. Moved to Major (weakness #2) with appropriate framing, and also mentioned as a Nice-to-Have.
- **"Insufficient connection between per-sample degradation and aggregate unpredictability" framed as structural.** The paper partially addresses this (line 193's argument about per-sample necessity) even if imperfectly. The connection is weaker than ideal but not absent. Moved to Major weakness #1, with the valid core retained.
- **The critic's claim that per-sample correlation degradation "does not address aggregate predictability"** is too strong. If individual samples' scores are less correlated with compute, the average of those scores is also affected — the paper's mechanism is relevant to aggregate unpredictability even if the direct link is not fully established. This overstatement is removed; the valid core (lack of aggregate-level evidence) is kept.
- **Strength Finder's generic phrasing about "grounded in standard tools"** — kept as it specifically mentions LM Eval Harness and 6ND FLOP approximation, which is concrete enough.

## Novel Insights

Beyond the paper's own contributions, the reviews surface an insightful framing tension: the paper would benefit from either (a) adding aggregate scaling-law analysis to match its broad claims, or (b) tightening its title and claims to match its per-sample evidence (e.g., "Why Per-Sample Multiple-Choice Performance Can Be Unpredictable with Scale"). The choice between these paths reflects a genuine strategic question about what kind of contribution the authors intend — a diagnostic insight versus a demonstrated prediction framework. The paper's mechanism is strong enough to support either framing, but the current version sits uncomfortably between them.

## Suggestions

1. **Add one aggregate figure** showing mean accuracy vs. compute alongside mean log-likelihood vs. compute for 2–3 representative benchmarks, with simple curve fits (polynomial or power-law) and prediction intervals. This would directly address the central concern without requiring a full scaling-law study.
2. **Tighten the claims in the title and abstract** to match the per-sample level of evidence, or add the aggregate analysis. The current framing overreaches relative to what is demonstrated.
3. **Analyze degradation as a function of the number of choices** — this is a cheap experiment (the data already exist) that would deepen the mechanistic story.
4. **Reframe Section 5's "might be possible" language** to be more clearly speculative, or remove it and focus on the diagnostic contribution, which is already sufficient.

## Score and Decision

The paper makes a genuine contribution: it identifies a novel factor (the transformation chain via dependency on specific incorrect choices) and demonstrates it systematically across diverse models and benchmarks. The mechanism is clearly illustrated and non-obvious. The primary weakness is a gap between the per-sample evidence and the paper's broader framing about "predicting downstream capabilities." This is a significant but addressable gap — it weakens the paper's headline claim without undermining the core empirical contribution. The paper does not have fatal flaws.

**Originality**: High — the specific factor and mechanism are novel.  
**Importance of question**: High — understanding why downstream scaling is harder than pretraining scaling is an active, important area.  
**Claims supported**: Partially — the per-sample mechanism is well-supported; the aggregate-level implications are not.  
**Soundness**: Good for what is tested; the missing aggregate analysis limits completeness.  
**Clarity**: Good, with clear figures and exposition.  
**Value to community**: Moderate to high — the diagnostic framework and recommendations are practically useful.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>