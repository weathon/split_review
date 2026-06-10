## Summary
This paper introduces LLM4GCL, a benchmark for evaluating LLMs and Graph-enhanced LLMs on Graph Continual Learning (GCL). It identifies a critical task-ID-leakage flaw in the commonly used "local testing" protocol for Node-level Class-Incremental Learning, proposes a corrected "global testing" evaluation, evaluates 9 methods across 7 datasets, and proposes SimGCL — a method using ego-graph-derived prompts, LoRA fine-tuning in the first session only, and training-free prototype classification for subsequent sessions.

## Strengths
- **Convincing demonstration of task ID leakage (Table 1, Section 3.1):** The paper shows that even an MLP with mean-pooling achieves 0% forgetting under local testing across all 7 datasets (e.g., Cora 90.3 AA, 0.0 AF), proving the existing evaluation is fundamentally flawed and class-incremental learning trivially degrades to task-incremental learning. This is a genuinely valuable methodological contribution.
- **Comprehensive benchmark design (Sections 3.1–3.2):** 7 datasets spanning citation, web, and e-commerce domains at multiple scales, 9+ methods from three categories (GNN, LLM, GLM), two evaluation paradigms (NCIL and FSNCIL), with controls for previous knowledge leakage (inter-task edges excluded) and label imbalance (unified sample sizes). The breadth enables meaningful cross-method comparisons.
- **Valuable empirical insights (Obs. 2–4, 6):** The counterintuitive finding that deliberately designed GLM methods underperform pure LLM-based approaches (e.g., ENGINE 59.2 vs. LLaMA 65.6 on Cora NCIL; ENGINE 52.2 vs. LLaMA 72.6 on Cora FSNCIL), and that prototype-based methods dominate in GCL (Cosine and SimpleCIL outperform alternatives by up to 29.7% and 39.2% over vanilla GCN and RoBERTa), provide useful guidance for the community.
- **Scaling and robustness analysis (Figure 3, Table 4):** Demonstrates that larger LLM backbones consistently improve GCL performance across both BERT and RoBERTa families, and that prototype-based methods maintain stability across session configurations (5–20 sessions), informing practical deployment.

## Weaknesses

### Fatal
None

### Major
- **Overclaimed SimGCL superiority with inaccurate "23/28" claim.** The paper states in Obs. 8 (line 173) that SimGCL "consistently overperform other baselines (23 out of 28)," but counting best results across Tables 2 and 3 yields approximately 20/28 (11 in NCIL, 9 in FSNCIL). More critically, SimpleCIL (RoBERTa + prototype matching, already in the benchmark) outperforms SimGCL on several important datasets: NCIL Arxiv-23 (Ā: 52.4 vs. 38.7, A_N: 38.8 vs. 13.6), FSNCIL Arxiv-23 (Ā: 49.8 vs. 31.8, A_N: 40.0 vs. 10.3), FSNCIL Arxiv (Ā: 46.4 vs. 36.3, A_N: 36.6 vs. 6.8), and FSNCIL WikiCS Ā (73.2 vs. 68.8). The paper attributes SimGCL's Arxiv-23 failure to sparse graph structure (line 194) but never explains why SimpleCIL, which uses no graph structure at all, dramatically outperforms it there — a direct contradiction of the rationale for including graph structure in the prompt. In Table 4, SimpleCIL dominates SimGCL on A_N across all Arxiv configurations (31.4 vs. 28.7, 35.9 vs. 30.4, 36.5 vs. 33.8, 39.1 vs. 17.5). The abstract's "around 20%" claim is technically about GNN-based baselines, but the consistent framing of SimGCL as superior to all methods is misleading given the evidence.

- **No ablation study for SimGCL.** SimGCL has three components: (a) ego-graph-derived prompts, (b) LoRA fine-tuning in the first session, and (c) a training-free cosine-similarity prototype classifier. The prototype classifier is essentially what SimpleCIL already does. Without an ablation isolating each component, it is impossible to determine whether ego-graph prompts and LoRA provide meaningful benefit beyond the prototype mechanism alone. Given that SimpleCIL sometimes outperforms SimGCL, there is reason to suspect graph-structured instruction tuning may actually hurt on some datasets.

### Minor
- **No variance or error bars reported.** All results in Tables 1–4 are single-point numbers with no standard deviation or multi-seed averages. Continual learning benchmarks are sensitive to class-to-session assignments, random splits, and initialization. For a paper positioning itself as a community benchmark to "establish a foundation for future research," statistical reporting is important for trustworthy comparisons.

- **Missing key hyperparameters in the main text.** The LoRA rank, scaling hyperparameter τ (defined in Eq. 2 but value never disclosed), ego-graph hop count, and training epochs for the first session are absent from the main paper, affecting reproducibility.

- **Observation numbering error.** Numbering jumps from ④ to ⑥, skipping ❺ entirely, and later switches from circled numbers (⑧) to plain numbers (Obs. 7, Obs. 8), suggesting revision artifacts.

### Trivial
None

