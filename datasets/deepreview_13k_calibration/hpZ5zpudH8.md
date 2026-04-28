# SpikSSD: Better Extraction and Fusion for Object Detection with Spiking Neuron Networks

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 6, 6, 3, 3

## Abstract
As the third generation of neural networks, Spiking Neural Networks (SNNs) have gained widespread attention due to their low energy consumption and biological interpretability. Recently, SNNs have made considerable advancements in computer vision. However, efficiently conducting feature extraction and fusion under the spiking characteristics of SNNs for object detection remains a pressing challenge. To address this problem, we propose the SpikSSD, a novel Spiking Single Shot Multibox Detector. Specifically, we design a full-spiking backbone network, MDS-ResNet, which effectively adjusts the membrane synaptic input distribution at each layer, achieving better spiking feature extraction. Additionally, for spiking feature fusion, we introduce the Spiking Bi-direction Fusion Module (SBFM), which for the first time realizes bi-direction fusion of spiking features, enhancing the multi-scale detection capability of the model. Experimental results show that SpikSSD achieves 40.8\% mAP on the GEN1 dataset and 76.0\% mAP@0.5 on the VOC 2007 dataset with only around 10\% firing rate, outperforming existing SNN-based approaches at ultralow energy consumption. This work sets a new benchmark for future research in SNN-based object detection. Our code is publicly available in supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents SpikSSD, an SNN-based object detection network. SpikSSD introduces a spiking residual network (MDS-ResNet) for feature extraction and Spiking Bi-direction Fusion Module (SBFM) for multi-scale feature fusion. Experiments on GEN1 and VOC dataset indicates the best performance of SNN-based object detection.

### Strengths
1.SpikSSD shows improvements in energy efficiency, achieving a 10% firing rate with competitive accuracy, which is beneficial for power-constrained applications.
2.Sufficient mathematical proof of the network structure mathematically, which proves the liability of the proposed MDS-ResNet.
3.Experiments on GEN1 and VOC proves the performance of SpikeSSD. On both dataset SpikeSSD proves to be the best SNN-based object detection network.

### Weaknesses
1.For object detection on images, the authors only provide experiment results on VOC dataset, which is insufficient since MS-COCO dataset is the mainstream dataset for this task. VOC dataset has much fewer images, which lacks of utility. There should be experiments on MS-COCO dataset and real-world images for validation qualitatively.

2.SBFM is too complicated for SNN-based network. SBFM fuses different scales of feature maps, but it is too complicated for training. To meet the requirement of SSD detection head, multiple features need to be generated. SBFM has a PAN-like structure but with 5 feature maps. There could be a more efficient way of feature fusion other than the proposed SBFM. The complexity of SBFM, with its multiple feature maps and bi-directional fusion, raises concerns about its practical implementation and computational overhead in resource-constrained SNN hardware. The design choices, while potentially beneficial for performance, may introduce unnecessary complexity that hinders real-world deployment.

3.The MDS-ResNet primarily extends SNN modules on mature ANN networks, which lacks new design or new insight on SNN. Core ideas like membrane-based shortcuts and spiking feature fusion have seen prior application. The modifications to the residual connections, while aiming to stabilize membrane potential, do not fundamentally deviate from existing approaches in adapting ANN architectures to SNNs. The core innovation seems incremental, lacking a novel perspective on how to leverage the unique properties of spiking neurons for feature extraction.

### Questions
1.There could be experiments on MS-COCO dataset and real-world images for validation qualitatively.

2. Could explain the following part with efficient manner? "SBFM has a PAN-like structure but with 5 feature maps. There could be a more efficient way of feature fusion other than the proposed SBFM."

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents an MDS architecture for solving the problem of SNN target detection. This approach enables the model to further utilize spike operations to reduce computing power. The authors validated it on multiple target detection datasets.

### Strengths
1. The author's analysis of the spike operation in the algorithm is very accurate, and based on this, he designed a spike-friendly MDS architecture.
2. The method proposed by the authors has good performance and energy efficient. (more elegant than EMS method~)
3. The author provides a relatively complete theoretical analysis.

### Weaknesses
1. This article appears to be incremental work.
2. See Question part.

### Questions
1. Can you make a more detailed comparison of the EMS and MDS architectures in terms of formulas? And show why the EMS architecture cannot be fused to the spike operation?
2. Regarding the calculation of energy consumption, can you give a discussion on how to deploy it on real hardware? Similarly, I would like to see a comparison between MDS and other model architectures?
3. What do you think of the method of gradient identity analysis? Are there any problems with this method's series of assumptions in discrete models such as SNN?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes an SNN-based single-shot multi-box detector SpikSSD. In the SpikSSD, this paper proposes a backbone MDS-ResNet. The MDS-ResNet adjusts the distribution of the input membrane synaptic to avoid gradient vanishing and explosion. Besides, this paper also proposes a Spiking Bi-direction Fusion Module (SBFM) to fuse spiking features in a bi-directional way. The proposed method is tested on GEN1 and VOC 2007 datasets, where the SpikSSD achieves good performance with only around 10% firing rate.

### Strengths
1. The proposed MDS-ResNet adjust uses tdBN in the shortcut to adjust the distribution of input membrane synaptic to alleviate the problems brought by gradient vanishing and explosion.
2. This paper gives a theoretical analysis of gradient vanishing/explosion for MDS-ResNet.

