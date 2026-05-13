# Learning Actionable Counterfactual Explanations in Large State Spaces

- Decision: Reject
- Scores: 5, 6, 1, 5

## Abstract
Counterfactual explanations (CFEs) are sets of actions that an agent with a negative classification could take to achieve a (desired) positive classification, for consequential decisions such as loan applications, hiring, admissions, etc.  In this work, we consider settings where optimal CFEs correspond to solutions of weighted set cover problems.  In particular, there is a collection of actions that agents can perform that each have their own cost and each provide the agent with different sets of capabilities. The agent wants to perform the cheapest subset of actions that together provide all the needed capabilities to achieve a positive classification.  Since this is an NP-hard optimization problem, we are interested in the question: can we, from training data (instances of agents and their optimal CFEs) learn a CFE generator that will quickly provide optimal sets of actions for new agents?

In this work, we provide a deep-network learning procedure that we show experimentally is able to achieve strong performance at this task.  We consider several problem formulations, including formulations in which the underlying ``capabilities'' and effects of actions are not explicitly provided, and so there is an informational challenge in addition to the computational challenge.  Our problem can also be viewed as one of learning an optimal policy in a family of large but deterministic Markov Decision Processes (MDPs).

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes three high-level data-driven CFE generators: hl-continuous uses ILP to find the least costly set of continuous actions to change an individual's status; hl-discrete selects from discrete actions by solving a set cover problem; hl-id assigns a label to provide general recommendations without specific actions for cases where information aren’t accessible. The datasets include real-world health, some semi-synthetic and fully synthetic datasets.

### Strengths
- The paper provides a comprehensive analysis across diverse feature types, different dataset dimensions, and varying CFE frequencies. It also discuss fairness.
- The proposed methods are model-agnostic. So it can be adapted to different models.

### Weaknesses
 - This paper is limited to binary classification.
- Equation (2) presumes a linear classifier, which may not represent the complexity of real-world models. This simplification could restrict the performance and generalizability of the proposed methods. Specifically, the use of a linear classifier to derive the parameters for the Integer Linear Program (ILP) may not accurately capture the decision boundaries of more complex non-linear models, leading to suboptimal counterfactual explanations. The reliance on pre-defined parameters, such as classifier coefficients and thresholds, may reduce the flexibility and accuracy of the approach across diverse datasets. These parameters are not directly derived from the data, potentially leading to counterfactual explanations that do not align well with actual case. The paper also does not include a sensitivity analysis of the pre-defined parameters.
- The study does not compare the proposed methods against other CFEs (only low-level CFE).

### Questions
I have a few questions that I’m still trying to fully understand. I would greatly appreciate any clarification you could provide on the following points:

- Why are these approaches considered "high-level"? Adjusting multiple feature combinations is not a new idea, so I’m curious about what uniquely qualifies these methods as high-level.
- How does the method handle datasets with both discrete and continuous actions?
- How are the pre-defined parameters, such as c and b, chosen? Since these parameters are not derived directly from the data, what guidelines or expertise inform their selection? Additionally, would the model’s performance benefit from dynamically adjusting these parameters based on the dataset, and is there a sensitivity analysis to evaluate how variations in bb might impact the results?

### Soundness
2

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
5

### Summary
In this paper, the author proposes an algorithm for generating high-level counterfactual explanations (CFs). Rather than modifying individual features, the approach involves modifying groups of features simultaneously. The task is formulated as an integer linear program to obtain an optimal solution. Three different versions of the algorithm are presented for generating CFs.

### Strengths
Strength:
1 The topic is quite interesting. 
2 The algorithm is concise and several case studies are provided.
3 The paper is well presented.

### Weaknesses
1 The motivation is unclear. From my understanding, they aim to define a high-level action to identify counterfactual explanations. However, they do not clearly explain why this high-level action is suitable for users to act upon. Additionally, they should clarify how these actions are identified.
2 The paper lacks a theoretical guarantee to demonstrate the efficiency of the proposed algorithm.
3 The proposed algorithms overlook the practicality of the generated counterfactual explanations (CFs).
4In Formula 2, the linear integer program (LIP) could be very time-consuming when the action space is large. They did not explain how to constrain the action space.

