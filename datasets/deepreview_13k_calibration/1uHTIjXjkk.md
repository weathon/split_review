# Potential Based Diffusion Motion Planning

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 1, 5, 5

## Abstract
Effective motion planning in high dimensional spaces is a long-standing open problem in robotics. One class of traditional motion planning algorithms corresponds to potential-based motion planning. An advantage of potential based motion planning is composability -- different motion constraints can be easily combined by adding corresponding potentials. However, constructing motion paths from potentials requires solving a global optimization across configuration space potential landscape,  which is often prone to local minima. We propose a new approach towards learning potential based motion planning, where we train a neural network to capture and learn an easily optimizable potentials over motion planning trajectories. We illustrate the effectiveness of such approach, significantly outperforming both classical and recent learned motion planning approaches and avoiding issues with local minima. We further illustrate its inherent composability, enabling us to generalize to a multitude of different motion constraints. Project website at \href{https://energy-based-model.io/potential-motion-plan}{https://energy-based-model.io/potential-motion-plan}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper seeks to address the problem of motion planning using a novel potential based method that leverages diffusion models. The main contribution lies in the proposed compositional potential based diffusion motion planning with motion plan refinement, as well as the experiment comparison against multiple baseline algorithms including evaluations on a real-world dataset.

### Strengths
+ The idea of leveraging recent advance in diffusion models for potential based motion planning is interesting.

+ The paper is well written in general that clearly presents the basic idea and how the algorithm works.

+ Experiments on simulation and real-world dataset are provided to demonstrate the effectiveness of the proposed method.

### Weaknesses
 - The literature review of motion planning is quite substandard. Authors are strongly encouraged to discuss the comparison against reactive local planning methods with collision avoidance such as velocity obstacles and safety barrier certificates.

- While the idea of using diffusion model is interesting, the paper fails to justify how the introduction of diffusion model could overcome local minima issues suffered from traditional potential field based approaches. In fact, all the static obstacles in the provided environment examples in Fig. 1-3 and Fig. 7 are convex and without any overlaps, where local minima may not exist even if using traditional potential field based planning.

- According to Algorithm 1, it seems the presented diffusion motion planning is a single-query planning technique that would require re-training for every different pair of start and goal configurations, which raises concern about the computation efficiency.

- It is unclear whether the presented planning method has any guarantees or empirical analysis in terms of collision avoidance and completeness. For instance, how to prove the denoising process in Eq. 10 does not introduce potential collisions of the new plan?

### Questions
Besides the items discussed above (see "weakness"), please find the additional questions in the following:

1. Could authors provide additional results showing the planning performance of the diffusion-based approach in environments with concave obstacles? With the given examples in Fig. 1-3 and Fig. 7 where only convex obstacles are presented, it is difficult to evaluate the improvement over local minima compared to traditional potential field based planning.

2. Could authors provide formal theoretical analysis to justify the presented method is free of collisions and comment on the optimality and completeness? For example, it seems the denoising process from Eq. 10 has no guarantees on collision avoidance for the new path.

3. Does the proposed diffusion motion planning need to be re-trained for every single pair of start and goal configurations? Could the algorithm be used for kinodynamic planning where the way two consecutive waypoints connect is constrained due to the kinematics and dynamic constraints of the robot model?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a potential field motion planning approach which uses score matching to learn energy functions which represent the attractor and repulsor potentials. The potentials are then combined via simple summation, producing a velocity policy where trajectories can be rolled-out. The method is pretty straightforward, and the paper easy to follow. The paper demonstrates the applicability of the method on pedagogical examples. 

My main concerns with the paper is as follows:

1. The introduction states that potential field methods have "fallen out of favour in recent years", this is not quite true, as reactive motion generation approaches, notably Riemannian Motion Policies (RMPs) (Ratliff, 2018) and Geometric Fabrics (GF) (van Wyk, 2022) are in effect potential field methods. RMPs and GFs are highly sophisticated frameworks, capable of composing potentials defined on multiple task-spaces, and combine each potential according to a weighting metric. This is in contrast to the simplistic approach proposed in this paper, which simply considers potentials in the same task space, and then naively sum everything together. 

2. Score-matching learns energy functions where the parameterised function's gradients match the target function, however, the energy function values themselves can be very different. This makes directly summing the potentials very unsound. What if the energy values of one obstacle is higher than that representing another obstacle?

3. SDFs are ubiquitous in robotics, and can be thought of as a potential that increases as one moves away from the surface of the obstacle. What would be the motivations of learning a potential to represent the obstacle when ones could build an SDF, which can model complex scenes very efficiently, and use that as the repulsor? 

4. The obstacle potential should not be in the C-space, it would be much easier to be constructed in the workspace, as it depends on the geometry of the workspace. However, the attractor potential is defined in the C-space. It is unclear how you combined these via simple addition.

### Strengths
See above.

### Weaknesses
The paper proposes a potential field motion planning approach which uses score matching to learn energy functions which represent the attractor and repulsor potentials. The potentials are then combined via simple summation, producing a velocity policy where trajectories can be rolled-out. The method is pretty straightforward, and the paper easy to follow. The paper demonstrates the applicability of the method on pedagogical examples.

My main concerns with the paper is as follows:

1. The introduction states that potential field methods have "fallen out of favour in recent years", this is not quite true, as reactive motion generation approaches, notably Riemannian Motion Policies (RMPs) (Ratliff, 2018) and Geometric Fabrics (GF) (van Wyk, 2022) are in effect potential field methods. RMPs and GFs are highly sophisticated frameworks, capable of composing potentials defined on multiple task-spaces, and combine each potential according to a weighting metric. This is in contrast to the simplistic approach proposed in this paper, which simply considers potentials in the same task space, and then naively sum everything together.

2. Score-matching learns energy functions where the parameterised function's gradients match the target function, however, the energy function values themselves can be very different. This makes directly summing the potentials very unsound. What if the energy values of one obstacle is higher than that representing another obstacle?

3. SDFs are ubiquitous in robotics, and can be thought of as a potential that increases as one moves away from the surface of the obstacle. What would be the motivations of learning a potential to represent the obstacle when ones could build an SDF, which can model complex scenes very efficiently, and use that as the repulsor?

4. The obstacle potential should not be in the C-space, it would be much easier to be constructed in the workspace, as it depends on the geometry of the workspace. However, the attractor potential is defined in the C-space. It is unclear how you combined these via simple addition.

### Questions
See above.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides a framework to adapt the diffusion model to the motion planning task. By considering the diffusion model as the potential-based energy model, the compositionality can be achieved by the addition of multiple independent energy models. Empirical results show that the learned model works well from 2D to 14D, and can generalize to unseen cases. Real-world datasets are also evaluated.

### Strengths
1. The paper is overall easy to understand.

2. The experiment looks promising.

### Weaknesses
 1. Typos. 
1a. Page 6, in the caption of Figure 4, there should be a space before '(b)'. And this caption text is not finished. 
1b. Page 6, at the end of this page, 'spasrse' should be 'sparse'.

2. Though the compositionality seems to work well, the theoretical side is unclear. See question 2.

3. Some settings of the experiments need to be further clarified to evaluate the paper better. See question 3.

### Questions
1. About the formulation of the compositionality:

- 1a: It seems that the unconditioned score function (c=∅) occurs only in Line 7 of Algorithm 1. Equation 6, 7, 8 simply ignores this term and combines all the conditional scores. Which one is actually used?

- 1b: If Line 7 of Algorithm 1 is the one that is actually used, it differs from the papers (Equation 9 of [1]), in the sense that there is no subtraction by the unconditioned score. Why does the author choose such a form? Isn't this wrong if applying Bayes' theorem with Equation 10 from [2]?

- 1c: Still about Line 7 of Algorithm 1: Why does the unconditioned score use $E_{\theta}^1$? What is special about $E_{\theta}^1$ compared to the other $E_{\theta}^i$?

2. About the theory side of the compositionality: 

- 2a: The basic assumption for Equation 10 from [2] to work is that all the conditions must be conditionally independent. Wouldn't this assumption be violated in this paper's experiment settings? For example, as a scenario mentioned in the paper, if C1={o1,o2,o3,o4} and C2={o3,o4,o5,o6}, will C1 and C2 still be conditional independent?

- 2b: Even the conditional independent assumption holds for t=T, for the intermediate t, is such an assumption still guaranteed, especially the distribution of $x_t$ now is actually affected by these conditions?  

3. About the experiment settings:

- 3a: What is the representation of the dynamic obstacles? Is it a vector consisting of the configurations from all timesteps in the trajectory?

- 3b: Since the dataset is generated from BIT*, why not compare it as a baseline?

- 3c: A general impression of the diffusion model is that it takes a long time to generate samples. Why is the planning time here lower than the other baselines? Does the planning time also include the sampling time of the diffusion model and the finetune time? Is there any additional optimization you did to speed up the process?

- 3d. For the real-world dataset, is it possible to evaluate the model's success rate systematically (like overlap on pixels)? It is hard to parse the normal controller and the model's performances solely from images.

- 3e. What is the timeout condition for the planning? 

- 3f. Are the metrics averaged over all the cases, or only the successful cases?

[1] Ajay, A., Du, Y., Gupta, A., Tenenbaum, J., Jaakkola, T., & Agrawal, P. (2022). Is conditional generative modeling all you need for decision-making?. arXiv preprint arXiv:2211.15657.

[2] Liu, N., Li, S., Du, Y., Torralba, A., & Tenenbaum, J. B. (2022, October). Compositional visual generation with composable diffusion models. In European Conference on Computer Vision (pp. 423-439). Cham: Springer Nature Switzerland.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a new approach to motion planning in high dimensional spaces using potential-based motion planning. Potential-based motion planning allows for the combination of different motion constraints by adding corresponding potentials, but it often suffers from local minima. The proposed approach involves training neural networks to learn easily optimizable potentials over motion planning trajectories, resulting in improved performance compared to classical and recent learned motion planning approaches.

### Strengths
The strengths of the paper are as follows:

1) They introduce a new approach to motion planning in high dimensional spaces using potential-based motion planning, which offers the advantage of composability by combining different motion constraints with corresponding potentials. 

