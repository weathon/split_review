# LLM-Mediated Guidance of MARL Systems

- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 3, 6, 6, 3

## Abstract
In complex multi-agent environments, achieving efficient learning and desirable behaviours is a significant challenge for Multi-Agent Reinforcement Learning (MARL) systems. This work explores the potential of combining MARL with Large Language Model (LLM)-mediated interventions to guide agents toward more desirable behaviours. Specifically, we investigate how LLMs can be used to interpret and facilitate interventions that shape the learning trajectories of multiple agents. We experimented with two types of interventions, referred to as controllers: a Natural Language (NL) Controller and a Rule-Based (RB) Controller. The NL Controller, which uses an LLM to simulate human-like interventions, showed a stronger impact than the RB Controller. Our findings indicate that agents particularly benefit from early interventions, leading to more efficient training and higher performance. Both intervention types outperform the baseline without interventions, highlighting the potential of LLM-mediated guidance to accelerate training and enhance MARL performance in challenging environments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This article presents a method for solving MARL tasks by inserting vectorized observations from the environment into an LLM prompt template and obtaining decisions from LLM mediators in two different ways (RB and NL). The aim is to leverage the reasoning and planning abilities of LLMs to assist in completing the fire extinguishing task in an environment called Aerial Wildfire Suppression.

In the rule-based method, the LLM mediator takes a prompt encoded with environment observation vector as input and outputs high-level actions for the environment. While, the natural language method allows the LLM mediator to output high-level actions in the same format by taking a natural-language strategy generated from the Strategy LLM, which uses an input prompt containing partial observations.

### Strengths
This article claims that the novelty lies in using LLM as a mediator to intervene between the action policy and the environment, dynamically. Especially, in the Natural-language intervention method, the prompt-encoded environment features are fed into a Strategy LLM and then the natural language outputs are fed into the LLM-Mediator for real-time action policy.

The writing style made this article easy to read and understand.

### Weaknesses
1. **Lack of novelty.** 

As mentioned in strengths, what this article claims as novelty is not quite robust. The novelty from my side is: translating prompt to natural language strategy and then translate it back to formatted expression. Embedding the environment information into LLM prompt has been studied by a lot of works in different ways. Simply applying this idea to multi-agent environment, as one of the "centralized training and execution (CTE)" methods, does not contribute to this area.

2. **The technical part is not detailed enough.** Besides the figures and the corresponding demonstration in Section4, it seems nothing else. 

a) How does this method train policy with MARL using the two LLMs(Pharia-1-LLM-7B-control-aligned and Llama-3.1-8B Instruct)? How do you collect the data for MARL? How is the learned RL policy used through this LLM-Mediator framewrok?

b) Why does this article choose CTE but not others, like "centralized training and de-centralized execution (CTDE)"? Any insight behind the choice?

c) In which part of multi-agent envrionment does this method improve? Do the agents collaborate better with each other?

3. **Evaluation part is short and not convincing.**

a) From Figure9 and Figure10, the performance of RB and NL does not seem significantly better than what this article claimed at line428 "significantly enhance agents’ performance in complex environments like AWS". 

b) Only one benchmark may not be enough. The authors should show the robustness for the method among different kinds of environments.

c) Selecting 'No Intervention' as the only baseline is not convincing.

4. **This article does not allocate a reasonable length to each section.** 

There are too much introduction to the environment AWS and the discussion of "LIMITATIONS AND POTENTIAL IMPACTS", making sections 4, 5, and 6 too short for detailed demonstration.

### Questions
See above in "Weaknesses" part.

### Soundness
1

### Presentation
3

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
In this work, the authors propose introducing LLM-mediated interventions to support multi-agent reinforcement learning (MARL) systems. In particular, the authors propose two separate strategies (i.e., rule based, natural language) designed to map linguistic specifications to agent instructions. The rule based approach is implements a more rigid protocol (e.g., "go to the closest fire") while the natural language approach involves prompting an LLM to develop a more dynamic strategy. The authors propose a novel  Aerial Wildfire Suppression (AWS) MARL environment to benchmark their approaches and report experiments indicating that the proposed interventions (may) increase reward over a no controller baseline.

