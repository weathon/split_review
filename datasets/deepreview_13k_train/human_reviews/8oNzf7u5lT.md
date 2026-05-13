# Pylic: Leveraging Source Code for Planning in Structured Environments

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
This paper investigates the application of program analysis techniques to planning problems in dynamic environments with discontinuities in long-horizon settings. Traditional approaches rely on specialized representations, which are often tailored to specific problems and domains. In contrast, we propose describing the combined planning and control problem directly as a desired property of the execution of simulator source code. This representation is expressive, naturally providing a means to describe desired properties of even very dynamic and discontinuous environments. We show that, despite this generality, it is still possible to leverage domain knowledge by relating it to the simulator source code. We study the effectiveness of this approach through several case studies in simulated robotic environments. Our results show that in these environments, our framework can improve the efficiency in solving the control and planning problem, relative to standard numerical and reinforcement learning methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a novel method of using trace information from the source code of a simulator to more efficiently solve planning problems. The method is evaluated on three simulation examples where it compares favorably to RL (SAC) and sampling-based MPC.

### Strengths
- The idea of using the source code of a simulator to speed up planning is interesting and appears novel.
- The paper is fairly well-written, but there are a lot of things going on
- The benchmark results are encouraging

### Weaknesses
The fundamental limitation of this approach is that it needs a human to extract what they call "meaningful events" that serves as the - foundation of the planning tree. This makes comparisons against model-free methods like RL and sampling-based MPC rather apples-to-oranges. If this step was more automatic, or shown to be very simple, I think the paper would be much stronger.
- This is exacerbated by not using any standard benchmarks that I can see.  
- The performance difference compared to model-free approaches also does not appear that large in two of three experiments. Ultimately if this is useful or not probably depends on the users proficiency in the syntax of the proposed framework and the level of understanding of the simulator code. Not sure if a user study might help.

Minor:
- The success rate curves could also use a confidence interval (or quartiles).

### Questions
- Why did you not include any standard benchmark environments from e.g. RL as you are comparing against RL?

### Soundness
2 fair

### Presentation
2 fair

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
The paper describes an approach that utilizes code inspection techniques to locate discontinuities in a task together with user-provided critical junction points to formulate a tree-based search problem. The approach assumes that solutions between junction points can be found by local numerical search methods while the global sequencing is guided by the user-provided "meaningful events".

### Strengths
The general idea of the work is interesting in that it attempts to leverage program verification approaches and logic to solve complex global optimization problems.

### Weaknesses
While the general idea is interesting, there are many issues with the paper in its current form.

The paper argues that other methods rely on specialized representations, which makes them hard or inconvenient to use. However, the proposed method requires the user to specify so-called "meaningful events". Judging from the examples and the description, this would appear to be an even more onerous requirement as they have to be defined by the end-user instead of the designer of a general method for particular problem scenarios. This aspect is insufficiently discussed in the paper, making it unclear that this approach is practical in contrast to other methods such as reinforcement learning, model-based control, or Monte Carlo tree search.

The core aspect of the work revolves around tracing the code logic to find control flow statements. In that context, the paper repeatedly mentions simulators as the code to be traced. However, in the experiments, only one example traces through something akin to a simulator and in all other instances, some generic logic code is traced. Therefore, the mention of simulators is quite confusing as in no instance is a proper simulator, such as pybullet, mujoco, Isaac Sim, drake, etc., traced. It also remains unclear that the discontinuities in the simulation that this process should find are necessarily "telegraphed" by control flow statements rather than pure linear algebra, which the proposed approach would not appear to register. Tracing general program execution can still be interesting, as the experiments show. However, the description of the applications and properties described in the main body of the text is misleading. Without seeing the experiments, I would have expected the proposed method to be able to trace through complex physics engines as employed by Isaac sim or pybullet.

The proposed method uses quite a few components and joins them together. While an overview is provided in Figure 1, this figure is never used in the text to help the reader understand how things connect. As such, it is hard to follow where the different pieces go and how they interact. For example, there is a connection between user-defined events, code tracing, and trace predicates. This can be gleaned from the text to some extent, but making the connections more easily understood and more evident would improve the readability of the paper significantly.

