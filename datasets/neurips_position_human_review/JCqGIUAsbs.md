# Embracing Evolution: A Call for Body-Control Co-Design in Embodied Humanoid Robot

- Decision: Reject
- Scores: 4, 6, 8

## Abstract
Humanoid robots, as general-purpose physical agents, must integrate both intelligent control and adaptive morphology to operate effectively in diverse real-world environments. While recent research has focused primarily on optimizing control policies for fixed robot structures, this position paper argues for *“evolving both control strategies and humanoid robots' physical structure under a co-design mechanism”*. Inspired by biological evolution, this approach enables robots to iteratively adapt both their form and behavior to optimize performance within task-specific and resource-constrained contexts. Despite its promise, co-design in humanoid robotics remains a relatively underexplored domain, raising fundamental questions about its feasibility and necessity in achieving true embodied intelligence. To address these challenges, we propose practical co-design methodologies grounded in strategic exploration, Sim2Real transfer, and meta-policy learning. We further argue for the essential role of co-design by analyzing it from methodological, application-driven, and community-oriented perspectives. Striving to guide and inspire future studies, we present open research questions, spanning from short-term innovations to long-term goals. This work positions co-design as a cornerstone for developing the next generation of intelligent and adaptable humanoid agents.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
4

### Summary
The paper argues that for humanoid robots, the physical hardware morphology of the robot needs and can be feasibly optimized (evolved) along with the control strategies for performing locomotion and manipulation with them, in order to develop embodied humanoid intelligence. The authors formulate the humanoid co-design problem as a two-level optimization problem, where the outer loop optimizes over designs and the inner loop learns control policies for a particular morphology. The paper then discusses the perceived challenges of co-design and proposes strategies for alleviating them.

### Strengths
- The paper is generally well written, and I appreciate that the background about humanoid robots and robot learning is provided in an approachable way, which could help readers from a variety of backgrounds engage with the paper.
- I believe that Section 3.2 indeed presents some of the most pressing technical and methodological challenges for co-design frameworks. Discussing and summarizing these challenges is a nice contribution.
- Additionally, the proposed solutions to the above challenges discussed in Section 4 appear to be technically reasonable, and although significant future research is required along each direction, pointing the community in such directions is valuable.

### Weaknesses
- One major area of potential improvement is the handling of the alternative position. The authors state that the alternative view is that “The predefined and fixed physical structures are sufficient for supporting the development [sic] embodied humanoid robots”. But, most of Section 3.2 focuses on a different alternative view, which can be summarized as “technical barriers prevent current practitioners from performing co-design for humanoid robots”. There is some discussion about the importance of co-designing humanoid robots in Section 5. But it’s confusing that the alternative view is first brought up in Section 3.2 and discussed later. Further, the points brought up in Section 5 do not address precisely the point in the alternative view. 
- The novelty of co-evolving control and design is overstated. While this problem has not been well studied for humanoids, it also does not appear significantly different in problem formulation for humanoids.
- There are some awkward phrasings and imprecise notation in the paper, for example, “the RL algorithm” L159 could be phrased as “perform reinforcement learning” or omitted entirely (any generic way to optimize equation 1 is sufficient). Neither f_c nor epsilon are defined in Equation 2.

### Questions
- Do the authors have any thoughts or discussion about whether or not body-control co-design can enable or accelerate the progress of methodological or algorithmic development in embodied AI?
- I’m not sure that I agree that embodied AI requires agents to “actively explore, interact with, and learn from their environments in a continuous and dynamic manner”, as opposed to “passively learning from fixed datasets”. The majority of research still falls into the latter category and I believe this is an open question. Is this a critical distinction to make here? Why not allow the problem statement to encompass many possible approaches?

### Presentation
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper argues that humanoid robots’ control strategies and physical structures should evolve together through a co-design process, rather than the alternative view of optimizing control while treating the physical structure as a fixed constant. It emphasizes the advantages of jointly optimizing both aspects, demonstrating the approach’s efficiency and effectiveness with concrete examples. The paper outlines key challenges in joint optimization and proposes potential solutions, while also highlighting open questions and future research directions prompted by co-design.