## Nice-to-Haves
- Discussion of computational costs (training/inference time) for the different methods, especially given SimGCL's efficiency claims.
- Analysis of whether the ranking of methods under local testing vs. global testing actually changes (not just absolute numbers), which would further strengthen the motivation for global testing.
- Reconciliation of Table 4 (Arxiv, where SimGCL beats SimpleCIL on Ā across all configurations) vs. Table 3 FSNCIL (Arxiv, where SimpleCIL dominates SimGCL) — these results appear contradictory and deserve discussion.

## Removed Points
These points are flagged to be removed, treat them with caution.
- Formatting/style nitpicks and parser artifacts (observation numbering inconsistency may be partly a parser issue).
- Generic demands for more datasets or baselines when 7 datasets and 9 methods are already comprehensive.
- Speculation about what might be in stripped appendices.

## Novel Insights
The identification and concrete demonstration of task ID leakage in local testing for GCL is the paper's most genuinely novel contribution — Table 1's demonstration that even MLP + mean pooling achieves 0% forgetting across all 7 datasets is striking and should change how the community evaluates GCL methods. The systematic finding that GLM-based methods surprisingly underperform pure LLMs in continual graph learning, attributed to LLM-GNN representation misalignment, is also a valuable empirical insight challenging assumptions in the GLM literature.

## Suggestions
1. Add an ablation study isolating SimGCL's three components (ego-graph prompts, LoRA, prototype matching) to demonstrate when and why graph structure helps vs. hurts.
2. Report multi-seed results (3–5 seeds) with mean ± std for at least the main benchmark tables.
3. Honestly reconcile the SimpleCIL vs. SimGCL comparison: acknowledge where SimpleCIL is stronger and explain why, rather than claiming SimGCL "consistently" outperforms all baselines.
4. Correct the "23 out of 28" claim to match the actual count (~20/28).
5. Disclose LoRA rank, τ value, ego-graph hop count, and training epochs in the main text.

## Score and Decision

**Calibration anchors used:**

| Round | Path | Avg Score | One-sentence comparison |
|-------|------|-----------|------------------------|
| 1 | ZHTYtXijEn | 2.33 | Weak CL method paper — our paper is clearly much stronger |
| 1 | gNoqEdT2wO | 2.33 | Weak multimodal CL benchmark — our paper has far more datasets, methods, and evaluation insight |
| 1 | WM5G2NWSYC | 2.00 | Weak CL method paper — our paper is clearly stronger |
| 1 | 6E8GCcCgxl | 3.25 | Weak CL method paper — our paper is stronger |
| 1 | 4sJJixGIZX | 5.00 | Online graph CL benchmark, rejected — our paper identifies a fundamental evaluation flaw, has more comprehensive evaluation, and proposes a method |
| 1 | RnxwxGXxex | 5.67 | Dynamic CL benchmark, accepted — both question evaluation validity; our paper has more concrete evidence but also more weaknesses |
| 1 | MB53uAZKSc | 6.25 | TiC-LM CL benchmark — comparable contribution level |
| 1 | Y1r9yCMzeA | 6.75 | GraphArena LLM graph benchmark, accepted — well-received with minimal weaknesses; our paper has more significant issues |
| 1 | GGlpykXDCa | 8.00 | MMQA LLM benchmark — stronger accepted paper |
| 1 | KbetDM33YG | 8.00 | Online GNN evaluation — stronger accepted paper |
| 1 | 07yvxWDSla | 8.00 | Synthetic continued pretraining — stronger accepted paper |
| 1 | RvUVMjfp8i | 8.00 | Realistic SSL evaluation — stronger accepted paper |
| 2 | IuXR1CCrSi | 6.00 | Talk like a Graph — comprehensive LLM+graph study, accepted; comparable quality and topic |
| 2 | 28qOQwjuma | 6.33 | LLM4Hypergraph benchmark — comparable quality, accepted |
| 2 | iSTMsye6SD | 5.25 | Knowledge-intensive reasoning benchmark, rejected — our paper is stronger |
| 2 | 70xhiS0AQS | 4.75 | TaskBench LLM benchmark, rejected — our paper is stronger |
| 2 | TLADT8Wrhn | 6.25 | TiC-CLIP continual CLIP training, accepted — comparable contribution level |
| 2 | wE1I9IGqeH | 6.00 | Continual open-vocabulary classification, rejected — comparable |

**Round-1 bracket:** 5.5–7.0. Clearly above rejected papers at 2.0–5.25, comparable to accepted benchmark papers at 5.67–6.33, and weaker than strong accepted papers at 6.75–8.0.

**Round-2 narrowing:** 5.5–6.5. The paper is clearly above the 4.75–5.25 rejected benchmarks and comparable to the 5.67–6.33 accepted benchmark papers. It's weaker than GraphArena (6.75) due to overclaiming and lack of ablation. The task ID leakage finding is a genuinely impactful contribution that elevates it above pure benchmark papers, but the SimGCL issues hold it back. Comparing to "Talk like a Graph" (6.0): both are comprehensive LLM+graph studies, but our paper has a more impactful finding (evaluation flaw identification) alongside more concerning issues (overclaiming). The net effect is comparable quality.

**Final score: 6.0**

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>