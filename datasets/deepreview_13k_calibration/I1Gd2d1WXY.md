# Adaptive Resolution Residual Networks

- Decision: Reject
- Avg Score: 3.75
- Scores: 6, 3, 3, 3

## Abstract
The majority of deep learning methods for signals assume a fixed signal resolution during training and inference, making it impractical to apply a single network at various signal resolutions. We address this shortcoming by introducing Adaptive Resolution Residual Networks (ARRNs) that implement two novel components: Laplacian residuals, which define the structure of ARRNs and allow compressing high-resolution ARRNs into low-resolution ARRNs, and Laplacian dropout, which improves the robustness of compressed ARRNs through a training augmentation. We formulate Laplacian residuals by combining the properties of standard residuals and Laplacian pyramids. Thanks to this structure, lower resolution signals require a lower number of Laplacian residuals for exact computation. This adaptation greatly reduces the computational cost of inference on lower resolution signals. This adaptation is effectively instantaneous and requires no additional training. We formulate Laplacian dropout through the converse idea that randomly lowering the number of Laplacian residuals is equivalent to randomly lowering signal resolution. We leverage this as a training augmentation that has the effect of improving the performance of the many low-resolution ARRNs that can be derived from a single high-resolution ARRN. We provide a solid theoretical grounding for the advantageous properties of ARRNs, along with a set of experiments that demonstrate these properties in practice.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Adaptive Resolution Residual Networks (ARRNs) to process signals at different resolutions. The proposed method contains two components: Laplacian residuals and Laplacian dropout. The authors show effectivenss of the proposed method mainly on CIFAR dataset at relatively low resolution.

### Strengths
1. Having a single network to process images at various resolutions is an important research topic.
2. The paper is well-written and figures are clear. The proposed method is well-motivated, lower resolution signals require a lower number of Laplacian residuals provides a natural and intuitive way to reduce the computational cost.
3. The proposed method is compared to many different prior architectures.

### Weaknesses
1. The experiments only show results for images at resolution less than 32, which is not very practical as real-world images to process are usually at much higher resolutions in applications. The lack of evaluation on higher resolution images limits the practical applicability of the proposed method. Specifically, the performance of the Laplacian residual and dropout mechanisms at resolutions such as 256 or 512, which are more common in real-world scenarios, is not explored. This makes it difficult to assess the method's scalability and effectiveness in practical settings.
2. The current experiments are mainly on CIFAR, more diverse datasets could make the results more convincing. The reliance on a single dataset, even with different resolutions, limits the generalizability of the findings. The method's performance on datasets with different characteristics, such as those with more complex textures, varying object sizes, or different types of noise, is unknown. This lack of diversity raises concerns about the robustness of the proposed approach.
3. Typo: page 1, bottom - "illustrated in ??"

### Questions
What are the main challenges to make the proposed method work for images at a more practical resolution? (e.g. around 256 in ImageNet)

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a resolution adaptive network that compress high-resolution image to low-resolution, they also propose Laplacian residuals. The authors claim that the proposed structure, namely residual plus Laplacian pyramids, greatly reduce computational cost on low resolution signals.

### Strengths
Using laplacian residual to replace standard residuals in cnn is an interesting and reasonable approach. 
The writing is ok.

### Weaknesses
1. The most fatal weakness is the experiments. As a paper that specifically discusses image resolution of neural networks, the largest resolution in the experiments is 32 \times 32. The cifar is not a suitable dataset to evaluate ARRN
Notice that a standard ImageNet setting has resolution of 224 \times 224, and many sota works have trained and evaluated on the resolution of 384 \times 384. The lack of experiments on higher resolution datasets severely limits the impact of this work, as it is unclear how the proposed method would scale to more realistic image sizes.

2. The novelty is limited. As said in the related work, this work is merely an extension of Lai 2017 & Singh 2021, which applies Laplacian pyramids to signal resolution. While the application of Laplacian residuals to CNNs is interesting, the core idea of using Laplacian pyramids for resolution adaptation is not novel in itself. The paper does not sufficiently demonstrate a significant departure from these previous works.

3. The inference time in Figure 7, from my experience, is overwhelming, given the resolution is 32 \times 32 at most. I'm not sure if this is the implementation or hardware problem, therefore i suggest the author provide a comparison between standard residual and laplacian residual. The lack of a clear benchmark against standard residual networks makes it difficult to assess the true efficiency of the proposed method.

