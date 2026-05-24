Now I have a solid picture of the calibration landscape. Let me write the final consolidated review.

**Round 1 bracket: 3.0–4.0.** HASTE is clearly weaker than the 4–6 band papers (which have proper evaluations with baselines and multiple benchmarks) but has a genuinely novel idea and coherent architecture distinguishing it from the 1–2 papers.

**Round 2 narrowing:** Comparing to anchors in the 3–4 range:
- **Demo Distillation (3.40)** — similarly missing baselines but at least had some comparisons; HASTE is worse in evaluation completeness but better in architectural novelty. Comparable overall.
- **SWE-Bench+ (3.75)** — limited contribution but thorough empirical analysis with clear methodology; HASTE has a more novel contribution but far less rigorous evaluation.
- **ACES (3.67)** — interesting idea but fundamental methodological concerns about evaluation validity (LLM-as-labeler); HASTE shares the evaluator validity concern but has a different core problem (comparative evaluation missing entirely).

HASTE sits at the lower end of this bracket due to the structural incompleteness of its evaluation.

Final score: **3.5**

Now let me write the review.

---

Let me organize the strengths and weaknesses carefully.

**Strengths to keep:**
1. Clear problem framing and well-motivated architecture (verified: Section 2.5, Section 1)
2. Concrete evidence of structural preservation (test3.py example with 6.8× compression and call-graph expansion that included a dependent class) (verified: Table 2, Section 5.1)
3. Precise formalization of hybrid ranking via RRF (verified: Section 3.3, Eq. 1)
4. Transparency about failure modes on SWE-PolyBench (verified: Figure 3, low-scoring instances discussed)

**Weaknesses:**

FATAL: None (the paper could be fixed with additional experiments)

MAJOR:
1. Baselines are defined (Section 4.1.3) but never compared against in the results (Section 5) — the paper's central claim about resolving the structure-relevance trade-off is unsupported without this comparison.
2. LLM-as-Judge is unvalidated (no human validation, no inter-rater reliability, no calibration) AND two promised metrics (AST Fidelity §4.2.2, Hallucination Rate §4.2.3) are never quantitatively reported.
3. The curated dataset has only 6 files; the Pearson correlation r=−0.97 for RQ2 is based on 6 data points, with the correlation visibly driven by a single point (test3.py).

MINOR:
4. SWE-PolyBench evaluation excludes instances with "processing errors" without stating what constitutes an error or how many instances were excluded.
5. Several implementation details are unspecified (which embedding model, call-graph traversal depth, token-budget filtering algorithm).

TRIVIAL:
6. The paper claims "Partial Builder" in Figure 1's caption but describes "Payload Builder" in the text.

Now let me write the review.## Summary

HASTE proposes a framework for code context compression that combines AST-guided chunking, hybrid lexical-semantic retrieval with reciprocal rank fusion, and call-graph expansion under token budgets. The goal is to resolve the trade-off between preserving structural coherence (syntactic validity) and maintaining semantic relevance when truncating code context for LLM prompts. The paper describes a modular pipeline architecture and evaluates it on 6 curated Python files and 12 SWE-PolyBench instances using an LLM-as-Judge metric.

## Strengths

- **Well-motivated problem framing and clearly articulated gap.** Section 2.5 crisply summarizes how prior work in AST representation, token-level pruning, hybrid RAG, and hallucination mitigation each addresses only part of the challenge, and none operates under strict token budgets while preserving syntax. This directly motivates HASTE's design and helps the reader understand what is new.

- **Concrete evidence of structural preservation under aggressive compression.** The test3.py case (Table 2, §5.1) shows HASTE achieving 6.8× compression (85.3% reduction) while scoring 90 on the Judge metric. The judge's justification confirms that call-graph expansion correctly included a dependent class definition, enabling a correct complex type hint — a task the paper argues would be impossible with structure-agnostic truncation. This is the single best piece of evidence for the framework's promise.

- **Principled hybrid ranking formulation.** Section 3.3 formally defines the RRF scoring function (Eq. 1) combining BM25 lexical scores and semantic similarity, with the smoothing parameter *k*=60 stated. This provides a reproducible foundation for the retrieval component.

- **Transparent reporting of failure modes on SWE-PolyBench.** Figure 3 and the accompanying discussion explicitly document low-scoring instances (scores of 10, 5, 0) and attribute them to ambiguous suggestions or generic templates, rather than only cherry-picking successes. This candor about limitations is valuable.

## Weaknesses

### Fatal

None. The paper's core ideas are coherent and potentially useful, and the evaluation problems are fixable with additional experiments rather than being fundamental flaws in the approach itself.

### Major

- **The baselines defined in Section 4.1.3 (IR-only, AST-only, naïve truncation) are never compared against in the Results section.** This is the single most critical weakness. The paper's central claim — that HASTE resolves the structure-relevance trade-off — *cannot* be evaluated without knowing how structure-only or relevance-only alternatives perform on the same tasks. Section 5 contains zero baseline data: no tables, no figures, no textual summary. The reader cannot determine whether HASTE is better, worse, or equivalent to the simplest alternatives. This omission renders the evaluation structurally incomplete relative to the paper's own stated research questions (RQ1 explicitly asks "compared to baseline methods").

