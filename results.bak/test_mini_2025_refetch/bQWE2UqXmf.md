Now I have sufficient calibration data. Let me write the final consolidated review.

## Summary

The paper introduces Raidar, a method that detects AI-generated text by prompting an LLM to rewrite the input and measuring the editing distance. The key insight is that LLMs modify human-written text more than machine-generated text (which they perceive as high-quality). Raidar operates purely on symbolic word output, making it compatible with black-box APIs, and achieves F1 improvements of up to 29 points over prior methods across 6 domains.

## Strengths

1. **Novel, intuitive, and well-motivated idea.** The central hypothesis — that LLMs are more invariant when rewriting their own output than human text — is clearly stated and empirically validated (Figure 2 shows clear distributional separation on 4000 Yelp samples). This is a genuinely different signal from log-probability-based methods.

2. **Large and consistent empirical gains.** Table 1 shows Raidar (Invariance) outperforms Ghostbuster on all six datasets, with gains as large as 29 points on Code (95.38 vs. 65.97) and 16 points on Yelp Reviews (87.75 vs. 71.47). The improvements hold across both in-distribution and out-of-distribution settings (Table 2).

3. **Operates on black-box symbolic output only.** As stated in Section 3.2, the detector uses discrete editing distances, not continuous probability features. This makes it compatible with APIs like GPT-3.5 and GPT-4 that only expose text — a practical advantage over DetectGPT and Ghostbuster.

4. **Broad evaluation across multiple dimensions.** The paper evaluates OOD generalization (Table 2), cross-model detection (Table 4 — detects text from Ada, GPT-3.5, GPT-4, LLaMA 2 without retraining), adversarial robustness with multi-prompt training (Table 3), and performance across rewriting models of different sizes (Table 5). This is a more comprehensive evaluation than typical in this area.

5. **Strong performance on short inputs.** Figure 5 shows 74 F1 on 10-word Yelp reviews, a regime where many detectors (GPTZero, Ghostbuster) degrade significantly.

## Weaknesses

### Major

1. **Ambiguity about how the three metrics are combined into the final detector.** Section 3.2 states "The invariance, equivariance, and uncertainty measured by the above metric will be used as features for a binary classifier." However, Tables 1–2 report results for each metric *separately* ("Ours (Invariance)", "Ours (Equivariance)", "Ours (Uncertainty)"). It is unclear whether the headline results come from a classifier trained on a single metric, or from one that combines all three. If the appendix (stripped in this format) clarifies this, the paper should state it explicitly in the main text. If each metric is used individually as a single feature, this is valid and should be stated; if they are combined, the combined result should be reported alongside the ablations. As written, a reader cannot tell what the "Raidar" detector actually is.

2. **The comparison to baselines is confounded by unequal rewriting/scoring model capacity.** The paper uses GPT-3.5-Turbo for rewriting, while DetectGPT uses OPT-2.7B for scoring. A large fraction of the F1 gain could come from the stronger rewriting model rather than the editing-distance idea itself. The paper partially addresses this with Table 5 (showing Raidar with Ada- and LLaMA 2-based rewriting), where even Ada achieves competitive results (e.g., Code 77.42 vs. Ghostbuster 65.97). However, a controlled experiment where the *same* model generates features for both Raidar and the baselines (e.g., using GPT-3.5 log-probabilities for Ghostbuster, or using OPT-2.7B as the rewriting model) would be needed to cleanly attribute the gains.

### Minor

3. **K (number of generations) for the uncertainty metric is not specified.** The uncertainty formula in Section 3.1 defines a sum over K outputs but never states what K is. This is needed for reproducibility.

4. **No confidence intervals or variance estimates.** F1 scores are reported as point estimates without confidence intervals or standard deviations. Given that some datasets are relatively small (e.g., Arxiv has 350 human abstracts), variance could be non-negligible.

5. **Prompt selection methodology is unclear.** Figure 6 shows substantial variation across prompts (e.g., on Code, best prompt ~90 F1 vs. worst ~75). The paper does not state whether the prompts used in main experiments were chosen on a held-out validation set or if they were fixed before seeing test data. If prompts were selected based on test-set performance, results would be optimistic.

### Trivial

6. The uncertainty metric (Section 3.1) averages pairwise distances across K generations but does not normalize by the number of pairs. Different K values would produce systematically different scales, though this does not affect classification if K is fixed.

## Nice-to-Haves

