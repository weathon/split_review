# AdaManip: Adaptive Articulated Object Manipulation Environments and Policy Learning

- Decision: Accept
- Scores: 8, 5, 6, 1, 8, 5

## Abstract
Articulated object manipulation is a critical capability for robots to perform various tasks in real-world scenarios. Composed of multiple parts connected by joints, articulated objects are endowed with diverse functional mechanisms through complex relative motions. For example, a safe consists of a door, a handle, and a lock, where the door can only be opened when the latch is unlocked. The internal structure, such as the state of a lock or joint angle constraints, cannot be directly observed from visual observation. Consequently, successful manipulation of these objects requires adaptive adjustment based on trial and error rather than a one-time visual inference. However, previous datasets and simulation environments for articulated objects have primarily focused on simple manipulation mechanisms where the complete manipulation process can be inferred from the object's appearance. To enhance the diversity and complexity of adaptive manipulation mechanisms, we build a novel articulated object manipulation environment and equip it with 9 categories of articulated objects. Based on the environment and objects, we further propose an adaptive demonstration collection pipeline and a 3D visual diffusion-based imitation learning that learns the adaptive manipulation policy. The effectiveness of our designs and proposed method are validated through both simulation and real-world experiments.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces AdaManip, a new environment and method for training robots to manipulate articulated objects with adaptive mechanisms.  Existing datasets often simplify these interactions, allowing objects to be manipulated without accounting for hidden states like locked latches or required rotation angles.  AdaManip addresses this by incorporating five key adaptive mechanisms: lock mechanisms, random rotation direction, rotate & slide, push/rotate, and switch contact.  The environment includes nine object categories (bottles, pens, coffee makers, windows, pressure cookers, lamps, doors, safes, and microwaves) with diverse instances, totaling 277 objects.

The authors also propose an adaptive demonstration collection pipeline that uses rule-based expert policies to generate trajectories reflecting realistic partial observation scenarios. These demonstrations are then used to train a 3D visual diffusion-based imitation learning model. 

Experiments in simulation and real-world settings with a Franka Panda robot demonstrate the effectiveness of AdaManip. The proposed method outperforms baseline approaches like VAT-Mart and AdaAfford, achieving higher success rates across all object categories.  Ablation studies confirm the importance of adaptive demonstrations and the strategy of limiting each demonstration to a single adaptive trial. The real-world experiments further validate the policy's ability to generalize and adapt to real-world objects and conditions.

### Strengths
- This paper points out an important but under-explored problem: the adaptive manipulation of articulated objects with complex mechanisms. Previous work primarily focused on simpler manipulations, neglecting the realistic challenges of hidden object states.
- The AdaManip environment and associated dataset are significant contributions. They provide a rich and diverse set of objects, as well as the rule-based demonstrations, enabling research on more realistic manipulation tasks.
- The categorization of five key adaptive mechanisms (lock mechanisms, random rotation direction, rotate & slide, push/rotate, and switch contact) provides valuable insights and serves as an inspiring framework for creating new tasks.
- The application of 3D visual diffusion-based imitation learning is a good baseline for this problem.  Diffusion models are well-suited to capturing the multi-modal nature of the task, where multiple valid manipulation trajectories can exist for a given observation.
- The real-world experiments are valuable, demonstrating the practicality of the approach.
- The paper is generally well-written and easy to follow.

### Weaknesses
- Relying on rule-based expert policies for demonstration collection can limit the complexity of the learned behaviors. Exploring methods for learning these demonstrations or incorporating human demonstrations could lead to more robust and generalizable policies.

- The source code and dataset have not been released.

- Environmental specifications, including frame rate and API details, are not provided.

- The paper primarily compares against affordance-based methods.  A comparison to other offline imitation learning methods (e.g., [1]) and online learning-from-demo methods (e.g., [2][3][4]) would provide a more complete picture of the method's performance.

