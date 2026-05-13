# Hierarchical Object-Oriented POMDP Planning for Object Rearrangement

- Decision: Reject
- Scores: 6, 6, 3, 5

## Abstract
We present an online planning framework for solving multi-object rearrangement problems in partially observable, multi-room environments. Current object rearrangement solutions, primarily based on Reinforcement Learning or hand-coded planning methods, often lack adaptability to diverse challenges. To address this limitation, we introduce a novel Hierarchical Object-Oriented Partially Observed Markov Decision Process (HOO-POMDP) planning approach. This approach comprises of (a) an object-oriented POMDP planner generating sub-goals, (b) a set of low-level policies for sub-goal achievement, and (c) an abstraction system converting the continuous low-level world into a representation suitable for abstract planning. We evaluate our system on varying numbers of objects, rooms, and problem types in AI2-THOR simulated environments with promising results.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a framework for the multi-object rearrangement problem within a Partially Observable Markov Decision Process (POMDP) setting. The authors introduce a hierarchical, object-oriented POMDP framework that utilizes a high-level planner to generate sub-goals and deploys low-level policies to accomplish these sub-goals effectively. To benchmark their approach, the authors present a new dataset, “Multi RoomR,” designed to address more complex scenarios. This dataset includes a larger number of objects (10 objects) and more extensive environments (2-4 rooms), providing a more challenging testbed. The authors evaluate different variants of their method on this new dataset and two existing benchmarks, demonstrating that their framework achieves performance comparable to the method with perfect knowledge, even under partial observability constraints.

### Strengths
1. The authors demonstrated that their framework in a partial observability setting achieves results comparable to those obtained with perfect knowledge.
2. The new dataset introduces more complex scenarios, which is evident from the performance gap. However, additional details about these scenarios would strengthen their contribution, and I suggest they provide further explanation, perhaps in the appendix, to clarify the dataset’s design and the specific challenges it presents.

### Weaknesses
1. I find the work is incremental with limited novelty “Zheng et al. (2023) and Zheng et al. (2022) extend this formulation to perform object search in 3D environments. However, they are all limited to the task of object search and do not include any tasks that require rearrangement. In our work, we build on their formulation of object-oriented POMDP and extend it to include rearrangement actions and their corresponding belief updates.” (lines 128-132). Despite, I find you have added a hierarchical POMDP planning as well, but I find it already in the literature, for example [1]. Adding a more distinct methodological advancement or exploring further applications beyond rearrangement might strengthen the impact of this work.

2. The paper lacks details about the newly introduced dataset, which is a key part of the stated contributions in the introduction. For instance, specifics on the types of objects included and the rationale behind their selection are missing. Additionally, there’s little information on how the scenarios were designed—such as the criteria for object placement, room configuration, or how these factors contribute to the complexity of the rearrangement tasks. Providing this information, perhaps in the appendix or a dedicated section, would give readers better insight into the dataset's structure and its intended challenges, thus strengthening the contribution.

3. Their method is evaluated only against variants of itself, lacking comparisons with other baseline approaches. This makes it difficult to assess the true advantages of their approach. I would expect, at a minimum, an ablation study that removes the object-oriented hierarchical planning component to demonstrate its effectiveness compared to flat planning methods.

### Questions
**Minor Improvements (Not considered in the score)**

1. BeliefUpdate instead of UpdateBelief function → line 10 in Algorithm 1

**Questions:**

1. Could you clarify your statement at the end of Section 1, where you describe the system as "an end-to-end planning system"? My understanding is that the detection model and low-level policies are trained independently, suggesting a modular rather than fully end-to-end approach.
2. What is the last row of Table1?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses a variation of a challenging POMDP setting, an object rearrangement task over multiple rooms, with imperfect object detection. The authors introduce a hierarchical approach to a solver, with planning over a computed abstract state, and trained low-level policies to execute high-level plans. The work tests this method on existing object rearrangement tasks, and introduces a dataset of additional, harder tasks, based on the AI2Thor simulator. The authors also provide experimental evaluations of their solver on these domains.

### Strengths
The paper has several strengths, with a new method proposed for a relatively novel setting, with experimental results and a contribution to the field in the form of a dataset of tasks. On originality, the paper tackles a more challenging extension of the multi-room rearrangement problem, i.e. adding imperfect detection and integrated decision making. They additionally do not assume perfect navigation, motion planning or manipulation, instead having trained or computed low-level policies. The work contributed is mostly of high quality (with some reservations described below), with experimental results that demonstrate their method works in harder domains (that were also contributed and represent a meaningful improvement over the current domains). The lack of assuming perfect object detection and perfect low-level control renders this contribution significant to the field.

### Weaknesses
However, there are some concerns with the paper. Firstly, the paper's presentation and clarity desperately needs to improve. Specifically around sections 3, 4.1, and 4.2, there are many open questions, missing details and unclear statements around the task definition and setup. For instance, how the agent works with the 2D and 3D maps, how does it learn information about the receptacles at the beginning, or how the observations are discretized before being passed to the belief update is unclear. These can impact the evaluation of the results, making the environment and task easier than initially understood, and could potentially rely on unrealistic assumptions, for which is there is also no discussion on. I have listed a lot of questions I had around this section later on, and I can only be confident in the results provided, if the authors can improve the clarity of the paper here. 

Additionally, there are other concerns with the results. The authors claim in Section 6 that existing baselines differ from other work in key aspects. I think a detailed comparison between your domain and method, versus other selected variants of the task and accompanying methods would significantly improve  the quality of the paper's results.  At the moment, all the authors say is:

> The primary distinction lies in the prior knowledge available to our system: we are given information
about the classes of objects to be moved, whereas other systems operate without this advantage.
but do not cite other systems or prior work that studies the other settings. 

Further, they claim that:

> In particular, while existing systems report initial visibility of approximately 60% of target objects
at the outset of their tasks, our scenarios present a more demanding exploration challenge. Only
about 20% of the objects are initially visible in our problem settings, necessitating more extensive
and strategic exploration. 

