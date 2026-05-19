- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 8, 5, 8
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

StructRAG proposes a framework for knowledge-intensive reasoning where an LLM-based router dynamically selects the optimal knowledge structure type (table, graph, algorithm, catalogue, or chunk), a structurizer converts raw documents into that structured format, and a utilizer decomposes the question and extracts precise knowledge from the structure. The router is trained via DPO on 900 synthetically generated preference pairs. Experiments on the Loong benchmark and Podcast Transcripts show improvements over long-context, standard RAG, RQ-RAG, and GraphRAG baselines, with gains increasing as documents grow longer.

## Strengths

- **Performance gains increase with document length and information dispersion.** The paper reports StructRAG's advantage over long-context baselines growing from ~9 points on the shortest document set (Set 1) to ~23 points on the longest (Set 4), and similar monotonic improvements over standard RAG (§6.2, Table 1). This pattern directly supports the claim that hybrid structurization is most beneficial when information is badly scattered.

- **Trained 7B router surpasses a much larger zero/few-shot model.** The router (Qwen2-7B with DPO) achieves higher type-selection accuracy than Qwen2-72B-Instruct with few-shot prompting (Table 5 in §7.1). This demonstrates that the training pipeline and synthetic data produce a meaningful capability even in a smaller model.

- **All three modules are shown necessary.** Ablation experiments (§6.3, Table 3) quantify that removing the router, structurizer, or utilizer drops overall score from 60.38 to 45.33, 53.92, and 55.94 respectively, establishing that each component contributes positively.

- **The paper transparently acknowledges EM trade-offs.** The case study (§7.3, Table 6) provides a concrete example of information loss during structurization (e.g., `$1,308,463` → `138463`) and links this to the exact-match deficits observed in sub-situations. The explanation is honest even if the severity assessment is debatable.

- **Efficiency advantage over GraphRAG.** The latency comparison (§7.4, Table 6) shows StructRAG is "obviously faster than GraphRAG" while outperforming it on both evaluated benchmarks, indicating practical deployability.

## Weaknesses

### Fatal
None.

### Major

- **The synthetic preference pipeline lacks external validation against ground-truth optimal types.** The router is trained via DPO on preference pairs generated entirely by an LLM pipeline (synthesize tasks → simulate solutions → judge quality). The paper never validates whether the LLM judge's preferred structure type actually leads to better downstream task performance (e.g., by manually annotating a held-out set of tasks with the genuinely optimal type, or by running the full StructRAG pipeline with each type exhaustively and measuring accuracy). While the router demonstrably outperforms raw LLMs at type selection, and router accuracy correlates with overall performance (§7.1, Figure 4), the training signal could encode stylistic preferences of the LLM judge rather than task-optimal structure choices. This gap weakens the claim that StructRAG selects the *truly optimal* structure type.

- **Exact-match deficits in sub-situations are acknowledged but under-explained.** The paper states StructRAG "falls short in seven sub-situations for the exact matching rate" (§7.3, line 238), yet attributes this primarily to formatting changes during structurization (e.g., `$1,308,463` → `138463`). This goes beyond formatting — it represents genuine information loss (removal of currency symbol, thousands separator) that could produce semantically wrong answers in precision-demanding tasks. The paper does not quantify how often such loss occurs across tasks, nor does it analyze whether the LLM-score metric might be biased toward structured but factually imprecise outputs. The overall EM is reported as better than baselines, but the paper does not reconcile why the method underperforms on EM in specific sub-situations while claiming superiority overall.

- **No confidence intervals, standard deviations, or statistical significance tests are reported.** The main results (§6.2) present raw score differences (e.g., improvements of 9, 15, 22, 23 points) without any measure of variance. Given the stochasticity of both LLM generation and LLM-as-judge evaluation, these differences could fall within noise for some settings. Without statistical grounding, the precision of the claimed improvements is unclear. This is especially relevant for the Podcast Transcripts evaluation, where only average head-to-head win rate is reported without per-dimension breakdowns or variance.

### Minor

