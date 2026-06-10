Here is my final consolidated review.

---

## Summary

This paper proposes two components for multi-task perception (drivable area segmentation and object detection) in unstructured driving environments: (1) ADC Learning, a two-phase semi-supervised training strategy that alternates between tasks with frozen branches then uses pseudo-labels to handle non-overlapping dataset annotations, and (2) SAMEnhancer, a post-processing tool that extracts point prompts from network predictions, runs Mobile SAM, and fuses the outputs via confidence-guided thresholding. Experiments on BDD100K and IDD show improvements over the paper's own ablations.

## Strengths

- **ADC learning directly targets a genuine practical problem that prior MTL methods do not address.** The paper correctly identifies that existing multi-task perception frameworks (YOLOP, MultiNet, DLT-Net, FULLER) "typically rely on well-aligned datasets with consistent annotations across all tasks" (line 44), while datasets like IDD have segmentation and detection annotations on non-overlapping images (line 47). The two-phase design (alternating training with frozen branches → pseudo-label cross-supervision) is a principled architectural response to this specific data constraint (lines 68–70).

- **Controlled experiment on BDD100K provides a clean baseline.** By taking the fully-annotated BDD100K dataset and splitting it into two non-overlapping halves (one with segmentation labels, one with detection labels), the paper creates an apples-to-apples comparison where the ground-truth upper bound is known (line 176). This is a sound experimental design choice for isolating the degradation-and-recovery story.

- **Cross-architecture validation.** ADC learning is tested with ConvNeXt, EfficientNet, and DenseNet encoders replacing the default YOLOP backbone (Table 2, line 180), demonstrating the method is not tightly coupled to a single architecture.

- **SAMEnhancer uses Mobile SAM (not full SAM).** The paper explicitly notes SAM's computational cost and selects Mobile SAM for real-time feasibility (line 131), rather than proposing an impractical full-SAM post-processor.

## Weaknesses

### Major

- **No comparison against any external baseline or prior method.** The experimental section compares only three conditions: the authors' YOLOP variant without ADC learning, the same variant with ADC learning, and that variant with both ADC learning and SAMEnhancer (Tables 1–3). There are zero comparisons to the original YOLOP pipeline, to any other multi-task framework (MultiNet, DLT-Net, LSNet, FULLER), to any semi-supervised learning baseline (self-training, mean teacher, co-training), or to any prior SAM-based segmentation refinement approach. A paper that proposes new methodology must demonstrate that the method is competitive with or exceeds alternatives—not merely that it beats its own ablation. Without this, the claim of "significant performance improvements" (abstract) is unsubstantiated as a research contribution relative to the state of the art.

### Minor

- **Ambiguous experimental isolation between ADC learning and SAMEnhancer.** Table 3 reports "Network prediction" → "Mobile SAM prediction" → "Merge result" for the SAMEnhancer ablation, but does not state whether the "Network prediction" row comes from the baseline YOLOP or from the ADC-enhanced model. Figure 4's caption suggests the bottom row (SAMEnhancer) is applied on top of ADC learning results, meaning the improvement in Table 3 may conflate ADC learning's effect with SAMEnhancer's effect. Without a column specifying which base model is used, the individual contribution of each component cannot be cleanly isolated.

- **Primary quantitative validation of ADC learning relies mainly on a structured dataset, diverging from the paper's stated motivation.** The paper frames its contribution around unstructured environments (title, abstract, introduction). Yet the main controlled ablation in Table 1 uses BDD100K, a city-road (structured) dataset. The paper states "A similar phenomenon was also observed in the IDD dataset with the same experiment" (line 182) but does not provide IDD-specific numbers separately in the text—only aggregated in a table that is rendered as an image. For a paper whose entire framing rests on unstructured environments, the evidence for the core claim on the target domain is underreported.

