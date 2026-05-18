- Decision: Reject
- Scores: 3, 3, 3, 3

## Merged Review

### Summary
The paper analyzes why direct fine-tuning of Stable Diffusion on specialized datasets yields poor text-image alignment and alignment drift. To address this, it proposes a contrastive learning approach that refines text feature representations during generation, improving alignment. Experiments are conducted on CUB and Oxford Flowers datasets.

### Strengths
- **Clear motivation and intuitive idea:** The paper is well-written, starting from a phenomenon analysis and proposing a simple, direct method to improve fine-tuning via supervision in feature space (Reviewer 1, 2, 4).
- **Interesting CLIP analysis:** The analysis of CLIP characterization and its impact on generated results is persuasive and guides future research (Reviewer 2).
- **Effectiveness on small datasets:** The method is validated on two fine-grained datasets, showing improved generation performance (Reviewer 2, 3).

### Weaknesses
- **Limited novelty and well-known issues:** The text-image alignment drift is essentially the real-to-synthetic domain gap, which is well-known. The paper treats this as a new finding without acknowledging existing domain adaptation approaches (e.g., Gal et al. “StyleGAN-NADA: CLIP-Guided Domain Adaptation of Image Generators”, SIGGRAPH 2022; Kim et al. “DiffusionCLIP: Text-Guided Diffusion Models for Robust Image Manipulation”, CVPR 2022). A line of similar works is not compared or contrasted (Reviewer 1).
- **Insufficient experiments and validation:**
    * Experiments are only on two small, fine-grained datasets. Validation on larger datasets (e.g., ood101, SUN397, DF-20M mini, Caltech101, CUB-200-2011, ArtBench-10, Oxford Flowers, Stanford Cars) is missing, making it hard to demonstrate broad effectiveness (Reviewer 2, 4).
    * Only two types of birds are shown in qualitative analysis; more categories and visualizations are needed to judge effectiveness (Reviewer 2).
    * No experiments on abstract or artistic datasets (anime, character portraits). Since the method relies on CLIP (which leans toward real photos), improvement on artistic creation is questionable (Reviewer 4).
- **Incomplete ablation and analysis:**
    * The paper designs category-based and sample-based loss functions but only validates the category-based version (Reviewer 2).
    * Lack of ablation at sample-level, category-level generation, and analysis of results (Reviewer 1, 2).
    * Does not discuss or compare with related work proposing similar auxiliary losses, e.g., image-text matching guidance in Li et al. “Upainting: Unified text-to-image diffusion generation with cross-modal guidance” (arXiv 2022) (Reviewer 3).
- **Evaluation metric concerns:**
    * Using only FID and Accuracy is insufficient. Metrics like CLIP Similarity should be added (Reviewer 2).
    * Image-text similarity from CLIP cannot faithfully convey fine-grained alignment (number, color, object relationships); optimizing this contrastive loss may not guarantee good generation results (Reviewer 3).
    * Real-world image-text pairs are noisy and intrinsically mismatched; optimizing contrastive loss may not lead to high-quality images (Reviewer 3).
- **Missing explanations and figure issues:**
    * Figure 2(b) lacks a legend—solid/dash lines and colors are not explained (Reviewer 1, 2, 3).
    * No definition of KDE in Figure 4 (Reviewer 2, 3).
    * [Reviewer 2 asks:] Why not use BLIP to generate captions for non-caption data?
    * [Reviewer 1 notes:] The phrasing “improving image-text alignment” and “reducing image-text alignment drift” is essentially the same—writing needs improvement.