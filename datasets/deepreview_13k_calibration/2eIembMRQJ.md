# Active Teacher Selection for Reinforcement Learning from Human Feedback

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5

## Abstract
Reinforcement learning from human feedback (RLHF) enables machine learning systems to learn objectives from human feedback. A core limitation of these systems is their assumption that all feedback comes from a single human teacher, despite querying a range of distinct teachers. We propose the \textit{Hidden Utility Bandit} (HUB) framework to model differences in teacher rationality, expertise, and costliness, formalizing the problem of learning from multiple teachers. We develop a variety of solution algorithms and apply them to two real-world domains: paper recommendation systems and COVID-19 vaccine testing. We find that the \textit{Active Teacher Selection} (ATS) algorithm outperforms baseline algorithms by actively selecting when and which teacher to query. The HUB framework and ATS algorithm demonstrate the importance of leveraging differences between teachers to learn accurate reward models, facilitating future research on active teacher selection for robust reward modeling.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers active teacher selection within the realm of RLHF,  tackling pivotal queries pertaining to the optimal teacher to consult and the most opportune moments for such consultations. Many existing works assumes the feedback comes from a single human teacher. The author(s) proposed a hidden utility bandit framework to mathematically formulate the problem, modelled the data generating process via POMDPs and developed active teacher selection algorithms for regret minimisation.

### Strengths
**Originality**: The manuscript tackles a novel and underexplored issue within the context of RLHF. To the best of my knowledge, there exists a limited number of theoretical and methodological papers on this subject. Many existing work considers scenarios featuring a single human instructor responsible for delivering feedback. The active teacher selection has not been explored comprehensively in the literature, rendering this paper a valuable contribution to the field.

**Clarity**: The writing is generally clear. 

**Significance**: The issue of active teacher selection holds considerable weight in practical scenarios, particularly given the potential high costs associated with soliciting input from teachers. The paper sheds light on intriguing findings that are in concordance with established knowledge in the field. For instance, it highlights instances wherein seeking insights from less knowledgeable instructors could yield richer information, thereby enhancing the accuracy of model parameter estimation.

**Quality**: The paper stands out for its soundness, evident in the problem formulation, the underlying principles of the proposed solution, and the methodological approach adopted. The authors have demonstrated proficiency in laying down a solid mathematical foundation, which underpins the validity and robustness of their work.

### Weaknesses
While the paper makes significant strides in addressing the active teacher selection problem within RLHF, certain aspects could benefit from further refinement and elaboration.

**Theoretical Justification**: The theoretical underpinnings of the algorithms presented in the manuscript are somewhat lacking. The paper does present two theories, yet these appear to be more of preliminary lemmas than comprehensive theoretical validations. A better analysis would entail a comparative study of the regret associated with the proposed algorithm against established benchmark methods, such as consistently relying on a single teacher. This comparative analysis would provide readers with a clearer understanding of the advantages and potential drawbacks of the proposed method. Specifically, the regret bounds should be derived with respect to a clear baseline, such as a uniform random teacher selection policy or a policy that always selects the teacher with the highest estimated competence. Furthermore, the assumptions under which the regret bounds hold should be explicitly stated and justified. The current theoretical analysis lacks a clear connection to practical performance, and it would benefit from a more rigorous treatment of the convergence properties of the proposed algorithms.

**Clarity and Notation**: The manuscript exhibits areas of ambiguity, marked by several instances of unclear notation and expressions, particularly in Sections 2 and 3. The abundance of notation can be overwhelming, detracting from the overall readability of the paper. A revision aimed at simplifying and clarifying these sections would enhance the manuscript's accessibility. For example, the definition of $\mathcal{D}$ and $\mathbb{D}$ is confusing, and the distinction between them is not immediately clear. Additionally, the HUB framework, a central component of the paper, is not adequately explained. The manuscript would greatly benefit from the inclusion of detailed examples illustrating the practical application of this framework. Providing clear, real-world scenarios that elucidate the concepts of 'arms' and 'items' within the context of the HUB framework would render the paper more informative and user-friendly. The current description leaves the reader struggling to understand how the abstract concepts map to concrete elements in the RLHF setting. For instance, what constitutes an 'arm' when the goal is to optimize a language model's response based on teacher feedback?

