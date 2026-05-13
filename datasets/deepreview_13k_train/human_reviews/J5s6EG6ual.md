# Investigating Self-Attention: Its Impact on Sample Efficiency in Deep Reinforcement Learning

- Decision: Reject
- Scores: 1, 3, 5

## Abstract
Improving the sample efficiency of deep reinforcement learning (DRL) agents has been an ongoing challenge in research and real-world applications. Self-attention, a mechanism originally popularized in natural language processing, has shown great potential in enhancing sample efficiency when integrated with traditional DRL algorithms. However, the impact of self-attention mechanisms on the sample efficiency of DRL models has not been fully studied. In this paper, we ponder the fundamental operation of the self-attention mechanism in visual-based DRL settings and systematically investigate how different types of scaled dot-product attention affect the sample efficiency of the DRL algorithms. We design and evaluate the performance of our self-attention DRL models in the Arcade Learning Environment. Our results suggest that each self-attention module design has a distinct impact on the sample complexity of the DRL agent. To understand the influence of self-attention modules on the learning process, we conduct an interpretability study focusing on state representation and exploration. From our initial findings, the interplay between feature extraction, action selection, and reward collection is influenced subtly by the inductive biases of the proposed self-attention modules. This work contributes to the ongoing efforts to optimize DRL architectures, offering insights into the mechanisms that can enhance their performance in data-scarce scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper claims to investigate the sample efficiency of self-attention mechanisms in image-based reinforcement learning. The paper mentions that they compare different types of scaled dot-product attention. However, the paper suffers from multiple major flaws including the model architecture as well as the choice of the self-attention operations used for experiments.

### Strengths
- The paper attempts to analyze different types of self-attention layers. The motivation is good.

### Weaknesses
 - The paper uses a self-attention layer within a couple of CNN layers as their model architecture. This is a very shallow unusual architecture for any visual representation learning. In Transformers, it is a very common practice to have a series of MHSA layers and MLP layers interleaved. At least use ViT? The current architecture used for the investigation is extremely limited and no concrete conclusions can be made using them.

- The paper mentions that they investigate different self-attention. However, the selection of the attention mechanism to compare seems highly arbitrary. The operations selected in this paper include Spatial-wise-Attention, Channel-wise-Row(/Column)-Attention, and so on, but I have not seen any major state-of-the-art models using these arbitrary attention mechanisms in its architectures. Are these being used in any of today’s large vision-language models? What’s the point of comparing something that’s not being picked up by anyone? It would have been much more meaningful to compare different types of Transformer components that’s actually being used in practice, such as linear attention mechanisms like Performer and sequential models like Mamba2, which are much more of interest to the general audience.

- The observations from the experiments seem inconclusive. It is very difficult to conclude from these limited experiments which do not show any major trend.

### Questions
- It will be great if the authors can provide more justifications on their choice of the model architecture and the selection of the attention operations.

- What do you mean by this sentence in line 318? " To visualize the effect of self-attention modules in the feature space, we extract the attended feature maps [math symbol] which are the element-wise sum of the attention maps [math symbol] and the feature maps [math symbol] of the first CNN layer." What is the "[math symbol]"? This seems totally out of context?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work investigates the performance differences on ALE games with different self-attention operations for visual reinforcement learning. The self-attention operations include (1) direct self-attention on the feature map, (2) self-attention on the height dimension, (3) self-attention on the width dimension, and (4) the sum of (2) and (3). The conclusion is that different attention operations have different impacts on different games, which is brought about by different game mechanics.

### Strengths
1. This paper investigates an interesting topic after Manchin et al., examining whether different attention operations can impact visual DRL learning differently.

2. This paper evaluates 56 games within the ALE benchmark, ensuring the broad applicability of the results, and uses stratified bootstrap confidence intervals for reliable assessment. Compared with Manchin et al., the experiment uses 56 games and 5 seeds, which enhances the experimental results.

3. The paper designs and contrasts four types of self-attention modules (SWA, CWRA, CWCA, CWRCA), revealing how each module’s inductive biases affect learning efficiency in specific environments.

4. The paper is brief and straightforward.

### Weaknesses
1.  After reading the entire paper, I still struggle to understand the connection between the terms “sample efficiency” and “attention operation” in this paper. To my understanding, the attention operation only makes differences in network structures. It makes sense that different network structures bring different learning performance. However, “sample efficiency” relates to choosing different transition pairs from the replay buffers or the experience batches. Could you explain more about this part?

2.  The related work section should contain more references. Three papers are not enough; you should investigate and survey more.

3. The types of self-attention are far more varied than different channel operation sequences. More investigations are required if the author aims to make significant and fundamental contributions to the ongoing efforts to optimize DRL architecture.

4. This paper's insights are poorly developed, lack theoretical analysis, and rely merely on limited observations. It fails to provide adequate insights for the community. E.g., “Different attention operations have different impacts on different games” cannot guide the community. Conclusions like “height dimension self-attention provides more performance improvement on vertically moving games” would be more beneficial.

### Questions
1. In Figure 6, methods lacking an attention mechanism seemingly learn critical environmental information effectively. Conversely, variants incorporating attention mechanisms appear to have limited learning capabilities, often failing to capture essential details or maintain precise focus. Could you provide explanations for this phenomenon?
2. Figure 7 shows that the mean and standard deviation of the logits for both CWRA and CWRCA are the lowest, which indicates a less exploratory behavior due to a more uneven logit distribution. Are the conclusions presented in the paper incorrect?
3. Could you analyze the causes and conditions under which artifacts occur? Are there potential ways to eliminate these artifacts? For example,  Related work like [2] explores artifacts in vision. Can you offer similar in-depth insights?
4. Beyond the scaled dot-product operation discussed in this paper, could other aspects of attention affect sample efficiency?

[2] Darcet, Timothée, et al. "Vision transformers need registers." In *International Conference on Learning Representations*, 2024.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the impact of self-attention when improving the sample efficiency in DRL. Specifically, the investigation focuses on how different types of scaled dot-product attention affect the performance in ALE. The methods are categorized by over which channels the dot product is applied, including SWA, CWRA, CWCA and CWRCA. In particular, the author discovered the effect of inductive biases of the self-attention modules, such as attending to objects movement horizontally or vertically can be rewarded in different game environments. The author conclude that self-attention modules have different effect to the interplay between the inductive bias and the game mechanics.

### Strengths
1. The topic is quite interesting, as it connects NLP and DRL, and self-attention has also attracted lots of attention in developing more advanced RL algorithms nowadays.

2. The setup of experiments is quite thorough and well-thought, especially with the evaluation metrics and state presentations.

3. The results are quite interesting and give us new perspective about the importance of self-attention. Meanwhile, I found te explanations of those results satisfactory.

### Weaknesses
1. The author did not give information about the choices of hyper-parameters or any ablation study regarding the network structure. In the experiment section, only the experimental setup and the evaluation methodology are discussed. This can be a problem.

2. Following point 1, what kinds of setups for self-attention modules have you tested? Have you tried to vary the number of self-attention layers and the heads? I think it is crucial to study all different aspects of MHSA as well. This is because MHSA is more applicable in NLP and Vision Transformers than simplex self-attention operations.

### Questions
1. Can you disclose the hyper-parameter choices?

2. Can you give more explanations on what the current results imply towards MHSA? Explain the rationale for focusing on single-head attention and whether the findings would generalize to MHSA.

### Soundness
3

### Presentation
3

### Contribution
2
