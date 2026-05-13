# Simple, Good, Fast: Self-Supervised World Models Free of Baggage

- Decision: Accept
- Scores: 3, 8, 6, 6

## Abstract
What are the essential components of world models? How far do we get with world models that are not employing RNNs, transformers, discrete representations, and image reconstructions? This paper introduces SGF, a Simple, Good, and Fast world model that uses self-supervised representation learning, captures short-time dependencies through frame and action stacking, and enhances robustness against model errors through data augmentation. We extensively discuss SGF’s connections to established world models, evaluate the building blocks in ablation studies, and demonstrate good performance through quantitative comparisons on the Atari 100k benchmark. The source code will be made available.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper discusses the design of a world model - a parametric model that predicts the transitions probabilities, reward functions and terminal state distributions to serve as a simulation environment for reinforcement learning. The paper proposes to simplify some existing elements in recent world-models, such as sequence models (i.e. RNNs, transformers), to focus on simple ingredients (e.g. frame stacking). It instead proposes to keep the maximum information and temporal consistency formulation as the most essential properties of effective world models. The resultant model is dubbed "Simple, Good and Fast World Models" (SGF) which demonstrates somewhat competitive performance against other existing world models in the Atari 100k benchmark.

### Strengths
## Presentation
This paper is well-written with thorough discussion on the related works, the design philosophy and the precise formulations of the proposed modeling. The discussions are usually precise and insightful. The important elements in building the proposed world-models, such as the POMDP formulation, the representation learning (including sufficient details, such as image augmentations, temporal consistency, covariance regularization), the dynamics learning (the conditional independence assumption and the resultant factorization) are all presented clearly, leaving the readers with no doubts on the technical components and the underlying reasoning.

In many cases, the discussions have involved clear contrast with prior works, for example in Table 1 where the design choices in a good selection of prior works are presented, and compared with the design choices in the proposed SGF.

## Empirical Studies
The paper is tested on the standard Atari 100k tasks that is standard for this kind of work. The empirical study seems sounds and demonstrates a few interesting properties of this work that may be useful for researchers in this area. In particular
- It has presented through ablation studies in Section 4.2. showing the importance of various design components, such as state (image) augmentations, action/frame stacking, temporal consistency and sample contrastive formulation. Additional details are also included in the appendix, such as in Table 3 in Appendix D.
- The paper has presented detailed comparisons with other methods, as presented in Appendix D Table 2.

### Weaknesses
There are a few limitations that seem to limit the contributions of this work.

- As discussed thoroughly in the related work section in the paper, world model in training reinforcement learning agents is not a new idea. In such cases, it is useful to establish that this work is addressing a significant weakness in prior works, without sacrificing other important metrics. In this case, the main motivation of SGF seems to be presenting a simple, fast, yet accurate method to train a good world model. While SGF certainly fit the bill for the first two, it seems to fall short significantly in the third. The result in Table 2 seems to suggest that SGF is much weaker than prior works such as IRIS and DreamerV3, which are all based on learning on imagination and hence are arguably fairly related.

-  The choice to drop sequence models appears to be a fairly significant limiting factor. This was acknowledged clearly in Line 462-464, which lists the decision to drop sequence models as a potential reasons why this work does not reach SOTA performance on Atari 100k. This seems like a fairly trivial observation - certain games in Atari 100k requires long term reasoning, and it is indeed one of the most challenging aspects of world models for RL agents. It should be expected that removing a components specifically designed to address this important challenge will result in inferior performance. It seems unlikely that researchers in this field will learn much more about how to design better world models if they are simply presented with results comparing methods with and without a sequence model - they probably already know that it is going to be much worse for certain tasks that require long term reasoning.

### Questions
I think it will be useful if the paper can present accuracy numbers in similar training time, or training time numbers at roughly the same accuracy numbers. That will be very useful in positioning this work against existing methods.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new approach to world modeling for the training of RL-based agents. The current state of literature employs different mechanisms to achieve a correct modeling of long sequences, including reconstruction, recurrent modules, memory, etc. The authors propose to simplify the world modeling and just use self-supervised techniques, inspired by VicReg, and a simple learning strategy for the system dynamics. There is a comparison of existing methods and the proposed one on Atari100k, and appropriate ablations of the components.

### Strengths
1. I believe these kinds of works are important. It is easy to just incrementally propose new components to improve the performance of systems while considerably increasing the engineering complexity. This does not give a clear view of the actual importance of the components included in the SOTA of world modeling. Going in a completely different direction is in my opinion a needed move sometimes, and it will help to shape new design choices for world modeling. Hence, the motivation is strong, and the reasoning behind that is coherent.
2. The results are compelling. I believe that on Atari100K the simple method proposed performs quantitatively well, even compared to baselines that are far more complex, and with considerably lower runtime.
3. The comparison with existing methods is nontrivial and requires a proper analysis of the literature. Table 1 is also interesting and will be useful for future work.
4. The paper is well-written and well-motivated, all introduced explanations are useful and the writing is compact enough. The proposed experiments are interesting.

### Weaknesses
1. I believe that while the proposed method focuses on short-term dependencies, as correctly stated in the limitation, how much performance degrades with an increasingly long-term dependency on actions would be important to quantify. This will allow us to assess the limitations of the proposed method in a more robust manner, for people to build upon. Specifically, the paper does not explore the method's performance when the agent needs to remember and act upon information from many steps in the past. This is crucial in many RL environments, and the lack of analysis makes it difficult to understand the applicability of the method in more complex scenarios. For example, in games requiring planning or memory of past events, such as Montezuma's Revenge, the method's performance might degrade significantly, and this should be quantified.
2. It is not clear to me why only VICReg is chosen for representation extraction. There are relationships with BYOL and SimSiam as reported in the appendix, but it is unclear how performance would change if these approaches were instead used for representation extraction rather than VICReg. The paper mentions that these methods are similar, but it does not provide any empirical evidence to support this claim in the context of the proposed method. Given the sensitivity of self-supervised learning to the choice of objective, it is important to understand how the performance would change if these alternatives were used. For instance, BYOL's reliance on a target network might lead to different dynamics in representation learning, and this should be explored.

