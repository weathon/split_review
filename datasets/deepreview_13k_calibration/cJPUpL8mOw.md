# REvolve: Reward Evolution with Large Language Models using Human Feedback

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Designing effective reward functions is crucial to training reinforcement learning (RL) algorithms. However, this design is non-trivial, even for domain experts, due to the subjective nature of certain tasks that are hard to quantify explicitly. In recent works, large language models (LLMs) have been used for reward generation from natural language task descriptions, leveraging their extensive instruction tuning and commonsense understanding of human behavior. In this work, we hypothesize that LLMs, guided by human feedback, can be used to formulate reward functions that reflect human implicit knowledge. We study this in three challenging settings -- autonomous driving, humanoid locomotion, and dexterous manipulation -- wherein notions of ``good" behavior are tacit and hard to quantify. To this end, we introduce \rewolve, a truly evolutionary framework that uses LLMs for reward design in RL. \rewolve generates and refines reward functions by utilizing human feedback to guide the evolution process, effectively translating implicit human knowledge into explicit reward functions for training (deep) RL agents. Experimentally, we demonstrate that agents trained on \rewolve-designed rewards outperform other state-of-the-art baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a framework that combines human feedback with genetic algorithms to guide LLMs in designing complex reward functions for agents. The authors conducted experiments on three tasks: Autonomous Driving, Humanoid Locomotion, and Adroit Hand Manipulation, and performed a comprehensive ablation study analysis.

### Strengths
- Well written, the technical approach is very clear, especially Figure 1 and Algorithm 1, which can help readers quickly understand the technical route of the paper.
- The experiments involve a wide range of task types, covering multiple dimensions of continuous and discrete action spaces and observation spaces for RL agents in virtual simulation environments.
- The authors have compared their work with a variety of baseline algorithms.

### Weaknesses
The paper does not clearly describe the foundational setup of the experiments and the comparison metrics. In fact, I do not understand the role of the "fitness score" mentioned in the text. In sections 2 and 3, it is used as a supervisory signal to guide the genetic algorithm in generating the reward function. However, in section 4, it becomes an evaluation metric for the experimental results of the paper. I am unsure whether this practice is appropriate because it raises the following concerns:
- (1) If the fitness score can effectively measure the performance of agents in the current task, then why not use it directly as the reward function to train the agents?
- (2) If the fitness score serves as a signal to guide the generation of the reward function, is it fair to use it as an evaluation metric for the experiments? This is because the REsolve method receives fitness supervision during training, whereas other baseline methods do not.
The insights provided by the paper are limited. When the RLHF paradigm was introduced, people saw that using human feedback could enable agents to perform challenging actions like backflips, which are certainly beyond the capabilities of rule-based reward functions. However, in the tasks and experimental setup implemented in the paper, all I understand is that the authors have used very costly human feedback to achieve a performance superior to the baselines, without offering additional insights or analyses to justify the necessity of this approach.

### Questions
- The first sentence of the paper mentions "Recent success...", but the cited articles are from 2018 and 2019. Is that really considered recent?
- How long does the entire pipeline process take? Are there cases where the reward function does not converge due to difficulties in summarizing it from human-provided language feedback? I think this is an important issue because the pipeline proposed in this paper seems overly complex and involves a lot of uncertainties.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
REvolve is an evolutionary algorithm for LLM reward function generation for RL tasks in robotics. Authors first point out that Eureka is not in fact an evolutionary algorithm (despite claiming to be so), because it does not preserve populations and do mutation and crossovers. REvolve takes Eureka and implements two main changes: make it an actual evolutionary algorithm, and use human labelers as a fitness function (instead of a manually-specified one as is done by Eureka). Authors demonstrate REvolve surpasses Eureka on 3 sim tasks: autonomous driving, humanoid locomotion, and adroit hand door opening.

### Strengths
1. Paper is written very clearly and is easy to understand.

2. Results included good ablations that tested the effect of human ratings as fitness functions for both REvolve and Eureka.

3. Human evaluations were conducted and full Elo scores reported between REvolve, Eureka, and their respective ablations.

4. Appendix contained detailed experimental setup information.

