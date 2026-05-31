## Summary

This paper presents the first systematic, from-scratch empirical study of how reasoning data should be allocated across the LLM training pipeline (pretraining → SFT → RL). The authors pretrain 8B models for 1T tokens while controlling the injection of reasoning data varying in diversity, quality, and scale. Their central finding is an asymmetric allocation principle: **diversity drives pretraining effectiveness, while quality governs SFT**. Additional findings include that front-loading reasoning into pretraining creates durable advantages that SFT cannot compensate for (refuting the "catch-up" hypothesis), that high-quality pretraining data has latent effects unlocked only after SFT, and that naively scaling SFT data with mixed-quality data harms mathematical reasoning.

## Strengths

1. **From-scratch pretraining at scale with controlled reasoning injection** — The paper pretrains 8B models from scratch for 1T tokens with a constant 80B token budget for reasoning data across all conditions. This is a substantial methodological advance over prior work that relies on mid-training or continued pretraining on existing models. Evidence: Section 2.3.

2. **Rigorous refutation of the catch-up hypothesis** — Table 4 shows that even doubling SFT epochs for the baseline model (M_base) fails to match the weakest reasoning-pretrained model (M_SHQ), with a remaining gap of +3.32%. This is clean, compelling evidence that SFT cannot substitute for reasoning-aware pretraining.

3. **Discovery of latent effects from high-quality pretraining data** — M_LMQ achieves only a +0.03 average gain over M_LDQ at the pretraining stage, but after SFT the gap widens to +4.25%. This reveals a previously undocumented synergy where high-quality data in pretraining instills latent potential activated during alignment. Evidence: Section 5, Table 4.

4. **Demonstration that naive SFT scaling is harmful** — Table 8 shows that doubling mixed-quality SFT data actively reduces math reasoning by -4.92%, while adding only 0.4% high-quality samples (D_ALF + D_SHQ) improves performance. This has clear and actionable practical implications.

5. **Full-pipeline tracking from pretraining through RL** — The paper documents how the gap widens at each training stage, culminating in an 18.74% absolute lead on expert-level benchmarks after RL (Table 3: M_LMQ at 56.66 vs M_base at 37.92). The compounding-advantage narrative is well-supported.

6. **Replication with 1.2B model** — Demonstrates robustness of the front-loading strategy across model scales (Table 14 in appendix).

## Weaknesses

### Fatal
None.

### Major
1. **Confounded comparison between diversity and repetition in pretraining.** The central claim that "pretraining benefits most from broad diversity" rests heavily on comparing M_SHQ (1.2M unique examples, repeated ~67× to reach 80B tokens) with M_LDQ (268M unique examples, near-zero repetition). These differ simultaneously in diversity, number of unique examples, and degree of repetition. The ~9% advantage of M_LDQ over M_SHQ could partially reflect overfitting from extreme repetition rather than (just) the value of diversity. A clean test would subsample LDQ to 1.2M unique examples, repeat to 80B tokens, and compare against both conditions. **This does not invalidate the paper's core claims** — the catch-up experiment (Table 4) and ALF experiment (Table 8) provide convergent evidence for the asymmetric principle — but it reduces the precision with which the diversity claim can be stated. Evidence: Table 1, Section 2.3.

### Minor
1. **Limited RL evaluation.** Only two conditions (M_base + SFT_SHQ and M_LMQ + SFT_SHQ) are carried through to RL. The headline 19% average gain rests on this single comparison. Including at least M_LDQ + SFT_SHQ + RL would help distinguish whether the compounding advantage is specific to the LMQ+SHQ combination or generalizes to other reasoning-pretrained models. Evidence: Table 3.

2. **SFT quality comparison confounded with epoch count.** In Table 5, when comparing SFT on D_SHQ vs D_LDQ, the training sample count is fixed at 4.8M. For D_SHQ (1.2M examples) this means ~4 epochs; for D_LDQ (268M examples) this means training on only ~1.8% of the dataset with minimal repetition. The superiority of D_SHQ could partly reflect the benefit of multiple exposures rather than quality alone. The ALF experiment (Table 8, 7.1M examples with ~0.68 epochs) provides convergent evidence that partially mitigates this concern but does not eliminate it for the Table 5 comparison. Evidence: Sections 3.1, Table 5.

3. **Ratio sensitivity confounded with total reasoning exposure.** Table 6 varies the reasoning proportion from 10%→20%→40% but this also changes total reasoning tokens from 40B→80B→160B. The paper discusses this as a ratio effect, but it confounds ratio with absolute exposure. A 10% ratio with 2× total pretraining tokens would be needed to separate these factors. Evidence: Table 6.

4. **No error bars or variance estimates.** Key results (especially small differences like the 4.25% latent quality effect) are presented as point estimates without confidence intervals or variance measures. Given that numbers are averages across multiple benchmarks, some measure of dispersion would help readers assess reliability. This is a common gap in large-scale pretraining studies but worth noting.

### Trivial
None.

## Nice-to-Haves
- Training loss curves during pretraining could reveal whether the SHQ model overfits from heavy repetition.
- Computational cost estimates (GPU-hours) would help practitioners evaluate the practical trade-offs.
- The headline gains in the abstract (19%, 11%, 15%) should be more clearly traceable to specific table entries with the denominator (absolute vs. relative improvement) explicitly stated.

