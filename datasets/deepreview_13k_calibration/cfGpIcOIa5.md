# GeoILP: A Synthetic Dataset to Guide Large-Scale Rule Induction

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 8, 3

## Abstract
Inductive logic programming (ILP) is a machine learning approach aiming to learn explanatory rules from data.
    While existing ILP systems can successfully solve small-scale tasks, large-scale applications with various language biases are rarely explored.
    Besides, it is crucial for a large majority of current ILP systems to require expert-defined language bias, which hampers the development of ILP towards broader utilizations.
    In this paper, we introduce GeoILP, a large-scale synthetic dataset of diverse ILP tasks involving numerous aspects of language bias.
    % including complex rule forms, high deduction complexity, and more realistic assumptions.
    The ILP tasks are built from geometry problems, at the level from textbook exercise to regional International Mathematical Olympiad (IMO), with the help of a deduction engine.
    These problems are elaborately selected to cover all challenging language biases, such as recursion, predicate invention, and high arity.
    Experimental results show that no existing method can solve GeoILP tasks.
    In addition, along with classic symbolic-form data, we provide image-form data to boost the development of the joint learning of neural perception and symbolic rule induction.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a large-scale synthetic dataset for inductive logic programming involving a number of challenging predicate language constructions.  The subject domain of geometry provides a rich set of predicates with symmetries, recursion, and constraints. Furthermore, when higher dimensional connective objects (e.g. line segments) are excluded from the background knowledge, predicates become black-box functions of the remaining universe of objects (e.g. points).  This setup provides an instructive setting in which to illustrate and investigate many prominent and unsolved challenges in ILP.

### Strengths
- This paper provides a reference dataset for investigating a number of important challenges in ILP for which no current datasets exist.
- The problem domain is intuitive, providing the potential to be expanded by others as additional points of interest arise. 
- Open challenges in ILP are well articulated, and the role of this dataset in providing a means to evaluate future developments in the field is conveyed clearly.

### Weaknesses
 - The predicate arity section may not be ideally motivated.  For example, the (teacher, subject, student) relationship would probably be addressed in practice by making the subject a predicate, since a relatively small set of subjects at that level of granularity exist.  While the authors' observation is valid, it but might not be compelling to someone unfamiliar with the nuance. The example of a ternary predicate, such as Course(teacher, subject, student), could be more clearly motivated. While the authors correctly point out that reducing this to multiple binary predicates like Math(teacher, student), Physics(teacher, student), etc., increases the number of predicates, the practical implications of this in the context of ILP could be further elaborated. Specifically, the combinatorial explosion of the hypothesis space and the challenges this poses for learning algorithms should be explicitly mentioned. Furthermore, the argument that treating 'subjects' as objects allows for additional relations, such as GoodAt(student, subject), is valid but could be strengthened by detailing how this flexibility is crucial for representing complex, multi-faceted relationships within the domain.
- In addition to combinatorial techniques referenced heavily in the writeup, there are a wide variety of published neuro symbolic techniques.  One of the few highlighted in this paper is by Evans and Grefenstette.  Evans et. all discuss raw data challenges [1], and his dissertation [2] has extensive discussion of challenges and approach. The paper could benefit from a more comprehensive discussion of neuro-symbolic approaches, particularly those that address challenges related to raw data input and complex reasoning. While the authors mention one specific method, the broader landscape of neuro-symbolic ILP techniques, including their strengths and weaknesses, should be explored. This would provide a more balanced perspective on the current state of the field and the potential of different approaches to tackle the challenges highlighted by the dataset.

### Questions
The statement "Enabling recursion is expensive for symbolic ILP, while neuro-symbolic ILP does not support mutual recursion" cites a singe neuro-symbolic method that presumably does not support mutual recursion.  Is there a theorem that says that no neuro-symbolic method can support mutual recursion?  

Is there a reason to exclude the wider neuro-symbolic techniques that have been explored?

Can you discuss the limitations of binary predicates in more detail?  I think this deserves more attention.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper  introduce GeoILP, a large-scale synthetic dataset of diverse ILP tasks involving numerous aspects of language bias.
The dataset consists of geometry problems modeled from levels as varied as textbook exercises, promoting the development of methods that can handle complex language biases, higher arity, and multi-task learning.

### Strengths
1. The paper is clearly written.

2. The dataset GEOILP is  large-scale and mimics real-world data better than traditional closed-world datasets.

### Weaknesses
The article provides a lot of background information, which results in insufficient coverage of its own work.
Firstly, the experimental section is difficult to support the contributions of this paper.
Also, although Section 5 offers a detailed introduction to the content of its dataset, it does not effectively highlight the characteristics of its dataset in comparison to other datasets.

### Questions
How strong is the generalization capability of the neural-symbolic model trained on this dataset? Can it solve tasks beyond geometric problems?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a novel Inductive Logic Programming (ILP) dataset to evaluate ILP algorithms and systems. The presented GeoILP tasks try to formulate geometrical background knowledge as logic programs, and the motivation is to learn geometrical theories/concepts from them. Moreover, the authors also visualised all the tasks and produced images for the problems. The difficulty of the tasks is varied, ranging from simple questions to IMO-level questions.

### Strengths
- The paper discussed the challenges for the current ILP area in detail, and the authors clearly understood the intrinsic disadvantages of ILP, thus the dataset is designed to motivate the community to resolve these long-neglected issues.
- The authors have covered extensive related works, and the paper is well structured and well written.

