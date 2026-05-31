Now I have a thorough picture of the paper. Let me do the calibration search before writing the final review.**Round 1 Bracket: 1.5 – 3.5**

HASTE is clearly weaker than REPOFILTER (5.60): no baseline comparisons, tiny n=6 evaluation, placeholder citation. It may be comparable to or slightly below D2Coder (1.67), which at least had real evaluation on SWE-bench but lacked technical detail. Initial bracket: **1.5–3.5**.Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

HASTE (Hybrid AST-guided Selection with Token-bounded Extraction) proposes a modular pipeline for code context retrieval under LLM token budget constraints. It integrates AST-aware chunking, hybrid BM25+semantic retrieval with Reciprocal Rank Fusion, and call-graph expansion to produce structurally coherent, token-bounded code contexts. The system is described as a deployed Python package and evaluated on a curated 6-file dataset and a small slice of SWE-PolyBench.

---

## Strengths

- **Coherent architectural design**: The modular pipeline (Scanner → Chunker → Identifier Extraction → Payload Builder → Hybrid Index → Retriever with RRF → Call-graph expansion → Token-bounded Exporter) represents a well-motivated engineering integration. The Retrieval Pipeline (Section 3.3) and its RRF formulation are described concretely.

- **AST-bounded chunking addresses a real problem**: Section 3.1 describes function/class-level AST-aware chunking that prevents the "Frankenstein context" problem of naïve line-based splitting. This design rationale is specific and grounded.

---

## Weaknesses

### Fatal

- **Baselines defined but entirely absent from results**: Section 4.1.3 defines three baseline conditions — IR-only retrieval, AST-only retrieval, and naïve truncation — and RQ1 asks explicitly "to what extent can HASTE's compression enable LLMs to perform correct code edits **compared to baseline methods**?" Table 2 shows only HASTE scores (Compression Ratio and Judge Score). Figures 2 and 3 show only HASTE scores. There is no table, figure, or reported number comparing HASTE to any of the three stated baselines anywhere in the paper. The paper's central empirical claim — that the hybrid approach beats simpler alternatives — cannot be assessed at all from the evidence presented.

- **Placeholder citation used as empirical motivation**: The reference list contains: *"Ziyao Zhang et al. LLM hallucinations in practical code generation… (Placeholder citation for illustrative purposes)."* This fabricated reference is actively invoked in Section 2.4 ("Zhang et al. [Zhang et al., 2025] identified incomplete or conflicting context as a primary driver of hallucinations") as empirical motivation for HASTE's hallucination-reduction claim. Using a self-acknowledged fabricated citation in the paper body is a scholarly integrity problem that also weakens the motivation of Section 2.4.

### Major

- **Evaluation scale is too small to support any conclusion**: The curated-dataset evaluation covers exactly six Python files (Table 1). SWE-PolyBench covers twelve instances, seven of which the paper confirms are "POLYBENCH-NOOP" tasks (Section 5.3) — tasks requiring only a non-empty, non-functional patch such as adding a comment. The remaining five substantive instances score 95, 10, 10, 5, and 0. A paper presenting one score in the high-90s, two at 10, one at 5, and one at 0 over just five non-trivial instances cannot support the abstract's claim of "significantly improving the success rate of automated code edits."

- **Two of three defined evaluation metrics have no reported results**: Section 4.2 defines three metrics — LLM-as-Judge, AST Fidelity, and Hallucination Rate. Table 2 and all figures report only Judge Scores and Compression Ratio. No AST Fidelity values and no Hallucination Rate values appear anywhere in the paper. The metrics are described and motivated (Section 4.2.2 and 4.2.3) but the data is simply missing.

- **The judge LLM is not identified**: Section 4.2.1 states "A general-purpose LLM is prompted with the task, reference code, and system output" with no model name, no prompt text, and no inter-rater reliability measure. Section 4.1.4 identifies the editor LLM as Gemini 1.5 Flash, but the judge is a different and unnamed model. The primary evaluation metric is therefore unreproducible as written.

