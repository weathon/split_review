- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

The paper introduces FS-SINR, a Transformer-based approach for few-shot species range estimation. Given a small set of observed presence locations for a previously unseen species (and optional text metadata), FS-SINR generates a species embedding in a single forward pass without any retraining, and uses it to predict range probabilities across all locations of interest. The model is trained on 35.5M citizen science observations across 44K+ species and evaluated on two benchmark datasets (IUCN, S&T).

## Strengths

1. **Feed-forward inference for unseen species without retraining.** Unlike the baselines (SINR, LE-SINR) which require per-species logistic regression training at inference time, FS-SINR produces a species embedding from context locations in a single forward pass (Section 3.2, Figure 2). This is a genuine architectural contribution enabling interactive exploration and efficient deployment.

2. **Consistent improvement across all few-shot settings on two benchmarks.** In Figure 3, FS-SINR outperforms both SINR and LE-SINR at every data regime (1, 2, 5, 10, 50 observations) on both IUCN and S&T datasets. The gains are most pronounced in the extremely low-data regime (1–10 observations) that represents the reality for the majority of species.

3. **Flexible integration of multiple input modalities.** FS-SINR can combine variable-length location sequences with text embeddings (range descriptions, habitat descriptions, taxonomic text) within a single model (Section 3.2.1). Table 1 validates that adding text improves zero-shot predictions, and Figure 5 shows controlled range generation from text plus a single location.

4. **Parameter efficiency.** FS-SINR uses 6.3M learnable parameters vs. SINR's 11.9M (Section 4.1), while achieving better performance — a non-trivial efficiency gain.

## Weaknesses

### Fatal
None.

### Major

1. **Unequal treatment of the location encoder confounds the few-shot comparison.** Section 4.1 states that for FS-SINR, "the parameters are updated jointly with the location and text encoders and species decoder during training." This means the location encoder is fine-tuned during FS-SINR training. In contrast, the baselines (SINR, LE-SINR) use a location encoder that was pretrained on the same training data but **not** fine-tuned — they only train a logistic regression head for each new species at inference time. The paper does not provide an ablation where FS-SINR's location encoder is frozen, so it is impossible to determine how much of the reported 5–10% MAP improvement comes from the proposed Transformer-based few-shot head versus the additional location encoder fine-tuning. This is a structural experimental confound rather than a methodological error, but it undermines the attribution of gains to the claimed contribution. A frozen-encoder ablation is necessary to substantiate the core claim.

### Minor

2. **The zero-shot comparison lacks a direct LD-SDM baseline.** Table 1 compares FS-SINR to SINR and LE-SINR in the zero-shot setting, but LD-SDM (Sastry et al., 2023) — cited in the paper as a representative zero-shot method — is not included in the table. Row 5 uses an FS-SINR variant with taxonomic text (as in LD-SDM), but this is not a direct comparison to LD-SDM itself. Including LD-SDM numbers (or explaining why they cannot be directly compared under the same protocol) would strengthen the zero-shot evaluation.

3. **Ablation results are stated but not shown in the main paper.** Section 4.3.1 asserts that "FS-SINR is robust to many of these changes" (different location encoders, architectural modifications, data amounts) but contains no quantitative results. The paper references "Tab. A1" in the appendix, which is not available in this submission. For a new-method paper, at least a summary table of the most important ablations (e.g., frozen encoder, varying context locations, impact of species decoder) should appear in the main paper.

4. **Limited number of evaluation runs and no significance testing.** Figure 3 reports standard deviations over only three random seeds. Some error bars overlap between methods (e.g., FS-SINR(5) vs. LE-SINR(RT) on S&T in some regimes), and no statistical significance is reported. While three runs are common practice in this domain, the authors should acknowledge the limitation and report whether the observed gaps are statistically meaningful.

### Trivial
None.

## Nice-to-Haves

- The FS-SINR loss (Eq. 2) uses a "full assume negative" approximation for presence-only data, which may introduce noise when species co-occur. A brief discussion of sensitivity to this approximation would be useful, but this is standard practice in the field and not a flaw.
- A small expansion: explaining whether the baselines' pseudo-absence strategy (20K points per species) was tuned for fairness. (The paper does describe the strategy — 10K uniform + 10K target — which partially addresses this.)

## Removed Points

- **"SOTA claim rests on only two baselines"** (general version): The critic faults the paper for comparing only to SINR and LE-SINR. However, these are the two most directly relevant few-shot methods in the literature. Traditional methods like MaxEnt are not designed for the few-shot setting with shared representations. The main SOTA claim is about few-shot estimation, where SINR and LE-SINR are the correct comparators. This criticism is retained only in its specific zero-shot form (Weakness 2 above). The broader "only two baselines" complaint is removed as scope-creep.

- **Criticism about pseudo-absence generation not being discussed for fairness**: The paper explicitly states (Section 4.1, line 118): "we train a per-species binary logistic regression classifier … in addition to adding 10,000 uniformly random and 10,000 target pseudo-absences as in Hamilton et al. (2024)." This is addressed. Removed.

- **"Qualitative examples are not necessary"**: Subjective opinion, not a weakness. Removed.

- **Strengths about "addressing an important problem" or generic praise from Strength Finder**: These are generic and conflict with the discipline of only keeping concrete, evidence-backed strengths. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new way of viewing the problem or an unrecognized implication of the results beyond what the authors themselves discuss.

## Suggestions

1. **Provide a frozen-encoder ablation.** Train FS-SINR with the location encoder frozen (i.e., only updating the Transformer and species decoder) and report the results alongside the fine-tuned version and baselines. This is the single most informative experiment for validating the paper's core claim.
2. **Add LD-SDM results to Table 1** for the zero-shot comparison, or explain why a direct comparison is infeasible under the same protocol.
3. **Move a summary of key ablations** (at least frozen encoder, varying context count, impact of species decoder) into the main paper, even as a small table.
4. **Report per-method confidence intervals** from bootstrapping or discuss the statistical reliability of the observed gaps given the limited number of runs.
