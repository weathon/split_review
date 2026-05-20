Now I have enough information to produce the final consolidated review. Let me compile my analysis.

**Round 1 bracket**: 5.0–6.5 (based on comparisons to anchors at 4.75, 5.0, 5.75, and 8.0+)

**Round 2 narrowing**: The paper sits between the withdrawn/rejected papers at 4.75–5.25 and the accepted poster at 5.75. It is clearly stronger than the 4.75 and 5.0 papers (better method, clearer story, actual theory), and roughly comparable to the 5.75 poster paper. I place it at **5.5**.

---

## Summary

This paper proposes *label annealing*, a finetuning method that adds a KL divergence penalty between the finetuned model's predictions and the initial model's predictions on the finetuning data itself, to mitigate forgetting when finetuning open-weight LLMs without access to original pretraining data. Experiments on Llama 3 8B span math finetuning, code finetuning, instruction tuning, and niche QA. A theoretical analysis is given in a linear regression setting.

## Strengths

- **Clear empirical preservation of pretraining knowledge.** In math and code finetuning (Tables 1, 2), label annealing retains MMLU and TriviaQA close to the base model while achieving target-domain improvements. For example, in math finetuning, TriviaQA drops only 2.12 points under label annealing (65.87 vs. base 67.99) vs. a 14.19-point drop under direct finetuning. The L2 regularization baseline fails to recover this knowledge.

- **Simple, practical, and well-specified method.** The method requires only two forward passes per batch and a KL divergence term on the finetuning data — no access to original pretraining data. The exposition (Figure 1, Section 2) is clear and the method is directly implementable.

- **Generality across four task settings.** The paper demonstrates the method on math finetuning, code finetuning, instruction tuning (supervised finetuning on UltraChat), and niche QA finetuning on QuALITY — showing either full forgetting mitigation or a smooth, tunable tradeoff.

- **Theoretical intuition via linear regression.** Theorem 1 provides closed-form solutions showing that label annealing preserves the component of pretrained weights orthogonal to the finetuning data while taking a convex combination in the data span — offering geometric intuition that direct finetuning and L2 regularization lack. The simplifications are stated transparently.

## Weaknesses

### Major

1. **Missing stronger baselines.** The paper compares only against direct finetuning and L2 weight decay toward initialization. Multiple stronger and more directly relevant baselines are not evaluated: Elastic Weight Consolidation (EWC), Learning without Forgetting (LwF), or other functional regularization techniques structurally similar to label annealing. The paper frames L2 regularization as a simplified case of EWC (Section 3.1), but this is a substantial simplification that does not substitute for a direct comparison. Without these baselines, the claim that label annealing is the preferred method for this setting is not adequately supported. This is the most important gap.

2. **The replay comparison (Table 3) creates tension with the paper's core motivation.** The paper's central motivation is that pretraining data is unavailable, making experience replay impossible. Yet Table 3 shows that adding 10% replay from the publicly available RedPajama corpus largely solves the forgetting problem on its own — achieving source-benchmark performance comparable to label annealing. The authors' response (that future training strategies will make reconstruction harder) is speculative and does not fully resolve this tension. The paper would be much stronger if it demonstrated scenarios where replay is genuinely impossible or ineffective, or if it compared label annealing against replay in a controlled compute budget.

### Minor

3. **Only one model (Llama 3 8B) is evaluated.** Results are limited to a single model size and family, leaving generality across model scales and architectures unsubstantiated.

4. **Overselling in the abstract.** The abstract claims label annealing "improves the model's performance in target domains without sacrificing other capabilities." This is accurate for the base model math/code experiments but the alignment and niche QA experiments (Figures 2, 3) clearly show a tradeoff rather than a "free lunch." The framing should more carefully distinguish between the two settings.

5. **Compute overhead is not discussed.** The method doubles the number of forward passes per training step (one for the finetuned model, one for the frozen copy). For large models on long contexts this is a meaningful cost, and the paper does not quantify it or discuss this tradeoff.

6. **The linear regression theory, while clean, is only loosely connected to the empirical setting.** The mapping from logit-based KL divergence to squared L2 loss on continuous outputs is approximate, and the single-linear-layer simplification is drastic. The theory provides useful geometric intuition but does not constitute rigorous justification for the nonlinear autoregressive LLM setting. This limitation is partially acknowledged but the section is presented as core evidence.

### Trivial

7. **No variance or statistical significance is reported.** All benchmark numbers are point estimates. Given modest benchmark sizes (e.g., HumanEval has 164 examples), reporting multiple seeds or confidence intervals would improve rigor.

8. **Temperature hyperparameter values are not reported.** The paper states that both λ and T are swept over, but the actual values or ranges of T used in experiments are not provided.

## Nice-to-Haves
- Comparison to EWC, LwF, or similar distillation-based forgetting methods.
- A direct performance-per-compute comparison (target vs. source performance per FLOP) would help practitioners assess the cost-benefit tradeoff.
- Results on at least one additional model family (e.g., Mistral 7B, Llama 2 7B) would strengthen generality claims.
- The replay experiment (Table 3) would be more appropriately placed in the main body, with a discussion of when replay may or may not be feasible.

## Removed Points

- *"Replay table should be in main body"* — This is a presentation preference, not a substantive weakness. Removed.
- *"Missing related works"* — Removed per instructions (cannot verify completeness of related work coverage without external sources).
- *"Pure formatting/style nitpicks"* — None present in the inputs; none removed.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's observation that the replay comparison undercuts the motivation is the most insightful meta-point, but it is surfaced in the weaknesses above and the paper itself partially acknowledges it in the limitations section.

## Suggestions

1. Add comparisons to EWC and LwF (or another distillation-based functional regularization method) to establish that label annealing is genuinely the best available approach, not just better than L2 weight decay.
2. Either strengthen the narrative around when replay fails (and show it empirically) or reframe the motivation to be less reliant on the unavailability of pretraining data. The current framing creates a tension that the paper's own data highlights.
3. Report the temperature values used in hyperparameter sweeps.
4. Discuss compute overhead explicitly — the double forward pass is a real cost that practitioners need to evaluate.

## Score and Decision

**Comparison to calibration anchors:**

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| Dissecting learning and forgetting in LM finetuning | tmsqb6WpLz.md | 5.75 | R1,R2 | Similar quality — this paper has a clearer method contribution but narrower model scope |
| Mitigating Catastrophic Forgetting with FAPM | fHvh913U1H.md | 5.00 | R1 | Our paper is stronger — better motivation, cleaner method, actual theory |
| Fine-tuning can cripple foundation models | VQ7Q6qdp0P.md | 4.75 | R1,R2 | Our paper is stronger — more comprehensive experiments, LLM-specific, with theory |
| Who's Harry Potter? Approximate Unlearning | PDct7vrcvT.md | 5.25 | R2 | Our paper is slightly stronger — cleaner evaluation, broader task coverage |
| Gradual Learning/Partially Mastered Knowledge | EukID7GvBy.md | 3.00 | R1 | Our paper is much stronger — not comparable |
| LVLM-CL | JIlIYIHMuv.md | 2.50 | R1 | Our paper is much stronger |

**Round-1 bracket**: 5.0–6.5  
**Narrowing**: The paper is clearly above the 4.75–5.25 papers (withdrawn/rejected) and comparable to the 5.75 poster paper, but the missing baselines and replay tension prevent it from reaching the 6+ range.  
**Final score**: 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>