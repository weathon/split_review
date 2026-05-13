# Expressive Modeling is Insufficient for Offline RL: A Tractable Inference Perspective

- Decision: Reject
- Scores: 5, 6, 5, 8

## Abstract
A popular paradigm for offline Reinforcement Learning (RL) tasks is to first fit the offline trajectories to a sequence model, and then prompt the model for actions that lead to high expected return. While a common consensus is that more expressive sequence models imply better performance, this paper highlights that tractability, the ability to exactly and efficiently answer various probabilistic queries, plays an equally important role. Specifically, due to the fundamental stochasticity from the offline data-collection policies and the environment dynamics, highly non-trivial conditional/constrained generation is required to elicit rewarding actions. While it is still possible to approximate such queries, we observe that such crude estimates significantly undermine the benefits brought by expressive sequence models. To overcome this problem, this paper proposes Trifle (Tractable Inference for Offline RL), which leverages modern Tractable Probabilistic Models (TPMs) to bridge the gap between good sequence models and high expected returns at evaluation time. Empirically, Trifle achieves the most state-of-the-art scores in 9 Gym-MuJoCo benchmarks against strong baselines. Further, owing to its tractability, Trifle significantly outperforms prior approaches in stochastic environments and safe RL tasks (i.e. with state/action constraints) with minimum algorithmic modifications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers the problem of RL via sequence modeling, an offline RL paradigm given offline trajectories of the form (s, a, r, R) where R denotes the return-to-go. This is achieved by optimizing and sampling from p(a_{t: T} | s_t, E[V_t] >= v). 

The authors highlight that there are two main challenges in training such policies. (1) Estimation accuracy: Ability to estimate the expected return of a state and a corresponding action sequence. (2) Tractability issues: Ability to efficiently sample from this distribution. The authors claim that both of these issues are jointly responsible for poor test time performance of RvS based methods. 

While fixing the estimation accuracy part is already an active area of research, the authors focus on fixing the tractability part by using Tractable Probabilistic Models (TPMs) for sampling P(V_t >= v | s_t, a_t). The authors experimentally show that their method works well in practice and beats many other offline RL methods on various benchmarks.

### Strengths
1. Address the tractability issue in RvS which seems to have been overlooked in the past works. 
2. Incorporate TPMs into RL via sequence modeling. 
3. Extensive experimental evaluation.

### Weaknesses
1. Limited intuition on what the TPM is doing. I would have appreciated if the authors can incorporate a section on what TPMs are and what they are designed to do. While I do see some discussion in Appendix B.1. on Probabilistic Circuits, a colloquially accessible introduction to TPMs in the main body is highly appreciated.

2. Triffle does not seem to be significantly better than other RvS algorithms. The performance gains, while present, do not appear substantial enough to definitively claim superiority. This raises concerns about the practical impact of the proposed method, especially considering the added complexity of incorporating TPMs.

### Questions
1. While the authors show in Theorem 1 that when |A| = 2^K, solving the sampling issue given the Naive Bayes Distribution could be NP-hard, can you please discuss why for this setting, sampling using (2) is efficient even when given oracle access to P_{GPT} and P_{TPM}? Can the authors discuss why computing Z or sampling using 2 is efficient when |A| = 2^K?

2. It is not clear from Table 1 and Table 2 if Trifle is significantly better than other RvS approaches. Can you please discuss any concrete examples where Trifle significantly (with a reasonable margin) outperforms other RvS approaches?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use tractable probabilistic models (TPM) in reinforcement learning via supervised learning (RvS) approaches such that the computation of the multi-step value estimate can be done in a more tractable manner (in replacement of the potentially high-variance Monte-Carlo estimate needed in normal autoregressive generative models). The authors showed that through thorough empirical analysis that obtaining the multi-step value estimate accurately and act according to it is crucial in achieving good performance at the inference time, and previous approaches have failed to do so to some extent. In contrast, the use of TPM readily addresses such issue and consequently results in performance improvement on a range of offline reinforcement learning tasks tested (nine original D4RL locomotion tasks, a modified gym-taxi task, and three action-constrained safe RL locomotion tasks).

