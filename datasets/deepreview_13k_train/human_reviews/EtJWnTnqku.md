# Medical Vision Generalist: Unifying Medical Imaging Tasks in Context

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
This study presents Medical Vision Generalist (MVG), the first foundation model capable of handling various medical imaging tasks---such as cross-modal synthesis, image segmentation, denoising, and inpainting---within a unified image-to-image generation framework. 
    Specifically, MVG employs an in-context generation strategy that standardizes the handling of inputs and outputs as images. By treating these tasks as an image generation process conditioned on prompt image-label pairs and input images, this approach enables a flexible unification of various tasks, even those spanning different modalities and datasets. 
    To capitalize on both local and global context, we design a hybrid method combining masked image modeling with autoregressive training for conditional image generation. This hybrid approach yields the most robust performance across all involved medical imaging tasks. To rigorously evaluate MVG's capabilities, we curated the first comprehensive generalist medical vision benchmark, comprising 13 datasets and spanning four imaging modalities (CT, MRI, X-ray, and micro-ultrasound).
    Our results consistently establish MVG’s superior performance, outperforming existing vision generalists, such as Painter and LVM.
    Furthermore, MVG exhibits strong scalability, with its performance demonstrably improving when trained on a more diverse set of tasks, and can be effectively adapted to unseen datasets with only minimal task-specific samples.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The work is about a new foundation model for medical image analysis that aims to unify multiple imaging tasks (segmentation, cross-modal synthesis, inpainting, and denoising), called Medical Vision Generalist (MVG). The implementation is within a single model using a standardized image-to-image generation framework. MVG distinguishes itself by employing in-context learning strategies, which eliminate the need for retraining on new datasets and enable quick adaptation to unseen tasks with minimal labeled samples. Also authors introduce a benchmark that covers 13 datasets across 4 medical tasks for various imaging modalities (CT, MRI, X-ray, and micro-ultrasound). The latter makes this study not only about the methodology but also an important contribution to the research community.

### Strengths
The comprehensiveness of imaging modalities and tasks. The paper addresses segmentation, cross-modal synthesis, inpainting, and denoising tasks across various modalities, like CT, MRI, X-ray, and micro-ultrasound.

High performance and generalization ability is remarkable. MVG outperforms SOTA models such as Painter and LVM in most metrics. It also demonstrates scalability with different datasets and adaptability to unseen datasets with minimal samples.

Methodology of training - hybrid approach with masked image modeling and autoregressive training is a novelty that provides strong performance across diverse tasks. Also this approach partly solves the problem with medical imaging data augmentation (like cropping operations).

### Weaknesses
As shown by authors, the hybrid use of autoregressive training boosts performance. However, it may impose higher computational costs during inference. The authors could provide a more detailed analysis of the trade-offs between performance and inference efficiency, especially when using MVG with heavy medical files, like the high resolution MRI.

The ablation study lacks detailed insights into the contribution of individual components. For example, how do masked image modeling and autoregressive training individually affect the performance? For example, as the authors mentioned, usual augmentation techniques for SSL, like image cropping, can not be applied to medical imaging. The cropping procedure might mislead the model training and plumet the performance. I wonder if the authors addressed that and conducted some experiments with (specific for medical domain) data augmentation?

The paper compares the authors model with generalist models, however the comparative analysis with specialist models such as U-Net and nnUNet could be more detailed. A deeper examination of the performance trade-offs between generalist and specialist models would help to position MVG’s contribution more clearly and to understand the limits of its applicability. Also, I suggest addressing not only the segmentation task in a great detail; additional qualitative examples for inpainting and denoising would improve the clarity and show how MVG compares visually to specialists.

Line 146 and subsection 4.2 :  “13 tasks…”. 
I suppose it is a miswriting, since there are 13 datasets, but only 4 tasks. 

Line 246 and Figure 3:
The sub-numeration of blocks in the figure would make the reference to its blocks and understanding easier. Instead of referring to blocks as "upper right" or "lower left".

Line 248: There is a reference to “Fig 3(a)”, but, again, no numeration in the image.

Table 1. I think it is important to note in the beginning of the article, that in the benchmark the proportion of datasets for 4 task in non-equal, with Segmentation task comprising the majority.

