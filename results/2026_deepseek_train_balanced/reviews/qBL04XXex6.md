## Summary

Boosting of Thoughts (BoT) proposes an iterative prompting framework for LLM reasoning. In each iteration, BoT generates multiple heterogeneous binary tree-structured reasoning paths, greedily aggregates them into a single chain, has the LLM self-evaluate this chain for errors and advice, and accumulates this "experience" into the prompt for the next iteration. The key insight is that error analysis from diverse reasoning trajectories, accumulated over iterations, can iteratively improve a simple initial prompt without requiring human-annotated examples.

## Strengths

1. **BoT outperforms ToT on Game of 24 by a meaningful margin without human annotation.** On the challenging Game of 24 task, BoT achieves 83.7% vs ToT's 74% (Table 2, lines 186–194) using the same evaluation setup, despite ToT using a hand-crafted prompt with example next-step thoughts. This is a direct, apples-to-apples comparison on a task where prior SOTA (ToT) already substantially exceeded simpler baselines (e.g., CoT at 4%, CoT-SC at 9%).

2. **The ablation study provides controlled, causally attributable evidence for the claimed mechanism.** Table 4 (lines 247–261) systematically ablates experience components (issues, advice), accumulation type (replace vs. add), and aggregation strategy (best-first, greedy, none). The results show that greedy aggregation consistently outperforms best-first by 2–10%, and that including both issues and advice yields the best performance — e.g., 83.7% on Game of 24 with full experience vs. 67.1% without aggregation. This supports the paper's core claim that each design choice contributes measurably.

3. **Qualitative trace demonstrates concrete iterative refinement.** Table 3 (lines 207–232) shows the aggregated thought chains and LLM-generated feedback at iterations 1, 5, and 8 for a specific problem (2, 7, 8, 9 → 24). The progression from vague feedback ("try other numbers and operations") to specific advice ("Evaluation Score: 0.5 is low") to a correct chain is stronger evidence than aggregate metrics alone, as it verifies the claimed mechanism is actually operating.

4. **Edge scores between parent-child nodes provide a principled signal for chain selection and leaf detection.** The edge score $V_{i-1,i}$ (line 81) quantifies confidence in each reasoning transition, enabling chain selection via $\sum V_i + V_{i-1,i}$ and leaf detection via thresholds. This is a testable design contribution that differs from ToT's uniform node evaluation.

## Weaknesses

### Major

1. **Numerical errors in Table 1 undermine trust in quantitative results.** Several values in the main results table and their deltas are incorrect, as verified directly from the paper's own numbers:
   - **AQuA**: BoT = 81.4, SOTA = 79.9, actual delta = **+1.5**, but Table 1 reports **↑2.5** (line 134). The same error appears in the prose at line 165 ("BoT is 2.5% higher than SOTA").
   - **BoT average**: Computing (92.7 + 97.1 + 81.4 + 62.5) / 4 = **83.4**, but the table reports **83.7** (line 134).
   - **Average delta**: The correct BoT-to-SOTA average gap should be approximately **−5.3** (83.4 − 88.7), not the reported **↓7.6**.
   
   These are not parser artifacts — they involve numbers the authors themselves computed and reported. Two of the five reported deltas are wrong, plus the average value itself. While the errors do not reverse the paper's conclusions, they are a concrete accuracy concern for the paper's primary evidence table.

2. **The "SOTA" baseline is a composite from different methods, making headline comparisons misleading.** The SOTA row (line 126) composites results from three different papers: Model Selection (best on SVAMP), PHP (best on AQuA), and CSV (best on GSM8K and MATH). No single method simultaneously achieves all four numbers. Computing an "Average" over this composite (88.7) and comparing BoT against it conflates performance across methods. The paper's claim that BoT "significantly surpasses the current state-of-the-art" (line 30, line 275) is based on this composite framing. Direct comparisons against individual methods (e.g., BoT vs CSV on all datasets) would be more appropriate and would make the MATH gap (where CSV achieves 84.3% vs BoT's 62.5%) less susceptible to framing effects.

3. **Computational cost is never quantified, despite the method being substantially more expensive than any baseline.** BoT uses M=15 trees per iteration for T=10 iterations. Each weighted binary tree involves multiple LLM calls (generating each node, scoring each node, scoring each edge). The total LLM-call count per problem is orders of magnitude larger than CoT (one call) and substantially larger than ToT (which searches a single tree). The paper claims BoT is "fast" (line 30) but provides **no wall-clock time, no token counts, no API cost estimates, and no comparison of computational budget against any baseline**. Without this information, the reader cannot assess whether BoT's gains are architectural or simply a function of vastly more LLM queries. The parallel-construction claim addresses wall-clock latency but not total computational cost.

### Minor

