## Summary

This paper proposes that scientific LLMs (Sci-LLMs) perform better when given high-level structured context from bioinformatics tools (Pfam, BLAST, InterProScan) than when given raw protein sequences, and that adding the raw sequence alongside this context *degrades* performance ("informational noise"). Through a systematic comparison of 6 models across 3 input modes on protein QA benchmarks (function, pathway, subcellular localization), the authors find context-only outperforms both sequence-only and sequence+context configurations. The paper contributes a reframing of Sci-LLMs as reasoning engines over expert knowledge rather than sequence interpreters, supported by embedding analyses, temporal generalization studies, efficiency comparisons, and wet-lab validation.

## Strengths

- **Systematic ablation showing raw sequence harms performance (Table 1).** Across all six models, Context-Only consistently outperforms both Sequence-Only and Sequence+Context. The degradation pattern (e.g., Intern-S1: 86.15→84.03, Evolla: 74.02→70.53) is a genuinely counter-intuitive finding that warrants attention, regardless of whether the context is answer-relevant. This is the paper's strongest empirical contribution.

- **Layer-wise trace pinpoints alignment as the bottleneck (Figure 3).** By tracking ARI through Evolla's pipeline (SaProt encoder 0.945 → Q-Former 0.916 → LLM decoder 0.809), the paper provides direct evidence that the degradation in *sequence-as-modality* models occurs during semantic alignment, not in the biological encoder. This concretely diagnoses the "modality gap" claimed in Section 3.3.

- **Temporal robustness analysis (Figure 4) is well-designed.** Using first publication year to track performance drift, the paper shows that the context-driven approach degrades more gracefully (slope -0.618) than Evolla (slope -0.923). The controlled comparison using DeepSeek-V3 as the base LLM mitigates confounds from training data cutoff dates.

- **Computational efficiency analysis (Table 2) shows practical advantages.** The batch-mode throughput (0.13s vs. 20s per sequence) and cost ($0.0005 vs. $0.0152) compared to Evolla are compelling for real-world deployment, even if some numbers need clarification.

- **Clear conceptual framing ("tokenization dilemma").** The paper articulates a well-motivated distinction between weak representation (sequence-as-language) and semantic misalignment (sequence-as-modality), providing a useful conceptual lens for the community.

## Weaknesses

### Major

- **The benchmark is structurally biased in favor of the context-driven approach.** The questions ask about molecular function, pathway, and subcellular localization. The context is built using InterProScan (identifies domains directly linked to function) and BLASTp (retrieves GO annotations from homologs) — the same tools and databases from which the benchmark's ground truth is derived. This does not invalidate the *noise* finding (sequence+context < context-only), but it makes the absolute superiority of context-only unsurprising. The paper would be substantially stronger if the benchmark included questions that require genuine sequence-level reasoning (e.g., mutation effect prediction, binding interface identification) where the context alone cannot supply the answer.

- **The "sequence-as-noise" claim has a plausible alternative explanation that is not tested.** The degradation in Sequence+Context vs. Context-Only could simply reflect that the specialized Sci-LLMs (Intern-S1, Evolla, NatureLM) were not trained on the input format of "raw sequence + structured context concatenated." The paper does not test whether a small adapter or fine-tuning on this input format would reduce or eliminate the degradation. Without this control, concluding that sequences are "inherently noisy" rather than "mismatched to the input format" is premature. (Note: the degradation is smaller and less consistent for general LLMs like Gemini2.5 Pro and DeepSeek-v3, which partially mitigates this concern but does not eliminate it for the specialized models.)

- **Internal inconsistency in the wet-lab validation (Section 5.6).** The text states: *"While Evolla (Figure 6) attains a reasonable 80.0% accuracy on Rhodopsin, it fails catastrophically on PETase."* However, Figure 6 reports Evolla achieving **5.00%** on Rhodopsin (1/20 correct) and **83.78%** on PETase — the opposite of what the text describes. This is a clear error. Either the text or the figure is wrong, and the authors must correct this and clarify which numbers are accurate.

- **No confidence intervals, standard deviations, or significance testing anywhere in the paper.** Table 1 reports single-point estimates for every model × input configuration. Given that several key comparisons involve small gaps (e.g., DeepSeek-v3: Seq+Context 86.03 vs. Context-Only 84.99; GPT-5: 76.45 vs. 75.76), it is impossible to assess whether these differences are meaningful. The temporal analysis (Figure 4) also lacks uncertainty quantification around the trend slopes.

- **The LLM-Score evaluation protocol is underspecified.** The paper states it uses "a general-purpose LLM as an expert judge" but does not specify which LLM (GPT-4o? DeepSeek? Qwen?), what prompt was used, the scoring rubric, or whether any calibration or human validation of the automated judge was performed. This is critical since LLM-Score is the paper's primary metric.

### Minor

- **The embedding analysis (Figure 2) is an unfair comparison.** The context-driven embeddings are generated by Qwen-embedding from the structured context text itself, which explicitly contains domain names and GO terms. The ARI of 0.958 against MMseqs2 clusters (50% sequence identity) is unsurprising — sequences with ≥50% identity will have similar BLAST hits and InterProScan results, producing similar text embeddings. This is not comparable to the sequence models' embeddings, which are derived from raw sequences and must infer functional structure. A fairer comparison would use the same embedding model on both context and sequence inputs, or compare sequence-level embeddings from the models against context-level embeddings from the same models (if they can process both).

- **The batch efficiency figure of 0.13s per sequence needs clarification.** Running InterProScan and BLASTp typically takes minutes per protein. The paper attributes the estimation to Appendix M (stripped). The authors must clarify whether 0.13s includes the bioinformatics toolchain or only the LLM API call after pre-computed contexts are cached.

