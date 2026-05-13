# SimBa: Simplicity Bias for Scaling Up Parameters in Deep Reinforcement Learning

- Decision: Accept
- Scores: 6, 8, 8, 8

## Abstract
Recent advances in CV and NLP have been largely driven by scaling up the number of network parameters, despite traditional theories suggesting that larger networks are prone to overfitting.
These large networks avoid overfitting by integrating components that induce a \textit{simplicity bias}, guiding models toward simple and generalizable solutions. 
However, in deep RL, designing and scaling up networks have been less explored.
Motivated by this opportunity, we present \textit{SimBa}, an architecture designed to scale up parameters in deep RL by injecting a simplicity bias. SimBa consists of three components: (i) an observation normalization layer that standardizes inputs with running statistics, (ii) a residual feedforward block to provide a linear pathway from the input to output, and (iii) a layer normalization to control feature magnitudes. 
By scaling up parameters with SimBa, the sample efficiency of various deep RL algorithms—including off-policy, on-policy, and unsupervised methods—is consistently improved.
Moreover, solely by integrating SimBa architecture into SAC, it matches or surpasses state-of-the-art deep RL methods with high computational efficiency across DMC, MyoSuite, and HumanoidBench.
These results demonstrate SimBa's broad applicability and effectiveness across diverse RL algorithms and environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents SimBa, an architecture specifically designed for deep reinforcement learning that scales up network parameters by integrating a simplicity bias. The SimBa architecture employs observation normalization, residual feedforward blocks, and layer normalization, fostering simplicity in function representation. By adopting these components, SimBa enhances the sample efficiency and compute efficiency of various RL algorithms. It performs comparably or better than state-of-the-art methods in diverse RL benchmarks, demonstrating effectiveness across off-policy, on-policy, and unsupervised settings.

### Strengths
1. **Innovative Application of Simplicity Bias**: The use of simplicity bias in SimBa to manage overparameterization effectively is a novel contribution to deep RL.

2. **Comprehensive Empirical Validation**: SimBa's performance is rigorously tested across multiple RL tasks, including DMC, MyoSuite, and HumanoidBench, showing consistent improvements in efficiency and scalability.

3. **Adaptability**: SimBa’s architecture is algorithm-agnostic and can integrate seamlessly with various RL algorithms, allowing its broad applicability.

4. **Effective Design Choices**: The architectural components (e.g., RSNorm and residual connections) seem thoughtfully selected to reduce complexity while enabling parameter scaling.

### Weaknesses
1. Missing relation works about normalization. Researchers show that the RMS Norm works well in training foundation models. The proposed RSNorm is too similar to the RMS Norm, while the author has no discussion about the RMS Norm (even not in related work). Since this work investigates designing and scaling up networks in deep RL, the same tricks in designing and scaling up LLMs should be considered.

2. Unfair comparison between SAC+SimBa v.s. others. Since SAC+SimBa introduces some other layers, it might include more parameters for the neural networks. The author can make some ablations with different sizes of SAC to exclude the capacity issue.

3. Missing details of the model size. I didn't find the detailed sizes of each model. If the sizes are small (such as 10M), the conclusions about the so-called "scaling up" are doubtful.

### Questions
1. I am curious about the scaling results on multi-task RL policies, since the proposed architecture is added to the representation part. By the way, maybe the author should also compare the results with baseline methods under scaled-up backbones.

2. The author chose a new metric named simplicity bias score for comparison and analysis. The results also show some effects of the initial parameter distributions. Why not compare with the baseline methods with initialization periodically?

Nikishin, E., Schwarzer, M., D’Oro, P., Bacon, P. L., & Courville, A. (2022, June). The primacy bias in deep reinforcement learning. In International conference on machine learning (pp. 16828-16847). PMLR.

### Soundness
3

### Presentation
3

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
The paper introduces SimBa (Simplicity Bias), a novel architecture designed to scale up parameters in deep reinforcement learning (RL) by incorporating simplicity bias. The key components of SimBa are:
- Observation normalization layer
- Residual feedforward block
- Layer normalization

The authors demonstrate that SimBa exhibits higher simplicity bias compared to standard MLPs and shows consistent performance improvements as the number of parameters increases. When integrated with various RL algorithms, including SAC, TD-MPC2, PPO, and METRA, SimBa improves sample efficiency. Moreover, SimBa matches or surpasses state-of-the-art off-policy RL methods across 51 continuous control tasks while maintaining computational efficiency

### Strengths
- Novel approach: SimBa addresses an important gap in deep RL research by exploring how to scale up network parameters while leveraging simplicity bias effectively.
- Versatility: The architecture improves sample efficiency across various RL algorithms, including off-policy, on-policy, and unsupervised methods.
- Performance: When applied to SAC, SimBa matches or surpasses state-of-the-art off-policy RL methods across a wide range of tasks.
- Computational efficiency: SimBa achieves high performance without relying on computationally intensive components or complex training protocols.
- Theoretical foundation: The authors provide a clear explanation of simplicity bias and how it's measured, grounding their work in existing theory.
- Significance: This work addresses an important gap in deep RL research by exploring how to effectively scale up network parameters while leveraging simplicity bias. The SimBa architecture offers a promising approach to improve performance across various RL algorithms and tasks without relying on computationally intensive components or complex training protocols

### Weaknesses
 - While the evaluation covers 51 continuous control tasks, it might be beneficial to see SimBa's performance on a wider range of RL domains, particularly with images.
- The paper doesn't discuss potential limitations or scenarios where SimBa might not be as effective

