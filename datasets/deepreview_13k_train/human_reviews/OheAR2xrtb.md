# ET-SEED: EFFICIENT TRAJECTORY-LEVEL SE(3) EQUIVARIANT DIFFUSION POLICY

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Imitation learning, \emph{e.g.}, diffusion policy, has been proven effective in various robotic manipulation tasks.
However, extensive demonstrations are required for policy robustness and generalization.
To reduce the demonstration reliance, we leverage spatial symmetry and propose \ours, an efficient trajectory-level \SE equivariant diffusion model for generating action sequences in complex robot manipulation tasks.
Further, previous equivariant diffusion models require the per-step equivariance in the Markov process, making it difficult to learn policy under such strong constraints.
We theoretically extend equivariant Markov kernels and simplify the condition of equivariant diffusion process, thereby significantly improving training efficiency for trajectory-level \SE equivariant diffusion policy in an end-to-end manner.
We evaluate \ours\ on representative robotic manipulation tasks, involving rigid body, articulated and deformable object.
Experiments demonstrate superior data efficiency and manipulation proficiency of our proposed method,
as well as its ability to generalize to unseen configurations with only a few demonstrations. Website: \href{https://et-seed.io/}{https://et-seed.io/}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a framework for learning SE(3) equivariant policies with diffusion models. The training and inference of the diffusion model is based on invariance and the SE(3) equivariance properties. Both simulation and real-world experiments are conducted and show promising results on four robotic tasks.

### Strengths
- The framework presented in this paper is interesting. Incorporating equivariance property in diffusion policy makes sense.
- The presentation of the paper is good.
- The experiments conducted in this paper is thorough and the results are convincing.

### Weaknesses
 - Not sure if including too much math background in the appendix is appropriate. Most content in Sections A and B, if not all of, is unrelated to this paper and should be deleted. Please don't expect that including seemingly sophisticated math in the paper can make the paper look awesome superficially and thus get better rating scores from reviewers. I actually lowered my score because of these unrelated math being included.
- Some math notations are not defined. For example, $E_{equiv}$ and $E_{inv}$.

- What is exactly the format of observation? Is it RGB images? Or colored 3D point clouds? How did the authors guarantee the transformation of input observation T is a simple transformation so that they can verify the equivariance of the policy with T? 
- In Algorithm 1, I didn't see how the equivariance and invariance are included anywhere. Does it mean that equivariance are only guaranteed because of inference?
- How are $E_{equiv}$ and $E_{inv}$ defined?

### Questions
- What is exactly the format of observation? Is it RGB images? Or colored 3D point clouds? How did the authors guarantee the transformation of input observation T is a simple transformation so that they can verify the equivariance of the policy with T? 
- In Algorithm 1, I didn't see how the equivariance and invariance are included anywhere. Does it mean that equivariance are only guaranteed because of inference?
- How are $E_{equiv}$ and $E_{inv}$ defined?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper combines score-based modeling and geometric deep learning for robot policy learning. The results are evaluated in both simulated and real-world robot environments. The authors claim that the proposed approach attains stronger performance than existing baselines.

### Strengths
- Real-world experiments are valuable. I appreciate the authors' efforts to conduct real-world validations of their approach
- Baseline comparisons add value. I appreciate the authors' efforts to compare against 3D representation policy learning works and probabilistic modeling of multi-modal trajectories such as EquiBot.

### Weaknesses
 **A. Presentation**.

The presentation of the paper needs a lot of care in both writing and figures.

There are currently too many display items in the teaser figure, some of which distract the readers from the fruit of the proposed technique. If the authors aim to convince the audience of probabilistic modeling of trajectories and geometric learning, then the figure should focus on those two things. Showing the performance graph directly in the first figure does not clarify that point. I would refer the authors to the teaser figures in diffusion policy and vector neurons, both of which are cited by the authors. Currently, the teaser figure does not strongly convey how trajectories are equivariant and how multi-modality is captured by score-based modeling. Perhaps part of the Figure 2 design can be used to improve this.

A few minor points: I am also unsure if you need almost ten lines of text to clarify the definitions of equivariant and invariant functions (L162-172). I'm not sure whether Algorithm and Figure 3 need to be taking that much space. Perhaps you can make more space there and add my suggested experiments.

**B. Missing critical experiments, novelty concerns**.

I am currently unconvinced and cannot fully assess the performance of the score-based modeling and geometric modeling. If the goal of this work is to showcase the capabilities of combining score-based probabilistic modeling and geometric learning, then I think the two strongest values would be (1) handling multi-modality in the supervision signals for imitation learning, as shown in many works such as diffusion policy, and (2) equivariant representations. If these are the authors' aims, these two points must be substantiated more deeply with visualizations.

I cannot find a single visualization of the generated trajectory in the main manuscript that showcases multi-modality. I cannot find a visualization that showcases equivariant representation either. These two points are not substantiated.

This is deeply related to the novelty of the work. By just reporting on the criterion of success rate, it is truly difficult to understand what caused the performance gaps between the prior works and this one. The dynamical process is abstracted away into a single scalar evaluation criterion. I need more convincing visualizations and results to understand and assess this work. The leading performance reported by the authors could be due to a bunch of things, and whether it is related to the incorporation of probabilistic and geometric modeling is hard to assess.


**C. Implicit Assumptions, evaluation criteria**.

There seem to be several assumptions in this work that I encourage the authors to clarify, perhaps in a limitation section. For example, there seem to be assumptions about perception and policy representation. The perception part needs to be a point cloud and a specified coordinate system by experts. The policy part assumes 6 DOF end-effector representation and the availability of an inverse kinematics/dynamics controller. These assumptions are non-trivial when it comes to more dexterous tasks. Consider spinning a pen with a robot hand. Do we expect the commands of the robot hand to be specified in task space, which would be highly difficult for high-frequency control, and what is the notion of equivariance there?

The presented tasks seem to be primarily trajectory generations in a single Euclidean frame. If this is true, it needs to be specified in the paper, perhaps a limitation section.

### Questions
Please see my comments in the weakness section. Thanks.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method for SE(3) equivariant diffusion policy. The key is a proved theorem that in the denoising process, only the last denoising step needs to be equivariant, and all previous denoising steps can be invariant. A new diffusion policy is designed based on this results, where the first K-1 denoising steps employ a invariant transformer, and the last one employs a equivariant transformer. Results on 6 simulation tasks show the proposed method, ET-SEED, performs better than existing baselines, especially on new poses not seen during training.

### Strengths
- This paper is overall very clearly written.
- The proposed method is straightforward in implementation yet very effective. 
- The experiments results show the strong performance of the proposed method.

### Weaknesses
 - Overall I think this is a good paper and do not have major weaknesses. One minor comment: for figure 3, the block for Inv. SE(3) transformer and Eqv. SE(3) transformer are identical, which seems like a typo?

### Questions
see weakness section

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a novel decomposition of an SE(3)-equivariant Markovian denoising process, classifying each denoising step into $p_1$, $p_2$, and $p_3$-type equivariance. In contrast to previous approaches that utilize $p_3$-type equivariance in which the denoising is equivariant to both the context input $c$ and the noised sample $x^{k}$, the authors demonstrate that equivariant denoising can be achieved through a combination of $p_1$ and $p_2$-type equivariance. Furthermore, the authors argue that training $p_1$ models is significantly easier than training $p_2$ and $p_3$ models, as $p_1$ denoising is invariant to $c$, whereas $p_2$ and $p_3$ denoising are equivariant to it. Consequently, the proposed ET-SEED model employs the invariant $p_1$ for all denoising steps except the final step, which uses $p_2$.

### Strengths
### **Strength 1. Novelty**
The paper introduces a novel approach to the SE(3)-equivariant pose/trajectory generation problem. Unlike previous works, ET-SEED achieves full equivariance by first generating the trajectory independently of the reference frame in which the context input (e.g., point cloud) is observed, then subsequently transforming it equivariantly with respective to the context frame. Results in Appendix E indicate potential advantages of this approach, though this conclusion should be interpreted with caution, as the experiment in Appendix E is limited to a single timestep and does not account for potential interactions across different timesteps.

Overall, the paper offers valuable new insights into defining equivariance condition for diffusion models, making it worth sharing with the community regardless of its limitations.

### **Strength 2. Experimental Results**
The authors present a benchmark comparison against two state-of-the-art methods (DP3 and EquiBot) across six simulated and four real-world tasks. ET-SEED outperforms these methods by a substantial margin in most settings, clearly demonstrating the benefits of this approach. It is particularly exciting to observe robots learning to perform complex, trajectory-level real-world tasks with only 20 demonstrations.

### Weaknesses
### **Weakness 1. No interdependence between each keypose**
The primary limitation of the proposed ET-SEED is that each keypose is denoised independently, with no interaction term between them. Consequently, this is not a true trajectory-level generative model. Joint modeling of all keyposes within a trajectory is indispensable to recent successes in trajectory-level generative models such as diffusion policy and action chunking transformer. Assuming each keypose is independent from the others is unrealistic. 

For example, if the robot needs to open a bottle cap and a drawer, it could start by grasping either the bottle cap or the drawer handle. However, once it has selected one action, say, grasping the bottle cap, the subsequent step should be opening the bottle cap rather than the drawer. While this issue could be addressed in a closed-loop manner by putting the current state as input, this approach is less suitable from an open-loop planning perspective.

I am willing to raise my score if this is my misunderstanding. Otherwise, I cannot give a very high score to the soundness of the method.


### **Weakness 2. Experiment in Appendix E**
The experiments in Appendix E provide a compelling reason for preferring $p_1$-type over $p_3$-type denoising. However, the comparison is limited, as each model is evaluated only with a single-timestep kernel, ignoring potential positive interactions that might arise across timesteps with $p_3$-type denoising.


### **Weakness 3. Requirement for Segmentation**
Many recent equivariant robotic manipulation models exhibit strong robustness to unsegmented inputs. In contrast, ET-SEED relies on object segmentation. While segmenting target objects is not particularly difficult these days due to open-vocab segmentation models like SAM, this requirement restricts ET-SEED’s applicability to object-centric tasks. With segmentation, the model is unable to manipulate non-object entities (e.g., a pile of tiny objects as a whole) or understand global scene context.

### Questions
Suggestion: Why did you use the SE(3)-transformer? More advanced models, like Equiformer v2, with improved efficiency and scalability are available nowadays.

### Soundness
2

### Presentation
3

### Contribution
4
