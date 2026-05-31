Now let me run calibration searches to properly score this paper.Initial bracket: **5.0 to 6.5**. The paper is stronger than the "Online Continual Graph Learning" (5.0, Reject) with a more impactful evaluation flaw analysis and a proper method contribution, but perhaps not as polished as the CLDyB (5.67, Accept) or TiC-LM (6.25, Reject). Let me narrow this.Now I have enough to write a comprehensive final review. Let me verify one more specific claim before writing.---

## Summary

This paper investigates whether LLMs can mitigate catastrophic forgetting in Graph Continual Learning (GCL). It makes three contributions: (1) identifying and demonstrating a fundamental task ID leakage flaw in the widely-used local testing evaluation protocol, (2) proposing the LLM4GCL benchmark covering 7 text-attributed graph datasets, 9 LLM-based/GLM-based methods, and two paradigms (NCIL, FSNCIL) under a corrected global testing protocol, and (3) proposing SimGCL, a method combining ego-graph-derived prompts with first-session LoRA tuning and a subsequent training-free prototype classifier that outperforms existing baselines on most evaluated datasets.

---

## Strengths

- **Task ID leakage identification is concrete and decisively demonstrated.** Section 3.1 and Table 1 show that under local testing, even a basic MLP with mean pooling achieves 0% forgetting and near-identical accuracy to the state-of-the-art TPP across all seven datasets (e.g., 90.3% vs. 95.2% AA on Cora). This reduces class-incremental learning to task-incremental learning and directly invalidates existing local-testing evaluations in GCL. This is a genuine, impactful contribution for the field.

- **Comprehensive benchmark design.** LLM4GCL provides a multi-domain, multi-scale evaluation spanning 7 datasets, 9 LLM-based methods, both NCIL and FSNCIL paradigms, and the corrected global testing protocol. Table 2 and 3 enable the first systematic apples-to-apples comparison of LLMs and GLMs for GCL.

- **SimGCL achieves large, consistent gains on most benchmarks.** SimGCL outperforms all baselines in 23 out of 28 dataset-metric combinations (Tables 2–3), with absolute improvements over the best GNN baseline of up to ~20% on Cora NCIL (84.6 vs. 65.4), 18.5% on Photo NCIL (82.1 vs. 63.6), and 35% on Products NCIL (71.1 vs. 36.1). These gains are achieved without any replay of historical data.

- **Prototype-based scalability analysis (Table 4) is an actionable finding.** The paper shows that prototype-based methods (Cosine, SimpleCIL, SimGCL) maintain stable or improving average accuracy as sessions increase (SimGCL rises from 51.6 at 5 sessions to 57.4 at 20 sessions on Arxiv), while all other methods degrade. This is a concrete design principle for practitioners.

- **Analytical insight into GLM failure modes.** The paper clearly separates LLM-as-Enhancer failures (GNN bottleneck, compounded forgetting) from LLM-as-Predictor failures (cross-architecture misalignment, over-adaptation to recent tasks), backed by consistent patterns across Tables 2 and 3.

---

## Weaknesses

### Fatal
None.

### Major

- **SimGCL's key claimed innovation—graph-structured prompting—is never ablated from LoRA fine-tuning.** SimGCL adds two components over SimpleCIL: (i) ego-graph-derived graph prompts, and (ii) first-session LoRA fine-tuning. No ablation isolates these. This means the substantial gains (e.g., +13.8% on Cora NCIL, +20.0% on Photo NCIL) cannot be attributed to the graph-structural component specifically, rather than to LoRA fine-tuning alone. Critically, the cases where SimGCL *underperforms* SimpleCIL—Arxiv-23 NCIL (38.7 vs. 52.4 $\bar{\mathcal{A}}$), Arxiv-23 FSNCIL (31.8 vs. 49.8), and Arxiv FSNCIL (36.3 vs. 46.4)—suggest LoRA fine-tuning can cause overfitting that overwhelms any structural benefit. Without the ablation (SimpleCIL → SimpleCIL+LoRA → SimGCL), the contribution of graph prompts is not established.

