## Summary

This paper presents a large-scale empirical study investigating how reasoning data — varying in scale, diversity, and quality — impacts LLM performance when introduced at different training stages (pretraining vs. SFT). The authors train 8B-parameter models from scratch for 1T tokens, controlling the reasoning token budget across conditions. Key findings include: (1) injecting reasoning data during pretraining creates advantages that persist and compound through SFT and RL, (2) an "asymmetric principle" where pretraining benefits from diverse/broad reasoning data while SFT benefits from high-quality reasoning data, (3) SFT cannot fully compensate for a reasoning-poor pretraining foundation under the tested conditions, and (4) high-quality pretraining data can have latent effects that emerge only after SFT.

## Strengths

- **Large-scale controlled pretraining experiment.** Training 8B models from scratch for 1T tokens with systematic variation of reasoning data diversity, quality, and scale is genuinely rare in the literature. The constant 80B reasoning token budget (line 93) ensures fair cross-condition comparison, and the scale exceeds prior studies on this question.

- **Asymmetric principle demonstrated within a single controlled framework.** Tables 1 and 5 together show a clean reversal: diverse data (M_LDQ, 64.09%) far outperforms narrow high-quality data (M_SHQ, 54.98%) in pretraining, but during SFT, high-quality data (SFT_SHQ, 44.99%) far outperforms large diverse data (SFT_LDQ, 31.54%). This within-study reversal proves the asymmetry is phase-dependent — a stronger demonstration than prior work studying only one phase.

- **Latent-effect finding across two stages.** The paper shows that adding high-quality but narrow data to a diverse mix (M_LMQ) yields minimal immediate advantage over M_LDQ in pretraining (64.07 vs 64.09), yet unlocks a +4.25% gain after SFT (Table 4, lines 213-215). This non-obvious result is supported by two-stage measurement.

- **RL phase demonstrates compounding returns, not convergence.** Table 3 shows the gap widening from +8.35% (pretraining) to +9.3% (post-SFT) to +18.57% (post-RL), including +39.32% on AIME. This monotonic widening refutes the alternative hypothesis that early advantages would wash out.

- **Controlled SFT scaling comparison (Table 8).** The head-to-head contrast of naive 2× scaling of mixed-quality data (hurting math by −4.92%) vs. targeted +0.4% addition of high-quality data (improving performance) provides concrete actionable insight.

## Weaknesses

### Major

- **Only two models compared in the RL phase.** The strongest headline claims — that "pretraining strategy dictates final accuracy" and that the advantage compounds to a "+19% lead on expert-level benchmarks" — are supported by Table 3, which compares only two models (M_base + SFT_SHQ + RL vs. M_LMQ + SFT_SHQ + RL). We do not know how other combinations (e.g., M_LDQ + SFT + RL, M_SHQ + SFT + RL, or models with different SFT data) would perform. This is a significant gap because RL is where the paper's most dramatic claims live.

- **The "catch-up" refutation rests on a narrow test.** The paper claims to refute the hypothesis that SFT can compensate for a weak pretraining foundation (Section 5, Table 4, lines 213-214), but the test only doubles SFT epochs (from 1 to 2) on the same 4.8M-sample dataset. The pretraining gap involves 80B reasoning tokens seen during next-token-prediction; a 2× epoch increase on 4.8M samples is orders of magnitude less additional exposure. A genuine test would involve scaling SFT data quantity, quality, and compute more aggressively. The conclusion may be correct, but the evidence as presented is narrower than claimed.

### Minor

- **"Front-loading" framing is slightly imprecise.** The paper uses "front-loading" to suggest early introduction of reasoning data. However, the training protocol (line 93) introduces reasoning data only in the last 400B of 1T tokens (600B base → 400B with 20% reasoning). The actual experimental contribution is "some reasoning during pretraining (even if introduced late) creates persistent advantages over no reasoning in pretraining." This is still interesting and well-supported, but the paper does not test whether reasoning data should go at the *front* of pretraining versus the *back*. The rhetorical framing overstates what was tested.

- **No uncertainty quantification for fine-grained comparisons.** While the paper reports multiple evaluation runs (16 for AIME, 4 for others at line 148), no standard deviations or confidence intervals are provided. This is consequential for fine-grained distinctions: the 0.4% improvement in Table 8, the 64.09 vs. 64.07 comparison in Table 1, and the +4.25% "latent effect" could all fall within noise. The large-margin results (e.g., 52.70 vs. 64.09) are clearly meaningful, but the precision implied by some claims is unsupported.

- **Diversity/quality confounded with dataset scale.** D_LDQ (268M samples) and D_SHQ (1.2M samples) differ along multiple axes — size, domain composition (71% math vs. 56% math), source, and curation method. Claims about "diversity vs. quality" are conflated with dataset scale. While acknowledged implicitly, this is never systematically disentangled (e.g., by controlling size while varying diversity).

- **Section 4 overclaims the catch-up refutation.** Table 2 (line 183) claims to "strongly refute" the catch-up hypothesis by comparing aggregate M_base+SFT vs. M_res+SFT, but this aggregate includes SFT on D_LDQ which actively degrades performance. The cleaner test is in Table 4 (Section 5), which still supports the finding but less dramatically.

### Trivial

- The optimization framework (Eq. 2 with budget constraint B) is decorative: the budget B is never actually traded off between phases. Pretraining is fixed at 80B tokens and SFT at 4.8M samples.
- The paper does not specify whether the "+19%" figure is absolute or relative (Table 3: 37.92 → 56.66 = +18.74 absolute, +49% relative).

