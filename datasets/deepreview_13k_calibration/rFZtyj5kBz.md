# Certifiably Byzantine-Robust Federated Conformal Prediction

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Conformal prediction has shown impressive capacity in constructing statistically rigorous prediction sets for machine learning models with exchangeable data samples.
    The siloed datasets, coupled with the escalating privacy concerns related to local data sharing, have inspired recent innovations extending conformal prediction into federated environments with distributed data samples. However, this framework for distributed uncertainty quantification is susceptible to Byzantine failures. A minor subset of malicious clients can significantly compromise the practicality of coverage guarantees.
    To address this vulnerability, we introduce a novel framework \name, which executes robust federated conformal prediction, effectively countering malicious clients capable of reporting arbitrary statistics in the conformal calibration process. We theoretically provide the conformal coverage bound of \name in the Byzantine setting and show that the coverage of \name is asymptotically close to the desired coverage level. 
    We also propose a malicious client number estimator to tackle a more challenging setting where the number of malicious clients is unknown to the defender. We theoretically show the precision of the malicious client number estimator.
    Empirically, we demonstrate the robustness of \name against various portions of malicious clients under multiple Byzantine attacks on five standard benchmark and real-world healthcare datasets.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider the conformal prediction interval construction in the federated learning setting where (1) each client reports conformality scores, and (2) a subset of clients are malicious and can report distorted scores to mess up with the interval construction. To alleviate the influence of malicious clients, the authors (1) identify malicious clients by comparing the score distributions from different clients under the assumption that conformity scores for benign clients are sampled from the same underlying distribution (IID setting), or from, essentially, distributions with bounded distance (non IID setting); (2) construct conformal prediction interval using the estimated benign clients.

### Strengths
The paper is overall easy to follow; and robust prediction intervals against malicious clients are an important question.

### Weaknesses
It seems to be that the assumptions considered seem over-simplified and may lead to less robustness and under-coverage of difficulty cases when violated: the entire paper is based on the assumption that benign clients have similar conformity score distributions, in both IID settings (identical) and non-IID settings (close), and a client whose conformity score is far from its K_b "neighbors" is claimed malicious.  However, in practice, benign clients can have data with different local characteristics, due to, e.g., demographic differences, differences in medical practice guidelines, etc.

I am sorry but I feel this is a very dangerous assumption, and leads to increased prediction disparity when leaving out minority samples that are not intentional attack. What makes it really dangerous is that this decision is  based on prediction quality, as a result, there is no way that you can even assess which samples during test are belonging to the left-out minority populations.

### Questions
More details of the nonIID setting + different levels of being nonIID can be helpful.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an algorithm called Rob-FCP to perform Conformal Prediction in a federated learning setting where some agents are potentially malicious. This algorithm first discards the malicious agents and then performs a standard conformal prediction algorithm. Authors theoretically provide the conformal coverage bound of Rob-FCP in the Byzantine setting and show that the coverage of Rob-FCP is asymptotically close to the desired coverage level under mild conditions in both IID and non-IID settings. An algorithm for automatically determining the number of malicious agents is also provided. Finally, empirical experiments demonstrate that Rob-FCP is effective.

### Strengths
1\ This is a very interesting problem for the conformal prediction community.

2\ The paper treats both the iid setting and the non-iid setting.

3\ The paper is well-written, clear, and easy to follow.

4\ The experience shows that the method performs well in this federated learning setting with malicious agents.

### Weaknesses
1\ A major weakness is that to calculate the vector distance $d_{k_1, k_2}$ in step 8 of the algorithm ("Algorithm 1 Identifying the malicious client"), we need to send all the vectors $v^{(k)}$ to the server. It seems to me that this step is very problematic in a federated learning context, as it requires each client to transmit a vector summarizing their local score distributions to a central server, which could still leak information about the local data distributions, especially if the dimension of the histogram is high. This is a potential privacy concern, even if the vectors are lower dimensional than the raw scores.

2\ Another important weakness is that the bounds of Theorem 1 and Corollary 1 are in $1/(\min n_i)$. Therefore, if a non-malicious agent has only one data point, the bound does not improve, even if the other agents have an increasing number of data. This may just be due to an artifact of the proof or maybe we really can't do any better. This has to be proven (or at least discussed). The bound's dependence on the minimum sample size across clients is concerning, as it implies that the overall performance is bottlenecked by the client with the fewest data points, regardless of the total data available across all clients. This is a significant limitation in practical federated settings where data heterogeneity is common.