4. **The method is underspecified in several respects critical for reproducibility.**
   - **Greedy aggregation matching** (line 92): "BoT searches all thoughts where the previous step is $\overline{z}_{i-1}$." Thoughts are natural-language strings. Is matching performed via exact string match, semantic similarity, or some other criterion? What happens when multiple candidate next-steps exist across different trees? This is the core mechanism of the claimed best-performing variant.
   - **Prompt templates**: The evaluation prompts $\sI_a$, $\sI_e$, and $\sI_f^t$ (for thought scoring, edge scoring, and chain analysis) are referenced but never shown in the paper. These are essential for reproducibility.
   - **Experience formatting**: The paper describes experience $\mathbf{F}^t$ as containing the thought chain, error reports, and advice, but never specifies how these are formatted, structured, or inserted into the prompt. Does the prompt grow without bound across iterations? Are older experiences truncated?
   - **Tree growth strategies**: Level-wise and leaf-wise growth are invoked by analogy to XGBoost/LightGBM but no algorithmic description is given for how they operate on language thought trees.

5. **The large MATH gap (21.8% below SOTA) is not adequately explained.** The paper attributes this to "weak LLMs may not perform well with BoT due to their lower ability to analyze reasoning chains" (line 165). However, the MATH results in Table 1 are from GPT-4 — the strongest available model. No analysis is provided of whether the issue is insufficient iteration count, inadequate tree depth/shape for MATH problems, or a fundamental limitation of the error-analysis approach on difficult multi-step mathematics. This is the paper's largest performance deficit and warrants deeper investigation.

6. **Overclaim on priority regarding "error analysis."** The paper states "our work is the first to highlight the importance of error analysis in enhancing the prompt" (line 41). However, the related work section itself cites Self-Refine (iterative self-refinement with LLM feedback), REFINER (evaluating each reasoning step as feedback), PHP (adding previous answer as a hint), and APO (iterative prompt refinement based on performance). The distinction between "error analysis" and the model-generated feedback used in these prior works is not sufficiently delineated to support a "first" claim.

### Trivial

7. **The leaf-threshold range [0.3, 0.8] (line 83) is stated without justification or sensitivity analysis.** How sensitive are results to this threshold? Where does it come from?

## Nice-to-Haves

1. Compare BoT against ToT under a matched computational budget (controlling for total LLM calls or total tokens consumed) to determine whether gains persist at equivalent cost.
2. Replace the composite SOTA row with direct comparisons against the strongest single baseline method on all datasets.
3. Provide full prompt templates for $\sI_a$, $\sI_e$, and $\sI_f^t$ in a supplementary section.
4. Report variance or confidence intervals for main results, given that LLM outputs are stochastic and margins are small (0.1–1.7% on some benchmarks).
5. Analyze the MATH failure mode — is it iteration count, tree depth, or the nature of error analysis on multi-step mathematics?

## Removed Points

These points were considered but moved here with justification:

- **"No human annotation tension"** (Harsh Critic): The critic claimed the paper's best results come from BoT+CoT (which uses human annotations), creating a tension with the annotation-free claim. However, the paper clearly distinguishes BoT (no annotation, surpasses SOTA on GSM8K by 0.1% and AQuA by 1.5%) from BoT+CoT (with examples, even better). The claim about surpassing SOTA without annotation is supported by BoT's own reported numbers. This criticism reflects a misreading of the paper. **Removed: factually incorrect.**

- **"First to highlight error analysis" scope creep** (Harsh Critic section-by-section notes about the related work claim): This concern is retained as a Minor weakness above. The critic's broader framing about the claim needing "precise" wording is subsumed by item 6.

- **Section-by-section notes about framing conflation in the Introduction**: The critic claimed the introduction conflates two different criticisms of prior work (discarding ineffective thoughts vs. requiring human annotation). This is an opinion about presentation style, not a verifiable weakness. **Removed: opinion, not a concrete flaw.**

## Novel Insights

Beyond the paper's own contributions, an interesting observation emerges from the qualitative trace (Table 3) and the ablation study taken together: the BoT mechanism works not because individual error analyses are highly accurate, but because accumulation across iterations dilutes the impact of any single flawed analysis. The first-iteration feedback is vague ("try other numbers") yet the method still converges. The ablation shows that even when only advice (without issues) is used, performance degrades but doesn't collapse (e.g., 80% vs 83.7% on Game of 24). This suggests the framework is robust to noisy self-evaluation — the aggregation and accumulation steps may be more important than the quality of any individual error analysis. The paper does not explicitly explore this robustness property, but the evidence is present in its results.

## Suggestions

1. **Correct the numerical errors in Table 1 and the corresponding prose.** The AQuA delta (+1.5, not +2.5), the BoT average (~83.4, not 83.7), and the average delta (~−5.3, not −7.6) all need fixing.
2. **Add a computational cost analysis** (token counts, API cost, or wall-clock time per problem) comparing BoT against CoT, CoT-SC, and ToT at comparable budgets.
3. **Replace the composite SOTA row with direct per-method comparisons**, or at minimum clarify that SOTA values come from different methods and remove the composite average.
4. **Specify the greedy aggregation matching mechanism** — how are natural-language "previous steps" matched across trees?
5. **Include the prompt templates** for $\sI_a$, $\sI_e$, and $\sI_f^t$ in a supplementary section.
6. **Conduct a sensitivity analysis** on the leaf threshold [0.3, 0.8] and report variance for main results.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>