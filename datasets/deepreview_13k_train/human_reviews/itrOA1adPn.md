# A computational approach to visual ecology with deep reinforcement learning

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Animal vision is thought to optimize various objectives from metabolic efficiency to discrimination performance, yet its ultimate objective is to facilitate the survival of the animal within its ecological niche. However, modeling animal behavior in complex environments has been challenging. To study how environments shape and constrain visual processing, we developed a deep reinforcement learning framework in which an agent moves through a 3-d environment that it perceives through a vision model, where its only goal is to survive. Within this framework we developed a foraging task where the agent must gather food that sustains it, and avoid food that harms it. We first established that the complexity of the vision model required for survival on this task scaled with the variety and visual complexity of the food in the environment. Moreover, we showed that a recurrent network architecture was necessary to fully exploit complex vision models on the most visually demanding tasks.  Finally, we showed how different network architectures learned distinct representations of the environment and task, and lead the agent to exhibit distinct behavioural strategies. In summary, this paper lays the foundation for a computational approach to visual ecology, provides extensive benchmarks for future work, and demonstrates how representations and behaviour emerge from an agent's drive for survival.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Motivated by the evolution of animal vision, this paper trains agents in a foraging task with deep RL, in which the complexity of the tasks is varied based on the visual complexity of the food images. The most complex food representations were based on CIFAR-10 images. In contrast to many other deep RL domains, agents are only rewarded for surviving. The results show that more complex visual complexity requires more complex vision models. An interesting observation is that for most complex tasks, recurrent network architectures were necessary. Additionally, the authors show that different network architectures learn different representations of the environment.

### Strengths
- Interesting idea to use recent advances in DNN to study visual ecology
- Since most neural networks for image recognition are purely feedforward it is an interesting result that recurrence facilitates object discrimination on visually complex tasks How is it using the recurrent dynamics? 
- Section 3.3. in particular presents an interesting investigation into how the neural network architecture shapes the reward system of the agent

### Weaknesses
 - My main issue is the comparison of a simple CNN to an animal vision system, i.e. "We modeled the CNN after the early mammalian visual system: the base layers were grouped sequentially into the photoreceptor (PR), bipolar (BP), retinal ganglion cell (RGC), lateral geniculate nucleus (LGN), and primary visual cortex (V1) layers.” As far as I understand, it’s just a different number of channels and kernel sizes? Naming the different layers in a network after biological brain regions does not directly make them more biologically realistic.
- Environments in nature are much more complex than the ones proposed in this paper. To study visual ecology, it seems our agent environments need to be more complex as well.
- There is a lot of related work in the evolutionary community, which isn’t mentioned, where survival is the only reward mechanism. 
- In conclusion, I would argue that a computational framework on visual ecology has to go beyond one experiment/domain with a slight variation on a deep RL setup

### Questions
- How would a model perform that is not "based on" the mammalian visual system?
- How realistic is the vision model when compared to animal vision?
- In nature, adaptation is a result of evolution and lifetime learning. Wouldn’t it be important for this research to combine both adaptation mechanisms in some way? In particular, the evolution of plastic neural networks with Hebbian learning rules could be relevant here.

### Soundness
2 fair

### Presentation
2 fair

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
This paper develops a simple environment off of ViZDoom that studies the problem of how neural net architectural choices affect performance of varying-complexity visual tasks. Authors develop 4 visual tasks that each require a different level of discriminative image processing capacity to perform well. Each task has objects, which are all placed as vertical images atop a 3D-pixelated plane, and images are classified into 10 different satiety scores, {-25, -20, ..., -5, 10, 20, ..., 50}. All tasks involve choosing an action at each timestep (forward/stationary/backward) in a specific direction (left, right, center) to avoid negative-satiety-score objects and make contact with positive-satiety-score objects to prevent satiety from falling to 0, which kills the agent. The paper calls this “visual ecology.”

Authors analyze the effect of architecture and hyperparameters on the lifespan of the agent in each of the 4 tasks, finding a loose correlation between larger kernel count and improved performance. RNNs performed better than fully connected networks on image embeddings, and inputting the satiety score allows the learned value function to more stably track the actual satiety value.

### Strengths
- An interesting problem to study: how environments affect visual processing.
- Did a thorough set of experiments given the environment’s capabilities.
- Writing mostly made sense and was clear throughout.

### Weaknesses
### Overall
(A1) Paper overall seems geared to a slightly less technical audience than ICLR. For instance, describing each conv layer as a different region of the brain (Section 2.1) seems like a weird thing to do, at least in the AI community. Why is the 4th conv layer analogized to the lateral geniculate nucleus, for example? What is the basis for creating these mappings between conv layers and mammalian brain regions? The paper does not provide sufficient justification for these analogies, which seem out of place in a machine learning context.

(A2) Additionally, some results are presented as interesting by the authors, but to me seem relatively straightforward and expected. For instance, including the input satiety into the architecture should obviously improve performance. The paper does not adequately explore the nuances of this improvement or compare it to other methods of incorporating state information.

