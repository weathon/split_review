Now I have all the evidence I need. Let me write the final consolidated review.

---

## Summary
This paper makes three contributions to Graph Continual Learning (GCL). First, it identifies and convincingly demonstrates a critical flaw in the standard "local testing" evaluation protocol for node-level class-incremental learning: disconnected test subgraphs leak task identity, reducing class-incremental learning to task-incremental learning. A trivial mean-pooling baseline achieves forget-free, near-SOTA performance under this flawed setup (Table 1). Second, it introduces LLM4GCL, the first systematic benchmark evaluating 15 baselines (GNN, LLM, and graph-enhanced LLM methods) across 7 text-attributed graphs under a corrected "global testing" protocol for both NCIL and few-shot NCIL. Third, it proposes SimGCL, a simple method combining graph-prompted instruction tuning with prototype-based classification that substantially outperforms prior methods on most datasets.

## Strengths
- **Convincing evaluation critique with a clean demonstration.** Section 3.1 and Table 1 show that under local testing, mean-pooled prototypes + task-specific MLPs achieve forget-free performance matching the state-of-the-art TPP method. This reveals that the widely-used local-testing paradigm fundamentally degrades class-incremental learning into task-incremental learning — a finding that should influence future GCL evaluation standards. The demonstration is crisp: the baseline requires no learning, just pooling.

- **First comprehensive, multi-dimensional benchmark for LLMs in graph continual learning.** LLM4GCL evaluates 15 methods spanning three architectural categories (GNN, LLM, GLM) across 7 datasets (Cora, Citeseer, WikiCS, Photo, Products, Arxiv-23, Arxiv) under two continual settings (NCIL, FSNCIL). The dataset selection spans multiple domains, scales (thousands to hundreds of thousands of nodes), and session configurations — providing the community with a strong foundation for future work.

- **Eight data-backed observations that yield actionable insights.** The paper derives concrete findings from its benchmark: LLMs outperform GNNs even without graph structure (Obs.❷), current GLM designs underperform due to overfitting and representation misalignment (Obs.❸), prototype-based methods are robust across architectures and session lengths (Obs.❻, Obs.8), and model scaling consistently improves continual learning performance (Obs.7). These observations are grounded in specific table results and offer clear guidance for future GCL system design.

- **SimGCL achieves substantial empirical gains while being simple and efficient.** Across NCIL and FSNCIL, SimGCL outperforms all baselines on 23 of 28 dataset-setting-metric combinations, with absolute improvements of up to ~20% over the previous best LLM-based method (e.g., Cora NCIL: 84.6% vs. 70.8% for SimpleCIL). Its design — single-session LoRA tuning followed by training-free prototype classification — directly addresses catastrophic forgetting by avoiding inter-session parameter updates.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **SimGCL lacks component-level ablation, leaving its mechanism partially opaque.** SimGCL combines (a) LoRA instruction tuning on the first session and (b) ego-graph-derived textual prompts on top of the SimpleCIL framework (RoBERTa + prototype classifier). The performance gap between SimGCL and SimpleCIL tells us the combined benefit of both additions, but does not disentangle whether the graph prompts, the LoRA tuning, or their interaction drives the improvement. An ablation with (i) SimpleCIL + LoRA tuning without graph prompts, and (ii) SimGCL without LoRA, would clarify what each component contributes. This matters because the paper positions SimGCL as a method contribution; without this ablation, the reader cannot assess whether the graph-prompting technique generalizes beyond the specific LoRA setup.

- **Performance failures on Arxiv-23 and Arxiv are acknowledged but not investigated.** SimGCL substantially underperforms SimpleCIL on Arxiv-23 (NCIL: 38.7 vs. 52.4 avg; FSNCIL: 31.8 vs. 49.8) and on Arxiv FSNCIL (36.3 vs. 46.4). These are not marginal gaps. The paper attributes them to sparse graph structure and expanded tuning sets (Obs.❽), but provides no diagnostic experiments (e.g., varying graph density, examining prompt quality, or testing whether the LoRA tuning overfits on these datasets). Understanding *when and why* the graph-prompting approach fails would make the paper's recommendations more robust and actionable.

- **No variance estimates are reported.** All results in Tables 2–4 and Figures 3–4 are presented as single-point estimates. In continual learning, where task ordering, class sampling, and random seeds can produce non-trivial variance, reporting standard deviations (or at minimum noting the number of seeds) would strengthen confidence in the relative rankings — particularly for cases where performance differences between methods are small.

### Trivial
- **Observation numbering is garbled.** The paper uses Unicode circled digits but skips ❺ and ❼ (jumping ❹→❻→❽), then reverts to plain digits for observations 7 and 8. This is a minor formatting error that does not affect the paper's substance.

- **Table 4 delta notation is unexplained.** The arrows (↑, ↓) with numeric deltas (e.g., "24.5 ↓0.0") appear to show change relative to the GCN baseline in each column, but this is never stated in the caption or text, making the table hard to interpret independently.