[1] Zhao, Tony Z., et al. "Learning fine-grained bimanual manipulation with low-cost hardware." arXiv preprint arXiv:2304.13705 (2023).

[2] Ball, Philip J., et al. "Efficient online reinforcement learning with offline data." International Conference on Machine Learning. PMLR, 2023.

[3] Rajeswaran, Aravind, et al. "Learning complex dexterous manipulation with deep reinforcement learning and demonstrations." arXiv preprint arXiv:1709.10087 (2017).

[4] Ho, Jonathan, and Stefano Ermon. "Generative adversarial imitation learning." Advances in neural information processing systems 29 (2016).

### Questions
- How is the "unlock mechanism" and other similar mechanisms simulated? Is this based on a specific collision shape or on some high-level discrete conditions?
- How is the real-world demonstration collected?
- Could you provide the detailed hyperparameter values for the diffusion policy, such as the action horizon and prediction horizon?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors present an imitation learning study focusing on tasks involving articulated objects. The study necessitates (1) a multi-modal action proposal and (2) adaptive manipulation based on historical actions.

The author conducted experiments both in simulation and real-world.

### Strengths
The motivation of the paper is sound. It is an important problem in imitation learning: (1) multi-modal action proposal and (2) adaptive manipulation from history actions.

### Weaknesses
Could the authors clarify any generalizations observed in the simulation results? Further details on the differences between the training and testing datasets would be helpful.

The manuscript requires significant revisions, particularly Figure 1 and 3, which is quite confusing. If I understand correctly, you employed a rule-based policy described as "adaptive" to collect data. However, it appears that this policy does not incorporate any prior knowledge about the object’s mechanism for the learning phase. Could you clarify this?

The real-world results presented are not convincing. There is a lack of discussion on generalization, and the evaluation seems overly simplistic with limited data. The methods used for collecting demonstrations in the real world are also unclear. Additionally, it is not specified whether the data collection method used in simulations is scalable to real-world applications.

I would like to see more discussion on history information part. How did you incorporate history? would simply adding history cause overfitting problem?

### Questions
Why did you choose point cloud input rather than RGB?

Further details about the real-world experiments are needed, specifically:

1. What type of low-level controller was used?
2. To what extent does the training generalize to the test scenarios?
3. What is the frequency of the policy?
4. How was the expert demonstration collected? 
-- Understanding the data collection process is crucial. Are 35 demonstrations sufficient to capture the task's multi-modal nature?

### Soundness
4

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this work, the authors investigate the task of learning manipulation policies for articulated objects. Specifically, they recognize a gap in the literature relating to the intersection between articulation and locking/sequential mechanisms that are often required in real-world articulated object manipulation scenarios (e.g. unlock the door before opening). Their contributions are roughly twofold: first, they design a set of novel articulated object simulation environments that model the locking/sequential mechanisms during articulation tasks; second, they propose a demonstration dataset and policy architecture to learn novel policies to tackle these environments. They demonstrate the effectiveness of their policies on their simulated environments and real-world embodiments of the same.

### Strengths
# Originality

While locking mechanisms and articulated objects have been studied (and modeled) independently, the interface of the two has not yet been particularly well-studied, despite the fact that many articulated objects require navigating locking/latching mechanisms to accomplish opening. Proposing tasks that model this aspect of the task is a good original contribution.

On the policy side, I can’t fully evaluate whether the design of the policy contains much novelty/originality, as it appears to be a straightforward modification of diffusion policies, but without enough architectural detail provided to assess novelty.

# Quality

The environment-modeling side of the paper seems high quality, with good diversity over tasks and attention to relevant details for releasing a new benchmark. The proposed policy and its analysis is of OK quality - not enough detail is provided in the experiments section for me to evaluate.

# Clarity

The paper is clear and well-written (except figures, which I will discuss later).


# Significance

The paper is of moderate significance, as this set of tasks (and an environment which accurately models it) is indeed important to study and is currently underexplored. Difficult to assess the significance of the policy proposal, however.

