# A Novel Security Threat Model for Automated AI Accelerator Generation Platforms

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
In recent years, the design of Artificial Intelligence (AI) accelerators has gradually shifted from focusing solely on standalone accelerator hardware to considering the entire system, giving rise to a new AI accelerator design paradigm that emphasizes full-stack integration. Systems designed based on this paradigm offer a user-friendly, end-to-end solution for deploying pre-trained models. While previous studies have identified vulnerabilities in individual hardware components or models, the security of this paradigm has not yet been thoroughly evaluated. This work, from an attacker's perspective, proposes a threat model based on this paradigm and reveals the potential security vulnerabilities of systems by embedding malicious code in the design flow, highlighting the necessity for protection to address this security gap. In exploration and generation, maliciously leverage the exploration unit to identify sensitive parameters in the model's intermediate layers and insert hardware Trojan (HT) into the accelerator. In execution, malicious information is concealed within the control instructions, triggering the HT. Experimental results demonstrate that the proposed method, which manipulates sensitive parameters in a few selected kernels across the middle convolutional layers, successfully misclassifies input images into specified categories with high misclassification rates across various models: 97.3% in YOLOv8 by modifying only three parameters per layer in three layers, 99.2% in ResNet-18 by altering four parameters per layer in three layers and 98.1% for VGG-16 by changing seven parameters per layer in four layers. Additionally, the area overhead introduced by the proposed HT occupies no more than 0.34% of the total design while maintaining near-original performance as in uncompromised designs, which clearly illustrates the concealment of the proposed security threat.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a novel threat model targeting automated AI accelerator generation platforms. It says that full-stack integration in the design process of accelerators has become common. In this work, it explores how manipulating the model parameters will result in misclassification introducing a method called Cross-layer Sensitive Filter Exploration (C-SFE). To achieve this, in this threat model the attacker has to be active in three components of the platform; design space exploration (DSE), software stack, and hardware generation. In DSE, the attacker finds the parameters to be targeted. In hardware generation, HT is inserted to change the targeted parameters. In the software stack, there is an interface injection to trigger the HT. The results show high misclassification rates for YOLOv8, ResNet-18, and VGG-16. The area overhead of the HT is 0.34% of the total design.

### Strengths
1. The authors say that the security aspect of accelerator generation platforms is largely unexplored, and this is one of the initial works done to explore security vulnerabilities.

2. The proposed HT introduces a very low area overhead (0.34%) making it hard to detect before runtime.

3. The paper presents multiple evaluations to justify their claims; attack performance, # of parameters vs classification rate, layout design with HT, resource utilization, etc.

### Weaknesses
 1. The evaluations of this threat model are limited to Gemmini. This can be further extended to other platforms such as GeneSys.

 2. Although the area overhead of the accelerator is very low, it would have been better to have runtime performance numbers compared to the benign platform to see whether there is a significant difference in the inference pipeline. Further, would there be a larger difference when the test dataset size increases?

 3. The discussion section (4.4) of the paper lacks depth. Perhaps to justify the findings of this section, it would be better to include them in the appendix.

 4. The paper mentions minimizing the exploration time during DSE. However, no clear numbers were presented how this would change for being and malicious platforms.

 5. In some written sections, the use of the word "parameter" becomes a bit confusing whether it is the model parameters of DSE parameters (ex: line 190).

 6. Minor issue: double quotations were not properly handled. (line: 394)

 7. Y axises of Figure 6 are not named.

### Questions
1. Would a simple validation of model parameters at the end of execution, along with the classification results, show that the parameters have changed? This is considering that given a trained model, we are aware of its model parameters.

2. Instead of carefully selecting which parameters to change, how would the results look like if parameters were changed randomly? I think this should be a baseline to be compared with. It is important to see whether a complex technique is required.

3. Why different numbers of kernels and parameters were selected for various models? Keeping them consistent across different models would be a good comparison to do.

### Soundness
3

### Presentation
2

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
In this paper, the authors propose a threat model in which the accelerator provider acts as an attacker by injecting hardware Trojans (HTs) through an EDA tool into the accelerator to enable misclassification attacks in Deep Neural Network (DNN) inference. They categorize these attacks into three types: 1-to-1, N-to-1, and others.

### Strengths
The paper assumes the EDA tool developer of the AI accelerator platform as the adversary, which is a compelling area of research.

### Weaknesses
The paper assumes that the EDA tool developer of the AI accelerator platform acts as the adversary, which is a compelling area of research. However, it is essential to demonstrate that the added HTs are challenging to detect by verification tools. In reality, substantial work has been done on HT detection and hardware formal verification. That said, the paper does not discuss whether existing HT detectors [1-5],  could identify the injected Trojans, including such an analysis would enhance the credibility of the claims.

Designing ASICs follows strict standards. SkyNet and similar projects rely on HLS rather than ASIC processes, which may facilitate deployment on FPGA but does not reflect the final circuit. For automatically inserted Trojans, can they pass through functional verification steps?

For IoT applications, it would be more appropriate to use platforms like the Ultra96 (as used in SkyNet) or KRIA KR260, which are MPSoC-based devices commonly utilized in IoT contexts.

It appears that the LoopConv module was mapped to LUTs, yet Fig. 6 does not clearly show the specific size and location. Based on Table 2, using the default optimization requires approximately 1,000 additional LUTs. This amount seems quite large for HT injection. 

