# Competitive Fair Scheduling with Predictions

- Decision: Accept
- Avg Score: 6.80
- Scores: 8, 6, 8, 6, 6

## Abstract
Beyond the worst-case analysis of algorithms, the recent learning-augmented framework considers that an algorithm can leverage possibly imperfect predictions about the unknown variables to make decisions to have guarantees tied to the prediction quality. We consider online non-clairvoyant scheduling to minimize the max-stretch under the learning-augmented framework, where the scheduler has access to job size predictions. We present a family of algorithms: *Relaxed-Greedy (RG)* with an $O(\eta^3 \cdot \sqrt{P})$ competitive ratio, where $\eta$ denotes the prediction error for job sizes and $P$ is the maximum job size ratio; *Adaptive Relaxed-Greedy* with an $O(\lambda^{0.5} \cdot \eta^{2.5} \cdot \sqrt{P})$ competitive ratio, where $\lambda$ denotes the prediction error for the minimum job size; *Predictive Relaxed-Greedy* with an $O(\lambda^{0.5} \cdot \varphi^{0.5} \cdot \eta \cdot \max \\{ \eta, \varphi \\} \cdot \sqrt{P})$ competitive ratio, where $\varphi$ denotes the prediction error for the maximum job size. We also present *${RG}^x$*, an algorithm that represents a trade-off between consistency and smoothness, with an $O(\eta^{2+2x} \cdot P^{1-x})$ competitive ratio. We introduce a general method using resource augmentation to bound robustness, resulting in *RR*-augmented *RG*, which achieves a $(1 + \epsilon)$-speed $O(\min \\{ \eta^3 \sqrt{P}, \frac{n}{\epsilon} \\})$ competitive ratio. Finally, we conduct simulations on synthetic and real-world datasets to evaluate the practical performance of these algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper uses the consistency-robustness framework to study the problem of learning-augmented job scheduling in multiple settings. The results are provided under multiple settings as functions of different notions of prediction errors, trade-offs between consistency-robustness, and resource augmentation settings. The paper then evaluates the performance of the proposed algorithms using both synthetic and multiple real data traces.

### Strengths
-- This is a very well-written paper with a comprehensive set of results both on the theoretical side and experiments. 

-- The theoretical results sound solid and consider multiple settings that are common to consider in the analysis of such problems. 

-- The experiments are great additions to the paper, especially since the author reports results for both synthetic and real traces.

### Weaknesses
 -- Overall, this paper presents a good set of results. However, the authors do not provide insights on the additional challenges with respect to closely relevant prior work and how their techniques and algorithms differ from existing results. The current version of the introduction only states the problem, introduces the notions and preliminaries, and states the technical contributions. There is a big missing part on the challenges to achieve such results and, in doing so, what type of techniques are required. 

-- Generally, the paper does not provide predictions based on lower bounds and notes on the Pareto-optimality of the provided consistency-robustness tradeoff.

### Questions
The answer to both comments on weaknesses will be great.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies an online scheduling problem where the objective is the notion of max-stretch, which is designed to balance fairness over jobs. Here, the stretch of a job is defined as the ratio of its response time and the job size, and the "max-stretch" is the maximum stretch of jobs. There exist some previous works on both offline and online versions of the scheduling problem, but they assume exact knowledge of job sizes. This paper considers the setting where job sizes are not precisely given while some predictions about the values are available. The paper studies several types of prediction models, for which nearly tight algorithms are developed.

### Strengths
- The paper provides a comprehensive study of the max-stretch scheduling, not only considering the problem with predictions but also the offline and online problem with exact job sizes (Section 3). 
- This paper considers several settings of different prediction models, concerning job sizes, the maximum job size, and the minimum job size. For all these settings, efficient algorithms are developed with a rigorous theoretical analysis. 
- Trade-offs between consistency and smoothness are also analyzed, and how to improve robustness via resource augmentation is addressed.
- Numerical results with real-world datasets are given.

