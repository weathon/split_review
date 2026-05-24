Now I have a solid understanding of the paper and the calibration anchors. Let me synthesize the final review.

**Round 1 Bracket:** Based on the calibration search, the most comparable papers (critique/meta-analysis papers) score between 4.0 (the memorization re-analysis, Rejected) and 6.5 (the micro-benchmarking reliability paper, Accept Oral). The SITE benchmarking critique scored 6.0 (Accept Poster). The min-p paper is clearly stronger than the memorization re-analysis (4.0) which had significant weaknesses (no code release, incomplete analysis). It is comparable to the micro-benchmarking paper (6.50) and somewhat stronger than the SITE paper (6.00). My initial bracket is **(5.5, 7.5)**.

**Round 2 Narrowing:** The most informative anchors inside this bracket are the SITE paper (6.00, Accept Poster) and the micro-benchmarking paper (6.50, Accept Oral). The min-p paper compares favorably to both: it has more extensive experiments, a more impactful finding (debunks a high-profile ICLR Oral), and clearer actionable lessons. However, it has two weaknesses (selective reporting claim not fully substantiated; NLP scope limited to GSM8K) that the micro-benchmarking paper does not share to the same degree. The final score is **6.5**.

---

## Summary

This paper is a post-publication re-analysis of a high-profile ICLR 2025 Oral paper on min-p sampling (Nguyen et al., 2024). It examines four lines of evidence from the original paper — human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community-adoption claims — and argues that each fails to support the claimed superiority of min-p sampling. The re-analysis is methodologically careful: it uses correct statistical testing with Bonferroni correction, develops a "Best-of-N" methodology to control for hyperparameter tuning volume, documents omitted data, and traces retracted community-adoption claims. From the case study, the paper derives six general lessons for rigorous empirical ML research.

## Strengths

- **Correct statistical re-analysis of human evaluations invalidates the original paper's central claim.** The paper re-runs the original human evaluation data with appropriate one-sided paired t-tests and Bonferroni correction for 12 comparisons. After correction, only 1 of 12 comparisons is significant at α=0.05, and none at α=0.01 — fully overturning the original claim that min-p "consistently" outperforms baselines across all settings. The visualization with confidence intervals (Fig. 1) makes this immediately clear.

- **The "Best-of-N" hyperparameter sweep methodology is a genuine methodological contribution.** The paper controls for hyperparameter volume by subsampling equal numbers of configurations per sampler and tracking the maximum achievable performance (Figs. 4 and 5). This is an effective tool for detecting cherry-picking and could be adopted broadly. The experiment is extensive: 9 models × 2 stages × 4 samplers × 31 temperatures × 6 hyperparameters × 3 seeds, requiring ~6000 A100-hours.

- **Data omission is clearly documented and shown to change conclusions.** The discovery that scores for one of two baseline samplers (basic sampling) were excluded without justification — comprising 1/3 of all collected data — is a clean finding. The paper shows that including these data changes the evidentiary picture, and that the camera-ready version added the table but did not update methodology or conclusions.

- **Community-adoption claims are debunked with concrete evidence.** The paper checks GitHub star counts of major LM repositories and finds the total (<453k) is less than half the claimed 1.1M stars. The retraction of these claims in the camera-ready version is documented, and the paper notes that 3 of 4 reviewers cited these numbers as justification for strong endorsement — an important meta-point about how unverified claims can influence peer review.

- **The derived lessons are well-grounded.** The paper's six lessons (control hyperparameter volume, apply correct statistics, practice data transparency, scrutinize qualitative summaries, ensure methodological clarity, watch for selective reporting) are not novel in isolation, but the concrete case study gives them weight and makes them actionable.

## Weaknesses

### Major

1. **The selective-reporting accusation (Section 4.3) is insufficiently substantiated.** The paper states that the first author shared a Telegram link showing the higher of two scores was reported for min-p and the lower for top-p, but it does not reproduce the Telegram content, provide a screenshot, or quote the messages. The accusation of intentional cherry-picking is the most serious claim in the paper, and it rests on evidence the reader cannot verify. The paper would be better served by softening the claim to "inconsistency that warrants investigation" or by including the Telegram evidence directly (e.g., in the appendix). This weakness is notable given the paper's own emphasis on transparency and reproducibility.

