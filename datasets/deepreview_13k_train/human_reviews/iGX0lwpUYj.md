# When to retrain a machine learning model

- Decision: Reject
- Scores: 6, 3, 5, 6

## Abstract
A significant challenge in maintaining real-world machine learning models is responding to the continuous and unpredictable evolution of data. Most practitioners are faced with the difficult question: when should I retrain or update my machine learning model? This seemingly straightforward problem is particularly challenging for three reasons: 1) decisions must be made based on very limited information - we usually have access to only a few examples, 2) the nature, extent, and impact of the distribution shift are unknown, and 3) it involves specifying a cost ratio between retraining and poor performance, which can be hard to characterize. Existing works address certain aspects of this problem, but none offer a comprehensive solution. Distribution shift detection falls short as it cannot account for the cost trade-off; the scarcity of the data, paired with its unusual structure, makes it a poor fit for existing offline reinforcement learning methods, and the online learning formulation overlooks key practical considerations.
To address this, we present a principled formulation of the retraining problem and propose an uncertainty-based method that makes decisions by continually forecasting the evolution of model performance evaluated with a bounded metric. Our experiments, addressing classification tasks, show that the method consistently outperforms existing baselines on 7 datasets. We thoroughly assess its robustness to varying cost trade-off values and mis-specified cost trade-offs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the problem of retraining a machine learning model in practical settings. In specific, this paper considers another dimension when making decisions – the retrain cost. To make decisions in an online setting, the proposed method learns a performance predictor to predict future model performance given some data shift features. Then the retraining decision will be made based on the future performance estimation and the retrain cost. Experiments on five public classification datasets demonstrate the effectiveness of the method.

### Strengths
- The paper clearly explains the targeting objective function and the proposed method.
- The studied problem seems new when the new retraining cost dimension is in the constraints.
- The writing is clear and easy to follow.

### Weaknesses
There seems to be some unstated assumptions/explanations.
- The proposed method comprises at least two modules, one performance predictor and one decision module. The paper doesn’t discuss or analyze 1) how the predictor’s performance affects the final results, and 2) what the performance requirement of the predictor is.

The related work needs more discussion.
- The paper claims the retraining cost is a new dimension and sets a hyperparameter to control the retraining rate. However, previous methods like change point detection methods often also have a hyperparameter that controls the sensitivity of detecting distribution shifts, which is similar to the effect of the alpha parameter used in the paper. The authors may need to compare their alpha parameter to the sensitivity parameters in change point detection methods, e.g., Adams and MacKay 2007 [1] and Li et al 2021 [2], conceptually or practically.

Besides,
- How does the method demonstrate the claim “have access to only a few examples”? Could you quantify what you mean by "a few examples" and to provide experimental results showing performance with varying amounts of data?
- The paper focus on completely retraining. Could you explain why your method framework refrains from adaptation? Detect-and-adapt sounds reasonable to me as well. Even more, adaptation is more data efficient. So could you discuss the tradeoffs between your approach and adaptation methods, maybe in the aspects of the computational costs or data efficiency.

### Questions
Here are some minor comments:
- Shouldn't the cost of the offline training phase also be incorporated? Maybe a discussion on how incorporating offline training might affect the method's performance is helpful.
- Does the performance predictor suffer from distribution shifts and therefore affect the method's performance?
- Please justify the range of the tested alpha values in the robustness study (fig 3), which only have a range of 0.1. A broader range is more helpful to evaluate the robustness of the method.

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
The paper addresses the challenge when to retrain ML models in real-world settings with distribution shifts. To this end they introduce an uncertainty-aware approach for performance estimation and continuously forecast model performance.

### Strengths
Performance estimation under distribution shift and the the effect of model retraining is an important task and the authors introduce an interesting uncertainty-aware PE approach and draw connections to RL.

### Weaknesses
Unfortunately the evaluation of the proposed approach is very limited and the author missed connections to several relevant research streams that have been working on this (or closely related tasks). Therefore closely related baselines are missing and dedicated datasets that were introduced for this task are not used for evaluation. 

More specifically, the authors do not discuss the clear connection to the active testing literature and to the whole field of label-free performance estimation. A meaningful presentation of the approach would require an in-depth discussion of the related work from these fields and, importantly, a thorough benchmarking especially to PE methods like [1-3]. Owing to the connection to active risk estimation (and active learning) it would also be interesting to evaluate which data-points exactly need to be labelled for re-training. 

