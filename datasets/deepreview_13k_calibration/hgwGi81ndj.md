# Efficient Exploration and Discriminative World Model Learning with an Object-Centric Abstraction

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 8, 6, 6, 6

## Abstract
In the face of difficult exploration problems in reinforcement learning, we study whether giving an agent an object-centric mapping (describing a set of \textit{items} and their \textit{attributes}) allow for more efficient learning. We found this problem is best solved hierarchically by modelling items at a higher level of state abstraction to pixels, and attribute change at a higher level of temporal abstraction to primitive actions. This abstraction simplifies the transition dynamic by making specific future states easier to predict. We make use of this to propose a fully model-based algorithm that learns a discriminative world model, plans to explore efficiently with only a count-based intrinsic reward, and can subsequently plan to reach any discovered (abstract) states.
    
    We demonstrate the model's ability to (i) efficiently solve single tasks, (ii) transfer zero-shot and few-shot across item types and environments, and (iii) plan across long horizons. Across a suite of 2D crafting and MiniHack environments, we empirically show our model significantly out-performs state-of-the-art low-level methods (without abstraction), as well as performant model-free and model-based methods using the same abstraction. Finally, we show how to reinforce learn low level object-perturbing policies, as well as supervise learn the object mapping itself.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a method for solving particular object-centric abstract MDPs with discrimitive world models, count-based exploration and planning / shortest path methods.
The paper shows very strong empirical results on two problem domains, Minihack and Crafting. The paper also presents results on learning low-level behaviors and object-centric representation (in a supervised way).
Overall the paper contains intersting insights into model-based RL when applied to higher level abstraction.

### Strengths
- Overall, clearly presented
- very efficient method for solving high-level problems of a particular structure (Ab-MDP)
- study of different transfer aspects
- extensive comparison to strong method and impressive results
- comprehensive analysis with lots of additional details in the appendix

### Weaknesses
 - The method needs quite strong assumptions on the high-level MDP, which are that usually only one element is changing or nothing changes. The authors also argue that replanning fixes some amount of violation of that assumption, but an environment where agent/object positions need to be modeled on the high level would not work from my understanding.

 - I did not understand the exploration used in section 4.1:
You introduced the count-based exploration before, but that does not seem to be used here? The task return is when running Dijkstra, right? Is there an exploration phase here?

 - The paper does not adequately address the limitations of the abstraction. Specifically, the method's efficiency will likely suffer when dealing with high-frequency changing attributes, such as object positions, as the abstract MDP state space grows significantly. This limitation should be discussed more explicitly.



### Questions
1. I did not understand the exploration used in section 4.1:
You introduced the count-based exploration before, but that does not seem to be used here? The task return is when running Dijkstra, right? Is there an exploration phase here?
1. Can the authors comment on why they did not employ value iteration on the high-level instead of Dijkstra. That could deal with stochastic outcomes. 
1. For the Dreamer and MuZero baseline: did you run enough / more updates per collected data in the transfer setting? If you reset the policy it needs to be learned again. Dreamer needs to run many updates using the dream-phase to rebuilt it. In this sense the comprison is a but unfair, as your are using run-time planning. I suggest to run Dreamer with a larger number of dream-updates with the new reward function before interacting with the environment.

## Comments:
- Very little detail about the training/architecture of the world model in the main paper, I suggest to at least mention the architecture and the loss in the main paper.
- The paper needs some careful proof reading:
    - Abstract: the last sentence : to reinforce learn and to supervise learn is an uncommon use of the words
    - first sentence of intro: have been major roadblocks: I think this is not correct. They have been topics of active research and many very effective solutions have been proposed. So I suggest to change that sentence
    - l086: eaching havin form
    - l143: more fully
    - l196: trainbale
    - l251: plot 95 confidence interval
    - l270: paragraph is missing details on how exploration is done etc.
    - l313/314, 331/332, 404/405
    
- In the related work, you might want to mention this paper:
Curious Exploration via Structured World Models Yields Zero-Shot Object Manipulation
https://openreview.net/forum?id=NnuYZ1el24C
that also shows that structured representations, world-model structure, and planning for exploration yield strong models and zero-shot capabilities (shown in manipulation).

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
The proposed using an abstract model of the world to plan with, and presents a model learning algorithm along with it. The main selling point of these abstractions is that they are object-centric. They respect specific useful tools in the environments, and curate the agent’s learning to be around them. These objects and their attributes are also human-interpretable.
They show how this can lead to better performance than existing model-based methods, and perform an empirical study into the components responsible for this, along with listing the settings where it does work.

