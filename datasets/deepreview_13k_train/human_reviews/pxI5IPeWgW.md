# ODE Discovery for Longitudinal Heterogeneous Treatment Effects Inference

- Decision: Accept
- Scores: 8, 8, 5, 8, 5

## Abstract
Inferring unbiased treatment effects has received widespread attention in the machine learning community.
In recent years, our community has proposed numerous solutions in standard settings, high-dimensional treatment settings, and even longitudinal settings.
While very diverse, the solution has mostly relied on neural networks for inference and simultaneous correction of assignment bias.
New approaches typically build on top of previous approaches by proposing new (or refined) architectures and learning algorithms. 
However, the end result---a neural-network-based inference machine---remains unchallenged.
In this paper, we introduce a different type of solution in the longitudinal setting: a closed-form ordinary differential equation (ODE).
While we still rely on continuous optimization to learn an ODE, the resulting inference machine is no longer a neural network.
Doing so yields several advantages such as interpretability, irregular sampling, and a different set of identification assumptions. 
Above all, we consider the introduction of a completely new {\it type} of solution to be our most important contribution as it may spark entirely new innovations in treatment effects in general.
We facilitate this by formulating our contribution as a framework that can transform any ODE discovery method into a treatment effects method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the Individualized Nonlinear Sparse Identification Treatment Effect (INSITE) framework for estimating heterogeneous time-varying treatment effects given dynamic and statist covariates. INSITE leverages deterministic ODE discovery methods to infer the population differential equation, which is fine-tuned to recover patient-specific differential equations. Experimental results on two synthetic datasets demonstrate that INSITE is competitive in counterfactual prediction relative to baselines.

### Strengths
- The paper outlines a comprehensive framework for leveraging ODE discovery methods in time-varying treatments/covariates setup
- The paper is relatively well-written and easy to follow
- Experimental results demonstrate that the proposed approach is competitive relative to baselines
- The learned ODES are interpretable, unlike previously proposed neural network approaches

### Weaknesses
 - I encourage the authors to include a discussion section focused on the limitations of the proposed approach. The paper makes strong assumptions about the underlying dynamics, e.g., 
1) The success of the INSITE is dependent on the choice of the library of candidate functions. Specifically, if the true underlying dynamics are not well represented by the chosen library, the method will likely fail to identify the correct equations. For example, if the true dynamics involve a term like $x^3$ and the library only includes terms up to $x^2$, the method will not be able to recover the correct model.
2) INSITE assumes that the system is sparse, which rarely holds in high-dimensional settings. In many real-world systems, especially those with many interacting components, the governing equations may involve a large number of terms. Forcing sparsity in these cases could lead to an oversimplified model that does not accurately capture the true dynamics.
3) INSITE assumes that the system is deterministic and noise-free. However, real-world systems often have noise and other stochastic elements, which can significantly affect the model's accuracy. The presence of noise can lead to inaccurate parameter estimation and potentially incorrect model identification. Furthermore, the deterministic assumption neglects the inherent variability in many real-world processes.
- I encourage the authors to include a complete description of how INSITE handles different treatment types (categorical and continuous ). Given that this setup is distinct from the previous ODE discovery methods, complete details should be provided in the main paper

**Underwhelming Experiments**
- While the paper claims to handle irregularly sampled data, which is typical in real-world settings (i.e., patient covariates are not measured continuously over time), the synthetic experiments don't seem to explore this scenario. The experiments use evenly spaced time points, which does not reflect the challenges of real-world data with missing or irregularly spaced observations.
- The synthetic experiments are too simplistic, $g(x)$ is an identity function, $x$ is 1-dimensional. I encourage the authors to explore more challenging scenarios, including semi-synthetic datasets. The use of an identity function for $g(x)$ makes the problem too easy, and the 1-dimensional state space does not reflect the complexity of real-world systems. More complex observation functions and higher-dimensional state spaces should be considered.

### Questions
- For the BSV scenario A (eqns 5 and 6), shouldn't we expect ODE methods to do as well as INSITE
- Fig 3(b): Shouldn't we expect INSITE to be monotonically increasing with $\gamma$

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies longitudal treatment effect estimation from a new prospective, using ordinary differential equation (ODE). This potentially opens up a new paradigm of treatment effect estimation methods that does not rely on neural network. The ODE approach naturally offers interpretability and requires slightly different assumptions for identification. The authors first discussed the difference and similarities between longitudal treatment effect estimation and ODE, then proposed a framework for bridging the problem and solution. The proposed framework is then compared with several neural network based longitudal effect estimators.

### Strengths
1. The ODE perspective is very novel for longitudal treatment effect estimation.
2. The paper is well-written and well-organized, with extensive additional information for reproducibility.
3. The ODE framework can relax the overlap assumption in causal effect estimation.

