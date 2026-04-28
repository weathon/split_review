# Resonator-Gated RNNs

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Sequence learning tasks frequently involve data with repetitive and periodic temporal patterns. Detecting these patterns is essential for accurate predictions and informed decision-making in various domains. There is, however, still huge potential in augmenting sequence learning algorithms in this regard. In RNN-based sequence learning, gated RNNs, such as long short-term memory networks (LSTMs)
and gated recurrent units (GRUs), are the de facto standard. While adept at capturing longer-term dependencies, gated RNNs still sometimes struggle with periodic data components, because their gating mechanism is designed to prioritize retaining static relevant information. As a result, these networks often challenged by periodicity in the data. We present a novel memory unit that incorporates a simple resonator circuit. The resonator facilitates the recognition of periodic data patterns, focusing on data-specific time scales and respective frequencies. Moreover, it enables the forward propagation of information through resonating dynamics while stably channeling the gradient backwards. We show that our resonator-gated RNN (RG-RNN) accelerates the training convergence on multiple sequence classifications tasks. Moreover, it significantly outperforms vanilla LSTMs on three out of four benchmark tasks in terms of accuracy. We conclude that resonator-based gating offers a new inductive bias to gated RNNs, focusing learning on the detection and processing of periodic data patterns.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to modify the LSTM architecture with a `resonator-gate` with the aim of improving the detection of periodic components of an input sequence. The resonator is defined based on the discrete time version of a `resonate-and-fire` neuron model and is of similar computational cost as the existing LSTM gates. The authors evaluate the performance of RG-RNN against LSTMs on four time-series dataset and demonstrate greatly improved training stability, convergence behavior and performance in almost all cases.

### Strengths
- Improving existing architectures for sequence prediction is important problem. As the authors note, LSTMs and GRUs have been the de facto standards for quite some time and an improvement in training performance will be greatly benificial. 
- The paper is overall well written and easy to follow. 
- Idea is simple, intuitive and easy to implement and test. 
- Experimental results on the 4 datasets are impressive, showing much-faster convergence and stability  in training (Figure 3) and improved performance (Table 1).

### Weaknesses
While experimental section overall is sound and (seemingly) reproducible, it can be greatly improved with experiments on time-series data from other data domains (ex. sensor data, from UCI Data-repo). Given the simplicity of the proposed method (both conceptual and in implementation) and the popularity of LSTM/GRU cells, an larger evaluation demonstrating stability/convergence behavior will be greatly strengthen the paper. The current evaluation, while promising, is limited to only four datasets, which may not be fully representative of the diverse range of time-series problems where LSTMs are typically applied. Furthermore, the paper does not explore the sensitivity of the RG-RNN to hyperparameter choices, which could impact the generalizability of the results. A more thorough analysis of the impact of different resonator parameters, such as the time constant, would be beneficial.

### Questions
- While Figure~1 demonstrates how the discrete time resonator dynamics behaves, it would be interesting to see this also as part of the LSTM architecture. For example, working with a  1D synthetic sequence prediction task (say on some periodic signal), is the difference in performance between an LSTM and RG-LSTM evident? 
- Can the modified gating mechanism be applied to GRU as well? How does the performance compare? 
-  'prioritize retaining static relevant information': Could you elaborate on `static relevant information`?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article addresses the challenge of RNNs in handling periodic data. To overcome this, the authors introduce the resonate-and-fire neuron and propose the Resonator-Gated RNN (RG-RNN), which outperforms LSTM on multiple periodic datasets.

### Strengths
1. The article is well-written and easy to understand. 
2. The method proposed is simple yet effective.

### Weaknesses
My main concern about this article is whether the comparison is comprehensive enough. For example, there have been new types of RNNs such as S4, S5, and LRU, so it would be interesting to compare the performance of these methods. Additionally, introducing the Transformer as a baseline can also help readers better understand the strengths and weaknesses of each model on periodic datasets.

### Questions
Add S4, S5, LRU and transformer as baseline.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper "RESONATOR-GATED RNNS" proposes to add two discretized resonating differential equations to the LSTM gate equations. The resulting RG-LSTM is compared to an LSTM baseline on the sequential MNIST,
permuted sequential MNIST, speech Commands VS and the OTDB dataset of physiological signal recordings.

### Strengths
- Cell convergence results appear to be competitive.
- The experimental evaluation features mean values and standard deviations over multiple runs.

### Weaknesses
 - Recurrent networks used to be the go to choice for sequence modelling. In the deep learning book (https://www.deeplearningbook.org/), chater 10 bears the title "10 Sequence Modeling: Recurrent and Recursive Nets" Consequently, the paper calls RNNs the go to standard for sequence modelling. However a lot has happend since 2016. Attention based systems like transformers have since emerged as a popular alternative to RNNs for sequence modelling tasks, unfortunately this development is not discussed in the related work. In the vision domain Trainsformers are known to struggle on small data-sets (https://proceedings.neurips.cc/paper/2021/file/c81e155d85dae5430a8cee6f2242e82c-Paper.pdf). Perhaps the same is true for sequential data? This could be possible way to extend the related work without having to run additional experiments.

### Questions
- What does the OTDB acronym mean?
- Which seed values have been used? Without the seeds, it won't be possible to reproduce the paper's experimental results exactly.
- What are the trainable parameters for the LSTM and RG-LSTM cells for each experiment?
  Was the cell state size identical in both cases? Does this mean that the RG-LSTM cell has more trainable parameters?
- Some authors suspect extra weights improve convergence (https://arxiv.org/abs/1803.03635 ).
- If the number of trainable weights was not the same, is the comparison fair?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Gated RNNs fail to learn periodic functions efficiently. To address this limitation, the authors augment the LSTM architecture with a module leveraging the subthreshold dynamics of resonate-and-fire neurons. They show that this mechanism is sensitive to periodic inputs and that it improves the performance of the base architecture on a few datasets.

### Strengths
The introduction of the method is clear and using resonate-and-fire neurons to improve performance on periodic data is a cute idea.

### Weaknesses
Overall, the main weakness of the paper is that it does not really test its claims thoroughly. For example, one claim is that the improved performance is due to the ability to capture periodic dependencies. From the experiments described, it is impossible to understand if this is true or if the improved performance comes from additional parameters. The authors claim that the number of parameters is not the main driver of the performance increase, but this is not sufficiently supported by the experiments. The paper lacks a proper ablation study that would isolate the effect of the resonate-and-fire module. For instance, it is not clear if a randomly initialized resonate-and-fire module would yield similar performance gains. Furthermore, the paper does not explore the sensitivity of the method to the parameters of the resonate-and-fire neurons, such as the time constant or the firing threshold. It is also not clear how the method performs on datasets with different types of periodicities, or with multiple periodicities at once.

### Questions
How does your work relate to recent literature on linear diagonal state-space models (for example Orvieto et al 2023, Resurrecting recurrent neural networks for long sequences, and references mentioned in the paper)? To me, those results suggest that resonate-and-fire type of mechanisms greatly simplify gradient-based learning in general, and not the learning of periodic functions specifically.

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