### Questions
They mention that previous methods have high computational complexity, impacting scalability. Could you clarify how your proposed algorithm addresses this issue?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper proposes to provide higher-level actions as CFEs to individuals who have received undesirable predictions from a classifier, instead of low-level CFEs that most previous techniques provide. The authors claim that higher-level CFEs are sparser, make more improvement to an individual, are diverse, more fair and personalized.

### Strengths
The paper proposes to tackle an interesting problem of providing higher level actions, that might make it easier to communicate actionable changes to a user

### Weaknesses
The paper suffers from several weaknesses. I have enumerated them below, and marked the ones that are major. If the authors like, they can only focus on the major weaknesses:

1. [Major] The paper's motivation states that their proposed technique will be useful in cases when an individual does not have access to the priviledged information such as the ability to query the classifier. Now the entire proposed technique hinges on the ability to generate CFEs for all individuals and then train another model on that top of that? So how is an individual who does have access to a classifier use this technique when the pre-requisite of the technique is to generate CFEs not for 1 just thousands of individuals and then use the technique to do something for that individual? The proposed technique does not need less privilege than having access to the classifier, in facts it requires a 1000X more priviledge, the ability to generate CFEs for thousands of individuals. So the question is how is your technique applicable for an individual who does have access to a classifier as claimed in your motivation? 
Could the authors explain how their method would be deployed in a real-world setting where individual users lack access to the classifier? Who would be responsible for generating the initial dataset of CFEs, and how would this be done with the restrictions the paper aims to address? 

2. in line 152 you mention there are 4 notable limitations of low-level CFEs. There are no references to show that these limitations are indeed "notable".

3. In line 154 you say: solving this problem is computationally expensive as it is NP-hard optimization for each new agent. What is an agent? Please define it. Also in practice this optimization is quite cheap, fast, and scalable. See the dozens of the papers cited in Verma et al 2020.

4. In line 157, you say that "each action modifies an individual feature" -- that is not true for most causality based CFE generation techniques, like Consequence-aware sequential counterfactual generation, Geco: Quality counterfactual explanations in real time, Amortized generation of sequential algorithmic recourses for black-box models.

5. [Major] Given example of a situation where a CFE providing organization would not have access to the underlying classifier. Usually CFEs are provided for financial situations like loans and credit cards, and the banks are supposed to provide CFEs. In this case, the banks have access to their own models. Your current example of a dietician and celiac **does not** do a good job, celiac classification is a very simple rule based thing and the advice (CFE as you say) is known to all the physicians. No body uses a complex model that makes a decision that nobody understands (due to it being a black-box model) and therefore you need a CFE. Could the authors provide a more relevant example, perhaps from domains like algorithmic hiring or credit scoring, where the decision-making process is less transparent and the need for actionable explanations is more apparent?

6. [Major] Is Hl-discrete not the same as HL_continuous with just binary weights on the features? Is that is the case, then why do you make it as a separate case, its just a special case of HL_continuous, does not need that much attention and focus in the paper.

7. The HL-ID suggestions are generic and not useful, it is like a banker suggesting to a person whose loan request is canceled to increase their credit score or their bank balance -- everybody knows that. The point of a CFE is to provide a specific and small changes that are easily achievable, not generic advice.

8. [Major] Line 258 Please define what you mean by the symbol individual -> CFE dataset. From what I understand this is a dataset of individuals and their corresponding CFEs (which you never mention how you computed)

