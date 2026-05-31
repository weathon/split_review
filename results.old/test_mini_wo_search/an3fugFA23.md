Now I have all the information I need. Let me produce the final consolidated review.

## Summary

The paper proposes Probability Distribution Estimation (PDE), a technique that estimates full token-level probability distributions from the partial top-K probabilities returned by proprietary LLM APIs (e.g., GPT-4, Claude-3, Gemini-1.5). This enables white-box detection methods (Entropy, Rank, LogRank, Fast-DetectGPT) — which previously required full distribution access — to work with proprietary models. The paper shows strong empirical results: Fast-DetectGPT with GPT-3.5 and PDE achieves ~0.95 average AUROC across five source models, outperforming its open-source Neo-2.7B counterpart by 51% relative to remaining space, while being 4.1× faster and 10× cheaper than the black-box DNA-GPT.

## Strengths

- **PDE enables a concrete, practical capability**: The paper demonstrates that Fast-DetectGPT, Rank, and LogRank — methods previously limited to open-source surrogate models — can be applied to proprietary LLMs through PDE. Table 2 shows that Fast-Detect (GPT-3.5) with PDE consistently outperforms Fast-Detect (Neo-2.7) across all five source models tested (GPT-4, Claude-3 Sonnet, Claude-3 Opus, Gemini-1.5 Pro, ChatGPT). This is documented in Section 3.3 (lines 218-221).

- **PDE is shown to be necessary for good performance via ablation**: Section 3.4 (line 228) shows that replacing PDE with a naive approach (assigning zero probability to ranks beyond K) drops Fast-DetectGPT (GPT-3.5) AUROC from 0.9630 to 0.9311, confirming that the estimation algorithm contributes meaningful signal beyond just the top-K probabilities.

- **Substantial efficiency gains over black-box alternatives**: Section 3.3 (line 212) reports PDE takes 462 seconds vs. DNA-GPT's 1911 seconds (4.1× faster), and costs ~10× less since PDE only echoes input probabilities rather than generating multiple completions.

- **Universality demonstrated across multiple detection methods**: Section 2.4 and Table 2 show PDE works with Entropy, Rank, LogRank, and Fast-DetectGPT, not just a single method.

- **Robustness validated across languages and low false-alarm regimes**: Table 3 shows PDE-based Fast-DetectGPT consistently outperforms baselines across six languages; Figure 6 shows strong true-positive rates at 1% and 10% false-positive rates (Section 3.5, lines 250-251).

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Zipfian parameter selection is underspecified in the main text.** The paper states (line 100): "To solve the two parameters, we introduce an additional loss function to minimize their deviations from typical values." What constitutes "typical values" is never defined, and the loss function is not described. While details may reside in the appendix (which the parser strips), the main-text description is too vague for readers to understand or reproduce the Zipfian estimation algorithm. This weakens a secondary PDE variant.

- **"First to enable white-box methods to proprietary LLMs" is slightly overstated.** The paper claims (lines 4, 278) to be the first to enable white-box methods on proprietary LLMs. However, the token *Likelihood* (which the paper itself uses as a baseline, e.g., "Likelihood (GPT-3.5)") is a white-box metric directly available from API logprobs — no estimation needed. The genuine novelty is enabling *methods that require the full predictive distribution* (Fast-DetectGPT's curvature calculation, Entropy, Rank, LogRank), not all white-box methods. The claim should be scoped to this subset.

- **No uncertainty quantification for main AUROC results.** The paper reports (line 127) that each experiment is run three times with the median reported, but no standard deviations, confidence intervals, or significance tests accompany the point estimates in Table 2. With N=150 per dataset, AUROC estimates have non-trivial variance. Per-dataset patterns (e.g., "Geometric performs best on Writing, Zipfian on XSum" from Figure 4) could be within noise. This weakens the strength of dataset-specific conclusions, though it does not threaten the paper's main comparative claims.

- **MLP training data is not described.** The paper states the MLP is "trained over data to model the correlation" (line 19) but does not specify: (a) what distribution data it was trained on (open-source model distributions? synthetic data?), (b) whether it generalizes across model families, or (c) whether it was trained on the same proprietary models it is later evaluated on. The paper releases code, so this is addressable, but as presented the MLP results (which are secondary to the Geometric/Zipfian results) cannot be properly interpreted.

### Trivial

- **"GPT-3.2" appears as a scoring model name** on line 133 and line 241. This is almost certainly a typo for GPT-3.5 (which is used throughout the paper as a scoring model).

## Nice-to-Haves
- Adding bootstrapped confidence intervals or error bars to the main AUROC tables would strengthen dataset-level conclusions, especially for the ablation patterns in Figure 4.
- A cleaner decomposition of the improvement from (a) PDE's distribution estimation vs. (b) simply using a larger/more capable scoring model would sharpen the contribution attribution. The paper partially addresses this by comparing Babbage (1.3B) vs. Neo-2.7 (2.7B) in Table 2.
- The paper could explicitly note which white-box methods are newly enabled (Fast-DetectGPT, Entropy, Rank, LogRank) vs. already usable through API (Likelihood) to avoid overclaiming.

## Removed Points
- **"51% relative improvement metric is ambiguous"**: The critic questions the 51% number, but the calculation depends on table values that are embedded in a parsed image and cannot be independently verified. The paper consistently reports this metric and defines "relative to the remaining space of the baseline."
- **"GPTZero listed but never compared"**: Table 2 is a parsed image; whether GPTZero appears in it cannot be verified from the extracted text. Removed as unverifiable.
- **"DetectGPT comparison missing"**: The paper explicitly justifies skipping DetectGPT (line 217: requires 100× API calls and is inferior to DNA-GPT, which is already a baseline). This is scope management, not a flaw.
- **"Table 2 is overcrowded"**: Style/formatting nitpick. Removed.
- **"Incomplete sentences in Section 3.4" / "GPT-3.2" as a substantive weakness**: These are parser artifacts (garbled text from PDF extraction), not author errors. Removed per hard rules.
- **"Cross-lingual numbers are suspiciously high"**: This is speculative. The results are reported as-is with no evidence of error. Removed.

## Novel Insights

The two reviews together surface an interesting tension: the paper's strongest results come from the simplest estimation algorithm (Geometric distribution — pure exponential decay with one parameter), despite it having the highest KL divergence from the true distribution. The Harsh Critic notes this as a potential issue, but it could equally be read as a strength: a very simple, well-behaved parametric form that preserves the relative ordering of probabilities well enough to compute expectations (μ̃, σ̃²) accurately for curvature-based metrics, even if individual probabilities are off. This suggests that what matters for Fast-DetectGPT is not pointwise distributional accuracy but preservation of certain statistical moments — a finding worth exploring more explicitly.

## Suggestions

1. Clarify the Zipfian loss function and what constitutes "typical values" for α and β — this is the single most underspecified part of the method.
2. Scope the "first to enable white-box methods" claim to methods requiring the full predictive distribution, and note that Likelihood (which operates on a single probability) is already available through API.
3. Add standard deviations or bootstrapped confidence intervals to the main AUROC results (Table 2), or at minimum clarify what varies across the three runs.
4. Specify what data the MLP estimator is trained on, even briefly (e.g., "trained on full-distribution samples from open-source models of comparable size").

## Score and Decision

**Score:** 7.0 — The paper presents a simple, practical, and well-motivated idea with strong empirical support. The methodological gaps (Zipfian parameter selection, MLP training data) are real but addressable and do not threaten the core contribution. The efficiency and accuracy gains over black-box methods are clearly demonstrated.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>