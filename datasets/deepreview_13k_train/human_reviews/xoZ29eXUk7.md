# A Multi-Agent Reinforcement Learning Framework for Evaluating the U.S. ‘Ending the HIV Epidemic’ initiative

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Human immunodeficiency virus (HIV) is a major public health concern in the United States, with about 1.2 million people living with HIV and 35,000 newly infected each year. There are considerable geographical disparities in HIV burden and care access across the U.S. The 2019 'Ending the HIV Epidemic (EHE)’ initiative aims to reduce new infections by 90\% by 2030, by improving coverage of diagnoses, treatment, and prevention interventions and prioritizing jurisdictions with high HIV prevalence. Identifying optimal scale-up of intervention combinations will help inform resource allocation. Existing HIV decision analytic models either evaluate specific cities or the overall national population, thus overlooking jurisdictional interactions or differences. In this paper, we propose a multi-agent reinforcement learning (MARL) model, that enables jurisdiction-specific decision analyses but in an environment with cross-jurisdictional epidemiological interactions. In experimental analyses, conducted on jurisdictions within California and Florida, optimal policies from MARL were significantly different than those generated from single-agent RL, highlighting the influence of jurisdictional variations and interactions. By using comprehensive modeling of HIV and formulations of state space, action space, and reward functions, this work helps demonstrate the strengths and applicability of MARL for informing public health policies, and provides a framework for expanding to the national-level to inform the EHE.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to simulate a real-world optimization problem and propose to solve it under MARL setting due the factored-controller nature of the problem.

### Strengths
Well written background and related work. Clear on the method used (PPO) and the simulation environment. The paper aim to solve a real-world problem, which should be considered a positivity due to its applicable nature, but I'm not entire sure this holds for ICLR.

### Weaknesses
The novelty of the proposed approach is limited, the problem can be viewed as a joint-action problem, solving it as a MMDP, hence viewing it as a factored action problem, does not change the problem and the learning process fundamentally. The simulation itself is also not novel to this paper, and only method (PPO) is used for evaluation. The core issue is that framing the problem as a multi-agent system, while perhaps more intuitive, doesn't inherently introduce a significant algorithmic challenge or novelty. The problem remains fundamentally a Markov Decision Process (MDP) with a large joint action space. The paper lacks a strong justification for why a factored approach is superior to, or even different from, a single-agent approach with a large action space, other than potential scalability concerns. The choice of PPO, while a solid algorithm, does not showcase any novel adaptation or modification to address the specific challenges of this problem. The paper would benefit from exploring other algorithms or modifications to PPO that could better leverage the problem structure.

### Questions
What would be the theory or explanation of the increased performance and why not factor the actions in other ways (or conjunction of jurisdiction) such as separating the action space further into different controllers for testing, treatment and prevention?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a reinforcement learning-based approach to evaluate the effectiveness of several intervention measures to minimise new HIV infections. Throughout the paper the authors formalize the HIV epidemic environment following the principles of RL and show how the framework can be used to tackle new infections.

### Strengths
The paper evaluates the impact of the HIV epidemic within US jurisdictions from a reinforcement learning perspective. This can be good since machine learning methods that model these scenarios can be leveraged to minimise the impact of these serious health concerns. The authors also analyse the impact of specific mitigation measures within their approach in detail, and look at the problem from a multi-agent perspective, which is important since different areas of impact may have different requirements and conditions.

### Weaknesses
Overall, this paper contains several inaccuracies and technical flaws from a MARL perspective. I outline here some points and more questions ahead.

* In section 1 the authors state that "To our knowledge, no prior research has explored dynamic jurisdictional interactions in these models."; while I accept this claim for HIV cases, it is important to note that governmental actions and interventions have been included in cases related to the study of pandemics or epidemics such as COVID-19 [1] or influenza [2, 3]. These are modelled using SIR and SEIR models that are not mentioned in this paper but can also be relevant when it comes to epidemic models.
* In section 3.2: "The MDP can be defined as a tuple"; The MDP reference is missing; also, it is not correct to define an MDP as a system with multiple agents; an MDP is formed by a single agent only, and it can indeed be extended to multi-agent MDPs [4]. The authors should clarify if they are using a Markov game or a decentralized partially observable Markov decision process (Dec-POMDP) instead.
* In section 3.2 it is described that each agent has a different individual observation but figure 1 gives the idea that all of them share the same state since these are represented as $S_t^j$; additionally, if the authors are considering individual observations in their MARL model, the problem should instead be modelled as a Dec-POMDP [5]; an MDP considers a fully observable state. The notation used for the state ($S_t^j$) is also misleading, as it suggests the state is specific to agent j, while the text describes it as a global state.
* In section 3.2 "For each agent j, $a^j$ signifies their set of possible actions": $a^j$ is defined here as a set but ahead we can see that it denotes the action of agent $j$: $a = a^1 	imes ... a^N$. This inconsistency in notation needs to be addressed. Furthermore, the action space definition $a = a^1 	imes ... a^N$ implies a joint action space, which is not explicitly discussed in the context of the MARL approach. It is unclear how the agents coordinate their actions, or if they act independently. I have outlined a few inaccuracies but, generally, the entire section 3.2 needs to be revised since it contains multiple inaccuracies.