### Questions
- Applicability: Are there any specific types of RL problems or environments where SimBa might not be as effective?
- Why are the standard errors in Figure 10 so high?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose the SimBa architecture, which, by inducing simplicity bias, allows scaling the size of neural networks in deep reinforcement learning problems. The proposed architecture is a neural network with residual connections, with post-layer normalization and observation normalization at the beginning. The authors claim that SimBa enables networks to scale up without sacrificing generalizability, avoiding the overfitting issues often associated with high-parameter models in RL.

### Strengths
1. Clear and Well-Motivated Objective: The paper identifies simplicity bias as an underexplored factor in RL network scaling.
2. Reproducibility Efforts: A public codebase and descriptions of evaluation setups are provided.
3. Broad experimental setup.

### Weaknesses
1. Statistical significance is not apparent from the presented results. The standard error overlaps in some plots, e.g., Figures 1b, BRO, and SimBa on Figure 5b, and Figure 8 has no rages, but I guess it would be more challenging to add them since the analysis is in two dimensions, and also from Figure 14. The tables in the Appendix do not have standard deviations. Moreover, authors could use some t-test or Mann–Whitney U test to demonstrate statistical significance.
2. It would be valuable to see reversed to Fig. 4 ablation, i.e., simplicity and Return when you turn off every single component. Clearly, all components analyzed in section 5.1 have some synergic effect -- they do not help much alone. However, it is not apparent how all of them are important in this synergy, i.e., from section 7.1, we know that RSNorm is very important -- If I understand correctly, SimBa without observation normalization works very poorly. But how will the lack of RSNorm affect the simplicity of the architecture? -- I would suggest visualizing this similarly to Figure 4, but on the Y-axis, it would be, e.g., SimBa - RSNorm or SimBa - Residual.




### Questions
1. Out of curiosity, SimBa is usually the most time-efficient (except SAC), but on HumanoidBench, it is slightly worse than TD7 and BRO. Do you know why?
2. The simplicity bias hypothesis looks pretty general; therefore, how will this architecture work on image-based problems?
3.  How do you expect SimBa to be applied in the discrete control tasks? Will it be enough to beat BBF on Atari as BRO on continuous control? -- Of course, new experiments on Atari would be too much for the rebuttal period, but maybe the authors have some thoughts about this.
4. How do your results about simplicity bias measured through Fourier features relate to this paper [1]? As I understand, authors of [1] claim that neural networks are naturally biased to learn low frequencies faster, and it is hard for them to learn high-frequency signals, which is present in reinforcement learning. SimBa promotes architectures that are biased towards low frequencies. Could you share your perspective on how these findings interact or complement each other?

[1] Yang, G., Ajay, A., & Agrawal, P. (2022). Overcoming the spectral bias of neural value approximation. arXiv preprint arXiv:2206.04672.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper builds upon the insights of the paper by [Teney et al, 2024], which shows that certain architectural implementations provide a simplicity bias, which could be one of the more causal explanations to their practical usefulness.

In order to transfer this notion of simplicity bias to RL, the authors run tests with SAC on proprietary state-based RL, ranging from easy (Cartpole etc.) to hard (Humanoid, Dog, etc.) environments.

To maximize the simplicity bias of vanilla SAC, the authors augment the original architecture with RSnorm, Residual Feedforward blocks and Layer Normalization. Additionally, the authors scale up the architecture.

The results are promising, showing that keeping a simplicity bias in the network allows for scaling up the network, elevating vanilla SAC to the level where it can perform very well on DMC-Hard tasks, without using algorithmic advancements. 

Although results are only done on state-based architectures, the harder environments like Humanoid & Dog still allow for sufficient difficulty in the evaluation. Additionally, pixel-based environments have already shown correlation between simplicity bias in the CNN and performance (Residual connections in CNN’s -> Impala architecture), although to the best of my knowledge, the reason being a simplicity bias was never concluded by these researchers.

### Strengths
- Easy to implement, which is promising for future work.

- Good comparison with a SOTA algorithm TD-MPC2, and even an ablation using SimBa on TD-MPC2.

- A strong step forward in the domain of non-algorithmic improvements in RL.

### Weaknesses
 - The plasticity analysis in Appendix C. could be confusing to the average reader. It shows a comparison to a basically ‘collapsed’ baseline MLP, as the effective rank is negligible. This might give a reader the impression that these are the representative network properties of training with a vanilla MLP, and paints a too strong picture of SimBa’s added network properties. I believe it would therefore be much more informative to the reader to add an additional 2 rows of figures to Fig. 15:
 		- Row 1: Plasticity analysis on DMC - medium
                - Row 2: Plasticity analysis with all the ablations of Fig. 4, to show the unique effects of every module.

- As important as it is to see that SimBa is computationally cheap, it would be also interesting to add some figures showing longer training (e.g. 5 million timesteps) on DMC hard and comparing to TD-MPC2 and the baseline SAC. The current results are limited to 1 million timesteps, which might not fully demonstrate the long-term benefits or limitations of the proposed approach, especially when compared to TD-MPC2 which might have different convergence properties over extended training.

- I believe a mention of the improvements that the Impala network gave to RL should be in the paper, and maybe a short sentence about the correlation (Residuals connections -> Simplicity Bias -> better Convergence). The paper currently lacks a discussion on the connection between architectural choices and the simplicity bias, which is a central claim of the paper. Specifically, the link between residual connections, which are a key component of the SimBa architecture, and simplicity bias should be explicitly stated, especially given the prior work on the Impala network and its use of residual connections.

### Questions
See Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
4