### Weaknesses
While the paper gives a comprehensive analysis of the online scheduling problem with predictions, the concept of scheduling with predictions is not entirely new. As very briefly summarized in the related work section, various works exist for online scheduling with predictions. One may argue that this paper extends the literature to the max-stretch scheduling. However, the specific novelty beyond applying prediction-based techniques to a different objective function (max-stretch) is not clearly articulated. The paper lacks a detailed comparison with existing prediction-based scheduling algorithms, making it difficult to assess the true advancement of the proposed methods. It is unclear if the developed algorithms and analysis techniques are fundamentally novel or simply adaptations of existing approaches to the max-stretch objective. The analysis of different prediction models, while comprehensive, does not sufficiently highlight why these specific models are chosen and how they relate to real-world scenarios. Furthermore, the practical implications of the consistency-smoothness trade-off could be explored in more detail, providing a more concrete understanding of the benefits and limitations of the proposed algorithms.

### Questions
What is the novel component of this work compared to the previous works on online scheduling with predictions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors consider the problem of preemptively scheduling jobs on a single machine to minimize the maximum stretch, where the stretch of a job is the response time of the job normalized by its processing time. The jobs arrive online and the processing times are unknown and are only revealed once a job is completed, i.e., jobs need to be processed non-clairvoyantly.

Since the problem admits strong adversarial lower bounds, the authors consider learning-augmented algorithms that initially have access to predictions on the minimum and maximum processing time over the jobs and, for each arriving job, receive a prediction of the jobs processing time upon arrival.  

The authors give algorithms that achieve a consistency (competitive ratio for accurate predictions) that matches the best-known clairvoyant algorithm, and are smooth w.r.t. a prediction error. Furthermore, the authors show that well established standard techniques are not enough to achieve the best-possible robustness unless the algorithm has access to a faster machine (speed-augmentation).
Besides this, the authors also give a polynomial-time algorithm for the corresponding offline problem and empirical experiments for the presented algorithms.

### Strengths
# Strengths:

* The learning-augmented results given in the paper are quite complete and answer most of the questions that one could have (consistency, smoothness, discussion of the robustness). 
* The algorithmic ideas are presented in a nice way by iteratively removing more assumptions from Section 4.2 to 4.4.
* I like that the authors also resolve the complexity of the offline problem with Theorem 3.2. The idea to reduce the problem to deadline scheduling (minimizing the maximum lateness) by finding the “correct” deadlines via binary search over the set of line intersections is very elegant. 
* The fact that Preferential Round  Robin (Theorem 6.1) does not work is a nice separation from many existing results on learning-augmented algorithms for scheduling problems.
* The experiments seem well-done.

### Weaknesses
# Weaknesses:

*   The main part of the paper does not really highlight the techniques that are used to prove the theoretical results, apart from the discussion on the overestimation of job sizes at the beginning of Section 4.1. Since the algorithmic ideas are similar to the Algorithm by Bender et al. (2002), it would have been nice to highlight the differences and challenges in the proof that are caused by using predictions instead of precise processing times. The way it is written now, it is hard to estimate the technical contributions. For example, it's unclear how the dynamic adjustment of the threshold α impacts the analysis compared to a static threshold, and how the algorithm ensures that the classification of jobs (as 'big' or 'small') remains consistent throughout the scheduling process, given that α changes over time. Furthermore, the analysis does not clearly articulate the challenges in bounding the competitive ratio when using these dynamic classifications, making it hard to see the novelty of the approach.
*   The appendix could use one more iteration of proofreading. Some examples:
    *   The authors state on page 14 that EDF is optimal for minimizing the maximum lateness, but use it already on page 13.
    *   The phrasing of Theorem A.1 does not seem to quite match the statement that you actually show. For example: If you plug-in the processing time vector $(p_1^*,...,p_n^*)$ in Theorem A.1, then the theorem says that there exists a schedule with minimum max-stretch $\max_{1 \le j \le n} \frac{C_j-r_j}{p_j}$. However, this holds directly by definition of the problem. For this reason, Lemma A.3 does not seem to be implied by the statement of Theorem A.1, but by the proof of the theorem, which indeed implies the lemma.  Otherwise, the approach of the authors to prove the offline result makes sense.
    *   There are several repetitions already on the first two pages of the appendix.

