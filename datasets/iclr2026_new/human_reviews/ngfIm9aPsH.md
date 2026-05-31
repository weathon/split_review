## Human Reviewer 1

### Summary
This paper proposes an object fidelity diffusion method, which extends the layout-to-image paradigm into the remote sensing sense. This method combines many existing modules to achieve controllable image generation.

### Strengths
1. This is a layout-to-image generation method for the remote sensing field.
2. The proposed method integrates an online-distillation strategy and DDPO fine-tuning to achieve high-fidelity image generation.

### Weaknesses
1. The proposed OF-Diff is primarily an assembly of existing, well-known components: ControlNet for conditioning, a form of online distillation for feature alignment, and DDPO for fine-tuning. 
2. The central claim of "reducing reliance on real images" is misleading; the method heavily depends on real images during training to extract shape masks via RemoteSAM and to train the teacher model in the distillation process. The "prior shape extraction" is essentially semantic segmentation, which is a standard technique. The paper fails to convincingly demonstrate what the key, novel insight is, beyond a specific combination of these existing blocks. 
3. The comparison methods discussed in the paper (such as LayoutDiffusion and GLIGEN) were not specifically designed for remote sensing imagery. Applying them directly to remote sensing scenarios and using them as baselines is unfair. Furthermore, the authors did not provide sufficiently detailed training configurations (such as whether all comparison methods underwent adequate adaptation to remote sensing data), which may have led to biased comparison results.
4. Although the paper demonstrates improvements in mAP for object detection tasks, it does not explicitly prove whether these gains stem from enhanced image quality or merely increased data volume. There is a lack of quantitative analysis regarding the actual contribution of generated images during detector training, such as through visualization or feature distribution alignment analysis.
5. The entire pipeline is critically dependent on the quality of masks produced by the ESGM, which itself relies on external models (RemoteCLIP, RemoteSAM). The paper provides no analysis of what happens when this module fails or produces noisy/incorrect masks, which is inevitable in practice. How robust is OF-Diff to errors in the initial shape prior? If the extracted mask is distorted, will the generation process fail catastrophically? This is a major point of practical vulnerability that is completely unaddressed.
6. The proposed system is exceptionally complex, involving multiple stages: ESGM, a dual-branch diffusion model with online distillation, and a subsequent DDPO fine-tuning step. The computational cost, memory footprint, and training time must be enormous compared to baselines like AeroGen. The paper completely omits any discussion of efficiency, training time, or inference speed. The practical utility is questionable if the method is an order of magnitude more expensive to train and deploy.

### Questions
1. Can you precisely state the novel algorithmic contribution of OF-Diff, distinct from the existing components (ControlNet, distillation, DDPO) it builds upon?
2. Have you attempted to fine-tune the CC-Diff baseline on your specific datasets to ensure a fair comparison? Could its distribution shift be mitigated?
3. How does the performance of OF-Diff degrade when the input shape masks from ESGM are noisy or partially incorrect? Please provide a robustness analysis.
4. Can you provide data on the computational cost (e.g., GPU hours, memory usage) of training OF-Diff compared to the key baselines?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
5

---

## Human Reviewer 2

### Summary
This work proposes a a method for generating satellite images conditioned on object layouts. Motivation for this work is the need of augmenting existing training datasets, thus, proposing a method for generating additional label-image pairs. Furthermore, this work focuses specifically on instance/object level generations (instead of the commonly adopted semantic maps conditioning or text conditioning).

### Strengths
- Authors identify a lack in current literature: few works sucessfully tackle instance-level generation given the difficulty of the task. Instance-level (layout-to-image paradigm) gives more precise control over the generations and alignment with the ground truth conditions.
- Authors propose a realiable pipeline for achieving high layout fidelity generations by DDPO finetuning, and without the need of using real control images.
- Authors provide ablation studies for the design decisions.
- Extensive evaluation is carried out.
- Qualitative results look strong compared to other models.

### Weaknesses
Authors do not provide any dataset augmentation experiment for OOD-datasets. Such experiment would be useful to prove the usefulness of the model beyond their training dataset distribution, to see if their generations are actually useful for other downstream datasets. I believe this is an important experiment that should be carried out, as it determines the overall usefulness of the generated images not just within the training distribution.

I suggest authors to select some other dataset (not DOTA or DIOR) and compare a baseline model trained on the original dataset and an augmented version of the target dataset.

In fact, Tables 6 and 7 show very small downstream improvements in terms of trainability when compared with other methods. Could authors provide some intuition why generations are not always profitable for training? Trainability is an important part of the work carried out. Authors could provide more ablation experiments showing whether the generated images are usefulness for training.

### Questions
- Given a baseline model trained on DIOR/DOTA default dataset, authors show downstream improvements when baseline model is trained with original + OF-Diff generations (Figure 5). It would be interesting to see the AP evolution given different amounts of synthetic vs real data. For instance:
   - Train a baseline model on 100% real images
   - Train a baseline model on 100% generated images
   - Train a baseline model on 50% real + 50% generated images
   - etc.
   - Train a baseline model on 100% real + 50% generated images
   - Train a baseline model on 100% real + 100% generated images
   - Train a baseline model on 100% real + 200% generated images
   - etc.
- Do authors have any intuition when the baseline model performance plateaus? In other words, the point at which generating more images will not improve downstream performance?

