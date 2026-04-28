# Budget-constrained Active Learning to De-censor Survival Data

- Decision: Reject
- Avg Score: 2.00
- Scores: 1, 1, 3, 3

## Abstract
Standard supervised learners attempt to learn a model from a labeled dataset.  Given a small set of labeled instances, and a pool of unlabeled instances, a budgeted learner can use its given budget to pay to acquire the labels of some unlabeled instances, which it can then use to produce a model. Here, we explore budgeted learning in the context of  survival datasets, which include (right) censored instances, where we know only a lower bound c_i on that instance’s time-to-event t_i.  Here, that learner can pay to (partially) label a censored instance – eg, to acquire the actual time t_i for an instance [eg, go from (3yr, censor) to (7.2yr, uncensored)], or other variants [eg, learn about 1 more year, so go from (3yr, censor) to either (3.2yr, uncensored) or (4yr, censor)].  This serves as a model of real world data collection, where followup with censored patients does not always lead to complete uncensoring, and how much information is given to the learner model during data collection is a function of the budget and the nature of the data itself. Many fields, such as medicine, finance, and engineering contain survival datasets with a large number of censored instance, and also operate under budget constraints with respect to the learning process, thus making it important to be able to apply this budgeted learning approach. Despite this importance; to our knowledge no other work has looked into doing this. We provide both experimental and theoretical results for how to apply state-of-the-art budgeted learning algorithms to survival data and the respective limitations that exist in doing so. Our approach provides bounds and time complexity  theoretically equivalent to standard active learning methods. Moreover, empirical analysis on several survival tasks show that our model performs better than other potential approaches that might be considered on several benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
- Presented work focuses on the problem of Bayesian active learning with the learner trained on survival analysis data. 
- The number of query steps is constrained by the given budget. In particular: 
   - the underlying data are right censored with the underlying latent classifier which indicates whether the patient died during the observation period;
   - the censoring corresponds to a patient dropping out of study and so after a particular time period we lose the access to the information whether the patient survived, the censoring bound is known. 
   - the learner can query an unlabeled dataset and obtain partially labelled censored instances, where some time interval can be queried, e.g. data are censored up to 3 years and we query information about additional two more years about the patient.  This corresponds to following up with the patient after some period;     
   - the budget constraint indicates that different labels have associated different costs and information content. 

Authors propose a solution based on the Bayesian Active learning by Disagreement (BALD) applied to querying a batch of given size.  Authors provide a budgeted greedy algorithm and incorporate mutual information scores from the BALD-like estimate. To budget constrain problem, authors try to optimize the cost coverage over the batch. 

Authors use 3 real life survival datasets to demonstrate their proposed method.

### Strengths
- The selected problem is very relevant and interesting for real life data applications. The paper well states the problem and aspire to provide a solution.
- Authors propose three alternative methods to demonstrate the strength of their approach.

### Weaknesses
1) Paper contains multiple typos, see e.g line 210. 
2) Terms are not clearly defined, e.g. Algorithm 1, line 275, what is a_BB_surv ? 
4) The paper is not very clearly written, there is missing description of  the learner, there is missing debate on the distributional properties of the BALD model.  
5) The results in the main section seems cherry-picked, e.g. it would be good to include more points in the budget constraints rather than 0, 1, 5, 20.
6) It would be good to provide study on the synthetic dataset to demonstrate how the proposed methods perform in the controlled setting.

### Questions
1) Is there a typo on the lines 211 - 215? In particular, can authors elaborate in more detail why the second equality ( between lines 212-213) holds? 
2) What does authors mean by statement: “ by omitting the first two lines we can reduce the computational complexity …” (lines 252 - 253)
3) Can authors provide more insights into how the prior and likelihood within the BALD are selected? 
4) Can you clarify how the proposed “approach provides bounds and time complexity are asymptomatically equivalent to standard active learning methods”? (Lines 29-31).

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors consider the learning of survival model with budget constrained active learning. The formulation of the problem (Section 3) requires that the training dataset has the complete information of event times and censoring times, which is not a typical survival problem in which the survival times cannot be all observed for training data. The active learning is only applied to the case where the budget is used to extend the study (expend the observation period) in order to observed possible more events. This scenario is not the typical consideration in survival analysis in medical or health studies, though in reliability study in industry, in which type II or Type I right censoring are often used to collect data, it is possible to observe more events by increasing the study time.  In clinical trial random right censoring is mostly the observational scheme and  extending study time may not be able to "acquire" the information assumed in the article.

