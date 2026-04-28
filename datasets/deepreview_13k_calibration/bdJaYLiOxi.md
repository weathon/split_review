# Radar Spectra-language Model for Automotive Scene Parsing

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 6, 5, 5

## Abstract
Radar sensors are low cost, long-range, and weather-resilient.
Therefore, they are widely used for driver assistance functions, and are expected to be crucial for the success of autonomous driving in the future.
In many perception tasks only pre-processed radar point clouds are considered.
In contrast, radar spectra are a raw form of radar measurements and contain more information than radar point clouds.
However, radar spectra are rather difficult to interpret.
In this work, we aim to explore the semantic information contained in spectra in the context of automated driving, thereby moving towards better interpretability of radar spectra.
To this end, we create a radar spectra-language model, allowing us to query radar spectra measurements for the presence of scene elements using free text.
We overcome the scarcity of radar spectra data by matching the embedding space of an existing vision-language model.
Finally, we explore the benefit of the learned representation for scene retrieval using radar spectra only, and obtain improvements in free space segmentation and object detection merely by injecting the spectra embedding into a baseline model.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Radar sensors are integral to driver assistance systems and the future of autonomous driving due to their cost-effectiveness, long-range capabilities, and resilience to adverse weather. Typically, radar data is processed in point cloud format, but raw radar spectra contain more detailed information, though they are harder to interpret. This research focuses on enhancing radar spectra interpretability in the automotive context. It introduces a radar spectra-language model that enables natural language queries about scene elements within radar spectra. To address data scarcity, the study aligns the embedding space of a vision-language model. By fine-tuning for automotive scenes, it improves performance. This learned representation benefits scene parsing, enhancing free space segmentation and object detection when integrated into a baseline model.

### Strengths
This paper introduces the text information into feature fusion for radar spectra interpretability.

### Weaknesses
1.	The framework seems to be a simple combination of existing methods. I didn’t see the specific design for the radar spectra language model. 
2.	The experiment of detection is not compared with SOTA methods such as RODNet.
3.	What is [20] in Table 3?
4.	If the description includes multiple object information, how do you align the text information with the corresponding object?

### Questions
If the description is not accurate will the information mislead the model?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The author proposes Radar-Spectra Language Model (RSLM) to help interpret the difficult modality (by humans).
In addition, the modality also does not have many datasets. Thus the approach is to leverage the expressive power Vision Language Model (VLM), and train a radar encoder to mimic the features produced by VLM.

RSLM first fine-tunes CLIP image encoder to road scenes (from self-driving car research). 
The best image encoder for the task is OpenCLIP.
To connect radar spectra to the resulting CLIP features, RSLM trains a radar encoder to output features that are as similar as possible to the CLIP features.
The best radar encoder network is Feature Pyramid Network (FPN), and it is trained using MSE loss on retrieval tasks.
The resulting features then are inputted to a network that is trained on two downstream tasks: object detection and free-space estimation.
The object detection losses are focal and smooth-L1 loss, while free-space estimation is trained using BCE loss.

RSLM is tested to find the optimal components, e.g. usage of OpenCLIP, FPN.
In addition, it also analyzes the performance of RSLM on object detection and free-space estimation.
RSLM is able to surpass the baseline, FFT-RadNet, these two tasks.

### Strengths
The radar spectrum pre-training to optimize on similarity to fine-tuned OpenCLIP is novel. It allows for pre-training without a need for explicit Radar-spectra dataset.

### Weaknesses
No discussion on what is still hard to do or not reliable.
Also analysis of the varying the difficulty of the input scenes would help answer the previous question.

### Questions
What self-driving related take would Radar-spectra be able to do well, while other modality cannot or struggle with?

Typos:
Pg. 3, "Prompt Generation" section: (e.g. a photo of a {}) -- {} symbol should be replaced.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a radar spectra-language model (RSLM). The RSLM is built upon CLIP with image as a bridge between radar and text. The RSLM is evaluated by a retrieval task and two downstream tasks. Experiments show that the RSLM has good zero-shot retrieval ability and can boost the performance of two downstream tasks.

### Strengths
1. To the best of my knowledge, this is the first paper trying to build a radar spectra-language model.
2. The fine-tuned VLM for autonomous driving scenes works much better than the off-the-shell CLIP.
3. The zero-shot retrieval ability of RSLM is impressive, especially for the small objects such as pedestrian and cyclist.

### Weaknesses
1. The author seems to lack paper writing skills. All the figures are unaesthetic bitmaps with low resolution and some of the figures are not necessary. For Figure 4a, it is better to use formulation instead of python code to describe the loss functions. For Figure 4b, such a simple architecture may be put in the supplement material. 
2. Changing the position encoding without finetuning may cause performance drop, and splitting the image may break some objects on the edge. A better and more common way is to pad black pixels to the top and bottom of the image. 
3. For the detection and segmentation downstream tasks, it is better to show some cases that the pretrained model helps improve the performance, not just numbers.
4. For autonomous driving tasks, the localization abilitiy is more important than the classification. Could you provide some visualizations such as attention map or GradCAM to see if the retrieved objects are corresponding to the right location?

Other issues:
1. For Equation 4, a period should be added in the end of the formula. 
2. All the quotation marks are single quotes. Please use backquote in front of the quoted phrases. 
3. Some of the RADIal is mistaken by RADiaL.

### Questions
See above

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a study to investigate vision-language models for scene understanding in automotive scenes. To this end, a benchmark is created. For autonomous driving scene understanding, the benefits for downstream object detection and free space estimation are discussed. Ablation studies are well conducted and the paper is well structured.

### Strengths
1. The presented work is one of the first to train a radar-language model for autonomous driving scene understanding.
2. The paper is overall well structured.

### Weaknesses
1. Please consider comparing your proposed model against some existing adapted language models for driving scene understanding.
2. Please consider directly comparing your proposed model against some object detection and segmentation models to verify the superiority of your proposed model.
3. Most of the components from the proposed framework are from existing works. It is hard to find any novel technical designs in the presented framework. Please better clarify the technical novelty and theoretical contributions of the presented work.
4. Would you consider giving an overview of your proposed framework at the beginning of the methodology section, which can help the readers better understand the work?
5. The computation efficiency should be discussed, which is critical in automotive scene understanding.
6. The writing style and presentation quality could be further enhanced. In the introduction, the space between different paragraphs should be enlarged.

### Questions
Would you consider presenting some visualization results of object detection and free space segmentation to qualitatively verify the effectiveness of your proposed method?

While there are not many works on radar-language models, there are extensive works on adapting large-language models for driving scene understanding. Would you consider discussing the relations and differences between your work and existing works in the related work section? 

Sincerely,

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
