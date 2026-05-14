Now I have a thorough understanding of the paper and calibration anchors. Let me construct the final consolidated review.

---

## Summary

This paper challenges the dominant sequence-centric paradigm in Scientific LLMs (Sci-LLMs) for biomolecular understanding. The authors articulate a "tokenization dilemma" — sequence-as-language tokenization destroys functional motifs, while sequence-as-modality approaches introduce semantic misalignment between biological and linguistic representations. They propose a context-driven approach that feeds LLMs structured, human-readable bioinformatics annotations (Pfam domains, GO terms, BLAST homolog annotations) instead of raw sequences. Through systematic experiments across seven LLMs on multiple benchmarks, they show that context-only input dramatically outperforms sequence-only input, and that adding raw sequences alongside context degrades performance — suggesting raw sequences act as informational noise. The paper includes wet-lab validation on novel proteins, temporal generalization analysis, and efficiency comparisons.

## Strengths

- **Compelling central empirical finding with broad model coverage**: Table 1 shows context-only consistently and substantially outperforms sequence-only across three specialized Sci-LLMs (Intern-S1, Evolla, NatureLM) and four general-purpose LLMs (DeepSeek-V3, Gemini 2.5 Pro, GPT-5, Qwen3). The degradation from Context-Only to Sequence+Context (e.g., Evolla drops from 74.02 to 70.53, Intern-S1 from 86.15 to 84.03) is a genuinely counterintuitive result that merits investigation.

- **Multi-faceted evaluation design**: The paper goes beyond a single benchmark, testing on protein QA, EC number prediction (hierarchical F1 metrics), temporal degradation across three decades of protein discoveries, wet-lab validation on truly novel unpublished sequences, and cross-modal generalization to DNA mutation prediction. This breadth strengthens confidence in the core findings.

- **Wet-lab validation on novel sequences** (Section 5.6): Achieving 100% accuracy on Rhodopsin (20 samples) and 97.3% on PETase (37 samples) using truly unpublished sequences is a meaningful test of generalization that cannot be explained by training-data leakage. The contrast with Evolla's 5.0% on PETase is stark.

- **Clear and well-articulated problem framing**: The "tokenization dilemma" conceptual framework (weak representation vs. semantic misalignment) provides a useful lens for understanding the limitations of current Sci-LLM paradigms. Section 5.2 and 5.3 provide concrete evidence for both horns through ARI-based representation analysis.

- **Practical efficiency analysis** (Section 5.5): The cost analysis showing the context-driven pipeline is ~23× cheaper and 1.3× faster than Evolla for single queries (and 154× faster in batch) while outperforming it demonstrates practical viability beyond academic benchmarking.

- **Thoughtful ablation of context components** (Appendix E): The finding that unconditionally combining ProTrek with GO/Pfam degrades performance (81.56 vs. 84.60), motivating a conditional fallback strategy, demonstrates careful engineering.

## Weaknesses

### Fatal

None.

### Major

- **The "informational noise" claim is not adequately isolated from confounds**: The paper consistently interprets the Sequence+Context < Context-Only degradation as evidence that raw sequences act as "informational noise." However, no control experiments rule out alternative explanations. The models tested were not trained to process inputs that intermix raw amino-acid sequences with structured textual annotations — the degradation could reflect an out-of-distribution input format rather than an inherent property of tokenized sequences. It could also be caused by attention dilution from longer inputs, or by the LLM attending to low-level sequence patterns that conflict with the high-level context. The paper would benefit from ablations such as: replacing the sequence with equal-length random or shuffled amino acids, testing models explicitly trained on mixed sequence+text inputs, or varying input ordering. Without such controls, the "noise" interpretation, while plausible, is not adequately demonstrated.

- **The representation analysis compares fundamentally different input types without sufficient caveats**: Section 5.2 compares ARI scores of sequence-based model embeddings (0.49–0.69 for sequence-as-language, 0.809 for Evolla) against embeddings from the text-embedding model Qwen-embedding applied to the functional context (ARI 0.958). The context already explicitly describes functional categories in natural language, so its superior clustering is expected and does not independently diagnose the "tokenization dilemma." The paper presents this as evidence that sequence-based representations are "weak," but the comparison is between an input that already encodes function labels in text and inputs that must infer function from primary sequence. The finding remains useful as a magnitude-of-gap diagnostic, but the paper should acknowledge that this comparison cannot cleanly isolate tokenization effects from the inherent information advantage of text-encoded functional annotations.

### Minor

