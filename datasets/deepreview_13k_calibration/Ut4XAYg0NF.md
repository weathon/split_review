# Explainable Sequential Optimization

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 6, 3, 5, 1

## Abstract
We propose formulating stochastic model predictive control into a coalition game to use Shapley values for feature attribution. Such analysis is crucial for transparency and achieving optimal outcomes in high-stake applications such as portfolio optimization and autonomous driving. We categorize Shapley values estimation methods into three families: those based on weighted linear regression, sampling permutations, and multilinear extension.  We survey, benchmark, and provide valuable insight into these methods, previously not attempted in this context. Our experiments show that halved Owen sampling from multilinear extension and KernelShap-Paired from weighted linear regression, both utilizing antithetic sampling, perform best.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper formulates stochastic model predictive control into a coalition game, and uses Shapley values for feature attribution. Specifically, it has performed a systematic study of explaining stochastic model predictive control systems. It has also surveyed existing methods for estimating Shapley values. Detailed experiment results have been provided in Section 5.

### Strengths
- The considered problem seems to be interesting and important.

- This paper has done a good job of literature review.

- The experiment results in Section 5 seem to be rigorous and extensive.

### Weaknesses
- The main body of this paper is not self-contained. In particular, some key concepts such as Shapley values are defined in the appendices. Please move them to the main body to make the paper self-contained and more readable.

### Questions
Please address the weaknesses listed above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper considers solving a control problem using explainable methods. Specifically, the author(s) proposes reformulating the control problem as a coalition game, enabling the use of Shapley values to specify the contribution of each individual feature. The author(s) also reviews relevant literature on Shapley value estimation and applies these methods in numerical studies.

### Strengths
I summarize the paper's contributions as follows:

* **Originality**: The application of Shapley values to sequential control appears to be novel, to the best of my knowledge. Additionally, the concept of "explainable" sequential optimization has received relatively little attention in the literature.
* **Quality**: The paper is soundly written. I did not identify any technical errors.
* **Clarity**: Overall, the paper is well-organized and easy to understand.
* **Significance**: The methods are relevant to the field of "explainable" AI and could potentially be very useful and applicable in practical scenarios.

### Weaknesses
1. The paper predominantly focuses on the example of portfolio optimization, where the meaning of Shapley value is clear. However, its interpretation becomes less unclear when applied to other control problems in robotics and operations research. The paper could be potentially improved by adding more use cases to strengthen the motivation of the proposal.  

2. Including numerical experiments is excellent, and I anticipated to see how the proposed methods demonstrate 'explainability' through Shapley values. However, it seems the authors focused solely on comparing different methods for computing Shapley ratios and reporting these estimates, without discussing their explanatory power. However, such explanations are necessary to illustrate how the proposed method is 'explainable'.

3. In terms of presentation, the paper reads like a survey paper as in several places, it mentions it surveys methods for Shapley value estimation and compare these methods numerically. It may be beneficial to revise the presentation to ensure the paper is not primarily a survey. 

4. Additionally, the main text frequently refers to the appendix for more detailed explanations, which disrupts the flow of reading. I suggest to reduce the number of such references where possible to enhance readability.

### Questions
Please refer to the weaknesses section

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
It would be useful to clarify the contributions of this paper in the rebuttal. It seems to me that this paper is a combination of an introduction to Shapley values, a literature review of this subject and an experimental study of related methods. If this is the aim, I believe that the paper would be better placed in a journal and it should be expanded. In particular, in the main paper, the introduction to the subject is quite short and assumes some knowledge of collaborative games. If the aim of this paper is to introduce this subject to a wider audience then a more thorough introduction is appropriate.  On the other hand, if the assumption is that the reader is already quite familiar with collaborative games then I wonder how much is gained by some light touch overview and an experimental study of a topic (Shapley values) which has been introduced in the 50s and for which a Nobel prize has been awarded -- surely a reader familiar with collaborative games will have a good understanding of Shapley values.

### Strengths
The paper provides an overview of classical subject in game theory and an extensive experimental study.

### Weaknesses
I believe that the paper is misplaced in a conference and it would be better to write a review article for a journal, if the aim is to introduce a wider audience to the subject.

### Questions
It would be useful to clarify the contributions of this paper in the rebuttal and to explain what the authors are aiming for.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes using Shapley values to perform feature attribution in Model Predictive Control (MPC) problems, where different features include constraints and losses. A portfolio optimization use case is considered where multiple Shapley value estimation methods are benchmarked.

### Strengths
The paper discusses and proposes an explainability approach to Model Predicting Control based on Shapley values which, to the best of my knowledge, is novel.
The experimental study is extensive and sound.

### Weaknesses
The main weaknesses of the paper are: 
- The presentation can be improved significantly. It would be good to define Shapley value somewhere in the main text? Moreover, all the plots are clearly not presentable (legends are too small, lines too thin). There are probably too many repetitive plots in the main text and too little details on estimation methods benchmarked. 
- The paper, starting from its motivations, is heavily focused on MPC for portfolio optimization setups. Thus, although I could imagine similar considerations hold in other MPC problems, it is not clear that experimental results transfer.
- Based on the above, the title is too general. Sequential optimization covers many sub-fields (e.g. bandits, online convex optimization, etc.) in which there is no notion of features (i.e. constraint or losses) similar to the ones considered in the paper.

### Questions
- The MPC is based on receding-horizons, where computed actions (and thus selected constraints/losses) are only useful for planning. How are these 2 time-scale separations (i.e. planning vs. acting) taken into account for computing Shapley values? 

- Was supplementary material correctly submitted as separate pdf? From what I see the submission contains a single *pdf with 36 pages.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper stuides the problem of explaining the influences of constraints and loss terms in stochastic model predictve control problems. In particular, an additive component atribution model is considered.

### Strengths
The problem setting is interesting. In multi-stage problems, credit assignment / attributing results to decisions is a very important topic to study.

----

### Weaknesses
*1.* The paper is not well-written and is very hard to follow. I have a hard time figuring out the connections between some sentences. 

*2.* The main contribution of this paper is missing in the main paper, i.e., the connection/formulation of the explainable stochastic MPC and coalition game is not well presented in Section 4. Table 1 does not provide enough information for readers to understand.


*3.* Simulation results are hard to follow. The baselines are not introduced or explained. The figures are too small. 

---

### Questions
N.A.

### Soundness
1

### Presentation
1

### Contribution
1
