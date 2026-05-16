Now I have all the information needed. Let me compose the final consolidated review.

## Summary

This paper presents the first scaling law for masked diffusion models (MDMs) on text, showing that MDMs exhibit a scaling rate comparable to autoregressive models (ARMs) with a ~16× compute gap (smaller than the 64× gap reported for continuous diffusion models). It proposes unsupervised classifier-free guidance (CFG) that exploits unpaired pre-training data and shows that a 1.1B MDM is competitive with larger ARMs on zero-shot benchmarks and conditional generation, while also claiming advantages on the reverse curse and temporal degradation.

## Strengths

- **First scaling law for MDMs with comparable scaling rate to ARMs (Sec. 3, Fig. 1-3).** The IsoFLOP analysis across compute budgets 6×10¹⁸ to 10²⁰ FLOPs fits a power-law and reveals that MDM loss decreases at a rate similar to ARMs. This fills an important gap in understanding MDM scalability. The finding that optimal MDM model size is ~half that of ARMs is a nontrivial architectural insight.

- **Unsupervised classifier-free guidance that outperforms standard CFG without paired data (Sec. 4, Eq. 6-8, Table 1).** The formulation leveraging the joint distribution learned during pre-training is clever and well-motivated by the MDM's unique conditional distribution property (Eq. 2). Unsupervised CFG improves MDM performance across all 8 zero-shot benchmarks (e.g., OpenBookQA from 27.00 to 34.20) and surpasses standard CFG on MT-Bench (1.60 vs. 1.53).

- **Competitive zero-shot language understanding (Table 3).** The 1.1B MDM outperforms the larger 1.5B GPT-2 on 4/8 benchmarks (BoolQ, OpenBookQA, RACE, LAMBADA), demonstrating that MDMs are not just perplexity curiosities but can deliver on standard evaluation tasks.

- **Flexible quality-efficiency trade-off in conditional generation (Table 6).** MDM matches ARM quality (score 1.57 vs. 1.56) while being 1.4× faster (396s vs. 555s) using default sampling, and can exceed ARM quality (1.60) at higher compute — all compared against an ARM with KV-cache optimization.

## Weaknesses

### Major

- **Reverse curse claim lacks a controlled comparison (Sec. 7.1, Table 5).** The paper fine-tunes the 1.1B MDM on fictitious statements and compares its reverse-direction accuracy to GPT-3 (175B) and Llama-2 (13B) using results cited from Berglund et al. and Lv et al. However, those earlier works evaluated GPT-3 and Llama-2 zero-shot (or on real factual knowledge from pre-training), *not* after comparable fine-tuning on the same fictitious dataset. The MDM is explicitly fine-tuned on the target bidirectional relationships, which could teach the task format itself. A properly controlled comparison would fine-tune a same-sized ARM on the identical fictitious data and evaluate both under the same protocol. Without this control, the "breaking the reverse curse" headline overclaims what the evidence supports. The 92% vs. 0% gap likely reflects a mix of architectural advantage and differential training, not architecture alone. This weakness conflicts with Strength Finder claim #3, which is therefore downgraded.

- **Temporal degradation experiment confounds architecture with training compute (Sec. 7.2, Table 7).** The paper acknowledges that the MDM (220M) required 16× more compute to reach a similar validation loss on SlimPajama (line 367: "MDMs require 16 times more computation to reach this performance level"). This means the MDM saw more tokens, more epochs, or both. The better generalization to FineWeb 2024 data (perplexity ~24 vs. ~27) could simply reflect more extensive training rather than inherent robustness from bidirectionality. Controlling for total training FLOPs or matching the ARM after extended training is essential before attributing the advantage to architecture. This weakness conflicts with Strength Finder supporting strength #2, which is therefore downgraded.

- **Zero-shot accuracy cherry-picked between two likelihood evaluation methods (Sec. 5).** The paper states that for each task, the method (chain rule or Monte Carlo) that gives *higher accuracy* is used (line 195: "the chain rule for likelihood evaluation results in higher accuracy for OpenBookQA and PIQA, while Monte Carlo estimation yields better accuracy for ARC-Easy, Hellaswag, RACE, and SIQA"). This is a form of test-set selection that inflates reported results. A principled approach would either pre-specify a single method or cross-validate the choice. The current practice undermines the fairness of the ARM comparison in Tables 1–3.

### Minor

- **No statistical confidence/error bars on any experimental result.** Throughout the paper (Tables 1–7), no standard deviations, confidence intervals, or multiple-seed results are reported. Many accuracy differences are small (e.g., 1–2 percentage points on PIQA, SIQA, BoolQ), and the MT-Bench scores vary over a narrow range (1.32–1.60). Without variance estimates, it is unclear which differences are meaningful. This is especially relevant given the claim that MDMs "consistently surpass ARMs across all tasks" when scaled.

- **The MDM loss is an upper bound on negative log-likelihood, not exact NLL (Eq. 3).** The paper acknowledges this (line 87: "upper bound on negative log-likelihood") but then uses this loss as the y-axis metric in the scaling law and directly compares its absolute value to ARM loss (which is exact NLL). The 16× compute gap is based on "comparable validation losses" between two different loss quantities. Whether the bound is tight enough to preserve the exact gap and exponent is not validated. This does not invalidate the scaling law (the within-family trend is sound), but the *absolute* gap figure should be treated as approximate.

