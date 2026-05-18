I now have a thorough understanding of the paper and all reviewer claims. Let me produce the final consolidated review.

## Summary

This paper introduces CLIBD, a CLIP-style contrastive learning framework that aligns images, DNA barcodes, and taxonomic text labels in a shared embedding space for fine-grained insect species classification. The key idea is using DNA barcodes—which can be obtained at scale without expert taxonomic annotation—as an alignment signal for image representations, enabling zero-shot classification and cross-modal retrieval (image-to-DNA) for both seen and unseen species. Experiments on BIOSCAN-1M and INSECT datasets show that the image+DNA alignment model substantially improves species-level classification accuracy compared to no-alignment baselines and outperforms BioCLIP and Bayesian zero-shot learning approaches.

## Strengths

1. **First contrastive-learning fusion of images and DNA barcodes for taxonomic classification.** Prior multimodal approaches for biodiversity (e.g., BioCLIP) only align images with text labels, while existing DNA+image methods (e.g., BZSL) rely on Bayesian modeling rather than end-to-end contrastive learning. The paper demonstrates that CLIP-style alignment across image, DNA, and text modalities produces a useful shared embedding space (lines 30–35, 80–84).

2. **DNA serves as a more effective alignment target than taxonomic labels alone.** The paper systematically shows (line 187) that the image+DNA (I+D) model consistently outperforms the image+text (I+T) model across taxonomic ranks. This is attributed to the scarcity of species-level labels (~3.36% of pretraining data) versus the rich taxonomic signal carried by DNA barcodes without requiring expert annotation. This is a concrete advantage over text-based methods like BioCLIP.

3. **Enables zero-shot cross-modal retrieval (image→DNA).** The paper demonstrates that image queries can retrieve correct DNA barcodes for unseen species (lines 189–191), which is practically important — it allows classification using DNA reference sets when no labeled images exist for a species. While cross-modal accuracy is lower than intra-modal, this capability is novel and supported by qualitative retrieval examples (Figure 4).

4. **Practical two-stage classifier (IS+DU) outperforms more complex Bayesian methods.** The paper develops a seen/unseen detection strategy with modality-specific retrieval and shows (lines 256–257) that it achieves higher unseen species accuracy than BZSL, despite BZSL's additional complexity. This provides a deployable solution for real-world scenarios.

## Weaknesses

### Fatal
None.

### Major

1. **The abstract's "over 8%" improvement claim is not explicitly grounded in the experimental prose.** The abstract states: "Our method surpasses previous single-modality approaches in accuracy by over 8% on zero-shot learning tasks." However, in the body of the paper, the 8% figure is never explicitly tied to a specific experimental comparison. The large numerical improvements cited in the prose (e.g., 6.27% → 52% species-level macro H.M. accuracy, line 185) are against a "no alignment" baseline (raw ViT-B without any fine-tuning on the target domain), not against "previous single-modality approaches." The BioCLIP comparison (Table 4, referenced at line 207) is described only qualitatively as "consistently outperforms" without stating the exact margin. The abstract's central quantitative claim therefore floats without a clear reference point. This is a presentation/verification issue that the authors must fix — either explicitly connect the 8% figure to a specific table/experiment or replace it with the precise, substantiated number.

### Minor

2. **The "no alignment" baseline used for the headline large improvements is weak.** The paper reports that species-level image-to-image retrieval jumps from 6.27% to 52% after alignment (line 185). The "before" baseline is a ViT-B pretrained on ImageNet with no fine-tuning on the insect domain. A more informative unimodal baseline would be a ViT-B fine-tuned on the BIOSCAN-1M training set with a supervised loss (e.g., cross-entropy on seen species). Such a baseline would likely achieve substantially higher than 6.27%, and the relative gain from multimodal alignment would shrink. The paper does compare against BioCLIP (a strong domain-specific baseline), which partially mitigates this concern, but a supervised fine-tuned image-only model would isolate whether the improvement comes from multimodal alignment or simply from any fine-tuning on the target domain.

3. **No statistical reliability information.** Results are reported as single point estimates with no error bars, confidence intervals, or multiple random seeds (line 173 describes training for "50 epochs with batch size 2000" but only one run). While the improvement margins are large (6% → 52%), making it unlikely that noise alone explains the gains, adding at least two seeds and reporting the range would strengthen the paper's rigor and is standard practice for contrastive learning experiments.