- **Missing runtime/computation analysis for SAMEnhancer.** Adding Mobile SAM as an additional inference step on every image incurs a non-trivial computational burden. In the autonomous driving context where real-time constraints matter, the paper should report inference time, FLOPs, or memory overhead with and without SAMEnhancer. The absence of this data makes it difficult to assess the practical deployability of the tool.

- **Limited experimental detail for reproducibility.** Training hyperparameters (learning rate, batch size, optimizer, number of epochs in Phase 1 vs Phase 2), pseudo-label generation specifics (whether they are thresholded, confidence-filtered, or used raw), and morphological kernel sizes for opening/closing operations are not reported.

- **"Degradation" is asserted but not measured quantitatively.** The paper claims alternating training causes "a significant drop in performance on the previous task" (line 66) but never shows the raw magnitude of this drop or how much ADC learning recovers it. The framing as "anti-degradation" would be stronger if the degradation itself were demonstrated with numbers.

### Trivial

- The fusion equation (Eq. 10) is typeset as a binomial-style conditional expression (`\binom{\tilde{Y}}{\hat{Y}}`), which is confusing and does not convey the intended logic (if confidence > 0.9, keep network prediction, else keep SAM prediction). This should be rewritten as a piecewise function or clear conditional.

## Nice-to-Haves

- Comparison to simpler post-processing alternatives (CRF, test-time augmentation, ensembling) would help contextualize SAMEnhancer's value beyond the cost of adding Mobile SAM.
- Reporting the fraction of pixels modified by SAMEnhancer would clarify whether the tool produces substantive changes or only marginal tweaks.
- Separating IDD-only results from BDD100K results in Table 1 would better align evidence with the unstructured-environment framing.

## Removed Points

These points were flagged for removal from the inputs. Treat them with caution.

- **Criticism that "BDD100K already has aligned annotations — the experiment artificially creates a problem that doesn't exist."** Removed: This misunderstands the experimental design. Creating a synthetic non-overlapping split from a fully-annotated dataset is a standard controlled-experiment technique for measuring degradation with known ground truth. The paper explicitly acknowledges that BDD100K is a city-road dataset used for this purpose (line 176).
- **Speculation that "fragmented polygon extraction may produce many small irregular polygons" as a weakness.** Removed: This is a hypothetical failure mode without evidence that it actually occurs in the paper's setting. The paper includes morphological preprocessing specifically to address fragmentation (lines 87–93).
- **Claim that "the 5-class detection taxonomy makes comparison impossible."** Removed: The paper explicitly states the collapsed taxonomy (line 162–163) and uses internal ablation, so the taxonomy is a deliberate design choice for the target domain, not a flaw.
- **Strength Finder's generic strengths** (e.g., "addressed an important problem"): Removed as generic/superficial and lacking specific content.
- Several framing complaints about thin technical novelty: While directionally accurate, these are judgments about positioning rather than specific, verifiable problems with the paper's claims. The core concern (missing baselines) is already captured in Major.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same core concern (self-referential evaluation) that is evident from reading the paper directly.

## Suggestions

1. **Add external baselines.** At minimum: compare to the original YOLOP pipeline (with full overlapping annotations as an upper bound), to a simple self-training baseline, and to a CRF post-processing baseline for segmentation. Compare to any prior SAM-based refinement approach cited in Section 2.3.
2. **Clarify the SAMEnhancer setup in Table 3.** State explicitly whether the "Network prediction" row uses the baseline model or the ADC-enhanced model. If the latter, add a separate row showing SAMEnhancer applied to the baseline model to isolate its independent contribution.
3. **Report IDD and BDD100K results separately** in Table 1, not aggregated, and highlight IDD-specific numbers in the text.
4. **Provide training hyperparameters** (learning rate schedule, batch size, optimizer, epochs per phase) and pseudo-label generation specifics to enable reproducibility.
5. **Report inference time** (ms per image) with and without SAMEnhancer on the same hardware to justify the computational cost.

## Score and Decision

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>