# BaB-ND: Long-Horizon Motion Planning with Branch-and-Bound and Neural Dynamics

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Neural-network-based dynamics models learned from observational data have shown strong predictive capabilities for scene dynamics in robotic manipulation tasks. However, their inherent non-linearity presents significant challenges for effective planning. Current planning methods, often dependent on extensive sampling or local gradient descent, struggle with long-horizon motion planning tasks involving complex contact events.
In this paper, we present a GPU-accelerated branch-and-bound (BaB) framework for motion planning in manipulation tasks that require trajectory optimization over neural dynamics models. Our approach employs a specialized branching heuristic to divide the search space into sub-domains and applies a modified bound propagation method, inspired by the state-of-the-art neural network verifier $\alpha,\beta$-CROWN, to efficiently estimate objective bounds within these sub-domains. The branching process guides planning effectively, while the bounding process strategically reduces the search space.
Our framework achieves superior planning performance, generating high-quality state-action trajectories and surpassing existing methods in challenging, contact-rich manipulation tasks such as non-prehensile planar pushing with obstacles, object sorting, and rope routing in both simulated and real-world settings. Furthermore, our framework supports various neural network architectures, ranging from simple multilayer perceptrons to advanced graph neural dynamics models, and scales efficiently with different model sizes.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents BaB-ND, a GPU-accelerated Branch-and-Bound framework designed for long-horizon motion planning in robotic manipulation tasks that require trajectory optimization over neural dynamics models. Addressing challenges associated with non-linearity in neural network dynamics, BaB-ND utilizes a branching heuristic to divide the action space into sub-domains and a modified bound propagation method (inspired by neural verification methods like α, β-CROWN) to efficiently prune non-promising regions. This systematic approach allows BaB-ND to outperform some existing methods in tasks like object pushing, sorting, and rope manipulation, where contact-rich dynamics and high-dimensional action spaces are involved. The framework supports diverse neural architectures (e.g., MLPs, GNNs) and demonstrates scalability and superior planning quality in both simulated and real-world settings.

Overall, this work presents a novel idea, with a clear presentation, and I could increase my rating if my questions are covered during the rebuttal phase.

### Strengths
**Originality**:
This paper is quite original in its approach to motion planning by adapting the branch-and-bound (BaB) algorithm for neural dynamics (ND) models. Unlike existing methods, which typically rely on sampling-based or gradient descent approaches, this work creatively applies a modified bound propagation technique inspired by neural network verification algorithms, specifically the α,β-CROWN method. This adaptation is novel for addressing the inherent non-linearity and complexity of neural dynamics in long-horizon planning tasks. It might set a new direction in combining machine learning verification methods with motion planning.

**Quality**:
The research demonstrates rigor and of high-quality.
- Good amount of testing across diverse scenarios (planar pushing, object sorting, rope routing)
- Performance advantages over existing methods like Mixed-Integer Programming and sampling-based approaches
- Robust handling of complex, contact-rich environments
- The video covers the experiments and demonstrates the improvement over alternative methods

**Clarity**
The presentation of the paper is good.
- Well-organized structure and methodology explanation
- Effective use of visual aids and diagrams
- The step-by-step example of applying BaB on a 1D problem is particularly helpful
- (mostly) clear differentiation between BaB-ND and traditional verification methods

**Significance**
The work is important in several fronts.
- It addresses a critical challenge in robotic motion planning: managing complex, long-horizon tasks with contact dynamics
- The provided solution is -somewhat- scalable, when compared to an existing method
- Different neural architectures (MLPs to graph neural networks) are used, which demonstrates its applicability on different architectures, and hence different types of problems.

### Weaknesses
There are several weaknesses/limitations of the work:

**Limited Task Diversity**:
- Current evaluation focuses primarily on basic manipulation tasks (pick-and-place and pushing, relying on planar motions)
- Framework's applicability remains uncertain for:
  - Complex 3D manipulation with critical contact points and impact forces
  - Highly constrained environments requiring precise 3D motions of the full robot kinematic chain
  - e.g., Real-world scenarios like book reordering across shelves

**scalability**: (somewhat similar to the comment above)
- Despite GPU acceleration, potential bottlenecks exist:
  - Computationally intensive bound propagation
  - Extensive branching requirements
  - Challenges for real-time applications
- Paper would benefit from:
  - Discussion of potential optimizations for real-time use
  - Experiments measuring latency in time-sensitive scenarios
  - Strategies for reducing computational overhead

**Lack of Comparative Analysis**:  I acknowledge that it'd be out of scope, but still some remarks:
- Comparisons with traditional motion planners that use full state information might be interesting, especially considering the somewhat long runtime of BaB-ND + the training time for each task. Overall, that could provide a better context regarding trade-offs between:
  - BaB-ND's computational costs (including training time)
  - Performance of conventional motion planning approaches
  - Overall efficiency in practical applications

