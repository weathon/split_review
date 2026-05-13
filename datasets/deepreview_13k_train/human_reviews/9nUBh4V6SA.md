# Hierarchically Encapsulated Representation for Protocol Design in Self-Driving Labs

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Self-driving laboratories have begun to replace human experimenters in performing single experimental skills or predetermined experimental protocols. However, as the pace of idea iteration in scientific research has been intensified by Artificial Intelligence, the demand of rapid design of new protocols for new discoveries become evident. Efforts to automate protocol design have been initiated, but the capabilities of knowledge-based machine designers, such as Large Language Models, have not been fully elicited, probably for the absence of a systematic representation of experimental knowledge, as opposed to isolated, flatten pieces of information. To tackle this issue, we propose a multi-faceted, multi-scale representation, where instance actions, generalized operations, and product flow models are hierarchically encapsulated using Domain-Specific Languages. We further develop a data-driven algorithm based on non-parametric modeling that autonomously customizes these representations for specific domains. The proposed representation is equipped with various machine designers to manage protocol design tasks, including planning, modification, and adjustment. The results demonstrate that the proposed method could effectively complement Large Language Models in the protocol design process, serving as an auxiliary module in the realm of machine-assisted scientific exploration.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This article studies for automatic experiment protocol design, representations in different levels of semantics : the protocol element instantialization with elementary operation representation, function abstraction as a sequential representation of the operation, and a model abstraction which specifies reagent and intermediate products.
The authors describe the 3 representations, propose an algorithm to automatically generate new protocols and demonstrate the creativity of the protocol generators based on the representation used.

The work can be framed as the hierarchical representation of policies for an MDP, trained from a natural language corpus, and used to generate new MDPs. The strength of this work lies in the fact that the methodology is tested across several experimental domains. However, the formalisation is not sound.

### Strengths
The article ambitiously represents a synthetic representation of experimental protocols across different experimental sciences : Genetics, Medical, Bioengineering and Ecology.
The article methodically studies the automatic computation of the representation, and then assesses the utility of the protocols generated.

### Weaknesses
 * The article lacks a sound formalisation of the problem.

** While the issue is to represent actions (experimental operations) at different levels of hierarchy, to model the change in the environmental reagents, there is no hint of using the formalisations of Markov Decision Processes or hierarchical actions/reinforcement learning. When the three levels of representations can be easily formalised using the MPD formalisation (for instance in terms of actions/policies, options and waypoints states/subgoals), the proposed formalisation seems imprecise. The lack of a formal framework makes it difficult to assess the completeness and correctness of the proposed representations. For example, the representation of an experimental operation could be more rigorously defined using concepts from planning literature such as preconditions, effects, and resources, which are not clearly delineated in the current work. The absence of a formal model also hinders the ability to reason about the properties of the generated protocols, such as their optimality or feasibility.

** while the word "planning" is used several times in the text, it is only at l.444 that the authors explicit planning tasks as "the exploration
of novel experimental goals". This definition is confusing. While "planning" generally refers to finding the succession of actions to obtain a predefined goal, exploring novel goals is different, and can be referred to as "goal babbling" for instance. The authors' use of "exploration of novel experimental goals" is ambiguous, as it conflates the notion of planning with the generation of new objectives, which are distinct processes. A clearer distinction between these two concepts is needed to avoid confusion. The term "novel" is also problematic, as it is not clear how novelty is defined or measured in the context of experimental goals. 

** In 2.2. the vocabulary used is confusing: a precondition is generally a property of the state that allows you to carry out your operations. It is a distinct notion from an input. The use of "precondition" to describe input reagents is misleading, as preconditions typically refer to the state of the environment that must be true before an action can be executed, rather than the resources required for the action. This conflation of terms makes it difficult to understand the precise requirements for executing an operation. For example, a precondition might be that a specific temperature has been reached, while an input would be a specific reagent.

** Some terms are not defined. For instance : execution context (in l.190 which is used differently from execution condition) and key-value pairs (l193)


