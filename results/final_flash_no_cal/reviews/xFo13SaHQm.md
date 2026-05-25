Now I have a thorough understanding of the paper and can critically evaluate each reviewer claim against the actual text. Let me construct the final consolidated review.

## Summary

This paper tackles the "copy-paste artifact" in identity-consistent image generation — where models replicate the reference face rather than preserving identity across natural variations. The authors contribute (1) **MultiID-2M**, a large-scale paired multi-identity dataset (~500k group photos with references + ~1.5M unpaired), (2) **MultiID-Bench**, a benchmark that quantifies the copy-paste trade-off via a new Copy-Paste metric and Sim(GT) as the primary identity metric, and (3) **WithAnyone**, a diffusion model trained with a contrastive identity loss (leveraging extended negatives from the paired dataset) and a ground-truth-aligned ID loss to reduce copy-paste while maintaining identity fidelity. Experiments against 13 baselines on single- and multi-person benchmarks, plus ablations and a user study, demonstrate that WithAnyone substantially reduces copy-paste artifacts while remaining competitive on identity similarity.

## Strengths

1. **Formal definition and quantitative mitigation of the copy-paste artifact.** The paper identifies a specific failure mode in ID-consistent generation and formalizes it via the Copy-Paste metric (Eq. 2). Table 1 and Figure 5 provide concrete quantitative evidence that WithAnyone escapes the trade-off curve binding all other methods: achieving the second-highest Sim(GT) among face customization models (0.460 vs. InstantID's 0.464) while maintaining a substantially lower copy-paste score (0.144 vs. InstantID's 0.337 and PuLID's 0.315). The multi-person results (Table 2) show even clearer advantages.

2. **MultiID-2M dataset enabling non-reconstructive training.** The large-scale paired dataset (~500k identified group photos with multiple references per identity, Section 3) directly addresses the "scarcity of large-scale paired datasets" that previously forced reconstruction-based training. The ablation study (Table 3) confirms its enabling role: removing the paired-tuning phase (Phase 3) degrades copy-paste substantially (CP rises from 0.161 to 0.239), and training on FFHQ alone collapses both identity similarity and variation (Sim(G) 0.224, CP 0.027). The dataset release is a significant community contribution.

3. **Ground-Truth-Aligned ID Loss.** The proposed objective (Eq. 4) uses ground-truth landmarks for ArcFace alignment, avoiding unreliable landmark extraction from noisy generated images. This design (Figure 7) enables identity supervision across all noise levels at negligible overhead, unlike prior methods that restrict ID loss to low-noise timesteps or require full denoising. The ablation (Table 3) shows removing it degrades Sim(GT) from 0.405 to 0.385 and increases CP.

4. **ID Contrastive Loss with Extended Negatives.** The InfoNCE-based loss (Eq. 5) exploits the labeled identities in MultiID-2M to draw thousands of negatives per sample (vs. only 63 batch-level negatives in ablation). The ablation (Table 3, "w/o Ext. Neg.") shows that removing extended negatives causes the model to collapse toward the reference (Sim(R) drops, CP drops anomalously to 0.074) — cleanly demonstrating the value of large-scale negative pools for identity discrimination.

5. **MultiID-Bench as a standardized evaluation framework.** The benchmark replaces Sim(Ref) — which rewards copy-paste — with Sim(GT) as the primary identity metric and introduces the Copy-Paste metric. Evaluating 13 models under this standardized protocol (Tables 1, 2) provides the most systematic comparative analysis of the fidelity-copy-paste trade-off in multi-ID generation to date.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by substantial evidence, and no single issue invalidates its contributions.

### Minor

1. **Claim of "highest face similarity" is not strictly accurate for the single-person setting.**  
   Section 6.1 states WithAnyone achieves "the highest face similarity with regard to GT," yet Table 1 shows InstantID has Sim(GT)=0.464 vs. WithAnyone's 0.460. The differences are small (0.004) and WithinAnyone dominates on CP (0.144 vs. 0.337), so the spirit of the claim is defensible, but a precise phrasing ("competitive identity similarity" or "state-of-the-art among methods supporting multi-ID generation") would be more accurate.

2. **No statistical uncertainty reported for any quantitative metric.**  
   Tables 1, 2, and 3 present only point estimates. Without standard deviations, confidence intervals, or significance tests, it is impossible to assess whether small differences (e.g., Sim(GT) 0.460 vs. 0.464) are meaningful. This is a common gap in generative model evaluation, but it weakens the evidential strength of fine-grained comparisons, particularly in the ablation study where changes are 0.01–0.02. The core CP metric differences are large enough (0.144 vs. 0.337) that the main claims are likely robust, but the paper should still report variance.

3. **User study uses non-obvious placeholder method names without mapping.**  
   Figure 8 labels methods as "Cure, UNO, iDetch, Uniformal, OmniGen." "UNO" and "OmniGen" match baselines from Tables 1/2, but "iDetch," "Uniformal," and "Cure" are not defined in the main text. Readers cannot interpret which methods were compared without this mapping. (The appendix, stripped in this extract, may contain the mapping, but the main text should be self-contained.)

4. **Correlation between the copy-paste metric and human judgment is asserted but not quantified in the main text.**  
   The paper states "the copy-paste metric exhibits a moderate positive correlation with human judgments" (Section 6.3) without reporting the correlation coefficient, confidence interval, or statistical test. This weakens the validation of the proposed metric. (Appendix H presumably contains details, but the main text should provide the core number.)

5. **Thresholds for including cases in Copy-Paste evaluation are not justified.**  
   The CP ranking excludes cases with Sim(GT) ≤ 0.40 (single-person, Table 1) and ≤ 0.35 (multi-person, Table 2). No motivation is given for these thresholds, nor is a sensitivity analysis provided. If different methods pass the threshold at different rates, the average CP scores become incomparable. The paper should report per-method sample sizes and discuss the threshold's effect.

6. **Sim(GT) as primary metric has acknowledged limitations that are not fully analyzed.**  
   The benchmark uses Sim(GT) — ArcFace similarity between the generated image and the ground-truth target image — to penalize copy-paste. However, because prompts are LLM-generated from the GT image, an incomplete caption could cause a good identity-preserving generation that matches the prompt (but differs from the GT image in incidental details) to receive a lower Sim(GT). While ArcFace embeddings are designed for identity-level invariance (mitigating concerns about lighting, expression, etc.), the paper does not analyze how sensitive Sim(GT) rankings are to caption quality or whether results are robust under different captioning strategies. This is a minor concern given that all methods are compared on the same prompts, but it merits discussion.

7. **Multi-phase training pipeline is only partially ablated.**  
   The ablation (Table 3) isolates Phase 3 (paired tuning), the GT-Align loss, the extended negatives, and the dataset source. However, Phases 1, 2, and 4 are not ablated — e.g., it is unclear whether the fixed-prompt reconstruction pre-training (Phase 1) and caption-based reconstruction (Phase 2) are both necessary, or whether a shorter pre-training schedule would suffice. This limits understanding of the training recipe's individual components.

### Trivial

- The paper does not include failure cases or limitation examples in the qualitative results — only successful outputs are shown.
- No computational cost (training time, GPU hours, inference speed) is reported.
- The verification that test identities have "no overlap to training data" (Section 4) is stated but the methodology (e.g., ArcFace similarity threshold check) is not described.

## Nice-to-Haves

- **Analyze sensitivity of the CP threshold.** Show a scatter plot of Sim(GT) vs. CP for all test cases and report per-method sample sizes above the threshold.
- **Add failure case analysis.** Discuss examples where identity similarity is low, copy-paste still occurs, or prompt adherence fails.
- **Report training cost.** GPU hours and inference speed would help practitioners assess the method's practicality.
- **Ablate the multi-phase structure more fully.** E.g., train without Phase 1 (jump directly to caption-based reconstruction) to validate that the fixed-prompt warm-up is necessary.

## Removed Points

*These points were flagged during review but are removed or demoted from the final assessment for the reasons indicated.*

- **Harsh Critic's claim that the "FFHQ only" ablation collapses two factors (dataset scale and paired supervision).** This is not accurate: the "w/o Phase 3" row already isolates the effect of paired supervision within the large dataset, while "FFHQ only" tests a completely different (small) dataset. The two factors are separately identified in the ablation table, so the criticism does not hold.
- **Harsh Critic's suggestion that the user study is "nearly non-interpretable" due to 10 participants.** Ten participants ranking 230 groups across four criteria is a reasonable user-study size for this field; the concern is about opaque labeling, not sample size per se.
- **Several of the harsh critic's "Section-by-Section Notes" are observations rather than actionable weaknesses** (e.g., noting that the four-stage pipeline description is "high-level," that baselines are numerous). These do not constitute concrete flaws.
- **Strength Finder's generic/superficial strengths** such as "the paper addressed an important problem" are removed. Only evidence-grounded strengths are retained.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective or analysis that was not already present in the paper itself. The paper's core insight — that the copy-paste artifact can be formalized and mitigated through paired-data training with contrastive identity loss and GT-aligned ID supervision — stands as stated.

## Suggestions

1. Correct the claim in Section 6.1 from "achieving the highest face similarity with regard to GT" to a more precise statement (e.g., "achieving identity similarity competitive with the state of the art while substantially reducing copy-paste artifacts").
2. Add confidence intervals (bootstrapped) or standard deviations to all quantitative tables.
3. Provide a clear mapping from user-study labels ("Cure," "iDetch," "Uniformal") to actual method names in the caption of Figure 8 or the surrounding text.
4. Report the Spearman/Pearson correlation between the copy-paste metric and human rankings from the user study, ideally with a confidence interval.
5. Justify the CP-evaluation thresholds (0.40/0.35) and include a sensitivity analysis or at least per-method sample sizes.
6. Add a brief discussion of the Sim(GT) metric's limitations and a robustness check (e.g., re-captioning a subset with a different LLM and verifying that rankings persist).
7. Include a failure-case figure showing representative limitations.

## Score and Decision

This paper makes three significant contributions — a large-scale paired dataset, a formalized benchmark with a novel copy-paste metric, and an effective training paradigm — that collectively advance the state of the art in controllable identity-consistent generation. The weaknesses are real but all addressable: they concern precision of claims, completeness of reporting, and methodological transparency rather than fundamental flaws. The core empirical results (especially the large CP reduction at competitive identity similarity) are convincing even without error bars, due to the effect sizes. The open-source release of dataset, benchmark, and model adds substantial community value.

**Score: 7.5**

**Decision: Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>