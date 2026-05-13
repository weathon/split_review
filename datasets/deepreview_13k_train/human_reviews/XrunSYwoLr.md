# Spatio-Temporal Approximation: A Training-Free SNN Conversion for Transformers

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Spiking neural networks (SNNs) are energy-efficient and hold great potential for large-scale inference. Since training SNNs from scratch is costly and has limited performance, converting pretrained artificial neural networks (ANNs) to SNNs is an attractive approach that retains robust performance without additional training data and resources. However, while existing conversion methods work well on convolution networks, emerging Transformer models introduce unique mechanisms like self-attention and test-time normalization, leading to non-causal non-linear interactions unachievable by current SNNs. To address this, we approximate these operations in both temporal and spatial dimensions, thereby providing the first SNN conversion pipeline for Transformers. We propose \textit{Universal Group Operators} to approximate non-linear operations spatially and a \textit{Temporal-Corrective Self-Attention Layer} that approximates spike multiplications at inference through an estimation-correction approach. Our algorithm is implemented on a pretrained ViT-B/32 from CLIP, inheriting its zero-shot classification capabilities, while improving control over conversion losses. To our knowledge, this is the first direct training-free conversion of a pretrained Transformer to a purely event-driven SNN, promising for neuromorphic hardware deployment.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study introduces a training-free method to convert ANN transformers into SNNs, preserving the weights of the original pretrained model to ensure its inference capability remains intact. The resulting SNN Transformer model outperforms its convolutional network counterparts.

### Strengths
1.This paper overcomes the differences in computational paradigms between ANN and SNN Transformers, and can accurately approximate ANNs with converted models.

2.The proposed training-free conversion strategy could enable the direct deployment of large-scale pretrained ANN models to low-power neuromorphic hardware.

### Weaknesses
1.The proposed Universal Group Operators use extensive spiking neurons to model fine-grained ANN operations. This high model complexity reduces power efficiency and incurs large memory usage. Specifically, the overhead of converting each ANN operation into a group of spiking neurons, especially for complex operations within the transformer architecture, is a concern. The paper should provide a more detailed analysis of the computational cost, including the number of spiking neurons required per ANN operation and the resulting memory footprint.

2.The current implementation only handles image Transformers. Longer sequences in language models may introduce more unaddressed issues such as threshold variations similar to that in spiking RNN. The paper lacks a discussion on how the proposed method would handle the increased sequence lengths and the potential for error accumulation in language models. The challenges of maintaining consistent spiking activity and avoiding vanishing or exploding gradients in longer sequences need to be addressed.

### Questions
1. Would employing model compression strategies, such as pruning, enhance the efficiency and reduce the size of the Universal Group Operators?

2. The conversion implementation integrates multiple existing ANN-SNN conversion algorithms, including SNM and Burst. Using the same combined conversion for ResNet baselines could enable a more fair comparison.

3. What hurdles might one encounter when adapting this technique to language Transformers? Would the method necessitate modifications?

4. What challenges might arise when adapting this method to larger-scale transformer models?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed Universal Group Operator (UGO) and Spatio-Temporal Approximation (STA) to fit the functions of LayerNorm, GELU layers and optimize the conversion error about self-attention modules.

### Strengths
1. The theoretical analysis about Temporal Estimation & Correction in Eq.5-Eq.11 is convincing.

### Weaknesses
1. From Tab.1-2, it seems that the author's approximate fitting methods for nonlinear operations such as LayerNorm require relatively long time-steps ($\geq 32$) to be effectively implemented, which will result in more significant time latency and energy consumption. In addition, even under 256 time-steps, the author's approximate fitting and error correction methods cannot completely eliminate the conversion error (there is a ~1% accuracy loss). Specifically, the reliance on longer time-steps raises concerns about the practical applicability of the proposed method in real-time or resource-constrained scenarios. It would be beneficial to see a more detailed analysis of the trade-off between time-steps and accuracy, potentially exploring the use of adaptive time-step strategies.

2. Regarding the fitting calculation of LayerNorm and Softmax layers, as well as the self-attention layer error correction calculation in Eq.9, it seems that the calculation steps and costs involved are still relatively large. I think this may hinder the algorithm's practical application. The complexity of these calculations, especially for large-scale models, needs further investigation. A breakdown of the computational cost for each component (LayerNorm, Softmax, and self-attention error correction) would provide a clearer picture of the overhead introduced by the proposed method.

3. I noticed that a previous work [1] achieved similar ANN-SNN Conversion performance to this paper when using BatchNorm layers directly (without involving nonlinear operations) and without error correction for attention modules. So I think the value of this approximate fitting and error correction method still needs to be further evaluated. While the proposed method aims to address the challenges of nonlinear operations, a direct comparison with [1] under similar conditions (e.g., using BatchNorm) would help to quantify the actual benefits of the proposed approach.