The authors inject a Trojan into the EDA tool, potentially enabling triggers or malicious optimization on the hardware. I believe this point should be emphasized, with more detail on the significance and application value of such EDA tools. However, this brings up a broader issue: an EDA tool superior to others would likely dominate the market, making it challenging for a provider to practically act as an attacker.

### Questions
Could the authors explain why they chose the U50 platform (a high-end, expensive database acceleration card) despite targeting IoT applications?

For inserted Trojans, can they pass through functional verification steps?

Could you provide component consumption under a fair comparison scheme, such as comparing a clean accelerator vs an HT-injected accelerator, both using Vivado's Area Optimization mode, Default mode, latency optimization, and so on?

Could the authors discuss how realistic their threat model is?

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
This paper attacks an AI accelerator generation platform using a unique threat model and adopting a genetic algorithm. The attack is evaluated across benchmark DNN models.

### Strengths
The paper explores a unique direction in exploiting security threats in automated AI accelerator platforms. The research direction is exploratory in nature and innovative.

### Weaknesses
Overall, the paper is very hard to follow, and the threat needs to be more explicit and clarify the assumptions. Since this is a unique direction, the authors should try to establish the threat model first. The summary of the weakness:

1. The threat model is vague and unclear on some assumptions. For example, sections 3.1 and 3.2 are confusing regarding what is the goal of the attacker. Is it a hardware trojan attack or an adversarial weight attack? Both terms are used. However, the threat model assumption is not equivalent for both cases. Moreover, there is discussion on how the attacker would gain access to model parameters, but hardly any discussion on how they will modify the parameters. The only discussion in the paper states in line 194, but how an attacker would insert this malicious code. 

2. The most concerning part is it is not clear whether the attacker can access the training stage or not. If not, then how can they modify model parameters? In the model production stage and inference stage where exactly the attacker is located.

3. Some of assumptions are also not well established and needs clarified. For example line 265 "Avoid attacking the model’s first layer an the final classification layer, as attacks on these two layers can have a significant impact on the model and are therefore more
 likely to be closely scrutinized by security engineers." I doubt if that is the principle machine learning engineers follow; even if that is the case, how do they scrutinize these layers? There is no standard list of model parameters.

4. Attack algorithm is naively adopting a genetic algorithm. Eqn. 1 is very similar to computing gradient, since the attacker can access model parameters why not compute the gradient. The authors claim their method does not need gradient computation, more justification is needed why GA would be faster than computing gradients.

5. Figure 7 is confusing; the description is not clear on the conclusion. Both attacks target the middle three convolution layers, but what does that mean from an attack efficacy and efficiency perspective?

6. The figure-2 needs to improve, the text are hard to read on part (b).

### Questions
Overall, I commend the authors for exploring a unique security problem. However, the paper in its current form requires a lot of improvement before being ready for publication. Please refer to the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a new threat model for AI accelerators. The proposed attack includes a complete pipeline that first finds out the sensitive parameters in the user-provided model and then embeds malicious code using bit flipping. The embedded Hardware Trojan (HT) is then triggered using information hidden in communication instructions. Evaluation results on three vision models show that the proposed attack can obtain a high attack success rate.

### Strengths
This paper has the following strengths:
+ The authors identify the vulnerability of AI accelerators in the context of a complete supply chain, starting from the pre-trained model from user to accelerator generation and then to deployment. 
+ The authors decompose the problem of HT insertion into multiple sub-problems, i.e., locating the sensitive kernels, and bit-level perturbation. The attack is also designed with the goal of ensuring stealthiness and minimal hardware overhead. 
+ Empirical results show that the proposed attack can achieve a high attack success rate with very few bit flips.

### Weaknesses
The paper has the following weaknesses:
- The preliminary section does not provide any information about the prior works on bit-flipping attacks. The lack of discussion makes it hard to understand the real innovation of this work since previous attacks have explored how to identify the sensitive kernels in the pre-trained quantized model (e.g., ProFlip). Specifically, the paper should discuss the limitations of existing bit-flipping attacks in the context of hardware Trojans (HTs). It is unclear how the proposed method differs from existing approaches in terms of stealthiness and hardware overhead.
- The proposed attack method is different from the previous model-level bit-flipping attacks since this paper is concerned with the hardware implementation of HT insertion. It's not clear why we cannot directly apply the existing bit-flipping attacks on AI accelerators. The challenges need to be clarified and empirical results can be used to support this. For instance, the paper should elaborate on the constraints imposed by hardware implementation, such as the regularity of attack locations and the number of parameters that can be modified, and how these constraints affect the applicability of existing bit-flipping techniques.
- The design of Cross-layer Sensitive Filter Exploration (C-SFE) is not clear. The authors mentioned in Section 3.4 that 'CSFE expands the decision boundary of a targeted category by flipping a few bits in one kernel per layer'. However, the paper does not explain whether different layers are equally important and whether the attack can exploit a single layer only. The paper should clarify the importance of each layer in the attack and whether the attack can be effective by targeting only a single layer or if it requires a cross-layer approach. Additionally, the paper should discuss the trade-offs between single-layer and cross-layer attacks in terms of attack success rate and hardware resource consumption.

### Questions
Please consider addressing the weakness points above.

### Soundness
3

### Presentation
2

### Contribution
2
