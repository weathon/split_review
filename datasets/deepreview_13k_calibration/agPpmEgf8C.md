# Predictive auxiliary objectives in deep RL mimic learning in the brain

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8

## Abstract
The ability to predict upcoming events has been hypothesized to comprise a key aspect of natural and machine cognition. This is supported by trends in deep reinforcement learning (RL), where self-supervised auxiliary objectives such as prediction are widely used to support representation learning and improve task performance. Here, we study the effects predictive auxiliary objectives have on representation learning across different modules of an RL system and how these mimic representational changes observed in the brain. We find that predictive objectives improve and stabilize learning particularly in resource-limited architectures. We identify settings where longer predictive horizons better support representational transfer. Furthermore, we find that representational changes in this RL system bear a striking resemblance to changes in neural activity observed in the brain across various experiments. Specifically, we draw a connection between the auxiliary predictive model of the RL system and hippocampus, an area thought to learn a predictive model to support memory-guided behavior. We also connect the encoder network and the value learning network of the RL system to visual cortex and striatum in the brain, respectively.
This work demonstrates how representation learning in deep RL systems can provide an interpretable framework for modeling multi-region interactions in the brain. The deep RL perspective taken here also suggests an additional role of the hippocampus in the brain-- that of an auxiliary learning system that benefits representation learning in other regions.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors use a multi-objective RL model that combines a Q-learning module with an auxiliary predictive objective to demonstrate advantages of predictive learning on representations for multi-regional interactions in neural networks.  Using foraging tasks on gridworld scenarios as an example, they demonstrate that using an auxiliary predictive module results faster training and smoother representations of the task environment.  They also demonstrate that increasing the time horizon for predictive learning produces networks that retrain faster on new tasks in the same environment.  Interestingly, the learned representation is crucial for this as scrambling the transition structure results in much slower learning. They then demonstrate that some of the representational changes observed in the model reflect similar changes observed in real neural networks.

### Strengths
The description of the methods and approach is fairly clear and the overall goals of the paper are clear, with some room for improvement.  The numerical experiments provided demonstrate how a predictive loss benefits the learned representations available in a downstream area (not necessarily directly related to the area responsible for prediction), without the "predictive area" necessarily providing any direct information to the area responsible for valuation and action selection.

### Weaknesses
One important feature that isn't clear from what is presented in the paper is how the environment itself may or may not affect these results.  I don't find any examples of what gridworld environments are being solved by these models, let alone how complex they are.  Surely the predictability of the environment itself has some bearing on the rate of learning and retrainability for novel tasks, not to mention the quality of representations?  Please provide examples of these environments.  If possible, please consider varying the complexity of the environments.  

minor:

- Bottom of page 3 "the standard double deep Q-learning temporal difference loss function":  Even though standard, please either provide the form of this loss or provide a reference.  

- page 4, just below figure caption, definition of positive sample loss:  should o_{t+1} be z_{t+1}?

- last sentence, first paragraph page 5:  "the predictive model is trained with..."  (No "be")

- first sentence, section 4.2:  remove "is used" at the end of the sentence.

- first sentence, last paragraph on page 7:  remove "to",I.e. "undergo experience-dependent changes".

- last paragraph, page 8:  "remembering the previous trial type". (Remove "whether"), also empty reference at the end of that sentence.

### Questions
- Can you provide example environments?

- What is the effect of varying the complexity of the environment?  


Similar to the above, the encoder seems to have all available information about the environment (in principle), so the predictive task is in some sense simpler than it otherwise might be for a real organism, which only has clues to its environment.  Do you have thoughts about how partial observability might affect the predictive module?  (This is beyond the scope of the paper, but might be worth speculating on.)

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper implements a deep RL framework with predictive auxiliary objectives for representation learning. The authors demonstrate in a gridworld setting that predictive objectives improve representation learning by preventing representation collapse and enhancing transfer learning when transition structure remains unchanged. The paper also relates the components of the deep RL model to different brain regions, including the sensory cortex, the hippocampus, and the striatum. They show that representation learning in the predictive model resembles the neural activity observed in the brain, and learning in the encoder model resembles neural observations in the visual cortex.

### Strengths
- Overall I really enjoy reading this work, due to its clear presentation both in the text and in the figures, experiments testing different perspectives of the model, and the strong link to the brain
- This work introduces a multi-region model that is developed from a normative perspective, instead of fitting to recorded data, which can be extended to other tasks and to test against new biological evidence
- I appreciate the discussion of the limitation that predictive auxiliary objectives may be less helpful when the transition structure or policy changes

### Weaknesses
 - It's interesting to see in section 4.4 where the authors describe the effects of value learning in the encoder network, but this part feels somewhat disconnected from the rest of the paper, as the primary focus is to demonstrate how predictive objectives can lead to representation changes similar to those seen in the brain

### Questions
- I'm curious to learn if there is a similarity between the action selection network and the neural activity observed in the striatum
- Figure 2: Were cells that didn't show place-like activities filtered out in these analyses?
- Were there also place-like activities in the encoder model?