- **The paper acknowledges but does not address an important scope limitation**: In Appendix J, the authors candidly note that their method cannot handle mutation effect prediction because InterProScan and BLAST are insensitive to single-point mutations. This is a significant limitation for a paradigm positioned as a general alternative to sequence-based approaches. The critic's suggestion to test on tasks where sequence-level information is indispensable (e.g., point mutation effect prediction) would strengthen the paper by delineating the boundaries of the context-driven approach.

- **Missing baseline for wet-lab validation**: Section 5.6 shows high accuracy on Rhodopsin/PETase classification using context. However, a simple baseline that classifies based solely on Pfam domain presence (e.g., "contains a 7-transmembrane domain → Rhodopsin") is not reported. Given that the context includes Pfam domain descriptions, such a baseline would help quantify the LLM's added value beyond the tool output itself. This is not fatal — the paper's broader contributions do not hinge on this experiment — but it weakens the claim that the LLM is doing meaningful reasoning in this specific task.

- **LLM-Score calibration is not examined**: The evaluation metric uses DeepSeek-V3 as an LLM judge (Section 5.1, Appendix C.1). While this is a reasonable choice for open-ended QA, the paper does not examine whether the judge LLM is susceptible to surface-level overlap with the context (e.g., giving higher scores when the answer shares vocabulary with the context, regardless of correctness). This could inflate scores for context-based answers. A small human evaluation study or correlation analysis would strengthen confidence in the metric.

### Trivial

- The paper's framing of "reasoning engines over expert knowledge" vs. "sequence decoders" is rhetorically effective but somewhat overstates the novelty — using bioinformatics tools to generate features for downstream ML is standard practice. The novel contribution is specifically the systematic demonstration that LLMs perform far better with tool-generated context than with raw sequences, and the counterintuitive noise effect.

## Nice-to-Haves

- A quantification of how often the context contains answer-equivalent statements for the test tasks, with results stratified by answer presence, would allow readers to assess the retrieval vs. reasoning confound directly.
- For the wet-lab validation, adding a domain-rule baseline (classify by Pfam domain presence) would better isolate the LLM's contribution.
- Ablating the Sequence+Context degradation with random/shuffled sequence controls would strengthen the noise interpretation.
- Testing on tasks where sequence-level information is indispensable (e.g., point mutation effect prediction, which the paper identifies as a limitation in Appendix J) would help delineate the paradigm's boundaries.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Issue 1 (context contains the answer, invalidating the comparison)**: The critic claims the context "frequently contains the answer itself" and the comparison is "fundamentally unfair." The paper explicitly addresses label leakage in Section 4: it uses InterProScan for intrinsic domain analysis (not identity lookup) and BLASTp to transfer GO terms from homologs, not the query protein's own records. This is standard bioinformatics practice. The QA example in Appendix I.1.1 demonstrates that the LLM synthesizes across multiple Pfam domain descriptions and GO evidence — it is not merely extracting a pre-written answer. While some BLAST-derived GO annotations from close homologs may be very similar to the ground truth, the paper's central claim is precisely that Sci-LLMs should leverage such structured knowledge rather than decode raw sequences. The comparison demonstrates this point. The critic's framing of this as "invalidating the core comparison" is itself invalid — it misunderstands the paper's thesis. However, the paper would benefit from a more explicit discussion (see Major Weakness about quantifying answer-proximate information).

- **Harsh Critic claim that "the novelty is overstated"**: The critic says this is "essentially a call to use well-established bioinformatics tools... which is already standard practice." The paper's novel contribution is not the use of bioinformatics tools per se, but (1) the systematic empirical demonstration across seven LLMs that this approach dramatically outperforms sequence-based approaches, (2) the counterintuitive finding that adding raw sequences degrades performance, and (3) the "tokenization dilemma" conceptual framework. This is sufficient novelty for an empirical paper.

- **Harsh Critic Section-by-Section note on temporal analysis**: The critic says the context-driven method's stability "is expected" because BLAST uses up-to-date databases. This is partially true but doesn't invalidate the finding — it supports the paper's argument that tool-augmented approaches are more temporally robust than sequence-trained models, which is a genuine practical insight.

- **Harsh Critic Section-by-Section note on efficiency analysis**: The critic notes the cost estimates rely on assumptions. The paper provides detailed cost estimation in Appendix M with explicit instance types, pricing, and throughput models. This is adequate for the paper's level of analysis.

- **Harsh Critic claim about Evolla's Q-Former analysis**: The critic says the ARI drop could be due to "simple compression and discretisation" rather than semantic misalignment. The paper's Appendix F provides complementary evidence through mutation sensitivity analysis — the Q-Former smooths out fine-grained mutation signals that the SaProt encoder captures. This supports the misalignment interpretation beyond simple compression. The criticism is acknowledged but the paper's analysis is reasonable as-is.