### Strengths
* Answers the questions they presented in the abstract and introduction.
* The Methods section is succinct and points the reader towards the relevant experiments, based on the topic / interest.
* Contributions are all listed usefully (and addressed)

### Weaknesses
 * Abstractions are not discovered. It would be beneficial to explicitly state this limitation earlier in the paper, as it significantly impacts the scope of the work. The reliance on pre-defined object abstractions limits the agent's ability to adapt to novel environments where such abstractions are not readily available or are not well-defined.
* The Abstract MDP proposed here and the options framework are two different mathematical objects. The Ab-MDP cannot be interpreted as options. Under the options framework, the Ab-MDP _may_ be interpreted as a semi-MDP. As mentioned in the appendix, it is the behavior, b, can be interpreted as an option. The paper should more clearly distinguish between the Ab-MDP as a planning space and the behavior as an option, highlighting that the Ab-MDP is a higher-level construct that uses behaviors as primitives, rather than being directly equivalent to options themselves. The current framing risks conflating these two concepts.
* In Section 4:
     - Paper doesn't explicitly mention how many seeds were used in the experiment. The appendix hints at least 3, but it would be good to know how many were used for each plot. This lack of clarity makes it difficult to assess the statistical significance of the results and the robustness of the conclusions. The paper should explicitly state the number of seeds used for each experiment and justify the choice.
     - Figure 4b: Which triangle is IMPALA, RND and ICM in each plot? The overlapping of these methods makes it impossible to discern their individual performance. The figure needs to be revised to clearly distinguish between these methods, perhaps by using different markers or slightly offsetting the data points.
     - Figure 5: Why do none of the black lines have error bars? Are they single seed? If so, that would be useful to specify in the caption. The absence of error bars makes it difficult to assess the variability of the results, and the reader is left to wonder if the results are representative or an outlier. If these are single seed runs, it should be stated explicitly, and if not, error bars should be included.
     - Figure 5a: Why does the blue line start high? Is this just a plotting artefact? The initial high performance of the blue line is not explained, and it is unclear if this is a plotting artifact or a genuine result. The paper should provide an explanation for this behavior, and if it is a plotting artifact, it should be corrected.
* [Very Minor] Last sentence of abstract: change wording to talk about “reinforcement learning” and “supervised learning”
* [Very Minor] Typo: line 325: “representatin”

### Questions
The relationship between the competence of a behaviour and the transition matrix was not made clear. Is the paragraph trying to say: a competent behaviour will have most/all of the probability mass concentrated on some other state s.t. X_{t+1} != X_t ?

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
4

### Summary
This paper proposes a method for efficient exploration and world model learning in reinforcement learning (RL) by leveraging an object-centric abstraction. The authors define an Abstracted Item-Attribute Markov Decision Process (Ab-MDP), where abstract states are sets of items and their attributes, and actions are abstract behaviors corresponding to object-perturbing policies. They introduce MEAD (Model-based Exploration of abstracted Attribute Dynamics), a fully model-based algorithm that learns a discriminative world model predicting the success probability of abstract behaviors. MEAD uses count-based intrinsic rewards and Monte-Carlo Tree Search (MCTS) for efficient exploration and plans using Dijkstra's algorithm to reach goal states. The method is evaluated on a suite of 2D crafting and MiniHack environments, demonstrating significant improvements in sample efficiency and performance over state-of-the-art baselines. The authors also show that MEAD transfers well to new environments and tasks and discuss how to learn the object-centric mapping and object-perturbing policies when they are not provided.

### Strengths
1. Novelty: The approach proposed improves exploration and world model learning in RL by utilizing object-centric abstractions and discriminative modeling.
2. Efficient Exploration: MEAD adopts a discriminative world model and countbased intrinsic reward for efficient exploration.
3. Experimental Results: Plots and explanations are detailed and clear.
4. Transfer and Generalization: The paper shows MEAD can transfer zero-shot and few-shot to new environments and object types indicating of its generalization ability.
5. Interpretable World Model: Object-centric abstraction naturally can lead to an interpretable world model which can be helpful for understanding agent behavior.

### Weaknesses
1. Assumption of Given Abstraction: The approach inherently assumes access to an object-centric mapping and competent object-perturbing policies. This limits the applicability in scenarios where getting these mappings can be cumbersome. Specifically, the reliance on a pre-defined object-centric mapping, which is crucial for defining the Ab-MDP, restricts the method's use in environments where such mappings are not readily available or are difficult to obtain. The paper does not sufficiently address the practical challenges of acquiring this mapping in complex, real-world scenarios.

