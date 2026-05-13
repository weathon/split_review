# Scalable Long Range Propagation on Continuous-Time Dynamic Graphs

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Learning Continuous-Time Dynamic Graphs (C-TDGs) requires accurately modeling spatio-temporal information on streams of irregularly sampled events.
While many methods have been proposed recently, we find that most message passing-, recurrent- or self-attention-based methods perform poorly on \textit{long-range} tasks. 
These tasks require correlating information that occurred ``far'' away from the current event, either spatially (higher-order node information) or along the time dimension (events occurred in the past).
To address long-range dependencies, we introduce \fulladgn (CTAN).
Grounded within the ordinary differential equations framework, our method is designed for efficient propagation of information.
In this paper, we show how CTAN's (i) long-range modeling capabilities are substantiated by theoretical findings and how  (ii) its empirical performance on synthetic long-range benchmarks %is vastly superior to other methods, while maintaining improved or competitive results on real-world benchmarks.
and real-world benchmarks is superior to other methods.
Our results motivate CTAN's ability to propagate  long-range information in C-TDGs as well as the inclusion of long-range tasks as part of temporal graph models evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposed a graph learning framework for continuous time dynamic graph learning, which utilize ANTI-SYMMETRIC DGN[1] to help CTDG method capture long-range information, by better model the evolution of the node memory. A special designed long range memorize task shows the effectiveness of the proposed method.

[1] https://arxiv.org/abs/2210.09789

### Strengths
1. This paper porosed CTAN, which is a new deep graph network for learning C-TDGs based on ODEs. 
2. This paper presented novel benchmark datasets specifically designed to assess the ability of DGNs to propagate information over long spatio-temporal distances within C-TDGs

### Weaknesses
1.	The model is an extension from existing model A-DGN to continuous dynamic graph, though the paper claims that it is the first ODE-based architecture suitable for C-TDGs, most of the original ideas are same as the previous work, and the paper fails to contribute more on the method, which makes the novelty of the paper limited.
2.	The paper's baseline models are "too old and uncompetitive", for example, there are several sequence based CTDG methods, for example, Graphmixer[1] and DyGFormer[2], that can capture long range dependency, the paper should consider compare with more up-to-date baselines to show the effectiveness.
3.	The experiment in Table 2 can not support the claim that the model can capture long-term information well, for example, the performance of LastFM with Edgebank increases by the sequence length growth, and the proposed method fails to outperform edgebank.
4.	The test setting on benchmark dataset is different to most existing methods, the paper only contains transductive setting, and neglects the inductive setting, the negative sample strategie is also different, makes me hard to compare the performance of proposed method with existing methods.

### Questions
1.	What is the difference between the proposed method and the existing method A-DGN? Does dynamic graph learning task contain more strength of using such method?
2.	As a memory based model, how can CTAN treat with inductive setting(cold start problem)?

3. Can ODE-based encoder outperform other sequence learning encoder, when comparing with sequence-based CTDG methods like DyGFormer?
4.	Since there are three negative sample strategie mentioned in Edgebank, why does the method only compare with baseline models on random negative sample?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a deep graph network called CTAN on continuous-time dynamic graphs. The CTAN model is designed within the ordinary differential equations framework that enables efficient propagation of long-range dependencies. The paper shows that the CTAN model can robustly perform stable and non-dissipative information propagation over dynamic evolving graphs. The number of ODE discretization steps allows scaling the propagation range. The paper further presents empirical results to demonstrate the effectiveness of the CTAN model.

### Strengths
S1. The paper is well-motivated by the need for scalable GNN models capable of capturing long-range dependencies in continuous-time dynamic graphs.

S2. The paper provides theoretical proof of the effectiveness of the proposed model.

S3. The paper empirically validates the proposed model on many graph benchmarks. The experimental results illustrate the superiority of the proposed model. 

S4. The paper is generally well-written and easy to follow.

### Weaknesses
W1. The benchmark datasets are all of moderate size. Validating the model's performance on larger, dynamic datasets would be beneficial.