* While the authors present comparative results of their representations and algorithms, there is no comparison with other approaches. How do the results compare quantitatively or qualitatively to the state of the art ? The lack of comparison with existing methods makes it difficult to assess the relative performance of the proposed approach. It is unclear whether the proposed representations and algorithms offer any advantages over existing techniques for automated experiment design. A more thorough evaluation would involve comparing the proposed method with other state-of-the-art approaches on a common set of benchmarks.

*While the authors mention as objectives the "exploration of novel goals", "generating novel experimental objectives" and aim to measure "a protocol's novelty", their metrics is only based on similarity measures. Diversity is not mentioned in the criteria. Could you add diversity measures or argue how the proposed metrics take into account diversity ? The evaluation metrics used in the paper focus on similarity to existing protocols, but do not explicitly measure the diversity of the generated protocols. This is a significant limitation, as the goal of the work is to generate novel experimental objectives. A more comprehensive evaluation would include metrics that measure the diversity of the generated protocols, such as the number of unique operations, reagents, or sequences of operations. It is also unclear how the similarity measures are calculated and whether they are sensitive to small variations in the protocols.

Minor comments : 

* Figures need a description to better understand what is shown
* l.234: "Any status transition of the product flow is caused, and is only caused, by the effects of operations". This stance excludes general evolving systems. What about dynamic systems, including with slow transformations, especially in biology or ecology?
* l.440 : "the three scenarios of protocol design introduced in sec 1". It seems sec 1 introduces 3 representations/levels of encapsulation. 
* The results should report computing load 

Typos : 

* l317 : "is consist of "
* l399: "to cover as rich context as possible"
* l420 : "we report and analysis"

### Questions
In section 2.1, why is an experimental objective specified both by the final product and the final operation ? I believe the specification of the final product is the objective, and the final operation is in most cases, only the means.  In the example of a test of the significance of a hypothesis, I would re-formulate the objective as the observation of a property that confirms or contradicts the hypothesis. A definition of a hypothesis based on an operation is restrictive on the generalisation of hypotheses. The authors write in l/225 "operations are the methods to realize rather than the objectives to achieve".

Why were other experimental domains, such as chemistry or physics left out ?

In section 4, I do not quite understand how the testing set is evaluated. Under which criteria/input/prompt is each protocol generated ? What is then the corresponding ground truth ?

### Soundness
2

### Presentation
1

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
This paper addresses the challenge of automated protocol design for conducting scientific experiments. While it is currently possible to automatically execute predefined protocols, it remains a challenge how to design new protocols or modify existing ones to achieve novel experimental objectives. The authors propose a hierarchical representation framework that enables automated protocol design by capturing both procedural and domain knowledge at multiple levels of abstraction. Specifically, the framework consists of three hierarchical levels: (1) a basic level that breaks down protocols into individual actions with their specific attributes (like timing, temperature, etc.), (2) an operation-centric view that groups and generalizes these actions based on their purpose, and (3) a product-flow-centric view that tracks how materials change and interact throughout the experiment. These three levels are implemented using Domain-Specific Languages (DSLs) that help verify and ensure the correctness of protocols. The framework includes an automated method to generate these representations for different scientific domains using (mostly) non-parametric modeling, allowing it to learn and adapt to different types of experiments.

### Strengths
1. The premise of the paper is extremely compelling - enabling AI agents (specifically LLMs) with a structured representation of expert knowledge that allows them to harness their generative capabilities to create novel experimental protocols. 

2. Representing the task of protocol modeling protocols as conditional probabilities is particularly elegant, as it enables better control and parameter learning compared to black-box approaches like neural networks, primarily because this representation naturally captures the logical dependencies between experimental steps. 

3. The dual verification system combining product and operation views is especially clever, as it allows simultaneous optimization of protocol operations while ensuring each step both builds on previous products and generates viable outputs for subsequent steps.

4.  The comprehensive evaluation across multiple scientific domains with real human experts demonstrates the practical utility and broad applicability of the method.