- **SimGCL's failures on Arxiv-23 and FSNCIL on Arxiv are only partially explained.** The paper acknowledges these anomalies in Obs. ⑧, attributing them to "sparse graph structure of Arxiv-23" and "expanded tuning set promoting overfitting." However, Arxiv-23 is not among the sparsest datasets, and the overfitting hypothesis for FSNCIL is asserted without supporting evidence. These systematic failures on two of seven datasets remain unexplained, weakening confidence in the robustness of the method.

### Minor

- **The headline claim of "~20% improvement over GNN-based SOTA" partially conflates protocol switch with method quality.** Under local testing, TPP achieves 89.6% on Products; under global testing it drops to 15.0% (Table 2). GNN methods were designed and tuned for local testing and never had a chance to adapt. The 20% gap measures both "protocol harm to GNNs" and "SimGCL quality." The true method improvement should be measured against LLM-based baselines that also run under global testing, where the gains are more modest on some datasets.

- **No oracle/upper-bound baseline is reported.** Without a joint training or non-continual performance ceiling, it is impossible to assess what fraction of the problem remains unsolved. On Products, the best method achieves 71.1% (SimGCL), but without knowing if the non-continual ceiling is 72% or 90%, this result cannot be contextualized.

### Trivial

- **The hyperparameter τ in Eq. 2 is introduced with no discussion** of how it is set or its sensitivity, limiting reproducibility of prototype classification.

---

## Nice-to-Haves

- **Ablation of SimGCL's components** (SimpleCIL baseline → +LoRA only → +graph prompts only → full SimGCL): this is the single most valuable addition and would directly confirm or refute whether graph-structured prompting carries independent value. This would substantially clarify the paper's method claim.
- **Reporting variance** across runs (standard deviation over multiple random seeds) would allow readers to assess whether small pairwise differences (1–5%) are reliable.
- **Joint training / non-continual oracle results** on each dataset to provide an upper bound for interpreting absolute performance numbers.
- **Analysis of when graph prompts help vs. hurt**: the paper identifies graph density (Obs. ④) as a factor but does not connect it cleanly to the Arxiv-23 anomaly; a deeper analysis of prompt length, neighborhood size, and overfitting would be useful.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Table 4 reports SimGCL without reporting SimpleCIL"** (harsh critic): **Factually incorrect.** SimpleCIL is explicitly present in Table 4 (line 188 in the paper text). Removed.

- **Observations numbering (skipping ⑤ and ⑦)**: The apparent skip in observation numbering (❶, ❷, ❸, ④, ⑥, ❽) is a PDF parsing artifact, not a paper error. Removed per the hard rule on formatting artifacts.

- **Ego-graph implementation details (hop count, tokenization, large-degree handling)**: Removed as a reproducibility nitpick. The paper provides enough detail for the approach to be understood; full implementation is expected in code.

- **"GNN methods should have been re-tuned/adapted for global testing"**: Removed under the hard rule — asymmetry favors the baseline, not the authors' method. If anything, the worse GNN results under global testing strengthen the authors' argument that LLM-based approaches are preferable under realistic evaluation.

- **Strength Finder: "SimGCL achieves large, consistent gains over all baselines"**: Partially removed/modified. As verified, SimGCL underperforms SimpleCIL on 5 out of 14 FSNCIL/NCIL dataset-metric pairs (Arxiv-23 both settings, Arxiv FSNCIL both metrics, WikiCS FSNCIL $\bar{\mathcal{A}}$). Reframed above as "most benchmarks."

- **Strength: "Scalability: SimGCL's Ā rises from 51.6 at 5 sessions to 57.4 at 20 sessions"** (Strength Finder): Kept as valid, but noted that this pattern is also shown by SimpleCIL without the graph-prompt component.

---

## Novel Insights

The most novel insight beyond the paper's own contributions is the observation that task ID leakage in graph continual learning is **structurally baked into the local testing protocol** (not merely an exploitable side-effect): because each test graph $\mathcal{G}_{q_j}$ is defined to equal the training subgraph $\mathcal{G}_{s_j}$, the test graph *is* the task ID — there is no information gap to close. This is subtly different from the paper's framing (which emphasizes that pooling can *predict* task IDs), and it implies that any method performing well under local testing should be considered suspect, not just methods that explicitly exploit task IDs. The corollary is that under-performing GNN methods in Table 2 may still be quite capable once properly re-evaluated, and the performance rankings in prior GCL literature may be even more compromised than the paper demonstrates.