### Strengths
The use of active learning in survival analysis is an interesting idea.

### Weaknesses
The authors consider the learning of survival model with budget constrained active learning. The formulation of the problem (Section 3) requires that the training dataset has the complete information of event times and censoring times, which is not a typical survival problem in which the survival times cannot be all observed for training data. The active learning is only applied to the case where the budget is used to extend the study (expend the observation period) in order to observed possible more events. This scenario is not the typical consideration in survival analysis in medical or health studies, though in reliability study in industry, in which type II or Type I right censoring are often used to collect data, it is possible to observe more events by increasing the study time.  In clinical trial random right censoring is mostly the observational scheme and  extending study time may not be able to "acquire" the information assumed in the article.

 The use of de-censoring as the label in survival analysis does not have much practical usage. It could be used in "reliability" in industry, though. The written English is not clear. The use of words and punctuation like  "and" and "," make the sentences hard to understand. For example, see  lines 269 and 282.

 The requirement of true times as well as censoring times for all the subjects in the training data is very restrictive in survival analysis. You may argue that in active learning you just use "complete data" as the initial step, then the  observations are biased, and the model learned from the data does not reflect the true survival model, and thus any further results based on the model are problematic.

 It seems y denotes the true survival time, but the test data have {x_Bi, y_Bi}, but not ctime_Bi cevent_Bi. It is not clear which are known and which are unknown. The English is hard to understand, too. For example, the meaning of "the model sees only when the data points are uncensored" (line 140, page 3).

 Survival time is often a continuous random variable, in the defined model (or procedure) in line 160, the previous defined time y is assumed to take values from {1, ..., t}. It is not clear what the notations y and t stand for.

 The notation "I" has multiple meaning in the context. I-oracle (line 156),  unit of time (line 158, ctime_i +I), and mutual information (line 197). The other notations like the second term on the right hand side of line 200 with the one one the left side of line 207, what the w_j on the right hand of line 207 stands for, and why we have the summation of of j from 1 to k here. You may not discard or add terms arbitrarily to confuse the readers.

 The BatchBALD method was developed in Kirsch et al (2019) already. It is not clear the information entropy in line 212 is from Kirsch et al (2019) or proposed by the author. 

 For survival data, the authors  tried to obtain the probabilities p(y|x, w D_train) by assigning zero for those value y which below the censoring time c_b, then normalized the probabilities of those values larger then c_b (conditional on the survival time being larger than c_b). This is obvious from the conditional probability rule. From line 297, if the instance is censored at ctime_b, why p(y|x,w,D_train)=0 for all y greater than ctime_i+I. How is the interpretation of the formula in line 301?

### Questions
1. The requirement of true times as well as censoring times for all the subjects in the training data is very restrictive in survival analysis. You may argue that in active learning you just use "complete data" as the initial step, then the  observations are biased, and the model learned from the data does not reflect the true survival model, and thus any further results based on the model are problematic.

2. It seems y denotes the true survival time, but the test data have {x_Bi, y_Bi}, but not ctime_Bi cevent_Bi. It is not clear which are known and which are unknown. The English is hard to understand, too. For example, the meaning of "the model sees only when the data points are uncensored" (line 140, page 3).

3. Survival time is often a continuous random variable, in the defined model (or procedure) in line 160, the previous defined time y is assumed to take values from {1, ..., t}. It is not clear what the notations y and t stand for.

4. The notation "I" has multiple meaning in the context. I-oracle (line 156),  unit of time (line 158, ctime_i +I), and mutual information (line 197). The other notations like the second term on the right hand side of line 200 with the one one the left side of line 207, what the w_j on the right hand of line 207 stands for, and why we have the summation of of j from 1 to k here. You may not discard or add terms arbitrarily to confuse the readers.