Line 255: “We hypothesize that this may be attributed to the masking strategy..." - Indeed, medical images data have fundamental and well known differences from the natural domain data; here, you could cite some papers that discuss this topic in more detail. For example (Huang et al., Self-supervised learning for medical image classification: a systematic review and implementation guidelines)

Line 465 and Table 4. The difference between Liver and Spleen datasets and Lung dataset is almost two times. Can you elaborate on the causes of such a huge difference?

Line 470: Data scalability section - there is no reference to Fig. 6.

The reliance on prompts to condition predictions introduces variability in outputs and performance, because different prompts may yield different results. Did authors address it somehow in their experiments? At the very least, how is the performance affected by the different prompts?

### Questions
Line 146 and subsection 4.2 :  “13 tasks…”. 
I suppose it is a miswriting, since there are 13 datasets, but only 4 tasks. 

Line 246 and Figure 3:
The sub-numeration of blocks in the figure would make the reference to its blocks and understanding easier. Instead of referring to blocks as "upper right" or "lower left".

Line 248: There is a reference to “Fig 3(a)”, but, again, no numeration in the image.

Table 1. I think it is important to note in the beginning of the article, that in the benchmark the proportion of datasets for 4 task in non-equal, with Segmentation task comprising the majority.

Line 255: “We hypothesize that this may be attributed to the masking strategy..." - Indeed, medical images data have fundamental and well known differences from the natural domain data; here, you could cite some papers that discuss this topic in more detail. For example (Huang et al., Self-supervised learning for medical image classification: a systematic review and implementation guidelines)

Line 465 and Table 4. The difference between Liver and Spleen datasets and Lung dataset is almost two times. Can you elaborate on the causes of such a huge difference?

Line 470: Data scalability section - there is no reference to Fig. 6.

The reliance on prompts to condition predictions introduces variability in outputs and performance, because different prompts may yield different results. Did authors address it somehow in their experiments? At the very least, how is the performance affected by the different prompts?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Medical Vision Generalist (MVG), a foundational model designed to handle diverse medical imaging tasks within a unified framework. MVG standardizes input and output as images through an in-context generation approach, treating tasks as an image generation process conditioned on prompt image-label pairs. To leverage both local and global context, MVG combines masked image modeling with autoregressive training for conditional image generation. Experimental results indicate that MVG outperforms existing vision generalists, such as Painter and LVM, demonstrating scalability and adaptability across modalities and datasets.

### Strengths
1. The authors insightfully recognize that a pure masking strategy is insufficient for medical image segmentation, leading them to incorporate an autoregressive training pipeline. Experimental results confirm the effectiveness of this approach.

2. Unlike other foundational models focused primarily on segmentation, this paper addresses a broader range of tasks, including cross-modal synthesis, image denoising, and inpainting, opening potential new research directions.

### Weaknesses
1. While the addition of multiple tasks is beneficial, the paper overlooks essential medical imaging tasks, such as image registration and inverse reconstruction, making MVG appear more like an expanded segmentation model than a comprehensive foundation model. The reviewer suggests that MVG’s learned feature representations could potentially support image registration by integrating a flow estimation head, and inverse reconstruction by using denoising as a regularizer, unfolding the inverse optimization problem with forward consistency [1] within the network.

2. Restricting training to 2D images raises concerns about MVG’s utility as a foundational model for medical imaging. Effective 3D analysis is crucial, as many anatomical structures (e.g., brain cortex, lung vessels, heart) span significant volumes, where 2D slices may miss critical contextual information.

3. The authors claim that MVG “scales well with multiple tasks and datasets,” yet the evidence provided in Figure 6 and Table 6 only demonstrates that more data improves performance, a known property of deep learning models, and that unified training is preferable to isolated training, which reiterates established insights for vision transformers requiring large-scale data.

4. The paper lacks runtime and complexity analysis, particularly GPU resources for training. Comparisons with resource-efficient models, such as nnU-Net trained on individual datasets, would offer a clearer picture. Specifically, what GPU/hours are required for training MVG on all datasets, and how does GPU memory usage compare to nnU-Net or other specialist models trained on individual datasets?

