# ReMatching Dynamic Reconstruction Flow

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Reconstructing dynamic scenes from image inputs is a fundamental computer vision task with many downstream applications. 
Despite recent advancements, existing approaches still struggle to achieve high-quality reconstructions from unseen viewpoints and timestamps.
This work introduces the \ShortName framework, designed to improve generalization quality by incorporating deformation priors into dynamic reconstruction models. Our approach advocates for velocity-field-based priors, for which we suggest a matching procedure that can seamlessly supplement existing dynamic reconstruction pipelines. The framework is highly adaptable and can be applied to various dynamic representations. Moreover, it supports integrating multiple types of model priors and enables combining simpler ones to create more complex classes. Our evaluations on popular benchmarks involving both synthetic and real-world dynamic scenes demonstrate a clear improvement in reconstruction accuracy of current state-of-the-art models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper tackles the challenge of dynamic scene reconstruction by introducing a novel loss function to incorporate diverse deformation priors into a unified framework. This new loss uses velocity-field-based priors and solves as a flow-matching problem. This design allows the framework to integrate a variety of deformation priors, such as piece-wise rigid transformations and volume-preserving deformations, enhancing the flexibility and generalization capabilities of existing models such as Gaussian Splatting. In experiments, the authors validate the robustness of their method across multiple benchmarks, demonstrating consistent improvements over baselines in both synthetic and real-world dynamic scenes.

### Strengths
- The paper introduces the ReMatching loss, designed to enhance dynamic scene reconstruction by leveraging deformation priors in a unified, adaptable way. This approach directly addresses limitations in generalization for dynamic NVS.
-  ReMatching focuses on incorporating velocity-field-based priors to better model deformations over time, enabling seamless integration with existing dynamic reconstruction models. The framework supports various types of deformation priors, including restricted deformations, piece-wise rigid transformations, and volume-preserving deformations.
- A notable feature of this framework is its capacity to combine multiple priors, allowing for the construction of more complex deformation classes. This adaptability is key for addressing the diverse requirements of real-world dynamic scenes.
- By using the Gaussian Splatting image model as a backbone, the framework consistently outperforms existing methods across multiple benchmarks, demonstrating improved reconstruction accuracy and robustness in both synthetic and real-world dynamic scenes. It shows that ReMatching is not only theoretically sound but also empirically robust across various challenging scenarios.

### Weaknesses
 - The proposed framework and loss function include some details and design choices, many of which seem crucial for achieving optimal performance. However, no ablation study is presented to isolate the effects of these parameters or design decisions, leaving it unclear how each contributes to the final results. Specifically, the impact of the ReMatching loss weight (lambda) and the number of pieces (k) used in the adaptive prior class are not explored. This lack of analysis makes it difficult to understand the sensitivity of the method to these hyperparameters and how they should be tuned for different scenarios.
- Introducing a new loss function raises questions about its impact on training stability and convergence speed, but these aspects are not explored in the paper. Additional insights into how this loss affects training dynamics would provide valuable context for readers, such as  runtime comparisons, convergence plots, or error analysis across iterations. Without this, it is hard to assess if the new loss introduces any practical challenges during training, such as slower convergence or oscillations in the loss landscape.
- The paper asserts that the method is simulation-free, meaning that each evaluation of $\psi_t$ requires only a single step, avoiding potential numerical instabilities. However, it's unclear if this claim has been experimentally validated or remains a theoretical assumption. The paper does not provide any empirical evidence to support the claim that avoiding simulation leads to greater stability or computational efficiency, and it remains unclear if this is a significant advantage over methods that do use simulation.
- From the quantitative results, the improvements over the second-best method are relatively modest. It remains unclear what the primary advantage of this approach is—perhaps robustness? The paper does not provide a clear explanation of why the proposed method is superior, especially given the relatively small improvements in quantitative metrics. It is also unclear if the improvements are consistent across different types of scenes or if they are more pronounced in specific cases.
- Additionally, there are numerous dynamic NeRF datasets and benchmarks beyond the synthetic, 360-degree dynamic NeRF dataset, such as those used in NSFF and DynIBaR, which feature more complex, real-world, forward-facing scenes. It would be insightful to see how well the proposed loss function performs on these more challenging datasets, as it would demonstrate its applicability to diverse, real-world scenarios. The lack of evaluation on these datasets limits the generalizability of the findings.

### Questions
- Would it be possible to apply the new loss function directly to a baseline method without altering any other components? This would allow for a strong, fair comparison that isolates the effect of the proposed loss. For example, the authors can try conducting an ablation study where ReMatching loss is applied to a baseline method (e.g., D3G) without any other modifications, and report the results. This would help isolate the impact of the proposed loss function.
- L215 "we assume that P are linear sub-spaces, hence allowing for fast solvers with a runtime of at most O(n)". Could the authors clarify why it is reasonable to assume P is linear and specify the fast solvers used? This additional detail would help readers understand the computational benefits and assumptions behind this approach.

