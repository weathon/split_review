# NeuralFuse: Learning to Recover the Accuracy of Access-Limited Neural Network Inference in Low-Voltage Regimes

- Decision: Reject
- Avg Score: 5.75
- Scores: 8, 5, 5, 5

## Abstract
Deep neural networks (DNNs) have become ubiquitous in machine learning, but their energy consumption remains a notable issue. Lowering the supply voltage is an effective strategy for reducing energy consumption. However, aggressively scaling down the supply voltage can lead to accuracy degradation due to random bit flips in static random access memory (SRAM) where model parameters are stored. To address this challenge, we introduce \textbf{NeuralFuse}, a novel add-on module that addresses the accuracy-energy tradeoff in low-voltage regimes by learning input transformations to generate error-resistant data representations. NeuralFuse protects DNN accuracy in both nominal and low-voltage scenarios. Moreover, NeuralFuse is easy to implement and can be readily applied to DNNs with limited access, such as non-configurable hardware or remote access to cloud-based APIs. Experimental results demonstrate that, at a 1\% bit error rate, NeuralFuse can reduce SRAM memory access energy by up to 24\% while recovering accuracy by up to 57\%. To the best of our knowledge, this is the first model-agnostic approach (i.e., no model retraining) to address low-voltage-induced bit errors.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents an add-on module that can be added to image classifiers when they are employed/inferenced in a low-power and error prone accelerator. The module is trained by various perturbated models (models that run on machines with bit errors in SRAMs). The proposed module can be trained on two real-life scenarios: 1) relaxed access and 2) restricted access. The extensive experimental results show that the proposed method is effective in error resiliency and power saving.

### Strengths
The paper presents an novel idea of adding a module to any image classifiers where the image model can suffer from low-voltage induced errors. This approach does not require retraining of the models and can be applied to any proprietary-protected DL models. 

The extensive experiments show the effectiveness of the work. The paper is well written and organized. 

As large models are being developed and deployed around the world, the proposed method can save significant energy and pave the way to greener AI. Although the work is only focused on the image classifier, it opens a door to robust DL in other domains.

### Weaknesses
The work assumes that the NeuralFuse generator can be employed on the hardware of no-error voltage. To justify this claim, it would be great if there is a comparison of the sizes (number of parameters) between NeuralFuse generator and the classifier. It is also unclear how the architecture of the NeuralFuse generator was chosen. While the paper mentions different architectures (ConvL, DeConvL, UNetL, ConvS, DeConvS, and UNetS), the reasoning behind these choices and their specific configurations is not well explained. A more detailed justification for the selection of these architectures, including the number of layers, filter sizes, and activation functions, is needed to fully assess the method's practicality and efficiency. Furthermore, the trade-offs between these different architectures in terms of accuracy recovery rate and energy saving are not explicitly discussed.

### Questions
The review can see the architectures of the generators in the appendix. How are the detailed architecture of generators decided? Any insights on the architecture of the NeuralFuse generator?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper aims to tackle the accuracy drop introduced by the increasing bit error rate under the low-voltage scheme by finding a more robust input representation. An error-resistant input transformation is proposed by utilizing a trainable generator, and a modified training loss is utilized to optimize the predicted outputs with/without bit-error injection. The experiments show an obvious accuracy improvement compared to the baseline.

### Strengths
* Neat paper structure and easy-to-follow content.
* A simple add-on strategy that can be used in access-limited scenarios.
* Extensive analysis of different generator architectures.

### Weaknesses
 * Lack of discussion of introduced overhead of the generator modules. For ImageNet-10, the best generator architecture, UNet-L, has 2.03G MACs. The introduced extra computation cost is significant compared to the vanilla model (ResNet18 only has 1.82 G MACs). It raises the concern that the introduced overhead for the generator is too large compared to the classifier, making the proposed strategy unrealistic. The author only discusses the energy of SRAM access without considering the computation energy and latency.
* The introduced generator modules may dilute the energy efficiency brought by the low-voltage scheme. Based on Appendix E, the total computations are very large. A more ideal accuracy-saving method should introduce less overhead. Specifically, the additional MAC operations introduced by the generator network, especially for larger architectures like UNet-L, could negate the energy savings from reduced voltage operation in the base model. This is a critical oversight, as the goal is to achieve energy efficiency, not just accuracy recovery.
* Lack of comparison with other error-resistant methods for bit-error rate. The author should add a comparison with other methods to show whether the costly input transformation is worth. The paper should include a comparison with techniques such as error correcting codes, algorithmic noise tolerance, or other fault-tolerant architectures to justify the proposed approach's overhead and effectiveness.

