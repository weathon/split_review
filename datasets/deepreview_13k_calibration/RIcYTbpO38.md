# Don't Judge by the Look: Towards Motion Coherent Video Representation

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 8, 3

## Abstract
Current training pipelines in object recognition neglect Hue Jittering when doing data augmentation as it not only brings appearance changes that are detrimental to classification, but also the implementation is inefficient in practice. In this study, we investigate the effect of hue variance in the context of video understanding and find this variance to be beneficial 
since static appearances are less important in videos that contain motion information. 
Based on this observation, we propose a data augmentation method for video understanding, named Motion Coherent Augmentation (MCA), 
that introduces appearance variation in videos and implicitly encourages the model to prioritize motion patterns, rather than static appearances.
Concretely, we propose an operation SwapMix to efficiently modify the appearance of video samples, and introduce Variation Alignment (VA) to resolve the distribution shift caused by SwapMix, 
enforcing the model to learn appearance invariant representations. 
Comprehensive empirical evaluation across various architectures and different datasets solidly validates the effectiveness and generalization ability of MCA, and the application of VA in other augmentation methods.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an interesting trick to improve action recognition performance in benchmark datasets. Specifically, hue jittering or hue variance has been shown to help improve performance most likely due to adding robustness to the appearance of the content and focusing more on the motion to perform better action recognition. The proposed MCA approach focuses on better data augmentation for video recognition tasks. Performance on multiple benchmarks shows evidence for this idea to be effective.

### Strengths
Proposes a simple yet effective trick to improve the quantified results by a small amount on multiple benchmark datasets. 

Comparison performed on multiple action recognition benchmark datasets with ablation study as well. 

The writing, figures, and explanation are reasonable and effective.

### Weaknesses
The novelty of the approach is limited, as-in a new network to extract unique embedding features is not what is being proposed here. This seems more like add-on that could be used with other solutions.



### Questions
1. How does this approach compare to the one that uses only optical flow or other motion representation and not appearance?
2. Does the MCA approach work better with other more modern and robust core networks than TCM?

### Soundness
3 good

### Presentation
3 good

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
The current study investigates the effect of hue variance on video recognition and proposes a data augmentation method called Motion Coherent Augmentation (MCA) that introduces appearance variation to encourage the model to prioritize motion patterns over static appearances. This approach is based on the observation that static appearances are less important in videos with motion information. The proposed method uses an operation called SwapMix to modify video samples' appearances efficiently and Variation Alignment (VA) to resolve distribution shifts caused by SwapMix, enforcing the model to learn appearance-invariant representations. Comprehensive experiments on different architectures and datasets demonstrate the effectiveness and generalization ability of MCA, achieving an average performance gain of 1.95% on the Something-Something V1 dataset compared to the competing method Uniformer.

### Strengths
The proposed Motion Coherent Augmentation (MCA) method addresses the issue of overfitting in video recognition by introducing an effective data augmentation strategy. The key advantages of MCA are:

- Hue Jittering: MCA leverages Hue Jittering, which is usually overlooked in object recognition, to generate new appearances for videos. This operation helps the model prioritize the motion pattern over static appearance.

- SwapMix: An efficient operation called SwapMix is introduced to modify the appearance of video samples in the RGB space. This operation helps simulate the effect of appearance variation while preserving important color attributes like saturation and lightness.

- Variation Alignment (VA): VA is used to construct training pairs with different appearances and encourage their predictions to align with each other. This helps the model learn appearance-invariant representations.

- Compatibility: MCA can be seamlessly integrated into existing video recognition approaches with minimal code modifications and provides consistent improvement. This indicates that the method is compatible with existing data augmentation techniques.

Experimental validation: Comprehensive experiments on various architectures and benchmarks demonstrate the effectiveness and generalization ability of MCA. The method demonstrates excellent performance and can further enhance the results of competing approaches like Uniformer.

In summary, the Motion Coherent Augmentation method addresses the issue of overfitting in video recognition by providing an effective data augmentation strategy that leverages Hue Jittering, SwapMix, and Variation Alignment. MCA achieves consistent improvement while being compatible with existing techniques, making it a promising approach for video recognition.

### Weaknesses
It is a valid point that the paper lacks a discussion on the generalization capabilities of MCA and how it could potentially improve the transferability of models. Introducing such a discussion could indeed help increase the impact of the work. A possible approach could be to analyze the performance of MCA on tasks that are different from the benchmark datasets used during training, and compare it to other data augmentation methods. Additionally, analyzing the learned representations using techniques like clustering or visualization could provide insights into their generalization potential. Overall, a thorough evaluation of the generalization capabilities of MCA could strengthen the paper and make it more impactful.

The relationship between MCA and existing video self-supervised methods is not further explored in the given text. It would be valuable to investigate how MCA can be integrated with other video self-supervised methods and examine the potential synergies between them. Understanding how MCA complements or enhances existing techniques could provide valuable insights into the effectiveness and generalization abilities of the combined approach. Further research is needed to explore the relationship between MCA and video self-supervised methods and determine how they can be effectively integrated to improve video recognition tasks.

### Questions
Whether the MCA data augmentation method provides gains in video domain adaptation or video domain generalization settings, where videos from different domains are involved, is not explicitly discussed in the given context. To assess whether MCA is beneficial in such video migration scenarios, an evaluation of its performance in tasks that involve domain adaptation or generalization would be necessary. Comprehensive experiments comparing MCA to other data augmentation techniques and assessing its effect on domain adaptation or generalization metrics would provide insights into its potential usefulness in video migration settings.


