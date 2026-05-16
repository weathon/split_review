Now I have a thorough understanding of the paper and all the claims. Let me produce the consolidated review.

## Summary

This paper proposes a novel training data extraction (TDE) attack: instead of extracting from a fixed pretrained LM, the adversary adversarially fine-tunes the LM to *amplify* its exposure of pre-training data. Since the adversary does not know the pre-training dataset, they pseudo-label self-generated texts using DetectGPT's perturbation discrepancy (ranking which generated texts are more "human-like" and thus more likely to contain training data), then apply RLHF to reward generations with lower perturbation discrepancy. Experiments on six OPT model sizes (125M–13B) show consistent amplification, reaching 4–8× more extracted training data for models >1B parameters. Ablation studies confirm the effect is not simply overfitting or repetition.

## Strengths

1. **Novel attack paradigm that shifts from passive extraction to active amplification.** Unlike prior work that improves extraction from a *fixed* LM (better prompts, ranking, sampling), this paper shows that an adversary who can fine-tune the model can make it *leak more* of its pre-training data. The combination of pseudo-labeling via perturbation discrepancy + RLHF is a creative and well-motivated pipeline. This represents a genuinely new threat model in the privacy literature.

2. **Pseudo-labeling avoids the need for ground-truth membership labels or arbitrary thresholds.** The attacker has no access to the training data, yet the paper shows that ranking texts by perturbation discrepancy and pairing top-half vs. bottom-half creates a signal that a reward model can learn (62–70% accuracy across model sizes, Table 1). The use of relative comparisons (pairwise preferences) rather than absolute thresholds is a principled choice that mitigates noise in the pseudo-labels.

3. **Systematic evaluation across six model scales with consistent methodology.** The experiments cover 125M to 13B parameters using the OPT family, with fixed generation settings and suffix-array verification against ten training datasets. The results show a clear log-linear trend in baseline exposure (replicating prior findings) and a consistently steeper slope after fine-tuning (Figure 2). The qualitative analysis (data source breakdown, extraction length distributions) adds useful texture.

4. **Ablation studies supporting genuine memorization amplification.** Three ablations demonstrate the effect is not just overfitting: (a) amplification persists after deduplication (2.6×–8.4×, Table 3); (b) up to 98% of extracted samples from the fine-tuned LM are unique (do not overlap with reference-LM extractions, Table 4); (c) generation diversity (self-BLEU, unique n-grams) is maintained or improved (Tables 5–6). These results strengthen the core claim that fine-tuning enhances retention of the *original* training data.

## Weaknesses

### Fatal

None.

### Major

1. **The core assumption linking perturbation discrepancy to training data membership is not empirically validated.** The entire pseudo-labeling pipeline (§4.1) assumes that texts with lower perturbation discrepancy (more "human-like" per DetectGPT) are more likely to contain pre-training data. This is a plausible heuristic — training data is human-written, so texts overlapping with it may appear more human-like — but the paper provides no direct calibration. The authors do not compare perturbation discrepancy distributions between known members (extracted texts) and known non-members (e.g., held-out generated texts that did not match training data). Without this validation, the causal mechanism remains opaque: the observed amplification could partially arise from the model learning to produce smoother, lower-perplexity text that the suffix-array matcher is more likely to flag as matching training data (e.g., common Wikipedia phrasings). RQ1 shows the RM can learn the perturbation-discrepancy ranking, and the attack works downstream, but this only shows internal consistency of the pipeline, not that perturbation discrepancy actually tracks membership. A calibration experiment comparing perturbation discrepancies on known members vs. non-members would directly test this assumption and would significantly strengthen the paper.

### Minor

1. **The RM training procedure discards failed runs without reporting how often they occur.** The paper states (§5.2): *"We present outcomes of repeated RM fine-tuning on different seeds until a valid result emerges five times"* and acknowledges observing *"flawed learning outcomes for multiple times, such as RM's test accuracy converging to 0."* However, the failure rate is not reported. If RM training fails in, say, 50% of seeds, the attack's reliability for a real adversary is much lower than the reported 63–70% accuracies suggest. The paper argues that an adversary can repeat training until success, which is reasonable, but the missing statistics make it impossible to assess the expected computational cost and reliability. Reporting the success rate across all attempted seeds would resolve this.

2. **Main TDE results are based on a single generation run per model (100k texts each).** While generating 100k texts is substantial, the paper does not provide confidence intervals or repeated runs for the main results (Table 2). The paper states this is because *"generating 100,000 massive texts can reduce bias for true positives"* — a defensible position but not a substitute for variance estimates. Given the known variance in TDE extraction results, at least one replication (e.g., for OPT-1.3B which shows the largest amplification) would help establish reliability.

3. **The computational cost of the attack is not discussed.** The pipeline requires: generating 100k texts of length 256 from the target LM, perturbing each 10× with T5-Large (770M), computing log-probabilities for all perturbed texts under the target model, RM training, and PPO fine-tuning. For a 13B model this is plausibly thousands of GPU-hours. Acknowledging this cost would help readers assess practical attack feasibility under realistic adversary budgets.