The paper states that the local search is sufficient to find parameters to reach the next meaningful event. However, it is not mentioned how this can be guaranteed or why this should hold in the first place. Are there theoretical guarantees that can alert the user when this is impossible, or does the user have to add "meaningful event" specifications until things can be solved?

The experimental section, while containing several experiments, is lacking in detail. There are detailed descriptions of the experimental setups, yet the discussion of the results is unsatisfactory as they provide no real insight. Furthermore, the choice of baselines and problem setups is perplexing. The biggest issue is that some of the experiments would be ideally suited for Monte Carlo tree search methods, especially given the tree search nature of the proposed system, yet approaches based on this technique are absent. Another aspect is that the problem setups for different methods are not identical,  making it unclear whether the results are comparable. A good example of this is 4.2, where the proposed method operates on a state representation of button states while the RL and MPC baseline operate on an entirely different state space.

### Questions
- Some of the description and experimental tasks used give a task and motion planning vibe, would such tasks and methods be sensible comparisons for this work?
- Is the need to have traced control flow labels, predicates, and user-specified "meaningful events" not more challenging and domain-specific than representations required by other approaches?
- How can the assumption of local searches finding connections between the sequence of "meaningful events" be guaranteed?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an approach that uses the code of the simulator (or I would the analytical model) and a set of interesting events to solve problems with complex dynamics system. The approach first searches over a sequence of interesting events that reach a goal and then reduces achieving each interesting event (as I understand) as an optimization problem.

### Strengths
- The paper is easy to read. It nicely uses a running example to ground the concepts discussed in the paper. 

- The paper makes its assumptions clear which makes the paper really understandable.

### Weaknesses
While the paper presents attempts to solve an interesting approach, it has a few significant limitations:

- In my opinion, the paper seriously lacks novelty. It invents (or introduces) new terms for concepts that have long existed. E.g., the main contribution claimed by the paper is using **code of the simulator** for solving the problem faster. However, this is nothing but having access to an analytical model of the system. Why to complicate the paper? The second term would be the **meaningful events**. The events that are required or necessary to be achieved in order to reach the goal state. These is analogous to landmarks [1] or critical regions [2]. Landmarks and critical regions have been extensively used in planning and robotics literature. The paper fails to articulate a clear distinction between their 'meaningful events' and existing concepts like landmarks or critical regions, especially given that both aim to decompose complex problems into subgoals. The lack of a formal definition for 'meaningful events' further weakens this distinction, making it seem like a re-branding of existing ideas without substantial novelty.

- The approach requires the analytical of the model of the system as well as a set of landmarks or critical regions to be provided upfront. This does not only require a domain expert at the train time but at the test time as well. Which is infeasible to have. Especially, when a lot of research has been focused on learning these landmarks or critical regions automatically as well as approaches than learn policy without explicitly having access to an analytical model of the environment and treating the simulator as a blackbox. The need for a domain expert to define 'meaningful events' and their relationships for each new problem instance significantly limits the practical applicability of the approach. While the authors claim the expert provides general principles, the paper does not clearly define how these principles are instantiated for different problems within the same domain without requiring further expert input at test time. This lack of clarity makes it difficult to assess the true level of automation provided by the proposed method.

- It is not clear from the paper that how a sequence of low-level action is generated to reach each meaningful event. My educated guess is the problem is reduced to an optimization problem but it has to be clear from the paper. The paper lacks a detailed explanation of the optimization process used to generate low-level actions for achieving each 'meaningful event'. While the authors mention an optimization problem, they do not specify the objective function, constraints, or optimization algorithm used. This lack of detail makes it difficult to reproduce the results or compare the approach with other optimization-based methods.

- Lastly, the empirical evaluation is extremely weak. Especially, the choice of the baselines. Given that this approach is a model-based optimization approach. This should be compared with a hierarchical planning approach [2,3,4] or a hierarchical optimization approach [5] or a model-based RL approach.

### Questions
Please refer to the previous section.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