### Strengths
The paper is very well-written with clear presentation of the method and informative empirical results with comparison to relevant baseline methods. The analysis (Section 3) of the correlation between inference-time optimality score (how well an action is selected based on the model's estimate of the return) and the actual return achieved is convincing, and it motivates the proposed TPM-based solution well. 

To the best of my knowledge, this paper is the first that uses TPM in offline RL and the thorough empirical study (especially the analysis on the estimated returns vs. actual returns in Figure 1 and 2) brings insights on how useful TPM is in the context of RL/offline RL/RvS.

### Weaknesses
The main weakness of the paper is the lack of convincing evidence that the proposed algorithm Trifle can also bring significant performance benefits to offline RL tasks.
- The harder D4RL tasks are not evaluated (Section 6.1). The nine tasks evaluated are relatively saturated at the moment and it is hard to see much performance gain (as seen in Table 1) on top of existing approaches. It would be great if the authors could test the method on harder tasks such as antmaze tasks.
- The performance improvements on two of the three domains considered (two MuJoCo domains, in Sec 6.1 and Sec 6.3) are marginal. There does seem to be a descent performance gain on one of the custom task (on the gym-taxi environment presented in Sec 6.2) but it is not a standard task that people have evaluated on (which is fine, but a more comprehensive set of experiments would make a stronger case).

Other minor comments:
- I found Theorem 1 to be a bit out of place because showing a problem is NP-hard brings little information on how easy it is to approximate the solution, which is what people mostly care about in practice.
- I found the details of the action-space-constrained task (Sec 6.3) to be quite terse. How is the constraint being conditioned (is it a boolean variable or the threshold value discussed in the caption of Table 2?) How is it being incorporated into the TPM?

### Questions
N/A

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper looks at the "tractability" (ability to answer probabilistic queries) issue in offline RL and uses TPMs (Tractable Probabilistic Models) for solving complex RL tasks.

### Strengths
1. The paper is very well written. I especially enjoyed reading section 4.

2. The experiments are well-designed and the baselines are good as well (though do note the comments in the next two sections).

### Weaknesses
The points are in the spirit of making the paper stronger and in some cases, did not contribute to the score.

1. It will be useful to have some details about the Probabilistic Circuits in. the main paper while the bulk of the details can be in appendix (as is the case now).

2. The experiments used medium (or medium-expert) datasets. It will be useful to see the behavior with expert only and weak datasets.

3. It is not clear if the proposed approach outperforms "Bayesian Reprameterized RCRL" baseline. While I do not think it is important to beat all the baselines, it is useful to (i) understand how the two methods stack against each other (sharing standard deviation numbers for BR-RCRL will help) and (ii) the difference between the two approaches. The authors should add more details about why they think the two approaches are tied so closely.

4. The authors should consider adding results with another TPM (even if for a subset of tasks) so that it is clear that their approach works across different TPMs.

5. It is not clear why the authors used the TT baseline (in place of a stronger alternative) for experiments in 6.2 and 6.3

### Questions
Listing some questions (to make sure I better understand the paper) and potential areas of improvement. Looking forward to engaging with the authors on these questions and the points in the weakness section

1. Are terms like "training time optimality" introduced by this paper? If yes, could we consider using existing terms like "expressivity"?
2. The authors mentioned a sampling approach where "we first sample from a prior distribution p(a_t | s_t ), and then reject actions with low expected returns" (section 4.1). Did they use this in conjunction with any of the baselines (to make them stronger) ?
3. Was beam-search used in the baselines ?
4. In table 1, could the authors report the standard deviation for all the approaches.

### Soundness
3 good

### Presentation
3 good

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
The authors examine the problem of offline RL via RvS approaches, and note that one (underexamined) issue is tractability - answering flexible probabilistic queries faithfully. Due to the nature of the dataset generation and stochastic MDP structure, this is particularly difficult. The authors use TPMs for RvS to address this problem, showing that they are better at achieving the requested returns, and perform competitively, particularly with suboptimal data. Furthermore, they are better suited for constrained-action RL.

### Strengths
This is a very well-written and clear paper. The authors do a very good job of concisely going through the material (offline RL and tractability), and motivate their solution with theory and empirical evidence. There is an extensive experimental section with different environments, many baselines, and various examinations of the results.

### Weaknesses
The improvement in scores over baselines don't seem so large. In particular, with constrained actions one might expect the TPM approach to produce more gains. However, I don't see this as a particular demerit for insightful research.

### Questions
I do not have any questions.

**Edit:** I have read the other reviews and the authors' feedback, and see no reason to update my (very positive) original rating.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
