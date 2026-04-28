# What Matters to You? Towards Visual Representation Alignment for Robot Learning

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
When operating in service of people, robots need to optimize rewards aligned with end-user preferences.
Since robots will rely on raw perceptual inputs like RGB images, their rewards will inevitably use \textit{visual} representations. 
Recently there has been excitement in using representations from pre-trained visual models, 
but key to making these work in robotics is fine-tuning, which is typically done via proxy tasks like dynamics prediction or enforcing temporal cycle-consistency. 
However, all these proxy tasks bypass the human's input on what matters to \textit{them}, exacerbating spurious correlations and ultimately leading to robot behaviors that are misaligned with user preferences.
In this work, we propose that robots should leverage human feedback to \textit{align} their visual representations with the end-user and disentangle what matters for the task.
We propose \textbf{R}epresentation-\textbf{A}ligned \textbf{P}reference-based \textbf{L}earning (\textbf{RAPL}), 
a method for solving the visual representation alignment problem and visual reward learning problem through the lens of preference-based learning and optimal transport.
Across experiments in X-MAGICAL and in robotic manipulation, we find that RAPL's reward consistently generates preferred robot behaviors with high sample efficiency,
and shows strong zero-shot generalization when the visual representation is learned from a different embodiment than the robot's.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposes Representation Aligned Preference-based Learning (RAPL).
It is a video-only tractable method to use human feedback preferences between three trajectories to align visual representations with what matter to the tasks.

RAPL first asks humans to rate preferences over a set of video triplets.

It then uses the Bradley-Terry model to interpret and leverage the preferences, but not directly to reward prediction.
Instead, it focuses all the data on representation alignment on the video pre-trained visual features (ResNet18).
It uses the optimal transport method, which transports one video embedding distribution to another, with minimal cost.
Given the aligned representation RAPL then uses optimal transport to design a visual reward for the robot policy.

RAPL is then tested against ground truth policy, TCC, and vanilla RLHF. 
We first tested the same embodiment for both training and testing.
This first test is done on a toy X-MAGICAL environment, and then a realistic IsaacGym simulator.
For the former, the task is kitchen top cleaning, with avoiding off-limits zone. 
With the triplet training size of 150, RAPL is able not only to make spatial progress, but to be close to human preference. 
This results in a higher overall binary success rate on the task.

The IsaacGym simulator also shows similar results, where the RAPL features are aligned with GT on preferred videos, and no alignment on dislikes.
Further analysis shows that RAPL focuses on task-relevant objects and regions is the reason for the significantly higher final task success rate.

RAPL is then tested on zero-shot generalization setup, where the testing robot embodiment is different from that of training.
This second test is also done in X_MAGICAL, and then the robot simulator. For both RAPL is the best, closest to the ground truth performance.
In fact, on some combination (X-MAGICAL train on short stick, test on medium stick), RAPL improves its performance of the previous non-cross modal setup.

### Strengths
The paper presented a novel preference-based representation alignment and robot policy learning techniques.

The testing section is quite thorough and goes in-depth on the various nuances of what is being learned and accomplished in the actual robot task.

### Weaknesses
No discussion on what is still hard to do or not reliable.
Also, evaluation based on difficulty level of the configuration, shape, number of objects needed to be cleared would help toward answering the previous question.
Another is to compare with a second, very different, task.

### Questions
How does the visual attention map (figure 11, supplementary material) computed?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a new method called Representation-Aligned Preference-based Learning (RAPL) to align robot’s visual representation using human preferences. The paper formally defines visual representation alignment problem for robotics as minimizing divergence between human’s latent preference and robot’s representation space. RAPL uses human preference rankings over video triplets to learn representations aligned with preferences of humans and it then uses optimal transport to map the aligned representation to the reward for training. Authors present results in simulation on table top manipulation and 2 block rearrangement tasks. They demonstrate RAPL outperforms and is sample efficient compared to RLHF and temporal consistency based methods in all environments. In addition, they also show RAPL enables zero-shot generalization of rewards to new embodiments for both tasks.

### Strengths
1. Idea of aligning visual representations to human preferences and using that to extract preference based rewards is interesting and novel
2. Experiments are well designed and demonstrate RAPL outperforms vanilla RLHF in the studied simpler manipulation and block movement tasks is promising.
3. Results demonstrating zero-shot generalization to new embodiements and sample efficiency gains further strengthen benefits of using RAPL.
4. Paper is well written and easy to follow

### Weaknesses
1. Experimental setup is promising but the evaluation is done on simpler tasks. With just 150 triplet dataset used for both the tasks to learn preferences the tasks being studied brings up a question about how well this approach works on more complex tasks? For example, the block movement task in x-magical environment only requires agent to avoid the blue box in the environment. This can essentially be treated as a simple obstacle to avoid in the environment which is simple to learn in general. Some example tasks authors could use for evaluation are: block stacking task with constraints where a user prefers stacking blocks based on size i.e. largest block is at lowest followed by smaller blocks irrespective of the color of boxes. This setup tests generalization ability of the policy to different colors and ability to reason about object size based on preferences. My point being preference-based learning needs to be evaluated with tasks that have distractors that are difficult to pick up. It’d be nice if authors can add more experiments on different manipulation tasks with such properties
2. One baseline I’d like to see in addition to RAPL is how well does a simple contrastive pretrained visual representation as reward with same optimal transport logic performs in comparison to RAPL. It is unclear how beneficial RAPL’s triplet sampling is for the current set of tasks being considered. 
3. For the cross-embodiment experiments the simple tasks of block movement doesn’t necessarily highlight how well the proposed approach is performing. I’d be interested in seeing similar results in simple object pick and place task similar to one asked in W1.
4. Human preferences are multi-modal in nature i.e. different people have different preferences. The current setup doesn’t consider multi-modal preferences and show experiments comparing different methods in such a setup which seems like a big flaw in current experimental setup. I’d like authors to consider adding experiments that’d demonstrate effectiveness of RAPL under such setting

