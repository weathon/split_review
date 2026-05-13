# LogicMP: A Neuro-symbolic Approach for Encoding First-order Logic Constraints

- Decision: Accept
- Scores: 5, 8, 5, 6

## Abstract
Integrating first-order logic constraints (FOLCs) with neural networks is a crucial but challenging problem since it involves modeling intricate correlations to satisfy the constraints.
This paper proposes a novel neural layer, LogicMP, which performs mean-field variational inference over a Markov Logic Network (MLN).
It can be plugged into any off-the-shelf neural network to encode FOLCs while retaining modularity and efficiency.
By exploiting the structure and symmetries in MLNs, we theoretically demonstrate that our well-designed, efficient mean-field iterations greatly mitigate the difficulty of MLN inference, reducing the inference from sequential calculation to a series of parallel tensor operations.
Empirical results in three kinds of tasks over images, graphs, and text show that LogicMP outperforms advanced competitors in both performance and efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel neural layer, called LogicMP, which can be plugged into any off-the-shelf neural network to encode constraints expressed in First Order Logic.

### Strengths
Relevance: 

The paper deals with a very important problem that is of interest to the larger AI community. 

Novelty: 

The paper introduces a novel layer. However, it fails to acknowledge other works that have integrated logical constraints into a neural network layer. Among the most relevant we find: 
- Nicholas Hoernle, Rafael-Michael Karampatsis, Vaishak Belle, and Kobi Gal. MultiplexNet: Towards fully satisfied logical constraints in neural networks. In Proc. of AAAI, 2022.
- Eleonora Giunchiglia and Thomas Lukasiewicz. Multi-label classification neural networks with hard logical constraints. JAIR, 72, 2021.
- Tao Li and Vivek Srikumar. Augmenting neural networks with first-order logic. In Proc. of ACL, 2019.

### Weaknesses
Clarity: 

Overall, I found the paper not very readable, and I think the authors should try to give more intuitions. 
See below for some questions I had while reading the paper.

- While the authors included an overview of Markic Logic Networks there are still some concepts that look a bit obscure. What does the weight associated with each formula represent? Is it a way of representing the importance assigned to the formula? Why do the authors need the open-world assumption? When explaining the MLNs, can you please add an example with: (i) an ML problem, (ii) what would the FOLC be in the problem, and (iii) what would be the observed and unobserved variables in the problem. 

- What does it mean that $Z_i$ is the partition function? Over what? 

- I am not sure how to read Table 1. Same applies for Figure 3.

- How is it possible that the complexity does not depend on the number of formulas $|F|$? 

- Finally, are the constraints guaranteed to be satisfied or they are just incorporated?

### Questions
See above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A scalable inference method is proposed for MLNs using neural networks. The main idea is to use Mean Field iterations to perform approximate inference in MLNs. Further, since this relies on sending messages in a ground MLN which can be very large, messages are aggregated across symmetrical groundings to improve scalability. It is shown that this can be formalized using Einsum summation. The advantage with this approach is that the messages can be computed through parallel tensor operations. Experiments are performed on several different types of problems and comparisons are presented using state-of-the-art methods

### Strengths
- The use of Einsum to aggregate and parallelize ground MLN messages in MF seems to be a novel and interesting idea for scaling up inference through neural computations.
- The experiments seem extensive and are performed on a variety of different problems showing generality of the approach

### Weaknesses
- In terms of significance, there has been a long history of work in lifted inference with the same underlying principle of using symmetries to scale-up inference in MLNs. One of the key takeaways from such work (e.g. Broeck & Darwiche 2013) is that evidence can destroy symmetries in which case lifted inference reduces to ground inference (if guarantees on the inference results are required). Here, while the approach is scalable, would the same problem be encountered. In the related work section, it is mentioned that for earlier methods, “The latter consists of symmetric lifted algorithms which become inefficient with distinctive evidence”. Does this mean that LogicMP does not have this issue? While the neural approximation can scale-up, I don’t know if there is a principled way to trade-off between quality of inference results (due to approximation using einsum) and scalability. The experiments though show that using LogicMP in different cases yield good results.

