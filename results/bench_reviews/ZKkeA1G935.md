Now I have all the information needed to produce the final consolidated review.

## Summary

This paper introduces LLM4GCL, a benchmark for evaluating LLMs and graph-enhanced LLMs on graph continual learning (GCL). It makes three contributions: (1) identifying a task-ID leakage flaw in the prevalent local-testing evaluation protocol for node-level class-incremental learning (NCIL); (2) providing a systematic benchmark with 7 text-attributed graph datasets and 16 methods (9 LLM/GLM-based); and (3) proposing SimGCL, a method that combines graph-prompted instruction tuning (with LoRA, first session only) with training-free prototype classification. SimGCL achieves SOTA on most metrics, with gains of up to 21.7% over the best GNN baseline.

## Strengths

- **Exposure of a fundamental evaluation flaw in GCL.** The paper demonstrates that local testing (where each task's test nodes come from that task's subgraph) allows trivial task-ID inference — even simple mean pooling over the test subgraph achieves 100% task ID prediction and zero forgetting. This is a genuine, field-wide contribution that should influence how GCL research designs its evaluation protocols going forward.

- **First comprehensive benchmark of LLMs/GLMs for GCL.** The benchmark integrates 16 methods across 7 diverse text-attributed graph datasets spanning citation, web link, and e-commerce domains, covering both NCIL and few-shot (FSNCIL) scenarios. This provides a standardized infrastructure where none existed before, and the released open-source platform lowers the barrier for future research.

- **SimGCL achieves strong performance across most settings.** SimGCL is the top performer on 6/7 NCIL datasets (average accuracy) and 4/7 FSNCIL datasets, with substantial margins on several (e.g., +19.2% on Cora NCIL over SimpleCIL, +14.9% on Photo FSNCIL). The design — single-session instruction tuning + frozen prototype matching — is computationally efficient and well-motivated.

- **Useful analysis of prototype-based methods in GCL.** Observation 6 (prototype-based learning improves cross-task generalization) is well-supported: Cosine, SimpleCIL, and SimGCL all outperform non-prototype baselines, providing actionable insight for the field. The scaling analysis (Figure 3) showing that larger LLM backbones improve GCL performance is also informative.

## Weaknesses

### Fatal
None.

### Major

- **Missing ablation study for SimGCL's components.** SimGCL combines: (a) ego-graph prompt design, (b) instruction tuning with LoRA (first session only), (c) prototype-based classification. Without ablations, it is impossible to attribute performance gains to specific components. For example, how much of the gain comes from instruction tuning vs. the graph prompt vs. simply using a frozen LLM backbone with prototypes? The closest baseline (SimpleCIL) also uses a frozen backbone + prototypes but differs in backbone choice and prompt design. An ablation comparing SimGCL with a plain text prompt (no graph structure), or without instruction tuning (frozen LLM + graph prompt + prototype), is needed to validate the design choices.

