# Rethinking the Expressiveness of GNNs: A Computational Model Perspective

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 5, 6

## Abstract
Graph Neural Networks (GNNs) are extensively employed in graph machine learning, with considerable research focusing on their expressiveness. Current studies often assess GNN expressiveness by comparing them to the Weisfeiler-Lehman (WL) tests or classical graph algorithms. However, we identify three key issues in existing analyses: (1) some studies use preprocessing to enhance expressiveness but overlook its computational costs; (2) some claim the anonymous WL test's limited power while enhancing expressiveness using non-anonymous features, creating a mismatch; and (3) some characterize message-passing GNNs (MPGNNs) with the CONGEST model but make unrealistic assumptions about computational resources, allowing $\textsf{NP-Complete}$ problems to be solved in $O(m)$ depth. We contend that a well-defined computational model is urgently needed to serve as the foundation for discussions on GNN expressiveness. To address these issues, we introduce the Resource-Limited CONGEST (RL-CONGEST) model, incorporating optional preprocessing and postprocessing to form a framework for analyzing GNN expressiveness. Our framework sheds light on computational aspects, including the computational hardness of hash functions in the WL test and the role of virtual nodes in reducing network capacity. Additionally, we suggest that high-order GNNs correspond to first-order model-checking problems, offering new insights into their expressiveness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new computational model—the Resource Constrained CONGEST (RL-CONGEST) model—designed to address the inconsistencies and irrationalities in the current analysis of GNNs' expressivity. The RL-CONGEST model forms a framework for analyzing the expressivity of GNNs by introducing resource constraints and optional pre-processing and post-processing stages. Through this framework, it can reveal computational issues, such as the difficulty of hash function computation in the WL test and the role of virtual nodes in reducing network capacity, thereby providing theoretical support for understanding and improving the expressivity of GNNs.

### Strengths
1. This paper clearly identifies three key issues that are commonly overlooked in the current analysis of GNNs' expressivity, which represents a relatively novel perspective.

2. The RL-CONGEST model proposed in this paper provides a theoretical framework for the expressivity of GNNs.

3. The paper conducts an in-depth analysis of the computational complexity of the WL test, which is valuable for understanding the potential and limitations of GNNs and also demonstrates the paper's solid theoretical foundation.

### Weaknesses
1. Lack of Empirical Validation: The paper lacks empirical experiments to support the theoretical results. This absence of empirical validation significantly weakens the practical relevance of the proposed RL-CONGEST model. Without experimental evidence, it remains unclear whether the theoretical insights translate into tangible benefits for real-world GNN applications. The analysis of computational complexity, while valuable, needs to be complemented by experiments that demonstrate the model's behavior on actual graph datasets.

2. Lack of Guidance on Model Design: The paper does not clearly propose how to use the RL-CONGEST model to enhance the expressive power of GNNs. While the framework provides a theoretical lens for analyzing GNNs, it falls short of offering concrete design principles. The paper does not explain how to leverage the resource constraints identified by the model to create more expressive GNN architectures. This lack of actionable guidance limits the practical utility of the proposed framework, making it difficult for researchers to apply the model in practice.

### Questions
1.Can you provide some empirical experiments to verify the correctness of the analysis results of the RL-CONGEST model?

2.Is the RL-CONGEST model applicable to the analysis of all different types of GNNs and tasks on graphs?

3.Do the computational resource limitations mentioned in the article reflect the constraints in the real world? Are these limitations applicable to all types of GNNs?

4.Can you further provide design guidance on how to use this method to improve the model's expressive power?

5.Since the article mentions analyzing the expressive power of GNNs under resource constraints, is the RL-CONGEST model applicable to learning tasks on large graphs that are also resource-constrained?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper examines the limitations of the theoretical expressiveness of GNNs and introduces a novel computational framework, RL-CONGEST, which factors out pre- and postprocessing and limits the computational power of nodes. The authors further analyze the WL-test within this framework and contribute some theoretical insights. RL-CONGEST, while positioned primarily for GNNs, also offers implications for understanding computational constraints in other computation models.

