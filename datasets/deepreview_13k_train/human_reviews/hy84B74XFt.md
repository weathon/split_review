# Towards Interpretable Controllability in Object-Centric Learning

- Decision: Reject
- Scores: 6, 8, 1

## Abstract
The binding problem in artificial neural networks is actively explored with the goal of achieving human-level recognition skills through the comprehension of the world in terms of symbol-like entities. Especially in the field of computer vision, object-centric learning (OCL) is extensively researched to better understand complex scenes by acquiring object representations or slots. While recent studies in OCL have made strides with complex images or videos, the interpretability and interactivity over object representation remain largely uncharted, still holding promise in the field of OCL. In this paper, we introduce a novel method, Slot Attention with Image Augmentation (SlotAug), to explore the possibility of learning interpretable controllability over slots in a self-supervised manner by utilizing an image augmentation strategy. We also devise the concept of sustainability in controllable slots by introducing iterative and reversible controls over slots with two proposed submethods: Auxiliary Identity Manipulation and Slot Consistency Loss. Extensive empirical studies and theoretical validation confirm the effectiveness of our approach, offering a novel capability for interpretable and sustainable control of object representations. Code will be available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies slot-based unsupervised image models, e.g., Slot-Attention, and proposes a way to introduce controllability in the slots. This is done via enforcing a form of equivariance of the image -> slot transformation to image augmentations, except that the augmentations applied in the slot space are a learnable mapping from the augmentation instuctions. The results demonstrate that the model successfully manages to control and manipulate slots given the instructions, and gracefully handles the inverse instructions to "undo" the given manipulations.

### Strengths
- The paper proposes a very original way to manipulate learnable objet slots in slot attention.
- The main advantage of the method is its simplicity: the augmentations are introduced on the image level, removing the need to implement per-slot manipulation strategies at training, yet the manipulations can be applied to individual slots at inference time leaving the other slots intact.
- The qualitative results are very impressive, even thought the datasets are quite simple. The findings of the paper are encouraging for the future research on slot controlability.

### Weaknesses
The main weakness of the method is the fact requires a pair of (image augmentation, augmentation instruction) to work, rather than only one of them. Iit is easy to generate both the augmentation and its instruction with simple image transformation in a controlled environment, but this is much harder to do in a realistic setup. Some image transformation may not have a clear apriori-known instruction, or vice-versa, some may only have the instruction for the augmentation (e.g., specified as text) without the knowledge of the augmentation. Eschewing this requirement would largely benefit the method and make it applicable in a more realistic setup.

### Questions
No questions

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces SlotAug, an object-centric learning method that allows for interpretable manipulation of the slots. The model is trained with image-level data augmentation and supports scaling, translating, or color shifting individual objects in the scene. The authors introduce the concept of sustainability, which refers to the ability to preserve the nature of the slots, allowing for multiple iterations of slot manipulations. To achieve sustainability, the authors incorporate two submethods, Auxiliary Identity Manipulation (AIM) and Slot Consistency Loss (SCLoss). In experiments on Tetrominoes, CLEVR6, CLEVRTex6, and PTR, the authors demonstrate the ability to manipulate slots and the effectiveness of their model in achieving sustainability of the slots.

### Strengths
This paper introduces a novel approach to the important problem of interpretable and controllable object representations. The idea of leveraging image-level augmentations to enable object-level controllability by taking advantage of the independence of the slots has not been done before, as far as I know. I found the paper generally well-written and easy to understand, although I do list some questions and suggestions regarding clarity below. The experiments clearly demonstrate the ability of their model to manipulate the slots and the benefits of AIM and SCLoss for improving sustainability. The results from section 4.3 are also encouraging in showing that this method potentially helps improve the representation quality of the slots themselves.

### Weaknesses
- In section 4.1.1, the authors claim that one of the reasons their method works is because of the spatial broadcast decoder independently decoding for each slot. This is supported in the appendix by an experiment on SLATE which uses a decoder where the slots are not completely independent. This seems potentially limiting as several recent works in scaling object-centric learning (OCL) to realistic scenes [2, 3, 4] rely on decoders where each slot may not be decoded independently. This may limit the applicability of this method to more realistic scenes that are supported by those OCL methods. Specifically, the reliance on independent decoding could hinder the model's ability to capture complex relationships between objects, which is crucial for understanding real-world scenes. The authors should acknowledge this limitation and discuss potential ways to address it, such as exploring alternative decoder architectures that allow for some degree of interaction between slots while still maintaining the benefits of their approach.
- The second claim in section 4.1.1, that the use of ARK is important, does not seem to be supported by any experiments. How well does this method work with vanilla slot attention? Is ARK required for this method to work? The lack of ablation studies on the necessity of ARK makes it difficult to assess its true contribution. It is unclear if ARK is simply a convenient choice or if it is essential for the method's success. Without these experiments, the claim that ARK is important remains unsubstantiated.
- I could not find which datasets are used for Table 1 and section 4.3 (Table 3 and Figure 6). The fact that segmentation quality is maintained and representation quality potentially improved is an important result. I would be curious about these results broken down by datasets. The absence of dataset details makes it difficult to reproduce the results and evaluate the generalizability of the method. Providing dataset-specific results would allow for a more thorough understanding of the method's strengths and weaknesses.
- In the appendix, the authors mention that the scaling augmentation takes into account the predicted attention maps between the encodings and the slots to handle the translation of objects during scaling. I am a bit confused about this. Does this mean that the augmentation changes as the model gets trained better? Or does this use some other pre-trained Slot Attention encoder? The description of the scaling augmentation is unclear and lacks sufficient detail. It is not obvious how the attention maps are used to handle translation during scaling, and the lack of clarity makes it difficult to understand the technical details of the method. A more detailed explanation, possibly with a visual example, would be beneficial.
- In terms of the presentation, I was initially unsure of the significance of sustainability until I saw the experimental results in section 4.2. For clarity, I would suggest showing a motivating example earlier in the text to explain the necessity of the AIM and SCLoss components. The lack of a clear motivation for sustainability early in the paper makes it difficult to appreciate the importance of the proposed method. A motivating example would help the reader understand the problem being addressed and the significance of the proposed solution.