4. **The uniqueness analysis (Table 4) uses a coarse overlap threshold.** The paper reports that 70.3–98.0% of extracted samples have <64 tokens of overlap with reference-LM extractions, concluding these are "new" memorized examples. While this threshold is standard in TDE evaluation, it cannot distinguish between genuinely new training data and different phrasings of the *same* memorized content. A finer-grained analysis (e.g., Jaccard similarity at the document level, or semantic similarity) would strengthen the claim that fine-tuning creates *new* memorization rather than surfacing different surface forms of already-memorized content.

### Trivial

- The paper states "four to eight-fold increase" but OPT-6.7B shows 3.8× (Table 2, last column). While 3.8 ≈ 4 is a reasonable rounding for "approximately four," the claim could be slightly more precise (e.g., "approximately four- to eight-fold" or "up to eight-fold").
- The paper does not show a verbatim example of an extracted text alongside its perturbation discrepancy, which would make the pipeline more tangible. (This is a presentation choice, not a substantive gap.)

## Nice-to-Haves

- **Control experiment with random/flipped labels.** Fine-tuning the target LM on pseudo-labels where the chosen/rejected labels are randomly assigned (or flipped) would test whether the perturbation-discrepancy signal is causally responsible for amplification. If amplification disappears under flipped labels, the case for the mechanism is strengthened. If it persists, the mechanism may be simpler (e.g., any additional fine-tuning on self-generated data increases exposure).
- **Comparison of perturbation discrepancy distributions between known members and non-members.** As noted in Major #1, a direct calibration experiment would validate the central assumption.
- **Testing on a non-OPT architecture (e.g., Pythia, LLaMA) to improve architectural diversity**, as the paper itself acknowledges this limitation.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"OpenAI fine-tuning API does not give white-box access"** — The reviewer interpreted the paper as claiming the API provides white-box access. The paper lists three *separate* reasons fine-tuning scenarios are realistic: (1) open-sourcing of models, (2) model extraction techniques (which can recover parameters from black-box access), and (3) the general trend of fine-tuning services. The API example is a trend indicator, not a claim that it provides white-box access. This criticism misunderstands the paper's threat model justification.
- **"Section 2.1 is missing the connection to membership inference"** — The paper has no §2.1 on membership inference. The background section (§2) covers DetectGPT and RLHF. Membership inference connections are discussed in the Related Work (§7.1). The reviewer appears to have conflated section numbers.
- **"Four to eight-fold claim not supported for all model sizes"** — As noted under Trivial, this is an overly precise pedantic complaint. 3.8× (6.7B) rounds to ~4, and the range across >1B models is 3.8–8.0. The characterization is accurate.
- **"The paper conflates amplification with baseline memorization"** — The paper's uniqueness analysis (Table 4) directly addresses this, showing most extracted samples from the fine-tuned LM are unique. The reviewer's claim that the overlap analysis is "coarsely binned" ignores that Table 4 reports five separate overlap bins (0–64, 64–128, 128–192, 192–256, 256), not a single threshold.
- **"Missing explanation for OpenSubtitles and DM Mathematics resistance"** — The paper provides a reasonable speculation: "these two datasets might have resisted TDE attacks because of their relatively high complexity." A deeper explanation would require a different paper.
- **"Single generation run" complaint** — The paper justifies this with the large sample size (100k texts). This is noted as a Minor weakness above (lack of variance estimates), but the reviewer's framing as a major gap is overblown.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface concerns about unvalidated assumptions and reporting gaps that are visible from careful reading of the paper itself; no reviewer identified a novel connection to a separate body of work or a theoretical issue the authors were unaware of.

## Suggestions

1. **Run a calibration experiment**: Take a sample of texts extracted by the reference model (known members) and texts not matched by the suffix array (known non-members). Compute their perturbation discrepancy distributions and show the separation. This would directly validate (or refute) the central assumption and is the single most impactful experiment to add.
2. **Report RM training success rate**: Across all attempted seeds, what fraction yielded "valid" (≥~55% test accuracy) RM training? This transparency would strengthen credibility.
3. **Add at least one replication** for the main TDE measurement on a representative model size (e.g., OPT-1.3B) with 2–3 independent runs, reporting mean and range.
4. **Discuss computational cost** in the Limitations section so readers can calibrate the attack's practicality.
5. **Consider a flipped-label control**: Fine-tune OPT-1.3B on pseudo-labels where the preference is reversed (reward higher perturbation discrepancy). If amplification disappears, this strengthens the causal story considerably.

## Score and Decision

This paper presents a novel attack paradigm that is well-motivated, reasonably executed, and relevant to the privacy and security community. The core idea — adversarially fine-tuning a model to amplify its own training data exposure — is creative and opens a new direction for TDE research. The experiments are systematic (6 model sizes, standard metrics, thoughtful ablations) and the results are consistently positive.

However, the paper has an important evidential gap: the foundational assumption that perturbation discrepancy correlates with training data membership is unvalidated. While the overall pipeline "works" empirically, the lack of direct calibration makes it unclear whether the mechanism is what the authors claim or something simpler (e.g., the model learning to produce smoother text that coincidentally matches training data patterns). This is fixable with additional experiments but is not a fatal flaw — the contribution stands as a novel attack even if the exact mechanism is partially unresolved.

The remaining issues (unreported RM failure rate, single-run results, computational cost) are addressable in revision. The paper makes a clear contribution and the core claims are supported by the evidence.

**Score**: 6.5 — A solid paper with a novel contribution, a systematic evaluation, and candid limitations. The main weakness is concrete and fixable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>