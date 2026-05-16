Here is my final consolidated review.

---

## Summary

This paper introduces Magnushammer, a two-stage transformer-based premise selector for the Isabelle proof assistant. The method uses contrastive training with a retrieve-then-rerank architecture (Select + Expand) to retrieve relevant premises from proof states. The paper reports strong empirical results: 59.5% vs. 38.3% on PISA, 34.0% vs. 20.9% on miniF2F against Sledgehammer, and a 57% → 71% improvement when replacing Sledgehammer in the Thor neural-symbolic prover. The authors also release a 4.4M-example premise selection dataset, the largest of its kind.

## Strengths

- **Strong empirical results with clean controlled evidence**: The Thor experiment (replacing Sledgehammer with Magnushammer within the same neural-symbolic pipeline, improving 57% → 71% while using 4× fewer parameters) provides a controlled comparison that cleanly isolates premise selection quality. This is the most compelling piece of evidence, as both variants share the same reasoning backend.

- **Significant end-to-end gains over a widely-used tool**: On the PISA benchmark, Magnushammer achieves 59.5% vs. Sledgehammer's 38.3%, and 34.0% vs. 20.9% on miniF2F. These are large absolute improvements on standard benchmarks using the same proof assistant.

- **Data efficiency**: Magnushammer outperforms Sledgehammer using only 4K training examples (0.1% of the available 4.4M dataset), demonstrating that the method learns effectively from limited data and that the contribution is not simply a function of dataset scale.

- **Scalability with compute budget**: Figure 1 shows that Magnushammer's proof success rate continues to improve as the computational budget grows, while Sledgehammer and BM25 plateau. This is a practical advantage for users who can allocate more resources.

- **Release of the largest premise selection dataset**: The paper open-sources 4.4M premise selection instances with 433K unique premises from Isabelle — the first such dataset for this proof assistant and the largest openly available for premise selection. This is a valuable community resource.

- **Well-motivated two-stage architecture**: The retrieve-then-rerank design (Select for fast retrieval via cosine similarity, Expand for contextualized cross-encoder scoring) is principled for balancing speed and accuracy in large formal libraries (30K–50K premises per state). The joint training — using hard negatives from Select for Expand — is a practical innovation.

## Weaknesses

### Fatal
None.

### Major

- **The headline comparison with Sledgehammer conflates different reasoning backends, partially but not fully addressed.** Magnushammer is evaluated by trying Isabelle tactics with retrieved premises (2s timeout), while Sledgehammer runs external ATPs (E, Vampire, Z3, etc.) which perform heavy combinatorial search and proof reconstruction. These are fundamentally different processes. The paper states "Up to this last step... Sledgehammer is essentially used as a precise premise selection tool" (line 110), but the ATP reasoning itself is a significant component of Sledgehammer's power — not just the premise filter. The compute-budget analysis (Figure 1) attempts to control for resource usage, and the Thor experiment provides a clean controlled comparison. However, the paper's central framing ("outperforms Sledgehammer") rests partly on an apples-to-oranges comparison that would benefit from more careful qualification. The paper should either (a) reframe the stand-alone comparison more transparently as "Magnushammer + Isabelle tactics vs. Sledgehammer (full ATP pipeline)" or (b) present retrieval-only metrics (e.g., recall@k) that isolate premise selection quality directly, as a complement to the end-to-end results.

### Minor

- **No ablation of the two-stage architecture (Select vs. Expand).** The paper claims that Expand's cross-encoder re-ranking is more accurate but slower, yet it does not report how much Expand improves over Select alone. If the improvement is small, one could argue the simpler Select model suffices; if large, it further justifies the design. Either way, this is a natural ablation that the paper omits.

- **No ablation of the negative mining strategy (M=3N).** The paper states that mining additional negatives (M=3N vs. standard batch-contrastive M=0) is "crucial for performance" (line 241) but provides no experimental evidence. An ablation comparing M=0, M=N, and M=3N would substantiate this claim.

- **No discussion of label noise in training data construction.** The dataset is built from human-written Isabelle proofs, where the premises explicitly used in a proof step are treated as positives and all others as negatives. This implicitly assumes that unused premises are irrelevant, which introduces label noise (a proof may rely on only a subset of relevant premises, and many unstated premises could also be useful). The paper does not discuss this issue or analyze its impact, despite relying on this assumption for both the contrastive and BCE losses.