- **Unsupervised CFG gains on several tasks are very small.** In Table 1, gains on PIQA (60.34→60.39, +0.05 points), BoolQ (61.50→62.17, +0.67), and SIQA (36.95→37.41, +0.46) are within noise range. Without significance tests or multiple seeds, the claim that unsupervised CFG "significantly improves" on *all* tasks is overstated for the smaller-margin cases.

- **IsoFLOP analysis uses C = 6ND (Sec. 3).** This formula is standard for ARM training FLOPs but may not perfectly capture MDM training compute (e.g., the integral over timesteps in Eq. 3 involves sampling-based estimation). Since the same formula is applied to both model families, the relative comparison of scaling rates is likely robust, but the absolute compute estimates for MDMs could have systematic error. A brief discussion of this limitation would improve the paper.

### Trivial

- Table 2 (line 236) has a formatting artifact where the FLOPs value for MDM is cut off ("$1.61 \times 10^{21}$" vs. the ARM entries).
- Line 39: "scaling computate budgets" appears to be a residual editing issue.

## Nice-to-Haves

- **Controlled reverse-curse experiment.** Fine-tuning a same-sized ARM on the same fictitious dataset and comparing both models identically would either validate or bound the claimed architectural advantage. If infeasible for GPT-3 scale, at minimum the paper should explicitly state the evaluation protocols for all compared models and discuss the confound.

- **Compute-controlled temporal degradation experiment.** Training an ARM for the same total FLOPs as the MDM (i.e., matching compute rather than loss) would isolate whether the robustness stems from bidirectionality or from more extensive training.

- **Validation of the MDM loss bound tightness.** Estimating the exact NLL (or a tighter lower bound) for a few model sizes would confirm whether the scaling exponent and the 16× gap remain stable when using comparable metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Strength: "MDM (1.1B) breaks the reverse curse that defeats GPT-3 (175B) and Llama-2 (13B)"** — Removed because it conflicts with the verified major weakness: the comparison does not control for fine-tuning vs. zero-shot evaluation protocols.

- **Strength: "MDM exhibits better robustness to temporal data shifts than ARM"** — Removed because it conflicts with the verified major weakness: the comparison confounds architecture with 16× more training compute.

- **Criticism: "The scaling law comparison is based on non-equivalent loss functions (MDM loss is upper bound, ARM loss is exact NLL)"** was downgraded from a structural/fatal issue to a minor concern after verifying that (a) the paper explicitly acknowledges the loss is an upper bound, (b) the scaling law primarily compares *rates* (exponents) which are within-family and remain valid even if absolute values differ, and (c) only the absolute gap (16×) is approximate — a limitation the paper acknowledges. The original framing as a "structural issue affecting all experiments" overstates the impact.

- **Criticism about the IsoFLOP formula (C=6ND) potentially overstating MDM compute** was downgraded to minor because the formula is applied symmetrically to both families; the relative comparison of scaling rates is unaffected. The reviewer's suggestion that the timestep integral changes FLOPs overlooks the fact that this integral is estimated via sampling with negligible overhead relative to total training.

- **Criticism about missing confidence intervals** was downgraded from "lack of statistical rigor" to minor. While real, this is the norm for large-scale LM benchmarks where single-run evaluation is standard, and requesting full multi-seed budgets across all experiments would be impractical.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **For the reverse curse:** Add a controlled experiment fine-tuning Llama-2 (13B) on the same fictitious dataset, or at minimum acknowledge the protocol mismatch explicitly and qualify the claim.
2. **For temporal degradation:** Train an ARM to the same loss with matched total FLOPs (not just matched loss at 16× less compute), or discuss why the compute confound does not explain the result.
3. **For zero-shot evaluation:** Pre-specify one likelihood method (preferably the chain rule, which yields exact NLL) and use it uniformly across all tasks, or present both results and justify the choice via held-out validation rather than test-set performance.
4. **Add confidence intervals / multiple seeds** for at least the smaller-scale experiments (unsupervised CFG ablation, temporal degradation) where the effects are modest.
5. **Clarify the Berglund et al. evaluation protocol** for GPT-3 to make the comparison transparent.

## Score and Decision

The paper makes genuine contributions — the first scaling law for MDMs is timely and useful, and the unsupervised CFG formulation is elegant. The scaling law and zero-shot/conditional generation experiments are solid and support the paper's core thesis that MDMs are a viable alternative to ARMs.

However, the two headline claims about "breaking the reverse curse" and "relieving temporal degradation" — which appear in the abstract, introduction, and conclusion as major selling points — are not supported by the experimental evidence as presented. The reverse-curse comparison mixes different evaluation protocols (fine-tuned vs. zero-shot), and the temporal-degradation experiment confounds architecture with training compute. These are not minor presentation issues; they are claims the paper centers as key advantages of MDMs over ARMs.

If the paper dropped or substantially qualified these two claims, the remaining contributions (scaling law, unsupervised CFG, competitive zero-shot/gen performance) would stand as a solid paper. But in its current form, the gap between the strong claims and the evidence is too wide.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>