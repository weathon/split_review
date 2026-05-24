Now I have all the information I need. Let me write the consolidated review.

---

## Summary

This paper studies how architectural choices—hidden size, mlp-to-attention ratio, and grouped-query attention—affect both inference throughput and training loss in decoder-only LLMs. The authors train over 200 models (80M to 3B parameters) and fit a conditional scaling law that augments the Chinchilla framework with architectural parameters. A search framework then identifies architectures that are Pareto-optimal in the accuracy–throughput trade-off. The resulting models (Panda, Surefire) achieve up to 42% higher inference throughput and 2.1% higher downstream accuracy compared to LLaMA-3.2 baselines under identical training budgets.

## Strengths

- **Substantial empirical foundation.** Over 200 models are trained across 80M–3B parameters with systematic variation of hidden size, mlp-to-attention ratio, and GQA. This dataset alone is a valuable resource for the community and grounds the paper's claims in real measurements rather than speculation.

- **Clear, well-validated empirical regularities.** The U-shaped loss curves for \(d_{\text{model}}/\sqrt{N}\) and \(r_{\text{mlp/attn}}\) (Figures 4–5) are consistent across model sizes and justify the functional forms used in the conditional scaling law. The inference throughput ablations (Figure 3, Appendix F–G) cleanly isolate the effects of each architectural factor across hardware platforms and serving frameworks.

- **Concrete, practically meaningful gains.** Under identical training setups, Panda-1B reduces training loss from 2.803 to 2.782 vs. the LLaMA-3.2-1B architecture and improves average zero-shot accuracy by 2.1 percentage points (Table 1). Surefire-1B matches the LLaMA baseline's loss while delivering up to 42% higher inference throughput on A100 with vLLM (Figure 7), with the throughput advantage persisting across SGLang and H200 (Appendix F–G).

- **Honest and thorough ablation of the method's limitations.** The paper does not oversell its scaling law as universal. Section 5.1 and Table 2 explicitly show that fitting on 1B models produces better 3B predictions than fitting on smaller scales (Spearman 1.000 vs. 0.500 in Figure 8), and the authors provide the pragmatic guideline of fitting on models roughly one-third the target size. This transparency strengthens rather than weakens the contribution.

- **The conditional calibration framework is simple, practical, and empirically validated.** The multiplicative calibration (Eq. 3) achieves MSE ≤ 0.0002 and Spearman ≥ 0.74 across three progressively harder extrapolation tasks (Figure 6). The two-step approach (Chinchilla reference + architectural calibration) is straightforward to adopt and does not require exotic infrastructure.

## Weaknesses

### Fatal

None.

### Major

- **The fitted coefficients shift appreciably across model scales, constraining the law's universality.** Moving from the multi-scale fit (80M–1B) to the 1B-only fit for 3B prediction changes the optimal \(r_{\text{mlp/attn}}\) from 1.055 to 1.229 (Section 5.1, Table 2), and the coefficients \(a_0, a_1, b_0\) shift meaningfully. This means the law is not a one-time fit that extrapolates indefinitely—it is closer to a local empirical model that should be refitted when the target scale changes substantially. The paper acknowledges this and reframes it as pragmatic guidance ("fit on models around one third of the target size"), but the headline framing of a "conditional scaling law" sets expectations higher than what the evidence supports. This limits generality but does not invalidate the method, which remains cheaper than brute-force search at the target scale.

### Minor

- **No uncertainty quantification for downstream accuracy improvements.** Table 1 reports a 2.1% average accuracy gain for Panda-1B and 0.6% for Panda-3B over LLaMA baselines without confidence intervals, standard deviations, or significance testing. The per-task breakdown is referenced as being in Appendix L (which exists in the original submission but was stripped by the parser). While single-run reporting is standard in this subfield, the training-loss reductions are modest (e.g., 2.803 → 2.782 for 1B), so knowing whether the downstream gains are robust would strengthen the evidential case.

