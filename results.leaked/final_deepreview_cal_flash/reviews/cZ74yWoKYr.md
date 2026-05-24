Now I have a thorough understanding of the paper and the review inputs. Let me write the final consolidated review.

---

## Summary

This paper presents a formal study of critical KV cache entry identification for LLM inference, framing the problem as minimizing output perturbation when the full cache is replaced with a subset. The authors derive an upper bound on output perturbation (Theorem 3.3) that reveals the importance of value states and the projection matrix $W^O$ — factors overlooked by prior attention-weight-only heuristics. They propose a two-stage greedy selection algorithm that constrains this bound, and integrate it as a plug-and-play replacement for the selection step in three existing eviction frameworks (SnapKV, AdaKV, HeadKV). Experiments on 29 datasets (Ruler + LongBench) across three LLMs (Llama-3.1-8B, Mistral-7B, Qwen2.5-32B) show consistent improvements, reducing average compression loss by more than half.

## Strengths

1. **Novel formalization of critical cache identification as output perturbation minimization.** The paper provides a clean theoretical framework (Definition 3.1, Theorem 3.3) that justifies why value states matter beyond attention weights. This is a principled departure from prior empirical heuristics and opens a new angle for cache-eviction research.

2. **Strong empirical breadth with consistent improvements.** The method is evaluated on 29 datasets (Ruler + LongBench), three LLMs, three base eviction methods, and multiple cache budgets. Across 90 test cases for long-dependency tasks, 88 (97.8%) show improvement. At 40% cache on Ruler, integrating with AdaKV on Qwen2.5-32B raises the average score from 71.09 to 83.87 and reduces loss from 24.3% to 10.7%.

3. **Truly plug-and-play with negligible overhead.** The algorithm replaces only the selection step (Algorithm 2, lines 5–9) and adds minimal computation: at 32K context, TTFT increases by only 0.06s (batch 1) and 0.04s/request (batch 4), while decoding latency is identical to the base eviction method. This makes the contribution immediately practical.

4. **Perturbation analysis confirms the mechanism.** Head-wise (Fig. 4), layer-wise (Fig. 5), and budget-wise (Fig. 6) analyses confirm that the proposed method reduces actual output perturbation — 92% of heads for Llama-3.1-8B and 86% for Mistral-7B show lower perturbation — directly explaining the downstream quality improvements.

5. **Hyperparameter analysis validates the two-stage design.** Table 4 shows that the two-stage structure ($\alpha = 0.5$) is necessary: removing it ($\alpha = 0$) causes catastrophic degradation on Mistral-7B (31.94 vs 42.85), while for Llama the product-only variant works well. This dissection clarifies the roles of the two components.

## Weaknesses

### Major

- **Algorithm 1 does not match its textual description, breaking the claimed theory–algorithm link.** The text (Section 3.4) states that stage 1 selects by *pure attention weights* and stage 2 uses the *product of attention weights and value-state norms*. However, Algorithm 1 computes a single score $\mathcal{A} = (A + \epsilon) \odot \|\mathbf{V}_{i,:}\|_1$ on line 3 and applies this same score in **both** stages. Assumption 3.4 and Theorem 3.5 rely on stage 1 guaranteeing cumulative attention weight > 0.5, but the pseudocode cannot provide this guarantee because it selects by the product, not by attention weights alone. Additionally, the pseudocode header lists $\alpha = 0.25$ while the text and all experiments use $\alpha = 0.5$.

  This is more than a typo: the claimed theoretical grounding for the two-stage design is not actually realized by the presented algorithm. The paper should either (a) revise the pseudocode to use pure attention weights in stage 1 and the product in stage 2 (as the text claims), or (b) revise the text and theoretical analysis to match what the pseudocode actually does (both stages using the product, with the two-stage greedy selection providing a different kind of benefit). The empirical results are strong regardless of which fix is chosen, but the current inconsistency undermines trust in the paper's central claimed contribution.

### Minor

- **Underspecified integration with the observation-window mechanism.** Algorithm 2 calls Algorithm 1 with a single query state $q$, but the paper never states what $q$ is. Is it the last query token from the observation window? The mean of the window? Something else? The base methods (SnapKV, AdaKV, HeadKV) accumulate attention weights over an observation window for their selection, while Algorithm 1 recomputes attention from scratch with a single query. Without specification, the comparison is not fully controlled and the method cannot be reproduced exactly. The authors should clarify this detail and, ideally, ablate whether the single-query vs. accumulated-attention choice affects results independently of the value-state term.

- **Theoretical scope is single-query, but the practical setting is multi-query.** The bound in Theorem 3.3 concerns output perturbation for a *single* attention step with one query. During autoregressive decoding, the evicted cache is used for many future queries. The paper offers no justification for why minimizing a single-query perturbation bound translates to better multi-query performance. While this kind of simplification is common in ML papers and the empirical results are credible on their own, the claimed “formal grounding” is weaker than presented.

- **Perturbation analysis is limited to the first decoding token.** Section 4.7 measures perturbation reduction only on the *first* decoding token. It is plausible that perturbation reduction compounds or decays over the generation — the paper does not examine this. Reporting perturbation on later tokens (e.g., at a few intermediate positions) would strengthen the link between the theoretical motivation and observed task-level improvements.

### Trivial

- **$\alpha = 0.25$ typo in Algorithm 1** — the header says 0.25 while the text and all experiments use 0.5. This should be corrected in the pseudocode.

## Nice-to-Haves

- An ablation that directly controls for the attention-aggregation strategy: compare (i) base method with accumulated attention only, (ii) base method with the product score computed from accumulated attention, (iii) base method with product score from single-query attention. This would cleanly separate the effect of the value-state term from the effect of switching to single-query attention.

