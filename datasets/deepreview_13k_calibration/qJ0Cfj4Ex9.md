# Learning Grounded Action Abstractions from Language

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 5, 6, 8, 6

## Abstract
Effective planning in the real world requires not only world knowledge, but the ability to leverage that knowledge to build the right representation of the task at hand. Decades of hierarchical planning techniques have used domain-specific temporal action abstractions to support efficient and accurate planning, almost always relying on human priors and domain knowledge to decompose hard tasks into smaller subproblems appropriate for a goal or set of goals. This paper describes Ada (Action Domain Acquisition), a framework for automatically constructing task-specific planning representations using task-general background knowledge from language models (LMs). Starting with a general-purpose hierarchical planner and a low-level goal-conditioned policy, Ada interactively learns a library of planner-compatible high-level action abstractions and low-level controllers adapted to a particular domain of planning tasks. On two language-guided interactive planning benchmarks (Mini Minecraft and ALFRED Household Tasks), Ada strongly outperforms other approaches that use LMs for sequential decision-making, offering more accurate plans and better generalization to complex tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the challenge of long-horizon planning. To make this more tractable, the authors leverage hierarchical planning using temporal action abstractions, breaking down intricate tasks into manageable subproblems. The novel contribution is a system that harnesses language to derive symbolic action abstractions and associated learnable low-level policies. By querying large language models (LLMs), the system proposes symbolic action definitions, subsequently integrating these into a hierarchical planning framework for grounding and verification. This approach is framed within a multitask-reinforcement-learning objective, where an agent interacts with an environment to solve tasks described in natural language. The ultimate aim is to construct a library of grounded actions that are both planning-compatible and efficient.

### Strengths
The system leverages language to derive symbolic action abstractions, a unique approach to decomposing complex tasks, and subsequently verifies them within a hierarchical planning framework, ensuring the practical applicability of the abstractions,  which was tested on two benchmarks, Mini Minecraft and ALFRED, and outperformed other baseline methods that incorporate language models into planning.

The paper presents a commendable effort in bridging the capabilities of large language models with hierarchical planning, the innovative approach of using language to derive action abstractions is particularly noteworthy.

### Weaknesses
 - Goal Misspecification: Failures on the ALFRED benchmark often occurred due to goal misspecification. The LLM did not accurately recover the formal goal predicate, especially when faced with ambiguities in human language. For instance, a request to "slice a tomato and put it on a table" could have multiple interpretations depending on the specific table intended (dining table, side table, coffee table, etc.). This ambiguity led to planning failures when the chosen interpretation did not match the ground truth goal in the environment.

- Policy Inaccuracy: The learned policies sometimes failed to account for low-level, often geometric details of the environment. This suggests that while the high-level planning might be sound, the execution at the lower levels needs refinement. This could be due to insufficient training data or limitations in the policy learning algorithm's ability to capture fine-grained environmental nuances.

- Operator Overspecification: Some learned operators were too specific. For instance, the learned SliceObject operator specified a particular type of knife. This led to planning failures if that specific knife type was unavailable in the environment, even if other suitable tools were present. This overspecification limits the generalizability of the learned operators and reduces the robustness of the planning system.

- Limitations in Hierarchical Planning: The paper acknowledges that it doesn't address some core problems in general hierarchical planning. For instance, it assumes access to symbolic predicates representing the environment state and doesn't tackle finer-grained motor planning. The paper also only considers one representative pre-trained LLM and not others like GPT-4. This limits the scope of the current work and highlights the need for future research to address these fundamental challenges in hierarchical planning.

### Questions
Questions:

- The two-stage prompting strategy involves symbolic task decomposition followed by symbolic operator definition. How does the system ensure that the decomposition is optimal or near-optimal for complex tasks?

- The author mentioned that one of the common failures on the ALFRED benchmark was due to goal misspecification, especially when faced with ambiguities in human language. Could you elaborate on how the system currently handles such ambiguities and if there are plans to improve this aspect?

- The paper demonstrates that action libraries from simpler tasks in Mini Minecraft generalize to more complex tasks. Are there plans to test this generalization capability in more diverse environments or tasks outside of the current benchmarks?

- How scalable is the proposed system? Specifically, if the number of tasks or the complexity of the environment increases significantly, how would the system's performance be affected?

Suggestions:

- Might consider introducing an interactive feedback loop where the system can ask clarifying questions when faced with ambiguous goals or tasks. This could help in refining the task understanding and improve planning accuracy.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed to leverage LLM to solve long-horizon planning problems by dynamically building a library of symbolic action abstractions and learning a low-level policy to execute the subgoals. They conducted experiments and relevant ablation studies on Mini Minecraft and ALFRED benchmarks to demonstrate the effectiveness of the proposed method.

