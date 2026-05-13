# Entity-Centric Reinforcement Learning for Object Manipulation from Pixels

- Decision: Accept
- Scores: 8, 8, 6, 8

## Abstract
Manipulating objects is a hallmark of human intelligence, and an important task in domains such as robotics. In principle, Reinforcement Learning (RL) offers a general approach to learn object manipulation. In practice, however, domains with more than a few objects are difficult for RL agents due to the curse of dimensionality, especially when learning from raw image observations. In this work we propose a structured approach for visual RL that is suitable for representing multiple objects and their interaction, and use it to learn goal-conditioned manipulation of several objects. Key to our method is the ability to handle goals with dependencies between the objects (e.g., moving objects in a certain order). We further relate our architecture to the generalization capability of the trained agent, based on a theoretical result for compositional generalization, and demonstrate agents that learn with 3 objects but generalize to similar tasks with over 10 objects. Videos and code are available on the project website: \url{https://sites.google

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This manuscript introduces an innovative approach that seamlessly integrates an object-centric model with a transformer to master structured representations crucial for goal-conditioned reinforcement learning (RL), particularly in scenarios entailing multiple objects or entities. The employed object-centric model, denoted as DLP, equips the framework with the capability to capture a structured portrayal of the environments. Concurrently, the transformer component adeptly models the dynamics of the entities and their intricate physical interactions. The clarity of the conceptual foundation is commendable, and the results showcased, particularly in the challenging realm of image-based control, are robust and hold promise. Furthermore, the paper hints at potential advancements in the field of compositional generalization. Given these strengths, I am inclined to recommend this paper for acceptance, acknowledging its significant contributions and merits. However, there are some unclear points in the current version and it would be better if the authors could provide clarification on them.

### Strengths
- **[General idea]** Overall, the concept presented in the paper is elegantly simple and straightforward—a notable strength, as this simplicity bodes well for better understanding and potential scalability of the framework. This is of particular importance, despite the approach essentially being a synthesis of OCR and transformer-based MBRL.

- **[Presentation]** The clarity and coherence of the presentation, spanning both the main paper and the appendix, are commendable, facilitating easy comprehension for the reader. Nevertheless, I have enumerated several recommendations in the subsequent sections to further enhance the manuscript.

- **[Experiments]** The experiments conducted using IsaacGym validate the method's efficacy, and the exploration of compositional generalization yields valuable insights. However, I have outlined several suggestions in the sections that follow, aimed at verifying some claims made in the algorithm's design.

### Weaknesses
I list the weaknesses and questions together here.

**[About the matching]** 

I concur with the authors regarding the permutation invariant block in the EIT, acknowledging its potential to obviate the need for matching post-OCR. However, the rationale behind the decision to forego a straightforward matching step subsequent to OCR is not entirely clear to me. Is this choice motivated by a desire for increased flexibility, or are there other factors at play? From my perspective, matching algorithms can serve as modular, plug-and-play components, exemplified by their seamless integration in slot attention mechanisms as outlined in [1]. I recommend a more thorough elucidation of this particular point in the rebuttal, as it would greatly enhance the clarity and comprehensiveness of the explanation. Specifically, it would be beneficial to understand how the proposed method handles scenarios where the object-centric representation might not provide a one-to-one mapping between detected entities across different views or time steps, a common issue in multi-object tracking and matching.

**[About the evaluation]**  

In order to rigorously assess the contribution of each individual component within the algorithm’s design, I recommend broadening the scope of the ablation studies conducted. Specific areas to consider include: (1) experimenting with alternative OCR methodologies in lieu of DLP, to evaluate the framework’s adaptability and performance consistency across varying OCR techniques; (2) a detailed evaluation of the impact that each component recognized by DLP has on the ultimate policy learning. This is particularly pertinent for elements that do not share a direct correlation with dynamics and rewards, such as background features. It would be crucial to analyze if the learned policy is truly leveraging the object-centric representation or if it is relying on spurious correlations. Additionally, the ablation should include removing the transformer component and evaluating the performance with a simpler architecture to understand the specific contribution of the transformer in modeling the interactions.

 **[About the compositional generalization]**  

-  Can the method generalize to the case where the novel objects (e.g., different shape but similar to the ones seen in the training, e.g., cuboid versus cube) exist during the inference phase? 

- Does the model possess capabilities for both extrapolation and interpolation with respect to the quantity of objects involved? To illustrate, consider a scenario wherein the model is trained on sets of 2, 4, 6, and 8 objects, and subsequently tested on sets of 3, 5, 7 (interpolation) as well as 1, 9, 10 (extrapolation). While I acknowledge the presence of some relevant results in Figure 5, a more systematic and thorough analysis of the model’s extrapolation and interpolation capabilities would be beneficial. This approach would align with the high-level conceptualization of generalization discussed in [2]. It is important to determine the limits of the model's generalization capabilities, especially when the number of objects significantly deviates from the training distribution. This should include an analysis of the performance degradation as the number of objects increases or decreases.

 **[About the interaction]**  

-  I would appreciate additional clarification from the authors regarding the nature of entity interactions within the model. From my perspective, these interactions can be broadly classified into two categories: (1) interactions that influence dynamics without impacting the reward, and (2) interactions that affect both dynamics and reward. While I understand that the transformer is capable of capturing both types of interactions, a more explicit discussion on how it accomplishes this, and the implications of these interactions on the model’s performance, would be highly beneficial and contribute to a more thorough understanding of the model’s capabilities. It would be helpful to see a breakdown of how the transformer attends to different objects and how these attention patterns correlate with the types of interactions.

- I am interested in understanding how the density and frequency of interactions influence the performance of policy learning within the model. Could the authors possibly quantify and assess the model’s precision in predicting interactions across varying levels of interaction density and frequency? One potential metric for this evaluation could be the accuracy of the predicted entity state in comparison to the ground truth state, especially if direct interaction capture proves challenging within the simulator. I hypothesize that a reduction in workspace size, given a constant number of objects, is likely to increase interaction occurrences. Focusing on this aspect would provide valuable insights into the model’s robustness and adaptability under different operational conditions. It would also be useful to analyze the attention patterns in the transformer as interaction density and frequency change, to see if the model is adapting its focus appropriately.

 **[About the presentation]**

Minor: I would recommend transferring the contents of either Appendix A or E to the main paper. This adjustment not only enhances the overall presentation but also efficiently utilizes the remaining available space (currently less than 9 pages).

### Questions
I list the weaknesses and questions together in the above section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an object-centric RL model that can learn to manipulate many objects and shows generalization capabilities. The main contribution is the combination of Deep Latent Particles (DLP) as entity-centric perception pipeline and a transformer for policy and Q function. By defining a reward based on feature closeness and geometric distance there is no matching between goal-image and current image required. The only caveat is that the objects need to be filtered (the robot needs to be removed).  
The proposed method is pretty simple in comparison to prior work that considers entity-entity interactions.

### Strengths
- scalability to many objects
- a relatively simple method
- no explicit matching is required
- multiview
- supplementary contains important comparisons w.r.t. the reward etc.

### Weaknesses
 - number of objects known.
- missing related work and baselines:
   - SRICS [1] is like SMOURL but dealing with object-object interactions 
   - DAFT-RL[3]: also tackles the interaction problem and baselines therein
     DRAFT-RL is fairly recent, but it contains, IMO, relevant related work and further baselines, such as:
     NCS [3], STOVE [4] etc.
- supervision/filtering of entities such that only objects go into chamfer reward computation is hidden in the appendix 
- only empirical results on one type of environment: I am wondering how well it would generalize to more cluttered scenes, e.g. to a kitchen environment
 
Details:
- Fig 5: too small font in the right subplot
- Appendix A: Chamfer rewards:
  The definition of $X_j$ and $Y_i$ after Eqn (1): what is the $i$ in the definition of $X_j$? Do I understand correctly, that it is all $x$ that have $y_j$ as their closest entity in $Y$? 
  Also afterward, when you write how to obtain standard Chamfer, the $sum_j$ is somehow missing for the second fraction. 
- I think some more information about the Generalized Density Aware Chamfer reward should go into the main text, and also that non-object particles are removed.
- A paper that also addresses many-object manipulation with an object-centric representation is [5] (not from images)

- citations/references are often published at conferences but listed as arXiv papers

### Questions
- how important is it that the robot is mostly white on a white background? What happens if a larger part of the robot is seen in the images? I suggest discussing this in the limitations. Also, the need to filter non-object entities. Other works would also move the robot to a particular position in the scene if part of the goal. 
- what happens if the number of latent particles is higher than the number of entities?
- How do you compare to the above-mentioned baselines?

--- Post rebuttal update. My concerns were addressed. I changed my score from 5 to 8.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors solve table-top goal conditioned tasks form pixels using particles encoding and a transformer based RL. This is an interesting improvement over previous SOTA works and its major weakness are: 1) entities are fixed cubes-with-specific-color, thus there is no possibility to generalize to other objects with different properties, 2) interaction between the objects has not properly been demonstrated and 3) related work could be improved.

