# UltraLightUNet: Rethinking U-shaped Network with Multi-kernel Lightweight Convolutions for Medical Image Segmentation

- Decision: Reject
- Scores: 1, 1, 6, 5

## Abstract
In this paper, we introduce UltraLightUNet (2D and 3D), an ultra-lightweight, multi-kernel U-shaped network for medical image segmentation. The core of UltraLightUNet consists of a new Multi-kernel Inverted Residual (MKIR) block, which can efficiently process images through multiple kernels while capturing complex spatial relationships. Additionally, our Multi-kernel Inverted Residual Attention (MKIRA) block refines and emphasizes image salient features via sophisticated convolutional multi-focal attention mechanisms. UltraLightUNet strategically employs the MKIR block in the encoder for feature extraction and the MKIRA block in the decoder for feature refinement, thus ensuring targeted feature enhancement at each stage. With only 0.316M \#Params and 0.314G #FLOPs, UltraLightUNet offers an ultra-lightweight yet powerful segmentation solution that outperforms state-of-the-art (SOTA) methods across twelve medical imaging benchmarks. Notably, UltraLightUNet surpasses TransUNet on DICE score while using 333$\times$ fewer \#Params and 123$\times$ fewer #FLOPs. Compared to the lightweight model, UNeXt, UltraLightUNet improves DICE scores by up to 6.7% with 4.7$\times$ fewer parameters. UltraLightUNet also outperforms recent lightweight models such as MedT, CMUNeXt, EGE-UNet, Rolling-UNet, and UltraLight_VM_UNet, while using significantly fewer #Params and #FLOPs. Furthermore, our 3D version, UltraLightUNet3D-M (1.42M #Params and 7.1G #FLOPs), outperforms SwinUNETR (62.19M #Params, 328.6G #FLOPs) and nn-UNet (31.2M #Params, 110.4G #FLOPs) on the FETA, MSD Brain Tumor, Prostate, and Lung Cancer segmentation benchmarks. This remarkable performance, combined with substantial computational gains, makes UltraLightUNet an ideal solution for real-time and point-of-care services in resource-constrained environments. We will make the code publicly available upon paper acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The authors introduce UltraLightUNet, an ultra-lightweight 2D and 3D U-shaped network designed for medical image segmentation. This network features novel Multi-kernel Inverted Residual (MKIR) and Multi-kernel Inverted Residual Attention (MKIRA) blocks, aiming to effectively balance computational efficiency with high segmentation performance across multiple medical imaging benchmarks. The architecture is motivated by the need to reduce computational demands in point-of-care diagnostics, particularly in resource-constrained environments.

### Strengths
- The paper is well-written and easy to follow.

- The experimental results are through, with diverse datasets and settings.

- In-depth ablation study and parameters consideration are presented

### Weaknesses
 - Despite the paper presents diverse experiments and ablation studies, I see a very close similarity to a CVPR 2024 paper, named EMCAD [1], which I detail in the next parts (Note that the EMCAD paper is not cited!)

- The proposed method (Figure 2) is clearly the same as last year CVPR paper, with approximately no change in any of the modules both in encoder and decoder of the network. Therefore, I see no novelty and contribution in the paper submitted.

- How is it possible for your method to just have 27000 parameters, while last year paper with the same architecture has at-least 3M parameters (its base version).

- The proposed method is not compared to other SOTA networks (such as [2]) which perform much better over some of the datasets used in the paper (such as ISIC)

### Questions
Please refer to weaknesses section.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The author proposed a 2D and 3D ultra-lightweight, multi-kernel U-shaped network for medical image segmentation, termed a UltraLightUNet. It consists of an Multi-kernel Inverted Residual (MKIR) block and an Multi-kernel Inverted Residual Attention (MKIRA) block.  MKIR was proposed to efficiently process images through multiple kernels while capturing complex spatial relationships, and MKIRA block refines and emphasizes image salient features via new sophisticated convolutional multi-focal attention mechanisms. This UltraLightUNet outperformed other methods with lower complexity.

### Strengths
1. The proposed network has a low number of parameters and low computational complexity than other widely used baselines and achieved promising segmentation accuracy.
2. Methods and results are thoughtfully described.