### Soundness
3

### Presentation
3

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
The paper introduces the ReMatching framework that provides deformation priors into dynamic reconstruction models. It can be adopted into multiple types or model priors and improve dynamic reconstruction accuracy over previous methods.

---

I rate the paper marginally below the acceptance threshold. The paper provides theoretical backgrounds and shows that it works, but it's not so clear what specific problem the paper is trying to tackle and overcome what challenges in the literature.

### Strengths
* Theoretical background

   The method provides theoretical background on its proposed representation. The supplemental further provides proof of lemma for better understanding.

* Good accuracy

  The method shows better accuracy than other previous works in general (depending on the evaluation datasets and metrics though).

### Weaknesses
 * Killing application?

   The method theoretically sounds good, but it seems not so clear what problem the method is mainly targeting. Are there any problems or failing cases that the proposed method solves whereas the previous method fails? Experiments (Table 1 and 2, Figure 2) show the benefit of the method for better rendering quality, but are there any major challenges that the method targets to solve? It's unclear if the improved rendering quality translates to solving a specific problem in dynamic scene reconstruction, or if it's just a general improvement. The paper needs to articulate more clearly the specific limitations of existing methods that this work overcomes, beyond just achieving better metrics.

* Improvement in generalization quality?

   The paper claims about the improvement in generalization quality, but the experiment shows that it doesn't clearly outperform previous methods, but is competitive or slightly better. In what sense does the paper improve generalization quality? The experiments seem to show marginal improvements, and it's not clear if the method actually learns a more generalizable representation of the dynamic scene, or if it's just overfitting to the training data in a way that happens to produce slightly better results on the test set. A more rigorous analysis of the generalization capabilities is needed, perhaps with different types of test data or more challenging scenarios.

### Questions
* Hyperparameter choice

   How is the method sensitive to the hyperparameter choice for the main objective loss and the entropy loss?

* (minor)

   Sometimes equations are referred to by just their numbers. In line 224, "problem from 5 with 9" $\rightarrow$ "problem from equation (5) to equation (9)". It would be good to double-check and revise them between Page 3 and Page 7.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper aims to solve dynamic reconstruction task. It proposes a new loss called ReMatching loss, in order to inject some physical priors into the learned deformation field. They also propose five categories of physics priors, and derive the corresponding forms of the RM loss respectively. The paper builds the model based on the deformable-3d-gaussian paper, and tests the performance for three of the five categories on both synthetic and real-world datasets, showing comparable performance to baselines.

### Strengths
In presentation, this paper shows dedicatedly derived loss form and clear derivation for different kinds of velocity priors. For the idea, the loss proposed by this paper constrains the function shape of deformation field with some physics priors. Working similar as a PINN loss, this framework seems flexible to different deformation designs.

### Weaknesses
1. In synthetic experiments, type IV and type V priors are selected for each scene. They should be thoroughly tested respectively to show the applicability under different scenarios. 

2. In real-world experiments, it is not clear which type of priors are used. And also, all of the priors should be tested to show the abilities. 

3. The velocity branches in the model only serve as a constraint part, but not used directly. The paper should demonstrate whether the learned velocity is meaningful or not. For example, using the velocity to advect the scene. 

4. The segmentation compared with SAM is not proper and confusing. Since SAM segments objects according to semantics but this paper segments according to motions, it’s not proper to punish SAM’s over-segmentation. Another question is about the bouncing ball example shown in the paper. As I know this scene includes some moving shadow on the ground, so the motion should not segment the shadow part as the same as the static ground. How is the segmentation applied?

5. The performances are only comparable, it’s hard to tell whether the priors are really helpful or not. 

6. There is a lack of an illustrative figure to show the main architecture of the proposed method, so the reader can only know how the idea is working till the end of the paper.

7. There are too many equations or derivations in the main text. Although they are clear and I appreciate the details, too many derivations in the main text make the paper lose its main focus. 

8. There are inconsistent baseline names in text and tables, for example, 3D Geometry-aware Deformable Gaussians is called DAG in main text but GA3D in the table.

### Questions
Apart from the questions listed in weaknesses, here are some more questions:

1. Why the baseline numbers in the table not the same as the published version? According to the published version of D3G and GA3D papers, the performance of this paper is actually on the same level. For example, on D-NeRF datasets, D3G has 40.43 PSNR on average, while two types of the model have 40.36 and 40.54 on average. (lego scene is deleted due to data discrepancy, details in next question)

