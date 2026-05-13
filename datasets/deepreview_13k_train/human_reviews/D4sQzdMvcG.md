# QAC:Quantization-Aware Conversion for Mixed-Timestep Spiking Neural Networks

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Spiking Neural Networks (SNNs) have recently garnered widespread attention due to their high computational efficiency and low energy consumption, possessing significant potential for further research. Currently, SNN algorithms are primarily categorized into two types: one involves the direct training of SNNs using surrogate gradients, and the other is based on the mathematical equivalence between ANNs and SNNs for conversion. However, both methods overlook the exploration of mixed-timestep SNNs, where different layers in the network operate with different timesteps. This is because surrogate gradient methods struggle to compute gradients related to timestep, while ANN-to-SNN conversions typically use fixed timesteps, limiting the potential performance improvements of SNNs. In this paper, we propose a Quantization-Aware Conversion (QAC) algorithm that reveals a profound theoretical insight: the power of the quantization bit-width in ANN activations is equivalent to the timesteps in SNNs with soft reset. This finding uncovers the intrinsic nature of SNNs, demonstrating that they act as activation quantizers—transforming multi-bit activation features into single-bit activations distributed over multiple timesteps. Based on this insight, we propose a mixed-precision quantization-based conversion algorithm from ANNs to mixed-timestep SNNs, which significantly reduces the number of timesteps required during inference and improves accuracy. Additionally, we introduce a calibration method for initial membrane potential and thresholds. Experimental results on CIFAR-10, CIFAR-100, and ImageNet demonstrate that our method significantly outperforms previous approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a novel Quantization-Aware Conversion (QAC) algorithm to optimize Spiking Neural Networks (SNNs). Based on the theorem that the quantization bit-width in ANN activations is equivalent to the timesteps in SNNs with a soft reset, the authors introduce a mixed-precision quantization-based conversion method. This approach enables ANNs to be efficiently converted into mixed-timestep SNNs, significantly reducing the required timesteps and improving accuracy during inference. Additionally, the paper presents a calibration method for the initial membrane potential and thresholds, further enhancing performance. Experimental results demonstrate that this method outperforms existing approaches on the several static image classification datasets.

### Strengths
The proposed method enables ANNs to be efficiently converted into mixed-timestep SNNs through mixed-precision quantization, reducing the average timesteps during inference while maintaining accuracy.

### Weaknesses
1. This work lacks sufficient innovation, as it primarily combines existing ANN mixed-precision quantization and ANN-SNN conversion methods to transform an ANN into a mixed-timestep SNN. Although the authors integrate these techniques, the approach remains largely unchanged, offering limited novelty. For example, their discussion of various gradient cases in QAT parameter selection closely aligns with previously referenced work [1]. Additionally, while the authors claim in their contributions to reveal that the ANN activation quantization bit-width is equivalent to the timestep in SNNs with a soft reset, similar insights have already been discussed in prior researches [2][3].
2. The authors convert an ANN into a mixed-timestep SNN, where different layers in the SNN may have different timesteps. However, they do not explain how data flows within such a mixed-timestep structure, how modules with different timesteps are connected, whether this can be implemented in hardware, and whether the asynchronous nature of the SNN can be maintained simultaneously.
3. In the experiments, the authors only tested on static datasets without using dynamic datasets. Could this be related to the question of asynchronous behavior mentioned previously?
4.Some figures in the paper take up considerable space while conveying limited information, and in some figures, the text is too small to read clearly. It is recommended to rearrange these figures for better clarity and efficiency of space.

### Questions
Please see weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a Quantization-Aware Conversion (QAC) method tailored for training Spiking Neural Networks (SNNs). A significant innovation highlighted is the establishment of a theoretical equivalence between the quantization bit-width of activations in Quantized Neural Networks (QNNs) and the timesteps used in SNNs. This equivalence forms the basis for a new training approach that optimizes both the computational efficiency and accuracy of SNNs. The paper substantiates these claims through experimental validation on standard datasets, including CIFAR-10, CIFAR-100, and ImageNet. Results indicate that the QAC method surpasses existing ANN-to-SNN conversion techniques in terms of both accuracy and operational efficiency

