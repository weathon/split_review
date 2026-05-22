Now I have sufficient calibration context. Let me write the consolidated review.

## Summary

This paper identifies and formalizes a novel practical problem in multi-modal entity alignment (MMEA) — Dual-level Noisy Correspondence (DNC), where misalignments occur simultaneously at the intra-entity (entity-attribute) and inter-graph (entity-entity and attribute-attribute) levels. The authors propose RULE, a framework that: (1) estimates correspondence reliability via a two-fold principle (uncertainty + consensus), (2) uses these estimates for robust attribute fusion and a dually robust loss for inter-graph alignment, and (3) employs a test-time MLLM-based Chain-of-Thought reasoning module to uncover latent attribute connections. Experiments across five benchmarks with seven baselines show consistent and often substantial improvements, with RULE maintaining strong performance even at 50% injected noise where baselines collapse.

## Strengths

- **Novel problem definition (DNC) with real-world justification**: The paper identifies and formalizes a genuinely overlooked challenge in MMEA — the simultaneous presence of intra-entity and inter-graph noisy correspondences. Figure 1(b) empirically demonstrates that both types of noise degrade existing methods, and the statistics cited (over 50% noise in ICEWS benchmarks) ground the problem in real data. This is a clear, well-motivated contribution.

- **Two-fold reliability estimation principle (uncertainty + consensus)**: Theorem 1 (Eq. 4) correctly motivates why uncertainty alone is insufficient, leading to the complementary consensus principle. Figure 4 cleanly validates that the two measures separate the three subsets (S_U, S_I, S_C), and Figure 3(b) shows the combined reliability score distinguishes clean from noisy pairs. The greedy marginal-contribution strategy for estimating consensus when ground-truth is unavailable (Eq. 6-7) is a principled approach inspired by information theory.

- **Comprehensive and highly competitive experimental results**: RULE is evaluated against seven SOTA methods on five benchmarks under three noise levels. The results are broadly impressive — for example, on ICEWS-WIKI Non-Name at 50% DNC (Table 1), RULE achieves H@1=58.2 vs. the best baseline at 42.4 (MEAformer), a 37% relative improvement. The advantage holds across all 15 Non-Name settings and all 15 All-attributes settings, and Figure 3(a) shows RULE's performance degrades much more slowly as noise increases.

- **Ablation studies validate each component**: Table 3 shows that removing the Dually Robust Learning ("w/o DRL") drops H@1 from 58.2 to 31.6, the TTR module contributes about 1.7 points, and the DRF module contributes about 7.8 points. These ablations cleanly isolate the contribution of each design choice.

- **Code released**: The paper provides a GitHub repository, supporting reproducibility.

## Weaknesses

### Fatal
None.

### Major

- **Test-time MLLM module is expensive and its cost is unreported**: The TTR module uses Qwen2.5-VL-72B-Instruct (72B parameters) with CoT prompting. For each entity, the module scans candidate attribute pairs from T_i^m (the highest-similarity correspondences) and runs a CoT prompt per candidate. The paper does not report: (a) the total number of MLLM calls, (b) runtime on any benchmark dataset, or (c) any discussion of practical deployment feasibility. For DBP15K (~15K entities), the per-entity cost could be substantial. This is a significant practical limitation — the contribution partially hinges on access to a very large MLLM, and no cheaper alternative or analysis is provided. The term "test-time robustness" is also somewhat imprecise here, since the module is less about robustness to label noise and more about leveraging external knowledge to improve recall.

- **The greedy consensus estimation is under-specified**: In Section 2.2.2, the value function is defined as `v(π) = max( (1/|π|) ∑_{j∈π} s_i^j )`. The `max()` operator is ambiguous — max over what? The notation suggests max over candidate entities, but this is not stated. The initial subset size is set to `⌊M/2 + 1⌋` without justification for why this particular size is chosen. The greedy strategy in Eq. 7 lacks pseudocode. This section needs clarification for reproducibility; as written, a reader cannot fully re-implement this component.

### Minor

- **Self-adaptive threshold determination has a circular dependency**: The thresholds β_u and β_c (Eq. 8) are computed from S_TP, defined as indices where the model's argmax matches the *annotated* label y_i. When inter-graph correspondences are noisy, y_i is unreliable, so S_TP may include noisy pairs. The paper estimates correct correspondences via the greedy strategy (Eq. 7), but this estimation itself depends on the current model's similarity scores, which are initially weak. This circularity is common in self-training and can work in practice, but the paper does not analyze when it might break (e.g., at very high noise levels). The ablation results at 50% noise suggest it works, but a discussion of initialization or warm-up is missing.

- **No confidence intervals or standard deviations reported**: Results in Tables 1-2 are reported as point estimates. Given random initialization, noise injection, and potentially stochastic training, standard deviations over multiple runs (e.g., 3-5 seeds) would be standard practice. The large margins make this less critical, but it remains an omission.

- **Dirichlet-based loss choice lacks comparative justification**: The dually robust loss (Eq. 11) uses MSE between refined labels and predicted probabilities under the Dirichlet density. Using MSE rather than the more standard Dirichlet-based cross-entropy (as in evidential deep learning) is unusual. The paper justifies it via Theorem 2 (upper bound proportional to Q_i), but no ablation compares against an alternative loss formulation (e.g., cross-entropy with the same pair-division strategy). Without this comparison, the specific benefit of the evidential formulation over simpler alternatives is unclear.