- **The LLM-as-Judge metric is unvalidated, and two promised metrics are never reported.** The primary evaluation uses Gemini 1.5 Flash as a judge scoring outputs on 0–100. No human validation, inter-rater reliability, calibration against ground-truth rubrics, or discussion of potential biases is provided. Separately, Sections 4.2.2 and 4.2.3 define **AST Fidelity** and **Hallucination Rate** as evaluation metrics — and the abstract claims "reducing model-generated hallucinations" — yet neither metric appears anywhere in Section 5 quantitatively. This creates an expectation the paper does not meet and weakens the evidence for the hallucination-reduction claim.

- **The evidence for RQ2 (compression–quality trade-off) rests on 6 data points.** The Pearson correlation of *r* = −0.97 between compression ratio and Judge Score (§5.2) is computed from the 6 curated files. With only 6 points, a single instance (test3.py) visibly drives the correlation. While the descriptive observation is informative, claiming that HASTE "effectively navigates" the trade-off frontier requires more than a 6-point regression, particularly without comparison to structure-agnostic pruning at equivalent compression levels.

### Minor

- **SWE-PolyBench evaluation is reported on only 12 instances after excluding "instances that resulted in processing errors,"** but the paper never states what constitutes a processing error, how many instances were in the original set, or whether the exclusion could bias results. If HASTE systematically failed to produce contexts for certain tasks, the selection would mask failures.

- **Several implementation details are underspecified**, making reproducibility harder than it should be: the embedding model (which specific encoder?) is not named (§3.2); the call-graph traversal depth is described only as "configurable" (§3.3) with the actual value used in experiments unstated; and the core token-budget filtering algorithm — the mechanism by which the expanded candidate set is pruned under budget — is described in a single sentence ("The expanded set is then filtered under a strict token budget") with no pseudocode or formal description.

### Trivial

- Figure 1's caption mentions a "Partial Builder" module, but the text of Section 3.1 describes a "Payload Builder" — these appear to be the same component but use different names.

## Nice-to-Haves

- Validating the LLM-as-Judge with human agreement on a held-out subset, or calibrating against task pass/fail outcomes.
- Including more code files (beyond 6) in the curated dataset and more tasks across multiple LLMs (e.g., GPT‑4o, Llama 3).
- Clarifying the SWE-PolyBench exclusion criteria and reporting results on the full instance set.
- Adding an ablation study isolating the effect of each component (AST-guided chunking, hybrid retrieval, call-graph expansion, token-budget filtering).

## Removed Points

These points were identified by reviewers but are removed from the main assessment for the following reasons:

- *Harsh Critic point 5 about reproducibility details (e.g., Partial Builder explanation, fusion strategy choice):* The appendix was stripped by the PDF parser; some of these details likely exist in the original submission. The token-budget filtering algorithm and embedding model identification are retained as Minor weaknesses because they are core architectural choices that should appear in the main body.
- *Strength Finder point 4 (quantitative analysis of compression-quality frontier):* This conflicts with the verified weakness that the correlation rests on only 6 data points. Per the filtering discipline, when a strength and verified weakness disagree, the weakness prevails. The raw observation (compression ratios achieved) is retained in Strengths, but claiming it as a "precise empirical characterization" overstates the evidence.
- *Harsh Critic point about "hallucination rate" in abstract creating unmet expectation:* This is addressed through the Major weakness about unreported metrics.

## Novel Insights

None beyond the paper's own contributions. The reviewers' inputs collectively surface the core evaluation gap but do not produce new technical insight about the method or domain that the paper itself does not articulate.

## Suggestions

1. **Run and report all baseline comparisons.** This is non-negotiable: add tables for IR-only, AST-only, and naïve truncation on both the curated dataset and SWE-PolyBench, reporting Judge Scores, AST Fidelity, and Hallucination Rate for each.
2. **Validate the LLM-as-Judge** by showing human agreement on a subset, or at minimum calibrate against binary pass/fail outcomes on the editing tasks.
3. **Report AST Fidelity and Hallucination Rate quantitatively** as Sections 4.2.2–4.2.3 promise.
4. **Scale the evaluation** to include more files, more tasks, and at least one additional LLM (e.g., an open-weight model). Report variance across runs.
5. **Document the token-budget filtering algorithm** with pseudocode or a formal description — this is the core technical contribution and its current one-sentence description is insufficient.

## Score and Decision

**Calibration details:**

**Round 1 bracket (3.0–4.0):** The paper is clearly weaker than the 4–6 band papers (LongLLMLingua at 5.80 has thorough multi-benchmark evaluation with baselines; Stated-CLM at 4.75 has comprehensive LongBench evaluation) but has