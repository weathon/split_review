Now I have all the information I need. Let me compile the final review.

---

## Summary

This paper conducts a large-scale empirical study investigating how reasoning data — varying in diversity, quality, and scale — affects LLM performance when introduced at different training stages (pretraining, SFT, and RL). Training 8B hybrid Mamba2/Transformer models from scratch for 1T tokens across multiple conditions, the authors uncover four key findings: (1) front-loading reasoning into pretraining creates durable advantages that post-training cannot recover; (2) an asymmetric allocation principle where diversity matters in pretraining but quality dominates SFT; (3) high-quality pretraining data has latent effects activated only after SFT; and (4) naive scaling of SFT data is harmful. The study represents a significant computational investment and provides actionable guidance for data strategy across the full training pipeline.

## Strengths

- **Durable front-loading advantage confirmed through the full pipeline (PT → SFT → RL).** Table 3 shows the model pretrained with reasoning data ($\mathcal{M}_{\text{LMQ}} + \text{SFT}_{\text{SHQ}} + \text{RL}$) achieves an 18.57% absolute lead over the baseline ($\mathcal{M}_{\text{base}} + \text{SFT}_{\text{SHQ}} + \text{RL}$) on expert-level benchmarks, with a 39.32% gain on AIME competition problems. This is direct evidence that early reasoning injection produces compounding returns through post-training.

- **Crisp asymmetric allocation principle with phase-dependent reversal.** Table 1 shows diverse data ($\mathcal{M}_{\text{LDQ}}$, avg 64.09) far outperforms narrow high-quality data ($\mathcal{M}_{\text{SHQ}}$, avg 54.98) during pretraining, while Table 5 shows the reverse during SFT: fine-tuning with high-quality $\mathcal{D}_{\text{SHQ}}$ (avg 44.99) dramatically outperforms diverse $\mathcal{D}_{\text{LDQ}}$ (avg 31.54). This phase-dependent reversal is a clean, actionable finding.

- **Strong refutation of the catch-up hypothesis.** Table 4 shows that even doubling SFT epochs for the baseline ($\mathcal{M}_{\text{base}} + 2\times\text{SFT}_{\text{SHQ}}$, avg 34.01) fails to match the weakest reasoning-pretrained model ($\mathcal{M}_{\text{SHQ}} + \text{SFT}_{\text{SHQ}}$, avg 37.33), let alone stronger ones. This directly demonstrates that SFT alone cannot compensate for a non-reasoning pretraining foundation.

- **Latent effect of high-quality pretraining data revealed by SFT.** In Table 4, $\mathcal{M}_{\text{LMQ}} + \text{SFT}_{\text{SHQ}}$ (avg 50.95) outperforms $\mathcal{M}_{\text{LDQ}} + \text{SFT}_{\text{SHQ}}$ (avg 46.70) by 4.25%, despite $\mathcal{M}_{\text{LMQ}}$ and $\mathcal{M}_{\text{LDQ}}$ having nearly identical pretraining scores (64.07 vs 64.09). This controlled comparison cleanly demonstrates a latent advantage unlocked only by alignment.

