Now I have a thorough understanding of the paper. Let me carefully filter the reviewer inputs and construct the final review.

---

## Summary

This paper conducts a large-scale empirical study (8B model trained from scratch for 1T tokens) investigating when and how reasoning data should be injected across the LLM training pipeline — pretraining, supervised fine-tuning (SFT), and reinforcement learning (RL). The central finding is that "front-loading" reasoning data into pretraining creates a durable advantage (≈19% absolute gain after RL) that SFT alone cannot recover. Secondary findings include an asymmetric allocation principle (diversity matters in pretraining, quality matters in SFT), evidence that naive SFT scaling with mixed-quality data is harmful, and a "latent effect" where high-quality pretraining data shows value only after SFT.

## Strengths

1. **Large-scale, systematic comparison of reasoning data across training stages.** The fully crossed design — four pretraining variants (none, D_LDQ, D_SHQ, D_LMQ) × multiple SFT recipes — goes well beyond prior work that studies stages in isolation. Maintaining a constant 80B reasoning token budget across all conditions (via repetition of smaller datasets) is a careful control that cleanly attributes effects to data characteristics rather than volume. (Section 2.3, Tables 1–5)

2. **Core claim is robustly supported: pretraining with reasoning data creates a compounding advantage that widens through post-training.** After the full pipeline (Table 3), ℳ_LMQ + SFT_SHQ + RL achieves 56.66% vs. 37.92% for ℳ_base + SFT_SHQ + RL (+18.74 points average; +39.32 points on AIME). Table 2 shows that averaging across SFT recipes, reasoning-pretrained models (ℳ_res) outperform ℳ_base by 9.3% after SFT. The gap is consistent across pretraining → SFT → RL, directly refuting the concern that early reasoning injection causes overfitting or diminishes later gains.

