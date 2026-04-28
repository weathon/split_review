# Unsupervised-to-Online Reinforcement Learning

- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 3, 3, 6

## Abstract
Offline-to-online reinforcement learning (RL),
a framework that trains a policy with offline RL
and then further fine-tunes it with online RL,
has been considered a promising recipe for data-driven decision-making.
While sensible, this framework has drawbacks: it requires domain-specific offline RL pre-training for each task,
and is often brittle in practice.
In this work, we propose \textbf{unsupervised-to-online RL} (\textbf{U2O RL}),
which replaces domain-specific \emph{supervised} offline RL with \emph{unsupervised} offline RL,
as a better alternative to offline-to-online RL.
U2O RL not only enables reusing a single pre-trained model for multiple downstream tasks,
but also learns better representations, which often result in \emph{even better} performance and stability
than \emph{supervised} offline-to-online RL.
To instantiate U2O RL in practice, we propose a general recipe for U2O RL
to bridge task-agnostic unsupervised offline skill-based policy pre-training and supervised online fine-tuning.
Throughout our experiments in nine state-based and pixel-based environments,
we empirically demonstrate that U2O RL achieves strong performance
that matches or even outperforms previous offline-to-online RL approaches,
while being able to reuse a single pre-trained model for a number of different downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Unsupervised-to-Online Reinforcement Learning (U2O RL) as an alternative to the conventional Offline-to-Online RL (O2O RL) framework. U2O RL replaces domain-specific, supervised offline RL with unsupervised offline RL, allowing a single pre-trained model to be adapted for multiple tasks. Experiments conducted across nine environments demonstrate that U2O RL can match or even surpass previous methods.

I do not currently agree with the direct acceptance of this paper. However, I recognize the importance of research on RL in pretrain-finetune frameworks. If the authors can satisfactorily address my concerns, I would be open to increasing my rating.

### Strengths
- The paper is well-written, and the proposed U2O RL framework is explained clearly.
- Research into specific paradigms within the pretrain-finetune framework for RL is valuable, and this paper contributes to that discussion.

### Weaknesses
 - While this paper proposes the U2O RL framework, it does not introduce any novel methods. Both the unsupervised offline RL pre-training and the online fine-tuning stages rely on existing algorithms. Additionally, the reward scaling adjustment in the bridging stage has already been employed in prior reward design approaches. Proposing a new “framework” is reasonable, but I believe the paper needs to provide more substantial evidence on why this U2O RL framework is more effective than the traditional O2O approach. Simply demonstrating feature co-adaptation to support the efficacy of representation learning in the offline phase may be insufficient. Furthermore, the paper should conduct a broader set of experiments: for instance, by testing various offline and online algorithms and using a wider range of environments to validate the framework’s effectiveness. Without these enhancements, the work seems somewhat incremental.
- For general reward maximization tasks, such as Walker, Cheetah, and Jaco, the U2O RL framework does not demonstrate a notable advantage; in some cases (e.g., Cheetah), performance is even lower. This could stem from difficulties in selecting an optimal skill latent vector  $z^*$  for these tasks, highlighting a potential limitation of the U2O framework.

### Questions
- Why does the feature dot product in the O2O framework for Walker Run and Cheetah Run (Fig. 4) diverge, indicating much poorer representation learning compared to U2O, yet the performance of O2O in these environments is similar or even superior to U2O? Intuitively, poorer representations should lead to poorer performance.

### Soundness
2

### Presentation
3

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
The paper presents an empirical analysis of how unsupervised to online finetuning for RL is better than offline to online finetuning.

### Strengths
1. The paper is clearly written and well motivated, having a single reusable model to perform finetuning makes sense and can improve RL pretraining.
2. The paper looks at a particular method HILP and provides a reward scale matching scheme to enable finetuning. This turns out to be quite important in performing efficient finetuning.
3. The paper considers a wide variety of tasks to demonstrate potential improvements over offline to online finetuning.

### Weaknesses
1. Insufficient empirical evidence to claim U20>O2O: In figure 3, it seems the results are not significant in 10/14 environments. How can we claim the U20 is a better strategy? Furthermore, insufficient details are provided about baselines of O2O and  off policy RL - eg. do they use the same network sizes and discount factor? It is clear in Table 1 that the baselines and U2O use different network sizes and discount factor as the prior entries are based on discount of 0.99 and use a network size of (256,256) for most tasks. These raises a number of questions on empirical evaluations - maybe the improvements in some domain is because of discount factor?
2. Claim of better features: As I understand, the main claim of the paper is that U2O learn better features. Feature rank collapse is a known problem with offline RL but there have been fixes provided for it in the past. Ex. DR3. It seems comparisons are not made to those modifications at all in this paper.
3. Generality of approach: Unsupervised RL encompasses a broad range of methods. Methods that are based on maximizing mutual information; methods that discover options; methods that capture a bag of skills and update it over time (eg. Voyager). This method relies on reusing policy and value functions to initialize and reward shaping; how will this method work for all the other unsupervised RL approaches. To be calling this a framework might be an overstatement as they consider very related unsupervised approaches based on a single bucket of successor features. 

