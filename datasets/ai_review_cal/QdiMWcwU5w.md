- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces Dynamic Noise Preference Optimization (DNPO), a self-improvement framework for LLMs that combines two components: Dynamic Sample Labeling (DSL) — which uses an external evaluator to construct preference pairs based on actual quality rather than assuming human data is always superior — and Noise Preference Optimization (NPO) — which injects trainable noise into the reference model's logits to prevent the stagnation that plagues prior iterative methods like SPIN. Experiments on Zephyr-7B show DNPO achieving a 2.6% average improvement over SPIN across benchmarks and a 29.4% win-rate gap in GPT-4 evaluations of generated data quality.

## Strengths

- **Empirical diagnosis of two concrete problems in self-improvement is well-motivated and visually supported.** Figure 1 shows that ~30% of model-generated data equals or surpasses human annotations across iterations, directly motivating DSL. Figure 2 shows that under SPIN, log-probability distributions of generated data remain nearly frozen across iterations, motivating NPO. These diagnostic observations are the paper's strongest conceptual contribution and are clearly presented.

- **Component-level ablation cleanly separates the contributions of DSL and NPO across iterations.** Figure 8 compares SPIN, SPIN+DSL, SPIN+NPO, and full DNPO across three iterations. The paper provides a reasoned interpretation of why DSL dominates in iteration 2 (peak generated-data quality → most mislabeling) and NPO dominates in iteration 1 (early stagnation). This granular analysis gives confidence that both components contribute meaningfully, not just one.

- **Consistent improvement over SPIN on standard benchmarks, not just GPT-based metrics.** Table 1 reports DNPO iteration 3 outperforming SPIN on average (0.612 vs 0.586), with gains on TruthfulQA (+3.4% over SPIN) and ARC (+3.3%). These benchmarks are evaluated via standard held-out metrics, independent of the GPT model used for DSL labeling, so the core claim is partially insulated from the evaluator-confound issue.

- **Figure 10 directly demonstrates the claimed mechanism — DNPO shifts distributions across iterations while SPIN's freeze.** This visual evidence connecting the method's design to its empirical behavior is strong and specific to the paper's core narrative about preventing stagnation.

## Weaknesses

### Fatal

None.

### Major

- **The joint objective (Obj. 10) is confusingly specified and undermines the claimed min-max formulation.** The paper derives a min-max problem (Obj. 9), then states it will not perform iterative min-max updates and instead "update both θ and θ_σ in a single iteration by minimizing" Obj. 10. However, Obj. 10 contains two loss terms that differ only by an unexplained prime (′) on one denominator's probability expression:
  ```
  min_{θ,θ_σ} [ Σ ℓ(... / p'(...))  −  Σ ℓ(... / p(...)) ] + α·(1/N)·Σσ_i²
  ```
  The prime is never defined. The paper's Section 5.4 describes these as "model loss" and "noise loss," but the reader cannot verify from the equations alone what the prime means or why subtracting one ℓ-term from the other implements the intended adversarial dynamic. The text and figure captions (lines 72–73, 88–89) describe an *alternating* freeze-then-train procedure, which is conceptually sound, but the written objective (Obj. 10) does not clearly match this description. The paper needs to either (a) define the prime, (b) explain how joint minimization of this objective approximates alternating min-max, and ideally (c) compare both variants empirically.

- **DSL's improvements are confounded with the use of a strong evaluator for labeling.** DSL uses GPT-4o-mini as `M_eval` to score responses and determine which is positive/negative. The same model (GPT-4o-mini) is then used to evaluate data quality in Figures 6 and 7. The ablation (Figure 8) compares SPIN (no evaluator) against SPIN+DSL (with evaluator), but this does not isolate the *dynamic selection* mechanism from the mere fact of using GPT-based annotations. A proper control would compare SPIN+*static* GPT-labeling (always prefer GPT's judged-better response, without dynamic switching) against SPIN+DSL, to show that the dynamic component, not just the stronger annotations, drives improvement. This is important because much of the claimed advantage (Figures 6, 7) could simply reflect the higher quality of GPT-annotated preferences. Note: the benchmark results in Table 1 are not affected by this confound, which limits the damage but does not eliminate it.

### Minor

