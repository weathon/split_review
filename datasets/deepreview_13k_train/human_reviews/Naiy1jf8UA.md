# MGDC-UNet: Multi-group Deformable Convolution for Medical Image Segmentation

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Recently, there has been growing interest in developing Vision Transformer (ViT) or Convolutional Neural Network (CNN) methods for 3D medical image segmentation, which necessitates both large receptive fields and adaptations to varying spatial geometries. Previous works in both CNNs and ViTs demonstrated limitations in capturing the complex spatial and semantic structure of 3D medical images. In this paper, we introduce MGDC-UNet, a multi-group deformable convolution network for 3D volumetric medical image segmentation. Our MGDC-UNet employs deformable convolution operators with learnable spatial offsets to improve attention on semantically important regions. Our approach leverages stable spatial distribution across subjects to enhance semantic learning. We also incorporate transformer components to augment feature learning and reduce inductive biases inherent in traditional CNNs. MGDC-UNet demonstrated superior performance accuracy on three challenging segmentation tasks using public datasets: 1). brain tumor segmentation (BraTS21), 2). CT multi-organ segmentation (FLARE21) and 3). cross-modality MR/CT segmentation (AMOS22). Our network also compared favorably with existing methods in terms of computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
MGCD-UNet is introduced in this paper as a multi-group deformable convolution network for 3D volumetric image segmentation. The network modifies UNet by using deformable convolution operators, learnable spatial offsets, and a transformer-like architecture. The aim of this work is to address the limitations in semantic learning, especially with long-term dependencies, attention to important areas, inductive biases, stability, and complexity. The method was tested on three segmentation datasets where it demonstrated superior performance.

### Strengths
The paper addresses a challenging problem in medical image segmentation, and it demonstrates improvement in the three tested datasets in terms of accuracy.

### Weaknesses
The novelty of the paper is very limited as the method is a combination of many widely used techniques. Specifically, on page 5, the authors claim to develop a new architecture that includes a reverse bottleneck; however, this design is just similar to the inverted residual block used in MobileNetV2 [1]. Also, the authors mention on page 2 that they have developed a deformable convolution approach for 3D volumetric images, however, 3D deformable convolution has been applied before for videos in [2]. Moreover, the authors claim on page 3 that their method is improving computational efficiency, however, the only component that seems to decrease complexity is the depth-wise convolution. Following that, many components are added such as linear layers, SoftMax, transformer components, and an extra loop over “groups” which adds to the complexity of the network. Tables 1 and 2 suggest that there is not much improvement in time and memory usage as other methods are comparable in performance (SegResNet inference time is 0.78 with memory usage of 3.3G while MGDC-UNET has inference time of 2.08 with 9.4G memory). 
Time and memory usage were not mentioned in Table 3 which is inconsistent with the previous tables. 
In Figure 1, we can clearly see that self-attention is comparable to the proposed MGDC. Figure 3 suggests a very small improvement but not significant. Similarly, in Figures 4 and 5, the improvement does not seem significant. 
On page 6, the authors claim that increasing kernel size from 3 to 7 causes enhancements, however, some results in Table 2 disprove this claim.
The title is too general and gives a sense that the method is tested on many image segmentation tasks to prove its applicability, however, the method is only tested on 3 datasets, and it is not generalizable.

### Questions
Please refer to the above concerns.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduced MGDC-UNet, a multi-group deformable convolution network for 3D volumetric medical image segmentation. MGDCUNet employs deformable convolution operators with learnable spatial offsets to improve attention on semantically important regions. Meanwhile, they leverage stable spatial distribution across subjects to enhance semantic learning. In addition, they also incorporate transformer components to augment feature learning and reduce inductive biases inherent in traditional CNNs.

### Strengths
The network can adaptively adjust the offset of sampled locations, concentrating its attention on semantically relevant organ positions. Furthermore, the authors dynamically adjust offsets and modulation scalars to mitigate the inductive biases inherent in traditional CNNs, achieving transformer-like spatial aggregation. Also introduced MGDC blocks with a hybrid deformable convolution and multi-layer perceptron (MLP) structure for effective channel scaling and enhanced feature learning.

### Weaknesses
1. The originality of the algorithm's contribution remains ambiguous. Both deformable convolution and MLP are well-established application techniques, and while the authors have successfully combined them to achieve improved performance, their original contribution appears relatively modest. The specific manner in which the multi-group mechanism is integrated with deformable convolution is not sufficiently detailed, making it difficult to assess the novelty of this combination. It is unclear how this specific configuration differs from existing uses of grouped convolutions with deformable kernels.

