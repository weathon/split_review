# DEQ-MPC : Deep Equilibrium Model Predictive Control

- Decision: Reject
- Scores: 5, 3, 6, 6, 3

## Abstract
Incorporating task-specific priors within a policy or network architecture is crucial for enhancing safety and improving representation and generalization in robotic control problems. Differentiable Model Predictive Control (MPC) layers have proven effective for embedding these priors, such as constraints and cost functions, directly within the architecture, enabling end-to-end training. However, current methods often treat the solver and the neural network as separate, independent entities, leading to suboptimal integration. In this work, we propose a novel approach that co-develops the solver and architecture unifying the optimization solver and network inference problems. Specifically, we formulate this as a joint fixed-point problem over the coupled network outputs and necessary conditions of the optimization problem. We solve this problem in an iterative manner where we alternate between network forward passes and optimization iterations. Through extensive ablations in various robotic control tasks, we demonstrate that our approach results in richer representations and more stable training, while naturally accommodating warm starting, a key requirement for MPC.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces DEQ-MPC, a framework that alternates optimizing the network and differentiable MPC layers like a deep equilibrium model. By jointly optimizing network and MPC solver states as a fixed-point problem, DEQ-MPC achieves smoother gradients, better warm-starting, and improved performance. The results are demonstrated in imitation learning on several classical robotic control tasks.

### Strengths
1. The authors propose coupled dynamics and MPC layer updates instead of decoupled updates in Diff-MPC, which offers better empirical performance, smoother gradients and leverages warm-starting. The combination of DEQ and Diff-MPC is novel.
2. The authors conduct diverse ablation studies to prove the effectiveness of the design choices.
3. The paper writing is clear and intuitive to read.

### Weaknesses
1. The technical methodology is incremental and not very inspiring. Though it provides improved performance compared to Diff-MPC, it complicates the approach by scheduling the alternating optimization and more hyperparameters. The core idea of alternating optimization between the network and MPC solver, while empirically effective, lacks a strong theoretical foundation and introduces additional complexity without a clear justification beyond performance gains. The specific scheduling of the alternating optimization, involving multiple ADMM iterations, adds to the hyperparameter tuning burden, making the method less straightforward to implement and adapt.
2. The experimental validations are done with a single random seed, which has the risk of overfitting. I suggest the authors try generating different versions of the dataset with different seeds or at least try different random partitions of the dataset. Then, report the performance with mean and variance. The lack of multiple random seeds and dataset partitions makes it difficult to assess the robustness and generalization capability of the proposed method. The reported results might be specific to the chosen seed, and the method's performance might degrade with different data splits.
3. No theoretical insights into why the proposed approach works better. The paper lacks a theoretical analysis that explains the improved performance of the proposed method over Diff-MPC. Without theoretical backing, it is difficult to understand the underlying mechanisms that contribute to the observed empirical gains. This makes it challenging to generalize the method to different tasks or environments.

### Questions
1. What are the convergence criteria used for computing validation errors of all methods?
2. What’s the runtime of the method compared to Diff-MPC?
3. How can this approach be practically more useful for RL or high-dimensional tasks?
4. Fig 1 does not look intuitive - what do the drones and bounded curves mean?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Incorporating task-specific priors like auxiliary constraints in policy training for robotic control can improve safety, flexibility, and generalization. Differentiable Model Predictive Control layers allow such constraints to be embedded directly in neural networks, enabling end-to-end training while retaining interpretability. However, standard differentiable MPC treats solvers as black-box layers, leading to potential instability and inefficiencies. To address this, the paper introduces Deep Equilibrium Model Predictive Control (DEQ-MPC)  to unify the optimization solver and network. The enables a joint inference-optimization approach that improves gradient flow, warm-starting, and stability in complex tasks. DEQ-MPC performs well in warm-starting scenarios. It has reduced iteration needs and this is useful for real-world deployment. The paper introduces two variants: DEQ-MPC-NN, and DEQ-MPC-DEQ. These variants highlight the trade-offs between performance and stability. The authors suggest that DEQ-MPC could be expanded to reinforcement learning and broader constrained optimization problems in the future.

### Strengths
The network and optimization solver unification enhances gradient flow and produces more stable and efficient training dynamics compared to traditional methods.

DEQ-MPC allows for seamless integration of constraints. This in turn gives better safety and reliability, which are important for safety-critical applications such as the robot applications.

DEQ-MPC reduces computation through efficient warm-starting