Minor comments:
* "The MDP can be defined as a tuple" in section 3.2: missing brackets in the tuple
* Missing brackets in many in-text citations
* Missing full stop at the end of some equations such as (4) or (7)
* Before equation (5) the full stop in "with the following objective." is misplaced

### Questions
1. In section 3.2.1 the proportion of PWH unaware of the infection is used as part of the state; is it possible in real life to know this proportion if people are not aware that they are infected? Does it affect the model if this number is unknown?
2. According to Algorithm 1, each episode is T years long. This means that each time step in an episode is one year; this makes me question whether this is a reasonable choice, since it means that we take only one action per year. Is that enough? during a year many changes might happen and several governmental measures might be needed.
3. It is unclear to me how MARL is being used here when compared to the SARL approach. From my understanding, in the SARL approach, there is a state (as per eq (1)) that describes the conditions of all the jurisdictions within a state (using the average, as stated in section 3.3.2), whereas in the MARL approach we have the same state but each jurisdiction has its own independent values; then, in SARL the actions performed influence the values in the state for all jurisdictions and then in MARL each jurisdiction performs an action that influences only its own state conditions. How are the multi-agent interactions between different jurisdictions integrated here? In order to say that this is following a MARL approach there needs to be some sort of interaction among the agents that will make them cooperate or work together towards some common goal. In the presented approach, I do not see that being done. Even the rewards are said to be given individually and its components only correspond to jurisdiction $j$ (as per eq (3)). This means that each agent is maximising an independent objective on its own, without any effect on the other agents. This sounds like multiple single-agent problems happening in parallel, without any interaction.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a multi-agent model for modeling interventions by different entities in the US to end the HIV epidemic in the US. They find that using MARL in this multi-agent framework yields better policies than using single agent RL and the associated single agent model. As part of this paper, they also provide a concrete multi-agent environment definition for HIV spread and control via interventions. In their environment each geographical jurisdiction is considered as a separate agent to model decentralized decision making.

### Strengths
The authors present a practical use case for deep MARL for a problem that potentially has an important social impact. The paper is well written and the concepts are clearly explained.

### Weaknesses
While the application described in this paper is for real-world use, it is not clear to me how useful this is as the state and more importantly the action spaces are considered to be very small. Also no validation is provided, which is important since this can affect real-world decision making.

### Questions
1. Is the difference between the single agent model and the multi-agent model only one of centralized versus decentralized decision making?
2. Are there situations where the rewards of one agent (jurisdiction) depends on the actions of other jurisdictions?
3. Is this multi-agent environment a fully cooperative one, in which case, this can be modelled as a Dec-POMDP.
4. Since the algorithm is run only for $T$ timesteps, shouldn't the author use a finite horizon MDP framework, where the timestep should also be added to the state?
5. Are there any resource constraints across all jurisdictions that need to be modeled?
6. Is the difference in the performance of the SARL and MARL policies a result of sub-optimality in learning or is it because of some other structural difference between the single and multi-agent environment?
7. How can the solutions be validated? Is there any validation for the environment? What are other precautions to be taken before using these solutions in the real world?
8. In such an environment, how does a baseline policy perform? Baseline policy could be the bestb policy from literature or if nothing is available for this environment, then a random policy could be used.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to achieve the EHE initiative by applying MARL to explore optimal combinations of actions at the jurisdictional level while considering cross-jurisdictional epidemiological interactions. By using the compartmental simulation model and training multiple agents based on PPO, this paper shows the effectiveness of MARL over SARL.

### Strengths
This paper uses recent machine learning tools to solve an important public health challenge of HIV.

### Weaknesses
1. In general, the paper's current writing has many public health terms. Thus, without much prior knowledge of HIV and public health terms, the paper is difficult to read.
2. It is unclear whether a comparable single-agent baseline is used. According to Section 3.3.2, SARL formulation applies $j=1$, so SARL outputs one action every timestep whereas MARL outputs $N$ actions every timestep. If this is true, then MARL outperforming the SARL baseline could be a straightforward result (due to outputting more actions). Instead, a more competitive baseline could be a centralized agent that outputs $N$ actions instead of one action. 
3. SOTA MARL applies centralized training and decentralized critic with a centralized critic. However, Section 3.3 applies multiple single-agent algorithms (i.e., multiple PPO) without the use of centralized critics. 
4. Results in Figures 2 and 3 need multiple seeds for statistical significance. 
5. Because multiple agents are interacting in the environment, MDP (Section 2) may not be the correct term, and a Markov game (Littman 1994) would be a more correct term to use.

### Questions
I hope to ask the authors' responses to my concerns (please refer to the weaknesses section for details).

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