- **r = −0.97 is statistically meaningless at n = 6 with a single dominant outlier**: The correlation in Section 5.2 is computed over six data points. Five of those points span compression ratios 1.2–2.7× with Judge Scores 98–100; one outlier (test3.py) sits at 6.8× / 90. The r = −0.97 is entirely driven by this single point; removing it leaves five near-identical values with no meaningful variance. Presenting this as evidence of a discovered "trade-off frontier" is not statistically supportable.

### Minor

- **SWE-PolyBench presentation conflates trivial and non-trivial tasks**: The aggregate presentation in Figure 3 — "a large number of instances achieve perfect or near-perfect scores" — is inflated by the 7 NOOP instances. The paper does acknowledge the NOOP designation, but buries it mid-paragraph. Reporting NOOP and non-NOOP results separately would more honestly characterize performance on tasks requiring genuine reasoning.

- **LLM-generated tasks without human verification**: Section 4.1.2 states tasks were "automatically generated using our Suggestion Generator" with no description of what the generator does, no human review step, and no difficulty control. Since these tasks also serve as retrieval queries, there is a potential circularity: the system's query generator may produce queries that match its own index preferentially.

### Trivial

- None beyond the verified issues above.

---

## Nice-to-Haves

- Run the three already-defined baselines on the same six curated files and the same SWE-PolyBench instances and report their Judge Scores and compression ratios in a single comparison table. This is not optional — it is the minimum needed to demonstrate the paper's claim — but it is listed here as a constructive path to fixing the paper.
- Report AST Fidelity and Hallucination Rate for all evaluated instances, as these are defined in the methodology and directly tied to the paper's stated contribution.
- Vary the token budget systematically across the same files to build a genuine compression-quality frontier rather than observing it post hoc across unrelated files.
- Exclude or separately analyse NOOP tasks in the primary SWE-PolyBench results.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "Empirical demonstration on diverse, realistic tasks" providing "evidence of generalizability beyond a single testbed" (Strength Finder)** — Removed. The claim of generalizability is directly contradicted by the tiny scale (n=6 curated, n=5 substantive SWE-PolyBench). The near-perfect average of 97.3 comes from a homogeneous set of trivial type-annotation tasks. This conflicts with the verified evaluation-scale weakness.

- **Strength: "Quantification of the compression-quality trade-off (r = −0.97)" as a "clear, measurable characterisation of the frontier" (Strength Finder)** — Removed. A correlation computed from 6 points with one lever outlier is not a validated characterisation of any frontier; this is a delusional strength as verified above.

- **Strength: "Well-defined, complementary evaluation metrics capturing semantic quality, syntactic integrity, and robustness" (Strength Finder)** — Removed. Two of the three metrics have zero reported results. The strength cannot hold when the data was not collected (or not reported).

- **Data Availability / double-anonymous tension (Harsh Critic)** — Removed as a scientific weakness. The PyPI name in the Data Availability section is a minor programme-committee concern, not a flaw in the scientific contribution.

- **"Section 3.4 (Observability) should not have been included" (Harsh Critic)** — Removed. It is standard practice in systems papers to describe monitoring infrastructure; it does not undermine the contribution.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the SWE-PolyBench NOOP task inflation misleadingly portrays success is correct and worth carrying into the review, but it is not a novel insight — it follows directly from reading the reported data.

---

## Suggestions

1. **Execute and report baseline comparisons.** Run IR-only, AST-only, and naïve truncation on the same six curated files and same SWE-PolyBench instances. Without this, the paper's core claim is unverifiable.
2. **Replace or remove the placeholder citation.** Either find the actual reference for the hallucination claim (or cite an existing work), or rewrite Section 2.4 to avoid dependence on it.
3. **Report all three defined metrics.** AST Fidelity and Hallucination Rate are motivated and defined but absent from results. Include them.
4. **Disclose the judge LLM and its prompt.** At minimum, name the model version and provide the evaluation rubric.
5. **Expand the evaluation dataset.** Six files is too small for any quantitative conclusion. Even 30–50 files of varied complexity would be a substantial improvement.
6. **Separate NOOP and non-NOOP SWE-PolyBench results.** Report the five substantive task scores in the primary analysis.

---

## Assessment on Key Axes

**Originality**: Moderate at the architectural level (AST + hybrid IR + call graph under a token budget in one pipeline), but the individual components are well-established. The novelty depends entirely on whether the combination demonstrably outperforms simpler alternatives — which the paper fails to show.

