# Distribution-Free Fair Federated Learning with Small Samples

- Decision: Reject
- Avg Score: 5.80
- Scores: 6, 5, 5, 8, 5

## Abstract
As federated learning gains increasing importance in real-world applications due to its capacity for decentralized data training, addressing fairness concerns across demographic groups becomes critically important. However, most existing machine learning algorithms for ensuring fairness are designed for centralized data environments and generally require large-sample and distributional assumptions, underscoring the urgent need for fairness techniques adapted for decentralized and heterogeneous systems with finite-sample and distribution-free guarantees. To address this issue, this paper introduces FedFaiREE, a post-processing algorithm developed specifically for distribution-free fair learning in decentralized settings with small samples. Our approach accounts for unique challenges in decentralized environments, such as client heterogeneity, communication costs, and small sample sizes. We provide rigorous theoretical guarantees for both fairness and accuracy, and our experimental results further provide robust empirical validation for our proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents FedFaiREE, an extension of the FaiREE post-processing method for fair classification, and its formal guarantees to the federated learning settings, leveraging the Q-digest method. Akin to FaiREE, the proposed framework works with any score-based function and outputs the best threshold to correct fairness violations. The provided experimental results illustrate that the proposed method shows promising performance on two Adult and Compas datasets.

### Strengths
* Addressing group fairness in federated learning is a very important and currently popular problem. Most existing approaches are in-process methods and the proposed one is a post-process method that can be combined with other methods.

* The authors provided experiments with baselines with and without applying FedFaiREE and showed improvements in the final models' performance.

* The paper presents its ideas in a clear and easy-to-follow manner.

### Weaknesses
* I find the novelty and contributions of this work to be limited, given that the main objective, formal guarantees, and algorithm are very similar to [1]. Specifically, the adaptation of the centralized FaiREE method to the federated setting using quantile estimation appears to be a straightforward extension. Moreover, the algorithm operates under the assumption of full client participation, a condition that may not always align with reality in FL settings. It would be beneficial to explore scenarios with partial client participation and analyze the impact on the convergence and fairness guarantees.

*  The proposed problem and guarantees rely on the assumption of binary target and attribute/group variables, which is a restrictive assumption. This raises questions about the actual utility of this approach and what are its guarantees in more realistic scenarios (e.g., multiple sensitive groups and multiclass problems). While the authors acknowledge the need for extending the work to multiclass problems, they do not provide a detailed discussion or experimental results for such scenarios. I note that extending the work to multiclass problems is also identified by the authors, but there are existing works that address multiple attributes for these fairness metrics, e.g., [3].

* The paper misses discussion and comparison to other works proposing the same idea -- i.e., how to optimize a fairness metric and produce results akin to centralized ML using the local information from clients (e.g., [2] and [4]). Also, while the authors briefly mention [5], a more explicit discussion of these proposed method's conceptual differences would benefit the paper. For instance, how does the proposed method compare to [2] and [4] in terms of the definition of group fairness and the optimization techniques used? A thorough comparison would help highlight the unique advantages and limitations of the proposed method.

* The experimental section requires enhancements: (1) the paper performs experiments using only two datasets, which limits the generalizability of the findings. It would be beneficial to include more diverse datasets, such as those with multiple sensitive attributes or a larger number of clients. (2) important experimental details are missing, e.g., the number of clients used in the experiments, standard deviation for each result, Dirichlet distribution parameter values that were explored, what is the sensitive group for each dataset etc.), (3) the comparison to AFL which optimizes for client-fairness (i.e. a different fairness concept in FL) should be justified. It is unclear why AFL is chosen as a baseline, and how the results are compared given the different fairness objectives.

### Questions
**Major**
*  Can you please give more insights (than the ones at the beginning of section 3.2) on why and how the proposed method differs from [1]?
   
* How does this work compare with the related works [2],[3],[4],[5] mentioned above? Is the group fairness definition studied here different from [2] and [4]? Please also revise the related work. 

