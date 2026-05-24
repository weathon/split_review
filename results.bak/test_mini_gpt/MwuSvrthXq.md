## Summary
The paper proposes WeCAN, a single-pass reinforcement-learning framework for heterogeneous DAG scheduling with task–pool compatibility coefficients. Its main technical components are compatibility-weighted cross-attention for variable task/resource environments, an LDD-aware DAG encoder, and a skip-action generation map intended to overcome representational limits of ordinary list scheduling. Empirically, WeCAN reports strong makespan and runtime results on TPC-H-derived and computation-graph scheduling benchmarks.

## Strengths
- **Concrete compatibility-aware architecture with useful ablation evidence.** Section 3.1 defines a weighted cross-attention layer in which task embeddings attend to pool embeddings while multiplying value contributions by \(K_{acc}(v,c)\) (lines 120–128). Table 3 supports that this design matters: the full “WeCA + LDDGNN” variant outperforms inside-weighting, decoder-only, final-only, and GAT-based variants on TPC-H-30 and TPC-H-50.
- **Single-pass scheduling is computationally attractive and empirically effective.** The decoder is explicitly non-autoregressive over network computation (lines 140–148), and Tables 1–2 show WeCAN-Greedy has runtimes close to heuristic methods while producing substantially lower makespans than heuristics and PPO-BiHyb.
- **The skip-action/generation-map analysis is a meaningful conceptual contribution.** The paper distinguishes reduced action/order spaces from feasible schedules (Section 4.1) and gives a formal criterion via Assumption 1 and Theorem 2 for when a generation map’s image contains an optimal schedule. This is more principled than treating list scheduling purely as an implementation detail.
- **Empirical results are strong across the reported benchmarks.** In Table 1, WeCAN-S(256) obtains the best makespan on all TPC-H settings, e.g. TPC-H-50 improves from One-Shot-S(256)’s \(35561\pm108\) and PPO-BiHyb’s 36333 to \(32814\pm47\). In Table 2, WeCAN-S(256) is also best on all three computation-graph families.
- **The paper includes relevant component-level and stress-test evaluations.** Table 3 isolates WeCA and LDDGNN contributions, and Figure 3 tests skip actions in a heavy-task setting that is aligned with the paper’s theoretical motivation.

## Weaknesses

### Fatal
None.

### Major
- **The “closes/fixes the optimality gap” language overstates what is actually proved for the learned scheduler.** The paper repeatedly states that skip actions “fix” or “close” the optimality gap, e.g. line 148 says the skip-score design “fixes the optimality gap,” lines 193–213 describe skip as closing the gap through surjectivity, and the conclusion says skip “closes optimality gap of list scheduling” (line 317). The theorems establish an important representational result: with skip actions, the generation map can assign positive probability to feasible/optimal orders, and for each problem there exist scores enabling an optimal greedy solution (Theorem 1, line 152). But the actual skip score used by WeCAN is a restricted function \(u_a(1-k/(2n))^{u_b}+u_c\) depending on learned global coefficients and the step count \(k\) (line 148), not on the full evolving resource/dependency state except through masks. Thus the theory supports “the enlarged generation map can represent schedules excluded by ordinary list scheduling,” not “the learned single-pass policy is guaranteed to find optimal schedules.” This is a framing issue, but it concerns one of the paper’s central claimed contributions.
- **The heterogeneous adaptations of the neural baselines are under-specified in the main experimental description.** The paper itself notes that One-Shot “does not consider compatibility coefficients or pool allocation” (lines 30–33), yet Section 5.1 compares against One-Shot and PPO-BiHyb in a setting with task–pool compatibility and pool assignment (lines 219–223). The paper says that for four list-scheduling algorithms it applies three pool-selection rules and selects the best (line 221), but it does not comparably explain how One-Shot and PPO-BiHyb receive compatibility information, how incompatible actions are masked, or how pool assignment is handled. Since the reported gains over these neural baselines are central to the “state-of-the-art” empirical claim, this missing protocol detail makes the fairness of the neural comparison harder to assess, even though the heuristic comparisons remain informative.