(A3) Related work section should be much more substantial. Have prior papers studied “visual ecology” or done analysis on neural vision architectures when given an environment the agent must survive/do tasks in? It is hard to evaluate the contributions of this paper without a solid summary of previous work in this area. The lack of a thorough literature review makes it difficult to assess the novelty and impact of the proposed approach.

### This paper is mainly limited in its analysis by an overly simple environment design.
(B1) Based on Figure 4C, it seems like satiety decreases at a constant rate, no matter what action the agent is taking. This seems undesirable, as animals expend different amounts of energy depending on different actions. For instance, being stationary should be much less draining on satiety than moving. This simplification limits the realism of the environment and the generalizability of the results.

(B2) Environment lacks interesting actions beyond moving in different directions or staying put. Additional simple actions may make the environment much more interesting, such as rotating field of view without changing (x,y) position, and needing to perform some manipulative action (such as triggering a set of discrete actions, such as “pulling vegetables out of the ground,” before being able to consume them). These additional actions can also have different satiety costs to them. The limited action space restricts the complexity of the learned behaviors and the insights that can be drawn from the study.

(B3) Environment does not accurately model effects of satiety on actions. Decreased satiety should have a harmful effect on the agent being able to take actions. A satiety=1 agent should not be as effective at moving around as a satiety=100 agent. Under this situation, it would be cool to analyze the satiety value at which the agent is most effective at finding food, since it would tend to be more stationary at higher satieties and tend to be less effective at moving around at lower satieties. The absence of this effect makes the environment less realistic and limits the potential for interesting analyses.

### The main claims in the paper could be better analyzed and argued.
(C1) First abstract claim: “The complexity of the vision model required for survival on this task scaled with the variety and visual complexity of the food in the environment.” This may sound trivial, but authors should define model complexity. Is model complexity only dependent on parameter count? That seems inadequate, since a huge, deep feed-forward network with the same parameter count as a CNN or an RNN should still not be as “complex” due to the inductive biases encoded in the latter two networks. Some of the author’s experimental choices for looking at complexity, such as focusing a lot on number of channels, is probably misguided, since increasing number of channels after a point is known to saturate network performance, as Figures 2D-F show. Things like residual connections, kernel dimension/size, and number of conv layers will probably make for more interesting graphs. The paper needs a more nuanced definition of model complexity and a more comprehensive exploration of architectural parameters.

(C2) Second abstract claim: “recurrent network architecture was necessary...for visually demanding tasks.” This claim makes sense from Figure 2C, but I do not feel like it is well-substantiated. For instance, one could feed the current image as well as the last $k-1$ images into the CNN, either stacked channel-wise or arranged as an $(m, n)$ array of images, such that $k = m\times n$. This would not involve the network being recurrent, but still captures information in the previous $k-1$ observations, and it is possible that this does comparably to RNNs. This claim also might not hold if transformers were used as the architecture. The paper should explore alternative architectures that can capture temporal dependencies before making strong claims about the necessity of RNNs.

(C3) Third abstract claim: “Different network architectures learn distinct representations of environment and task, leading to different behavioral strategies.” Agent behavior was better investigated in the results, but not necessary the “distinct representations” part of this claim, though there was Figure 4C which showed the different value functions. One suggestion here is that it would be better to revise Figure 4B and 4C, for instance, to show the sensitivity of all 4 methods of $\hat{V}$ on the same image observation at the same location in the environment, so that readers can see the “distinct representations” in image space as well as in value space. The paper needs a more thorough analysis of the learned representations, going beyond value functions to directly compare the internal states of different architectures.

