# Grokking Tickets: Lottery Tickets Accelerate Grokking

- Decision: Reject
- Scores: 6, 6, 3, 3, 3

## Abstract
Grokking is one of the most surprising puzzles in neural network generalization: a network first reaches a memorization solution with perfect training accuracy but poor generalization, but with further training, it reaches a perfectly generalizable solution. 
We aim to analyze the mechanism of grokking from the lottery ticket hypothesis, identifying the process to find the lottery tickets (good sparse subnetworks) as the key to describing the transitional phase between memorization and generalization. 
Firstly, with the lottery tickets identified via the magnitude pruning after perfect generalization, we show that the lottery tickets drastically accelerate grokking compared to the dense networks on various configurations (MLP and Transformer, and an arithmetic and image classification task). 
We also show that the speedup is significant even when compared with the dense networks with the same weight norm as the lottery tickets. 
Besides, the speedup only happens when training ``good'' subnetworks are identified at the generalization solution. Specifically, speedup does not happen when using tickets identified at the memorization solution or transition between memorization and generalization or when pruning networks at the initialization (Random pruning, Grasp, SNIP, and Synflow). 
The results indicate that the weights norm of network parameters is not enough to explain the process of grokking, but the importance of finding good subnetworks to describe the transition from memorization to generalization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work provided a new perspective for analyzing the grokking phenomenon, that is the lottery ticket hypothesis.

The authors first showed an interesting observation they made. They trained a neural network to the grokking stage and then performed one-shot pruning. They called the subnetwork obtained as “grokking ticket”. The authors observed that the grokking ticket can significantly shorten the training epochs needed to achieve the grokking stage, compared to the dense network.

Furthermore, the authors conducted a series of ablation experiments to deconstruct the effects brought by the grokking tickets, including:
* Pruning stage: tickets obtained before the grokking stage won’t accelerate the occurrence of the grokking stage.
* Weight norms: as the grokking phenomenon has been connected to the weight norms in the literature, the authors also compared the grokking tickets with dense networks whose weights are scaled to have similar norms. The results showed no acceleration through weight scaling.
* Weight decay: the authors showed with numerical results that the grokking tickets at appropriate pruning ratios can waive the necessity of weight decay, which has been assumed necessary for grokking to happen.

### Strengths
+ This work provided a new brandnew perspective for investigating and understanding the grokking phenomenon, that is the sparse network structure. The authors made interesting observations on the acceleration of grokking brought by pruning, which connects the seemingly disjoint topics.

+ The authors provided results of well-designed experiments that decoupled grokking tickets and weight norms (thus weight decaying), which have been assumed to be the key of grokking, throwing light on a higher level of property that grokking could possess.

+ Moreover, this work also provided a perspective of using grokking phenomenon to understand pruning and specifically lottery tickets. Many previous studies have shown that SNIP, GraSP and SynFlow achieved similar accuracies on classification tasks but Fig. 7 in this work showed very different behaviors with these methods.

### Weaknesses
- While this work made a lot of interesting observations, profound analysis and investigation behind empirical results are lacking.

- The writing quality of this work is not satisfactory.

### Questions
n/a

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the grokking phenomenon in neural networks through the lens of the lottery ticket hypothesis, positing that identifying optimal sparse subnetworks ("lottery tickets") is crucial for the transition from memorization to generalization. The authors present experiments using MLP and Transformer architectures on tasks like modular addition and MNIST classification to demonstrate that these identified subnetworks can significantly accelerate grokking.

### Strengths
**Novel Approach:** The paper introduces a novel concept of "grokking tickets" within the context of the lottery ticket hypothesis, which is an original contribution to the understanding of neural network learning dynamics.

**Experimental Evidence:** Initial experimental results indicate that the identified subnetworks do indeed accelerate the grokking process, which could have implications for the efficiency of training neural networks.

**Clarity of Presentation:** The paper is well-structured and presents its methodology and findings clearly, making a case for the importance of subnetwork identification in neural network training.

### Weaknesses
**Theoretical Underpinning:** The paper lacks a comprehensive theoretical framework that explains why and how grokking tickets work, leaving the reader to infer the underlying principles from empirical observations.

