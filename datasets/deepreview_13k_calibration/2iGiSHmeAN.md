# BroGNet: Momentum-Conserving Graph Neural Stochastic Differential Equation for Learning Brownian Dynamics

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 8, 6

## Abstract
Neural networks (NNs) that exploit strong inductive biases based on physical laws and symmetries have shown remarkable success in learning the dynamics of physical systems directly from their trajectory. However, these works focus only on the systems that follow deterministic dynamics, such as Newtonian or Hamiltonian. Here, we propose a framework, namely Brownian graph neural networks (BroGNet), combining stochastic differential equations (SDEs) and GNNs to learn Brownian dynamics directly from the trajectory. We modify the architecture of BroGNet to enforce linear momentum conservation of the system, which, in turn, provides superior performance on learning dynamics as revealed empirically. We demonstrate this approach on several systems, namely, linear spring, linear spring with binary particle types, and non-linear spring systems, all following Brownian dynamics at finite temperatures. We show that BroGNet significantly outperforms proposed baselines across all the benchmarked Brownian systems. In addition, we demonstrate zero-shot generalizability of BroGNet to simulate unseen system sizes that are two orders of magnitude larger and to different temperatures than those used during training. Finally, we show that BroGNet conserves the momentum of the system resulting in superior performance and data efficiency. Altogether, our study contributes to advancing the understanding of the intricate dynamics of Brownian motion and demonstrates the effectiveness of graph neural networks in modeling such complex systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce an innovative framework, Brownian graph neural networks (BROGNET), that integrates stochastic differential equations and GNNs to directly learn Brownian dynamics from trajectories. Their method enforces the conservation of linear momentum within the system, leading to empirically observed improved performance in learning dynamics. The authors showcase the effectiveness of BROGNET by applying it to various benchmarked Brownian systems. They also demonstrate its ability to generalize to simulate previously unseen system sizes and temperatures

### Strengths
The main idea of the paper is interesting. It is well-written and the proposed method seems to be novel.

### Weaknesses
Some parts are unclear and require further explanations. There are questions and vague points that need addressing:

1. How does the suggested framework manage noisy or incomplete trajectory data, and is it capable of accurately learning the underlying  dynamics in such cases?

2. How does the choice of activation function affect the performance of the MLPs? Were other activation functions considered, and if so, how did they compare to the chosen function?

3. Can the MLP be replaced with other types of neural networks, such as convolutional neural networks or recurrent neural networks? How would this affect the performance of the proposed framework?

4. Can you provide more details on the scalability of the proposed framework? How does the computational complexity scale with the number of particles, and how does this affect its applicability to large-scale systems?

5. How were the hyperparameters chosen, and how does the choice of hyperparameters affect the performance of the proposed framework?

6. How the choice of graph topology affects the performance of the proposed framework? Were other graph topologies considered, and if so, how did they compare to the chosen topology?

7. How does the proposed method handle systems with external fields or other sources of non-deterministic forces?

8. Can you provide more details on the benchmarked Brownian systems used to evaluate BROGNET's performance? How do these systems compare to real-world applications?

### Questions
Please see above!

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces BroGNet, a GNN that is momentum conservative designed based on SDEs for Brownian dynamics learning.
The authors provide a very thorough introduction and related work section to motivate the paper and to provide the reader with sufficient background. Then, the method is presented, followed by several experiments in different scenarios. The proposed method seems to significantly outperforms existing methods.

### Strengths
The paper is mostly easy to follow and read.

The authors provide a very good background section to explain different terms, such that even non expert readers can understand the paper.

The experimental section looks promising under various settings.

The authors provide good explanations about the baselines and the experiment details.

### Weaknesses
Missing literature about GNNs: while this paper is concerned with learning brownian dynamics from data, there is a complementary topic in GNNs and that is the design of GNN architectures inspired by ODEs. I believe that the authors should add a discussion to the related work section to clarify the difference between the two. Some references are provided in [1-5].

Missing literature about Neuro ODEs: please see [6,7].

It is not clear why the authors propose to use the square plus activation. Is there a specific reason? (besides the experimental result provided in the appendix)

Reading the appendix, I understand that the authors used only one message passing layer in their implementation. Can you please elaborate on this point? What would the performance be like when adding more layers?

Regarding the dynamic graph used here, how different is the proposed procedure than [8] ?

