Now I have a clear picture from the anchors. Let me write the final review.

## Summary of Calibration Anchors

**Round 1 (Bracketing):**
- Weak anchors (<3.5): SaOxhcDCM3 (3.20), EOPLy80bBm (3.00), f7aWmxgSN4 (3.00), OdoS6cH8MP (2.00) — None topically similar to this paper.
- Middle anchors (3.5–7.5): GtpubstM1D (5.71, Advancing Mathematical Reasoning), cijO0f8u35 (5.25, Scaling Relationship), 1hQKHHUsMx (6.75, What Pretraining Data for Reasoning), w6nlcS8Kkn (6.67, To CoT or not to CoT).
- Strong anchors (>7.5): f4gF6AIHRy (8.00, Dimensional Collapse), 07yvxWDSla (8.00, Synthetic CPT), jOmk0uS1hl (8.00, Training on Test Task), wg1PCg3CUP (8.00, Scaling Laws for Precision).

**Bracket:** This paper sits between ~5.0 and ~7.0, below the 7.5+ papers which have higher novelty/cleanliness, above the <3.5 papers which have major flaws or different quality levels.

**Round 2 (Narrowing):**
- Inside bracket: eENHKMTOfW (6.00, Training Mice), KHTkRhq2aB (6.00, PAFT), MLhquJb1qN (5.25, Time Transfer), 54KcduuYeG (5.50, AutoScale).
- Upper band: KIPJKST4gw (7.25, At Which Training Stage Code Data Helps), 1hQKHHUsMx (6.75), zpDGwcmMV4 (6.75, Mistakes on Grade-School Math).

**Comparisons:**
- vs. GtpubstM1D (5.71): Current paper is stronger — trains from scratch not CPT, broader domain coverage (math+science+code), controls token budgets, includes RL phase, has cleaner catch-up experiment. Score above.
- vs. KIPJKST4gw (7.25): Current paper is slightly weaker — that paper's code-vs-NL comparison is cleaner than the confounded comparison here. However, current paper's scope is broader and budgets are better controlled. Score below.
- vs. eENHKMTOfW (6.00): Comparable — both are solid empirical studies with practical findings. Current paper has more novel findings but also more significant weaknesses. Score around here.

**Final score: 6.0**

---

## Summary

This paper conducts an extensive empirical study on how reasoning data (varying in diversity, scale, and quality) affects LLM performance when introduced at different training phases. The authors pretrain 8B models from scratch for 1T tokens under four reasoning-data conditions, cross them with multiple SFT recipes, and evaluate through RL. The core findings — that injecting reasoning data during pretraining creates durable advantages that SFT alone cannot recover, that the optimal data strategy is phase-dependent (diverse data for pretraining, high-quality data for SFT), and that high-quality pretraining data can show latent benefits unlocked only after SFT — are well-supported at the aggregate level and constitute a meaningful empirical contribution.

## Strengths

1. **Systematic, fully-crossed three-phase design with controlled token budgets.** The paper trains 4 pretraining conditions × 3 SFT recipes (12 models) plus RL, all with fixed 80B reasoning-token budgets. This goes substantially beyond prior work (Cheng et al. 2024, Liang et al. 2025, Gandhi et al. 2025), which studied only mid-training interventions or did not control budgets across phases. The design makes the "front-loading" comparison testable rather than anecdotal.

2. **Clean refutation of the "catch-up" hypothesis (Table 4).** Doubling SFT epochs on $\mathcal{M}_{\text{base}}$ (29.92→34.01) still fails to match even the weakest reasoning-pretrained model ($\mathcal{M}_{\text{SHQ}}+\text{SFT}_{\text{SHQ}}$ at 37.33). This is a controlled, quantitative disconfirmation — not a qualitative claim.

