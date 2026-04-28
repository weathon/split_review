# A Dynamic Model of Performative Human-ML Collaboration: Theory and Empirical Evidence

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5

## Abstract
Machine learning (ML) models are increasingly used in various applications, from recommendation systems in e-commerce to diagnosis prediction in healthcare. 
In this paper, we present a novel dynamic framework for thinking about the deployment of ML models in a performative, human-ML collaborative system. In our framework, the introduction of ML recommendations changes the data-generating process of human decisions, which are only a proxy to the ground truth and which are then used to train future versions of the model. We show that this dynamic process in principle can converge to different stable points, i.e. where the ML model and the Human+ML system have the same performance. Some of these stable points are suboptimal with respect to the actual ground truth. As a proof of concept, we conduct an empirical user study with 1,408 participants. In the study, humans solve instances of the knapsack problem with the help of machine learning predictions of varying performance. This is an ideal setting because we can identify the actual ground truth, and evaluate the performance of human decisions supported by ML recommendations. We find that for many levels of ML performance, humans can improve upon the ML predictions. We also find that the improvement could be even higher if humans rationally followed the ML recommendations. Finally, we test whether monetary incentives can increase the quality of human decisions, but we fail to find any positive effect. Using our empirical data to approximate our collaborative system suggests that the learning process would dynamically reach an equilibrium performance that is around 92\% of the maximum knapsack value. Our results have practical implications for the deployment of ML models in contexts where human decisions may deviate from the indisputable ground truth.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
* This paper examines Human-ML collaboration under performative prediction settings through theoretical analysis and an empirical experiment on ML-assisted combinatorial knapsack problems.
* In the setup, users interact with a predictive system in discrete time steps. At each time step $t$, a model $M_t$ predicts a label $Y_{M_t}$ based on features $X$. This prediction serves as decision support for a human decision-maker, who then makes their own prediction $Y_{H_t}$​​. Pairs $(X,Y_{H_t})$ are used to train the subsequent model $M_{t+1}$, and it is assumed that $M_{t+1}$​ perfectly aligns with its training distribution. Definition 1 introduces utility $\mathbb{U}(X, Y)$ for prediction-label pairs, defining its properties axiomatically. It then defines a the collaborative characteristic function which captures one-step utility improvement, and $\\mathbb{L}_{\\Delta\\mathbb{U}}(s,t)$ as the trajectory of expected utilities for a system whose initial utility is $s$. Propositions 1 and 2 show that utility trajectories converge under monotonicity assumptions.
* The empirical section evaluates the impact of model-based advice on human solutions for the 0-1 knapsack problem. Human participants interact with an ML-supported system to solve knapsack problems, possibly receiving predictions of the optimal solution. Six models with varying accuracy were trained before the experiment using synthetic optimal solutions, and each experimental group received distinct models and possibly different monetary incentives. Results indicate that incentivization schemes had no significant impact on solution quality, while decision-support quality correlated with human solution quality. Collaborative learning trajectories were presented based on these results.

### Strengths
* The paper addresses a well-motivated topic.
* The empirical analysis is grounded in data from real human subjects.
* Results seem to provide interesting insights into ML-assisted decision-making contexts.

### Weaknesses
 * The paper claims to provide an empirical evaluation of performative prediction but seems to lack essential elements of this setup. Specifically, prediction models were trained on synthetic data before the experiment, and the experiment does not include "feedback loops" which are a defining component of performative prediction. The absence of iterative model retraining based on human feedback fundamentally limits the study's ability to capture the dynamics of performative prediction, where model outputs influence future training data and model behavior.
* The theoretical analysis applies to a limited form of performative prediction, assuming that utility trajectories are determined solely by population-wide average utility, without taking the structure of the predictor into account. Functions like the collaborative learning path are interesting, it is not clear whether the definition are applicable in more general scenarios. The assumption that the system's trajectory is solely determined by average utility, without considering the specific characteristics of the model or the human decision-maker, is a significant limitation. This simplification may not hold in real-world scenarios where individual model biases and human decision-making heuristics can significantly affect the system's evolution.
* The empirical approach uses an atypical learning task: predicting a binary solution vector for a combinatorial 0-1 knapsack problem based on random synthetic instances and optimal solutions. The paper notes a possible analogy to multi-task classification, but it’s unclear how results extend to conventional ML tasks on non-synthetic data. The use of a combinatorial optimization problem, while having some interesting properties, makes it difficult to generalize the findings to more common machine learning tasks such as image classification or natural language processing, where the data and model characteristics are very different.