### Strengths
-	The paper is clear, well written and the topic is very interesting for the community
-	The viewpoint is a nice work around to solve depth ambiguities 
-	The conditional goal transformed is sound and nicely implemented for an actor-critic RL.
-	Inputs are just pixels, thus making the problem very complex.
-	Clever use of the Chamfer Distance with the particles.
-	Examples animations provided that shows the system working.

### Weaknesses
 **Related work**

The literature review is too focused on RL and could be improved.

Example of missing SOTA object-centric perception:
M. Traub et al. Learning what and where: Disentangling location and identity tracking without supervision,”  International Conference on Learning Representations, 2023.

“learning to manipulate” The citations related to manipulation are only for image segmentation, there is a scarce but very good literature on object-centric manipulation. The majority with full observability but some from pixels.

- Works based on Interaction Networks, Propagation Networks and Graph networks. E.g., A. Sanchez-Gonzalez, N. Heess, J. T. Springenberg, J. Merel, M. Riedmiller, R. Hadsell, and P. Battaglia. Graph networks as learnable physics engines for inference and control.

- Examples from pixels: 
van Bergen & Lanillos (2022). Object-based active inference. Workshop on Causal Representation Learning @ UAI 2022.
Driess et al. "Learning multi-object dynamics with compositional neural radiance fields." Conference on Robot Learning. PMLR, 2023.