### Strengths
* The paper introduces RL-CONGEST, a new computational model that addresses aspects previously overlooked in the GNN literature, particularly computational constraints at the node level.
* Some shortcomings in prior work are highlighted and critically analyzed, including preprocessing complexities and computational limits.
* RL-CONGEST has potential standalone value beyond GNNs, as it provides a framework to study computational complexity and expressiveness that could benefit other areas.

### Weaknesses
 * Section 3.1: The authors argue that preprocessing time complexity is often underestimated in the GNN literature, with Wollschläger et al. (2024) as an example. However, this appears to be an isolated case rather than a trend in the field. A more robust case for this claim could be made by referencing additional studies or a systematic analysis that demonstrates the prevalence of overlooked preprocessing complexities. Zhang et al. (2023), which the authors cite and analyze, actually discusses preprocessing time explicitly in the paper, which weakens the generality of this argument. While it is valuable to account for preprocessing, demonstrating that this issue extends across multiple papers would strengthen the point. Further, as most of these papers mainly focus on expressiveness, computational complexity might just not be the main focus.

* Section 3.2: The “mismatch” claim between models with and without features lacks clear evidence. The advantage provided by features in model initialization is well-known, and the WL test is adaptable to both anonymous and pre-colored contexts. More detail and examples of specific instances where this mismatch has led to issues in the literature would clarify and strengthen the claim. The authors tend to write around what the mismatch actually is in this section and should clearly define it.

* Section 3.3: The assertion that CONGEST is “inappropriate” for direct use is somewhat unconvincing, as it can still serve as an upper bound for computational capacity. While RL-CONGEST’s constraint on node computation is a useful contribution, existing models are still relevant for the purpose of their analysis. Furthermore, Theorem 4 should explicitly assume a connected graph and the version stated in the paper is technically wrong. It is also worth noting that in many GNN studies, expressiveness rather than computational complexity is the focus, so adding computational constraints could shift the narrative and purpose of the study. If the authors are proposing RL-CONGEST as a practical standard for GNNs, specific examples and a discussion on which complexity classes should be used for GNNs would help contextualize it within the field.

* Adding computational constraints to CONGEST is an interesting approach, but it becomes very detached from the application in GNNs. For example, the authors do not go into detail on what complexity classes we should allow for GNNs. One could make an argument that as GNNs are usually implemented with fixed size networks that run in constant time, the computational envelope should also be constant to yield the most realistic bounds. RL-CONGEST is interesting on its own, but how the computational constraints should be best put to use should be discussed in paper that claims to investigate the GNNs. The paper would benefit from more guidance on how GNN practitioners should employ RL-CONGEST, along with concrete examples of benefits. A more precise articulation of the expected impact or practical value this framework could offer would also strengthen the contribution.

Overall, the paper makes several claims and only backs up some of them. In the end, it is not clear how the newly proposed model is supposed to be used in future work (should everybody just use their own complexity classes for the local computation, what benefit does this have?) and leaves the question on what impact this work can have. The authors should address this issue and formulate some clear benefits of their framework.

### Questions
* Could the authors clarify specific insights from the RL-CONGEST model that would be practically useful for GNN practitioners?
* Do the authors envision RL-CONGEST serving as a new standard or benchmark model for GNN complexity analysis? If so, could they suggest specific complexity classes for GNN applications or examples that showcase RL-CONGEST’s advantages?
* Could you clarify your position on CONGEST's usefulness as an upper bound and discuss whether RL-CONGEST complements rather than replaces existing models?
* Could you add a discussion on appropriate complexity classes for GNN analysis using RL-CONGEST? In that context, can you provide guidelines or a framework for GNN practitioners on how to effectively use RL-CONGEST in their research or applications?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors very correctly point out that the current theoretical analysis of GNNs is lacking in a few key ways (e.g. granularity and taking into account computational expense). To remedy that they propose using Resource-Limited CONGEST model, instead of usual CONGEST and relating WL-tests to model-checking problems that can prove a more granular expresivity testing.

### Strengths
I agree with the authors that the theoretical expresivity analysis of GNNs is quite lacking. It makes a lot of sense to limit the computational power of the nodes (GNN update functions). As that is more realistic. The idea to use model-checking problems instead of WL to judge the theoretical power of GNNs is novel and I think quite promissing, as it allows for higher granularity. 