2. **The NLP benchmark re-analysis is limited to a single task (GSM8K), yet the paper draws broad conclusions.** The original paper claimed "superior performance across benchmarks" using both GSM8K and GPQA. The current paper acknowledges it "only evaluated GSM8K CoT" due to compute budget, but the abstract and framing repeatedly state that "min-p's claimed superiority vanishes when controlling for hyperparameter tuning" without the qualifier "on GSM8K." The conclusion about NLP benchmarks is therefore narrower than the paper's language suggests. This does not undermine the human evaluation or community-adoption findings, but it is an overreach in the NLP domain.

### Minor

1. **The 7.80 vs. 5.80 discrepancy is noted but not explained.** The paper reports that one value in Table 15 of the original paper appears incorrect (7.80 should be 5.80 based on publicly posted data) but does not explain how the discrepancy might have arisen or attempt to verify it beyond stating it as a belief. A brief verification step would strengthen this claim.

2. **The "Best-of-N" analysis inherently disadvantages basic sampling.** Since basic sampling has only temperature as a tunable parameter, it is naturally swept less extensively than other samplers (which also have k or p). The paper acknowledges this but does not discuss whether a fairer comparison (e.g., sweeping temperature more finely for basic) would alter the results. This is a minor concern because the main finding — min-p does not outperform — still holds even controlling for this asymmetry.

3. **The paper's framing occasionally conflates "the original paper did not provide sufficient evidence" with "the original paper was wrong."** While the data do show the original claims were unsupported, the paper's strongest claims ("min-p does not outperform," "min-p's superiority vanishes") would benefit from the same precision it demands of others, e.g., "the evidence does not support the original claim of superiority."

### Trivial

None.

## Nice-to-Haves

- A GPQA evaluation at reduced scale (2–3 models, fewer hyperparameters) would substantially strengthen the NLP section, even if not as extensive as the GSM8K sweep.
- The Telegram evidence, if reproduced in an appendix, would make the selective-reporting claim bulletproof.
- Providing confidence intervals or bootstrapped uncertainty estimates for the GSM8K results would further strengthen the analysis.

## Removed Points

- The harsh critic's point about the 7.80 vs. 5.80 discrepancy reading "as an assertion" — the paper frames it as "we believe," which is appropriately cautious for a claim about a discrepancy in another paper's data. Not a weakness.
- Cleaned formatting/style nitpicks about presentation per the removal rules.
- The strength finder's claim about selective reporting being "direct evidence" — this is overstated; it's an allegation without reproduced evidence, so I have moved it from core strengths to a weakness.
- The harsh critic's suggestion of a "placebo test" for hyperparameter-sweep analysis and the request for a 7th lesson — these are nice-to-haves, not weaknesses.

## Novel Insights

Beyond the paper's own contributions, one genuinely novel insight emerges from the intersection of findings: the debunked community-adoption numbers were cited by 3 of 4 reviewers and the Area Chair as justification for strong endorsement. This creates a troubling feedback loop where unverified external-validation claims (GitHub stars, adoption counts) influence peer review, which then amplifies the paper's visibility. The paper documents this loop but does not explicitly name it as a phenomenon; recognizing it as a systemic risk factor in ML peer review would be a useful extension.

## Suggestions

1. Reproduce the Telegram evidence in the appendix (screenshot or quoted data) and reframe the selective-reporting claim as "inconsistent reporting that warrants investigation" rather than presenting it as established fact.
2. Qualify the NLP conclusions in the abstract and discussion to reflect that the re-analysis covers only GSM8K (not GPQA).
3. Add a brief verification of the 7.80/5.80 discrepancy (e.g., "the mean of the relevant column in the posted data is 5.80, confirmed by [specific calculation]").
4. Consider addressing the inherent disadvantage of basic sampling in the Best-of-N analysis with a brief discussion or a supplementary experiment with finer-grained temperature sweeps for basic.

## Score and Decision

**Calibration Anchors** (all rounds):

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| eAVPivm2jv (Memorization critique) | 4.00 | R1 | Weaker: rejected, had incomplete experiments and no code release |
| FRp8cu1aKF (Feature Selection critique) | 4.67 | R1 | Weaker: rejected, split review (2,2,10), narrower scope |
| ZHKVPkJMSI (SITE benchmark critique) | 6.00 | R1/R2 | Comparable but slightly weaker: similar critique genre but less extensive experiments |
| cReExMQLiK (Micro-benchmarking reliability) | 6.50 | R2 | Comparable: similar quality of analysis and impact; this paper is slightly stronger in impact (debunks a high-profile paper) but weaker in the substantiation of one claim |

**Round 1 bracket:** (5.5, 7.5)  
**Round 2 narrowing:** Compared against the SITE paper (6.00) and micro-benchmarking paper (6.50), the min-p paper is slightly stronger than the former and comparable to the latter, warranting **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>