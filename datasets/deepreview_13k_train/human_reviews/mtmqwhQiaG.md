# Canonic Signed Spike Coding for Efficient Spiking Neural Networks

- Decision: Reject
- Scores: 6, 6, 6, 3

## Abstract
Spiking Neural Networks (SNNs) seek to mimic the spiking behavior of biological neurons and are expected to play a key role in the advancement of neural computing and artificial intelligence. The conversion of Artificial Neural Networks (ANNs) to SNNs is the most widely used training method, which ensures that the resulting SNNs perform comparably to ANNs on large-scale datasets. The efficiency of these conversion-based SNNs is often determined by the neural coding schemes. Current schemes typically use spike count or timing for encoding, which is linearly related to ANN activations and increases the required number of time steps. To address this limitation, we propose a novel Canonic Signed Spike (CSS) coding scheme. This method incorporates non-linearity into the encoding process by weighting spikes at each step of neural computation, thereby increasing the information encoded in spikes. We identify the temporal coupling phenomenon arising from weighted spikes and introduce negative spikes along with a Ternary Self-Amplifying (TSA) neuron model to mitigate the issue. A one-step silent period is implemented during neural computation, achieving high accuracy with low latency. We apply the proposed methods to directly convert full-precision ANNs and evaluate performance on CIFAR-10 and ImageNet datasets. Our experimental results demonstrate that the CSS coding scheme effectively compresses time steps for coding and reduces inference latency with minimal conversion loss.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a novel approach that reduces coding time steps by weighting individual spikes, allowing each spike to transmit increased information density. The introduction of negative spikes successfully breaks temporal dependencies, thereby reducing inference delay. The proposed Compressed Spike Sequence (CSS) encoding method improves both throughput and processing speed in converted Spiking Neural Networks (SNNs), while maintaining minimal conversion accuracy loss, providing an effective solution for enhancing the practical efficiency of SNNs.

### Strengths
1.This paper proposes a novel non-linear coding approach named Compressed Spike Sequence (CSS) that breaks the linear relationship constraints inherent in traditional coding schemes.
2.The paper introduces negative spikes and a one-step silent period mechanism that balances coding efficiency and inference latency.
3.The method is comprehensively validated on standard datasets including CIFAR-10 and ImageNet, with extensive testing across network architectures of varying depths (such as VGG and ResNet), and detailed ablation studies analyzing the contribution of each component.
4.The proposed approach achieves nearly lossless ANN-to-SNN conversion with fewer time steps, and can be directly applied to full-precision ANNs without additional quantization training.

### Weaknesses
1.The proposed coding scheme lacks sparsity characteristics, which may lead to higher energy consumption. Specifically, the use of weighted spikes, while increasing information density per spike, inherently reduces the number of zero-activity time steps, thus limiting potential energy savings from sparse activations. This is a significant concern, as sparsity is a key advantage of SNNs over traditional ANNs.
2.The selection of parameters (such as \beta and \theta) lacks theoretical guidance. The paper does not provide a clear methodology for choosing these parameters, which could lead to suboptimal performance. The impact of these parameters on the overall performance and convergence of the network needs to be more thoroughly investigated and justified.
3.Hardware implementation requires processing exponential operations of \beta, handling both positive and negative spikes, and controlling the silent period. The need for exponential operations introduces computational overhead, and the management of both positive and negative spikes adds complexity to the hardware design. Furthermore, the precise control of the silent period requires additional circuitry, which could increase the area and power consumption of the hardware.

### Questions
1.What is the energy consumption of this SNN compared to ANN? It is suggested to add comparative experiments on energy consumption.
2.What is the level of support for this type of neuron in existing neuromorphic hardware? Is deployment and implementation feasible in the future?

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
4

### Summary
This paper introduces a novel Canonical Signed Spike coding for Spiking Neural Networks to enhance performance and reduce latency in ANN-SNN conversions. The CSS incorporates non-linearity by weighting spikes and negative spikes, allowing more information per time step. The authors also propose a Ternary Self-Amplifying neuron model to further reduce latency. Experimental results on CIFAR-10 and ImageNet show that CSS improves inference latency and accuracy with minimal conversion loss, advancing SNN performance on large-scale datasets.

