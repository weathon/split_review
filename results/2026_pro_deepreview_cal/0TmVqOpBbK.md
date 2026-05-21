Now I have a thorough understanding of both the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

This paper introduces a conditional scaling law that extends Chinchilla by incorporating architectural factors—hidden size and mlp-to-attention ratio—to predict training loss for architectural variants. The authors train over 200 models (80M–3B parameters) to fit the law and propose a search framework that jointly optimizes inference throughput and accuracy. The resulting architectures (Surefire-1B, Surefire-3B) achieve up to 42% higher inference throughput than LLaMA-3.2 configurations while maintaining or improving downstream accuracy under matched training budgets.

## Strengths

- **Well-documented empirical regularities:** The U-shaped relationships between loss and both $d_{\text{model}}/\sqrt{N}$ (Figure 4) and $r_{\text{mlp/attn}}$ (Figure 5) are consistent across 80M, 145M, and 297M model scales, supported by training over 200 models. These are genuinely informative empirical findings about architectural trade-offs.

- **Practical architecture improvements validated at scale:** The search framework (Algorithm 1) produces Surefire-1B and Surefire-3B models that deliver up to 42% higher inference throughput than LLaMA-3.2 configurations while matching or exceeding accuracy on nine downstream tasks (Table 1, Figure 7). The gains persist across vLLM and SGLang on both A100 and H200 GPUs (Appendix F/G), confirming the throughput improvements are not artifacts of a particular serving stack.

- **Actionable fitting-strategy insight:** Figure 8 and Table 2 demonstrate that fitting the conditional scaling law using models within a closer size range (1B → 3B) yields significantly better predictions than extrapolating from much smaller models (Spearman 1.0 vs. 0.5). The practical guideline—fit on models roughly one-third the target scale—is a concrete takeaway for practitioners.

- **Robustness of simple calibration:** The multiplicative and additive calibration schemes achieve comparable predictive performance, and more complex joint (non-separable) formulations do not improve results (Appendix J). This is a useful negative result that justifies the parsimonious separable formulation.

- **Thorough ablation of outliers:** The paper explicitly tests and documents that extreme mlp-to-attention ratios (below 0.5 or above 5) degrade scaling law fit quality, providing practical bounds on the law's applicability.

## Weaknesses

### Fatal

None.

### Major

- **Calibration coefficients assumed D-invariant but never tested:** The calibration factors $a_i, b_i$ in Eq. (3) are described as "shared across all $N, D$" (line 165). Yet every experiment uses a fixed token-to-parameter ratio $D = 100 N_{\text{non-emb}}$ ($5\times$ Chinchilla optimal). The paper provides no evidence that the same U-shaped relationships and calibration coefficients hold when $D$ is varied independently of $N$. The paper's stated scope is architecture optimization under fixed parameter and token budgets (line 86: "we study how to design an architecture that satisfies both efficiency and accuracy requirements"), so this does not invalidate the core contribution. However, it means the law cannot be used to make predictions when the training budget changes—a significant limitation on the claimed extension of Chinchilla's framework, which is fundamentally about predicting performance across varying $(N, D)$.

- **Extrapolation across large scale gaps is unreliable:** When the law is fitted on 80M–1B models and evaluated at 3B, Spearman correlation drops to 0.5 (Figure 8 left), indicating the architectural optimum shifts with scale in ways the shared-coefficient model does not capture. The paper is transparent about this and provides the practical workaround of fitting on models ~1/3 of the target scale (Table 2, Panda-3B$^\circ$). However, this substantially undercuts the cost-saving motivation of scaling laws: if one must train 1B models to predict 3B behavior, the savings relative to just searching at 3B are modest. The paper would benefit from analyzing *why* the coefficients shift and whether a scale-dependent parameterization could recover predictive power across wider gaps.

### Minor

- **LLaMA baseline training conditions are implicit:** Table 1 reports loss and accuracy for "LLaMA-3.2-1B" and "LLaMA-3.2-3B" alongside the authors' Panda and Surefire models. The paper states it trains "LLaMA-3.2-style" transformers (line 195) and that Panda-1B outperforms "the open-weight LLaMA-3.2-1B baseline configs" (line 273). The loss values (2.803 for LLaMA-3.2-1B vs. 2.782 for Panda-1B) strongly imply both were trained under identical 100B-token budgets. However, the paper never explicitly confirms that the LLaMA entries in Table 1 were retrained by the authors under the same conditions rather than being the public models. This should be stated unambiguously.

- **GQA search procedure is underspecified:** Algorithm 1 describes a local search over GQA values with early stopping, but the number of candidates evaluated and the specific early-stopping criterion are not detailed. Given that GQA significantly impacts throughput (Figure 11, Appendix F) and the final models use GQA values of 7 and 9, the reproducibility of this step matters.

### Trivial

None significant enough to list.

## Nice-to-Haves

- **Vary the token budget to test D-invariance:** Even a small experiment—e.g., training a handful of 145M architectures at $D=50 N_{\text{non-emb}}$ and $D=200 N_{\text{non-emb}}$ to check whether predicted loss orderings hold—would substantially strengthen the claim that calibration coefficients are D-independent.