### Questions
- Are the qualitative examples cherry-picked? Are there common failure scenarios the reader should be aware of?
- I am confused about the use of the SRT decoder in some of the experiments since that method does not have any notion of slots. Was this supposed to be the OSRT decoder [1]?


[1] Object Scene Representation Transformer. https://arxiv.org/abs/2206.06922 

[2] Simple Unsupervised Object-Centric Learning for Complex and Naturalistic Videos. https://arxiv.org/abs/2205.14065

[3] Object-Centric Slot Diffusion. https://arxiv.org/abs/2303.10834

[4] SlotDiffusion: Object-Centric Generative Modeling with Diffusion Models. https://arxiv.org/abs/2305.11281

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes an equivariant consistency regularization for SlotAttention architectures. The idea is for each augmentation of an image, learn a corresponding augmentation that can be applied directly to the object slots, allowing users to modify object representations directly. 
The paper is a bit like adding an equivariant consistency loss (e.g. https://paperswithcode.com/paper/unpaired-image-to-image-translation-using) to SlotAttention. Where image augmentations have corresponding transformations on the Slot representations.

### Strengths
### Related Work
- Decent coverage on learning interpretable latents using VAE/GANs

### Experiments
- I appreciate including error bars. I wish more papers did this. 
- Generally well-organized experiments ssection

### Weaknesses
### Overall
Overall the paper is hard to follow, because common terms like equivariances are called different names (e.g. sustainability) and not clearly defined. The experiments are only on variants of CLEVR, with no evaluations on real-world data. Even on CLEVR, the results are not very convincing, and the method requires defining specific image augmentations for each equivariant action — so it is hard to use this on real-world datasets.


### References:
- Related work ignores the majority of work on object detection + localization. Learning approaches to identifying and localizing objects far predates slot attention — it’s a core computer vision task. Learning approaches go way back, too — OverFeat, deformable parts models, RCNN + children, YOLO, SAM, etc.


### Method:
The authors introduce (as a contribution) new language for agreed-upon terms like equivariance, and the new language doesn’t add anything in my opinion. It is neither intuitive nor well-defined, and only serves to make the work harder to understand.
For example:
1. “In this work, we introduce sustainability which stands for the concept that object representations should sustain their integrity even after undergoing iterative manipulations.”
What is integrity? It seems to be defined in terms of the "durability test" (AKA invertability). But equivariance and invertibility are already in common usage for a while now.


### Experiments:
Experiments are on variants of CLEVR, which is a very simple dataset that was generated in ways that privilege this algorithm. No evaluation on real-world datasets. Other work (e.g. instruct pix2pix https://arxiv.org/pdf/2211.09800.pdf) DOES show zero-shot results on real-world datasets.
Regardless, the results even on CLEVR are not convincing — leading to little to no improvement for object detection.

### Misc:
Many terms feel philosophical, when they could be stated more concretely. E.g. “Then, the model performs spatial binding on img_{ref} to produce slots{_ref}”. Meaning you run the image through the model to get the slot latents?

### Questions
### Comparison to related work:
For interpretable latents (e.g. VAE or GANs), the authors note that these require “manual efforts to identify the features associated with specific properties.”
    - In this work, too, you have to hand-design the augmentation and regenerate appropriate training data. This is also a manual effort, and arguably harder than a post-hoc approach?


### Definition of "Durability Test"
This is defined in the paper as “The multi-step test involves a series of instructions to modify an object and another series to restore it to its initial state.”
1. This is a fine definition, but why not also write out the equations: e.g.  $(g_1 * … * g_k)^{-1} (g_1 * … * g_k) x = x$ ?

However, the requirement that image augmentations are invertible is a strong one (e.g. viewpoint change is not invertible from the image alone). Why not make the approach more general and focus on measuring equivariance

E.g. you can measure the equivariance of the whole model by augmenting the images $(g_1 * … * g_k) (image) = (h_1 * … * h_k) (slots)$ where $g_i$ is an image aug and $h_i$ is the corresponding instruction ref2aug

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
