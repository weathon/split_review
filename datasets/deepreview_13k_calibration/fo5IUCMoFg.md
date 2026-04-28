# Offline vs. Online Learning in Model-based RL: Lessons for Data Collection Strategies

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Data collection is crucial for learning robust world models in model-based reinforcement learning.
The most prevalent strategies are to actively collect trajectories by interacting with the environment during online training or training on offline datasets.
At first glance, the nature of learning task-agnostic environment dynamics makes world models a good candidate for effective offline training. However, the effects of online vs. offline data on world models and thus on the resulting task performance have not been thoroughly studied in the literature. In this work, we investigate both paradigms in model-based settings, conducting experiments on 31 different environments.
First, we showcase that online agents outperform their offline counterparts.
We identify a key challenge behind performance degradation of offline agents: encountering Out-of-Distribution states at test time.
This issue arises because, without the self-correction mechanism in online agents, offline datasets with limited state space coverage induce a mismatch between the agent's imagination and real rollouts, compromising policy training.
We demonstrate that this issue can be mitigated by allowing for additional online interactions in a fixed or adaptive schedule, restoring the performance of online training with limited interaction data.
We also showcase that incorporating exploration data helps mitigate the performance degradation of offline agents. Based on our insights, we recommend adding exploration data when collecting large datasets, as current efforts predominantly focus on expert data alone.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a large-scale empirical analysis of offline model-based reinforcement learning. The main takeaway is that, encountering OOD states at test time is a main reason for test-time performance degradation of agents. In addition, the authors suggest that this issue can be mitigated by allowing for only interactions.

### Strengths
1. The takeaway of this empirical study,  i.e. visiting OOD states causes performance degradation, is clearly presented.
2. The performance of Dreamer-v3 is thoroughly examined in 31 tasks.

### Weaknesses
1 The paper confirms a widely studied issue, but it does not reveal novel insights. I agree that, many standard offline RL algorithms (e.g. CQL), approach the issue of visiting OOD states from the perspective of Q values. But I do not think the issue if fundamentally different for offline model-based RL, since in both case, the root cause is that a neural network sees samples not in its training set. See the question 1 & 2 for my suggestion on improving the novelty of this paper. 

2. Although aimed to provide insights for practitioners, the three benchmarks used in this paper, DMC, Metaworld, and MinAtar, are in fact not very realistic. In consequence, it is questionable if the same conclusions hold when using more powerful simulators (so it is harder to collect "exploratory" data, since trajectories terminate early).

### Questions
1. Since you mention in line 260 that "the paradigm is shifted from ... to the coupling of a world model and a policy network". Could you dissect this coupling? For example, could you provide results of a variant of your Passive agent, which uses the world model of the Active agent but trains its policy from scratch? This is just an example of decoupling the world model and the policy network. Other similar ideas suffice.

2. Could you provide results of Active agent and Passive agent deployed on environments that are slightly different from their training environments? In other worlds, will the superiority of Active agents disappear when their world model cannot accurately predict states?

3. Could you provide results for domains that utilize more realistic simulators, such as Maniskill, LeggedGym, or HumanoidBench?

### Soundness
3

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
This paper examines how different data collection strategies, particularly offline and online data collection, impact the learned world model and policy under the MBRL setting. This investigation is primarily experimental and is conducted using DreamerV3, a state-of-the-art MBRL algorithm. The authors perform extensive experiments across various environments, leading to the following key conclusions:

1.	Insufficient data coverage in MBRL can result in high prediction errors by the model, both in predicting the next state and rewards, on OOD states. Consequently, policies learned from model-generated trajectories may exploit these errors due to the nature of RL.

2.	On-policy samples play a critical role in MBRL. Even with the same sequence of previously collected on-policy training data, minor differences in model initialization can lead to performance degradation. Using purely expert data does not yield good performance either, as distribution shifts occur between the expert policy and the current policy.

3.	Exploration data (or data collected with exploration-enhanced policies) can alleviate issues related to insufficient data coverage. Thus, including exploration rewards during data collection can be beneficial.