5. The BatchBALD method was developed in Kirsch et al (2019) already. It is not clear the information entropy in line 212 is from Kirsch et al (2019) or proposed by the author. 

6. For survival data, the authors  tried to obtain the probabilities p(y|x, w D_train) by assigning zero for those value y which below the censoring time c_b, then normalized the probabilities of those values larger then c_b (conditional on the survival time being larger than c_b). This is obvious from the conditional probability rule. From line 297, if the instance is censored at ctime_b, why p(y|x,w,D_train)=0 for all y greater than ctime_i+I. How is the interpretation of the formula in line 301?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper focuses on a problem of great practical interest, when the dataset is partially labeled and the data is censored. It proposes a budgeted learning (a subfield of active learning) method in the context of survival analysis.
It's a niche subject, but the method is very new and original, I am convinced it can be used for practical purposes. 

I am not familiar with either active learning or survival analysis (so I'll put 2 on the confidence score).

### Strengths
- This paper is clear, domains are well introduced (whereas the paper is at the intersection of survival analysis and active learning)
- The results are convincing, and the authors have made the effort to compare themselves with “naive” methods (sanity checks part), even though there is no work dealing with this case.

### Weaknesses
 - I have some minor comments, it's more a question of presentation than content.

 - the assumptions are not sufficiently discussed by the authors. The PdWR reviewer also mentions that the real time requirement in the training data is very restrictive.
- previous work is not sufficiently discussed. In addition, the ViVr reviewer mentions that the algorithm is merely an adaptation of the algorithm by Khuller et al. (1999).
- the authors answer quite briefly to all the reviewers' comments, referring only to their new version of the paper. However, we do not yet have access to it.

### Questions
1. Assumptions: 
- for clarity, I think it would be better to present the assumptions in a formal manner: Assumption 1: (...), Assumption 2: (...)
- for the assumption  that censoring is independent of the features, it is common in survival analysis but can they the authors discuss this more in details what it implies in practice by taking an example ? 
2. The measure MAE-PO should be described in the main text. 
3. Line 388, the authors describe clearly how the real dataset is "censored". However, I think it's a pity that the authors don't discuss enough the realistic aspect of having the selected datasets censored (and partially labeled), perhaps a realistic situation for a dataset could be put forward. 

Minor comments: 
- line 139: **, where** L is the size of the training data.
- line 165: 3.1 INITIAL ASSUMPTIONS -> there is no 3.2 section, maybe the authors could use \paragraph instead of \subsection
- it may be personal but I don't like the notations $ctime_i$ and $cevent_i$, maybe the authors can use a shorter version like $c^t_i$ and $c^e_i$ (it is just a proposition)

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an active learning (AL) approach for survival analysis data, where the AL is constrained to a budget. The proposed approach is essentially an extension/adaptation of the BatchBALD algorithm (Kirsch et al., 2019) to account for survival data and a limited budget. The main motivation and application comes from the medical domain, where the proposed approach aims to identify which patients to follow up with to maximize the mutual information criterium of BatchBALD. The empirical results based on 3 real-world datasets in the medical domain show that the proposed approach can outperform standard BatchBALD, as well as 5 additional naive baselines.

### Strengths
1) The **problem addressed in this paper is relevant** and the existing research on the topic of AL for survival data is indeed limited. 
2) The proposed approach is **an original combination of existing ideas**, namely budgeted learning and BatchBALD for AL, with the latter being "tweaked" to work with survival data.