### Minor
- **Generalization/adaptability claims are somewhat broader than the main evidence.** The architecture is plausibly adaptable to variable pool/task types, and Figure 2 provides a useful controlled test. However, the main benchmark setup uses three heterogeneous pools (line 219), and TPC-H heterogeneity is partly constructed by adding random memory constraints and task types/compatibilities (line 219). Figure 2 reports percent improvement over best heuristics under “more pool,” “more pool type,” “more task,” and “more task type,” but not absolute makespans, variance, or detailed shift magnitudes. The evidence supports promising controlled adaptability, but the broad abstract/conclusion language about robust performance across diverse heterogeneous environments should be calibrated.
- **The description of “masking” inside WeCA is technically imprecise.** Equation at lines 122–124 multiplies the compatibility diagonal outside the softmax. Therefore \(K_{acc}(v,c)=0\) zeroes a pool’s value contribution but does not remove that pool from the softmax normalization. The text says “incompatible pool assignments are inherently masked in attention calculation” (line 126), which is not exactly true for the stated formula. This does not invalidate the method—Table 3 suggests the outside-softmax design is empirically useful—but the mechanism should be described accurately.
- **Evaluation statistics are not fully transparent in the main text.** Table 1 reports “standard deviation among random seed” (line 231), and Section 5.3 states that an ablation uses 10 test problems (line 311), but the main results do not clearly state the number of train/test instances, whether all methods share the same test set, or whether variation across problem instances is separated from variation across training seeds. This is not fatal, but clearer reporting would make the robustness claims easier to interpret.
- **The skip-action stress test is narrow relative to the theoretical discussion.** Figure 3 uses a heavy-task variant created by replacing 1% of tasks with long-duration, high-resource-demand tasks (line 313). This is a reasonable diagnostic test, but by itself it supports skip actions in one predicted failure mode rather than broadly validating the optimality-gap theory across scheduling regimes.

### Trivial
None.

## Nice-to-Haves
- Report the frequency and timing of learned skip actions, especially in the heavy-task experiments, to connect the theoretical motivation to actual policy behavior.
- Vary heavy-task rate, resource-demand skew, and duration skew to show when skip actions help and when they do not.
- Include absolute makespans and variance/error bars for the environment-fluctuation experiments in Figure 2.
- Explicitly state whether runtime excludes model training cost. This is acceptable for an amortized scheduler, but the comparison should make the inference-only setting clear.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Pure notation/formatting nitpicks.** Comments about inconsistent notation such as \(p(v)\), \(\rho(v)\), \(\lambda(c)\), or the apparent \(F(t,v)\) versus \(F(t,c)\) issue were not retained as substantive weaknesses. They are minor cleanup issues and may be affected by extraction/formatting.
- **Criticisms depending on missing appendix details.** The paper explicitly says LDDGNN and several implementation details are further specified in Appendix G or other appendices (e.g. lines 132 and 223). Since appendices are stripped from the provided extraction, I did not treat missing appendix-level details as major flaws.
- **Missing related work / absent references.** Any request for additional related work was removed under the instructions, since external existence/completeness of related work cannot be verified here.
- **Typos, grammar, figure-caption artifacts, and parser issues.** These were removed per instruction. The extracted PDF contains duplicated figure descriptions and garbled figure text, but these are parser artifacts rather than author errors.
- **Training-cost-as-unfairness criticism.** I did not treat exclusion of training cost as a major weakness. For learned amortized schedulers, inference-time comparisons are standard, though the paper should state this clearly.
- **Overly broad “evaluation lacks rigor” concerns without concrete anchors.** General concerns not tied to a specific table, claim, or protocol statement were removed or narrowed to the concrete evaluation-statistics and baseline-adaptation issues above.

## Novel Insights
The paper’s most interesting insight is that the limitation of one-shot/list-scheduling neural schedulers is not only architectural but also representational: the learned network scores orders, while the generation map determines which feasible schedules can actually be reached. This makes the skip action more than a heuristic idling choice; it is a way to enlarge the image of the generation map while preserving single-pass neural inference. The strongest version of the paper would separate this representational insight from the empirical claim that a particular restricted skip-score parameterization learns to exploit it.

## Suggestions
- Rephrase “fixes/closes the optimality gap” as “removes a representational restriction of ordinary list-scheduling maps” or “allows optimal schedules that ordinary list scheduling may exclude.”
- Add a concise baseline-adaptation paragraph for One-Shot and PPO-BiHyb: what inputs they receive, how compatibility matrices are represented, how incompatible actions are masked, and how pool assignment is performed.
- Expand Figure 3-style diagnostics: vary heavy-task proportions and report skip frequency/timing.
- Add a small table with train/test instance counts, number of random seeds, whether all methods use the same test set, and whether reported standard deviations are across seeds, instances, or both.
- Correct the WeCA masking explanation: outside-softmax compatibility weighting removes incompatible value contributions but does not remove those pools from the attention denominator.

## Score and Decision

### Qualitative evaluation
- **Originality:** High. The compatibility-weighted cross-attention design and generation-map/skip-action analysis are specific and nontrivial contributions for heterogeneous DAG scheduling.
- **Importance:** Strong. Fast heterogeneous DAG scheduling with compatibility constraints is a practically meaningful problem.
- **Support for claims:** Mostly good for empirical performance on the reported benchmarks, but weaker for broad optimality and generalization claims.
- **Experimental soundness:** Generally solid, with strong tables and useful ablations, but the neural baseline adaptation and evaluation-statistics reporting need clarification.
- **Clarity:** Mostly understandable, but some theoretical framing and mechanism descriptions need tightening.
- **Value to the community:** High enough for acceptance: the method is practical, empirically strong, and introduces a useful way to think about generation maps in neural scheduling.