### Questions
* When are the conditions in Definition 1 expected to hold? Examples of suitable utility functions in binary classification and scalar regression can be very helpful.
* Could notation in eq. (1) be clarified? Specifically, $Y_{H_{t-1}}$ seems to appear both as an argument of the function, and as a variable sampled from $D_{t-1}$.
* How was Appendix Figure 6 (L403) generated?
* In the theoretical analysis, how would results change if the training set in each step was finite?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the dynamic model of performative human-ml collaboration from both theoretical and empirical perspectives. The paper introduces the notion, the Collaborative Characteristic Function which connect the predicted label and the unknown ground truth. The paper does some empirical study that involves real human on the knapsack problems. Experimental results show that human tend to improve the model's performance, and human may submit worse results than the prediction by models.

### Strengths
Originality: A substantive assessment of the strengths of the paper, touching on each of the following dimensions: originality, quality, clarity, and significance.
Quality: The paper is supported by a robust empirical study involving 1,408 participants working on the knapsack problem. The statistical analyses performed provide strong support for the conclusions drawn, particularly regarding human improvements over ML predictions. Additionally, the paper critically examines the impact of monetary incentives on decision quality, contributing valuable insights to the field.
Clarity: The paper's motivation and conclusion are clear.
Significance: The paper gives some suggestions about  the consideration of human behavior and the selection of the dataset to train the model.

### Weaknesses
1.Abstractness of Problem Domains: The study does not focus on specific classification or regression tasks, which makes the findings somewhat abstract. A more concrete application, such as image classification or natural language processing tasks, would enhance the practical relevance of the research. The current approach makes it difficult to assess the generalizability of the findings to real-world machine learning problems.
2.Limited Application Scope: The research primarily concentrates on the knapsack problem, neglecting more realistic scenarios, such as medical diagnosis or financial forecasting. Exploring applications in critical areas like healthcare, where the consequences of suboptimal decisions are significant, would significantly increase the paper's impact and relevance. The knapsack problem, while useful for initial study, lacks the complexity and nuance of real-world decision-making environments.
3.Participant Preference Variability: While the study involves 1,408 participants, it lacks a detailed analysis of their preference differences. Understanding how individual preferences, such as risk aversion or cognitive biases, might affect decision-making is essential, as these variations could lead to suboptimal choices in certain instances. A deeper investigation into the heterogeneity of human decision-making processes is needed.
4.Simulation of Human Behavior: Beyond conducting real experiments with participants, the paper does not explore the potential for simulating human behavior. Employing simulations, perhaps using cognitive models or reinforcement learning agents trained on human data, could reduce the costs associated with extensive human experimentation while still providing valuable insights into collaborative decision-making dynamics. Such simulations could also allow for the exploration of a wider range of scenarios and parameters.

### Questions
Can the author open-source the dataset provided by real human?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper primarily presents a new dynamic framework for thinking about the deployment of ML models in performative human-ML collaborative systems, helping to understand how ML influences human decision-making processes. This research is intriguing and has practical value.

### Strengths
This paper has several strengths, as follows:
1.	A new dynamic framework is proposed for considering the deployment of ML models in human-ML collaborative systems.
2.	The involvement of participants in real-world scenarios enhances the credibility of the research. The design of the empirical study allows for clear identification of the actual ground truth, providing evidence for the research results.
3.	The findings of the paper have practical significance, aiding companies in optimizing the training and deployment strategies of ML models.