### Questions
1. How would behavior have changed if there were no drive for survival, but just a drive for collecting high reward (without a limit of 100)?
2. Suggestion: Authors should compare their designed environment with Fruitbot in ProcGen (https://github.com/openai/procgen#environments), where an agent also tries to get good objects and avoid bad objects.
3. What was the motivation behind choosing Gabors as one of the tasks? Visually, it seems to be the most contrived of the 4 tasks.
4. Are object positions in the environment randomly initialized?
5. What was the mean distance (in terms of optimal number of actions to reach) between each positive-satiety object and its closest positive-satiety neighbor? What was the actual distance traveled by the agent? May be good to measure this. This would be similar to Figure 6’s “Wasted Nourishment” but would instead be measuring “Wasted actions.”
6. Was each environment initialized to have an equal frequency of positive and negative satiety objects?
7. How was the satiety inputted into the network? Was it normalized to be a value between (0, 1)? One could try inputting the satiety into the CNN directly with FiLM layers (https://arxiv.org/pdf/1709.07871.pdf) and see if this increases the effect of input satiety over non-input satiety architectures. Also, why was the input satiety concatenated for the second FC layer instead of the first?
8. Precisely define the reward function. Section 1 says it is “the survival of the agent,” but does that mean it is a sparse 0/1 reward, or is it a constant +1 for all timesteps the agent is alive, and 0 else?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, the Authors set to study how differences in environments pose different requirements for neural architectures enabling vision and decision-making. To this end, they have implemented a 3D simulation of a foraging task where agents had to collect positively rewarded objects and avoid negatively rewarded objects. The agents comprised of a CNN to process pixel data and an actor-critic RL module for decision-making; they were trained end-to-end using the PPO algorithm. The Authors varied the architectures/inputs of the agents and compared their performance in environments with varied complexity of visual stimuli.

### Strengths
The text is well-written and easy to follow.

The description of the experiments is sufficiently detailed.

The question posed by the Authors is interesting and important.

However, the means used to address the question appear insufficient (see below).

### Weaknesses
My main concern regarding this work is that the entire study is conducted on a (particular implementation of) an artificial system, only somewhat paralleled to the brain, so all the results may end up being specific to this system and may not generalize beyond it. Should such experiments be conducted with real-life animals representing different “complexities” of neural processing, we would be able to learn something about real-world neurobiology. Should the models explicitly contain and consider particular biologically relevant architectural choices, we could be able to learn about the (focused) impacts of such. In current settings, sadly, the results relevant for a (generic) CNN and PPO may not inform us about such things.

My secondary concern is that I do not agree that end-to-end processing is necessarily beneficial for learning the optimal representations in submodules of the neural network. Specifically, for the longest time, it’s been an ongoing debate with no clear outcome. The examples include audio processing (where SOTA was switching between using mel-spectrograms, then deep-learning representations such as the ones in wav2vec, then again considering mel-spectrograms), vision processing (e.g. using feature-based pre-alignment before training the triplet loss in facial recognition), and control (where control submodules are trained end-to-end, e.g. in quadruped robots with manipulators, but vision models are separately pretrained). Related to this point, I think that the aforementioned cases are relevant and need to be discussed in the paper.

My ternary concern follows that, in this specific work, the end-to-end training may be unnecessary, increasing the training time but, potentially, not providing new insights. In the specific case of foraging, most of the works successfully operate on simple state representations, reducing the computational time from months on a GPU cluster to seconds on a laptop. I am familiar with only one work using 3D simulation for a foraging task but, likewise, I didn’t find their case well-argued. Either way, if there is indeed a benefit of using an end-to-end model in the current framework, it would make sense to highlight this benefit via a baseline analysis where the blocks of the same model are trained separately.

Lastly, if focus on different submodules of the proposed model, the results do not seem surprising. Indeed, more complex architectures are needed to distinguish more complex stimuli (e.g. texture in MNIST digits as opposed to color in apples). Surely, RNNs have the capacity to embody more complete information about the state, compared to feedforward architectures, departing from Markovian task formulation and enabling longer-term planning. These results are known in the respective fields, and the related literature seems relevant enough to be included/discussed in this paper. The other results, such as agents slowing down before stimuli, are interesting but may be specific to the proposed framework – unless proven otherwise.

Overall, while the results are technically correct and well-described, the concerns above sadly preclude me from recommending the paper to be accepted to the ICLR at this point.

### Questions
Minor:

-page 2: Merell et al modeled a rat, not a mouse.

-page 3: “the reward at every frame was equal to the current satiety of the agent”. This reward shaping seemingly contradicts an earlier statement that “In our framework we reduced the reward function to the survival of the agent, and avoided further fine tuning of the reward” (page 1).

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper trains agents to survive in 3D environments where survival depends on food gathering (and avoidance of harmful items). The appearance of food items can vary in complexity, from two-color items to CIFAR10 classes. Various type of agent architectures are compared, including feedforward vs recurrent, with or without an input for satiety, and linear vs nonlinear activations.

Recurrence and satiety inputs are found to consistently improve performance. However, network size seems to have a very modest effect across conditions, except perhaps for RNNs (judging from Figure 2).

The authors demonstrate that recurrence is used at least in part specifically for object discrimination, and that the agent's learned value function is influenced by both food countdown and satiety.

### Strengths
- The experiment is rather interesting in itself.

- The results, such as they are, seem well supported.

- The paper is well written, though some information is missing - see below.

### Weaknesses
 - The results are not exactly earth-shattering. More difficult tasks seem to benefit from more complex architecture and additional inputs. If anything, the surprising result is the *low* impact of network size on performance (Figure 2).

- Some clarifications are needed, see below.

- Although the architecture is reasonably well-described, the training itself is not, with little detail except for a mention of PPO. E.g. what is the reward function, exactly?

-  From the Discussion: "In particular, we demonstrated how recurrent brains attended to latent variables beyond the agent’s hunger and the immediate presence of food." - I'm sorry, I missed that part. Can you point out more explicitly where this is shown in the paper and what "latent variables" are "demonstrated" to be attended to, beyond satiety and food items? I agree that this would be quite interesting.

- What's an "ELU" nonlinearity?

### Questions
- Although the architecture is reasonably well-described, the training itself is not, with little detail except for a mention of PPO. E.g. what is the reward function, exactly? 

-  From the Discussion: "In particular, we demonstrated how recurrent brains attended to latent variables beyond the agent’s hunger and the immediate presence of food." - I'm sorry, I missed that part. Can you point out more explicitly where this is shown in the paper and what "latent variables" are "demonstrated" to be attended to, beyond satiety and food items? I agree that this would be quite interesting.

- What's an "ELU" nonlinearity?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
