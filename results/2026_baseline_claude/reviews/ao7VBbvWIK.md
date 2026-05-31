## Summary
HASTE (Hybrid AST-guided Selection with Token-bounded Extraction) is an engineering framework for code context retrieval that combines hybrid information retrieval (BM25 + dense embeddings with reciprocal rank fusion), AST-aware chunking, and call-graph expansion to feed LLMs with compact but structurally coherent code under tight token budgets. The system is evaluated on six curated Python files and twelve SWE-PolyBench instances using an LLM-as-judge protocol, reporting near-perfect judge scores and compression ratios up to 6.8×.

---

## Strengths
- **Meaningful problem framing.** The context-window bottleneck in LLM-assisted software engineering is real and practically important. Bridging structural integrity (AST) with relevance (IR) is a sensible design direction.
- **Modular, reproducible pipeline.** The pipeline is described at a level of detail sufficient to re-implement: chunker uses Tree-sitter AST, retrieval uses RRF with BM25 and a dense index, call-graph expansion is bounded by a configurable depth and token budget. An open PyPI package is mentioned.
- **Honest failure analysis on SWE-PolyBench.** Section 5.3 candidly discusses cases where HASTE scores 0–10, attributing them to bad upstream prompts or LLM reasoning failures rather than over-claiming.

---

## Weaknesses

### Fatal

1. **Baselines are defined but never evaluated.** Section 4.1.3 introduces three baselines (IR-only, AST-only, naïve truncation) as the core comparative foil for HASTE, but neither Table 2, nor Figures 2–3, nor any other part of the paper reports a single number for any of these baselines. The central claim—that HASTE outperforms structure-agnostic and relevance-agnostic methods—is entirely unsupported. Without this comparison, there is no scientific evidence that HASTE is better than the simplest alternatives.

2. **Evaluation dataset is fatally small.** The curated benchmark consists of **six** Python files and six editing tasks. No statistical conclusions can be drawn from six observations. The reported Pearson r = −0.97 with n = 6 is a textbook example of a small-sample correlation artefact: with six points spanning a wide range of x-values, almost any scatter will yield |r| > 0.9. Presenting this as "a strong negative correlation" and using it to characterise HASTE's compression–quality frontier is not scientifically valid.

3. **Primary metric (AST Fidelity, Hallucination Rate) not reported.** Section 4.2 defines AST Fidelity and Hallucination Rate as evaluation metrics alongside LLM-as-judge. Neither metric appears anywhere in Section 5. All reported results are judge scores (a single number from a prompted LLM), which cannot be independently verified and conflates multiple properties of the output. The paper's claim that HASTE "maintains high structural fidelity" and "reduces model-generated hallucinations" (abstract) is entirely unquantified.

4. **Placeholder citation in the reference list.** Reference "Zhang et al. [Zhang et al., 2025]" ends with the parenthetical "(Placeholder citation for illustrative purposes)." This is one of the core papers used to motivate HASTE's hallucination-reduction contribution in Section 2.4. Including a dummy citation in a submission is a serious integrity concern.

### Major

5. **SWE-PolyBench evaluation is dominated by trivial NOOP tasks.** Seven of twelve instances are "POLYBENCH-NOOP" tasks that require a syntactically valid but functionally empty patch (e.g., inserting a comment). Achieving a perfect score on a no-op does not test context retrieval quality at all. Of the remaining five non-trivial instances, four score ≤10. These failure rates are not discussed in relation to the baselines (which were not run), so it is impossible to know whether HASTE helps on real tasks.

6. **Tasks are trivially simple relative to context-window pressure.** Five of the six curated files are between 52 and 391 lines (Table 1). Gemini 1.5 Flash has a 1M-token context window. For these files, naïve truncation would simply include the entire file, making compression meaningless. The only file where context management matters is test5.py (1,317 lines), yet it achieves only 1.2× compression—the lowest in the set—suggesting HASTE barely engages its compression mechanism on the largest file.

7. **Call-graph expansion mechanics under-specified.** The paper states that HASTE traverses call graphs "up to a configurable depth" and filters under a "strict token budget," but never reports what depth or budget was used in any experiment, nor how often expansion was triggered or truncated. Without these details, the contribution is non-reproducible and non-comparable.

8. **No novelty beyond engineering assembly.** Every component—BM25, dense retrieval, RRF, AST chunking, call-graph traversal—is individually well-established. The combination is reasonable engineering, but the paper does not identify a conceptual insight, a new algorithm, or a theoretical result that is not already available in the cited literature. For a conference like ICLR, systems contributions are welcome, but they must be substantiated by rigorous comparative evaluation.

### Minor

- The compression ratio metric (original/compressed) is inconsistent with the "85% compression" claim in the abstract (85% means 1/0.15 ≈ 6.7×, which matches test3.py only). The other five files achieve 1.2–2.7×, corresponding to 17–63% compression. Claiming "up to 85%" as a headline number is misleading when it applies to one file out of six.
- The RQ2 correlation scatter plot (Figures 2c and 2d) has only six data points and a 6.8× outlier that mechanically drives the correlation; removing test3.py would almost certainly produce r ≈ 0. Reporting this as an evidence of a frontier is not meaningful.

### Trivial
- None beyond the above.

---

## Nice-to-Haves
- Report results for all three baselines on all benchmark tasks; a table with mean ± std across a statistically adequate sample would transform the paper.
- Use functional correctness (e.g., pass@k on unit tests) rather than or in addition to LLM-as-judge, since correctness in code is verifiable.
- Include an ablation table removing one component at a time (no call-graph, BM25-only, semantic-only, full HASTE) over a larger sample.

---

## Novel Insights
None beyond the paper's own contributions.

---

## Suggestions
- Replace the six-file curated dataset with a benchmark of at least several hundred tasks (e.g., the full SWE-PolyBench or SWE-bench Lite) and run all three baselines on the same tasks.
- Remove or replace the placeholder citation before any submission.
- Report the AST Fidelity and Hallucination Rate metrics that are defined in the methodology but absent from results.
- Select files that genuinely stress the context window (e.g., files of >5K lines) to make the compression benefit measurable.
- Replace the correlation analysis (n=6) with a proper regression or bucket analysis over a larger dataset.

---

## Score and Decision

The paper addresses a legitimate engineering problem and describes a coherent pipeline. However, the core scientific claim—that HASTE outperforms baseline retrieval strategies—is entirely unsupported by experimental evidence (baselines defined but not evaluated). The curated evaluation comprises six files with trivially simple tasks, the three defined evaluation metrics are partially never reported, and the paper contains a placeholder citation. These are not minor gaps; together they mean the paper's claims cannot be verified from what is actually presented.

MY FINAL SCORE: <score>1</score>
MY FINAL DECISION: <decision>Reject</decision>