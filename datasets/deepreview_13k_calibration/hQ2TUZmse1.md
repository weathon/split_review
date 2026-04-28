# Refining Counterfactual Explanations With Joint-Distribution-Informed Shapley Towards Actionable Minimality

- Decision: Reject
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Counterfactual explanations (CE) identify data points that closely resemble the observed data but produce different machine learning (ML) model outputs, offering critical insights into model decisions. Despite the diverse scenarios, goals and tasks to which they are tailored, existing CE methods often lack actionable efficiency because of unnecessary feature changes included within the explanations that are presented to users and stakeholders. We address this problem by proposing a method that minimizes the required feature changes while maintaining the validity of CE, without imposing restrictions on models or CE algorithms, whether instance- or group-based. The key innovation lies in computing a joint distribution between observed and counterfactual data and leveraging it to inform Shapley values for feature attributions (FA). We demonstrate that optimal transport (OT) effectively derives this distribution, especially when the alignment between observed and counterfactual data is unclear in used CE methods. Additionally, a counterintuitive finding is uncovered: it may be misleading to rely on an exact alignment defined by the CE generation mechanism in conducting FA. Our proposed method is validated on extensive experiments across multiple datasets, showcasing its 
effectiveness in refining CE towards greater actionable efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper titled "Refining Counterfactual Explanations with Joint-Distribution-Informed Shapley Towards Actionable Minimality" proposes a framework for improving counterfactual explanations (CE) in machine learning models. Current CE methods often include unnecessary feature changes, making them difficult to apply in practical scenarios. The approach proposed in this paper seeks to minimize these changes while maintaining the validity of the counterfactual exercise, making CE more actionable for both users and stakeholders, particularly in terms of simplified and actionable decision-making.

*Major contributions of the paper include:*
1. The setup of a well-defined problem for finding CE with minimal feature changes (Equation 1).
2. The development of the algorithm "COunterfactuals with Limited Actions (COLA)" to find the solution to the previous point.

*Sub-contributions that are incorporated into the definition of COLA:*
- The definition of a generic Shapley framework (p-SHAP), which nests several other commonly used Shapley frameworks for computing feature importance and allows for incorporating the distributional connection between factual data $x$ and counterfactual data $r$, i.e., their joint distribution $Prob(x,r)$, in its computation.
- They show that p-SHAP correctly measures the causal behavior of shifting $x$ towards $r$ (Theorem 4.2).
They propose Optimal Transport (OT) techniques to recover $Prob(x,r)$, given $x$ and $r$, which can be incorporated into p-SHAP for CE. The OT guarantees tighter bounds on the distance between factual and counterfactual, $D(f(x), y^*)$, under the assumption that the model $f$ is Lipschitz continuous and $y^* = f(r)$ (Theorem 4.1).
- They derive the computational complexity of COLA.

The authors combine a collection of algorithms in order to construct COLA. Each of the algorithms is listed below:

a. FIND $r$: For a counterfactual $y^*$ and a factual $x$, find $r$ within an $\epsilon$ radius of $x$ to minimize the distance $D(y^*, f(r))$.

b. COMPUTE $Prob(r,x)$: Once $r$ is found, use it to estimate the joint density $Prob(x,r)$, (mostly) with OT.

c. COMPUTE p-SHAP values: Once $Prob(x,r)$ is obtained, use it to estimate p-SHAP values $\phi$ between $x$ and $r$.

d. OBTAIN THE CE: Using $\phi$, together with $Prob(x,r)$ and $r$, edit $x$ minimally in order to obtain the CE of $y^*$ from $x$, called $z$.

*Numerical Results:*
- The authors test their algorithm using four different datasets, where the task is classification. They show that the algorithm is feasible and achieves $z$ with empirically minimal changes compared to five other CE algorithms, with minimal or zero misalignment $D(f(z), y^*)$, across 12 different classifier models.
- In simpler setups, the authors compare COLA’s performance in terms of finding the $z$, measuring its performance $D(f(z), y^*)$, while comparing it to the optimal theoretical performance. Although not achieving optimality for some scenarios, COLA sometimes still outperforms CE methods that use exact alignment.

