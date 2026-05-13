# Who Should Join the Decision-Making Table? Targeted Expert Selection for Enhanced Human-AI Collaboration

- Decision: Reject
- Scores: 6, 5, 5, 6, 5, 5

## Abstract
Integrating AI and human expertise can significantly enhance decision-making across various scenarios. This paper introduces a novel approach that leverages the Product of Experts (PoE) model to optimize decision-making by strategically combining AI with human inputs. While human experts bring diverse perspectives, their decisions may be constrained by biases or knowledge gaps. To address these limitations, we propose an AI agent that provides probabilistic, rule-based insights, complementing and filling human experts' knowledge gaps. A key feature of our approach is the strategic selection of human experts based on how well their knowledge complements or enhances the AI’s recommendations. By dynamically adapting the expert selection process, we ensure that decisions benefit from the most impactful and complementary inputs. Our PoE model calibrates inputs from both AI and human experts, leveraging their combined strengths to improve decision outcomes. Furthermore, operating in an online setting, our framework can also continuously update the AI’s knowledge and refine expert selection criteria, ensuring adaptability to evolving environments. Experiments in simulation environments demonstrate that our model effectively integrates logic rule-informed AI with human expertise, enhancing collaborative decision-making.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper leverages a Product of Experts (PoE) model that combines AI with input human expertise for enhanced decision-making, where an AI agent provides probabilistic, rule-based insights to choose a human expert for a specific case. The system dynamically selects human experts based on how well their expertise and recommendations might fit a specific scenario, while continuously updating its knowledge and selection criteria in an online setting. Through simulation experiments, the model demonstrates effective integration of rule-informed AI with human expertise.

### Strengths
This paper introduces a solution for a very relevant problem, and its a good idea for an AI to choose who to ask rather than making call themselves in critical settings like patient diagnosis.

### Weaknesses
1. I have a central problem with the premise of this paper.  The paper indirectly acknowledges an AI cannot be trusted to make direct medical decisions and it can be used well for augmenting human expertise. Yet it claims competence in selecting which human expert should make those decisions. This implies the system can reliably evaluate medical expertise, which might requires equal or greater medical knowledge than making the diagnoses itself. Maybe this is wrong, and a doctor's expertise pertaining to certain cases can be evaluated without any medica knowledge as its captures in the features $x$, but if the model is so good, why not use it for almost similar strategy for diagnosis. Instead of doctors, you choose diagnosis.


2. Almost all experiments are done on synthetic data, but many cases when it is not clear which expert to reach out to are the ones which are not so simple. And the rules for generating the synthetic data are fairly simple, so I am not sure how well it covers these rare boundary cases where such an AI system might actually be needed.

### Questions
1. Is it actually perception in active perception module?

2. So the AI cannot be trusted to make critical decisions, but can be trusted to choose the expert to make critical decisions? Why one failure mode is different than the other? What if a wrong expert is chosen? 

3. Rule 2 in line 198 is actually not a rule but a guideline which is shown to be false. Sometimes a patient responds positively to a drug, but that’s because the drug is targeting a symptom not the actual cause of the symptoms. I understand this is an example, but it clearly a red flag in terms of author understanding of medical domains.

4. Who is providing these rules for feature construction? Are they given by experts and verified through a panel of experts?

5. In Equation 2, why $g_a$ is modeled as Gumbel noise? An explanation for this should be added in the paper.

6. Line 220: How would you recommend getting $w_a$ when due to less data MLE cannot be used confidently?

7. How much data will you need to build a Human Expert Reliability Model for each expert? And how do you plan to get this data in a real world setting?

8. Are you assuming that all experts are available all the time? In real world, an expert might not be available, and another expert whose score is less might be available and for a particular case might be able to give an equally good advice. I am guessing a naive approach will be to go to the next expert according to information gain. But then a lot of time can be wasted in asking the expert with highest information gain. How can we extend this model to incorporate such a scenario?

