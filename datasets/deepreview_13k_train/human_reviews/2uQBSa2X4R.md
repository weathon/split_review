# Robust Gymnasium: A Unified Modular Benchmark for Robust Reinforcement Learning

- Decision: Accept
- Scores: 8, 5, 5, 8

## Abstract
Driven by inherent uncertainty and the sim-to-real gap, robust reinforcement learning (RL) seeks to improve resilience against the complexity and variability in agent-environment sequential interactions. Despite the existence of a large number of RL benchmarks, there is a lack of standardized benchmarks for robust RL. Current robust RL policies often focus on a specific type of uncertainty and are evaluated in distinct, one-off environments. In this work, we introduce Robust Gymnasium, a unified modular benchmark designed for robust RL that supports a wide variety of disruptions across all key RL components—agents' observed state and reward, agents' actions, and the environment. Offering over sixty diverse task environments spanning control and robotics, safe RL, and multi-agent RL, it provides an open-source and user-friendly tool for the community to assess current methods and foster the development of robust RL algorithms. 
In addition, we benchmark existing standard and robust RL algorithms within this framework, uncovering significant deficiencies in each and offering new insights.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Robust-Gymnasium, a unified and modular benchmark designed for evaluating robust reinforcement learning (RL) algorithms. It addresses the lack of standardized benchmarks for robust RL by providing a platform that supports a wide variety of disruptions across key RL components, including agents' observed state and reward, agents' actions, and the environment. The benchmark includes over sixty diverse task environments spanning control, robotics, safe RL, and multi-agent RL. The paper also benchmarks existing standard and robust RL algorithms within this framework, revealing significant deficiencies in current algorithms and offering new insights. The code for Robust-Gymnasium is available online.

### Strengths
- Robust-Gymnasium offers a broad range of tasks for evaluating robust RL algorithms, covering various domains.
- The benchmark is highly modular, allowing for flexible construction of diverse tasks and easy integration with existing environments.
- It supports different types of disruptions, including random disturbances, adversarial attacks, internal dynamic shifts, and external disturbances.
- The benchmark is designed to be user-friendly, with clear documentation and examples.

### Weaknesses
 - The variety of disruptions and the modular nature might make the benchmark complex to understand and use for some users.
- The effectiveness of some robust RL algorithms might rely on the quality and quantity of offline demonstration data.
- The performance of algorithms on the benchmark could be sensitive to hyperparameter tuning, which might not be straightforward.

### Questions
- How does Robust-Gymnasium handle continuous action spaces and high-dimensional state spaces?
- Can the benchmark be used to evaluate the robustness of RL algorithms in partially observable environments?
- What are the limitations of the current implementation of Robust-Gymnasium, and how might these be addressed in future work?
- How does the benchmark compare to other existing RL benchmarks in terms of robustness evaluation?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work proposes a new benchmark for robust reinforcement learning termed Robust-Gymnasium. The manuscript introduces a framework for MDPs under disturbances and models its benchmark after it. There are three types of disturbances: observation, action and environment disruptions. The paper outlines 60 standard tasks that can be used in the benchmark with these disturbances and provides an experimental validation using baselines from standard, robust, safe, and multi-agent RL demonstrating the utility of the benchmark.

### Strengths
1. Clarity  
a) The text uses clear language and is easy to follow.  
b) Figure 1 is very  useful as it nicely summarizes environments, agents and disruptions and Figure 2 is a nice addition to describe the environment flow.  

2. Problem Motivation  
a) I think the motivation for this problem is solid and we do need benchmarks that test real world robustness. Even if this benchmark is not perfect for that as it creates artificial disturbances, this might be the closest we can get with general solutions. I do think the benchmark solves a good problem the community is facing.  

3. Novelty  
a) I am not aware of any benchmarks for robust RL that are very extensive lending credibility to the novelty of this benchmark.  

4. Experiments  
a) While I am not familiar with some of the baselines, it seems that the evaluation is somewhat extensive. At least I believe it is sufficient to demonstrate that current algorithms fail on this benchmark which allows for new research to be done.  
b) I do appreciate the two setting evaluations of training and testing. I think it is crucial to demonstrate what happens when training works fine but disturbances occur during testing. This experiment highlights the importance of this work.

