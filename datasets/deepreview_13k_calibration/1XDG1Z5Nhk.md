# Sparse Backpropagation for MoE Training

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
One defining characteristic of Mixture-of-Expert (MoE) models is their capacity for conducting sparse computation via expert routing, leading to remarkable scalability.
However, backpropagation, the cornerstone of deep learning, requires dense computation, thereby posting challenges in MoE gradient computations.
Here, we introduce SparseMixer, a scalable gradient estimator that bridges the gap between backpropagation and sparse expert routing. 
Unlike typical MoE training which strategically neglects certain gradient terms for the sake of sparse computation and scalability, SparseMixer provides scalable gradient approximations for these terms, enabling reliable gradient estimation in MoE training. 
Grounded in a numerical ODE framework, SparseMixer harnesses the mid-point method, a second-order ODE solver, to deliver precise gradient approximations with negligible computational overhead.}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper attempts to address the backpropagation issue of Mixture of Experts (MoE). There is a growing interest in sparsely activated networks, specifically Mixture-of-Experts (MoE), which selectively activate parts of modules for specific inputs, leading to efficiency improvements. However, gradient estimation in MoE is challenging due to the non-differentiable nature of expert routing. Existing methods like Straight-Through (ST) estimators are not compatible with MoE, which leads to the neglect of gradient computation for routing during training, impacting convergence and model quality. The paper introduces SparseMixer, a novel approach that reconciles sparse MoE routing and backpropagation using numerical methods for ordinary differential equations. SparseMixer provides reliable gradient approximations even with a subset of experts activated and accelerates training convergence by up to two times. It also enables MoE models to consistently outperform dense models when used with Switch Transformer.

### Strengths
(1) This paper discusses an very important research question in MoE, the backpropoagation issue of routing function, which is easily be overlooked by researchers if not be pointed out specifically. This research question is timely and important. 

(2)  The first order approximation used in this paper only requires the output of one expert, not sacrificing scalability.

(3) SparseMixer does not require hessian or other second-order derivatives, having negligible computation overheads.

### Weaknesses
 (1) While SparseMixer achieves consistently improvement over the vanilla Switch Transformer, what I can see is the improvement is a bit marginal in Table1. Esp. as the number of experts increases, the performance gains become more marginal. My conjecture is that the main evaluation task in the paper, GLUE, is two simple to demonstrate the empirical benefits of SparseMixer. I would like to see more results on more challenging tasks, where the performance gains of S+S might be larger. 

(2) The marginal performance improvement is also contradictory to the authors' motivation. If the neglect of the gradient computation for
routing is indeed crucial for MoE, we should see much significant improvements. 

(3) What is the cost induced by SparseMixer? Table 3 does not provide enough information to justify the overheads. Can we see any time difference as the number of experts continues to increase?

### Questions
Please see the above Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents SparseMixer, a scalable gradient estimator that bridges the gap between backpropagation and sparse expert routing.  In specific, the paper presents SparseMixer to provide scalable gradient approximations for the gradients terms that are not taken into account, enabling reliable gradient estimation in MoE training. The authors demonstrate SparseMixer to Switch Transformer on both pre-training and machine translation tasks, with the claim of considerable performance gain, accelerating training convergence by up to 2 times.

### Strengths
1. The idea of improving gradient computation at scale to improve MoE training is novel to me.

2.The paper consistently demonstrate the impact of neglecting $\Delta_0$ in the pre-training with MoE.

3. The paper is written well and the results back up the improvement.

### Weaknesses
1. Straight-Through (ST) -- > straight through estimator (STE) ? 

2. Please define ODE first in the abstract before using the abbr.

3. Please introduce definitions of $\Delta_0$ and $\Delta_1$.

4. It is not quite clear why the training speed improves.

5. Please demonstrate results with other MoE gating methods. as few of them tried to improve MoE training.

### Questions
Please see weakness.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes SparseMixer to move beyond discrete and bridge the gap between sparse MoE routing and backpropagation. SparseMixer utilizes a second-order ODE solver to deliver precise gradient approximations. Their experiments show SparseMixer not only accelerates training convergence by up to two times but also facilitates MoE with properly trained expert routing.

