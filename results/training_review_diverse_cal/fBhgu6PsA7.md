I've now read the full paper and verified the reviewer claims. Let me produce the final consolidated review.

---

## Summary

This paper proposes MoFO (Momentum-Filtered Optimizer), a fine-tuning algorithm for LLMs that selects and updates only the parameters with the largest momentum magnitudes within each parameter block at every iteration. The core idea is to keep the fine-tuned model closer to the pre-trained initialization than full-parameter fine-tuning, thereby mitigating forgetting of pre-training knowledge. The paper provides empirical validation on instruction fine-tuning (MetaMathQA, Code-Alpaca with Llama-2-7B) and continual fine-tuning (TRACE benchmark with TinyLlama-1.1B), plus a convergence analysis of a gradient-descent variant and ablations comparing momentum-based, gradient-based, and random selection rules.

## Strengths

1. **Clean, well-motivated algorithm with a tight empirical loop.** The paper identifies a concrete correlation (closer minima → less forgetting) and designs MoFO to directly exploit it. Figure 3 shows MoFO converging ~5× closer to the pre-trained model than Adam while achieving nearly identical fine-tuning loss, directly supporting the central thesis.

2. **MoFO outperforms regularization-based methods on both fine-tuning task performance and forgetting mitigation.** On MetaMathQA (Table III), MoFO achieves GSM8K=47.7% vs. L1 (39.0%) and L2 (44.5%), while improving average general capability by +0.4% — in contrast to L1 (-0.3%) and L2 (-0.4%), which both degrade. This validates the paper's claim that not modifying the loss function preserves fine-tuning performance.

3. **Strong ablation showing momentum-based selection is strictly better than gradient-based or random selection at the same budget.** Table IV (all at 10% update fraction) shows MoFO (45.4% GSM8K) substantially outperforms Gradient-filtered BCD (40.2%) and Randomized BCD (35.0%). This isolates the momentum selection mechanism as the driver of performance, not merely updating fewer parameters.

4. **Demonstrated compatibility with replay methods in continual learning.** On the TRACE benchmark (Table V), MoFO+Replay achieves OP=47.0 vs. Replay alone (45.5), and MoFO+GEM achieves OP=41.7 vs. GEM alone (40.8). This shows MoFO can be stacked with existing forgetting-mitigation techniques.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparisons to the most directly relevant baselines for forgetting mitigation.** The paper evaluates against Full FT, L1, L2, and HFT, but does not compare against Elastic Weight Consolidation (EWC) — a widely used regularization method specifically designed to constrain important parameters — or LoRA, the most popular parameter-efficient fine-tuning method, which the paper itself acknowledges "forgets less" (Related Works). The paper's central claim is "superiority over existing methods in mitigating forgetting" (Abstract), but EWC and LoRA are the methods any practitioner would benchmark against. The L1/L2 comparisons provide partial evidence but are not sufficient to substantiate this broad claim. This gap is notable given the paper makes empirical assertions about how these method classes compare (e.g., that modifying the loss "may impair fine-tuning performance" — shown against L1/L2 but not tested against the more principled EWC; that LoRA "forgets less but learns less" — stated but not tested head-to-head).

### Minor

2. **Convergence analysis is for a substantially different algorithm than the one used in practice.** The paper proves convergence (Theorem 1) for a gradient-descent version of MoFO that filters by gradient magnitudes, not the proposed Adam-based momentum-filtering version. The paper is transparent about this gap ("it seems rather non-trivial to prove the convergence of the original version of MoFO"), but the abstract's phrase "rigorous convergence analysis" overclaims by implying the actual algorithm is analyzed. The theoretical result is standard for nonconvex block coordinate descent with Lipschitz gradients and does not provide insight into the momentum-based selection mechanism that is the claimed contribution.

3. **No statistical uncertainty reported.** The paper does not report the number of seeds, standard deviations, or confidence intervals for any experiment. For key claims (e.g., MoFO's +0.4% average improvement vs. Full FT's -5.6% decline on MetaMathQA), it is impossible to assess whether the differences are statistically significant. Single-run evaluations are common in LLM fine-tuning due to cost, but this should at minimum be acknowledged as a limitation.

4. **No analysis of computational overhead.** The momentum filtering operation requires sorting momentum values within each parameter block at every iteration, introducing O(d_k log d_k) overhead per block. The paper states it partitions to "reduce computational complexity" (line 128) but provides no wall-clock time comparison against standard Adam or HFT. For practitioners, the practical overhead matters for adoption.

### Trivial