### Strengths
- The paper attempts to contribute to important theoretical explainability literature, in addition to connecting to real-world demands to make model explanations more actionable. This is a growing demand in several areas of society, especially with current and incoming AI regulation.
- The authors thankfully write for a broader audience without being too verbose. Although most of the paper’s contribution is presented starting in Section 4, the content before this section provides several points of entry and the exact amount of revision a reader needs to understand their framework. I personally learned from their exposition.
- The method is mostly sound and tries to be as generic as possible (e.g., as p-SHAP is a generic formulation), and the authors provide intuition for most of their steps. Overall, the paper seems well-polished and organized, lacking only a few important adjustments. 
- A clear algorithm is defined, consisting of a collection of widely used algorithms, and its computational complexity is derived, which is informative for scalability. 
- Their methodology is tested in a wide variety of settings, i.e., using four different divergence functions, four different datasets, comparing COLA to five other CE algorithms, and utilizing 12 different classifiers. This is useful to demonstrate the robustness of their method compared to others.

### Weaknesses
 *PRESSING ISSUES*
- COLA has a well-defined procedure to compute $z$. It seems clear from Theorem 5.1 that $z$ would satisfy the constraints from Equation 1, but it is not clear how the chosen $z$ from COLA is actually optimal, i.e., why is it minimizing, or closer to minimizing, the problem in Equation 1, given that the last algorithm in COLA to find $z$ does not minimize any function. Even if it is not optimal, as suggested by Figure 4, the paper would benefit from having a clearer narrative of why COLA is closer than other methods to optimal, considering the minimization problem in Equation 1. Specifically, while the method uses feature attribution to identify important features, it does not explicitly minimize a loss function related to the objective in Equation 1 when generating the final counterfactual $z$. The connection between the feature importance scores and the minimization of feature changes is not clearly established, leaving a gap in the explanation of why COLA's approach leads to minimal changes.
- The connection between $p-SHAP$ and $p_{OT}$ in Section 4 can be improved. This is the part that seems to be able to benefit the most from clarity and extra sentences connecting these two different topics and situating them in the bigger goals of the paper. A few suggestions:
    - When introducing the OT problem in this section, the reader might benefit from having a sentence or two mentioning what the goal of OT is, in addition to its purpose in p-SHAP. This is somewhat done in row 209, but I believe it would be clearer if it comes earlier in the previous paragraph. The current explanation does not sufficiently highlight how OT's ability to find the most cost-effective way to transform one distribution into another directly aids in identifying the minimal feature changes needed for a counterfactual.
    - It would be great to have a clear explanation/insight in the paper about why $A_{prob}$ does not necessarily require knowledge of how $r \sim \mathcal{D}$ is generated in order to achieve good CE performance. The paper should clarify why the method's reliance on the joint distribution $Prob(x,r)$ derived from OT, rather than the counterfactual distribution itself, is beneficial for feature attribution. It's not immediately obvious why this approach avoids issues related to the specific CE algorithm used to generate $r$.
    - In the “Theoretical Aspects of p-SHAP”, it would be helpful to know more precisely why using OT for obtaining the joint distribution $Prob(r,x)$ helps later with minimizing $D(f(z),y^*)$. This connection doesn’t seem to be precise as it is. The paper needs to explicitly state how the joint distribution obtained via OT translates into a minimization of the distance between the predicted counterfactual and the target counterfactual, especially considering that the final step of obtaining $z$ does not involve direct optimization.
    - Theorem 4.1 is labeled as “p-SHAP towards CE”, but the theorem is much more a result of OT + Lipschitz continuity of $f$, and its direct connection to p-SHAP seems to be missing. The theorem's connection to p-SHAP is not clearly articulated, and it should be made more explicit how the bounds derived from OT and the Lipschitz constant are used to guide the feature attribution process in p-SHAP.

*OTHER*
- The paper provides so many entry points for the reader, and it would be nice to also have the definition of “Exact Alignment” and “Feature Alignment (FA) performance” at least once in a footnote.
- Perhaps writing a sentence at the beginning of Section 3, and/or at the end of Section 2, so the reader knows what to expect in the transition from Section 2 to Section 3, and how they fit in the big picture of the paper.
- Row 472: Result III could benefit from having a sentence entry point to situate the reader as to why this is important and how it fits in the big picture of the paper. Furthermore, another sentence would be useful to provide insights on why $CF-P_{OT}$ outperforms $CF-P_{Ect}$.
- Please add titles to the x-axes of Figures 3 and 4, either in the image or in their descriptions.

### Questions
Specific suggestions (please feel free to ignore these if I didn’t understand things well):
- In order to make this methodology widespread and for reproducibility, I don’t know if the authors considered converting their code (in the supplemental material) to a Python package or creating a Python class? I am not sure if the editor should require this for publication?
- Typo on row 196? “First p-SHAP degrades to RB-SHAP”, shouldn’t it be B-SHAP?
- Typo on row 474? Word alignment misspelled?
- Perhaps clarify on row 231 that it is the tightest Lipschitz upper bound, not necessarily the tightest upper bound.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a post-hoc modification of a set of counterfactual explanations. It does so with the aim of reducing the modification-costs of the counterfactual explanations found. To do so, it employs a new variant of the common SHAP feature attribution technique, which explicitly includes both in-distribution and counterfactual-distribution data in the SHAP baseline prediction computation. The feature attributions so obtained are used to modify the existing set of counterfactual explanations, and it turns out that this modification reduces the costs associated with the counterfactuals.

