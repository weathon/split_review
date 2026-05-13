# Exploring the Limitations of Layer Synchronization in Spiking Neural Networks

- Decision: Reject
- Scores: 6, 8, 6, 3

## Abstract
Neural-network processing in machine learning applications relies on layer synchronization. This is practiced even in artificial Spiking Neural Networks (SNNs), which are touted as consistent with neurobiology, in spite of processing in the brain being in fact asynchronous. A truly asynchronous system however would allow all neurons to evaluate concurrently their threshold and emit spikes upon receiving any presynaptic current. Omitting layer synchronization is potentially beneficial, for latency and energy efficiency, but asynchronous execution of models previously trained with layer synchronization may entail a mismatch in network dynamics and performance. We present and quantify this problem, and show that models trained with layer synchronization either perform poorly in absence of the synchronization, or fail to benefit from any energy and latency reduction, when such a mechanism is in place. We then explore a potential solution direction, based on a generalization of backpropagation-based training that integrates knowledge about an asynchronous execution scheduling strategy, for learning models suitable for asynchronous processing. We experiment with 2 asynchronous neuron execution scheduling strategies in datasets that encode spatial and temporal information, and we show the potential of asynchronous processing to use less spikes (up to 50\%), complete inference faster (up to 2x), and achieve competitive or even better accuracy (up to $\sim$10\% higher). Our exploration affirms that asynchronous event-based AI processing can be indeed more efficient, but we need to rethink how we train our SNN models to benefit from it.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Current spike neural networks (SNNs) must compute and integrate all presynaptic currents from the previous layer before performing calculations for the neurons in the next layer. This dependence on layer synchronization deviates significantly from the original intention of asynchronous SNN design. Ideally, neurons should be able to emit and receive spike currents at any time and at any location within the network. In this paper, the authors address this issue and explore potential solutions. They propose a generalized approach for gradient training that allows for scheduling strategies using asynchronously processing neurons. Experiments demonstrate that this method can save energy and improve latency under asynchronous processing.

The authors highlight a key issue within the SNN research community: most SNNs are layer-synchronized, i.e., time-driven, rather than achieving the original goal of implementing asynchronous event-driven mechanisms. The authors discuss and conduct some experiments on asynchronous networks, and the results are intriguing.

At this stage, my rating is "6: Marginally above acceptance threshold." I would be very willing to raise my score if the authors could address and clarify the following issues.

### Strengths
1. **Importance of the Research Content**: Although the original intention of SNN research was for asynchronous computation, most current SNN work is time-driven (i.e., layer-synchronized as mentioned in the paper). However, the asynchronous design of SNNs is crucial for applications in event-driven neuromorphic processors. This paper could contribute significantly to the SNN research community.

2. **Novelty of the Results**: The experiments presented in the paper showcase many intriguing advantages of the asynchronous design, such as enhanced neuronal activity while the overall network remains sparser (Figure 2); key information flowing freely during asynchronous inference (Figure 3); and reduced inference latency under asynchronous network processing (Figure 4). These results provide strong support for the future development of asynchronous computation.

### Weaknesses
1. **Accuracy of Unlayered Method**: I reviewed the accuracy of the Unlayered method (Table 2), and it generally falls below that of the traditional Layered method. What is the network architecture of the Layered methods compared in Table 2? Can the performance of the Unlayered method be demonstrated using the network architecture from this work [1]? Because these networks are more used by SNN researchers, it would be more convincing to compare the methods in the same network structure.
2. **Network Sparsity and Energy Consumption**: The paper presents many instances of network sparsity; however, the neuronal activity has also increased, and these two factors have opposing effects on energy consumption. Which of these factors is dominant?   Could experiments be conducted to analyze the energy trade-off between the increased neuronal activity and network sparsity, further investigating the impact of each factor on energy consumption within the asynchronous framework? Table 3 shows the energy efficiency of asynchronous computation, but there is no significant reduction, and it does not even decrease by an order of magnitude. I find this outcome somewhat unsatisfactory. Could the authors provide some clarification?

### Questions
1. **Input Encoding in Asynchronous Processing Framework**: How is event data encoded as input into the network within the asynchronous processing framework? Although lines 210-215 provide an explanation, I am still unclear about the form of the input data. Could the authors provide some equations for clarification? Perhaps an example with a single input event could be illustrated step-by-step, or a small code snippet could be submitted to demonstrate how a single input event is encoded and processed within the asynchronous framework.

2. **UNLAYERED BACKPROPAGATION**: In UNLAYERED BACKPROPAGATION, due to the dynamic nature of asynchronous processing, the backpropagation may occur across layers rather than layer-by-layer in a chained manner. Does this training approach lead to faster convergence during network training?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper highlights an important aspect of SNN, that is asynchronous computation of spikes, resulting in energy efficiency.  This work points out that, the training of SNN uses GPU and when deployed on asynchronous neuromorphic processes, the performance may be reduced during inference if asynchronous computation is adopted.

An generalized backpropagation algorithm is introduced which exploits the vectorized computation of the hardware and also allows asynchronous computation during inference without compromising the accuracy.

### Strengths
The paper is well-written and easy to follow. 

Highlighted an important aspect of training SNNs (asynchronous computation) which is generally ignored while training SNN models. 

The related work is very well explained, with their contributions and limitations. 

Through empirical results, the paper demonstrates the effectiveness of the proposed algorithm in terms of sparsity and accuracy.

