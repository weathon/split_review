# MetaGFN: Exploring Distant Modes with Adapted Metadynamics for Continuous GFlowNets

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 5, 3, 6, 3

## Abstract
Generative Flow Networks (GFlowNets) are a class of generative models that sample objects in proportion to a specified reward function through a learned policy. They can be trained either on-policy or off-policy, needing a balance between exploration and exploitation for fast convergence to a target distribution. While exploration strategies for discrete GFlowNets have been studied, exploration in the continuous case remains to be investigated, despite the potential for novel exploration algorithms due to the local connectedness of continuous domains. Here, we introduce Adapted Metadynamics, a variant of metadynamics that can be applied to arbitrary black-box reward functions on continuous domains. We use Adapted Metadynamics as an exploration strategy for continuous GFlowNets. We show three continuous domains where the resulting algorithm, MetaGFN, accelerates convergence to the target distribution and discovers more distant reward modes than previous off-policy exploration strategies used for GFlowNets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper identifies that the exploration for continuous setting remains lacking in the context of GFlowNets. On the basis, it incorporates Adapted Metadynamics as an exploration strategy for continuous GFlowNets. Experiments demonstrate that the proposed method can accelerate convergence and provide more effective exploration.

### Strengths
- The theoretical results are sound and comprehensive.
- The research problem is fundamental and related to various subjects.

### Weaknesses
1. The process for selecting the low-dimensional collective variables $z(x)=
(z_1(x),\cdots,z_d(x))$ is not clear. Could the authors give an example illustrating how to obtain these CVs?

2. If the CVs can only obtained from expert knowledge, does this limit the applicability of the method to certain domains?

3. The choice of hyperparameters of KDE such as Gaussian width $\sigma$ and Gaussian height $w$ is not fully explained. Could the authors give more details?

4. Although the authors introduce adaptive metadynamics on pages 5-6, a more explicit breakdown of the differences and potential advantages of adaptive metadynamics over standard metadynamics would be helpful.

5. The experiments only reach a maximum dimension of 4 in the grid environment. Is this truly representative of high-dimensional cases? Expanding the experiments to higher dimensions would be more convincing.

6.  The terms "Adaptive Metadynamics" and "Adapted Metadynamics" are used interchangeably in the paper. If both terms refer to Algorithm 1, it would be helpful to choose one term consistently throughout to avoid potential confusion.

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates the exploration strategies for continous Generative Flow Networks (GFlowNets) by proposing a variant of metadynamics, termed Adapted Metadynamics. The proposed method, MetaGFN, applies to arbitrary black-box reward functions over continuous domains. The authors prove that Adapted Metadynamics is consistent and converges to standard metadynamics in a certain limit. They also empirically show that MetaGFN outperforms existing GFlowNet exploration strategies on continuous domains.

### Strengths
The paper introduces a variant of metadynamics that enables explorations in black box rewards and continuous spaces. It proves that the method reduces to standard metadynamics in a limit and provides empirical evidence that MetaGFN outperforms existing GFlowNets exploration strategies. This paper is well-written and has clear structures.

### Weaknesses
1. The process for selecting the low-dimensional collective variables $z(x)=
(z_1(x),\cdots,z_d(x))$ is not clear. Could the authors give an example illustrating how to obtain these CVs?

2. If the CVs can only obtained from expert knowledge, does this limit the applicability of the method to certain domains?

3. The choice of hyperparameters of KDE such as Gaussian width $\sigma$ and Gaussian height $w$ is not fully explained. Could the authors give more details? 

4. Although the authors introduce adaptive metadynamics on pages 5-6, a more explicit breakdown of the differences and potential advantages of adaptive metadynamics over standard metadynamics would be helpful.

5. The experiments only reach a maximum dimension of 4 in the grid environment. Is this truly representative of high-dimensional cases? Expanding the experiments to higher dimensions would be more convincing.

