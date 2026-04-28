# Adversarial Imitation Learning via Boosting

- Decision: Accept
- Avg Score: 5.75
- Scores: 6, 6, 6, 5

## Abstract
Adversarial imitation learning (AIL) has stood out as a dominant framework across various imitation learning (IL) applications, with Discriminator Actor Critic (\dac{}) \citep{kostrikov2018discriminatoractorcritic} demonstrating the effectiveness of off-policy learning algorithms in improving sample efficiency and scalability to higher-dimensional observations. Despite \dac's empirical success, the original AIL objective is on-policy and \dac's ad-hoc application of off-policy training does not guarantee successful imitation \citep{kostrikov2018discriminatoractorcritic, Kostrikov2020Imitation}. Follow-up work such as \vdice{} \citep{Kostrikov2020Imitation} tackles this issue by deriving a fully off-policy AIL objective. 
Instead in this work, we develop a novel  and principled AIL algorithm via the framework of \emph{boosting}. Like boosting, our new algorithm, \alg, maintains an ensemble of \emph{properly weighted} weak learners (i.e., policies) and trains a discriminator that witnesses the maximum discrepancy between the distributions of the ensemble and the expert policy. We maintain a weighted replay buffer to represent the state-action distribution induced by the ensemble, allowing us to train discriminators using the entire data collected so far. In the weighted replay buffer, the contribution of the data from older policies are properly discounted with the  weight computed based on the boosting framework.  
Empirically, we evaluate our algorithm on both controller state-based and pixel-based environments from the DeepMind Control Suite. \alg{} outperforms \dac{} on both types of environments, demonstrating the benefit of properly weighting replay buffer data for off-policy training. On state-based environments, \alg{} outperforms \vdice{} and \iq \citep{garg2021iq}, achieving competitive performance with as little as one expert trajectory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors proposed AILBoost that exploits gradient boosting algorithm with the variational form of reverse KL divergence. Similar to the sample-based discrepancy minimization in AdaGAN (Tolstikhin et al., 2017), AILBoost adapted weighted replay buffer, where each trajectory and its importance are stored together in the replay buffer, which is later used to minimize the discrepancy between the expert's state-action occupancy measure and the mixture of agent's state-action occupancy measures. The empirical studies with controller-state-based and pixed-based environments show that AILBoost outperforms ValueDICE (Kostrikov et al., 2020) and DAC, both of which are well-known baselines in the AIL literature.

### Strengths
- Using gradient boosting with weighted replay buffer and applying it to adversarial imitation learning is interesting. 
- Empirical results were evaluated with many metrics (IQM, Mean, Optimality GAP), which makes the results more reliable.
- Potential issues and limitations with the algorithm's scalability are discussed.
- Literature review on AIL is clearly done.

### Weaknesses
 - Presentation should be improved: Abstract and Introduction (especially, Abstract) include too many details about existing works, which will be mentioned in Related Works and Preliminaries. Making Abstract and Introduction more succinct seems needed. 
- The algorithm's complexity grows due to using all previous histories. However, this can be approximated by ignoring old samples, as mentioned by authors in Section 4. 
- Contributions are focused on empirical sides and not on the theoretical sides; I don't think this is a crucial weakness, though.
- There are two different forms of reverse KLD; (1) Donsker-Varadhan dual form from ValueDICE (2) Variational form from f-divergence GAIL. In AILBoost, the second form was used. It is not clear why the first form was not considered, especially given its connection to ValueDICE, a baseline in the paper.
- The idea of using weighted replay buffer and boosting seems applicable to general AIL frameworks, although authors applied this only to the variational form of reverse KLD. It would be beneficial to see if this idea can be applied to DAC, and if so, what the performance would be. This is important because the training procedure that combines DAC with boosting may be simpler than the one with rev KLD.
- In page 7, line 1, "we always warm start from $\pi_t$". ---> What does this mean? Also, Appendix A doesn't appear in the manuscript. 
- AILBoost's computational complexity increases as $t$ increases in Algorithm 1. A comparison of training times among DAC, ValueDICE and AILBoost is needed to understand the practical implications of this increased complexity.
- In Figure 1, "AILBoost outperforms DAC, ValueDICE, IQ-Learn, and BC across all metrics, amount of expert demonstrations, and tasks" ---> This is true from IQM perspective, but not true when 1 demonstration is considered with Mean and Optimality Gap. 
- Figure 2,3,4's file sizes seem to be too large, which I think end up the heavy file size (34MB) of pdf file and makes text loading slow. Can we make those figures' sizes smaller?