### Questions
* Could the author provide a more complete overhead analysis of the introduced generator? The author should show the introduced energy cost of computation (both memory and computation) and extra latency overhead in 4.4. The paper would be more meaningful if it saved accuracy under small overhead.
* Could the author compare with other error-mitigation methods for bit error in SRAM?

### Soundness
2 fair

### Presentation
4 excellent

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
In this study, the authors introduce NeuralFuse, a data preprocessing module designed to enhance resilience against bit errors arising from low-voltage SRAM, while also offering potential energy savings. Comprehensive tests affirm its efficacy in enhancing models affected by perturbations, ensuring transferability across diverse DNN architectures, and bolstering robustness in weight quantization.

### Strengths
1. It focuses on a system aspect of neural network computing: a power-saving method with low voltage operation.
2. The proposed module can work in a plug-and-play manner and does not require retraining the deployed model.

### Weaknesses
1. The net benefits of introducing NeuralFuse in tandem with low-voltage operation remain uncertain. While there are energy savings associated with SRAM accesses, these reports overlook the comprehensive energy consumption of NeuralFuse, particularly the MAC operations. The energy consumption of the NeuralFuse module, especially when using larger configurations, could negate the benefits of low-voltage SRAM operation. The reported SRAM access energy savings do not account for the additional MAC operations introduced by NeuralFuse, which, given the scale of some configurations, may be substantial and potentially outweigh the gains from reduced SRAM access energy.
2. Even though there's a notable enhancement in recovered accuracy, it might fall short when juxtaposed with the original accuracy, notably in the case of ResNet50. The recovery of accuracy, while present, does not consistently reach the original performance levels, particularly for more complex architectures like ResNet50. This discrepancy raises concerns about the practical applicability of the method in scenarios where high accuracy is paramount.
3. The significant fluctuation in accuracy suggests that the optimized model may lack consistent predictability. The observed variability in accuracy, likely due to the stochastic nature of bit flips, introduces an element of unpredictability that could be problematic for real-world deployments where consistent performance is crucial.

### Questions
1. How does the energy consumption from SRAM accesses compare to the total inference cost of a DNN? While acknowledging that the overall energy consumption hinges on a myriad of factors, providing a general perspective would be insightful.

2. The true efficacy of power savings from the low-voltage operation remains ambiguous. While Table 2 highlights energy savings, it narrowly focuses on the consumption related to SRAM accesses. Given that the large configurations of NeuralFuse exhibit similar MACs to the base models (as seen in Table 7), the feasibility of NeuralFuse, when accounting for its total overhead, merits reconsideration.

3. The unpredictability of model performance under low voltage operation, especially with bit flips at the MSBs, poses challenges for practical implementation. Could you shed more light on its real-world applicability or potential use-cases?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes NeuralFuse, a model-agnostic approach that learns input transformations to generate error-resistant data representations. NeuralFuse dynamically adds a correction term to the model input to protect the DNNs in both nominal and low-voltage scenarios and can be applied to DNNs with limited access. Experimental results show that NeuralFuse can reduce SRAM memory access energy by up to 20-30% while recovering accuracy by up to 57% at a 1% bit error rate.

### Strengths
Strength:

1.	The idea is quite interesting. Without error-aware training (adversarial training), it learns input-dependent, model-agnostic calibrator for the model input, the DNN’s accuracy can be protected.

2.	The proposed neural network can protect the DNN accuracy while still showing energy efficiency benefits.

3.	It thoroughly investigates the transferability to different error rates, model architecture, and quantization bitwidth.

### Weaknesses
Weakness:
1.	The transferability on different error rate and model size is not very good, according to Table 1, which means re-training is still required for different model/dataset/SRAM voltages.

2.	The energy saving is only ~20% by reducing SRAM voltage, while the accuracy drop is beyond 1%. It needs some justification on this trade-off.

3.	The method seems to be equivalent to adding extra layers in the early stage of the network and train it with noise-aware training. Why not train other layers with the memory error? It is not very intuitive that weight errors in all layers (even MSB flips) can be well protected by only changing the model input. More explanation is needed to justify this. Can we add a protector to later layers and do some calibration? Or even parallel branches? Or protect the weights loaded from memory block-wise, which can still maintain model-agnostic?

### Questions
listed in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