2. More experimental details should be provided to facilitate replication of the proposed method as well as a fair assessment of the performance of all comparison methods, e.g. batch size, learning rate, loss function, etc. The lack of specific hyperparameter details makes it challenging to reproduce the results and verify the claims. For instance, the learning rate schedule, optimizer details, and specific loss function parameters are all missing.

3. The authors should have given more details about the data strategy, how the training dataset, validation set, and test set were divided, and how the optimal model was selected for performance comparison. It is not clear how the 5-fold cross-validation was implemented. The exact splits used for training, validation, and testing within each fold, as well as the criteria for selecting the best model from each fold, are not specified.

4. The datasets utilized in the experiments of the paper all feature objects with clear boundaries that are easy to segment. Given the authors' claim that their method can better capture complex pathological features, for a more comprehensive evaluation of the algorithm's performance, it would be advisable for the authors to attempt performance assessment on datasets with complex pathological and morphological characteristics, such as retinal OCT image segmentation, for example the dataset of RETOUCH -The Retinal OCT Fluid Detection and Segmentation Benchmark and Challenge.

### Questions
1. The originality of the algorithm's contribution remains ambiguous. Both deformable convolution and MLP are well-established application techniques, and while the authors have successfully combined them to achieve improved performance, their original contribution appears relatively modest.
2. More experimental details should be provided to facilitate replication of the proposed method as well as a fair assessment of the performance of all comparison methods, e.g. batch size, learning rate, loss function, etc.
3. The authors should have given more details about the data strategy, how the training dataset, validation set, and test set were divided, and how the optimal model was selected for performance comparison.
4. The datasets utilized in the experiments of the paper all feature objects with clear boundaries that are easy to segment. Given the authors' claim that their method can better capture complex pathological features, for a more comprehensive evaluation of the algorithm's performance, it would be advisable for the authors to attempt performance assessment on datasets with complex pathological and morphological characteristics, such as retinal OCT image segmentation, for example the dataset of RETOUCH -The Retinal OCT Fluid Detection and Segmentation Benchmark and Challenge.

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
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces MGDC-UNet, a method for 3D volumetric medical image segmentation that combines multi-group deformable convolution with transformer components. The goal is to address limitations in capturing complex spatial and semantic structures inherent in existing methods. MGDC-UNet employs deformable convolution operators with learnable spatial offsets, enhancing attention on semantically important regions. The approach leverages the stable spatial distribution across subjects to improve semantic learning.

While MGDC-UNet demonstrates superior accuracy on three challenging segmentation tasks—brain tumor segmentation (BraTS21), CT multi-organ segmentation (FLARE21), and cross-modality MR/CT segmentation (AMOS22)—it does have some limitations. 

The novelty of the multi-group deformable convolution might be somewhat constrained, as it's a widely used technique in segmentation. In Figure 1, the results suggest that the proposed method's performance is comparable to self-attention. Similarly, in Figure 3, the results indicate that MGDC-UNet may not significantly outperform previous methods.

### Strengths
MGDC-UNet demonstrates superior accuracy on three challenging segmentation tasks.

### Weaknesses
The novelty of the multi-group deformable convolution might be somewhat constrained, as it's a widely used technique in segmentation. In Figure 1, the results suggest that the proposed method's performance is comparable to self-attention. Similarly, in Figure 3, the results indicate that MGDC-UNet may not significantly outperform previous methods.

### Questions
See comments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
They introduce MGDC-UNet, a multi-group deformable convolution network for 3D volumetric medical image segmentation. Their MGDCUNet employs deformable convolution operators with learnable spatial offsets to improve attention on semantically important regions.


They use three challenging segmentation tasks using public datasets: 

1) brain tumor segmentation (BraTS21)

 2)  CT multi-organ segmentation (FLARE21) 

 3)  cross-modality MR/CT segmentation (AMOS22)

MGDC-UNet demonstrated superior performance accuracy in the three challenging segmentation tasks.

### Strengths
Well organized and clearly written.

The effectiveness of proposed method has been well supported by experiments.

### Weaknesses
The did not mention the limitation of their method.

They did not add results of their model for small dataset like MRBrainS dataset and MICCAI iSEG dataset (minor issue).

### Questions
could you change your title?  Because (This paper only uses the three datasets, and it cannot represent all medical image segmentation tasks.)

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