4. Prior works have proposed using unsupervised to online objectives and can be attributed correctly: [1,2,3,4]. I believe the claiming of an entirely new framework is somewhat overclaimed.

### Questions
1. Can the explanation of O2O vs off-policy online RL can be made clear in the paper? Those are important baselines. It seems to be important to put the U2O algorithm in main paper as it wasnt clear that the old dataset was kept around.  It would help to be very clear the differences between U20, O2O and Off-policy online RL 
2. Why are results missing in Table 1?
3. In line 249, it might be helpful to have a citation for the reward regression technique with successor features reward.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a new offline-to-online (O2O) reinforcement learning (RL) method, where they replace the offline RL pre-training 
stage, with offline unsupervised RL pre-training.
The offline unsupervised RL pre-training consists of learning an offline policy conditioned on a latent skill vector, resembling a multi-task or goal-conditioned policy.
The paper proposed to name this problem setting as unsupervised-to-online RL (U2ORL).
They evaluate their method in nine tasks from five benchmarks.
They claim that their results suggest that their approach either matches or outperforms O2O RL methods.

### Strengths
Overall, I found the paper well-written and easy to follow.
The problem that the authors are working on -- pre-training in RL -- is important and definitely of interest to the community.

For the most part, I found the experiments insightful and thorough.
I particularly like the feature dot product analysis, this is a nice addition to the paper.

### Weaknesses
The biggest issue with this paper is that the abstract claims "we empirically demonstrate that U2O RL achieves strong performance that matches or 
even outperforms previous offline-to-online RL approaches ...".
However, Figure 12 suggests that O2O outperforms U2O when the offline data only contains expert data.
As such, this claim that U2O either outperforms or matches O2O is false. It is dependent on the type of offline data.
The authors clearly address this in the conclusion but as a reader, I am very disappointed getting to the 
end of the paper to find the claim in the abstract is false.
The authors need to update the abstract and correct this claim.

Further to this, I want to know how U2O compares to O2O in Kitchen when using the "complete" data set.
It seems like the authors have avoided including results when using expert data sets because their method 
performs worse than O2O RL methods in this setting.
These results are important and should be included.
I suggest the authors include results for the Kitchen task with the complete data set and include a discussion of how their method performs against O2O RL when using different types of offline data sets.

How I see it, this method requires a diverse data set that is collected by an unsupervised RL method.
This paper then proposes a new way to pre-train on this diverse data set.
That is a good contribution, but do not overclaim your contribution.
This could, for example, motivate collecting diverse data sets and the investigation of how to best incorporate expert data into this method.

Finally, this paper is fairly incremental as it simply combines existing methods. 
As such, I think it is important that the experiments are thorough so that we gain lots of insights about why we should care about this U2O method.
I think the authors are almost there as the results provide insights that I think are valuable to the community.

### Questions
- Do you agree that your method does not outperform O2O methods when using expert data sets?
- Why have you only included one experiment using exert data sets, put it in the appendix, and not explained the results in the main text?

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel concept termed unsupervised-to-online reinforcement learning (U2O), which replaces the conventional task-specific offline RL pretraining in the offline2online RL paradigm with task-agnostic unsupervised offline RL pretraining. The study reveals that unsupervised pretraining enables agents to adapt more quickly to downstream tasks compared to domain-specific offline RL pretraining. This advantage stems from the richer and more general-purpose representations fostered by unsupervised learning, which encode a broader range of task features and thus prevent feature collapse specific to any single task. The paper presents a practical and straightforward implementation of their U2O method. Empirical experiments conducted on state-based and image-based tasks, along with extensive ablations, demonstrate the effectiveness of leveraging unsupervised pretraining for general-purpose representation over traditional offline RL pretraining.

### Strengths
1. Replacing O2O with U2O is a reasonable and innovative approach.
2. The authors comprehensively discuss the advantages of U2O over O2O, supported by extensive empirical evidence.
3. Experimental results indicate that U2O outperforms O2O in terms of performance.
4. The paper is well-written, clearly highlighting the challenges and contributions.
5. The detailed explanations in the Experiments and Appendix effectively justify why U2O is superior to O2O.

### Weaknesses
1. One potential limitation is the skill identification process. In this paper, the authors determine the optimal skill $z*$ by minimizing the MSE loss w.r.t to the single-step reward using a small reward-labeled dataset. Ideally, a skill should encapsulate more long-horizon information and should not be solely defined by single-step rewards. More advanced skill identification process can be developed in the future.
2. The scope of this paper is relatively narrow. In my view, unsupervised pretraining can facilitate various types of fine-tuning, including offline RL fine-tuning, imitation learning, and others. Limiting the study to only online RL fine-tuning could be expanded for a more comprehensive evaluation.
3. I'm curious about the impact on online RL fine-tuning if offline RL pretraining incorporates regularizations like DR3 to prevent feature collapse. It seems the key advantage of U2O over O2O doesn't stem from this factor.
4.  I agree with other reviewers that the paper may overstate some claims.

### Questions
N/A

### Soundness
4

### Presentation
4

### Contribution
3
