# Weakly Supervised Virus Capsid Detection with Image-Level Annotations in Electron Microscopy Images

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
Current state-of-the-art methods for object detection rely on annotated bounding boxes of large data sets for training. However, obtaining such annotations is expensive and can require up to hundreds of hours of manual labor. This poses a challenge, especially since such annotations can only be provided by experts, as they require knowledge about the scientific domain. To tackle this challenge, we propose a domain-specific weakly supervised object detection algorithm that only relies on image-level annotations, which are significantly easier to acquire. Our method  distills the knowledge of a pre-trained model, on the task of predicting the presence or absence of a virus in an image, to obtain a set of pseudo-labels that can be used to later train a state-of-the-art object detection model. To do so, we use an optimization approach with a shrinking receptive field to extract virus particles directly without specific network architectures. Through a set of extensive studies, we show how the proposed pseudo-labels are easier to obtain, and, more importantly, are able to outperform other existing weak labeling methods, and even ground truth labels, in cases where the time to obtain the annotation is limited.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a domain-specific weakly supervised object detection method that relies on image-level annotations instead of bounding boxes. They use a pre-trained model to generate pseudo-labels for training, showing that these labels outperform other weak labeling methods and even ground truth labels in time-constrained scenarios.

### Strengths
- the paper is well-written and easily to follow. 
- it proposed an relevantly simple but effective method for an impactful task. In their experimenst, aurthors sucessfully demonstrated the supriority over the consider baselines, includig supervised method as well as zero-shot learning with large scale pretrained models. 
- the authors utilized the spatial information and explored an novel way to refine the localization neural networks provide.

### Weaknesses
The proposed method has potential to work for not only electron microscope images but other medical images. It will be interesting and also brings broader impact if authors can provide discussions around this.

The current setup with Gaussian as a prior assumes that the object to detect is in a round shape. How easily it can be extended to different objects and how accurately it will work?

### Questions
The current setup with Gaussian as a prior assumes that the object to detect is in a round shape. How easily it can be extended to different objects and how accurately it will work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a method for weakly-supervised object detection (WSOL) of virus capsids in EM images, which can be used for rapid curation of bounding boxes. The overview of this method (presented in Figure 1) uses an iterative process in which: 1) Grad-CAM from a pretrained encoder is use to output saliency maps of the highest-scoring virus location, 2)  gradient descent is used to optimize the location of the virus, 3) virus is masked out using known information about the virus size. This process repeats until all viruses are removed (referenced as Ours (Opt)), with the bounding boxes created using this process usable for developing weakly-supervised object detectors (Ours (OD)). Comparisons against human annotators (weakly-supervised binary annotation, location, bounding box) and self-supervised detectors were performed, with comparison against human annotators (with and without time constraints) also performed.

### Strengths
Overall, this work presents a very unique methodology and study design for curating bounding boxes in EM images. A contribution not emphasized in this work is the simplicity of the method, using a very intuitive heuristic that outperforms current unsupervised, deep learning-based detectors such as SAM and CUTLER. Though specific to EM, I believe the uniqueness and simplicity of this work would still be of interest to the computer vision community. The related work section is all comprehensive, and the authors of this work reference related works in weakly-supervised and self-supervised object detection very well.

### Weaknesses
 - Though the related work section provides a comprehensive overview of current progress in WSOL methods, was there a reason why this work does not compare against other WSOL methods such as Xu et al. [1] (CREAM), Wei et al. [2] (ISIC), and other more recent works such as LOCATE [3] and GenPromp [4]? Though specific to EM, many other works in the WSOL domain can also be readily adapted.
- In addition to lack of comparisons, one of the main limitations of this work that may prevent broader interest in the ICLR community is that the proposed method is too specific to EM and is not evaluated on diverse tasks. Though EM is unique compared to natural images which are generally more object-centric, other modalities such as histopathology and multiplexed imaging share similar characteristics (as noted in [5]), with the image scale is objective with units per pixel being fixed. Specifically, the contributions of this work would be strengthened if shown that a simpler heuristic can also be created for other imaging domains.
- Following other works which have found pretrained Vision Transformers (ViTs) to be strong in WSOL [4,5,6], was there as a reason why a ResNet-101 was used for classification instead of a ViT? Moreover, was the DINO-ViT used in CUTLER trained using EM images, or was it using a pretrained checkpoint from ImageNet? As ViTs have been also found to have natural fit for microscopy images [5], it would be interesting to explore how the a DINO-ViT for EM images would: 1) improve the WSOL results of this work, and 2) improve the CUTLER baseline reported in this work.
- Though this work is well-written, it was difficult to understand the training dataset and the downstream dataset for evaluation and annotator labeling. Though described in text, including a table with the distribution of labels for train and test may be simpler to communicate.

### Questions
See above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The manuscript presents a class activation map (CAM)-based weakly supervised learning method for virus particle detection in electron microscopy images. Specifically, it first uses a pre-trained classifier to obtain an initial position of a virus using GradCAM (Selvaraju et al. 2017), and then iteratively refines the position with a Gaussian mask with a dynamic standard deviation. It repeats this process for each virus until all the viruses are detected in the input image. The proposed method is evaluated on 5 electron microscopy image datasets, and the experimental results are promising.

