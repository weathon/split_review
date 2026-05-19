# Learning General-purpose Biomedical Volume Representations using Randomized Synthesis

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
\looseness=-1
Current \textit{volumetric} biomedical foundation models struggle to generalize as public 3D datasets are small and do not cover the broad diversity of medical procedures, conditions, anatomical regions, and imaging protocols. We address this by creating a representation learning method that instead anticipates strong domain shifts at training time itself. We first propose a data engine that synthesizes highly variable training samples that enable generalization to new biomedical contexts. To then train a single 3D network for any voxel-level task, we develop a contrastive learning method that pretrains the network to be stable against nuisance imaging variation simulated by the data engine, a key inductive bias for generalization. This network's features can be used as robust representations of input images for downstream tasks and its weights provide a strong, dataset-agnostic initialization for finetuning on new datasets. As a result, we set new standards across \textit{both} multimodality registration and few-shot segmentation, a first for any 3D biomedical vision model, all without (pre-)training on any existing dataset of real images.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work proposes a new method for general (few-shot) medical image segmentation and registration. The method is based on generating realistic and varying synthetic data and training a generalist 3D segmentation and registration models on this data. The goal is to develop a method for generalizing to different imaging devices, medical procedures and conditions as well as different populations. 

The data synthesis engine is capable to generate highly diverse samples and uses the totalsegmentattor dataset for shape templates. The “foundational” model is then pretrained using contrastive pretraining and finetuned in multi-modality registration and few-shot segmentation. 

In experiments the authors demonstrate excellent performance in both downstream tasks.

### Strengths
-	Innovative approach with a highly powerful general synthetic data engine, I think this work adds a lot to the discussion on “foundational” models in medicine. 

-	The method requires a comparatively small number of trainable hyperparameters compared to existing models while achieving a higher accuracy. This in my opinion is an important contribution towards sustainable models. 

-	The authors provide the source code which is a major plus for reproducibility and discuss reproducibility aspects. 

-	The authors evaluate the effect of different pretraining strategies in reasonable ablation studies. 

-	The authors honestly show negative results in the appendix.

### Weaknesses
-	Considered datasets. If I am not missing any details the authors mostly evaluate their method on CT and MRI images. They even consider an MRI image as out of distribution. I think experimentation and ablation on more difficult and diverse datasets, such as 3D microscopy or Ultrasound, even if the results are not all positive would add to the discussion and validate the claim of a “general volumetric biomedical foundation model”

-	Framing of contribution. I would prefer if the authors tone down their wording about the model and clearly point out that it is a model for radiology or CT and MRI dataset and not a “general volumetric biomedical foundation model”.

-	Hyperparameter selection: What range of hyperparameters was tested, and how much time or resources were spent on tuning? How were the hyperparameters for the four baseline methods chosen? Especially for fine-tuning the baselines on your datasets, which I assume is done? Clearly describing the hyperparameter search is important for reproducibility. Please correct me if I was missing such details from the main manuscript.

### Questions
Please see weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors present a method to generate highly variable synthetic imaging data which is then used to pre-train a 3D network using contrastive learning. The data generation method consists of drawing samples from a semantically labelled repository of biomedical shape templates to randomly populate an empty 3D volume. The volume is then deformed. Empty space and organ 'envelopes' are also simulated. To simulate different modalities and protocols, random intensity transformation is applied to the deformed 3D volume to yield 2 images. Typical imaging artifacts such a sbias field and blurring are simulated through random augmentations.The two images are fed into a UNet, and contrastive pre-training is performed on features at each decoder layer. An anchor point is chosen in one of the images, and all voxels of that label in both images are considered positive, and everything else negative pairs. The network yields features that can be used to finetune on other modalities and tasks. Importantly, the representations are modality-agnostic and anatomy-agnostic.

### Strengths
* The paper is very well written - it lays out the prior work and puts the contirbute in context.
* The approach yields representations that are both modality-agnostic and task-agnostic while removing the need for dataset-specific and anatomy-specific pre-training.
* Authors present results of several downstream tasks using their features including multi-modality registration image registration and few-shot segmentation on which their method outperform the others compared.
* Authors perform ablation studies on the various components of their pipeilne.
* The Authors present extensive visualization and quantitative results in their main text, and supplementary material. Algorithms and parameters are clearly presented too which allows for further scrutiny and improved reproducability.
* Authors are aware of the limitations of their approach and include these in the paper.

### Weaknesses
* The segmentation task performed using the Authors features may yield better results than the other methods that are compared, however the result still misses significant portions of the anatomical regions they aim to segment. The features require further adjustment and extensive fine-tuning to be useful in diagnosis and treatment.

### Questions
* Authors compare their randomized shape template-based synthetic data engine to one that uses data with no biomedical priors and one using brain regions. Can Authors elaborate more on the intuiton for why their randomly deformed template shapes are so effective? Is there some point at which the extent of the deformation causes the representations to be less useful?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a pre-training approach for downstream tasks related to fine-grained volumetric medical data: image registration and semantic segmentation. The authors propose to learn appearance invariance and shapes of human anatomy through synthetic dense pixel volumes. In this process, 3D volumes are synthesized by randomly recomposing 3D anatomical shapes and assigning multiple sets of random pixel values, in together with synthetic noises and deformations. Pairs of synthetic volumes are used for multi-scale contrastive learning. The proposed approach demonstrates improved image registration and low-shot image segmentation results compared to some previous works. Detailed ablation studies on the pre-training configurations toward downstream performances are conducted.