### Weaknesses
 1. The overall novelty is low. The author mainly proposed two modules, CMFA and MKDC modules. MKDC just applied several depth-wise convolutional layers to extract features from different channels. This idea has already proposed in the Scale-Aware Modulation Meet Transformer [1]. MKDC module employed average and max pooling, and convolution layers, which are the channel-wise and spatial-wise attention. Many various attention-based modules have been proposed between 2018 and 2020 (like the CBAM [2]). The overall network is similar with [3] [4].
 2. The experimental results are limited. First, authors reported FLOPs and Params to demonstrate that the network has a lower computational complexity than other baselines. It is achieved by mainly replacing convolutional layers with depth-wise convolutional layers. However, it will take longer time to train networks which employ depth-wise convolutional layers compared with those with standard convolution layers. Thus, training and test time are needed to be reported. Second, the comparison in Synapse, MSD prostate, and FETA is insufficient. Synapse is a popular benchmark, but only a few baseline methods were reported. Additionally, the performance reported for these baseline methods in this paper is much lower than the performance in the original paper. For example, Swin Unet reported 79.13 in their paper [5], but only 77.58 was reported for it in this manuscript. If authors run experiments for baselines on their own, please make sure the baseline networks have been fully optimized. Only seven 3D methods proposed before 2022 were compared in MSD prostate and FETA. However, 3D segmentation networks between 2023 and 2024 were not compared, and these networks usually achieve more superior performance with lower computational complexity.
 3. The motivation is unclear. The author mentioned that several 3D segmentation networks, including 3D U-Net, SwinUNETR, 3D UX-Net, UNETR, nnU-net and nnFormer, have high computational demands, so they proposed their lightweight network. However, these baseline networks are proposed in 2021 and 2022, and in recent years many lightweight 3D segmentation networks have been proposed and this challenge has been tackled, such as [6][7][8][9][10]. However, authors didn't discuss and explore these lightweight networks. Additionally, modules in this manuscript were proposed based on the idea of ConvNeXt, but its lightweight version was not discussed. Some other depth-wise convolution-based lightweight networks were also not discussed [11].
 4. The theoretical development is not solid. Authors reviewed Vision Transformers in the related work, but it is not related to the work in this manuscript. The network in the manuscript employs a convolutional neural network architecture and attention mechanisms. Additionally, insufficient theoretical development in the Method section, and it is unclear how this design improved the segmentation performance. 
 5. No model interpretability. The interpretability of the CMFA and MKDC modules were not discussed, such as saliency maps. It is important to understand the mechanisms of attention-based modules.
 6. The overall impact is low. The overall improvement in the segmentation performance is low. For example, its best DSC score in the Polyp dataset was 93.48, but other baselines achieved 93.29 and 93.18. Its best DSC score in the Synapse dataset was 78.68, but other baselines achieved 78.40. 

Minors: (1) lacking qualitative results for 3D segmentation results in Synapse, MSD Prostate, and FETA.
(2) Only overall DSC scores were reported for multi-class segmentation tasks, but organ-specific DSC scores were not reported.
(3) lack p-values and standard deviations

### Questions
1. Provide more detailed and necessary experimental details, including recent works in lightweight network design and other more advanced baselines, training and test time in experiments.
2. Demonstrate more solid theoretical development
3. Discuss model interpretability

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces UltraLightUNet, a novel ultra-lightweight, multi-kernel U-shaped network designed to improve medical image segmentation. Leveraging a new Multi-kernel Inverted Residual (MKIR) block for efficient multi-scale feature extraction and a Multi-kernel Inverted Residual Attention (MKIRA) block for refined feature enhancement, UltraLightUNet achieves high segmentation accuracy with minimal parameters and computational load. With only few parameters and FLOPs, the 2D version of UltraLightUNet outperforms existing lightweight and transformer-based segmentation models across multiple medical imaging benchmarks, while the 3D variant, UltraLightUNet3D, achieves superior results on complex 3D medical segmentation tasks with even greater efficiency. These performance gains make UltraLightUNet a viable option for real-time applications in resource-constrained environments, such as point-of-care diagnostics.

### Strengths
The paper's primary strength lies in its originality, presenting a lightweight model architecture, UltraLightUNet, that effectively combines multi-kernel convolutions and attention mechanisms, a novel approach for achieving high segmentation accuracy with low computational overhead. This innovation addresses a critical need for practical, high-performance segmentation models in resource-constrained environments, adding value to the field by bridging computational efficiency and segmentation quality. In terms of quality, the paper’s methodology appears well-supported by rigorous experimental validation across 11 datasets and comparison with SOTA models, demonstrating robust performance gains and highlighting the practical implications of the architecture's low parameter count and FLOPs. Clarity is another strength; the paper methodically explains the architecture components, from the MKIR and MKIRA blocks to grouped attention mechanisms, making it accessible to readers with a background in medical image segmentation. Finally, the significance of UltraLightUNet is considerable due to its broad applicability across a range of medical imaging tasks and its potential for real-time use in settings like point-of-care diagnostics. The model’s lightweight design, paired with high accuracy, addresses critical bottlenecks in deploying AI-driven diagnostics in clinical environments, establishing the paper as a meaningful contribution to the field. I am glad to see the author will open-source the code to promote research in this line.