9. If actual medical data is used in the process, do you envision any privacy leakage concerns?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a approach that leverages the Product of Experts (PoE) model to optimize decision-making by strategically
combining AI with human inputs. The proposed approach performed strategic selection of human experts based on how well their
knowledge complements or enhances the AI’s recommendations. Experiments in simulation environments demonstrate that the proposed method can effectively integrates logic rule-informed AI with human expertise, enhancing collaborative decision-making.

### Strengths
1. The research topic is timely and relevant. As human-AI collaboration becomes more prevalent, it is important to study how to effectively combine the strengths of both AI and human to achieve human-AI complementarity.

2. The paper is well-written overall and easy to follow.

### Weaknesses
1. The main contribution claimed by the authors is the algorithmic combination of AI probabilistic predictions with human deterministic decisions. However, this contribution closely mirrors the work presented in a NeurIPS 2021 paper [1], which similarly develops algorithms that integrate probabilistic model outputs with class-level human decisions. Equation (4) in the current paper is nearly identical to Equation (1) in the 2021 NeurIPS paper. Despite this resemblance, this foundational work is overlooked and is not included as an important baseline in either the discussion or experimental sections.

2. The evaluation has some limitations. 1) Limited experimental setting: The evaluation scenario is restricted to a specific medical decision-making task, leaving it unclear whether the proposed method generalizes to other AI-assisted decision-making contexts. 2) Limited baselines: In addition to the NeurIPS 2021 method, several established methods in collective intelligence and crowdsourcing, such as GLAD [2] and even the basic EM algorithm, are missing from the baselines. This absence raises questions about the method's effectiveness compared to well-established techniques.


3. Another important contribution of the paper claimed by the authors is that the approach can enhance model interpretability and human-AI interaction. However, there is no empirical support provided through human subject experiments to support these claims about the method's utility and effectiveness in ehancing human understanding of AI behavior or further improving the human-AI collarboration in decision making.

### Questions
See above Weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a solution to the expert selection problem in human-AI collaboration. The AI in the paper is logic-based, which is interpretable by humans. The algorithm estimates the posterior recommendation of actions, conditioning on AI predictions and doctor decisions. The expert is then selected by maximizing the information gain. The method is evaluated on a synthetic dataset.

### Strengths
The question in the paper is novel and important. It proposes to select human experts into the decision-making team to maximize the marginal information gain. The approach improves the complementarity of the human-AI team.

### Weaknesses
I found the approach in the paper not convincing enough:

* Claim on interpretability: while the paper claims a lot about the interpretability and reliability of the system, I found few statements are evaluated in the evaluations. e.g.
  - the AI is constructed from logic rules, which the paper claims to be interpretable and transparent. However, compared to other black box learning algorithms, there are no evaluations of the interpretability or the reliability of such logic-rule-based AI predictions. It is unclear whether such a construction is necessarily good or how it affects the performance of the system. 
  - the evaluations seem to be purely based on synthetic data. See my question below. 

