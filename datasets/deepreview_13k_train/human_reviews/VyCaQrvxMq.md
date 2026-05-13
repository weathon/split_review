# Quantum-Inspired Reinforcement Learning in the Presence of Epistemic Ambivalence

- Decision: Reject
- Scores: 6, 8, 3, 6

## Abstract
The complexity of online decision-making under uncertainty stems from the requirement of finding a balance between exploiting known strategies and exploring new possibilities. Naturally, the uncertainty type plays a crucial role in developing decision-making strategies that manage complexity effectively. In this paper, we focus on a specific form of uncertainty known as epistemic ambivalence (EA), which emerges from conflicting pieces of evidence or contradictory experiences. It creates a delicate interplay between uncertainty and confidence, distinguishing it from epistemic uncertainty that typically diminishes with new information. Indeed, ambivalence can persist even after additional knowledge is acquired. To address this phenomenon, we propose a novel framework, called the epistemically ambivalent Markov decision process (EA-MDP), aiming to understand and control EA in decision-making processes. This framework incorporates the concept of a quantum state from the quantum mechanics formalism, and its core is to assess the probability and reward of every possible outcome. We calculate the reward function using quantum measurement techniques and prove the existence of an optimal policy and an optimal value function in the EA-MDP framework. We also propose the EA-epsilon-greedy Q-learning algorithm. To evaluate the impact of EA on decision-making and the expedience of our framework, we study two distinct experimental setups, namely the two-state problem and the lattice problem. Our results show that using our methods, the agent converges to the optimal policy in the presence of EA.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a framework to include quantum states in MDPs, with the aim of representing “epistemic ambivalence (EA)”. EA is a concept borrowed from the philosophical literature and represents situations in which a person believes in two (or more) contradicting statements at the same time. The proposed EA-MDP is based on augmenting the traditional state space with a Hilbert space H_EA that reflects EA and is a quantum state. Theoretical results are developed, showing that in an EA-MDP, an optimal value function and an optimal policy exist.

### Strengths
This is a novel, innovative work, which develops an entirely novel framework. The paper is well-written and also includes some analysis.

### Weaknesses
I was left puzzled by what EA might actually represent in the context of sequential decision processes in practice. I tried to understand by looking at some of the literature on EA, but most of it was on an abstract philosophical level that did not help too much. Maybe it is too much to ask of this paper, but given that the audience at ICLR does not have a background in philosophy, it would be very helpful to give concrete examples. The experimental setups remain at an abstract level and the real-world equivalent to the setup is not clear. This makes it unclear how the concept can actually be useful to solve real-world decision processes.

I looked at the literature on EA cited by the authors [Amaya 2021, Williamsom 2021, Lam 2013]. These sources present ambivalence as a concept distinct from uncertainty, whereas the authors describe it as a form of uncertainty. This should be clarified. 

Furthermore, the distinction between the proposed EA-MDP and partially observable MDPs (POMDPs) is not sufficiently clear. The paper claims that EA-MDP uses a quantum-inspired approach to manage ambivalence, but it is unclear how this fundamentally differs from how POMDPs handle uncertainty arising from partial observations. The argument that the environment in a POMDP is not aware of the probabilities associated with the quantum state is not convincing, as the belief state in a POMDP can be viewed as a probability distribution over possible states, which is conceptually similar to the quantum state in EA-MDP. The paper needs to provide a more rigorous comparison, highlighting the specific conditions under which EA-MDP would be advantageous over POMDPs.

### Questions
1) I looked at the literature on EA cited by the authors [Amaya 2021, Williamsom 2021, Lam 2013]. These sources present ambivalence as a concept distinct from uncertainty, whereas the authors describe it as a form of uncertainty. This should be clarified. 
2) What are real-life examples of EA for which a sequential decision process could be formulated? Is it possible to motivate the experiments with such examples?
3) In which way is EA-MDP expected to outperform partially observable MDPs in practice?

### Soundness
2

