Now I have a thorough understanding of the paper and the reviews. Let me write the consolidated final review.

---

## Summary

This paper introduces LLM4GCL, a systematic benchmark and study of whether large language models (LLMs) can alleviate catastrophic forgetting in Graph Continual Learning (GCL). The paper makes three contributions: (1) it identifies a genuine flaw in the widely-used *local testing* evaluation paradigm for Node-level Class-Incremental Learning (NCIL), showing that task ID leakage reduces the problem to trivial task-incremental learning; (2) it provides a comprehensive benchmark evaluating 9 methods across 7 text-attributed graph datasets under a more realistic *global testing* setup; and (3) it proposes SimGCL, a simple method combining graph-prompted instruction tuning with training-free prototype classification, which achieves best results on 23 out of 28 evaluated metrics.

## Strengths

- **Identifies a critical and previously undiscussed evaluation flaw in GCL.** The paper is the first to formally demonstrate that the standard *local testing* setup in node-level class-incremental learning suffers from trivial task ID leakage (Table 1). A simple mean-pooling prototype classifier achieves 100% task-ID prediction accuracy and zero forgetting on all seven datasets. This finding directly calls into question the validity of prior GCL results that used local testing and is a genuine methodological contribution.

- **Provides a comprehensive and well-designed benchmark (LLM4GCL).** The benchmark systematically compares 9 methods (GNN-based, LLM-based, and GLM-based) across 7 diverse text-attributed graphs spanning citation networks, web link networks, and e-commerce networks, with varying scale and density. The results (Tables 2, 3, 4) reveal non-obvious findings — e.g., that deliberately designed GLMs underperform pure LLM methods in GCL, and that prototype-based methods are particularly effective — providing actionable guidance for future work.

- **SimGCL achieves substantial and consistent improvements on most evaluations.** Across the NCIL and FSNCIL scenarios, SimGCL outperforms all baselines on 23 out of 28 metrics, with gains of up to ~20% over the next best method on datasets like Cora (84.6% vs. 70.8% average accuracy). The design is clean and well-motivated: single-session instruction tuning with LoRA bridges the distribution gap, while training-free prototype generation avoids parameter-update-induced forgetting.

- **Rigorous analysis of why current GLMs fail in GCL.** The paper provides concrete explanations grounded in experimental observations: LLM-as-Enhancer methods inherit GNN limitations and overfit in few-shot scenarios (Obs. ❸-❶), while LLM-as-Predictor methods suffer from cross-architecture representation misalignment (Obs. ❸-❷). This goes beyond mere reporting of results and offers diagnostic value for future method design.

## Weaknesses

### Fatal
None.

### Major

1. **SimGCL's performance collapses in long-session and certain dataset configurations, and this failure mode is not adequately analyzed.** On Arxiv-23 in the NCIL scenario, SimGCL achieves only 13.6% final accuracy ($\mathcal{A}_N$) versus SimpleCIL's 38.8% — a gap of 25 points. Similarly, in the 2-way 20-session setting on Arxiv (Table 4), SimGCL's final accuracy drops to 17.5% compared to SimpleCIL's 39.1%, despite SimGCL having the highest *average* accuracy (57.4%). This large and systematic gap between average and final accuracy suggests that SimGCL's single-session instruction-tuned representations degrade badly for late-arising classes. The paper's Obs. 8 lumped prototype methods together as exhibiting "consistent performance stability," but SimGCL's 40-point gap between average and final in 2W20S is the opposite of stable. The paper acknowledges inferior performance on Arxiv-23, attributing it to sparse graphs and larger tuning sets, but the 2W20S collapse occurs on the same (denser) Arxiv graph and with identical tuning set size — so the explanation does not cover this case. A deeper analysis of why SimGCL fails in long-session regimes (e.g., prototype bias toward early classes, representation quality degradation over sessions) is needed to substantiate the claim that SimGCL is a generally effective method.

2. **No variance or statistical significance reporting.** Every result in Tables 2, 3, and 4 is reported as a single point with no standard deviation, confidence interval, or mention of number of runs. Many baselines (EWC, LwF, LLM-based methods) involve stochastic components (random splits, weight initialization, training order). Without variance, the reader cannot assess whether SimGCL's reported improvements are robust, especially in cases where metrics are close (e.g., on Arxiv NCIL, SimGCL's $\bar{\mathcal{A}}$ is 59.9 vs. SimpleCIL's 50.6, but $\mathcal{A}_N$ is 33.8 vs. 36.5 — the ordering flips by metric). This is essential for a benchmark paper that aims to establish reliable comparisons.

### Minor

3. **The global testing setup has a residual structural cue that could theoretically be exploited.** Because inter-task edges are removed to prevent knowledge leakage during training, the evaluation graph in global testing consists of disconnected components, each corresponding to a single task's subgraph. While this is far less problematic than local testing (where the model knows *which* graph it is tested on), it is not a complete elimination of task-relevant structural information — a method designed to run connected-components analysis could in principle infer task boundaries. The paper states that global testing "prevents the issue of task ID leakage" without discussing this nuance. This does not invalidate the benchmark (no evaluated method exploits this, and the paper's core findings about LLM/GLM performance stand), but it should be acknowledged as a limitation.

4. **The paper lacks an ablation isolating the effect of graph-structured prompts from the effect of instruction tuning.** SimGCL uses both (a) instruction tuning with LoRA and (b) ego-graph-derived prompts. An ablation comparing SimpleCIL (which uses RoBERTa off-the-shelf) against a variant where SimpleCIL also receives instruction tuning but without graph prompts would isolate whether the gains come from the graph information or from the fine-tuning itself. This limits the ability to attribute SimGCL's improvements to its claimed source (graph structural knowledge via prompts).