### Weaknesses
1. The language is often very abstract and abstruse. This is sometimes expected because the topic itself is very abstract. But making it simpler would enable the reader to appreciate the contributions more if there was more clarity in explanations. 

2. The work suggests it uses LLMs for the protocol design and it is indeed mentioned where LLMs are used. There are no details, however
on how exactly LLMs are employed in the suggested framework (i.e. do they receive the input from the DSL? or is the DSL a step along the way). It is somewhat intuitive, but an explicit description would be helpful. I appreciated the details in the Appendix but this should be mentioned in the main text.

3. It is not clear how scalable this approach is for more difficult protocols. It is not also clear for someone outside of the tested areas if there even are more difficult protocols. This could be addressed.

Other points:
- It would be very helpful to start with a motivational example of some particular case of research design like the one in Figure 1. Currently, it reads very abstract. But the Figure is helpful. 

- Lines 92-107 are supposed to briefly summarize the mechanism introduced by authors but it is very hard to comprehend. It would be good to correspond these to Figure 1B.

### Questions
1. Can you provide more intuition on what the interface \phi is? Is that simply a set of possible experiments for a given operation (such as the given “homogenization”)? Or a set of functions? Why is it operationalized the way it was operationalized?

2. The motivating examples and descriptions seem to be very heavily concerned with natural sciences. Is it possible to extend your framework to, say psychology or experimentation in computer science itself?

3. How scalable is the framework for more complex protocols?

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
2

### Summary
The authors propose a hierarchical structured representation of experiment protocols to improve the reliability of novel protocols generated by LLMs with RAG. 
* The representation is actually a dual representation over operation-centric and flow-centric views of a protocol.
* This works because the representation serves as a domain-specific language to generate protocols in a bipartite graph-like structure, which enables verification of both the "nodes" and "edges" of the protocol, improving its reliability. 
* However, to use this structured representation requires extracting the entities, which is domain-specific. To do this, they use a Dirichlet Process Mixture Model to extract entities from natural language protocols, which they then aggregate for functions but not for components. 
* To demonstrate the improved viability of protocols generated by this approach, they subselect a test set of 140 protocols from their database with the intent of evaluating across 3 different protocol design tasks and 4 domains. They evaluate generated protocols against the ground truth using six distinct metrics. They compare seven different design approaches which consider different elements of their proposed representation, with and without verification, showing how the different aspects of their approach contribute to its success.

### Strengths
The authors make three contributions:
1. They present the protocol design problem setting, as well as the hierarchical representation of protocols.
2. The propose a method to automatically determine the elements of this structured representation from existing protocols.
3. They perform experiments assessing the value of their representation by testing different methods based on this representation on a varied set of tasks.

# originality

The proposed representation and method appear quite novel, and the choice of metrics to assess the protocol designers is interesting. However, there is no mention of the extensive literature on problem decomposition for LLMs, e.g. Chain-of-Thought reasoning (Wei et al. (2023)). This makes it difficult to ascertain exactly how novel such a decomposition really is. it would be helpful to compare and contrast to existing methods in the literature both for the applied problem of protocol design (e.g. O’Donoghue et al. (2023)) and the solution of task decomposition (e.g. Wei et al. (2023)). It would also be helpful to explicitly state in the contributions whether the is a new problem formulation, application of an existing method to a new domain, or both.

# quality

The conclusions drawn in section 4.5 are the following: 
1. Their proposed approaches outperform naive counterparts.
2. Dual-view hierarchical representations excel at protocol design tasks.
3. The approach generalizes across scientific domains.

The first claim is sound considering the extensive metrics used to assess different approaches. However, it is also shallow compared to the amount of information in Figure 3. On average, it seems that the approach put forward performs well, but there is significantly more variability in their performance. Furthermore, different metrics seem to behave different to the new metrics, with IoU metrics increasing the tail of good results (e.g. IoU metrics), and Sim metrics decreasing the tail of bad results. It is surprising that this is not discussed in more detail, and that there is no estimator of uncertainty (e.g. std, stderr, variance) in the tables in Appendix A. 

