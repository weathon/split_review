# Zero Shot Generalization of Vision-Based RL Without Data Augmentation

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Generalizing vision-based reinforcement learning (RL) agents to novel environments remains a difficult and open challenge. Current trends are to collect large-scale datasets or use data augmentation techniques to prevent overfitting and improve downstream generalization. However, the computational and data collection costs increase exponentially with the number of task variations and can destabilize the already difficult task of training RL agents. In this work, we take inspiration from recent advances in computational neuroscience and propose a model, Associative Latent DisentAnglement (ALDA), that builds on standard off-policy RL towards zero-shot generalization. Specifically, we revisit the role of latent disentanglement in RL and show how combining it with a model of associative memory achieves zero-shot generalization on difficult task variations \textit{without} relying on data augmentation. Finally, we formally show that data augmentation techniques are a form of weak disentanglement and discuss the implications of this insight.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes an algorithm based on SAC, that performs latent disentanglement representation and combines it with an associative memory model to achieve zero-shot generalization in vision-based RL. The paper shows that the proposed approach improves upon several baselines when tested in two evaluation environments (color hard and distracting cs). In addition, the authors theoretically prove that data augmentation methods for vision-based RL implicitly perform "weak" disentanglement, and therefore lead to a noticeable zero-shot generalization.

### Strengths
* The paper tackles the important challenge of generalization in vision-based RL.

* The paper is well-written and easy to follow.

* The background section clearly explains the different methods for disentanglement representation and associative memory. Also, it provides motivation for using these methods for zero-shot generalization.

* There is a good discussion about the relevant work of zero-shot generalization in vision-based RL.

* The paper visually demonstrates (Figure 6) that the resulting disentanglement representation successfully encodes different data attributes.

### Weaknesses
* The method was tested in a narrow set of test environments (color hard and distracting cs). The paper could be improved if the authors would show the benefit of the proposed approach on standard (and more challenging) procedurally generated vision-based datasets for zero-shot generalization in RL, such as Procgen [1] or Crafter [2].

* In lines 180-184, the authors mention that one drawback of previous approaches is that the latent representation excludes all information not relevant to the training tasks, which can hinder adaptation to new tasks that involve information that was previously considered irrelevant. The paper would benefit from a concrete experiment that showcases this failure and demonstrates how the proposed approach handles it. 

* Some baselines are missing from the experiment section. For example, a comparison to methods that use the information bottleneck to exclude irrelevant information from the state representation in vision-based RL, such as [3]. 

* An ablation study of |zd| (the dimension of the latent space) is missing. 
 
[1] Cobbe K, Hesse C, Hilton J, Schulman J. Leveraging procedural generation to benchmark reinforcement learning. In International conference on machine learning 2020 Nov 21 (pp. 2048-2056). PMLR.

[2] Hafner D. Benchmarking the spectrum of agent capabilities. arXiv preprint arXiv:2109.06780. 2021 Sep 14.

[3]  Maximilian Igl, Kamil Ciosek, Yingzhen Li, Sebastian Tschiatschek, Cheng Zhang, Sam Devlin, and 492 Katja Hofmann. Generalization in reinforcement learning with selective noise injection and information 493 bottleneck. In Advances in Neural Information Processing Systems 32, pages 13956–13968, 2019.

### Questions
1. Please address the aforementioned weaknesses.

2. Is it possible to utilize an RNN unit instead of frame stacking to incorporate temporal information into the latent code?

3. Section A.2 and Figure 7 are not clear to me. Would you please explain the experimental setting there and the results? 

4. How was the hyperparameter search done for all the baselines?

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
This work introduces Associative Latent Disentanglement (ALDA), a zero-shot generalization strategy for vision-based RL free of data augmentation. Inspiring by neurobiology, ALDA enables agents to generalize to out-of-distribution (OOD) activities by combining associative memory with disentangled latent representations. The results of the experiments show that ALDA is just as good at generalization as or better than current augmentation-based methods, especially in difficult OOD settings.