As for datasets, the WILD-time benchmark [4] was designed for the very task the authors address and the proposed method should be evaluated on the datsasets curated in this paper. 

In addition, I find the evaluation lacks important details, eg how often is re-trained with the different baselines for a given cost (and what is accuracy).

### Questions
See above

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
Authors consider the problem how deciding when to retrain machine learning model based on the relative importance of accuracy and retraining effort.  The work only considers classification tasks. The proposed solution is based on uncertainty of the future states, and it continuously forecast the model performance to make decisions on whether to retrain or not. The trade-off between accuracy loss and retraining cost is modeled through a hyperparameter \alpha, which allows us to consider different scenarios, e.g., when we are considering LLM (huge retraining cost) or very simple ML models (low retraining cost). 

The challenges that the solution aims at solving are (a) how to work with very limited information, (b) how to measure the impact of the distribution drift, (c) how to specify the trade-off between retraining and poor performance.

### Strengths
- The work focuses on a timely problem that has not been studied enough in the literature. The problem of deciding when to retrain a model is crucial in real deployments of ML models.

- The authors show analytically the relation of their proposed formulation and problem with similar approaches, such as reinforcement learning (cf. 8.6) and CARA formulation (8.7). 

- Results in one of the datasets show that the proposed solution (UPF) is able to keep track of the optimal solution when the relation between accuracy and retraining cost varies. This behavior is shown for both total cost and number of retraining instances.

### Weaknesses
 - Very important: It is not mentioned in the title or main parts of the work (Abstract) that the work focuses on classification only. It is important, as there is no discussion or result on how this solution could work for regression tasks. Please make sure you explicitly mention this, including a possible modification of title. 

- It is not clear how the solution solves some of the 3 challenges mentioned in the abstract. A reader would think that the challenges highlighted in the abstract would be solved or at least considered in the work. However, it is not clear how, for example, the solution delas with "1) very limited information". While some results are provided in the appendix, it would be appreciated if the evaluation of how this challenge is handled by the solution is given more importance and mentioned in the main text. For example, how the performance of the proposed solution and the baselines evolves as the amount of the available information decreases would be really helpful. 

- Among the limitations mentioned for the most important baseline (CARA), it is said that CARA assumes that "the difficulty of the task remains constant". But it seems that the proposed solution also considers such aspect. The authors fix the complexity of retraining for any time, the number of samples, etc, so the difficulty is not modified throughout the experiment. We can see this in the text between (2) and (3), where the temporal dependance of the retraining cost c, cost loss e, and number of predictions N is dropped. 

- Authors mention in the abstract and other times that "online learning formulation overlooks key practical considerations. A proper comparison (in evaluation results) against online learning approaches is missing (as well as against RL, mentioned below). In such way, it would be clear why online learning cannot be used. Is it because it doesn't consider retraining cost? How can we compare retraining cost (of the whole model) with the incremental updates applied in online learning? Why is it discarded? What are the challenges of including it in the evaluation?

- IMPORTANT: Problems with mathematical notation: Some terms are not defined, some terms are called in different ways, and some mathematical assumptions are not well supported. ... The detailed cases are provided in the following box "questions". 

- Proposition 3.1 is interesting. However, it is difficult to fully grasp its significance because the result is not shown in the Results Section. Prop. 3.1 provides a bound but we do not know if this bound is tight or so loose that it is meaningless. Some results on the values provided by the bound and the practical values obtained by the algorithms would be extremely appreciated. 

- Lack of complexity comparison. The complexity of the algorithm and the corresponding comparison with the baselines is missing. For example, while CARA is evaluated and compared against the proposed algorithm, it is several times mentioned that CARA is computationally intensive (cf. 8.1). Yet, we do not know if the proposed algorithm is similarly demanding or it offers significant improvement in terms of complexity reduction. A quantitative analysis of the complexity of the different solutions would be welcome to strengthen the contribution of the paper. 

- While the comparison with Reinforcement Learning (RL) is discussed in the main document and the appendix, highlighting that RL is not sample efficient and is not impractical, and authors show the analytical correspondence of the proposed formulation and the RL formulation, it would have been welcomed if the authors have provided quantitative proofs of such claims. Evaluating a SotA RL algorithm adapted to the problem considered and measuring its performance with the same datasets and use cases would have provided support to the claim of not considering RL for the problem. 

- From appendix 8.5, we can see that the selected dataset to show the main results in Section 6 (e.g., fig. 2) is the best case, where the proposed algorithm clearly performs better than the baselines. This behavior is not so evident for the other datasets in 8.5. For example, In Fig. 5, for the yelp dataset, we can see that the proposed algorithm is not among the best performing solutions, and it is overpassed by several cases, some as simple as adwin.

- The results section have some flaws, 
    - Why Figure 3 only shows the values of alpha between 0 and 0.1, when previous figures show the range between 0 and 1? Please provide an explanation or extend the range evaluated to match that of the other cases.  

- In appendix 8.5, the oracle is not provided. Thus, we miss information about how far are algorithms from the best.

### Questions
- UPF, the name of the proposed solution, is not defined

- Mathematical issues:
    - In (1), x_i,j and y_i,j are not defined. While one can infer that they corresponds to input parameters and classification labels, it is not mentioned anywhere. The same happens with X, Y. Moreover, if X, Y represent the set of values in D_j (please explain it), the notation in (2) is not rigorous and should be modified, as the values should be x_i,j and y_i,j that below to D_j. Besides this, x_i,j is later used to refer to a different term. Please do not use the same notation for two different things,  correct this problem. 
    - It is not clear why the authors define the matrix PE. The values in PE are never used as a matrix, they are always considered as individual values. Thus, why creating a matrix? one can just define the values as scalars. 
    - How does g(t, I_<t) depend on t apart from I_<t? if there is no more dependence, please remove "t,", keep only the second value. 
    - There are several inconsistencies in the use of the notation, for example with the sub-index \phi of \alpha. 
    -  The whole section 4 is a bit unclear and could benefit from a revision.  The following points are examples of this aspect. 
        - g_\phi is not defined but directly mentioned in Section 4.  What is defined before is g() with no sub-index. Thus, it is not clear at first what is the meaning of \phi. 
        - PE_i,j in line 240 has a different notation and it is not anymore a matrix. Moreover, two lines below the comma between i and j is dropped, the same happens to A_i,j and _ij. Please be consistent with notation. 
        - In (8), shouldnt the left part also respect the i<j  condition on the right part?
        - In (9), please provide a proof of mutual independency. 
        - x_i,j is used here for something different than in (1)
         a_ii,j is not defined. What is it? A realization of A_i,j? please be explicit. 
        - How accurate is the approximation of Beta as a normal distribution? Could the authors include results for the case in which no approximation is done?
        - Which is the reason for which you can assume that the variance for all x_i,j is constant? (line 267) 
        - Again, it is not explained what \phi refers to.
        - Footnote 2 must be in the main text. It is an important aspect, a definition of a key value, and should be in the main text. 
        - It is not clear what "l_1 distance between the average feature vectors of the two recent datasets" refers to. x_i,j = [i,j,i-j,z_shift] are referred to as input features. Are the "feature vectors" referring to x_i,j? or do they refer to the input data of the dataset? Please explain better this aspect, maybe re-naming some of these terms. 
        - In (13), the notation of P(A_i,j) is not clear. It seems that it refers to a probability of an event A_i,j, but it actually means that the distribution of A_i,j is a Beta distribution. Please explain better this relation, maybe re-denoting P() for other notation. 
        - In (14), we do not know the values for times bigger than t, it is not clear how you perform the steps related with forecasting.Shouldnt it be that T in the sum becomes "t"?
        - In line 300, it is misleading that "we only incur the performance cost of the old model", because we also incur in the future cost for the decisions we will make. 
        - "W" in (19) is not defined. 
   
- Section 5: Do datasets D_j include all previous datasets? not specified. 

- Section 5: C(\theta) sometimes has sub-index alpha, sometimes not. Be consistent. 

- Section 5: What is "w". 

- Section 5: Line 400, "For \mu...", it is not clear why this is included in dataset. A better explanation of how you use \mu would be appreciated.

- In table 2, bold values are not clearly explained