**Limited Experimental Scope:** The experiments are confined to a narrow set of tasks and architectures, which might not fully demonstrate the generalizability of the proposed method.

**Lack of In-Depth Analysis:** The paper does not provide an in-depth analysis of the scalability of the approach or a comparison with other state-of-the-art methods across varied settings.

**Comment on References:** While the paper presents a novel approach to understanding the grokking phenomenon in neural networks, the reference list does not appear to be fully comprehensive. It would strengthen the paper to include a broader range of sources that contextualize the work within the larger body of research on neural network pruning, generalization, and learning dynamics.

### Questions
1. Can the authors elaborate on the theoretical foundations that might explain the observed acceleration in learning due to grokking tickets?

2. Would the authors consider expanding their experimental evaluation to include a wider variety of tasks and network architectures to confirm the robustness of their findings?

3. How do the authors envision the scalability of the proposed method, and how does it compare with other pruning or training acceleration techniques in terms of computational efficiency and performance?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the effect of lottery tickets in the context of Grokking and finds that the Grokking tickets obtained during the generalization phase can accelerate the speed of the model to reach the generalization phase. The found that the speedup only happens when subnetworks are identified at the generalization solution. Whereas, there is no speed up when we try to identify subnetworks at initialization, or at the memorization solution or the transition between memorization  and generalization. In general, this is an interesting combination of LTH and Grokking but with some mediocre observations.

### Strengths
1. This paper explores the role of LTH in Grokking and make a good combination of LTH and Grokking. 

2. The finding that only subnetworks discovered during the generalization phase can speedup the generalization process is reasonable, aligning with previous findings of LTHs. 

3. Figure 1 clearly demonstrates the main message delivered by this paper. 

4. They also demonstrate that it is possible to induce grokking without weight decay when using the grokking tickets.

### Weaknesses
1. My major concern is that while the combination of LTH with Grokking is new to the community, the empirical findings shown in this paper is somehow mediocre. For instance, i. it is not surprising to see that the subnetworks obtained during the generalization phase is crucial for grokking speedup.  ii. The lottery tickets learn faster than the original dense model has already been demonstrated in the original LTH paper and many other previous works. iii. The definition of the Grokking Tickets has no essential difference than the original Lottery Tickets and can be covered by the original ones since the original LTH does train the dense model to the end. 

2.  Perhaps, the authors can emphasize the contribution of the papers from the perspective of Grokking. Why the grokking tickets are important for Grokking?

3. Besides the speedup, does Grokking tickets bring any performance benefits over the dense one?

### Questions
Please refer to the above weaknesses.

### Soundness
3 good

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
The paper analyzes a phenomenon called ``Grokking'' by using the ``Lottery Ticket Hypothesis'' as a tool to uncover the reasons for Grokking. Grokking here refers to delayed generalization, i.e., test accuracy grows to its peak value long after the network has fit the training. The hypothesis examined here is that neural network training results in a sparse network. Sparsity may then be used to explain the reason behind delayed generalization. The paper conducts an empirical analysis with modular addition using a small Transformer  and briefly studies an MLP with large initialization as suggested by Liu et. al.  Ablations are conducted that show that the grokked solution checkpoint generalizes faster than checkpoints collected at earlier points during optimization.

### Strengths
- The paper uses the lens of sparsity to study Grokking. This is a promising avenue of exploration
- The empirical analysis for modular addition asks and then attempts to answer very sensible and relevant questions. 
  - The choice of checkpoints suggest that useful sparsity occurs later on in optimization (close to or after solution is grokked)
  - Ablations with fixed norm and fixed sparsity are useful to readers interested in Grokking
  - The choice of pruning appears to make a difference. Checkpoints after generalization perform better than other algorithms used in pruning literature

### Weaknesses
- The paper attempts to make a connection to the Lottery Ticket Hypothesi (LTH). Sparsity is a reasonable hypothesis that has been explored by Merrill et. al. previously in literature. However, I am not convinced that connecting LTH to this work is necessary. Merrill 2023 make observations about sparse networks without invoking LTH
- Nanda et. al. (Nanda 2023) show that the network after generalization consists of a few sinusoids, i.e., finds a sparse solution. So sparsity being an explanation has been shown in prior literature. Also suggest that the authors consult Gromov 2023 for the solution found a 