### Strengths
### Presentation
The authors provide a clear and polished description of their proposed system and the problem that it solves. I was able to easily follow the flow of ideas being presented throughout the work, and found the visual illustrations of the AWS system helpful. 

### Motivation
The problem that the authors study --- using Natural Language Instructions to coordinate multi-agent systems --- is well motivated and compelling. Generally, there is an opportunity for natural language specifications to improve the adaptability of coordination of agents interacting in an environment. 

### Replicability 
The authors provide code for replicating their study design and experiments.

### Weaknesses
### Novelty
My primary concern with this work is that the novelty of the proposed framework is unclear.

The authors claim that no existing systems support the use of LLMs for MA learning systems (line 43). However, recent work has studied this problem (see Sun & Huang, 2024 and references therein for a recent overview). Additionally, while the authors claim that the proposed AWS environment has more complex environmental dynamics than prior work (i.e., C1 on line 110), it is unclear how the proposed benchmark differs substantively different dynamics from existing simulation environments such as Minecraft (e.g., Wang et al., 2023).

Further, the rule-based and natural language controller implementations, while useful points of comparison, appear to be engineering system implementation efforts as opposed to research contributions. The authors also mention this in the statement of contributions C1, explaining “We implement a novel *system*.”



### Experimental Evaluation
Based on the current experimental results, I am unable to make an assessment as to the proposed LLAMA/PHARMA interventions over the no intervention conditions. In particular, the method used to construct statistical uncertainty intervals is not reported, and the intervals overlap over time steps. Additionally, the current performance results do not indicate a robust reward trend over time steps.

On a more minor note, updating the coloring to shades that are easy to distinguish in Figures 9 and 10 would be helpful.

Furthermore, to further validate the proposed approach in the future (i.e., rule-based and natural language controller generated interventions), it would be helpful to provide a comparison against existing MARL approaches and compare across additional environments. Given the current results, it is unclear how well the provided results compare against other MARL frameworks or generalize to different environments.