The potential of integrating MCA with existing video self-supervised methods to further enhance the performance is not explicitly discussed in the given text. However, it is worth exploring the compatibility of MCA with other video self-supervised methods and investigating whether their combination can lead to improved results. By combining the strengths of MCA in introducing appearance variation and prioritizing motion patterns with other self-supervised techniques, it is possible to enhance the overall effectiveness of video representation learning. Further research and experimentation are needed to explore the potential synergies and benefits of integrating MCA with existing video self-supervised methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a new augmentation technique for training video recognition networks, referred to as Motion Coherent Augmentation (MCA). The method is a simple but effective modification of existing Hue Jittering method, adapted specifically to video content (e.g. to learn appearance invariant representation, capturing motion patterns). The method is well explained and the experiments confirm the efficacy of the proposed solution.

### Strengths
Simple but effective augmentation technique
Can be easily applied to improve any of video recognition methods
Evaluated on multiple datasets

Overall the paper is well written and clearly presents the contributions. The proposed augmentation technique (MCA) consists of two parts: SwapMix ( a method, which permutes RGB channels and computes the linear interpolation between original and the permuted image), and Variation Alignment (a method that forces the network to become invariant to SwapMix, ie. the network is explicitly trained to return the same class distributions for both, original image and SwapMix-ed image. The multiple experiments on multiple video datasets confirm the efficacy of the proposed technique. The ablation analysis of different components of the method has also been presented.

### Weaknesses
Slows down the training and requires more GPU resources
The analysis of impact of \lambda_{AV} has not been evaluated.

### Questions
Could authors provide the analysis of \lambda_{AV} impact on training performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a method of augmentation for video action recognition. The authors focus on “Hue Jittering”, which is one of common ways to data augmentation for images since it is implemented in common frameworks such as pytorch.

However it is computationally inefficient to compute hue and perform  jittering, then the authors propose SwapMix, which is randomly swap RGB channels of a given video frames (Channel Swap), followed by a linear blending with the original frames.

In addition, the authors propose Variation Alignment (VA) to enhance the invariant to appearance change by SwapMix. It is simply align the  model outputs for the original and SwapMix-ed frames by minimizing cross-entropy of two outputs.

Motion Coherent Augmentation (MCA), the name of the proposed method, is the combination is SwapMix and VA, which is used in experiments.

Experimental results demonstrated that 
- the proposed MCA improved performances of different models (TSM, SlowFast, and Uniformer) for different datasets (SSv1/v2, UCF101, HMDB51),
- and outperformed other augmentation methods such as Cutout and CutMix.

### Strengths
It is interesting that changing hue of video frames is a pretty simple and channels swap is very fast to compute even on CPU, nevertheless the proposed MCA provides performance improvements on common action recognition datasets.
It might become a practical standard for endusers as it is easy to use and implement.

### Weaknesses
The main weakness of the paper is the lack of solid motivation.

Insufficient survey

The paper says “there has been a lack of studies for data augmentation methods in video recognition” in section 2, however, there a lot of works such as follows.

* Mitigating and Evaluating Static Bias of Action Representations in the Background and the Foreground, ICCV2023
* Learning representational invariances for data-efficient action recognition. 2023 CVIU
* Frequency Selective Augmentation for Video Representation Learning, AAAI 2023
* Enabling Detailed Action Recognition Evaluation Through Video Dataset Augmentation, NeurIPS 2022
* Learn2Augment: Learning to Composite Videos for Data Augmentation in Action Recognition, ECCV 2022
* ObjectMix: Data Augmentation by Copy-Pasting Objects in Videos for Action Recognition, MMAsia22
* Exploring Temporally Dynamic Data Augmentation for Video Recognition, arXiv 2022
* VideoMix: Rethinking Data Augmentation for Video Classification, arXiv 2020

Table 3 shows comparisons with other augmentation methods, however, which are for images. It should be better to compare other video augmentation methods for comparisons as the proposed method is for videos.

In addition, these prior works have tried to tackle the background bias or scene bias (similar to “static appearance” in page 2), which exists in action recognition datasets. It should be better to discuss how the proposed method can contribute to solve the issue.



Weak motivation for hue jittering: The paper says “Among them, Color Jittering is widely used to transform color attributes like saturation, brightness, and contrast” in the introduction. Indeed it is true, but there are a tens of methods for augmentations implemented in famous libraries such as imageaug, albumentations, and kornia. However, there is no discussions or evidences why hue jittering is so important to explore.

Weak motivation for backbone model: Experiments used TSM, a 3D CNN with shift modules, however it is merely one of a vast amount of models for action recognition. Other models (slowfast and uniformer) are used but not for all datasets. It should be justified why TSM is the best for demonstrating the effect of the proposed method. Otherwise, recent methods (such as ones  referred in the paper) should also compared.


Minor comments:

Channel swap: Swapping channels for augmentation is not new and have been implemented in libraries.
https://kornia.readthedocs.io/en/latest/augmentation.module.html#kornia.augmentation.RandomChannelShuffle
https://albumentations.ai/docs/api_reference/full_reference/#albumentations.augmentations.transforms.ChannelShuffle


Definitions: Affinity, Diversity, and high Expected Calibration Error (ECE) are mentioned in the paper, and only Affinity is defined. However, ECE only is shown in experiments (affinity may be from Fig5 indirectly).

### Questions
Questions are same as above; comparisons and motivations.

Figure 5 shows TSM with SwapMix, and the performance drops to about 42%. However in Table 5, TSM+SwapMix shows performance over 46%. Why this happens ?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor
