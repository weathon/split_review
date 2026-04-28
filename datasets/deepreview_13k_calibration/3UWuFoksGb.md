# Learning Planning Abstractions from Language

- Decision: Accept
- Avg Score: 5.50
- Scores: 3, 5, 8, 6

## Abstract
This paper presents a framework for learning state and action abstractions in sequential decision-making domains. Our framework, {\it planning abstraction from language (\model)}, utilizes language-annotated demonstrations to automatically discover a symbolic and abstract action space and induce a latent state abstraction based on it. \model consists of three stages: 1) recovering object-level and action concepts, 2) learning state abstractions, abstract action feasibility, and transition models, and 3) applying low-level policies for abstract actions. During inference, given the task description, \model first makes abstract action plans using the latent transition and feasibility functions, then refines the high-level plan using low-level policies. \model generalizes across scenarios involving novel object instances and environments, unseen concept compositions, and tasks that require longer planning horizons than settings it is trained on.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an RL agent that solves the problem by utilizing symbolic abstraction and object-centric representation learning. Given a problem and a goal description for the environment, the proposed method uses LLM as a parser to translate the goal description (or instruction) as a collection of action predicates (verb and objects combination), where those action predicates are used as action abstraction (options or skills in hierarchical reinforcement learning).

Training requires human demonstration annotated with an action predicate. Given the demonstration data, the proposed method trains several functions. State abstraction function takes in the segmented output of a point cloud transformer to disentangle pixel input and it provides a latent space state representation. Action transition model takes in the latent abstract state and symbolic encoding of action predicates. Feasibility function predicts whether an abstract action is applicable in the current state.

After training necessary functions with annotated demonstration data, the planning stage uses the state abstraction function to get a latent state and utilize the feasibility function to select applicable actions. Planning with symbolic action predicates is done by brute-force search over all actions in the problem. Last,  given a high-level plan, the low-level policy is trained.

### Strengths
* Originality: The novel aspect of the presented method is combining symbolic planning with action predicates extracted from natural language goal descriptions or instructions and latent space representation learning with point cloud transformers. The abstract planning is done at the symbolic level, and the abstract state transitions are tracked with object-centric representation learned from segmented pixel data.
* Quality: The overall description of the method is easy to understand and the experiment was conducted on two types of the environments.
* Clarity: Figures help understanding the overall approach
* Significance: I think this is an interesting work that integrating many things to work.

### Weaknesses
 * Originality: Individual components are existing approaches and the originality is on bring those components and implement an agent to solve mini-grid and kitchen world problems.
* Quality: Due to missing details, it is difficult to assess the quality. Specifically, the paper lacks a detailed description of the training process, including the specific loss functions used for each component (state abstraction, action transition, feasibility prediction), the number of training trajectories, and the optimization algorithms used. This makes it hard to reproduce the results or understand the nuances of the method.
* Clarity: There are many missing details in the paper. For example, the paper does not specify how the point cloud transformer is trained for each environment, the architecture of the abstract transition model, or the precise implementation of the feasibility function. The description of the low-level policy training is also very high-level.
* Significance: The comparison is made only against a simpler baselines (end to end RL and behavior cloning). It is not clear how the proposed method compares to other hierarchical reinforcement learning methods or symbolic planning approaches that also use object-centric representations. The lack of comparison with relevant baselines makes it difficult to assess the true significance of the proposed method.

### Questions
### General questions
1. The title is “learning planning abstractions from language.” In the paper, the role of the LLM is parsing an instruction sentence to extract action predicates and objects. The remaining part of the work is independent of language models or language. The parsing could have been done manually or other methods. I cannot see the rationale of using LLM, other than demonstrating that LLM can do the parsing. What is “learned” from language?

2. What if the goal description or instruction did not reveal enough information to extract required high-level actions? Then, should we collect demonstrations following the derived high-level actions?

3. The instructions in the paper are quite simple sentences to parse. What is the longest abstract plan needed to solve the problem? How many abstract actions were needed?

### Section 4
4. In section 4.2, how the model was trained given annotated demonstrations? Is it learned per each abstract action? How many trajectories were given to the training process? How did you train Point Cloud Transformer for mini-grid environment and kitchen world environment? Can you present the details on the training of models?

5. In section 4.3, planning is done with BFS search. If the feasibility prediction fails, how did you handle the error? Does a set of actions derived from LLM parser always guarantee to solve a problem? How can you ensure the action space can solve all problems in the test set? Or a human demonstrator should create trajectories that solves problem given the action predicates?

6. In section 4.4, low-level policy is trained using an actor-critic algorithm. Can you present the details?

### BabyAI experiments.