### Strengths
+ The method is technically feasible.
+ The writing is easy to follow. 
+ Representing abstract actions with symbols and reasoning them with LLM is an interesting attempt.

### Weaknesses
 + **Lack of novelty.** This pipeline is reminiscent of the Voyager model, which also aims to tackle long-horizon tasks via the creation of a dynamic skill library. This limits the contributions of this paper. It is better to highlight the differences between this work and Voyager. 

+ **Benchmark is too simple.** It should be noted that the test environment used in the current work (Mini Minecraft) is significantly less complex than the original Minecraft version, resulting in reduced task difficulty. Especially the success rate in Mini Minecraft even reaches 100%. 

+ **Concerns about generalization ability.** The proposed method relies heavily on symbolic representations. I'm concerned that it may be difficult to generalize to complex real-world environments, which are often not easily symbolized. 

+ **Missing important citations.** [1, 2] are also important methods that leverage LLM as the planner to decompose the long-horizon task into subgoals. I suggest the authors to include some discussion and comparison of such methods.

### Questions
As stated in the Weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose to exploit the world knowledge of LLMs for learning action abstractions for hierarchical planning. These action abstractions can then be used to solve long-horizon planning problems, by decomposing a goal into subgoals and solving them using bi-level planning. More specifically, given a task and symbolic state, the authors use LLMs to propose symbolic (high-level) operators and their corresponding definitions (in PDDL) which are then used by a bi-level planner to generate a feasible low-level plan. The useful operators (planning-compatible and grounded) are retained in an operator library (i.e. reusable) and used for subsequent tasks, including those that require the composition of learned operators.

### Strengths
1. Overall, the paper is well-motivated, clearly written, and supported by strong empirical evidence.
2. The proposed idea of exploiting knowledge of LLMs for action abstraction is intuitive and effective and would be of interest to the planning and decision-making community.

### Weaknesses
It would be nice to have some statistics on the length of the plan sequence (both in terms of high-level and low-level actions), and the number of learned operators, to get an understanding of the task complexity (especially for the compositionality experiments) in Minecraft and ALFRED domains. It is hard to get an idea from just the empirical evidence.

It is unclear how the system addresses the issue of semantically similar or redundant operators being added to the operator library. Since the LLM generation is not conditioned on the existing operators, there is a risk of adding redundant operators that could increase the search space for the planner. For example, if a 'place *args' operator exists, the LLM might propose a 'put *args' operator which is semantically similar. Similarly, if a 'clean *args' operator exists, the LLM might propose a 'clean_and_cool *args' operator. Without a mechanism to identify and filter such redundancies, the operator library could grow unnecessarily large, impacting the efficiency of the planner.

In Sec 3.4 (Scoring LLM Operator Proposals), the operators are selected based on their executability in the low-level planning, but the overall goal is not accounted for. This could lead to the selection of operators that are feasible but not necessarily useful for achieving the overall task goal. For instance, an operator might be executable in the low-level environment but not contribute to the high-level plan's success. The current scoring mechanism doesn't seem to explicitly penalize such operators, which could lead to the inclusion of suboptimal operators in the library.

Minor Comment:
* Sec 3.4: s/b > \tau_r

### Questions
1. In Sec 3.1 (Symbolic operator definition), is there a process through which you identify and/or discount semantically similar (redundant) operators from being added in the operator library since the LLM generation is not conditioned on it (i.e. the LLM is not aware of the existing operators in the library).

2. In Sec 3.4 (Scoring LLM Operator Proposals), the operators are selected based on their executability in the low-level planning, but the overall goal is not accounted for. Wouldn't this lead to the selection of some operators that are just "feasible" but not "useful"?

Minor Comment:
* Sec 3.4: s/b > \tau_r

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a method to iteratively learn a set of action operators that can be used by a symbolic planner to generate high-level plans that are then refined into a series of low-level plans. The action operators are learned using a LLM and their selection is guided by a reward signal. To propose a set of action operators, the LLM decomposes language-based instructions into series of high-level actions. High-level actions that do not have a corresponding action operator are then passed to the LLM (along with a few-shot prompt) for the LLM to generate an operator definition consisting of the list of variables the action operates over, the preconditions that must be met to execute the action, and the effect the action has on the environment. The set of proposed action operators are then evaluated by planning with them to solve environment tasks, and are scored based on how often they are used and how often their use leads to task success. Only action operators with high scores are retained. The authors evaluate on Mini Minecraft and Alfred, and compare against several baselines that use LLMs to provide a low-level sequence of actions, specify subgoals, and to specify the plan as code. Across tasks and baselines, the proposed method performs best.