- **No error analysis.** The paper reports only aggregate success rates. An analysis of which problems Magnushammer solves that Sledgehammer does not (and vice versa), or a breakdown by problem characteristics, would deepen understanding of the method's strengths and failure modes.

- **No measure of variance or statistical significance.** Results are reported as single numbers. Given nondeterminism in both Sledgehammer's ATP solvers and tactic execution, some measure of variance (multiple runs, confidence intervals) would strengthen the compute-budget comparisons especially.

### Trivial
None.

## Nice-to-Haves

- A direct retrieval evaluation (recall@k) comparing Magnushammer's premise selection against Sledgehammer's heuristic filter (e.g., "mash" or the internal relevance front-end) would cleanly isolate premise selection quality without conflating it with downstream proving power.
- A discussion of how often the premise embedding cache is updated in deployment (premise databases change as new theorems are proved) would address a practical concern.
- An analysis of training stability — whether the alternating training of Select and Expand causes interference — would strengthen the methodology section.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Missing Sledgehammer configuration details (ATPs, timeouts, version):** The experiments subfile (stripped by the parser) contains these details per the paper's cross-references. The original submission had this information.
- **Missing hyperparameters in main text (learning rate, transformer size, optimizer, etc.):** These are documented in the experiments subfile (stripped). The parser removes appendix content from all papers.
- **Insufficient compute-budget definition:** The paper explicitly cross-references Sections \ref{sec:compute_budget_definition} and \ref{sec:budget_experiments} (in the stripped experiments subfile) for the definition. The original submission contains this specification.
- **Criticism about Sledgehammer being "not reproducible" due to missing ATP configuration:** Same reason — the experiments subfile contains these details in the original submission.
- **Complaint about computational cost of training vs. Sledgehammer's zero-training requirement:** This is a feature of all learned approaches vs. heuristic baselines, not a specific weakness of this paper. The paper's data efficiency result (4K examples) partially addresses this.

## Novel Insights

The harsh reviewer's observation about the comparison fairness is the most substantive concern: the paper's headline claim mixes premise selection quality with the choice of reasoning backend (Isabelle tactics vs. ATPs). However, the strength finder correctly identifies that the Thor experiment (where the only variable changed is Sledgehammer→Magnushammer) provides a clean resolution. This tension — between a buzzy end-to-end comparison and a cleaner but less flashy controlled experiment — is common in systems papers and is handled reasonably well here, though the framing could be more transparent. The lack of ablations for the two-stage design and negative mining is the most actionable gap: these are standard experiments the authors could trivially run, and omitting them leaves reasonable doubt about which design choices actually drive performance.

## Suggestions

1. Add an ablation comparing Select-only vs. Select+Expand. This is the single most informative missing experiment.
2. Add an ablation of the negative mining factor (M=0, M=N, M=3N) to substantiate the claim that mining additional negatives is "crucial."
3. Reframe the Sledgehammer comparison more carefully: qualify that Magnushammer + Isabelle tactics is compared against Sledgehammer's full ATP pipeline, or add retrieval-only metrics (recall@k) to directly measure premise selection quality.
4. Add a brief discussion of label noise in the dataset construction and why contrastive learning is robust to it (the paper cites work on false negatives in contrastive learning but does not connect this to their own data).
5. Add variance estimates or confidence intervals for the main results, especially the compute-budget comparison.

## Score and Decision

This paper makes a solid contribution: a well-engineered neural premise selector with strong empirical results, a valuable dataset release, and a clean controlled experiment (Thor) that validates the approach. The methodological gaps are real but addressable — missing ablations and a comparison that could be more carefully framed — and do not undermine the core contribution. The paper is clearly above the acceptance threshold.

**Originality:** Good — applying contrastive two-stage retrieval to premise selection for Isabelle is novel, though the architecture follows established IR practices.

**Importance of research question:** High — premise selection is a bottleneck in automated theorem proving, and improving it has direct practical impact.

**Claims well supported:** Mostly yes, though the headline comparison could be more transparently framed.

**Soundness of experiments:** Solid core (Thor experiment, data efficiency, compute-budget scaling) with some missing ablations.

**Clarity of writing:** Clear and well-organized.

**Value to community:** High — dataset release alone is a significant contribution.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>