- A cost/API-call comparison with baselines would be useful for practitioners. Raidar uses 1 rewrite call per input vs. DetectGPT's 100 perturbations, which is likely cheaper, but this is not quantified.
- Analysis of failure cases (false positives/negatives) would improve understanding of the method's limitations.
- Combining all three metrics into a single classifier and reporting the joint result would strengthen the deliverability of the method.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Equivariance T/T^{-1} is self-inverse and doesn't reverse":** The paper's T and T^{-1} for the "opposite meaning" example are the same prompt, which is a valid self-inverse transformation (applying "opposite" twice returns to the original). The paper also provides a proper non-self-inverse pair (Expand/Concise). The criticism misunderstands the design.
- **"Method is not reproducible as stated":** Overstated. The basic algorithm (compute editing distance → feed into binary classifier) is described. The missing details (K value, metric combination) are real but are addressed as weaknesses #3 and #1 above. The paper also provides a GitHub repository.
- **"Adversarial evaluation is limited to two hand-crafted prompts":** This is a scope observation, not a flaw. The paper shows multi-prompt training substantially improves robustness, which is a meaningful finding, and the adversarial evaluation is more than many detection papers provide.
- **"The code dataset result may not transfer to less structured code":** This is speculation without a concrete anchor in the paper. The paper notes the HumanEval dataset, which is a standard benchmark.

## Novel Insights

The harsh critic's observation that the comparison is confounded by model capacity (weakness #2) is a genuine insight that the authors should address. The critic correctly identifies that the marginal contribution of the *algorithm* versus the *rewriting model's strength* is not disentangled. The Strength Finder's observation that Table 5 partially addresses this (showing strong results with smaller rewriting models like Ada) is also useful and tempers the severity. The core tension between these two perspectives is the paper's most interesting unresolved question.

## Suggestions

1. **Clarify the detection algorithm precisely:** State explicitly whether the three metrics are used individually or combined. If combined, report the joint result. If used individually, state this clearly and explain that each row in Table 1 is a single-feature classifier. Move this from the appendix to the main text.

2. **Add a controlled-cost experiment:** Either (a) run Ghostbuster/DetectGPT with GPT-3.5-Turbo log-probabilities where available, or (b) run Raidar with OPT-2.7B as the rewriting model and compare to DetectGPT's OPT-2.7B-based results. This would isolate the algorithmic contribution.

3. **Specify all hyperparameters in the main text:** State K for the uncertainty metric, the training/validation split, and the prompt selection procedure.

4. **Add confidence intervals or bootstrap estimates** for the main F1 results (or at minimum, note whether the results are stable across multiple runs).

5. **Consider adding a "Combined" row to Table 1** that uses all three metrics as features in the same classifier, alongside the single-metric ablations.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (score < 3.5): F3Migaak2i (avg 3.0, withdrawn), B37UmlxsaP (avg 2.5, reject) — clearly below this paper
- Middle band (3.5–7.5): cWiEN1plhJ (avg 5.0, accept poster, Few-Shot Detection), HsB1sQvXML (avg 3.8, reject, LLM Detectors Still Fall Short), WbqBj2aC5k (avg 5.4, reject, Online Detecting), ccxD4mtkTU (avg 4.75, accept poster, Misinformation Detection)
- Strong band (>7.5): syThiTmWWm (avg 7.75, oral), UHPnqSTBPO (avg 8.0, oral) — not comparable domains

**Round 2 (Narrowing, estimated bracket 5.0–6.7):**
- z9j7wctoGV (avg 6.0, accept poster, Deep Kernel Relative Test) — comparable domain, similar breadth of evaluation; Raidar's idea is cleaner but has the metric-combination ambiguity. Similar quality.
- Xlayxj2fWp (avg 6.67, accept poster, DNA-GPT) — very similar paper (training-free detection via LLM regeneration); Raidar is comparable in breadth but DNA-GPT has cleaner presentation. Raidar is slightly below.
- 4eJDMjYZZG (avg 6.0, accept poster, LLM Detectors Are Easily Optimized Against) — different paper type (attack paper) but similar quality tier.
- fwHVclv0ij (avg 5.25, reject, Online Detection for Black-Box LLMs) — Raidar is stronger.

**Final placement:** Between Few-Shot Detection (5.0) and DNA-GPT (6.67). Comparable to Deep Kernel (6.0). The paper has a strong novel contribution and broad evaluation, but the metric-combination ambiguity and the uncontrolled model comparison prevent it from reaching a higher tier.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>