7. The report on BabyAI experiments shows that baseline will not completely fail in all problems. The presented paper and the report also used similar low-level policy algorithm and neural network architectures. It also offers imitation learning experiments. Can you make some comparison with those baselines? What are the high-level actions extracted from LLM and what are the plans found for the problems? Can you present the sample efficiency or training/test performance?

[1] Hui, D. Y. T., Chevalier-Boisvert, M., Bahdanau, D., & Bengio, Y. (2020). BabyAI 1.1. arXiv preprint arXiv:2007.12770.

### Kitchen Worlds experiments.
8. How many high-level actions were annotated and trained to solve this environment?  From the description in the experiment section, the length of the plan is mostly one or two. Could you present details on the high-level plan and the low-level policies?

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
The paper proposes a framework for solving problems in sequential-decision making by combining LLM-generated high-level abstract actions, imitation learning and a low-level policy by a framework-agnostic traditional RL agent.

The pipeline in more detail is that given a prompt in human language which defines “a language goal”, an LLM decomposes to a verb and corresponding nouns and adjectives (e.g. ‘place’, ‘bowl’, ‘green’), with the assumption that these prompts can always be decomposed to this format. After this,

- a state abstraction function is learned that can identify the objects in the environment

- an abstract transition model is learned which predicts the next state given the current abstract state and high-level action. This model also has a feasibility component that predicts whether a future action can accomplish the language goal

- A breadth-first search algorithm selects the shortest sequence of actions that accomplishes the language goal

- Finally, a low-level policy is applied according to the sequence of high-level actions. These policies are learned with traditional RL

The paper tests the method on two environments: BabyAI (three task setting) and Kitchen-Worlds (two task settings), compare against low-level (regular) and high-level (when the agent has access to the defined ) RL in the former and Goal-Conditioned BC in the latter.

### Strengths
Originality: the paper proposes a novel way to solve sequential decision making problems by combining LLM prompting, imitation learning and traditional reinforcement learning.

Quality: the paper places the work in the literature very well, comparing the differences between previous works and mentions future work. The problem formulation is mostly clearly written up.

Clarity: The paper is mostly well-written and apart from a few inconsistencies, easy to understand.

Significance: its originality could be considered significant.

### Weaknesses
I have three main reservations:

- There is no available code, no experiment details (chosen hyperparameters, tuning) about the algorithm or the baselines and as such the results are not reproducible. The lack of specific details regarding the training process, such as the learning rate, batch size, and optimization algorithm used for both the abstract state representation and the low-level policies, makes it impossible to replicate the reported results. Furthermore, the absence of information on how the hyperparameters were selected (e.g., through a validation set or cross-validation) raises concerns about the robustness of the findings.

- The experiments themselves, the results, and the metrics are described in a very high level without details which does not allow the reader to indeed verify how well they support the claims. For instance, the paper mentions a 'success rate' but does not specify how success is determined in each environment. Is it based on reaching a goal state, completing a sequence of actions, or some other criteria? The lack of clarity on the evaluation protocol makes it difficult to assess the significance of the reported results. Furthermore, the paper does not provide details on the number of training runs or the variance in performance across different runs, which are crucial for evaluating the reliability of the method.

- Scalability: as the number of actions, objects and their combinations increase, the necessary training data size increases intractably (combinatorial explosion). I am concerned that this approach might be feasible for simple problems only due to its inherent limitations. The method relies on learning an abstract transition model, which requires data for all possible combinations of abstract states and actions. As the number of objects and actions increases, the size of this space grows exponentially, making it difficult to collect sufficient training data. This limitation is particularly concerning for real-world applications where the number of possible states and actions can be very large.

Furthermore, there are a few things that are unclear to me which could be further weaknesses. (I’ve listed the questions in the next section.)

My initial rating is due to the above reasons. I would be willing to increase the score if the above concerns are addressed adequately.

Clarity issues:
The notion of “tasks” is not defined in the problem formulation. I understand this is not easy to do, but including it would make the paper stronger. The expression “language goal” is also used a few times throughout the paper, without definition (and I believe tasks = language goals)

4.2 third paragraph third sentence. Did you mean to say something along the lines of “maps the abstract state representation at the current step and an abstract action $a’$ to the next abstract state $s’_{t+1}$” ?

Typos/style issues that did not affect the score:

Introduction
First paragraph; A “good” state and action representations -> Remove “A”
“As the state abstraction extracts relevant information about the actions to be executed” no need for the first “the”, and could you back this up with some sort of example in brackets, ideally with a citation (I can sort of guess what you mean, but I find this a bit too vague and unclear)

Third paragraph: “an particular object” -> a particular object

4th paragraph: “that setups” -> that sets up

4.2