* Information gain: the paper takes an approach from rational decision-making by estimating the posterior distributions and maximizing information gain. While I agree that the posterior conditioning on a multi-dimensional signal space can be hard to estimate, I feel the PoE model is poorly justified. How well can it represent the posteriors and what are the alternatives? What are the assumptions? e.g. is it implicitly assuming the signals from the doctors are conditionally independent? Particularly, the following paper might be relevant: 
> Ziyang Guo, Yifan Wu, Jason D. Hartline, and Jessica Hullman. 2024. A Decision-Theoretic Framework for Measuring AI Reliance. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency (FAccT '24).

* Greedy selection vs optimal: the algorithm for expert selection is a greedy algorithm that maximizes marginal information gain. However, there's no analysis of the algorithm being optimal or approximately optimal. In fact, this signal selection problem has been shown to be computationally hard: 
> Chen, Y., & Waggoner, B. (2016, October). Informational substitutes. In 2016 IEEE 57th Annual Symposium on Foundations of Computer Science (FOCS) (pp. 239-247). IEEE.

### Questions
It seems like Table 1 compares the output of the PoE model with different setups. However, the paper claims: "In our AI-human collaborative system, it is important to note that the final decision rests with the human expert team, with the support of the AI agent in the decision-making process." I wonder how real human make decisions under a synthetic dataset, or the evaluation does not consider real human decisions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this work, the authors propose a framework for improving human-algorithm decision-making by dynamically querying an ensemble of human experts. In particular, the authors develop a Product of Experts (PoE) model which factorizes the final probability of an action recommendation into a product of expert-specific and algorithmic decision recommendations. The authors also devise an entropy-based expert selection strategy that selects a subset of experts to inform decisions. The authors validate their framework theoretically and via synthetic experiments.

### Strengths
### Technical Framework

The authors propose a simple and interpretable approach for incorporating diverse expert feedback in collaborative algorithmic system recommendations. Both the rule-based controller and PoE are simple and easy to understand. I especially appreciated the 
Advantages of PoE in Collective Intelligence subsection describing the rationale for PoE. This is quite interesting and I encourage the authors to add additional intuition for this point in the main paper. The targeted expert selection approach is also interesting and well-motivated.

### Motivation and Prior Work

The work has a clear grounding in prior work and demonstrates a novel set of approaches in comparison to existing approaches. The authors do a nice job of motivating the framework and providing a high-level overview early on in the work.

### Weaknesses
### Related Work: 
- This paper generally covers relevant related work. There are several works that study expert heterogeneity in other contexts. For example, Rambachan (2024), Rambachan, Coston, & Kennedy (2024), and Lakkaraju et al. (2018) use heterogeneity as an instrumental variable for identification under unobservables. De-Arteaga et al. (2023) use heterogeneity to mitigate measurement error issues.

Rambachan 2024, Identifying Prediction Mistakes in Observational Data, https://academic.oup.com/qje/article-abstract/139/3/1665/7682113.

Rambachan, Coston, & Kennedy 2024, Robust Design and Evaluation of Predictive Algorithms under Unobserved Confounding, https://arxiv.org/abs/2212.09844.

De-Arteaga et al., Leveraging Expert Consistency to Improve Algorithmic Decision Support, https://arxiv.org/abs/2101.09648. 

Lakkaraju et al. 2018, The Selective Labels Problem: Evaluating Algorithmic Predictions in the Presence of Unobservables, https://cs.stanford.edu/~jure/pubs/contraction-kdd17.pdf.

### Formal Model: 
- The motivation for a simple rule-based agent is strong, as it offers transparency in high-stakes applications such as the running medical example. However, I do find it odd that algorithmic recommendations would be stochastic in this context (i.e., e.q 2). This would introduce additional variance in the selection of actions that may be unwanted by decision-makers. Similarly, there is a tension between the algorithmic recommendation being probabilistic and the human expert opinion being deterministic. (Line 244) Could you please elaborate on the rationale for this decision, and provide contexts in which it is likely to be reasonable? I understand this is necessary for the technical machinery but have concerns about the real-world applicability of this setup. 
- The outputs of the AI-human ensemble model seem to imply that the algorithmic system will make the final decision (i.e., e.q. 6). However, I appreciated your clarification on lines 342-348 mentioning that humans have final authority over the decisions. This point would be helpful to make early on in the setup of the paper to help the reader understand the overall workflow. 
- The indolence assumption imposed by the PoE model is strong. This assumes that human experts’ opinions do not influence one another. It would be helpful to provide a rationale for this assumption and a real-world context in which it is likely to be reasonable. Further, you might outline explicitly somewhere how you can get around this indolence assumption in the future. I understand that the assumption is helpful for the clean factorization and estimation approach, but would like additional justification. 

### Experiments: 
- Generally, the synthetic experiments demonstrate the utility of the proposed approach. I especially appreciated the ablations and Figure 2 illustrating the construction of the cognitive regions. 
- However, I did find the setup of the synthetic experiment to be somewhat contrived. While the proposed design illustrates one configuration of regions in which the proposed approach improves accuracy and reward, I these results do not tell me how the proposed approach performs across an array of data generating processes (i.e., systematically varying the space of co-variates, decision rules, and other simulation parameters). Further, the experiments do not illustrate the specific failure modes of the proposed approach. 
- Given that a key advantage of the proposed expert selection approach is information gain, it would be helpful to report the regret evaluated against the optimal configuration of experts for each decision instance. It would also be helpful to provide a temporal visualization of cumulative reward over time steps. 
- This work would be strengthened substantively via an evaluation on real or semi-synthetic data. I understand that it is not possible to simulate environmental dynamics of collaborative decision-making in real time, but it would be helpful to illustrate how this framework might fit into a real-world decision-making workflow. Such an evaluation would also alay some of my modeling concerns (see above).

### Presentation: 
- I find the semantics of “true action” (244) unintuitive. Is “true action” the final action that is proposed by the system? 
- Minor: It is more standard (and readable, in my opinion) to omit boxes around equations. This is a minor point and I understand if the authors choose to keep the current format.

### Questions
- Could you describe a realistic real-world decision-making setting in which an algorithm would provide probabilistic predictions and human experts’ decisions would be deterministic?
- Under the simulation framework, could you elaborate on how the final decision of the collaborative team is generated at each time step? I checked through the appendix for the technical setup but this was not clear.
- Under what data generating conditions would the proposed PoE approach perform worse than MoE, majority voting, or other alternatives?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed one AI-human collaborative framework with an active module which optimally select the human expert from the multi-disciplinary team. This framework includes the linear utility function, Plackett-Luce model, Product-of-Experts model, Human Expert Rilability model, and AI-Human ensemble model. The active learning idea is used to select the expert who can provide the most valuable contributions, such as the greatest informaiton gain or reduce the current entropy. In the model learning phase, MLE is used to learn the AI agent's logic rule and associated weights. MAP is used to estimate the parameters in the human's reliability model. The framework is tested based on the synthsized datasets with simulated patients and doctors.

### Strengths
- The idea, select the expert using the active learning algorithm, is good, which helps to save time and effort. 
- Follow the existing Plackett-Luce model to model the probability distribution of the selected action. 
- Fuse human opinions and AI recommendations via the product-of-experts model.

### Weaknesses
 - The experiments do not fully support the advantages claimed for the proposed framework, specifically its robustness to influence from weak experts. Although the authors present some results in Appendix C, the robustness bound is unclear, and it is not evident how the advantage of the PoE model is demonstrated through the experimental results. The core issue is that the experiments do not isolate the impact of the PoE model from the expert selection process, making it difficult to ascertain the true benefit of the PoE component.
- The method for selecting the hyperparameter value is not clear. Specifically, the paper lacks details on how the prior for the MAP estimation of human reliability and the convergence criteria for the expert invitation process are determined. This lack of clarity makes it difficult to reproduce the results and assess the sensitivity of the model to these parameters.
- The proof explaining how targeted expert selection helps to find the optimal action is not well explained. The paper claims that maximizing information gain leads to the optimal solution, but it does not provide a rigorous justification for this claim. The potential for the algorithm to converge to a local optimum is not sufficiently addressed.
- The experiments are not comprehensive. Although Mixture of Experts, majority voting, and weighted voting are included, these approaches are insufficient to fully evaluate the model. The selection of baseline methods does not cover the state-of-the-art techniques in human-AI collaboration, which limits the scope of the evaluation.
- Why are level-0 and level-1 patients generated in this way? Does this imply that the proposed framework only works for the two-level scenario presented in the paper? The paper does not provide a clear explanation of the rationale behind this two-level patient generation, and it is unclear whether the proposed framework can be generalized to more complex scenarios with multiple levels of patient complexity.

### Questions
- In the AI-human ensemble model, it is unclear how to set the value for the hyperparameter, \eta. This is particularly important if the authors aim to apply this framework in a healthcare setting, as small changes in \eta could significantly impact the final medical decision.   
- In the targeted expert selection, why is the optimal solution guaranteed to be obtained by maximising information gain? How is the potential issue of minimising entropy leading to locally optimal solutions addressed?
- The experiments are not comprehensive. Although Mixture of Experts, majority voting, and weighted voting are included, these approaches are insufficient to fully evaluate the model.
- Why are level-0 and level-1 patients generated in this way? Does this imply that the proposed framework only works for the two-level scenario presented in the paper?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a Product-of-Experts (PoE) model to enhance decision-making in AI-human collaborative systems, particularly in complex, high-stakes domains such as healthcare. The PoE model integrates a logic-informed AI agent with human expert opinions, leveraging probabilistic recommendations and expert reliability modelling to filter out noisy inputs and prioritize high-quality decisions. Notable features include targeted expert selection based on information gain and entropy reduction, the use of synthetic datasets for evaluation, and a structured approach to decision-making under varying levels of complexity. The model's primary goal is to improve collaborative efficiency by strategically selecting experts whose insights add the most value, thus reducing consultation costs and optimizing decision accuracy.

### Strengths
1) Writing is generally acceptable.
2) The sequential expert selection approach invites experts based on information gain, effectively filtering out less informative inputs. This could be critical in time-sensitive or resource-constrained environments like healthcare. 
3) The model's use of confusion matrices to assess expert reliability provides a defence against unreliable or noisy inputs. 
4) The incorporation of a logic-informed AI agent has the potential to make it interpretable by leveraging established medical knowledge and rules --- however, this has not been tested.