### Questions
How does evidence affect Einsum computations? Does it break symmetries making it harder to parallelize?

There has been studies in databases regarding width of a FOL (Vardi)  (e.g. in a chain formula, the width is small). This has also been used to scale-up inference using CSPs (Venugopal et al. AAAI 2015, Sarkhel et al. IJCAI 2016). Would this be related to Einsum optimization?

In the experiments were the weights for the MLN formulas encoded by LogicMP learned (it is mentioned in one case that the weights was set to 1). How do these weights impact performance?

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
The paper proposes a mean-field variational scheme for inference in Markov Logic Networks. The corresponding message passing scheme exploits some structure of the formulas and a tensor operation to speed-up a naive mean filed approximation.

### Strengths
The technique is sound and the paper is generally well-written. 
Experiments are diverse.

### Weaknesses
The novelty of the paper is limited and cannot be assessed from the current paper. This is a major weakness,

The paper fails in positioning in the wider field of neuro-symbolic AI.

The paper claims to be the first method capable of encoding FOLC (pag. 2, “Contributions”). This is not true. The authors themselves cite ExpressGNN. However, there are many other papers attempting at this. I will cite some here, but many more can be found following the corresponding citations: 
Deep Logic Models, Marra et  al, ECML 2019 
Relational Neural Machines, Marra et al, ECAI 2020 
NeuPSL: Neural Probabilistic Soft Logic, Pryor et al, 2023 
DeepPSL: End-to-End Perception and Reasoning, Dasaratha et al, IJCAI 2023
Backpropagating Through MLNs, Betz et al, IJCLR 2021  

Many of these systems have CV and citation networks experiments.

### Questions
1) The paper mentions FOLC but it never defines them. All the examples, though, are definite clauses. Are non-definite clause supported? If yes, are you employing them in your experiments?  

2) Is there an impact in the size of the observed / non-observed split? Usually, there is a great imbalance between the two and it is not clear to me how this may impact the message passing / the pruning of messages.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces LogicMP, a neuro-symbolic method designed to efficiently integrate first-order logic constraints (FOLCs) into neural networks. LogicMP performs mean-field variational inference over an MLN, and its computation is paralleled by leveraging the structure and symmetries in MLNs. The authors demonstrate the effectiveness and efficiency of LogicMP through empirical results in various domains. The results show that LogicMP outperforms the baselines in both performance and efficiency.

### Strengths
- The paper is well-motivated and easy to follow.
- Using Einsum notation to formalize the message aggregation of first-order logic rules is very interesting.
- The performance of the proposed method is better than previous work.

### Weaknesses
- Although LogicMP focuses on encoding FOLs into neural networks, it cannot handle existential quantifiers, which significantly limits its applicability.
- The evaluation appears somewhat limited. Firstly, it only compares 3 neuro-symbolic baselines (SL, its variant SLrelax, SPL). These methods compile the constraint into a probabilistic circuit and then perform exact inference. Given that LogicMP performs approximate inference, comparing it with methods using exact inference seems somewhat unfair. Indeed, some other works encode the constraints and perform efficient approximate inference [1,2]. Lastly, since most previous work encodes propositional logic into neural networks, a more comprehensive evaluation on these previous benchmarks would enhance the paper's comprehensiveness and validity.

[1] DL2: Training and Querying Neural Networks with Logic

[2] Injecting Logical Constraints into Neural Networks via Straight-Through Estimators

### Questions
- What is the expressiveness of LogicMP? Can it encode any quantifier-free first-order logic formula? Additionally, the notation in the first paragraph of Section 2 is somewhat confusing. For instance, is a specific structure required for $f$? In other words, should $f$ be represented in the form of a disjunction of logical atoms? Moreover, is the logical atom $\mathtt{C}(e_1, e_2)$ a general form to represent any relation between $e_1$ and $e_2$?
- Why not directly solve problem Eq.1? In problem Eq.1, we can perform the weighted counting in a parallel manner, rather than using sequential generation as required when solving problems Eq.2 and Eq.3. Moreover, quite a few techniques in fuzzy logic can efficiently handle the discrete potential function $\phi_f(\cdot)$, such as translating the disjunction into the product or the minimum.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