6.  The terms "Adaptive Metadynamics" and "Adapted Metadynamics" are used interchangeably in the paper. If both terms refer to Algorithm 1, it would be helpful to choose one term consistently throughout to avoid potential confusion.

### Questions
The questions are the same as in the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors work on exploration for GFlowNets in the continuous setting. Specifically, they combine continuous GFlowNets with Metadynamics, a Langevin dynamics based exploration strategy. They validate their method on a few smaller scale tasks.

### Strengths
- Connecting continuous GFlowNets and meta-dynamics is novel.
- Authors provide theoretical motivation for their approach.
- The proposed method works on the provided environments.

### Weaknesses
My biggest concern is that the authors fail to show their method's applicability in larger environments. The authors state this in their limitations, but then I feel the method loses its significance, especially since the novelty is rather limited. Even in the provided experiments, the results are not significantly better than the baselines. I would also like to see the runtime analysis of the baselines--this might make the work more appealing. Besides, while I understand the importance of theoretical nature of the writing, a intuitive explanation will greatly improve the quality of the work.

### Questions
- How does the method work for flow matching?
- What is the condition for terminating states in the hypergrid? In the work, I see $\mathcal{X} \approx R^d$, but to what extent does the approximation hold?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper adapts metadynamics technique from molecular modelling to improve mode exploration in continuous GFlowNets. The approach works in the setting of black-box reward distributions without access to reward gradients, employing kernel density estimates in a lower-dimensional collective variable space. The experimental evaluation is carried out on three continuous environments, showing that the proposed MetaGFN approach outperforms various existing GFlowNet exploration techniques.

### Strengths
This paper tackles a challenge that arises in GFlowNet training — mode exploration, which has received especially little attention in the literature in the case of continuous environments. Adapting metadynamics technique from molecular modelling, the paper falls into the important category of cross-disciplinary research.

The key strength of the paper in my opinion is thorough experimental evaluation in the presented environments. In addition to the proposed MetaGFN approach, paper presents the results for a number of baseline techniques, which were proposed in the previous works for discrete GFlowNets but in turn adapted by the authors to the continuous case. A faithful comparison is carried out, showing that MetaGFN has superior performance on average, but also clearly stating its shortcomings in some cases. I found Figure 5 really insightful.

### Weaknesses
I believe that the presentation of the proposed approach and the overall clarity of the paper can be greatly improved.

Without prior knowledge of metadynamics, it is challenging to understand the proposed approach from the text. Firstly, I suggest to move Section D of the Appendix to the main text, especially Algorithm 3, since it is crucial for understanding the overall structure of MetaGFN algorithm. Moreover, even though it is possible to understand the exact method from Algorithms 1, 2 and 3, I still have very little intuition about it. Before going into low-level details in Section 3, I would suggest adding a more high-level discussion explaining how the method works, some intuition behind it, and why it should improve exploration in continuous GFlowNets (Section 2.4 contains some, but it still doesn't give much high-level intuition). This would make the paper more accessible to a broader ML community.

In addition, some important details are unclear from the description of the experiments. Firstly, I failed to find in the text how collective variables are chosen for line and grid environments. The choice of collective variables is a crucial point in the algorithmic design of the proposed method, so emphasizing this is critical. Secondly, the clear descriptions of the choice of forward and backward kernels are missing. Especially little overall detail is given about grid environment. Is it the same as the one from [1]? It is possible that I missed some of these points while looking through appendix, but then it is one more reason to highlight them.

Next, from my understanding, the efficiency of the method directly depends on the choice of lower dimensional collective variable space. However, the dimensions of spaces of terminal states in all experiments are very low themselves (the maximum dimension is 4), so the big question is whether the proposed method can perform well in higher-dimensional tasks. Thus I suggest adding some higher-dimensional environment to the experiments. The method can still be interesting and viable if it can only perform well in lower dimensions, but then this should be clearly stated as a limitation, or experimentally demonstrated otherwise.

A minor detail, pdf works really slow when looking at Figure 4. I think reducing the density of the grids used to plot the training curves could help with it.

If all my concerns are addressed during rebuttal, I'm open to increasing my score.

References:

[1] Salem Lahlou, Tristan Deleu, Pablo Lemos, Dinghuai Zhang, Alexandra Volokhova, Alex Hernández-García, Léna Néhale Ezzine, Yoshua Bengio, Nikolay Malkin. A theory of continuous generative flow networks. ICML 2023

### Questions
0) Some experimental details are missing, see Weaknesses.

