# Debiased Machine Learning and Network Cohesion for Doubly-Robust Differential Reward Models in Contextual Bandits

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
A common approach to learning mobile health (mHealth) intervention policies is linear Thompson sampling. Two desirable features of an mHealth policy are (1) pooling information across individuals and time and (2) modeling the differential reward linear model with a time-varying baseline reward. Previous approaches focused on pooling information across individuals but not time, thereby failing to capture trends in treatment effects over time. In addition, these approaches did not explicitly model the baseline reward, which limited the ability to precisely estimate the parameters in the differential reward model. In this paper, we propose a novel Thompson sampling algorithm, termed "DML-TS-NNR" that leverages (1) nearest-neighbors to efficiently pool information on the differential reward function across users $\textit{and}$ time and (2) the Double Machine Learning (DML) framework to explicitly model baseline rewards and stay agnostic to the supervised learning algorithms used. By explicitly modeling baseline rewards, we obtain smaller confidence sets for the differential reward parameters.  We offer theoretical guarantees on the pseudo-regret, which are supported by empirical results. Importantly, the DML-TS-NNR algorithm demonstrates robustness to potential misspecifications in the baseline reward model.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies Thompson sampling in contextual bandit models applied for mHealth intervention applications. In existing works, the approaches focus on pooling information across individuals but not across time. Furthermore, in existing works, the baseline reward model is not modeled, limiting the ability to estimate the parameters in the differential reward model. 

Towards overcoming these limitations, the paper proposes a new algorithm (called DML-TS-NNR) that achieves both of the above considerations. It considers nearest neighbors to allow pooling information across both, individual users and time. The algorithm also leverages the Double Machine Learning (DML) framework to model baseline rewards. This algorithm enables achieving improved statistical precision and can learn contextually-tailored mHealth intervention policies better. 

Finally, the paper presents a theoretical analysis and provides regret guarantees. The paper also presents experimental studies on simulation datasets; experimental results show that the proposed approach displays robustness to potential misspecifications in the baseline reward model.

### Strengths
– Paper is well written; key contexts and essential background is well established. 

– Related work: Discussion of related work is well organized and seems to  adequately cover background literature. Relevant papers also seem to be adequate cited elsewhere in the paper wherever useful. 

– I think one of the main strengths is that the paper is theoretically grounded. The paper presents useful theoretical results on regret analysis of the algorithm proposed and clearly states the assumptions involved.

### Weaknesses
– Experiments:

1. While the heatmap establishes statistical significance (Fig 2, right), the actual difference (or lift/improvement provided) in Fig 2(left) seems marginal. It's difficult to assess the practical significance of the observed differences in cumulative reward, especially given the log transformation applied to the step count data. The magnitude of improvement, while statistically significant, appears small, raising questions about the real-world impact of the proposed method.

2. The empirical results in the main paper are from simulation studies. The paper also claims that it performs analysis on a real-world IHS dataset but that is deferred to the appendix. The lack of a detailed presentation of the real-world IHS dataset results in the main paper limits the ability to fully evaluate the practical applicability of the proposed method. The focus on simulation studies, while useful for controlled experiments, does not fully address the complexities of real-world mHealth interventions.

3. Minor comment: Are error bars available for Fig 1? (Or are they so small that the bars are negligible given that it was run for 50 trials?) The absence of error bars in Figure 1 makes it difficult to assess the variability of the results and the robustness of the observed differences between the methods. Without error bars, it is challenging to determine if the observed differences are consistent across different runs or if they are due to random fluctuations.

### Questions
– The experiments section discussed three variants of the proposed method. Empirical results show two of these turn out to be best-performing (sec 5.1). So why is the third method relevant? And how do we decide which of the method is the best? 

–  The simulation results In Fig 1 seem to suggest a sharp difference in cumulative regret of the methods tested. However, on the Valentine study (Fig 2), the differences between the cumulative rewards seem rather small and not as dramatic as Fig 1 results. Why is there such a difference?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied the problem of learning mobile health (mHealth) intervention policies. The paper proposed a new Thompson sampling
based algorithm, named “DML-TS-NNR”, which achieves two desirable features: (1) pool information across individuals and time (2)  model the differential reward linear model with a time-varying baseline reward. Theoretical guarantees on the pseudo-regret are provided, and are supported by empirical evaluations.

### Strengths
- The paper studied a significant and practical problem motivated by mHealth applications, and overall the model, proposed algorithm and its analysis were presented with a good clarity.
-  The proposed DML-TS-NNR algorithm achieves reduced confidence set sizes and provides an improved high probability regret bound.
- The algorithm design takes the motivating application into account: the individuals’ enrollment occurs in a staggered manner, which mimics the recruitment process in mHealth studies. 
- Empirical experiments support the theoretical result and show that the proposed algorithm outperforms other baselines.

### Weaknesses
 - This paper is not presented in the correct ICLR latex template format 
- Section presents the basic model, however the connection between the model and the particular mHealth application was missing, especially how the model and its assumption fit into the application was not elaborated clearly.
- It was unclear the major innovation of the proposed algorithm in comparison to related prior works, e.g. (Yang et al., 2020; Tomkins et al., 2021).

### Questions
- Can the algorithm be extended when the network structure is not fully known?

### Soundness
3 good

### Presentation
2 fair

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
This paper presents a double/debiased machine learning (DML)-based nonlinear contextual bandit algorithm that takes into account network cohesion.

### Strengths
1. This paper thoroughly reviewed previous literature. 
2. The simulation study has been thoroughly conducted, which enhances the empirical power of the proposed method and makes it more plausible.

### Weaknesses
Overall, this paper is overly biased towards theoretical aspects. I understand “what” problems authors have solved, but I cannot understand “why” the authors have solved the problem. 