Finally, the authors propose two strategies to mitigate performance degradation: incorporating exploration data and adding limited on-policy samples based on the world model loss. While the first approach is straightforward, the second is implemented by monitoring the ratio of world model loss between evaluation and training trajectories. On-policy samples are added once this ratio exceeds a manually set threshold.

Although the paper provides a thorough set of experiments and findings, many of these conclusions have been drawn in prior studies. The primary contribution of this work lies in its experimental validation and in proposing practical remedies for performance degradation.

### Strengths
1.	Thorough experimentation: The authors conducted extensive experiments across various environments, providing strong support for the claims made in the paper through the results.

2.	Clear presentation: The paper is well-organized, with definitions and experimental settings clearly presented, making the paper easy to follow.

### Weaknesses
1.	Lack of novelty: While the paper offers several analyses, many of these insights exist in previous research. For example, the issue of “lack of self-correction causing OOD errors” is a well-known challenge that has been extensively discussed in both offline RL and offline MBRL algorithms [1][2]. Similarly, the use of on-policy samples or exploration data to achieve broader data coverage has been widely studied in the offline (or offline to online) model-free setting [3][4]. Simply extending these methods to the model-based setting does not add substantial novelty. 
2.	Insufficiently effective solution: Despite dedicating a substantial portion of the paper to analyzing issues in offline MBRL methods, the final solution is not effective enough. Whether using exploration data or incorporating on-policy samples, the authors do not provide a principled approach for deciding when and how to incorporate these data. Additionally, the approach relies heavily on hyperparameters in the data strategy, which limits its generalizability across different environments and datasets. 


### Questions
1.	Do the authors have any deeper analysis of the causes and impacts of OOD errors? Currently, most of the analysis either reproduces findings from previous works or directly interprets results without additional insight. A more in-depth analysis beyond compounding error and distribution shift, especially within the MBRL setting, would add value.
2.	Although DreamerV3 is a powerful algorithm, it is unique in its model architecture and algorithmic pipeline compared to other MBRL algorithms. Have the authors conducted any horizontal comparisons across different MBRL algorithms under similar environments or experimental settings? 
3.	The authors claim that the world model loss serves as a pessimistic indicator of performance degradation. However, Figure S2 in Appendix A.3.1 shows that while the world model loss sometimes reflects performance degradation, it can be highly unstable due to its reliance on sampled data batches. Additionally, the scale of the world model loss varies significantly across different environments and model architectures. How do the authors interpret the world model loss when it is unstable or has a relatively small scale?

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
3

### Summary
This work demonstrates the importance of state novelty in offline model-based reinforcement learning and identifies data composition as a key factor in mitigating performance degradation. The findings on mixed exploratory datasets and self-generated data integration provide valuable insights, suggesting an effective directions for enhancing offline agent robustness and adaptability.

### Strengths
1. The paper is overall well written and the main idea is easy to follow. 
2. The authors provide sufficient experimental evidence to illustrate the challenges as well as to demonstrate their proposed approach, which enhances both the performance of Passive agents and the efficiency of the online training process.

### Weaknesses
1. The novelty of the proposed method is limited. The mixed reward function employed relies on an exploration-exploitation trade-off, which is a well-established framework. Specifically, the use of a weighted sum of intrinsic and extrinsic rewards, while effective, does not introduce a fundamentally new approach to balancing exploration and exploitation. For OOD detection, the authors utilize an ensemble approach within the world model, combined with a supervised learning method—both of which are commonly applied in offline RL and lack significant innovation. The ensemble method, while improving robustness, does not address the core challenge of detecting novel states in a fundamentally different way than existing techniques. The supervised learning component for OOD detection, often relying on a distance metric or a classifier trained on in-distribution data, is also a standard practice.

2. The approach appears to require task-specific parameter adjustments (e.g., weights for exploration and the OOD ratio), which suggests limited feasibility and generalizability of the method across diverse tasks. The need to tune these parameters for each new task diminishes the practical applicability of the method, as it requires significant effort and computational resources to identify the optimal parameter settings for each environment. Furthermore, the paper does not provide a systematic way to determine these parameters, relying instead on an unspecified process, which makes it difficult to replicate the results or apply the method to new tasks without extensive trial and error.

