Now I have enough calibration to finalize. Let me write the complete review.

## Summary
This paper introduces LLM4GCL, the first benchmark for evaluating LLMs and graph-enhanced LLMs (GLMs) in Graph Continual Learning (GCL). It makes three contributions: (1) identifying a task-ID-leakage flaw in existing "local testing" evaluation for Node-level Class-Incremental Learning (NCIL), (2) systematically evaluating 9 LLM/GLM baselines across 7 text-attributed graphs under corrected "global testing," and (3) proposing SimGCL, which uses ego-graph-derived prompts for LoRA-based instruction tuning in session 1 and training-free prototype classification thereafter.

## Strengths
- **Well-evidenced identification of task-ID leakage in prior GCL evaluation (Section 3.1, Table 1):** The paper demonstrates that standard local testing degrades class-incremental to task-incremental learning. Even trivially simple methods (mean pooling + MLP) achieve 0% forgetting across all 7 datasets, matching the previous SOTA TPP. This is a genuine and important methodological critique backed by reproducible evidence.
- **Comprehensive benchmark design (Section 3.2):** The paper integrates 9 methods across 3 families (GNN-based, LLM-based, GLM-based) on 7 datasets from citation, web-link, and e-commerce domains with varied scales, enabling nuanced cross-method comparisons. This is the first evaluation of LLM/GLM methods in the GCL setting.
- **Counter-intuitive finding that GLMs underperform pure LLMs in GCL (Obs. ❸, Tables 2–3):** Deliberately designed graph-enhanced LLMs (GraphPrompter, GraphGPT, LLaGA) consistently fail to outperform pure LLM methods like SimpleCIL, attributed to GNN-LLM representation misalignment during continual learning. This is non-obvious and practically relevant.
- **Training-free prototype design for incremental sessions (Equations 1–2):** After a single first-session LoRA fine-tuning round, subsequent sessions use frozen-embedding prototype classification with no parameter updates. SimGCL shows A_N values dramatically higher than continuously-trained methods (e.g., 80.0% vs. 38.2% for GCN on Cora in Table 2).

## Weaknesses

### Fatal
None.

### Major
- **SimGCL's backbone is unspecified in Tables 2/3 (Section 3.2, Tables 2–3):** The baselines section states "RoBERTa integrated with SimpleCIL" but SimGCL's row in Tables 2 and 3 does not identify which LLM backbone it uses. Figure 3 evaluates SimGCL with BERT and RoBERTa variants of different sizes, but the headline results in Tables 2/3 are silent. Without knowing the backbone, readers cannot determine whether improvements come from SimGCL's design choices or from model scale.

- **Inconsistent SimGCL gains over SimpleCIL; "20%" claim is misleading (Abstract, Tables 2–3):** The abstract claims SimGCL "surpasses the previous state-of-the-art GNN-based baseline by around 20%," comparing against Cosine (the best GNN method) rather than SimpleCIL—the strongest LLM-based baseline that already uses prototype matching. Against SimpleCIL, SimGCL's results are mixed: in NCIL, SimGCL loses on Arxiv-23 (Ā: 38.7 vs 52.4; A_N: 13.6 vs 38.8) and Arxiv A_N (33.8 vs 36.5). In FSNCIL, SimGCL loses on WikiCS Ā (68.8 vs 73.2), Arxiv-23 (Ā: 31.8 vs 49.8; A_N: 10.3 vs 40.0), and Arxiv (Ā: 36.3 vs 46.4; A_N: 6.8 vs 36.6). On Arxiv-23 and Arxiv in FSNCIL, the gaps reach ~30 points. The "20%" figure selectively highlights the best case against a weaker comparator.

- **No ablation isolating SimGCL's components (Section 3.3):** SimGCL has three design elements: (a) ego-graph-derived text prompts, (b) LoRA-based instruction tuning in session 1, and (c) prototype-based classification for subsequent sessions. SimpleCIL already uses (c). Without ablations isolating (a) from (b), it is impossible to determine whether gains come from graph-structured prompt text, from LoRA fine-tuning, or whether a simpler prompt without LoRA would suffice.

- **GLM baselines evaluated without prototype-based inference (Tables 2–3):** The paper's central finding (Obs. ❻) is that prototype-based methods dramatically outperform continuously-trained methods. Yet GLM baselines (GraphPrompter, GraphGPT, LLaGA) are all evaluated under continuous training without any prototype-based variant. The paper cannot distinguish whether SimGCL outperforms GLMs because of its specific design or simply because it uses prototypes while they do not.

### Minor
- **Observation numbering is broken (Section 4):** The sequence jumps from Obs. ④ to Obs. ❻, skipping ❺ entirely. The numbering then switches from circled numerals to Arabic (7, 8), suggesting an editing oversight.

