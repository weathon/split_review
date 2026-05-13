# The Power of the Senses: Generalizable Manipulation from Vision and Touch through Masked Multimodal Learning

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
Humans rely on the synergy of their senses for most essential tasks. For tasks requiring object manipulation, we seamlessly and effectively exploit the complementarity of our senses of vision and touch. This paper draws inspiration from such capabilities and aims to find a systematic approach to fuse visual and tactile information in a reinforcement learning setting. We propose \textbf{M}asked \textbf{M}ulti\textbf{m}odal \textbf{L}earning (\textbf{M3L}), which jointly learns a policy and visual-tactile representations based on masked autoencoding. The representations jointly learned from vision and touch improve sample efficiency, and unlock generalization capabilities beyond those achievable through each of the senses separately. Remarkably, representations learned in a multimodal setting also benefit vision-only policies at test time. We evaluate M3L on three simulated environments with both visual and tactile observations: robotic insertion, door opening, and dexterous in-hand manipulation, demonstrating the benefits of learning a multimodal policy. Code and videos of the experiments are available at \url{https://sferrazza.cc/m3l_site}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes to learn visuo-tactile representation for manipulation with mask autoencoding. By utilizing MAE objective and structure, the learned joint representation improves the performance, sample efficiency and generalization ability of the policy. The method is evaluated in simulation for tactile insertion, door opening and in-hand cuda rotation tasks. Results also show the joint representation improves the vision-only policy performance in the test time.

### Strengths
1. Utilizing MAE architecture for modeling multimodal information for manipulation is intuitive and easy to understand. MAE objective for modeling joint representations is also a natural choice.
2. This work provides enough technical details, hyper-parameters, and visualization for reproducing the results.
3. This provides an interesting result that with multimodal self-supervised learning, the performance of vision-only policy improved during the test.

### Weaknesses
1. Manipulation with tactile sensor and visual input has been evaluated in the real world for different tasks[1]. To actually validate the performance of the proposed method, the real world evaluation is required. Especially for noisy tactile sensory information. 
2. To validate the effectiveness of MAE architecture and self-supervised objective in this application, additional baselines (not limited to the baselines i mentioned) need to be compared. Qi, et al utilize a visuotactile transformer to model sequential observations. Hansen, et al show promising result in applying self-supervised learning in visual RL. 
3. Missing tactile-only baseline, to fully address the essence of the multimodal representation.
4. Additional arm (or hand) proprioception information should be included in this kind of multi-modal manipulation pipeline, since it’s much easier to get (in sim and real) and provide rich information for manipulation tasks.
5. Out of three tasks, the proposed framework only outperforms vision-only baselines in In-hand rotation tasks. It seems tactile insertion and door-opening tasks are not quite tasks to evaluate the additional usage of tactile information.
6. For generalization experiments, randomization on on physical parameters might not be enough. Adding different level of noise to the visual observation and tactile reading and test the generalization on that end could further validate the effectiveness of the proposed self-supervised pipeline.

### Questions
1. It would be great for authors to address the things mentioned in the weakness section
2. The result in FIgure 10, shows the learned MAE could reconstruct almost the full observation with quite limited observation. I’m wondering whether the learned model can show the same level of performance if there are noise in visual observation or tactile reading. Otherwise it looks lille the model is overfitting to the training distribution.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an approach for combining visual and tactile data in training robot manipulation policies in simulation. The main contribution of the paper is a representation learning algorithm (M3L) based on masked auto-encoding that can ingest both image observations and tactile observations (taxels). The policy learning with the learned representations can be performed with existing reinforcement learning algorithms like PPO. Experiments on three robot simulation tasks show that the proposed approach is effective in distilling multimodal touch+vision representations for policy learning.

### Strengths
- The paper presents a neat idea of combining touch and vision through an existing paradigm of masked autoencoding, and showing that this is helpful for simulated robot manipulation tasks. The overall idea is simple and can be used widely with minimal modifications. 

- The simulation results are interesting in terms of the same algorithm being able to learn policies for very different tasks when trained separately on each simulation environment. It is good to note that these tasks span fine-grained manipulation, articulated object opening, and dexterous manipulation. 

- The overall paper is well-written and insights are communicated clearly. Sufficient details are provided in the Appendix, and the video results are helpful in understanding the tasks.

### Weaknesses
1. The paper ignores several different related works, both in terms of tactile sensors used for robotics, and machine learning approaches that use touch as a modality for manipulation tasks. Here are some missing papers that should be discussed:

         a) robot learning papers with tactile data [1,2] these papers show real-robot dexterous manipulation tasks with either tactile data along or with both vision and tactile data (followed by RL with sim2real transfer)
         b) versatile tactile sensors for real-world manipulation [3]

