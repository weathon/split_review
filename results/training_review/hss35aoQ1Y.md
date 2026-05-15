Now I have all the information needed to synthesize the final review.

## Summary

This paper proposes InstructDET, a data-centric pipeline that leverages foundation models (LLaVA, LLaMA) to automatically generate diverse referring expressions for object detection, constructing the InDET dataset (3.6M instructions across 120.6K images). The instructions cover single-object descriptions (via global-text and local-visual pipelines) and multi-object descriptions (via semantic clustering and LLM summarization). The authors train a DETR-based ROD model (DROD) on InDET and report improvements on the InDET test set and modest gains on standard RefCOCO/g/+ benchmarks.

## Strengths

- **Systematic data generation pipeline with two complementary strategies.** The global prompt pipeline (LLaVA → LLaMA with in-context examples) and local prompt pipeline (visually-prompted LLaVA) are thoughtfully designed to produce different types of expressions — relational from global, visually detailed from local — and combining them is a principled approach to instruction diversity. The CLIP-based filtering with local-enhancement scoring (Eq. 1) is a reasonable solution to the known global-bias problem.

- **Multi-object expression generation via semantic clustering.** The approach of concatenating single-object expressions, clustering via BERT+DBSCAN, and summarizing commonalities with LLaMA is a genuinely novel method for generating G5–G6 instructions (spliced and commonality descriptions) — instruction types that are nearly absent in prior REC datasets. This fills a real gap.

- **Controlled evidence across architectures that InDET improves logic reasoning (Figure 6a).** Training MDETR, G-DINO, and UNINEXT on InDET yields better performance on a 2K "logical reasoning" subset than training the same models on RefCOCO or Flickr. This experiment controls for model architecture, providing cross-architecture evidence that InDET data is beneficial.

- **Dataset analysis and taxonomy (G1–G6).** The 6-group guideline is a useful framework for characterizing instruction types, and the distribution analysis in Figure 3(c) convincingly shows that InDET covers a broader range of expression types than RefCOCO or Flickr, which are concentrated in G1–G2.

## Weaknesses

### Fatal
None.

### Major

- **Headline comparison on InDET test set (Table 1) is misleading due to asymmetric training.** The paper reports DROD at 62.24 AP vs. UNINEXT at 43.37 AP on the InDET test set, but the evidence strongly indicates that MDETR, G-DINO, and UNINEXT are evaluated zero-shot (not fine-tuned on InDET training data), while DROD is trained on InDET. The paper does not state this explicitly, which makes the 20-point gap appear to be a model improvement when it is primarily a consequence of training-data exposure. This comparison inflates the apparent contribution and undercuts the central quantitative claim. The paper should fine-tune baselines on InDET for a fair comparison, or clearly label that the comparison is zero-shot.

- **Gains on standard REC benchmarks (Table 2) are small and confounded by data scale.** DROD achieves 88.92/90.86/85.57 on RefCOCO vs. UNINEXT's 87.64/90.35/83.49 — improvements of +1.28/+0.51/+2.08 on a highly saturated benchmark. More critically, DROD trains on InDET (3.6M instructions) while the baseline trains on RefCOCO (~100K expressions). The paper does not control for training set size (e.g., training DROD on a random subset of InDET matched to RefCOCO's size), so it is impossible to attribute the improvement to instruction *diversity* rather than simply having *more* training data. This confound also applies to the logical reasoning experiment (Figure 6a).

- **The logical reasoning experiment (Figure 6a) does not control for data volume.** The paper shows MDETR/G-DINO/UNINEXT trained on InDET outperform the same models trained on RefCOCO or Flickr on a 2K logic-reasoning subset. But InDET is orders of magnitude larger than those datasets. Without controlling for data quantity (e.g., comparing against a matched-size random subset of InDET, or showing that the logic-reasoning instructions in InDET specifically drive the gain), the conclusion that InDET "improves logic reasoning" is not causally supported — the improvement could be from scale alone.

### Minor

- **The shuffled-instruction metric is a reasonable heuristic but unvalidated.** The paper interprets a larger performance drop on word-shuffled instructions as evidence of better comprehension, on the grounds that a model which understands compositional meaning should be disrupted by shuffling while a keyword matcher would be robust. This logic is defensible — it is not "backwards" as one reviewer claimed — but the metric has not been validated against any ground-truth comprehension benchmark. The observed drops could also reflect differential sensitivity to distribution shift (shuffled text being out-of-distribution for all models). Controlled semantic perturbations (negation, synonym substitution, distractor insertion) would strengthen this analysis.