### Strengths
The overall methodology is straightforward and easy to understand. It echoes with the classical computer vision concept of invariance learning in the deep neural network era (although learned through a data-driven approach).

Improved image registration results on two public image registration benchmarks and image segmentation performance on six image segmentation datasets are shown, compared to those of some existing works. 

The paper is well-written with sufficient clarity. The illustrations are self-explanatory. Readers will enjoy reading it.

### Weaknesses
Technical novelty: The core idea behind the approach is to leverage data-driven approach to learn invariance to pixel values through paired synthetic shapes and different pixel values, and to learn semantic-independent shape representation through random geometric (real-world and pure synthetic) shapes – both key ideas come from the well-established SynthMorph (random Ising shapes with random intensity + synthetic deformation for training registration networks. Hoffmann et al.) and SynthSeg (GMM-like pixel value model for repainting brain structures. Billot et al.) Despite leveraging more anatomical shapes beyond brain structures and applied to a contrastive framework, the essence remains unchanged.  

Many medical decisions are made not only on shape but also on subtle textures, for example, differentiating subtypes of tumors/lesions – toward which the proposed over-simplified appearance model by nature falls short. More sophisticated texture models need to be carefully studied beyond this manuscript.

For the same reason, high-level global semantic information such as relative locations between anatomical structures cannot be learned due to the nature of this approach. 

Real-world value: Given the increasing number of large-scale publicly accessible volumetric image datasets such as CT-RATE (Hamamci et al.), Totalsegmenter (Wasserthal et al.), and AbdomenAtlas (Li et al.), and the derived 3D foundation models, the real-world application of the proposed framework is unclear. Some of these large-scale public datasets come with fine-grain pixel-wise labels and associated radiological reports which provide additional supervision signals and text alignment potentials. The claimed generalization capability can be learned from multi-site large real-world datasets as well, through the intrinsic heterogeneity of big data and possibly through intense data augmentation.

### Questions
The proposed workflow involves many hyper-parameters (Figure 12) controlling the properties of generated synthetic volumes -- what is the rule of thumb for choosing them?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes training a backbone that generalizes across different datasets using synthetically generated dataset. The proposed pre-training strategy has 3 main steps: 1) Given a large datasets of 104 annotated organs, randomly sample anatomies, deform them and create a volume by ensembling these anatomies, 2) add noise and other augmentations to the volumes that are sampled in the previous step to simulate realistic looking synthetic medical images from labels, 3) train a U-Net with a contrastive objective by sampling two volumes that share the same 3D semantic layout but differ in appearance, treating corresponding features at different encoder levels as positives and all others as negatives. The pre-trained backbone is validated on two different tasks: 3D registration and 3D few-shot segmentation; using multiple datasets.  The results show the effectiveness of the proposed backbone in the experiments compared to existing methods.

### Strengths
- Foundational models are showing promising performance lately; however, we lack of a 3D model that work across different modalities in medical imaging. The paper proposes a solution to this important problem using domain randomisation and contrastive learning.
- The paper contain experiments on multiple datasets both for registration and few shot segmentation, and the results demonstrate the potential of the method.
- The idea of combining the ideas of domain randomisation and local contrastive learning to train a generic 3D backbone is quite interesting and, to my knowledge, is novel.

### Weaknesses
- One issue I see in the paper is the convoluted description of the data engine step, especially the part creating the label ensemble model in section 3. I understand that this step is mainly based on the domain randomisation idea proposed in the literature. However, it is not really clear to me the steps between 201-207, especially the parts multiplying the masks with a randomly deformed sphere and randomly encasing half of the foreground-masked volumes.

- The images generated in the data engine step do not seem like as real medical images. Do they look like this because the deformation is too large? It is not clear why one would prefer training the model using such unrealistic images.

- The paper does not discuss the recent foundational models that show better generalization performance on many medical image datasets [1]. The downstream task performance of the representations obtained from the proposed backbone should be compared with the those obtained by the representations of a foundational model (e.g. DinoV2 [2]). For example, [3] is a recent paper that uses DinoV2 features for registration; but the same applies for the segmentation experiments. One can use the DinoV2 features for segmentation.

[1] Cekmeceli et al. "Do Vision Foundation Models Enhance Domain Generalization in Medical Image Segmentation?"
[2] Oquab et al. "DINOv2: Learning Robust Visual Features without Supervision"
[3] Song et al. "DINO-Reg: General Purpose Image Encoder for Training-Free Multi-modal Deformable Medical Image Registration"

### Questions
1- What are the exact steps of the "label ensemble model" described in Section 3? Please write elaborate description of these steps.
2- Why do the generated images not look like real medical images? Is it because the deformation is too large? Why such "unrealistic" looking images are preferred rather than more realistic ones obtained with smaller deformation?
3- How does the quality of the representations obtained by the proposed backbone compares with SoTA foundational models such as DinoV2 or SAM2?

### Soundness
3

### Presentation
3

### Contribution
3