3. **Demonstration of phase-dependent data sensitivity via cross-tabulated comparisons (Tables 1 and 5).** The same datasets produce different effects at different phases: $\mathcal{M}_{\text{LDQ}}$ outperforms $\mathcal{M}_{\text{SHQ}}$ at pretraining (+9.11), while $\mathcal{D}_{\text{SHQ}}$ outperforms $\mathcal{D}_{\text{LDQ}}$ at SFT (+13.45). Because the same datasets are used in both phases, this contrast isolates phase-dependent rather than dataset-dependent effects.

4. **Latent effect finding (Table 4).** $\mathcal{M}_{\text{LMQ}}$ and $\mathcal{M}_{\text{LDQ}}$ are nearly identical at pretraining (64.07 vs 64.09), yet $\mathcal{M}_{\text{LMQ}}+\text{SFT}_{\text{SHQ}}$ (50.95) outperforms $\mathcal{M}_{\text{LDQ}}+\text{SFT}_{\text{SHQ}}$ (46.70) by +4.25 after SFT. This demonstrates that high-quality pretraining data can encode latent benefits activated only by alignment — a non-obvious result.

5. **Evidence that naive SFT scaling harms math reasoning (Table 8).** Doubling $\mathcal{D}_{\text{LDQ}}$ in SFT drops MATH SFT AVG from 28.38 to 23.46, while adding 0.4% high-quality filtered data ($\mathcal{D}_{\text{ALF}}$) raises it to 60.95. This directly supports the claim that "naively scaling SFT data can be detrimental."

## Weaknesses

### Fatal
None.

### Major

1. **Confounded dataset comparisons undermine the core attribution claim.** $\mathcal{D}_{\text{LDQ}}$ (268M samples, broad domain coverage, heterogeneous quality) and $\mathcal{D}_{\text{SHQ}}$ (1.2M samples, narrow math-heavy coverage, curated high quality) differ on **three axes simultaneously**: size, diversity, and quality. The paper attributes $\mathcal{M}_{\text{LDQ}}$'s pretraining advantage to "diversity and scale" and the SFT advantage of $\mathcal{D}_{\text{SHQ}}$ to "quality," but these attributions are confounded. The $\mathcal{D}_{\text{ALF}}$ ablation partially addresses this for the SFT phase by filtering within $\mathcal{D}_{\text{LDQ}}$ itself, but the pretraining-phase attribution remains unsubstantiated at the claimed level of precision. A clean test would require datasets that independently vary one axis at a time.

2. **Differential repetition rates during pretraining are uncontrolled.** $\mathcal{D}_{\text{SHQ}}$ (1.2M samples) must be repeated ~67× to reach the 80B reasoning-token budget, while $\mathcal{D}_{\text{LDQ}}$ (268M samples) is seen roughly once. The paper acknowledges repetition ("When a reasoning dataset is small, it is repeated") but does not discuss whether this differential repetition rate affects the comparison — e.g., whether the $\mathcal{D}_{\text{SHQ}}$ model overfits or experiences diminishing returns from repeated examples.

3. **RL phase only compares two of the four pretraining conditions (Table 3).** The claim that pretraining choices "dictate the final performance ceiling" is only demonstrated for $\mathcal{M}_{\text{base}}$ vs. $\mathcal{M}_{\text{LMQ}}$. Whether $\mathcal{M}_{\text{SHQ}}$ or $\mathcal{M}_{\text{LDQ}}$ also compound through RL is untested, which weakens the generality of the strongest claims.

### Minor

1. **Percentage claims in the abstract are ambiguously presented.** The headline numbers (19%, 11%, 15%) use "%" without distinguishing absolute percentage-point differences from relative gains. Tracing each to a specific table row requires interpretation — e.g., the 19% gain from Table 3 is 18.74 percentage points (a ~49% relative gain), but which convention is used is never stated. For a paper whose contribution is empirical, this is a basic communication lapse.

2. **"Front-loading" metaphor overstates what the experiment tests.** The experiment introduces reasoning data only in the last **400B of 1T tokens** (after 600B of pure $\mathcal{D}_{\text{base}}$), testing late-pretraining injection, not front-loading from token 0. The title and central metaphor imply stronger claims about timing within pretraining than the design supports. The comparison tested — "pretraining vs. SFT" — is meaningful, but should be described more precisely.

