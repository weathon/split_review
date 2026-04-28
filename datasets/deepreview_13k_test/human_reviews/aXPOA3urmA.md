# Cross-Domain Reinforcement Learning via Preference Consistency

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Cross-domain reinforcement learning (CDRL) aims to utilize the knowledge acquired from a source domain to efficiently learn tasks in a target domain. Unsupervised CDRL assumes no access to any signal (e.g., rewards) from the target domain, and most methods utilize state-action correspondence or cycle consistency. In this work, we identify the critical correspondence identifiability issue (CII) that arises in existing unsupervised CDRL methods. To address this identifiability issue, we propose leveraging pairwise trajectory preferences in the target domain as weak supervision. Specifically, we introduce the principle of cross-domain preference consistency (CDPC)–a policy is more transferable across the domains if the source and target domains have similar preferences over trajectories–to provide additional guidance for establishing proper correspondence between the source and target domains. To substantiate the principle of CDPC, we present an algorithm that integrates a state decoder learned through preference consistency loss during training with a cross-domain MPC method for action selection during inference. Through extensive experiments in both MuJoCo and Robosuite, we demonstrate that CDPC enables effective and data-efficient knowledge transfer across domains, outperforming state-of-the-art CDRL benchmark methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper describes a new method of cross domain reinforcement learning
based on the idea of receiving target domain preference labels rather than
target domain reward labels.  It proposes training an encoder/decoder to
map between source and target states including previouly proposed
consistency and reconstruction losses and adding in a preference loss.  It
also adds MPC at inference time to improve the action selection.  It
demonstrates its results in simulation using some standard cross-domain
experiments and compares to several methods using cross-domain approaches
and some that don't.

### Strengths
The paper is well written and easy to understand and I believe it presents
a new idea.

### Weaknesses
I have a few major concerns which are listed here:

1. I did not find the problem setup very compelling.  Its hard to imagine
robotics applications where its easy to get preference data but the reward
function is unknown.  This might well happen in language models or other
similar applications.  But the empirical studies were done on robotics
examples where the reward functions are well known.  In order to be
convincing, I think the empirical studies should be done in applications
where this problem setup really happens.

2. Cross domain preference consistency seems to make sense in the
applications that were shown -- basically you change the
kinematics/dynamics of a robot that still has roughly the same task
capability and does the same task.  Maybe that really is your main use
case, but that again leads to point 1 above.  In robotics it would be nice
to be to change the task for the same robot, but it seems unlikely that
CDPC applies in that case.

3. The effects of MPC are not well tested in the empirical study.  It seems
possible that the main thing making the algorithm perform well is the MPC
rather than the decoder learned via eq 5.  A useful comparison would be to
take the same target domain dynamics model to generate trajectories and
evaluate those trajectories with the critic learned by SAC-Off-TR and by
SAC-Off-RM.  You similarly could test CAT-TR plus MPC and DCC plus MPC to
see whether MPC is useful for resolving some of their limitations.


Here are some additional minor notes:

1. I did not find figure 1 helpful.  I agree some version of this figure
would be appropriate.  I found the decimal and binary distinction to be
confusing and maybe unnecessary.  While it was clear there were two
decoders, it was less clear how/why they both had zero cycle consistency
loss.

2. SAC-Off-TR is advertised as a "topline that should be an upper bound".
I don't believe that statement is accurate since while it does have the
benefit of the true reward function, it does not have the benefit of the
source domain information.

3. The empirical results figures are too small to read and on several I had
to just go with the text and ignore the figure.  Figs 5, 6, and 11 could
probably be remedied by simply scaling up to use all the horizontal space
available.  The others need bigger reformatting.  This would take up more
vertical space, but you could deduplicate and tighten up some of the text
in the early sections to make room.

### Questions
Please comment on the concerns listed above, focusing on the first three listed as "major" concerns.

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
For cross-domain transfer in RL, the paper proposes a CDPC method using preference consistency between the target and source domains. The proposed approach learns a state decoder to connect target domain trajectories with source domain trajectories, and then use MPC to select actions for the target domain based on the corresponding source domain rewards. Experiments show data efficiency of the proposed CDPC method and improved final performance compared to some prior methods.