- **Obs. ❽ overstates SimGCL's dominance (Section 4, lines 173–174):** The claim "SimGCL consistently overperform other baselines (23 out of 28)" includes comparisons against weak GNN methods. Against SimpleCIL specifically, SimGCL wins on approximately 21/28 dataset×metric pairs. The paper would be stronger if it honestly acknowledged the large-margin losses on Arxiv-23 and Arxiv (FSNCIL) rather than presenting only aggregate counts.

- **Ego-graph prompt design underspecified (Section 3.3):** The prompt template is described qualitatively but key design choices are missing: number of hops in the ego-graph, neighbor selection strategy when degree is high, and the exact prompt format. This affects reproducibility.

### Trivial
None.

## Nice-to-Haves
- Applying prototype-based inference to at least one GLM baseline (e.g., GraphPrompter) would substantially strengthen the paper by testing whether SimGCL's advantage is design-specific or prototype-generic.
- Adding targeted ablations: SimGCL without LoRA (ego-graph prompt + prototypes only) and SimGCL without ego-graph (LoRA + prototypes only).
- Reframing the "20%" claim to compare against SimpleCIL, or acknowledging that gains over the strongest LLM baseline are modest and inconsistent.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's concern about formatting/typos: these are parser artifacts, not author errors.
- The RoBERTa citation concern (Conneau et al., 2019): This may refer to XLM-RoBERTa which is indeed by Conneau et al., and the original RoBERTa reference (Liu et al., 2019) is also cited elsewhere in the paper. This is a minor citation ambiguity, not a clear error.

## Novel Insights
The paper's most genuinely novel insight is the identification and demonstration of task-ID leakage in existing GCL evaluation (Table 1). The finding that even trivially simple methods achieve 0% forgetting under local testing is a convincing and important methodological critique that should reshape how the GCL community evaluates methods. The secondary insight—that prototype-based approaches with LLM backbones significantly outperform GNN-based continual learning under corrected global testing—is well-supported and practically relevant.

## Suggestions
- Specify SimGCL's backbone explicitly in Tables 2 and 3 (and all result tables).
- Add targeted ablations: SimGCL without LoRA (ego-graph prompt + prototypes only) and SimGCL without ego-graph (LoRA + prototypes only).
- Apply prototype-based inference to at least one GLM baseline to test whether SimGCL's advantage is design-specific.
- Reframe the "20%" claim to compare against SimpleCIL or acknowledge that gains over the strongest LLM baseline are modest and inconsistent.
- Fix the missing Obs. ❺ and standardize observation numbering.

## Score and Decision

**Retrieved anchors (all rounds):**
- Round 1: "Online Continual Graph Learning" (5.0, graph CL benchmark, rejected) — weaker than our paper, lacks method contribution and the task-ID leakage finding
- Round 1: "Stabilize continual learning with hyperspherical replay" (3.0, continual learning) — much weaker, no graph or LLM focus
- Round 1: "Dynamic Mixture-of-Experts for Incremental Graph Learning" (4.75, graph CL) — consistent method but no benchmark insight; weaker overall
- Round 1: "Topology-aware Embedding Memory for Learning on Expanding Graphs" (5.40, graph CL) — method-focused, no benchmark contribution
- Round 1: "Towards Continuous Reuse of Graph Models" (5.75, graph CL, accepted) — method with consistent improvements, weaker benchmark
- Round 1: "N-ForGOT: Open Temporal Graph Learning" (6.25, graph CL, accepted) — strong method with theory, comparable but narrower scope
- Round 1: "Online GNN Evaluation Under Test-time Distribution Shifts" (8.00, graph) — much stronger, different topic
- Round 2: "Evaluating and Improving LLMs on Graph Computation" (6.75, LLM graph benchmark, accepted) — strong pure benchmark, no method
- Round 2: "CLDyB: Dynamic Benchmarking for CL" (5.67, CL benchmark, accepted) — comparable benchmark-only contribution
- Round 2: "Advancing Prompt-Based Methods for GCL" (6.50, prompt-based CL, accepted) — stronger method with more consistent improvements
- Round 2: "Class Incremental Learning via Likelihood Ratio Based Task Prediction" (6.00, CIL, accepted) — method paper, different focus

**Round-1 bracket: 5.5–6.5**

The paper is clearly stronger than the 5.0 anchors (which are rejected papers with limited contributions) and comparable to the 6.25 anchors (accepted papers with solid but not exceptional contributions). The benchmark contribution (task-ID leakage, comprehensive LLM/GLM evaluation) is genuinely valuable and stronger than most graph CL anchors. The method contribution (SimGCL) adds value but is undermined by inconsistent results, missing ablations, and the unspecified backbone. The paper sits above "CLDyB" (5.67, pure benchmark) due to its deeper insight and method addition, but below "N-ForGOT" (6.25) due to its method inconsistencies. The "MISA" paper (6.50) has more consistent method results.

**Final score: 6.0** — The benchmark contribution is strong enough to merit acceptance, but method issues (unspecified backbone, inconsistent results over SimpleCIL, missing ablations, misleading "20%" claim) prevent a higher score.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>