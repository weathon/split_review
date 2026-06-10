## Summary
This paper presents RASO, a foundation model for surgical object recognition trained using a weakly-supervised data pipeline that generates tag-image-text triplets from unannotated surgical lecture videos. The pipeline processes 2,200 procedures to produce 3.6M tag annotations across 2,066 unique surgical tags. The model achieves consistent improvements over baselines in zero-shot settings across four surgical benchmarks (2.9–10.6 mAP gains) and surpasses prior SOTA on CholecT50 supervised action recognition with substantially less training (4 vs. 200+ epochs).

## Strengths
- **Scalable weakly-supervised data generation pipeline**: The pipeline processes 2,200 surgical procedures, producing 901K images and 3.6M tag annotations across 2,066 unique tags — far exceeding existing surgical dataset scales (e.g., EndoVis17/18 with 11 classes). The multi-stage label engine combining biomedical NER (spaCy), SceneGraphParser for verb-noun action triplets, and GPT-4o annotation is a principled design over raw image-text pair training (Section 4.1–4.2, lines 67, 76–80).
- **Consistent zero-shot outperformance across four benchmarks**: RASO achieves gains of 2.9 mAP (CholecT50), 4.5 mAP (Cholec80), 10.6 mAP (RSS), and 7.2 mAP (GraSP). Critically, even without GPT-4o fine-tuning, RASO (w/o FT) outperforms all baselines on three of four datasets (Section 5.2, lines 103, 117), demonstrating that the weakly-supervised pretraining itself transfers genuine domain knowledge.
- **Supervised performance with 50× less training**: On CholecT50 triplet recognition, RASO achieves a mean score of 57.5, surpassing Rendezvous while being fine-tuned for only 4 epochs vs. Rendezvous's 200+ epochs (lines 119–120). This efficiency advantage concretely evidences the value of the pretraining stage.
- **Temporal fusion yields both accuracy and speed gains**: The attention-based temporal-fusion mechanism enables RASO (video) to outperform RASO (image-based) on CholecT50 video recognition with faster inference (Table 4, Figure 4), jointly addressing a practical requirement for surgical applications.

## Weaknesses

### Fatal
None.

### Major
- **Zero-shot evaluation conflates in-domain pretraining data with method**: RASO is pretrained on 901K in-domain surgical images from WebSurg, while the baselines (CLIP, BiomedCLIP, PubMedCLIP) were trained on general or biomedical data — not surgical lecture videos. Even SurgVLP, the only surgical-domain baseline, does not report training at comparable scale. The observed gains cannot be attributed to the RASO architecture or tag-image-text training framework specifically, because the critical comparison is missing: what does the same base architecture (RAM/Swin-Transformer + CLIP text encoder) achieve when pretrained on the *same* WebSurg data *without* RASO's specific modifications? Without this controlled ablation, the paper's core methodological claims (temporal fusion, tag-image-text training) are confounded with the simple benefit of large-scale in-domain pretraining data. The paper still demonstrates that the overall system works, but the attribution of *why* it works is ambiguous.

### Minor
- **No error bars or variance reported**: None of the tables include standard deviations or confidence intervals. For improvements as small as 2.9 mAP (CholecT50) and 4.5 mAP (Cholec80), variance could affect the reliability of the reported ranking.
- **No analysis of tag quality or noise**: The pipeline generates 3.6M tag annotations, but there is no human evaluation, precision/recall analysis, or sample-level correctness check of the NER, SceneGraphParser, or GPT-4o outputs on surgical transcripts. A small-scale validation study would substantially strengthen this contribution.
- **No ablation of individual data sources**: The pipeline combines NER tags, SceneGraphParser action triplets, and GPT-4o annotations, but their relative contributions to final performance are not quantified.
- **No conclusion/discussion section**: The paper lacks a discussion of limitations, failure cases, data biases (e.g., the training data is concentrated on laparoscopic cholecystectomy from WebSurg), or deployment considerations.
- **Supervised video recognition comparison is internal only**: Table 4 compares RASO (video) vs. RASO (image-based). While this validates the temporal fusion mechanism, an external video recognition baseline would better position the result.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment training the same base architecture on the same WebSurg data with and without RASO-specific modifications to separate data-driven from method-driven gains.
- Analysis of GPT-4o API cost for the 120K-image annotation step.
- Explicit tag-coverage analysis between the 2,066-tag vocabulary and test-set labels to characterize the open-set capability more precisely.

## Removed Points
These points were flagged but are removed as they reflect parser issues, misunderstandings, or noise:
- **Architecture section (Section 3.1) appears empty in extracted text.** This is a PDF parsing artifact. The instruction specifies that formatting artifacts from extraction are not paper problems. The paper references the architecture in the introduction and Section 3.2, and the original PDF likely contained descriptive content (text or figure) that the parser failed to capture. Not penalized.
- **Tag overlap undermining zero-shot claim.** Zero-shot evaluation in vision-language models routinely evaluates on categories present in the pretraining vocabulary (e.g., CLIP on ImageNet). The model has not seen the specific image-label pairs from test benchmarks. This is not a weakness.
- **Segmentation framing mismatch.** The paper explicitly positions RASO as the recognition component needed to enable grounded segmentation (line 18–20). This is proper motivation, not a mismatch.
- **SurgVLP noise comparison.** The paper's pipeline filters non-visual content via GPT-3.5 and extracts structured tags rather than using raw transcripts — a principled noise reduction strategy. The paper already addresses this.
- **Supervised Rendezvous comparison conflating pretraining with architecture.** The paper transparently discloses this limitation (line 119). The result demonstrates the value of pretraining, which is a stated contribution.
- **"Supervised Video Recognition" section heading implying external baselines.** The section is clearly presented as a comparison of two RASO variants to validate the temporal fusion mechanism; the framing is not misleading when read in context.

## Novel Insights
None beyond the paper's own contributions. The reviews surface the standard methodological concern about data vs. method attribution but do not reveal any insight about the paper that the paper itself does not convey.

## Suggestions
1. Add a controlled experiment: train the same base architecture on the same WebSurg data with and without RASO-specific modifications to disentangle data-driven from method-driven gains.
2. Report standard deviations over multiple runs for all main results.
3. Include a small-scale human evaluation (e.g., 200–500 random tag annotations) to validate tag quality from the generation pipeline.
4. Add ablation studies quantifying the contribution of each label source (NER, SceneGraphParser, GPT-4o).
5. Add a conclusion/discussion section addressing limitations, failure modes, and the concentration of training data on laparoscopic cholecystectomy.
6. Include at least one external video recognition baseline for the supervised video comparison.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>