### Questions
1. Can the authors explain the discrepancy in ACDC Dice scores for UniverSeg between Table 2 in this paper (0.54) and Table 6 in the UniverSeg paper appendix (0.70)?

2. Is the failure of mask modeling in segmentation tasks due to the use of L1 loss? Have alternative segmentation losses, such as Dice loss, been tested?

3. Could the authors elaborate on the motivation and practical benefits of MVG in medical imaging? Clinically, how does a foundational model outperform specialist models in practice, such as in speed, ease of deployment, or cost-effectiveness? Technically, what key insights from MVG could guide future researchers in developing clinically and economically viable foundational models?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a medical vision generalist (MVG) model, which unifies various medical imaging tasks including segmentation, cross-modal synthesis, denoising, and inpainting within a single image-to-image generation framework. MVG utilizes in-context learning, treating tasks as image generation processes conditioned on prompt image-label pairs, allowing for flexible adaptation to different modalities and datasets. The authors have also curated a comprehensive benchmark with 13 datasets across four imaging modalities to evaluate MVG, which consistently outperforms existing generalist models.

### Strengths
The paper first uses in-context learning to unify multiple medical vision tasks, which is original.
The proposed output space unification strategy is useful when training with multiple segmentation tasks.

### Weaknesses
The advantage of unifying multiple medical vision tasks through the MVG model could not be verified based on the evidence provided in this paper.  
According to Table 2 and Table 5, the performance gain in segmentation tasks could be due to the colorization strategy instead of unifying other vision tasks. 
Regarding cross-modal synthesis, inpainting, and Denoising tasks, the improvement by the MVG model is marginal compared to the previous generalist model and all generalist models performs worse than specialist models in each task according to Table 3.
Besides, the experiments on the scalability were conducted on several small datasets, which could not demonstrate the potential to increase the performance when unifying all datasets.

### Questions
To better demonstrate the advantage of unifying multiple medical vision tasks through the MVG model, the authors could make the following efforts to address the concerns,
1. compare the segmentation performance while isolating the effects of the colorization strategy from task unification.
2. discuss potential reasons for the marginal improvements in these tasks and propose strategies to close the gap with specialist models
3. conduct scalability experiments on the unified datasets.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors introduce a unified framework, named Medical Vision Generalist, for medical imaging analysis tasks, including segmentation, cross-modality synthesis, inpainting and denoising. The authors formulate the learning task as prompt-based learning task and prompt include task-image and task-label pairs. The authors adopt a single-channel colorization method to unify the output space of images across tasks. The authors combine the masked imaging modeling and auto-aggressive training method to train the model. To demonstrate the framework's capabilities, the authors curate a comprehensive generalist medical vision benchmark.

### Strengths
- The paper is well written and easy to follow. 
- The paper proposes a solution to address the generalization of medical imaging analysis, such as cross-domain problem.
- The paper proposes a unified colorization formulation to unify the different output types of medical imaging analysis tasks. 
- The paper treats the different learning tasks as a prompt-based learning task. 
- The paper introduces a new benchmark for generalist medical imaging analysis.

### Weaknesses
 - The proposed framework is limited to 2D scenario.
- The paper does not explain the clinical motivation why a generalized medical imaging analysis model is needed. To me, since there are many pre-trained specialized models, medical researchers can just pick one of the state-of-the-art models and get better performance than the generalized models. 
- The motivation of combining the masked imaging modeling and auto-aggressive is not clear. In the experiment, auto-aggressive training is more superior than masked imaging modeling. Then why combining them in the first place?
- The generalization of proposed framework is not very convincing, since the organs in the unseen-dataset also appears in training set. What about other types of medical imaging dataset, such as pathology data?

### Questions
- Could the authors explain the potential clinical benefits of your proposed framework in detail? 
- Could the authors add more unseen-dataset evaluation to test the generalization of the proposed framework, for example cell data whose semantic is not available in the training data?
- Could the authors explain architecture of your ViT, such as the embedding size or number of layers or the total number of parameters, since the network requires 8 A5000 gpus to train?
- Could the authors explain the training time of auto-aggression modeling?
- Could the authors explain the inference resources needed of your model? Can it run on CPU under an acceptable time? How much time does it require to infer a given test image under a given test hardware?

### Soundness
3

### Presentation
4

### Contribution
3