2) The proposed approach trains neural networks to learn easily optimizable potentials over motion planning trajectories, resulting in improved performance compared to classical and recent learned motion planning approaches. 
 
3) The effectiveness of the approach is demonstrated by outperforming existing classical and learned motion planning algorithms. The approach showcases the composability of motion planning, allowing for the generalization to multiple sets of motion constraints and an increased number of objects.

4) The results and comparisons are extensive.

### Weaknesses
The weakness of the paper are as follows:

1) For higher dimensions, sampling based algorithms have proven to be the best choice. The authors have considered RRT* as the sampling based algorithm for comparison. Please note that RRT* is a old method. The authors must strive to compare their methods against recent state of the art approaches such as Informed RRT* [1], Fast Marching Tree (FMT*) [2], Batch Informed Trees (BIT*)[3], RABIT* [4] and ABIT* [5].

2) I worked on sampling based algorithms for a while now and the order of magnitude improvement from RRT* to ABIT* is 30 times more.

3) The authors must cite sufficient state of the art papers on sampling based motion planning and provide more convincing arguments as to why their approach must be preferred over these state of the art sampling techniques.

4) Furthermore, all the above mentioned algorithms have asymptotic optimality guarantees i.e. the cost of the feasible path converges to global optimal path in the limit of large number of samples.

5) In Fig. 4, I do not think it makes sense to measure the success rate for RRT* or other sampling based algorithms. This is because RRT* using collision checking modules and the RRT* is guaranteed to find a feasible path if it exists (proven in original RRT* paper). Since you are using NNs in your approach and other approaches under comparison, it makes sense to measure the success rate.

### Questions
1) A thorough literature review must be made for sampling based algorithms and convincing arguments on why your approach must stand out must be made in the introduction as well.

2) Comparisons with state of the art such as ABIT*, RABIT*, Informed RRT* must be made.

3) Do you have guarantees for your approach.

4) Since you are using NNs, there is no guarantee that the success rate would be 100%?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
