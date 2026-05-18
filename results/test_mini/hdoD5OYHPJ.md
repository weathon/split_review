Now I have all the information needed. Let me construct the final consolidated review.

---

## Summary

This paper proposes AutoCLIP, a method that reweights prompt template contributions per image at zero-shot inference time using a single gradient step on a logsumexp objective, entirely in the embedding space (no extra encoder passes). The method is simple (a few lines of code), unsupervised, and improves accuracy on ~85% of 990 tested configurations across 7 datasets, 6 VLMs, and 3 prompt strategies, with an average gain of 0.45 pp and peak gains of ~3 pp.

## Strengths

- **Clean, well-motivated method with genuine practical advantages.** AutoCLIP performs per-image prompt reweighting via a single closed-form gradient step on logsumexp, entirely in the embedding space without additional forward/backward passes through VLM encoders. This is a concrete practical advantage over test-time prompt tuning methods that require multiple augmentations and backpropagation through text encoders.

- **Unusually extensive evaluation.** The paper tests 990 combinations (7 datasets × 6 VLMs × 3 prompt strategies × multiple K values) with 7 runs each and standard errors reported. The scale and rigor of this evaluation substantially exceed what is typical for this sub-area — compare to the calibration anchors in this space (e.g., CARPRT, BaFTA, BAT-CLIP), which evaluate on fewer settings.

- **Ablations justify key design choices.** The paper compares logsumexp against max, mean, and entropy objectives (Figure for results_tta_losses, confirming logsumexp as best), and ablate β sensitivity (Figure for results_entropy_rate, showing stability over [0.7, 0.9] for most datasets). The weight visualization (Figure for weights) provides compelling qualitative support for the method's intuition.

- **Benefit scales with prompt diversity and size.** The average gain monotonically increases from Δ=0.06 (K=4) to Δ=0.57 (K=200), and is largest for WaffleCLIP (Δ=0.61). This trend is clean empirical evidence that the method leverages prompt set diversity as intended.

- **Controlled synthetic experiment provides useful mechanistic insight.** The simple toy model (varying class-prompt entanglement ρ and instance noise ε) offers a plausible explanation for why AutoCLIP helps more on smaller VLMs and less on larger ones, and why it can slightly hurt on ViT-L-14 + ImageNet-C. While the analysis is simplified, the paper appropriately hedges its conclusions.

## Weaknesses

### Major

- **No empirical comparison to ZPE (Allingham et al., 2023), the most closely related prior work.** The paper correctly notes that ZPE operates in a different setting (batch-level, requiring source-distribution statistics), while AutoCLIP is single-image and source-free. However, these are differences in setting, not incomparability — one could run ZPE in its native setting (batches of test images with pre-computed source features) alongside AutoCLIP on the same datasets and compare accuracy. Without this comparison, the reader cannot assess whether AutoCLIP's more restrictive (but more practical) assumptions come at an accuracy cost or whether it is actually competitive or superior. Since ZPE is the only other method that reweights prompts in embedding space, this omission is a significant evidential gap. CARPRT (a contemporary paper on class-aware prompt reweighting) includes ZPE as a baseline; AutoCLIP should do the same.

### Minor

- **The "essentially without free hyperparameters" claim is overstated.** The paper states that AutoCLIP "comes essentially without free hyperparameters" (line 42), yet it acknowledges that β (the entropy reduction factor) is "the new free hyperparameter" (line 143). The ablation (Figure for results_entropy_rate) shows that β=0.7 beats the default β=0.85 on several datasets (e.g., Oxford Pets and EuroSAT), and the paper itself recommends β=0.7 for future work. This does not invalidate the method — the β=[0.7, 0.9] range is reasonably stable for most datasets — but the claim of being hyperparameter-free should be softened to reflect that one globally-set hyperparameter (β) exists and modestly impacts results on some datasets.

- **Average gains are modest and the paper could frame this more transparently.** The average gain across all 990 settings is 0.45 pp, and EuroSAT actually degrades (Δ=-0.24). The abstract highlights "up to 3 percent point accuracy," which is accurate (max observed is +2.9 pp) but the full distribution is heavily stacked near zero. The paper does report the 85% improvement rate and the average, but providing a histogram of Δ across all 990 settings would give readers a more complete picture of how often the method helps vs. hurts and by how much.

- **The controlled synthetic experiment's conclusions, while hedged, extend beyond what the evidence supports.** The paper uses a simple additive Gaussian noise model (parameter ρ for "entanglement") to explain real VLM behavior (e.g., "for smaller VLMs, the text embeddings are more entangled"). This is a plausible hypothesis, but the paper does not provide any direct measurement of actual class-prompt entanglement in real CLIP models of varying sizes. The hedging language ("possible explanation") is appropriate, but the narrative weight placed on this explanation (it appears in both the controlled setting section and the conclusion of the main experiments) risks over-interpreting a toy model.

