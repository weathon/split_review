Now I have all the information needed. Let me compose the consolidated review.

## Summary

HATFormer adapts the TrOCR transformer architecture for historical Arabic handwritten text recognition (HTR) with three customizations: (1) a BlockProcessor that packs text-line images into a 384×384 ViT container while preserving horizontal resolution, (2) a custom Arabic BBPE tokenizer that reduces token counts by over 300%, and (3) a two-stage training pipeline using 1M synthetic printed images followed by overtraining on real handwritten data. The main empirical result is an 8.6% CER on the Muharaf historical dataset, a 51% improvement over the previous best published baseline (17.6%).

## Strengths

- **Strong empirical gains on the most relevant benchmark.** On the historical Muharaf dataset, HATFormer achieves 8.6% CER vs. 17.6% for Saeed et al. (2024), a 51% relative improvement. This is the paper's central claim and is well-supported by Table 1. The ablation study (Table 3) shows each proposed component contributes substantially to this gain: BlockProcessor removal increases CER by 11.4%, custom tokenizer removal by 10.9%, and synthetic pretraining removal by 4.2%.

- **Novel BlockProcessor design with clear motivation.** The paper identifies that ViT's default 384×384 resize compresses typical Arabic text-line images by ~1.6× horizontally (Section 4.1), degrading stroke clarity. The proposed solution — packing the line into a 384×384 grid via segmentation into 384-pixel-wide chunks stacked vertically — is well-motivated and its critical importance is validated by the ablation study (11.4% CER increase when removed).

- **Custom Arabic BBPE tokenizer with substantial compression.** Training a BBPE dictionary on an Arabic corpus reduces token sequence length by over 300% compared to the default ASCII-biased tokenizer. The ablation confirms this is not merely an efficiency gain: removing it increases CER by 10.9%, demonstrating that compact representation simplifies the classification problem.

- **Comprehensive cross-dataset evaluation.** Section 5.4 reports systematic cross-dataset experiments showing that training on historical Muharaf generalizes to modern handwriting (26% CER) better than the reverse (≥40% CER). The system also outperforms the Saeed baseline on most cross-dataset pairs (e.g., 27.5% vs. 33% on Muharaf→KHATT).

## Weaknesses

### Fatal

None.

### Major

- **Claim that attention addresses three specific Arabic challenges is asserted without direct evidence.** The abstract and introduction (lines 6, 36–37) state that the attention mechanism "effectively address[es]" cursive writing, context-dependent character shapes, and diacritics, and Contribution 2 (line 47) says the method "has proven effective" in this regard. Yet no experiment isolates or measures the model's handling of these phenomena. The ablation study tests the BlockProcessor, tokenizer, synthetic data, and overtraining — none of which directly probe the attention mechanism's role. No analysis compares CER on words with vs. without diacritics, on characters in different positional forms (initial/medial/final/isolated), or on text where cursive joins are artificially broken. The attention maps (Figure 5) are referenced but not quantitatively analyzed against these three challenges. This claim appears in the abstract, introduction, and contribution list, but the evidence for it is merely the overall system performance — which conflates many factors. The paper would be stronger without this attribution claim, or with targeted experiments to support it.

### Minor

- **BlockProcessor description lacks full precision for the segmentation step.** The paper says the processor "warp[s] it to fill in the ViT's 384×384-pixel image container from left to right and top to bottom" (line 106) and mentions "six nonoverlapping complete rows that are 384 pixels wide" (line 107). The intended operation — segmenting the 64-pixel-high line into 384-pixel-wide contiguous chunks and stacking them vertically — can be inferred from context and dimensions, but the term "warping" is geometrically imprecise for this packing/tiling operation. A step-by-step description (or pseudocode/diagram) would make the core contribution fully reproducible without guesswork.

- **Baseline comparison transparency is incomplete.** For the Lamtougui (2023) and Momeni (2024) baselines, the paper relies on published CER numbers and explicitly notes that "dataset splits used in these baselines may differ from those in our experiments, potentially affecting direct comparisons" (line 172). This is an honest acknowledgment, but the paper does not report what splits those baselines used, making it difficult for readers to assess the comparison's fairness. For the Saeed (2024) baseline on Muharaf (17.6% CER), the paper says they "retrained their model on each dataset for a fair comparison" (line 172), yet 17.6% matches Saeed's original publication — it should clarify whether this is the retrained result or the published number.

- **No quantitative analysis of attention maps.** Figure 5 is referenced (line 177) to "illustrate how the attention mechanism captures character relationships," but no quantitative metrics (e.g., attention entropy, positional bias, per-head relevance scores) are provided. For a paper that attributes a significant part of its performance gain to the attention mechanism's handling of Arabic-specific challenges, this is a missed opportunity to substantiate the claim.