3. **Demonstration that naive SFT scaling with mixed-quality data is actively harmful.** Table 8 shows that doubling the volume of D_LDQ in SFT yields no average improvement and degrades math (−4.92%), while adding a small fraction (0.4%) of high-quality long-CoT data (D_ALF') produces consistent gains. This provides a concrete, actionable caution against "more is better" in SFT.

4. **Comprehensive evaluation across diverse reasoning domains.** Models are assessed on math (GSM8K, MATH-500, AIME24/25), science (MMLU, MMLU-Pro, GPQA), code (LiveCodeBench, HumanEval, MBPP), and instruction following (IFEval), with RL verification for the most critical comparisons. This breadth strengthens the generalizability of the findings.

5. **RL validation confirms that pretraining advantages persist and compound.** The paper does not stop at SFT but extends key comparisons through GRPO (Table 3), showing that the gap between reasoning-pretrained and baseline models grows rather than shrinks. This substantially increases the practical relevance of the conclusions.

## Weaknesses

### Major

1. **The "latent effect" claim (Section 5, Table 4) is confounded by data overlap and cannot be interpreted as presented.** ℳ_LMQ was pretrained on D_LMQ = D_LDQ ∪ D_SHQ; ℳ_LDQ was pretrained on D_LDQ only. Both are then SFTed on D_SHQ. The paper attributes ℳ_LMQ's +4.25% post-SFT advantage over ℳ_LDQ to a "latent" quality effect that is "unlocked" by SFT. However, ℳ_LMQ has already been exposed to the exact D_SHQ data points during pretraining (repeated to meet the 80B token budget), while ℳ_LDQ sees D_SHQ for the first time during SFT. The post-SFT gap could therefore reflect straightforward additional exposure to those specific examples rather than any latent quality-dependent mechanism. The paper does not acknowledge or attempt to control for this confound. A proper test would withhold D_SHQ from pretraining entirely, or compare models with matched pretraining exposure to the SFT data distribution.

2. **The "catch-up" refutation is based on a single, weak intervention, but is stated as a general impossibility.** The paper tests the catch-up hypothesis by doubling SFT epochs for ℳ_base on D_SHQ (Table 4). When this 2× intervention still falls short of ℳ_SHQ + SFT_SHQ, the paper concludes that "pretraining instills a foundational reasoning capability that cannot be fully replicated by simply scaling the SFT phase" (Section 5) and the abstract claims "establishing foundational capabilities that cannot be fully replicated by later-stage SFT, even with more data." The evidence supports the weaker claim that *doubling SFT epochs on one dataset is insufficient* — not that no amount or variety of SFT could ever compensate. More aggressive scaling (higher-quality SFT data, larger SFT datasets, multi-epoch training with curriculum) might close the gap. The conclusion is broader than the experiment supports.

3. **The asymmetric principle (diversity in pretraining, quality in SFT) is confounded by domain composition.** D_LDQ (56% math, 27% science, 17% code) and D_SHQ (71% math, 21% code, 8% science) differ not just in diversity/quality but in domain proportions, dataset size (268M vs. 1.2M samples), and response format. The claim that "diversity drives pretraining" is supported by ℳ_LDQ > ℳ_SHQ in pretraining, but this advantage could partly reflect D_LDQ's broader science and code coverage — domains on which the evaluation also measures performance. Similarly, the claim that "quality governs SFT" (Table 5: ℳ_res + SFT_SHQ >> ℳ_res + SFT_LDQ) could partly reflect D_SHQ's heavier math focus in evaluations that heavily weight math benchmarks. The paper would be strengthened by reporting domain-specific scores and explicitly discussing whether the pattern holds when domain coverage is controlled.

4. **No variance or uncertainty reporting.** All reported numbers are point estimates without confidence intervals, standard deviations, or significance tests. For benchmarks where the paper averages 16 runs (AIME) or 4 runs (MATH-500, GSM8K, etc.), standard errors could be reported. For single-pass evaluations, the stability of results is unclear. This is especially problematic for small-gap comparisons (e.g., Table 1: ℳ_LDQ 64.09 vs. ℳ_LMQ 64.07; Table 7: 50.95 vs. 52.63), where the reader cannot assess whether observed differences reflect genuine effects or evaluation noise.

### Minor

1. **SFT data sampling procedure is unspecified.** Section 3.1 states that each model is "finetuned on 4.8M reasoning samples from D_res." For datasets larger than 4.8M (D_LDQ has 268M samples, D_LMQ has 269.2M), the sampling procedure (random? stratified by domain? deterministic?) is not documented. This affects reproducibility and could introduce uncontrolled variability across SFT runs.

2. **D_ALF' construction is under-specified.** Table 8 and the surrounding text refer to "scaling D_ALF with high-quality D_SHQ (D_ALF')" and note "a marginal increase in dataset size (0.4% more samples)." The mixing ratio, whether this is a union or weighted combination, and the resulting dataset size are not clearly stated. The 0.4% figure requires clarification (0.4% relative to what baseline?).

3. **Catch-up test uses only one SFT data source.** The doubling experiment uses only D_SHQ. Since D_SHQ is heavily math-focused, it is not clear whether the result generalizes to SFT on more diverse or code-heavy data. A test with D_LDQ or D_LMQ as the SFT corpus would strengthen the claim.

4. **The "19% average gain" in the abstract is ambiguous.** It is stated without clarifying whether this is in absolute percentage points (it appears to be: 56.66 − 37.92 = 18.74 ≈ 19%) or relative improvement. The paper should be explicit.

### Trivial

- Table 2 averages over three SFT recipes; the full breakdown is in the (stripped) appendix. Referencing this explicitly in the main text would help readers who cannot see the appendix.
- The paper describes the RL data (Nemotron-Crossthink) but does not report its size or composition.

## Nice-to-Haves

