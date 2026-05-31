Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper makes two core contributions: (1) identifying and empirically demonstrating a task-ID leakage flaw in the standard local-testing protocol used in graph continual learning (GCL), and (2) introducing LLM4GCL, a benchmark for evaluating LLM-based and graph-enhanced LLM methods under a corrected global-testing protocol on 7 text-attributed graph datasets with 15 baselines. The paper also proposes SimGCL, a method combining first-session LoRA-tuned LLM instruction tuning with training-free prototype classification, which achieves state-of-the-art results on most datasets (often by 15–20+ percentage points).

## Strengths

1. **Clear identification of task-ID leakage in GCL evaluation (Section 3.1, Table 1).** The paper provides concrete, reproducible evidence that even a basic mean-pooling operation achieves 100% task-ID prediction accuracy under local testing, matching the previous SOTA (TPP) while being far simpler. This is a genuine methodological contribution — GCL papers using the local-testing protocol have been unknowingly evaluating a fundamentally easier task.

2. **Strong empirical performance on most datasets (Table 2).** SimGCL achieves large, practically meaningful gains over prior methods on 6 out of 7 datasets in NCIL (e.g., Cora: 84.6 vs. 70.8, Photo: 82.1 vs. 63.6, Products: 71.1 vs. 66.8). The margins are not incremental.

3. **Systematic analysis of why GLMs underperform in GCL (Obs. 3, Section 4).** The paper goes beyond a simple ranking to provide a structured decomposition: (a) LLM-as-Enhancer methods inherit GNN bottlenecks and overfit in few-shot settings, and (b) LLM-as-Predictor methods suffer from LLM-GNN representation misalignment during incremental updates. This analysis is evidence-backed and useful for future research.

4. **Controlled session-configuration analysis (Table 4).** Varying both class-per-session width (2W–8W) and session count (5S–20S) on Arxiv, the paper shows that prototype-based methods (Cosine, SimpleCIL, SimGCL) maintain stable performance while other methods degrade severely as sessions increase. This isolates a key design principle.

5. **Scaling-law evidence in the GCL context (Figure 3).** Demonstrating that larger LLM backbones consistently improve performance across all task sessions for both SimpleCIL and SimGCL adds concrete grounding for the value of pretrained models in GCL.

6. **Clear rehearsal-free scope.** The paper explicitly commits to rehearsal-free methods and justifies this by real-world privacy and storage constraints, making the comparisons fair within this defined scope.

## Weaknesses

### Fatal

None.

### Major

1. **SimGCL's advantage over SimpleCIL on Arxiv-23 reverses without adequate explanation.** On Arxiv-23 (sparse graph) in NCIL, SimGCL achieves 38.7/13.6 vs. SimpleCIL's 52.4/38.8 — a substantial *deficit* (Table 2). The same pattern holds in FSNCIL (31.8/10.3 vs. 49.8/40.0, Table 3). The paper's explanation ("sparse graph structure provides limited topological information, potentially compromising LLMs' structural comprehension") does not explain why graph-structured prompts would *actively hurt* relative to using no graph structure at all (SimpleCIL). If graph prompts are uninformative, the model should fall back to text-only performance, not underperform it. This suggests graph prompts may introduce noise or distribution shift on sparse graphs — a failure mode the paper neither resolves nor adequately analyzes. Since this is the strongest evidence against the paper's structural-awareness narrative, it weakens the core claim about graph prompts.

2. **Missing ablation to separate the contributions of graph prompts from first-session LoRA tuning.** SimGCL's claimed novelty over SimpleCIL involves two factors: (a) graph-structured prompts and (b) first-session LoRA instruction tuning. SimpleCIL has neither. The paper never runs the obvious control: **LLM + first-session LoRA tuning + prototype classification WITHOUT graph prompts.** Without this, it is impossible to attribute SimGCL's gains to graph-aware prompting vs. simply the first-session tuning improving representation quality before prototype extraction. The paper's Obs. 8 attributes success to "graph-structured instruction tuning and prompting framework enhanc[ing] LLMs' comprehension of graph topology," but the evidence for this specific attribution is absent. Given that SimpleCIL already closes much of the gap on several datasets (e.g., WikiCS: SimpleCIL 71.4 vs. SimGCL 73.5; Arxiv: SimpleCIL 50.6 vs. SimGCL 59.9), the *incremental* value of graph prompts is unclear without this ablation.