---

## Suggestions

1. **Run the three-way ablation**: SimpleCIL (no graph prompts, no LoRA) → SimpleCIL+LoRA (no graph prompts) → SimGCL (both). Report results on at least Cora, Arxiv-23, and one FSNCIL dataset. This directly addresses the most significant weakness.
2. **Report joint-training (non-continual) upper bounds** for each dataset as a single row in Tables 2–3. This requires no new method development and costs little compute.
3. **Investigate Arxiv-23 more carefully**: compare SimGCL's graph prompt lengths/truncation behavior against denser datasets to test the sparse-graph hypothesis empirically.
4. **State the τ hyperparameter value and its tuning procedure** in the main text or an appendix table.
5. **Reframe the abstract's "~20% over GNN-based SOTA"** to clarify that this is under the new global testing protocol, and that the gain over the strongest LLM-based method (SimpleCIL) is the more informative comparison for method novelty.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: High — task ID leakage identification is original and impactful; SimGCL is simple but combines elements from prior work.
- *Importance of research question*: High — GCL evaluation validity and LLM applicability to graph continual learning are genuinely important.
- *Claims well-supported*: Moderate — the evaluation flaw and benchmark findings are well-supported; SimGCL's performance is demonstrated but the contribution of graph prompts specifically is not established due to the missing ablation.
- *Soundness of experiments*: Moderate — comprehensive dataset and method coverage, but no variance, no oracle, and unexplained failures on Arxiv-23 weaken confidence.
- *Clarity of writing*: Good — generally well-organized; observations are clear.
- *Value to research community*: High — the evaluation flaw finding and LLM4GCL benchmark are genuinely useful.

**Calibration anchor comparison:**
| Paper | Avg Score | Round | Comparison |
|---|---|---|---|
| WRKVA3TgSv (LLMs Modify Graphs) | 3.00 | R1 | Much weaker; no evaluation critique, no method |
| 4sJJixGIZX (Online Continual Graph Learning) | 5.00 | R1/R2 | Weaker; graph CL benchmark without evaluation flaw finding; no method novelty |
| RnxwxGXxex (CLDyB) | 5.67 | R1/R2 | Comparable; both are benchmark + critique of existing evaluation; this paper's finding is more impactful but method is less robustly validated |
| mLTbDVzHVh (Hierarchical Prompt CL) | 5.25 | R2 | Weaker method contribution, similar benchmark scope |
| GURRWHkPtx (Language Models are Graph Learners) | 5.50 | R2 | Similar topic (LM+graph node classification), narrower scope, no continual learning, rejected |
| MB53uAZKSc (TiC-LM) | 6.25 | R1/R2 | Benchmark of similar scale; that paper was rejected for "benchmark alone is insufficient" — same concern applies here partially, mitigated by SimGCL method |
| TLADT8Wrhn (TiC-CLIP) | 6.25 | R2 | Larger-scale benchmark, stronger engineering but less conceptual novelty than the task ID leakage finding |
| KbetDM33YG (Online GNN Eval) | 8.00 | R1 | Much stronger — rigorous theory + extensive evaluation; not comparable |

**Round 1 bracket**: 5.0–6.5

**Round 2 narrowing**: The paper is stronger than Online Continual Graph Learning (5.00, Reject) because of the task ID leakage finding and the actual method contribution. It is comparable to but slightly weaker than CLDyB (5.67, Accept) and TiC-CLIP (6.25, Accept): it has a more impactful single finding but a less robustly ablated method. The missing ablation is the key limiter — without it, SimGCL's contribution beyond SimpleCIL+LoRA is not established, which undermines a core claim. The paper sits closer to the 5.0–5.67 range than to 6.25.

**Final score: 5.5, Reject.** The benchmark and evaluation flaw contributions are solid and worth disseminating, but the missing ablation is a genuine evidential gap for the method's core novelty, and the unexplained performance reversals on Arxiv-23 weaken confidence in SimGCL's robustness. The paper would be in stronger shape for acceptance with the three-way ablation added.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>