4. **Data split description is initially ambiguous.** Line 153 says "Records for well-represented species... are partitioned at an 80/20 ratio into seen and unseen," which could be read as splitting records within the same species — violating the zero-shot setting. Line 155 clarifies that "unseen species are mutually exclusive... and do not overlap with seen species," but this clarification should come before, not after, the potentially confusing statement. The exposition should be unambiguous from the start (e.g., "Species with ≥9 records are randomly split: 80% assigned to the seen set and 20% to the unseen set").

### Trivial
None of note.

## Nice-to-Haves

- **Stratify retrieval accuracy by key set size.** The paper discusses (line 220 and Figure 5) how performance depends on the number of records in the key set, but doesn't report accuracy stratified by reference set size or control for it. This would increase transparency.
- **Brief discussion of inference scalability.** The method requires storing and searching a large database of image and DNA embeddings. A short discussion of how this scales to larger datasets like BIOSCAN-5M (5 million records) would help practitioners assess deployability.
- **Quantify the improvement over BioCLIP explicitly in the prose** (e.g., "CLIBD I+D+T achieves X% species-level accuracy vs. BioCLIP's Y%"), rather than solely in the table.

## Removed Points

- **"The 8% claim is unsupported / cannot be located"** — kept as Major #1 but downgraded from "structural issue that undermines the entire narrative" to a presentation/verification issue. The paper's experimental evidence otherwise supports the core contribution; the claim may well be backed by numbers in Table 4 (which is not visible in the extracted text), but the prose should explicitly anchor it.
- **"Attention rollout not connected to quantitative evaluation"** — the critic's observation is correct but this is a minor point. Attention analysis is qualitative and supplementary. Moved to implicit acknowledgment in Strengths (it's a nice addition but not central evidence).
- **"Novelty concerns — straightforward combination of existing ideas"** — the critic's own admission that "novelty-through-application can be sufficient" undermines this as a weakness. The paper's contribution is the demonstrated effectiveness of DNA as a contrastive alignment target, which is genuinely novel in this domain. Removed.
- **"Missing related works"** — per instructions, I cannot verify existence of missing references. Removed.
- **"The paper should also cover Y / additional tasks"** — demands for broader scope beyond the paper's stated direction are scope creep. Removed.

## Novel Insights

The reviews collectively surface an interesting observation: the paper's strongest evidence is not the single "8%" number from the abstract but rather the systematic ablation showing that DNA outperforms text as an alignment target (I+D > I+T consistently across ranks), combined with the BioCLIP comparison showing that even the I+T-only variant of CLIBD outperforms BioCLIP on insect data. This suggests that domain-specific pretraining (even with just images and taxonomic labels) matters more than the broad multi-kingdom pretraining of BioCLIP — and DNA goes further still. The key takeaway is not "CLIBD is 8% better" but "DNA barcodes provide a self-supervised taxonomic signal that bypasses the need for expert labels, and contrastive learning can exploit this signal effectively." The paper would be strengthened by reframing its contribution around this insight rather than a specific percentage improvement.

## Suggestions

1. **Ground the abstract's quantitative claim explicitly.** Either (a) directly reference the specific comparison that yields the "over 8%" figure and point to the corresponding table/experiment, or (b) replace the number with a precise, substantiated figure tied to a specific comparison (e.g., the BioCLIP gap, or a supervised fine-tuned image-only baseline gap).

2. **Add a supervised unimodal baseline.** Compare the I+D model against a ViT-B fine-tuned on BIOSCAN-1M seen species with cross-entropy loss (image-only). This would isolate the benefit of multimodal alignment from the benefit of domain fine-tuning, and would make the contribution significantly stronger.

3. **Add at least two random seeds** and report the range or standard deviation for the main test-set accuracy numbers.

4. **Clarify the data split description** by leading with the unambiguous species-level split (e.g., "Species with ≥9 records are split 80/20 into seen/unseen; all records of a seen species go to training") before discussing allocation details.

5. **Move the BioCLIP comparison margin into the prose.** Explicitly state in the text what the accuracy gap is (e.g., "CLIBD I+D+T achieves X% species-level accuracy vs. BioCLIP's Y%") rather than only in the table.

6. **Reframe the abstract's contribution** around the insight that DNA provides a scalable, label-free alignment signal for fine-grained visual classification, rather than leading with a specific percentage improvement that is hard to verify.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>