3. **No discussion of potential data contamination.** The evaluation benchmarks (GSM8K, MATH-500, AIME24/25, GPQA-Diamond, LiveCodeBench) overlap in domain and style with the training data. Data contamination is a standard concern for training-data studies and should be addressed.

4. **Instruction-following drop at higher reasoning ratios (Table 7).** INS drops from 49.82 to 44.81 when going from 80/20 to 60/40 reasoning ratio. This is a substantial practical concern for the "front-loading" recommendation and is discussed only briefly as a "breadth-alignment trade-off" without deeper analysis.

### Trivial
None.

## Nice-to-Haves

- Justify the 600B-token warmup before any reasoning data. This is an important design parameter that goes undefended.
- Report variance or uncertainty for key comparisons. While large-scale pretraining experiments rarely report error bars, stating the number of evaluation runs (already provided) is useful; a simple bootstrapped confidence interval for the headline claims would strengthen them.
- Extend RL evaluation to the $\mathcal{M}_{\text{SHQ}}$ and $\mathcal{M}_{\text{LDQ}}$ conditions to determine whether compounding effects are universal across data compositions.
- Test whether the onset position of reasoning data within pretraining (e.g., starting at token 0 vs. token 600B) changes the conclusions.

## Removed Points

The following points from the harsh critic were removed after verification against the paper:
- **"SFT numbers are low and need contextualization"** — The paper is about relative comparisons, not absolute performance on hard benchmarks (AIME, GPQA) for an 8B model. This is a scope nitpick.
- **"Reproducibility limited by proprietary data"** — The paper cites released NVIDIA datasets and model architectures; questioning availability of cited entities violates the hard rules.
- **"Variance/error bars missing"** — Not standard for large-scale pretraining studies; moved to Nice-to-Haves.
- **"1.2B Transformer experiment mentioned in passing"** — Appendix is stripped, so this cannot be verified.
- **"The 600B warmup goes undefended"** — This is a design choice that holds constant across all conditions, so it does not affect internal validity; moved to Nice-to-Haves.

## Novel Insights

The most striking finding that emerges beyond the paper's own framework is the **asymmetric sensitivity to repetition**: small, high-quality datasets ($\mathcal{D}_{\text{SHQ}}$) must be repeated heavily during pretraining yet still underperform large, diverse datasets seen once. This suggests that in pretraining, **coverage of diverse reasoning patterns matters more than exposure frequency**, even when quality is lower — a potentially important scaling principle. The latent effect (high-quality data showing no immediate benefit but unlocking gains after SFT) also runs counter to the intuitive "more quality always wins" narrative and suggests that the interaction between data properties and training phases is more nuanced than simple dominance rankings. Together with the catch-up refutation, these results point toward a training strategy where pretraining is optimized for breadth (exposure to diverse problem structures) and SFT for depth (intensive refinement on high-quality examples).

## Suggestions

1. **Disentangle the confounded axes in at least one key comparison.** For example, downsample $\mathcal{D}_{\text{LDQ}}$ to match $\mathcal{D}_{\text{SHQ}}$'s sample count to isolate scale from diversity/quality, or diversify $\mathcal{D}_{\text{SHQ}}$'s domain coverage while keeping quality fixed. Even one additional controlled comparison would substantially strengthen the asymmetric principle claim.

2. **Clarify the reporting convention for all percentage claims.** State clearly whether numbers in the abstract and intro are percentage-point differences or relative gains, and ensure every claimed figure can be directly located in a table.

3. **Replace "front-loading" with a more descriptive term** such as "pretraining injection" or "early-phase reasoning data" unless experiments are added that vary the onset position within pretraining.

4. **Discuss the repetition rate confound and potential overfitting** for the small-scale $\mathcal{D}_{\text{SHQ}}$ condition, which would improve the paper's scientific rigor.

5. **Add a data contamination analysis** using standard substring matching or n-gram overlap between training and evaluation sets.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>