### Strengths
1. The paper takes ideas from neuroscience and combines latent disentanglement with associative memory to present a new, augmentation-free method for zero-shot generalization in RL.

2. The methodology is sound, with experiments across challenging tasks that effectively support the primary claims of the paper.

3. The paper is generally clear and well organized, though some technical sections could be further clarified for readability.

4. This work has potential impact by presenting an efficient alternative to data augmentation, likely inspiring further research on generalization in RL without large datasets.

### Weaknesses
1. More proof of ALDA's generalization ability would be obtained by extending the studies to more varied settings, such as Procgen.
Procgen's randomly produced levels and diverse game environments present distinct challenges, unlike those found in the DMControl suite. These settings may demonstrate the efficacy of ALDA's generalization across diverse activities, offering a comprehensive assessment of its adaptation to novel and intricate situations.

2. More illustrations or pseudocode could help to clarify the function of associative memory in processing OOD samples. Particularly, pseudocode illustrating ALDA's processing of an OOD sample—from initial encoding to final output—would effectively elucidate the function of associative memory in the generalization process.

3. An assessment of ALDA's effectiveness in real-world settings would demonstrate its applicability and scalability. For example, testing on a robotic manipulation job requiring the robot to generalize to objects of diverse forms, sizes, or textures not seen during training, could effectively showcase its generalization capabilities in practical applications.

### Questions
1. In order to show that ALDA is generalizable to a wider variety of OOD contexts, could you test it on other benchmarks, such as Procgen?

2. Could you elaborate on the associative memory dynamics in ALDA, perhaps using a pseudocode or flow diagram, to show how it specifically supports zero-shot generalization?

3. Is the method applicable to an offline reinforcement learning setting, given that online reinforcement learning can be costly and risky in real-world environments? It would be beneficial to address the adjustments necessary for adapting ALDA for offline reinforcement learning, along with the potential obstacles the authors expect in this adaptation.

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
A common way to improve the generalization ability of an agent in reinforcement learning is through data augmentation. However, collecting data can be costly with increasingly varied tasks.
This paper achieves zero-shot generalization by learning disentangled representations, where each latent feature dimension corresponds to an unique source of variation in the input image.
Inspired by neuroscience, the authors incorporate associative memory into the original representation learning loss in QLAE, and build a novel framework called Associative Latent DisentAnglement (ALDA) for RL.
ALDA is evaluated on various control tasks with two types of variations (color-hard and distracting backgrounds), and compared to state-of-the-art methods.
While its performance lags behind data-augmentation-based methods for generalization, it outperforms previous approaches of learning disentangled representations.

### Strengths
- Improving generalization by learning better representations is not a new concept.
For instance, Zhang et al. [2021] aim to encode only task-relevant information from input images.
However, the idea of training disentangled representations specifically for generalization, particularly without data augmentation, is a novel approach.
Recently, numerous studies have explored the effects of scaling laws on enhancing generalization, yet methods for achieving generalization without exposure to out-of-distribution data remain relatively under-explored.

- The idea of considering memory for generalization is intuitive and the author build an interesting connection between the disentangled representation learning framework and associative memory network.

A. Zhang, R. McAllister, R. Calandra, Y. Gal, and S. Levine. Learning invariant representations for reinforcement learning without reconstruction. ICLR 2021

