Now I have sufficient calibration. Let me write the final consolidated review.

---

## Summary

This paper introduces GraphRAG-Bench, a benchmark and empirical framework for systematically investigating when graph structures benefit retrieval-augmented generation. It features (1) a four-level task taxonomy spanning fact retrieval, complex reasoning, contextual summarization, and creative generation — moving beyond the fact-retrieval-heavy focus of existing benchmarks; (2) two corpora with controlled information density (tightly structured NCCN medical guidelines and loosely organized pre-20th-century novels); and (3) multi-stage evaluation metrics covering graph quality, retrieval performance, and generation accuracy. The paper evaluates seven GraphRAG frameworks against RAG baselines and derives nine observations about when and why GraphRAG outperforms vanilla RAG, along with an efficiency analysis of token costs.

## Strengths

1. **Well-motivated and targeted benchmark design.** The paper convincingly demonstrates (Figure 2) that existing benchmarks (HotpotQA, MultiHop-RAG, UltraDomain) allocate 0% of their questions to creative generation and overwhelmingly focus on simple fact retrieval (e.g., HotpotQA has 78.2% fact-retrieval questions). The four-level task hierarchy (Table 1) directly addresses this gap and is a genuine contribution for the community. The inclusion of creative generation tasks is a notable departure from prior work.

2. **Controlled corpora with different information densities.** The paper deliberately selects two corpora with contrasting structure — NCCN medical guidelines (dense, hierarchical domain knowledge) and pre-20th-century novels (loosely organized, implicit narratives) — enabling evaluation of GraphRAG's claim to handle both structured and unstructured contexts. This is a clear improvement over generic Wikipedia-based benchmarks that lack domain hierarchies.

3. **Multi-stage evaluation beyond final-answer accuracy.** The paper introduces separate metrics for graph quality (node/edge count, clustering coefficient), retrieval performance (context relevance, evidence recall), and generation accuracy (faithfulness, evidence coverage). Tables 4 and 5 disaggregate retrieval and graph-structure results, enabling more fine-grained diagnosis of where graph structures contribute than prior work that treats the pipeline as a black box.

4. **Efficiency analysis with concrete token-cost data.** Tables 6–7 report average token costs, revealing dramatic disparities (MS-GraphRAG global: ~331k tokens vs. RAG: ~0.9k on the novel dataset). Observations 8–9 on prompt inflation and its relationship to task complexity provide practical, actionable guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Under-specified evaluation setup.** The caption of Table 3 states "using GPT-4o-mini," but it is unclear whether GPT-4o-mini is used (a) as a single generator for *all* methods, (b) as an evaluator that scores outputs from each method's own generator, or (c) both. Each GraphRAG framework (MS-GraphRAG, HippoRAG, LightRAG, etc.) has its own default generation pipeline. If different methods use different base LLMs or different prompt templates, the comparison conflates graph-related differences with LLM-choice differences, and the paper's central claims about "when GraphRAG surpasses traditional RAG" are compromised. The paper must specify: (i) what LLM generates answers for *every* baseline, (ii) how the RAG baseline retriever is configured (retriever model, chunk size, top-k), and (iii) whether the same LLM and prompt template is used across all systems. This is the most significant weakness in the experimental design.

2. **No statistical significance or variance reporting.** All results in Tables 3, 4, 5, 6, and 7 are reported as point estimates without confidence intervals, standard deviations, or replication information. The number of test questions per task level is not stated in the main text. This makes it impossible to assess whether reported differences (e.g., 60.14 vs. 60.92 for fact retrieval ACC, or 53.38 vs. 42.93 for complex reasoning ACC) are meaningful or within noise. For a benchmark that claims to provide reliable guidance about when to use GraphRAG, this omission is significant.

### Minor

3. **Dataset construction details are deferred to the appendix.** Section 3.2 describes question generation and evidence extraction at a high level ("systematically transforms raw text into structured domain ontologies," "calibrate questions by progressively integrating evidence types") without specifying how gold evidence subgraphs are defined, what quality checks are performed, how many questions per category, or any annotation protocol. While the appendix may contain these details, the main text should stand with enough information for an initial assessment, especially for a benchmark paper. The paper states "Relevance check and refinement. To ensure accuracy... Full methodological details are provided in Appendix C" (lines 150–151), which is too deferential for a benchmark contribution.

4. **Obs.3 compares different metrics without acknowledging the asymmetry.** Observation 3 states "RAPTOR scores highest in faithfulness (70.9%) on the novel dataset, though RAG covers more evidence (40.0%)" — comparing *faithfulness* (a precision-aligned metric: is the answer faithful to the context?) against *evidence coverage* (a recall-aligned metric: does the answer cover all required knowledge?). These are different evaluation dimensions. The qualitative trade-off described is reasonable, but the observation would benefit from explicitly noting that these are different metrics measuring complementary aspects rather than directly comparable scores, or from reporting both metrics for both methods.

5. **Graph complexity analysis (Section 4.3) lacks normalization consistency.** Figure 5 reports raw node/edge counts, which are difficult to compare across datasets of different sizes. The paper mentions "per 10k corpus tokens" for HippoRAG2 values in the text (line 269) but does not apply this normalization consistently across all methods in the figure. The structural variation analysis could be tied more directly to downstream retrieval and generation performance.

### Trivial
- The paper refers to HippoRAG2 as both "HippoRAG2" and "HippoRAG (Gutiérrez et al., 2025)" inconsistently across tables.