### Strengths
- The ability to transfer knowledge across two RL domains is important for data efficiency but also challenging. This paper proposes a method based on the idea of preference consistency when we only have preferences over trajectories in the target domain. The idea is to find a mapping such that the preference ordering of trajectories in the source domain and the corresponding trajectories in target domain are consistent. Then based on this mapping, one can get the preference of any two target domain trajectories by mapping them back into the source domain and utilizing our source domain knowledge, which then allows one to apply MPC to select the best action. The idea is pretty novel and seems to be effective.

-  Multiple experiments are conducted to evaluate different aspects of the proposed CDPC method. It is shown that CDPC performs better than prior methods in several domain transfer problems, and ablation studies show the importance of the proposed preference consistency loss in terms of preference accuracy and final performance.

### Weaknesses
- In addition to the learned decoder, CDTO requires to learn a target-domain dynamics model, but little detail is provided for the target-domain dynamics model. Are the samples used in learning the target-domain dynamics taken into account in the sample efficiency calculation compared with other methods? Are there experiments showing the importance of the quality of this learned dynamics model?

### Questions
- For the preference accuracy in Figure 8, how is the preference accuracy evaluated? Are they evaluated on the same set of trajectories for all the methods?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel framework for cross-domain reinforcement learning that leverages pairwise trajectory preferences in the target domain as weak supervision. The proposed Cross-Domain Preference Consistency (CDPC) principle aims to address the correspondence identifiability issue (CII) in unsupervised CDRL by aligning trajectory preferences across source and target domains. Extensive experiments in MuJoCo and Robosuite demonstrating the effectiveness of CDPC in knowledge transfer across domains.

### Strengths
-  The idea of cross-domain preference consistency is Interesting.
- The experimental results are comprehensive.

### Weaknesses
- In the standard unsupervised Cross-Domain Reinforcement Learning setting, the learner is typically provided with a set of target-domain trajectories that contain only state-action pairs, without any reward signal. The authors, however, introduce an additional preference signal, which the reviewer believes contravenes the foundational assumption of unsupervised learning. The introduction of a sufficient number of preference signals could potentially allow for the inference of the underlying reward function, thus undermining the unsupervised nature of the task. Furthermore, the reviewer notes a lack of specificity in the experimental section regarding the quantity of preference signals used. The manuscript does not clarify how many preference data points were utilized, what proportion of the dataset they represent, or how the performance of the model scales with the amount of preference data. It is crucial to understand the sensitivity of the model's performance to the quantity of preference data, as this could significantly impact the generalizability and robustness of the proposed method.

- Regarding Figure 1, a lack of clarity on the implications of the correspondence identifiability issue. It appears that both $\tau_\alpha$ and $\tau_\beta$ are optimal trajectories, and the existence of multiple optimal trajectories within the same environment is a common occurrence. The reviewer questions whether the authors aim to identify a unique one-to-one mapping between the source and target domains. The necessity for uniqueness is not immediately apparent, and the manuscript would benefit from a more detailed explanation of why a unique mapping is required and how it affects the overall goal of the cross-domain transferability of policies.

- Concerning Equation 3, the reviewer inquires about the origin of the transition kernel T of the source domain. It is unclear whether this is learned through training or directly accessible through an environmental model.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a novel method, CDPC, to address the challenge of representation learning in cross-domain reinforcement learning. By leveraging trajectory preference signals from the target domain, the CDPC approach significantly enhances learning efficiency during knowledge transfer between the source and target domains.

### Strengths
1. Studies an important problem of cross-domain RL from offline data.

2. Shows a counterexample of the exist unsupervised CDRL issue (figure 1) and prpose a principle of cross-domain preference consistency to address this issue.

3. Clear writing in most places.

4. The experimental results on MuJoCo and RoboSuite demonstrate that our approach outperforms existing Cross-Domain Reinforcement Learning (CDRL) methods.

### Weaknesses
1. The reason for using MPC instead of other planning methods during the testing phase has not been clearly explained.

2. Although the experiments demonstrate that the combination of PBRL and MPC is highly effective in the context of CDRL, the advantages and underlying mechanisms of this integration have not been thoroughly analyzed. The work lacks theoretical exploration and a detailed discussion of its contributions.

3. The layout of the experimental results on page 10 requires revision.

4. Equations (3) and (5) should indeed be written with ":=" for consistency, just like Equations (2) and (4). Ensuring uniform formatting across all equations is important for clarity and professionalism in the presentation.

### Questions
1. How is "weak supervision" defined in the paper? No specific information has been provided. Please clarify this in the introduction section.

2. Are there any theoretical justification for the CDPC?

### Soundness
2

### Presentation
3

### Contribution
2