### Calibration

**Round-1 bracket.** The paper is clearly stronger than the weak scheduling/RL anchors around 3–5 because it has a coherent method, substantial benchmark results, and meaningful ablations. It is below the strongest 8-level anchors because of overclaiming and some important experimental-protocol ambiguity. After Round 1, I bracketed it at **6.5–7.5**.

**Round-2 narrowing.** Compared with the 6.0–6.25 anchors, this paper is more focused and has stronger direct empirical support. Compared with the 7.5 scheduling anchor, it is somewhat weaker because that anchor’s reviews emphasized broad benchmark coverage and fewer concerns about baseline adaptation. It is closest to the 7.0 neural combinatorial-optimization anchor: strong contribution and experiments with fixable but real caveats. Final score: **7.0**.

### Retrieved anchors and comparison

**Round 1**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/10eQ4Cfh8p.md` — avg 3.00 — Much weaker than this paper; that work had unclear design justification, missing ablations, weak baselines, and poor presentation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/z4Ho599uOL.md` — avg 3.00 — Much weaker; LLM/job-shop scheduling anchor with substantial methodological and empirical concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/bntJK4NyIW.md` — avg 2.00 — Much weaker and less topically relevant; severe systems/distributed-training concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/iWCfiDxLIY.md` — avg 3.00 — Much weaker; graph/NCO method with limited evidence and significant concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/b9aCXHhdbv.md` — avg 4.50 — WeCAN is stronger; this anchor had reasonable ideas but substantial missing details and incomplete experimental analysis.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CJEBFNBLhO.md` — avg 4.25 — WeCAN is stronger; this anchor is more infrastructure/benchmark oriented and less directly convincing as a method paper.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/8WtBrv2k2b.md` — avg 5.00 — WeCAN is stronger; that paper had promising RL scheduling results but serious formulation/baseline clarity concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/Dgc5RWZwTR.md` — avg 4.75 — WeCAN is stronger; this anchor had more diffuse contribution and weaker support.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JDud6zbpFv.md` — avg 8.00 — WeCAN is weaker; this strong anchor was viewed as a clean, well-supported contribution despite some concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/7BLXhmWvwF.md` — avg 8.00 — WeCAN is weaker; that anchor had a strong benchmark/method package in RL/robotics.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/9pW2J49flQ.md` — avg 8.00 — WeCAN is weaker; that anchor had stronger formal/experimental support for its central claims.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6PbvbLyqT6.md` — avg 8.00 — WeCAN is weaker; that anchor was judged a more mature accepted contribution.

**Round 2**
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/AloCXPpq54.md` — avg 6.00 — WeCAN is stronger; that paper had important design/baseline weaknesses, whereas WeCAN’s empirical evidence and ablations are more convincing.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/CFLEIeX7iK.md` — avg 5.75 — WeCAN is stronger; this anchor is more of a solver-selection framework with less direct methodological impact.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/WszeEzjcq2.md` — avg 5.33 — WeCAN is stronger; that anchor had mixed reviews and more limited positive evidence.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yEwakMNIex.md` — avg 6.25 — WeCAN is stronger overall; RedCO is ambitious but had applicability and reduction-scope concerns, while WeCAN is more focused and empirically cleaner.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GM7cmQfk2F.md` — avg 7.00 — WeCAN is comparable; both have strong neural CO results with some requests for clearer justification/ablation/protocol details.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jKhNBulNMh.md` — avg 6.67 — WeCAN is slightly stronger or comparable; this anchor is innovative but less directly tied to scheduling and has broader interpretability/positioning questions.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/6hvtSLkKeZ.md` — avg 6.40 — WeCAN is stronger; that anchor is a solid neural CO application but less novel and less broadly evidenced.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jsWCmrsHHs.md` — avg 7.50 — WeCAN is somewhat weaker; this scheduling anchor had very comprehensive benchmark support and fewer central overclaiming concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/yEox25xAED.md` — avg 6.60 — WeCAN is comparable to slightly stronger; both have interesting RL/graph ideas, but WeCAN has clearer direct scheduling utility.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jBYQAtzp5Z.md` — avg 6.80 — WeCAN is comparable; this anchor is more theory-oriented scheduling, while WeCAN is more empirical/methodological.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/jKhNBulNMh.md` — avg 6.67 — Duplicate retrieval; comparison as above.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>