### Weaknesses
1. This paper claims they propose a backbone MDS-ResNet based on spiking neural networks. Is the backbone specifically designed for object detection? If so, what part of MDS-ResNet is specifically designed for objection detection? The paper introduces a Membrane-based Deformed Shortcut (MDS) to optimize identity mapping, but it's unclear how this directly addresses the unique challenges of object detection, such as multi-scale feature representation or handling complex spatial relationships. If not, it should be evaluated on classification datasets such as ImageNet [1] to show the generalization of the proposed backbone [2-5]. The current evaluation only on object detection datasets limits the understanding of the backbone's broader applicability.
2. In the area of object detection, COCO [6] is a general dataset, why not evaluate the proposed method on this dataset? The absence of COCO evaluation makes it difficult to compare the proposed method with the broader literature and understand its performance on a more complex and diverse dataset.
3. What's the motivation for the proposed bi-directional fusion? What challenges are handled by the bi-directional fusion? It would be better to introduce more about that. The paper mentions that the Spiking Bi-direction Fusion Module (SBFM) enhances feature representation in both spatial and temporal domains, but it lacks a detailed explanation of why a bi-directional approach is necessary over a simpler, unidirectional fusion method. What specific limitations of existing fusion methods does SBFM address, and how does it handle the potential for increased computational complexity?
4. The experimental table of the paper shows the proposed method has a low energy. How is the low energy consumption realized? On general computational devices or specifically designed devices? If the low energy depends on specifically designed devices, how is the low energy realized? The paper claims low energy consumption, but it does not clarify whether this is achieved through algorithmic design or specific hardware implementations. The lack of clarity on the computational platform and the assumptions made in energy calculations makes it difficult to assess the practical significance of the reported energy efficiency.

### Questions
Please see the weaknesses part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces SpikSSD, a Spiking Single Shot Multibox Detector that leverages a fully spiking backbone network (MDS-ResNet) and a novel Spiking Bi-direction Fusion Module (SBFM) for object detection in Spiking Neural Networks (SNNs). The model shows strong performance on the GEN1 and PASCAL VOC 2007 datasets, achieving a mean average precision (mAP) comparable to or better than existing SNN-based models with a low firing rate.

### Strengths
The paper highlights the low energy consumption of SpikSSD, reporting approximately 10% firing rates, which is notable in comparison to conventional ANNs.

### Weaknesses
The results are primarily limited to GEN1 and VOC 2007, which may not fully represent the performance across diverse object detection tasks. The paper could be strengthened by including more diverse datasets or a comprehensive analysis of SpikSSD's generalization capabilities. While the paper introduces the MDS to stabilize membrane synaptic inputs, the theoretical foundations are only briefly discussed. A more rigorous exploration of why MDS effectively stabilizes membrane potential and prevents gradient vanishing/explosion would strengthen the paper’s contributions. Additionally, it’s unclear how the MDS compares with existing methods for managing synaptic input variance in SNNs. Although the results are promising, the comparisons are limited to SNN-based models. The paper would benefit from a broader comparison with non-SNN state-of-the-art object detectors on similar datasets to better highlight SpikSSD's competitiveness in real-world applications. Given that SNNs are often measured against ANN counterparts, direct ANN comparisons could showcase where SNNs might still be falling short. While SBFM achieves bi-directional fusion, the paper lacks a detailed justification of why this method is uniquely advantageous in SNNs as opposed to standard fusion techniques. It would also be helpful to clarify the specific benefits of using a spiking-only architecture over incorporating mixed approaches if they offer potential improvements in performance. The paper does not include ablation studies to validate the specific contributions of MDS-ResNet and SBFM. Without this, it is difficult to assess whether the performance gains are directly attributable to these components. Such studies could better clarify the impact of each proposed module.

### Questions
Certain sections lack clarity, particularly regarding the mechanisms of MDS and SBFM. Visualizations of neuron firing patterns and more illustrative figures could help elucidate these mechanisms. Additionally, providing more detail in the methodology could allow for better reproducibility.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a spiking neural network backbone MDS-ResNet, and a spiking object detection model SpikSSD. Based on EMS-ResNet, the proposed MDS-ResNet modifies the shortcut connection in the residual blocks. The SpikSSD combines the proposed bi-directional feature fusion and MDS-ResNet. Experimental results show that the proposed SpikSSD outperforms existing spiking object detection methods.

### Strengths
1. This paper analyzes in detail the gradient vanishing or explosion for MDS-ResNet.
2. The proposed SpikSSD model achieves state-of-the-art mAP metric performance on GEN1 and VOC2007 datasets compared to existing spiking object detection methods.

### Weaknesses
1. In the method section, the authors spend a lot of words introducing the proposed backbone MDS-ResNet. However, MDS-Blocks 1, 2, and 4 are already utilized in MS-ResNet and EMS-ResNet, while only MDS-Block 3 is newly proposed, and it closely resembles MDS-Block 2. Moreover, the gradient analysis of MDS-ResNet is similar to EMS-ResNet. Therefore, I believe that the MDS-ResNet architecture should not be regarded as a main contribution of this paper. I suggest that the authors detail why MDS-Block is more effective for object detection tasks than MS-Block and EMS-Block.
2. The SpikSSD is only evaluated on VOC 2007 and GEN1 datasets, while EMS-ResNet is evaluated mainly on COCO 2017 dataset. I wonder if SpikSSD also works well on COCO 2017. If possible, please provide the experimental results on COCO 2017 dataset.
3. Figure 1 illustrates the firing patterns of MDS-ResNet and EMS-ResNet. However, it does not indicate on which task or dataset the evaluation is performed. Furthermore, it is not clear whether this phenomenon holds for all tasks or only for specific tasks.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
