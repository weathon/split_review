# Diffusion Curriculum: Synthetic-to-Real Data Curriculum via Image-Guided Diffusion

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 3, 5

## Abstract
Low-quality or scarce data has posed significant challenges for training deep neural networks in practice. While classical data augmentation cannot contribute very different new data, diffusion models opens up a new door to build self-evolving AI by generating high-quality and diverse synthetic data through text-guided prompts. However, text-only guidance cannot control synthetic images' proximity to the original images, resulting in out-of-distribution data detrimental to the model performance. To overcome the limitation, we study image guidance to achieve a spectrum of interpolations between synthetic and real images. With stronger image guidance, the generated images are similar to the training data but hard to learn. While with weaker image guidance, the synthetic images will be easier for model but contribute to a larger distribution gap with the original data. The generated full spectrum of data enables us to build a novel "Diffusion CurricuLum (DisCL)". DisCL adjusts the image guidance level of image synthesis for each training stage: It identifies and focuses on hard samples for the model and assesses the most effective guidance level of synthetic images to improve hard data learning. We apply DisCL to two challenging tasks: long-tail (LT) classification and learning from low-quality data. It focuses on lower-guidance images of high-quality to learn prototypical features as a warm-up of learning higher-guidance images that might be weak on diversity or quality. Extensive experiments showcase a gain of 2.7$\%$ and 2.1$\%$ in OOD and ID macro-accuracy when applying DisCL to iWildCam dataset. On ImageNet-LT, DisCL improves the base model's tail-class accuracy from 4.4$\%$ to 23.64$\%$ and leads to a 4.02$\%$ improvement in all-class accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a curriculum learning (CL) method that leverage synthetic image generation as data augmentation in combination with CL algorithm to tackle data-challenging tasks, e.g., long-tailed and low-quality distribution learning. The proposed method, DisCL, generattes images using both text and real images conditioning, with various image guidance scales to regulate the similarity to the real image, allowing for control over the hardness/complexity of the generated sample. CL is applied to select which complexity of samples (image guidance scale) to use based on the task at hand, e.g., for long tail learning an diverse-to-specific CL algorithm is used, while for low-quality image learning an adaptive algorithm is used. A first set of experiments compare DisCL versus baselines using data augmentation or balanced softmax for long tailed classification, showing positive impact mostly on less represented classes. A second set of experiments, test DisCL in the task of low-quality images using the iWildCam dataset. Here, DisCL is plugged to state-of-the-art fine-tuning techniques to show improved performance on both out-of-distribution and in-distribution examples.

### Strengths
- The method is simple and seems to work for both long-tailed and low-quality image classification.

### Weaknesses
1. Lacking of some relevant related works. The method does not mention nor compare against methods that already tried to leverage synthetic data as data augmentation to cope with unbalanced data, e.g., Hemmat-Askari et al 2023, or for representation learning / classification e.g., Tian et al 2024a and 2024b, Astolfi et al 2023. In particular, Hemmat-Askari et al 2023 seems quite related as they target the same task and use similar synthetic data generation approach while having some sort of adaptive curriculum learning (feedback guidance) which regulates the type of generation needed by the model. It would be nice to understands how DisCL compare against it. Finally, ALIA ( Dunlap et al 2023) is mentioned as a related work and a baseline in 3.1.2, but never presents in the results.

2. Weak / unclear experimental settings:
    - Resnet-10 choice is motivated for the comparison with LDMLR; However, most of the comparisons are with CUDA, which uses resent-32 for CIFAR-100 and resenet-50 for ImageNet. Do you expect you results to hold with these larger resnet?
    - Some experimental details are unclear to me. 
        - it is not clear to me whether baselines and DisCL are trained for the same amount of iterations/epochs. 
        - In the training details the authors say: _"To preserve a constant imbalance-ratio throughout all training stages and experiments, we undersample the non-tail samples at \"each stage\" so that ratio of tail-samples to non-tail samples matches the proportion of tail classes to non-tail classes present in the original data (13.6%)."_. If I am reading this correctly the authors say that they prefer to maintain imbalanced the dataset, despite having the possibility to rebalancing it with synthetic data. Why this choice?
        - The results on ImageNet-LT show small improvements w.r.t. to balanced softmax (BS) baseline (+1.5%). By looking at Hemmat-Askari et al 2023 results, the BS baseline is outperformed by a large marging. I understand that the number of generated data on Hemmat-Askari et al is on another scale (1.3M vs. 25K). Do you think the scale is enough to justify this difference?  
        - Also, combining BS with DisCL sometimes leads to lower results than CE + DisCL (see Table 2). Is there any intuition why BS does seem to be as effective for DisCL
        - Bolding in table 2 is inconsistent