### Weaknesses
1. Clarity   
a) Overall, several sections are very wordy and or redundant, repeating lots of information but missing useful information early on. Some examples:
* Section 2.1 and 2.2 could be more concise, it feel like they are repeating the same thing multiple times when describing the disruptors. To remedy this it might be good to consolidate the functionality and highlight specific disruptors in section 2.2. For instance, it is not clear to me what random noise on an environment disruptor means. I also don’t quite understand what “The environment-disruptor uses this mode to alter the external conditions of the environment.” entails.
* The same goes for sections 3.2 and 2.2. Both sections address the design of disruptors and essentially repeat a lot of information. It seems easy to simply combine these two sections which will also avoid confusion about how disruptors work.  I understand that there is supposed to be a differentiation between the universal framework and the implementation but nonetheless there would be lots of text that can be cut for clarity.   
b) I find that section 3.2 is missing crucial information. The section can likely be improved by adding additional information about the state-action space and how the different disruptors affect them for each environment. The space for this can likely be obtained by condensing sections 2.1 and 2.2. If action spaces are similar, it might be possible to cluster environments and add information about the action spaces per cluster such as “these environments all use joint control with action spaces according to the number of degrees and an additional grasp action”.  

2. Related Work   
a) In L 73, the text states “While numerous RL benchmarks exist, including a recent one focused on robustness to environment shifts (Zouitine et al., 2024), none are specifically designed for comprehensively evaluating robust RL algorithms.” I only skimmed the referenced work but it seems that the citation aims to do exactly that. However, they might have a less comprehensive benchmark. We can likely count them as X work but I believe a more thorough differentiation from this paper would benefit the presented manuscript.  
b) I appreciate the additional section on robust benchmarks in Appendix A. In general for benchmark papers, I find it beneficial to demonstrate the novelty of the benchmark but providing citations to benchmarks that are related to demonstrate that there is a gap in the existing literature. Here is a non-exhaustive list of possibly relevant recent benchmarks that might be of use as a starting point [1-11]. There are older benchmarks too such as ALE and DM Control for which I recommend standard citations. Such a differentiation does obviously not have to happen in the main text.  

3. Benchmark Feedback  
a) “Notably, in our benchmark, we implement and feature an algorithm leveraging LLM to determine the disturbance. In particular, the LLM is told of the task and uses the current state and reward signal as the input” L302 - It seems quite wasteful to have to run a full LLM at every environment step and it might be good to have simpler adversarial features that don’t limit usage to labs with lots of money for compute. The LLM feels a lot like using an LLM for the sake of the LLM. It is unclear to me why this choice was made rather than a simpler adversarial attacker.  
b) What I am missing is metrics other than cost and reward that are useful to determine whether one is making progress on this benchmark. Given two algorithms with the same performance, what let’s us determine whether either of them is more robust? I think providing useful metrics of interest would be good to make this benchmark stand out. For instance, reliability metrics such as those in [12] might be useful to measure.  
c) The second thing I am missing is guidelines on how to choose parameters for the disturbances. I think elaborating on what values are valid in section 3.2 as I mentioned before and providing suggestions would be useful for standardized usage of the benchmark. For instance, it is unclear in section 4.3, why the attacks follow a Gaussian distribution and not a Uniform distribution. Is this more realistic? Maybe it is arbitrary but then it should at least be stated earlier that this is recommended by the work.  

4. Experiments  
a) It is unclear over how many seeds the experiments were conducted. Given the high variance in RL results in general [13], and the need for many experiments even without disturbances [14], we should conclude that more robust experimental evaluation is needed in Disturbed MDPs. For instance, 5 random seeds would definitely not be enough to draw meaningful conclusions from many of the provided graphs.  
b) It is unclear to me how the tasks were picked and why the evaluations are not incorporating all tasks for all baselines. Running all tasks with all baselines would definitely strengthen the argument for the necessity of the benchmark and avoid uncertainty about how to choose tasks. At least, there should be one experiment that runs one algorithm on all tasks to verify that all tasks are in fact still learnable. I understand that that is computationally costly but I believe it is needed to verify the utility of the benchmark.

Minor suggestions  
* In L156, L180, In Disrupted MDP -> In a Disrupted MDP
* L192 and L197: for environment disruptor -> for the environment disruptor
* L201 Disrupted-MDP allows disruptors to operate flexibly over time during the interaction process.

### Questions
Q1: In section 2.1, can you elaborate why maximization of the reward is over disturbed actions but not disturbed states?  

