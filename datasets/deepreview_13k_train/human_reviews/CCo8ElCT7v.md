# Comprehensive Comparison between Vision Transformers and Convolutional Neural Networks for Face Recognition Tasks

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
This paper presents a comprehensive comparison between Vision Transformers and Convolutional Neural Networks for face recognition related tasks, including extensive experiments on the tasks of face identification and verification. Our study focuses on six state-of-the-art models: EfficientNet, Inception, MobileNet, ResNet, VGG, and Vision Transformers. Our evaluation of these models is based on five diverse datasets: Labeled Faces in the Wild, Real World Occluded Faces, Surveillance Cameras Face, UPM-GTI-Face, and VGG Face 2. These datasets present unique challenges regarding people diversity, distance from the camera, and face occlusions such as those produced by masks and glasses. Our contribution to the field includes a deep analysis of the experimental results, including a thorough examination of the training and evaluation process, as well as the software and hardware configurations used. Our results show that Vision Transformers outperform Convolutional Neural Networks in terms of accuracy and robustness against distance and occlusions for face recognition related tasks, while also presenting a smaller memory footprint and an impressive inference speed, rivaling even the fastest Convolutional Neural Networks. In conclusion, our study provides valuable insights into the performance of Vision Transformers for face recognition related tasks and highlights the potential of these models as a more efficient solution than Convolutional Neural Networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this manuscript, the authors attempt to study the performance of general-purpose Vision Transformers in Face Recognition scenarios and contrast their findings against general-purpose Convolutional Neural Network architectures. They claim that ViT performance perform better than the compared CNNs in this scenario.

### Strengths
The document is mostly well-presented in its structure, use of the English language, and figures.

### Weaknesses
This work completely disregards other popular works in the face recognition literature. The authors compare general-purpose CNNs and ViT_B32 when efficient face recognition-specific approaches are already available such as MobileFaceNet [1], ShuffleFaceNet [2], VarGFaceNet [3], GhostFaceNets [4], EdgeFace [5], among others. Furthermore, it does not mention previous studies on transformers for face recognition [6] and part-based face recognition with vision transformers [7], for example. They also do not comment on recently popular Hybrid (ViT+CNN) approaches, as in EdgeFace [5] and MobileFaceFormer [8]. 
The datasets described are not divided into scenarios and do not include relevant challenging datasets (e.g. using TinyFace [9] and SurvFace [9] to complement low resolution comparisons with SCface). In general, this study misses many comparisons in the state of the art for face recognition scenarios such as: cross age with AgeDB [10], cross pose with CFP [11], racial-bias analysis with RFW [12], among many others.

### Questions
Suggestions:
- Familiarize with recent literature specific on face recognition and gather benchmark on key datasets.
- Analyze the components that make the face recognition-specific approaches more accurate on face recognition scenarios.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an empirical, mainly quantitative, comparison between CNNs and Vision Transformers (ViTs) as evaluated on both face identification and face verification. Five different CNNs and one VT are evaluated across six datasets. It is found that the ViT (ViT-B32) almost consistently outperforms all CNN architectures. The experiments are systematic.

### Strengths
* Empirical investigations of the behavior and performance of neural networks is of large importance. It is brave of a paper to take a step back and systematically compare architectures rather than constantly presenting new -- potentially not as thoroughly tested -- models or add-on modules.

* We are in the middle of a paradigm shift between vision Transformers and CNNs so it is certainly important right now to try and map out empirical differences between the two.

* Five datasets and six models are used (extensive evaluation)

* The code is made public.

Minor but positive things:

* The three paragraph of the introduction had a good flow and were easy to read (see only that the first face paragraph could be a bit more specific)
* 2.1 is informative and well-written

### Weaknesses
 * No uncertainty (e.g., standard deviations across random seeds) are presented for the different results. This may be ok since the models are evaluated across many different datasets, but in that case the seed should be fixed and that should be stated.

* Missing a clear motivation for why facial recognition is the investigated task. Has it previously not been done for this field, are CNNs still considered the main models there? Also, it would be constructive to discuss the ethical risks vs. benefits of surveillance computer vision applications. (An ethical statement could be in order.)