* How does FedFaiREE perform for different fairness constraint parameter $\alpha$, different levels of data heterogeneity across clients and confidence level $\beta$? My understanding is that only $\alpha=0.1$ for the adult dataset, $\alpha=0.15$ for compas, and $\beta=0.95$ for all experiments.

*  I'm interested in understanding how heterogeneity and imbalancedness are introduced across clients for these datasets, using the Dirichlet distribution. Why the parameter for adult was set to 1 and for compas was set to 10? Additionally, what is the standard deviation for each result reported in the tables (both supplementary and main)? This should be included in the results. 

* What's the number of clients studied per dataset? If the number is low you should empirically examine how this approach scales for a larger number of clients. To illustrate that, you can consider for example the  ACSIncome dataset, where the data are naturally noniid and partitioned into 50 states and Puerto Rico and treat each place as a client (i.e., 51 clients). 


 **Minor:** 

* It would be good for the authors to acknowledge the concerns regarding the COMPAS dataset within the fairness community. 

* The margins around Figure 1 around the figure require editing. The main text touches on the figure's description.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a fairness Post-hoc approach that estimates a decision threshold for a classifier scoring function per sensitive attribute in a federated setting. This is done by computing a quantile estimate of the score function in a distributed manner such that the decision of the classifier achieves the best error subject to satisfying a confidence upper bound on the desired level of fairness. Note that the classifier needs to have access to the sensitive attribute at inference time since the learned decision threshold depends on it.

### Strengths
The idea seems promising, well grounded theoretically and the experiments show good performance for the proposed solution.

### Weaknesses
I find the presentation a bit hard to follow and should be simplified. I think the paper is hard to follow in terms of notation and procedure. The clients step is clear and the overall goal of having one threshold per sensitive attribute based on the desired fairness level seems reasonable. Even though this means that the sensitive attribute needs to be accessible at inference time.
However, update on the server and related notation is hard to follow. For instance it seems that K (Eq.4) is obtained based on the desired probability of not satisfying the fairness tolerance (|DEOO|> \alpha in Prop 3.2). Then the final pair k_0,k_1 are chosen to minimize the misclassification error (Eq 5) from the set of K. However, it is not clear to me how do you derive a single threshold for the scoring function from k_0,k_1 which seem to be two vectors of size S.

### Questions
Is the minimization of Eq. 5 done in a greedy manner? Do you evaluate all of the possibilities in K?

What is the global rank of a rank (i.e., last line in Step 2 Section 3.1 )

How does your method connect with Hardt et al 2016 which is a centralized post-processing fairness technique that also relies on finding a threshold per sensitive group to satisfy a fairness criteria.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a distribution-free post-processing approach to impose (approximate) equality of opportunity on a binary classifier with binary sensitive labels. The classifier is built as a sensitive-label-dependent threshold over a sensitive-label-dependent scoring function. This calibration procedure has finite sample guarantees.

### Strengths
The calibration procedure is distribution free and has finite sample guarantees. As a post-processing approach, it produces a simple pair of thresholds. To alleviate the communication costs of computing the quantile distribution across all clients, an efficient distributed quantile algorithm (Q-digest) is used.

### Weaknesses
Though conceptually simple, I found the presentation and the notation to be exceedingly hard to follow. I am also unsure on why, exactly, is there a need to maintain per-client score rankings other than to update the per-client sketches prior to aggregation. The paper lacks clarity on how the per-client score sorting contributes to the overall fairness calibration, and it's not immediately obvious why maintaining these rankings is necessary beyond the Q-digest computation. Specifically, the connection between the local ranks and the global fairness constraints is not well-explained. The paper would benefit from a more detailed explanation of how these local rankings are used to enforce the desired equality of opportunity, and why this approach is superior to simply using the scores directly.

Since the distributed quantile learning algorithm is not a contribution of this paper, and the notation is hard to follow, it is hard to evaluate the contribution and the insight of this work. The lack of clarity in the notation makes it difficult to assess the novelty and significance of the proposed method. The paper relies on a pre-existing distributed quantile algorithm, and the core contribution seems to be in the application of this algorithm to the fairness problem. However, the presentation does not clearly articulate the specific challenges addressed by this application or the insights gained from it. Without a clear understanding of the technical details and the rationale behind the approach, it is hard to determine the value of the work.