3. The lack of pseudocode for the proposed approach limits clarity. The absence of algorithmic details makes it challenging to understand the exact implementation of the method and to reproduce the results. Without a clear step-by-step description, it is difficult to assess the complexity of the approach and to identify potential bottlenecks or areas for improvement. This lack of transparency hinders the adoption and further development of the proposed method by the research community.

### Questions
1.  What is the intuition behind constructing a Tandem agent? Training an offline policy that mirrors the action order of the Active agent seems unusual, especially since such an agent is unlikely to be employed in an offline setting prior to online learning. 
2. How are the parameters selected for each task? The paper mentions deriving upper bounds based on the performance results of the Active agent. Does this imply that the Active agent must be trained first in order to establish the appropriate parameter ranges? Clarification on this process would enhance understanding.

### Soundness
2

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
This paper focuses on the data collection strategy for model-based RL. It is principally concerned with three types of agent: 'Active', which is allowed to interact with the online environment to update its world model (a bit like Dreamer); 'Passive', which samples random data from the replay buffer of the 'Active' agent; and 'Tandem', which receives identical data to the 'Active' agent but has a different initialisation. They show that these three agents have a performance disparity, and subsequently consider some different sampling techniques to improve the fidelity of the world model or the agent performance (such as including exploration bonuses). There is an extensive appendix, largely comprised of additional results.

### Strengths
I found this to be, besides certain confusing sentences, a generally well written and presented paper. That said, I feel it is significantly lacking in contribution. Much of what it says is seemingly obvious or feels like shifting goalposts to fit a narrative.

I provide a list of my perceived strengths of this paper below:
- As stated, this was a generally well written and formatted paper.
- The paper is extensive in its experimentation, covering a broad range of environments and settings.
- The paper is well referenced, and provides good coverage of related literature. In weaknesses I provide a few papers which I believe are missing from the literature review but, generally, the authors have done well to contextualise against prior work.
- I think the paper is well structured, following a reasonable trajectory of 'What we explore -> Some analysis -> Mitigation strategies'
- Defining notation used throughout the paper early, and remaining consistent with plotting colours etc. even when more or less baselines are included, helped make results more interpretable. This holds even to figure 1, which is a nice touch.
- I think the motivation of the paper is good - too often there is a focus on proposing new methods in research, so I appreciate this analytical approach to understand the current deficiencies in model based RL. Asking the question of 'what is the best data collection strategy for 'MBRL' is a good one, though I explain some of my hesitations about this in the weaknesses section.
- Though I would question if **all** the experiments are needed, especially due to their limited reference in text, the authors provide the necessary information for both reproducibility and compute requirements.

### Weaknesses
My principle concern with this work, and what limits me from increasing my score, focuses on its significance; I think there are interesting questions about if this is potentially misguided, which I get into below, but overall my main assessment is that a lot of these findings are quite trivial. For instance, it is well known that training a world model on purely expert trajectories will lead to subpar policies due to overestimation bias in OOD states, and in that situation an imitation learning approach may be more expected. Similar, it should not be a surprise that introducing additional data to the agent via online sampling will lead to better performance.

Below, I cover more specific feedback. That said, I think the researchers behind this work are asking an important question and have clearly put a lot of effort into this project. I am keen to discuss this with the authors in more depth as, while I hold strong conviction after reading the paper, I am open to being persuaded that I have misjudged the work. I apologise that the review has ended up longer than expected, though I think many of the points have a degree of overlap and thus am happy for the authors to respond more holistically to the points I raise rather than going through bullet point by bullet point. 

