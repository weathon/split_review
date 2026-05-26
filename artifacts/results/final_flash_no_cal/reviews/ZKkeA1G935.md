Now I have sufficient information from the paper to produce the consolidated review. Let me carefully verify each claim.

## Summary

The paper makes three main contributions: (1) identifying that the widely-used *local testing* evaluation in GCL suffers from task-ID leakage, reducing class-incremental to task-incremental learning; (2) establishing LLM4GCL, the first systematic benchmark evaluating LLMs for graph continual learning across 9 methods and 7 text-attributed graph datasets under the corrected *global testing* setup; and (3) proposing SimGCL, which fine-tunes an LLM with LoRA on the first session then uses training-free prototype classification for subsequent sessions. The paper reports that SimGCL outperforms existing GNN-based and LLM-based baselines on most metrics.

## Strengths

- **Identification of a critical evaluation flaw in GCL.** The paper convincingly demonstrates that the local testing paradigm allows perfect task-ID prediction, reducing class-incremental learning to easier task-incremental learning. Table 1 shows that even mean pooling achieves "flawless task ID prediction" and zero forgetting, matching prior SOTA. This is a genuine contribution that calls prior GCL evaluations into question and motivates the global testing alternative. (Section 3.1, Table 1)

- **First comprehensive benchmark for LLMs in GCL.** LLM4GCL integrates 9 methods (GNN-based, LLM-based, GLM-based) and 7 diverse text-attributed graph datasets under a unified global-testing evaluation. This provides a reproducible foundation for future work and fills a clear gap in the literature. (Section 3.2, Tables 2–4)

- **SimGCL shows strong empirical performance across most settings.** The proposed method achieves the best results in 23 out of 28 reported metrics across NCIL and FSNCIL settings (Tables 2, 3), with particularly large gains on Photo (82.1 vs. 63.6 for the best prior method). The design principle — single-session fine-tuning + training-free prototype classification — is both efficient and principled for rehearsal-free continual learning. (Tables 2, 3, Section 3.3)

- **Detailed experimental analysis and ablation of session configurations.** The paper provides eight observations and evaluates methods across varying class/session splits on Arxiv (Table 4), showing that prototype-based methods (Cosine, SimpleCIL, SimGCL) remain robust even with many sessions. (Table 4, Obs. 1–8)

- **Open-source platform.** The code and benchmark are released, enabling reproducibility and extension. (Section 1, code link)

## Weaknesses

### Major

- **Missing ablation isolating the effect of first-session fine-tuning from the graph prompt.** SimGCL fine-tunes an LLM with LoRA on the first session and uses a graph-structured prompt, while SimpleCIL (its strongest baseline) uses a frozen RoBERTa with prototype classification. The paper does not include a controlled experiment that fine-tunes the LLM with LoRA *without* the graph prompt and then applies prototype classification. Without this, it is unclear whether the gains of SimGCL over SimpleCIL come primarily from the first-session adaptation (which any fine-tuning would provide) or specifically from the graph-prompted instruction tuning. The claimed advantage of the graph prompt component is not cleanly supported. (Section 3.3, Tables 2–3)

### Minor

- **Overclaimed "consistently outperform."** Observation ❽ states that SimGCL "consistently overperform[s] other baselines (23 out of 28)." However, on Arxiv-23, SimpleCIL substantially outperforms SimGCL (\(\bar{\mathcal{A}}\) 52.4 vs. 38.7; \(\mathcal{A}_N\) 38.8 vs. 13.6). On Arxiv, SimpleCIL's \(\mathcal{A}_N\) (36.5) exceeds SimGCL's (33.8). The word "consistently" is too strong given these counterexamples; a more nuanced characterization acknowledging the failure cases on high-session-count datasets would be appropriate. (Table 2, Obs. ❽)

- **Ambiguity about whether the global test graph includes inter-session edges.** Section 3.1 states the benchmark "excludes inter-task edges, using only intra-task connections" — this sentence appears in the context of preventing *training-time* knowledge leakage. However, the definition of global testing uses "the union of the subgraphs from all previous tasks," and Figure 1's caption says global testing uses the "complete graph with inter-session edges." The paper does not clearly state whether the test-time graph includes inter-session edges or not. If the test graph mirrors the training restriction and lacks inter-session edges, each session's nodes form isolated components, and a model could infer task membership from graph connectivity — partially undermining the claimed prevention of task-ID leakage. The text and figure need reconciliation. (Section 3.1, Figure 1)

