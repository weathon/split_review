# Spiking CenterNet: A Distillation-boosted Spiking Neural Network for Object Detection

- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 3, 5, 6

## Abstract
In the era of AI at the edge, self-driving cars, and climate change, the need for energy-efficient, small, embedded AI is growing. 
Spiking Neural Networks (SNNs) are a promising approach to address this challenge, with their event-driven information flow and sparse activations.
We propose Spiking CenterNet for object detection on event data.
It combines an SNN CenterNet adaptation with an efficient M2U-Net-based decoder.
Our model significantly outperforms comparable previous work on Prophesee's challenging GEN1 Automotive Detection Dataset while using less than half the energy. 
Distilling the knowledge of a non-spiking teacher into our SNN further increases performance.
To the best of our knowledge, our work is the first approach that takes advantage of knowledge distillation in the field of spiking object detection.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper does knowledge distillation on SNNs

### Strengths
Not applicable

### Weaknesses
This paper has no contributions besides just applying knowledge distillation on SNN. Further there are many works that have shown ANN-to-SNN distillation can help. I recommend the authors to look at all the SNN work out there that focus on improving SNN performance using interesting SNN optimization techniques such as those from the research group of Priya Panda, Guoq Li, and many others....

### Questions
See weaknesses above

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces "Spiking CenterNet," a novel object detection approach that leverages the energy-efficiency of Spiking Neural Networks (SNNs). Positioned as a solution for the growing demand in edge devices and self-driving cars, this method combines an SNN-based adaptation of CenterNet with an M2U-Net-based decoder. Significantly, the authors incorporate Knowledge Distillation to further enhance the performance of their SNN, making their model stand out in object detection tasks using event data. The primary contribution lies in merging the benefits of SNNs with knowledge distillation to optimize object detection in energy-constrained environments.

### Strengths
The integration of an SNN adaptation of CenterNet with an efficient M2U-Net-based decoder is a novel approach in the object detection domain.
The model not only addresses the energy efficiency challenge but also outperforms comparable object detection models on event data.

### Weaknesses
1. In principle, there’s no new architecture built for object detection. The proposed Spiking CenterNet appears to be a direct adaptation of the original CenterNet, simply replacing the conventional neural network components with spiking counterparts. While the integration with the M2U-Net-based decoder is mentioned, the core detection mechanism seems unchanged. This raises concerns about the novelty of the architectural contribution.
2. The preprocessing of event-data makes it quite similar to binarized conventional videos, instead of digging into the intrinsic benefits of asynchronous properties. Specifically, the method of accumulating events into frames, as described, seems to discard the temporal richness inherent in event data. This approach potentially undermines the advantages of using SNNs, which are inherently suited to processing sparse, asynchronous data streams.
3. The improvements made by Knowledge Distillation are quite limited, while the whole paper emphases on KD a lot. More importantly, since the idea of KD is guiding SNN models by ANN models, how to obtain the unique advantages of SNNs from KD. The paper heavily emphasizes the role of Knowledge Distillation (KD) in enhancing performance. However, the reported improvements from KD appear marginal. This is particularly concerning given the fundamental differences between ANNs and SNNs. It is unclear how KD, which typically involves transferring knowledge from a continuous-valued ANN to a discrete-valued SNN, can effectively capture and transfer the unique spatio-temporal dynamics of SNNs.
4. The sparsity listed in table 2 is not the sparsity but the density (higher sparsity means sparser). This is a critical error that affects the interpretation of the results. The values presented suggest a misunderstanding of the concept of sparsity in the context of SNNs.

### Questions
See the weaknesses, also:

1. what's the reason for choosing the architecture? Is that possible to employ other kinds of structures?
2.  How to guide an efficient SNN by an ANN teacher, in terms of the spatio-temporal representation ability, the non-linear firing dynamics etc?
3. Why emphases on KD a lot, given the benefits of KD are quite limited.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Spiking CenterNet for object detection on event streams. It combines an SNN CenterNet adaptation with an efficient M2U-Net-based decoder. This work is the first approach that takes advantage of knowledge distillation for object detection using SNNs.

### Strengths
1) The topic of distillation-boosted SNN for object detection is very interesting and attractive.

2) This paper replaces CenterNet’s upsampling by the more efficient modules from M2U-Net (Laibacher et al., 2019) and add binary skip connections between encoder and decoder, which improves gradient flow despite the spiking communication.

3) This work utilizes Knowledge Distillation (KD) for SNNs in the context of object detection.

### Weaknesses
1) The innovative KD in this paper has little effect on the accuracy, and only improves by 0.006. Related knowledge is not explained clearly, such as event-based object detection methods. The advantages of using CenterNet, such as the need for an NMS, are not explained. More specifically, the paper should elaborate on why CenterNet was chosen over other object detection frameworks and what specific advantages it offers in the context of SNNs, especially concerning the absence of Non-Maximum Suppression (NMS). Furthermore, a more thorough comparison with existing event-based object detection methods would strengthen the paper's contributions.

2) The authors should explore deeper backbone for the proposed framework, such as ResNet50, ResNet101. Whether the effect is better than shallow network? This is a crucial point as the performance of deep learning models often significantly improves with increased depth. The paper should investigate if this holds true for the proposed SNN architecture and KD approach.

3) The details of the proposed method are not clear. For example, how is the identity mapping between encoder and decoder implemented, and how is it different from the implementation in ANN? The paper needs to provide a more precise description of the identity mapping mechanism, including its implementation details and how it differs from traditional ANN implementations. A diagram illustrating this mapping would be beneficial.

4) The relevant work is not fully introduced, and KD has little effect on performance improvement, which brings large energy consumption. The paper should discuss the trade-off between the marginal performance gain achieved through KD and the associated increase in energy consumption. A quantitative analysis of this trade-off would be valuable.

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents Spiking CenterNet, an SNN for object detection. It employs knowledge distillation from a non-spiking SNN to improve the accuracy. The implementation of the proposed method for the Prophesee’s GEN1 Automotive Detection Dataset shows better results than related works.

### Strengths
1. The tackled problem is relevant to the community.

2. The technical descriptions are clear and comprehensive.

3. The results show better results than prior SNNs.

### Weaknesses
Some aspects need to be clarified.

1. Please highlight more clearly the differences between Cordone et al. (2022) and the proposed method (other than applying knowledge distillation). Specifically, a more detailed comparison of the architectural differences and the implications for spike-based processing should be included. It is not sufficient to simply state that knowledge distillation is the key difference; a deeper analysis of the underlying mechanisms is required.

2. Please discuss what are the challenges of applying knowledge distillation for SNN object detection, compared to existing knowledge distillation methods between other types of networks. The discussion should include the specific difficulties arising from the temporal dynamics of SNNs, the discrete nature of spikes, and the impact on the distillation process. It is important to understand how these factors affect the transfer of knowledge from the teacher network to the student SNN.

3. Please provide more details (setup and tool flow) for the implementation of the proposed method on the neuromorphic hardware. This should include details about the specific hardware platform, the mapping of the network onto the hardware, and the tools used for simulation or deployment. The current description lacks the necessary specifics to assess the feasibility of the implementation.

4. If possible, please provide the source code for reviewers’ inspection during the rebuttal.

### Questions
1. Please highlight more clearly the differences between Cordone et al. (2022) and the proposed method (other than applying knowledge distillation).

2. Please discuss what are the challenges of applying knowledge distillation for SNN object detection, compared to existing knowledge distillation methods between other types of networks.

3. Please provide more details (setup and tool flow) for the implementation of the proposed method on the neuromorphic hardware.

4. If possible, please provide the source code for reviewers’ inspection during the rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
