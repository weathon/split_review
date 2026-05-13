# An Intuitive Multi-Frequency Feature Representation for SO(3)-Equivariant Networks

- Decision: Accept
- Scores: 5, 6, 6, 6, 6

## Abstract
The usage of 3D vision algorithms, such as shape reconstruction, remains limited because they require inputs to be at a fixed canonical rotation. Recently, a simple equivariant network, Vector Neuron (VN)~\citep{deng2021vector} has been proposed that can be easily used with the state-of-the-art 3D neural network (NN) architectures. However, its performance is limited because it is designed to use only three-dimensional features, which is insufficient to capture the details present in 3D data. In this paper, we introduce an equivariant feature representation for mapping a 3D point to a high-dimensional feature space. Our feature can discern multiple frequencies present in 3D data, which, as shown by~\cite{tancik2020fourier}, is the key to designing an expressive feature for 3D vision tasks. Our representation can be used as an input to VNs, and the results demonstrate that with our feature representation, VN captures more details, overcoming the limitation raised in its original paper.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper the authors propose a representation for point cloud data that can be used with the existing method [1] to improve expressivity while maintinaing equivariance to 3D rotations. The representation is constructed by transforming points to an axis-angle representation, then lifting that representation to a random subspace of SO(n). The subspace is defined by three matrices J_1, J_2, and J_3, where J_1 is a random vector in the Lie algebra of SO(n), and J_2 and J_3 (also in the Lie algebra) are matrices whose Lie bracket is close to J_1. The final SO(n) representation of a given point is the exponential map of the linear combination of J_1, J_2, and J_3, where the combination coefficients are determined by the axis-angle representation.

[1] Deng, Congyue, et al. "Vector neurons: A general framework for so (3)-equivariant networks." Proceedings of the IEEE/CVF International Conference on Computer Vision. 2021.

### Strengths
*Originality:* The proposed approach appears novel. Although other approaches have used a Fourier like representation to represent 3D objects [1,2,3], this approach differs from those in that 1) the representation is intentionally high-dimensional, 2) only a subspace of the high-dimensional space is considered.

*Quality:* In the experiments, proposed method performs on-par with or better than most baselines.

*Clarity:* (see weakness)

*Significance:* Designing expressive equivariant representations is a challenging and important problem in the field.


[1] Esteves, Carlos, et al. "Learning so (3) equivariant representations with spherical cnns." Proceedings of the European Conference on Computer Vision (ECCV). 2018.

[2] Cohen, Taco S., et al. "Spherical cnns." arXiv preprint arXiv:1801.10130 (2018).

[3] Kondor, Risi, Zhen Lin, and Shubhendu Trivedi. "Clebsch–gordan nets: a fully fourier space spherical convolutional neural network." Advances in Neural Information Processing Systems 31 (2018).

### Weaknesses
*Quality:*
* The authors' critique of methods using spherical harmonics appears somewhat misguided. While they position their work as more intuitive, the analogy they draw to the Fourier basis, which is fundamental in signal processing, suggests that spherical harmonics are a similarly well-established and valid approach. Furthermore, the assertion that spherical harmonics are solely derived from quantum mechanics is inaccurate; their application predates quantum mechanics by over a century. A more balanced perspective would acknowledge the historical significance and widespread use of spherical harmonics in various fields.
* The paper lacks a thorough analysis of the impact of choosing a higher-dimensional input representation space. Specifically, how does the choice of  `n` affect the model's performance, and what are the trade-offs in terms of computational cost? This is a critical aspect that needs further investigation and clarification.
* The notation used throughout the paper is inconsistent. For instance, the variables $\hat{u}$ and $\vec{u}$ appear to be used interchangeably in section 3, leading to confusion. A consistent notation would significantly improve the clarity of the paper.
* Certain proofs, particularly that of Proposition 1, are missing or inadequately addressed. The authors refer to the proof of Theorem 1 for the proof of Proposition 1, but the former does not sufficiently cover the latter. This omission needs to be rectified.

*Clarity:* The paper's presentation is challenging to follow, especially for readers not deeply familiar with advanced mathematical concepts like the Lie bracket. The authors introduce these concepts without providing adequate motivation or explanation, which hinders the overall understanding of the proposed method.