### Questions
- More succinct Abstract and Introduction are needed. I think they are quite dense in its current form. One example I could think is adding a small figure to describe AILBoost's contribution, but this is not a mandatory comment to follow.
- There are two different forms of reverse KLD; (1) Donsker-Varadhan dual form from ValueDICE (2) Variational form from f-divergence GAIL. In AILBoost, the second form was used. Do we have any reason for not using the first form?
- The idea of using weighted replay buffer and boosting seems applicable to general AIL frameworks, although authors applied this only to the variational form of reverse KLD. Can we apply this idea to DAC, and if possible, can we see the performance for those cases? One reason I'm asking is the training procedure that combines DAC with boosting may be simpler than the one with rev KLD.
- In page 7, line 1, "we always warm start from $\pi_t$". ---> What does this mean? Also, Appendix A doesn't appear in the manuscript. 
- AILBoost's computational complexity increases as $t$ increases in Algorithm 1. Can you please compare training times among DAC, ValueDICE and AILBoost?
- In Figure 1, "AILBoost outperforms DAC, ValueDICE, IQ-Learn, and BC across all metrics, amount of expert demonstrations, and tasks" ---> This is true from IQM perspective, but not true when 1 demonstration is considered with Mean and Optimality Gap. 
- Figure 2,3,4's file sizes seem to be too large, which I think end up the heavy file size (34MB) of pdf file and makes text loading slow. Can we make those figures' sizes smaller?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a novel adversarial imitation learning algorithm, AILBoost, which follows the framework of boosting. On the policy side, AILBoost maintains a weighted ensemble of policies and performs gradient boosting in the domain of state-action occupancy measures. On the discriminator side, AILBoost employs a weighted replay buffer combined with an expert dataset to train discriminators that maximize the discrepancy between the current mixed policy and the expert in an online manner. Empirically, AILBoost outperforms benchmarks in continuous control tasks across both controller state-based and pixel-based environments.

### Strengths
1.The author applies a mixed policy class which naturally connects with the buffer replay under the adversarial imitation learning framework, this is an interesting discovery.
2.By using a weighted mix of the learned policies, AILBoost performs gradient boosting, making the policy update smoother, which proves to be useful.

### Weaknesses
1.While thorough in its overall idea, this work lacks in-depth theoretical analysis. I suspect that noise during the policy rollout in each round might compound through the buffer replay, potentially disrupting the analysis of the discriminator. Specifically, the state-action pairs sampled from the environment during policy rollout at each boosting round are subject to sampling noise, and this noise could be amplified when these samples are used to train the discriminator in subsequent rounds. This could lead to a discriminator that learns spurious correlations, which would then negatively impact the policy learning process.

2.The "weak learner" presented in this study doesn't conform to the traditional definition of weak learnability, which could be misleading. Contrary to AdaBoost, if the learner's base policy class fails to match the performance of the expert, then even mixing them at the initial state won't achieve expert-level performance. This is because the boosting procedure relies on the assumption that each weak learner can provide some improvement over the previous ones, but if the base policy class is fundamentally incapable of achieving expert-level performance, then no amount of mixing will overcome this limitation. The paper does not adequately address this limitation, which is critical for the practical applicability of the proposed method.

### Questions
Questions:
1.Why using weighted mixing instead of using the DAgger[1] style average mixing?

2.Is the smooth loss condition in Section 4.1 hard to satisfy? Is the specific condition that $d^{\pi}$'s state action distribution covers the expert's state action distribution? Could you point out the exact theorem that makes this claim?

3.Can I get a definition for "off-policy"? I believe the proposed algorithm is still "on-policy" as it compares the current mixed policy state distribution to the expert's.

4.The noise during the policy rollout each round might compound via the buffer replay and disrupt the analysis on the discriminator's side. If this is the case and we need to gather new samples from the mixed policy every round, does this challenge the claim of being fully off-policy?

5. It would be interesting to see experiments where the learner is truly weaker than the expert, such that the expert is nonrealizable. Is weak learnability in imitation learning sufficient for near-expert performance?

