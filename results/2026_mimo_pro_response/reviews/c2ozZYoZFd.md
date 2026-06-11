Now I have enough data to calibrate. Let me finalize my review.

**Calibration analysis:**

- **"Is Memorization Actually Necessary for Generalization?"** (avg 3.75, rejected): A critique paper finding methodological errors in Feldman & Zhang (2020). Scored 6,3,3,3. Our paper is substantially stronger—more comprehensive (4 lines of evidence vs. 1), more empirical investment (~6000 A100-hours), and has a novel methodological contribution (Best-of-N).

- **"Is Memorization Actually Necessary for Generalization?"** (avg 4.40, rejected, different submission): Same topic, scored 5,5,6,3,3. Rejected for overly strong claims and tightness issues.

- **"Large Language Models Cannot Self-Correct Reasoning Yet"** (avg 6.75, accepted): Critique paper finding prior self-correction claims unsupported. Scored 5,6,8,8. Our paper has stronger empirical backing, better presentation, and a more devastating critique.

- **"One slice is not enough"** (avg 7.33, accepted): Evaluation methodology paper for T2I models. Scored 6,8,8. Comparable in addressing evaluation methodology, but our paper's critique is more targeted and our empirical investment larger.

- **"Training on the Test Task"** (avg 8.00, accepted): Evaluation methodology paper about confounds in LLM benchmarking. Scored 8,8,8,8. Stronger than our paper—more general, paradigm-shifting contribution.

**Round 1 bracket: 6.5–7.5.** Our paper is clearly above the rejected critique papers (~4) and the accepted critique at 6.75, but slightly below the high-scoring evaluation methodology papers at 8.0 due to being more critique-focused than paradigm-shifting.

**Final score: 7.0.** The paper is a strong, well-executed critique with substantial empirical backing (~6000 A100-hours), a novel methodological contribution (Best-of-N), and actionable lessons. Its minor weaknesses (incomplete benchmark re-analysis, vague community adoption critique, no inter-annotator agreement, Best-of-N not formally specified) do not undermine its core claims.

---

## Summary
This paper presents a comprehensive re-analysis of "Turning Up the Heat: MIN-P Sampling for Creative and Coherent LLM Outputs" (Nguyen et al., 2024), an ICLR 2025 Oral paper that introduced min-p sampling. Examining all four lines of evidence from the original paper—human evaluations, NLP benchmarks, LLM-as-a-Judge evaluations, and community adoption claims—the re-analysis finds that none support min-p's claimed superiority. The paper introduces a novel "Best-of-N" methodology for fair hyperparameter comparison, supported by ~6000 A100-hours of compute.

## Strengths
- **Novel "Best-of-N" hyperparameter-volume control methodology**: Section 3.1 introduces a principled subsampling approach (N=1 to 100, 150 repetitions) to equalize hyperparameter tuning volume across methods. This addresses a pervasive problem in ML benchmarking and is demonstrated through a comprehensive sweep across 9 models, 2 stages, 4 samplers, 31 temperatures, and 6 hyperparameters per sampler (Figures 4-5).

- **Thorough statistical re-analysis with appropriate corrections**: Table 1 applies 12 one-sided paired t-tests with Bonferroni correction across all condition combinations, and additionally applies the Intersection-Union Test (max p-value = 0.378). The result—only 1/12 comparisons significant after correction—directly contradicts the original paper's claim of consistent superiority.

- **Substantial independent empirical investment (~6000 A100-hours)**: The authors used the original code to run an extensive sweep (9 models × 2 stages × 4 samplers × 31 temperatures × multiple hyperparameters), providing strong evidence that min-p's advantages vanish under controlled conditions.

- **Documented discovery of omitted data**: Section 2.1 establishes that scores for basic sampling—comprising 1/3 of total collected data—were excluded from the original paper's methodology, analysis, and results without mention or justification, publicly confirmed by the original authors.

