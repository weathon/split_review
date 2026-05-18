Now I have all the verified information. Let me compose the final consolidated review.

---

## Summary

This paper presents HATFormer, a transformer-based encoder-decoder system for historical Arabic handwritten text recognition (HTR), built on TrOCR. The authors introduce three key Arabic-specific adaptations: (1) an aspect-ratio-preserving image processor (BlockProcessor) that mitigates information loss from ViT's fixed-size resizing, (2) a custom Arabic BBPE tokenizer for more compact text representation, and (3) a two-stage training pipeline with synthetic pretraining and overtraining. On the Muharaf dataset (the largest public historical Arabic handwriting collection), HATFormer achieves 8.6% CER — a 51% relative improvement over the previous best result (Saeed et al., 17.6% CER). The cross-dataset analysis shows that training on historical data generalizes better to modern handwriting than the reverse direction, a practically useful finding.

## Strengths

- **Significant performance improvement on historical Arabic HTR.** The 8.6% CER on Muharaf (vs. 17.6% from Saeed et al.) is a genuine advance for an under-served problem — 51% relative improvement in a language with far fewer resources than English. This directly demonstrates the value of the proposed adaptations.

- **Ablation study rigorously quantifies each component's contribution.** Table 4 decomposes the gains: removing BlockProcessor increases CER by 11.4%, removing the Arabic BBPE tokenizer by 10.9%, removing synthetic Stage-1 training by 4.2%, and removing overtraining by 1.3%. This proves all four components are necessary and that the headline improvement is not driven by any single factor alone.

- **Cross-dataset generalization evidence.** Table 3 shows that training on historical Muharaf achieves 26% CER on modern KHATT, while training on modern data achieves ~40% CER on historical Muharaf. This is a useful finding: historical data generalizes to modern handwriting better than the reverse, supporting the practical utility of the system for diverse collections.

- **Practical contributions for reproducibility and humanities use.** The paper commits to releasing the image processor, tokenizer, model weights, source code, synthetic dataset, and an OCR Error Diagnostic App. This is valuable for a domain (historical Arabic HTR) where such resources are scarce.

## Weaknesses

### Fatal
None.

### Major

- **Contribution 1 overclaims the breadth of SOTA results.** The first contribution states that HATFormer "outperforms the state of the art across various Arabic handwritten datasets." This is not supported by the data: on KHATT, HATFormer (15.4% CER) is *worse* than Saeed et al. (14.1%); on MADCAT, it achieves 4.2% vs. Rawls et al.'s 1.5%. The paper's own main text acknowledges these disparities — the 51% improvement applies specifically to Muharaf, and the paper calls the MADCAT result "comparable" while noting they did not optimize for KHATT/MADCAT. However, the broad "across various datasets" claim in the contribution list creates a rhetorical mismatch that damages credibility. This is fixable by restricting the claim to historical Arabic HTR (or specifically to Muharaf), where the paper's contribution is genuinely strong.

### Minor

- **Contribution 2 (attention addressing Arabic challenges) is not convincingly substantiated.** The paper claims that "leveraging the attention mechanism" differentiates cursive characters, decomposes context-dependent shapes, and identifies diacritics. The only evidence is Figure 4 (attention maps) and the overall system performance. No quantitative breakdown is provided — e.g., diacritic vs. non-diacritic error rates, or character confusion analyses targeting the three claimed challenges. The ablation study shows synthetic pretraining helps, but this does not isolate *attention* as the causal mechanism; any high-capacity architecture with appropriate training data might show similar improvements. This claim would be better positioned as a motivating narrative or tested with targeted analysis.

- **Baseline comparison conditions not fully specified.** The paper reports retraining Saeed et al.'s model "for a fair comparison" but does not explicitly confirm whether identical train/validation/test splits were used. Since HATFormer uses an 85-15-5 split on Muharaf (different from potential splits in the original Saeed et al. work), this ambiguity weakens the controlled nature of the headline 51% improvement comparison. The paper should state clearly whether the retrained baseline used the same partition as HATFormer.

- **No confidence intervals or variance reported.** All CER values are point estimates from single runs. While the large ablation gaps (11.4%, 10.9%) are likely robust, the smaller 1.3% gain from overtraining and some cross-dataset differences could potentially fall within run-to-run noise. Reporting variance would strengthen confidence in the conclusions.

- **Synthetic data domain not characterized.** The paper describes sampling from an 8.2M-word Arabic corpus but does not state whether it is domain-matched to historical 19th–21st century manuscripts or general modern Arabic. Since the downstream task is historical, a domain mismatch could affect the synthetic pretraining's relevance (e.g., vocabulary coverage of archaic terms, realistic ink bleed/faded text simulation).

### Trivial