### Weaknesses
1. There seems to lack a formal identification result in terms of identifying the causal effects from the ODE perspective.
2. The experiments are conducted on synthetic datasets only. Results on real-world datasets could further strengthen the evaluation.

3. There is a lack of clarity regarding the "strong assumptions" required by the framework. The statement "Unique to the proposed framework and INSITE, is that the discovered differential equation is fully interpretable; however, it relies on strong assumption" needs further elaboration. It's unclear what these assumptions are and how they might limit the applicability of the method.

4. The data generation process in the synthetic benchmark in Eq 5 seems to closely follow with the ODE assumption in Eq 3, raising concerns about the generalizability of the results. Specifically, the close alignment between the data generation and the model assumption might lead to overly optimistic performance estimates. It is necessary to see how the method performs when the data is generated in a way that violates the ODE assumptions.

### Questions
What are the "strong assumptions" mentioned in this statement? " Unique to the proposed framework and INSITE, is that the discovered
differential equation is fully interpretable; however, it relies on strong assumption"

The data generation process in the synthetic benchmark in Eq 5 seems to closely follow with the ODE assumption in Eq 3, is there experiment results when such the data is generated in different ways?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a framework that can transform any ODE discovery method into a treatment effects method. This involves reformulating the longitudinal heterogeneous treatment effects problem as an ODE discovery problem, with the goal of recovering the underlying system of ODEs based on observed datasets. A proposed model called INSITE (section 5) is built using this framework and tested in accepted benchmark settings.

### Strengths
- The exposition of the method is quite clear. The proposed INSITE framework is very flexible, as it can be used on top of many other time varying TE methods.

- It's reasonable and natural to model this treatment effect over time problem as a dynamical system with ODEs representation. This research brings together two previously separated fields, i.e., temporal TE estimation and ODE discovery, which set up a bridge for these communities.

- The experimental simulation, especially in the appendix, is comprehensive and appears to be reproducible for me.

### Weaknesses
1. The presentation of this paper, such as the related work, should be further improved before acceptance. e.g., the $T$ appears at section 2 but is introduced in section 3 ("is called the time horizon"). Another example is ODE discovery paragraph in B.1; I didn't understand why RNN and LSTM are considered ODE discovery methods. The connection between the described method and Neural ODEs, a more relevant class of models, is not clearly established, which weakens the motivation for the proposed approach.

2. Compared to existing black-box TE methods (like neural-network based architectures), the authors claim that the main contribution of this work is a human-readable, interpretable framework. But if the current form of the manuscript only offers empirical validation, I feel that its contributions might not yet meet the threshold of ICLR conf. I wonder that have authors investigated the inherent theoretical properties of the ODE-based framework (which is a white-box model compared to deep network)? e.g., for certain nonlinear differential equations, the solution might be chaotic, meaning it's highly sensitive to initial conditions $\boldsymbol{x}_0, \boldsymbol{v}$ and treatment plan $\boldsymbol{a}$ at $t_0$. The paper lacks a discussion on the stability of the discovered ODEs and how this impacts the reliability of treatment effect predictions, especially in long-term scenarios. Furthermore, the identifiability of the ODE parameters given the observed data is not addressed, which is crucial for the interpretability claim.

3. Given the claimed emphasis on 'human-readability', how does the proposed method facilitate better decision-making or insights for practitioners in the field is still unclear. Addressing these concerns with more discussions on closed-form ODE would further enhance this work. The paper does not provide concrete examples of how the discovered ODEs can be used to inform treatment decisions or provide insights into the underlying mechanisms of treatment effects. The practical utility of the framework beyond empirical validation remains unclear.

4. Minor issues don't affect the rating:

- page 8: $\gamma = 0$ corresponds no time-dependent -> add 'to' for consistency

- Table 5: word 'Intrepetible' -> 'Interpretable'

- there's one paragraph exceeds the 9 pages limit of the main body

- the full name of ODE/ODEs appears many times in the text, which seems unnecessary

### Questions
- The assumption 3.1 is not only about existence and uniqueness (these are very mild assumptions and acceptable), but also about the continuous trajectory. I wonder if this is too strict and it may limit the scope of application for the method you've proposed. Could it be relaxed to weaker conditions, such as piecewise continuity? As time changes, different patterns of $\boldsymbol{x}(t)$ may emerge over the interval from $t_0$ to $T$.

- In practice, what method do you use for solving ODEs? How about the complexity of gradient query / solving for this numerical system? Is your method faster than the neural network-based approaches?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author investigated longitudinal treatment effect estimation from the perspective of ODE discovery. They introduced a framework capable of converting any ODE discovery method into a treatment effect estimation approach. They explored the distinctions between ODE discovery and treatment effect estimation. Furthermore, they presented a versatile solution capable of accommodating both continuous and categorical treatments. Importantly, their method yields interpretable equations, a crucial requirement in the healthcare field.