### Questions
Please respond to the weaknesses listed. Given the many clarification required I consider this work below the acceptance bar.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper tries to incorporate the curriculum learning technique into image data augmentation. 

This paper evaluated the proposed method on two tasks: long-tail classification and image classification with low-quality data to show the effectiveness.

Contribution: This paper reveals that curriculum learning is a way to balance synthetic data with various quality and real data.

### Strengths
1. The experiment is well designed.
2. The visualization is good.
3. A substantial improvement has been achieved for some tasks.
4. Combine the curriculum learning into generative data augmentation.

### Weaknesses
1. In line 87, "We harness image guidance in diffusion models to create a spectrum of synthetic-to-real data". I don't think this is a contribution of yours. In ICLR 2023, one paper called "IS SYNTHETIC DATA FROM GENERATIVE MODELS READY FOR IMAGE RECOGNITION?" has already proposed to leverage both image and text guidance for data augmentation, and there are a lot of following works.

2. In the method part, most words are recalling the diffusion theory and image-text guidance, which are both not your contribution. I think the main contribution is how to leverage the various quality data with curriculum learning. However, the Sec. 3.2 is quite short and simple.

3. In the ablation part of Table 1, compared with CE + Text-only Guidance (39.10% overall accuracy) and All-Level Guidance (39.40% overall accuracy), the CE + DisCL gets very limited improvement.

### Questions
In the Table 2 and Table 3, can you provide the results of CE + Text-only Guidance and CE + All-Level Guidance.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Training deep learning models with low-quality or limited amounts of data often results in overfitting or suboptimal performance. To overcome this challenge, data augmentations have been an integral part of training deep learning models. However, classical data augmentations offer limited diversity and may also result in out-of-distribution samples, hampering the performance of the model. Therefore, recent research has focused on using generative models for data augmentations. Building in this direction, the authors propose a method to create a spectrum of interpolations between synthetic and real images called Diffusion Curriculum (DisCL). Focusing on the long-tail classification and learning from low-quality data tasks, the author demonstrates the efficacy of DisCL.

### Strengths
- The authors address the gap between real and synthetic data generated using diffusion models by designing a generative curriculum that can adjust the quality, diversity, and difficulty of the data for different training stages. This provides a new perspective on generative data augmentation, given that the majority of prior work considered a fixed image guidance scale throughout the training.
- The effectiveness of generative data augmentation strategies primarily depends on the performance of the generative model. To address the potential shortcomings of the generative models and thereby improve the effectiveness of the data augmentation, the authors proposed using CLIPScorer to filter out low-fidelity images.

### Weaknesses
 - The paper is difficult to follow. This is partly because key details are missing in the main paper. For instance, in Section 4.1, the authors mention the use of a set of diverse textual prompts, while the details are deferred to the appendix. Another instance is in Section 4.2, where the authors mention that inspired by DoCL, they propose an adaptive curriculum. However, there is no discussion of the proposed adaptive curriculum in that section. The lack of clarity regarding the specific implementation of the adaptive curriculum makes it difficult to assess the novelty and effectiveness of the proposed approach. Furthermore, the paper would benefit from a more detailed explanation of how the diverse prompts are generated and how they contribute to the overall performance.
