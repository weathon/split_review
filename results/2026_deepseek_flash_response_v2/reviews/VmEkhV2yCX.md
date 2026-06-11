Now I have all the information I need. Let me compile the final review.

## Summary

This paper conducts controlled pretraining experiments from scratch (8B-parameter models on 1T tokens) to study how reasoning data should be allocated across the LLM training pipeline. It trains four base models varying reasoning data properties (none, small high-quality, large diverse, large mixed-quality) and evaluates them at pretraining, SFT, and RL stages. The key findings are: (1) an **asymmetric principle** where diversity drives pretraining gains while quality drives SFT gains, (2) **latent effects** of high-quality pretraining data activated only after SFT, and (3) **harmful effects** of naively scaling mixed-quality SFT data.

## Strengths

1. **Asymmetric principle (diversity in PT, quality in SFT) is well-supported by a clean crossed design.** Tables 1 and 5 show that with identical token budgets, diversity drives pretraining gains ($\mathcal{M}_{\text{LDQ}}$ at 64.09 vs $\mathcal{M}_{\text{SHQ}}$ at 54.98, a +9.09 point gap) while quality drives SFT gains ($\mathcal{M}_{\text{res}} + \text{SFT}_{\text{SHQ}}$ at 44.99 vs $\mathcal{M}_{\text{res}} + \text{SFT}_{\text{LDQ}}$ at 31.54, a +13.45 point gap). Because the same three datasets are used in both phases, this comparison cleanly isolates the phase-dependent effect of diversity versus quality, ruling out the confound of different data sources.

2. **Latent effect of high-quality pretraining data discovered via post-SFT emergence.** $\mathcal{M}_{\text{LMQ}}$ and $\mathcal{M}_{\text{LDQ}}$ score nearly identically at pretraining (64.07 vs 64.09), but after SFT on the same recipe, $\mathcal{M}_{\text{LMQ}}$ achieves an additional +4.25% gain over $\mathcal{M}_{\text{LDQ}}$ (Table 4). This non-obvious finding — high-quality data in pretraining shows no immediate benefit yet creates latent capability — is supported by a controlled comparison where all other training variables are held fixed.

3. **Evidence that naive SFT scaling actively harms math reasoning.** Table 8 shows that doubling mixed-quality SFT data yields a 4.92% absolute drop in math accuracy (28.38→23.46) with negligible average gain, while a marginal 0.4% addition of high-quality data improves performance. This is actionable negative evidence for SFT data strategy.

4. **Compounding advantage tracked across three training stages.** The gap between $\mathcal{M}_{\text{base}}$ and reasoning-pretrained models grows from +8.35% at pretraining (Table 1) to +9.3% after SFT (Table 2) to +18.74% after RL (Table 3). On AIME24/25, the gap reaches 32.92 and 17.92 absolute points respectively (Table 3). Three-stage tracking provides stronger evidence than a single evaluation snapshot.

5. **Ecologically valid experimental scale.** Training 8B models from scratch for 1T tokens (512 H100 GPUs) is substantially more realistic than the fine-tuning-only studies that dominate this space, increasing confidence that findings apply to real-world training pipelines.

## Weaknesses

### Major

1. **The "SFT cannot catch up" claim is weakened by a confound with total reasoning data quantity.** The paper claims that SFT cannot compensate for a missing pretraining foundation (the "catch-up" hypothesis). To test this, the catch-up experiment (Table 4) doubles SFT epochs for $\mathcal{M}_{\text{base}}$ (from 4.8M to 9.6M sample exposures) and shows it still cannot match $\mathcal{M}_{\text{SHQ}} + \text{SFT}_{\text{SHQ}}$. However, the reasoning-pretrained models received **80B tokens of reasoning data in pretraining** plus 4.8M SFT samples — roughly an order of magnitude more total reasoning exposure than $\mathcal{M}_{\text{base}}$'s 9.6M SFT sample exposures. The experiment tests whether *slightly more SFT* helps, not whether a comparable reasoning data budget allocated entirely to SFT could match pretraining exposure. A proper test would need conditions such as (0B PT + 80B SFT) vs (80B PT + 0B SFT). The claim that "SFT cannot compensate" is therefore overconfident relative to the evidence presented. **Importantly, this issue does not affect the asymmetric principle or the latent effects findings**, which rely on comparisons within the reasoning-pretrained group where total token budgets are controlled.

### Minor

2. **Percentage reporting is ambiguous throughout.** The abstract and introduction report absolute differences as "X%" without specifying that these are absolute percentage-point differences (e.g., "19% average gain" from Table 3 corresponds to 56.66−37.92=18.74 absolute points, which would be 49.4% relative improvement). The "11% average gain" for diversity (abstract) does not cleanly match any single comparison in the tables — it could be $\mathcal{M}_{\text{LDQ}}$−$\mathcal{M}_{\text{base}}$=64.09−52.70=11.39 (absolute points), but this conflates "adding reasoning data" with "diversity." The paper should consistently report and label absolute percentage points as such.