### Trivial

- The paper would benefit from specifying ego-graph construction details (e.g., maximum neighborhood size, whether sampling is used) in the main text rather than relegating them to the (removed) appendix.
- Some notation inconsistencies (e.g., $\bar{\mathcal{A}}$ vs. $\bar{A}$ between Tables 2 and 3).

## Nice-to-Haves

- A dedicated limitations section would improve transparency.
- Time and compute cost comparisons across methods (the paper mentions efficiency for SimGCL but provides no wall-clock or FLOP comparisons).
- Analyzing prototype-based methods vs. linear classifiers as an additional control condition.
- For Observation ❹ (dense graphs help GLMs), an ablation that artificially reduces graph density would strengthen the claim from correlational to causal.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **"Global testing allows trivial task ID leakage through connectivity" (harsh critic #1, as a fatal flaw):** The critic's claim that connected-component analysis reveals task identity is technically valid as a *theoretical* possibility, but it is not a fatal flaw. In local testing, task ID leakage is **trivial** (the model is literally shown only that task's graph). In global testing, a method would need to deliberately run dedicated analysis to infer components and map them to tasks — no evaluated method does this. The concern is real but minor, and the paper's findings about LLM/GLM performance are unaffected. Downgraded to minor weakness #3.

- **"Minor modifications claim is vague and undersupported" (harsh critic):** The abstract says "even minor modifications can lead to outstanding results," referring to using PEFT and prototype classifiers on LLMs — which are indeed modest changes. The critic interpreted this as referring to the local-to-global switch, which is a misreading. Removed.

- **"Baseline selection leans on older methods" (harsh critic):** EWC, LwF, and GCN are standard GCL baselines in the CGLB framework that the paper builds on. Including them ensures comparability with prior work. The paper also includes more recent methods (TPp, TEEN, Cosine, and multiple LLM/GLM baselines). Not a valid weakness.

- **"Observation ❹ is speculative" (harsh critic):** The observation is presented as a correlational finding ("may enhance," "this improvement likely stems from"), not a causal claim. Requiring a density-ablation experiment for every correlational observation is not standard practice. Removed.

- **"Missing ego-graph neighborhood details" (harsh critic):** The paper references the appendix for extended details. The appendix was stripped by the parser. Defaulting to minor/trivial.

- **Strength Finder strengths that are generic or unsupported:** Some claimed strengths (e.g., "Rigorous analysis of why current GLMs fail") overlap with the paper's own claims and are retained as stated. No strengths needed removal.

## Novel Insights

None beyond the paper's own contributions. The most interesting finding — that prototyped-based LLM methods naturally resist catastrophic forgetting while GLMs that integrate GNNs actually perform worse — is clearly articulated by the paper itself. The reviews did not surface deeper insights beyond what the paper already presents.

## Suggestions

1. **Analyze the long-session failure mode of SimGCL.** Compare prototype quality across sessions (e.g., via nearest-class-center distance or t-SNE visualization of prototypes for early vs. late classes). Consider a variant that re-trains or adapts LoRA on a small replay buffer to understand whether the issue is representational bias or something else.
2. **Add variance reporting (mean ± std over 3–5 seeds)** for all benchmark results. This is especially critical given the stochasticity in baselines and the fact that metric ordering flips in some cases.
3. **Acknowledge the connectivity-based structural cue in global testing** as a limitation, even if only to explain why it does not affect the reported results.
4. **Add an ablation** comparing SimpleCIL with vs. without instruction tuning (but without graph prompts) to isolate the contribution of graph-structured prompts vs. fine-tuning. This would strengthen the attribution of SimGCL's gains.

## Score and Decision

**Calibration Report:**

*Round 1 (Bracketing):* Searched three bands for GCL + LLM/continual learning benchmark papers. Weak band (score < 3.5) returned papers scoring 2.0–3.25 — clearly weaker than this paper. Middle band (3.5–7.5) returned anchors at 4.4–6.5. Strong band (>7.5) returned anchors at 8.0 — clearly stronger. Bracket: [4.5, 6.5].

*Round 2 (Narrowing):* Searched within (4.5, 6.5) for GCL benchmarks and CL-with-pretrained-models benchmarks. Key anchors:

| Anchor | Avg Score | Round | Comparison to This Paper |
|--------|-----------|-------|--------------------------|
| OCGL (4sJJixGIZX) | 5.00 | 2 | Pure benchmark without novel method; this paper is stronger |
| CLDyB (RnxwxGXxex) | 5.67 | 2 | Benchmark-only, more sophisticated dynamic design; comparable quality |
| Scale-Free GLM (nFcgay1Yo9) | 5.75 | 2 | Method + theory, slightly stronger execution; similar tier |
| TiC-LM (MB53uAZKSc) | 6.25 | 2 | More extensive benchmark but rejected for limited novelty |
| Topology-aware EM (PQStRgYfuJ) | 5.40 | 2 | GCL method paper; this paper has broader scope |
| LMs as Feature Extractors (ClixrtIHUJ) | 5.25 | 2 | CL with pretrained models, similar tier |

*Final determination:* This paper sits between the OCGL (5.0) and CLDyB/Scale-Free GLM (5.67–5.75) anchors. It has the benchmark + method combination that the 5.0 paper lacks, but its weaknesses (unexplained failure modes, no variance) prevent it from reaching the 5.75 level. Score of **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>