*   Apart from the first point, the presentation in the main part is mostly fine with the following small exceptions:
    *   Lines 038-040: You state that job sizes are typically estimated using ML.  Do you mean in other theoretical learning-augmented results or in practice? If you mean the latter, it would be nice to have a reference for this. 
    *   Line 046: I think there are learning-augmented results on scheduling problems with additive errors. Maybe clarify that this refers to your error.
    *   Lines 094-096: I agree that the assumption of knowing the precise processing times may be unrealistic. However, it is a bit strange to use the adversary as an argument since having an adversary might not be a very practical assumption as well.
    *   Related work/offline scheduling: Would be nice to reference  some flow-time (response-time) results and briefly discuss the differences. (As your offline problem seems to be a special case of minimizing the maximum weighted response time, such a discussion seems relevant.)   
    *   Maybe mention a bit earlier that preemption is allowed.
 * Experiments: I am not sure if we learn something by comparing the speed-augmented RG+ to the other algorithms running at normal speed. It seems like an unfair comparison. Maybe it would be more interesting to also run RG+ on normal speed to empirically analyze the impact of Theorem 6.1 on real-world instances.

### Questions
# Questions:

1. More of a comment than a question: It is interesting to me that your algorithms nearly do not use the predicted processing times and essentially only use them for the classification whether a job is big or small. Maybe you can prove similar results (with different error measures) if the predictions are p_max, p_min and, for each job, a bit that predicts the job to be either small or big.
2. Theorem 6.1 shows that the blackbox combination of two algorithms will not benefit from the predictions. However, this does not exclude the possibility of a different technique to achieve an improved consistency and a robustness of O(n)? If it does not exclude that possibility, then calling Theorem 6.1 the “Necessity of Resource Augmentation” might be misleading.
3. Experiments: I assume that GWR gets access to the precise processing times? Any idea on why the competitive ratio does not increase with the prediction error in Figure 6?  
4. Just to make sure I understand since I was a bit confused reading it: Section 4.3 still assumes that $p_\min^e$ is given up-front but, in contrast to Section 4.2, it might be wrong even with respect to the predicted job sizes, i.e., $p_\min^e \not= \min_j p_j$ might hold. Is this right?

### Soundness
3

### Presentation
3

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
The authors consider the minimum max-stretch scheduling problem under the learning augmented framework. Jobs $J_j$ $1\leq j \leq n$ arrive sequentially. Job $J_j$ arrives at time $r_j$, has compute time $p_j^*$ and is released at time $C_j$. The goal is to minimize the max stretch, $\max_{j \in [n]} \frac{C_j-r_j}{p^*_j}$.

The authors present several algorithms:
- An offline algorithm achieving optimal max-stretch in poly-time, improving upon previous literature where a poly-time approximation algorithm was known.
- A family of relaxed-greedy algorithms to schedule online under different types of available predictions.
- An algorithm that explores the smoothness consistency trade-off
- An algorithm for the resource augmented setting

### Strengths
The results presented in the paper are quite nice and turn in an array of contributions. They address a relevant problem in scheduling under a currently popular and pertinent lense, algorithm with predictions.

The paper is not very well written but remains relatively easy to parse.

### Weaknesses
The paper lacks insights into the results and techniques. It is currently a list of theorems, and it takes some time to figure out how they are related to each other and what the actual contribution is. Listed below is a list of elements on which the paper could improve.