### Weaknesses
1) The **contributions are not very clear**. The authors should clearly state which contributions they are claiming. Is the extension of BatchBALD to a budget-constrained setting the central contribution? If so, why is the theoretical analysis included in the appendix rather than in the main text? Is the adaptation of BatchBALD to survival data the central contribution? Both? The narration is ambiguous with respect to this, thus unnecessarily increasing the difficulty of assessing novelty.
2) The **novelty is unfortunately low**. It is not clear how the proposed approach for accounting for the budget constraint is different from the existing approaches for budgeted learning from the literature. The adaptation of BatchBALD proposed for survival data is also very incremental and not adequately grounded. The authors also mention that "so far no method has been developed looking at
budgeted learning with survival data" - however, there are other works in the literature looking at applying BALD for right-censored data (see e.g., https://arxiv.org/pdf/2402.11973). How does the proposed approach relate to these works?  
3) There are **several concerns regarding the soundness** of the proposed approach. The extension of BatchBALD to a budget-constrained setting is not clearly described and is not adequately grounded. The proposed approach is an adaptation of the algorithm proposed in (Khuller et al., 1999) "by omitting the first two lines". However, it is not clear what lines the authors refer to and, most importantly, what are the theoretical grounds for doing so. Similarly, the adaptions of BatchBALD for survival data are essentially presented as "algorithmic tweaks" (e.g., setting probabilities to zero and renormalizing) without a proper theoretical justification. Lastly, it is not clear how the authors handle the fact that the queried instances can still be censored - are the censored times assumed to be known a priori before querying? If so, how limiting is that assumption in terms of the applicability of the proposed approach? 
4) The **limited application scope** of the proposed approach is also a topic of concern. Although I agree with the authors that AL for survival data is a topic worth investigating, and the literature is indeed lacking on this, the application scope is, in my opinion, broader than the medical domain application presented in the paper. This limits the target audience of the paper quite a lot. I would encourage the authors to consider revising their presentation to broaden the scope of application to other domains as well. For example, the authors mention applications in finance and engineering in the abstract - it would be interesting to discuss those as well. Lastly, the authors consider only approaches where time is discretized into bins (they use Multi-Task Logistic Regression as the underlying survival model), and the proposed adaptation of BatchBALD to handle survival data in Section 5 relies on this assumption, which can be quite limiting. This should be discussed in the paper. 
5) The presented **claims are not adequately supported by empirical evidence**. Looking at the results in Table 1, the improvements over standard BatchBALD are very marginal. However, the text claims that "BBsurv outperforms other algorithms when budget is equal to 20 across all 3 real world datasets", which does not seem to always be the case. In fact, even "Entropy" seems to perform quite comparably - did the authors perform a statistical significance test? Confusingly, the Table 1 caption states that "Budget = 10", which is inconsistent with the text. Moreover, the results in Table 1 seem to be inconsistent with Figures 1 and 2. If one considered a vertical line at Budget = 10 (or 20, whichever it is), shouldn't the values and relative order of the approaches be consistent with Table 1?
6) The **presentation can be significantly improved**. There are several typos, poorly constructed sentences, incorrect grammar usage, sentences that are too informal for scientific paper, etc. I strongly encourage the authors to carefully revise the writing and overall presentation of the paper. Other aspects of the presentation, such as mathematical derivations, can be significantly improved. For example, the authors should include numbers for the equations. Similarly, it is unclear how the authors transition from the eq. of the mutual information at the beginning of Section 4.1 to the computation of its right-most term 2 equations below. The right term is an expected entropy, while 2 equations below only the entropy is considered. Can you clarify?

### Questions
1) Can you please clearly list the main claimed contributions of the paper? 
2) There are other works in the literature looking at applying BALD for right-censored data (see e.g., https://arxiv.org/pdf/2402.11973). How does the proposed approach relate to these works?  
3) Please clarify the theoretical ground for "omitting the first two lines" of the algorithm of (Khuller et al., 1999) and for setting the probabilities to zero and renormalizing in the adaptation to BatchBALD to survival data? 
4) Are the censored times assumed to be known a priori before querying? If so, how limiting is that assumption in terms of the applicability of the proposed approach?
5) How can the proposed approach be generalized beyond discretized time bins? 
6) The results in Table 1 seem to be inconsistent with Figures 1 and 2. If one considered a vertical line at Budget = 10 (or 20, whichever it is), shouldn't the values and relative order of the approaches be consistent with Table 1?
7) It is unclear how the authors transition from the eq. of the mutual information at the beginning of Section 4.1 to the computation of its right-most term 2 equations below. The right term is an expected entropy, while 2 equations below only the entropy is considered. Can you clarify?

### Soundness
1

### Presentation
2

### Contribution
2