3\ Citations are not always appropriate. For instance, the split conformal prediction method is attributed to Lei et al., 2018 but the citation should be Papadopoulos et al., 2002.  The same applies to the FCP which does not cite the first paper due to Lu et al., 2021, and the more recent one Humbert et al., 2023, and to related work on federated learning, which only cites papers from 2019 and above.

4\ Although the experiences are well explained and in large quantities, I think that the parameters of the experiments are not always given (maybe I am wrong). For example, we do not know how malicious data are generated. The lack of clarity on how malicious data is generated makes it difficult to assess the robustness of the proposed method under different attack scenarios. It is crucial to understand the specific mechanisms used to simulate malicious behavior to fully evaluate the method's effectiveness.

Minor:
1\ "marginal prediction coverage: ..." the definition is with an "inclusion"
2\ Mixture coefficients in the definition of $Q_{\lambda}$ are missing.
3\ Problem in the definition of $N_m$.
4\ In the abstract and introduction, the federated learning framework is also justified by privacy concerns. In general, it is not true that federated learning guarantees privacy.

### Questions
1\ Is it possible to compute the vector distance $d_{k_1, k_2}$ with a federated algorithm ?

2\ The $\min{n_i}$ in the bound of Theorem 1 and Corollary 1 cannot be improved or is it just an artifact of the proof?

3\ In Theorem 1 and Corollary 1, $\varepsilon$ appears in the bound. Is it possible to control it? 

4\ In addition to the previous question, in the experiment how much time it takes to compute the quantile? (and for wich $\varepsilon$ ?)

5\ Regarding my remark on privacy, is it possible/easy to extend Rob-FCP in order to have differential privacy guarantees?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies federated conformal prediction (i.e. perform conformal prediction when the calibration dataset is distributed among multiple agents) where there may be Byzantine agents who may act maliciously. The paper shows how to detect such malicious behaviors by recording their deviation from the rest of the population; for each agent, they record the empirical histogram over H bins, calculate the average distance away from their closest neighbors where the distance is measured by the Lp distance between their H histogram bins, and mark agents with high distance away from their neighbors as malicious agents. 

They show that under a few assumptions (iid or non-iid + some other assumptions), their algorithm can identify malicious agents and provide a target coverage guarantee (Theorem 1 and Corollary 1). In the case the number of malicious agents is not known, they show a way to estimate such number via some approximation (approximating the multinomial with multivariate normal). 

Finally, they evaluate their algorithm on a few different datasets (Section 5).

### Strengths
-The idea to identify the malicious agents behavior via their deviation from the non-malicious agents in terms of the non-conformal score distribution seems novel.
-Their algorithm seem to perform quite well in their experiments.

### Weaknesses
 -The main reason why the algorithm in the paper works seems to be due to the homogeneity of the non-malicious agents. Even in the experiments, the clients are partitioned randomly and hence their distributions will be pretty similar. However, as discussed even in the intro of the paper, there can be many settings where there is quite a bit of heterogeneity among the agents not due to their Byzantine and malicious behaviors but the underlying distributions are just inherently different. In fact, this heterogeneity seemed to me the motivation to studying this problem — i.e. the bolded sentences in the second paragraph of the intro. But the paper seems to study cases when there isn’t much heterogeneity?

 -It’s not clear to me what is exactly meant by the non-iid setting. Is it just that the agents’s non-conformal scores don’t come from the same distribution? However, the assumption that the v^(k) values (the histogram values) aren’t too different across agents in the non-iid setting essentially gives you an iid setting, right? I’m a little confused on the difference so it would be helpful to compare exactly the iid setting and the non-iid setting (along with other assumptions made for each setting) and how exactly they are really different.