### Weaknesses
The joint inference-optimization structure is more complex to implement and deploy. The paper does not adequately address the practical challenges associated with this increased complexity, such as the need for specialized hardware or software libraries. The current implementation details are vague, making it difficult to assess the true overhead of this approach. Furthermore, the paper lacks a thorough discussion on how the proposed method scales with the size of the optimization problem, which is a critical factor for real-world applications.

Current evaluations focus on toy examples like pendulum, cart pole, and trajectory tracking, so DEQ-MPC’s effectiveness is not clear. We do not need machine learning for pendulum and cart pole.  As such, the paper results are preliminary. The experiments do not demonstrate the method's ability to handle high-dimensional state spaces or complex, non-linear dynamics that are typical of real-world robotic systems. The choice of these simple environments makes it difficult to generalize the results to more challenging scenarios. The paper needs to demonstrate the benefits of this approach on more complex robotic tasks where the advantages of the proposed method would be more apparent.

### Questions
The evaluation of the method is weak. Pendulum and cart pole are useful for debugging a method but not for arguing its effectiveness. Can you evaluate your method on more compelling cases? Unless we see some significant results for more realistic problems this solution remains a theoretical contribution.

Can you comment on the complexity of the solution -- performance, energy requirements, and implementation requirements.

Can you explain more clearly and comprehensively how you wire this architecture?

Can you summarize the properties of this approach? How large are the models? How do you train them? What is the cost of training? What is the cost of inference?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper considers differentiable model predictive controllers with parameters that depend on the output of a neural network. Standard practice is to run the network once and then solve the MPC optimization problem. However, the authors argue that this may yield optimization problems which are challenging to solve, potentially leading to unstable training dynamics. Instead, they propose to condition the neural network on the solver state and alternate between running the network and solving the optimization problem. They also explore making the network a deep equilibrium model, which is an implicit layer that converges to a fixed point. Therefore, both network inference and the optimzation solver become iterative algorithms, which can alternate until convergence. The authors evaluate their proposed approach, DEQ-MPC, on a number of simulated dynamical systems engaged in a waypoint tracking task, in which the waypoints are the output of the neural network. They compare to Diff-MPC, which uses the exact same solver as their method, except they only run the neural network once prior to solving the MPC optimization problem. Their evaluations show that DEQ-MPC outperforms Diff-MPC on all benchmark systems. Moreover, through extensive evaluations, they find that the deep equilibrium model generally outperforms using a standard neural network. They also explore benefits of DEQ-MPC in terms of generalization, network capacity, sensitivity to constraints, validation loss curve monotonicity, sensitivity to cost function parameters, and warm-starting.

### Strengths
- Improving the performance of structured policy classes, such as differentiable MPC, is an important and timely problem.
- The paper is well organized and overall clearly written. It does a good job explaining the novelty and results and provides enough information to support its claims.
- The results are promising and indicate that DEQ-MPC can outperform more standard implementations of differentiable MPC by alternating between network inference and the optimization solver. Although the tasks considered are all trajectory tracking, they provide extensive evaluation of their method compared to baselines and tease apart what aspects are most important.

### Weaknesses
 - It would be great if Table 1 included end-to-end neural network results as well. This is an important comparison point that is discussed a bit in the ablations. But the paper would benefit from highlighting this more centrally.
- There is a lot of discussion about gradient smoothness and alignment with the global or desired update direction. However, the analysis really only looks on loss curves. Given that this is discussed so heavily in the argument for the method, it would be great to see how well the IFT gradients align with the true gradients that would be computed via backpropagation. If not that, at least look at the smoothness of gradients across epochs during training.
- A minor point, but I don't feel that Figure 1 conveys enough information about the approach. It would be nice if the DEQ-MPC layer part highlighted that the network inference could also be iterative, rather than just conditioned on solver state.
- The evaluations only really consider one task, which is waypoint tracking. Although this is evaluated across many different systems, it would really strengthen the paper to consider other flavors of tasks as well. Or maybe even inferring dynamics parameters too, rather than just terms in the cost function.
- The evaluations also only consider fairly short-horizon tasks (T=5). It would be great to see how results scale with longer horizons. And same goes for evaluating the warm-starting ability of DEQ-MPC. There are very few warm-starting steps during training and evaluation.
- There are some details that appear to be missing (unless I missed them), such as the number of fixed point iterations for the DEQ used within DEQ-MPC.
- DEQ-MPC appears to also use intermediate losses that compute gradients through multiple iterates, rather than just the final solution. It is unclear if diff-MPC is also trained this way. If not, it would be an important ablation to see if it would help improve diff-MPC's performance.

