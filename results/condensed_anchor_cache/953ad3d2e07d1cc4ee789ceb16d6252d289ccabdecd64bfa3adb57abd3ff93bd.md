- Decision: Accept
- Scores: 6, 6, 8, 6

## Merged Review

### Summary
The paper proposes SiD-LSG (Guided Score Identity Distillation with Long-Short Guidance) for data‑free one‑step text‑to‑image generation. It adapts Score identity Distillation (SiD) to Stable Diffusion (SD1.5, SD2.1) by incorporating Long and Short Classifier‑Free Guidance (LSG) strategies. The method optimizes a model‑based explicit score matching loss with a score‑identity approximation and LSG. On the COCO‑2014 validation set it achieves a record data‑free FID of 8.15 (SD1.5) and 9.52 (SD2.1) while maintaining competitive CLIP scores.

### Strengths
- **Adaptation of SiD to text‑to‑image models**: SiD is successfully extended to pretrained DDPM‑based t2i models (SD1.5, SD2.1), enabling one‑step generation. (Reviewers 2,3,4)
- **Two explicit CFG strategies**: The paper introduces *long CFG* (applied to the teacher model with guidance scale τ>1, improving text‑adherence) and *short CFG* (applied to the fake score network with τ∈(0,1), improving FID). These provide a clear mechanism to balance FID and CLIP scores. (Reviewer 1)
- **State‑of‑the‑art data‑free results**: The method achieves the best reported FID under the data‑free setting: 8.15 for SD1.5 and 9.52 for SD2.1, with competitive CLIP scores. (Reviewers 1,2,4)
- **Comprehensive experimental evaluation**: The paper includes extensive experiments, ablations, and comparisons. (Reviewers 2,3)
- **Well‑written with solid foundation**: The paper is clearly written, the theoretical/mathematical background is sound, and the method is presented as novel and important. (Reviewer 3 – more positive, rated 8)
- **Inference efficiency**: Reducing generation to a single step significantly accelerates image synthesis. (Reviewer 4)

### Weaknesses
- **Unexplored trade‑off between FID and CLIP**: No single τ value optimally balances both metrics (Tables 1, 2). The paper does not investigate the intrinsic reasons for this trade‑off (e.g., impact on feature space or alignment of the student score function under varying guidance). (Reviewer 1)
- **Missing intuitive ablation to isolate contributions**: Tables 1 and 2 lack separate results for SiD with (i) short CFG only, (ii) long CFG only, (iii) CFG only, and (iv) original SiD under the same τ. This makes it difficult to assess the individual and synergistic effects of the two guidance strategies. A baseline with a single fixed τ is also omitted. (Reviewer 1)
- **Incorrect claim about first incorporation of CFG into fake score network training**: The paper states (L268‑269) it is “the first to incorporate CFG into the training of the fake score network,” but SwiftBrush already uses CFG 4.5 for both teachers (see their Implementation Details, Section 4.1). (Reviewer 2)
- **Connection between short guidance and long‑and‑short guidance unclear**: The short guidance setting (κ2=κ3<1) does not directly extend to the long‑and‑short setting (κ2=κ3>1); the relationship is not explained. (Reviewer 2)
- **Long and short guidance scheme is simple**: The configuration (κ1=κ2=κ3=κ4=1.5) applies the same CFG to both teachers, which SwiftBrush already did. (Reviewer 2)
- **Missing comparisons with recent methods**: SwiftBrush v2 and DMD2 are not mentioned or compared. (Reviewer 2)
- **Expensive training protocol**: Batch size 512 with 64 gradient accumulation steps on H100 (80G) FP32; backpropagation through score networks forces a per‑GPU batch size of 1 on the same hardware. Generating synthetic “false” images for training and requiring both conditional/unconditional CFG passes further increases computational cost, reducing practicality for resource‑limited researchers. (Reviewers 2,4)
- **Poor figure readability**: Figures 3, 4, 6, and 9 use the same color for FID and CLIP curves with only a small transparency difference, making them hard to differentiate. (Reviewer 2)
- **Fig. 6 incorrectly placed in Appendix**: The figure discussed in Section 3.2 is relegated to the Appendix and should be moved to the main text. (Reviewer 2)
- **Missing critical comparison with SwiftBrush‑like CFG**: The paper does not provide results for the configuration κ1=1, κ2=κ3>1, with κ4 either 1 or equal to κ2, which is needed to isolate the effect of the proposed CFG scheme. (Reviewer 2)
- **Unclear definitions of strategies in main text**: The long/short/long‑and‑short strategies are not clearly defined in the main paper; the discussion should be moved from the appendix to improve clarity. (Reviewer 2)
- **Lack of FP16 performance analysis**: The paper mentions FP16 training efficiency but does not provide key results using FP16 or analyze the performance drop compared to FP32. (Reviewer 2)
- **Limited novelty**: The core contribution is the adaptation of the existing SiD framework to DDPM‑based t2i models (SD1.5, SD2.1) and the addition of CFG variants. (Reviewer 3; also implied by Reviewers 1,2,4)
- **Distillation on relatively old networks**: The experiments are performed only on SD1.5 and SD2.1, which are outdated. (Reviewer 3)
- **Data‑free limitation**: Not using real training data may hinder the model’s ability to capture fine‑grained details and achieve photorealism compared to methods that leverage real data. (Reviewer 4)
- **Unclear applicability to models without CFG**: For models like FLUX that use word embedding instead of CFG for inference, it is not clear whether the proposed guidance strategies apply. (Reviewer 4, question)
- **Missing investigation for v‑prediction networks**: The paper does not address whether the method generalizes to v‑prediction models or how the theory would need to be altered. (Reviewer 3, question)