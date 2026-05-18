Now I have a thorough understanding of the paper and all reviews. Let me produce the final consolidated review.

---

## Summary

This paper introduces ADAPT, a deep continuous prompting method for vision-language models (CLIP) that allows context lengths of soft prompts to vary across layers and between the image/text branches automatically. The key mechanism is iterative pruning of context tokens using saliency criteria (Snip, gradient norm, L2 norm) to remove unimportant tokens until a target total context length is reached. Experiments on 11 datasets show an average accuracy improvement from 79.83% to 81.70% over the best baseline, with near-lossless compression (77% parameter reduction for only 0.61% accuracy drop).

## Strengths

1. **Novel and well-motivated idea.** Heterogeneous context lengths via iterative pruning of soft prompts is a genuinely new contribution. The paper correctly identifies that fixed context lengths across all layers are suboptimal when different layers have different adaptation needs, and the pruning approach provides a principled way to allocate tokens where they matter. The paper states it is the first to prune prompts for heterogeneous context lengths, which appears accurate.

2. **Strong empirical results across diverse benchmarks.** ADAPT (τ_target=128) improves average accuracy from 79.83% to 81.70% over 11 datasets (Section 4.2), with substantial gains on challenging datasets such as EuroSAT (+6.13%) and Aircraft (+9.63%). When τ_target is selected per-dataset, average accuracy reaches 82.67%. These gains are achieved with the second-lowest GFLOPs among prompting methods and <0.1% of ViT-Base parameters.

3. **Pruning-based compression is near-lossless.** The ablation (Table 2) demonstrates that reducing τ_target from 128 to 32 reduces trainable parameters by 77.16% while only dropping accuracy by 0.61%. This is a practically valuable finding — the saliency-based pruning successfully identifies redundant tokens without meaningful performance degradation.

4. **Visualization confirms genuine heterogeneity.** Figure 3 shows the learned binary masks for EuroSAT, revealing that context lengths indeed vary substantially across layers and between image/text branches, validating that the method produces the claimed heterogeneous structure rather than a trivial uniform one.

5. **Robustness to scoring criterion choice.** Table 3 compares Snip, gradient norm, and L2 norm as importance scores and finds near-identical performance. This robustness is a practical strength, easing deployment.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between motivating theory and pruning criterion.** The paper's central narrative (Section 1, Section 5) argues that different layers deviate differently from optimal weights depending on distribution shift type, and that context lengths should be allocated accordingly. However, the pruning criterion — saliency scores (Snip, gradient norm, L2 norm) — measures a token's contribution to the loss, not a layer's "deviation from optimality." The paper does not validate that layers receiving longer context are indeed those whose weights are farther from optimal, nor does it analyze learned mask patterns on datasets with known shift types (e.g., input-level shift vs. output-level shift). The observed gains could stem from conventional pruning regularization (removing redundant tokens) rather than from principled per-layer allocation. This gap does not invalidate the empirical results, but it leaves the paper's interpretative claim unsupported. Adding the analysis suggested by the reviewer (correlating mask patterns with shift types from Lee et al., 2022) would substantially strengthen the paper.

### Minor

2. **Experimental details underspecified in visible text.** The paper states it evaluates under the "few-shot learning setting" (Section 4.2) but the visible text does not specify the number of shots used in the main experiment (line 164 mentions 1-shot/4-shot and 16-shot regimes in passing, but the main setup is unclear). The experimental setup section (Section 4.1) appears to have been lost to the parser, but this information should be stated explicitly in the results section as well, since it is critical to interpreting the results. No standard deviations or confidence intervals are reported for any result, making it impossible to assess the significance of the reported gains. The claim "79.83% to 81.70%" identifies that ADAPT surpasses the best baseline (implied by context on lines 27 and 118), but the paper would benefit from stating explicitly which baseline this corresponds to.

3. **Algorithm specification has gaps.** While the method's mechanism is conceptually clear, the visible text does not report key hyperparameter values used in experiments: the accumulation period n_k, pruning rate r_p, and total training epochs are mentioned (line 111) but their specific values are absent. These details were likely in the missing Section 4.1, but a reader looking only at the method description cannot reproduce the exact procedure without making assumptions.

4. **"Non-parametric" claim is slightly overstated (line 23).** The method involves hyperparameters (τ_target, n_k, r_p, warmup epochs) that control the pruning process, and τ_target in particular strongly affects results (Table 2). Calling the context length determination "non-parametric" is imprecise — the method is *automatic* (no manual per-layer assignment) but not non-parametric.

### Trivial