### Questions
See Weakness Section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Summary:
The paper proposes a training-free method to convert transformer to SNN platforms. It proposes universal group operators to approximate nonlinear activations and temporal-corrective self-attention layer to approximate spike multiplications. Compared to prior work, it is the first to support pretrained transformers with SNNs without training.

### Strengths
Strength:

1.	The idea is novel. Use multiple spiking neurons to estimate the nonlinearity functions. The temporal-corrective self-attention can achieve unbiased multiplication between two variable matrices. 

2.	The convergence and error bound have solid theoretical guarantees and experimental validation.

3.	Compared to prior work with training/calibration, this work can quickly convert ViT to SNN hardware with high fidelity with a small timesteps T.

4.	It also shows the efficiency benefits compared to ANNs, which justifies the advantages of SNN-based transformer.

### Weaknesses
Weakness:

1.	The latency/runtime benefit of SNN-based transformer with different timesteps T needs to be compared to ANN accelerators.

2.	The proposed method can have a high fidelity with a small timestep, but there is still 1% gap compared to ANNs, even with a large T. 
Compared to the training/calibration-based method, the training-free one shows a higher accuracy gap. (Table2, SNM, Calib on resnet20 can fully recover the accuracy). Can the authors comment on that?

3.	Is there any randomness in the spikes-based multiplications given the current data encoding? If there is, the output of the computing result is not deterministic. How robust is it to randomness? To have a deterministic output, the effective resolution will be reduced, thus harming accuracy. Can the authors comment on that?

4.	How does the spiking-based multiplication differentiate from the standard multiplication mechanism in stochastic computing?

5.	There are other acceleration methods to speed up and reduce energy consumption by a large factor without sacrificing accuracy, e.g., model compression and better architecture design. Moving to a new hardware platform with 30-40% energy reduction seems not very convincing.

### Questions
Questions are listed in the weaknesses part.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This research presents a novel method for spiking neural networks from pretrained Transformer models (or models with multi-head attentions). The suggested Universal Group Operators and Temporal-Corrective Self-Attention Layer allow a pretrained Transformer to be converted to a completely event-driven SNN without the need for training, which holds promise for neuromorphic computing. Effectively positive experimental outcomes were obtained.

### Strengths
The ability to convert pretrained Transformer models into spiking neural networks without the need for training is more appealing than training Spiking Transformers directly.


For neuromorphic computing and widespread deployment, the pure implementation on spiking neurons is promising.



The universal nature of the conversion method used here makes use of linear models' capacity for global approximation. The inverse function is converted correctly.

### Weaknesses
In comparison to conventional artificial neural networks, there may be a slight accuracy gap due to the approximation error from Universal Group Operators. This approximation error is concerning, particularly given the complex non-linear functions within the Transformer architecture. The method's reliance on fitting these functions with a linear combination of spiking neuron outputs introduces a potential bottleneck in performance. The quantization effects, especially the uneven quantization observed in Figure 3, could lead to information loss, further exacerbating this accuracy gap.

The proposed method has only been tested on the ViT-B/32 model from CLIP; it is unknown if it can be applied to other models. This lack of generalization is a significant weakness. The method's applicability to other Transformer variants, which may have different architectural nuances and non-linearities, is not demonstrated. The absence of experiments on other models raises concerns about the robustness and universal applicability of the proposed approach.

The converted models perform computations at a marginally higher rate than traditional spiking CNNs (which have more synapses and neurons). This higher computational cost, despite the potential benefits of event-driven processing, is a practical concern. The method's efficiency compared to existing SNN implementations, especially in terms of spike rate and overall computational load, needs further investigation.

### Questions
From Figure 3, I can observe severe, uneven quantization. Can you explain how this quantization affects the accuracy of the output?

How do you prepare the data for pretraining non-linear activations? For GeLU, do you record the actual responses of the ANN and train it on these activation values? For other nonlinearities (inverse, exp, layer norm), how do you pretrain?

Also, why do these nonlinearities need so many kinds of losses here (Table 3)? Can you explain why Huber loss fits exp, gelu, and inverse? And why does MSE fit the layer norm?

Besides, do you evaluate the actual increment of neurons by using UGO? I want you to give me a table reporting the difference in neuron number and weight according to the models listed in Table 1.

Are you going to release the weight of the pretrained nonlinearity? Do you test the sensitivity of changing $N$ and $T$?

I think there is a typo in equation (22). $V_{th} \Vert w_2\Vert_1$ should be $(V_{th} \Vert w_2\Vert_1)/T$.

Why do you mention setting $V_{th}$ using the strategy proposed by Li et al., who proposed to use dynamic thresholds, and demonstrating the quantization gap using the maximum activation as a threshold?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
