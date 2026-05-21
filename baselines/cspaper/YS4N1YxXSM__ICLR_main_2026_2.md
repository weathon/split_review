---
job_id: d254c7c7-3148-4661-b680-cf4a324ab02c
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: YS4N1YxXSM.pdf
paper: QuoKA: Query-Oriented KV Selection for Efficient LLM Prefill
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on efficient transformer inference and sparse attention for LLMs, which fits general machine learning, representation learning for language, and ML systems/infrastructure.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, method, experiments/results, related work, and conclusion, and it presents a concrete algorithm with substantial empirical evaluation. While I have technical concerns about the theorem, complexity claims, and some experimental positioning, these do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to reviewers, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper proposes QuoKA, a training-free sparse attention method for accelerating chunked prefill in LLM inference by selecting a subset of representative queries and then using them to select relevant keys and values. The method is motivated by an empirical observation that queries with lower cosine similarity to the mean query are more informative for approximating full attention, and is implemented using standard linear algebra operations without custom sparse kernels. The paper evaluates QuoKA on NIAH, RULER, LongBench, Math500, and latency measurements across several hardware platforms and model families.

## Strengths
The paper targets an important and timely problem, namely reducing prefill latency for long-context LLM inference under chunked prefill. This is a practically relevant bottleneck, and the focus on hardware-agnostic deployment is useful because many prior sparse-attention approaches are tied to specific kernels or accelerators.

The core idea is simple and operationally attractive. Algorithm 1 on **Page 3** is easy to follow at a high level: first select a small subset of informative queries, then normalize queries and keys, score them via cosine similarity, aggregate over queries, and gather the top-$B_{\mathrm{SA}}$ KV entries. This makes the method relatively easy to implement in existing inference stacks.

The empirical results are broadly strong. In particular, **Table 1 (Page 7)** shows very large gains over the listed baselines on RULER across multiple models and lengths. The margins are not marginal, for example on Qwen-3-4B at length 32k, QUOKA reports 74.83 versus 40.72 for SampleAttn and 39.31 for Loki. Even allowing for benchmark variance, that is a substantial gap. Similarly, **Table 3 (Page 8)** shows that on LongBench, QUOKA often stays much closer to dense attention than the competing methods at the same budgets.

The efficiency story is also compelling. **Figure 5 (Page 9)** is one of the stronger parts of the paper because it goes beyond isolated kernel timing and includes TTFT trends on A100 as well as attention latency on CPU and consumer GPU. The qualitative slope differences in the curves support the claim that the method scales better with context length than dense attention, and the multi-hardware presentation strengthens the portability claim.

The qualitative NIAH visualization is helpful. In **Figure 4 (Page 6)**, QUOKA appears much closer to full attention than SampleAttention over both document length and needle depth, which supports the paper’s claim that query selection matters in chunked prefill. This figure is more convincing than a single scalar average because it reveals the failure pattern over depth and length.

The ablation direction is sensible. The appendix tables on cosine-vs-dot-product scoring and max-vs-mean aggregation align with the design choices in Sections 3.2 and 3.3, so the method is not presented as a bag of unexplained heuristics.

## Weaknesses
1. **The theoretical justification is much weaker than the paper suggests, and Theorem 1 does not really establish the main claim.**  
   The central conceptual claim in Section 3.1 on **Pages 4-5** is that queries with low cosine similarity to the mean query are the ones that “attend to the majority of keys” and are therefore especially informative for KV selection. However, **Theorem 1 (Page 5)** only gives an upper bound on $\mathrm{CosSim}(M_Q,q^*)$ under assumptions involving a *single* key $k$, namely $\mathrm{CosSim}(k,q_0)=\beta_q>0$ and $\mathrm{CosSim}(M_Q,k)=\alpha_q<0$. This does not imply that such a query interacts strongly with many keys, nor does it show optimality of the proposed ranking score $S_q=-\mathrm{CosSim}(M_Q,q^*)$ for approximating attention over a chunk of queries. At best, it says that if a query aligns positively with one negatively mean-aligned key, then that query cannot be too close to the mean. That is far from the much broader narrative in Section 3.1.  
   Put differently, the theorem is neither a correctness result for the selection rule nor an approximation guarantee for the objective in **Equation (4)**. The gap matters because the method’s main novelty is precisely the query selection heuristic. Right now, the theory reads more like suggestive geometry than actual support for the algorithmic claim.

