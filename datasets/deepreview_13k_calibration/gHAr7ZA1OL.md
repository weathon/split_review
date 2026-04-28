# Modulated Phase Diffusor: Content-Oriented Feature Synthesis for Detecting Unknown Objects

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
To promote the safe deployment of object detectors, a task of unsupervised out-of-distribution object detection (OOD-OD) is recently proposed, aiming to detect unknown objects during training without reliance on any auxiliary OOD data. To alleviate the impact of lacking OOD data, for this task, one feasible solution is to exploit the known in-distribution (ID) data to synthesize proper OOD information for supervision, which strengthens detectors' discrimination. From the frequency perspective, since the phase generally reflects the content of the input, in this paper, we explore leveraging the phase of ID features to generate expected OOD features involving different content. And a method of Modulated Phase Diffusion (MPD) is proposed, containing a shared forward and two different reverse processes. Specifically, after calculating the phase of the extracted features, to prevent the rapid loss of content in the phase, the forward process gradually performs Gaussian Average on the phase instead of adding noise. The averaged phase and original amplitude are combined to obtain the features taken as the input of the reverse process. Next, one OOD branch is defined to synthesize virtual OOD features by continually enlarging the content discrepancy between the OOD features and original ones. Meanwhile, another modulated branch is designed to generate augmented features owning a similar phase as the original features by scaling and shifting the OOD branch. Both original and augmented features are used for training, enhancing the discrimination. Experimental results on OOD-OD, incremental object detection, and open-set object detection demonstrate the superiorities of our method. The source code will be released at https://github.com/AmingWu/MPD.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the out-of-distribution object detection (OOD-OD) task, and proposes a method named MPD to tackle it from the frequency perspective. Following the previous method VOS that alleviates the OOD-OD problem by adaptively synthesizing virtual outliers, MPD also attempts to synthesize suitable virtual OOD features as well as generate augmented features for supervised training. Different from VOS that assumes a class-conditional multivariate Gaussian distribution of the feature space, MPD in this paper tries to add noise to the phase domain in the diffusion way. Moreover, the authors find that the Gaussian Average for processing each step is better than directly adding noise. Many experiments and ablation studies have verified that MPD is superior than previous methods for dealing with OOD-OD.

### Strengths
I think this paper has at least the following several major contributions:

1. The authors approach the OOD-OD problem from the phase domain of the extracted image features, which is an aspect that is interesting and rarely studied.

2. Introducing diffusion to generate different features is a new attempt in OOD. After discovering that simply and directly adding noise according to the original method was problematic, the authors proposed their own effective improvement strategies.

3. Quantitative experimental results prove the advancement of MPD in many OOD-OD benchmarks.

### Weaknesses
Similarly, we summarize the weaknesses of this paper as follows:

1. Actually, studying the processing of features from a phase perspective is not the first of its kind in this paper. In other words, the method [1] has proven that phase-related features are content-oriented in the DG field, which is very similar to OOD. This paper directly uses such a conclusion of DG in OOD and cannot be regarded as a complete innovation.

2. Generally speaking, there are quite a few steps in the continuous transformation of the Diffusion model, such as dozens or even hundreds of steps. The method in this paper seems to only use up to 4 interations (T=4 in Table 5). Why not try more steps? Is it because more parameters are introduced (such as the U-Net model for predicting feature maps, and two branches for generating new features in OOD) that it is inconvenient to increase T to a too large number? If so, the authors need to explain clearly how the new method MPD increases the number of parameters compared to the original basic detector, such as the used Faster R-CNN.

3. As we all know, Faster R-CNN is a classic but outdated detector. It gives a weak baseline of detection comparing to recent new ones. The actual value of OOD-OD is to achieve robust and generalizable object detection in real applications. Thus, using advanced basic detectors such as YOLOv5 [2], YOLOv8 [3], TOOD [4] and DETRs is more meaningful. And it will be important to see if the proposed MPD works or not on these superior detectors. It may not be practical to do more experiments. The authors could give similar explanations and discussions. For example, is MPD universal to these superior detectors?