### Weaknesses
1. The paper is hard to follow, the complexity may make it difficult for readers to understand.
2. The research focuses primarily on the knapsack problem scenario, which may limit the generalizability of the results. It is recommended that the authors consider validation in different types of problems to enhance applicability. Specifically, the current study does not explore the impact of varying problem structures on the collaborative characteristic function. This is a significant limitation, as the knapsack problem has a very specific structure that may not be representative of other decision-making scenarios. For example, problems with continuous decision spaces or those involving complex dependencies between variables might exhibit different collaborative dynamics. The authors should consider how their framework would apply to such scenarios.
3. The paper mentions the failure to find a positive impact of incentive mechanisms on human decision quality, and the explanation for this phenomenon is insufficient, leading to a superficial discussion of the incentive mechanisms without exploring their potential reasons. The discussion lacks a deeper analysis of why the incentives failed to produce the expected results. For instance, the authors do not explore whether the incentive structure was properly understood by the participants, or if the magnitude of the incentives was sufficient to motivate a change in behavior. Furthermore, the paper does not consider the possibility of other factors, such as cognitive load or task complexity, that might have influenced the participants' responses to the incentives.


### Questions
1.	The paper initially presents that current human-ML collaborative systems face three crucial challenges, but the subsequent text does not detail the innovations made in addressing or alleviates these three issues. I hope to see a clear exploration of how the paper addresses or alleviates each of these challenges in the introduction.
2.	A deeper discussion on incentive mechanisms: Provide more discussion on the ineffectiveness of incentive mechanisms to help readers understand the potential reasons of this phenomenon.
3.	The contributions are trivial, making readers difficult to understand the key points of this paper. I hope the author can rewrite their contributions.
4.	In Definition 1, the definitions of Ymin and Y' are not specified. In Defination 5, the definition of x1…xn  should be placed in the main text.

### Soundness
2

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
This paper presents a theoretical framework for describing the collaboration process between ML models and human decision-making. By defining a utility function and a collaborative characteristic function, it gives a sufficient condition for achieving a stable point in the optimal case. Additionally, an empirical experiment with real users offers interesting insights into practical applications.

### Strengths
1. The studied problem is important. Developing a collaborative system that integrates ML models with human decision-making to consistently achieve better outcomes is both a valuable and challenging topic for academia and industry.
2. A theoretical framework is proposed to describe the collaboration process and quantify the quality of solutions from both models and humans. A sufficient condition, which ensures non-decreasing utility, is provided to guarantee the achievement of a stable point.
3. An empirical experiment was conducted with real users, offering interesting insights into practical applications.

### Weaknesses
1.	The theoretical framework primarily aims to describe the problem. Both the theory and convergence conditions rely on acquiring the utility function, which seems to be merely achievable with the knowledge of the ground truth. However, as discussed in Introduction and Related Works, a key intuition of this paper is addressing the inaccessibility of ground truth in real-world scenarios. Consequently, the theory offers limited insights at the methodological level. Specifically, the assumption that a utility function can be defined and, more critically, *known* for both the ML model and the human decision-maker, is highly unrealistic in practical settings. This reliance on a known utility function undermines the practical applicability of the theoretical results, as it is precisely this function that is unknown in most real-world scenarios where collaborative decision-making is needed.
2.	Several expressions and derivations are unclear and lack rigor. E.g., it seems that $\delta_{M_t}$ in Eq. (3) should be determined jointly by ${M_t}$and $X$. In Definition 3 and Proof A.6, $U(H(X, Y_{M_t}))$ should be instead be written as  $U(X, H(X, Y_{M_t}))$ instead. Additionally, the logic behind the proof of Proposition 1 is unclear, particularly why $E_{x \in \mathcal{X}}(U(Y_{M_{t+1})}=0)$ holds. And Observation 2 is also confusing. Why should the absolute difference in distance measures equate to the difference in utilities? The lack of clarity in these mathematical formulations and proofs significantly weakens the theoretical contribution of the paper. The notation is inconsistent, and the assumptions behind key steps are not well-justified, making it difficult to follow the logic and assess the validity of the claims.
3.	The authors devote substantial space to describing the experiment and results related to monetary incentives. However, since these are empirical observations of a single confounding factor in a specific scenario, they provide limited insight and generalizability from a broader perspective. The study focuses on a very narrow context, and the results are heavily dependent on the specific experimental setup and the particular user population. The insights gained from this experiment are not easily transferable to other collaborative decision-making scenarios, limiting the broader impact of the empirical findings.

### Questions
All my questions are listed in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2