## Nice-to-Haves
- **Ablation isolating SimGCL's components** (LoRA-only vs. graph-prompts-only) to clarify the method's mechanism.
- **Targeted experiments on Arxiv-23 and Arxiv failure cases** to understand the conditions under which graph prompting degrades performance.
- **A task-ID inference diagnostic under global testing** (e.g., reporting how accurately task ID can be predicted from connectivity or component-level features) to quantify whether the corrected protocol fully prevents the leakage the paper critiques.
- **Standard deviations or confidence intervals** for the main result tables across multiple random seeds or task-order permutations.
- **A specification of the class-removal thresholds** (which classes were dropped, at what sample-count cutoff) to improve reproducibility.

## Removed Points
*These points were flagged in the input reviews but are removed or demoted for the stated reasons.*

- **Missing computational cost comparison (Harsh Critic).** The paper explicitly states that time-efficiency analysis is provided in Appendix E. Since the appendix was stripped by the parser, this criticism cannot be verified against the paper as written and is removed per the evaluation protocol.
- **"No description of platform features, API, or design" (Harsh Critic).** The paper provides a specific repository URL and describes LLM4GCL as integrating baselines, datasets, and evaluation loops. A full API specification is beyond the scope of a conference submission and is appropriately deferred to the codebase. Removed as a nitpick about implementation details.
- **"The global testing protocol may not fully resolve structural leakage" (Harsh Critic).** This concern is speculative — it posits that disconnected components might still leak task identity through connectivity patterns or component-level features, but provides no concrete evidence that this occurs in practice. The paper's fix (union of subgraphs with global class sets) is a clear improvement over local testing. Demoted from major concern to a brief mention in Nice-to-Haves as a diagnostic suggestion.
- **Request for discussion of prototype-based CL in CV (Harsh Critic).** The paper does cite Zhou et al. (2025) and discusses SimpleCIL as a baseline. While a deeper comparison across modalities could be interesting, the paper's scope is GCL specifically, and the related work already covers CL with PTMs in both CV and NLP. Removed as scope creep.

## Novel Insights
The paper contributes a compelling instance of a broader pattern increasingly recognized across machine learning: evaluation protocol flaws can completely distort research progress, making trivial baselines appear competitive with sophisticated methods. The demonstration that local testing reduces class-incremental to task-incremental learning — and that a mean-pooling baseline matches SOTA under this flawed protocol — echoes similar findings in link prediction (degree bias), long-sequence modeling (random initialization artifacts), and graph classification (dataset effectiveness). The paper's insight that *the test graph topology itself can leak supervision* is a specific, well-articulated contribution to this growing literature on benchmark validity, and the systematic comparison of GNN, LLM, and GLM methods under a corrected protocol yields genuinely informative observations about where each architecture family excels or fails.

## Suggestions
- Add the component ablation for SimGCL (LoRA-only, graph-prompts-only variants). Even a partial ablation on a subset of datasets would substantially strengthen the method contribution and let the paper make a precise claim about which design choice matters.
- Run a simple diagnostic for residual task-ID leakage under global testing — for example, train a logistic regression classifier to predict task ID from component membership or mean node features, and report its accuracy. If the accuracy is near chance, the protocol is clean; if elevated, the paper gains a more nuanced understanding of its own evaluation.
- In the revision, expand the investigation of Arxiv-23 and Arxiv failure cases rather than treating them as footnotes. Understanding failure regimes is often more informative for practitioners than aggregate "wins" counting.

## Score and Decision

**Round 1 bracketing:** Weak anchors (graph CL benchmarks, scores 2.0–3.0), middle anchors (graph evaluation protocols, scores 4.75–5.67), strong anchors (CL benchmarks with pretrained models, scores 8.0–9.0). Initial bracket: the paper sits clearly above the middle anchors and below the strong anchors, in the ~6.0–7.5 range.

**Round 2 narrowing:** Compared against:
- *"Rethinking the Effectiveness of Graph Classification Datasets"* (avg 6.00, Reject) — a similar evaluation-critique paper. Our paper is stronger: the task-ID leakage demonstration is cleaner, the benchmark is broader, and the paper also contributes a method.
- *"Implicit degree bias in the link prediction task"* (avg 6.00, Reject) — another evaluation-critique paper with a clean demonstration of a sampling bias. Comparable in insight quality; our paper has broader scope.
- *"Elastic Feature Consolidation for Cold Start EFCIL"* (avg 7.00, Accept) — a strong method paper with good theory and ablations. Our paper has a different contribution profile (benchmark/evaluation vs. pure method) but comparable overall quality.
- *"Budgeted Online Continual Learning"* (avg 7.50, Accept) — a strong method + evaluation-framework paper. Slightly stronger than ours in methodological depth and ablations.

Our paper is clearly above the 6.00 anchors and comparable to the 7.00 anchor. It falls slightly below the 7.50 anchor due to weaker ablations and unexplored failure cases. Final placement: **7.0**.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>