3. **No variance or statistical significance reporting.** All results in Tables 2, 3, and 4 are reported as single-point estimates with no standard deviations, confidence intervals, or significance tests. For a paper that aims to establish a benchmark and evaluation standard, this is a notable omission — readers cannot assess whether the reported differences are statistically meaningful. Multiple random seeds with variance reporting are standard practice for benchmark papers in this field (cf. CLDyB at 5.67, which included such reporting and was accepted).

### Minor

1. **SimGCL backbone not explicitly stated for main results.** The paper does not clearly state which LLM backbone produces the SimGCL results in Table 2. Figure 3 suggests RoBERTa-large (355M), but this should be stated explicitly in the experiment section.

2. **Hyperparameters not reported.** The scaling parameter τ in Equation (2), LoRA rank and target modules, and learning rate are not reported in the main text. The appendix was stripped by the parser, but these details should be in the main paper.

3. **Prompt templates not shown in full.** The graph prompt template is described in prose (Section 3.3) but never shown verbatim. Since prompt design is a claimed contribution, the full template should be included for reproducibility.

4. **No efficiency analysis.** The paper claims efficiency from single-session training as a stated advantage over multi-session approaches, but provides no wall-clock time, FLOPs, or parameter-count comparisons to substantiate this.

5. **TPP included as a GNN baseline despite being designed for local testing.** While the paper correctly explains why TPP fails under global testing, including TPP in the "GNN-based method" comparison (where it achieves 45.7 vs. GCN's 57.0 on Cora) somewhat inflates the apparent GNN-baseline gap. This is a minor presentational issue since the paper does identify the reason for TPP's failure.

### Trivial

None.

## Nice-to-Haves

- Adding the critical ablation: SimGCL vs. LLM+first-session LoRA tuning+prototype *without* graph prompts. This would cleanly separate the value of graph-aware prompting from instruction tuning, and either strengthen or refine the paper's core claim.
- Variance reporting across 3–5 random seeds for all main results.
- A direct analysis of prediction shifts on Arxiv-23: what percentage of predictions change from correct to incorrect when adding graph prompts? Are errors concentrated on nodes where graph structure conflicts with text content?
- Including the full prompt template text in an appendix or main paper.
- Efficiency benchmarks (wall-clock time, parameter counts).

## Removed Points

These points were raised by the harsh critic or strength finder but removed from the main review for the following reasons:

1. *"LLM baselines are underutilized / unfair comparison"* — Removed. The paper includes SimpleCIL (a strong LLM+prototype baseline). The naive fine-tuning baselines (BERT, RoBERTa, LLaMA) are standard comparisons; their poor performance is expected and informative. The comparison is not structurally unfair.
2. *"GNN baselines may be undertuned"* — Removed. Pure speculation with no evidence.
3. *"No evaluation on non-TAGs"* — Removed. Scope is explicitly text-attributed graphs (Section 2: "In this benchmark, we evaluate the continual learning capabilities of LLMs through node classification tasks on Text-Attributed Graphs (TAGs)").
4. *"GLM implementations may be suboptimal"* — Removed. Speculative, no evidence of implementation mismatch.
5. *"Overstates novelty about being first to analyze flaws"* — Removed. The paper is the first to identify and demonstrate this *specific* evaluation flaw in GCL. The broader task-vs-class-incremental distinction is well-known, but its specific manifestation through graph subgraphs in GCL is a new contribution.
6. *"Rehearsal-based methods should be included"* — Removed. The paper explicitly scopes to rehearsal-free methods and justifies this choice. Criticizing this is scope creep.
7. *Strength: "Important problem"* — Removed as generic/superficial; not specific to this paper.
8. *Strength about "addressed an important question"* — Removed as generic.

## Novel Insights

The reviewer synthesis surfaces one genuinely novel observation that goes beyond the paper's own contributions: the Arxiv-23 failure pattern (SimGCL underperforming SimpleCIL) suggests a potentially systematic limitation of graph-prompt-based approaches on sparse graphs. Existing GCL and GLM papers typically report average performance and treat sparse graphs as merely "challenging," but the reversal pattern here — where injecting structural information actively harms performance — hints that graph prompts may introduce noise or distribution shift rather than useful signal when structure is sparse. This is a testable hypothesis: one could measure whether SimGCL's prediction errors on Arxiv-23 are concentrated on nodes with low-degree neighborhoods (where the ego-graph prompt contains little informative structure). If confirmed, this would be a useful design constraint for future graph-enhanced LLM methods. The paper's own explanation ("limited topological information compromising structural comprehension") does not account for the *negative* effect relative to ignoring structure entirely.

## Suggestions

1. Run the critical ablation: SimGCL vs. LLM + first-session LoRA tuning + prototype — without graph prompts. This single experiment would cleanly separate the value of graph-aware prompting from instruction tuning.
2. Add variance/std reporting for all main results. Even 3 random seeds would substantially improve reliability.
3. Analyze the Arxiv-23 failure: compare prediction changes between SimpleCIL and SimGCL on a per-node basis. Show whether errors concentrate on low-degree nodes.
4. Report backbone choice, τ, LoRA rank/target modules, and full prompt templates explicitly.
5. Consider reframing the SimGCL contribution more cautiously — it is a strong combination of existing ideas (LoRA tuning + prototype classification + graph prompting), not a fundamentally new architecture.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- **Weak band** (avg < 3.5): `ZHTYtXijEn.md` (2.33), `SI6zocV2SS.md` (1.50), `ZyMXxpBfct.md` (1.50), `kf9phcBvQ5.md` (3.00) — These are substantially weaker: fundamental methodological errors, no proper evaluation, or purely conceptual. The current paper is far stronger.
- **Middle band** (avg 3.5–7.5): `4sJJixGIZX.md` (5.00, Reject), `MB53uAZKSc.md` (6.25, Reject), `CkKEuLmRnr.md` (7.00, Accept), `RnxwxGXxex.md` (5.67, Accept) — These are the most relevant peers.
- **Strong band** (avg > 7.5): `07yvxWDSla.md` (8.00), `KbetDM33YG.md` (8.00), `PdaPky8MUn.md` (8.00), `P7KIGdgW8S.md` (8.00) — Clearly stronger: polished, theoretically grounded, or definitive benchmarks.

**Bracket:** 5.0–6.5

**Round 2 (Narrowing):**
- `4sJJixGIZX.md` (5.00, Reject) — Online Continual Graph Learning. Both are benchmark papers, but current paper is stronger: has a novel method contribution and identifies an evaluation flaw. OCGL was criticized for lacking algorithmic novelty and using dated baselines.
- `RnxwxGXxex.md` (5.67, Accept) — CLDyB: dynamic benchmarking for CL with PTMs. Similar profile (benchmark + analysis). Current paper is comparable in contribution weight but CLDyB is more polished. The current paper's identification of task-ID leakage is a more concrete contribution, but CLDyB's dynamic benchmark idea is more novel.
- `MB53uAZKSc.md` (6.25, Reject) — TiC-LM: large-scale continual pretraining benchmark. Stronger data-scale contribution, but rejected. Current paper is slightly weaker in benchmark scale but has a novel method.
- `EzExZ5d8ES.md` (4.75, Reject) — DyMoE for incremental graph learning. Current paper is clearly stronger: broader evaluation, cleaner problem identification.

**Final score placement:** The paper is better than OCGL (5.00) and DyMoE (4.75), comparable to CLDyB (5.67) but with less polish, and weaker than TiC-LM (6.25, rejected) in terms of benchmark scale. The missing ablation, variance reporting, and unexplained Arxiv-23 failure prevent it from reaching the 6+ range, but the evaluation flaw identification and strong empirical results on most datasets make it a clear step above the rejected GCL papers in the 4-5 range.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>