- The concept that the choice of the starting timestep $t$ controls the impact of $z_{real}$ has been extensively studied in prior works, notable being SDEdit [1]. Therefore, it would be easier for the readers to follow if the authors cite the existing works and explain the similarities. The paper does not adequately discuss the relationship between the proposed method and the existing literature on controlling the influence of real images in diffusion models through manipulation of the starting timestep. A more detailed discussion of how the proposed method builds upon or differs from SDEdit [1] would be beneficial.
- Using generative models for data augmentation has been an active area of research, with many approaches proposed in the literature [2,3,4,5]. The authors can compare their approach with these existing works to substantiate their novelty and demonstrate the impact of using a pre-defined or adaptive generative curriculum. The current evaluation is limited. The paper lacks a thorough comparison with existing data augmentation techniques using generative models. Specifically, it would be beneficial to see a comparative analysis against methods that employ fine-grained modifications, local sampling, hard negative generation, and diverse synthetic data generation. The current evaluation does not clearly demonstrate the advantages of the proposed curriculum-based approach over existing methods.

### Questions
- Are ‘diverse to specific’ and ‘easy to hard’ curriculum strategies the same? If so, why are they called differently?
- In Table 1, for the “Few” class, the impact of DisCL is more significant when using Cross Entropy compared to when Balanced Softmax is used. Why?
- One of the benchmarks for learning from low-quality data is ALIA. Which Table contains the results with ALIA?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the challenge from training computer vision models (image classification task) with low-quality or scarce data. The paper proposes Diffusion Curriculum (DisCL) which leverages diffusion models to synthesize hard image examples data with different guidance scales and then utilizes a Generative Curriculum Learning to select appropriate synthetic data from the full spectrum of generated data for training data augmentation.  Experiments are conducted on two tasks: long-tail classification and learning from low-quality data, to show the method's effectiveness.

### Strengths
1. The idea of adjusting guidance scales to obtain a greater variety and quality of training data augmentation is interesting and novel.
2. Generative Curriculum Learning is reasonable and can adjust for different tasks.
2. The proposed method proves its effectiveness in both experiments in long-tail classification and learning from low-quality data.

### Weaknesses
1. A tradeoff is the speed of generating a full spectrum for images.  For large datasets, the diffusion models can consume a long time to generate a full spectrum of needed images.

2. I am concerned about using only the pre-trained stable diffusion model without further fine-tuning (I am happy to update the rating if the following questions are addressed).
  1. Were there any observed biases/failures in the synthetic data generated for small resolution datasets (For example CIFAR100-LT)? I am concerned because of the resolution differences between the CIFAR100-LT dataset and the resolution stable diffusion model is trained on.
  2. In real-life scenarios, some datasets we want to train the models are not real photographs, do you think a pre-trained diffusion model and your proposed method can be effective for Long-Tailed or low-quality datasets in domains of Comics, Drawings, etc?
  3. Using Clip score as a threshold to filter out generated images is reasonable but for some classes, it can be easy to filter out too many generated data from pretrained stable diffusion (therefore not a full spectrum of data can be generated and saved). May I ask if this situation also occurs in your experiments and could you provide the percentage of filtered images and any strategies you employed to ensure sufficient data?

### Questions
I am concerned about using only the pre-trained stable diffusion model without further fine-tuning (I am happy to update the rating if the following questions are addressed).
1. Were there any observed biases/failures in the synthetic data generated for small resolution datasets (For example CIFAR100-LT)? I am concerned because of the resolution differences between the CIFAR100-LT dataset and the resolution stable diffusion model is trained on.
2. In real-life scenarios, some datasets we want to train the models are not real photographs, do you think a pre-trained diffusion model and your proposed method can be effective for Long-Tailed or low-quality datasets in domains of Comics, Drawings, etc?
3. Using Clip score as a threshold to filter out generated images is reasonable but for some classes, it can be easy to filter out too many generated data from pretrained stable diffusion (therefore not a full spectrum of data can be generated and saved). May I ask if this situation also occurs in your experiments and could you provide the percentage of filtered images and any strategies you employed to ensure sufficient data?

### Soundness
3

### Presentation
3

### Contribution
3