This work also provides interesting motivation for why virtual nodes help, as they are a very common tool in practice. One of the first works to look at this theoretically to the best of my knwoledge.

It's generally well written and easy to follow.

### Weaknesses
Authors stress that "unlimited computational resources of CONGEST" is an issue and chose to just use a more restrictive computation class for the node updates. Ideally I'd like to see this being contrasted with the universal approximation theorem for MLPs. As the update function is usually an MLP it's power I'd say is more defined by approximation quality of whatever computation it needs to perform.

In the section "Additional Features Empower Models by Breaking Anonymity?" authors say that it's not good that some expressive GNNs might be breaking anonymous setting by using additional features. I would say that this is not a good way to look at this. In my opinion that the point of a good chunk of more expressive GNN research is precisely how to add pseudo-indentifiers to a graph with as few negative impacts (bad generalization).

Speaking about negative impacts of node identifiers, in the proposed computation model authors permit "nodes to be aware of their own unique IDs". This doesn't make much sense from ML perspective as generalization will be terrible if a stable ID assignment is not possible, and normally it is not possible to do so on general graphs. So for a paper arguing about making theoretical GNN analysis more realistic I think this is a noteable issue.
Authors do motivate this choice by saying that "real-world graph datasets are rich in node features". I'd argue that this is still very far away from node IDs, e.g. say if features are just a few different atom types in case of many molecular tasks. I'd like to see some data analysis showing the unique identifiability of nodes in multitude of real world datasets to convince me that this is the case.

The work also lacks direct applicability to fixing or ranking GNN architectures. Which would be the main benefit of the newly proposed GNN analysis. To make the paper complete I would like to see analysis/ranking of some few popular GNN architectures and hopefully showing that this translates to some real tasks, for example ones for which the assumptions, such as unique identifiability by node features, more or less hold.

Also, speaking about popular GNN architectures, authors skipped the two first subgraph GNN papers, when discussing subgraph GNNs (https://arxiv.org/abs/2110.00577 https://arxiv.org/abs/2111.06283)

### Questions
Distributed computing has various computation models already, besides LOCAL and CONGEST. It would be nice if authors would dig a bit deeper in the distributed computing literature to see what alternatives already exist and if they would be more fitting than CONGEST. It's been a while since I looked at those myself, but for example https://arxiv.org/pdf/1202.1186 investigates a very restricted computational model, that should still be able to simulate a WL test (it was also used in some simpified GNNs https://arxiv.org/pdf/2205.13234). I'm sure that others exist as well.

### Soundness
3

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
4

### Summary
In this paper, the authors first explain the limitations and unrealistic assumptions of several current approaches in analyzing the expressive power of GNNs, including underestimated preprocessing time, anonymous WL tests with non-anonymous features, and unrealistic assumptions in the CONGEST model. Next, the authors propose the RL-CONGEST model to address these issues. Several results are derived: (1) GNNs require substantial width and depth to simulate the WL test; (2) virtual nodes can help reduce computation costs, although they do not improve theoretical expressive power; (3) the RL-CONGEST model can solve the PNF model-checking problem with 
$k$-WL graph transformation in $O(k^2)$ rounds.

### Strengths
1. The paper is well-structured and nicely presented.
2. The stated limitations of existing approaches make sense to me, and the examples are intuitive.
3. The new results derived by the RL-CONGEST model are interesting.

### Weaknesses
My main concern is about the practical implication of the proposed model beyond what the author presented. 
1. One question is how we can use the RL-CONGEST model to effectively estimate and compare the representational power of different GNN variants or even predict their performance in real-world applications.
2. The authors claim that the proposed framework can be used for analyses involving non-anonymous node features. I wonder how this framework can be leveraged to truly evaluate differences between various added features, such as SPD or resistance distance. In my view, although the broken symmetry introduced by these additional features is undoubtedly a source of improved expressivity, different features have varying degrees of power; some can help count more complex graph structures than others.

### Questions
See above.

### Soundness
3

### Presentation
4

### Contribution
2