2. Abstraction Learning: The authors discuss learning the object-centric mapping and the policies. However, more details and empirical validation would strengthen this section. The description of learning the object-centric mapping via supervised learning is brief, and the practical challenges of collecting a sufficiently large and diverse dataset of (S, X) pairs are not discussed. Furthermore, the method's sensitivity to the quality of the learned mapping is not thoroughly explored. Similarly, the explanation of how object-perturbing policies are learned lacks sufficient detail, and the impact of imperfect policies on the overall performance of MEAD is not adequately addressed.

3. Experimens: It is not clear if the experiments using PPO and Dreamer-v3 are applied to Ab-MDP or to the MDP setting. It is mentioned that these methods are used in Ab-MDP, but there also is "we also show the final performance of state-of-the-art exploration  methods in the low level MDP" in the caption for Figure 4. Additionally, there is no comparison with any of the methods that are closer to the proposed method (a good number of them are mentioned in the Related Work section). Also, for the comparison with PPO and Dreamer-v3, the proposed method is not evaluated in the settings and environments in which the baseline methods are mostly evaluated for their performance. Therefore, it is unclear how the proposed method is generalizable over more complex environments and the comparison do not sound quite fair. The lack of comparison with methods that use similar high-level representations, such as those mentioned in the related work, makes it difficult to assess the specific advantages of the proposed approach. The experiments do not adequately demonstrate the method's scalability to environments with a large number of objects and object attributes.

4. Clarity: Certain parts of the paper and the overall flow of information can be improved and clarified. For example, the paragraph starting at line 161 and ending in line 167 could be revised to convey the message more clearly. Additionally, the explanation of T(X′|X, b) in lines 109-111 could be rephrased for better clarity. Here are some errors I noticed: in line 316, "the agent observe" should be corrected to "the agent observes," and in line 331, "themin" should be separated as "them in."

### Questions
1. Could you provide more details on how the object-centric mapping \( M \) is learned in practice, especially in complex environments and the environments where such mappings are not readily available? How does the performance of MEAD depend on the quality of this mapping?

