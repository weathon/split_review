# Generalizable Motion Planning via Operator Learning

- Decision: Accept
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
In this work, we introduce a planning neural operator (PNO) for predicting the value function of a motion planning problem. We recast value function approximation as learning a single operator from the cost function space to the value function space, which is defined by an Eikonal partial differential equation (PDE). 
    Therefore, our PNO model, despite being trained with a finite number of samples at coarse resolution, inherits the zero-shot super-resolution property of neural operators. %any desired resolution. 
    We demonstrate accurate value function approximation at $16\times$ the training resolution on the MovingAI lab's 2D city dataset and compare with state-of-the-art neural value function predictors on 3D scenes from the iGibson building dataset. 
    Lastly, we investigate employing the value function output of PNO as a heuristic function to accelerate motion planning. We show theoretically that the PNO heuristic is $\epsilon$-consistent by introducing an inductive bias layer that guarantees our value functions satisfy the triangle inequality. With our heuristic, we achieve a $30\%$ decrease in nodes visited while obtaining near optimal path lengths on the MovingAI lab 2D city dataset, compared to classical planning methods ($A^\ast$, RRT$^\ast$).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper casts motion planning as a problem of learning a value function modelled by an Eikonal PDE. The authors propose to view the solution as a non-linear operator mapping costs to value function solution, and learn this using fourier neural operators. The paper proposes to adjust standard Fourier neural operators by (1) encoding the obstacles, given by an SDF, and (2) enforce triangle inequality is satisfied. The paper argues that the neural operator formulation enables the querying to be done in at a higher resolution than the resolution of 2D maps used in training.

I appreciate the novelty of casting motion planning into an operator learning problem, and the approach presented is solid. My main concern is a critical one: the simplicity of the experimental setups -- the evaluations were all conducted in 2d "grid-world"-like environments (point mass moving in 2d layouts e.g. Fig 4.), whereas other methods of learning how to plan generally evaluate on higher degrees of freedom tasks, such as robot manipulators of 6 or 7 DOF.

### Strengths
See review above

### Weaknesses
This paper casts motion planning as a problem of learning a value function modelled by an Eikonal PDE. The authors propose to view the solution as a non-linear operator mapping costs to value function solution, and learn this using fourier neural operators. The paper proposes to adjust standard Fourier neural operators by (1) encoding the obstacles, given by an SDF, and (2) enforce triangle inequality is satisfied. The paper argues that the neural operator formulation enables the querying to be done in at a higher resolution than the resolution of 2D maps used in training.

I appreciate the novelty of casting motion planning into an operator learning problem, and the approach presented is solid. My main concern is a critical one: the simplicity of the experimental setups -- the evaluations were all conducted in 2d "grid-world"-like environments (point mass moving in 2d layouts e.g. Fig 4.), whereas other methods of learning how to plan generally evaluate on higher degrees of freedom tasks, such as robot manipulators of 6 or 7 DOF.

### Questions
How well does the learned planner scale wrt the dimensions of the search space? As most of the citations come from the robotics literature, I would like to see motion planning beyond 2D or 3D toy examples. Consider evaluation on robot manipulators with 6 or 7 DOF.

### Soundness
3

### Presentation
3

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
This paper introduces the novel use of neural operators to solve the Eikonal equation for motion planning in 2D and 3D environments. The proposed method takes an environment occupancy map, along with start and goal points, to predict the optimal value function for path planning in free space. By leveraging the generalization capabilities of neural operators, the authors demonstrate improved adaptability across different environments compared to conventional methods. Experimental comparisons with search-based methods and neural motion planners validate the effectiveness and computational efficiency of this approach.

### Strengths
1. Innovative Use of Neural Operators: The authors adopt neural operators, which have shown superior generalization in PDE-solving applications, suggesting potential advancements in both performance and scalability.

2. Generalization Across Datasets: Experimental results indicate the method’s potential to generalize across diverse environments, which is a noted advantage over physics-informed neural networks (PINN) approaches.

3. Computational Efficiency: The approach demonstrates fast computational performance for small-resolution cases, making it potentially suitable for real-time applications.

### Weaknesses
1. Scalability Constraints:
Since the method relies on grid-space convolutions, it faces intrinsic limitations in scaling to higher-dimensional spaces, a notable restriction for applications in manipulation tasks.

2. Dependence on Supervised Learning:
 The method’s reliance on supervised learning demands ground truth PDE solutions, which may be impractical to obtain in complex environments.

3. Presentation Issues:
 - Notation Clarity: The pipeline figure uses the same symbol for the SDF operator and PNO, leading to ambiguity. It would be clearer to differentiate these in the figure.