- Finally, regarding the use of particles for robotic control I really think that this work is seminal: 
Levine, S. et al. (2016). End-to-end training of deep visuomotor policies. The Journal of Machine Learning Research, 17(1), 1334-1373.

As an aside comment, we can find similar table-top behaviours as the one presented here using LLMs, e.g., “Palm-e: An embodied multimodal language model.”

**Methods:**

This sentence requires elaboration: “Obviously, we cannot expect compositional generalization on multi-object tasks which are different for every N.”

Assumption 1. Probably you are using a standard notation but please explain what is \alpha* and v*.

Could you explain the consequence of Theorem 2.

Why did you use off-policy algorithm TD3?

¿Why do you need RL to train the DLP? It was mentioned that this module is pretrained, so no goal would be needed. Otherwise, you constraint the training for the defined goals that are set by the designer.

Goal definition – Using the encoder. This is a common technique but prevents for proper generalization. How you would encode in this architecture non-predefined goals?, like move red objects to the left.

Particles and only cubes. Using particles is very interesting, but evaluation with non-cube objects is not tested. This means that it could be that the experiments are assuming that the objects are point-mass entities. This would prevent generalization. In particular, the definition of cube-red as a single entity seems very restricted so you cannot perform behavioural operations on other shapes with different colours or other properties. 