- **No error bars or multi-run statistics.** All results in Tables 2–4 are reported as single numbers. Given the known variance in continual learning experiments and the modest margins on some datasets (e.g., WikiCS \(\bar{\mathcal{A}}\) 73.5 vs. 71.4 for SimpleCIL), it is impossible to assess statistical significance. For a paper positioning itself as a benchmark and making strong comparative claims, this is a notable omission. (Tables 2–4)

- **SimGCL's backbone LLM is not specified for the main results.** The main tables (Tables 2, 3) do not state which LLM backbone SimGCL uses. Figure 3 suggests it could be using RoBERTa-large or LLaMA, but this is not explicitly stated in the table captions or text. The reader cannot tell which backbone drives the main results. (Tables 2, 3; contrast with Figure 3 which names backbones)

- **No sensitivity analysis for key hyperparameters.** The scaling parameter \(\tau\) in Eq. (2) is introduced without discussion of how it is set or its impact on results. Similarly, the LoRA rank is not mentioned. For a paper proposing a new method, some sensitivity analysis for \(\tau\) would strengthen the claims. (Section 3.3, Eq. 2)

- **Task/session ordering not specified.** The paper defines sessions with disjoint classes but does not state whether the order of classes across sessions is fixed, randomized, or based on some criterion. Different task orders can produce different results; this should be documented for reproducibility. (Section 3.1–3.2)

### Trivial

- The forgetting ratio (AF) used in Table 1 is not formally defined in the main text; it is only labeled as "forgetting ratio" in the caption.
- Observation numbering jumps from ④ to ⑥ to ⑧ (circled numbers) then to 7 and 8 (Arabic numerals), creating minor confusion.
- The baseline name "GCN <sub>LLMEmb</sub>" in Table 2 is referred to as "GCN<sub>Emb</sub>" in the observation text (Obs. ❸), a small inconsistency.

## Nice-to-Haves

- An ablation comparing SimGCL (full) vs. LoRA fine-tuning without graph prompt + prototype vs. frozen LLM + graph prompt + prototype would cleanly disentangle the contributions of fine-tuning and the graph prompt.
- Reporting results with standard deviations over multiple random seeds would substantially increase confidence in the comparative claims, especially on datasets where margins are small.
- A sensitivity study for the scaling hyperparameter \(\tau\) and the LoRA rank would help practitioners deploy the method.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *Harsh critic's Issue 1 (strong version):* "The global testing setup may still permit task ID leakage" and "would invalidate the evaluation design." This is removed because the Figure 1 caption explicitly states that global testing uses "the complete graph with inter-session edges," which prevents the connectivity-based leakage the critic describes. The paper is ambiguous about training vs. test graph construction, so a *Minor* clarity concern is retained, but the critic's stronger structural-invalidation claim is not supported by the paper as written. The ambiguity concern is retained in Minor weaknesses above.
- *"Table 1 does not directly show task-ID prediction accuracy"* — Partially addressed because the paper states that mean pooling "achieves flawless task ID prediction" as a claim separate from the table; the table demonstrates that the simpler method matches the SOTA's accuracy and forgetting, which is the relevant evidence. Demoted to a subtlety, not a weakness.
- *"AF is not defined in the main text"* — True, but the caption defines it as "forgetting ratio"; this is a formatting detail. Retained as Trivial.
- *Strength Finder's "consistent and substantial performance gains"* — The word "consistent" is too broad given the Arxiv-23 counterexample. The strength is retained but rephrased to avoid the overclaim.

## Novel Insights

The meta-review does not surface a genuinely novel insight beyond the paper's own contributions. The paper itself offers the key novel observation: that local testing in GCL permits trivial task-ID leakage, which the paper demonstrates and corrects with global testing. The finding that a simple prototype-based method with first-session fine-tuning outperforms more complex GCL-specific and GLM methods is the paper's second main insight. Neither is contradicted or significantly extended by anything in the reviews.

## Suggestions

- Clarify whether inter-session edges are included in the test graph. If they are (as Figure 1 suggests), state this explicitly in Section 3.1 and distinguish the test graph from the training graph construction. If they are not, discuss the implications for task-ID leakage via connectivity.
- Add a controlled ablation: fine-tune the LLM with LoRA on the first session using *only the raw text* (no graph prompt), then apply the same prototype classification pipeline. Compare this to full SimGCL to isolate the graph prompt's contribution.
- Tone down the "consistently overperform" claim to accurately reflect the Arxiv-23 and Arxiv \(\mathcal{A}_N\) counterexamples.
- Add error bars or multi-run statistics (at least 3–5 seeds) for the main results in Tables 2–4.
- Specify which LLM backbone SimGCL uses in the main results, either in the table caption or a footnote.
- Report the task ordering policy used for the session splits.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>