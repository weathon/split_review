# InstantPortrait: One-Step Portrait Editing via Diffusion Multi-Objective Distillation

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Real-time instruction-based portrait image editing is crucial in various applications, including filters, augmented reality, and video communications, etc. However, real-time portrait editing presents three significant challenges: identity preservation, fidelity to editing instructions, and fast model inference. Given that these aspects often present a trade-off, concurrently addressing them poses an even greater challenge. While diffusion-based image editing methods have shown promising capabilities in personalized image editing in recent years, they lack a dedicated focus on portrait editing and thus suffer from the aforementioned problems as well. To address the gap, this paper introduces an Instant-Portrait Network (IPNet), the first one-step diffusion-based model for portrait editing. We train the network in two stages. We first employ an annealing identity loss to train an Identity Enhancement Network (IDE-Net), to ensure robust identity preservation. We then train the IPNet using a novel diffusion Multi-Objective Distillation approach that integrates adversarial loss, identity distillation loss, and a novel Facial-Style Enhancing loss. The Diffusion Multi-Objective Distillation approach efficiently reduces inference steps, ensures identity consistency, and enhances the precision of instruction-based editing. Extensive comparison with prior models demonstrates IPNet as a superior model in terms of identity preservation, text fidelity, and inference speed.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper tries to tackle the task of portrait editing with identity preservation and style consistency.  It first trains a full-step diffusion model to produce images with robust identity preservation. Then it trains a one-step model that is distilled from the full-step model to further enhance the style, and identity of the edited images.

### Strengths
1. The visual results are impressive. Many details are created, while the identity is well-preserved. 
2. The approach design is reasonable. It first generates the identity-preserved image, then distills the model for efficient inference. 
3. The experiments are convincing.

### Weaknesses
Several limitations can be improved to make this paper better.
1. The dataset creation process is reasonable. However, it is still not very clear to me how this dataset is used. The authors mention that when creating the dataset, they use the AID loss to preserve identity. Then what data is used to train the first stage? Is the data from another model that also uses the AID loss?
2. There are many losses included in the training. How are they tuned? Is there a guideline for the tuning of the hyper-parameters?
3. Using the distilled version of the model usually results in a reduced diversity of styles and texture details. If the diversity can be further evaluated, this work can be more convincing.
4. For the facial expression control, any thoughts on why the current model cannot achieve it and any future plan on how to achieve it?
5. Could you list the source code link you use for IP-Control, which also achieves impressive results?

### Questions
Please list the details of all the comparison methods, including which codebase you are using, which model checkpoint, etc.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces the Instant-Portrait Network (IPNet), a one-step diffusion-based real-time portrait image editing model. The proposed IPNet can address challenges such as identity preservation and editing fidelity. The training process has two stages. The first stage is to train an Identity Enhancement Network for robust identity preservation. The second stage uses a novel Diffusion Multi-Objective Distillation approach to train the IPNet with multiple losses. Extensive comparisons demonstrate that IPNet outperforms existing models in identity consistency, instruction fidelity, and speed.

### Strengths
1. This paper constructs a paired dataset for portrait image editing, consisting of 10,000,000 pairs of images at a resolution of 1024x576. This extensive dataset is invaluable for both this paper and future research in the field of portrait editing. Additionally, the supplementary materials provide a detailed description of the dataset construction process.
2. This paper presents significant strengths in its approach to portrait image editing. It achieves one-step instruction-based editing with high precision in identity preservation, accurate execution of editing instructions, and fast inference.

### Weaknesses
1. The description of the methodology in this paper lacks clarity and omits important details, which may confuse readers. For instance, in section 3.2.2 on Identity Distillation Loss, there is insufficient explanation regarding how the teacher and student models sample time steps during the training process, as well as how the IPNet is distilled to achieve one-step inference. Specifically, the paper does not clarify the exact mechanism of time step selection for both teacher and student networks, nor does it detail how the distillation process enables one-step inference, which is crucial for understanding the core contribution.
2. The paper does not provide a comprehensive explanation of the model and experimental details, lacking important information such as the weights assigned to the different loss functions and specific training details for the two stages. The absence of specific loss weights, batch sizes, and optimization parameters makes it difficult to reproduce the results and evaluate the robustness of the method. Furthermore, the paper does not specify the exact architecture of the networks used, which is essential for a complete understanding of the model.
3. This paper confines the task to portrait editing under fixed poses, only altering attributes such as clothing, makeup, and style without the capability to generate new poses or expressions. However, the comparison models, IPAdapter and InstantID, offer more versatile functionalities, including the ability to generate new poses and expressions. While IPNet demonstrates superior performance within the scope of this paper, it’s possible that IPAdapter and InstantID, when fine-tuned on the dataset presented in this paper, could achieve comparable results to IPNet. The paper does not provide sufficient evidence to rule out this possibility, which limits the impact of the proposed method.

### Questions
1. This paper introduces a dataset for portrait editing. Will it be open-sourced? Making it publicly available would greatly benefit the development of this research area.
2. In constructing the dataset, the authors used IPAdapter combined with ControlNet. Similarly, Table 1 compares the performance of IPAdapter with ControlNet. Could you clarify whether the base models for IPAdapter and the choices for ControlNet in these two instances are the same? Different base model selections will undoubtedly lead to varying performance outcomes.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a one-step text-based portrait image editing method, which can achieve the balance between identity preservation and text alignment. They firstly train an Identity Enhancement Network (IDE-Net) to ensure robust identity preservation. Then, they propose a diffusion Multi-Objective Distillation process to distill IDENet into IPNet, achieving one-step instruction-based portrait image editing.

### Strengths
1. They propose to distill IDENet into IPNet with the diffusion Multi-Objective Distillation process, achieving one-step instruction-based portrait image editing.
2. They propose an Annealing Identity Loss that balances identity preservation and text alignment.
3. They design a dataset generation pipeline to generate a large-scale paired dataset, where each pair contains: 1) an input image; 2) a text prompt; and 3) a target image generated by SDXL with IPAdapter and ControlNet.
4. Experiment results show that they can generate high-quality image editing results with better identity preservation.

### Weaknesses
1. This paper primarily allows editing only the style of portraits; it is not suitable for modifying expressions, poses, or the subject’s position within the image, which imposes certain limitations.
2. The necessity of IDENet remains unclear. Can you provide a more detailed justification for training IDENet rather than using existing methods like IPAdapter or InstantID, and discuss how this choice impacts the overall performance of IPNet?

### Questions
1. Is IDE-Net purely a reconstruction model? Does it take text as input, and could you provide some sample results?
2. If we directly train IDE-Net with the adversarial loss from 3.2.1, the triplet loss from 3.2.3, and the original IDENet losses, would the results surpass those of IPNet?
3. When performing distillation, since IPNet only involves a single step of sampling, how is the number of noise-adding and denoising steps for IDE-Net determined? 
4. Given that the proposed dataset is paired, why wasn’t diffusion loss, some photometric loss, or the losses used in IDENet, applied when training IPNet? Can using those losses provide a more accurate supervision signal than IDENet’s distillation loss?


I look forward to the author’s response, and I am willing to raise my score if some of my concerns are addressed.

### Soundness
3

### Presentation
2

### Contribution
3