### Weaknesses
First, while the model is evaluated across various medical imaging datasets, these datasets are relatively straightforward, covering simple segmentation tasks and organs rather than more complex applications like CT/MRI tumor and lesion segmentation. Specifically, the datasets used primarily involve segmenting well-defined anatomical structures, which do not fully represent the challenges of segmenting tumors with irregular shapes, varying intensities, and ambiguous boundaries often seen in clinical practice. 

Second, the masks are mostly binary segmentation tasks. The multi-class segmentation is not well explored. Adding more complicated and multi-class segmentation would better demonstrate the model's capability for broader, real-world medical imaging tasks. The current evaluation does not adequately address the model's ability to differentiate between multiple tissue types or disease states, which is a crucial requirement for many clinical applications. For example, segmenting different tumor subregions or identifying multiple organs in a single image would provide a more comprehensive assessment.

Third, while the proposed blocks—MKIRA, MKIR, MKDC, GAG, and CMFA—are illustrated in the Method section, the paper lacks sufficient theoretical or conceptual motivation for why these specific block designs should enhance segmentation performance. The paper describes the architecture but does not provide a clear rationale for why these particular combinations of multi-kernel convolutions and attention mechanisms are superior to other possible designs. A more detailed explanation of the underlying principles and how they relate to the specific challenges of medical image segmentation would be beneficial.

Lastly, the paper does not discuss the limitations of UltraLightUNet. A dedicated discussion on limitations would provide readers with a more balanced understanding of the model’s practical use and potential future directions for research.

### Questions
Typically, there is no free lunch. Are there any limitations or tradeoffs of the method? Providing those will be helpful for readers.

How it would work on more complicated problems (e.g., 3D tumors/lesions) and multi-class segmentation problems?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript proposes a novel U-shaped network incorporating various modules for medical image segmentation, with a focus on reducing computational costs. Key contributions include the Multi-Kernel Inverted Residual Block, Multi-Kernel Inverted Residual Attention, and Grouped Attention Gate. As a result, the proposed model achieves remarkable computational efficiency and delivers superior segmentation quality compared to state-of-the-art models. The manuscript is well-written and well-organized; however, more detailed technical insights into each module would enhance clarity and depth.

### Strengths
This manuscript presents various experiments validating the model's performance. The multi-kernel structures employed effectively capture multi-scale contexts, enhancing segmentation accuracy without adding complexity. The reported results demonstrate that the proposed model’s segmentation performance surpasses that of significantly heavier architectures.

### Weaknesses
Although well-organized, the manuscript could benefit from a deeper focus on explaining how each module reduces computational costs while maintaining high performance. The method section lacks clear evidence or mathematical proof to support the model’s design, which may present a scientific limitation. Additionally, there are no ablation studies evaluating the individual contributions of each module in terms of both segmentation performance and parameter efficiency. The manuscript claims superior performance, but it does not provide sufficient theoretical justification for its design choices, relying instead on empirical results. The lack of a theoretical foundation makes it difficult to understand the underlying mechanisms that contribute to the model's effectiveness and generalizability. The multi-scale approach, while effective, lacks a novel theoretical contribution, and the manuscript does not adequately address how its approach differs fundamentally from existing methods.

### Questions
1. Can you clarify the effects of the proposed modules in the model with clear evidence or mathematical insight? The current equations in the manuscript seem somewhat redundant, serving primarily as mathematical restatements. It would be helpful to provide more rigorous insights or proofs demonstrating how each module contributes to performance improvement and computational efficiency.

2. Which proposed module is the most critical? Please provide ablation studies to highlight the individual impact of each module on both segmentation performance and computational cost. This would help identify the key components driving the model's success.

3. General multi-scale approaches are not novel. For instance, the "Spatial Feature Conservation Networks (SFCNs) for Dilated Convolutions to Improve Breast Cancer Segmentation from DCE-MRI" (International Workshop on Applications of Medical AI, 2022) employs a multi-scale strategy. What distinguishes your model’s approach to multi-scale feature extraction? Please elaborate on the unique contributions and insights of your method in this context.

4. What are the differences among UltraLightUNet- T, S, and L in terms of model? Layer difference? Please explain in details in the manuscript.

### Soundness
2

### Presentation
3

### Contribution
2