2. **Several mathematical formulations are underspecified or imprecise, which makes it harder to assess the method rigorously.**  
   There are multiple places where notation is loose enough to obscure exactly what is being optimized or computed.
   - In **Equation (4) (Page 4)**, the paper writes  
     \[
     \min_{f(Q,K)} \left\| \mathrm{Softmax}(QK^\top/\sqrt d + M)V - \mathrm{Softmax}(Q\hat K^\top/\sqrt d + M)\hat V \right\|,
     \]
     but this is not a well-defined optimization problem as written. The codomain of $f$, the admissible dependence of $\hat K,\hat V$ on $f$, the norm being used, and whether causality inside the chunk is preserved in the reduced operator are not specified. As a motivating surrogate this is fine, but the paper phrases it almost like a formal objective.
   - In **Algorithm 1 (Page 3)**, line 2 defines $M_Q \leftarrow \text{mean}(Q,\text{dim}=2)$, but the tensor axes are not defined before the algorithm. Later line 8 reshapes with $(b,n_{\mathrm{KV}},\frac{n_Q}{n_{\mathrm{KV}}},N_Q,d)$, which implicitly assumes divisibility and a particular layout corresponding to GQA. This probably holds for the tested models, but it should be stated explicitly in the main paper because it is a structural assumption of the method.
   - In **Section 3.3 (Page 5)**, the statement that pre-aggregation “achieves the same average” after normalization relies on linearity of the mean and outer product, but the exact equality is only true for the particular aggregation order used in the algorithm. Since the method averages normalized queries across query heads before forming scores, the paper should clearly show the identity being used. Otherwise it reads like hand-waving around a nontrivial implementation choice.

3. **The exposition sometimes overstates what the figures demonstrate.**  
   **Figure 2 (Page 4)** is used as primary evidence for the geometry-driven query selection rule, but the support is weaker than the text suggests. **Figure 2(b)** is a 2D PCA projection from one layer/head of one model, and proximity in the projected plane is not reliable evidence of actual angular alignment in the original space. Likewise, **Figure 2(c)** shows a correlation between $S_q$ and $\log(\max_k A)$ with reported correlation 0.737, but that is a correlation for a single analyzed head and does not establish robustness across layers, models, or prompt types. The paper uses these visuals to motivate a fairly general claim about query informativeness, yet the evidence shown in the main paper is narrow and anecdotal.  
   This matters because the method’s novelty hinges on the query geometry observation. If that observation is fragile or only true in some heads, then the justification for the algorithm is much weaker than the empirical performance suggests.

4. **The comparison space is incomplete for the specific design choice of representative-query selection.**  
   The paper compares against existing sparse attention baselines, which is good, but it does not compare against simpler or alternative representative-query selection strategies that are much closer to its own proposal. For example, Section 3.1 argues that selecting queries far from the mean is the right way to reduce redundancy, but there is no comparison against selecting high-norm queries, selecting queries with largest variance contribution, stratified sampling across positions, or cluster-based representatives. Without these ablations, it is hard to know whether the gain comes from the specific “low cosine to mean query” rule or from the broader idea of using a small subset of queries at all.  
   This is especially important because the strongest baseline, SampleAttention, differs exactly in how queries are chosen. The paper should isolate whether QuoKA’s advantage comes from the *selection criterion* itself rather than from other implementation details such as scoring normalization and aggregation.

5. **The empirical evaluation is strong on synthetic long-context benchmarks, but weaker on realistic end-to-end downstream settings than the claims imply.**  
   The paper emphasizes broad applicability across architectures and tasks, yet the main evidence is concentrated on NIAH, RULER, LongBench relative averages, and Math500. NIAH and RULER are useful, but they are synthetic stress tests. LongBench is more realistic, but in the main paper **Table 3 (Page 8)** only reports normalized averages rather than raw task-level scores, variance, or per-task behavior. Since some entries exceed 1.0, the average can hide both improvements and regressions on specific tasks.  
   The issue is not that LongBench is missing, but that the presentation in the main paper is too compressed to support strong “near-baseline accuracy” claims across diverse applications. For a method intended for deployment, I would want clearer visibility into which tasks degrade first and whether the gains are consistent across retrieval, summarization, QA, and code settings.

6. **Some of the efficiency claims are not as cleanly supported as the paper suggests, because method overhead is not fully unpacked in the main text.**  
   Section 4.6 and **Figure 5 (Page 9)** present attractive speedups, but the explanation of when QuoKA wins is somewhat thin. The method adds overhead from query subselection, normalization, score computation $\bar QK^\top$, top-$k$, and gathers before calling the dense attention kernel. This is partly acknowledged in the appendix complexity discussion, yet the main paper does not decompose runtime into selection overhead versus reduced attention cost. That matters because on shorter contexts or on hardware with different memory/computation balance, the crossover point may move substantially.  
   Also, the headline claim in the abstract mixes attention speedup and TTFT speedup. Since TTFT includes non-attention costs, a more careful decomposition in the main paper would help establish how much of the system-level gain is attributable to attention sparsification rather than incidental pipeline effects.