2. The simulation results are interesting in terms of the same algorithm being able to learn policies for very different tasks (as mentioned in the strengths) but it is unclear to me why experiment with only three tasks? Most reinforcement learning in simulation papers show results on a large number of environments, and this is important to understand the capabilities of the proposed approach, without over-indexing on a particular environment. The current set of tasks, while diverse, does not provide a comprehensive evaluation of the method's robustness and generalizability across a wider range of manipulation challenges.

3. There are no external baselines compared against. All the comparisons are with variants of the proposed M3L algorithm. The related works in representation learning that use vision-only observations, including papers that do pre-training for representation learning are relevant for empirical comparisons (for example [4,5]). Without these comparisons, it is difficult to assess the true advantage of the proposed multimodal approach over existing vision-based methods. The lack of comparison with established representation learning techniques makes it hard to determine if the performance gains are due to the novel combination of touch and vision, or simply due to the use of a masked autoencoding approach.

4. The introduction mentions "M3L demonstrates better zero-shot generalization to unseen objects and variations of
the task scene" however the experiments show only very weak generalization to minor changes in the object (in particular mass, damping, friction variations). Hence the claim is not really substantiated in my understanding. It is important to show generalization to actually different objects (for example with geometric variations like shape and size, in addition to the current variations). Also, the results should evaluate this for a number of different objects and not just a single new object, in order for the conclusions to be statistically significant. The current evaluation is insufficient to support the strong generalization claims made in the introduction. The limited variation in object properties does not adequately test the method's ability to generalize to novel scenarios.


### Questions
Refer to the list of weakness for more details. 

1. Is it possible to provide a more detailed treatment of related works? In particular, robot learning papers with tactile data [1,2] and versatile tactile sensors for real-world manipulation [3] are relevant, and missing.

2. Is it possible to have more than three simulation tasks? Most reinforcement learning in simulation papers show results on a large number of environments, and this is important to understand the capabilities of the proposed approach, without over-indexing on a few particular environments.

3. Is it possible to compare with external baselines? The related works in representation learning that use vision-only observations, including papers that do pre-training for representation learning are relevant for empirical comparisons (for example [4,5])

4. Is it possible to evaluate generalization with different objects (shapes, sizes, visual appearances) ? Since generalization is a main claim of the paper, this seems particularly important. 

5. Real-World tactile data is usually very noisy, but simulation data is clean. Is there anything that will need to be changed in the approach for bridging this gap or making the representations more robust to noise, when real-world deployment is attempted? In general, the results in the paper are not convincing for justifying the last paragraph of page 9, because there is very little generalization demonstrated in simulation itself.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduced a technique that merges multimodal self-supervised representation learning with robot policy learning through the PPO algorithm. This approach showcases that by utilizing masked autoencoding for both policy and visual-tactile representations, one can enhance sample efficiency and achieve superior generalization capabilities.

### Strengths
1. The content is articulately written, making it easily comprehensible.
2. The appendix offers in-depth details about both the model and the environment, ensuring reproducibility of the work.
3. The model innovatively incorporates multimodal representation features to address robot learning tasks, marking a significant stride in this research direction.

### Weaknesses
1. A prevalent challenge in contemporary research within this domain is tactile simulation. The tactile simulation employed in this study lacks the desired accuracy. Moreover, the introduced method hasn't been empirically tested or combined with tactile sensors in real-world experiments, which is a missing link for comprehensive validation.
2. The ViT model, as utilized, is computationally intensive and has a propensity to overfit to specific problems. The potential benefits of ViT's self-supervised pre-training techniques, such as MAE, ought to be realized across a diverse range of datasets or environments. Given the constraints observed in the study—limited tasks, a restricted set of objects, and minimal variations in background textures—it's challenging to fully endorse the promise of the proposed approach. The limited dataset size and lack of diversity in object shapes and textures raise concerns about the generalizability of the learned representations.
3. As discerned from Figure 6, there's an inconsistency in the results between the baseline and the proposed method across various tasks. This discrepancy muddles the clarity needed to conclusively determine the efficacy of the proposed method. It would be advisable to extend the scope by implementing over 10 distinct tasks and undertaking comprehensive statistical analyses to more convincingly demonstrate the method's effectiveness. The current set of tasks, while varied, does not provide a sufficiently robust evaluation of the method's capabilities across a wide range of manipulation scenarios.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
