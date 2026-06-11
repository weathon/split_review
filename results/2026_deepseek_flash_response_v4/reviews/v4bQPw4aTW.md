## Summary

AdaBoN proposes a two-stage, prompt-adaptive strategy for Best-of-N alignment that allocates inference-time compute across a batch of prompts. It first uses an exploration budget (d samples per prompt) to estimate reward distributions via Gaussian KDE, then greedily allocates the remaining budget based on estimated marginal gains, with optimality of greedy allocation justified by a concavity result. Across 12 LM-RM pairs, 50 batches, and 3 datasets, AdaBoN consistently outperforms uniform allocation (BWR consistently > 0.50) and remains competitive against uniform allocations with ~20% larger budgets (EST ~148–156 vs budget B=120).

## Strengths

1. **Theory-aware greedy allocation**: Proposition 3.1 proves that the expected-max function \(f(n) = \mathbb{E}[\max\{c, X_1, \dots, X_n\}]\) is concave and monotonically increasing for any distribution with finite first moment, justifying the optimality of the greedy procedure for the second-stage budget assignment. This explicit theoretical grounding is absent in prior work (Damani et al., 2024).

2. **Comprehensive evaluation within its scope**: The paper evaluates across 4 LMs × 3 RMs = 12 pairs, 50 distinct batches per configuration, and 3 datasets (AlpacaEval, HH-RLHF, PKU-SafeRLHF). Tables 1–2 show consistent BWR > 0.50 across all pairs, with some pairs (e.g., Qwen-Mistral) reaching 100% of batches above 0.50. This is substantially more thorough than Damani et al. (2024), whose real-valued reward experiments cover only a single LM-RM pair and a single batch.

3. **Latency-conscious design**: The two-stage structure requires only two serial calls to the base LM — one for the exploration phase and one for exploitation — since queries within each phase can be parallelized. The paper explicitly motivates this design choice against fully sequential bandit-based alternatives that would incur higher latency.

4. **Minimal hyperparameter tuning**: Scott's rule provides automatic bandwidth selection for KDE, leaving only the exploration budget \(d\) as a tunable hyperparameter. The paper shows (Table 3, Appendix G.1) that fixing \(d = 0.75B\) incurs only a minimal drop in median BWR compared to the best-tuned choice across \(d \in \{0.6B, 0.7B, 0.75B, 0.8B\}\), demonstrating robustness.

5. **Evaluation metrics tailored to the problem**: BWR (Equation 3) correctly accounts for RM scores being only ordinally meaningful, and EST (Equation 5) directly quantifies computational savings against larger uniform budgets. These are more informative than raw expected reward for the reward-model setting.

## Weaknesses

### Fatal

None.

### Major

- **No comparison against any adaptive baseline**: AdaBoN is compared only against uniform (non-adaptive) allocation. The paper explains why a direct comparison with Damani et al. (2024) is impractical (no available implementation, training 216,000 MLPs is prohibitive), but does not implement even a simple heuristic adaptive baseline. Examples: after the exploration phase, allocate remaining budget to the prompt with the lowest observed maximum reward ("least-helped" heuristic), or to the prompt with the largest estimated marginal gain from a different estimation method. Without any adaptive comparator, the experiments show that *being adaptive* helps (which the toy example in Section 2.3 already established) but cannot distinguish whether AdaBoN's *specific design* — KDE estimation + greedy allocation — matters, or whether any reasonable adaptive scheme would perform similarly. This weakens the claim that AdaBoN as a specific algorithmic proposal is an advance over prior art.

### Minor

- **Exploration-exploitation split underexplored**: With \(d = 0.75B\) (90 out of 120) per prompt and \(K = 5\), only 150 out of 600 total LM calls (25%) are allocated adaptively. The ablation in Appendix G.1 explores only the narrow range \(d \in \{0.60B, 0.70B, 0.75B, 0.80B\}\) and does not test smaller exploration budgets (e.g., 0.25B or 0.50B) that would make the adaptive component more impactful. A wider exploration of the trade-off would help characterize how much of the gain comes from the adaptive tail versus the large uniform exploration phase.

- **BWR measures win rate but not magnitude**: BWR tells the reader that AdaBoN wins more often than it loses (0.54–0.62), but not by how much in reward terms. The paper's justification that RM scores are only ordinally meaningful (Section 4.2) is valid for raw scores, but a complementary metric such as the average rank improvement, or the fraction of batches where AdaBoN achieves a strictly better top-1 response, would help assess whether the wins are narrow or substantively better.

### Trivial

None.

## Nice-to-Haves

