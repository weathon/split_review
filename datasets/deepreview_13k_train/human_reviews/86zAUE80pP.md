# CPPO: Continual Learning for Reinforcement Learning with Human Feedback

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
The approach of Reinforcement Learning from Human Feedback (RLHF) is widely used for enhancing pre-trained Language Models (LM), enabling them to better align with human preferences. Existing RLHF-based LMs however require complete retraining whenever new queries or feedback are introduced, as human preferences may differ across different domains or topics. LM retraining is often impracticable in most real-world scenarios, due to the substantial time and computational costs involved, as well as data privacy concerns. To address this limitation, we propose Continual Proximal Policy Optimization (CPPO), a novel method that is able to continually align LM with dynamic human preferences. Specifically, CPPO adopts a weighting strategy to decide which samples should be utilized for enhancing policy learning and which should be used for solidifying past experiences. This seeks a good trade-off between policy learning and knowledge retention. Our experimental results show that CPPO outperforms strong Continuous learning (CL) baselines when it comes to consistently aligning with human preferences. Furthermore, compared to PPO, CPPO offers more efficient and stable learning in non-continual scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies the problem of continual learning from humans, where the signal from humans takes the form of a preference. The main challenge of continual learning is retaining past knowledge, while still able to maximize reward on the newly acquired preferences. To stabilize the training procedure, this work proposes "stable learning", favoring actions that are both a) high probability under the existing model -- i.e. retaining past knowledge and b) high reward for the new preferences acquired -- i.e. conforming to the new preferences.

These two aspects are turned into "knobs" \alpha and \beta, which are used to weigh parts of the objective function to either increase the effects of learning new knowledge or retaining old knowledge. The values of \alpha and \beta are adjusted by collecting roll-out samples and classifying them into 5 categories, normal, high performing, ... noise. Where each category has an influence on the adjustments on these two knobs.

Empirical results are promising.

### Strengths
## originality : fair
The paper proposes a straight-forward (but nonetheless novel) idea to use samples in the continual learning process to modify the learning rates, whereby adjusting the rate in which the model retains old knowledge and learns new knowledge. 

## Clarity : good 
The approach is clearly explained.

### Weaknesses
## Quality : less than ideal.
It is unclear if the proposed method is actually better than the baselines from table 8, as there is no confidence intervals being computed, nor is there statistical tests being performed. Depending on the results, the authors might have to conduct additional human evaluations, so that the confidence intervals "pulls apart". 

Table 8 is the only evaluation that is conducted directly against humans, it is the only "non-proxy" evaluation of the proposed method -- directly asking humans to rate the responses -- rather than evaluating it indirectly through a reward model.

As such, the authors should look to conduct evaluations more in the form of direct human ratings, to give readers who are not too familiar with the details of RLHF (such as myself) confidence that the approach works well "end to end", when evaluated directly against humans.

## Significance : unclear
As someone not directly in the RLHF community, I leave this to other seasoned reviewers.

### Questions
please provide confidence intervals and t-tests for table 8. It would be good to show the proposed method is significantly better than PPO.

### Soundness
2 fair

### Presentation
3 good

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
This paper looks at a more ambitious form of RLHF that does not require complete retraining from scratch when new feedback is introduced as a result of human preferences that may vary over time across domains and topics. The authors propose to modify the PPO algorithm leveraged within RLHF training by designing an algorithm to accomplish 4 key desiderata: 

1. Examples with high reward and high generation probability have a high policy learning weight and high knowledge retention weight. 
2. Examples with high reward and low generation probability or high generation probability and low reward have a high policy learning weight and low knowledge retention weight. 
3. Examples with low reward and low generation probability have a low policy learning weight and low knowledge retention weight. 
4. All other examples are learned with default weightings. 

The authors then conduct experiments comparing their proposed method favorably during continual RLHF training to generic PPO as well as relevant baselines and ablations.

### Strengths
- I like the central motivation of this paper as I believe it is an important setting that has been under-explored to date in the context of RLHF. 
- The experimental results seem pretty good, suggesting that there may at least be some strong insights coming out of this paper about the impact of extreme examples of the efficacy of continual training. 
- Focusing on different treatment of extreme examples is a bit outside the norm within the continual learning context that is generally focused on either experience replay or knowledge retention strategies coming from different motivations. This gives the paper a certain degree of originality, but I feel it also makes justification of the particular approach more important, which is an area where I find the paper to be lacking. 
- There are a number of useful charts and tables throughout the text that help readers get the main idea when they may get confused.

### Weaknesses
 - The continual RL problem solved by this paper is never really formulated. Equation 4 is proposed as an objective, but it is never made clear what problem it solves. This makes it feel a bit arbitrary to me. For example, see recent work proposing formal definitions of the problem [1], [2]. 
- In general I find section 3 prior to section 3.2.1 to be very hard to follow. A number of things are referred to as theoretically justified or derived, but as far as I can tell this is not true in any meaningful sense. I think I would be much more open to the positioning of the contribution if the authors just started with the desiderata of section 3.2.1 and explained the reason for each intuitively maybe with the aid of a little bit of math for each one (something that is currently lacking in my view). The paper could be better positioned in my view more as an exploration of the impact of these various intuitions and their impact on continual RLHF. This is because, in my mind, the current discourse does not really deliver on proposing this technique as a theoretically justified approach for RL. 
- Improvements in Table 6, Fig 5, and Table 8 seem to be there but it is not clear how significant these are or exactly why this would generalize across domains. I didn’t notice any analysis of statistical significance, which is odd because PPO (and most RL methods) are known to have high run to run variance in general, so it is very hard to take RL results seriously without this. 

Because I worry about statistical significance and generality of the results and don't believe the formulation is well justified as presented, I lean towards rejection at this time. 