### Strengths
- The paper is very well written and easy to follow. 
- The authors incorporate LLM to address the challenging problem of identifying abstract actions.
- The baselines evaluate different ways to incorporate LLMs into planning and action selection tasks.
- The environment on which the methods are evaluated assess actions of different complexity.

### Weaknesses
 - It would be helpful in the results section, "How does or approach compare to using the LLM to predict just goals, or predict task sequences?", to call out the specific parts of the proposed algorithm that address the limitations observed in the baseline approaches.
- It would have been beneficial to include experiments with multiple LLMs in order to understand the required LLM characteristics.
- It is not clear from the reported experiments and results how much noise the system can handle.
- There are no comparisons to systems that rely on hand-coded action abstractions or other methods for identifying/learning the action abstractions.

### Questions
- In section 3.2, the authors state that at each iteration operators are learned for only those tasks that were not solved in the previous iteration. How often were the found plans subpar? For example, taking unnecessary, but valid actions? In the experiment section, the tasks are listed as randomly ordered. How sensitive was the found action operator library to the task ordering?
- In the results section the authors discuss Alfred failure cases as including "operator over specification". When over specification occurred, were multiple instances of the action with different objects seen? For example, a slice object with butter knife and one with steak knife. Were the over specifications arbitrary or driven by the training data? For example, a steak knife was chosen even through a butter knife would also work versus the sharpness level was needed to cut the object.
- The authors suggest that encouraging more diverse proposals could address the failure mode. Was soliciting more diverse proposals attempted? Why would more diverse proposals address operator over specification? 
- Why Alfred instead of Habitat?
- How accurate were the different parts of the LLM's output? How correct were the mappings from language description to goal specification? 
- Might the Mini Minecraft experiments, while good to test how composable the action abstractions are, simplify the action abstraction process by learning the action abstractions on the simpler tasks for which it is easier to identify action abstractions that are more primitive? Compared to learning the actions on the compositional tasks to see how well the method is able to identify useful and flexibly reusable action abstractions?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method that learns a library of symbolic action abstractions (i.e., high-level actions) using LLMs.
Given a natural language instruction and a state (object classes, predicates, etc.), the proposed method uses LLMs to plan a sequence of high-level actions.
In the case of the undefined operator of any high-level action, it further uses LLMs to define the operator based on in-context examples.
Such obtained operators are iteratively refined.
The low-level actions to conduct each high-level action are acquired by BFS such that they satisfy the desired subgoal state.
The low-level action policies are updated based on rewards from the environment after task completion with the policies.
The proposed method outperforms baselines in its empirical validations based on ALFRED and Mini Mincraft.

### Strengths
- The paper is generally written well and easy to follow.
- The paper tackles an important issue of action grounding present in LLMs used for action planning.
- Using LLMs to acquire high-level actions and their unknown operators looks reasonable and intriguing.
- The two-staged pipeline for the generation of candidate operator definition is well-motivated and sounds sensible.
- The proposed method achieves strong performance over the baselines by noticeable margins.

### Weaknesses
 - Some assumptions made are a bit practically unrealistic. For example, $\Phi$ is assumed to be perfect and all environmental information is known, but they are usually not the case, especially for task planning for robotic agents (Shridhar et al., 2020; Krantz et al., 2020; Weihs et al., 2021). Specifically, the assumption of a perfect symbolic representation $\Phi$ that maps the environment to a set of object classes and predicates is a strong one. In real-world scenarios, this mapping is often noisy and incomplete, leading to errors in high-level action planning. The paper does not address how the proposed method would handle such imperfect mappings, which is a significant limitation for practical applications.
- Obtaining high-level action abstractions needs the corresponding low-level policies to generate low-level actions but it seems that it requires extensive interaction with environments (e.g., brute-force search to find a low-level action sequence that satisfies the subgoal condition). This reliance on extensive environmental interaction raises concerns about the method's sample efficiency. The brute-force search for low-level action sequences, while effective in finding a solution, is computationally expensive and may not scale well to more complex environments or tasks. Furthermore, the paper does not explore alternative methods for acquiring low-level policies that might be more efficient, such as imitation learning or reinforcement learning with shaped rewards. Can the proposed method be also applied to some offline scenarios without these interactive environments? And is there any efficient approach to this?
- The detail of the baseline in Table 1 is unclear. For example, for "Code Policy Prediction," the authors prompt the LLM to predict 1) imperative code policies in Python and 2) the function call sequences with arguments. What is the modification made for each? It is not clear how the LLM is prompted to generate code policies and how these policies are executed in the environment. The description lacks details on how the LLM handles the grounding of these code policies to the environment's state and actions. Furthermore, the paper does not specify how the function call sequences are generated and how they are used to achieve the task goals, making it difficult to understand the baseline's implementation and compare it to the proposed method.

### Questions
See weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