- **Strength Finder's "Ablation study" as a core strength**: While useful, this is an engineering detail that supports the main pipeline design rather than being a core contribution. Kept as a supporting strength rather than elevated.

- **Formatting / parser artifacts**: All typos, garbled text, broken characters in figures/tables are parser artifacts — not author errors. Removed from consideration.

## Novel Insights

Beyond the paper's own contributions, the results raise an interesting meta-question about evaluation in Sci-LLM research: how much of reported Sci-LLM performance on biological tasks is attributable to memorized sequence-to-function mappings from training data versus genuine biochemical reasoning? The temporal degradation analysis (Section 5.4) provides suggestive evidence that specialized Sci-LLMs may rely heavily on memorization of well-studied protein families — their performance collapses on recently discovered proteins — while the context-driven approach (which uses tools rather than memorized sequence-function mappings) remains stable. This observation, while requiring further validation, points toward a broader need for temporal or novelty-based evaluation splits in biological AI benchmarks.

## Suggestions

- Add an experiment or at minimum a discussion quantifying how often context components contain answer-proximate information, stratified by BLAST e-value or sequence identity of the top homolog, to help readers assess the retrieval-vs-reasoning balance.
- For the Sequence+Context degradation, acknowledge the OOD input format as a potential confound and discuss how future work could isolate the "noise" effect from format mismatch.
- Add a Pfam-domain-rule baseline for the wet-lab binary classification task to strengthen the claim about LLM reasoning value.
- Consider reframing the representation comparison in Section 5.2 as a diagnostic of the information gap rather than as independent evidence for the "weak representation" horn — the comparison is informative but doesn't cleanly isolate tokenization effects.

## Score and Decision

**Anchor comparison:**

- `/home/wg25r/review_agent/human_reviews_2026/ACroNFU7Do.md` (LiveProteinBench, avg 4.0, Reject): A benchmark paper with limited methodological novelty and a small dataset. This paper is substantially stronger — broader experiments, wet-lab validation, clearer thesis, and a counterintuitive finding.
- `/home/wg25r/review_agent/human_reviews_2026/0FN0u6qTAi.md` (Protein-as-Second-Language, avg 4.0, Reject): Clever framing but narrower experimental scope. This paper has broader evaluation across more models, tasks, and modalities.
- `/home/wg25r/review_agent/human_reviews_2026/cliPM6kk9J.md` (QAProt, avg 5.0, Reject): A dataset paper with significant evaluation methodology issues. This paper is stronger — it makes a paradigm argument with systematic empirical support.
- `/home/wg25r/review_agent/human_reviews_2026/KjyQhJUobQ.md` (ProtFunAgent, avg 3.0, Reject): Tool-augmented protein annotation but with less comprehensive evaluation. This paper is clearly stronger.
- `/home/wg25r/review_agent/human_reviews_2026/NskQgtSdll.md` (PepBenchmark, avg 6.0, Accept Poster): A well-executed benchmark with solid curation but limited technical novelty. This paper is comparable — it has more novel findings (the noise effect, temporal analysis, wet-lab) but some similar caveats about experimental design.
- `/home/wg25r/review_agent/human_reviews_2026/5BRMteyNOp.md` (SciRecipe, avg 6.0, Accept Poster): Strong empirical contribution in a different domain. Comparable quality level.
- `/home/wg25r/review_agent/human_reviews_2026/KJNgtPNxtv.md` (PFMBench, avg 3.5, Reject): Comprehensive benchmark but limited novelty. This paper is stronger.
- `/home/wg25r/review_agent/human_reviews_2026/7cDfYiqe4X.md` (Protap, avg 3.5, Reject): Benchmark with experimental design issues. This paper is stronger.

The paper presents a well-articulated thesis with broad empirical support. The central finding — that context-driven approaches dramatically outperform sequence-based approaches across diverse models and tasks, and that adding raw sequences degrades performance — is genuine and important. The multi-faceted evaluation (protein QA, EC prediction, temporal analysis, wet-lab validation, DNA generalization, cost analysis) provides converging evidence. The main weaknesses are that the "informational noise" interpretation is not fully isolated from alternative explanations, and the representation analysis partially compares incommensurable representations. These weaken the paper's strongest claims but do not invalidate its core contribution. The paper sits at the level of a solid poster acceptance — a meaningful empirical contribution with some caveats that prevent it from being a standout.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>