### Weaknesses
 - The design of the dataset is thoughtful, however, it is still like the previous ILP tasks, which are not very accessible to the ICLR community. For example, the representation of Logic Programming or Prolog is not user-friendly for normal users. The definition and theorems in plane geometry described with logic programs in this paper sometimes are difficult to understand.
- Prolog is not a popular language for theorem proving, modern machine learning techniques such as LLMs could not handle them well enough.
- The experiments in this paper are not enough, it is only experimented with Popper.

### Questions
- Induction will be a very challenging problem for LLMs, would it be possible to extend the dataset and make a natural language version, so that people can compare ILP with LLMs?
- Why not use formal languages that are designed specifically for automated proof, such as lean4 or Coq?

### Soundness
3

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
2

### Summary
This paper proposed a new dataset in the geometry domain to help the researcher enhance the inductive logic programming (ILP) models. The authors indicated that there is no reference hypothesis in the current ILP datasets. This paper proposes a larger-scale ILP dataset with reference hypotheses. This paper also describes the algorithm for how to generate the synthesis data and the corresponding reference. 

However, the paper is borderline rejected for the following reasons: (1) The motivation of the paper is not explicitly discussed in the paper. (2) The Experiments are not explicitly investigated in the paper. Hence, the overall contribution of the paper is limited. (3) Some terminology is vague to use such as learning from raw data and open-world assumption.

### Strengths
The paper builds a novel ILP dataset to boost the development of the ILP community development. The proposed ILP is very challenging based on the statements of the paper. In addition, the authors present the methodology for generating the proposed ILP dataset.

### Weaknesses
1. Based on the structure of the paper, only Section 5 describes the proposed GeoILP. The rest of the Sections look like a survey to describe the development of the ILP methodology. Hence, the contribution of the paper including the method to generate the datasets and the evaluation of the proposed dataset for proving some properties such as learning recursive rules and long variables rules with the existing ILP models is still limited. 
2. When learning from raw data, the authors only discussed learning rules with the help of a pre-trained perception model. However, some discussions about learning from raw data directly without the symbolization process by the perception model are missing.
3. The hypothesis space explored by the GeoILP dataset seems overly complex, particularly with the inclusion of 8-arity predicates. The paper lacks discussion on how using terms within atoms, a common technique in ILP, might address the challenges posed by this complexity. The absence of this discussion raises concerns about the dataset's practical relevance for existing ILP systems.
4. The paper claims that Popper supports predicate invention and noise handling [Cropper & Morel, 2021b; Hocquette et al., 2024] in line 507, yet Section 6.1.1 of Cropper & Morel (2021a) explicitly states that Popper does not have these capabilities. This discrepancy casts doubt on the experimental methodology and the validity of the results.
5. The paper does not adequately address how the open-world assumption (OWA) interacts with the rule format. While the knowledge base uses OWA to determine the truth value of ground atoms, the connection between OWA and the intentional/extensional predicates, especially in the context of rule format, remains unclear. The lack of a reference in the original OWA paragraph further weakens this section.

### Questions
1. Why is this dataset helpful in solving the ILP problem? 
    1. Having reference hypotheses to guide the evaluation of the ILP model is not essential in all senses. In some ILP datasets proposed by [1] or FB15KSelected, the knowledge graph is easy to understand. Hence, there is no need to have a reference in addition. 
    2. Besides, some ILP models support precision and recall as quantitative metrics to evaluate the learned rules from data [3]. 
    3. Furthermore, when generating a set of rules, how to evaluate the performance of an ILP model based on the proposed reference hypotheses. Is the reference complete based on the background knowledge, positive examples, and negative examples?
2. Based on these proposed datasets, the authors mentioned that no one ILP model can successfully learn rules from the GeoILP. The results are further explained in Section 6.2. The symbolic ILP models can not learn even one rule in the *basic level* setting. However, there is no explicit explanation about the basic level in line 520 page 10.  In addition, in line 524 on page 10, the authors stated that three neuro-symbolic models cannot solve the GeoILP because of the features of these ILP models. However, some neuro-symbolic ILP models can learn rules with three or more body atoms and any arities of a predicate [2]. The authors should also analyze more ILP models in Experiments to investigate the current performance of the ILP models.
3. In addition, there is no reference in the Open-world assumption paragraph of Section  4.2. In addition, the open-world assumption is not clearly explained as to why the open-world assumption is related to intentional and extensional predicates in line 428 on page 8. The knowledge base uses the open-world assumption to determine the Boolean value of a ground atom, which is defined in line 257 on page 5. However, in line 428, the open-world assumption is applied based on the rule format. Hence, the authors should explain more about the connections between open-world assumptions and the format of rules. 

Reference:
[1] Richard Evans, Edward Grefenstette: Learning Explanatory Rules from Noisy Data. J. Artif. Intell. Res. 61: 1-64 (2018)
[2] Xujie Si, Mukund Raghothaman, Kihong Heo, Mayur Naik: Synthesizing Datalog Programs using Numerical Relaxation. IJCAI 2019: 6117-6124
[3] Tim Rocktäschel, Sebastian Riedel: End-to-end Differentiable Proving. NIPS 2017: 3788-3800

### Soundness
2

### Presentation
2

### Contribution
2