## Removed Points
- **Harsh critic's claim about missing reproducibility** due to proprietary datasets: removed. The paper describes datasets and experimental design in sufficient detail for principles to transfer, and references to cited datasets are assumed valid.
- **Pure formatting/style nitpicks** from the harsh critic: removed per instructions.
- **Strawman weaknesses** (e.g., "the paper does not discuss X" when X is outside scope): removed.
- **Speculative fatal flaws** (e.g., "the diversity claim could be entirely driven by repetition"): demoted. The concern is real but the claim is stated as a confound, not as proven wrong. The paper's broader claims survive this weakness.
- **Strength Finder's generic strengths** ("addresses an important problem," "timely topic"): removed. Only concrete, evidence-grounded strengths retained.

## Novel Insights
None beyond the paper's own contributions. The reviews did not surface a genuinely novel interpretation of the results that the paper itself does not already discuss.

## Suggestions
1. **Highest priority: Disentangle diversity from repetition in the pretraining comparison.** Sub-sample D_LDQ to 1.2M unique examples, repeat to 80B tokens, and compare against both the current M_SHQ (1.2M, repeated) and M_LDQ (268M, not repeated). Either outcome (subsampled-LDQ matches M_LDQ → diversity claim holds; subsampled-LDQ matches M_SHQ → original gap was driven by repetition) is informative.
2. **Extend RL evaluation** to at least one intermediate condition (e.g., M_LDQ + SFT_SHQ + RL) to turn the two-point comparison into a trend.
3. **Acknowledge the SFT epoch confound explicitly** and leverage the ALF result (which has minimal repetition) to argue that the quality-dominance claim is supported by convergent evidence.
4. **Acknowledge the ratio/total-exposure confound** in Table 6 and discuss why the conclusion about ratio sensitivity remains reasonable despite this.

## Score and Decision

**Round 1 — Bracketing:**
Three calibration queries were used to identify anchor papers in score ranges <3.5, (3.5–7.5), and >7.5 on topics related to reasoning data, pretraining, and LLM training.

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `qgLyKwXVDs` (FreeLM) | 2.00 | R1 | Much weaker submission; this paper is substantially stronger |
| `mfTM4UdYnC` (LogicJitter) | 2.50 | R1 | Much weaker; unrelated topic |
| `koza5fePTs` (Planning Capabilities) | 2.00 | R1 | Much weaker |
| `EukID7GvBy` (Gradual Learning) | 3.00 | R1 | Much weaker |
| `506Sxc0Adp` (Diversity Coefficient) | 4.00 | R1 | Weaker; narrower contribution |
| `kDakBhOaBV` (Diversity Coefficient) | 4.00 | R1 | Weaker; same paper variant |
| `GtpubstM1D` (Advancing Math Reasoning) | 5.71 | R1/R2 | Closest topical match. This paper has stronger experimental design (from-scratch pretraining vs. continued pretraining) and broader scope |
| `qUJsX3XMBH` (Random Selection for SFT) | 4.40 | R1 | Weaker; narrower scope |
| `07yvxWDSla` (Synthetic Continued Pretraining) | 8.00 | R1 | Stronger; cleaner methodology and no confounds |
| `f4gF6AIHRy` (Diversified File Selection) | 8.00 | R1 | Stronger; cleaner methodology |
| `PdaPky8MUn` (Never Train from Scratch) | 8.00 | R1 | Stronger; cleaner analysis |
| `jOmk0uS1hl` (Training on Test Task) | 8.00 | R1 | Stronger; cleaner methodology |

**Round 1 bracket:** between 5.0 and 7.5.

**Round 2 — Narrowing:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| `oqsQbn4XfT` (Diversity of Synthetic Data) | 5.80 | R2 | Weaker; this paper's from-scratch experiments are more substantive |
| `1hQKHHUsMx` (What Kind of Pretraining Data) | 6.75 | R2 | Comparable quality on a different question; cleaner methodology but narrower scope |
| `EDoD3DgivF` (Linear Representations) | 6.00 | R2 | Different focus; this paper is more applied/empirical |
| `miGpIhquyB` (Dataset Generation) | 5.50 | R2 | Weaker |
| `cijO0f8u35` (Scaling Math Reasoning) | 5.25 | R2 | Weaker |
| `28gMnEAgl9` (Abstract Reasoners) | 5.33 | R2 | Weaker |
| `BGnm7Lo8oW` (Learning to Reason at PT Scale) | 5.50 | R2 | Weaker; cleaner motivation but less empirical substance |

The most informative anchor is `1hQKHHUsMx` (avg 6.75, Accept — "What Kind of Pretraining Data"). That paper is cleaner methodologically (no confound comparable to the repetition/diversity issue here) but has much narrower scope (80 queries, simple math, two models). This paper has broader scope and more actionable findings but has the confounds discussed above. This comparison situates the paper slightly below 6.75.

**Final score: 6.5**

The paper makes a strong, timely, and actionable empirical contribution through the first systematic from-scratch pretraining study of reasoning data allocation. The identified confounds (diversity/repetition, SFT epoch count, RL condition count) are real but addressable and do not threaten the paper's core findings — the catch-up experiment (Table 4) and the ALF experiment (Table 8) provide convergent evidence for the asymmetric principle. With the suggested controls, the paper would be substantively stronger.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>