### Presentation
2

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
In this paper, the authors develop the EA-MDP, a variant of the classic MDP, that can capture a different form of uncertainty called Epistemic Uncertainty (EA). In a EA state, the agent can coexist in multiple configurations at the same time. The authors demonstrate that the fundamental results of MDP planning, such as the contractiveness of the Bellman operator, also hold in this setting, with some modifications. The most notable difference is that rewards depend on the outcome of each quantum state (which can be interpreted as measurements), and therefore rewards should be computed through an additional expectation. The authors also demonstrate the result of planning an optimal policy for EA-MDPs, in two small discrete environments, for a range of environment parameters.

### Strengths
The definition of the EA-MDP appears to be an appropriate model for epistemic uncertainty. This fulfills the main objective of the paper. Moreover, the model seems to be consistent and well designed. The theoretical results in Section 5 prove the minimum basic properties that allow to extend the classical planning tools to EA-MDPs with small modifications. I could not find mistakes in the proofs of these results.

The experimental demonstrations and the pictures help the reader to understand the basic principles about how the model work.

The topic and the ideas seem to be novel. However, I am not able to confideltly relate this paper with the related work of previous uses of quantum information in ML.

### Weaknesses
1. The paper tries to preserve the great generality allowed by quantum states, basis states, and outcomes. However, this complicates the exposition for an audience that is not familiar with the formalisms used in quantum mechanics. Some concepts are still not entirely clear to me:
	- What is the need for treating outcomes as distict entities from the underlying states? In my understanding, outcomes may be restricted to be the set of discrete locations of the system. Clearly, this would be a limitation with respect to more general bases such as eq (22), however, this seems to be sufficient for what is needed in RL. Specifically, it is unclear why the reward function cannot directly map the quantum state \(\psi_{s_t}\) to a reward value, instead of requiring an additional expectation over outcomes. This additional layer of abstraction, while potentially useful for very general cases, adds complexity without a clear justification in the context of RL.
	- What is the role of $s_t$ in equation (3)? I would expect $\psi_{s_t}$ to be a complete description of environment state by itself. The fact that the state space contains the "underlying state of the system" seems to contradict the intuition that the quantum state $\phi_{s_t}$ is describing a mixture of basis states. It is not clear why the state needs to be decomposed into two parts, a classical underlying state and a quantum epistemic state, especially when the epistemic state is meant to capture the uncertainty about the true state. The introduction of $s_t$ seems to reintroduce a notion of a true state, which the quantum state is supposed to make uncertain.

An example early on in the paper would greatly help in clarifying most concepts, even before the experimental section.

2. It should be pointed out that the EA state is observed by the agent. This is analogous to what happens in standard, fully-observable MDPs. However, the rich information provided by the EA state allows to fully compute the superposition of states. In turn, this allows to plan in EA-MDP with analogous techniques as for MDPs, by means of an additional expectation over outcomes. While convenience is surely an advantage, this also means that the proposed framework cannot be used by an agent that encounters conflicting observations, because the environment should return the explicit quantum state, which itself encodes the EA uncertainty. This discrepancy slighly contradicts the main motivation of this work, which is the development of RL algorithms in presence of conflicting evidence. The agent's ability to directly observe the full quantum state, including the superposition, implies a level of access to the environment that is not realistic in many scenarios where epistemic uncertainty arises from partial or conflicting observations. This limitation should be explicitly acknowledged and discussed.

### Questions
The authors may answer the doubts listed in Weaknesses, point 1.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors propose a novel sequential decision-making framework that incorporates the concept of epistemic ambivalence. In particular, they propose an MDP-based framework that leverages concepts from quantum mechanics to quantify the epistemic ambivalence, primarily via the state-space and reward function. They show that this MDP framework can be used to find an optimal policy, and present two empirical experiments in support of this.

### Strengths
This paper tackles an interesting problem of decision-making under epistemic ambivalence. Most of the MDP-related literature only considers epistemic and/or aleatoric uncertainty, so considering this kind of uncertainty is refreshing. The paper incorporates several non-trivial aspects of quantum mechanics into an MDP framework which is impressive. The paper is generally well-written, and the technical concepts are explained in a relatively clear manner.

