# Spiking Hybrid Attentive Mechanism with Decoupled Layer Normalization for Joint Sound Localization and Classification

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 8, 1, 5

## Abstract
Localizing and identifying sound sources simultaneously through binaural cues is a crucial ability of humans, which facilitates our perception of complex surrounding scenes. 
Brain-inspired Spiking Neural Network (SNN) offers an energy-efficient and event-driven paradigm thus it is highly suitable for simulating the signal processing of such perceptions in organisms. 
Despite recent progress, most existing approaches in SNNs solely focus on a single task, disregarding the broad practicality of multitasking, or fail to consider the complementary features from audio modality for explicit enhancement. 
Inspired by the biological information sharing within multiple tasks, in this study, we propose a powerful multi-feature oriented sound source localization and classification framework based on SNNs, namely SpikSLC-Net.
Specifically, we design a novel Spiking Hybrid Attention Fusion (SHAF) mechanism that incorporates spiking self-attention modules and spiking cross-attention modules, which can effectively capture temporal dependencies and align relationships among diverse features. 
Then, considering the vanilla layer normalization (LN) requires dynamic calculation during runtime and involves a significant amount of floating-point operations, we present a unique training-inference-decoupled LN method (DSLN) for SNNs.
To further aggregate the multi-scale audio information, two task-specific heads are introduced for the final direction-of-arrival (DoA) estimation and event class prediction.
Experimental results demonstrate that the proposed SpikSLC-Net achieves state-of-the-art performance with only 2 time steps on SLoClas dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper designed a multi-task spiking neural network (SNN), by incorporating spiking self-attention modules and cross-attention modules that can capture temporal dependencies, to solve both sound source localization and classification tasks. The authors further introduced training-inference-decoupled layer normalization (DSLN), and demonstrated similar performance in benchmarking on SEC tasks with fewer time steps.

### Strengths
1. This paper showed novelty as a first implementation in multi-task learning with full SNNs in audio domain, while previous papers on SNNs have focused more on single classification task. 
2. Strong benchmarking performance in showing superior accuracy in both SEC and localization tasks, lower MAE for localization task, at fewer time steps. , which further brought possibility on short latency given few time steps required by SNN.

### Weaknesses
1. Most previous SEC task reported F1 score to account for potential bias in sound classes. Would it be possible to show F1 score benchmarking with previous SEC task (potentially could leverage some DCASE datasets) instead? Such high accuracy was unclear to me if there were any biases, and unclear whether your algorithm has specific bias on precision vs. recall. 
2. Ablation studies of DSLN do not suggest the difference is statistically significant, suggesting a relatively small or even no impact on the strong performance in SEC and localization tasks. 
3. Additionally, ablation studies did not show how self-attention and cross-attention modules could play an essential role in decoding these tasks. The non-significant differences in numbers of SHAF blocks and embedding dimensions (Table 2) posed a confusing and open question on where the major performance benefits from. It would be more persuading by providing a stronger ablation study, showing how SHAF blocks contribute to the essential performance boosting here, while the rest of modules (multi-task) remained in the model.

### Questions
1. Following above in weaknesses, I think it would be helpful to perform ablation studies, showing the role of the proposed SHAF blocks and DSLN specifically in the superior performance. The fact that ablation studies did not show strong impact wrt different hyperparameters in SHAF and LN modules, pose a question on whether the major benefit comes from the multi-task heads, or different algorithmic complexity of this SNN vs. previous SNN.  
2. Can authors provide benchmarking with F1 score, precision, recall? 
3. Can authors provide an algorithmic complexity analysis of this SNN vs. previous SNN?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a Spiking Neural Network based framework for sound source localization and classification. The framework incorporates a novel Spiking Hybrid Attention Fusion (SHAF) mechanism and a unique training-inference-decoupled Layer Normalization method (DSLN), and achieves state-of-the-art performance on the SLoClas dataset with minimal computational steps.