Q2: L213 “Not all task bases support every type of disruption.” Could you elaborate why not? What is the limitation? This answer should likely be added to the text.  

Q3: For Safety Gym, how do disturbances interact with the constraints?   

Q4: I am confused about the adversarial disturbance mode. The text states “Any algorithm can be applied through this interface to adversarially attack the process.” L301. Does that mean that there are no standard disruptors implemented and the user has to implement them themselves?  

Q5: Does the LLM for the adversarial disturbance mode require the user to run a local LLM?  

Q6: Are there any tasks that you believe become significantly harder by introducing the perturbations, so much so that they might be unsolvable now?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a robust reinforcement learning benchmark, designed for facilitating fast and flexible constructions of tasks to evaluate robust RL.  This benchmark provides various robust RL tasks by adding various perturbations to standard tasks from multiple RL benchmarks.

### Strengths
- The provided overview in Figure 1 is good. 
- Sixty robust RL tasks are offered in this benchmark.

### Weaknesses
This paper made an effort in transforming diverse RL tasks into robust RL tasks where environmental perturbations are considered. However, it might be of limited significance, since there are some existing benchmarks that allow to add disturbances to RL tasks to test the robustness of RL algorithms. Besides, it offers a limited technical contribution, as the main technical work is to add a wrapper to the existing RL benchmarks that implements disturbances.  Therefore, I recommend rejection.

I have some other concerns about the current version.   
- The author stated that this is the first unified benchmark specifically designed for robust RL in the introduction. It is a bit overstated, as RRLS focuses on the evaluations for robust RL and some other benchmarks allow for evaluating the robustness of RL algorithms.
- In Section 3.2, the authors present several disruptors that are used in previous works. Providing citations to them is suggested. 
- The discussion about the limitation of the benchmark is missing.

### Questions
.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce a robust reinforcement learning benchmark that addresses multiple types of robustness. These include robustness concerning the transition kernel, observation noise, action noise, and reward noise. The framework considers both random noise and adversarially selected worst-case noise. To generalize robustness, the concept of a "disrupted MDP" is introduced. The environments proposed are diverse, primarily involving robotics and continuous control tasks, covering both single and multi-agent settings.

Agents are evaluated on this benchmark across multiple tasks, using various baselines such as SAC and PPO for standard RL approaches. For Robust RL with a nominal transition kernel, baselines like RSC are used. The paper also includes evaluations for robust learning under dynamic shifts (OMPO), state adversarial attacks (ALTA), visual distractions (DBC), safe RL (PCRPO and CRPO), and multi-agent RL (IPPO).

### Strengths
- The paper is well written
- The benchmark is an important contribution to the robust reinforcement learning community, offering a unified framework that fills a significant gap. It is comprehensive, covering a broad spectrum of robustness types, making it a valuable tool for evaluating and designing Robust RL algorithms.

### Weaknesses
 - M2TD3, a state-of-the-art baseline for robustness under model misspecification, is not cited. Its inclusion would strengthen the paper’s coverage of relevant baselines.
- The explanation of adversarial disturbance via LLMs is interesting but could be more general. Instead of focusing on LLMs, the paper should emphasize the adversarial setup and consider an adversary such as two player Markov games with potential LLM integration as an example. The current framing limits the scope of the adversarial approach, potentially overlooking more general adversarial strategies.
- While the benchmark is nearly exhaustive, baselines like RARL and M2TD3 are missing. It is unclear how uncertainty sets can be built with the benchmark. Including examples in the appendix on constructing such sets, as proposed in the M2TD3 paper, would be beneficial. The lack of clarity on uncertainty set construction hinders the practical application of the benchmark for robust RL algorithms that rely on such sets.
- The environments are primarily robotics-based, except for Gymnasium Box2D. Including use cases like autonomous driving or drone simulations would diversify the benchmark and offer more relevant challenges to the community, fostering the development of more general RRL algorithms. The current focus on robotics limits the applicability of the benchmark to other critical domains.

### Questions
Remarks: 
- Emphasize the introduction of the "disrupted MDP" by bolding its first mention.
- There is a minor formatting issue on line 132 with a space before "environment-disruptor."
- Providing examples in the appendix on how to modify external parameters like wind would enhance usability.

### Soundness
4

### Presentation
4

### Contribution
3
