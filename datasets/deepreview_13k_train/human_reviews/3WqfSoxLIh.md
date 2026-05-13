# FDTDNet: Privacy-Preserving Lensless Object Segmentation via Feature Demultiplexing and Task Decoupling

- Decision: Reject
- Scores: 6, 5, 6, 8

## Abstract
Camera-based vision systems pose privacy risks, whereas lensless cameras present a viable alternative by omitting visual semantics from their measurements due to the absence of lenses. However, these captured lensless measurements pose challenges for existing computer vision tasks such as object segmentation that usually require visual input. To address this problem, we propose a lensless object segmentation network via feature demultiplexing and task decoupling (FDTDNet) to perform object segmentation for lensless measurements. Specifically, we propose an optical-aware feature demultiplexing mechanism to get meaningful features from lensless measurements without visual reconstruction and design a multi-task learning framework decoupling the lensless object segmentation task into two subtasks, i.e., the reason for contour distribution maps (CDM) and body distribution maps (BDM), respectively. Extensive experiments demonstrate that our FDTDNet achieves highly accurate segmentation effect, which sheds light on privacy-preserving high-level vision with compact lensless cameras.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a model for segmentation that operates on measurements from a lensless camera. Instead of prior approaches that first attempt to reconstruct an RGB image and then carry out segmentation, the paper's approach directly operates on the lensless measurements. The architecture is endowed with knowledge of the optical measurement process through "optical feature demultiplexing", along with other innovations. Experimental results confirm the benefits of this approach.

### Strengths
- The paper is generally well motivated (except for the question of privacy below) and written. It makes sense that a single unified approach would work better than segmenting reconstructed images.
- The OFD approach is novel and interesting. It has the potential to be useful beyond the segmentation task as a general way of processing lensless measurements for vision tasks.
- The experiments and ablations are extensive and largely convincing.

### Weaknesses
 - The paper adds an unnecessary "privacy preserving" claim (in its title!) that is really only discussed in the (first paragraph of the) introduction, and mostly by citing other papers. Privacy preserving is a strong claim and should not be made without more care. If anything, a paper that shows improved performance at segmentation implies that lensless measurements  carry a fair amount of information about the underlying scene, and could leak private details. A video of segmentation masks could, for example, be enough to identify people by gaits. At that point, we get to deciding what privacy preserving means and what kind of privacy is being preserved.

  But this entire question is un-necessary to the central contribution of the paper --- a better segmentation approach for lensless cameras. The paper would be stronger, and in my opinion more sound, if it dropped the superfluous privacy claim from its title.

- The ODM + CDM approach could be explained a bit better, and especially discussed more with related work. Has this division into subtasks been tried before? How does this relate to CDMNet?

- Minor point, but the paper should make the experimental results section a bit more self contained and describe the content of the two benchmark datasets.

### Questions
Please address the points brought up in the weakness section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents FDTDNet, a framework for object segmentation using lensless cameras, designed to enhance privacy by bypassing visual image reconstruction.

### Strengths
1) Quality: All figures and tables are well-designed and of high quality, except Figure 2, which will be discussed in the weaknesses section below.
2) Performance: Experiments across two different datasets validate the method’s performance. this proposed approach consistently outperforms competing methods.

### Weaknesses
Updated Review 

Firstly, I would like to thank the authors for the clarifications and modifications provided during the discussion period. Your detailed explanations regarding the mathematical equations, as well as the associated adjustments, have addressed my initial confusion to some extent. Upon closer re-examination, it has become clear that many of the equations in the paper are existing, well-established results rather than novel contributions. While these equations may be important to your implementation, they do not appear to represent theoretical innovations. I strongly recommend that the authors explicitly highlight their contributions and clearly distinguish them from prior work to improve clarity on this point.

In addition to these observations, I have identified other concerns, including some raised by other reviewers, which I believe are more critical and warrant further discussion:

1. Overclaims on Privacy Protection:
- As highlighted by other reviewers, the privacy-preserving aspect of the proposed method seems overstated. 
- While the idea of bypassing visual reconstruction aligns with privacy goals, the OFD block appears to perform some level of visual reconstruction at varying scales, which undermines the claim of mitigating sensitive privacy leakage. 
- Moreover, privacy protection is presented as a core contribution, yet this aspect feels secondary or incidental to the main framework. 
- Additionally, alternative imaging methods, such as single-pixel imaging or minimalist cameras, are capable of achieving similar or better privacy-preserving effects. These methods are neither discussed nor compared, which weakens the claimed contribution in this area.
- I just noticed that this point has already been addressed by the authors through revisions, so it does not require excessive concern. However, it should be noted that the contribution has been further weakened as a result, making it even more important for the authors to clearly articulate their innovations and contributions, as well as how their method differs from existing approaches.

2. Dataset Limitations and Lack of Real-World Experiments:
- The lack of real-world experiments. 
- As pointed out by the AC, the datasets used in the paper are limited to controlled conditions (e.g., FlatCam/PhlatCam captures with clear foreground-background separation). This constrained setup does not sufficiently demonstrate the robustness or generalizability of the proposed method to complex, real-world scenarios, such as cluttered backgrounds, occlusions, or diverse illumination conditions. 
- Without such evidence, it is difficult to assess whether the method is robust enough for broader applications.

