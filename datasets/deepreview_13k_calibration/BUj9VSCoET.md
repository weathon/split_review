# Efficient Residual Learning with Mixture-of-Experts for Universal Dexterous Grasping

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
Universal dexterous grasping across diverse objects presents a fundamental yet formidable challenge in robot learning. Existing approaches using reinforcement learning (RL) to develop policies on extensive object datasets face critical limitations, including complex curriculum design for multi-task learning and limited generalization to unseen objects. 
To overcome these challenges, we introduce ResDex, a novel approach that integrates residual policy learning with a mixture-of-experts (MoE) framework. ResDex is distinguished by its use of geometry-unaware base policies that are efficiently acquired on individual objects and capable of generalizing across a wide range of unseen objects. Our MoE framework incorporates several base policies to facilitate diverse grasping styles suitable for various objects. By learning residual actions alongside weights that combine these base policies, ResDex enables efficient multi-task RL for universal dexterous grasping.
ResDex achieves state-of-the-art performance on the DexGraspNet dataset comprising 3,200 objects with an 88.8\% success rate. It exhibits no generalization gap with unseen objects and demonstrates superior training efficiency, mastering all tasks within only 12 hours on a single GPU.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work combines concepts from residual policy learning, mixture of experts and student-teacher distillation to train generalizable grasping policies with a dexterous hand in simulation. The proposed method ResDex has multiple stages of reinforcement learning in simulation, including the training of proprioception only policies on different types of objects, training of a residual mixture of experts policy and training of policies with a curriculum of reward functions. The resulting policies are shown to achieve a high performance for grasping unseen object instances and categories.

### Strengths
1. The authors propose a residual mixture-of-experts policy for dexterous grasping, where the individual base policies are trained on different datasets. This is both a novel and a very interesting idea. In particular, the individual policies are trained on clusters of object geometries using only proprioceptive information, whereas the high level mixing policy is trained with state information.
2. The work further includes a curriculum of two reward functions: the first reward function encourages similarity to demonstrated grasps, whereas the second reward only encourages grasping success. This is a good trade-off between encouraging natural and optimal grasps.
3. The method is compared to prior work on the reinforcement learning of dexterous grasping and it is shown to achieve a higher zero-shot grasping success rate. Appropriate ablations for the various parts of the mixture policy are included.

### Weaknesses
1. The paper lacks any real-world experiments. Therefore, it is not clear if the specific design decisions made in this work, which increase the performance in the simulator, lead to a higher real-world grasping success rate. Further, real-world evaluation might be challenging because the Shadow Hand is very expensive. The work could be strengthened by also running experiments with the LEAP Hand, for example, which is more accessible.

### Questions
Is a sophisticated robot hand necessary to reach a high performance, or could similar performance be reached with simpler hands like the LEAP or Allegro?

### Soundness
4

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
4

### Summary
For universal dexterous grasp execution, this work introduces a residual RL policy based on a mixture of experts for the base geometry-unaware policies.  The major motivation is to address the training inefficiency and limited generalization issues in the previous work. Technically, the authors propose to combine residual RL and the mixture of experts to tackle the gradient interference issues in training multi-task RL and the limited diversity of using a single base policy. The simulated benchmarking results and ablation study demonstrate superior generalization performance against the baseline.

### Strengths
- This work tackles an important problem in learning-based grasping, i.e., how to learn a performant policy for grasp execution;

- The creative combination of existing ideas to address the problems in the previous work is well-motivated and sensible;

- The idea of using geometry-unware training to enhance the generalization of the base policy is interesting and meaningful;

- The presentation is easy to follow and possesses good readability; 

- Comprehensive comparison and ablation study in the experiments.

### Weaknesses
 - The definitions of different reward functions are scattered across several sub-sections. It would be more clear for the reader if they could be grouped and discussed together.

- It would be clearer to reframe the technical contributions in the draft so that the readers can grasp the key idea more conveniently. It's because the main technical contribution is to develop a novel combination of existing techniques and demonstrate its effectiveness in learning generalizable grasping policies. 

-  There is no specific comparison on this aspect. It would be nicer to also compare the training time with Unidexgrasp as the authors claim that the previous approach is inefficient, and this has been addressed by the proposed idea. 

- In the experiment part, for conciseness, the ablation of different numbers of experts in Tables 1 and 2 can be taken out and put into the ablation study subsection.

- The actions from different base policies are summed together based on the predicted weights of the hyper policy. I am wondering about the rotation representation used in this summation as they lie in a different space than the Euclidean one. 

- Is it seemingly contradictory to first perform geometry-aware clustering and then learn a geometry-unware policy? In the end, the mixture of experts is geometry-aware. For the presentation part, it would be clearer to refine the texts for such differences. For the technical part, can they be merged into a single step in a more intelligent way?

- How is the part of grasp synthesis done? 

- It seems that the number of experts doesn't represent the specific grasp styles as the model performs the best with only 4 experts, which is counter-intuitive for a dataset with more than 3k objects.

### Questions
- The actions from different base policies are summed together based on the predicted weights of the hyper policy. I am wondering about the rotation representation used in this summation as they lie in a different space than the Euclidean one. 

- Is it seemingly contradictory to first perform geometry-aware clustering and then learn a geometry-unware policy? In the end, the mixture of experts is geometry-aware. For the presentation part, it would be clearer to refine the texts for such differences. For the technical part, can they be merged into a single step in a more intelligent way?

- How is the part of grasp synthesis done? 