2. What are the computational requirements of MEAD compared to the baselines? For example, how does the planning  (MCTS and Dijkstra's algorithm used) affect it and is it feasible in more complex environments with larger state space and action space?

3. How does your method compare to the methods closer to yours, such as the ones mentioned in your Related Work section?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work presents MEAD, a model-based planning method that learns a semantic reward-free world model in an abstracted MDP. The learned model is then combined with standard search algorithms to generate goal-reaching trajectories.  The abstracted MDP comprises of an object-centric mapping, where a state consists of a discrete set if items, each associated with a set of attributes. Notably, this work focuses on learning a discriminative world model, which predicts the probability of reaching a particular state, given an action (defined in the paper as behaviour) and current state. Results on 2-D crafting and Minihack show that MEAD significantly outperforms existing baselines.

### Strengths
1. **Clear writing and presentation**: The paper is well-written and generally easy to follow. It provides the right intuition and effectively builds up motivation where needed. The related work thoroughly covers existing work in the area.  
2. **Strong and Extensive Results**: The proposed method performs strongly against competitive baselines and it can have significant advantages in settings where the assumptions of the work are satisfied. The paper also has a comprehensive set of experiments and analysis to support its claims. Notably, the paper has numerous ablations to understand the importance of the different components of the proposed method, which was enjoyable to read.

### Weaknesses
1. **Limited Applicability**: The presented method assumes access to object-centric maps, low-level behavior policies and discrete space for attributes. Many RL environments do not provide access to all of the above, and while it is possible to learn these policies/maps, it might require a lot of overhead. Specifically, the requirement for pre-trained low-level policies is a significant limitation. In many complex environments, acquiring a sufficient set of competent low-level policies can be as challenging as solving the original task. The paper does not sufficiently address the practical cost and scalability of learning these policies, particularly in scenarios with a large number of objects and attributes, where the number of required low-level policies could become prohibitively large. Furthermore, the assumption of discrete attributes limits the applicability to many real-world robotic domains where attributes like position, speed, and orientation are continuous.
2. **More clarity in results**: The paper does not do a good job of introducing the baselines and only describes them superficially in the main paper. More detailed descriptions will help increase clarity. It is difficult to assess the true novelty and advantage of MEAD without a deeper understanding of the baseline methods, including their specific assumptions, limitations, and implementation details. This lack of clarity makes it difficult to pinpoint the exact source of MEAD's performance gains.

### Questions
1. The underlying assumptions of Section 4.1 need to be clarified further. If Dreamer and other baseline policies also assume access to these behaviors and operate in the same abstract MDP, then what are the most likely for the differences in sample efficiency. Inference for MEAD is done using Dijkstra's, how is it done for the other methods? Some analysis of the results in *Section 4.1* would be helpful . 

2. In general, it would be useful to have 2 sentence descriptions of the baseline methods or a table that shows the high-level differences between MEAD and baselines (access to behavior policies, abstract world model, inference-time strategy, etc.,). This will help increase clarity as currently it is a bit difficult to keep track of the differences. 

3. In the transfer experiments, Dreamer and other baseline struggles, and the authors hypothesize that this may be due to a distribution shift. Why does MEAD not suffer from a similar distribution shift? Does this have to do with the discriminative model it learns or because of other assumptions in the work. 

4. Section 4.3.1 discusses learning all low-level behaviours. However, I imagine that in most environments, the number of behaviors is extremely large ( $N*m$) and most of the them are incompetent. How much overload does this actually add in practice? What are the total number of low-level policies learned and what fraction of the behaviors are competent (success probability above some threshold)? What are the cumulative training steps (and wall-clock hours) spent in learning these behaviors, and how do they compare to the metrics for the world-model training? 

5. How do you expect this method to perform when attributes are continuous (eg., speed, position, etc.,)? Continuous attributes can be commonly found in many robotic domains, and this work relies on having a discrete set of states.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Summary: The authors propose a method to perform exploration and planning in an abstract MDP which they denote as Ab-MDP. 
This assumes the  a set of abstract states is given, where the abstract state consists of an item id and a specific attribute for the object. The authors define as a competent behaviour, when the corresponding attribute of an item changes in an admissible manner within k steps. The authors train a forward model that predicts the probability i.e. the next 
possible state from the competent behaviour. For finding the correct set of behaviours, MCTS together with a count based intrinsic reward is used. During inference time, the behaviours can then simply be found
by applying the Dijkstra algorithm on the probabilities of the competent behaviours put out by the forward model. The authors show that their model trained on the Ab-MDP outperforms methods trained on a low-level MDP as well 
as known model-based methods such as Dreamer on the Ab-MDP. 

Overall, I find the proposed abstraction an interesting and necessary view for exploration and policy learning in reinforcement learning. However, I feel that this work makes very strong assumptions on the needed abstractions for the proposed Ab-MDP, being tailored to the tested environments. 
One thing that would mitigate this is a discussion on how the proposed item id, item attribute abstraction can be a general representation for other problems. For instance the attributes (in world, standing on, in inventory) may be meaningless in other environments or be a level of abstraction 
That is too coarse to learn a good policy. How do we choose a good level of abstraction? Or what are desirable attributes that may allow for learning a good policy in most cases? I think this is important to make the Ab-MDP formalism more generalisable.

### Strengths
- Learning from more complex and abstract behaviours is an important problem in reinforcement learning, especially since the current focus so far as the authors state is mainly on problems that can be solved without much planning.
- The authors propose a straightforward architecture to explore and plan from discrete sets, i.e., abstract states showing they perform better than models that are not tailored to this abstract MDP.
- The paper is well written and the provided illustrations help in making the method understandable. I also found the ablations to be insightful justifying the components of the method.
- I think the results are promising, showing that the definition of a problem can be just as important as the underlying methods to solve it.

### Weaknesses
 - The paper makes a lot of assumptions about the nature of how attributes and behaviours of the states are encoded. While a thorough explanation is provided for the given environments, it seems unfeasible to do this exhaustively for more complex environments.  I feel there needs to be a more general analysis of what constitutes an item attribute, I.e. a good abstraction level for an Ab-MDP.  In my view, when defining a new framework such as a variation of an MDP, it should define a general way to see the MDP that either is a useful abstraction or is tailored to a specific set of problem. While I see that the authors attempt this, it seems more that the authors restrict the MDP in a specific way to work with the given environments.

- At inference time, the authors rely on Dijkstra to plan towards a specific state with their trained forward model. While this seems feasible for static environments, it seems less feasible for procedural environments, where, e.g., the position of objects could change. At the moment it seems to me that with the current environments the forward model has to learn all possible combinations of item id and item attributes. Could you illustrate how performance degrades w.r.t to how much the forward model is trained, i.e., how much the encoder overfits to the environments?

- In the end, the authors perform a lot of manual feature engineering to make both environments fit in the Ab-MDP paradigm. In this way the contribution becomes really about learning a good model for this feature engineered solution. Although I do value the attempt of a world model paradigm that is based on discrete states (see positives).

### Questions
- How do you train Dreamer-v3 on the proposed environments? I would assume performance to be worse for the proposed Ab-MDP since for instance the latent space bottleneck in Dreamer is tailored to continuous and not discrete states.

### Soundness
2

### Presentation
3

### Contribution
2