- **No uncertainty quantification.** No standard deviations, confidence intervals, or statistical significance tests are reported for any metric. Given that GCL results can be sensitive to random seeds, task ordering, and the few-shot nature of FSNCIL, single-run numbers are unreliable for comparing methods. This makes it difficult to assess whether reported improvements (e.g., SimGCL's 19% gain on Cora) are meaningful or within noise.

### Minor

- **Overclaim of "consistent" superiority (Obs. 8).** The paper titles Obs. 8 "SimGCL consistently overperform[s]" baselines, but the data show that SimpleCIL outperforms SimGCL on Arxiv-23 in both NCIL (52.4 vs. 38.7 avg accuracy) and FSNCIL (49.8 vs. 31.8 avg accuracy), and also on Arxiv FSNCIL (46.4 vs. 36.3 avg). The paper *does* acknowledge these failures in the text ("SimGCL demonstrates relatively inferior performance on the arxiv-23 dataset"), but the headline claim and the title of Obs. 8 are overstated. The method is best on most metrics but not "consistently" superior.

- **Contradiction in Table 4 (varying sessions).** The paper claims prototype methods (including SimGCL) "demonstrate consistent performance stability across all experimental configurations, as their training-free prototype generation mechanism remains unaffected by session variations." However, SimGCL's final accuracy (A_N) drops sharply from 33.8 (4W10S) to 17.5 (2W20S) — a 48% decline — while SimpleCIL stays stable (36.5→39.1). This suggests SimGCL's prototype mechanism does degrade with more sessions (or with fewer classes per session), and the paper provides no discussion of this pattern.

- **LLM backbone for SimGCL is not explicitly stated in the method or table captions.** The main experiments (Tables 2-3) do not specify which LLM backbone SimGCL uses. Figure 3 implies RoBERTa-large (355M) is the default, but this should be stated upfront in Section 3.3 and in all table captions.

- **Task ID leakage analysis operates at the subgraph level, not per-node.** The paper shows that mean-pooling across the *entire test subgraph* achieves 100% task ID prediction. While the structural flaw is real (separate subgraphs per task leak distributional cues), the evidence does not establish that a *single-node* classifier can infer task ID with 100% accuracy. The paper should either demonstrate per-node leakage or clarify that the issue is about the evaluation protocol enabling implicit task identification at the aggregate level. This does not undermine the contribution, but the framing slightly overstates the strength of the evidence.

### Trivial
None (all minor points are captured above).

## Nice-to-Haves

- Reporting results with multiple random seeds (mean ± std) would substantially strengthen the benchmark's reliability.
- Session-wise accuracy curves (per-task accuracy across sessions) for SimGCL vs. SimpleCIL on representative datasets (e.g., Cora vs. Arxiv-23) would help explain where and why SimGCL's advantage appears or disappears.
- Measuring task ID prediction accuracy under global testing (should be near chance) would provide a cleaner empirical demonstration that global testing fixes the leakage.
- Testing on non-citation graph domains (e.g., social, biological) would test the generalizability of findings.

## Removed Points

- **Formatting/style nitpicks (numbering of observations, etc.):** These are parser artifacts or trivial presentation issues with no bearing on the paper's scientific contribution. Removed per instructions.
- **"Missing related works":** Removed — we cannot independently verify the existence of missing references.
- **Criticism that task ID leakage analysis is "not as clean as presented":** Weakened to minor tier. The reviewer's per-node concern is technically valid but the core finding (local testing allows task inference) is not undermined — even subgraph-level leakage suffices to invalidate the protocol.
- **Strength Finder's claim that SimGCL achieves "consistent performance gains over all existing baselines":** Overclaimed language filtered; kept only the evidence-based version.
- **Abstract being "ambiguous" about the 20% improvement:** The paper specifies "on certain datasets" in the contribution list, so this is adequately scoped.
- **Criticism about TPP's near-zero performance:** The paper already explains this (TPP was designed for local testing). Removed as already addressed.

## Novel Insights

The most striking finding from the review synthesis is the asymmetry between SimGCL's performance on dense vs. sparse graphs: the method excels on Cora, Citeseer, Photo (denser graphs) but underperforms SimpleCIL on Arxiv-23 (sparse). This suggests that the graph-prompted instruction tuning may provide more benefit when there is rich topological structure to encode, and may even hurt when the graph is sparse — a hypothesis the paper mentions in passing but does not systematically test. Additionally, the Table 4 results reveal that prototype methods are *not* uniformly stable: SimGCL's final accuracy collapses in the longest-session (2W20S) setting while SimpleCIL does not, hinting that instruction tuning in the base session may overfit in ways that hurt late-session prototype quality — an explanation that would be testable with the missing ablation study.

## Suggestions

1. Add a component ablation for SimGCL: compare (a) full SimGCL, (b) frozen LLM + graph prompt + prototype (no instruction tuning), (c) SimGCL with plain text prompt (no graph structure), (d) SimGCL with full fine-tuning instead of LoRA. This is the single most important addition.
2. Add standard deviations over at least 3 random seeds to all tables.
3. Tone down the language in Obs. 8 from "consistently overperform" to "generally outperforms" or "achieves best or second-best performance in most metrics (20/28)."
4. Address the Table 4 discrepancy: discuss why SimGCL's A_N drops at 2W20S while SimpleCIL remains stable.
5. Explicitly state the LLM backbone used for SimGCL in Section 3.3 and in every table caption where SimGCL appears.
6. Add a brief discussion or experiment showing that task ID prediction under global testing is near chance, confirming the protocol correction.

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| hEe8IYhyhN.md (IPAL) | 5.00 (Reject) | GCL method paper with 4 datasets, no evaluation critique. Current paper has broader scope and more novel contributions. |
| e6N1ZFY2X1.md (Graph2Hyper) | 4.50 (Reject) | GCIL method with hypernetworks, 4 datasets, 2 classes/task only. Current paper has more comprehensive evaluation. |
| sieYp1CpYk.md (Randomized Reps) | 4.00 (Withdrawn) | Limited novelty (transferring existing idea to graphs). Current paper has stronger novelty. |
| B6t4qcdmM0.md (CAPL) | 2.50 (Reject) | Weak experiments, missing baselines. Current paper is substantially stronger. |
| rMHZfCznhZ.md (RLAP-CLIP) | 6.00 (Accept) | Strong CL method paper with ablations and theoretical analysis. Current paper lacks ablations and has overclaims, making it weaker. |
| cvztBvlglK.md (LMLM) | 6.50 (Accept) | Strong method + theory + experiments. Current paper contributes evaluation critique + benchmark but weaker on method validation. |

The paper has genuine and timely contributions: exposing the task-ID leakage flaw is a service to the GCL community, and the LLM4GCL benchmark fills an important gap. However, the paper's narrative centers on SimGCL as the headline contribution, and this part is weakened by (a) the overstated "consistent superiority" claim, (b) the complete absence of ablations to validate design choices, (c) no uncertainty quantification, and (d) a contradiction in the varying-sessions analysis that the paper does not discuss. These issues are addressable with revisions, but in the current form the paper's central claim about its method is not fully supported by the evidence presented.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>