6.In Algorithm 2, why do we calculate $\pi_{t+1}$ without the expert dataset? Is this practical? Any further justification?

7.Why in Algorithm 2, line 10, is the replay buffer given uniform weight for all samples? Any further justification?

8.Could you explain more about the meaning of 1000 policy updates per 100 discriminator updates in section 5.3?

9. As a follow up question from question 1, I believe the returned mixed policy is following the online reduction similar to DAgger[1], among DAgger style algorithms, MoBIL[2] is also using weighted policies, which may be worth mentioning.

Minor suggestions:

Please mention "10 trajectories" in the caption of Figure 3.
Please provide more description on the performance of behavior cloning in Figure 3.
Can you provide each task's plots corresponding to Figure 1 in the appendix? Also, all plots related to Figure 2 and Figure 3 would be appreciated.

[1]Ross S, Gordon G, Bagnell D. A reduction of imitation learning and structured prediction to no-regret online learning[C]//Proceedings of the fourteenth international conference on artificial intelligence and statistics. JMLR Workshop and Conference Proceedings, 2011: 627-635.
[2] Cheng C A, Yan X, Theodorou E, et al. Accelerating imitation learning with predictive models[C]//The 22nd International Conference on Artificial Intelligence and Statistics. PMLR, 2019: 3187-3196.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel algorithm called AILBoost for adversarial imitation learning (AIL) in the framework of boosting. AIL has been successful in various imitation learning applications, but existing methods have limitations in terms of off-policy training and sample efficiency. AILBoost addresses these limitations by maintaining an ensemble of weak learners (policies) and training a discriminator to maximize the discrepancy between the ensemble and the expert policy. A weighted replay buffer is used to represent the state-action distribution induced by the ensemble, allowing for training using the entire collected data. The algorithm is evaluated on state-based and pixel-based environments from the DeepMind Control Suite and outperforms existing methods in terms of sample efficiency and performance. The paper also discusses the benefits of boosting in AIL and the robustness of AILBoost across different training schedules.

### Strengths
Strengths of the Paper:

1. The paper introduces a novel algorithm, AILBoost, for adversarial imitation learning that leverages the framework of boosting. This approach is unique and different from existing methods in the field. The use of boosting in the context of AIL is a creative combination of ideas that brings new insights and potential benefits.

2. The paper provides a thorough and well-structured description of the AILBoost algorithm, including the theoretical foundations, algorithmic details, and empirical evaluation. The authors present a clear motivation for their approach and provide a comprehensive analysis of its performance compared to existing methods. The empirical evaluation is conducted on a benchmark suite of environments, and the results demonstrate the effectiveness and superiority of AILBoost.

3. The paper is well-written and easy to follow. The authors provide clear explanations of the concepts, algorithms, and experimental setup. The organization of the paper is logical, with sections dedicated to preliminaries, algorithm description, and experimental results. The use of figures and tables further enhances the clarity of the presentation.

4. The paper addresses important limitations in existing adversarial imitation learning methods, particularly in terms of off-policy training and sample efficiency. By introducing AILBoost, the authors provide a principled and effective solution that improves the performance and scalability of AIL algorithms. The empirical results demonstrate the significance of AILBoost, as it consistently outperforms existing methods across different environments and tasks.

### Weaknesses
Weaknesses of the Paper:

1. While the paper compares AILBoost with existing off-policy AIL algorithms such as DAC, ValueDICE, and IQ-Learn, it would be beneficial to include a comparison with more state-of-the-art IL methods as well. Specifically, comparisons against methods that achieve strong performance in high-dimensional state spaces or with limited expert data would be valuable. This would provide a more comprehensive evaluation and demonstrate how AILBoost performs relative to the best-performing IL algorithms in the field, particularly those that may employ different techniques such as behavior cloning with advanced regularization or other forms of imitation learning beyond adversarial approaches.

2. The paper lacks a detailed theoretical analysis of the AILBoost algorithm. While the authors provide some intuition and connections to boosting algorithms, a more rigorous theoretical analysis would strengthen the paper's claims. Specifically, providing formal proofs or guarantees of convergence, optimality, or sample complexity would enhance the theoretical foundation of AILBoost. For example, it would be beneficial to analyze the conditions under which the ensemble of weak learners converges to the expert policy, or to provide bounds on the approximation error of the learned policy.