-In proving the main result (Theorem 1), the appearance of the inverse of the CDF of the standard normal distribution seems surprising as there was no normality assumption before; it would be good to cite a reference for what is referred to as “the binomial proportion confidence interval” or eqn (13) in the proof of Theorem 1. Also, can’t one just apply the DKW inequality (https://en.wikipedia.org/wiki/Dvoretzky%E2%80%93Kiefer%E2%80%93Wolfowitz_inequality) here? It should be sufficient to show concentration of the empirical CDF (which exactly characterizes the empirical histogram values v(k)_h) toward the true CDF (which also characterizes the true bar(v) values). This would avoid the need to union bound over H values too as DKW tells you that over all possible h values (i.e. hth cut point), the empirical and the true CDF value is close with high probability. 


 -How’s the final (1-alpha)-quantile being calculated after identifying the benign clients? Is it simply combining all the clients non-conformal scores altogether and then calculating the (1-alpha)-quantile? If that’s the case, I’m not understanding the federated nature of this problem except for the fact that some of the clients data are being ignored due to their apparent distributional difference to other clients?  How can one tell if this distributional difference of some clients is due to their malicious behavior or truly inherent distributional difference?

### Questions
-It’s not clear to me what is exactly meant by the non-iid setting. Is it just that the agents’s non-conformal scores don’t come from the same distribution? However, the assumption that the v^(k) values (the histogram values) aren’t too different across agents in the non-iid setting essentially gives you an iid setting, right? I’m a little confused on the difference so it would be helpful to compare exactly the iid setting and the non-iid setting (along with other assumptions made for each setting) and how exactly they are really different.


-In proving the main result (Theorem 1), the appearance of the inverse of the CDF of the standard normal distribution seems surprising as there was no normality assumption before; it would be good to cite a reference for what is referred to as “the binomial proportion confidence interval” or eqn (13) in the proof of Theorem 1. Also, can’t one just apply the DKW inequality (https://en.wikipedia.org/wiki/Dvoretzky%E2%80%93Kiefer%E2%80%93Wolfowitz_inequality) here? It should be sufficient to show concentration of the empirical CDF (which exactly characterizes the empirical histogram values v(k)_h) toward the true CDF (which also characterizes the true bar(v) values). This would avoid the need to union bound over H values too as DKW tells you that over all possible h values (i.e. hth cut point), the empirical and the true CDF value is close with high probability. 


 -How’s the final (1-alpha)-quantile being calculated after identifying the benign clients? Is it simply combining all the clients non-conformal scores altogether and then calculating the (1-alpha)-quantile? If that’s the case, I’m not understanding the federated nature of this problem except for the fact that some of the clients data are being ignored due to their apparent distributional difference to other clients?  How can one tell if this distributional difference of some clients is due to their malicious behavior or truly inherent distributional difference?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study a robust conformal prediction problem in a federated learning setting. Since local datasets share some privacy properties, some agents may not truthfully report their non-conformity score.  In this scenario, making a prediction interval based on this contaminated data would be harmful and lack the correct coverage probability. To solve such an issue, the authors propose a novel algorithm and obtain a coverage bound close to the desired level under both iid and non-iid settings.

### Strengths
1. The authors study a realistic setting where the agents may not be truthful in reporting their non-conformity score, and they developed an ``outlier detection" algorithm to ensure the prediction sets are made based on truthful agents.

2. Rigorous theoretical guarantees are provided on the coverage probability lower and upper bounds.

3. The methodology is applied to various types of datasets to measure its performance, which is great.

### Weaknesses
1. It seems the results are derived based on either knowing the number of truthful agents or being able to consistently estimate this quantity.  This could be a relatively strong assumption in reality.

2. The assumption on bounded distribution disparity could be relatively strong. There would be the cases where the underlying distributions of different group of agents are not the same. In that case, this assumption can be easily violated. Moreover, even if the agents report true non-conformity scores, if the underlying distributions are significantly different, the non-conformity scores themselves may not be comparable across agents, which would undermine the validity of the proposed approach.

### Questions
1. Could the authors establish some theoretical guarantees where the number of truthful agents is not correctly estimated? What will happen if they are underestimated or overestimated? 

2. Could the authors also provide some numerical results to illustrate the sensitivity if the number of truthful agents is not correctly identified?

3. Again, as I mentioned in the weakness part, if the distributions of underlying agents are no-i.i.d., it is very likely that assumption 3.1 will be violated, even if the agents report the true non-conformity score. It seems the current algorithm may not handle this point very well.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