### Strengths
1. The paper introduces a simple yet promising method for weakly supervised object detection. Meanwhile, it conducts extensive ablation studies to show that the proposed weakly supervised method can outperform other more fine-grained annotation-based approaches (e.g., bounding box and point annotations), given a certain time budget.

2. The paper designs a specific user study to demonstrate the effectiveness and efficiency of the proposed method.

### Weaknesses
1. In the experiments, the proposed method is not compared with other state-of-the-art weakly supervised learning methods, such as Zeng et al. 2019, Wei et al. 2022, and Lu et al. 2020. In addition, it is not compared with other CAM-based weakly supervised object detection methods in the experiments, such as Xu et al. 2022. Without a comparison with recent state of the art, it is difficult to determine the superiority of the proposed methods over other approaches.

2. The method requires the object size to be known in advance. This needs additional effort to estimate the size of target objects before applying the method. It would be helpful to provide an in-depth discussion on this design (probably also including the effects of using different estimated object sizes).

3. It seems that the proposed method needs to repeat the optimization process (i.e., solving Equation (2)) for each virus. The time cost may be high if there is a large number of viruses in the input image.

4. The method is evaluated on only virus detection in electron microscopy images, where viruses do not overlap. Thus, the method may not generalize to object detection (e.g., cell or nuclei detection) in other microscopy imaging modalities, such as hematoxylin and eosin (H&E) or immunohistochemistry (IHC) stained brightfield microscopy images, and fluorescence mages, which often have touching or overlapping cells or nuclei. In addition, the repeated optimization for each object would be expensive for H&E or IHC images that typically have thousands of or even more cells/nuclei.

### Questions
1. The proposed method is based on the GradCAM method. What if the GradCAM does not provide good initializations or even wrong saliency maps? What are the effects of inaccurate saliency map creation on the quality of the pseudo-labels generated by the proposed method? 

2. During the optimization process of the proposed method, i.e., solving Equation (2), is the classifier C fixed and not updated? If so, is the optimization of Equation (2) simply to find the position that has the highest value in the prediction map C(I * M(p_t)) at each time step? But if not, what algorithm is used to optimize Equation (2)? 

3. During the postprocessing, the method uses non-maximum suppression to eliminate virus particles that have low detection scores. Are the detection scores of virus particles obtained from the initial CAM map or the prediction map from the Gaussian-filtered input, C(I * M(p_t))?

### Soundness
3 good

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
This paper addresses the challenge of expensive and time-consuming annotation requirements for training state-of-the-art object detection models. The authors propose a domain-specific weakly supervised object detection algorithm that leverages image-level annotations instead of annotated bounding boxes. By distilling the knowledge of a pre-trained model focused on virus presence/absence prediction, the proposed approach generates a set of pseudo-labels that can be used to train an object detection model effectively. The method utilizes an optimization approach with a shrinking receptive field, enabling the extraction of virus particles directly without relying on specific network architectures.

### Strengths
- Addressing Expensive Annotation Requirement: The paper tackles the challenge of acquiring costly bounding box annotations by proposing a weakly supervised approach that relies on image-level annotations. This significantly reduces the manual labor and time required for annotation, making the training process more efficient.
- Extensive Comparative Studies: The authors conduct comprehensive studies to evaluate the effectiveness of the proposed pseudo-labels. The results demonstrate that the generated pseudo-labels outperform other weak labeling methods and even ground truth annotations in scenarios where annotation time is limited. This indicates the superiority and practical value of the proposed approach.

### Weaknesses
 - Limited Model Exploration. The paper primarily focuses on using Faster-RCNN with a ResNet-101 backbone as the detection model. It would be beneficial for the authors to consider exploring other models, such as DETR, to evaluate their effectiveness in the proposed approach. The current choice limits the generalizability of the findings, as different architectures might exhibit varying performance characteristics with the generated pseudo-labels. Specifically, the transformer-based architecture of DETR could offer different inductive biases and potentially improve detection accuracy, especially given its attention mechanism which might be more robust to variations in virus particle appearance. Furthermore, the paper does not explore the impact of different backbone networks within the Faster-RCNN framework itself, such as ResNet-50 or more recent architectures like EfficientNet, which could provide a more comprehensive understanding of the method's robustness.
- Lack of Discussion on Low Signal to Noise Ratio (SNR) in EM Images: While the authors mention that low SNR in EM images can impact the performance of methods designed for other imaging modalities, there is a lack of in-depth discussion, algorithm design, and experiments addressing how to mitigate the low SNR problem and how it specifically affects the capacity of weakly supervised object detection (WSOD) methods in the EM scenario. The paper should include a more detailed analysis of how the low SNR affects the quality of the generated pseudo-labels and the subsequent training of the object detection model. For example, the authors could investigate the impact of different noise levels on the performance of their method and explore techniques such as denoising or data augmentation strategies specifically tailored to low SNR EM images. The absence of such analysis limits the practical applicability of the proposed approach in real-world EM imaging scenarios.

### Questions
In general, I find this work to be commendable. However, there are certain limitations that should be addressed for further improvement. Specifically, it is crucial to include testing with DETR to evaluate the effectiveness of transformer-based architectures. Additionally, at least providing a thorough discussion on the low SNR problem would significantly enhance the quality of the paper. If these questions are well solved, I would like happy to raise my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