- Please, revise the "* denotes statistical significance ..." sentences, mostly in tables. some have typos (e.g. Table XX), and some are not clear. If * represents the same for all tables, just use the exact same sentence in each of the tables, to make it clear for the reader. For example, in Table 5, "∗ denotes statistical significance with respect to the next best baseline," probably wants to express that "∗ denotes statistically significant difference with respect to the next best baseline,", as in Table 3, where there is actually a typo ("significanct"). Please be consistent referring to the same concept exactly in the same terms each time it appears. 

- Conclusions could be extended to provide some more insights about the contribution, limitations/to-do points, and key take-away messages of the work 

------ Typos and writing suggestions ------
- "uncertainly", line 092
- Line 314, "15" -> (15), same for line 325 with 16- 18
- In appendix 8.2, please correct the repeated typo "t1" instead of "t_1"
- In appendix 8.2, please correct the repeated typo "p" instead of "pe"
- In appendix 8.2, please explain what the red color means. Please also explain each of the steps in the derivation. 
- "each datasets", appendix 8.4.
- In 8.4, please explain each column in Table 4, especially w, T.
- In 8.5,  please correct the first line "Figures 4,  5 8" 
- no comma in "We observe in Table 3,"
- Adwin and Fhddm -> wrong style in line 459

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on retraining problem i.e., when to retrain or update the machine learning model during its development. The authors provide a theoretical formulation of the retraining problem. Then, they propose a novel retraining decision strategy based on performance forcasting. Besides, the authors also give detailed discussion about the relationship between the proposed formulation and offline reinforcement learning. Experiments on tabular and image datasets are conducted to support the proposed method.

### Strengths
1. The investigated problem is newly proposed and important in practice. Determining when to retrain or update the machine learning model is of great importance in many real-world applications.
2. The authors provides a rigorous formulation of the retraining problem. The analysis about upper limits on the optimal number of retrain based on performance bounds is novel and sound in my view.

### Weaknesses
First of all, I would like to acknowledge that I am unfarmilar with the related works. From my reading of the paper, I have the following concerns:
### Major
- Some essential related works are not well compared in this work. For example, in section 4.1, the authors propose to learn a performance predictor to forecast unknown entries in PE. As far as I can tell, the motivation of such predictor is very close to uncertainty estimation/quantification [1] [2]. However, the paper do not discuss the difference bettween the predictor in 4.1 with this line of works. Specifically, the paper does not address how the proposed predictor differs from methods that estimate prediction confidence or model calibration, which are crucial for assessing model reliability. The lack of discussion on how the proposed performance predictor relates to or differs from these established techniques is a significant oversight.
- Strict assumptions. In line 217, the authors assume that all the dataset is IID and there is no distribution shift. Such assumption seems inpratical to me. If there is no distribution shift, why the performance of machine learning model drops as time goes by? I suspect the IID assumption is relatively too strong for the retrain problem this paper focuses on. Besides, I also have concerns if the learned performance predictor described in 4.1 can work well under distribution shifts. Since it is not easy to aquire such a predictor in OOD detection or error detection tasks according to [1] [2]. The assumption of conditional independence of $A_{i,j}$ given parameters $\alpha$ and $\beta$ also seems overly strong. It is unclear how this assumption would hold in practice, especially when dealing with complex data where dependencies between data points are common. The paper needs to provide a more thorough justification for this assumption.
- Limited experiments. The authors conduct experiments on both tabular and image datasets under binary classification settings. The number of samples, features and classes are all very small in these datasets. Thus I have concerns about whether the proposed method is practical on more realistic benchmarks. The datasets used are not representative of real-world scenarios where models are deployed. The lack of experiments on larger, more complex datasets makes it difficult to assess the scalability and practical applicability of the proposed method. For example, the image datasets used are far smaller than typical image classification tasks, and the tabular datasets lack the complexity of real-world tabular data.
### Minor
- The retrain problem may have been mitigated to some extent by techniques from other fields. For example, life-long learning and transfer learning. If this is true, the importance of this paper will be weaken. Some discussion about this point will benefit the overall quality of this paper.

It is possible that I missed some details of this paper. I am pleased to be corrected by the authors.

### Questions
See above.

### Soundness
2

### Presentation
2

### Contribution
3
