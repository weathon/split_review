Here's my synthesized review based on careful cross-checking of the paper against all reviewer claims.

---

## Summary

This paper introduces LLM4GCL, the first systematic benchmark evaluating large language models (LLMs) for graph continual learning (GCL), and proposes SimGCL, a method that combines graph-prompted instruction tuning (with LoRA in the first session) with training-free prototype classification in incremental sessions. The paper makes a genuine conceptual contribution by identifying task-ID leakage in the prevalent "local testing" evaluation setup for GCL, where test and train samples share the same subgraph, allowing trivial task inference that reduces class-incremental to task-incremental learning. The proposed SimGCL outperforms baselines on 23 of 28 reported metrics across two settings (NCIL and FSNCIL) and seven text-attributed graph datasets.

## Strengths

- **Identification of task-ID leakage in local testing is a genuine and important flaw.** The paper provides concrete evidence (Table 1) that even simple mean-pooling achieves zero forgetting and matches the previous SOTA TPP under local testing, demonstrating that this evaluation paradigm is fundamentally broken. This is a significant service to the GCL community and will likely influence future evaluation standards.

- **First comprehensive benchmark for LLMs in GCL under realistic conditions.** LLM4GCL integrates 9 LLM/GLM methods across 7 text-attributed graph datasets with two settings (NCIL and FSNCIL), using the more challenging *global testing* setup. The benchmark also carefully addresses *previous knowledge leakage* (removing inter-session edges) and *label imbalance* (class subsampling), setting a higher standard for GCL evaluation.

- **SimGCL achieves substantial gains on most datasets.** On the NCIL setting, SimGCL outperforms all 14 baselines on 13 of 14 metrics (Table 2), with absolute gains of up to 21.7% on Photo (AA 82.1 vs. next-best 66.5) and 18.0% on Citeseer in FSNCIL (AA 78.0 vs. next-best 75.9). These are large margins that suggest the approach has genuine merit.

- **Diagnostic analysis of why existing GLMs fail in GCL.** The paper identifies two concrete failure modes: overfitting in LLM-as-Enhancer methods and LLM-GNN representation misalignment in LLM-as-Predictor methods (Obs. 3). This goes beyond simple accuracy reporting and helps guide future research.

- **The paper explicitly acknowledges its own failure cases** (Arxiv-23 and Arxiv in FSNCIL) and provides reasoned explanations (sparse graph structure, overfitting from larger tuning sets), which is good scientific practice.

## Weaknesses

### Major

- **No variance reporting anywhere.** Tables 2, 3, and 4 report a single value per metric per dataset with no standard deviations, confidence intervals, or indication of multiple runs. GCL results are known to be sensitive to task order splits and stochasticity. Given that the paper makes strong comparative claims ("surpasses previous SOTA by around 20%"), the absence of any uncertainty quantification undermines the statistical credibility of every quantitative claim. Whether the reported differences (e.g., 84.6 vs. 70.8 on Cora) are robust or could arise from a single favorable run cannot be assessed.

- **No ablation isolating the method's components.** SimGCL combines (a) instruction tuning with LoRA, (b) graph-structured prompts, and (c) prototype-based classification, but the paper provides no ablation to separate any of these contributions. The reader cannot tell whether the graph prompts add value beyond standard instruction tuning, or whether the prototype classifier is essential vs. simply updating a linear head. Since SimpleCIL (which also uses first-session tuning + prototype generation) performs strongly, the key question—what value does the graph prompt add?—remains unanswered.

### Minor

- **The LLM backbone used by SimGCL for the main experiments (Tables 2 and 3) is not specified in the main text.** The paper describes SimGCL only as "a GLM-based approach" using "instruction tuning with LoRA" but never states which underlying LLM (e.g., RoBERTa-large, LLaMA) was used to produce the headline numbers. Figure 3 shows results with multiple backbones (BERT variants and RoBERTa-large on Arxiv only), but the backbone for Tables 2 and 3 is unclear. While the appendix likely contains this detail (and the parser strips appendices), a paper's central empirical claim should not require the appendix to interpret.

- **"Consistently overperform" overstates the results.** SimGCL wins 23/28 metrics, but the failures on Arxiv-23 and Arxiv in FSNCIL (e.g., A\_N of 10.3 vs. 40.0 for SimpleCIL on Arxiv-23, Table 3) are severe—these are the two largest and most realistic datasets. The paper does acknowledge these cases in Obs. 8, but the abstract's claim of "surpasses previous SOTA by around 20%" and Obs. 8's "consistently overperform" are misleading when the method is worse by 30+ points on the biggest datasets. The paper would benefit from more measured language.

- **The baseline backbone for SimGCL comparisons is not controlled.** SimpleCIL explicitly uses RoBERTa-large. If SimGCL also uses RoBERTa-large, a controlled comparison is possible; if it uses a different (or larger) backbone, the gap may partly reflect model capacity. Figure 3 shows both methods with multiple backbones but only on Arxiv. The main tables lack this controlled comparison, making it unclear how much of SimGCL's advantage comes from the method vs. the backbone choice.