- **Figure 7 (trade-off landscape) presents ARI on the x-axis and a conceptual "Semantic Alignment" on the y-axis with no quantitative measurement.** The semantic alignment axis is not derived from any experiment, making the figure illustrative rather than evidential. The positioning of dots is not supported by data.

### Trivial

- The wet-lab section text says "80.0% accuracy on Rhodopsin" for Evolla but the figure shows 5.00%. This error needs correction.

## Nice-to-Haves

- Testing models *trained* to combine sequence and context would strengthen the noise claim. If an adapter or fine-tuning on sequence+context eliminates the degradation, the effect is an artifact of input mismatch rather than a fundamental property.
- An ablation where context is intentionally degraded (e.g., shuffled GO terms, removed domain information) would help isolate what makes the context valuable and test whether the embedding separation is due to content rather than formatting.
- Reporting per-sample or per-task variance would help assess whether degradation is consistent or noise-driven.
- A controlled baseline where all models receive the same generic context (holding context constant) would isolate the contribution of sequence-specific information.

## Removed Points

These points from the input reviews were removed as invalid or mischaracterized:

- *"Wet-lab sequences are not truly novel if BLAST/InterProScan found strong homologs"* — The paper acknowledges this limitation explicitly in the Conclusion section ("For truly novel orphan proteins...our method's performance may be constrained"). The wet-lab validation is presented as a test of generalization to *unpublished* sequences, not to the entire unseen protein universe.
- *"The efficiency comparison is not apples-to-apples"* — The comparison is between three reasonable deployment scenarios; the paper is transparent about what is being compared. The concern about specialized hardware vs. API calls is a real-world cost difference, not an unfair comparison.
- *"The temporal analysis confounds two factors"* — The paper explicitly discusses both factors (context sparsity for the context approach, training data cutoff for Evolla) and attributes different slopes to different mechanisms. The analysis does not claim to cleanly separate them.
- *"Missing related works"* — Cannot be verified and is excluded per guidelines.
- *"Formatting nitpicks"* — Excluded per guidelines.
- Criticisms about missing appendix content (dataset details, prompt design, cost estimation) — The parser strips appendices; these exist in the original submission.

## Novel Insights

The most genuinely novel observation is the *degradation pattern itself*: across all six models, giving an LLM both a rich structured context AND the raw sequence *consistently* produces worse results than context alone. This is not what one would naively expect — the conventional assumption is that more information, even if redundant, should not actively hurt. If this pattern holds under controlled experiments (e.g., with models trained on the combined format), it would be a genuinely important finding with practical implications for how biological QA systems should be designed. The layer-wise diagnosis in Evolla (Figure 3) — showing that the SaProt encoder produces excellent representations (ARI 0.945) that degrade through the Q-Former (0.916) and LLM decoder (0.809) — further pinpoints *where* information is lost. This diagnostic methodology is independently valuable for the field.

## Suggestions

1. Report confidence intervals (e.g., bootstrap) for all main results in Table 1 and significance tests for the context-only vs. sequence+context comparisons.
2. Specify the LLM used as the expert judge, the prompt template, and the scoring rubric. Validate LLM-Score against human annotations on a sample.
3. Correct the wet-lab inconsistency (80.0% vs. 5.00% for Evolla on Rhodopsin; clarify the PETase numbers).
4. Add a control experiment: train a small adapter or fine-tune one model on the sequence+context input format to test whether the degradation disappears.
5. Clarify what the 0.13s batch time includes (toolchain + API or just API call).
6. Replace the embedding comparison (Figure 2) with a fairer setup: either (a) use the same embedding model on both inputs, or (b) compare sequence embeddings from the models against their own context embeddings.
7. Add a benchmark task that cannot be answered from homology/domain information alone (e.g., mutation effect prediction) to test whether sequence truly adds no value in the context+sequence setting.

## Calibration Report

**Round 1 bracket (wide search):** <3.5 (weak anchors: 2.5–3.0), 3.5–7.5 (mid anchors: 4.0–5.0), >7.5 (strong anchors: 8.0). The paper clearly falls in the middle band.

**Round 2 narrowing (4.0–7.5):** Read anchors at 4.0 (LiveProteinBench, Protein-as-Second-Language), 4.5 (CoPeP), 4.67 (VenusX), 5.0 (QAProt, NABench), 6.5 (Flow Autoencoders, Reverse Distillation). The current paper is stronger than the 4.0–5.0 anchors (which were rejected for limited novelty, dataset concerns, or superficial evaluation) but less methodologically rigorous than the 6.5 anchors (which were accepted as posters).

**Final score: 5.5.** Positioned between the 5.0 reject-level papers (better central thesis, more systematic comparison) and the 6.5 accept-level papers (less rigorous in evaluation design, missing significance testing and key controls).

### Anchors referenced
| ID | Avg Score | Round | Comparison |
|---|---|---|---|
| ACroNFU7Do | 4.00 | 1 | Weaker — narrower benchmark, less novel thesis |
| 0FN0u6qTAi | 4.00 | 1 | Comparable — similar evaluation issues, weaker central claim |
| cliPM6kk9J | 5.00 | 1 | Comparable — interesting dataset but evaluation concerns |
| zcmL592XRG | 4.67 | 2 | Weaker — benchmark paper with limited novelty |
| QI2xC19p7U | 4.50 | 2 | Weaker — narrow evaluation, methodological concerns |
| d0gvsym66h | 5.00 | 2 | Comparable — similar evaluation rigor concerns |
| 5p9uled7JM | 6.50 | 2 | Stronger — more rigorous methodology, cleaner evaluation |
| gqCh1k0CEX | 7.00 | 2 | Stronger — thorough experimental design, significance testing |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>