2. The lego scene is known that data discrepancy exists in the scenarios presented in the training and test sets. This can be substantiated by examining the flip angles of the Lego shovels. So some works, like D3G, try to evaluate the model on the validation split because evaluating on the test split is meaningless. Which split is evaluated here? 

3. GA3D has reported its performance on HyperNeRF dataset, so why this baseline is deleted from the HyperNeRF experiments?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper tackles the problem of dynamic view synthesis (with multi-view input). To model the time-dependent function, it introduces a flow-matching mechanism. Essentially, by assuming that a flow or velocity field exists that can reconstruct the true time-dependent functions with some predefined flow priors, e.g., rigid or volume-preserving, this paper utilizes the alternating projection method (AMP) to guide the training of the velocity field. Further, with some specific time-dependent function format, the authors demonstrate that there exist closed-form solutions to such AMP problems. Empirical experiments on D-NeRF and HyperNeRF datasets demonstrate the effectiveness of the proposed approach.

### Strengths
- originality-wise: I appreciate the principled way that the authors formulate the problem of dynamic view synthesis as a prior-guided flow-matching problem. This will be useful and interesting to the community.
- quality-wise: the approach presented in the paper is solid and the experiments demonstrate the effectiveness.
- clarify-wise: overall, the paper is easy to follow.
- significance: the task of dynamic view synthesis is of great importance to many downstream applications, e.g., AR/VR.

### Weaknesses
## Confusion about Eq. (9)

I am quite confused with the definition used to derive Eq. (9). Concretely, the authors state $V = \mathbb{R}^n$ in L202, which is an Euclidean space. However, the authors further define $\psi_t  = (\gamma_t^1, \dots, \gamma_t^n)^T$ where $\gamma^i: \mathbb{R}_+ \mapsto \mathbb{R}^d$ is a function. Do these conflict? The space $V$ should be the codomain of $\psi_t$, which seems to be $\mathbb{R}^{n \times d}$ rather than $\mathbb{R}^n$. This discrepancy makes the subsequent derivation unclear.

Further, I got confused about how Eq. (9) is derived based on the above definition. I tried to follow the product rule for the divergence, i.e., L212. However, I am unable to reach the result, especially $u_t (\gamma_t^i)$. The connection between the continuous formulation in Eq. (4) and the discrete representation in Eq. (9) is not well established. Specifically, it's unclear how the divergence operator acts on the discrete trajectories $\gamma_t^i$ and how this relates to the velocity field $u_t$.

## Inadequate visualization

Since the underlying mechanism is to train a velocity field $v$ (Eq. (2)) and its corresponding flow $\phi_t$ (Eq. (3)), I am quite curious to know 1) how the reconstructed flow as well as velocity fields look like; 2) how the prior set $\mathcal{P}$ (L153) look like; and 3) the difference between the prior and the trained flow. Without visualizing these key components, it is difficult to assess the behavior of the method and the impact of the flow priors. For example, showing the actual velocity fields and how they change over time would be very helpful. Also, visualizing the prior set would clarify the constraints imposed on the flow.

I think this is important such that readers can be well aware of the performance of the approach.

## Speed

Can the authors clarify the efficiency of the flow-matching approach? I think the main overhead compared to vanilla Gaussian Splats comes from the computation of the ReMatching loss $L_\text{RM}$ (Eq. (7)). The computational cost of this loss, especially the partial derivatives, should be discussed in more detail.

If I understand correctly, in Algorithm 1, the $\texttt{solve}$ step in L189 will be solved analytically based on those priors specified Sec. 4, which should be quick. Further, the computation of $\rho$ in L190 should also be quick due to those priors. However, it is not clear how the analytical solutions are derived and what their computational complexity is. A more detailed analysis of the computational cost of each step in Algorithm 1 would be beneficial.

## Missed reference

The following work utilizes an ODE solver to conduct dynamic reconstruction from videos, which is quite relevant to this work.

[a] Class-agnostic Reconstruction of Dynamic Objects from Videos. NeurIPS 2021.

### Questions
1. Can authors clarify how to make HyperNeRF a multi-view dynamic view synthesis benchmark? Essentially, HyperNeRF only has two views. If the authors use up those two views, how to evaluate view synthesis results? Or do we only conduct time-interpolation evaluations? If the authors indeed carry out monocular dynamic view synthesis, please correct L100 as the "multi-view images" statement is not correct.

2. In L131, the authors state that there is a reference function $\psi_0$ to be pushed forward. Concretely, does $\psi_0$ refer to the initialized Gaussian mean $\mu^i$ in Eq. (29)?

3. In L849, the authors state that they use **forward-mode** auto differentiation. Can authors clarify the reason of not using the traditional backpropagation, i.e., reverse-mode? Essentially, what prevents from using that?

### Soundness
3

### Presentation
3

### Contribution
3