### Weaknesses
My biggest concern with this paper is that the experiments, while interesting, fail to support the overall narrative of the paper. In particular, the narrative of the paper suggests that the EA-MDP leverages quantum mechanics to optimize decision-making under epistemic ambivalence. This implies that one should be able to take a given MDP-based system that has epistemic ambivalence, convert it to an EA-MDP, and then use the proposed quantum-inspired methods to find an optimal policy. However, the experiments presented in the paper start with an EA-MDP that is already formulated and then proceed to solve it, thereby missing the crucial step of showing how this EA-MDP can be derived from a regular MDP. This gives the impression that the primary use-case for the EA-MDP is to model quantum phenomena. Of course, modeling quantum phenomena using MDPs is in itself a worthwhile and an interesting topic, however if this is indeed the intended use-case for the EA-MDP, then the text should make this more clear. Conversely, if the EA-MDP can indeed be used more generally to optimize decision-making under epistemic ambivalence, then a more intuitive and complete set of experiments is required, where the experiments show how one can turn a regular MDP to an EA-MDP. The authors used a good analogy related to buying or selling stock in the presence of conflicting evidence at the start of the paper when explaining epistemic ambivalence. I suggest that the authors use more compelling and intuitive experiments that are similar to this analogy.

Moreover, the paper could (potentially) benefit from a comparison between epistemic ambivalence and entropy, given that these concepts appear to be similar in nature. Moreover, and especially given that there are lots of existing MDP-based methods that utilize entropy, it would be useful if the authors could compare their method to methods that use entropy (or some sort of other baseline) to highlight the usefulness and advantages of their methods.

Finally, it may be more beneficial to the reader, in the context of ICLR, if most of the equations in Section 6 of the paper be moved to the appendix, and that the resulting extra space in the main body be used instead to better explain the experiments and/or to include more helpful figures to better explain the intuition behind the experiments.

Overall, this paper feels stuck somewhere in the middle between a physics paper and a ML paper. Both directions can be good, however the authors need to lean into one direction or the other. A good litmus test that the paper currently fails, is that after reading the paper I should be able to know under which conditions the EA-MDP is a good tool to use. However, in its current state, the paper is unable to successfully answer this question.

### Questions
1) What are the implications of the $\approxeq$ in Equation 12?

2) From an MDP perspective, it appears odd that in the two-site experiment, there is only a single action in the action-space. If there is only a single action, then is there no decision to be made? Could the authors please explain how and why only having a single action makes sense? (see lines 368-369). Is it perhaps that there should be two actions: {move to the other site, remain in the current site}?

### Soundness
2

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
This paper presents a theoretical framework that integrates quantum mechanics with reinforcement learning, exploring the interactions between EAs and quantum states. They introduce a novel reward operator that considers separated quantum outcomes, facilitating the calculation of expectation values under a bijective mapping between quantum states and environmental rewards. The analysis includes the optimal value functions for two-site and many-site systems, highlighting the effects of complex probability amplitudes on the reward structure. Experimental results demonstrate significant variations in optimal policies as parameters change, particularly at phase transition points. This work contributes to a deeper understanding of how quantum features can enhance decision-making processes in reinforcement learning environments.

### Strengths
The paper effectively bridges quantum mechanics and reinforcement learning, offering fresh perspectives on reward calculations and decision-making processes. The mathematical formulation is rigorous, with well-defined operators and expectation values that enhance the theoretical foundation of the study.

### Weaknesses
The paper could benefit from more detailed discussions on the practical implementation of the proposed framework in real-world scenarios.

### Questions
How do the findings of this framework extend to more complex or varied environments beyond those studied in the paper?

What computational challenges might arise when implementing this quantum reinforcement learning model in real-world scenarios?

How does the performance of this quantum-based approach compare to traditional reinforcement learning methods in terms of efficiency and accuracy?

### Soundness
3

### Presentation
3

### Contribution
3
