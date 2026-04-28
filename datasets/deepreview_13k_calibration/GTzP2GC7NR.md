# When SNN meets ANN: Error-Free ANN-to-SNN Conversion for Extreme Edge Efficiency

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Spiking Neural Networks (SNN) are now demonstrating comparable accuracy to convolutional neural networks (CNN), thanks to advanced ANN-to-SNN conversion techniques, all while delivering remarkable energy and latency efficiency when deployed on neuromorphic hardware. However, these conversion techniques incur a large number of time steps, and consequently, high spiking activity. In this paper, we propose a novel ANN-to-SNN conversion framework, that incurs an exponentially lower number of time steps compared to that required in the existing conversion approaches. Our framework modifies the standard integrate-and-fire (IF) neuron model used in SNNs with no change in computational complexity and shifts the bias term of each batch normalization (BN) layer in the trained ANN. To reduce spiking activity, we propose training the source ANN with a fine-grained $\ell_1$ regularizer with surrogate gradients that encourages high spike sparsity in the converted SNN. Our proposed framework thus yields lossless SNNs with low latency, low compute energy, thanks to the low time steps and high spike sparsity, and high test accuracy, for example, 75.12% with only 4 time steps on the ImageNet dataset. Codes will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel ANN-SNN conversion framework that significantly reduces the number of required time steps while maintaining high accuracy and computational efficiency. By integrating the QCFS activation function and adjusting the biases of the BN layers, the paper demonstrates how to achieve consistency in activation outputs between ANN and SNN without increasing computational complexity.

### Strengths
1. The writing is generally smooth, and the arguments presented are supported by corresponding proofs and experiments.
2. The experimental results show certain advantages, suggesting that this may be a promising approach.

### Weaknesses
1. This paper merely introduces a spiking neuron model rather than a new conversion paradigm, which limits its novelty.
2. The integration of BN layers is not new.
3. The authors' discussion and proofs seem to revolve around the equation s^l(t) = a^l_{t}. However, the authors directly present this point without sufficiently establishing the rationale for the validity of this equation, which raises doubts.
4. The data presented in Table 1 is concerning, as it does not align with the data from the original papers cited.

### Questions
1. Can the authors provide a detailed example to clarify the meaning of the relationship between \(s^l(t) = a^l_{t}\), \(T = \log_2 Q\), and the relationship between \(a^{(l-1)}\) and \(2^{(t-1)} s^{(l-1)}(t)\)?
2. In Table 1, for the ResNet18 model, the ANN accuracy for the OPI method is stated as 92.74%, whereas the original paper reports an accuracy of 96.04%. The results for the BOS method on VGG16 and ResNet18 models for T=8,T=16,T=32 are inconsistent with the original paper. Additionally, for the ResNet20 model, the original ANN accuracy for BOS is reported as 91.77%, but the authors present it as 93.3%. The results for T=6,T=8,T=16,T=32 also do not match those in the original BOS paper. Please provide a reasonable explanation for these discrepancies.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper outlines a framework for transitioning Quantized Neural Networks (QNN) to Spiking Neural Networks (SNN) with the goal of markedly reducing the time steps for achieving top-tier accuracy while keeping computational complexity low. Modifications to the standard integrate-and-fire (IF) neuron model, adjustments to the bias terms in batch normalization (BN) layers, and the addition of regularizer terms are proposed to boost the efficiency of the conversion.

### Strengths
+ The manuscript analyzes key errors inherent in ANN-to-SNN conversion approaches, highlighting areas critical for improving conversion accuracy.
+ The work implements binary encoding during the conversion of Quantized Neural Networks (QNN) to Spiking Neural Networks (SNN), which reduces the number of time steps required.

### Weaknesses
 + The paper's reliance on training ANNs from scratch using the QCFS activation function restricts its ability to convert pre-existing ANNs directly to SNNs. Thus, the definition of 'error-free' conversion provided is narrow, only ensuring the error-free transition from QCFS-equipped ANNs (equivalent to QNNs) to SNNs. This limitation significantly reduces the practical applicability of the proposed method, as it necessitates retraining existing models, which is computationally expensive and time-consuming. The paper does not adequately address the challenges of adapting the QCFS activation function to models trained with more common activation functions like ReLU, which would be crucial for real-world deployment.
+ As in the domain of QNNs->SNNs, the approach to modifying integrate-and-fire (IF) neurons by separating their Accumulation and Generation phases does not significantly stand out from similar methods previously established in Spikeconverter [1]. The specific implementation details regarding the accumulation and generation phases are not sufficiently differentiated from existing methods. The paper lacks a detailed comparison of the proposed neuron model with other existing models, particularly in terms of computational complexity and hardware implementation feasibility. The novelty of the proposed approach is therefore questionable.