On offline scheduling:
- The first theorem (Thm 3.1) and the first paragraph contradict each other. The Thm says the algorithm is poly time in $n$, the paragraph says it is not. 
- Earliest deadline first is referenced without being defined (defined only in the appendix).
- The paragraph states that there are infinite candidates for the max-stretch. That is not a convincing argument: with $r_{max}$ the max release time, $U=\frac{r_{max}+\sum_j p_j}{\min_j p_j}$ is an upper bound on the max-stretch. Then there are $U/\epsilon$ candidates for $\epsilon$ approximations of the max stretch.
- The nice contribution of Thm 3.2 is Lemma A.1.: instead of doing a binary search over uniformly spread candidate max stretch, the authors find a list of candidates that contains the true max stretch. This entails that the proposed algorithm is optimal instead of approximately optimal. This is a nice contribution, but it takes reading the Appendix to figure it out.

On Relaxed-Greedy:
- Streamline the pseudo-code of relaxed greedy. In its current form, it does not help the reader. Maybe every subroutine does not need to be detailed. (e.g. JobRelease() takes 4 lines but is fairly useless)
- The main algorithmic idea is the reduction to two job-size, where the criteria for job length classification depends on $p_{min}$ and $p_{max}$. It would be helpful to get this insight earlier: it would help the reader understand the algorithm. It would also highlight why $p_{min}$ and $p_{max}$ play a special role.
- Thm 4.6 and 4.7: there is too many theorems in the paper, it is hard to tell what's important and what's not. Those two could easily become propositions.
- Definitions 4.8 and 4.9 are clutter: it is the same as the previous ones with $\alpha$ replaced with $\alpha_{r_j}$. If there is a difference I missed it should be highlighted, otherwise, I suggest dropping them. I am also not convinced by the use of vocabulary $r$-long.

On $RG^x$:
It should be said earlier in the text that FIFO is O(P) competitive and that $RG^x$ interpolates between FIFO and the proposed algorithms.


On notations:
- Maybe replace $p_j$ with $\hat{p}_j$ and $p^*_j$ with $p_j$

### Questions
Is the algorithm in Thm 3.1 poly time or not?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the scheduling problem of preemptively minimizing the maximum stretch on a single machine. It assumes that both job arrivals and processing times are uncertain.  This problem can be interpreted from the perspective of fairness, as an algorithm needs to give every job at least a k-fraction of the processor on average to achieve a max-stretch of at most k.

For this online problem strong lower bounds (n = number of jobs) on the competitive ratio exist, which is the worst-case ratio between an algorithm's max-stretch and an optimum's max-stretch. Thus, the authors apply the learning-augmented framework to this online problem. That is, they assume that predictions on the unknown processing times are given to an algorithm when a job arrives, and present bounds on the competitive ratio depending on the quality of these predictions. Here, the quality \eta is measured by the worst case ration between predicted and actual processing times. In the clairvoyant online setting, where an algorithm is oblivious to future job releases but jobs arrive with known processing times, a O(\sqrt(P)) competitive algorithm is known, which is asymptotically almost best-possible. Learning-augmented algorithms are a recently popular technique for beyond worst case analysis, and have become an established subfield in the intersection of algorithm theory and machine learning.

The main results of the present paper can be summarized as follows:
- An algorithm (RELAXED-GREEDY) that uses predictions on the processing times but assumes to know the maximum and minimum prediction at time 0 with a competitive ratio of at most O(\eta^3 \sqrt{P}). That is, if the prediction error is small, the algorithm achieve a performance close that of the best-known algorithm for the clairvoyant setting.
- Variants of the previous algorithms that do not need the assumption of knowing the maximum and minimum prediction value in advance, but instead receive a prediction on these values. The performance guarantees then depend also on the quality of the predictions on these aggregated values.
- A further variation of the previous algorithm in which the user can control the trade-off between the consistency bound (the bound assuming the predictions are correct) and the error-dependent bound using a hyperparameter.
- A general method to additionally achieve a robustness in O(n) using a processor that is (1+\eps) times faster than the optimum's machine (speed augmentation)
- An empirical evaluation of the proposed algorithms.