- It seems that the number of experts doesn't represent the specific grasp styles as the model performs the best with only 4 experts, which is counter-intuitive for a dataset with more than 3k objects.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes residual learning with an MoE method for generalized grasping in simulation. The proposed method includes a set of k geometry-unaware base policies and a hyper policy that learns the weights of each base policy. It also includes a residual action based on the geometry and position of the target object and the robot's proprioception. 

The proposed method avoids complex curriculum design and can be trained within 12 hours on a single 4090 GPU. Its performance peaks SOTA methods and shows no performance drop when generalized to unseen objects and categories. All claims are supported by solid experimental evidence from simulation.

### Strengths
- This paper proposed a novel combination of residual learning and MoE for general dexterous grasping.
- The proposed method significantly outperforms SoTA grasping methods on a large-scale simulation benchmark.
- The proposed method avoids complex curriculum design and observes almost zero performance drop when generalizing to unseen objects and categories.
- The proposed method can be trained within 12 hours on a single 4090 GPU.
- Extensive experiments in simulation support the authors’ claims.
- Overall, the paper is well-organized and written.

### Weaknesses
 - The authors did not discuss the proposed method's limitations and failure cases. It will be interesting to see and discuss what cases still challenge the proposed method.
- There is no real robot experiment to test if the learned policy adapts well to noises and challenges in the real world.
- In line 353, the authors wrote, “Increasing k leads to a slight performance gain.” This is not true, as the proposed method performs best when k=4 and the performance drops with k larger than 4. It would be better to discuss why the model performs best when k=4.
- When reading subsections 4.1 and 4.2, I am confused about whether the base policy is trained on a single object or multiple objects. The paper contains both descriptions. This confusion is quickly resolved when I discover MoE in subsection 4.3. I suggest specifying how the base policy is used early in subsection 4.1 to avoid this confusion in the future.

### Questions
- In line 064, what do you mean by “base policies that only observe … 3D positions of objects to infer the object location”? What’s the difference between the 3D positions of objects and the object location?
- When training the base policy, do you train it with randomized object positions? What about orientations?
- Tables 1 and 2 suggest that the proposed method’s performance peaks with four base policies. Why is it not the case that more base policies always yield better performance?
- What is the setup for the vision-based policy? How many cameras are used? How are the cameras placed? Are there any treatments for the observed point cloud before feeding it into the policy? Is the vision-based policy evaluated in simulation or on real robots?
- Around line 421 “… and we evaluate their performance on the training set”, does the training set refer to the training set of the ablation study (i.e., the six objects), or the training set of DexGraspNet?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors introduce ResDex, which integrates residual policy learning with a Mixture-of-Experts (MoE) framework for learning universal dexterous grasping policies. The method addresses drawbacks in conventional methods such as UniDexGrasp and UniDexGrasp++, including limited generalization and complex multi-task curriculum design, by leveraging geometry-unaware base policies. ResDex achieves efficient training and superior generalization, performing state-of-the-art on the DexGraspNet dataset.

### Strengths
1. Thorough experiments: The experiments are comprehensive, including comparisons with baselines and ablation studies that validate the importance of the method's components.
2. Performance: ResDex demonstrates state-of-the-art success rates on the DexGraspNet dataset, achieving 88.8% success in grasping unseen objects.
3. Clarity: The method is well-explained, and the presentation is enhanced by figures and tables that clearly illustrate key components of the approach.

### Weaknesses
1. Complexity of Approach: While simpler than UniDexGrasp and UniDexGrasp++, the combination of multiple base policies and MoE adds complexity, which goes against the original spirit of residual RL to reduce exploration burden. The use of multiple base policies, even if individually simple, introduces a layer of coordination that is not present in standard residual RL, potentially increasing the difficulty of training and hyperparameter tuning. The method's reliance on a mixture of experts also adds computational overhead during both training and inference. 
2. Training Efficiency: The claim of training efficiency is not substantiated through controlled experiments. Although training times are given in the appendix, there is no comparison to baselines using comparable parameter counts and hardware. The lack of a direct comparison makes it difficult to assess whether the method truly offers efficiency gains over existing approaches. The authors should provide a more rigorous comparison, controlling for factors such as network size and hardware, to support their claim.
3. Generalizability: While generalization is a key claim, the evaluation is limited to simulation on DexGraspNet data. In contrast, both UniDexGrasp and UniDexGrasp++ evaluated generalizability in different experimental settings, providing stronger support for their claims. The evaluation should include tests on datasets with different characteristics, such as objects with varying textures, shapes, and sizes, to provide a more thorough assessment of the method's generalization capabilities. The current evaluation does not sufficiently demonstrate the robustness of the method to unseen scenarios.
4. Minor Writing Issues: There are some citation issues (e.g., misuse of \citep vs. \citet in lines 101-102, line 296). Section 4.4 would benefit from a \begin{algorithm}. Additionally, the term "geometry-unaware" could be more appropriately named "geometry-agnostic."

### Questions
1. How is $g$ in equation 2 sampled? Will randomly sampling $g$ cause gradient interference?
2. In lines 160 and 237, are $q$ and $q_t$ hand joint positions or hand joint angle configurations?
3. One reason for using MoE is that "the base policy typically provides only a single grasping pose for its training object." Does this limitation arise due to the use of argmax for base actions (line 252)? Will other multimodal policy training methods also address this?
4. Could the authors provide more insights into how combining residual policy learning with MoE improves learning? Given that residual RL typically combines known, stable controllers with RL, what role does the MoE play? How does $\pi^H_{\phi}$ learn to weight $a^B_{t,i}$ dynamically without having $a^B_{t,i}$ as input? Could $\lambda_t$ collapse to a mean or one-hot value?

### Soundness
3

### Presentation
3

### Contribution
3