- **The paper lacks a limitations section**: Obvious limitations that should be discussed include: reliance on a very large MLLM at test time, potential failure when both uncertainty and consensus are miscalibrated, and the assumption that attribute encoders are fixed during training.

### Trivial

- "Theorem 1" (Eq. 4) is a straightforward observation rather than a substantive theorem. The proof in Appendix E is likely a few lines. This is a minor overclaim.

- The value function in the consensus estimation is not fully specified (as noted above in Major). This is both a reproducibility and a presentation issue.

## Nice-to-Haves

- A sensitivity analysis on the threshold hyperparameter β (fixed to 0.3 everywhere) would strengthen the claim of robustness.
- Reporting inference cost (number of MLLM calls, total runtime on one benchmark) for the TTR module would substantially address the practical concern.
- An ablation using standard cross-entropy loss (or a simpler MSE baseline) vs. the Dirichlet-based loss would clarify the benefit of the evidential formulation.
- Results on the "name" attribute alone, as a simple textual matching baseline, could help contextualize the improvements (though this is already implicit in the Non-name vs. All-attributes comparison).

## Removed Points

These points were flagged but removed after verification against the paper:

- **"Baseline comparison is unfair because baselines aren't designed for noise"**: The paper uses the same CLIP backbone and standard evaluation protocols. The comparison is informative — it shows *how much* existing methods degrade under noise, which is precisely the paper's motivation. This is a feature, not a bug. **Removed.**

- **"CLIP backbone not specified for all methods"**: The paper explicitly states "For fair comparisons, we adopt the same backbone (i.e., CLIP) for all baselines and our method." **Removed.**

- **"Not yet released / cannot be independently verified"**: The paper provides a GitHub repository link. Speculation about unreleased artifacts is disregarded per hard rules. **Removed.**

- **"Appendix content cannot be verified"**: Appendix content was stripped by the parser; the original submission includes these sections. Per hard rules, this is not a valid weakness. **Removed.**

- **Various formatting/typo nitpicks**: These are parser artifacts, not author errors. **Removed.**

## Novel Insights

The paper's framework-level insight — that noisy correspondence in MMEA requires *simultaneous* treatment of intra-entity and inter-graph noise through a unified reliability estimation — is genuinely novel and applicable beyond this specific task. The two-fold principle (uncertainty + consensus) is well-motivated: uncertainty captures whether the model has *any* strong belief, while consensus captures whether that belief aligns with the annotation. This dual lens could be useful in other alignment tasks with noisy correspondences. The innovation of using an MLLM at test time to resolve attribute-level ambiguities that survive training-time noise is also noteworthy, though its practical cost limits the insight.

## Suggestions

1. **Clarify the greedy consensus estimation** (Section 2.2.2): Provide pseudocode, specify what the `max()` operator ranges over, and justify the initial subset size. Without this, the method cannot be faithfully reproduced.

2. **Report TTR inference cost**: On at least one benchmark (e.g., ICEWS-WIKI), report the number of MLLM calls, total runtime, and the candidate pool size |T_i^m|. Discuss whether a smaller MLLM (e.g., 7B) could be used as a cheaper alternative and with what accuracy trade-off.

3. **Add standard deviations**: Run the main experiments (Tables 1-2) with at least 3 random seeds and report standard deviations.

4. **Add a loss ablation**: Compare the proposed Dirichlet-based MSE loss against a standard cross-entropy loss (with the same pair-division strategy) to isolate the benefit of the evidential formulation.

5. **Add a limitations paragraph**: Acknowledge the practical cost of the TTR module, the potential for circular dependency in threshold estimation to fail at extreme noise levels, and the assumption of fixed attribute encoders.

## Score and Decision

**Calibration report.**

Round 1 bracket: Based on three queries, the paper clearly sits above the 3-4 range (weak/rejected papers) and below the 8.0 range (exceptionally clean top-tier papers). Initial plausible bracket: **5.5–7.5**.

Round 2 anchors compared:

| Anchor | Avg Score | Round | Comparison to this paper |
|--------|-----------|-------|-------------------------|
| GEEA (z3dfuRcGAK) | 6.67 | 1,2 | Weaker empirical evaluation (fewer baselines/datasets), more theoretical framing. This paper is at least as strong. |
| MoMoK (ue1Tt3h1VC) | 6.60 | 1,2 | Mixed reviews citing limited novelty. This paper has clearer novelty (new problem definition). Slightly stronger. |
| NeuSymEA (NNUiUwQWx6) | 5.75 | 1,2 | Outdated dataset (DBP15K only), weaker empirical results. This paper is clearly stronger. |
| MOFI (QQYpgReSRk) | 6.25 | 2 | Mainly a scale/data contribution with limited technical novelty. This paper has stronger technical novelty. |

Round 1 bracket: (5.5, 7.5). Round 2 narrowed the plausible range to **6.0–7.0**. Comparing against GEEA (6.67) and MoMoK (6.60), this paper has stronger novelty (new problem definition) and more comprehensive evaluation, but also has more unresolved concerns (TTR cost, under-specified components, missing confidence intervals). The final score is positioned at the lower end of the range suggested by the strongest comparable papers, reflecting that the weaknesses, while not fatal, are genuine gaps the authors should address.

**Score: 6.5 — This is a solid paper with a clear novel contribution (the DNC problem formulation) and strong empirical support. The main concerns (under-specified methodology in one component, unreported MLLM inference cost, missing confidence intervals) are addressable and do not undermine the core claims, but do prevent the paper from reaching the highest tier.**

**Decision: Accept**

<score>6.5</score>
<decision>Accept</decision>