Also this rises the problem of permutation invariant, maintaining the identity of an object may is important in tasks that object permanence is needed for instance in dynamic-sequential tasks.

**Experiments**

¿Why adjacent goals require interactions? This can be solved reactively.

I find very interesting the Ordered-Push. Should be the EIT trained for each task or it is trained on all tasks and the executed?

I understand that you relegated the Chamfer distance to the Appendix, but it could be great that at least a written explanation is placed (or the equation) to understand how the rewards works.

Using this distance (and the L2)  as rewards why is RL needed, would it be enough to use a KL as objective function? Or are there other rewards used?

What is state input? Full observability?

The agent is learning arm-object interaction thanks to the RL approach but it is not clear that the system is learning objects interaction.
Compositional generalization. While I agree that training on N objects and then executing the task with less and more objects shows generalization capabilities. This does not necessarily endorses composition. 

Could you explain how the system changes when including more objects at the level of the  DLP and the EIT?

Baselines: The text says: “We use DLP as the pre-trained OCR for this method for a fair comparison”, but then SMORL is only compared in the results showed with “state” access. Does this mean that this is without using pixels as input.

It is interesting that using RL also unstructured approach cannot handle the complexity. We obtained similar results using an ELBO loss. However, this makes the comparison too naïve. As the comparison of your algorithm is against full observable (state) and unstructured.

**Minor comments**

- Please check open quotes, in latex you can use ``word”
- Self attention -> Self-attention

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an object- or entity-centric RL algorithm for learning goal-conditioned manipulation. As object-centric representations, the authors use the Deep Latent Particles (DLP) method. The novelty is in the policy and Q-network, for which they propose an Entity interaction transformer (EIT), which is a transformer-based architecture to process the structured per-object latent representations. They test the method in an object manipulation task, with a robot manipulator and 2 static viewpoints provided as observations. They adopt a goal-conditioned RL setup, where the goal state is provided as target images, and introduce a Chamfer reward term to train the policy and Q function. The experiments show that their method can match the performance of another structured latent state method (SMORL), and outperform it when using image goals. Moreover, they demonstrate compositional generalization, where an agent trained on i.e. 3 colored cubes can generalize to a task with N colored cubes.

### Strengths
- This paper provides various novel contributions such as the transformer architecture for the Q and policy network, the Champfer reward to train policies conditioned on goal images, and demonstrates compositional generalization.

- The experimental results show ablations for the various components, such as the Champfer reward, using object-centric structured latent state spaces and using multiple views.

### Weaknesses
 - The method seems very tied to the experimental setup of having a robot manipulator that needs to push objects to a particular location. Some of the proposed novelties such as the Champfer reward don't seem very applicable beyond this use case. Specifically, the Chamfer distance, while useful for aligning point clouds or object shapes, might not be the most appropriate reward signal for tasks that require more complex interactions or involve non-rigid objects. This limits the general applicability of the proposed method.

- The experiments are limited to a single environment of colored cubes. It would be interesting to see whether the approach can scale to various objects (for example YCB objects), and more cluttered scenes. The lack of diversity in object shapes and textures makes it difficult to assess the robustness of the learned representations and policies. Furthermore, the current setup does not explore the challenges of occlusions or varying lighting conditions, which are common in real-world scenarios.

- As hinted by the authors SMORL is more sample efficient, as it learns to manipulate a single object and can then generalize to the others. This seems to be an essential feature / reason to go to object-centric approaches. The fact that the proposed method does not leverage this aspect raises questions about its practical applicability in scenarios where data efficiency is critical.

### Questions
- An important rationale for object-centric representations for RL is that once you learn a policy on one object, you can apply it to other objects (i.e. explaining the sample efficiency gap with SMORL). Why did the authors choose to discard this feature in their architecture, and would there be options to combine the strengths of both?

P.S: Fig 6 caption has a typo "mathcing"

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