### Strengths
- Method offers interpretable solutions for better understanding.
- Handles various treatments through defined continuous or piecewise equations.
- Applicable for estimating treatment effects at both population and individual levels.
- Manages diverse between-subjects variability effectively.
- Yields improved results even in cases of model misspecification.

### Weaknesses
 - Determining the correct form of ODE is highly challenging.
- The discussion lacks guidance on learning a feature library, a crucial aspect for this method.
-Assuming y=x poses the question: what if this assumption is invalid? Would ODE or neural networks be more appropriate to model the outcome function? How might this framework integrate with a neural network or other machine learning techniques as g function for the outcome?

### Questions
Is it possible to combine any feature learning method within this framework to acquire the necessary dictionary? My primary concern revolves around the challenge of determining the equation's form.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to solve a task of ODE discovery in the treatment effect estimation setting. Although the task is not sufficiently explained in the main paper, I believe it is to construct an ODE model with simple expressions (e.g., log, exp, sin) from time series data at continuous time stamps. Thus, the paper seems to tackle a novel task. However, it is completely unclear because the motivation is not sufficiently described, the paper is not well structured, the problem setting is not clearly presented, and many important descriptions are moved to Appendix.

### Strengths
- Introducing the ODE discovery in the context of treatment effect estimation seems novel.

### Weaknesses
### weaknesses:
 (A) Problem setting is unclear

- First of all, in Section 1, please clearly state that what the ODE discovery task is and what its goal is. The current description does not sufficiently explain how finding an ODE model relates to interpretability. For example, the paper should explicitly state that the goal is to find underlying closed-form concise ODEs from observed trajectories and explain how these transparent equations lead to interpretability.

- It is unclear whether time $t$ is defined as continuous or discrete. For instance, in Section 2, “at $t \in [T]$” seems to say that the value of time $t$ is discrete and it is included in index set $[T]$. However, for example in Assumption 2.2, “time point $t \in [0, T]$” seems to say that it is continuous. The authors should clearly define time as a continuous variable represented as $t \in [0, T]$, where $T$ represents the time horizon.

- In Section 3, “we assume that time-varying features and outcomes … are discrete measurements of underlying continuous trajectories…” is unclear. I could not understand what is discrete and what is continuous. Do you imply that trajectories are defined at continuous time and their observations are measured at discrete time? Or do you mean that the values of features and outcomes are continuous in ODE models, but their observed values are discrete? Similarly, “discrete (or continuous) treatment plan” is unclear to me. This makes the paper extremely difficult to follow. The authors should explicitly state that trajectories are defined in continuous time, while observations are made at discrete time points, possibly at varying intervals. They should also clarify the concept of "discrete (or continuous) treatment plan" in relation to the set of allowed treatments.

- Eq. (3) introduces function $g$, and the authors say “it is known and is often assumed to be the identity.” Why? Is it because $g$ describes the treatment outcome as a function of the observed features, and knowing $g$ is the same as specifying the outcome variable? If so, the authors should state this explicitly and provide further clarification on the role and common assumptions regarding $g$.

- Please separate the paragraph at “The goal of ODE discovery is …” in Section 3. Please do not mix the proposed problem setting and the existing one in the same paragraph, which is hard to follow.


(B) The technical soundness is unclear

- **Assumptions**: I could not understand why the authors say that “Assumption 2.2 can be relaxed with Assumptions 3.1 and 3.3.”  I could not see what the point of Discrepancy 1 is. It simply says that “the assumptions in treatment effect estimation do not correspond one-to-one to those in ODE discovery,” which seems trivial. It is hard to follow. The authors should elaborate on how Assumptions 3.1 and 3.3, which concern statistical model specification, allow for a relaxation of the overlap assumption (Assumption 2.2). A clearer explanation of the connection between these assumptions is needed.

- **The soundness of employing ODE discovery methods**: Although the proposed method employs the existing ODE discovery method (called SINDy), it is unclear what this method does and how it works. What is the advantages and the limitations of this method? How can we choose the existing methods? The authors should provide a more detailed description of SINDy, including its workings, advantages, limitations, and how it compares to other potential ODE discovery methods.

- **Ability to express the variability of each subject**: The authors seem to simply change the constant values in simple ODE models to express the variability across subjects. Can we really always express the treatment and the outcome curves with such a simple strategy, given that the continuous time series data often involve complex dynamics? The paper should provide a more thorough justification for this approach. It should also discuss the limitations of this strategy and acknowledge that more complex scenarios might require different ODE learners.

(C) The difference from existing ODE-based treatment effect estimation methods is unclear in the main paper

- Please briefly summarize the description of “Dynamical systems, ODEs, and treatment effects” in Appendix B.1 in the main paper. This will make the motivation of this paper clearer. The summary should clearly outline the distinctions between the proposed method and existing ODE-based treatment effect estimation methods.

### Questions
See all questions in (A), (B), and (C), in particular, (B).

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