### Strengths
The paper presents a new problem perviously unreported in the literature, and solves it effectively. The empirical findings seem to be robust and diverse. The paper presents the proposed method adequately and displays the improvements it provides through exhaustive experiments.

### Weaknesses
The writing could be clearer. The paper introduces and repeatedly uses terms without defining them: "exact alignment" (line 25, 197, etc; finally explained only on line 308), "well-performed action plans" (line 98), etc. It would be useful to define the terms at the time of their first use.

I do not understand the "decoupling" phenomenon mentioned in line 85-86, and the reference to the later demonstration was lost (or I may have missed it). Perhaps more exposition and an explicit reference to where in the paper to find this "later" would be helpful.

The "counter-intuitive finding" described in lines 101-105 remained difficult to parse until I had reached the end of the paper, because "associating" and "alignment" had not been defined yet. These terms can be defined and explained earlier in the paper, so that the findings become easier to understand in a first read. The abstract could also be amended similarly to ensure that it is easier to understand.

It is unclear to me why the proposed SHAP variant performs better than other SHAP variants, or indeed why would SHAP feature attributions be a good way to perform post-hoc optimisations on generated counterfactual explanations at all. The paper presents the proposed method adequately and displays the improvements it confers, but I'm unsure why this is the case. Any intuition or ideas that the authors have about this would be good to include. While additional experiments aren't strictly necessary, I am curious about how non SHAP based methods would perform. I have not looked at the code directly, but if the results are easily replicable, this might lead to rapid future work in this area, providing more understanding of the phenomena reported in the paper.

### Questions
Reordering the writing would help readers make sense of the contributions in a single pass. The inclusion of SHAP seems arbitrary - and although demonstrated to work well - it is unclear why other methods are not included.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes an algorithm to compute CFEs for datapoints such that a minimal number of features are changed, thereby generating sparse CFEs.

### Strengths
The paper establishes an excellent mathematical framework to generate CFEs such that they change the smallest number of features from the original datapoint. This framework connects CFEs with Feature attribution technique SHAP.

### Weaknesses
### summary:
 The paper proposes an algorithm to compute CFEs for datapoints such that a minimal number of features are changed, thereby generating sparse CFEs.

### soundness:
 3

### presentation:
 3

### contribution:
 1

### strengths:
 The paper establishes an excellent mathematical framework to generate CFEs such that they change the smallest number of features from the original datapoint. This framework connects CFEs with Feature attribution technique SHAP.

### weaknesses:
 There are several weakness in the paper, I list them as follows. The authors only need to address the ones marked as major for the rebuttal (if they like to):
1. Line 51: "some CE algorithms assume differentiable models, whereas others are designed specifically for tree-based or ensemble models" -- this is misleading, as many CE algorithms work for black-box ML models, you can find them in the Verma et al. survey paper. 

2. [Major] Line 79: "Three major challenges remain in addressing this problem". The next three lines do not sounds like challenges at all. The first one says that one CE algorithm will not suffice (which is not true as past work have proposed algorithms that work for generating sparse CEs), the second one about not assuming anything about the model (this is not novel several works have done this), and the third is about how feature attribution techniques can be misleading (which is obvious because they are not optimized to be used as CE, a feature that is marked as important by some FA method does not necessarily mean that it is an effective way to change the prediction). Please state the challenges (if there are any).

3. Line 124 $M_{c_{ik}}$ is not defined which makes understanding Eq 1(d) and 1(e) hard. Also how does having $c_{ik}$ = 0 allows no change in its value? I don't see that being implied from the equation

4. B-SHAP and RB-SHAP have different background distributions and it is clear to the community about the advantages and disadvantages of each. You define CF-SHAP, but never state what trade-off does one expect when using background distribution from CF distribution instead of the training distribution. Please explain what should one expect from such a FA method. 

5. Line 197, correct the typo from RB-SHAP to B-SHAP.

6. The first paragraph of section 4 is obvious, it is just a generalization of the notations from Equations 4-6, I don't think there is a need to give so much attention and explanation for it. 