5. The toy example in Section 5 illustrates intuition but is carefully constructed (a 2D loss surface with minima along lines) and does not constitute evidence about the loss landscape of actual LLMs. The paper correctly scopes this as an "insight," so this is not a flaw — merely worth noting that the claimed mechanism (reducing "interference among attractors") remains a plausible story rather than a demonstrated fact.

6. The continual fine-tuning evaluation (Table V) reports only aggregated OP and BWT scores without showing per-task accuracies. Per-task results would help assess whether MoFO preserves different types of knowledge uniformly or trades off across tasks.

## Nice-to-Haves

- A comparison against a version of MoFO that selects parameters based on the full Adam update magnitude |m̂/√(v̂+ε)| rather than raw momentum |m_t| would clarify whether the specific choice of momentum magnitude is critical or if any "large update" selection rule works.
- An experiment tracking the correlation between momentum magnitude and eventual contribution to reducing fine-tuning loss vs. moving away from initialization would deepen the mechanistic understanding.
- Some guidance for selecting α across different tasks/models (e.g., based on a measurable property of the optimization trajectory) would improve practical usability.

## Removed Points

- **"HFT comparison confounded by parameter count" (from Harsh Critic):** The ablation study in Table IV directly controls for update fraction (all methods at 10%) and shows MoFO > Gradient-filtered > Randomized BCD. This already establishes that the *selection rule* matters, separate from the per-iteration parameter count. The direct HFT comparison (where HFT uses ~50% and MoFO uses 15%) actually *strengthens* MoFO's case by showing it can do more with less.
- **"Toy example does not constitute evidence" as a weakness:** The paper explicitly frames this as a toy example for intuition (Section header: "Why MoFO Converges to a Closer Point"; line "We attempt to answer this question by the following toy example"). It is not presented as empirical evidence. Criticizing it for not being evidence is misreading its intended role.
- **"Adam vs Lion observation is a known phenomenon":** This is background/motivation, not a claimed contribution. Its purpose is to establish the correlation between distance and forgetting to motivate the method, not to claim novelty.

## Novel Insights

The reviews collectively surface a deeper point: the paper would benefit from empirically bridging the gap between the toy example's intuition and the real optimization dynamics. The central claim is that MoFO's momentum-based selection reduces "interference among attractors," but this remains a hypothesized mechanism. An analysis experiment tracking, at each iteration, which parameters are selected and how their selection correlates with movement toward vs. away from the pre-trained initialization would transform a plausible story into a demonstrated fact. This is a stronger criticism than simply "add more baselines" — it cuts to whether the paper's claimed *explanation* for MoFO's behavior is correct.

## Suggestions

1. **Add EWC and LoRA as baselines** in the instruction fine-tuning experiments (MetaMathQA and Code-Alpaca). This is the single most impactful addition. If computational budget is limited, prioritize LoRA on the MetaMathQA setting where the paper's claim about "high-rank updates achieving better fine-tuning performance" can be directly tested.

2. **Scoping the theoretical claim more precisely** — replace "rigorous convergence analysis" in the abstract with "convergence analysis of a simplified gradient-descent variant" to match what is actually proved.

3. **Report at least 2-3 seeds** for a representative setting (e.g., the MetaMathQA experiment with the key methods) with means and standard deviations, or at minimum acknowledge single-run evaluation as a limitation.

4. **Include a brief wall-clock time comparison** (e.g., training steps per second for MoFO vs. Adam vs. HFT on Llama-2-7B) to quantify the computational cost of the sorting operation.

5. **Add per-task accuracies** for the TRACE continual learning benchmark (as a table or appendix figure) to show the distribution of forgetting across task types.

## Score and Decision

**Originality:** The idea of using momentum magnitudes as a selection criterion for BCD-style updates is novel and well-motivated. **Importance:** Mitigating forgetting during LLM fine-tuning is a timely and practically important problem. **Claims:** The core empirical claims are supported against the baselines tested, but the broad claim of "superiority over existing methods" is not fully substantiated without EWC/LoRA comparisons. **Soundness:** The experiments are well-designed and the ablations are informative, but the lack of statistical uncertainty measures weakens confidence. **Clarity:** The paper is clearly written and well-structured. **Value:** The method is simple, has no dependency on pre-training data, and is orthogonal to replay strategies — making it practically useful.

The paper makes a solid, well-motivated contribution with a clean algorithm, informative ablations, and consistent positive results. The main gap is the absence of comparisons to EWC and LoRA, which are the most directly relevant methods for the problem being addressed. This is a notable weakness but not a fatal one — the paper still demonstrates genuine value against the baselines it does include. The theoretical analysis is honestly scoped in the main text. Overall, the paper would benefit from strengthening these comparisons, but in its current form it represents a useful contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>