### Weaknesses
There are 3 primary categories of weakness
* The policy itself was not fully characterized. Not many details were provided as to the architecture, training procedure, etc. and I was not able to really assess in comparison to existing literature. In particular, the treatment of point clouds and history were glossed over, when in other works it has been shown that these details matter for different kinds of generalization. Additionally, the ablations don’t provide much insight into why the design decisions of the policy lead to improved performance over the baselines - “Ours” without history is much stronger than the baselines.
* Experimental details: It was unclear whether the baselines were fairly conducted - were the VAT-MART and AdaAfford methods trained on the same data as “Ours”? Or were pretrained weights used?
* Generalization characterization: when releasing benchmarks with metrics, ideally we would also receive a set of metrics with a clear experimental protocol, as well as what conditions/generalization criteria the experiment is trying to measure. Overall “success rate” for a single kind of evaluation is somewhat coarse. Instead, it would be desirable to have a clear set of different benchmarks, e.g. to measure cross-instance generalization, generalization across initialization/viewpoint, cross-class generalization, etc. 



Smaller weaknesses
* Figure 1 is too dense, and the symbols unintuitive. More text should be incorporated into the diagram, it’s really hard to figure out what’s going on.

### Questions
* Why wasn’t 3D Diffusion policy considered as a policy class? https://3d-diffusion-policy.github.io/
* Why was the decision made to use a logical lock/mechanism for task progression instead of a physical mechanism?
* How is success rate defined?
* How many history steps are needed for success across the tasks? Would be good to understand this mechanism a bit more.
* How is sim2real accomplished? Is a new dataset collected in real setting? Or is it transferred zero-shot.

# Update post-rebuttal

The authors have done a good job responding to my questions. In particular, it is good to see that the DP3 baseline and their policy baseline are roughly equivalent in performance, matching my expectations. It's also good to see that additional high-quality recovery demonstrations improve success rates. This makes it a stronger paper - although because the policy-level changes are primarily a data contribution rather than a policy contribution, I maintain that my current score of 6 (marginal accept) is warranted.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper proposed a framework that aims to adaptively learn manipulation policy based on previous policy execution results. The framework is based on diffusion policy learning. The manipulation specifically targets articulated object manipulation such as safe and doors. Both simulation and real-world experiments are conducted.

### Strengths
- The studied problem in this paper is interesting.
- The paper presentation is good and clear.
- The experiment results look strong and outperform related baselines.

### Weaknesses
- There isn't much technical novelty in this paper. It seems that the algorithm/model itself does not guarantee adaptive. The only "adaptive" component stems from adaptive demonstration collection. How is this "adaptive" policy different from vanilla diffusion policies?
- The experiment shows that the proposed method is better than AdaAfford, which is quite surprising. If what the authors of AdaAfford argued is true, AdaAfford should also be able to solve the problem presented in this paper. Why is AdaAfford "not so stable due to the capability limit of cVAE"? Why is the method in this paper stable? How does "stable" defined? Is it because diffusion model vs. cVAE, or it's because output actions vs. point cloud affordance?

### Questions
The authors can reply to the questions raised in "Weakness" section.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a new simulation environment and framework for adaptive manipulation of articulated objects with diverse mechanisms. The AdaManip environment includes nine object categories and five types of *adaptive* mechanisms. Using a novel adaptive collection method, the authors generate a dataset to support training for complex, multi-step manipulation tasks. The paper further introduces a 3D diffusion-based imitation learning framework to model multi-modal action distributions, enabling policies that adjust based on previous actions. Well-designed experiments demonstrate results in simulation and real-world scenarios indicating that AdaManip achieves high success rates and outperforms baseline methods in handling complex articulated objects.

### Strengths
- The AdaManip environment addresses a gap in existing robotic manipulation environments by focusing on objects with realistic, multi-step (adaptive) mechanisms, supporting a range of complex manipulation scenarios. This is valuable for advancing robot manipulation learning on real-world objects and increasing robots' learned policies' generalizability.