- **Ablation on naive SFT scaling reveals active harm.** Table 8 provides a clean counterexample to "more is better": doubling mixed-quality SFT data ($2\times\text{LDQ}$) yields no average gain and actively reduces math accuracy by −4.92%, while a 0.4% addition of high-quality data ($\mathcal{D}_{\text{ALF}}'$) improves overall accuracy.

## Weaknesses

### Fatal

None. The core claims are well-supported by the evidence presented.

### Major

None. The issues identified are addressable and do not threaten the paper's central conclusions.

### Minor

- **Token budget asymmetry between baseline and reasoning-augmented models.** $\mathcal{M}_{\text{base}}$ is pretrained on 1T tokens of $\mathcal{D}_{\text{base}}$ alone. The reasoning-augmented models receive 600B $\mathcal{D}_{\text{base}}$ + 400B (80% $\mathcal{D}_{\text{base}}$, 20% $\mathcal{D}_{\text{res}}$) = 920B $\mathcal{D}_{\text{base}}$ + 80B $\mathcal{D}_{\text{res}}$. Thus $\mathcal{M}_{\text{base}}$ sees 80B *more* $\mathcal{D}_{\text{base}}$ tokens than the reasoning models. While the paper frames this as "when token counts are controlled" (total tokens: 1T for all), base tokens are not controlled. The confound does **not** invalidate the results — the ratio experiments (Table 6) show that increasing the reasoning fraction *improves* performance even as base tokens decrease further, which argues against "less base data helps" — but the magnitude of the reasoning-specific benefit is somewhat uncertain. The paper should explicitly acknowledge this asymmetry. The cleanest control would be a baseline trained on 920B $\mathcal{D}_{\text{base}}$ tokens, matching the reasoning models' base exposure.

- **Single training run per condition with no statistical uncertainty estimates.** All pretraining, SFT, and RL experiments are single-seed runs with no error bars, confidence intervals, or variance estimates from training. While the scale of these experiments (512 H100 GPUs, 1T tokens per run) makes multiple seeds prohibitively expensive — a genuine constraint the field accepts — the paper should at minimum acknowledge this limitation explicitly. Some mitigation exists: evaluation metrics (e.g., AIME pass@1 averaged over 16 generations) provide evaluation variance, but this does not capture training variance. The paper would be strengthened by a brief statement about expected run-to-run variability at this scale, drawing on literature precedence.

- **RL phase tested on only two conditions.** The RL experiments compare only $\mathcal{M}_{\text{base}} + \text{SFT}_{\text{SHQ}}$ vs. $\mathcal{M}_{\text{LMQ}} + \text{SFT}_{\text{SHQ}}$. This does not test whether the asymmetric principle (diversity in PT, quality in SFT) carries through to RL for other conditions (e.g., $\mathcal{M}_{\text{LDQ}}$ or $\mathcal{M}_{\text{SHQ}}$ backbones). The gap is understandable given resource constraints, but the paper's claim that front-loading reasoning yields "compounding returns" through RL is based on a single comparison pair. Discussing whether the asymmetric principle is expected to hold through RL would strengthen the paper.

### Trivial

- **SFT epoch counts not specified.** The paper states "each 8B LLM is finetuned on 4.8M reasoning samples from $\mathcal{D}_{\text{res}}$" but does not state how many epochs this implies for each dataset. For $\mathcal{D}_{\text{SHQ}}$ (1.2M samples), this is ~4 epochs; for $\mathcal{D}_{\text{LDQ}}$ (268M samples), ~0.018 epochs. The "catch-up" experiment ($2\times$ epochs) is relative to this unspecified baseline. Stating the epoch count explicitly would aid reproducibility.

- **Formalism mismatch in Equation (2).** The budget constraint $\mathcal{B} = |\mathcal{D}_{\text{res}}^{\text{PT}}| + |\mathcal{D}_{\text{res}}^{\text{SFT}}|$ uses sample counts, but the experiment controls tokens (80B reasoning tokens in PT vs. 4.8M samples in SFT). The formalism should reflect the token-level control actually used.

## Nice-to-Haves

- A dedicated limitations section addressing: (a) single architecture (8B hybrid), (b) single pretraining scale (1T tokens), (c) single seed per condition, (d) limited RL evaluation, and (e) reliance on specific reasoning datasets (Nemotron, Guha et al.).
- A full cross-table (each pretrain condition × each SFT condition) for a few key metrics, rather than averaging across $\mathcal{M}_{\text{res}}$ for SFT comparisons. The paper references Table 13 (in the appendix) which presumably provides this breakdown; moving a representative subset to the main text would strengthen the asymmetry claim.
- Additional RL conditions (e.g., $\mathcal{M}_{\text{LDQ}}$ and $\mathcal{M}_{\text{SHQ}}$ backbones) to test whether the asymmetric principle extends through RL, if resources permit.

## Removed Points

These points were identified by reviewers but removed after verification against the paper:

1. *"The '19% average gain' claim in the abstract could mislead readers into thinking it's a universal figure."* — Removed. The abstract is appropriately concise; the specific stage context is clear from the body of the paper, and this is standard practice for abstract-level claims.
2. *"Reasoning behind the 20% ratio is not justified."* — Removed. The paper explicitly states this ratio was set to accommodate the smallest dataset ($\mathcal{D}_{\text{SHQ}}$ at 1.2M samples) being repeated to reach 80B tokens, and the ratio sensitivity experiments (Table 6) systematically address this.
3. *"The paper would benefit from a 'reverse' condition: pretrain with narrow high-quality data then SFT with diverse data."* — Removed. The paper partially addresses this: Table 5 shows $\mathcal{M}_{\text{res}} + \text{SFT}_{\text{LDQ}}$ (diverse SFT) performing poorly. Additionally, $\mathcal{M}_{\text{SHQ}}$ (narrow pretrain) is included in the $\mathcal{M}_{\text{res}}$ aggregate for Table 5, and the full cross-breakdown is referenced via Table 13 in the appendix.
4. *Weakness about missing/insufficient related work.* — Removed per hard rules: I cannot externally verify missing citations.
5. *Critical Issue about "confound could reflect noise or less relevant material in base data."* — The claim of a confound is retained but downgraded from a "critical issue" to Minor, since the ratio experiments (Table 6) provide evidence against the alternative explanation, and the comparison is practically meaningful as a fixed-budget allocation problem.
6. *Strength about "Controlled token budget for fair comparison across data types"* — Partially retained but reframed. The controlled budget argument is valid for comparisons *among* reasoning models ($\mathcal{M}_{\text{SHQ}}, \mathcal{M}_{\text{LDQ}}, \mathcal{M}_{\text{LMQ}}$ all receive exactly 80B reasoning tokens), which supports the diversity/quality findings within pretraining. The baseline comparison is where the asymmetry exists, and this is covered in the weaknesses.

## Novel Insights

None beyond the paper's own contributions. The core novel insights — front-loading reasoning is critical, diversity dominates pretraining while quality dominates SFT, the latent effect, and the harm of naive SFT scaling — are all presented clearly in the paper. The reviews did not surface any additional unanticipated observations.

## Suggestions

- Add a brief limitations section explicitly acknowledging the token budget asymmetry, single-seed runs, single architecture, and limited RL coverage. This would improve the paper's scientific candor and help readers calibrate the generality of the findings.
- In the abstract or introduction, clarify that the "19% gain" refers to the cumulative benefit after the full RL phase, to avoid potential misinterpretation.
- Report the number of SFT epochs explicitly for each dataset configuration in Section 3.1.

## Score and Decision

### Calibration Anchors

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| KIPJKST4gw | 7.25 | 1 (mid) | Most directly comparable — studies at-which-stage to introduce code data for LLM reasoning. Similar method (systematic ablations) and similar limitation (token budget confound). The current paper is stronger: from-scratch 1T-token pretraining vs. continued pretraining, 8B vs 2.6B models, includes RL phase, broader data dimensions. |
| 1hQKHHUsMx | 6.75 | 1 (mid) | Studies reasoning via influence functions on pretraining data. Narrower scope (80 queries, simple math). Current paper is far more comprehensive. |
| GtpubstM1D | 5.71 | 1 (mid) | Studies math reasoning with problem-solving data. Mixed reviews including a 1-score outlier. Current paper is substantially stronger in scope and execution. |
| w6nlcS8Kkn | 6.67 | 1 (mid) | Meta-analysis of CoT effectiveness. Different methodology entirely. Not directly comparable. |
| f7aWmxgSN4 | 3.00 | 1 (low) | Weak anchor — knowledge graph learning in LLMs. Not comparable. |
| qgLyKwXVDs | 2.00 | 1 (low) | Weak anchor — fine-tuning-free language model. Not comparable. |
| 3OyaXFQuDl | 7.00 | 2 (narrow) | Studies compute-optimal synthetic data for reasoning. Different topic, but similar empirical rigor. Current paper is stronger in computational investment and scope. |
| 5HCnKDeTws | 6.75 | 2 (narrow) | Scaling laws for finetuning. Narrower task scope (translation/summarization). Current paper is stronger. |
| oI5tZaWkF9 | 7.50 | 2 (narrow) | Data weighting for synthetic text classification. Different topic. |
| f4gF6AIHRy | 8.00 | 1 (high) | Proposes algorithmic contribution (DiSF). Different paper type. |
| jOmk0uS1hl | 8.00 | 1 (high) | Conceptual contribution about evaluation confounds. Different paper type. |
| 07yvxWDSla | 8.00 | 1 (high) | Proposes method (EntiGraph). Different paper type. |

**Round 1 bracket:** The paper sits between the weak anchors (~2–3) and the strong method/concept anchors (8.0). The most comparable mid-range anchor (KIPJKST4gw at 7.25) suggests the paper is at least at 7+ range.

**Round 2 narrowing:** Reading the most comparable anchors in full (KIPJKST4gw at 7.25, 3OyaXFQuDl at 7.00, 5HCnKDeTws at 6.75) and comparing against the paper under review — the current paper is clearly stronger in scope (from-scratch 1T-token pretraining vs. continued pretraining or finetuning-only), computational investment, comprehensiveness of data variation, and the inclusion of all three training stages (PT, SFT, RL). The nearest anchor in topic and methodology (KIPJKST4gw at 7.25) had a token budget confound similar to the one identified here, yet still received 7.25. The current paper is stronger, placing it above 7.25. It does not, however, propose a novel algorithm or concept in the way the 8.0 anchors do, which distinguishes it from that tier.

**Final score:** 7.5 — a strong empirical contribution with clear, actionable findings, above the most comparable anchors but not at the novel-method tier.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>