* Missing a comment on how the hyperparameters common for all architectures were selected (e.g., following another paper's set up, just as standard hyperparameters, etc). It is important that they were not selected to optimize a specific architecture, and it would be good to convince the reader about this.

* I would avoid referring to my own paper as having 'paramount significance' (strong wording, verging on over-selling). The number of times the word 'remarkable/y' (6) is a bit exaggerated as well.

* No explanation is offered for why the ResNet surpassed the ViT in Fig. 7b.

Detailed minor suggestions:
* References should be in parentheses (Dosovitskiy et al. (2020))
* This paragraph could be made more specific (since you claim that it in fact does present **very specific** challenges), it is currently not so informative: "...that presents very specific features and challenges. The main challenges are related to the low inter-class variance and the high intra-class variance that can be observed in most face image datasets Cao et al. (2018); Huang et al. (2008). This makes face recognition a more difficult task than..."
* I would (sadly) avoid using the wording 'in spirit' in this context (2.1, page 3)
* 'Convoluting' should be changed to 'convolving', and quotations should be removed
* page 4, "an for" >> "and for"
* It could be nice with a table summarizing the 5 datasets and tasks.
* Fig. 6: would be nice to have accessible in the caption whether this dataset is made for face verification or face identification.

### Questions
* Page 5, "is bounded between 0 (the worst measure of separability) and 1 (a perfect measure of separability), with 0.5 indicating that a network has no class separation capability whatsoever." >> if 0.5 already has 0 separability, what happens between 0.5 and 0? Maybe rephrase
* 3.3: it is not clear to me if you use the checkpoint from the best epoch or from the 25th (last) epoch for the test results in Table 2? If you just use the last epoch (which I suspect since you say that each model has been trained for 25 epochs), it would be more informative to report the validation accuracy at this epoch (for the model you actually use.)

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper presented a fair and comprehensive benchmark of 5 CNN-type networks and Vision Transformer on 5 face recognition benchmark datasets in terms of face verification and validation tasks. This benchmark enforced the exact training and testing set splits for fair comparison and compared the training and test accuracy, the number of parameters and inference time. The results show that the ViT network compares favorably to those CNN-type networks w.r.t. the face recognition performance and computation complexity on these benchmarks.

### Strengths
This paper performed a rigorous evaluation of EfficientNet, Incpetion, MobileNet, ResNet, VGG and ViT networks by training them for face recognition tasks and compared their performance thoroughly.

### Weaknesses
Certainly this is a quite useful technical report on the evaluation of different popular network architectures for face recognition tasks. I am not convinced this work’s “paramount significance as it pioneers a comprehensive evaluation of ViTs against CNNs”.

This benchmark compared the performance of 6 vanilla networks trained for face recognition tasks. In fact, there are many dedicated face recognition methods and pipelines including face detection and alignment, etc. The FR field probably cares more about the end-to-end performance of the whole face recognition pipeline.

The FRTE is probably the most thorough evaluation for the industry, which tests the performance of binary programs provided by different FR vendors on a blind set with no limitation of the training dataset or anything.

Face recognition Technology Evaluation (FRTE) organized by NIST
https://pages.nist.gov/frvt/html/frvt1N.html

Important references missing:
DeepFace: closing the gap to human-level performance in face verification, CVPR 2014. 
Deep learning face representation by joint identification-verification, NIPS 2014
Comparing vision transformer and convolutional neural networks for image classification: a literature review, 2023.

### Questions
The performance appears saturated on some face recognition datasets. The results of several cases may affect the benchmark. Is there any more challenging test set for face recognition?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a comprehensive comparison between ViTs and CNNs for face recognition tasks, focusing on face identification and verification. The study evaluates six models (EfficientNet, Inception, MobileNet, ResNet, VGG, and ViTs) on five diverse datasets, highlighting the performance, robustness, and inference speed of ViTs compared to CNNs.

### Strengths
1. This paper conducts thorough experiments on various network architectures for different evaluation tasks and datasets in face recognition.
2. It offers valuable insights for the design of network structures in face recognition applications.

### Weaknesses
1. This paper seems more like an experimental evaluation report, primarily focusing on the organization of test numbers.
2. It would be beneficial for the authors to extrapolate some new insights from these figures, potentially providing fresh perspectives on training or evaluation in face recognition.

### Questions
None.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