### Strengths
1. The pre-training of LLMs is costly, and MoE is one promising sparse training method to reduce the training overhead. The paper makes some contributions to improving the backpropagation of MoE Training.

2. The experiment results show the effectiveness of the proposed methods on a specific model.

### Weaknesses
My concern includes two aspects:

1.  The experiment is kind of weak since there are also some other MoE architecture and other base models, while the authors only focus on Switch. Currently, the author only focuses on a simplified setting of the switch Transformer layer (Fedus et al., 2021). However, there are also other popular MoE architectures, e.g. (Shazeer et al., 2017; Lepikhin et al., 2020; Lewis et al., 2021) as mentioned in the paper, and (Yanqi et al., 2022; Nan et al., 2022) in the following.

Zhou, Yanqi, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang, Vincent Zhao, Andrew M. Dai, Quoc V. Le, and James Laudon. "Mixture-of-experts with expert choice routing." Advances in Neural Information Processing Systems 35 (2022): 7103-7114. Du, Nan, Yanping Huang, 

Andrew M. Dai, Simon Tong, Dmitry Lepikhin, Yuanzhong Xu, Maxim Krikun et al. "Glam: Efficient scaling of language models with mixture-of-experts." In International Conference on Machine Learning, pp. 5547-5569. PMLR, 2022.

2. The writing of Section 3 is too fragmented and can be improved a lot. I would recommend authors to enrich Sections 3.2 and 3.2, since currently, they read like an experiment report with step-by-step procedures, instead of a well-written technical paper with good motivation and intuition of the proposed techniques.

### Questions
1. Can the authors explicitly present the physical running time? The results in the experiment section do not give a clear comparison.

2. What is the experiment platform, e.g. torch version or GPU model?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work investigates the problem non-differentiable of the expert selection, which is relevant in today Sparse Mixture of Experts (SMoE) implementations. Motivated from ODE methods, the proposed method, SparseMixer, derives a mid-point method to approximate the gradient with neglectable overhead. Experiments on pre-training, finetuning, and machine translation show that SparseMixer consistently outperforms SwitchTransformer and Dense training.

### Strengths
- SMoE has shown to be a promising direction to massively scale transformer models. This works investigates the non-differentiable problem of selection experts, which is at heart of existing SMoE strategies. 
- The proposed method is sound.
- The empirical results are encouraging where SparseMixer consistently outperforms SwitchTransformer with neglectable overhead.

### Weaknesses
## Major concern - limited broad impact
Although the method is sound, it seems to be only applicable to the case of choosing only $1$ expert per layer. However, most modern architecture employ a TopK function that choose $k=2$ experts, which has shown to achieve better results, e.g.[A]. Thus, despite the encouraging results, it may not bring immediate impact.

## Major concern - contribution of $\omega$-scaling
$\omega$-scaling essentially makes the network deeper, thus using it improves the performance is easy to understand. However, it also makes comparing with SwitchTransformer to be unfair because of the additional trainable parameters. How would SwitchTransformer+$\omega$-scaling performs against SparseMixer?

## Major concern - complexity analysis
I found the results in Table 3 to be questionable where SwitchTranformer and SparseMixer have identically average training costs. However, SparseMixer introduces several components such as $\omega$-scaling, computing the gradient $\nabla_0$, all of which contribute to the forward and backward computation. Thus, I think reporting the **total** training is more accurate to understand the overhead of SparseMixer.

## Minor concern - limited baselines
The number of baselines considered is quite limited. The authors also considered a simple naive Transformer architecture. Other advanced architecture such as GLAM [A] and other SMoE strategies such as XMoE [B] should be included to make the experiment more comprehensive.

## Minor concern - presentation
- I suggest the author to replace "MoE" to "SMoE" as MoE usually refers to using all experts. This work consider the selecting only 1 expert, thus adding the "sparse" keyword would make the presentation clearer. 
- Best results are not highlighted in Table 2.

### Questions
- Can SparseMixer be extended to $k>1$ easily?
- Please clarify the empirical contribution of $\omega$-scaling, i.e. comparing SparseMixer without $\omega$-scaling with SwitchTransformer **OR** SparseMixer with SwitchTransformer + $\omega$-scaling.
- Please clarify the overhead in SparseMixer in Table 3 and report the total training time.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