- **Expression filtering pipeline lacks sensitivity analysis.** The CLIP-based filtering score $S_f = S_l - \alpha_1 S_g$ uses a dynamic threshold, but the paper does not ablate the effect of filtering on downstream ROD performance, report how many expressions are discarded, or analyze sensitivity to $\alpha_1$. These details may be in the appendix (which was stripped during parsing), but they are important for understanding the pipeline's contribution.

- **LLaMA-based instruction-to-group assignment is unvalidated.** Section 4 assigns each instruction to a G1–G6 group using LLaMA with in-context examples, but the paper provides no accuracy analysis or human validation of these assignments. The group-level results in Table 1 rely on this assignment being correct, so noise in the grouping could affect the per-group conclusions.

### Trivial
None.

## Nice-to-Haves

- Report variance or confidence intervals for the main results, or at minimum note that single-run evaluation is standard for this benchmark setting.
- Evaluate on images from distributions beyond COCO/Flickr/O365 (e.g., LVIS) to test generalization to unseen domains.
- Show examples of expressions that were filtered out by the CLIP filter to build intuition about its behavior.

## Removed Points

These points from the reviews were removed with brief justification:

- **"Evaluation on InDET test set is circular"** — softened to "misleading" since the paper does have a standard train/test split; the issue is an unfair (asymmetric) comparison, not circularity.
- **"Shuffled metric is methodologically unsound / backwards"** — removed as factually incorrect about the paper's logic. The paper's reasoning (keyword matchers are robust to shuffling, composition-understanding models are not) is standard and defensible; the real concern is lack of validation, which is kept as a minor weakness.
- **"DROD model conflates architecture contribution with data contribution"** — strawman; the paper explicitly calls it a "conventional ROD model" (Section 5) and does not claim architectural novelty.
- **"Missing training hyperparameters, inference threshold, ablation studies"** — the paper states these are in the appendix (Sec. supp-model, supp-ablation), which was stripped during parsing.
- **"No user study"** — scope creep for a data-generation paper.
- **"The paper does not report variance or statistical significance"** — moved to Nice-to-Haves; single-run evaluation is standard for this benchmark.
- **"Largest real-world REC dataset is misleading"** — the paper correctly states the dataset contains *images* from existing sources with *new* instructions; this is standard practice and not misleading.
- **"Expression filtering pipeline is ad-hoc"** — subjective opinion; the paper provides clear motivation for the design.
- **"No validation of instruction quality via human evaluation"** — this is a useful suggestion but not a methodological flaw; moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fine-tune baselines on InDET for Table 1.** This is the single most important fix. Run UNINEXT (and ideally MDETR, G-DINO) fine-tuned on InDET training data and compare on the InDET test set. This would reveal whether DROD's advantage is due to architecture/training recipe or simply having seen InDET. Even if fine-tuned baselines approach DROD, it would validate the data-centric contribution.

2. **Control for training set size.** Train DROD on a random subset of InDET matched to the size of RefCOCO (or UNINEXT's pretraining data) and compare to the full-dataset version. This is necessary to separate the effect of instruction diversity from data scale.

3. **Validate the shuffled-instruction metric** with controlled semantic perturbations (e.g., synonym substitution, negation, distractor insertion) that have unambiguous expected effects on a model that truly "comprehends."

4. **Add human validation** of the LLaMA-based instruction-to-group assignment and a small human evaluation of generated instruction quality (naturalness, correctness).

5. **Report the filtering rate and ablation** of the CLIP filter: how many expressions are discarded, and how does downstream ROD performance change without filtering?

## Score and Decision

**Originality:** Good — the data generation pipeline combining two complementary foundation model strategies with CLIP filtering is novel.  
**Importance of research question:** Moderately important — making ROD more practical via diverse instructions is a worthwhile goal.  
**Claims support:** Insufficient in parts — the headline comparison is misleading, and the scale confound weakens the causal claims about diversity.  
**Soundness of experiments:** Adequate but with notable gaps — the fair comparisons (Table 2, Figure 6a) provide some support, but confounds remain.  
**Clarity of writing:** Good — the paper is well-organized and the pipeline is clearly described.  
**Value to community:** Moderate — InDET could be a useful resource, and the data generation methodology is reusable.

The paper presents a genuine contribution in its data generation pipeline and the InDET dataset. However, the evaluation oversells the results via an asymmetric comparison (Table 1) and fails to disentangle data diversity from data scale. The paper would benefit from major revisions to its evaluation protocol, but its core methodological contribution is sound.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>