### Weaknesses
1. Natural language feedback to the LLM is extracted from a series of checkboxes that the user ticks. This requires a human to predefine the specific characteristics that the agent must exhibit, which may bias the prompting of the model by constraining the natural language feedback to this small discrete list of checkboxes. So while the authors argue that no manual engineering is required for providing the fitness function, there is manual engineering required to provide a good list of attributes for the human labelers to choose from, and it seems like these attributes must be tailored for each task.

2. A more in-depth analysis that would be helpful to the paper would try to quantify the total amount of human effort needed in REvolve vs Eureka auto: amount of time to define the natural language feedback checklist, provide all pairwise ratings and natural language feedback throughout training in REvolve, vs time to define a fitness function in Eureka. Since it requires hundreds of human labels over N=5 generations, I suspect REvolve involves much more human effort than Eureka auto, but the promising part of this work is that REvolve auto outperforms Eureka auto on all three tasks.

3. Presumably there is additional effort involved in REvolve vs Eureka, from a ML practitioner standpoint, in needing to tune additional parameters related to the mutation and crossover operations (such as p_m, or number of islands).


### Questions
1. What proportion of the LLM-generated reward functions were executable? Eureka mentioned many generated reward functions could not be executed.

2. Each human provides feedback consisting of a pairwise preference assessment and natural language feedback (extracted from a selection of checkboxes). This seems somewhat demanding. How important is each of these two components, relatively? Ablating either of the two components would have been informative.

3. Did authors try allowing humans to provide open-form natural language feedback, not constrained to a checklist?

4. Were the human evaluators for the policy’s final performance in Table 2 the same as the human evaluators that provided feedback during training? If so, I would take issue with that, because then the non-auto methods are given an unfair advantage over the auto methods since they were evaluated on the same distribution of human evaluators as during training.

5. During crossover, how are the “most effective” reward components determined? Through human natural language feedback?

6. Perhaps show an evaluation comparison as training proceeds through the N=5 generations. This would tell us whether REvolve consistently outperforms Eureka, or whether REvolve learns faster with increasing generation index.

7. What is the feasibility of REvolve on real robot tasks? Authors mentioned sim2real as a promising approach, but given the difficulty in simulating high DOF robots (such as humanoids), training on simulation data may not necessarily yield satisfactory results. However, only training with real data would be expensive with REvolve especially with the high demand on human feedback.

### Soundness
3

### Presentation
4

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
This paper introduces a reward design framework. It proposes a fitness function that involves human feedback and natural language. It applies evolutionary algorithms to evolve a population of reward functions by LLMs, where the prompt is the output of the fitness function.

### Strengths
REvolve uses the evolutionary algorithm with genetic operators like mutation, crossover, and selection to overcome the disadvantage in greedy search in Eureka and present good performance. 
REvolve leverages LLMs to generate reward function explicitly and employ human preference to guide the reward function generation implicitly, which enhances the interpretability and aligns with humans.

### Weaknesses
No major weaknesses under the topic of explicit reward function generation, but it lacks the discussion of the comparison to an implicit reward design, for example, a reward model from human preference.

(1) In Figure 3 (left), it seems auto grows faster than human feedback. In Figure 3 (right), auto grows exponentially but others grow linearly. What will happen given more generations? Will the auto surpass human feedback? I would suggest to run more generations to see a clear trend.

(2) A follow up question for (1). If the auto surpass human feedback, or even human driving, would human evaluators still prefer human feedback to auto?

(3) To solve reward design problem, REvolve is a good solution for explicit reward function generation, but how does this method compare with implicit reward models, i.e., RLHF, in terms of performance, interpretability, computational requirements?

### Questions
(1) In Figure 3 (left), it seems auto grows faster than human feedback. In Figure 3 (right), auto grows exponentially but others grow linearly. What will happen given more generations? Will the auto surpass human feedback? I would suggest to run more generations to see a clear trend. 

(2) A follow up question for (1). If the auto surpass human feedback, or even human driving, would human evaluators still prefer human feedback to auto?

(3) To solve reward design problem, REvolve is a good solution for explicit reward function generation, but how does this method compare with implicit reward models, i.e., RLHF, in terms of performance, interpretability, computational requirements?

### Soundness
3

### Presentation
4

### Contribution
3