- **The router makes decisions based on only "core content C" (titles or first few sentences) with no justification or ablation.** The paper states (§3, Eq. 2) that the router uses "the core content C of documents" defined as "the concentrate of the titles or the first few sentences from each document" (line 100), because "it is impractical to process the entire set of documents at once." This design choice is never ablated or analyzed — e.g., how router accuracy varies with document length, or whether important information might be missed when useful content is not in introductory sections.

- **The synthetic training data (900 preference pairs) is relatively small, and the seed tasks are underspecified.** The paper mentions "several manually collected seed tasks" covering "possible structure types" (line 145) but does not specify their number, diversity, or how they were chosen. The total training data is 900 pairs across five structure types, and no held-out router accuracy against ground-truth optimal types is reported. While the router comparisons are informative, the small data size raises questions about coverage of diverse task-structure mappings.

- **The structurizer processes each document independently (§3, Eq. 3), which could introduce cross-document inconsistencies.** The paper does not discuss whether independent processing of documents could produce redundant, contradictory, or misaligned structured knowledge when information from multiple documents needs to be integrated (e.g., consolidating financial indicators across reports into a single coherent table).

- **The "w/o router" ablation uses random routing (§6.3, line 202), which is an unrealistically weak baseline.** The paper separately compares to fixed-type routing (§7.2) and LLM-based routing (§7.1), which helps mitigate this concern, but the main ablation claims should reference a more meaningful alternative than random.

### Trivial
None.

## Nice-to-Haves
- A small-scale human evaluation comparing answer quality between StructRAG and the best baseline on a subset of tasks, especially those where the method shows EM deficits, would substantially strengthen the claims.
- Per-dimension breakdowns for the Podcast Transcripts win rates (comprehensiveness, diversity, empowerment, directness) would allow readers to assess whether the advantage is consistent or driven by one dimension.
- An analysis of structurizer failure modes (malformed tables, missing edges, incoherent pseudo-code) would help characterize the framework's robustness boundaries.

## Removed Points
- **Missing baselines (Self-RAG, Corrective RAG, ITER-RETGEN):** Removed per instructions — "DO NOT mention missing related works."
- **GraphRAG adapted to Qwen2-72B may not be optimal:** Removed — the paper explicitly states this choice was made for fair comparison (line 188); this is a reasonable methodological choice.
- **Efficiency comparison not apple-to-apple:** Removed — if GraphRAG's pipeline inherently involves more steps, measuring actual latency is the relevant comparison.
- **Criticism that "StructRAG loses on exact match" as a general statement:** Removed as factually imprecise — the paper claims overall EM is better than all baselines (line 197), and the EM sub-situation deficits are explicitly acknowledged and discussed. The critic's framing that the method "wins on an opaque LLM score but loses on exact match" directly contradicts the paper's stated results.
- **Framing that the EM case study is "downplayed":** Partially removed as an overstatement — the paper does acknowledge the issue and provides a concrete example. However, the concern about insufficient analysis of the severity is retained in the Major weaknesses section.

## Novel Insights
None beyond the paper's own contributions. The harsh critic's framing of the synthetic preference pipeline as a potential LLM self-consistency loop is a useful perspective but was already implicit in the paper's honest description of the method. The tension between the method's soft-score gains and its sub-situation EM deficits is the most interesting unresolved issue surfaced by the reviews.

## Suggestions
1. **Validate the synthetic preferences.** Take a subset of tasks, manually annotate which structure type produces the best actual task accuracy (by running the full StructRAG pipeline with each type), and compare the router's choices against these ground-truth labels. This would directly address the most serious concern about the training pipeline.
2. **Quantify the EM deficit.** Systematically analyze across tasks how often structurization alters information in ways that affect exact match, and propose mitigations (e.g., preserving original text for precise numerical values alongside the structured representation).
3. **Add variance reporting.** Report per-task results with confidence intervals or standard deviations (via multiple runs or bootstrap resampling) for the main benchmark results.
4. **Ablate the core-content design choice.** Show how router accuracy changes when using different amounts of context (full document summaries vs. titles vs. first paragraphs) to justify the current design.
5. **Provide per-dimension breakdowns** for the Podcast Transcripts win rates rather than a single average.