### Questions
*Questions:*
- What is meant by “$R^z(\hat{u})$ is a rotation matrix defining the orientation measured from the $z$-axis to $\hat{u}$.” Is it the 2D rotation about the axis $z \times \hat{u}$ that aligns the $z$-axis and $\hat{u}$?
- It seems like the map is from SO(3) to a subspace of SO(n) is that right
- Is the axis arbitrarily selected?
- Createsearchspace from Algo 2 is not described in the text, how does this work?

*Possible typos:*
- “Theorem 1. theoremIf” → “Theorem 1. If” 
- Are $\hat{u}$ and $\overrightarrow{u}$ used interchangeably in section 3? It would be clearer if the notation were consistent
- “intuitively, just like F1, F2 and F3 represent angles” → “intuitively, just like F1, F2 and F3 represent axes of rotation”
- Should “axes ψ(ˆx), ψ(ˆy), and ψ(ˆz)” be “axes ψ(F_1), ψ(F_2), and ψ(F_3)”? If not what does $\hat{.}$ mean here?
- “ effective-yet-rotation-equivariant” →  expressive yet rotation equivariant
- In section D, readers are referred to the proof of Thm 1 for the proof of Prop 1, but the proof of Thm 1 does not prove Prop 1.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a frequency-based input representation for Vector-Neuron for SO-3 equivariant network. It provides compelling evidence to support the claim of keeping equivariance with this input representation. Both visualized and numerical results demonstrate the effectiveness of the proposed method, thus validating its ability to achieve equivariant representations.

### Strengths
- The paper presents sufficient mathematical proofs, which provide robust support for the proposed representation. This strong evidence reinforces the credibility of the approach.
- The multi-frequency design demonstrates its effectiveness in terms of both visualization and benchmark performance. 
- The writing style and figures in the paper are great as they effectively elucidate the design and motivation behind the proposed representation. 
- The experiments conducted in the study convincingly demonstrate the effectiveness of the proposed method across various downstream tasks.

### Weaknesses
 - Lack of ablation studies
- (This is not a weakness) Does author try to extend the method on scene (indoor) ?

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper targets the challenging 3D representation problem and a new equivariant feature representation which can map 3D points to high-dimensional feature space is presented. The experimental results have been validated on several tasks like point-cloud completion, shape compression, normal estimation, point cloud registration, point cloud classification and segmentation. Reasonable results have been reported with a comparision with the existing work.

### Strengths
1. A new 3D representation is presented which can discern multiple frequencies in the 3D data. Also, it provides theretical justification of the proposed approach. 
2. The proposed approach is valiated on several tasks like point-cloud completion, shape compression, normal estimation, point cloud registration, point cloud classification and segmentation. Competitive performances have been reported with a comparison of the existing baselines.

### Weaknesses
1. For the experiments on point-cloud completion, as the experimental setup discussed, it samples 300 points for the evaluation. How about the performance of different number of sampled points?

2. For the experiments on the test classification and part segmentation, it seems the proposed algorithm does not have obvious performance gain over the existing work like PaRINet. What is the main reason under this result?

3. A minor suggestion, the baselines are usually introduced in the year before 2022. Is it possible to report more recent results for the comparison in the experimental section, like the work published in 2023?

### Questions
Please address the questions in the weakness section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces an equivariant feature representation to map per 3D point to a high-dimensional feature vector, which is supposed to be more capable to represent rich point information. Extensive experiments are conducted to verify the effectiveness in multiple tasks: point cloud completion, 3D shape compression, normal estimation, point cloud registration, and point cloud classification and segmentation. The results are very positive.

### Strengths
The primary strength of the proposed component lies in its capability to map 3D points to high-dimensional feature space with the property of SO(3)-equivariant, while the existing work Vector Neuron(VN) can only deal with three-dimensional features. The construction of the frequency-based transformation function D in equation (1) looks very reasonable and provable. 

Secondly, the effectiveness of the proposed module has been extensively evaluated on multiple tasks and datasets, which makes this work very solid and convincing.

### Weaknesses
There are some minor questions.

1. The proposed component is always applied together with the existing VN module. Is it possible to work by its alone? If so, how to extend it? 

2. Since the construction of transformation function D is related to different frequencies. However, in the evaluation, there is a lack of concrete experiments to deeply analyse how such frequency-based function can help the network to learn more discriminative features. Although most of downstream tasks have excellent performance, it is unclear what type of features are learned while keeping the SO(3) equivariance. Specifically, it would be beneficial to see an analysis of how different frequency components contribute to the learned representations and how they affect performance on downstream tasks. For example, are the lower frequency components capturing global shape information while higher frequencies capture finer details? This is not clear from the current experiments.