W2. None of the C-TDG benchmarks include negative instances. The authors introduce negative sampling to the benchmark datasets by randomly sampling non-occurring links in the graph. However, the distributions of negative sampling can differ significantly from uniform distributions in real-world applications. Demonstrating the performance of the proposed model in handling negative instances across various distributions would be advantageous.

W3. Some important baselines are omitted in the experiments. For example:
- CAW: Inductive representation learning in temporal networks via causal anonymous walks. ICLR 2021
- NAT: Neighborhood-aware scalable temporal network representation learning. LoG 2022.

### Questions
Please refer to the Weaknesses part for details.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new deep learning framework called Continuous-Time Graph Anti-Symmetric Network (CTAN) to address the problem of long-range propagation in continuous-time dynamic graphs (C-TDGs). The authors propose a theoretically motivated ODE-based framework to enable effective long-range propagation in dynamic graph learning. The paper also experimentally evaluates the proposed solutions on both synthesized and real-world networks.

### Strengths
S1. Modeling long-range dependencies is an important problem in dynamic graph learning.

S2. The paper provides a theoretical analysis of how the anti-symmetric weight matrices ensure stability and non-dissipativeness of the ODE for long-range propagation.

S3. The paper is generally well-written and easy to follow.

### Weaknesses
W1. The idea of using ordinary differential equations (ODEs) to model dynamic graphs is not novel.

W2. The authors design the sequence classification on temporal path graphs to validate the algorithm. However, I have reservations about the rationale of basing the prediction of the initial node's features solely on the last node in the sequence. Such a design indeed increases the difficulty of the task, as it requires the model to effectively propagate long-distance dependencies. However, from a practical standpoint, it may not be quite reasonable, as it completely ignores the intermediate information. Moreover, a binary classification task with only two types of features is too simple.

W3. More baselines should be included in the experiments. For example, [1-3].

### Questions
See W1-W3 for details.

Minor Comment

The authors claim to present a scalable method for propagating long-range dependencies in the title and introduction, but do not follow through with this assertion in the subsequent discussion. This might give the reader the impression that the author has not fully delivered on the promise of the title in the text. I would suggest the authors elucidate the method's scalability in the methodological discussion section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents Continuous-Time Graph Anti-Symmetric Network as a new graph neural network for Continuous-Time Dynamic Graphs. The authors build upon ideas presented in the literature that oversmoothing can be avoided if the eigenvalues of the dynamics are chosen carefully -- thereby facilitating long-range information transfer.

### Strengths
The paper is well written, and clearly articulates an important problem for GNNs as well as a potential solution.
The proposed solution is not entirely new, but appears to be well implemented.

### Weaknesses
 - While the benefits of having a non-dissipative dynamics is discussed, the disadvantages are not discussed very prominently. If all modes are essentially undampended there is also no filtering of noise -- the tradeoffs here should be discussed. Even better would be an experiment that considers the robustness of these ideas when faced with (adversial or even just random) noise.
- Relating to the previous point, the authors actually have added a dissipative term (-yI) when discretizing their dynamics via an Euler discretization -- I think they should discuss the importance of this term.
- Proposition 1 is essentially standard linear algebra; calling this a proposition and adding a formal proof seems to be somewhat disproportionate to what this does -- I suggest the author can simply discuss this.
- The temporal aspects of the data are almost never used; the authors simply use a "temporal" interpretation -- this raises some questions:
a) why not compare with other (non-temporal) architectures as baselines that can deal with this kind of data?
b) what benefits does the architecture really bring to temporal graphs? It appears to me that the contribution provided here is in some sense orthogonal to the fact that temporal graphs are considered as data?! Please discuss these aspects further.

### Questions
See above. 

In particular, I would encourage the authors to more clearly articulate the trade-offs that come with imaginary eigenvalues (e.g., while no energy is dissipated but oscillations can arise) and how they address this trade-off.
Moreover, it seems that the temporal aspects of the data is actually not really central to the exposition at hand -- in what parts does this play a strong role? This should be discussed more.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