### Strengths
- The paper seems to be the first to consider max-stretch in the non-clairvoyant setting. The results are a nice package and a solid contribution to the area of learning-augmented algorithms. Thus, it generally also fits well to ICLR.
- The paper addresses the crucial assumptions of knowing the minimum and maximum processing time in advance, which was made by previous works. They show that relaxing these assumptions to prediction information only loses small factors in the competitive ratio.
- Empirical experiments indicate that their algorithms perform well on real-world data sets.

### Weaknesses
There are two questions that may influence the set of results, and thus, the overall contribution. Thus, I currently value them slightly negatively, but I am open to change this depending on the rebuttal.

Besides that, I think the main weakness is the presentation. I have the feeling that the abstract and the initial parts of the introduction are filled with too many technical details, and are not approachable for the broader ML community. In particular, I am missing a better introduction and highlighting of learning-augmented algorithms and a stronger motivation and connection to machine learning (as ICLR is an ML conference). I think a slightly more informal introduction could strongly increase the readability. 
Some other examples where I got confused:
- The paragraph on "prediction errors" also contains the definition of the prediction model, and moreover distinguishes between several different models, which are hard to grasp at this point in the writeup.
- Line 87: You mention "preferential round robin", but it is unclear what that is or in which reference one can find it.
- Line 89: In point 4 of the list of contributions, you only mention that you conduct experiments, but not outline any interesting findings.
- Line 94: Why is this assumption unrealistic? In practice?
- Line 397: "This shows the necessity of resource augmentation". This is a strong claim, and I am not sure if it is correct. Just because some technique does not work, this does not imply that one immediately needs strong assumptions such as speed augmentation.



### Questions
- In line 86 you claim that your algorithm achieves "optimal robustness of O(n) with (1+\eps)-speed", but I could not find a proof for this claim or a reference to related work. In particular, Theorem 3.5 only considers a lower bound regarding a unit speed processor. It is not obvious to me why this should still hold under speed augmentation, specifically because for other objectives such as total flow time, speed augmentation suffices to achieve a constant competitive ratio [Kalyanasundaram and Pruhs 2000]. I think this is an important question to address, because if a constant competitive ratio is possible under speed augmentation, in my opinion, the result of Theorem 6.4 is way less interesting.
- Line 418-423: It is unclear in the main part why monotonicity is important. I figured out that it is used in Line 1637 for the proof of Theorem J.6. I do not understand why this property is even necessary for the proof. The proof of Theorem J.6 is not very detailed, so it is hard to understand why monotonicity is important. I think it is not necessary to obtain this result: You run your main algorithm on the speed-1 machine and RR on the speed-\eps machine, but both work on copies of the actual instance. Whenever one of the algorithms finishes a job which is still running in the other algorithm, the actual job can complete in the actual schedule. However, we can still make the other algorithm continue working on the job because it works on its independent copy, and the actual processing time is known now. Thus, the overall bound is still the minimum of the two bound of the algorithms, and no algorithm gets "distracted" by a completion of a job in the other algorithm.


Additional remarks:
- The idea of a distortion prediction error has first been considered by Azar, Leonardi and Touitou (STOC 21). I would at least add this reference when the error is defined in line 48.
- Line 60: I think the definition of smoothness and robustness is equivalent. I think smoothness should be explained differently.
- Personally, I think that stating bounds in the related work section is not helpful. The considered problems are very different and the variables are not explained. Instead, I would prefer to have more references to related work on algorithms (scheduling) with predictions.
- If you keep the results on the offline problem, I would at least mention in the results section. Otherwise, this comes quite unexpected in the paper, and it is not clear (in the beginning of section 3) what the benefit of this result in the context of the results mentioned earlier is.
- Line 207: the maximum is not defined properly

### Soundness
3

### Presentation
2

### Contribution
3
