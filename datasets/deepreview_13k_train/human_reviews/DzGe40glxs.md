# Interpreting Emergent Planning in Model-Free Reinforcement Learning

- Decision: Accept
- Scores: 8, 8, 8, 8

## Abstract
We present the first mechanistic evidence that model-free reinforcement learning agents can learn to plan. This is achieved by applying a methodology based on concept-based interpretability to a model-free agent in Sokoban -- a commonly used benchmark for studying planning. Specifically, we demonstrate that DRC, a generic model-free agent introduced by [Guez et al. (2019)](https://arxiv.org/abs/1901.03559), uses learned concept representations to internally formulate plans that both predict the long-term effects of actions on the environment and influence action selection. Our methodology involves: (1) probing for planning-relevant concepts, (2) investigating plan formation within the agent's representations, and (3) verifying that discovered plans (in agent's representations) have causal effect on agent's behavior through interventions. We also show that the emergence of these plans coincides with the emergence of a planning-like property: the ability to benefit from additional test-time compute. Finally, we perform a qualitative analysis of the planning algorithm learned by the agent and discover a strong resemblance to parallelized bidirectional search. Our findings advance understanding of the internal mechanisms underlying planning behavior in agents, enabling improved diagnosis, interpretation, and control of agent planning processes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper investigates whether planning -- a typically “model based” ability -- can emerge within the internal representation of “model free” agents. Specifically, the authors apply concept-based interpretability methods to identify planning-relevant concepts, whether they emerge, if they support planning, and if they can be intervened on to change the behavior of the agent. This is done for a “deep repeated ConvLSTM” (DRC) agent architecture trained on Sokoban tasks.

### Strengths
**[Originality]**
The investigation of emergent planning using a concept-based interpretability approach is original and interesting.

**[Quality]**
The paper is of high scientific quality, the experiments are rigorous, hypothesis driven and the conclusion (in the affirmative) is well backed-up.

**[Clarity]**
The paper is clearly written with relevant information adequately provided. 

**[Significance]**
Provides a greater understanding about what is possible with model-free training alone.

### Weaknesses
The setting the authors investigate is ultimately restricted to a single agent architecture (DRC) trained using a single type of model-free RL algorithm (IMPALA) in a single environment type (Sokoban). The author is candid about this limitation. Nevertheless, repeating the analysis over more environments could make the general results more convincing, and investigating other architecture and/or learning rules would make the insights more generally applicable (e.g. could it be that some algorithms give rise to planning while others do not?).

Further, the paper does not address the *consequence* of planning, i.e. why is planning useful at all? For instance, [Guez 2019] investigates *data efficiency* and *generalization* as signs for planning. [Wan 2022] shows that even model-based approaches do not necessarily exhibit adaptability to local change. Thus, while it is nice to see a concept-based notion of planning, investigating whether this *leads* to things such as data efficiency, generalization and adaptability can shed greater light for the usefulness of having these representations at all.

### Questions
1. Figure 4 demonstrates the quality of the probes. However, for completeness, would it be possible to provide additional metrics such as precision, recall, class confusion matrices, etc.? The reason is that the results in this work depend heavily on the probes, and therefore it would be good to be fully transparent about the behavior of the probes and its implication on the results.

2. L447: “we [intervene] by adding the representation of NEVER to cell state position on the short path”. Could the authors describe in more details how the representation is computed for interventions (ideally as equations / pesudocodes)? 
    - To my understanding, the authors train linear probes $f: \mathbb{R}^d \rightarrow \mathbb{R}^{|C|}$, with $d$ being the internal DRC representation dimension, and outputting a $|C|$-dimensional logit over the number of concepts (left right etc.). The idea here is to add a $d$-dimensional vector back into the internal DRC representation to change the agent’s behaviour, but since we are mapping from $|C|$ dimension to $d$ where $|C| << d$ (many $d$ can map onto the same prediction with high probability), how is this mapping done? Would one have to optimize for a $d$ that maximizes each class probability? 
    - Also, why add instead of replace? What would happen if you replace?

3. Can the authors briefly discuss if / how the method can be applied to other model-free methods  that do not have the same architecture as DRC? Is it applicable to all architectures trained with model-free objectives?

4. Spelling: L202 behavior should be capitalized

### Soundness
4

### Presentation
4

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
This paper investigates the internal behavior of a Deep RL algorithm, namely, DRC by Guez et al. (2019). The purpose of this work is to verify whether this model-free RL agent is capable of planning, even if it does not rely on an explicit model of the environment. This hypothesis is tested in a discrete environment called Sokoban. The paper contains three analyses: testing for important concepts in the neural network activations with linear probes, investigating how these concepts evolve during internal RNN iterations and during episode steps, and observing whether the policy can be influenced by providing a bias to these activations using the concepts above.

### Strengths
The paper addresses an interesting topic for the RL and planning communities. Understanding whether some form of planning-like behavior is present in model-free RL would greatly help in merging concepts that are now discussed separately and it can help in creating more capable hybrid agents.

The paper adopts an interesting technique that I did not previously encountered in the RL literature. They apply linear probes to the activations of the policy network with specific concepts that are symbolic representations of the future behavior of the policy. The definition of behavior-dependent concepts is an interesting concept that provides useful insights about the policy. The authors also confirm that forcing the internal representation related to the desired concepts can influence the policy in the expected way.

The paper is well written and it is easy to follow.

### Weaknesses
1. This paper studies one algorithm, DRC, in only one class of environments, Sokoban. This strongly limits the applicability of some of the insights, which cannot be immediately applied to different algorithms and environments. For example, although the idea of behavior-dependent concepts is interesting, the proposed concepts are strongly dependent on Sokoban (there is one feature for each cardinal direction and for each direction in which the box can be pushed by the agent). Nevertheless, considering that the intended purpose of the paper is to understand whether any model-free RL agent is capable of a planning-like behavior, a positive answer can be answered even by looking at a single agent and environment class. 

2. The paper often tends to be inclined towards a positive answer that DRC agents can plan, and omits to discuss alternative explanations for the observed behaviors. For example, an LSTM that is trained for N iterative steps is likely to provide more accurate answers after N interative steps at test time. Moreover, advancing throughout the episodes makes the concepts gradually easier to predict. Therefore, Figure 6 apparently represents the expected behavior of the network and it is not necessarily an instance of "plan formation", as suggested. Similarly, the fact that the arrows evolve as in Figure 1 does not necessarily imply that the agent is evaluating then refining an hypothetical policy. In some parts, the paper seems to over-interpret the meaning of a small number of empirical observations. For example, the statements in lines 373-376 or 425-427 are not sharp implications as stated in the text. Question (1) is also related to this point.

### Questions
(1) The policy network contains come convolutional layers. Thus, in my understanding, the fact that the activations in the policy network linearly correlate with the future movements of the agent can also be explained from the fact that the CNN can learn to encode the spatial gradients of the value function with respect to actions and neighboring states. If true, this hypothesis can be an alternative explanation for the presence of the concepts in the policy network.

(2) How an intervention is performed in practice? A quick description is given in line 462, but I believe a more precise description is required.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides the first mechanistic evidence (non-behavioural) that model-free reinforcement learning agents can learn to plan.  The authors do this by studying a Deep Repeated ConvLSTM (DRC) agent playing Sokoban. While previous work showed that DRC agents exhibit planning-like behaviors, this paper demonstrates that they may actually perform internal planning.

There are three main steps in the methodology: Firstly they use linear probes to probe for planning-relevant concepts in the agent's representations. They then look at how plans form within these representations and finally look at the causal relationship of this planning by intervening on the agent behaviour.

Using this methodology, they claim that the DRC agent have an internal representation of planning concepts and can form plans through an algorithm that is like a parallel bidirectional search, planning forward and backwards. It then evaluates and adapts its plans. There is further evidence from the fact that the agent develops planning capabilities that correlate with improved performance when given extra "thinking time".

All of this is done within the Sokoban environment.

### Strengths
The paper's main strength is in its rigorous approach to demonstrating mechanistic evidence of planning in model-free agents. The probing experiments are well-motivated and well-designed. The authors then build on this foundation through interventional experiments that demonstrate these representations causally influence the agent's behavior. 

The authors also show that the emergence of these planning capabilities correlates with improved performance when given extra computation time, connecting their mechanistic findings to previously observed behavioral results. The ablation studies also validate their methodological choices and demonstrate the robustness of the findings.

### Weaknesses
The lack of detail in the main part of the paper on what a concept means (which is left to the appendix) means that this important point is hard to follow. If reading the appendix is necessary to understand the paper, then the particular detail should not be in the appendix. The same goes for most sections of the appendix which should not be seen as appendices, but actually necessary parts of the paper to understand it as a whole.

One significant methodological weakness is the lack of statistical rigor in the empirical evaluation. The authors run only 5 random seeds for their experiments and perform no statistical significance testing, making it difficult to assess the reliability of their results. For example, when comparing performance between different probe types or intervention strategies, it's unclear whether the observed differences are statistically meaningful. The paper would be significantly strengthened by proper statistical analysis, including hypothesis tests, confidence intervals, and effect size calculations. The error bars in figure 4 are also surprisingly small and regular which is itself surprising. However, given that there is no code provided, it is impossible to know how reliable these results are..

Another major limitation is the narrow scope of the investigation. The paper focuses exclusively on a specific architecture (DRC) in a single environment (Sokoban), which means that it's impossible to know how well these methods or results generalise. The DRC architecture is somewhat atypical, with its multiple computational ticks per timestep, and it's unclear whether more conventional architectures could learn similar planning capabilities. It does not seem all that surprising that an architecture of this type might develop an intrinsic world-model.

Additionally, while Sokoban is a well-established planning benchmark, it has a very specific structure that may make it particularly amenable to the type of planning discovered. The authors do not discuss how their findings might extend to other environments or architectures. While the causal aspects of the paper strengthen their arguments, it would be particularly interesting to see negative results where planning is not found, using the same techiques.

### Questions
Have you tested whether more conventional architectures (without multiple computational ticks) can learn similar planning capabilities?
Can you provide statistical significance tests for your key comparisons, particularly where differences appear small relative to standard deviations?
In cases where the agent forms "almost correct" plans, what prevents it from finding the optimal solution? Is this a systematic failure mode?
Can you provide more analysis of the correlation between concept representation and additional compute benefit?
What led you to choose the specific concepts (Agent Approach Direction and Box Push Direction) to probe for? Did you investigate other potential planning-relevant concepts?
What happens with stronger or weaker interventions in the causal aspects of the experiments?
How computationally expensive is your probing methodology? Would it be feasible to apply this analysis in real-time during training?
Can you look at how the planning concepts emerge through the training process?
Will code be made available to reproduce the results shown here?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors conduct a series of experiments that mechanistically interpret learned neural network weights of reinforcement learning (RL) agents using deep repeated convLSTM (DRC) to determine whether they are internally planning on an implicitly learned model. The agent network is probed for specific, predetermined concepts in the Sokoban domain. The results evidence that these agents do learn spatially local concepts and reason about them in a manner resembling parallelized bi-directional search.

### Strengths
- This is a novel and interesting use of mechanistic interpretability.
- Provides solid empirical evidence that model-free RL agents can implicitly learn to plan under certain conditions.
- Performed experiments are highly relevant and results are well analyzed. all points made about the results are clear and it does not seem like any outstanding phenomena were overlooked.
- The discovery that this is reminiscent of bi-directional search is powerful, and may have implications on the future of model-based RL.
- visualizations of plans are easily interpretable and highly informative.

### Weaknesses
 - Does not dive into the effect of probing different layers, even though such results are displayed.
- Only tested domain is Sokoban. analyzing second domain that is fundamentally different from grid domains is highly recommended to show that this is not a domain-specific phenomenon.
- Does not provide any background on probing, even though this is a central part of the experimentation.
- No theoretical explanation as to why planning behavior emerges.

### Questions
- Is it possible that algorithms other than DRC that also exhibit emergent planning will be more similar other planning algorithms (as opposed to bi-directional search)?
- Can you explain or conjecture why parallelized bi-directional search is the algorithm that emerges in this case?
- What about the size of the model and the agent's capacity to learn the world model? Is there a tradeoff between the model size and the quality of concepts that are learned?
- It seems like DRC is a perfect fit for problems like Sokoban with spatially local properties.
- Is it possible to perform many computational ticks to arrive at a final plan and then act blindly according to that plan? would this yield high accuracy? what is the horizon to which such an agent can plan, and does this also have anything to do with the model size?

### Soundness
3

### Presentation
3

### Contribution
4