### Questions
what exactly is the use of the per-client score sorting?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a versatile post-processing method that can be used together with other pre-processing and in-processing techniques to ensure fairness in federated learning. The method is distribution-free and only requires small samples and communication costs. Under a binary label prediction task, the authors derived theoretical guarantees for both model fairness and performance under Equality of Opportunity, after which was further extended to a distribution shift setting and an extended Equalized Odds fairness notion. Empirical experiments on Adults and Compas datasets were also carried out to demonstrate the superior performance and fairness of the proposed FedFaiREE method when compared to other baselines.

### Strengths
1. The paper is clearly written and has strong motivation paragraphs with well-categorized related works.
2. The authors further study estimation and approximation methods for better adoption in practice.
3. The theoretical results and analyses are sound. The guarantees derived are further extended to a setting with test distribution shifts and also a stronger extended notion of fairness.
4. The method proposed is versatile since it can be used in combination with other pre-processing and in-processing techniques to ensure better fairness.

### Weaknesses
1. The setting of the paper may be restrictive since it only applies to tabular data with binary prediction labels. Nevertheless, simpler settings might be needed for the ease of analysis.
2. The empirical validation of the method and performance is not comprehensive enough.

Some other details are given below in the Questions section.

### Questions
1. Help me understand the theoretical results: How tight is the bound that is derived in (7)? If the optimal classifier is indeed unfair, how can you still achieve an optimal misclassification error with the DEOO constraint?
2. How difficult is the extension to multiple labels? The current empirical validation section still appears not as convincing due to the simplistic setting and well-behaved binary label prediction datasets used. A larger-scale setting also supports the necessity of federated learning.
3. Why is the same $\alpha$ used for all experiments on a dataset (i.e., 0.1 for Adult and 0.15 for Compas)? How should this alpha be set in practice?
4. What is the trend of accuracy (ACC) when we shrink $\alpha$? What is a good point to stop (for $\alpha$) in order to balance accuracy and fairness? What is the lowest value of $\alpha$ we can go?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel algorithm called FedFaiREE, designed to tackle fairness concerns in federated learning. Existing fairness algorithms primarily cater to centralized data environments, relying on large samples and distributional assumptions. This paper addresses the pressing need for fairness techniques tailored to decentralized systems with finite samples and distribution-free guarantees. FedFaiREE is specifically developed for distribution-free fair learning in decentralized settings with small samples. The algorithm considers the unique challenges posed by decentralized environments, including client heterogeneity, communication costs, and small sample sizes commonly encountered in practical scenarios. The paper offers rigorous theoretical guarantees for both fairness and accuracy, and the experimental results provide strong empirical validation of these theoretical claims.

### Strengths
The strengths of FedFaiREE are as follows:

1. **Effective Fairness in Challenging Conditions:** FedFaiREE offers a simple yet highly effective approach for ensuring fairness in scenarios with limited samples and distribution-free conditions. This is particularly important in real-world applications where such conditions are prevalent.

2. **Theoretical Fairness Guarantees:** The paper provides theoretical guarantees that FedFaiREE can achieve nearly optimal fairness when the input prediction function is appropriate. This adds a level of confidence in the algorithm's ability to deliver on its fairness objectives.

### Weaknesses
My primary concern regarding this paper centers on its contribution when compared with previous work, particularly the FaiREE algorithm designed for centralized learning. Based on my interpretation, the overall process appears quite similar, with the primary distinction being the distributed aggregation process. I would greatly value it if the authors could delve deeper into the algorithmic variances and the technical challenges associated with the algorithm's design and theoretical analysis. This deeper exploration would enhance the paper's clarity and help readers better understand the specific advancements and innovations brought about by FedFaiREE in relation to its predecessor, FaiREE.

### Questions
see above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