- **"CNNs and RNNs are no longer required" overstates the evidence.** The paper claims (line 176) that results "imply that CNNs and RNNs are no longer required for HTR," but on KHATT, the Saeed (2024) hybrid baseline actually outperforms HATFormer (14.1% vs. 15.4%). The paper acknowledges this but still makes the sweeping statement. Transformer-only HTR works well on some benchmarks but the evidence does not yet support declaring CNNs/RNNs obsolete.

### Trivial

- The word "warping" in the BlockProcessor description (line 106) would be better replaced with "packing" or "tiling" to avoid confusion with geometric image warping (stretching/distortion).

## Nice-to-Haves

- A targeted analysis of diacritic handling (CER on lines with vs. without diacritics) or character-form accuracy (initial/medial/final/isolated) would substantially strengthen the claim about attention addressing Arabic-specific challenges.
- A brief qualitative error analysis showing common failure modes would complement the ablation study and guide future work.
- Discussion of the domain gap between printed synthetic data and historical handwriting (and whether a handwriting-specific synthetic generator could yield further gains) would be a natural addition.

## Removed Points

These points are flagged by reviewers but are removed or downgraded for the following reasons:

- **"Overtraining presented as a novel finding"** — The paper explicitly credits Mosbach et al. (2020) and Hao et al. (2019) (lines 140–143) and frames it as a technique they leverage, not a discovery. Removed because the paper does not claim novelty here.
- **"Synthetic data domain gap weakens claims"** — The paper acknowledges using printed text (Section 5.1) and the ablation shows synthetic pretraining helps by 4.2% CER. The observation is valid but is a future-work direction, not a weakness of the presented system. Moved to Nice-to-Haves.
- **"Missing reproducibility details" beyond BlockProcessor** — The reviewer's concern about reproducibility centered on the BlockProcessor description (addressed above in Minor). Other concerns about undisclosed hyperparameters are standard for a conference paper and are addressed in Section 4.3 (learning rate, batch size, warmup steps, GPU count).
- **"No discussion of handwritten synthetic generator"** — This is a suggestion for future work, not a weakness of the current paper. Moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a synthetic insight that reinterprets the paper's results in a way the authors did not themselves identify.

## Suggestions

1. **Replace "warping" with explicit language.** Describe the BlockProcessor operation step by step: given a 64-pixel-high line image of width W, segment it into ⌈W/384⌉ contiguous chunks of 384 pixels each (except the last), pad the last chunk if needed, and stack these chunks vertically to form a 384×384 image. Include a diagram or pseudocode.

2. **Clarify baseline comparisons.** Report the train/validation/test splits used in the Lamtougui (2023) and Momeni (2024) papers, or justify why cross-split comparison is still meaningful. Clarify whether the 17.6% CER for Saeed on Muharaf is from the authors' retraining or from the original publication.

3. **Either substantiate or drop the attention-challenge claim.** If kept, add an experiment comparing CER on lines with vs. without diacritics, or on characters in initial/medial/final/isolated forms. If no such experiment is feasible, remove the claim from the abstract and contribution list, as the overall system results are already strong without it.

4. **Add quantitative attention analysis.** Report at minimum the average attention entropy or a positional-attribution metric to support the claim that attention is meaningfully focusing on character-relevant regions.

5. **Tone down the "CNNs/RNNs no longer required" statement.** Replace with a more measured conclusion, e.g., "transformer-only architectures can be competitive with or surpass hybrid CNN-RNN baselines on historical Arabic HTR, as shown by the Muharaf results."

## Score and Decision

**Originality:** 6/10 — The paper adapts an existing architecture (TrOCR) with well-motivated customizations. The BlockProcessor and Arabic BBPE tokenizer are practical engineering contributions rather than architectural novelty.  
**Importance of research question:** 8/10 — Historical Arabic HTR is genuinely underserved, and the 51% improvement on Muharaf is practically meaningful for digital humanities.  
**Claims well supported:** 6/10 — The central empirical claim (8.6% CER on Muharaf) is well supported by ablation studies. However, the unsupported attribution to the attention mechanism for Arabic-specific challenges detracts from an otherwise clean paper.  
**Soundness of experiments:** 7/10 — The ablation study is thorough and the cross-dataset evaluation is a strength. The baseline comparisons have acknowledged limitations but are handled transparently.  
**Clarity of writing:** 6/10 — Generally clear, but the BlockProcessor description uses imprecise language ("warping") and the paper would benefit from more explicit implementation details for its core contribution.  
**Value to community:** 7/10 — The planned release of model weights, tokenizer, synthetic data generator, and error diagnostic app would be valuable resources for Arabic HTR research.  

The paper makes a solid empirical contribution to an important and under-resourced problem. The main weaknesses — the unsupported attention-challenge claim, imprecise BlockProcessor description, and baseline transparency — are addressable but need attention. The core empirical results (51% improvement on Muharaf, validated by ablation) are credible and practically significant.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>