### Weaknesses
It's commendable that the authors have highlighted the asynchronous aspect of SNNs. Could the authors provide some comparative empirical results in terms of accuracy and sparsity with some previous works?

For example, the state of the art directly trained SNN models. Such as, [1,2,3], I believe they belong to the class of synchronous computation of spikes.

[1] Temporal Efficient Training of Spiking Neural Network via Gradient Re-weighting

[2] GLIF: A Unified Gated Leaky Integrate-and-Fire Neuron for Spiking Neural Networks

[3] Membrane Potential Batch Normalization for Spiking Neural Networks

### Questions
Check the Weaknesses.

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
3

### Summary
This paper points out most current works train SNNs in a synchronous way, while SNNs should be running in an asynchronous environment, which leads to a gap. Then this paper quantifies this gap and develops a training method better suited for asynchronous inference. Experiments show the effectiveness of this method in accuracy, inference speed, and energy consumption.

### Strengths
This paper considers a critical problem for SNNs that they are expected to run in an asynchronous way, while most current SNN training strategies train them synchronously.

### Weaknesses
1. See questions.
2. There are some word and grammar mistakes and some figures should be improved. For example, 'compex' in line 363 should be 'complex', 'To what extent this is the case is not explored in this work.' in line 334 is incoherent, the legends in Figure 4 stretches over two subfigures.

### Questions
1. I am not sure about Algorithm 1. Does $\boldsymbol s$ represent whether there is a spike or the timing of the spike? If it represents the timing, why it is an integer? If it represents whether there is a spike, how to determine the arrival order of input spikes, which is critical in asynchronous simulation?
2. In SelectSpikes() in Algorithm 1, the two scheduling policies seem not to consider the difference in input spike arrival times. How the asynchornization is achieved then?
3. Due to the above reasons, I am not sure whether Algorithm 1 reflects the real asynchronous property of SNNs. If not so, the comparisons in the experiments are not fair since layered training with async RS inference is not a practical situation.
4. How the classification result is determined by the network? What do 'on output', 'on spiking done', and 'forward steps after output' in Figure 2 and Figure 3 mean?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an asynchronous simulation method for deep SNNs. The network structure, vectorized simulation algorithm, backward methods, and experiment results on some simple datasets are provided.

### Strengths
As we know, most (or all?) existing software frameworks for deep SNNs use a (layer-wise) synchronous simulation method. The idea of the asynchronous simulation in this paper is very interesting. The source codes in the supplementary materials indicate that the authors have developed an asynchronous primary software framework, which will benefit the SNN community.

### Weaknesses
Unfortunately, this paper is written unclearly. The difference between synchronous and asynchronous simulation methods is not explained clearly. It is better to illustrate the difference by a figure, i.e., an example to show thow the synchronous/asynchronous method simulates an SNN.

The advantages of using the asynchronous simulation method are not shown. I guess that this simulation method is more similar to how the asynchronous neuromorphic chip works. However, I believe that not all of SNN researchers are familiar to the hardware, and it is hard for them to understand the advantages of asynchronous simulation without the knowledge about neuromorphic chips I suggest that the authors add more background knowledge about asynchronous neuromorphic chips (such as uBrain and Speck), and why the existing simulation methods are not so good for them such as the difference between synchronous simluation and asynchronous on-chip inference.

I am not sure that I really understand the methods in this paper. Thus, I have the following questions. Please feel free to clarify my wrong understanding. 

What is the role of `c` in Algorithm 1? It is only used as the output.

I am not sure if the key characteristic of the proposed asynchronous method is "selecting spikes". More specifically, suppose a layer has `N` inputs, the previous synchronous simulation method uses the spike tensor `S` with `N` elements as inputs. The proposed method will firstly apply a scheduling strategy to create a `mask` to select elements (spikes) in `S`, and use `S[mask]` as inputs. If so, it seems that this characteristic is trying to mimic the asynchronous spike firing in chips, which do not have a global clock. The role of the global clock is similar to "time-step" in SNNs simulated by the synchronous method. Then, what is the relation between the asynchronous spike firing in chips and the randomly selecting in simulation? I guess (note that I am not the expert of neuromorphic hardware) that the events (spikes) are processed (chronologically) orderly in chips, and this behavior is more similar to the synchronous simulation with a large number of time-steps. While the randomly selecting is disordered.

### Questions
I am not sure that I really understand the methods in this paper. Thus, I have the following questions. Please feel free to clarify my wrong understanding. 

What is the role of `c` in Algorithm 1? It is only used as the output.

I am not sure if the key characteristic of the proposed asynchronous method is "selecting spikes". More specifically, suppose a layer has `N` inputs, the previous synchronous simulation method uses the spike tensor `S` with `N` elements as inputs. The proposed method will firstly apply a scheduling strategy to create a `mask` to select elements (spikes) in `S`, and use `S[mask]` as inputs. If so, it seems that this characteristic is trying to mimic the asynchronous spike firing in chips, which do not have a global clock. The role of the global clock is similar to "time-step" in SNNs simulated by the synchronous method. Then, what is the relation between the asynchronous spike firing in chips and the randomly selecting in simulation? I guess (note that I am not the expert of neuromorphic hardware) that the events (spikes) are processed (chronologically) orderly in chips, and this behavior is more similar to the synchronous simulation with a large number of time-steps. While the randomly selecting is disordered.

### Soundness
3

### Presentation
2

### Contribution
2