9. [Really Major] What is the job of the neural networks you train in section 4.2? From what I understand you first gather this dataset of individuals and CFEs, then somehow you get the actions for HL-continuous (mentioned on line 322-323) and then you use these actions to generate CFEs for new individuals? If this is the case, then what do you need the neural networks for, you can just use ILP to do this as stated in Section 3.1. The experimental section is really badly written and I did not understand the motivation of what you are doing at all. Please rewrite the section stating why you did something before telling what you did and even before that show the full pipeline of what you plan to do (ideally in a figure). Could the authors provide a clear, step-by-step explanation of their method's pipeline, including:

**a)** How the initial dataset of individuals and CFEs is generated
**b)** The specific role of neural networks in the process
**c)** How this approach differs from or improves upon using ILP directly
**d)** A diagram illustrating the full pipeline from data generation to CFE prediction for new individuals

10. [Major] Where do you magically get the actions to use in HL-continuous (or discrete) you mention in line 322?

11. Please explain the job of neural networks in HL-ID CFE generator? In this case you don't even have access to the classifier, so what loss are you optimizing over? You don't even know if the actions you propose will do anything to change the prediction of the classifier (because of the setting)

12. The assumptions and statements in the experimental results section 5.1 are either unsupported or obvious:
      1. Line 362: sparsity might be undesirable and challenging because individuals aim to implement as many changes as possible: No this is not true at all, in case of CFEs individuals want to just change the classifier prediction and want to implement as **less** changes as possible to get it. Your examples of health are invalid because nobody uses a complex neural network classifier to classify if someone is unhealthy and healthy, and your goal is not to change the prediction of the classifier, but to become healthy. And therefore in a health example you want to implement a lot of changes, not in the case of a usual CFE like a financial situation. 

       2. Line 372: Despite hl-continuous CFEs having fewer actions on average, they result in more feature changes: This is **really obvious** in your case. You are just clubbing multiple changes to several features and calling that one action. I could define one action that changes all features and that final datapoint is classifier as positive by the classifier. So then I can say my proposed techniques just requires 1 action and this action changes all the features and achieves 100% success rate. I don't think that is useful. 

      3. Line 404: Additionally, on average, hl-continuous CFEs, with fewer actions (∼ 2) result in states that are more distant: This is also **obvious**. If your actions make large changes in features, it is obvious that the new datapoint will be more distant. 

       4. Line 409: hl-continuous CFEs tend to be more desirable for decision-makers and individuals alike: how can you claim this? Did you do a user study or even any automated metric to show this? I don't think this is true. 

13. Line 390: What does "having a higher CFEs frequency" mean? What is CFEs frequency?

### Questions
All my questions are written in the weakness section. Overall, the authors really need to convince that their technique is usuable at all (because currently it seems it is not -- one needs to have access to thousands of CFEs to use this technique) and write the section on how to actually use the technique (section 3.2 and 4.1 need to be explained much more better with a motivation for each part)

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors identify limitations in traditional low-level counterfactual explanation (CFE) generators and propose an alternative approach involving three data-driven counterfactual generators. These generators are trained with high-level CFEs, which consist of combinations of high-level actions, where each action can alter multiple features. The high-level counterfactuals are defined as follows: (1) hl-continuous CFE, representing the lowest-cost subset of hl-continuous actions that can achieve recourse (either by addition or subtraction of the feature changes that correspond to each action); (2) hl-discrete CFE, which is formulated as a minimum weight set cover problem using hl-discrete actions (limited to the positive feature changes that correspond to each action); and (3) hl-id, for which the exact cost and the resulting feature changes are unknown. For (1) and (2) once the counterfactuals are defined, an integer linear programming (ILP) solution is applied to each instance, creating a training dataset consisting of (X, CFE) pairs. The generators are trained with these datasets.

### Strengths
1. Once the generator is trained, the counterfactual explanation (CFE) prediction is very efficient. With proper training and a high-quality dataset, the generator can achieve high accuracy in its results.
2. If a predefined set of actions is available, generating counterfactuals for subgroups can be more straightforward.
3. The proposed approach enables fairness auditing in a more structured and systematic manner.