Regarding equation (8), this seems a bit like a discretized version of an advection operator (see [9,10]) for example. Can the authors expand on this point and clarify the differences?

### Questions
Regarding the dynamic graph used here, how different is the proposed procedure than [8] ?

Regarding equation (8), this seems a bit like a discretized version of an advection operator (see [9,10]) for example. Can the authors expand on this point and clarify the differences?

[8] Dynamic Graph CNN for Learning on Point Clouds

[9] ADR-GNN: Advection-Diffusion-Reaction Graph Neural Networks

[10] Advective Diffusion Transformers for Topological Generalization in Graph Learning

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed Brownian graph neural networks (BROGNET) which is a new framework combining stochastic differential equations and graph neural networks to learn Brownian motion dynamics directly from trajectories. The architecture ensures linear momentum conservation, leading to improved learning of dynamics. Several baselines were proposed for comparison due to the limited existing benchmarks. The BROGNET's distinctive momentum conservation feature made it significantly superior to all other baselines. It also demonstrated the ability to generalize to much larger system sizes and different temperatures than those seen during training.

### Strengths
1. I do like the design of predicting interacting forces rather than total forces on each node which naturally conserves total momentum conservation. Such “hard constraint” (or physics-based inductive biases in the paper) not only rigorously adheres to physical principles but also significantly enhances the model's performance, compared with more straight forward methods such as adding regularizers to penalize the physics violation. I suggest adding a few sentences in the first paragraph to explicit distinguish the “hard constraints” vs “soft constraints”.

There are a few additional papers in this trajectory worth mentioning. The natural constraint design in this paper is more less like ref [A], as the constraint is pure summation. While it can be generalized as special cases of Ref[B],[C],[D] as well.

[A] A machine learning-aided global diagnostic and comparative tool to assess effect of quarantine control in COVID-19 spread, Patterns, 2020.

[B] ConCerNet: A Contrastive Learning Based Framework for Automated Conservation Law Discovery and Trustworthy Dynamical System Prediction. ICML 2023.

[C] Learning Physical Models that Can Respect Conservation Laws. ICML 2023.

[D] Unravelling the performance of physics-informed graph neural networks for dynamical systems. NeurIPS, 2022. (this is already cited.)

2. The model can generalize to unfamiliar system sizes and temperatures with zero-shot learning.

3. The outperforms existing baselines in various tasks.

### Weaknesses
1.	My major concern lies on the comparison baselines. Firstly, the prior work baselines (BFGN, BNequIP) do not seem very strong to me. However, I’m not an expert in partical-based systems and I’m not expecting each accepted paper will include comparisons with all the popular models. More importantly, to show the benefits of the physics-informed inductive bias, it is worth comparing the other model with the same backbone structure + training with regularization on the physics violation. I appreciate the ablation study with BDGNN which essentially shares the same backbone model. But adding a comparison experiment by training BDGNN with regularizing on momentum conservation will better prove the power of inductive bias. Specifically, a comparison with a model that uses the same architecture as BROGNET but is trained with a loss function that includes a term penalizing deviations from momentum conservation would be highly beneficial. This would isolate the effect of the hard constraint and demonstrate its superiority over a soft constraint approach.

2.	Regarding the sde integrator, I’m a bit concerned about the gradient stability due to the stochastic integral. Did you meet any issues when the random distribution of noise term leading to large error during back-propagation? Or do you need some sampling method to get the approximation of the drift term along with the variance of the stochastic term?

### Questions
1.	Typos: 2nd line under equation 7: ativation 

2.	Is there any specific reason to use squareplus as activation function? I understand the comparison experiments with ReLU in appendix H which shows similar performance, but why squareplus is chosen at firsthand as it’s less popular?

3.	Equation 10 is questionable. \Delta \Omega should have the magnitude of \Delta t, but the following sentence mentioned “is a random number sampled from a standard Normal distribution”. Do you miss a magnitude of \Delta t?

4.	What does || || mean in equation 5,6?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
## Summary

The paper proposes a Graph Neural Network (GNN)-based method for simulating the over-damped limit of Langevin dynamics, which reduces to Brownian dynamics when no acceleration is present. Contributions include the use of additional MLPs for predicting random diffusion and decoding edge latent as interacting forces to enforce linear momentum conservation. However, the paper has several significant shortcomings, including a lack of motivation, limited benchmarking, and insufficient definition and references. Due to these issues, I recommend rejecting the paper.

