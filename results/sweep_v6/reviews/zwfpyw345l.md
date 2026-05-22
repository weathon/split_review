Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper proposes a hierarchical code embedding model (CodeTransformer-GAT) that combines token-level, function-level, and module-level attention with graph-structured dependencies, intended as state representations for reinforcement learning agents operating on code. The model is evaluated on three code-related tasks — code completion (PY150), program repair (ManySStuBs4J), and algorithmic problem solving (APPS) — against five baselines. Results in Table 1 show consistent improvements (e.g., 72.9 vs. 68.4 BLEU for code completion over CodeBERT), and an ablation study attempts to isolate the contribution of each hierarchical level.

## Strengths

- **Consistent empirical advantage across three tasks (Table 1).** The proposed model outperforms all five baselines on every metric: Code Completion BLEU (72.9 vs. 68.4), Program Repair Success Rate (54.3% vs. 48.6%), Algorithmic Solving Pass Rate (67.5% vs. 61.3%), and Average Reward (0.74 vs. 0.67). The margin is non-trivial — about 4–6 absolute points on each task.
- **Ablation study confirms each component contributes (Table 2).** Systematically removing token-level, function-level, and module-level attention each degrades performance (by –6.2%, –3.6%, –2.4% respectively on the program repair task), and removing CDG edges drops success rate by 1.9%. This provides evidence that the multi-level design and graph dependencies each add measurable value.
- **Task-dependent attention specialization (Section 6.3).** The paper reports that module-level attention distances differ by task (2.1 edges for code completion vs. 3.8 edges for program repair), suggesting the hierarchical attention adapts its focus to task-specific structural demands rather than applying a fixed pattern.

## Weaknesses

### Fatal

None.

### Major

- **The submission is in an unfinished state, which undermines trust in the entire work.** Section 7.1 is literally a placeholder: its full content is "Need to discuss several limitations of this study." Multiple sentences throughout the paper are fundamentally incoherent — e.g., the conclusion states "The hierarchical cherry-picking of the code embedding system with multi-level attention Research into mechanisms provides major breakthrough in reinforcement learning state representation for code related task" — which is not a parser artifact but a composition failure. The abstract describes "exciting results with Neural Investigations." A paper with a placeholder limitation section and a nonsensical conclusion cannot be evaluated as a finished submission. The "Use of LLM" statement (Section 9) confirms heavy LLM assistance, but the level of incoherence suggests insufficient human oversight of the generated text.

- **No MDP specification for any of the three RL tasks.** Despite framing all three tasks as RL problems, the paper provides exactly one sentence of MDP description: "Each task was implemented as a Markov Decision Process (MDP) where states represent the current program state and actions correspond to valid code modifications or additions" (line 169). No state space, action space, reward function, transition dynamics, or episode termination condition is formally defined for any task. "Code Completion" with PY150 as "predict the next token" is described with "rewards based on prediction accuracy and semantic correctness" — neither term is operationalized. "Algorithmic Problem Solving" on APPS (a text-to-code generation benchmark) recast as RL receives no MDP definition at all. Without these definitions, the experimental setup is not reproducible and the reported numbers cannot be independently verified.

- **No variance reported on any quantitative result, despite claiming statistical tests.** All numbers in Tables 1 and 2 are point estimates. No standard deviations, confidence intervals, or p-values are reported anywhere, even though line 219 states "statistical significance tested via paired t-tests (p < 0.01)." No t-statistics or actual p-values appear. Every result in the field of RL requires multi-seed reporting; its absence makes the reported improvements — including the 4–6 point margins — uninterpretable as meaningful signal rather than noise.

- **Weaknesses in the baseline setup reduce confidence in the comparisons.** (a) Flat-GAT is described as "a graph attention network applying uniform attention across all nodes regardless of hierarchy" — but GATs (Veličković et al., 2017) by definition compute *non-uniform* attention weights via a learned mechanism, so this description is contradictory and unclear. (b) CodeBERT is a pre-trained encoder; the paper states it is "fine-tuned for RL" but provides no details on how its output was adapted to a policy network. (c) No hyperparameter search is reported for any baseline; all models are simply listed with the same RL algorithm, but whether each baseline's hyperparameters were independently tuned is unspecified.

### Minor

- **No comparison against strong hierarchical code models that already exist.** SG-Trans (Gao et al., 2023, cited in the paper), GraphCodeBERT, and syntactic GNNs are not included as baselines, even though the paper's core claim is about the value of hierarchical attention for code. Without these comparisons, it is unclear whether the gains come from the specific hierarchical design or simply from having more parameters / more attention mechanisms than the baselines used.

- **The "Uniform Attention" variant in the ablation (49.8% vs. 54.3% full model) shows only a 4.5% drop.** This suggests that a model with uniform cross-level mixing performs reasonably close to the full hierarchical design, which somewhat undercuts the claim that the level-specific attention is critical. This deserves more discussion than the paper provides.

- **The scalability analysis (Figure 3) reports 0% prediction error at 0 functions** — an artifact of how the x-axis is labeled, but the data showing trivial code having error-free prediction is unrealistic and the figure styling choices are not adequately explained. Also, "Baseline 1" and "Baseline 2" are never identified in the caption or text.

- **The paper claims the model learns "embeddings end-to-end for the RL objective"** but provides no analysis comparing the learned embeddings to frozen pre-trained embeddings, leaving it unclear whether the RL fine-tuning actually changes the representations meaningfully.