- The neural network structure lacks clarity. The description mentions $F^{-1}(R(F()))$, but it may be more informative to explicitly state the intermediate layers, e.g., $L = F^{-1}(R(F()))$, with a clear distinction that the output should be denoted as $\Phi $ rather than $L_M $.

4. Experimental Comparisons:
 The paper currently compares against VIN and NTFields, which are established but not necessarily state-of-the-art. Incorporating comparisons with more advanced methods like Differentiable Spatial Planning using Transformers [1] and Progressive Learning for Physics-Informed Neural Motion Planning [2] would provide a more comprehensive benchmark.

The original experiment struggled to fit the value function accurately, but adding the PINN loss has shown improvements. However, the current method has only been tested on environments with isolated cluttered obstacles. This makes it difficult to assess its ability to generalize to more complex scenarios, such as the maze-like Gibson environments, where optimal paths often require navigating through multiple turns.

### Questions
Despite its limitations in scaling and reliance on ground truth training data, the proposed method represents a promising direction for motion planning through neural operators. I have the following questions to further explore its potential:

1. Pure PINN Loss: Could pure PINN loss be used to train the network instead of supervised learning? An analysis of its generalization performance could reveal insights into the potential for unsupervised or semi-supervised learning.

2. Testing on General Geometries: The method’s scalability could be further assessed by testing on general geometries, as seen in [1]. This could help to understand whether the approach can extend to higher-dimensional space planning.

3. Visualization of Results: It would be more effective to display contour lines of the value function instead of only color representations. Contour lines could better reveal any artifacts in the value function, providing clearer insights into the method's performance.

[1] Fourier Neural Operator with Learned Deformations for PDEs on General Geometries

### Soundness
3

### Presentation
2

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
This paper proposes a method, called Planning Neural Operator (PNO), for approximating the value function of a motion planning problem, viewed as the solution operator to the Eikonal PDE. The authors claim to achieve generalizable motion planning by using a resolution-invariant architecture, which encodes obstacle geometries as well as goal positions. This is done by leveraging the Fourier Neural Operator (FNO) and the Domain-Agnostic FNO (DAFNO). The paper also proposed a method for integrating the learned operator as a heuristic into the A* algorithm which achieves a 33% decrease in the number of explored nodes while maintaining epsilon-consistent optimality.

### Strengths
- The paper, although math-heavy, was an enjoyable read. The authors did a very good job of presenting complex theoretical concepts simply while maintaining a good formalism.
- The authors provide a detailed literature review and clearly position the proposed approach within existing work  in traditional and neural motion planning.
- Experiments are conducted on multiple datasets, showcasing the performance of the method on different types of 2D and 3D environments of different resolutions. Results support most of the authors’ claims.

### Weaknesses
 - Several assumptions are made to justify the existence of the neural operator approximation. However, the reasoning behind these assumptions, and their implications in practical, real-world scenarios, are not thoroughly discussed. Specifically, the assumption of a proper policy existing for all start positions and the equicontinuity and uniform positivity of the cost function space are not sufficiently justified in the context of complex, real-world environments with sensor noise and imperfect actuation.
- The model’s performance for robots with high degrees of freedom (DOF) such as manipulators are not explored. This raises questions about the applicability of the approach to more complex, higher-dimensional tasks common in robotic motion planning. The experiments are limited to point robots in 2D and 3D environments, which does not fully demonstrate the method's capability to handle the complexities of articulated robots with kinematic constraints.
- While the paper mentions design decisions like encoding obstacle geometries and ensuring triangle inequality, the specific impact of these features is not thoroughly examined through ablation studies. It would be beneficial to quantitatively show how each architectural component contributes to the final performance, especially the modifications to the Fourier Neural Operator (FNO). For example, the paper does not provide a detailed analysis of how the choice of DeepNorm impacts the training stability and generalization performance compared to other normalization techniques. Also, the method's sensitivity to the parameters of the FNO layers, such as the number of modes and hidden dimensions, is not explored.

### Questions
- Could you provide more details on the intuition behind the assumptions required in the paper and how it relates to the practical application of your method in real-world scenarios?
- Have you tested PNO in real-world robotic setups beyond the synthetic and iGibson environments? If so, could you share results or insights on how PNO performs in tasks involving more complex real-world constraints or unstructured environments?
- How does the proposed method scale to tasks with significantly higher degrees of freedom (DOF) beyond the environments presented in the paper? Have you performed any scalability studies on more complex robotic systems?
- Could you provide more detailed ablation studies that show the contributions of specific components in your architecture, such as obstacle encoding, triangle inequality enforcement, and modified Fourier Neural Operator layers? This would clarify how each design choice impacts overall model performance.
- In table 1, do you have an explanation on why the success rate of your method particularly drops for the 16x16 maps ?

### Soundness
2

### Presentation
3

### Contribution
2