### Questions
see Weaknesses.

### Soundness
3

### Presentation
2

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
This paper presents a novel ANN-to-SNN conversion framework that incorporates a modified IF neuron model and shifts the bias term of each batch normalization layer in the source ANN, along with a fine-grained ℓ1 regularizer. The framework achieves remarkable results, reaching 75.12% accuracy on ImageNet with only 4 time steps. This work makes two significant contributions: it achieves an exponential reduction in the required number of time steps while simultaneously establishing a new state-of-the-art benchmark for ANN-to-SNN conversion methods.

### Strengths
1. The paper provides rigorous theoretical analysis, with clear mathematical proofs demonstrating how the modified IF neuron model and batch normalization layer bias shifts successfully eliminate quantization error at T = log2Q. The theoretical foundation is well-established and thoroughly documented.
2. The framework achieves exceptional empirical results, notably reaching 75.12% accuracy on the challenging ImageNet dataset with only 4 time steps. This represents a significant advancement in the field, as achieving such high accuracy with such low latency on large-scale datasets has been a longstanding challenge in ANN-to-SNN conversion research.

### Weaknesses
1. The motivation for introducing the fine-grained ℓ1 regularizer is inadequately explained. While the paper's primary goal is to address the low accuracy of ANN-to-SNN conversion under low time steps, the authors don't sufficiently justify why compressing spiking activity is necessary. This raises questions about whether such compression might actually degrade SNN performance rather than enhance it. The paper lacks a clear explanation of how this regularization directly contributes to improved accuracy or reduced latency, especially when the primary focus is on minimizing time steps.
2. The paper lacks comprehensive comparisons with state-of-the-art BPTT-only methods. Current BPTT-based approaches have demonstrated the capability to achieve over 80% accuracy on ImageNet with only 4 time steps[1], yet this benchmark is not addressed in the comparative analysis. The absence of a direct comparison with these methods, particularly those achieving higher accuracy at similar latencies, makes it difficult to assess the true advancement of the proposed approach.
3. The paper's error analysis framework lacks clarity. While the proposed method appears to target unevenness error, Section 4 focuses mainly on deviation error. In [2], deviation error is categorized into clipping error, quantization error, and unevenness error. The authors seem to use QCFS from [2] to address the first two errors and their novel ANN-to-SNN conversion framework to solve Unevenness error. However, this logical progression and the relationships between different error types are not clearly explained. The distinction between deviation error and unevenness error, and how the proposed method specifically addresses the latter, needs further clarification.
4. The paper exhibits organizational issues with equation numbering and placement. For instance, equations 3 and 4 on line 133 are not presented in sequential order, indicating a need for better structural organization of mathematical content. This lack of sequential presentation disrupts the logical flow of the mathematical arguments and makes it harder to follow the derivation.

### Questions
1. Review and improve the logical consistency throughout the paper's details.
2. Clarify the similarities and differences between deviation error and unevenness error.
3. The authors should release their code to demonstrate the reproducibility of their proposed method.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on SNNs on CV tasks, particularly the image recognition task on ImageNet and CIFAR-10. The overall method is making SNN neurons more artificial to reduce the gap between the target ANN and the SNN after ANN-to-SNN conversion to achieve ultra-fast SNN inference. Constraints on firing rate and quantization are added during ANN training; an error correction method is used during SNN inference, specifically, by revising the spiking neuronal model.

The writing style and table style mainly follow [1], and Figure 1 likely follows the style of Figure 1 in [2].

[1] Bu T, Fang W, Ding J, et al. Optimal ANN-SNN conversion for high-accuracy and ultra-low-latency spiking neural networks[J]. arXiv preprint arXiv:2303.04347, 2023.

[2] Li C, Ma L, Furber S. Quantization framework for fast spiking neural networks[J]. Frontiers in Neuroscience, 2022, 16: 918793.

### Strengths
1. The abstract is well-written, and I particularly like the first sentence. It clearly and effectively summarizes the current state of research on SNN algorithms.

2. Bias correction itself is not new, but this paper gives a format about conducting the bias shift with BN layers, which is new.

### Weaknesses
1. Line 59: "Our resulting SNN can be implemented on neuromorphic chips, such as Loihi (10)." Please provide experimental results demonstrating implementation on Loihi, or clarify how the proposed method is compatible with Loihi's constraints without actual implementation.

2. Line 125 "QCFS can enable ANN-to-SNN conversion with minimal error for arbitrary T and Q, where T denotes the total number of SNN time steps. ". How "arbitrary" is ensured? Please provide specific examples or experimental results demonstrating QCFS performance across a range of T and Q values, or explain the theoretical basis for this claim.