## Nice-to-Haves

- Evaluate more model variants through the RL pipeline to strengthen the central claims.
- Add variance information (at minimum std or confidence intervals) for key comparisons.
- Report n-gram overlap analysis to address potential data contamination concerns with D_SHQ evaluation overlap.
- Strengthen the catch-up test with more aggressive SFT scaling (larger data volumes, varied curricula, more compute-matched comparisons).

## Removed Points

- Harsh critic's claim that the "front-loading" claim is contradicted by the training schedule as a **fatal** issue: This is overstated. The paper's contribution is about introducing reasoning during pretraining vs. deferring it to post-training; the experiment validly tests this question. The term is mildly imprecise but not contradictory to what was actually tested.
- Harsh critic's criticism about missing data contamination analysis and proprietary data limiting reproducibility: These are generic concerns applicable to most large-scale LLM papers and not specific weaknesses of this study.
- Harsh critic's claim that the catch-up test shows "merely that 2× SFT data ≠ 80B pretraining tokens — not a surprising finding": Demoted because the test is still a valid disconfirmation of one reasonable version of the catch-up hypothesis, even if stronger tests would be more convincing.
- Various section-by-section nitpicks about specific phrasings and the Strength Finder's generic/superficial strengths.

## Novel Insights

The paper's most novel observation is the *asymmetric principle*: the same reasoning data properties have opposite effects depending on training phase (diversity matters for PT, quality for SFT). The latent-effect result — where high-quality data in pretraining appears neutral until activated by SFT — is genuinely non-obvious and suggests that evaluations limited to any single training phase may miss important interactions. These findings challenge the common practice of treating data quality as a uniformly desirable property.

## Suggestions

- Run more pretraining backbones through the RL pipeline (at minimum M_LDQ and M_SHQ) to validate whether the compounding advantage generalizes beyond the single M_LMQ vs. M_base comparison.
- Report variances for the key comparative results (Tables 4, 5, and fine-grained distinctions in Table 8).
- Reframe the "front-loading" language and "catch-up refutation" claims to match what was actually tested, or add experiments that directly test within-pretraining timing.
- Include a more thorough catch-up test (e.g., scaling SFT data volume rather than just epochs) to strengthen this central claim.

## Score and Decision

**Calibration anchors used (all rounds):**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| SaOxhcDCM3.md (Self-Consuming Loop) | 3.20 | R1 | Different topic, weak paper |
| mfTM4UdYnC.md (LogicJitter) | 2.50 | R1 | Different topic, weak paper |
| qgLyKwXVDs.md (FreeLM) | 2.00 | R1 | Different topic |
| f7aWmxgSN4.md (Universality in KG Learning) | 3.00 | R1 | Different topic |
| qUJsX3XMBH.md (Rethinking Data Selection) | 4.40 | R1 | Similar genre (empirical SFT study); current paper is clearly stronger in scale and novelty |
| miGpIhquyB.md (Dataset Generation) | 5.50 | R1, R2 | Similar genre; current paper comparable but has larger-scale experiments |
| x83w6yGIWb.md (Calibration Data Pruning) | 5.50 | R1, R2 | Mixed reviews (6,5,8,3); current paper is slightly stronger empirically |
| Nsms7NeU2x.md (Data Contamination) | 6.75 | R1 | Strong empirical+theory paper; current paper slightly weaker due to overclaiming and narrower RL evidence |
| 54KcduuYeG.md (AutoScale) | 5.50 | R2 | Similar genre (data composition); similar quality but current paper has rarer large-scale from-scratch experiments |
| oqsQbn4XfT.md (Diversity of Synthetic Data) | 5.80 | R2 | Similar genre; comparable quality, current paper slightly less methodologically novel |
| FDhAngvHuf.md (Bias of Web-filtered Text) | 5.50 | R2 | Different topic |
| 4xBew7kuYB.md (Training Data Effects on SLMs) | 5.50 | R2 | Different topic |
| jOmk0uS1hl.md (Training on the Test Task) | 8.00 | R1 | Strong paper; current paper clearly below |
| 3bq3jsvcQ1.md (Step Back Prompting) | 8.00 | R1 | Strong paper; different genre |
| f4gF6AIHRy.md (Dimensional Collapse) | 8.00 | R1 | Strong paper with novel method; current paper below |
| mMPMHWOdOy.md (WizardMath) | 8.00 | R1 | Strong paper; different genre |

**Round 1 bracket:** 4.5–6.5  
**Round 2 narrowing:** Closest anchors at 5.50–5.80; current paper is slightly below "Diversity of Synthetic Data" (5.80) due to overclaiming and limited RL evaluation, comparable to "AutoScale" (5.50) and "Calibration Data" (5.50). Above "Rethinking Data Selection" (4.40).

The paper conducts rare and valuable large-scale from-scratch experiments with a well-controlled design. Its core findings (asymmetric principle, latent effects) are interesting and practically useful. However, the paper systematically overstates its claims relative to the evidence: the strongest headline numbers come from a single RL comparison (2 models), the "catch-up" refutation is based on a narrow test, and the "front-loading" framing is imprecise. These issues are significant enough to prevent acceptance at a top venue but do not negate the paper's genuine empirical contributions. The paper would benefit substantially from addressing the RL breadth and claim-calibration issues.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>