Wang et al., Voyager: An Open-Ended Embodied Agent with Large Language Models (http://arxiv.org/abs/2305.16291)

Sun & Huang, LLM-based Multi-Agent Reinforcement Learning: Current and Future Directions (https://arxiv.org/pdf/2405.11106)

### Questions
1. How does the design of the proposed framework differ from prior MARL systems, particularly those that leverage natural language instructions? 
2. How does the performance of the proposed NLI and Rule-Based controllers improve upon existing MARL approaches, particularly those cited in response to question one above? 
3. What specific characteristics in the AWS evaluation system differ from prior MARL evaluation environments? Why might future work use the AWS framework over these alternatives?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This empirical study paper investigated how LLMs can be used as a controller to intervene the learning process of MARL. The main contributions of this paper are evaluating the capability of two representation of prompts, referred to as rule-based controller and natural language controller. The later one can give some insights into the potential performance of human-in-the-loop training for MARL. The experments were conducted on a complex environment called Aerial Wildfire Suppression, and showcased the effectiveness of intervened MARL learning process by LLMs.

### Strengths
1. From the perspective of an empirical and engineering work, this paper seems like an original work, as I cannot find duplicated counterparts online. Although the paradigm of intervening MARL learning process is not a completely new idea, the leverage of LLMs to produce the interventions should be novel.
2. The motivation of this paper is clear, and the descriptions of appraoches and experimental platforms are comprehensive. This paper well took the advantage of one additional page to provide illustrative figures, which can aid in understanding the paper.
3. The overall quality of this paper is good, which is evident in the complete discussion of limitations of the proposed paradigm and its gap to the realistic applications. The general style of this paper should lie in an empirical study paper, based on which I think it is an examplar that include every component it should involve. Furthermore, this paper has released the code, and the details of experimental settings is evident to reproduce the results.
4. As the prevalence of LLMs, the research trend and flavour in many fields have been influenced, which is an inreversible situation. To adapt to this tendancy, the combination of LLMs and MARL is reasonable, if this can really help improve the performance or close the gap to the realistic application. The trial made in this paper well shedded light on the possibility of this combination, which is thrilled to MARL reseachers such as myself. In this sense, I believe this paper studied significant work.

### Weaknesses
1. This experiments lack some instrucmental baselines to verify the importance of LLMs to generate interventions, such as the baseline which replaces the LLMs by a reinforcement learning agent (learner). I believe with this comparison, the result of this paper can be more convincing.
2. As for the statement in line 499-501 that "The findings suggest ... in complex environments," I wonder if this claim is certainly correct, as the computational cost from LLMs is known to be expensive also. If the cost induced by LLMs can offset the cost of extra costs led by explorations is deserved to investigate further.
3. Although this paper have made a good description about its approach and experimental results, the insightful analysis is lacking. For example, to most of MARL researchers, the most prominent question could be what mechanism the LLM-based controller has learned. It is better if this paper can demonstrate and analyze some intervention strategies learned, other than the numeric results.
4. As for a paper to be published on top venues, I believe the demonstration on the only one setting as extinguishing burning trees is not enough to convince others that the proposed approach is effective. To alleviate this weakness, I suggest you may do more experiments on other settings with different objectives.

### Questions
Please see weaknesses and give a reply to those concerns.

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
5

### Summary
This paper investigates how LLMs can be used to interpret and facilitate interventions that shape the learning trajectories of multiple agents. The experiments including two types of interventions, referred to as controllers: a Natural Language (NL) Controller and a Rule-Based (RB) Controller. The NL Controller, which uses an LLM to simulate human-like interventions, showed a stronger impact than the RB Controller. This paper indicates that agents particularly benefit from early interventions, leading to more efficient training and higher performance. The experiments were designed to compare agents’ performance under three different intervention setups: No Controller, RB and NL Controller. Both intervention types outperform the baseline without interventions, highlighting the potential of LLM-mediated guidance to accelerate training and enhance MARL performance in challenging environments.

### Strengths
1, This approach moves beyond static curriculum-based methods, providing real-time, adaptive interventions that respond to the evolving states of agents and environments.

2, The results demonstrate that interventions, especially during early training, accelerate learning to reach expert-level performance more efficiently.

3, The authors provide a thorough comparison between different types of controllers (RB, NL, and no intervention), making it clear that LLM-mediated interventions provide substantial performance improvements. And also this paper shows the different results by using different LLMs, which indicates that this method can be utilized with different LLMs.

### Weaknesses
1,Scalability: The experiments are all conducted using the default settings of 3 agents. Given that the paper aims to address multi-agent scenarios, it would be more convincing to demonstrate the method's performance with a larger number of agents, such as 4, 5, or 6 agents, to showcase its scalability more effectively. The current setup does not sufficiently explore the potential for increased complexity and emergent behaviors that can arise with a larger number of interacting agents. Specifically, the coordination challenges and communication bottlenecks that might occur with more agents are not addressed.

2,MARL Method: The experiments exclusively use Proximal Policy Optimization (PPO) as the base MARL algorithm. To strengthen the findings, it would be beneficial for the authors to implement and evaluate the method using other MARL algorithms like QMIX, VDN, MADDPG or other MARL methods, providing a broader assessment of its effectiveness. The reliance on a single algorithm limits the generalizability of the results, as different algorithms have varying strengths and weaknesses in different multi-agent scenarios. For example, value-based methods like QMIX might reveal different insights compared to policy gradient methods like PPO.

3,Test Environment: The testing is limited to the Aerial Wildfire Suppression (AWS) environment. There is no evaluation demonstrating the generalizability of this method to other environments, such as StarCraft II, Hanabi, or other established multi-agent benchmarks. Expanding the experiments to include these environments would provide stronger evidence of the method's versatility. The AWS environment, while complex, may not capture the full range of challenges present in other multi-agent tasks, such as those involving strategic planning, negotiation, or imperfect information.

### Questions
The method is clear and it does make sense to me. Like I state in the weaknesses, if there would be more results to prove the performance of this method, it would be more convincible.

Moreover, there are a lots of works of using LLM to do reward generation to help reinforcement learning training. What is the advantage of proposed method compared to reward generation by LLMs? Such as Text2reward, DrEureka, Reward design with language models.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates a method to use a pretrained LLM as a central controller, to guide otherwise decentralized MARL-trained agents. The environment is a simulation in which three drones have to contain wildfires, with observations consisting of a feature vector and a low-resolution RGB rendering of the drone's surroundings. The mediation approach is fairly simple, with either "soft-coded" (parametrized) rules, or natural language strategies being converted into actions, which individual agents are then forced to take. The paper's central claim is that this simple approach can significantly improve the agents' performance on complex tasks.

### Strengths
The paper is generally well-written and understandable. The overall idea of using an LLM to facilitate coordination is very interesting and likely to be valuable in the near future, as foundation models become more and more widespread and capable.

### Weaknesses
My main issue is the experimental validation of the approach, seeing as this is an entirely empirical paper with no significant theory.
In short, in the current state of the paper, I'm largely unconvinced that this method actually does provide significant benefits, and if so, how large they are.
This is largely based on the results presented in Figures 9 and 10:
1. The graphs are somewhat under-explained. They have very large shading, which is not explained in the paper - I'd assume it's a measure of dispersion, in this case, probably the full range of values between the 10 averaged runs (though it might be standard deviation/error?). There seem to be frequent outliers, there's significant overlap between all lines, and the upper bounds (and in some cases - the averaged (?) lines) are oddly non-monotonic. For example, there seems to be at least a single run with Llama 3.1 intervention at the very beginning of the training, that outperforms the final average performance. This might point at insufficiently tuned hyperparameters, unstable performance, or even an insufficient sample size.
2. The baseline seems undertuned. The environment seems to be relatively new, without a well-established baseline performance, so it's hard to tell whether it's really that difficult for regular PPO, or if better hyperparameters could significantly change the shape of the graphs.
3. The training doesn't seem to have converged - the performance of each method keeps increasing on average, although this may very well be significantly impacted by the statistical noise, so it's rather hard to tell.
4. Rule-based performance seems to largely match the natural language mediator - we see that also in Table 1, which also clearly shows the massive scale of the uncertainty, with uncertainty values often exceeding the averages. The role of the LLM in the rule-based system seems to be largely insignificant - it is merely converting structured data into natural language, for it to be converted back into structured data by the LLM controller. This is somewhat supported by the fact that RB performances for Llama 3.1 and Pharia 1 are very close. So if the results we get are very close between the rule-based system, and the LLM-based natural language system, why bother with the LLMs? We can see LLMs as a proxy for a human operator, but then we're confounding the quality of the LLM's strategy and the usefulness of the extra centralized information itself, plus the transcription fidelity of the controller.

Even if we accept that RB/NL interventions improve the performance over the baseline (which I can still accept on an intuitive level), the comparison hardly seems fair - as far as I understand, no-intervention models have no access to any global information, so they simply do not know where the fire might be if it's outside of their field of vision. Merely pointing them in the right direction would likely boost their performance significantly, and this information can be conveyed through the RB/NL systems.

There is also the question of how interventions affect the training process. As PPO is a (mostly) on-policy algorithm, training it on actions that have been taken due to the mediator override breaks all mathematical validity of the algorithm, at least without some form of e.g. importance sampling. I don't see any discussion of this in the paper, suggesting that those samples were just thrown into the rollout buffer without extra consideration. It is possible that training was performed without interventions, and performances are reported based on separate evaluation rollouts, but this should be stated explicitly in the paper.

Finally, I would really like to see some expreriments

Nitpicks:
- Lines 202-203 - incorrectly formatted citations
- Figure 3 describes both the environment logic ("drop water") and the algorithm itself (controllers), which are (or should be) entirely orthogonal. The algorithm does get its own diagram in Figure 4, but by the time this reader reached it, they already spent some brainpower trying to disentangle Figure 3.
- To get a sense of the complexity of the training, I'd be curious to see the actual wall time duration of the training. Of course this measure depends on many factors, but it's still good to know if it's minutes, hours, or days (or more?)

### Questions
1. What was your approach to hyperparameter tuning, especially for the baseline method (no intervention)?
2. Do you believe it is the case that regular RL algorithms largely fail on this task, as suggested by Figure 9?
3. Did you try running the baseline for a longer time to see whether the final performance here is stable?
4. Do you have any comments on the additional global information given to the RB/NL variants, which is inaccessible to the no-intervention variant?
5. How do you interpret the large uncertainties present in the training curves?

### Soundness
1

### Presentation
3

### Contribution
2