- Reporting per-sample correlation between perturbation reduction and task accuracy on the MultiNews subset would strengthen the causal claim linking the theory to the empirical gains.

## Removed Points

These points were raised by reviewers but are removed or downgraded for the following reasons:

1. **"Unfair comparison due to observation-window asymmetry"** (Harsh Critic point 2, fairness aspect) — The claim that the baseline benefits from observation-window averaging while the proposed method uses single-query attention is speculative. The paper does not specify what $q$ is used, so the direction and magnitude of any bias cannot be determined. The criticism that the integration details are underspecified is valid (kept as a Minor weakness), but calling the comparison "unfair" is an unsupported conclusion. *Removed to Minor.*

2. **"These issues are not fixable by adding experiments alone; they require rewriting the algorithm description"** (Harsh Critic) — The issues are indeed fixable with a corrected pseudocode and clarified text. The empirical results are not invalidated. This characterization overstates the severity. *Removed.*

3. **"Missing baselines like StreamingLLM, FastGen, MInference"** (Human Reviewer 1) — The paper explicitly scopes itself as enhancing existing cache eviction frameworks; these are architecturally different approaches. The three chosen baselines (SnapKV, AdaKV, HeadKV) are the most directly comparable SOTA eviction methods. *Removed per instructions not to demand methods outside the paper's scope.*

4. **"Limited to smaller models (7B)"** (Human Reviewer 4) — The paper already includes Qwen2.5-32B and scales to 32B parameters, which is a substantial model size. Requesting 70B experiments for a conference submission in this area is beyond reasonable expectations. *Removed.*

5. **"Request for AlpacaEval evaluation"** (Human Reviewer 2) — The paper focuses on long-context evaluation, which is the relevant scenario for KV cache eviction. Short-context benchmarks like AlpacaEval are outside scope. *Removed.*

## Novel Insights

The harsh critic correctly identifies a mismatch between the algorithm pseudocode and its textual/theoretical framing — this is the paper's most significant weakness and points to a deeper issue in how theory-motivated ML papers sometimes present their algorithms. The theoretical framework (output perturbation bound) genuinely exposes the role of value states, a factor completely absent from prior heuristics. The empirical validation is unusually thorough (29 datasets, 3 models, 3 base methods, multiple budgets). However, the disconnect between the theory (which requires stage 1 to be pure attention-weight selection) and the implementation (which uses the product score throughout) means the paper currently cannot fully support its strongest claim of being a "formally grounded" method — it is a well-motivated heuristic with strong empirical backing. This distinction matters: the paper would be strengthened by either fixing the algorithm to match the theory, or weakening the claims about theoretical guarantees to match what is actually implemented.

## Suggestions

1. **Fix the pseudocode.** Either change Algorithm 1 to implement two separate scoring functions (stage 1: attention weights only; stage 2: product of attention weights and value norms), or change the text and Assumption 3.4 to match the current pseudocode. The $\alpha$ value should be consistent ($0.5$ throughout).

2. **Specify $q$ explicitly.** State in Algorithm 2 exactly what query is passed to Algorithm 1 when the "our selection" branch is taken. If it is the last query token in the observation window, say so and justify why this choice is consistent with the theory.

3. **Acknowledge and discuss the single-query vs. multi-query gap.** Add a brief paragraph acknowledging that the theoretical bound is derived for a single attention step, and discuss why (or whether) minimizing single-query perturbation is a reasonable proxy for multi-query performance. This would strengthen the "formal grounding" claim.

4. **Extend perturbation analysis beyond the first token.** Even a small experiment showing perturbation at a few later decoding steps would significantly strengthen the link between theory and practice.

---

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries covering the score bands yielded the following anchors:
- **Band <3.5:** IntelLLM (3.00), MixAttention (2.00), PrefixQuant (3.00), Polybasic Speculative Decoding (3.00) — all substantially weaker than the current paper, confirming the paper does not belong in the reject-with-major-flaws band.
- **Band 3.5–7.5:** This paper's own human review (5.75), LSH-E (3.83), CAKE (7.00), EMS (4.60) — placing the paper solidly in the middle band.
- **Band >7.5:** Retrieval Head (8.00), Cut Your Losses (8.50), Probabilistic Perspective (8.00), FlexPrefill (8.00) — these are more foundational works or tackle different problems; the current paper is clearly not at this level.

**Round-1 bracket:** [5.0, 7.0].

**Round 2 (Narrowing):** A targeted query in (4.5, 7.5) returned this paper (5.75), MPCache (5.00), MiKV (5.00), and CAKE (7.00). Comparing to these:
- *MPCache (5.00)* — more niche (crypto-specific), less directly comparable. This paper is stronger in both novelty and empirical breadth.
- *MiKV (5.00)* — mixed-precision approach with limited novelty. This paper has a more novel theoretical framing.
- *CAKE (7.00)* — better presentation polish and layer-wise allocation, but less novel theoretically. This paper is slightly weaker on presentation but has a more original theoretical contribution.
- *Own human review (5.75)* — the human reviewers flagged incremental concerns and missing baselines, but acknowledged the solid motivation and reasonable algorithm.

**Final score determination:** The paper's original theoretical perspective and unusually broad empirical validation are genuine strengths. The algorithm-text inconsistency is a real weakness that prevents a higher score. Comparing against the anchors, the paper is clearly above the 5.0 papers and sits between its own human average (5.75) and CAKE (7.00), closer to the former due to the unresolved algorithmic inconsistency. **Score: 6.0.**

**Decision:** Accept. The contribution is solid and well-validated empirically. The major weakness (algorithm-text mismatch) is fixable with careful revision and does not invalidate the empirical results or the core insight about value states.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>