### Questions
- Are all cost function and dynamics model parameters manually set or also learned end-to-end? If manually set, how would this approach extend to the scenario where we want to learn dynamics, cost, or both jointly in an end-to-end fashion?
- How many iterations are used running each DEQ model, or are they run until a fixed-point is reached?
- Does the Diff-MPC baseline use the augmented Lagrangian method or is it iLQR like in the original paper? Does the network it use also contain the temporal convolutions?
- Would Diff-MPC perform better if its gradients were computed using multiple intermediate iterates, like in the proposed DEQ-MPC approach? This was one aspect of the ablation that appeared to be missing.
- Are the IFT gradients only valid at a fixed point? If so, using them to compute gradients on intermediate solutions that have not converged may give incorrect, although still useful, gradients. How do the gradients computed through the IFT compare to the exact gradients computed via autodiff?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a novel deep learning method integrating dynamics learning and model predictive control (MPC). Optimization is performed in two stages: update weights then solve MPC repeat. This yields several advantages once the model is trained. Examples of these are smoother gradients during training and for MPC. The model can be warm-started much more readily than alternative methods and constraints can be strictly adhered to also. The authors demonstrate the effectiveness of their methods using five examples and compare their algorithms to alternative Diff-MPC methods.

### Strengths
The strengths of this paper are numerous. The algorithmic setup is original and an interesting idea. The contributions are compelling.

The authors show that this method outperforms alternative Diff-MPC methods in the environment setups. The algorithm is well-ablated and compelling enough with minor changes to justify the authors’ claims. The paper is well-presented and easy to follow. Though I do not know the Diff-MPC literature well, this paper appears significant enough for publication.

### Weaknesses
Despite the numerous strengths, there are a few weaknesses. However, these are readily addressable.

The majority of the weaknesses revolve around the reporting of the results. There are no standard deviation error bars on the reported numbers or figures (Fig. 2 to 7) or Table 1. Stating the number of experiments completed and adding standard deviation as a plus/minus spread of error in Table 1 would strengthen the paper. Comparing the statistical significance of the reported rewards in Table 1 would improve the paper also. For example, it would be interesting to know if there was any statistical difference in performance between DEQ-MPC-NN and DEQ-MPC-DEQ in the Quad-Pole scenario. A Mann-Whitney U-test could work here. I leave it up to the authors to choose how they evaluate their statistics. Similarly, figures Fig. 2 to 7 do not show the standard deviations of the validation error or the normalised returns  across multiple training runs. This would strengthen the comparison.

### Questions
As seen in the weaknesses section, the reporting of results is a limitation of the paper. However, this is easily remedied. Please follow my recommendations in the weaknesses section. Please justify the statistical comparisons you use. Other than this, the paper is well-written, original, and of significance.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces an approach to integrating MPC with deep learning by combining optimization solvers and network inference in a unified fixed-point framework. The proposed DEQ-MPC iteratively alternates between deep equilibrium models neural network predictions and MPC optimizations using the ADMM method until a stable equilibrium is reached.

### Strengths
The paper's strength is its approach of updating the neural network and MPC simultaneously using ADMM, allowing adaptive, joint optimization that improves stability, gradient alignment, and efficiency.

### Weaknesses
The paper presents an interesting approach; however, there are some areas for potential improvement. First, it lacks a novel theoretical contribution and does not provide formal proofs to support its framework. Additionally, there is minimal analysis of computational expense, which would strengthen the understanding of its practical feasibility. The presentation could also benefit from greater clarity, as certain aspects, such as the representation of parameter theta, are not entirely clear, which may make the paper challenging to follow. While the paper mentions task-specific priors, concrete examples or integration of these are not demonstrated, which could further enhance the practical relevance of the approach.

### Questions
1. Could the authors elaborate on any theoretical foundations or formal proofs that validate the convergence of the proposed framework? 
2. What is the computational overhead of DEQ-MPC compared to traditional differentiable MPC? Have there been any benchmarks or evaluations on computational efficiency, especially in real-time applications?
3. The paper mentions the use of parameter theta, but its role and significance are unclear. Could the authors clarify what theta represents?
4. Although the paper claims to incorporate task-specific priors, there are no explicit examples. Could the authors provide examples of how task-specific priors are integrated into DEQ-MPC, and the impact these have on task performance?

### Soundness
1

### Presentation
1

### Contribution
2