### Questions
1. How do the method perform with long-term dependencies?
2. How do feature extraction perform if we change the SSL training objective?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors introduce model-based method: SGF (a Simple, Good, and Fast) world model.
The simplicity of the model is that: it stacks 4 previous frames and actions to capture short-time dependencies, and it uses data augmentation to enhance robustness. It is trained to provide maximum information and temporal consistency.
For simplicity, it does not use: image reconstructions, discretization of representations, sequence models (RNN, transformers, ...),  probabilistic predictions for deterministic environments.

They use several loss functions:
- MSE-loss for temporal consistency (between next embedding and action-conditioned next embedding)
- Variance and Covariance regularization loss for Information Maximization (use the current and next batches of embeddings as input)
- Loss for 3 distributions for Dynamics learning: 
    - transition - probability of transition to y'-representation if a-action is applied to y-representation (gradient is only propagated to a-action)
    - reward - probability of r-reward if a-action is applied to y-representation
    - terminal - probability of e-terminal-action if a-action is applied to y-representation

They train several models using AdamW optimizer: 
- Encoder (f computes representations from current and next input image observations): 4 convolutional layers (kernel size 4, stride 2, pad 1), linear layer dim = 512, norm-layer, SiLU activation
- Projector (g computes current and next embeddings from current and next representations): MLP with 2 hidden layers of dim = 2048
- Predictor (h predicts action-conditioned next embedding): MLP with 2 hidden layers of dim = 2048
- Transition network: MLP with 5 hidden layers of dim = 1024, and a residual connection from the input to the output (suggested to use the sequence model for future work)
- The networks of the reward distribution, terminal distribution, policy, and value function: MLPs with 2 hidden layers of dim = 1024

This simple approach achieves shorter training times compared to other world models and good performance on the Atari 100k benchmark.

### Strengths
In this work, authors try to find the most necessary components that are the most optimal in terms of accuracy and training time.

1. The presented SGF approach lies on the Pareto optimality curve on the chart of Accuracy (normalized mean score) and Training time (hours) - Figure 5, where the other points on the Pareto optimality curve are: SPR, DreamerV3, EfficientZero (performs lookahead)

2. The optimal combination of improvements (frame stacking, action stacking, temporal consistency, augmentations, sample-contrastive) has been found to achieve the highest accuracy in five games - Figure 4

3. Optimal sizes of models and training times have been found in Table 6 to achieve the highest possible mean scores

4. The presented experimental results show the necessity of temporal consistency in Figure 7

### Weaknesses
1. While optimal sizes of models and training times have been found in Table 6 to achieve the highest possible mean scores, this may mean that either the scalability of the approach is limited, or the approach must scale in many directions simultaneously to achieve even higher mean scores. Although the approach lies on the Pareto optimality curve on the Accuracy vs Training time chart, i.e. it is one of many optimal options, it is not shown how this approach can be scaled or improved to achieve the highest accuracy with increasing Training time. 
Or it requires more serious architectural changes, f.e. as the authors suggest for future work - to use the sequence model for transition network.

2. The proposed method is optimal for tasks that are probably simple enough and do not require remembering very old events, so it is sufficient to have a stack of 4 previous frames and actions, and it is not shown how this approach can be transferred to more complex tasks where orders of magnitude more memory of early events is required.

### Questions
Although this is partially explained in the Limitations, could you go into more detail about: for more complex tasks than Atari-games, where longer term knowledge needs to be remembered (where orders of magnitude more memory of early events is required), what parts of the models should be scaled up or significantly modified / replaced (e.g. using  sequence model: RNN, Transformers, ...) to be optimal in terms of accuracy and training time?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a world model that uses self-supervised representation learning, captures short-time dependencies through frame and action stacking, and enhances robustness against model errors through data augmentation. This paper is based on a partially observable Markov decision process. It stacks the recent observations and actions to capture short-time dependencies. It introduces stochasticity through data augmentation. To build meaningful representations of observations, this paper enforeces information maximization and temporal consistency of the features.

### Strengths
1. This paper contains thorough experiments.
2. The method is simple and fast.

### Weaknesses
1. The strategy of stacking observations and actions seem overfitting to the chosen dataset, Atari 100k benchmark, rather than fitting to the real-world, where long-term dependencies are common. The method's reliance on short-term context via frame and action stacking may not generalize to environments requiring reasoning over extended time horizons. This is a significant limitation as many real-world tasks involve complex temporal relationships that cannot be captured by simply concatenating recent frames and actions. The model's architecture appears tailored to the specific temporal dynamics of Atari games, which are often characterized by relatively short-term dependencies, and may not be suitable for more complex environments.
2. Related to the first weakness, while the games in the dataset are deterministic, real-world can be very stochastic. It is questionable whether the model can be applied in real-world cases. The deterministic nature of the Atari environment allows the model to potentially exploit specific patterns in the frame sequences, which may not be present in stochastic real-world scenarios. The lack of explicit mechanisms to handle stochasticity, such as modeling uncertainty or using probabilistic transitions, raises concerns about the model's robustness and applicability to real-world tasks where unpredictable events are common.

### Questions
Considering its simplicity, it would be nice and help the paper strongly if scalability can be demonstrated. Can it be scaled?

### Soundness
3

### Presentation
3

### Contribution
3