## Detailed Comments

### 1. Lack of Motivation and Benefits

The paper does not provide adequate motivation for replacing traditional simulation techniques for the over-damped Langevin system with GNNs. Given that the dataset is generated from simulators that can easily model such systems, the authors need to justify the utility of their approach. This could be in the form of improved simulation speed or to-reality accuracy, although the latter would require validation beyond simulated data.

### 2. Lack of Definitions and References

- In Figure 1, the term "ohe(type)" is used without definition or context, making it unclear to the reader.
- The "squareplus" activation function is mentioned but not cited.

### 3. Limited Benchmarking

The paper restricts its experiments to simple spring systems, providing only a narrow validation of its methodology. Prior work in this domain typically includes experiments on 3-4 different datasets to establish the method's applicability.

## Conclusion

While the paper introduces a GNN-based method for simulating over-damped Langevin dynamics, it suffers from multiple critical flaws, including a lack of clear motivation, insufficient references, and limited benchmarking. These drawbacks severely compromise the paper's value and applicability. Therefore, I recommend rejecting this submission.

The authors should consider submitting to a workshop on this specific topic or, including more datasets to show the method's capability.

### Strengths
Small contributions like: decoding edge as force so linear momentum is conserved.

### Weaknesses
## Review

### summary:
 ## Summary

The paper proposes a Graph Neural Network (GNN)-based method for simulating the over-damped limit of Langevin dynamics, which reduces to Brownian dynamics when no acceleration is present. Contributions include the use of additional MLPs for predicting random diffusion and decoding edge latent as interacting forces to enforce linear momentum conservation. However, the paper has several significant shortcomings, including a lack of motivation, limited benchmarking, and insufficient definition and references. Due to these issues, I recommend rejecting the paper.

## Detailed Comments

### 1. Lack of Motivation and Benefits

The paper does not provide adequate motivation for replacing traditional simulation techniques for the over-damped Langevin system with GNNs. Given that the dataset is generated from simulators that can easily model such systems, the authors need to justify the utility of their approach. This could be in the form of improved simulation speed or to-reality accuracy, although the latter would require validation beyond simulated data. It is unclear why a neural network approach is needed when analytical and numerical solutions for Brownian motion are readily available and computationally inexpensive. The authors should clarify the specific problem they are trying to solve that cannot be addressed by existing methods.

### 2. Lack of Definitions and References

- In Figure 1, the term "ohe(type)" is used without definition or context, making it unclear to the reader. The term should be explicitly defined, as it is not universally known, and its purpose within the model should be explained.
- The "squareplus" activation function is mentioned but not cited. This is a relatively recent activation and requires a proper citation.

### 3. Limited Benchmarking

The paper restricts its experiments to simple spring systems, providing only a narrow validation of its methodology. Prior work in this domain typically includes experiments on 3-4 different datasets to establish the method's applicability. The use of only spring systems limits the generalizability of the approach. The authors should demonstrate the performance of their method on more complex systems with varying interaction potentials and particle densities to properly evaluate its effectiveness.

## Conclusion

While the paper introduces a GNN-based method for simulating over-damped Langevin dynamics, it suffers from multiple critical flaws, including a lack of clear motivation, insufficient references, and limited benchmarking. These drawbacks severely compromise the paper's value and applicability. Therefore, I recommend rejecting this submission.

The authors should consider submitting to a workshop on this specific topic or, including more datasets to show the method's capability.

### soundness:
 3 good

### presentation:
 3 good

### contribution:
 3 good

### strengths:
 Small contributions like: decoding edge as force so linear momentum is conserved.

### weaknesses:
 See above.

### questions:
 How hard is it to simulate Brownian motions? If not hard, w.r.t. simulation time or numerical or modeling challenges, there is no point in replacing it with NN?

If otherwise, please show the challenges in your draft.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 6: marginally above the acceptance threshold

### confidence:
 3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### code_of_conduct:
 Yes

### role:
 Review

### Questions
How hard is it to simulate Brownian motions? If not hard, w.r.t. simulation time or numerical or modeling challenges, there is no point in replacing it with NN?

If otherwise, please show the challenges in your draft.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