- **The baseline comparison protocol could be stated more explicitly.** Table 1 reports training loss for LLaMA-3.2-1B and LLaMA-3.2-3B, which strongly implies the authors retrained these architectures under their own setup (since training loss under the authors' data/training regime would not be available from public checkpoints). However, the text uses the phrase "open-weight LLaMA-3.2-1B baseline configs," which could be read either way. Stating unambiguously that all models in Table 1 were trained under identical conditions would preempt confusion.

- **The derivation of \(L_{\text{opt}}(N,D)\) is vague.** Section 4 says: "instead of fitting the Chinchilla scaling law, we empirically searched over architecture variants to find the optimal loss \(L_{\text{opt}}(N, D)\) for \(N_{\text{non-embed}} < 1\text{B}\) scale." It is unclear whether this means taking the minimum observed loss among all trained variants of a given size, or fitting a Chinchilla-style law and using its prediction. Clarifying this would aid reproducibility.

- **Hyperparameter sensitivity across architectures is not discussed.** Training hyperparameters (learning rate, batch size, warm-up, etc.) were fixed across all 200+ architectures following prior work. If some architectural configurations interact differently with these choices, the reported loss rankings could partly reflect hyperparameter–architecture interaction. The paper does not include a sensitivity analysis (e.g., re-training a subset of architectures at a different learning rate). This is a generic concern that applies to most scaling-law work and does not undermine the core findings, but acknowledging it would strengthen the paper.

### Trivial

- The term "conditional scaling law" in the title and abstract encourages readers to expect a universal relationship akin to Chinchilla. The paper's own evidence shows it is more of a local empirical model requiring refitting at new scales. Adjusting the terminology—or at least prominently caveating the scope—would better align framing with evidence.

## Nice-to-Haves

- A sensitivity test retraining a handful of architectures at two different learning rates to confirm that the discovered optimal architectures are robust to hyperparameter choice.
- Discussion of whether the optimal architecture depends on prompt/generation length and batch size (the paper studies a fixed 4096/1024 pattern, which is reasonable for a first study, but deployment patterns vary).
- A quantitative cost statement: how many GPU-hours are saved by training the 1B-scale grid to design a 3B model vs. a brute-force search at 3B.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Harsh critic's claim that "per-task breakdown is deferred to an appendix that was stripped from the review copy" → REMOVED.** The parser strips appendices from all papers; they exist in the original submission. Per hard rules, we do not fault the paper for missing appendix content.

2. **Harsh critic's claim that the paper should "re-center the narrative from 'a conditional scaling law' to 'a local empirical model for architecture search'" → REMOVED.** This is a framing preference, not a valid weakness. The paper already discusses the coefficient shift transparently.

3. **Strength Finder's claim that "the conditional scaling law accurately predicts loss for unseen model sizes" as an unqualified strength → QUALIFIED in the main review.** This is true within the tested extrapolation range but the coefficient shift at larger gaps constrains the claim. The paper's own ablation in Figure 8/Table 2 shows this.

4. **Harsh critic's concern about whether baseline LLaMA comparisons use public checkpoints vs. retrained models → KEPT but demoted to Minor.** The paper provides training loss for the LLaMA baselines, which implies retraining. The issue is one of clarity, not fairness.

5. **Harsh critic's demand for confidence intervals and statistical testing → KEPT as Minor.** While standard practice in the subfield omits these, the small loss deltas make the concern worth noting.

## Novel Insights

Beyond the paper's own contributions, the review process surfaces an interesting tension: the paper's strongest empirical finding—the U-shaped dependence of loss on both \(d_{\text{model}}/\sqrt{N}\) and \(r_{\text{mlp/attn}}\) with nearly identical optima across model sizes (Figures 4–5)—suggests the underlying architectural optimality is surprisingly stable. Yet the fitted coefficients of the parametric law that captures these curves shift with scale (Section 5.1). This implies the functional form is correct but the calibration relative to the Chinchilla baseline drifts, perhaps because the baseline \(L_{\text{opt}}\) itself is imperfectly estimated or because architectural effects have a scale-dependent interaction with the Chinchilla terms. Untangling this could be a productive direction for future work.

## Suggestions

- Add a sentence to the caption of Table 1 or to Section 5.1 explicitly stating that the LLaMA-3.2 baseline rows represent models trained by the authors under their own setup using the LLaMA architectural configuration.
- Report the standard deviation of the average accuracy across the nine downstream tasks, or provide per-task results in the main text for the key models in Table 1.
- Clarify the procedure for obtaining \(L_{\text{opt}}(N,D)\) in Section 4: was it the minimum observed loss among all trained variants of that parameter count, or a fitted Chinchilla law?
- Consider adding a brief note in Section 7 (Limitations) about the hyperparameter-sensitivity concern, even if only to acknowledge it as unaddressed.

## Score and Decision

### Calibration anchor comparison

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| ulGwcj1egv | 3.00 | 1 | Unrelated topic (router-selective transformers); much weaker |
| BjZP3fTlVg | 3.00 | 1 | Unrelated topic (risk-controlled deployment); much weaker |
| 2DD4AXOAZ8 | 2.00 | 1 | Unrelated topic (MixAttention); much weaker |
| n7iwmPacDt | 3.00 | 1 | Unrelated topic (speculative decoding); much weaker |
| BDisxnHzRL | 4.25 | 1 | Scaling laws for downstream performance; this paper has broader scope and stronger empirical validation |
| T2h2V7Rx7q | 5.25 | 1 | Multilingual scaling laws; narrower contribution |
| xGM5shdGJD | 5.20 | 1,2 | Meta-analysis of scaling law estimation practices; this paper contributes original models and a novel framework |
| KnoS9XxIlK | 6.00 | 2 | Multi-power law for loss curves; narrower contribution |
| iZeQBqJamf | 6.50 | 1,2 | Over-training scaling laws, 104 models; comparable empirical scope and methodology. This paper is somewhat stronger due to the architecture+inference angle and concrete throughput gains |
| vPOMTkmSiu | 6.60 | 2 | Scaling laws for MT downstream performance; different domain |
| o9YC0B6P2m | 6.75 | 2 | LR annealing scaling law; narrower contribution |
| JCiF03qnmi | 6.80 | 2 | CBS scaling; different topic, similar empirical model-size range |
| i9K2ZWkYIP | 7.00 | 2 | Sparsity scaling laws; most comparable anchor. Both extend Chinchilla with a new dimension, both train many models. This paper has more concrete practical gains (throughput) but a less elegant/unified formulation |
| Tzh6xAJSll | 7.60 | 2 | Associative memories; different topic, more theoretical |
| TJo6aQb7kM | 7.60 | 1 | Ternary language models; different topic |
| wg1PCg3CUP | 8.00 | 1 | Precision-aware scaling laws; clearly stronger—cleaner theoretical formulation, more universal law, 465 runs |
| E4Fk3YuG56 | 8.50 | 1 | Cut cross-entropy; unrelated topic |
| t7P5BUKcYv | 8.00 | 1 | MoE++; unrelated topic |

**Round 1 bracket:** 5.5–7.5. The paper is clearly stronger than the 4.25–5.25 rejected anchors and weaker than the 8.00+ strong anchors.

**Round 2 narrowing:** The paper sits between iZeQBqJamf (6.50, over-training scaling) and i9K2ZWkYIP (7.00, sparsity scaling). It has stronger practical impact than the former and comparable novelty to the latter, but its law is less universal (coefficient shift) and has some minor evidential gaps. Final score: **6.5**.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>