- **No error bars, confidence intervals, or multiple-run statistics are reported.** All benchmark scores (Table 1, Figures 5, 8) appear to be single-run point estimates. Given that DNPO's improvement over SPIN is modest (~2.6% average), the results could be sensitive to random seeds in data subsampling (20k from 200k), initialization, or evaluation variance. While single-run reporting is common in LLM papers, the specific nature of the claim — *consistent* improvement across iterations — would benefit substantially from statistical grounding.

- **Key hyperparameters and training details are missing.** The paper does not report learning rate, batch size, optimizer, number of epochs per iteration, number of training steps, or the α penalty coefficient for the variance term in Obj. 10. These omissions hinder reproducibility, especially given the non-standard optimization objective.

- **Only one base model (Mistral-7B / Zephyr-7B) is tested.** The method's generalizability to different model scales (1B, 13B, 70B) or base architectures is unknown. The paper frames DNPO as a general framework for "large-scale AI systems to enhance themselves autonomously," but the evidence is limited to a single 7B model.

- **Only SPIN is compared as a baseline.** Other iterative self-improvement methods (self-rewarding LM, iterative DPO with data filtering, or repeated DPO on self-generated data) would strengthen the evaluation. The paper claims "current methods fail to ensure consistent improvements" but empirically tests only one.

### Trivial

- The DSL equation (Obj. 2) writes ratios as p_θ_t(y|x)/p_θ(y|x) (reference/model) rather than the more standard p_θ(y|x)/p_θ_t(y|x) of DPO. Since ℓ is defined as a negative log-sigmoid function, the sign reversal may be absorbed, but the paper does not explain this, creating unnecessary confusion.

- The conclusion overstates the scope: "provides a path forward for large-scale AI systems to enhance themselves autonomously" is too broad for experiments on a single 7B model across three iterations.

## Nice-to-Haves

- A comparison of the alternating min-max training (as described in prose) versus the joint minimization (Obj. 10) would clarify whether the approximation sacrifices anything.
- Quantifying the stagnation problem with gradient-norm statistics before/after NPO would strengthen the causal narrative.
- Reporting the computational cost of the 131M-parameter noise generator (4096×32000 weight + 32000 bias) relative to the base model would be useful for practitioners.

## Removed Points

These points are flagged to be removed — treat them with caution if cited:

- **"The figure is backed only by GPT-4o-mini evaluation, creating a circular dependency"** (from Harsh Critic's Section 1 note): This is an overstatement. The paper's Figure 1 uses GPT-4o-mini to observe that ~30% of generated data is as good or better than human data. This is a measurement, not a circular dependency. The observation motivates DSL; it is not used as evidence of DSL's success.
- **"Critical baseline missing / reproducibility complaints about undisclosed hyperparameters"**: These are demoted from Major to Minor per instructions — missing hyperparameters are real but addressable, and the paper provides the essential structure.
- **"Missing related works"**: Removed by instruction (cannot confirm from external sources).
- **"No proof in appendix"**: Removed by instruction (appendices are stripped in parsing).
- **"Typo/formatting"** complaints: Removed by instruction (parser artifacts).
- **Strength Finder generic praise** (e.g., "this paper addressed an important problem"): Removed per instruction — generic strengths without specific evidence are dropped.

## Novel Insights

None beyond the paper's own contributions. The harsh critic and strength finder did not surface observations not already present in the paper, though the critic's framing of the DSL confound and Obj. 10 ambiguity are helpful structural critiques.

## Suggestions

1. **Clarify Obj. 10.** Define the prime notation, state whether the two ℓ terms differ in which parameters receive gradients (stop-gradient on noise for the first term?), and explain why the joint minimization approximates the min-max formulation. Even better, add an ablation comparing the described alternating training against the implemented joint minimization.

2. **Add a controlled ablation for DSL.** Compare SPIN + *static* GPT-labeling (always use GPT's judged-best as positive) against SPIN + DSL (dynamic switching based on source). Without this, the DSL mechanism's unique contribution is unidentifiable.

3. **Report error bars (at least 3 seeds)** for the core benchmark results and the ablation study.

4. **Add training details** — learning rate, batch size, optimizer, epochs per iteration, and the α value in Obj. 10 — to a reproducibility statement.

5. **Test on at least one additional model scale or base architecture** to support the claimed generality.