7. **There are several clarity and consistency issues that, while not fatal, are distracting and occasionally confusing.**  
   Examples include repeated use of “prefetch” where the paper clearly means “prefill”, such as in **Figure 1 caption (Page 2)** and multiple spots in Section 3. There are also inconsistencies in capitalization and naming, for example QuoKA/QUOKA/Quoka, and some table/model names appear malformed in the appendix. These are not scientific flaws by themselves, but they reduce trust in the precision of the presentation.  
   More importantly, some baseline names in the main paper are inconsistent with references or table labels, for example “LESSISMORE” in text versus “LevelsMere” in **Table 1 (Page 7)**. This makes it unnecessarily hard to parse the results and raises concern about possible transcription issues.

8. **The paper argues hardware agnosticism, but the evidence is still narrower than that claim sounds.**  
   I agree the method does not require custom sparse kernels, which is a genuine portability advantage. Still, “hardware agnostic” is a strong phrase. The runtime evidence in **Figure 5 (Page 9)** covers A100, one Xeon CPU, and an RTX 2080, which is useful but not enough to justify broad claims across accelerators. The method also depends heavily on efficient dense GEMM/topk/gather implementations, and those primitives can behave very differently on mobile NPUs, DSPs, or edge-class accelerators, which are highlighted in the introduction.  
   I am not asking for exhaustive hardware coverage, but the paper should phrase the portability claim more carefully: compatible with standard kernels is supported, universally hardware-agnostic in practice is not fully demonstrated.

## Questions
1. The biggest issue for me is the justification of the query selection rule in Section 3.1. Can the authors provide stronger evidence that ranking by
   \[
   S_q=-\mathrm{CosSim}(M_Q,q)
   \]
   is superior to other representative-query schemes, such as position-stratified sampling, high-norm queries, leverage-score-like heuristics, or clustering-based representatives? Even a small controlled comparison would substantially increase my confidence that the proposed heuristic is the real source of gain.

2. Can the authors clarify exactly what **Theorem 1** is intended to prove relative to the algorithm? As written, it seems to connect mean-dissimilar queries to one key under sign constraints, but the paper uses it to motivate a much broader statement about interaction with many keys and approximation of full attention. If there is a more precise interpretation, please spell it out carefully.

3. Please clarify the exact tensor dimensions and assumptions in **Algorithm 1**, especially around lines 2, 8, and 9. What are the shapes of $Q$ before and after query subselection, and is the reshape on line 8 always valid only when $n_Q$ is divisible by $n_{\mathrm{KV}}$? A brief explicit shape annotation in the main paper would help.

4. On the efficiency side, could the authors provide a breakdown of the runtime components in **Figure 5**, for example query scoring/topk/gather overhead versus dense attention on the reduced KV set? This would make the crossover behavior much easier to understand and would help assess deployability on shorter contexts.

5. For **Table 3**, could the authors report or at least summarize raw LongBench scores or task-category-level averages in the main paper? The normalized averages are useful, but they hide whether some tasks degrade significantly while others improve slightly.

6. In **Figure 2(c)**, how stable is the reported correlation across layers, heads, and prompts? If the result is highly heterogeneous, that would affect how universal the geometric motivation really is.

7. The paper repeatedly uses very strong language like “hardware agnostic” and “near-baseline accuracy.” I would be more comfortable if these were backed by sharper scope conditions. Can the authors specify the regimes where QuoKA is not expected to help, for example short contexts, non-GQA settings, or devices with expensive gather/topk?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None. The paper studies inference efficiency for publicly available models and benchmarks, and I did not identify a specific ethics issue requiring escalation based on the main paper.

## Soundness Rating
2: fair. The empirical evidence is substantial and generally supportive, but the main theoretical motivation is weaker than claimed, several formulations are underspecified, and some conclusions are broader than what is rigorously established.

## Presentation Rating
3: good. The paper is generally readable and the high-level method is understandable, with useful figures and broad experiments, but there are notable notation issues, terminology inconsistencies, and some over-interpretation of the geometric evidence.

## Contribution Rating
3: good. The paper makes a practically relevant contribution for chunked prefill efficiency, and the empirical gains appear meaningful. I do think the conceptual novelty is somewhat narrower than the framing suggests, and the method would benefit from stronger isolation of what component is actually new and necessary.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper addresses an important problem and presents a simple, practically useful method with strong empirical results, especially on RULER/LongBench and latency benchmarks. I remain unconvinced by the current theoretical story and I think the paper overstates what its geometry analysis proves, but the empirical gains are strong enough that I lean positive overall.

## Reviewer Confidence
4: confident. I am confident in the core assessment and carefully checked the main algorithm, figures, equations, and results tables, though I would still welcome clarification from the authors on the theoretical interpretation and some implementation details.