1. The storyline for the Introduction is somewhat drastic. Without any examples of the contextual bandit on mHealth, it's difficult to understand what sets mHealth apart and makes it special.
2. The motivation is quite weak in this paper. I understand that this paper relaxes many assumptions made in previous literature. However, there is a lack of discussion regarding the practical benefits of relaxing these assumptions and addressing complex problems. It is important to explain the significance of relaxing the assumptions/challenges (1,2,3,4) mentioned in the first paragraph and provide examples of how each of the four challenges mentioned in the Introduction hampers the practicality of mHealth. Without such examples, it is difficult to persuade readers why "DML-TS-NNR" is necessary.
3. Please cite Chernozhukov et al., (2018) when mentioning DML.
4. In the related work section, the paper does not mention the Bandit literature that takes into account network cohesion. I’d like to see the comparison between this paper versus the Bandit literature taking account of the network interference. 
5. I believe that the related work section does not include any papers on DML (or doubly robust) contextual bandits. Please correct me if I am mistaken.
6. The math wall of this paper is huge. The notations are heavy, but no verbal explanation is provided. For example, in Theorem 1, I can't pull the implication of this regret bound. Is it good or bad?

### Questions
1. This paper is written in a way that highlights how the proposed method is best suited for mHealth. What is the reason for this?
2. To my knowledge, the paper doesn’t assume the iid. However, the DML theory with sample splitting is developed based on the iid assumption. So, there must be more explanation of how this iid-based method can be used to address the problems in non-iid settings. Also, is the method provided by Chen et al., (2022) applicable to the non-iid setting?
3. This paper used a DML-based method. Then, how can I read the fast-convergence properties or doubly robustness of the algorithm in Theorem 1?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies mobile health intervention policies. Specifically, the setting that has the following four features, 1) the time-varying nature of feedback (captured by the hidden parameter theta^*_t) 2) the Non-linear relationship between action and outcomes (captured by conditional model for the observed reward in eq(1)) 3) Intervention efficacy changing over time and 4) similar features lead to similar outcomes (captured through the user graph). To tackle this they introduce a novel reward model in eq(1) that mimics a linear differential equation with a potentially non-linear component g_t(s) (which they consider as the baseline reward). Finally, to capture the idea that users showing similar symptoms require similar intervention they introduce the user graph. The assumption is that connected users share similar underlying vectors \theta_i implying that the rewards received from one user can provide insights into the behavior of other connected users. They also introduce a time connection graph G_t (the use of which is not fully clear to me). Finally, they propose an algorithm that has access to these graphs and proceeds in stages. In each stage k, it puts the data into partitions and uses an MAB algorithm (TS here) to select actions from these partitions, uses a least square estimate to the function f_hat(m), observes the reward, and updates the model. This approach balances exploration and exploitation simultaneously. They theoretically analyze their algorithm with a regret upper bound and conduct empirical evaluations.

### Strengths
1) The setting seems novel and relevant. However, the reward model needs more justification. See questions
2) The proposed algorithm is theoretically analyzed with a regret upper bound.
3) They conduct experiments to justify their algorithm.

### Weaknesses
1) The paper presentation can be improved. Some of the notations are never introduced. For example \delta in eq (1) is never introduced. In section 3.2 I think you should clearly state this as an assumption that connected users in graph share similar \theta_i. Furthermore, the role of the time-connection graph $G_t$ is unclear and requires more explanation.
2) The model requires more justification. The reward model in equation (1) is presented without sufficient motivation. The baseline reward $g_t(s)$ is introduced abruptly, and its significance is not well-explained. The connection to existing literature, such as conservative bandits, is not explored, which could provide a better understanding of the model's assumptions and limitations.
3) The technical novelty seems not that significant. While the combination of ideas is interesting, the individual components (MAB, least squares, user graph) are well-established. The paper needs to better highlight the specific technical challenges and innovations in their approach.
4) Needs more experiments to justify the setting. The experiments should include more diverse scenarios and comparisons to existing methods. The current experiments do not fully demonstrate the advantages of the proposed approach, especially in terms of the specific benefits of the user graph and the time-varying feedback.

### Questions
1) How is the graph G_time used? You suddenly introduce it in section 4 while discussing the algorithm. Do you construct a similar Laplacian matrix L and calculate tr(\Theta^\top L \Theta)?
2) Why is Thompson sampling here and not any other MAB algorithm? From the pseudocode, or even from the regret proof overview (I did not check the appendix) it did not seem to me that TS is giving any benefit. Can you elaborate on this?
3) Regarding the feedback model, the baseline reward $g_t(s)$ is suddenly introduced. What is it and why is it significant? Also, a follow-up is similar to conservative bandits studied in the literature, where the reward must not go down below the baseline reward. Is that work somehow connected to your setting?
4) I was slightly confused with the regret definition. First, is the observed set \O_k is just the history in stage k? Secondly, why are you averaging over each of the stages k? The usual definition of regret will be summing over all stages of $k\in [K]$?
5) Regarding the algorithm design I have a few questions. Observe that at the beginning of every stage k, you randomly assign the points to a partition in m. It might happen that in the first partition itself, you end up with a sequence of highly non-informative samples. Then when you use your MAB algorithm (TS here) to select an action you might end up with a very bad estimation of f_hat(m). How do you guard against this possibility? Also in the same line, how do you ensure sufficient diversity while allocating the points to partition? Do you have any underlying assumptions on this? 
6) It is not clear how the regret bound is analyzed. What is the key technical challenge in the analysis of your regret bound and how it differs from Abeille & Lazaric (2017)? Also, how does the harmonic number show up? It seems the regret bound scales as $\sqrt{K}$ which matches the standard linear bandit scaling of $\sqrt{T}$. However, where does the dimension d show up?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