### Questions
See weakness. 
Page 1, second last row has an incorrect citation.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
To address most deep learning methods for signals that assume a fixed signal resolution during training and inference, this paper proposes Adaptive Resolution Residual Networks (ARRNs). The networks include Laplacian residuals and Laplacian dropout. The Laplacian residuals allow the compressing of high-resolution ARRNs into low-resolution ARRNs, and the Laplacian dropout improves the robustness of compressed ARRNs through training augmentation. The experiments demonstrate the effectiveness of the proposed method.

### Strengths
This paper proposes Adaptive Resolution Residual Networks (ARRNs) which can be used at various signal resolutions. To this end, the authors propose Laplacian residual and Laplacian dropout.

### Weaknesses
1. The authors do not investigate sufficient related work.
2. The experiments section should be improved.

1.  Some related studies are necessary.  The authors state that "The majority of deep learning methods for signals assume a fixed signal resolution during training and inference" There are many networks [1-4] that do not have such an assumption and they can be trained with different resolution inputs. It would be better to discuss these papers.

[1] Learning continuous image representation with local implicit image function.  
[2]  Local texture estimator for implicit representation function.  
[3] Implicit transformer network for screen content image continuous super-resolution.  
[4] CiaoSR: Continuous Implicit Attention-in-Attention Network for Arbitrary-Scale Image Super-Resolution.  

2. The authors highlight that it is impractical for the majority of deep learning methods to apply a single network at various signal resolutions. Could you provide some examples of such application scenarios in the paper?

3. The experiments are not sufficient. The authors mainly conduct experiments on image classification on CIFAR10 and CIFAR100. It is not convincing that the proposed method does not hinder performance or require re-training. The authors should conduct more experiments on ImageNet with more neural networks. In addition, can the ARRNs used in other tasks, e.g., super-resolution?

4. On the first page, in the third paragraph of the introduction, there is an issue: illustrated in ??

### Questions
1. Some related studies are necessary.  The authors state that "The majority of deep learning methods for signals assume a fixed signal resolution during training and inference" There are many networks [1-4] that do not have such an assumption and they can be trained with different resolution inputs. It would be better to discuss these papers.

[1] Learning continuous image representation with local implicit image function.  
[2]  Local texture estimator for implicit representation function.  
[3] Implicit transformer network for screen content image continuous super-resolution.  
[4] CiaoSR: Continuous Implicit Attention-in-Attention Network for Arbitrary-Scale Image Super-Resolution.  

2. The authors highlight that it is impractical for the majority of deep learning methods to apply a single network at various signal resolutions. Could you provide some examples of such application scenarios in the paper?

3. The experiments are not sufficient. The authors mainly conduct experiments on image classification on CIFAR10 and CIFAR100. It is not convincing that the proposed method does not hinder performance or require re-training. The authors should conduct more experiments on ImageNet with more neural networks. In addition, can the ARRNs used in other tasks, e.g., super-resolution?

4. On the first page, in the third paragraph of the introduction, there is an issue: illustrated in ??

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposes the ARRN, which is a network architecture designed to address the problem of signal resolution variation in machine learning tasks. It uses Laplacian residual connections to adapt the resolution of models quickly, reducing computation as resolution decreases. ARRNs also incorporate Laplacian dropout to enhance the networks' robustness to low-resolution signals. This allows for training high-resolution ARRNs that can later be compressed into effective low-resolution ARRNs.

### Strengths
1.	The idea is simple and clear.
2.	The experiments show the effectiveness of the proposed algorithm.
3.	The proposed algorithm has low computational cost and without requiring retraining.

### Weaknesses
1.	The practicability of the algorithm is not very reliable. One issue is that the algorithm can only deal with the sizes contained in the feature maps. The other is that the performance of the algorithm will drop quickly without residual dropout.
2.	The experiments cannot show the advantages of the proposed approach. See the questions below.

### Questions
1.	The application scenario of the algorithm is not clear. Because the proposed algorithm can only deal with the resolutions contained in feature maps, and the paper only verifies it on very small images (e.g, 32x32), it cannot explain the effectiveness of the algorithm.
2.	Without the residual dropout, the effectiveness of the algorithm will be poor. This is related to the content described in subsection 4.2. It is not clear whether residual dropout leads to better performance or the laplacian residuls introduced in subsection 4.2. 
3.	The paper does not compare with networks that adapt to resolution, but only with the approach of upsampling the low-resolution inputs. This cannot explain the superiority of the algorithm.
4.	How to set the filter kernels \phi^{low}_n?
5.	There is a missing of reference in page 1. In the first paragraph of subsection 3.1, there are two successive “ideal”.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