### Soundness
2

### Presentation
2

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes Object Fidelity Diffusion (OF-Diff), a novel diffusion-based model for layout-to-image generation in remote sensing (RS). The key idea is to improve object fidelity and layout controllability without relying on real-image references at inference time. The authors introduce:
1. Enhanced Shape Generation Module (ESGM) to extract object shape priors from bounding box layouts.
2. Online distillation to align shape-based generation with real-image features during training.
3. DDPO (Denoising Diffusion Policy Optimization) to fine-tune the model for better diversity and semantic consistency.
The model is evaluated on DIOR-R and DOTA datasets using a comprehensive set of metrics including FID, KID, YOLOScore, and downstream detection mAP. Results show superior fidelity, layout consistency, and downstream utility, especially for small and polymorphic objects.

### Strengths
1. OF-Diff does not require real-image references at inference, a significant practical improvement.
2. State-of-the-art results on both DIOR-R and DOTA datasets, with mAP improvements of up to 8.3% on airplane and 7.7% on ship categories.
3. The paper is well-structured, with clear problem motivation, method description, and experimental analysis.

### Weaknesses
1. The online distillation and DDPO fine-tuning steps are computationally expensive, but the paper does not report training time, GPU usage, or memory overhead.
2. The paper shows that adding captions improves aesthetics but hurts fidelity (Fig. 7). However, this trade-off is not deeply analyzed. A user study or perceptual evaluation would help clarify when and why to use captions.
3. The method heavily relies on ESGM-generated shape masks. While the paper mentions that distorted masks lead to poor generation, it does not quantify how robust the model is to noisy or incomplete masks?
4.The model is only evaluated on two datasets (DIOR-R and DOTA), both of which are airborne/satellite optical imagery.

### Questions
see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
2

---

## Human Reviewer 4

### Summary
This paper introduces Object Fidelity Diffusion (OF-Diff), a novel layout-to-image diffusion model designed specifically for generating high-fidelity remote sensing (RS) imagery. The primary motivation is to address critical failure modes in existing methods, such as control leakage, structural distortion, and dense generation collapse, which limit their utility for downstream tasks like object detection.

### Strengths
1. ESGM: Leverages pre-trained vision-language and segmentation models (RemoteCLIP and RemoteSAM) to extract precise object shape masks, providing strong geometric priors beyond simple bounding boxes.

2. Employs a teacher-student architecture where a "teacher" decoder (conditioned on both image and shape features) guides a "student" decoder (conditioned only on shape features). This allows the model to learn to generate high-fidelity textures and details without requiring real image references during inference.

3. Applies Denoising Diffusion Policy Optimization (DDPO) as a post-training step, using a reward function based on KNN distance and KL divergence to enhance the diversity and distributional consistency of the generated images.

Comprehensive experiments on the DIOR and DOTA datasets demonstrate that OF-Diff outperforms state-of-the-art methods in generation fidelity, layout consistency, and its utility in improving downstream object detection performance.

### Weaknesses
1. The ESGM module is critically dependent on two large, specialized models: RemoteCLIP and RemoteSAM. While effective, this raises questions about the framework's scalability, accessibility, and potential biases inherited from these foundational models. The paper could benefit from a discussion on the computational cost of this "template extraction" phase and an analysis of how errors from ESGM might propagate through the diffusion pipeline.

2. The paper clearly defines the DDPO reward function (Equation 9) but omits crucial implementation details for the KNN component. As the authors know, computing KNN in the high-dimensional pixel space is infeasible and perceptually meaningless. It is standard practice to compute this in a low-dimensional embedding space (e.g., using a CLIP or VAE encoder). While this is likely what the authors did, this critical detail should be explicitly stated in the implementation section to ensure reproducibility and clarity. Mentioning the specific pre-trained encoder used would be essential.

3. The paper exclusively focuses on object detection as the downstream task. While this is a highly relevant application, remote sensing involves many other perception tasks, such as semantic segmentation and change detection. Demonstrating the utility of OF-Diff for these other tasks could further strengthen the paper's claims of general applicability.

### Questions
Robustness of ESGM: The quality of the generated images seems highly dependent on the quality of the shape masks produced by ESGM. How does OF-Diff perform when ESGM fails or produces a distorted mask (e.g., for objects with complex boundaries or under heavy occlusion)? Is there a mechanism to handle such failures, or does the model simply replicate the distorted shape?

On the DDPO Reward Function: The KNN reward term encourages diversity by pushing generated samples away from the nearest neighbors in the real dataset. Could this potentially penalize the generation of "typical" or common instances and favor only rare or outlier-like objects? How was the balance between the KNN and KL terms (controlled by $\omega$) determined to prevent this?

Inference Speed and Cost: Could you provide details on the inference speed of OF-Diff compared to other methods? Specifically, since ESGM is only used to populate a mask pool for inference, how large does this pool need to be for good performance, and does the selection from this pool add any significant overhead?

Regarding the use of captions (Section 4.5): You note that including captions improves aesthetic appeal but harms downstream performance by deviating from the real data distribution. This is a very interesting finding. Does this imply that for data augmentation purposes, it is better to have models that are "faithful" to the original dataset's quirks and potential imperfections rather than models that generate more "idealized" or aesthetically pleasing images? I would appreciate it if you could elaborate on this insight.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
5