## Nice-to-Haves
- A controlled experiment where the *only* variable is the presence or absence of graph-enhanced retrieval, with all other components (chunking, retriever model, LLM, prompt template) held fixed, would more cleanly isolate the effect of graph structure.
- Reporting the number of questions per task level and per dataset in the main text would help readers calibrate the reliability of reported scores.
- Qualitative examples showing one full example per difficulty level (question, gold evidence, retrieved contexts from RAG vs. GraphRAG) would illustrate the benchmark's diagnostic capability.
- An ablation on graph construction parameters (e.g., varying extraction density within a single framework) would help connect graph structural properties to downstream performance.

## Removed Points

- **"Suspicious data consistency in Table 3 (identical values across datasets)"**: The Harsh Critic claimed that HippoRAG2 reports *identical* values across Novel and Medical datasets for Fact Retrieval ACC (60.14), Complex Reasoning ACC (53.38), etc. In the parsed text, these values appear **only once** (line 189). The parsed Table 3 shows a single set of GraphRAG rows without a dataset subheader. Based on the observations (Obs.3 explicitly references "on the novel dataset" for RAPTOR's faithfulness score), these GraphRAG rows correspond to the Novel dataset, with Medical results likely deferred to the appendix (Appendix G). The claim of "identical values across datasets" is not verifiable from the text as written and appears to be a misinterpretation of the table structure.

- **"Circularity in gold evidence favoring GraphRAG"**: The Harsh Critic speculated that "if the gold evidence set is constructed using the same graph-based ontology that GraphRAG methods use, there is a potential circularity favoring GraphRAG." This is a speculative concern with no evidence in the paper that the gold evidence annotations are biased toward any particular retrieval paradigm. Removed as an unsupported speculation.

- **Generic area-of-concern sweeps** (e.g., "could the metric be measuring a proxy?", "are confounders controlled?"): These are exploratory questions from the Harsh Critic rather than specific identified problems. Removed per filtering discipline.

## Novel Insights

None beyond the paper's own contributions. The main value from the reviews is the identification that the evaluation setup (whether all methods share the same generator LLM and prompt template) is underspecified in the current version, which is a concrete concern that the authors can address in a revision.

## Suggestions

1. **Clarify the evaluation setup explicitly.** State in a dedicated paragraph: "For all methods, we use GPT-4o-mini as the [generator / evaluator / both]. All methods receive the same prompt template [show in appendix]. The RAG baseline uses [retriever model, chunk size, top-k]." Without this, the central empirical claims cannot be properly evaluated.

2. **Add confidence intervals or error bars.** If single-run evaluation is standard for large-scale benchmarks (which is arguable), at minimum report the number of questions per task-dataset cell so readers can gauge sample-size effects. For key comparative claims, consider bootstrap estimates of variance.

3. **Move key dataset construction details into the main text.** Specifically: number of questions per task level per dataset, how gold evidence subgraphs are extracted, and any quality assurance metrics (e.g., sample-level human verification rates). The current text is too high-level for a benchmark paper.

## Score and Decision

### Calibration

I retrieved 12 anchor papers across two rounds.

**Round 1 (Bracketing):**
- Weak band (avg < 3.5): Sp6znUhP1n (3.33, Reject), KQL9UuQv6k (3.00, Withdrawn), QTKuEyRHaY (3.00, Withdrawn), Y2JL8JXwmf (2.50, Withdrawn)
- Middle band (3.5–7.5): QcgkUJbfxT (5.00, Reject — *similar-topic GraphRAG-Bench paper*), DBqOInhRkG (4.67, Reject), CiyENV6CND (4.50, Reject), uDgDuVMpfW (5.00, Reject)
- Strong band (7.5+): VKGTGGcwl6 (8.00, Oral), UJ2UUjT2ko (8.00, Poster), 9gw03JpKK4 (8.00, Oral), DM0Y0oL33T (8.00, Oral)

**Initial bracket:** 4.5 to 6.5

**Round 2 (Narrowing):**
- QcgkUJbfxT (5.00, Reject) — Similar-name GraphRAG-Bench paper; narrower domain (CS textbooks only), pretraining contamination concerns. Our paper has better task diversity, avoids pretraining contamination, and has more meaningful corpora. **Our paper is stronger.**
- DBqOInhRkG (4.67, Reject) — RARE benchmark for RAG robustness. Comparable evaluation depth but our paper's benchmark design (task hierarchy + controlled corpora) is more targeted. **Our paper is somewhat stronger.**
- ddpLHL9JJo (4.67, Reject) — MIRAGE multi-hop reasoning benchmark. **Our paper is stronger.**
- 9lPq01iKOV (5.50, Accept Poster) — Frustratingly Simple Retrieval paper. A method paper with strong results on established benchmarks. Hard to directly compare, but its score (5.5) anchors the upper-middle range.
- mCtfkypdm6 (6.00, Accept Poster) — LinearRAG, a GraphRAG method paper with cleaner experimental controls than our benchmark paper. **Our paper is weaker on experimental rigor.**
- 4zAbkxQ23i (6.00, Accept Poster) — RAVENEA, a multimodal RAG benchmark with human annotation and rigorous quality control. More thorough evaluation infrastructure. **Our paper is weaker on evaluation rigor.**

**Narrowing result:** Our paper sits between the 5.0 similar-topic GraphRAG-Bench (weaker benchmark design) and the 6.0 accepted papers (stronger experimental methodology). It has genuine contributions in benchmark design (task hierarchy, controlled corpora, multi-stage metrics) but is held back by the underspecified evaluation setup and lack of variance reporting. The most comparable accepted paper is Frustratingly Simple Retrieval at 5.50, which also has a mixed score profile with dispersed reviewer scores (4, 8, 6, 4). Our paper has a comparable strength of contributions with similar methodological gaps.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>