### Trivial

- **No runtime numbers provided.** The paper repeatedly claims "minor additional computation overhead" but does not report wall-clock time per image, which would help practitioners weigh the cost-benefit. Given that the method operates entirely in embedding space (no extra encoder passes), the overhead is almost certainly small, but a concrete number would be useful.

- **The default β=0.85 is used in the main experiments, but the ablation later recommends β=0.7.** This creates a minor inconsistency between the reported numbers (β=0.85) and the recommended configuration. The authors should either re-run main experiments with β=0.7 or update the default and recommendation to match.

## Nice-to-Haves

- A histogram showing the distribution of Δ across all 990 configurations (instead of only averages and standard errors).
- An analysis of why EuroSAT systematically hurts (e.g., comparing image embedding variance or average similarity to class descriptors across datasets, to test the "uninformative embeddings" hypothesis).
- A comparison to ZPE under ZPE's native setting (batch + source distribution) to clarify the trade-offs between the two approaches.
- Ablation on the number of gradient iterations (the paper says preliminary experiments showed no benefit beyond one iteration, but this data is not shown).

## Removed Points

- **Strength Finder claim re: "Hyperparameter-free step-size tuning via entropy control"** — The strength is partially valid (the bisection method does automatically determine α given β), but conflicts with the verified weakness that β is a free hyperparameter with tangible impact on results. Moved here because the "hyperparameter-free" framing is inaccurate.
- **Strength Finder claim: "Consistent accuracy improvement across diverse settings"** — Verified as correct from the paper; kept in strengths above.
- **Harsh Critic's concern about "up to 3 percent point" rounding** — The largest gain in Table 1 is +2.9 pp, which is appropriately rounded. Not a real issue.
- **Harsh Critic's claim about the synthetic experiment being "speculative" at a Fatal level** — The paper uses appropriate hedging language ("possible explanation," "likely corresponds"), so this is a minor weakness, not fatal.
- **Human-finder's (Harsh Critic) demand for "histogram of Δ across 990 settings"** — Kept as nice-to-have, not a core weakness.

## Novel Insights

None beyond the paper's own contributions. The review surfaces no insight that was not already present in the paper's own framing and results.

## Suggestions

1. Add an empirical comparison to ZPE (Allingham et al., 2023) on a representative subset of datasets and models. Even if the settings differ (batch vs. single-image, source vs. source-free), running ZPE in its native configuration alongside AutoCLIP would clarify the practical trade-offs.
2. Soften the "essentially without free hyperparameters" claim to something like "with a single, globally-shared hyperparameter β that is stable over [0.7, 0.9] for most datasets." Alternatively, update the default to β=0.7 based on the ablation evidence.
3. Add a histogram of Δ accuracy across all 990 settings to help readers assess the full distribution of gains and losses.
4. Provide a brief runtime measurement (e.g., milliseconds per image added by AutoCLIP) to substantiate the "minor overhead" claim.
5. Either move the EuroSAT drop from discussion to a more prominent limitation, or provide additional analysis to explain why it occurs.

---

## Score and Decision

**Calibration Anchors** (all from the human-reviewed corpus):

| Anchor | Path | Avg Score | Comparison to Paper |
|--------|------|-----------|---------------------|
| CARPRT | fRpAUgKJhT.md | 5.75 | Similar topic (prompt reweighting for CLIP); CARPRT compares to ZPE but has more limited experiments. AutoCLIP has cleaner method and more thorough eval but lacks ZPE comparison. Slightly weaker than CARPRT due to this gap. |
| BaFTA | KNtcoAM5Gy.md | 5.50 | Both are lightweight test-time methods for CLIP. BaFTA uses online clustering; AutoCLIP uses gradient on logsumexp. Comparable quality and depth. |
| BAT-CLIP | z7PhIgVmZU.md | 5.50 | More complex (bimodal TTA with multiple losses). AutoCLIP is simpler and has fewer methodological concerns. Slightly stronger. |
| InCPL | Rc3RP9OoEJ.md | 5.00 | InCPL uses labeled in-context examples (information leakage concern). AutoCLIP is fully unsupervised and cleaner. Stronger. |
| DefNTaxS | B2ChNpcEzZ.md | 4.00 | Prompt augmentation via taxonomies. AutoCLIP has more rigorous evaluation and cleaner method. Stronger. |
| Active TTP | pdzHpQbGrn.md | 2.50 | Poorly motivated with marginal improvements. AutoCLIP is much stronger. |

AutoCLIP's position relative to these anchors: it is comparable to or slightly better than the 5.5-level papers (BaFTA, BAT-CLIP) on method cleanliness and experimental thoroughness, but the missing ZPE comparison is a real gap that papers in this band typically fill. It is clearly stronger than the 4-5 band papers. It is not at the 6+ level, as the average gains are modest and the method is an incremental (albeit clean and practical) contribution.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>