[1] Khetarpal, Khimya, et al. "Towards continual reinforcement learning: A review and perspectives." Journal of Artificial Intelligence Research 75 (2022): 1401-1476.

[2] Kumar, Saurabh, et al. "Continual learning as computationally constrained reinforcement learning." arXiv preprint arXiv:2307.04345 (2023).

Detailed Comments on Equation 5:

A particular issue with the start of section 3 is with equation 5 and the discussion around it. What do you mean when you say “By introducing the actor-critic version, the clipped ratio, and the entropy bonus, we claim that Eq.(4) can be improved to (the derivation is detailed in Appendix Section B)”? What does "improved" mean in this context? Also going through Appendix Section B, it seems apparent to me that this is not a derivation of any particular theory/lemma/proposition or fact, rather it is just a series of steps that are not explained in the main text. For example, the authors mention improvement when they say: “In the PPO method, the objective is to maximize the expectation of the advantage function instead of the reward value. Hence, we improve the above objective as” -- here the "improvement" is either empirical or related to the theory about bias/variance. It is mentioned again when they say: “we introduce the knowledge retention penalty instead of the true KL divergence, we discuss the reason in lines 134-137 in our paper. Here, the above objective is improved as:”  -- here the improvement is based on the authors own empirical observations and computational justification. The authors also write "Then we introduce the importance sampling like PPO, the above objective can be written as" -- importance sampling is a deep theoretical topic related to off-policy optimization while having issues related to variance to implement in practice. I find the analysis of and flippant discussion of this component of the algorithm to be entirely inadequate in the appendix. It is also not even discussed in the main text.

### Questions
1. What is the statistical significance of the reported results across random seeds? 
2. What problem formulation is equation 4 a solution to? 
3. The key difference with generic RLHF seems to be that the optimization of the two terms is only over a subset of the data in equation 4. Why does it help us to essentially throw away data? Or is this motivated as part of a computational constraint from some implicitly considered problem formulation that is not spelled out? 
4. The hard cutoff based on hyperparameter k seems a bit weird to me. Towards what metric would the hyperparameter k be optimized for if it can't be equation 4 itself? This gets even weirder for me when the hard cutoff is then relaxed in equation 6. I don't get why it was ever introduced to begin with. 
5. Why does equation 6 make equation 5 easier to optimize? I buy that equation 6 is more general than equation 5, but this is the key motivation for this sense and it is really not clear to me why this would be the case. Especially considering that focusing on only a subset of the data would require less computation, which I presume is a major constraint of the implicit problem formulation.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new method, CPPO, to align language models with human preferences in the continual learning setting, exempting the need to do LM retraining. Based on PPO, CPPO introduces a new imitation loss term to imitate the old policy outputs, and a weighting strategy is applied to balance the policy gradient loss and the imitation loss. The weighting strategy can be implemented in a heuristic way or a learnable way through the Lagrange function. As a result, in the continual learning setting, the policy (Language model) can seek a good trade-off between new task performance and old knowledge retention. The experiments show that the method outperforms all baselines and is close to the ChatGPT in terms of several metrics such as reference preference model score.

### Strengths
1. The work aims to address a practical and important issue, language model alignment in a dynamic human preference setting. 
2. The paper is well-written. 
3. The main idea and the motivation behind it make sense.
4. The evaluation is thorough with reasonable metrics and adequate baselines.

### Weaknesses
I wonder about the performance of 1) $M_{\pi2}$ on the Task-1 test set and 2) $M_{\pi1}$ on the Task-2 test set. The result of the first experiment can show how much knowledge the model retains for the first task. In addition, the second experiment is supposed to show a mediocre result to prove the two tasks have a clear difference and that the experiment setting is indeed a continual learning setting. The performance gap of $M_{\pi1}$ and $M_{\pi2}$ on Task-2 can reveal to what extent the two data distributions mismatch.

### Questions
N/A

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem in the continual learning problem in the RLHF module of training language models. The authors propose continual PPO (CPPO), which utilizes a sample-wise weighting strategy based on the vanilla PPO algorithm to balance policy learning and knowledge retention. Experimental results show that CPPO has a good continual learning ability in the domain incremental learning summary task.

### Strengths
- This paper studies the important problem of reinforcement learning with human feedback (RLHF) in a continual manner due to the limitation of computational cost or data privacy, which may have a great impact to the LLM community.
- The paper is well written and easy to follow.
- CPPO outperforms multiple baselines in the proposed summarization benchmark.

### Weaknesses
 - The major contribution of this paper is to propose the problem of RLHF in a continual manner, however, the motivation and necessity of this problem is lack of detailed explanation and support, hindering readers’ understanding of its value. The authors should introduce more related work that retrain or finetune the LM when new data arrive. Furthermore, the storage and computational cost of different approaches should be analyzed, for example, the retraining methods [1], replay-based methods [2] and regularization-based methods [3].
- The experiment part is weak.
    - In the main experiment to evaluate the continual learning ability of CPPO in NLP tasks, only one benchmark Reddit TL;DR summarization is considered. What’s more, the length of the continual task stream is only 2, which is not enough for a solid evaluation of continual learning ability compared to related work [4][5][6][7].
    - The proposed CPPO method can also be applied to other continual reinforcement learning tasks other than RLHF. Simpler conventional control tasks like DoorGym [4][5] should be included to further validate the soundness of CPPO.
- The mathematical symbols and spellings need to be checked, for example,
    - $A_i$ in Eq.(3) was not mentioned before.
    - explanation of Eq.(4), k is a hyperparameter → $k$ is a hyperparameter.
    - In Eq.(6), coefficients should be $C_1, C_2$, not $r_1, r_2$.
    - Experiment settings: lkie → like.

### Questions
see weeknesses

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