3. Dataset Renaming and Reporting Discrepancies:
- As pointed out by the AC, the datasets were renamed. The renaming of datasets (e.g., DISC, DIRC) without proper justification raises concerns about the transparency and rigor. 
- Furthermore, as also pointed out by the AC, discrepancies in the reported results for competing methods (e.g., RecSegNet) compared to their original papers call into question the reliability of the reported comparisons. These issues must be clarified to ensure confidence in the findings.

Given the above concerns, I am lowering my score due to the recognition of more significant flaws of this paper. Specifically:

1. Overclaims regarding privacy protection (I just noticed that this point has already been addressed by the authors through revisions, so it does not require excessive concern. However, it should be noted that the contribution has been further weakened as a result, making it even more important for the authors to clearly articulate their innovations and contributions, as well as how their method differs from existing approaches.)
2. Insufficient experimental validation on real-world datasets
3. Transparency and rigor issues related to dataset naming and reported results

If the authors can address these points convincingly, I am willing to adjust my rating back to a positive recommendation. 


_____________________________

Initial Review

This paper has two main issues:

1) Clarity:
- The equations are overly complex. The mathematical presentation, particularly in the OFD mechanism on page 3, lines 162-215 (Equations 3-11), is overly dense and challenging to understand.
- This section mainly stacks equations without sufficient explanation, making it difficult for readers to grasp the underlying principles. It would be beneficial to include more intuitive or conceptual explanations alongside these equations. 
- Additionally, labeling elements of Figure 2 to indicate which parts correspond to specific equations could greatly improve clarity. Given the length and complexity of this section, I suggest either simplifying the equations or providing clearer explanations.

2) Analysis: 
- The paper could benefit from a more in-depth discussion of its limitations. 
- Although some failure cases are illustrated in Figure 12 on page 16 (Appendix), it would be helpful to place these directly in the main text and discuss potential solutions more explicitly. 
- Discussion about addressing these limitations directly within the main body is suggested.
- However, this is a minor suggestion. My main concern is the first point about clarity.

### Questions
1) Can the authors provide further insights into how the method might generalize to more complex datasets, particularly in scenarios where small objects or highly cluttered backgrounds are present? 
2) How does the proposed FDTDNet handle noise in real-world lensless measurements? Could additional noise abatement strategies enhance the robustness of the segmentation?
3) Could the authors expand on the potential for adapting the method to edge devices, considering the computational demands highlighted in the complexity analysis?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
To enhance segmentation accuracy while ensuring privacy, the authors propose a one-step method called FDTDNet for lensless object segmentation from lensless measurements without visual reconstruction. They propose an optical-aware feature demultiplexing (OFD) mechanism aimed at refining the features obtained from lensless measurements via modeling the linear equation between the semantic features bound to lensless measurements and those corresponding to visual inputs. They decouple the segmentation task into a contour distribution map (CDM) and a body distribution map (BDM) inference by contour-/bodydistribution learning branches, and propose a contour-body interaction (CBI) module for reasoning segmentation results from correlations between CDM and BDM. They conducted extensive experiments to verify their methods.

### Strengths
The originality is supported by modelling the linear equation between the semantic features bound to lensless measurements and those corresponding to visual inputs, and application of multiple current machine learning methods to a new domain, i.e., lensless object segmentation. The quality, clarity and significance of this work is good.

### Weaknesses
Equation 1 is the basis for their modeling and derivation of the relationship between the original image and the measurement in the feature space. However, Equation 1 itself is not convincing. That is, does the linearity between the original image and the measurement mean that the semantic features of the original image and the measurement are also linear? The authors should have a more rigorous derivation or proof for this. Specifically, the assumption that a linear relationship in the image domain directly translates to a linear relationship in a high-dimensional semantic feature space is a significant leap. The paper lacks a theoretical justification for this assumption, particularly given the non-linear nature of typical feature extraction processes. Furthermore, the authors should discuss the potential impact of this assumption on the model's robustness and generalizability.

### Questions
In OFD, one downsampling and two CBRs are used to transform $A_L $ or $A_R$ into its semantic space, and one PVT is used to transform the measurement Y into its semantic space. Why not do the same for AL/AR and Y? What is the author's consideration?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a one-step method without intermediate image reconstruction, addressing privacy concerns and computational efficiency.

### Strengths
1. Introduces an Optical-Aware Feature Demultiplexing mechanism that enhances feature extraction from lensless measurements.
2. Effectively decouples segmentation into contour and body tasks, leveraging a mutual learning strategy.
3. Demonstrates superior performance on two datasets, outperforming state-of-the-art methods in multiple metrics.

### Weaknesses
 1. The performance of the network is not analyzed, such as the number of parameters, number of floating-point operations, inference time, etc.
2. Lack of explanation and verification of the weight setting of the hybrid loss function.
3. The paper does not explain the advantages of this one-step segmentation over the prior visual reconstruction method, and the experiment does not compare it with another method.
4. There is a lack of a more detailed description of the datasets. According to my understanding, are these datasets all synthetic? Are the measurements of the images synthesized using prior knowledge?

### Questions
1. The performance of the network is not analyzed, such as the number of parameters, number of floating-point operations, inference time, etc.
2. Lack of explanation and verification of the weight setting of the hybrid loss function.
3. The paper does not explain the advantages of this one-step segmentation over the prior visual reconstruction method, and the experiment does not compare it with another method.
4. There is a lack of a more detailed description of the datasets. According to my understanding, are these datasets all synthetic? Are the measurements of the images synthesized using prior knowledge?

### Soundness
3

### Presentation
3

### Contribution
3