**POMDP Literature**: Given that the paper addresses the problem using POMDPs, it is imperative to include a thorough discussion of relevant POMDP literature. Incorporating references and discussions around works such as https://www.cs.cmu.edu/~ggordon/boots-siddiqi-gordon-closing-loop-psrs.pdf, https://arxiv.org/abs/2006.12484, https://arxiv.org/pdf/2207.13081.pdf, alongside an exploration of their relevance to the current study, would lend greater depth and context to the paper. The current discussion of POMDPs is too brief and does not adequately situate the proposed approach within the broader landscape of POMDP research. Specifically, the paper should discuss how the proposed method relates to existing POMDP solution techniques, such as value iteration, policy iteration, and Monte Carlo tree search. Furthermore, the paper should address the challenges of applying POMDPs to large-scale RLHF problems, such as the curse of dimensionality and the computational cost of solving the POMDP.

### Questions
* Page 3, shall $\mathbb{D}=\mathbb{D}^1\times \mathbb{D}^2\times \cdots \times \mathbb{D}^K$ be $\mathcal{D}=\mathcal{D}^1\times \mathcal{D}^2\times \cdots \times \mathcal{D}^K$?
* Page 3, shall the utility for teacher query cost be $-f^{\beta_t}$ instead of $f^{\beta_t}$?
* There is a question mark at the bottom of Page 3.
* What are the arms in practice?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this work, the author study a hidden bandit model with an option obtain item comparison feedback from a set of expert teacher. There formulation require solving a POMDP which is intrinsically hard to solve in practice so they propose to use a off-the-shelf Monte Carlo planner to obtain an approximate solution to the POMDP problem. Further, they performed experiments on two real world examples of Conference Recommendation and COVID-19 Vaccine testing to demonstrate the effectiveness of their method.

### Strengths
- Proposes an interesting bandit model that combines direct feedback from arms and comparison feedback from experts.
- They conduct several empirical experiments to validate effectiveness of their algorithm.
- They discusses how to infer noise parameter when item utilities are known.

### Weaknesses
1. Notations and problem setup can be significantly improved. The problem clearly seems to be a simpler partially observable bandits problems with additional preference based feedback. But the authors have unnecessarily complicated it to be a POMDP and using a discounted cumulative value. The use of a POMDP framework, while technically applicable, introduces unnecessary complexity. A more direct formulation leveraging the structure of partial observability in bandit problems could lead to a more streamlined analysis and potentially more efficient algorithms. The justification for using a discounted cumulative value is also not clear, as the problem seems to be more naturally framed as a regret minimization problem.
2. There is no discussion about tradeoff between reward obtained from actual arms and cost of querying the teacher. If cost of querying the expert is low, is it ok to just keep querying them to maximize the cumulative return even if does not help learning about the optimal arm? The paper lacks a clear analysis of the exploration-exploitation trade-off, especially concerning the cost of querying the teacher. A crucial aspect missing is a discussion on how the algorithm balances the immediate reward from arm pulls versus the information gain from teacher queries. If the teacher's cost is negligible, the algorithm might over-rely on teacher feedback, hindering the learning process about the actual arm utilities. This could lead to suboptimal performance in the long run.
3. The paper is easy to follow but has bunch of notation issues that can be fixed.  
    a. Rewards and costs have been mixed together.. The cost for teacher should be decreased while utility for arms should be increased. I guess the authors meant to use $1/f^a$ or -$f^a$ as corresponding reward function when querying teacher.  
    b. Typo : $f^{\beta_t}$ is ill defined.  
    c. Formal definition of terms like $\mathcal U^*, \mathcal D^{\mathcal C*}$  is missing.
    d. Figure 3.b, 3.c lack legends.
4. No theoretical guarantee on algorithm is provided.

### Questions
1. In section 3.2 authors assume that $\Delta_{ij}$​’s or $\mathcal U$ is known. In that case, what is there to learn more? The learner can simply estimate the multinomial parameter for each arm and compute the optimal arm.
2. In real world both $\beta$ and $\mathcal U$ would be unknown and has to estimated. How do you intend to handle this?

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
The authors study the problem of reinforcement learning from a set of distinct teachers instead of a single teacher. To solve this problem, the authors develop a hidden utility bandit framework to model the teacher’s rationality and querying cost.  Specifically, this paper proposed an active teacher selection algorithm to decide when and which teacher to choose. Experiments are carried out on the paper recommendation task and the COVID-19 vaccine testing task.