### Strengths
The paper's approach of using negative spikes for information encoding is innovative. This technique may compensate for the over firing issue and reduce conversion error.

The one-step silent period seems to be an effective approach which significantly enhances the performance of SNN models.

### Weaknesses
The ablation study provided in this paper is insufficient. As it stands, the empirical results primarily support the effectiveness of the negative spike and silent period techniques. A more detailed evaluation of the amplification factor's effect is necessary. Moreover, a comprehensive comparison between the TSA neuron and the standard IF neuron would better highlight the advantages of the proposed neuron model.

The paper is hard to follow and sometimes confusing. For example, the final neuron function for TSA neurons is not provided in the manuscript, which makes it difficult to fully understand the general behavior of the TSA neuron. Clear and detailed descriptions of such core elements are essential for readability and comprehension.

### Questions
Equation 3 makes no sense since the dirac function is a generalized function and is only well-defined within an integral over a specified range. The authors should consider using heaviside step function to describe the neuron firing.

Equation 3 appears to represent the discrete form of a LIF neuron function. However, based on the experiments, the scaling factor $\beta$ is consistently set to values greater than one, which is atypical for a traditional LIF neuron model. 

To improve clarity, it would be beneficial if the authors provide the explicit mathematical function for the TSA neuron model. 

It confuses me whether CSS coding serves as an input encoding method for the SNN or if it refers to the encoding capabilities inherent in the TSA neuron itself.

In lines 305-306, it is mentioned that a new term is added to the right side of Equation 8 after a silent period. Could the authors clarify the purpose of doing so?

It would be better if the authors can provide the pseudo code for the conversion and the inference process.

### Soundness
2

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
The paper proposes a novel spiking input encoding called Canonic Signed Spike (CSS), which incorporates non-linearity into the encoding process by weighting spikes at each step of neural computation. To mitigate the temporal coupling phenomenon in the SNN using CSS encoding, the paper proposes a Ternary Self-Amplifying (TSA) neuron model and a one-step silent period, which reduces the encoding latency.

### Strengths
1. The idea that decouples the input and output when inference SNN is novel.
2. The experiments are detailed and convincing.

### Weaknesses
1. The method section is hard to read and some notations are not explained. For example, what are the detailed steps that generate Eq(5), and what is the meaning of τ (\tau) in Eq(5)? 
2. The compared SOTA work in rate code is not superior. Fast-SNN [1] and Offset[2] works can achieve lossless conversion accuracy with less latency (time-step).
3. The energy consumption of the SNN encoded by CSS is missing. 
I will raise my rating if the authors can solve the questions.

### Questions
1. Can the author provide a comparison between this work and other SOTA SNN conversion works such as (Fast-SNN[1], Offset[2])? 
2. Can the author provide the number of synaptic operations of the SNN using CSS? The calculation code can be found in https://github.com/zhouchenlin2096/Spikingformer/tree/master/energy_consumption_calculation.
3. Can the authors provide a more simple explanation of the equivalence of ANNs and SNNs?


[1] Hu Y, Zheng Q, Jiang X, et al. Fast-SNN: fast spiking neural network by converting quantized ANN[J]. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023.
[2] Hao Z, Ding J, Bu T, et al. Bridging the gap between anns and snns by calibrating offset spikes[J]. arXiv prepri

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new ANN-SNN Conversion learning framework, which is based on Canonic Signed Spike (CSS) coding scheme and Ternary Self-Amplifying (TSA) neuron model.

### Strengths
1. The authors conduct theoretical analysis and proof for the ANN-SNN Conversion process based on CSS coding scheme.

### Weaknesses
1. The concept of firing negative spikes has already been proposed by [1].
2. This paper involves firing negative spikes, however, most of the comparative works selected by the authors in Table 2 are based on firing binary spikes. Furthermore, training high-performance converted SNN models under low time latency is currently one of the research focuses in the domain of ANN-SNN Conversion, but the authors do not reveal the performance of CSS under low time latency ($\leq 4$ time-steps) as demonstrated in [1, 2, 3].

### Questions
See Weakness Section.

### Soundness
1

### Presentation
2

### Contribution
1
