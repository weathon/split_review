# Exposure Bracketing is All You Need for Unifying Image Restoration and Enhancement Tasks

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 6, 5, 8

## Abstract
It is highly desired but challenging to acquire high-quality photos with clear content in low-light environments. Although multi-image processing methods (using burst, dual-exposure, or multi-exposure images) have made significant progress in addressing this issue, they typically focus on specific restoration or enhancement problems, and do not fully explore the potential of utilizing multiple images. Motivated by the fact that multi-exposure images are complementary in denoising, deblurring, high dynamic range imaging, and super-resolution, we propose to utilize exposure bracketing photography to unify image restoration and enhancement tasks in this work. Due to the difficulty in collecting real-world pairs, we suggest a solution that first pre-trains the model with synthetic paired data and then adapts it to real-world unlabeled images. In particular, a temporally modulated recurrent network (TMRNet) and self-supervised adaptation method are proposed. Moreover, we construct a data simulation pipeline to synthesize pairs and collect real-world images from 200 nighttime scenarios. Experiments on both datasets show that our method performs favorably against the state-of-the-art multi-image processing ones.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a framework for a new setting of image restoration. It uses raw images as input and process several kinds degradation in one network. The architecture can perform well.

### Strengths
1. A novel setting combing several image restoration tasks, utilizing raw space images.
2. The performance is good enough.
3. Extensive experiments are done to prove characteristics of the proposed method.

### Weaknesses
1. The BracketIRE and BracketIRE+ are similar with all-in-one. The authors should discuss on this issue.
2. The computational cost seems to be high. The fairness of comparison is doubtful.
3. The datasets must be publicly, otherwise the work is not so essential.
4. The method of converting RGB to raw images is not well justified. The method used in UPI requires camera-specific parameters. The paper does not specify the CMOS sensor type used for the videos, nor if it matches the UPI setting. Furthermore, the use of RIFE for frame interpolation may introduce artifacts and alter the original video data distribution.
5.  It is unclear if the authors perform packing operations on the raw data. Many raw image processing methods pack color channels for efficient processing.
6. The exclusion of 10 and 4 invalid pixels around the input image is not well explained. It is unclear if the proposed method can handle marginal areas of the image.

### Questions
1. The way to convert RGB into raw is not suitable. For the method used in UPI, it need parameters from cameras. What is the type of CMOS for those videos? Is it the same with the setting of UPI? Would the RIFE affect data distribution of the original videos?
2. As the input is raw images, do the authors perform packing operation for those data? Many methods would do packing to split color channels.
3. Why do the authors  exclude 10 and 4 invalid pixels around the original input image? Do the proposed method deal with marginal areas?
4. The FLOPs of TMRNet is huge compared with others.
5. It seems to be the first work using this kind of unified image restoration setting. For the BracketIRE, can it compare with some all-in-one methods, such as AdaIR and Perceive-IR?
6. Why do the authors add SR for BracketIRE+? To match the title as restoration tasks or to show the ability on low resolution images?

Scores can be raised upon replies.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a temporally modulated recurrent network based on exposure bracketing photography for image restoration and enhancement in low-light environments. This paper simulates the paired data and pre-trains the temporally modulated recurrent network with synthetic images. Additionally, a self-supervised adaptation method is utilized to improve the model's robustness in real-world unlabeled images. Experiments presented in the paper validate its effectiveness for multi-image processing.

### Strengths
1. This work is well-complete overall, including data simulation, real-world data collection, and method design and experiments. 
2. The experimental results show improvements in both visual quality and quantitative metrics, demonstrating its effectiveness.

### Weaknesses
1. The comparison methods in Table 2 are all trained on synthetic data, while TMRNet is fine-tuned on real-world data. This comparison is somewhat unfair. It is recommended that the authors include the results of TMRNet without fine-tuning on real-world data and provide a note.
2. This paper claims that more frames result in better performance, would it introduce frames with over-exposure or large blur, making the restoration process more challenging?
3. In summarizing the contributions, the authors claim to unify image restoration and enhancement tasks, which seems somewhat exaggerated. First, this is not a new task; in fact, methods of HDR have already been addressing issues such as noise, blur, or ghosting. Additionally, even if the input includes images with various degradations, this has also appeared in previous papers, such as R1 and R2. Therefore, it would be better if the authors could change this contribution point or use a more appropriate wording.

### Questions
Refer to Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors proposed a neural network capable of performing denoising, deblurring, HDR, and SR altogether using exposure bracketing. The proposed network structure has a novel feature, called temporally modulated recurrent network, which is claimed to be effective in handling multiple images with different degradation. To train the network, the authors also constructed a dataset by applying synthetic degradation sequentially. The two loss functions are also developed to train the network in a self-supervised manner.