- **SimGCL's scaling parameter τ (Eq. 2) is not analyzed.** Whether τ was tuned per dataset, its sensitivity, and its default value are not discussed. This matters because a poorly chosen τ could artificially inflate or suppress prototype matching scores.

### Trivial

- The paper refers to its observation numbering inconsistently (Obs. 5 is skipped in the main text between Obs. 4 and Obs. 6).

## Nice-to-Haves

- An ablation comparing SimGCL (graph prompts + tuning + prototype) against a version with text-only prompts (no graph structure) would cleanly isolate the contribution of the graph prompt.
- Reporting results averaged over 3-5 random task-order seeds (with std) would substantially strengthen the empirical claims.
- A comparison of SimGCL vs. SimpleCIL using the *same* backbone across all datasets (not just Arxiv in Figure 3) would cleanly separate method from backbone.
- Reporting computational cost (runtime, parameter count, memory) would help practitioners assess the practical trade-offs.

## Removed Points

These points were flagged by reviewers but are removed for the following reasons:

1. *"Task ID leakage evidence is incomplete (no direct task-ID accuracy reported)"* — The paper's Table 1 shows identical AA/AF across TPP and simple mean-pooling, and the argument is clearly that perfect task ID prediction follows from the shared train/test subgraph. This is logically sound and the evidence is sufficient.

2. *"Selection criteria for datasets are arbitrary"* — The paper provides three concrete criteria (multiple domains, diverse scale/density, various sessions) which are reasonable.

3. *"Graph prompt template is not concretely specified"* — The template is described (task description, graph structure with [Node ID][Node Text], question with label options) and referenced to Wang et al. 2025. This is standard practice.

4. *"Missing related works"* — The reviewer has no external basis to assert this.

5. *"Formatting/style nitpicks"* — These are parser artifacts, not paper problems.

## Novel Insights

The only genuinely novel insight that emerges from reading the reviews together — beyond what the paper already states — is that the paper's two main contributions (the task-ID leakage critique and the SimGCL method) are somewhat in tension: SimGCL itself uses prototype matching (Eq. 2), which is conceptually related to the TPP/mean-pooling approach that the paper shows to be problematic under local testing. The global testing setup prevents task-ID leakage but the underlying prototype mechanism is similar. The reviews do not surface any other cross-cutting insight not already present in the paper.

## Suggestions

1. Specify the LLM backbone used for SimGCL in all main-table results directly in the main text (not only in the appendix).
2. Include a controlled comparison where SimGCL and SimpleCIL use the same backbone across all datasets.
3. Add an ablation: SimGCL minus graph prompts (text-only prompt) vs. full SimGCL.
4. Report all metrics as mean ± std over multiple random seeds/task orders.
5. Tune the language around "consistently outperforms" to accurately reflect the failure cases on Arxiv-23 and Arxiv.

## Score and Decision

### Calibration

**Round 1 (Bracketing):** Searched for three bands of anchors on topics related to graph continual learning, benchmarks, and LLM evaluation. Weak band (score < 3.5) yielded papers like OCGL-adjacent work scoring ~2.3. Middle band (3.5–7.5) yielded OCGL (5.0), CLDyB (5.67), TiC-LM (6.25), and a graph pattern benchmark (7.0). Strong band (>7.5) yielded papers scoring 8.0 (e.g., online GNN evaluation). Initial bracket: **4.5–6.0**.

**Round 2 (Narrowing):** Searched within (4.0, 6.5) for more anchors. Retrieved OCGL (5.0, Reject), CLDyB (5.67, Accept), TPLR (6.0, Accept), Task-tree GIT (5.25, Reject), TiC-LM (6.25, Reject), Continual LLaVA (4.75, Reject), TiC-CLIP (6.25, Accept).

**Key anchor comparisons:**
- **OCGL (5.0, Reject):** Similar benchmark+framework paper but without a proposed method and less conceptual novelty. The current paper is stronger (identifies task-ID leakage, proposes SimGCL) → score should be ≥5.0.
- **CLDyB (5.67, Accept):** Stronger methodological execution (more careful experimental design). The current paper has weaker experimental rigor (no variance, no controlled backbone comparison) → score should be <5.67.
- **Task-tree GIT (5.25, Reject):** Comparable profile — solid conceptual contribution but meaningful methodological gaps. The current paper has a more concrete and impactful flaw discovery → score near this range.
- **Continual LLaVA (4.75, Reject):** Benchmark + method paper with similar experimental gaps. The current paper has stronger conceptual novelty → score should be >4.75.

**Final score:** **5.0**. The paper has a genuinely important conceptual contribution (task-ID leakage) and SimGCL shows impressive results on most datasets, but these are undercut by the absence of variance reporting, the unspecified backbone, missing ablations, and overclaimed consistency. The paper is a clear contribution on its conceptual and benchmark contributions, but the evidential support for the method claims is not yet at the level of a strong accept. Score 5.0 reflects a paper that could become an accept with a major revision targeting the experimental methodology gaps.

<score>5.0</score>
<decision>Reject</decision>