1) Could the proposed approach be applied to diffusion sampling tasks, e.g. on environments from [2]? If yes, adding some to the experimental evaluation would further strengthen the paper.

2) [2] introduces an approach where Metropolis-adjusted Langevin algorithm is used to explore the space of terminal states, store the results in a replay buffer, and then use the backward policy to sample trajectories ending in points stored in the buffer. Thus it shares a lot of similarities with the proposed method. Do I understand correctly that it cannot be employed in your setup because MALA requires access to the reward gradient? I believe it is important to add a discussion about this to the paper, so the work is clearly positioned in comparison to previous litareture.

3) In the definition of Measurable pointed graph, line 122, is it enough to bound the number of steps required to be able to reach any measurable set to guarantee acyclicity of the environment? The construction in [1] explicitly states that for some $N$, the support of $\kappa^N\left(s_0, \cdot\right)$ should contain only the sink state.

References:

[2] Marcin Sendera, Minsu Kim, Sarthak Mittal, Pablo Lemos, Luca Scimeca, Jarrid Rector-Brooks, Alexandre Adam, Yoshua Bengio, Nikolay Malkin. Improved off-policy training of diffusion samplers. NeurIPS 2024

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces MetaGFN, an exploration algorithm for continuous Generative Flow Networks (GFlowNets) that combines metadynamics with GFlowNets to improve exploration in continuous domains. The authors prove the consistency of their adapted metadynamics approach and conduct experiments to showcase the performance of the proposed MetaGFN method.

### Strengths
- The writing is clear and well-structured
- The methodology is explained in sufficient detail
- Addresses an important challenge in training GFlowNets

### Weaknesses
- Limited and unconvincing experimental evaluation:
  - The experimental evaluation relies exclusively on simple, toy environments that fail to capture the complexity and challenges of real-world applications, especially the line and Grid tasks with small scale. For example, the authors can consider the more complex and challenging molecule generation task and biological sequence design tasks from (Bengio et al., 2021) and (Jain et al., 2022) with high-dimensional and complex spaces. 
  - The authors have not demonstrated the method's effectiveness in scenarios where exploration is genuinely challenging or where reward signals are naturally rare
  - The results exhibit high variance (column 2, row 2 in column 3, rows 1-2 in column 4, rows 1-2 in column 5 in Fig. 4) and L1 loss values (all figures in Fig. 4), contradicting the paper's claims about robustness
- Insufficient empirical evidence for claims:
  - The paper claims that MetaGFN "is the most robust" (line 375) variant, yet this assertion is questionable given the high L1 loss values and large variances shown in the results (Fig. 4)
- Scalability concerns:
  - No evaluation in high-dimensional spaces, which is crucial for real-world applications
  - Missing discussion of potential limitations in high-dimensional settings
- Novelty concerns: 
  - The paper primarily combines two existing methods (metadynamics and GFlowNets), but the experimental results do not convincingly demonstrate advantages over simpler alternatives, and the practical utility of the method remains uncertain given the limited evaluation. Therefore, the contribution seems incremental without strong empirical support

### Questions
1. How does MetaGFN perform in more challenging exploration settings? This is crucial for practical applications but isn't addressed in the current experiments.
2. How does the method scale to higher-dimensional problems? The current experiments are limited to low-dimensional spaces.

### Soundness
2

### Presentation
2

### Contribution
2