### Weaknesses
1) My biggest concern is with the evaluation. The evaluation lacks real-world case studies, which would provide valuable insight into how the model performs with actual patient data. This absence limits the credibility of the model's robustness. Specifically, the use of synthetic data and predefined rules provides controlled evaluation. However, it fails to convince me in terms of accounting for real-world complexities and noise in patient data and other contextual factors, which could unjustifiably reduce the perception of the expertise of doctors. This risks overestimating or underestimating the doctor's performance. The work remains untested in unpredictable scenarios.

2) I believe that the classification of doctors into narrow specialists, broader experts, and random decision-makers lacks the complexity of real-world expertise. This setup does not accurately reflect the variability and complexity of real-world expertise, potentially limiting its practicality to actual clinical settings.

3) The model's design favours convergence on a single recommended action, which may not reflect real-world cases where multiple treatment options could be equally viable. Yes, Level-1 scenarios kind of capture this, but the authors' intention for Level-1 scenarios was very different. This limitation affects cases where multiple and often complementary actions play a role.

4) How we can reliably compute the confusion matrices is unclear.

### Questions
1. How would the model handle cases that require interdisciplinary collaboration across narrow specialties (e.g., when Doctors 1, 2, and 3 must work together)? 

2) What are the authors' plans for validating the model on real-world patient data? Could they provide insights into how they might address the unpredictability and variance seen in genuine cases beyond synthetic data? 

3) Following the previous question, what specific process was used to collect the domain knowledge? What were the specific sources consulted?

4) How would the model handle scenarios where multiple actions could lead to positive outcomes? Would the authors consider expanding the model to support probabilistic representation for multiple viable actions, allowing for flexibility in cases where a single action may not be optimal?

5) How do the authors envision healthcare professionals interacting with the model (and vice versa), particularly when interpreting the logic-informed AI recommendations alongside expert input? How could you convince the community that the proposed AI is the best way to select the set of doctors to work with the AI? 

6) Given the reliance on historical reliability scores, how does the PoE model address potential bias against early-career doctors or those with limited track records? Have the authors considered adding mechanisms to ensure junior experts still have training opportunities or some input, particularly in non-critical cases?

### Soundness
2

### Presentation
2

### Contribution
2