- Adding a simple adaptive heuristic (e.g., after d exploration samples, allocate remaining budget greedily to the prompt with the lowest observed maximum reward) would substantially strengthen the evaluation at minimal implementation cost.
- Bootstrap confidence intervals on the median BWR across batches would complement the quartile-based reporting in Table 1.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No error bars on main BWR results"** (Harsh Critic): Table 1 already reports median [Q1, Q3] across 50 batches, which is informative about spread. Bootstrap CIs on the median would be a minor addition, not a missing requirement. → Removed (demoted from critique to Nice-to-Have).
- **"EST capped at 2B may truncate distribution"** (Harsh Critic): The observed EST values (~148–156) are well below \(2B = 240\), so the cap does not affect results. → Removed.
- **"Damani et al. comparison not included" framed as a fatal gap** (Harsh Critic): The paper provides valid justification (no available implementation, computational prohibitive cost of 216K MLPs). The lack of *any* adaptive baseline is kept as a Major weakness above, but the specific complaint about Damani being absent is not a fatal oversight given the practical constraints honestly stated in Section 4.2. → Demoted from "fatal/major gap" to "no adaptive baseline" under Major.
- **"Magnitude of wins not reported"** (Harsh Critic): The paper justifies BWR over raw expected reward because RM scores are only ordinally meaningful. This is a principled design choice, not an oversight. → Demoted from critique to Minor.
- **Several generic strengths from Strength Finder** (e.g., "this paper addresses an important problem"): Removed as generic/superficial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any perspective that meaningfully reframes or extends the paper's findings.

## Suggestions

- Add at least one simple adaptive heuristic baseline to isolate whether AdaBoN's specific KDE+greedy design adds value over any reasonable adaptive scheme. The simplest candidate: after the exploration phase, allocate the remaining budget greedily to the prompt with the lowest current observed max reward (a "least-helped" heuristic). This would cost almost nothing to implement and would immediately clarify whether the formal estimation procedure buys anything over common-sense allocation.
- Report the ablation on exploration budget \(d\) over a wider range (e.g., 0.25B to 0.90B) to better characterize the method's sensitivity and the practical impact of the adaptive component.

## Score and Decision

**Round 1 bracketing (three parallel queries with score filters):**
- Weak anchors (avg < 3.5): Polybasic Speculative Decoding (3.00), Efficiently Deploying LLMs (3.00), Inferring from Logits (3.00), FlashSampling (2.50) — all on different topics, AdaBoN is clearly stronger.
- Middle anchors (3.5–7.5): Damani et al. (6.50), Inference-Aware Fine-Tuning (5.67), Inference Scaling Laws (5.75), LASeR (5.25), Large Language Monkeys (5.00), Cost-Effective Multi-LLM (5.50), Prompt Risk Control (6.50).
- Strong anchors (avg > 7.5): Syntactic/Semantic Control via SMC (8.00), Scaling Laws for Precision (8.00), LLAMBO (8.00), Hidden Cost of Waiting (8.00) — all on different topics, AdaBoN is not comparable.

**Round 1 bracket:** 5.0 – 6.5.

**Round 2 narrowing (queries within the bracket):**
- Anchor papers read in full within the bracket:
  - **Damani et al.** (avg 6.50, scores 6/8/6/6): Directly comparable prior work on adaptive compute allocation for LM decoding. Weaknesses include weak baselines (only best-of-k and random), limited evaluation in real-valued reward setting (1 LM-RM pair, 1 batch). AdaBoN has stronger evaluation (12 pairs, 50 batches) and theoretical grounding but narrower scope. → AdaBoN is **slightly weaker** than this anchor.
  - **Inference-Aware Fine-Tuning** (avg 5.67, scores 5/6/6): Evaluated on only 1 model + 1 task. AdaBoN is **stronger**.
  - **LASeR** (avg 5.25, scores 3/5/5/8): Criticized for weak baselines and conceptual concerns about reward definition. AdaBoN is **stronger**.
  - **Large Language Monkeys** (avg 5.00, scores 6/6/5/3): Criticized for limited novelty (trivial scaling observations). AdaBoN is **stronger**.
  - **Cost-Effective Multi-LLM** (avg 5.50, scores 6/5/6/5): Criticized for limited evaluation (1 dataset) and being an incremental extension. AdaBoN is **stronger**.
  - **Inference Scaling Laws** (avg 5.75, scores 6/3/6/8): Different type (analysis paper), comparable quality but AdaBoN has a clearer methodological contribution.

**Final calibration:** AdaBoN is weaker than Damani et al. (6.50) due to narrower scope (alignment only vs. code+math+chat) and the same baseline weakness. It is stronger than the 5.0–5.5 range papers (Large Language Monkeys, LASeR, Cost-Effective Multi-LLM). It is comparable to Inference-Aware Fine-Tuning (5.67). The paper is solid and well-executed within its chosen scope, but the absence of adaptive baselines limits what the evaluation can establish about the method's value relative to alternatives.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>