**Importance of the research question**: High. Token-bounded, structure-aware code context retrieval is a real and practically significant problem.

**Whether claims are well-supported**: Very poor. The central comparative claim is supported by zero comparative evidence. The abstract states HASTE "significantly improv[es] the success rate of automated code edits" but this is never tested against any baseline.

**Soundness of experiments**: Very weak. n=6 curated, three metrics defined but one reported, a fabricated citation in the motivation, and a statistically indefensible correlation as the main quantitative finding.

**Clarity of writing**: Adequate; the system design is described legibly. The discrepancy between the three defined metrics and the one reported metric is a significant clarity failure.

**Value to the research community**: Low in current form. The pipeline idea has potential value but the paper as submitted offers no evidence beyond a system description.

---

## Calibration

**Round 1 anchors:**
- `/dsALpkd1OU.md` (D2Coder), avg 1.67, Round 1 — real SWE-bench evaluation with some baselines but severe technical detail gaps; more substance than HASTE despite its problems.
- `/2HN97iDvHz.md` (LLM Data Center), avg 3.00, Round 1 — system-style paper with engineering framing, Reject.
- `/mS7xin7BPK.md` (LEGO-Compiler), avg 3.40, Round 1 — actually scored 6.50 (metadata error); more rigorous than HASTE.
- `/xFezgECSLa.md` (LLM-Based Algorithms), avg 3.00, Round 1 — theoretical framing, Reject.
- `/TS8PXBN6B6.md` (AST-T5), avg 5.67, Round 1 — strong AST pretraining paper with proper comparative evaluation; far stronger than HASTE.
- `/RrWAtQNGAg.md` (CodeChain), avg 4.00, Round 1 — dataset paper, Reject.
- `/2umZVWYmVG.md` (LLM Code Reasoning), avg 3.75, Round 1 — evaluation paper, Reject.
- `/oOSeOEXrFA.md` (REPOFILTER), avg 5.60, Round 1 — closely topically related; has extensive evaluation, real benchmarks, comparisons. Vastly stronger than HASTE.
- `/KIgaAqEFHW.md` (miniCTX), avg 8.00, Round 1 — strong accept; irrelevant comparison.
- `/EytBpUGB1Z.md` (Retrieval Head), avg 8.00, Round 1 — strong mechanistic analysis; irrelevant.

**Round 1 bracket: 1.5 – 3.5**

**Round 2 anchors:**
- `/JVJE5yZRxm.md` (Teaching Code Execution to Tiny LMs), avg 3.00, Round 2 — code execution study, has real training experiments and evaluation; stronger than HASTE.
- `/zEPYCDaJae.md` (DataSEA), avg 2.50, Round 2 — automated LLM pipeline system paper; similar lack of baselines and limited scope but does have some evaluation; comparable to HASTE.
- `/ech9J3xl9X.md` (Narrow Transformer), avg 2.50, Round 2 — fine-tuned small code LM, limited novelty but has real benchmarks.
- `/CscKx97jBi.md` (Improve Code Generation with Feedback), avg 3.00, Round 2 — feedback-based code generation with some evaluation.
- `/dsALpkd1OU.md` (D2Coder), avg 1.67, Round 2 — has real SWE-bench evaluation but severe gaps.
- `/kNvwWXp6xD.md` (Seeker), avg 3.00, Round 2 — multi-agent exception handling, has evaluation.
- `/BltaWJZMeR.md` (DataSciBench), avg 3.20, Round 2 — benchmark paper with semi-automated pipeline.

**Round 2 narrowing**: HASTE is comparable to DataSEA (2.50) in that both are system pipeline papers leaning on engineering combination with limited evaluation. HASTE is worse than DataSEA because (a) its baselines are defined but absent, (b) one citation is a self-acknowledged placeholder, and (c) two of its three defined metrics have no results. HASTE is comparable to or slightly worse than D2Coder (1.67), which despite severe technical-detail gaps at least attempted a real comparative evaluation on SWE-bench. The placeholder citation and the total absence of baseline comparisons push HASTE to the bottom of the bracket.

**Final score: 2.0**

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>