Second paragraph:
“Which encodes the raw state from a given point cloud”: from -> to
“By applying a pooling operation for the point cloud” for -> to

Third paragraph:

“The abstract transition function $\tau’$ takes the following form. It maps [...] -> remove “takes the following form. It”

5th paragraph

“We appends” -> we append

“Of the Transformer encoder at this query possible will be used” -> no need for possible?

4.3
1st paragraph: last sentence is not needed, or its information content should be moved towards the end of the second paragraph. E.g. “we can generate the final tree, the leaves of which are $a’_K$ which correspond to the underlying abstract action in the language goal”.

2nd paragraph: subsequence -> subsequent

searchs ->searches

5
EXPERIMENT -> EXPERIMENTS

5.2

2nd paragraph: “designed to evaluate models’ abilities” -> missing the after evaluate

Citation for the Goal-Conditioned BC baseline is missing.

6

“A framework that leverage” -> leverages

### Questions
In the state abstraction function, how do you know when to stop training to have the right number of point clouds? Or else, do you assume that the number of objects in the environment is known beforehand? Is this end-to-end trained? (I think the paper would benefit if these points were made clearer there.)

What kind of pooling operation do you use? Max or average? And what is the dimensionality of the per-object latent feature?

How is the generalization success rate actually calculated? What does it mean that an agent “fails to solve the tasks”? I am assuming given the allowed number of steps?

For the loss of the feasibility prediction model, do you use the L_2 norm?

This is just notation, but in the reinforcement learning literature s’ usually denotes the next state, and $\hat{s}$ is used for an approximate state. Why did you decide to change this convention?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a framework for learning state and action abstractions from language-annotated demonstrations. The abstract actions and states are use to train a transition model in the latent space to learn the feasilbility of newer latent actions. This allows agents to generalize actions learned from language to longer, unseen tasks.

### Strengths
**Originalty:** The paper investigates a problem is not tackled in the literature but can realistically exist. The paper is a novel and creative framework for addressing this problem.

**Clarity:** The paper is well-writtten.

**Significane:**  This work has the potential to be impactful in language-based agent interactions. Furthermore, the framework can be adapted to other sequential planning domains. 

**Quality:** The problem described is well-motivated. The approach to addressing the problem is laid out clearly and simply and it reads reasonably. The model framework is creative and intuitive. The experimental design is sound and makes sense to test their claims and results support the claims made by the authors.

### Weaknesses
I don't have any major gripes. However, I found the description of the experimental domains lacking. Particularly I am not totally clear on the difference between the key-door and two-corridor environments.

### Questions
No questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a framework that learns state and action abstractions for planning. It does this by leveraging demonstrations with corresponding language annotations. These demonstrations are used to discover actions, which in turn is used to generate state abstractions. Finally, low-level policies are also learned corresponding to the high-level actions. The evaluation is done on two domains and the results show generalization wrt environments and objects.

### Strengths
1. The paper is well written. Except for the algorithm description, other parts like motivation, problem formulation, etc., are explained nicely.
2. The approach seems to be novel.

### Weaknesses
1. Other related approaches: 
* There are related approaches that use language to guide the abstraction process. E.g., Peng et al., the difference is that human input. Here, this paper gets it in the form of language-annotated task descriptions.
* Approaches like LIV (with PointCLIP instead of CLIP) can learn a latent representation, which can be used for planning. 

Peng et al., Learning with Language-Guided State Abstractions.

LIV: Ma et al., LIV: Language-Image Representations and Rewards for Robotic Control.

CLIP: Radford et al., Learning Transferable Visual Models From Natural Language Supervision.

PointCLIP:  Zhang et al., PointCLIP: Point Cloud Understanding by CLIP.


2. Reproducibility:
* I am not sure how reproducible the work is. There are a large number of details that are swept under the rug. And without an algorithm, it gets difficult to follow the paper. The supplementary material is also not submitted. 
* The inputs are not clear. 

3. Experimental Evaluation:
* I would suggest performing experiments for the accuracy of the feasibility function. 
* The experiments from the grid-like BabyAI setup are not convincing of generalization. The paper claims to withhold "red key" in training, but they can learn the model agnostic to such properties. So, this is more of a verification that their approach works. But as we can see, the accuracy for novel concept combinations is only 91\%.

Minor points:
* Incorrect citation: I do not believe Silver et al. learn (invent) new predicates as stated in the last two lines of page 1.

### Questions
1. Who provides the examples for prompting in Fig. 3 left?
2. The training is performed on how many tasks? Was the environment structure the same for all of them? Or was it changed in between tasks? If it was changed, was it ensured that the test environment configuration was not present in the training set? 
3. What is the reason for not achieving 100\% accuracy for novel concept combinations?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