- I found lines 19-23 in the abstract very confusing. I think part of my view on the misguidance in this work is the flippant use of 'offline' and 'online' to refer to data collection. For instance, in the abstract it says the below, which seems to suggest that the problem with  offline learning is that it collects data online:
> We identify a key challenge behind performance degradation of offline agents: encountering Out-of-Distribution states at test time. This issue arises because the data collected online primarily benefits the online agent by learning from its own mistakes, but it leaves many states unvisited. As a result, the offline agent suffers from insufficient coverage of the state space.
- Another point I feel is not addressed is that an offline dataset is generally colelcted prior to policy learning and, as such, is not designed. The paper focuses on finding better ways to shape offline datasets (eg line 28 in the abstract, adding exploration data), ignoring the fact that an offline dataset is presumably pre-collected and there is not ready access to the online environment to collect more data.
- I think it is misinformed to say current efforts predominantly focus on expert data (line 29) when arguably the most common offline benchmark, D4RL, has random, medium and mixed policy datasets in addition to their robotics data.
- I think there are some missing reference examples; most notably, World models by Ha & Schmidhuber is a seminal MBRL paper. I think a relevant recent paper is The Edge-of-Reach Problem in Offline Model-Based Reinforcement Learning, Sims et al. (2024).
- I am a bit unclear on Figure 1. We are focused on model-based RL here, but there seems to be no demonstration of the world model in figure 1 - just an agent. 
- The explanation of the active agent is very unclear.
- Equation 5 introduces a policy input reconstruction loss, but this does not seem to be used elsewhere in the paper.
- On line 217, it is worth pointing out that Dreamer V3 has the online data collection discussed here. I am not quite sure what the argument is. 
- I am unsure what is means in line 234 onwards:
> Their mistakes are catastrophic, as their world models and thus their policies have their unique fallacies that cannot be corrected by the task-oriented data with limited state space coverage, which is collected by and catered to the Active agent.
- There is a lot of discussion about how the passive agent experiences worse performance than the active agent in section 3.4, but again this seems quite trivial; the agent is not able to interact with the real-world so effectively does not receive any online feedback about its overestimation bias. Just because it is trained on the same data as the active agent, it is obvious that this lack of correction would harm performance; the reason many don't sample online during training isn't because they think it won't help, but because it is impossible or impractical.
-I'm a bit unsure about what is meant by line 300. Again, there is little insight in the fact that the replay buffer trajectories will have a lower reconstruction loss since they make up part of the training signal of the model; this is equivalent to having a higher supervised test loss compared to training.
> However, in our observation, the quality of imagined trajectories for all agents is poor with mean world model loss being more than 5 to 10 times higher compared to trajectories in the replay buffer due to accumulated error in open-loop multi-step predictions, as shown in Appendix A.4
- When considering potential mitigations, I again bring up what I believe to be misguidance in this paper. For instance, I think assuming we are rolling out a policy for collecting offline data to do offline RL with (4.1) can be potentially misguided - in this case we could just do online RL. Instead, I think an assumption in offline RL is that there is a precollected offline dataset that we then have to work with. Similarly, I think the fact that an exploration only dataset underperforms is expected, but I think this hinges on the fact that the dataset size is small.
- In section 4.2, it is suggested that offline data is 'often cheaply available', which seems in conflict with the statement in the introduction that 'collecting expert trajectories is expensive'. Again, it should be no surprise that allowing an agent to interact with the real world will increase performance.

I also raise some very minor points and typos below.
- Lots of the bibliography is incorrectly formatted, seemingly including the names of authors from different papers.
- There are a number of 'bulk references' (i.e., a large number of papers cited in a row) without explanation of what each of these papers are or their relevance to the statement. It would be good to disambiguate between these many references.
- In equation 1, $\pi$ is used on both sides of the equation which is unintuitive. The LHS should be labelled $\pi^*$
- In the explanation of Dreamer, $R_t$ is used to define the critic without definition.
- Pages 8 and 9 have a large amount of whitespace. It would look better to remove this via formatting.
- On line 514, there is a missing space after the full stop: 'best facilitates offline training.In'

### Questions
- I really don't understand how the Tandem agent with the same random seed and exact same data as the active agent could perform worse; a chaotic system is one where a small change in inputs causes large changes at output, but that is not the case here. Can you please elaborate how there could be any difference between the Tandem and Active agent please? Is the only difference here hardware determinism?
- In the discussion of pessimistic indication of performance degradation, I am a bit confused. Is the argument that model loss underestimates performance *degradation* (as in agents perform better than their model loss suggests) or that model loss underestimates performance (agents perform worse that their model loss suggests)?
- Is it not true that you have an offline collected RL dataset, and thus are unlikely to be able to curate this yourself?

### Soundness
2

### Presentation
3

### Contribution
2