### Strengths
+ Introduction of a novel insight that links the quantization bit-width in ANNs to the timesteps in SNNs, supporting the use of mixed-timestep strategies for SNNs.

+ Development of a mixed-precision quantization-based conversion algorithm that translates ANNs into mixed-timestep SNNs, optimizing for both accuracy and computational efficiency.

+ Experimental results on various image recognition datasets, demonstrating improvements over traditional conversion methods in terms of both accuracy and timestep efficiency.

### Weaknesses
 + The training procedure for the Quantization-Aware Conversion (QAC) includes two distinct phases, necessitating an additional training step to calibrate the membrane potentials' initial values and thresholds. This essentially doubles the training cost. It is crucial that the paper assesses the impact of this calibration step both before and after its application. Including ablation studies to highlight the effects of this calibration would provide a clearer picture of its necessity and impact, which should be explicitly stated for a fair comparison with other methods.
+ The QAC method appears to employ a Quantization-Aware Training (QAT) approach to train a Quantized Neural Network (QNN) before converting it to an SNN, rather than supporting the direct conversion of existing ANNs into SNNs. This positions QAC more as a specialized training method rather than a straightforward conversion technique. To fairly evaluate the efficacy and practicality of QAC, comparative experiments against direct training methods should be conducted. These comparisons would effectively showcase the trade-offs involved, helping to better position QAC in the landscape of SNN training methodologies and underline its specific advantages and limitations.

### Questions
See Weaknesses.

### Soundness
3

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
4

### Summary
This paper presents an ANN-to-SNN conversion method, called Quantization-Aware Conversion (QAC). It reveals the relationship between the quantization levels of activations in ANNs and the timesteps in SNNs. Drawing inspiration from the mixed precision quantization technique used in ANNs, QAC allows for converting ANNs to SNNs with varying timesteps. Experimental results demonstrate that QAC achieves competitive performance compared to state-of-the-art methods with few timesteps.

### Strengths
1. This paper is technically solid. It details the equivalence between the quantization levels of activations in ANNs and the timesteps in SNNs, the four cases of gradient estimation, and the calibration of initial membrane potential.
2. The proposed QAC method yields SNNs with few timesteps.

### Weaknesses
1. The motivation for this technique is unclear. This paper reveals the equivalence between the quantization bit-width of ANN activations and the timesteps in SNNs with soft-threshold resets. However, if the quantized ANNs are equivalent to SNNs with soft reset, why don't we just use the quantized ANNs? I suggest the authors highlight the advantages of SNNs compared to the quantized ANNs.
2. The performance of the converted SNNs by the QAC method lags behind the state-of-the-art methods with more timesteps.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

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
This paper proposes Quantization-Aware Conversion (QAC) algorithm, which is a new ANN-SNN Conversion scheme based on mixed precision quantization and calibrating the membrane-related parameters (e.g. initial membrane potential and firing threshold).

### Strengths
1. In Eqs.(7)-(10) and Fig.2, the authors' analysis for four cases regarding parameter settings is interesting.
2. The authors calibrate the initial membrane potential and threshold under the condition of freezing pretrained weights.

### Weaknesses
1. In Fig.1, it seems that the inference time-steps of the converted SNN in different layers are various. Therefore, I would like to know if the authors choose vanilla IF model that emits binary spikes during the inference phase? Assume that the $l$-th layer adopts $T_l$ time-steps, when $T_l\neq T_{l+1}$, how do the IF neurons in the $l+1$-th layer receive the spike seqence $[oldsymbol{s}^l(1),...,oldsymbol{s}^l(T_l)]$ from the previous layer?

### Questions
See Weakness Section.

### Soundness
2

### Presentation
2

### Contribution
2