### Strengths
1. The proposed method is the first method that performs the four restoration and enhancement tasks altogether.
2. The necessity of the temporal modulated recurrent network is clearly explained, and its effectiveness is supported by experimental results. 
3. The necessity of the introduced loss functions is clearly explained, and their effectiveness is supported by experimental results. 
4. The constructed synthetic and real datasets will be helpful for researchers in the related field. 
5. The paper is well-written and well-organized.

### Weaknesses
1. I understand that ICLR accepts application-oriented papers. However, from the theoretical point-of-view, the manuscript does not contain sufficient technical novelties. The network can perform the four different tasks altogether since it is simply trained using the synthetic (and real) dataset containing four degradation. In other words, except for the dataset, the network does not have significant novelties compared to existing video restoration networks.  

2. The proposed temporal modulation network seems not very original. This reviewer cannot see a significant difference between the proposed network and a commonly used conv-LSTM (with different conv layers for each layer). Several other temporal modulation networks have also been explored, e.g., Temporal Modulation Network for Controllable Space-Time Video Super-Resolution, CVPR 2021. 

3. The proposed self-supervised loss functions are also not very different from existing loss terms, e.g., Exponential Moving Average Normalization for Self-supervised and Semi-supervised Learning, CVPR 2021. 

4. The effectiveness of the proposed network module and loss functions needs to be justified by other public datasets.

### Questions
Since the paper is especially well-written, I do not have specific questions for clarification. See my concerns in the Weakness section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper addresses the challenge of acquiring high-quality photos in low-light environments by unifying image restoration and enhancement tasks using exposure bracketing photography. This paper proposes a solution that includes a temporally modulated recurrent network (TMRNet) and a self-supervised adaptation method, pre-training the model on synthetic paired data and then adapting it to real-world unlabeled images. They also construct a data simulation pipeline and collect real-world images from diverse nighttime scenarios. Experiments show that their method outperforms state-of-the-art multi-image processing techniques.

### Strengths
This paper presents a paradigm for addressing low-light imaging through exposure bracketing photography with a simple yet effective network structure. This practical technical approach is orthogonal to mainstream research, which can more easily inspire subsequent studies.
The core contribution of this paper lies in the construction of the dataset and the corresponding training methods, particularly the self-supervised adaptation method. The dataset creation method is solid, and the design of the self-supervised adaptation method is clever.
The paper is well-organized, with clearly articulated problems, solutions, and experimental results that are easy to understand.
The impressive experiments show clear advantages over the compared methods.

### Weaknesses
1. **The use of RIFE**

   In previous work simulating realistic blur on the UPI-based REDS video deblurring dataset, I tried using RIFE to interpolate frames to 1920fps. While RIFE is an advanced frame interpolation algorithm, I observed that it still introduces artifacts in areas with significant motion and complex textures. These limitations may reduce the generalization ability of models trained on such synthetic data when applied to real-world blurred scenes. Specifically, the interpolation process can create unrealistic motion trajectories and introduce ghosting artifacts, which are not representative of real-world camera shake or object motion. This discrepancy between synthetic and real blur could lead to a model that is over-fitted to the artifacts of the synthetic data, thus limiting its effectiveness on real-world images.

2. **Comparison with AI-ISP**

   While the proposed self-supervised adaptation method shows promise, it still faces challenges when paired data is available compared to supervised methods. It would be helpful if the authors could clarify how this approach compares to AI-ISP, which addresses RAW denoising, super-resolution, deblurring, and HDR processing as independent subtasks. By decomposing these tasks, it is possible (though challenging) to obtain paired real data to replace synthetic data, potentially enhancing performance in practice. Alternatively, the authors could demonstrate that exposure bracketing provides a clear advantage over handling each subtask independently on synthetic data as an indirect validation of its benefits. For example, a comparison could be made against a pipeline where each subtask (denoising, deblurring, HDR) is handled by a separate, specialized network trained on paired data, to see if the joint approach of exposure bracketing offers a significant advantage in terms of final image quality or computational efficiency. Addressing these concerns would clarify the practical advantages of the proposed approach, and I would be inclined to improve my rating accordingly.

### Questions
I think the flowchart of the synthetic paired dataset is critical, would it be better to move it from the supplementary material to the manuscript?

[After Rebuttal]: The authors have addressed my concerns, thus I am inclined to improve my rating.

### Soundness
4

### Presentation
4

### Contribution
3