### Strengths
- The paper argues its position clearly, supporting it with concrete arguments and examples.
- The paper’s position is quite relevant to the community. It identifies the alternative position and points out that most of the current research follows it. This could inspire valuable discussions in the community.
- Major challenges of jointly optimizing for the control strategies and physical structure of humanoid robots are identified, and the paper presents potential solutions and research directions to address them.

### Weaknesses
- The necessity for jointly optimizing for control and the physical structure seems weak. While the arguments make co-design preferable, they do not show it is essential. For example, for the point adaptive body shaping, this can be addressed by having separate predefined designs for each specialized scenario as we do now, not necessarily co-designing control and morphology. Regarding the point on fostering cross-disciplinary collaboration: why is such collaboration valuable beyond serving the purpose of co-designing control and morphology? The argument feels circular—co-design is said to be necessary because it fosters collaboration, and collaboration is deemed important because it supports co-design.
 
- The impact of jointly optimizing control and physical structure in existing work is not well analyzed. Is this co-design mechanism necessary for robots beyond humanoids? If so, why is it necessary? If not, what makes humanoid robots uniquely suited to require such co-design?

### Questions
- Is co-design necessary only for humanoid robots, or for robots in general? For existing work on co-design for other robot morphologies like quadruped robots, why and how is it necessary?
- For hardware developers, avoiding overfitting the physical structure to a narrow set of tasks would require optimizing control strategies across a diverse task set following the proposal in Section 4.3. Is this realistically feasible for companies primarily focused on hardware?
- The paper proposes learning a meta-policy across diverse tasks to prevent overfitting the co-design to limited scenarios in Section 4.3. However, wouldn’t this make it harder for the joint optimization to converge—an issue the paper identifies as a key challenge in Section 3.2.1?

### Presentation
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This position paper argues that humanoid robots should be co-designed—optimizing control policies and physical morphology together—rather than developing control systems for fixed robot structures.

Core Position: The authors argue that evolving the physical structure alongside control strategies is essential for achieving true embodied intelligence in humanoid robots, drawing on biological evolution, in which organisms adapt both form and behavior to their environments.

Main Contributions:

1. Formulation: Presents humanoid co-design as a bilevel optimization problem where control-policy optimization feeds into morphology optimization, subject to resource and behavioral constraints.

2. Feasibility Analysis: Addresses three major challenges that have limited co-design adoption:
(1) Computational complexity, (2) Physical evaluation difficulties, (3) Limited task scalability.

3. Necessity Arguments: Makes the case from three perspectives:
(1) Methodological, (2) Application, (3) Community.

### Strengths
The paper presents a compelling argument advocating for the integration of body-control co-design in humanoid robots, emphasizing its importance for advancing embodied intelligence.
The authors clearly argue for the necessity of simultaneously optimizing control strategies and robot morphology, drawing inspiration from the process of biological evolution. This perspective is well-supported by solid reasoning and provides effective approaches to achieve co-design. By organically combining control and morphology design, the authors suggest that humanoid robots can better adapt to real-world tasks and dynamic environments.
The argument is based on rigorous logical reasoning, and the paper also proposes practical methodologies such as strategic exploration, Sim2Real transfer, and meta-policy learning to ensure the practical feasibility of the co-design approach.

### Weaknesses
1. Implementation Challenges: The paper could provide more concrete examples of how co-design has been successfully implemented in current humanoid robotics or other fields. It would help readers visualize the practicalities of the proposed approach.
2. Alternative Approaches: The paper mainly focuses on co-designing both control and morphology. An alternative view that could be discussed further is the possibility of leveraging modular, adaptive control models that do not require redesigning the physical structure but instead adapt to varying tasks and environments using more flexible, robust control algorithms.
3. Scalability and Generalization: Although the co-design framework promises improved performance, scalability across diverse tasks and environments is a significant challenge. The paper could address how co-design might be generalized to a broader range of robots or non-humanoid systems, as the primary focus here is humanoid robots.

### Questions
Feasibility of Real-Time Co-Design: Given the significant computational complexity involved in co-designing both the robot's control and morphology, how do the authors foresee scaling these techniques for real-time applications, especially in dynamic environments with changing task requirements?

### Presentation
3