- The paper notes in Section 5.1( ablation of weight norms) that a subnetwork has increased weight norm after a generalizing solution is found by gradient descent while other weights end up with smaller norms. This is the same observation made in Merrill 2023 where the authors study subset parity learning problem
- The observation that the sparse generalized solution optimizes faster than the dense network while interesting is not critical to understanding Grokking. It is known that regularization or lowering capacity of models via regularization does help shorten the time between fitting and generalization in algorithmic datasets. This observation falls in-line with the above
- Given the empirical nature of the paper, the number of datasets considered in the analysis appear to be inadequate. Power 2022 construct various algorithmic datasets. Gromov 2023 use a MSE solution with MLP for addition. Have the observations been confirmed in more settings than the ones considered in the paper? 

- [Gromov 2023]  Grokking modular arithmetic
- [Meriill 2023] William Merrill, Nikolaos Tsilivis, and Aman Shukla. A tale of two circuits: Grokking as competi- tion of sparse and dense subnetworks, 2023.
- [Nanda 2023] Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, and Jacob Steinhardt. Progress measures for grokking via mechanistic interpretability, 2023.
- [Power 2022] Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin, and Vedant Misra. Grokking: Gener- alization beyond overfitting on small algorithmic datasets, 2022.

### Questions
**Major Issues**

- Please see weakness section
- Using sparsity as an explanation for Grokking has been done before in other papers. How is the analyses presented in the paper adding to existing literature? Without a clear answer, the novelty of the work in the paper is insufficient for me to vote for acceptance at the conference.

**Minor Issues**

- Introduction
  -  Power et. al, observed Grokking in many algorithmic datasets including modular addition. 
  -  Barak et. al. [2] demonstrated Grokking on subset parity dataset before Merrill et al.
  -  ``accelerate'' the grokking process may be confusing to readers outside the area of Grokking. Perhaps emphasize that the time to generalization is shorter?

- Page 7
  - leaders should be readers

[2] https://openreview.net/forum?id=8XWP2ewX-im

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper have conducted a set of experiments that demonstrate the effectiveness of grokking tickets in accelerating the generalization process. The results of the study suggest that the transition phase between memorized and generalized solutions corresponds to the exploration of good subnetworks, or lottery tickets.

### Strengths
1. The paper delves into the connection between grokking and LTH, demonstrating the grokking tickets hold good properties beyond just a sparsity.

2. Experimental results validate their findings.

### Weaknesses
1. The writing needs improving, and at times, I find it hard to follow the text. For instance, the term "grokking tickets" is used 12 times before its formal definition presented, which presents a certain impediment to readers.

2. I am uncertain about the practical significance of the findings. Specifically, I understand that one of the conclusions is that tickets found during the $C_{mem}$ phase exhibit better performance. However, this seems to align with the common practice in LTH research~\cite{chen2021unified, gan2022playing}, where networks are thoroughly trained and then pruned based on optimal validation scores during each pruning iteration. Therefore, the question arises as to what contribution the findings in the paper make to the discovery of improved lottery tickets.

3. The experimental results in Section 5.2 appear to support the author's claims that poor selection of subnetworks harms generalization. However, as mentioned in 2, the grokking tickets results seem to represent the outcomes of LTH approaches. It appears that the author has primarily validated that LTH with IMP can outperform most PaI methods. 

4. While the existing results do indeed support the author's assertions, the use of overly simplistic tasks (modular addition and MNIST classification), basic baselines (MLP and single-head Transformer), and a lack of additional experimental configurations (such as performance under multi-layer MLPs or multi-head attention) leave me with reservations regarding the validity of the conclusions.

### Questions
1. The paper could be better organized. To name a few, in 2.1 ‘abuse’ -> ‘abuse of’; in 5.1 ‘leaders’->’readers’. Excessive space is devoted to some trivial aspects, such as formulas for weight initialization.

2. It is advisable to include additional backbones and experimental setups to comprehensively validate the claims.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
