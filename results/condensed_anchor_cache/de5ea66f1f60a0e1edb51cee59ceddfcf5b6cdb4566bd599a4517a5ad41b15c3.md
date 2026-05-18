- Decision: Reject
- Scores: 6, 5, 6, 5

## Merged Review

### Summary
The paper proposes HATFormer, a transformer-based encoder-decoder architecture (building on TrOCR) for historical Arabic handwritten text recognition. It introduces a custom image processor (BlockProcessor) to adapt elongated text lines for ViT input, an Arabic BBPE tokenizer, and a training pipeline leveraging synthetic data. The model achieves CER 8.6% on Muharaf (51% improvement over prior SOTA) and CER 4.2% on a private non-historical dataset. The code/model will be released. All four reviewers acknowledge the strong performance, but raise concerns about novelty, ablation inconsistencies, insufficient analysis, and limited experimental details.

### Strengths
- **Strong empirical performance**: Significant improvement on Muharaf dataset (CER from 17.6% to 8.6%, outperforming best baseline by 51%). Also obtains SOTA on one dataset and competitive results on two others. (Reviewers 1,2,3,4)
- **Novel preprocessing (BlockProcessor)**: Line-warping technique to fit elongated text lines into ViT’s square format. Some reviewers find it innovative and potentially applicable to other scripts. (Reviewers 1,2) However, one reviewer notes that similar block processing approaches exist (e.g., Fuyu-8B, Fadeeva et al.) and that according to Table 3 the BlockProcessor actually decreases performance (Reviewer 4). (Disagreement preserved.)
- **Pre-training strategy**: Extensive pre-training on synthetic Arabic data, critical given limited real data; English pre-training still beneficial (Table 3). (Reviewer 1) However, details of this pre-training are very limited (Reviewer 2).
- **Open-source**: Code and dataset will be released; model link provided. (Reviewers 1,4)
- **Clear writing**: Approach appears easy to reproduce. (Reviewer 4)

### Weaknesses
- **Ablation study inconsistencies**: Removal of block processing leads to significant performance degradation (suggesting benefit), but removal of custom BBPE improves results almost to original model level – counterintuitive and requires investigation (bugs, unintended interactions). (Reviewer 1) Contrary observation: according to Table 3, BlockProcessor actually decreases model performance (Reviewer 4). These contradictory findings need clarification.
- **Limited novelty**: Main novelties (BlockProcessor, Arabic BBPE tokenizer) are already studied in prior works (e.g., Fuyu-8B, Fadeeva et al. for block processing; BPE tokenizer standard for VLMs). The core approach is two-stage fine-tuning of an existing model, which may be insufficient contribution. (Reviewer 4) Missing comparisons to similar block-processing works (Pack’n’Patch, Pix2Struct) and to full-page recognition methods (e.g., DAN by Coquenet et al.). (Reviewers 1,4)
- **BlockProcessor design issues**: Horizontally flipping text-line images before warping does not adapt to Arabic-specific characteristics; changing ViT patch order due to flipping may be problematic given pre-trained English weights; also poses problems with mixed Arabic/Latin text. (Reviewer 1)
- **Generalisation and dataset coverage**: Model not trained on all available datasets to assess true generalisation. (Reviewer 1) Only one existing method compared on Muharaf dataset. (Reviewer 2) Dataset descriptions insufficient: readers cannot distinguish historical vs non-historical; no detailed info about synthetic generated dataset; OpenHART (used in experiments) not mentioned in dataset section. (Reviewers 1,3) Also, incorrect claim about RIMES: number of handwritten pages is not 12500, only a fraction is fully handwritten. (Reviewer 1)
- **Insufficient analysis of intrinsic challenges**: Analysis of three challenges (cursive, diacritics, etc.) in appendix is not enough; need comprehensive analysis showing how the method overcomes them. (Reviewer 3) No analysis of limitations or flaws shown in experimental results. (Reviewer 3)
- **Line-recognition focus**: Title does not reflect that the method works on extracted lines, not full pages; this is part of a larger document analysis system and may introduce errors in subsystems. (Reviewer 3)
- **Missing experimental details**: Pre-training procedure with synthetic data very limited. (Reviewer 2) Need to clarify if retraining of baseline (Saeed 2024) also used synthetic printed data. (Reviewer 2 question)