The second claim is hard to interpret, as there are no baselines from the literature that are evaluated. As such, it is unclear what is meant by "excel" in this case. Given the highly variable performance values in Figure 3 and the lack of baselines from the literature, it is not possible to conclude this from the available results. You could alternatively state that the dual-view approaches outperform their counterparts across all tasks on average across all metrics.

The third claim is well supported by the experiments across four domains and the aggregate results. That being said, an additional set of results in the appendix that shows results by scientific domain would also be helpful in supporting this claim, especially if these results were to show that the proposed methods performed best across all domains separately (i.e., tables like those in appendix A, but partitioned by domain instead of task).

# clarity

As a non-expert on protocol design, I found the problem motivation well done. The task is well situated within its broader context. Figure 1A is enlightening, but Figure 1B is slightly confusing, as the relationships between the different elements could be made clearer. The problem setting is well presented with a judicious use of notation and examples throughout. The experiments are well explained as well.

# significance

The motivation put forward in the introduction accurately captures the significance of this work. However, it could be improved even more by relating it to existing work that creates structured workflows using LLMs, and relating it to the more general problem of getting LLMs to structure their outputs.

### Weaknesses
 # Presentation

* Figure 3 Caption is not standalone, very small font sizes for xticks and y ticks. The x-axis is not mentioned, which makes interpretation impossible.

* Figure 2 labels and ticks are too small, the caption is largely uninformative without the main text

* Fig 1 B is unclear

* Limitations section is empty (Appendix G)

# Soundness
* Line 361: A reference to Fig 2B is insufficient for the claim that function abstraction works. Idem for Fig 2C. The results must be interpreted (see the "Quality" section in strengths for more details).

* The testing set is susceptible for memorization because you are using LLMs. It would be good to have a set of protocols that are after the cutoff dates of the LLM training.

* it would be good to introduce the SA algorithm in more detail so that we understand what the similarity score actually represents.

* Lack of baselines from the literature

# Contribution 
* Very limited discussion of the results.

* Unclear whether they consider the problem setting to be a contribution. It would be important to contrast the problem formulation with that of prior work, such as that of O’Donoghue et al. (2023). In particular, whether their formulation of the protocol design problem (not the representation itself) differs in any meaningful way. This is important because the identification of the protocol design problem is cited as a contribution on line 147.

### Questions
* Line 44: What is a "protocol portal"? Such terminology, if not generally entrenched in the suggested domain, should be introduced.

* Line 199: "The total amount of the instance actions can be extremely high, i.e., about 150K per domain," how do you arrive at this number?

* How do you track quantities of reagents? The algorithm seems to treat them as a set and remove them if used once without any notion of quantity.

* Line 504: what it t( ) ?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work focuses on the automated design of self-driving labs' protocols. Protocols specify how robots in self-driving labs conduct experiments. In many cases, conservative protocols are not sufficient because they do not allow for significant scientific discovery. However, designing new protocols is a cumbersome and error-prone process. To tackle these challenges, the authors suggest LLMs for the generation of protocols.

### Strengths
- The problem is relevant and timely. Automation is much-needed and of high added value.

- The problem is open without sufficient solutions in the area. The approach seems to be novel and contributes to the state of the art.

- The contribution seems to be sound and the evaluation is convincing.

- Clear presentation and discussion.

### Weaknesses
 - It is unclear why LLMs are chosen for this purpose. This is essentially a big design-space exploration problem with the added opportunity of using a physical actor in purposeful experimentation. A similarly apt approach could be using digital twins with traditional learning methods, e.g., reinforcement learning and obtain a formally modeled protocol.

- I find it somewhat concerning that a costly and potentially hazardous endeavor such as robotized experimentation with chemicals and biologically active materials is approached at the level of LLMs and the safety concerns are not discussed. For example, certification of protocols through formal verification might not be possible in this approach.

### Questions
- Why LLMs and not some other AI method? This would allow for a better positioning of the work.

- How can the generated protocols be certified? This would be a much-appreciated, brief discussion point.

### Soundness
3

### Presentation
3

### Contribution
3