- **Identification of selective reporting in LLM-as-a-Judge**: Section 4.3 documents that Table 3(b) reported the higher of two min-p scores (52.01 for p=0.05) but the lower of two top-p scores (50.07 for p=0.9 vs. 50.43 for p=0.98)—a concrete, verifiable instance of inconsistent methodology.

- **Actionable field-level lessons**: Section 6 distills six concrete guidelines (fair hyperparameter comparison, rigorous statistical testing, data transparency, qualitative scrutiny, methodological clarity, consistent reporting), each directly traceable to a specific finding in the case study.

## Weaknesses

### Fatal
None

### Major
None

### Minor

- **GPQA benchmarks not re-analyzed**: The original paper evaluated on both GSM8K and GPQA; the re-analysis only covers GSM8K (acknowledged at line 150: "Due to our compute budget, we only evaluated GSM8K CoT"). This means the benchmark critique is incomplete, affecting one of the paper's four lines of evidence.

- **Vague critique of revised community adoption claim**: Section 5 states the camera-ready "has a different statement of community adoption, which we believe remains misleading" (line 204) but does not specify what the revised claim says or why it is misleading. Given that community adoption is one of the four examined lines of evidence, this lack of specificity weakens the critique.

- **No inter-annotator agreement for qualitative coding**: Section 2.3's manual annotation of human evaluators' qualitative preferences (Figure 2) is a key finding, yet no inter-annotator reliability metric is reported. Since the paper advocates methodological rigor, reporting reliability data (e.g., Cohen's kappa) would strengthen the finding and model the standards it advocates.

- **Best-of-N framework lacks formal specification**: The "Best-of-N" methodology (Section 3.1) is the paper's most novel methodological contribution beyond critique, but it is introduced ad hoc within the min-p analysis rather than as a standalone, formally specified framework. A clearer algorithmic specification and discussion of assumptions would increase its reusability.

- **Table 1 analysis limited to "high diversity" setting**: The justification for focusing on high diversity is reasonable (the authors told them to ignore low diversity; low diversity top-p hyperparameters were poorly chosen), but this limitation should be stated more prominently—the analysis tests consistency within the high diversity setting, not across all settings.

## Nice-to-Haves
- The LLM-as-a-Judge critique (Section 4) would benefit from a Best-of-N style analysis controlling for hyperparameter volume, analogous to the NLP benchmark analysis in Section 3, to make the critique more consistent across sections.
- Adding GPQA re-analysis would complete the benchmark critique.
- Formally specifying the Best-of-N methodology with algorithm pseudocode and applicability guidelines would enhance its value as a standalone contribution.

## Removed Points
These points are flagged to be removed; treat them with caution.

- The harsh critic's point about the Best-of-N framework's generalizability to methods with genuinely different intrinsic hyperparameter counts is valid but speculative. The paper's analysis controls for volume explicitly (6 hyperparameters per sampler, line 133), so this is a generalizability concern beyond the paper's scope. Removed as scope creep.
- The harsh critic's question about whether Table 1 uses camera-ready or original submission data is a precision nitpick. The paper says "the authors' published data" (line 56) and the visual/analytical conclusion (Fig. 1) is the same regardless. Removed as trivial.

## Novel Insights
The paper's most genuinely novel contribution is the "Best-of-N" subsampling methodology for fair hyperparameter comparison, which provides a reusable framework for the broader ML community. Beyond that, the case study's documentation of how four independent lines of evidence in a high-visibility publication can all be flawed—and how these flaws propagated through the review process (3 of 4 reviewers citing retracted adoption numbers)—provides a uniquely comprehensive illustration of systemic review failures.

## Suggestions
- Formally specify the Best-of-N methodology as a standalone contribution with algorithm pseudocode, assumptions discussion, and applicability guidelines.
- Add the GPQA re-analysis to complete the benchmark critique, or explicitly frame the benchmark contribution as partial.
- Specify what the revised community adoption claim says in the camera-ready and explain why it remains misleading.
- Report inter-annotator agreement for the qualitative coding.

## Calibration Report

**All retrieved anchors across rounds:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Is Memorization Necessary? | lf8QQ2KMgv | 3.75 | R1 | Weaker critique, rejected; our paper is more comprehensive |
| Is Memorization Necessary? | GbEmJmnQCz | 4.40 | R1 | Same topic, rejected; our paper has stronger evidence |
| Critique Ability of LLMs | 50P9TDPEsh | 4.67 | R1 | Different topic (critique ability), rejected |
| Do Think Tags Help LLMs Plan? | 85Ik12q2hP | 4.00 | R1 | Critical evaluation, rejected; our paper is more rigorous |
| Reevaluating Theoretical Analysis | JslyktsKMY | 5.75 | R1 | Re-evaluation paper, rejected; our paper has stronger empirical backing |
| (Mis)Fitting Scaling Laws | xI71dsS3o4 | 5.75 | R1 | Survey/re-analysis, accepted; our paper is more focused and impactful |
| Re-Reading Improves Reasoning | 3jXCF5dNpC | 6.00 | R1 | Different topic, rejected |
| Class-wise Autoencoders | RW37MMrNAi | 5.60 | R1 | Different topic |
| LLMs Cannot Self-Correct | IkmD3fKBPQ | 6.75 | R2 | Critique paper, accepted; our paper is more comprehensive and rigorous |
| One slice is not enough | Im2neAMlre | 7.33 | R2 | Evaluation methodology, accepted; comparable rigor |
| Strong Model Collapse | et5l9qPUhm | 8.00 | R1 | Strong theoretical contribution; not directly comparable |
| LLM-SR | m2nmp8P5in | 8.00 | R1 | Different topic |
| Training on the Test Task | jOmk0uS1hl | 8.00 | R1 | Evaluation methodology; stronger paradigm-shifting contribution |
| Retrieval Head | EytBpUGB1Z | 8.00 | R1 | Different topic |
| Never Train from Scratch | PdaPky8MUn | 8.00 | R1 | Fair comparison methodology; comparable topic, stronger general contribution |
| Realistic Evaluation of SSL | RvUVMjfp8i | 8.00 | R1 | Different topic |
| Online GNN Evaluation | KbetDM33YG | 8.00 | R1 | Different topic |
| On Evaluating Safeguards | fXJCqdUSVG | 6.50 | R2 | Critique of evaluation, accepted; our paper is more rigorous |
| PRIME | QrEHs9w5UF | 6.25 | R2 | Different topic |
| Knowledge Localization | tfyHbvFZ0K | 7.50 | R2 | Re-examination paper, accepted |
| SMC for LLMs | xoXn62FzD0 | 8.00 | R2 | Different topic |
| Proving Test Set Contamination | KS8mIvetg2 | 7.50 | R2 | Evaluation integrity, accepted |
| Discrete Diffusion | 71mqtQdKB9 | 6.60 | R2 | Different topic |
| Bridging Data Provenance | G5DziesYxL | 6.50 | R2 | Data transparency, accepted |
| MetaCLIP | 5BCFlnfE1g | 6.75 | R2 | Different topic |
| Domain constraints | 1mNFsbvo2P | 7.25 | R2 | Different topic |

**Round 1 bracket: 6.5–7.5.** Our paper is clearly above the rejected critique papers (~4) and the accepted critique at 6.75 (which had presentation issues), but slightly below the high-scoring evaluation methodology papers at 8.0 due to being critique-focused rather than paradigm-shifting.

**Final score: 7.0.** The paper sits at the midpoint of the bracket. It is stronger than "LLMs Cannot Self-Correct" (6.75) due to more comprehensive evidence, better presentation, and a novel methodological contribution. It is comparable to "One slice is not enough" (7.33) in addressing evaluation methodology. It is slightly below "Training on the Test Task" (8.00) and "Never Train from Scratch" (8.00), which offer more general, forward-looking methodological contributions.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>