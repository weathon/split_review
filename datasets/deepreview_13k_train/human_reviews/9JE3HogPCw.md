# Hadamard Representations: Augmenting Hyperbolic Tangents in RL

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Activation functions are one of the key components of a deep neural network. The most commonly used activation functions can be classed into the category of continuously differentiable (e.g. tanh) and piece-wise linear functions (e.g. ReLU), both having their own strengths and drawbacks with respect to downstream performance and representation capacity through learning (e.g. measured by the number of dead neurons and the effective rank). In reinforcement learning, the performance of continuously differentiable activations often falls short as compared to piece-wise linear functions. We provide insights into the vanishing gradients associated with the former, and show that the dying neuron problem is not exclusive to ReLU's. To alleviate vanishing gradients and the resulting dying neuron problem occurring with continuously differentiable activations, we propose a Hadamard representation. Using deep Q-networks, proximal policy optimization and parallelized Q-networks in the Atari domain, we show faster learning, a reduction in dead neurons and increased effective rank.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the dying neuron problem with tanh-type activations. The paper's first result is that bounded activation functions like tanh perform worse than ReLU-type activations. It is argued that the poor performance is probably due to the vanishing-gradient/dying-neuron problem faced by the tanh-type activations. The paper then proposes to solve the dying-neuron problem using Hadamard representations. Finally, it is shown that Hadamard representations outperform the standard DQN architecture.

### Strengths
The paper is generally well-written. The proposed solution is simple to use and novel. The usefulness of the proposed method is shown to be more effective than standard DQN.

### Weaknesses
The biggest issue with the paper is the weak empirical evaluation—particularly the following two points.
* The number of hidden units in Hadamard Representations is twice that of the base system. However, the comparison with the base system with 1024 hidden units is not done correctly. The base system with 1024 hidden units is not tuned. At least the learning rate of the base system should be tuned. I suspect that something like 5e-5 could be a good value for the learning rate for the base system with twice the number of hidden units. Using default hyper-parameters is insufficient when the architecture is changed by making it twice as wide. The paper has to convincingly show that  Hadamard representations provide a benefit over a well-tuned base system with twice as many hidden units.
* Missing baseline. The paper does not compare Hadamard representations to resetting baseline like Redo [1] and continual backprop[2]. Why not just reset the units that have saturated in the tanh network?

### Questions
See Weaknesses

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims to counteract the dead neuron and rank-collapse phenomena in RL. It proposes the 'Hadamard representation': simply duplicating the final encoder layer in the encoder of the 'Nature DQN' architecture and taking the elementwise product between the two outputs. Empirically, the results show an overall moderate increase in learning speed, together with lower dead neurons and higher rank-collapse as averaged over 8 Atari games.

### Strengths
1. Overall, I found the paper well-written and easy to parse through.

2. Already in the introduction, the paper concisely introduces the problem settings and effectively conveys the tradeoff between ReLU and Tanh with results (fig. 1) and toy examples (fig. 2).

3. Evaluation is conducted both with canonical off-policy and off-policy architectures/algorithms (Nature DQN and PPO) widely used in the broader literature.

### Weaknesses
Major:

1. The experiments are conducted on a very small fraction of only 8 hand-picked Atari games. While the performance of the proposed method is slightly higher than ReLU on average, this does not hold consistently even across these 8 games (as reported in the Appendix). Moreover, while these environments are notably sensitive to stochasticity, evaluation is carried out with only 5 random seeds I believe this to be very much insufficient for a paper with a simple architectural contribution that should be thoroughly validated. Thus, I am very much not convinced of the generality of these results, even across the full set of Atari environments, and would strongly encourage to expand this section. In case Atari is too demanding, I would suggest considering other more computationally-friendly benchmarks such as the 16 environments in the highly-parallelizable Procgen benchmark.

2. Even in the results of this paper, there does not seem to be a clear relationship between dead neurons/effective rank and performance, (e.g., ReLU outperforms Tanh while having a higher number of dead neurons). Thus, even analytically, I feel the paper in its current states leaves many unresolved questions and provides very little novel information.

3. I believe the claims about the probabilities of neurons 'dying' such as: "Taking a product of hyperbolic tangent activated neurons thus reduces the probability of neuron saturation from p to p^2." (ln242-243) are not correct, and potentially misleading, as they make independence assumptions that are not even reported by the paper's own results in Appendix C.3.

Minor:

Figures 3 and 5 show 32 very small graphs each with the value distribution of 16/512 hand-picked neurons at two hand-picked points during training. I did not find these figures convey much meaningful information and would suggest replacing them with a graph showing the percentage of dead neurons for tanh/relu/and Hadamard representations throughout training.

I would suggest adding Subsection numbers.

### Questions
I would appreciate it if the authors could address, in their response, the criticism raised above. In addition:

- In the MLP block of several modern LLMs such as Llama, the hidden representation is computed as (using this paper's notation) f(A_1x + B_1) * (A_1x + B_2). According to the paper's own analysis in Section 3, this simpler version should entirely prevent the dead neuron phenomenon with respect to the input activations. I wonder if the authors have considered and/or have this version.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a novel activation function based on Hadamard representations to address the limitations of traditional activation functions in reinforcement learning. It highlights issues like vanishing gradients and dying neurons, demonstrating that the proposed method improves learning efficiency and representation capacity in deep Q-networks and proximal policy optimization.

### Strengths
1. The proposed Hadamard representation effectively addresses dead neuron issue with existing activation functions, particularly in reinforcement learning contexts.
2. The experimental results show clear improvements in learning speed and performance metrics, providing solid empirical evidence for the claims made.
3. The paper presents a well-defined problem and clearly articulates its contributions, making the paper easy to understand.

### Weaknesses
1. The lack of a diverse range of network architectures tested limits the generalizability of the findings. The paper should test HR on various networks and test HR on different layers. It would be better if HR were a universal activation function suitable for all layers, rather than only suitable for the last layer.
2. Absence of detailed comparisons with other novel activation functions that have emerged recently.
3. The paper did not conduct tests on diverse tasks, e.g. MuJoCo, DMControl. using only Atari does not demonstrate that this is a universal issue in reinforcement learning.
4. As mentioned in Line 279, the experiments are all performed on 8 Atari games. Testing on only 8 Atari games does not sufficiently demonstrate a stable improvement in performance.
5. In the PREVENTING DYING NEURONS section in Line 191, the analysis is not related to reinforcement learning task at all. So, claiming that HR is an activation function particularly suitable for reinforcement learning feels somewhat forced.

### Questions
1. How do Hadamard representations compare with other recent activation functions not covered in the paper?
2. What potential challenges might arise when applying this method to different neural network architectures?
3. What is the result if HR is tested on various tasks, e.g. MuJoCo, DMControl, and more tasks on Atari?

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the role of activation functions on performance in reinforcement learning. Continuously differentiable, such as Tanh, can have advantages, including bounded output and smooth gradients. Practically, however, ReLU activations are more preferred. The authors investigate the reason and identify that the number of saturating tanh activations for all inputs increases with experience throughout the training. This decreases the network’s representation power (measured by the effective rank). To resolve this problem, the authors introduce Hadamard representations (HR) with Tanh. The authors showed that HR with Tanh experiences less saturation and mitigates loss in effective rank, which also reflects on performance. Through a series of experiments, the paper demonstrates the effectiveness of HR with Tanh.

### Strengths
This paper presents a novel approach to have more effective representations for reinforcement learning. Based on insights from previous works on dying/dormant neurons and their relationship to reduced network capacity, the authors present the Hadamard representations that experience less dormancy and thereby maintain the network representational capacity. I think this research is fundamental and important, and the proposed method is very simple to use and integrate into a wide range of methods, further enhancing its potential impact.

### Weaknesses
- Some definition inaccuracies:
  - The authors claim that the dying neuron problem is not exclusive to ReLU but also extends to Tanh and provide a definition where the activation output $|\alpha_i| \approx 1$. This definition is problematic for two reasons: 1) Intuitively, the neuron is not ‘dead’ if its output is not zero, and 2) the definition doesn’t work for ReLU. Instead, I suggest making this definition about saturating neurons, which would only work for tanh and sigmoid. The figures measuring the fraction of dead units (e.g., Figure 6a) need to reflect the fraction of dead or saturated units instead.  It is important to distinguish between saturated and dead neurons, as a saturated neuron, while having a near-zero gradient, can still output a large value, whereas a dead neuron outputs zero. Thus, the definition should be refined to classify neurons as either saturated or dead based on their output and gradient behavior. We cannot say a saturated ReLU.
  - The authors mentioned that the definition of a dead/saturating neuron applies when we test the neuron in all data in the buffer. Is this quantity actually being measured in the experiments? I am asking this because going through all the data in the buffer at each evaluation time seems very computationally expensive, so I was wondering if some approximation is made in measuring this quantity in the experiments section (e.g., sampling a fixed small number of samples from the buffer instead).
- Relatively limited empirical evaluation:
  - The empirical evaluation could be more substantial. The authors used 8 Atari environments with only five independent runs (with some overlapping error bars). I encourage the authors to use a larger number of independent runs (e.g., 10) to have more statistically significant results. Adding more environments would be great, although I recognize the hurdle of running extra Atari games.
  - More relevant activation function baselines are needed. Specifically, concatenated ReLU has been shown to improve plasticity in reinforcement learning [1] in addition to adaptive rational activations [2]. I think adding these two baselines is very relevant to understanding the effectiveness of HR Tanh against other recently investigated activation functions. Specifically, the concatenated ReLU (CReLU) shares similarities with the proposed Hadamard Tanh by increasing the dimensionality of the activation space, and it has been shown to improve performance in RL tasks. Therefore, it is crucial to compare against CReLU to demonstrate the effectiveness of the proposed approach.

**Minor issues:**
- The discussion in lines 207-212 needs revising.
- In line 103, $r_t$ should be $r_{t+1}$.
- In line 205, $h^\prime(x)$ should be $z^\prime(x)$.
- “Stronly” in line 357 is a typo

### Questions
- The authors mentioned in line 367 that they considered addition operation instead of Hadamard product and showed it performs poorly. There was no reason or postulate for why this is the case. Can the author provide a probability analysis similar to the one given on page 5?
- If the score is normalized with respect to the ReLU activation baseline score, why doesn’t the final ReLU baseline reach 1 at the end of training in Figure 7a and Figure 9a but slightly less than 1?
- Why did the authors use HR Tanh only for the last layer? What happens if you use it in all layers? The authors did mention that the success might not translate to convolutional layers. Can the authors present an experiment showing that and suggest what the reason might be? Additionally, why wasn't HR Tanh applied for the last two fully connected layers in the architecture?
- In line 13, “linear-unit functions” should be “piece-wise linear functions”
- I don’t see the reason for the paragraph starting at line 467. It is not relevant to the conclusion of the paper, and hence it should be removed.
- In some environments, such as Seaquest and SpaceInvaders, HR hurts performance compared to ReLU. Is there a reason for why?

### Soundness
3

### Presentation
3

### Contribution
3