### Weaknesses
1. Training the generator requires solving integer linear programming (ILP) problems, which are specifically suited for linear classifiers. For other types of classifiers, creating the dataset necessitates brute-force methods, which may not be efficient. Furthermore, the reliance on ILP for generating the training data introduces a significant limitation, as it restricts the applicability of the proposed method to scenarios where the underlying decision model can be effectively approximated by a linear function. This raises concerns about the generalizability of the approach to more complex, non-linear models commonly encountered in real-world applications. The computational cost of generating the training data via brute-force methods for non-linear models also needs to be addressed, as it could render the approach impractical for large datasets or complex models.
2. The hl-discrete CFEs are limited to positive changes, which may not apply to non-linear models. Even for linear models, this approach requires additional preprocessing and a deeper understanding of the model's internal. The limitation to positive changes is particularly concerning, as it may not be possible to achieve recourse by only increasing feature values. This constraint significantly restricts the solution space and may lead to suboptimal or infeasible counterfactual explanations. Moreover, the need for additional preprocessing and a deep understanding of the model's internals to apply this approach adds complexity and reduces its usability.
3. The hl-continuous and hl-discrete generators still rely on query access to the model and the cost of actions to create the training set, meaning that these requirements are not fully eliminated. The reliance on query access to the model is a significant drawback, as it limits the applicability of the method in scenarios where the model is not readily accessible or when the cost of querying the model is prohibitive. The need for cost information for actions further restricts the method's applicability, as this information may not always be available or accurate.
4. For the hl-id generator, the challenge remains in how to construct the training dataset, as the process is not clearly defined. The lack of a clear and well-defined process for constructing the training dataset for the hl-id generator is a major concern. The absence of a systematic approach raises questions about the reliability and reproducibility of the results obtained using this generator.

### Questions
1. Consider introducing the notion of high-level actions at the beginning of the introduction, defining them as combinations of low-level actions.
2. Why are hl-continuous counterfactuals considered superior to low-level counterfactuals? While having a predefined set of high-level actions with known outcomes can simplify the CFE generation process and facilitate testing, the feasibility of combining actions may not always be straightforward, and the constraints could be more complex. Have you tested your approach on more complex datasets with additional constraints to demonstrate its effectiveness?
3. For the ILP in Definition 2 (line 196), the condition $\epsilon_j\leq a_j$ appears to be redundant. If $a_j=0$ then $e_j$ has no effect, and if $a_j=1$ this condition always holds since both $\epsilon_j$ and $a_j$ are in $\{0,1\}$. Additionally, there seems to be a typo on the same line, where $\epsilon_i$ should be $\epsilon_j$.
4. Could you clarify the need for hl-discrete actions? It seems unnatural to limit changes to only "positive changes." Moreover, since the focus is on binary features, isn't this approach overly restrictive in your experiments, where $t = 1$ means targeting a specific state?
5. For the ILP in Definition 4, the constraint on line 220 should be written as $\sum_{j\in J}d_{ji}a_j +x_{i} \geq t_i$.
6. Could you clarify how the generators produce "generalizable CFEs" (line 52)
7. Regarding Figure 2 (a) Comparing actions may not be meaningful, as a high-level action can modify multiple features simultaneously, whereas a low-level action changes only one feature (also stated on line 356). (b) In the bibliography, the number of features changed is important for explainability. You should emphasize that, in the case of high-level actions, having more feature changes does not necessarily reduce explainability. (c) a more distant state does not necessarily indicate a higher improvement. Since most ML models used for generating CFEs are non-linear, the concept of CFEs is inherently linked to minimizing cost. Thus, the goal of a CFE generator should not be maximizing improvement, which contradicts the problem being addressed. (d) Higher frequency is expected because the actions are predefined, resulting in more "global" CFEs. (General comment:) It would be beneficial to include variance or standard deviation in the figures for a more comprehensive analysis.
8. In line 367, you mention "diverse improvements." Could you clarify what you mean by this?

### Soundness
2

### Presentation
3

### Contribution
2