Overall, within the spike neural network framework, this is a useful contribution. Although I have doubts about it's performance relative to traditional ANNs and CNNs, it is nice to see SNNs applied to a wider array of complex audio tasks.

### Strengths
The paper introduces a novel approach to simultaneous sound source localization and classification using SNNs. I haven't seen such use of SNNs for audio-related multi-task learning

The introduction of the Spiking Hybrid Attention Fusion mechanism, is interesting. This mechanism seems to capture temporal dependencies and aligns relationships among diverse features.

Layer Normalization: The DSLN method proposed for SNNs addresses the challenges associated with dynamic calculation during runtime in vanilla layer normalization. This method reduces the floating-point operations required, making it more suitable for SNNs.

Energy Efficiency: The framework’s design is motivated by energy efficiency, which is a significant consideration for deploying models in real-world applications, especially on edge devices.

The paper shows strong  performance on the SLoClas dataset

The ablation studies are good and show that the proposed layer norm maintains strong performance while reducing the overall computation

### Weaknesses
Baselines - The method compares with other SNN baselines and one ANN baseline. However I would like to see comparisons with other recent ANN methods. For example the method in (https://arxiv.org/pdf/2010.06007.pdf) is able to localize and separate speech to 2.1 degrees, although it uses 8 microphones to do so.

Achieving 99% accuracy with only 2 timesteps during inference is impressive, but it does raise questions about overfitting. It would strengthen the paper to have some real world examples or examples on a different dataset besides the Sloc dataset.

### Questions
Do you have any other results to compare against traditional ANN methods?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a spiking neural network model (SpikSLC-Net) for joint sound localization and classification. Extending earlier work on attention in spiking neural networks, the authors propose a cross-attention mechanism. In addition, the propose a form of layer normalization which they claim to be more suitable for spiking neural nets than the vanilla version. They show that their approach outperforms a few earlier spiking neural network approaches on the SLoClas dataset.

### Strengths
+ Spiking neural networks are an interesting and important research direction
 + Sound localization and classification are relevant perception problems
 + Models able to solve multiple tasks are a relevant research direction also in the auditory domain

### Weaknesses
1. Unclear why this particular combination of problems and approaches

It is not clear to me what the goal of the paper is. If it's about sound localization and classification, why do we need spiking neural nets? If it's about spiking neural nets, why such a narrow focus on this particular (combination of tasks)? What motivates the development of the LN layer for spiking nets? The paper reads like a very specific approach to a very specific problem, where the approach is not motivated by the requirements of the problem. Thus, it remains unclear to me what we can learn from this paper.


2. Claims not supported well by experiments and evidence

The paper makes four main claims at the end of the introduction. The first three of them are not supported by evidence in my opinion.

 1. The authors claim their paper is the first to use multi-task learning in SNNs and audio-related tasks. That may well be the case, by why is this a contribution? There is little evidence presented that multi-task learning is necessary to achieve the goal (sound localization and classification) or that it improved performance on either of the tasks. Table 3 shows that training each task individually works almost as well on localization and equally well on classification. As there are no error bars given, it remains difficult to judge whether there is an effect at all.

 1. The Spiking Hybrid Attention Fusion (SHAF) mechanism is presented as a contribution of the paper. However, I could not follow its description in the paper because too many symbols were not defined. Moreover, it is not clear to me whether this mechanism could actually be implemented with spiking neurons on neuromorphic hardware, since Q,K,V are claimed to be real-valued.

 1. The training-inference-decoupled LN method (DSLN) is presented as a contribution of the paper. Again, I could not follow what is happening since too many symbols were undefined. Generally, it is not clear to me what's the goal here. Since the whole point of layer norm is to normalize by activation statistics of other units in the same layer, I don't understand how the authors want to absorb it into the weights of the previous layer (seems to be the goal of Eq. 15) and why they drop the variance normalization (if getting rid of the sqrt is the goal, they could, e.g., use mean absolute deviation instead).


3. Lack of strong baselines

The authors claim to outperform earlier methods. That might be the case for the two spiking neural nets in Table 1, but how strong are these baselines? The ANN baseline casts some doubt: Why would the spiking version outperform an ANN baseline? What's the mechanism that makes a spiking net perform better than one that doesn't restrict itself to spiking? This seems to be an implausible claim or a very weak baseline.


4. Narrow evaluation

In case the goal is not to solve these two particular tasks (sound localization and classification) but to make a contribution to spiking neural nets in general, the paper would need a more thorough evaluation of a broader set of problems/datasets to demonstrate the usefulness of the method. If, however, the goal is to solve these particular two tasks, then I think there are better approaches than SNNs and it is not clear why the authors focus on SNNs.


5. Lack of clarity in methods

I found the description of the methods extremely hard to follow and could not resolve a number of questions. Part of the reason is that in many cases the motivation for doing something is not spelled out clearly at the outset, another part is that many symbols are simply not defined, not explained or their dimensions remain unclear. A few examples:

 1. Fig. 2: Meaning of N, F, B_g and B_m are unclear. They are not defined in the figure caption. N seems to be used at multiple places for multiple different things. In this Fig. it might refer to the number of microphone pairs, but later (Eq. 8) it shows up again with a different meaning. It looks like T x F x E from Fig. 2 might correspond to T x N x D in Eq. 8, but since neither are defined, I can only guess.

 1. The meaning of the symbols in Eq. 8 is unclear. First, the dimensions T x N x D: What does each mean? If T refers to time, does this mean attention extends over time? What are the dimensions of W_Q, W_K and W_V? and what does the product X_alpha W_Q mean? Why is there a batch norm around this product? That's not usually the case in Transformer attention. What is the meaning of SN(.)? The action potential symbols in Fig. 3 do not really help. What are the dimensions of SN(.), both input and output?

 1. Section 4.3, in particular Eq. 15 remains unclear to me. W, W'_*,* are only defined in terms of dimensions, but it's neither clear what they are, how they come about nor what m and n in their dimensions mean. Also, A_i has not been introduced.

### Questions
### 1. Why this combination of problems and approaches

It is not clear to me what the goal of the paper is. If it's about sound localization and classification, why do we need spiking neural nets? If it's about spiking neural nets, why such a narrow focus on this particular (combination of tasks)? What motivates the development of the LN layer for spiking nets? The paper reads like a very specific approach to a very specific problem, where the approach is not motivated by the requirements of the problem. Thus, it remains unclear to me what we can learn from this paper.  
  
  
### 2. Claims not supported well by experiments and evidence

The paper makes four main claims at the end of the introduction. The first three of them are not supported by evidence in my opinion.

 1. The authors claim their paper is the first to use multi-task learning in SNNs and audio-related tasks. That may well be the case, by why is this a contribution? There is little evidence presented that multi-task learning is necessary to achieve the goal (sound localization and classification) or that it improved performance on either of the tasks. Table 3 shows that training each task individually works almost as well on localization and equally well on classification. As there are no error bars given, it remains difficult to judge whether there is an effect at all.

 1. The Spiking Hybrid Attention Fusion (SHAF) mechanism is presented as a contribution of the paper. However, I could not follow its description in the paper because too many symbols were not defined. Moreover, it is not clear to me whether this mechanism could actually be implemented with spiking neurons on neuromorphic hardware, since Q,K,V are claimed to be real-valued.

 1. The training-inference-decoupled LN method (DSLN) is presented as a contribution of the paper. Again, I could not follow what is happening since too many symbols were undefined. Generally, it is not clear to me what's the goal here. Since the whole point of layer norm is to normalize by activation statistics of other units in the same layer, I don't understand how the authors want to absorb it into the weights of the previous layer (seems to be the goal of Eq. 15) and why they drop the variance normalization (if getting rid of the sqrt is the goal, they could, e.g., use mean absolute deviation instead).



### 3. Lack of strong baselines

The authors claim to outperform earlier methods. That might be the case for the two spiking neural nets in Table 1, but how strong are these baselines? The ANN baseline casts some doubt: Why would the spiking version outperform an ANN baseline? What's the mechanism that makes a spiking net perform better than one that doesn't restrict itself to spiking? This seems to be an implausible claim or a very weak baseline.



### 4. Narrow evaluation

In case the goal is not to solve these two particular tasks (sound localization and classification) but to make a contribution to spiking neural nets in general, the paper would need a more thorough evaluation of a broader set of problems/datasets to demonstrate the usefulness of the method. If, however, the goal is to solve these particular two tasks, then I think there are better approaches than SNNs and it is not clear why the authors focus on SNNs.


### 5. Lack of clarity in methods

I found the description of the methods extremely hard to follow and could not resolve a number of questions. Part of the reason is that in many cases the motivation for doing something is not spelled out clearly at the outset, another part is that many symbols are simply not defined, not explained or their dimensions remain unclear. A few examples:

 1. Fig. 2: Meaning of N, F, B_g and B_m are unclear. They are not defined in the figure caption. N seems to be used at multiple places for multiple different things. In this Fig. it might refer to the number of microphone pairs, but later (Eq. 8) it shows up again with a different meaning. It looks like T x F x E from Fig. 2 might correspond to T x N x D in Eq. 8, but since neither are defined, I can only guess.

 1. The meaning of the symbols in Eq. 8 is unclear. First, the dimensions T x N x D: What does each mean? If T refers to time, does this mean attention extends over time? What are the dimensions of W_Q, W_K and W_V? and what does the product X_alpha W_Q mean? Why is there a batch norm around this product? That's not usually the case in Transformer attention. What is the meaning of SN(.)? The action potential symbols in Fig. 3 do not really help. What are the dimensions of SN(.), both input and output?

 1. Section 4.3, in particular Eq. 15 remains unclear to me. W, W'_*,* are only defined in terms of dimensions, but it's neither clear what they are, how they come about nor what m and n in their dimensions mean. Also, A_i has not been introduced.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose SpikSLC-Net, a novel SNN based architecture dealing with sound event localization and classification tasks simultaneously. To effectively integrate acoustic features extracted jointly from both GCC-PHAT and Log-mel Spectrogram,  they combine SSA module together with its extended SCA module and propose a novel SHAF block involving the aforementioned two attention modules, which is declared as fundamental to utilize synchronization information between multiple feature modalities. Experiments also manifest a state-of-the-art performance of the proposed architecture.

### Strengths
1. To the best of my knowledge, it is the first work for a SNN based model manifesting its strong effectiveness in multitasking like SELC task, even exceeds the performance of ANN model.
2. The paper is well written and clearly presented. The motivation is meaningful and interesting.
3. Employing GCC-PHAT feature and Log-mel Spectrogram altogether to fully explore the characteristic of sound sources is advisable, which naturally fit for the design of multi-head attention mechanism.

### Weaknesses
1. Though achieving state-of-the-art performance on SLoClas dataset, the proposed architecture still lacks novelty. According to my understanding, the core part of the architecture is the SHAF block, however its components are just copies or slight modifications/extensions of spiking self attention mechanism proposed in [zhou et al., 2022]. The extension seems straight forward and may not be regarded as a genuine technical contribution.
2. Some of the notations are not align with the others. For example, sometimes the embedding feature dimension is denoted as $D$, but sometimes not (fig 2).
3. Though performing best on SLoClas dataset, it is hard to conclude that the current work is better than previous works in terms of sound localization and classification. More experiments on various datasets is recommended.
4. Comprehensive analysis of the robustness to noisy environment is insufficient.
5. As in [zhou et al., 2022], comparison of computation complexity and estimated power consumption are highly recommended to be embraced in the experiments.

### Questions
The above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