7. [Really Major]. You mention a lot of details about the optimal transport thing to compute the most sparse CE, and do a really good job at explaining Algorithm 1 in Section 5. At this point, I am excited and was anticipating some great experimental results because you spent such a large part of the paper establishing strong mathematical grounds for generating CFEs and even proved some theorems, but the experimental section is **extremely weak** and does not convince me at all about the relevance of the propose technique. 
       1. First and the most important weakness is that you need another CFE generation technique to generate a CFEs for a lot of datapoints that you use to compute the joint distribution and then generate a CFE using your technique, is that right? If that is the case, in the paragraph of computation complexity, why do you not include that? Also it is not the case that your technique just takes a CFE from some other technique and refines it, it needs a whole lot of datapoints and CFEs to even start functioning. Please correct me if I am wrong. 

       2. The experimental results are very weak for the following reasons:
              **a.)** Result 1 in Section 6 (lines 415 - 421) are not useful when a datapoint does not achieve the desired classification. In other words, if a datapoint does not achieve y* classification (which makes it a valid CFE), there is no point in mentioning the sparsity of that, because it is an invalid and not useful CFE. Therefore the third column in Table 3 is not useful at all. 

             **b.)** Several baselines are mentioned in lines 368-372, but none of them are used in the experimental results section? Why? Aren't these the baselines that you need to compare against to show that your technique is better than them atleast in the one metric you are targeting (which is sparsity)? Instead what you do in Table 3 is compare against 5 variations of your own proposed method. Sure one of your own method is better than the other 4 you mention, that does not tell me anything about how does COLA compare to previous techniques. Please let me know if you disagree. Therefore Result 2 is not useful. 

             **c.)** The baselines considered in the paper (the results for which are not reported atleast in the main paper), are outdated and several new techniques have been proposed that are better at all metrics than DiCE and KNN, for e.g. see Amortized Generation of Sequential Algorithmic Recourses for Black-box Models. 

            **d.)** An underlying and unstated key assumption in the formulation of the paper is that sparsity is the most important metric to consider when generating CFEs. This is atleast not agreed upon by the community, see the list of metrics proposed in Verma et al. survey paper.

### questions:
 I have stated all the questions in the weakness section of the review. The paper needs to really strengthen its experimental results section. I would expect something like a table, where the columns are the various metrics along with a CFE is evaluated, like validity, proximity, sparsity, distance of training data manifold, adherence to causal constraints, and the time to generate the CFEs (including dependence on any other technique) and the rows to be a large set of baselines. Only when the numerical results demonstrate the superiority of COLA, can the supporting theory, theorems, and the claims of near-optimal performance be useful.

### flag_for_ethics_review:
 ['No ethics review needed.']

### rating:
 6

### confidence:
 5

### code_of_conduct:
 Yes

### role:
 Review

### Questions
I have stated all the questions in the weakness section of the review. The paper needs to really strengthen its experimental results section. I would expect something like a table, where the columns are the various metrics along with a CFE is evaluated, like validity, proximity, sparsity, distance of training data manifold, adherence to causal constraints, and the time to generate the CFEs (including dependence on any other technique) and the rows to be a large set of baselines. Only when the numerical results demonstrate the superiority of COLA, can the supporting theory, theorems, and the claims of near-optimal performance be useful.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the challenge of creating valid and actionable counterfactual explanations by minimizing unnecessary feature changes. The authors introduce the COLA framework, which computes a joint distribution between observed and counterfactual data to inform Shapley values for feature attributions. This joint-distribution-informed approach allows them to refine the counterfactual explanations without imposing restrictions on model types or algorithms to compute the counterfactuals.

### Strengths
This paper addresses the important task of making counterfactual explanations actionable by minimizing unnecessary feature changes.

The authors offer a detailed theoretical basis for their methodology with clear explanations and motivations. 

By sharing their code and giving computational details, the author makes the approach more accessible and transparent.

The results seem robust and the counterintuitive finding that relying solely on exact alignment between factual and counterfactual data can be suboptimal is interesting.

### Weaknesses
The approach is computationally demanding, mainly due to the optimal transport (OT) calculation, which may limit its scalability in large datasets. (which the authors acknowledge.)

While OT provides a probabilistically informed alignment, it may only sometimes yield the optimal feature attributions for all tasks, as it lacks task-specific tuning and causal considerations. However, the authors denote this as future work.

The approach is primarily evaluated on binary classification and tabular data, leaving its effectiveness on multiclass or regression and other data types (e.g., images, text) scenarios unexplored.

### Questions
How well would this method generalize to different multiclass and regression settings?

### Soundness
3

### Presentation
3

### Contribution
3