### Questions
Overall, the method proposed in this paper is innovative and effective. Please go back to the two questions I mentioned in the weaknesses of items 2 and 3. Let me shorten these two questions as below:
1. How the proposed MPD increases the number of network parameters?
2. How about using advanced basic detectors instead of the outdated Faster R-CNN?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on the OOD object detection problem and propose to detect unknown object without relying on auxiliary OOD data. This paper exploits ID data to generate OOD data by considering the phase information in frequency spectrum. A modulated phase diffusion (MPD) is designed, with some detailed forward and reverse compuation. Experiments on several tasks show the effectiveness.

### Strengths
+The proposed technical framework sounds good, by leveraging frequency information, U-net and augmented features.
+ Experimental results are comparable to previous SOTA models.

### Weaknesses
 - This paper writting has a large space for improvement and not easy to follow. Although the authors presented the main motivations of this paper, there are still many places unclear. The phase information of ID features is used to generate OOD features. Since phase represents more the content, the amplititude information may be more important for different styles (OOD featuers).
-The motivation on the augmented features (ID or OOD?) is not estabilished. It is unclear why these augmented features are needed, and how they contribute to the overall goal of OOD detection. The paper does not clearly articulate the specific role of these features in the training process and how they help the model distinguish between ID and OOD samples.
-What is the difference between OOD-OD and open-set OD? The authors seem list them as different. But as I see, they are the same problem. The paper needs to clarify the subtle differences, if any, between these two problem settings, as they both deal with detecting objects from unknown classes. A more detailed discussion of the nuances of each problem is needed to justify treating them as separate entities.
-The forward and reverse process are not clear due to the poor writting. The description of the modulated phase diffusion (MPD) process is difficult to follow, making it hard to understand the technical details of the proposed method. The lack of clarity in the explanation hinders the reader's ability to grasp the core mechanism of the approach.
-Fig.1 and Fig.2 are redundant which evens show similar objective about the proposed MPD. Also, the designed method seems complex and not easy to follow. The paper would benefit from a more concise and streamlined presentation of the method. The redundancy in figures and the perceived complexity of the method make it challenging to understand the core contributions.
-I also concern about the claim "lacking unknown data". Since OOD-OD is problem setting, it is rational to suppose some categories are unknown, such as open-set OD. The paper's claim of lacking unknown data seems contradictory to the problem setting itself. It needs to clarify what is meant by "lacking unknown data" and how it relates to the OOD detection problem.
-Lacking the visualization results of phase based OOD data synthesis.

### Questions
1. How about the conventional unknown object detection based on a simple threshold, such as entropy based.
2. Minimizing the KL between ID and OOD is strange in Eq. 7.
3. In Eq. 9, there are many losses, which makes the training not easy.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript attempts to use the Diffusion model to solve the unsupervised out-of-distribution object detection (OOD-OD) task. This method uses two inverse processes to synthesize the phase information of unknown and known samples, respectively. The experimental results validate the effectiveness of the method.

### Strengths
1. Gradual phase averaging: Instead of adding noise, MPD gradually performs Gaussian averaging on the phase of extracted features. This helps to prevent rapid loss of content in the phase, ensuring that important information is preserved during the process.

2. Experimental superiority: MPD has demonstrated superior performance in various tasks, including OOD-OD, incremental object detection, and open-set object detection. The experimental results validate the effectiveness and advantages of the MPD method in promoting safe deployment of object detectors.

### Weaknesses
The idea of replacing Gaussian noise in the diffusion process with Gaussian average operation seems to be an experimental result, lacking theoretical explanation and formula derivation.

### Questions
1. Why choose to generate phase instead of the original image or amplitude? What are the phase advantages?
2. Why choose a 5x5 kernel for the Gaussian average? Has the author tried other types or sizes of kernels?
3. If Gaussian noise is replaced by the Gaussian average, is the diffusion model still valid? Can you provide the formula derivation?
4. The description of the OOD phase in Figure 2 is confusing, the meaning of approximately equal and not equal symbols is unclear.
5. What are the shortcomings of this method? Does its training and reasoning time have any advantages compared to previous methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