- A wider range of reasoning ratios in the downstream SFT analysis (Table 7 only tests 80/20 vs. 60/40).
- Reporting the instruction-following (IFEval) breakdown within individual models rather than only as averages, to better characterize the breadth-alignment trade-off.
- An explicit statement of how many SFT epochs are used. (The paper says "4.8M reasoning samples" and the catch-up test refers to "2× epochs," implying one epoch is standard, but this is never stated.)

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **Concern about the "first systematic study" claim (Harsh Critic).** The paper acknowledges prior mid-training work in Section 6 and clearly distinguishes its contribution. The claim of "first" refers to the joint manipulation across *both* pretraining and SFT at this scale, which is defensible.
- **"Only two ratios tested for downstream effect" framed as a weakness.** This is descriptive of what the paper chose to test; a wider sweep would strengthen the analysis but the absence is not a flaw. Moved to Nice-to-Haves.
- **Criticism about missing appendix / missing proofs / missing references.** These are stripped by the parser and exist in the original submission.
- **Claim that D_LDQ "contains" D_SHQ.** This is incorrect — D_LDQ and D_SHQ are distinct datasets from different sources. D_LMQ is the union of D_LDQ and D_SHQ. The paper is clear on this.

## Novel Insights

Beyond the paper's own contributions, the most novel cross-cutting insight from the reviews is that the **experimental design reveals a structural tension**: the datasets used to operationalize "diversity" (D_LDQ) and "quality" (D_SHQ) differ on multiple correlated axes (domain composition, dataset size, response format, source quality). This means the paper's central dichotomies — diversity vs. quality, quantity vs. curation — are not fully disentangled. A follow-up could construct datasets that vary diversity and quality orthogonally (e.g., a diverse high-quality dataset, or a narrow low-quality one) to isolate the causal factors. The review process surfaces that the paper's conclusions are stronger than the confound-control allows, but the core direction of each finding remains plausible and worth investigating further.

## Suggestions

1. **Address the data overlap confound for the latent effect claim.** Either (a) run a controlled experiment where D_SHQ is withheld from pretraining entirely, or (b) explicitly qualify the latent effect claim by acknowledging the confound and reframing the result as "models that see high-quality data during pretraining benefit more from subsequent SFT on that same data — whether this is a latent quality effect or a data repetition effect cannot be determined from the current design."

2. **Temper the catch-up conclusion to match the evidence.** Replace "SFT cannot compensate for a weak foundation" with "2× SFT on high-quality data cannot close the gap opened by pretraining with reasoning data; whether more aggressive SFT interventions could do so remains an open question."

3. **Discuss domain confounds explicitly when making the asymmetric principle claim.** Show domain-specific scores and note that the diversity/quality distinction is partially entangled with domain coverage.

4. **Add standard errors or confidence intervals** for all main results, especially for small-gap comparisons. Even bootstrap estimates from the reported multi-run evaluations would substantially improve interpretability.

5. **Clarify methodological details:** (a) how the 4.8M SFT samples are selected from larger datasets, (b) the construction and mix ratio of D_ALF', (c) the number of SFT epochs used for standard runs.

## Score and Decision

This paper makes a genuine contribution with a large-scale, systematic investigation of reasoning data placement across the LLM training pipeline. The primary finding — that front-loading reasoning into pretraining creates a durable advantage that SFT alone cannot replicate — is well-supported by multiple consistent comparisons (Tables 1–4) and validated through RL (Table 3). The finding about harmful naive SFT scaling (Table 8) is also clean and actionable.

However, several secondary claims are weakened by confounds and overclaiming. The "latent effect" is confounded with data repetition. The "catch-up" refutation rests on a single intervention. The asymmetric principle is partially entangled with domain composition. And the absence of any variance reporting makes it impossible to assess the reliability of fine-grained comparisons.

These are significant weaknesses in the paper's supporting arguments, but they do not invalidate the core contribution. The paper would be substantially improved by recalibrating the claims, acknowledging the confounds transparently, and reporting error bars. In its current form, the conclusions outrun the evidence on several fronts, but the experimental effort and the primary result are valuable enough to warrant publication.

**Score:** 6.5  
**Decision:** Accept (weak-to-moderate accept, contingent on addressing the major concerns in a rebuttal)

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>