### Trivial

None.

## Nice-to-Haves

- A formal MDP specification (state, action, reward, transition, termination) for each of the three tasks would be needed for reproducibility.
- Reporting means and standard deviations over multiple seeds is standard practice in RL and should be added.
- Including SG-Trans, GraphCodeBERT, or a syntactic GNN as baselines would strengthen the claim that hierarchical attention specifically drives the improvement.
- A t-SNE plot of the learned state space (which the paper mentions in Section 6.4 but does not show) would help illustrate the representation quality claim.
- Specific examples of attention patterns at each hierarchical level would strengthen the analysis in Section 6.3.

## Removed Points

These points were flagged by the reviewers but are either factually incorrect, misunderstanding the paper, or violate the hard rules:

- **"Citations to Zhang et al., 2025 and Guo et al., 2025 are from future or same-year work that cannot be verified."** From the current date (May 2026), 2025 is last year, not future. This reflects a reviewer knowledge gap, not an author error. **Removed per rule: do not question the existence of cited references.**
- **"The description of SALE is inaccurate."** The paper states SALE learns "joint embeddings" — the method's own name (State-Action Learned Embeddings) confirms it learns joint state-action embeddings. The paper's description is accurate. **Removed.**
- **Generic suggestion to "evaluate on standard code representation benchmarks"** (clone detection, code classification) to disentangle embedding quality from RL dynamics. This is outside the paper's stated scope (RL state representation) and demands the paper solve an entirely different evaluation paradigm. **Moved here as scope creep.**
- **"The paper misrepresents prior work by claiming traditional approaches ignore hierarchical code models"** while the related work cites some of these. This is a contradiction that the reviewer points out but the paper's claim is about *RL-specific* hierarchical models, not hierarchical models in general. The phrasing is imprecise but not a deliberate misrepresentation. **Demoted.**
- **Pure formatting/style nitpicks** (figure choices, table formatting, LaTeX issues). **Removed.**
- **Vague suggestion about "concrete examples of hierarchical embeddings" with t-SNE plots.** The paper mentions t-SNE but does not show it; this is noted in Minor weaknesses above. The stronger demand for specific visualizations is a nice-to-have, not a core weakness. **Moved to Nice-to-Haves.**

## Novel Insights

None beyond the paper's own contributions. The reviews raise valid concerns about the paper's completeness and methodological rigor but do not identify any new scientific insight or alternative interpretation of the results that the paper itself missed.

## Suggestions

1. Address the single most damaging issue: the submission must be finished. Replace the placeholder Section 7.1 with a genuine limitations discussion, and rewrite the incoherent passages (especially the conclusion, abstract, and introduction) so the paper makes sense as a whole. Do not rely on LLM writing without thorough human editing.
2. Provide explicit MDP definitions — state space, action space, reward function, transition dynamics, and termination conditions — for each of the three tasks, ideally in an appendix. Without these, the experimental setup is not reproducible.
3. Report means and standard deviations over at least 5 random seeds for all tables, and report the actual p-values or test statistics for the claimed t-tests.
4. Correct the misleading description of Flat-GAT (GATs do not apply "uniform attention"), and provide more detail on how CodeBERT was adapted for RL fine-tuning.
5. Add at least one strong hierarchical code baseline (e.g., SG-Trans, GraphCodeBERT) to the comparison to demonstrate that the gains come from the specific design rather than from adding capacity.

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `mrBd4hyWlP.md` (CRL-Net) | 1.67 | MRI paper with poor writing and weak experimental validation. The current paper is slightly better: it has a coherent (if underspecified) method and more extensive experiments, but shares similar writing quality issues. |
| `OXIIFZqiiN.md` (IGCP) | 1.50 | LLM-generated-looking paper with nonsensical content. The current paper is above this — its method is at least describable and the experiments produce numerical results. |
| `N18Z2MkMEa.md` (FALCON) | 3.00 | Code+RL paper with presentation issues and unclear methodology but coherent writing. The current paper is weaker — it has a placeholder section and fundamentally broken sentences that FALCON does not. |
| `vLqkCvjHRD.md` (Coarse-Tuning) | 4.75 | Decent RL-for-code paper with clear motivation and solid (if limited) experiments. The current paper is substantially below this — Coarse-Tuning has clear writing, proper experimental design, and is a finished submission. |
| `vfzRRjumpX.md` (CodeSage) | 5.75 | Well-executed code representation paper with thorough experiments. The current paper is far below this in both execution quality and completeness. |
| `OwtMhMSybu.md` (DETOCS) | 7.33 | Strong RL paper with clear methodology and state-of-the-art results. Not comparable in quality. |

The paper's core ideas (hierarchical code attention, optimizing for RL objectives) are reasonable but the submission is in an unfinished state. A placeholder limitation section, a nonsensical conclusion, and multiple incoherent sentences indicate the paper was submitted before the authors completed their writing and analysis. The missing MDP definitions and lack of variance reporting mean the experimental results cannot be properly evaluated, even if the underlying method is sound. Against the calibration anchors, the paper is closest to the ~2.5–3.0 band: above papers that are clearly nonsensical (IGCP at 1.50) but below papers that at least have coherent writing and complete sections (FALCON at 3.00).

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>