**Insufficient Hyperparameter Analysis**: The BaB-ND framework includes various hyperparameters, such as the choice of branching heuristic, bound propagation depth, and sampling rates. However, there is limited discussion or analysis on how these hyperparameters influence performance across different tasks or neural architectures. Since tuning these parameters is likely critical for achieving optimal results in different scenarios, an expanded study on hyperparameter sensitivity would be beneficial. For instance, sensitivity experiments could provide insights into the trade-offs between solution quality and computational efficiency, guiding practical implementation.

### Questions
- In the supplementary video, it is stated that planning time / horizon is the same for all methods. How would the performance of the baseline methods change if we increase the planning time? In the experiments, it is shown that BaB-ND outperforms other methods in almost all tasks. May it be the case that other methods have not yet found their optimal solutions?

- Can you prune enough sub-domains so that the algorithm does not end up sampling exhaustively? In which cases (or for which type of objective functions) can you provide an assurance that enough sub-domains will be pruned? Can you give a theoretical insight into it? More generally, since the proposed method relies on sampling, in which cases it performs poorly compared to the non-sampling methods?

- Why isn't there any sampling-based method for scalability comparison? It is expected for a sampling-based method to be more scalable compared to MIP (?).

- How is the close-loop control achieved and feedback received?  

- data collection: how are the variations (assuming there are) of the task achieved? 

- Fig.6: consistency on the plots is preferred. For rope routing, cost performance is reported for the open-loop scenario, whereas success rate is reported for the closed-loop. Why is it so?

- Could the authors discuss potential modifications for real-time application?

- Could the authors expand on hyperparameter sensitivity?

- Are there potential optimizations for early-stopping propagation in bound calculations? The current early-stopping approach helps avoid excessive error from deep-layer propagation, but it may not achieve the tightest bounds possible. Any chance on adative stopping based on some criteria/threshold?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a GPU-accelerated Branch-and-Bound (BaB) framework for planning in robotic tasks using neural dynamics models, employing α,β-CROWN for bound propagation. The framework supports various neural network architectures, such as MLPs and GNNs, but the model requires customization based on different scenarios, selecting specific architectures for tasks like object sorting and rope routing​.

### Strengths
1. The framework leverages bound propagation from neural network verification (α,β-CROWN) to optimize neural dynamics in planning tasks. By structuring the search space into sub-domains and pruning non-promising regions, it shows potential for handling high-dimensional, complex scenarios. 
2. BaB-ND effectively focuses on feasible solutions over global optimization, adapting BaB methods for motion planning in complex, contact-rich robotic tasks. It supports diverse neural architectures, such as MLPs and GNNs.
3. With GPU acceleration, BaB-ND hints at the potential to manage extended planning horizons and complex models

### Weaknesses
1. The code URL provided in the paper is currently unavailable.
2. Figure 6 has an ambiguous y-axis, making it difficult to understand what is being measured and, therefore, hard to assess the framework’s actual performance or effectiveness based on this chart.
3. Most experiments are conducted in 2D scenarios, and even the 3D rope manipulation task appears relatively simple, which raises questions about the framework's scalability to more complex 3D environments and interactions, especially with deformable objects.
4. Although a generalized pipeline is proposed, the framework’s actual scalability across more diverse and complex tasks remains unproven. The comparisons are mostly limited to similar methods, without broader baselines that might better validate its extensibility and robustness.
5. The current experiments focus on relatively simple tasks, leaving uncertainty about the framework’s effectiveness in more complex or varied scenarios. Custom neural network design for each task could make adaptation time-consuming and resource-intensive.
6. The framework’s success is sensitive to selecting suitable network architectures for each task. Without careful selection, mismatches could lead to substantial inefficiencies or even failure, indicating a high demand for expert design and tuning.

### Questions
1. Given that most experiments are based in 2D, what modifications would be necessary to extend the framework to more complex 3D tasks or interactions with deformable objects? Is the focus on 2D a practical choice, or does it reflect inherent limitations in handling higher-dimensional complexity?

2. Would including broader baselines from other methodologies provide a more comprehensive benchmark for evaluating the framework? Stronger comparisons could help clarify its extensibility.

3. How might the framework perform in a wider range of challenging scenarios? Additional experiments with more varied conditions would offer insight into its adaptability to complex tasks or novel object interactions.

4. Since each scenario requires a custom-designed network, how practical is this approach for real-world applications? What are the estimated time and resource requirements for designing and tuning a model for a new scenario, and could this affect the framework’s usability in resource-limited settings?

5. Does the current setup introduce complexity that might hinder practical implementation? If an optimal network is not chosen, how significantly would this impact performance, and are there ways to mitigate this dependency on precise network selection?

### Soundness
3