3. **No variance or significance estimates.** Every experiment trains a single model per condition. While understandable given the computational expense of pretraining from scratch, the absence of uncertainty quantification is a limitation, especially for small-margin claims (e.g., the 4.25% latent effect, or $\mathcal{M}_{\text{LDQ}}$ at 64.09 vs $\mathcal{M}_{\text{LMQ}}$ at 64.07 in Table 1). This should be explicitly acknowledged.

4. **Single architecture at a single scale.** Experiments use one hybrid Mamba2+Transformer architecture at 8B parameters. The paper mentions a 1.2B experiment (Table 14, appendix) but does not discuss whether findings transfer to standard transformer architectures or other scales in the main text, limiting generalizability claims.

5. **No discussion of potential benchmark contamination.** Evaluation benchmarks (GSM8K, MATH-500) cover domains that overlap with training datasets ($\mathcal{D}_{\text{LDQ}}$ contains 56% math, $\mathcal{D}_{\text{SHQ}}$ contains 71% math). The paper does not discuss whether any deduplication or filtering was performed to prevent overlap between training data and evaluation sets.

### Trivial

6. The paper should clarify that "constant budget of 80B reasoning tokens across all experiments" (Section 2.3) refers only to the three reasoning-pretrained models, not the full experimental design including $\mathcal{M}_{\text{base}}$.

## Nice-to-Haves
- A properly budget-controlled catch-up experiment (matching total reasoning tokens between PT-heavy and SFT-heavy allocations) would significantly strengthen the central claim.
- Reporting absolute percentage points vs. relative improvements consistently throughout.
- A brief discussion of potential data contamination mitigation.

## Removed Points
The following points from the input reviews were filtered out:
- **Criticism about Equation 2's budget constraint being "never implemented"**: The paper presents Equation 2 as a formalization of the research question, not an experimental protocol. The valid concern about the catch-up experiment's confound is retained in Major #1 above.
- **Missing overfitting analysis**: The paper references Appendix B for this analysis, which was stripped by the parser; the analysis exists in the original submission.
- **Criticism that the paper's "central claim is not supported"**: This overstates the issue. The catch-up claim is weakened, but the asymmetric principle and latent effects findings are independently supported.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions
- **Reframe the catch-up claim** to accurately reflect the evidence: the catch-up experiment shows that *doubling SFT epochs* cannot close the gap, which is weaker than "SFT cannot compensate." The paper's strongest and most novel contributions (asymmetric principle, latent effects, harmful naive SFT scaling) do not depend on a definitive catch-up proof and would benefit from a more precise framing.
- **Clarify all percentage reporting** as absolute percentage points vs. relative improvements.
- **Add explicit discussion** of single-run variance limitations and potential benchmark contamination.

---

Now let me proceed with calibration.

**Round 1 bracket:** Based on the calibration search, I identified a plausible bracket of **5.0–6.5**. The paper is clearly stronger than papers at scores 2–3 (narrow scope, weak methodology) and clearly weaker than papers at scores 7.5–8.0 (flawless execution, no major confounds). The most comparable anchors sit in the 5.25–6.75 range.

**Round 2 narrowing:** I read the full reviews of six anchor papers in the 5.25–6.75 range. The paper under review is:
- **Stronger than** "Scaling Relationship on Learning Mathematical Reasoning" (5.25): that paper had very narrow evaluation (only GSM8K), limited novelty, and questionable loss comparisons. Our paper has broader evaluation, more novel findings, and cleaner experiments.
- **Comparable to** "Advancing Mathematical Reasoning in Language Models" (5.71): both papers compare PT vs SFT for reasoning and have real contributions but also notable flaws. Our paper has better-controlled comparisons (from-scratch PT vs. CPT) but shares similar weaknesses around single architecture and limited variance estimation.
- **Comparable to** "Dissecting learning and forgetting in LM finetuning" (5.75): that paper had a well-executed analysis but limited novelty of findings. Our paper has more surprising/novel findings but a more significant weakness in one claim.
- **Slightly weaker than** "Knowledge Manipulation in Language Models" (6.50) and "What Kind of Pretraining Data Do LLMs Rely on When Doing Reasoning?" (6.75): those papers have cleaner execution with no major confounds in their central claims, despite narrower scope. Our paper's confound in the catch-up claim prevents it from reaching this tier.

**Final score:** 5.5. This reflects the paper's genuinely novel contributions (asymmetric principle, latent effects) and impressive experimental scale, tempered by the significant confound in the headline catch-up claim and several minor issues. The paper is a solid contribution that should prompt useful discussion, but the central "front-loading" claim needs stronger evidence.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>