### Questions
1. In Figure 6. the RLHF results are quite poor. Have authors tried scaling training for RLHF for the same experiment to figure out how long does it take to reach RAPL/GT performance?

My major concern is evaluation on simple object movement tasks and no evaluation on tasks with multi-modal preferences if authors add more experiments that'd address my concerns I’d be happy to update the rating

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes Representation-Aligned Preference-based Learning (RAPL), a method which leverages human feedback to align visual representations with the end-user. Preference-based learning and optimal transport are used for this alignment and for the policy learning. Experimental results in two different environments reveal that RAPL outperforms prior work by learning a policy which both leads to higher rewards and has better sample efficiency.

### Strengths
- Well-written. The paper is very well-written and easy to follow. The figures very much aid in understanding the paper.
- Experiments. The experiments reveal that the proposed methodology outperforms baseline methods by non-trivial margins. The experiments are done across a number of environments, and evaluate the proposed methodology in a number of different ways.
- Ablations and Visualizations. Ablations are conducted and visualizations are included to better understand how and why the proposed methodology performs better than the baselines.

### Weaknesses
 - Missing / weak baselines.
  - Zhang et al (2020) is described to be the most similar to the proposed methodology. Why is this not compared to?
  - The main baseline appears to be TCC (Zakka et al., 2022; Kumar et al., 2023). Which of these (Zakka et al., 2022 vs Kumar et al., 2023) is used as the baseline? Furthermore, both Zakka et al., 2022 and Kumar et al., 2023 report results on {long-stick, medium-stick, short-stick, gripper} tasks -- why are these tasks not used to report results, for a completely fair comparison? This would be the most revealing comparison to the baselines.
  - A comparison to other pre-training work is made by comparing to MVP-OT, which is revealing. MVP is trained on Ego4D, so there is a massive distribution shift, perhaps explaining the poor performance. For a fairer comparison, could Masked Visual Pre-training be performed on data from the environments directly (e.g. using the trajectories)? 
  - While the visual backbone models are initialized with ImageNet pre-trained weights, may be revealing to include this (without any further training) as another baseline.
- Data is simulated. A simulated human model is used, rather than learning from real end-user feedback. 
- Figure 3 qualitatively shows the reward correlation -- quantification of such correlation using e.g. Spearman's correlation coefficient, compared to baselines, would be revealing.

### Questions
- How is the proposed approach better than GT for "Avoiding"?
- There seem to be error bars on many of the plots -- how many trials is this over?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper attempts to utilize human feedback to synchronize visual representation with the end-user's priorities for the task at hand. The authors present the Representation-Aligned Preference-based Learning (RAPL) method to tackle challenges in visual representation alignment and visual reward learning. Trials conducted in XMAGICAL and robotic manipulation demonstrate that RAPL consistently produces desired robot behaviors with notable sample efficiency and robust zero-shot generalization.

### Strengths
The paper pioneers the formalization of the visual representation alignment challenge in robotics, framing it as metric learning within the human representation space. Their proposed RAPL targets resolving the alignment issue and facilitates learning visual robot rewards through optimal transport. Experimental results further demonstrate that RAPL consistently yields desired robot behaviors, maintaining high sample efficiency. Lastly, they also show zero-shot generalization across embodiments.

### Weaknesses
1. The task complexity may not adequately highlight the significance of human feedback in robot learning. The current tasks, while demonstrating the method's capabilities, do not fully capture the nuances of real-world scenarios where human feedback is crucial for resolving ambiguities or specifying complex, multi-faceted objectives. The tasks seem relatively straightforward, and it's not clear that the learned representations are truly necessary to solve them, or if simpler methods could achieve similar results.
2. While the approach captures human-like preferences, there's no concrete evidence to validate its representation of genuine human preferences in real-world tasks. The paper relies on simulated human feedback, which may not accurately reflect the complexities and inconsistencies of actual human preferences. This raises concerns about the generalizability of the learned representations and rewards to real-world applications where human input is inherently subjective and variable. The current method of preference generation may not be sufficiently complex to capture the full spectrum of human preferences.
3. The author should elaborate in the main paper on their method of utilizing privileged access to state information for dataset generation. The current description is too brief and lacks sufficient detail. It is unclear how the privileged state information is used to generate the preference dataset, and what specific reward functions are employed. This lack of clarity makes it difficult to assess the validity and generalizability of the approach.
4. While the efficacy of this approach is demonstrated with the X-Magical and ISACCGym robots, it would be beneficial to see its applicability in other robotic embodiment or real-world scenarios. The current experiments are limited to simulated environments and specific robot platforms. It is not clear how well the method would generalize to different robotic systems or to real-world scenarios with more complex dynamics and sensory inputs. The lack of real-world validation limits the practical impact of the research.

### Questions
All listed in the weakness section. I would consider changing my rating, if the author could address my questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