### Presentation
3

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
The paper presents an approach for solving complex long-horizon motion planning tasks using a GPU-accelerated branch-and-bound (BaB) framework. The primary innovation is the integration of bound propagation methods inspired by neural network verification, namely CROWN, to handle the non-linearity of neural dynamics models. This method allows for efficient partitioning of the search space and systematic pruning of sub-domains that cannot yield better solutions, focusing the search on promising areas. The authors demonstrate that BaB-ND outperforms existing sampling-based and mixed-integer programming (MIP) methods in handling contact-rich manipulation tasks like planar pushing and object routing. The framework supports various neural architectures and shows scalability, making it applicable to real-world robotic planning problems.

### Strengths
- The paper tackles an important and challenging problems in robot motion planning, especially in scenarios involving long-horizon, contact-rich tasks.
- The paper provides a solid overview of related work in neural dynamics, motion planning, and neural network verification, positioning the contribution well within the context of existing research.
- The use of a branch-and-bound (BaB) framework integrated with bound propagation methods adapted from neural network verification shows potential for enhancing motion planning capabilities.
- The proposed method is designed to support various neural network architectures, allowing applicability to different robotic models and tasks.
- The experiments are complex and challenging, showcasing the method’s applicability to real-world scenarios such as object routing and planar pushing.

### Weaknesses
 - The method section is highly abstracted, which leaves readers unable to connect theoretical concepts such as the objective function, inputs, bounds, and sub-domains to practical robotic manipulation problems. Explanations remain too abstract and disconnected from practical robotic tasks. Also, the paper does not detail the method sufficiently, particularly the bounding step, making it difficult for readers to understand the full implementation of the approach.
- Understanding the methodology relies heavily on prior familiarity with the CROWN method, making the paper less accessible to readers who are not already experts in neural network verification techniques.
- Although GPU acceleration is mentioned as a key advantage, the paper does not provide sufficient detail or evidence to demonstrate how GPU acceleration is implemented or its specific benefits.
- While the paper compares performance against sampling-based methods, the absence of Mixed-Integer Programming (MIP) as a baseline for evaluating the optimality of solutions is a significant oversight. Additionally, runtime performance is not benchmarked against methods like MPPI and CEM.
- The paper does not include an ablation study to show the importance of individual components or design choices in the proposed method, leaving gaps in understanding the contribution of each element.
- From a robotics perspective the use of a branch-and-bound framework with neural dynamics in contact-rich robotic manipulation seems novel, however, the novelty and contribution from a machine learning perspective is not clear.

### Questions
- Can you provide more details on the bounding step of the method? How are bounds estimated in a way that ensures meaningful pruning of sub-domains in practical robotic tasks?
- Could you illustrate the method using a specific example of a robotic manipulation task, detailing how abstract concepts like the input u and bounds map to task-specific elements?
- How is GPU acceleration implemented in your approach, and what specific parts of the framework benefit from it? Could you provide runtime comparisons with and without GPU acceleration?
- Why was Mixed-Integer Programming (MIP) not used as a baseline for comparing the quality of the solutions? Similarly, why were methods like MPPI and CEM not included for runtime performance comparisons?
- Have you considered performing an ablation study to show the contribution of individual components, such as the branching heuristic or specific modifications to the bound propagation method?
- Could you provide more details on the novelty of the approach from a machine learning point of view ?

### Soundness
3

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
4

### Summary
This work introduces a divide-and-conquer approach for planning long-horizon manipulation trajectories. The method relies on a dynamics function trained on simulated data and operates through branching, bounding, and searching.

### Strengths
The writing is clear and well-structured, and the appendix contents are helpful.

The concepts and formulation are well-defined, and the 1D toy example effectively validates the idea.

The method includes extensive experiments, both simulated and real-world, with comparisons to several baseline methods.

### Weaknesses
The specific novelty and distinctions of the proposed method compared to neural network verifiers are unclear, beyond its focus on model-based trajectory planning.

The robot experiments lack clarity, with important details omitted.

The limitations and potential future directions of this work are not discussed.

The learned dynamics function relies on a well-designed simulator, which may limit the scalability of this method to a wide variety of tasks.

The method assumes static initial poses for obstacles and goal regions, making it challenging to adapt to dynamic changes.

### Questions
What are the definitions of open-loop and closed-loop performance? They are unclear, making the results in Figure 5 difficult to interpret.

For data collection to train the dynamics function, thousands of episodes are gathered in the simulator. How is action sampling handled for each task? Are actions randomly generated? Is there a sim-to-real gap? Why not train an RL agent in the simulator instead?

Is it possible to extend the current method to scenarios where obstacles or goal regions are dynamic?

What is the action space or control signal for most tasks? It appears to be limited to translations in the 2D plane.

With a 20-step planning horizon, how many actions does the controller execute? What is the planner’s operating frequency?

It appears that much of the processing time is consumed by searching. It will dramatically increase computation time and workload when the action space includes both 3D translations and 3D rotations. Would this limit scalability to a full 3D action space?

### Soundness
3

### Presentation
3

### Contribution
2
