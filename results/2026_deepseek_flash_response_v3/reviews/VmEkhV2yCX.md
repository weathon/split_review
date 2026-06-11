Now let me write the complete final review.

## Summary

This paper conducts an empirical study of how reasoning data — varying in diversity, scale, and quality — affects LLM performance when introduced at different stages of training (pretraining vs. SFT). The authors pretrain 8B-parameter models from scratch for 1T tokens with controlled injection of reasoning data, then apply SFT and RL. The central finding is an **asymmetric principle**: pretraining benefits most from broad diversity and scale of reasoning data, while SFT is dominated by data quality. Additional findings include a **latent effect** where high-quality pretraining data shows minimal immediate benefit but emerges after SFT, and a demonstration that naive SFT scaling with mixed-quality data can be counterproductive.

## Strengths

1. **Fully-crossed experimental design isolating pretraining vs. SFT contributions**: The paper pretrains four base models from scratch (M_base, M_SHQ, M_LDQ, M_LMQ) and fine-tunes each on three distinct SFT datasets (D_SHQ, D_LDQ, D_LMQ), producing 12 SFT models (Section 2.3, Table 2). This setup enables clean attribution of effects to data characteristics at each stage, going beyond prior work that only intervened in one phase.

2. **Controlled token budget isolates data character from quantity**: All reasoning-augmented pretraining runs use exactly 80B reasoning tokens at a fixed 80/20 base/reasoning ratio over 400B tokens (Section 2.3, line 93). The comparison between M_SHQ (small, high-quality, low diversity) and M_LDQ (large, lower-quality, high diversity) therefore attributes the +9.09% pretraining gap to data diversity and scale rather than simply more reasoning tokens.

3. **Falsifiable "catch-up" test with double SFT compute**: The paper explicitly tests whether a baseline model (M_base) given 2× SFT epochs can match a reasoning-pretrained model (M_SHQ + SFT_SHQ). Table 4 shows the doubled baseline still falls short by 3.32%, providing direct empirical evidence that the pretraining advantage persists beyond increased SFT budget.

4. **Latent-effect discovery backed by a clean counterfactual**: M_LMQ (combining diverse + high-quality data) shows only +0.02% gain over M_LDQ at pretraining (Table 1, 64.07 vs 64.09), but opens a +4.25% gap after SFT (Table 4, 50.95 vs 46.70). This non-obvious result — that pretraining quality effects can be invisible at pretraining and only emerge after alignment — is a genuinely novel finding supported by the controlled design.

5. **RL phase confirms compounding rather than diminishing returns**: Table 3 shows the gap between M_LMQ+SFT+RL and M_base+SFT+RL widens to 18.57% average and 39.32% on AIME — the gap grows through each training stage. This provides concrete evidence against the "overfitting" hypothesis raised in the introduction (Section 1, lines 30–31).

6. **SFT scaling ablation with a controlled detrimental baseline**: Table 8 compares naive 2× scaling of mixed-quality data (2×LDQ) against targeted addition of high-quality data (ALF*). The 4.92% drop in math accuracy from the naive strategy is a concrete demonstration that "more SFT data is not always better."

## Weaknesses

### Major

- **"Catch-up" claim is overstated given total reasoning volume imbalance.** The paper states (lines 36–37) that its results "refute the catch-up... hypothesis, proving that SFT cannot compensate for a weak foundation." However, the catch-up experiment compares M_base + 2× SFT epochs against models that saw **80B reasoning tokens during pretraining alone**. The SFT dataset is 4.8M samples; even at a generous average of ~4K tokens per sample (long by SFT standards), the 2× condition exposes M_base to roughly 38B reasoning tokens — less than half the 80B the reasoning-pretrained models saw *before any SFT*. The experiment tests whether *doubling SFT epochs* closes the gap, not whether a matched total volume of reasoning tokens could. The paper's own Equation 2 frames the problem as a fixed-budget allocation constraint, yet the experiments never enforce this. This does not undermine the core asymmetric principle finding, but the "refutation of catch-up" is overclaimed relative to the actual experimental control.

### Minor

- **"Front-loading" mischaracterizes the intervention.** The paper's title, abstract, and headline claims use "front-loading" to describe its intervention. However, Section 2.3 (line 93) states that reasoning data is introduced only in the last 400B tokens of 1T pretraining (after 600B tokens of base-only data). This is the *late* phase of pretraining — closer to what the paper itself calls "mid-training" in the related work (citing Ai et al., 2025; Wang et al., 2025). The comparison (reasoning in pretraining vs. only in SFT) remains meaningful, but "front-loading" implies introduction from token 0, which does not match the actual design.

- **No variance or uncertainty estimates for key comparisons.** All comparisons are reported as single numbers without error bars, confidence intervals, or multiple training seeds. While the paper reports Pass@1 averaged over multiple evaluation runs for AIME (16 runs) and other benchmarks (4 runs, line 148), these are evaluation runs on the same model, not training seeds. For large-margin results (e.g., the 19% RL gap in Table 3) this is less concerning, but for small-margin comparisons — 64.07 vs. 63.97 (20% vs. 10% reasoning ratio, Table 6), 42.66 vs. 43.04 (ALF vs. ALF*, Table 8), and the +4.25% latent effect (Table 4) — it is impossible to assess whether these reflect real phenomena or noise.