5. **No discussion of monotonic pruning.** The masks only decrease (tokens are never added back). This design choice is reasonable but unremarked. A sentence explaining why regrowth is unnecessary would be helpful.

6. **"Time-dependent" binary mask overstates what is a straightforward iterative removal process.** The mask's time dependence is simply that it changes at pruning steps; it is not a learned or scheduled function of time.

## Nice-to-Haves

- **Comparison with manually-assigned heterogeneous context lengths.** The paper compares against methods with fixed context lengths per layer. Adding a baseline where context lengths are manually assigned (e.g., all tokens in early layers, fewer in later layers, or a linear decay schedule) would directly test whether the automatic pruning is better than any sensible hand-crafted assignment. This would strengthen the demonstration that the automatic allocation is the source of the gains.

- **Analysis of mask patterns by shift type.** As noted in the Major weakness, correlating the learned masks with distribution shift categories (input-level, feature-level, output-level shifts from Lee et al., 2022) would validate the motivating narrative. If masks align with expectations (e.g., early layers retain more tokens for input-level shifts), the central claim would be convincingly supported.

- **Computational cost of the pruning process itself.** The paper reports inference FLOPs but not the training-time cost of computing importance scores over accumulated steps. A brief accounting would be appropriate.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Criticism that Table 1 / Figure 1 are absent from extracted text.** These are parser artifacts — the paper clearly references them and they exist in the original submission. Removed per hard rules on parser artifacts.

- **Criticism that the algorithm is "referenced but not present."** Algorithm 1 is part of the original paper; the parser stripped it. Removed per hard rules.

- **Criticism that the paper "never identifies what the baseline average corresponds to."** The visible text states "Adapt surpasses state-of-the-art methods" and presents 79.83% as the baseline against which ADAPT's 81.70% is compared. From context, this is the best prior method's average. While it could be clearer, the claim is not unidentifiable. Downgraded — it is not factually wrong and is partly addressed by context.

- **Criticism about "the few-shot regime is mentioned but the number of shots (1, 4, 16?) is never stated."** Line 164 references these shot counts; the experimental setup (Section 4.1, lost to parser) likely specified this explicitly. Kept in Minor but with acknowledgment that the setup section is missing.

- **Claim that "the paper does not present the crucial numbers in prose" about Table 1.** The paper does present the key numbers in prose: 81.70% average, 79.83% baseline, 6.13% on EuroSAT, 9.63% on Aircraft. Removed as factually incorrect — the paper does report these numbers.

- **Criticism that comparison with manually assigned context lengths is missing.** Moved to Nice-to-Haves; it is a reasonable suggestion but not a required baseline.

- **Strength Finder's claim about "Clear connection to surgical fine-tuning motivation."** This conflicts with the verified Major weakness (the connection is asserted but not demonstrated via analysis). Per the rule "when a strength and weakness disagree, the weakness wins," this strength is dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews surface two key tensions: (1) the paper's motivating narrative (deviation from optimal weights) is not empirically validated by the pruning patterns, and (2) the method's effectiveness is empirically demonstrated but its interpretability claim remains speculative. These are genuinely insightful concerns that the authors should address, but neither invalidates the practical contribution.

## Suggestions

1. **Validate the motivating narrative directly.** For datasets categorized by distribution shift type (Lee et al., 2022), analyze whether the learned binary masks align with expectations: early layers should retain more tokens for input-level shifts, later layers for output-level shifts. This would turn the plausible-but-unverified story into a demonstrated property of the method.

2. **Report standard deviations and the exact experimental protocol (number of shots, seeds, splits) prominently.** Even with a lost Section 4.1, the results section should state the shot count explicitly and include variance information.

3. **Report the hyperparameter values used for n_k and r_p.** A brief sentence or a note in Table 1/Table 2 would suffice for reproducibility.

4. **Add a baseline with manually assigned heterogeneous context lengths** (e.g., linear decay of context length from early to late layers) to directly demonstrate the advantage of automatic allocation over any sensible fixed schedule.

5. **Explicitly identify which baseline achieves the 79.83% average** (e.g., "the best prior method, MaPLe, achieves 79.83%") rather than leaving it implicit.

6. **Tone down the "non-parametric" claim** — replace with "automatically determined" or "without per-layer manual design," which are both accurate and no less impressive.

## Score and Decision

The paper presents a genuinely novel and empirically effective method for heterogeneous prompt tuning. The core weakness — the gap between the motivation and the pruning criterion — is a genuine limitation but does not undermine the empirical contribution: the method works well regardless of whether its interpretative story is fully validated. The missing experimental details and under-specification are addressable. This is a solid paper with a clear contribution.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>