### Weaknesses
- According to the paper, the strong disentanglement requires that each dimension in the latent representation corresponds to a unique source of the variation in the image.
As for the weak disentanglement, a more clear and precise definition (line 216 to line 219) might be helpful for the reader to understand. 
For example, one natural question to ask is if several dimensions in the latent representation $\textbf{z}$ correspond to one unique source, is this a weak disentanglement?
I would appreciate it if you could provide concrete examples for these two types of disentanglement.
This would help readers better understand the key concepts and their implications for the method.
- And the relationship between disentanglement and generalization ability is not so clear to me.
According to the line 233 to line 235, if I understand correctly, weak disentanglement can also lead to generalization.
Is strong disentanglement a necessary condition for generalization or is weak disentanglement sufficient?
If not, please explain more about the benefits and drawbacks of using strong disentanglement vs. weak disentanglement? 
- In the section of experimental results, an explanation is provided for the performance gap between ALDA and SVEA.
However, as mentioned in the paper, the proposed method can definitely be combined with data augmentation.
So, it will strength the paper if the results of combining ALDA and data augmentation are presented.
- minor: missing punctuation on line 305.
In figure 2, $n_s$ is not defined in the paper. 
I guess it is $n_z$ on line 290.

### Questions
- In Figure 2, the encoder is only updated by the ALDA loss, as indicated by the green arrow and the latent model is updated by both the ALDA loss and the critic loss, as indicated by the red arrow.
Is there a reason for this? Any ablation study for this design choice?
- On line 345, according to "the scalar codebooks Z, which can be interpreted as predetermined memories", are the codebooks trained or pre-defined?
If trainable, are they trianed with equation 8 such that $V$ are actually trained parameters?
If pre-defined, how the values are chosen?
- Is there an intuitive connection between equation 7 and Figure 1?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes Associative Latent DisentAnglement (ALDA), a novel method for zero-shot generalization in vision-based reinforcement learning (RL) without data augmentation. ALDA combines disentangled latent space representations with an associative memory mechanism inspired by biological systems like the hippocampus. This enables RL agents to generalize to out-of-distribution (OOD) environments by recalling previously seen factors of variation, without need of augmentation in training. ALDA outperforms several state-of-the-art methods in tasks involving distribution shifts, demonstrating zero-shot generalization without using data augmentation.

### Strengths
Originality:
The idea of using disentanglement and associative memory for RL to achieve zero-shot generalization is relatively less explored. It is nice formulation to combine both for RL. Unlike existing methods that rely heavily on data augmentation, ALDA achieves generalization without it.

Quality:
The paper is well-researched. It shows data augmentation is one form of disentanglement. It proposed new methods to combine disentanglement and association. The experimentation is carried with ablation studies on different component of the method.

Clarity:
The paper is generally clear, with a well-structured narrative that explains the problem, the motivation, and the solution. It draws inspiration from biological system which is well articulated

Significance:
Its significance lies in that it presents a method for generalization without augmentation. It would be very useful under the case that we cannot anticipate what shift will happen.

### Weaknesses
The papers lacks a more thorough discussion of its failure cases.

Suggestion: 
1. What if you vary distracting intensity, how would that change the relative results, especially compared to SVEA. 
2. I also notice it perform worse than SVEA in the training environment, can you add interpretations on that?

### Questions
1. In figure 6, top half, the robot starts from different pose when traversing the latent code. what if it starts from the same as in the bottom half

2. What if we compare the proposed method to data augmentation method that uses simpler augmentation, such as color jitter or random crop? For example 

Kostrikov, Ilya, Denis Yarats, and Rob Fergus. "Image augmentation is all you need: Regularizing deep reinforcement learning from pixels." arXiv preprint arXiv:2004.13649 (2020).

Hansen, Nicklas, and Xiaolong Wang. “Generalization in Reinforcement Learning by Soft Data Augmentation.” 2021 IEEE International Conference on Robotics and Automation (ICRA), IEEE, 2021. Crossref, https://doi.org/10.1109/icra48506.2021.9561103.

You can also test of SVEA only using simpler augmentation.

I understand that the main contribution of this paper is generalization without augmentation, it is okay that it is not performing as good.

3. Can you combine the proposed approach with data augmentation? How would you do that?

4. Can you combine disentanglement / association with dynamics? How would do you that?

### Soundness
3

### Presentation
3

### Contribution
3