but again, lack a reference for this information. Additionally, from a brief overview, it appears that [Mirakhor et al. 2024](https://ojs.aaai.org/index.php/AAAI/article/view/28902) (note, it was published before the period ICLR allows for concurrent work) is a relevant comparison, as they operate in similar conditions (i.e. multiple rooms, rearrangement task, with similar setups such as swap and blocked goal cases) and provide similar contributions (i.e. novel planner and new dataset). I want to see how the proposed method and provided datasets compare, to contextualize the effectiveness of this approach. 

Lastly, the authors mention this (lines 64, 508), but do not elaborate on this in the Limitations section. The proposed method requires a factored object-oriented state representation, and the proposed belief update and abstraction method rely on this fact as well (see enumerations over objects in Algorithm 2 and "Generating Abstract State"). This assumption is fairly strong, and presents a stumbling block in environments where object classes might not be fully known, i.e. imagine you see an unknown object that's blocking the goal location for a known object. I'm not suggesting that the proposed method needs to be able to handle such cases, but a fuller discussion of limitations needs to go beyond just the independence assumption and include ideas of how this might be relaxed in the future or how other methods in literature handle such cases.

### Questions
Questions:
- it is not clear how the agent generates the 2D map. The paper says it discretizes the world into grids of size 0.25m, but how is that done? Does the environment provide it? If not, how is it computed from the sequences of observations during the exploration phase? It's even less clear how the agent generates the 3D map mentioned in line 154. 
- The setup of the task is unclear. Is the first phase of exploration (where the agent "traverses the world" and "gains location information about the receptacles") something that the agent has to to plan how to do and output a sequence of actions? Or is this information provided by the environment? How does the agent know what the type of the object is during this phase? From the previous paragraph, the environment simply outputs the RGBD image of the current view from the agent POV, the location and if the action was successful. If the agent does have to do this, you must include more detail about how this works, and how it interacts with the planning system provided. 
-  The definition of the abstract POMDP is not clear. What change does the 'object independence' assumption make to the mathematical formulation of the OO-POMDP provided above? You provide some detail in the observation model bullet point but you reference "conditional independence" here and "object independence" above, so it's not clear to me what the relationship is between this and the above's "abstract" nature. My suggestion is to describe the overall system first (like the initial paragraph of section 4.3), since that provides much needed context to understand your formalism. Alternatively, I would try and make the abstraction system clearer when you define the abstract POMDP. The current presentation is very confusing. 
- How are the object locations in the ground truth image observation discretized to the 2D map? is this done by the environment or the perception system? The understanding is the perception system just runs object detection and grabs the 3D location via the depth map. 

Nits (not affecting score):
- typo on line 87 in caption (sawp -> swap)
- typo on line 354 (the OO-POMDP planner,uses Partially)
- typo in line 162, the title of section 4 should have the full form of the acronym, HIERARCHICAL OBJECT ORIENTED POMDP (HOO-POMDP), and should have a space between oriented and the parenthesis. 
- formatting of line 230 is wrong (should be in latex math mode, something like: [$cost = -1 \times N_{a}$] where $N_{a}$ is the number of required actions). 
- typo in line 248, space should be there between z and This
- the section in lines 196 to 201 are really difficult to read because of how compressed the math definitions are. it would be good to expand them to be easier to read.
- typo in line 212 (null is malformed)
- no need to redefine the acronym in line 316
- space around hypen in line 323
- randomly repeated twice in line 369
- A* is formatted incorrectly in line 380.
- missing period on line 452
- minor, but please bold the best result in the results Table 1, or otherwise easily indicate which performed the best.

### Soundness
3

### Presentation
2

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
The approach presents a POMDP based hierarchical planning approach for object rearrangement in multi-room settings. As far as I understand, the approach starts with high-level and low-level actions and performs hierarchical POMDP planning. Before the planning, the approach runs a SLAM equivalent  and builds a map of the environment. After, it performs POMDP planning and executes actions. The paper evaluates the approach in AI2THOR multi-room settings.

### Strengths
Object rearrangement, i.e., object pick and place tasks are important. The idea that only a subset of objects are visible and the overall setting is a POMDP is important for long-term generalist robots. 

The also addresses problems with block paths where it has to re-arrange objects in order to free up the space in order to move. This problem is rarely handled by many approaches as it is a hard problem.

### Weaknesses
The paper suffers from the following weaknesses: 

- **Lack of clarity**: A few claims in the paper are not clear and unsubstantiated. E.g., 
    - It is unclear what kind of hierarchies are being used in the paper after mentioning it multiple times throughout the paper. The paper mentions about high-level subgoals and low-level actions, however, never defines what constitutes as a high-level subgoal and what actions are low-level actions? The problem definition describes actions but doesn't make the distinction. The paper should clarify this. Specifically, it is not clear if the high-level actions are simply a sequence of waypoints or if they involve more complex decision making. The paper needs to explicitly define the action space for both high and low-level components and how they interact.
    - The paper assumes that whether an action is executed successfully or not is known. How does it ensure this in a POMDP setting where there is a probabilistic observation model. It is not clear how the system determines action failure given that the state is only partially observed. The paper needs to explain how the system differentiates between a failed action and an unsuccessful observation, given that both can lead to the same perceived outcome.
    - The transition model includes a "PickPlace" action. Is it a single action? If it is does it mean the agent can take this and the object magically transforms to the target location? If it is not a single action, then what is the sequence of actions that are executed when this action is called? The paper needs to clarify the mechanics of this action within the transition model and how it interfaces with the low-level control.
    - The approach compares in settings where the agent has to remove obstacles in order to move from one location to another. This is good! However, how is known that picking some action would free up that space? It requires more than a object oriented state space which the paper doesn't clearly explain. Specifically, how does the system reason about the spatial relationships between objects and how does it update its belief about the environment when an object is moved? The paper needs to provide a more detailed explanation of the state representation and how it enables such reasoning.
    - It is unclear how the approach collects initial belief of the object location to even build any policies? The paper needs to clarify how the initial belief is formed and how it is updated over time, especially given the partial observability of the environment. It is not clear how the system handles the initial uncertainty about object locations and how this uncertainty is incorporated into the planning process.

- **Lack of Novelty**: The paper claims that this the first approach that does object rearrangement in multiple rooms formulating it as a POMDP and the existing methods assume object locations. However, most of the current approaches such as TAMP (Curtis et al. 2022, Shah et al. 2020) operate in continuous state and action settings. The presented approach operates in discrete state and action spaces making the problem much simples. It is unclear how the approach is any different from any existing POMDP solvers? The paper needs to clearly articulate the novelty of their approach compared to existing POMDP solvers, especially given that they are operating in a discrete state and action space. The paper should also discuss the limitations of their approach compared to TAMP methods that operate in continuous spaces.

References:

Shah, Naman, et al. "Anytime integrated task and motion policies for stochastic environments." 2020 IEEE International Conference on Robotics and Automation (ICRA). IEEE, 2020.

Curtis, Aidan, et al. "Long-horizon manipulation of unknown objects via task and motion planning with estimated affordances." 2022 International Conference on Robotics and Automation (ICRA). IEEE, 2022.

### Questions
Please refer to the weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper deals with the problem of Multi-room rearrangement using a Hierarchical POMDP approach. The problem is difficult as it involves a number of difficulties including combinatorial expansion in complexity with increasing number of objects, partial observability due to limited field of view, scalability etc. The paper tackles the partial observability by maintaining an object oriented belief state to account for the possible locations of the objects. From this belief, the object state is abstracted which indicates whether the object is picked, placed, is held etc. Based on this state space for all the objects, the POMDP planner generates a high-level action to be executed such as the PickPlace, Move, Rotate etc. These high-level actions are then executed by the low-level policies which are heuristic as well as RL based. The paper claims to achieve a scalable and efficient rearrangement plan in Multi-room rearrangement scenarios. The paper also introduces a novel dataset MultiRoom R.

### Strengths
- The paper tackles a very complex and understudied problem of Multi-room rearrangement.
- Usage of POMDP based planners to effectively address uncertainities in a large multi-room space is very interesting.
- The supplementary video was good.
- The paper also presents a new dataset Multi RoomR which includes "blocked path scenarios" as an additional complexity in rearrangement.

### Weaknesses
 - **Uncertainty over objects start locations :** As stated in the paper line 338-339 : “The location $pick_i$ is sampled based on the belief distribution of where the object could be…” So for an unseen object, is the initial belief distribution a uniform probability over the entire 2D map? If yes, doesn’t it imply that your planner starts execution based on a randomly sampled location? Doesn’t it make planning less effective? Moreover, for predicting $loc_i$ of each object, wouldn’t the use of any common sense priors make the $loc_i$ prediction better and lead to faster convergence?
    - Don’t you think it would be better to use some commonsense knowledge about the object-receptacle-room relationships as a bias for belief initialization and update? Because in indoor scenarios, multiple methods have shown that the application of commonsense knowledge for indoor environments aids in planning - Sarch et al.[1], Kant et al.[2] and Mirakhor et al. [3,4].
-  **Comparison Results :** This paper shows no comparison study with the existing state-of-the art (SOTA) methods. As stated in Sec 2 : Related Work - Mirakhor et al. [4] addresses the multi-room rearrangement problem. Even other rearrangement methods that show results in single room rearrangement such as Gadre et al.[5], Sarch et al.[1] and Trabucco et al.[6] should be compared with to ground the claims of this paper. In fact, all these methods have shown their results in Ai2Thor. As stated in Line 507-508 the author mentions that they have an advantage over the SOTA method because “classes of objects to be moved are known” - Is it known for every rearrangement scenario, if so why do you need it? Or Is this method limited to only these classes of objects? Please clarify. Also, as you stated in Line 509-513 that your problem initialization is much more difficult due to initial object visibility. What is the reference or study for the claim on the existing methods initial visibility being approximately 60%? Please show empirically how difficult the problem becomes with variations in the percentage of initial object visibility.
- **Scalability :** To understand whether this method is scalable to an increasing number of objects and rooms, more results need to be shown with the number of objects varying from 5, 10, 15 say up to 20 on the same dataset. Similar results can be shown with the number of rooms varying from 2,3,4 & 5, keeping the number of objects constant. Presently, the paper shows results for only 5 objects on RoomR and Procthor, whereas it shows results for 10 objects on Multi-RoomR. This makes it difficult to establish a trend for results with an increasing number of objects and rooms.
- **Ablation study :** The two baselines - PK and PD used in the paper study only the perception efficacy, what about the planning efficacy? Can you replace your planner with some alternatives such as a classical traveling salesman problem (TSP) solver, an optimizer based OR-Tools[7] planner, a greedy planner etc. This will give an insight of how close to the optimal is this planner and how much of an improvement is this method over the heuristic strategies.
- **Novel Dataset (Multi RoomR) :** As far as I know, ProcThor has multi-room scenarios with up to 5 rooms and about 20 objects. But, the authors have stated in Line 418-420 about ProcThor having - “2 rooms, 5 objects”. Are you sure about this? This begs the question regarding the motivation of the new dataset - Multi RoomR? What was missing in ProcThor? What is the object, receptacle, room type distribution in the new dataset? How do we gauge the complexity of this new dataset, if there are no comparison results with SOTA methods?
- **Metrics and problem configurations :** To show the efficacy of planning, will it now be more beneficial to show the time and distance the agent took to solve the entire task? Moreover, to highlight the difficulty of partial observability, can you specify how many or what percent of objects are initially visible and how many actions or time does the agent take to find them?

### Questions
Same as the Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