- Adaptive Demonstration Collection: The method for collecting adaptive demonstration trajectories in a rule-based fashion is well-motivated.

- The use of diffusion models for action distribution in policy learning is innovative and effectively models the multi-modal distribution necessary for tasks where visual cues alone are insufficient.

- Extensive Evaluation: The paper provides detailed simulation and real-world experiments. Performance metrics such as success rates across nine object categories and comparisons with baseline methods, including ablation studies, illustrate the framework's effectiveness.

### Weaknesses
- Although the framework outperforms baselines like VAT-MART and AdaAfford, it would benefit from additional baseline comparisons, especially with RL methods (or more specifically, with dense reward annotation) or DAgger, that may be adaptable to adaptive manipulation tasks, or recent work, FlowBotHD, that incorporates history into flow in order to learn to adapt to past errors using a flow-based policy (which is your sequential rule-based policy but with flow representations).

- More emphasis on how AdaManip differs from environments like PartNet-Mobility in complexity or adaptability would better explain the novelty of AdaManip. For example, you could talk about whether there are particular types of mechanisms or object categories that AdaManip includes that PartNet-Mobility does not.

### Questions
- Since the policy is a rule-based sequence, how does the proposed method compare with traditional planning methods? Specifically, please provide a brief comparison or discussion of how your method relates to or differs from traditional planning approaches for articulated object manipulation.

- Is diffusion policy the only viable solution? Specifically,  maybe discuss potential alternative approaches and explain why you chose diffusion policy over other methods.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a novel robotic simulation environment and a dataset which targets solving articulated object manipulation tasks with some adaptive mechanisms, adjusting the feedback from failed or successful past actions. The approach uses a 3D diffusion-based behaviour cloning method to model multi-modal action distribution. The experiments show that this method outperforms existing models in both simulated and real-world scenarios, illustrating its potential for real-world applications.

### Strengths
1. The paper introduces a new simulation setup with more varied and complex object interactions, which improves over existing datasets. This new setup helps robots learn and practice in a way that better matches real-world conditions, making their training and testing more realistic.
2. The presented experimental results demonstrated the proposed policy outperformed the baseline on a significant level, proving its effectiveness and applicability.
3. Real-world experiments are promising and impressive.

### Weaknesses
1. The paper's main contributions focus on introducing a new manipulation environment and demonstrating real robot experiments, but it lacks significant innovation in the underlying methodology, raising questions about its fit for this particular conference.
2. The paper lacks comprehensive ablation experiments to justify design choices. For example, it does not explain why action history was chosen over observation history, which is more common in reinforcement learning research. Additionally, there is no comparison with sampling-based methods that first identify plausible actions and then plan over them.
3. The paper does not discuss the scalability of the approach or its ability to generalize across different objects in a zero-shot setting. It also fails to explore how the method would handle combinations of the five proposed manipulation mechanisms.
4. The method relies heavily on the quality of the collected data, and the diffusion model learns everything simultaneously, which could lead to redundancy and potential overfitting to the training data.

### Questions
1. How does your method provide significant methodological innovation beyond creating a novel environment and conducting real robot experiments?
2. Why did you choose to use action history instead of observation history, which is more commonly used in reinforcement learning? Have you conducted experiments to compare the effectiveness of these approaches?
3. How does your method perform compared to sampling-based methods that propose plausible actions and plan over them? Have you evaluated this as a baseline?
4. Can you elaborate on how your approach scales to new, unseen objects in a zero-shot setting? What is the expected performance when combining multiple proposed mechanisms?
5. How do you ensure that your method generalizes effectively across different categories of articulated objects?
6. Could you provide more details on how your method handles potential overfitting, given its reliance on the quality of collected data and the "learn everything at once" nature of the diffusion model?
7. What are the limitations of your adaptive policy learning approach when applied to more complex or real-world scenarios with more diverse mechanisms?

### Soundness
3

### Presentation
3

### Contribution
2