- **Stage 2 training duration not reported.** The paper mentions that overtraining "can take twice as long as the minimum validation loss" but does not provide the actual number of epochs or training steps. Reporting this would aid reproducibility.

## Nice-to-Haves

- A direct ablated comparison isolating the synthetic pretraining from the TrOCR initialization would strengthen the synthetic data argument. Currently, Table 1's "F" (random init) shows the importance of pretrained weights broadly, but "TrOCR init + synthetic pretraining" vs. "TrOCR init only" would more cleanly demonstrate the value of Arabic-specific synthetic data.
- The MADCAT comparison could be sharpened by reporting CER with and without their Arabic post-processing normalization, testing whether the gap to Rawls et al. (1.5%) closes.
- The cross-dataset generalization finding (historical→modern > modern→historical) is interesting and could be unpacked further — e.g., does this hold across different writing styles, time periods, or degradation levels?

## Removed Points

These points were flagged for removal and should be treated with caution; they do not appear in the main review above.

- **Strength removed: "Systematic adaptation of transformers to Arabic-specific challenges"** — This strength from the Strength Finder claimed the paper provides "empirical evidence via attention maps (Figure 4) showing how the attention mechanism addresses" Arabic challenges. This conflicts with the verified weakness that the attention claim is not substantiated by quantitative analysis. Per the rule, the weakness wins, so this strength is dropped.

- **Harsh Critic's point about "fairness of baseline comparisons" regarding splits being potentially different for Muharaf** — This is kept in Minor but downgraded from the reviewer's framing. The paper says "for a fair comparison" which strongly implies same splits; the ambiguity is a clarity issue, not evidence of unfair comparison.

- **Harsh Critic's point about "unsupported claim about attention addressing intrinsic Arabic challenges"** — Kept as a Minor weakness rather than a structural/fatal flaw. The paper's core contribution is a well-engineered system that works, not a scientific proof of mechanism. The attention framing is a motivating narrative, and the overall system performance (especially the ablation) does demonstrate that the system handles Arabic challenges effectively, even if attention is not isolated as the specific cause.

- **"Validation stopping criteria discrepancy"** — The paper's rationale for different stopping criteria (loss vs. CER) between stages is clearly explained in Section 4.3. The reviewer's request for more detail is reasonable but does not constitute a discrepancy or error.

- **"Synthetic dataset generation details" about domain matching** — Kept as Minor but the reviewer's framing as a structural gap is downgraded. The synthetic data is one of several components, and the ablation shows its benefit even if the corpus is not explicitly historical-matched.

## Novel Insights

The cross-dataset finding that training on historical Arabic handwriting (Muharaf) generalizes better to modern handwriting (KHATT, 26% CER) than the reverse direction (~40% CER) is a genuinely non-obvious result. It suggests that the diversity and variability in historical manuscripts may provide a more robust training signal than cleaner modern datasets, even for modern-domain test data. This is a practical insight for practitioners building Arabic HTR systems for heterogeneous collections. Beyond the paper's own contributions, no additional novel insights emerge from the reviews.

## Suggestions

1. **Restrict the SOTA claim in Contribution 1** to historical Arabic HTR (or specifically to Muharaf), where the paper's contribution is genuinely strong. The Abstract already does this reasonably well; align the contribution list with it.
2. **Explicitly confirm** that the retrained Saeed et al. baseline used the same train/validation/test splits as HATFormer. This removes ambiguity from the headline result.
3. **Either drop Contribution 2's attention-specific claim or support it** with a targeted quantitative analysis (e.g., CER on diacritic vs. non-diacritic characters, or character confusion breakdowns showing the attention mechanism reduces specific error types).
4. **Report CER with variance** (e.g., 2–3 runs or bootstrap confidence intervals) for the main results and the ablation study.
5. **Characterize the synthetic data corpus** — state whether it is domain-matched to historical Arabic and, if not, discuss potential limitations.

## Score and Decision

The paper presents a genuine advance for an under-served problem (historical Arabic HTR), supported by a well-designed ablation study and an interesting cross-dataset analysis. The major weakness — overclaiming in Contribution 1 — is a presentation issue rather than a methodological flaw, and the remaining weaknesses are minor or easily addressable. The core technical contributions (BlockProcessor, Arabic BBPE tokenizer, synthetic + overtraining pipeline) are sound and their individual value is quantified.

**Originality**: Good — adapting English HTR transformers to Arabic-specific challenges with well-motivated components.  
**Importance**: High — historical Arabic manuscript digitization is under-resourced.  
**Claims support**: Adequate for the main result (Muharaf); Contribution 1's scope is overstated.  
**Soundness**: Solid ablation, but single runs and ambiguous baseline splits are minor concerns.  
**Clarity**: Clear writing, though attention claim could be more precise.  
**Value to community**: High — code/model/tool release in a resource-scarce domain.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>