### Strengths
1.	The studied problem is timely and interesting. Current RLHF assumes all the human feedback is collected from a single human teacher instead of a variety of teachers, which is the focus of this paper.
2.	The authors formulate the teacher selection problem in a hidden utility bandit (HUB) framework. Naïve MAB algorithm does not decide when and which teacher to select. The proposed active teacher selection algorithm solves the hub problem by maintaining the belief over the utility function to decide the time and which teacher to query.
3.	Experiments on the paper recommendation and Covid-19 vaccine testing problem demonstrate the effectiveness of the proposed problem.

### Weaknesses
1.	The authors claim that the naïve bandit algorithm does not decide when to query the teachers. However, one simple modification of the naïve bandit algorithm is to add a binary action to decide whether to query the teacher based on the state by extending it to the contextual bandit setting. The authors need to justify the strengths of the proposed algorithm over this simple algorithm.
2.	There is no theoretical guarantee of the regret of the proposed algorithm. 
3.	In the experiments, it’s better to demonstrate the number of query times to show the efficiency of the learning by querying teachers.

### Questions
See the Weaknesses for the questions.

### Soundness
2 fair

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
This paper proposes an approach for selecting the best teacher (annotator) during the process of learning the reward function in a bandit-like setting. The characteristic feature of the setup is that several teachers are available with varying reliability but the same preferences. The authors introduce the problem of Hidden Utility Bandit where there is a choice between drawing an arm and querying the teacher about the utilities of the observations. The authors conduct experimental studies on paper recommendations application and on COVID-19 vaccine testing.

### Strengths
The paper is well written and easy to follow. The goal of the paper is to model the reward learning setup with more realism and to remove the assumption of having a single teacher and it is an important goal. I find the observation about the fact that not the most reliable teacher would be selected all the time (because the odds of the selection from less reliable teachers allow us to estimate the difference in utilities) quite interesting and insightful.

### Weaknesses
My main concern is about the applicability of the assumptions in the problem formulation to the real domains. When introducing HUB formalization, it would be useful to draw parallels with the real applications. This becomes more clear in the experimental studies, but then it seems to be a bit artificial. For example, it seems that there is an assumption that all the teachers have the same utility function (it would be useful if the paper stated all the assumptions of the introduced framework clearly, another one that is not stated clearly is that the space in which the reward is learnt is assumed to be discrete). I am not sure this assumption is suitable for the paper recommendation applications (section 4.1) as it means that everyone has the same preferences. Other examples: it seems that after asking for a preference in recommendation, one needs to wait for a day to propose an article, or the results of vaccine application are observed immediately etc. The studied setting sounds interesting, but so far I am not convinced that problem formulation fits the real applications well. I think in order to be more convincing, it might be useful to find another realistic application for the proposed method, or modify the assumptions of the method to fit the real world applications better.

I think the related literature lacks the literature on selecting the annotators when annotating data for supervised learning in crowdsourcing and active learning (see some examples, but more can be easily found).

F. Rodrigues, F. Pereira, and B. Ribeiro. Gaussian process classification and
active learning with multiple annotators.ICML, 2014.

C. Long, G. Hua, and A. Kapoor. Active visual recognition with expertise estimation
in crowdsourcing. In International Conference on Computer Vision, 2013

K. Murugesan and J. Carbonell. Active learning from peers. In Advances in Neural
Information Processing Systems, 2017

[BOOK] Human-in-the-Loop Machine Learning: Active learning and annotation for human-centered AI 2021

The question of the related literature brings me to the next point. The authors claim that this new problem formulation lacks the baselines in the related literature. However, as the problem has a component of selecting the annotators for crowdsourcing annotation and bandit problem that maximizes the reward, a simple baseline could be to do it in two stages: 1) active teacher selection to learn the reward function, 2) bandit algorithm to maximize the sum of rewards. Would such a baseline be applicable?

After reading the paper, I still have some questions related to the main method. What is the advantage of re-formulating the problem as POMDP (as it still has a single state as a bandit)? How does it relate to the contextual bandit algorithms? The NaiveHUBInference is described in many details, but the proposed method of the paper is very brief and lacks details. I would like to hear more about it. Is the policy learnt on the fly or some prior simulations are needed?

Some minor questions:
- for estimating \beta the authors propose to use a dataset of preferences, however, if such a dataset is available, the reward might be learnt directly and used in the future.
- Information in tables could be made a bit more readable (Figure 2 and 7)
- RLHF term in the title is confusing. The focus of the paper is on rewards learning, and it could be better reflected in the title.

### Questions
I would like to hear from the authors regarding my concerns on the applicability of the method assumptions to real problem domains, how the method related to the annotator selection in crowdsourcing literature and if comparison to such a method is applicable.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
