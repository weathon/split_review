# PTaRL: Prototype-based Tabular Representation Learning via Space Calibration

- Decision: Accept
- Scores: 8, 8, 8

## Abstract
Tabular data have been playing a mostly important role in diverse real-world fields, such as healthcare, engineering, finance, etc.
With the recent success of deep learning, many tabular machine learning (ML) methods based on deep networks (e.g., Transformer, ResNet) have achieved competitive performance on tabular benchmarks. However, existing deep tabular ML methods suffer from the \textit{representation entanglement} and \textit{localization}, which largely hinders their prediction performance and leads to  \textit{performance inconsistency} on tabular tasks.
To overcome these problems, we explore a novel direction of \textit{applying prototype learning for tabular ML} and propose a prototype-based tabular representation learning framework, \textsc{PTaRL}, for tabular prediction tasks. The core idea of \textsc{PTaRL} is to construct prototype-based projection space (P-Space) and learn the disentangled representation around global data prototypes. Specifically, \textsc{PTaRL} mainly involves two stages: (i) Prototype Generation, that constructs global prototypes as the basis vectors of P-Space for representation, and (ii) Prototype Projection, that projects the data samples into P-Space and keeps the core global data information via Optimal Transport. Then, to further acquire the disentangled representations, we constrain \textsc{PTaRL} with two strategies: (i) to diversify the coordinates towards global prototypes of different representations within P-Space, we bring up a diversification constraint for representation calibration; (ii) to avoid prototype entanglement in P-Space, we introduce a matrix orthogonalization constraint to ensure the independence of global prototypes. 
Finally, we conduct extensive experiments in \textsc{PTaRL} coupled with state-of-the-art deep tabular ML models on various tabular benchmarks and the results have shown our consistent superiority.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces several techniques to improve the performance of neural networks on tabular data. The study demonstrates that deep tabular models often face issues related to representation entanglement and the loss of global structure. To address these challenges, the paper proposes the construction of a prototype-based projection space with two carefully designed constraints aimed at decoupling the projected representations.

### Strengths
- The suggested representation learning pipeline can be integrated into various deep tabular models.
- Figure 1 clearly illustrates that the phenomenon of representation entanglement has not been mitigated as the model capacity is gradually increased.
- The primary concept for enhancing representation involves using weighted prototypes to approximate the original mapped features. This idea is indeed intriguing.

### Weaknesses
- The illustration (Fig. 2) does not clearly depict the overall pipeline; it still remains unclear.
- More details of the optimization process could be provided.

### Questions
1. How is equation (4) optimized? Compared to the traditional OT problem, it includes \theta_f as a variable to be optimized.
2. Could you provide more technique details about the workflow of the PTARL algorithm (Algorithm 1)?
3. The illustration (Fig. 2) could benefit from improvement as it currently lacks clarity in depicting the overall pipeline. For instance, there are two blocks labeled "Hidden Representation"; could you clarify the distinction between them? Additionally, the three sentences on the right side of the figure require further explanation for better understanding.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The existing deep tabular ML models suffer from the representation entanglement and localization. To address this, the authors explore a novel direction of applying prototype learning  framework. The proposed framework involves to construct prototype-based projection space and learn the disentangles representation around global data prototypes.

The proposed method contains two stages: prototype generating and prototype projecting. The former is to constructs global prototypes as the basis vectors of projection space for representation, and the latter is to project the data samples into projection space and keeps the core global data information via optimal transport. The authors show the efficiency of the proposed method with various benchmarks.

### Strengths
The proposed approach is novel and the experimental results are impressive.

### Weaknesses
It would be great if the authors apply the proposed method to recent deep models for tabular representation, such as SAINT [1].

[1] Saint: Improved neural networks for tabular data via row attention and contrastive pre-training, NeurIPS workshop 2022

### Questions
I wonder if the authors believe that the proposed method can be applied to generative models.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents PTaRL, a model-agnostic method to enhance deep-learning methods for tabular data prediction. The method inserts a sound prototype learning step after the penultimate layer of any DNN to alleviate the issue of representation entanglement and localization. The results show improvement across several architectures and datasets.

### Strengths
- The problems identified (representation entanglement and localization) and the results (including the ablation study) are convincing.
- The various steps — the joint optimization of DNN representation, prototypes, and projection coordinate plus the two constraints — are intuitive. 
- The paper reads smoothly.

### Weaknesses
- The concepts of “global data structure information” and “sample location” are not very clear, at least not as concretely demonstrated as entanglement and orthogonality.

### Questions
The whole purpose of using the prototype seems to be for capturing “global data structure information” so as to avoid “sample localization”. However, after reading Section 4, I am still unclear what “global data structure information” really is. Could the authors provide a more explicit definition and description of it? Similarly for “sample location.”

I feel Figure 4 is a much better example of disentanglement than Figure 1, because I still see substantial overlap in the bottom row of Figure 1.

I don’t quite understand how Figure 5 shows diversification.

I was wondering where the boosted performance sits in the literature as a whole. The paper shows DNN and DNN + PTaRL. Do these now match the performance of XGBoost and other state-of-the-art tree-based methods? How much better are they compared to older methods, such as kernel prototype classification and regression? Is it possible to apply PTaRL on different DNN depths to show the contribution of deep-learning representation vs the contribution of the prototype representation? I think knowing the answer to the first question (related to XGBoost) will be very useful. I can understand if the authors feel the other questions are more distracting than useful, since the paper has a focus on enhancing deep-learning approaches.

Overall, the paper is quite well rounded. The problems, solutions, implementations, and results all work together well.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