- **Percentage gains stated without specifying absolute vs. relative.** The paper reports "+19%," "+11%," and "+15%" gains (abstract, lines 36–37) without stating whether these are absolute percentage points or relative improvements. From the tables, these are clearly absolute percentage point differences (e.g., 56.66 − 37.92 = 18.74 pp in Table 3). Stating them as "19%" without clarification could be misinterpreted as a relative improvement, which would be substantially larger (a 50% relative gain on a base of ~38).

### Trivial

- The 1.2B Transformer ablation (referenced as Table 14, likely in the stripped appendix) is mentioned only in passing (line 172). Inlining a brief summary of the result would help readers assess generality without consulting the appendix.

## Nice-to-Haves

- The paper tests whether 2× SFT epochs close the catch-up gap, but does not test whether a longer RL phase for M_base (more than 1 epoch) could close the RL gap shown in Table 3. Adding this would strengthen the catch-up analysis.
- A brief quantification of dataset properties (e.g., topic diversity, average response length, complexity scores) for D_LDQ, D_SHQ, and D_LMQ would help ground the "diversity" and "quality" labels beyond dataset provenance.

## Removed Points

These points from the original reviews were removed after verification against the paper:

- **"First systematic study" claim is overstated** (Harsh Critic): The paper genuinely appears to be the first to systematically vary diversity, quality, and scale of reasoning data across both PT and SFT at this scale. Prior mid-training work (Wang et al., Ai et al., Gandhi et al.) does not perform this kind of systematic cross-variation. The claim is reasonable.
- **Criticism about D_SHQ repetition causing memorization/overfitting** (Harsh Critic): Speculative without evidence. The paper's results show M_SHQ underperforms M_LDQ at pretraining, which is consistent with limited diversity, not necessarily memorization. No data supports this concern.
- **Missing related works**: The paper has an adequate related work section covering the relevant literature. Per hard rules, I cannot flag missing references without external verification.
- **Formatting/style nitpicks**: Removed per hard rules about parser artifacts.
- **Criticisms about missing appendix content**: The appendix is stripped by the parser. Per hard rules, I cannot penalize the paper for content removed during PDF extraction.

## Novel Insights

The reviews collectively surface an interesting tension: the paper's strongest and most defensible finding (the asymmetric principle — diversity for PT, quality for SFT) is somewhat buried beneath more attention-grabbing but less well-supported claims about "front-loading" and the "catch-up refutation." The fact that the asymmetry finding requires a fully-crossed 4×3 design to uncover — and that it leads to a non-obvious practical recommendation (use diverse data for PT, curated data for SFT, don't just use "best" data everywhere) — is itself the paper's most valuable contribution. This asymmetry finding is robust to the volume confound critique, and the latent effect provides an additional mechanistic insight.

## Suggestions

1. **Recast the catch-up discussion.** Replace "proving that SFT cannot compensate for a weak foundation" with a more precise claim: "under realistic SFT budgets (2× epochs, same data), a model without reasoning in pretraining cannot match models that had reasoning during pretraining." The volume confound should be acknowledged.

2. **Replace "front-loading"** with more precise terminology reflecting that reasoning data was introduced in the late phase of pretraining (e.g., "early injection in the training pipeline" or "reasoning-augmented pretraining").

3. **Add variance information.** Report standard deviations or confidence intervals from the multiple evaluation runs already performed (16 runs for AIME). For smaller-margin comparisons, consider bootstrap estimates.

4. **State percentage types explicitly.** Clarify in the abstract that reported gains (19%, 11%, 15%) are absolute percentage point differences.

## Score and Decision

**Calibration anchors (all rounds):**

| Anchor | Avg. Score | Round | Comparison |
|--------|-----------|-------|------------|
| qgLyKwXVDs (FreeLM) | 2.00 | R1-bracket | Not topically similar; paper is far stronger |
| 8uXkyWFVum (Amuro and Char) | 4.20 | R1-bracket | Similar topic (PT/FT relationship); current paper is far stronger (8B from scratch vs. 1B, broader eval, novel findings) |
| GtpubstM1D (Adv. Math. Reasoning) | 5.71 | R1-bracket | Similar topic; current paper is more comprehensive (systematic diversity/quality/scale variation vs. focused math-only study) |
| cijO0f8u35 (Scaling Relationship) | 5.25 | R2-narrow | Similar topic; current paper is much stronger (full pretraining, diverse benchmarks, novel findings) |
| pszewhybU9 (InsTag) | 6.25 | R2-narrow | Comparable empirical rigor; current paper has larger-scale experiments but slightly weaker presentation |
| 5HCnKDeTws (When Scaling Meets Finetuning) | 6.75 | R2-narrow | Similar empirical style; current paper slightly weaker due to overclaiming/terminology issues |

**Round 1 bracket:** 5.5–6.5. Paper clearly above 4.20 and 5.25 anchors, comparable to 5.71 and 6.25 anchors, slightly below 6.75 anchor.

**Round 2 narrowing:** After reading full reviews of anchors at 5.25, 5.71, 6.25, and 6.75, the paper sits closest to the 5.71–6.25 range. It is stronger than the 5.25 paper (which evaluated only GSM8K), slightly stronger than the 5.71 paper (more systematic design, broader evaluation), comparable to the 6.25 paper, and slightly weaker than the 6.75 paper (which has cleaner framing and no overclaiming issues). **Final score: 6.0.**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>