- **Cost-benefit analysis of the law-fitting procedure:** Training 200+ models is non-trivial. A rough break-even calculation—at what target model scale does the compute spent on the sweep get paid back by improved architecture?—would help practitioners decide when to apply this method.

- **Analyze why coefficients shift with scale:** Rather than only noting that refitting on closer-scale models helps, exploring whether the coefficients themselves follow a systematic trend with $N$ could turn an observed weakness into a more principled extension.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Harsh Critic Point: "Cost analysis of law-fitting procedure is missing"** — REMOVED. Moved to Nice-to-Haves. The paper's contribution is demonstrating the method works; cost analysis is beneficial but not required for validating the core claim.

- **Harsh Critic Point: "Hyperparameter sensitivity across architectures"** — REMOVED. The paper follows standard practice of using fixed hyperparameters from prior work. Tuning hyperparameters individually for 200+ architectures would be computationally prohibitive and is not standard in scaling law studies.

- **Harsh Critic framing of D-dependence as "structural gap" that "severely limits" the contribution** — DEMOTED from fatal to Major. The paper explicitly scopes itself to architecture optimization under fixed (N,D) budgets (line 86). The D-invariance claim is an overstatement, but it does not undermine the demonstrated practical results.

- **Strength Finder: Generic strengths about problem importance** — REMOVED. Statements like "the problem is important" are not concrete strengths specific to this paper.

## Novel Insights

The paper's finding that scaling-law-based architecture predictions degrade when extrapolating across wide parameter-count gaps—and that refitting on models ~1/3 the target scale recovers strong predictions—is an honest and useful observation rarely surfaced so clearly in scaling-law papers. Most works present their best-case extrapolation; this paper's willingness to document where predictions break down and to quantify the "closer is better" principle (Figure 8, Table 2) is methodologically valuable for the field.

## Suggestions

- Explicitly state in the Table 1 caption or surrounding text that all models including the LLaMA baselines were trained by the authors under identical data, token budget, and hyperparameter conditions. This resolves the ambiguity for readers who might otherwise question the comparison.
- Consider reframing the conditional scaling law's scope more precisely: rather than claiming coefficients are "shared across all $N, D$," state that they are validated for the $D = 100 N_{\text{non-emb}}$ regime and that D-invariance is an assumption requiring future validation. This would strengthen the paper's credibility without weakening its contribution.
- Include a brief quantitative analysis of the coefficient shift between the 80M-1B fit and the 1B-only fit (the two sets of $(a_i, b_i)$ values are already reported in Sections 5.1 and the ablation). Characterizing whether the drift follows a systematic trend would be more insightful than merely noting it exists.

## Score and Decision

**Calibration anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|---|---|---|---|
| `ulGwcj1egv` (FiRST) | 3.00 | R1 | Significantly weaker — narrow latency contribution, limited scale |
| `2DD4AXOAZ8` (MixAttention) | 2.00 | R1 | Much weaker — small-scale, limited validation |
| `KQALhPTAfj` (Navigating Scaling Laws) | 3.75 | R1 | Weaker — less empirical depth, narrower contribution |
| `iIGNrDwDuP` (Scaling Laws for Diffusion Transformers) | 5.25 | R1 | Weaker — establishes existence of scaling laws, less practical impact |
| `6VhDQP7WGX` (Inference Optimal VLMs) | 5.80 | R1 | Comparable — scaling law for trade-off, practical method, mixed generalization |
| `iOy2pITOoH` (Spark Transformer) | 5.50 | R1 | Weaker — architectural modification without scaling-law framework |
| `wg1PCg3CUP` (Scaling Laws for Precision) | 8.00 | R1 | Clearly stronger — clean unified framework, 465 runs, strong validation |
| `xGM5shdGJD` (Hitchhiker's Guide) | 5.20 | R2 | Weaker — meta-analysis without new scaling law, limited novelty |
| `T2h2V7Rx7q` (Multilingual Scaling Laws) | 5.25 | R2 | Weaker — narrower contribution |
| `iZeQBqJamf` (Over-training Scaling) | 6.50 | R2 | Slightly stronger — cleaner extension of Chinchilla, addressing two clear gaps, 300× compute reduction |
| `FxNNiUgtfa` (Knowledge Capacity) | 7.25 | R2 | Stronger — novel information-theoretic framing, multiple novel results |

**Round 1 bracket:** 5.0–6.5. The paper has stronger empirical grounding than the 3–4 range anchors and a more novel contribution than the meta-analysis anchors (~5.2). It does not reach the clarity and theoretical unity of the 8.0 anchor.

**Round 2 narrowing:** The paper is comparable to "Inference Optimal VLMs" (5.80) — both establish scaling laws for a specific trade-off (architecture/inference vs. visual tokens/LLM size), both propose practical methods, and both have acknowledged generalization limitations. It falls below "Language models scale reliably with over-training" (6.50), which has a cleaner extension of Chinchilla with demonstrable 300× compute reduction for prediction. Our paper's strengths (200+ models trained, thorough ablations, practical throughput gains) are offset by the untested D-invariance of calibration coefficients and the extrapolation degradation at 3B.

**Final score: 6.0.** This is a solid empirical contribution with genuine practical value, but the scaling law's generality is not fully established, and the extrapolation limitations meaningfully constrain the cost-saving promise.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>