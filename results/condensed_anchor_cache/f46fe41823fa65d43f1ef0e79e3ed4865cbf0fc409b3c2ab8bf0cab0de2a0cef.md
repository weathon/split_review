- Decision: Accept
- Scores: 6, 6, 6, 5

## Merged Review

### Summary

The reviewers acknowledge that InstructDET introduces a data-centric approach for referring object detection (ROD) by leveraging foundation models (LLaVA, LLaMA, CLIP) to generate diverse instructions from images with bounding boxes, creating the InDET dataset. The dataset is claimed to be the largest real-world REC dataset and covers many scenarios including multi-object instructions. A simple DROD model trained on InDET outperforms prior methods on both standard REC benchmarks and the InDET test set. While the idea of enriching dataset via foundation models is seen as interesting and novel, reviewers raise significant concerns about dataset quality, reproducibility, experimental fairness, and missing comparisons.

### Strengths

- InDET is the largest real-world REC dataset and covers many scenarios, including multiple object instructions (R1).
- The DROD model is simple yet effective, and its strong performance proves the quality of InDET (R1).
- The paper proposes an interesting research direction: improving ROD by enriching datasets via foundation models rather than better model design (R2).
- The CLIP-based verification step to remove VLM hallucinations is novel and interesting (R2, R3).
- The method is scalable; performance can improve with more bbox data (R3).
- The model trained on the curated dataset outperforms prior arts by a large margin, even with the same network architecture (R2).
- The resulting dataset may be a good resource for future visual grounding research (R4).

### Weaknesses

- **Reproducibility & insufficient detail** (R2, R4): The data generation procedure is described at an overly abstract level. Critical details are missing, e.g., exact prompts and their generation procedure (number of queries, services used, costs), the dataset and training setting used to fine-tune LLaVA, and how the expression verification and LLaMA diversification steps work (R2). The statement “initializing LLaVA with minigpt4 weights” is unclear and potentially incorrect because LLaVA finetunes the entire LLM, whereas minigpt4 only finetunes a linear layer and the architectures differ (R4).
- **Terminology confusion** (R2): The naming of “pathways” and “dropout” are confusing – “pathways” is easily confused with network parallel branches, and “dropout” with a regularization method. The distinction between “single modality” and “multi modality” pathways is unclear: both use LLaVA with image + text inputs; it is also unclear why the single modality pathway uses an out-of-box LLaVA while the multi-modality pathway requires a finetuned version.
- **Missing experiments** (R1, R3, R4):
  - Previous REC models should be trained on InDET and evaluated on RefCOCO/+/g to further validate the dataset (R1).
  - Table 2 fairness is unclear: it is not stated whether the compared methods (MDETR, G-DINO, UNINEXT) all used the same training images and bounding boxes; without that, performance differences may not be solely due to diversified instructions (R3).
  - The paper should also compare against current state-of-the-art methods like PolyFormer (R4).
  - An experiment to investigate the saturation point of scalability is needed, e.g., using SAM to generate bounding boxes for many web images and then scaling the proposed pipeline to analyze performance vs. dataset size (R3).
- **Dataset quality concerns** (R4, echoed by R2): The single-modality pathway uses LLAMA (not instruction-tuned) and the multi-modality pathway uses LLaVA; both have known problems (hallucinations, inability to describe small objects). This raises questions about the accuracy and reliability of generated instructions, especially in complex or fine-grained scenarios. A minority reviewer (R4) was more critical on this point, noting the dataset’s quality may be questionable and that the experimental validation is insufficient to demonstrate practical utility.
- **Language errors** (R2): The submission contains many grammatical mistakes and strange word choices, making it harder to follow. It could benefit from proofreading.