3. All experiments are conducted on very small-scale point clouds like objects. Is it possible to scale up the proposed method on larger scale 3D point clouds such as room-level ScanNet/S3DIS datasets or even urban-level SensatUrban dataset? If not, what are the potential reasons? The method's applicability to larger, more complex scenes is not demonstrated, and it's unclear if the computational cost would scale favorably.

4. In Section 2.2, the last line states that "Our feature representation can xxxx, which is not equivariant, so that it is equivariant". It's suggested to clarify the point?

5. In page 4, the section "Theorem 1.", you may need to remove the word "theorem"?

### Questions
Details in weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
**UPDATE**  
After reading the rebuttal, I now better understand and appreciate the contribution. While I still believe this is a testimony to the much needed improvement in writing, I believe the work should be accepted. 


The work proposes an SO(3) equivariant pointcloud network by extending vector neurons representation from a list of 3-dim vectors to a list of k-dim vectors. To accommodate this  increase in dimensionality a rotation operator construction is developed that can map a rotation in SO(3) to k dim.

### Strengths
- The work demonstrates improvement in detail preservation compared to the baseline VN. Quantitatively, it manages to bridge the reconstruction gap reported in VN with the non-equivariant baseline, occNet. Qualitatively, it can be seen the the proposed method is able to preserve some details such as the vehicle side mirror.
- The paper compares performance with the baseline VN on many additional applications including compression, normal estimation, classification, segmentation and registration. In all of them if demonstrates superior performance.

### Weaknesses
 - The paper's presentation is one of the main reasons for my low rating. It is possible that I did not understand some important insights, but given my relatively broad background in the field, this suggests that the authors did not do an adequate job of presenting and conveying their ideas to the reader. Key issues include the lack of a clear motivation, insufficient highlighting of limitations in existing solutions, inadequate consideration of the suggested design choices, and—most importantly—an outdated comparison with relevant literature
- The description of the limitation of VN is not clear. VN embeds features in a high dimensional space. But instead of using a n-dim vector, they use a nx3 matrix to keep the rotation operation in its same form as in the input space. It is thus my understanding that the representation capacity shouldn’t be smaller than any other global-embedding network which maps inputs to a high n-dim space. Therefore, i couldn’t quite understand the authors claim about VN having “3dim” features. First, I don’t think this is an accurate description of the dimensionality of VN, but more importantly i don’t understand how the fact that the vectors in the list live in 3 dimensions is causing issues with representing geometric details. I’ll try to give an intuitive example. Imagine a very dense pointcloud that captures fine details of the shape. Such a pointcloud may have 10^6 points and these points may live in 3D. My point is, the fact that the points live in R^3 isn’t itself a problem for capturing these details. Instead, what is known to cause issues with capturing fine details in neural fields is global representations. To fight this, many methods focus on partitioning the shape or scene into smaller regions and representing each of them with a local function, like switching from occnet to conv-occnet. In fact, there have been several follow up works to VN that try to do that. Other works tried to improve the encoder too. These works are not mentioned in the submission but should be discussed and compared with: [1,2,3,4].
- It is perhaps my misunderstanding, but it seems the lifting to R^N replaces the principal axes in R^3 with a 3-dim subspace in R^N. Why then is this helpful?
- The compression experiment is a bit unclear to me. There’s no report of the compression ratio — how much is the original pointcloud compressed wrt the embedding? It seems to measure reconstruction on the train set rather than compression.

**Minor**:

- The presentation should be more accurate. Sentences like “Equivariant neural networks (NN) change the output accordingly when the point cloud input is rotated without additional training.” are not accurate.  Equivariant NN are more general than that. Here the authors refer specifically to point cloud networks that are rotation equivariant.
- why is z/z not shown for part segmentation?

Typos:
* theoremIf

### Questions
- which experiment is meant to demonstrate that the lack of details is due to the 3 dim feature vector? Take the non-equivariant network occNet. This network maintains better details and still has N dim. I therefore am not convinced that the issue is with the dim of the features. 
- I understanding that the motivation in the proposed lifting to k-dim is to keep it simpler than other tensor networks, but how is the proposed representation compare to it? is it less expressive? i would be glad to see a discussion

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