### Soundness
4 excellent

### Presentation
4 excellent

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
In this work, the authors explore modeling the effect of auxiliary predictive losses on a deep RL agent trained to navigate a spatial gridworld environment. The architecture consists a convolutional encoder that encodes the visual observation, a prediction layer that generates predictions for the auxiliary losses, and a Q-learning agent that takes the encoded state and returns Q-values/actions for the main reward objective. There are two auxiliary losses: a positive sampling loss, which is predicting future states, and negative sampling loss, which encourages representations of non-consecutive states to be distinct from each other. Multiple analyses inspired by neuroscience experiments were employed to show the value of these predictive losses: visualizing the latent state space showing that predictive losses help with representational collapse, showing how long horizon state predictions help with learning new goal locations, looking at how the predictive auxiliary objectives help in producing the "splitting" phenomenon, and showing how the encoder (through virtue of prediction) will adapt to novel transition sequences. 

Overall, I think this work is cool and exciting. But I do think portions of the submission have clarity that is below the caliber of an iclr paper. I have initially rated marginally below acceptance (5), but I want to assure the authors that most of my issues are with regards to providing clarity/details. I hope to see the incorporation of more clarity and details in the writing during the rebuttal and would be more than happy to re-evaluate my score after such changes.

### Strengths
* The experiments seem to be done soundly and rigorously. 

* The authors do an excellent job introducing various relevant neuroscience experiments and grounding the phenomenon into specific predictions for their model. 

* The authors use an exciting emerging framework of auxiliary losses to tackle an important problem, which is modeling multiple regions of the brain simultaneously while performing a difficult task.

### Weaknesses
The related works section is a little small/sparse. The authors do a good job in highlighting works on auxiliary predictive losses in RL within the machine learning realm, but I think there is also a growing body of work that is using this framework to produce various behavioral phenomenon in cognitive science/neuroscience. These are complimentary works to the current submission and would be good to include. Here are some examples that I feel should definitely be included:

1. Kumar et al. 2022 NeurIPS use auxiliary predictive losses in RL agents to predict abstractions of the observation, operationalized through language and symbolic programs, in order to reproduce abstract human biases. 
2. Jensen et al. 2023 bioRxiv introduce a predictive auxiliary loss which helps the agent learn when to plan and reproduces replay patterns seen in rodent hippocampal work. 
3. This is not exactly auxiliary predictive loss, but I think it is having the same effect, Binz & Schulz 2022 NeurIPS show adding a regularization term to the loss on the number of bits required to compress the agent's weights reproduces quirks in human exploration.

I think the clarity in some portions in this submission can be improved. 

1. On page 4, the description of the auxiliary losses can be improved. Its an important part of the work so it'd be good to have this be as clear as possible. A sentence describing what exactly $\tau$ is representing and why  $\mathcal{L_{+}}$ is a loss term that enforces transition structure in the state representations would be very helpful. Also, for the third term in $\mathcal{L_{+}}$, shouldn't it be $\tau (z_{t+1},a_{t+1})$ and not $\tau (o_{t+1},a_{t+1})$? For the negative sampling loss term, making it explicit $z_{i}$ and $z_{j}$ are latent representations of states that are not consecutive in the same area where the loss term is introduced would be helpful. It'd also be good to have a sentence explaining the motivation for choosing these two specific auxiliary losses. I suspect its loosely inspired by pattern completion vs pattern seperation in hippocampus (respectively) but it would be good to confirm that in this section. 

2. It would be helpful to state what the colors in Figure 2D mean. It wasn't clear to me upon first read. 

3. The memory component in page 8 is not explained at all. It seems important to describe what this is to put Fig. 4's results in context. 

There are a couple of design decisions that left me a little confused (details in the questions section). It would be nice for the authors to clarify the motivations behind them.

Last, I don't think there was any section in the paper explicitly discussing the limitations of the work. I think this is an important part of any iclr paper so it'd be good to include one.

### Questions
1. Why use an off-policy learner (Q-learning) rather than on-policy? An on-policy learner would seem to be more biologically realistic. Also I think an actor-critic approach (e.g. A2C, PPO, etc) may reflect what striatum is doing more than Q-learning? 

2. Is there a reason why there is no recurrence in the model? Striatum will indirectly project back to sensory cortex via thalamus. Also it may be possible that hippocampus projects back to sensory visual cortex. Hippocampal activity early in a trial can be predictive of information in visual cortex at a later time in the trial (see Hindy et al. 2016 Nature Neuroscience). Regardless of the biological realism of these recurrent connections, I think there could be useful normative principles in having recurrent loops between modules in this architecture. 

3. Fig 5c: The change in firing rates seem pretty small between before/after exposure. Are these changes statistically significant?

References:
Hindy, N. C., Ng, F. Y., & Turk-Browne, N. B. (2016). Linking pattern completion in the hippocampus to predictive coding in visual cortex. [Nature neuroscience](https://www.nature.com/articles/nn.4284), 19(5), 665-667.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