3. Line 159 "Importantly, the resulting function is equivalent to the ANN ReLU activation function, because ϕl(T)≥0." Is the resulting function Equation 6? Why does this function equal to ReLU? Please provide a more detailed explanation or mathematical proof of why ϕl(T)≥0 implies equivalence to ReLU, including any assumptions or conditions required. The current explanation lacks sufficient detail to establish a clear causal relationship between a positive value and equivalence to ReLU. Several intermediate steps are omitted in demonstrating how a positive value leads to equivalence with ReLU, which makes the claim unclear.

4. Line 192 "As our work already enables a small value of T, the drop in SNN performance with further lower T <log2Q becomes negligible compared to prior works.". Why small T make your performance drop negligible? I do not see obvious logical relationships between time steps T and performance drop. Does any proof support this? Please provide empirical evidence or theoretical analysis demonstrating how the performance drop changes with T, particularly for T <log2Q, compared to prior works.

5.  " Moreover, at low timesteps, the deviation error increases as shown in Fig. 2(a), and even dominates the total error, which highlights its importance for our use case. " Why will the deviation error dominate the total error? Is this your imagination or do you actually have quantitative experiments to support this? Please provide quantitative analysis or experimental results that break down the components of the total error at different timesteps, showing how the proportion of deviation error changes. Alternatively, citing papers that illustrated this point. I strongly disagree with giving such a strong claim without any support.

6. "In particular, spikes are transmitted to the next layer as soon as they are computed. Moreover, our implemented framework adheres to this scheme and thus our reported
accuracies are consistent with the asynchronous implementation." This sentence is a little bit confusing. Why wait T time for each layer will not slow down SNN inference and will not damage the asynchronous implementation? Please clarify how your method maintains asynchronous behavior while still requiring T timesteps for each layer, perhaps by providing a more detailed description of the spike transmission process or a diagram illustrating the timing of computations across layers.

7. Line 804. In this equation, it seems that the β_c^l is replaced by β^l directly. Why it is legit to do this direct replacement? The last sentence of Theorem I (Line 815), β_c^l does not equal β^l. Yet, in the Proof (Line 820), β_c^l is replaced with β^l directly, which seems inconsistent.

8. Line 209 "In this section, we propose our ANN-to-SNN conversion framework, which involves training the
source ANN using the QCFS activation function (5), followed by 1) shifting the bias term of the BN
layers, and 2) modifying the IF model where the neuron spiking mechanism and reset are pushed after
the input current accumulation over all the time steps.". This summary of Section 5 is completely missed to mention the contents in Section 5.2. Are the L1 Norm introduced in Section 5.2 a major part of your method anymore? Please  include the content from Section 5.2 in the summary if it is indeed a major part of their method, or to explain why it was omitted and clarify its role in the overall framework.

9. Line 329. Could you give an example of what "a" in the equation represents? The other two questions are, how t in SNN can be explicitly represented in ANN during ANN training, and how summation is conducted in ANN training? Does it need to modify each layer`s computations to support summation on time dimension?

10. The addition of constraints in training for better ANN-to-SNN conversion, the modifications of neuronal models, and the application of error correction methods—as well as the overarching methodology of enhancing SNN performance by making SNN more artificial were not new ideas. It was proposed in [1] and probably some in other previous studies. Please give credits to previous related paper(s).

11. Are you the first one to use L1 norm in SNN research? If not, please cite previous papers and discuss the differences to previous work that uses L1 Norm. Also, I do not find the L1 norm contents to have a tight connection to your other methods. L1 norm is also not discussed in the related work section and the summary in the beginning of the method section.

### Questions
Except for questions in the weaknesses section,  I have three minors listed below:

1. "However, these conversion techniques incur a large number of time steps, and consequently, high spiking activity". It is not obvious more time steps lead to high spike activity. Does any equation support this?

2. "while leveraging quantization-aware training in the ANN domain(2; 5). ". Could you specify which contents in reference (2) talk about "quantization-aware training in the ANN domain"?

3. “In fact, there is only a ∼3% (36.2% to 33.0%) drop in the spiking activity of a VGG16-based SNN”. Revise to "We observed ~3%...". "there is" is inappropriate as there is not any "there" that shows these detailed quantitative results in the rest of the paper. If you actually want to point to a position that presents these results, please write exactly which figure and results in which section you refer to. e.g. " “In fact, we can see from Figure x and it only has a ∼3% (36.2% to 33.0%) drop"

### Soundness
2

### Presentation
3

### Contribution
2