3. The paper briefly mentions the hyperparameters used in the experiments but does not provide a thorough discussion on their selection or sensitivity analysis. It would be valuable to explore the impact of different hyperparameter choices on the performance of AILBoost and provide insights into the robustness and generalizability of the algorithm. For instance, the learning rates for the discriminator and policy, the number of weak learners, and the weighting scheme for the replay buffer could all have a significant impact on performance. A detailed analysis of how these parameters interact and affect the final result is needed.

4. The paper does not include ablation studies to analyze the individual components or design choices of AILBoost. By systematically removing or modifying specific components of the algorithm and evaluating their impact on performance, the authors could gain a deeper understanding of the contributions of each component and provide insights into their importance. For example, an ablation study could investigate the effect of using a fixed weighting scheme versus an adaptive one for the weak learners, or the impact of warm-starting the weak learners with the previous models.

5. The paper briefly mentions that AILBoost may have increased memory cost due to maintaining weak learners. However, a more comprehensive discussion on the limitations of AILBoost, such as computational complexity, scalability to larger environments, or potential failure modes, would provide a more balanced perspective on the algorithm's practical applicability. Specifically, a discussion of the computational cost of training multiple weak learners and the potential for increased training time would be valuable.

### Questions
1. Could you provide more insights into the computational complexity of AILBoost? Specifically, how does the algorithm scale with the number of weak learners, the size of the replay buffer, and the dimensionality of the state and action spaces? This information would be valuable for understanding the practical feasibility of AILBoost in larger and more complex environments.

2. In Section 4, you mention that AILBoost maintains a weighted replay buffer to represent the state-action distribution induced by the ensemble. Could you provide more details on how the weights are computed and updated in the replay buffer? Additionally, how does the size of the replay buffer affect the performance of AILBoost? It would be helpful to understand the trade-off between memory usage and performance.

3. The paper mentions that AILBoost achieves competitive performance with as little as one expert trajectory. Could you provide more insights into the limitations and trade-offs of using a small number of expert demonstrations? How does the performance of AILBoost change as the number of expert trajectories increases? It would be interesting to see if there is a threshold or diminishing returns in terms of performance improvement with more expert demonstrations.

4. In the experimental evaluation, you compare AILBoost with existing off-policy AIL algorithms. Could you provide more insights into the reasons behind the superior performance of AILBoost compared to these baselines? What are the key factors or design choices in AILBoost that contribute to its improved performance? This information would help in understanding the specific advantages of AILBoost over existing methods.

5. The paper briefly mentions the limitations of AILBoost, such as increased memory cost. Could you elaborate on other potential limitations or failure modes of the algorithm? Are there any specific scenarios or environments where AILBoost may not perform well? Providing a more comprehensive discussion on the limitations of AILBoost would help in understanding its practical applicability and potential areas for future improvement.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a AIL method so-called AILBoost with policy boosting. In each round, the policy is ensembled considering the weakness of current policy. The ensemble training coefficient selection is simple with $\alpha (1-\alpha)$. It indicates that ensembling the policy is just to cover the small difference between expert and agent rollouts. Experiments show that AILBoost outperforms ValueDICE and DAC in state based and image based environments with small performance gains.

### Strengths
The method is easy to follow. Experiments are well conducted. The performance of AILBoost is convincing.

### Weaknesses
I do think this paper has some inspirations for AIL community, especially the experiment results are convincing.

I have a question about how the policies are ensembled? Is there a random number to choose which weak learner to perform? (this way keeps the multi-modalities for sampling) Or the policies are added with the outputs? Or any other ensemble methods? I am confused about this. However, ensembling the outputs of different policies may be wrong?

I do think it is a good idea to ensemble the weak learner for adversarial imitation learning. If the authors could resolve my confusion, I would like to raise my score.

### Questions
I have a question about how the policies are ensembled? Is there a random number to choose which weak learner to perform? (this way keeps the multi-modalities for sampling) Or the policies are added with the outputs? Or any other ensemble methods? I am confused about this. However, ensembling the outputs of different policies may be wrong?

I do think it is a good idea to ensemble the weak learner for adversarial imitation learning. If the authors could resolve my confusion, I would like to raise my score.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
