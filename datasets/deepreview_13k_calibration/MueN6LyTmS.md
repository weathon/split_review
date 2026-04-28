# Subequivariant Morphology-Behavior Co-Evolution in 3D Environments

- Decision: Reject
- Avg Score: 5.20
- Scores: 1, 5, 6, 6, 8

## Abstract
The co-evolution of morphology and behavior in 3D space has garnered considerable interest in the field of embodied intelligence. 
While recent studies have highlighted the considerable benefits of geometric symmetry for tasks like learning to locomote, navigate, and explore in dynamic 3D environments, its role within co-evolution setup remains unexplored.
Existing benchmarks encounter several key issues: 1) the task lacks consideration for spatial geometric information; 2) the method lacks geometric symmetry to deal with the complexities in 3D environments.
In this work, we propose a novel setup, named Subequivariant Morphology-Behavior Co-Evolution in 3D Environments (3DS-MB), to address the identified limitations.
To be specific, we propose EquiEvo, which injects geometric symmetry, i.e., subequivariance, to construct dynamic, learnable local reference frames, enabling the joint policy to generalize to diverse task spatial structures, thereby improving co-evolution efficiency.
Then, we evaluate EquiEvo on the proposed environments, where our method consistently and significantly outperforms existing approaches in tasks such as locomotion navigation and adversarial scenarios.
Extensive experiments underscore the importance of subequivariance for the co-evolution of morphology and behavior, effective morphology-task mapping and robust morphology-behavior mapping.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This submission proposed a strategy for morphology+control co-optimization that incorporates subequivariance-based geometric symmetry into the policy module as an inductive bias to accelerate training in 3D environments. This approach constructs a local orthonormal basis and projects sensing information with spatial properties such as velocity and position into this local basis to enhance the generalizability of the policy module over diverse transformations, particularly those that result from translations, rotations or reflections of the morphology or task.

### Strengths
Originality

This work provides an original extension to morphology+control co-optimization frameworks that explicitly address geometric symmetry in policy learning.

Quality and clarity

The authors made an effort to formalize their policy architecture with mathematical definitions, which should help reduce potential misunderstandings when others attempt to reproduce their results.

Significance

Co-optimization of morphology and control is an important longstanding unsolved problem. Supporting a diverse set of morphologies with a more efficient controller would reduce the time needed for designing morphology-specific network architectures. Attention and effort in this area has significance for robotics and other forms of "embodied intelligence".

### Weaknesses
Lack of novelty

The primary contribution of this work is a substitution of the reinforcement learning policy module from the Transform2Act approach with an equivariant GNN. Compared to the work cited by authors (Chen et al., 2023 https://arxiv.org/abs/2305.18951) (Chen et al., 2024 https://arxiv.org/abs/2407.12505), this submission appears to be a repackaging of an existing subequivariant reinforcement learning idea with a different problem setup. This submission reuses the same local reference frame (LRF) transformation as in https://arxiv.org/abs/2407.12505 with the same proof process in their appendix. As far as I can tell, the only appreciable difference is the addition of a relatively simple translation to the Og(3) setup in https://arxiv.org/abs/2407.12505 forming Eg(3). A more compelling contribution would include a demonstration of significant differences in results. While the authors claimed their setup can inject symmetry into generated morphological designs, their claim is not well supported.

Lack of evidence of generalizability

Although the symmetry enhancement is the core claim, improved symmetry was only explored within a single basic agent skeleton -- the ant morphology. There was no metric or quantitative analysis to test the consistency of symmetry improvement across varied morphologies, or how the improvement of implementing LRF transformation in the policy module affects the optimization algorithm. 
Without visualizations of generated morphologies from additional environments, and without a symmetry-based metric to measure the improvement across different setups, it is difficult to assess the claims of the submission.

Lack of experiment design and analysis

Following up on the above point, the only metric that was considered was reward. In two of the three explored benchmark environments (the humanoid and sumo) the morphology transformation was omitted and only attribute transformations were possible. In this reduced setting, it was unclear how morphology metrics changed over time (e.g. the limb lengths on both sides of the agent) should be readily available but was not extracted and analyzed. However the submission claims “integrating morphology evolution with sub-equivariance yielded a synergistic effect” (Sect. 4.3) which is not supported by the experiments and could simply be the policy network producing better control under LRF transformation that are independent of morphology.

Lack of clarity

The mathematical notation was inconsistent and rather confusing. For example, symbols like “m” are overloaded with different meanings across subscripts (equation 3), superscripts (equation 3), and variables (equation 9, 10, 11) without further clarification of meaning in a verbal format, which undermines the clarity of the theoretical framework. In addition to restructuring the mathematical framework and standardizing notion, explaining the symbols used in equations with natural language, a few words even, would improve clarity immensely -- a symbol table would be ideal.

### Questions
1. Can you provide a concrete analysis of the contribution of subequivariant policy in morphology evolution?

2. Can you provide morphology metrics figures over time? Such as the length of limbs, and compute the symmetric error of design by comparing the difference of limb length divided by total limb length? 

2. Can you analyze the features of the group of evolved morphologies at each point of the timeline using multiple trials, and explain how your policy module affects evolution?

3. Can you run experiments starting from different morphologies, and introduce varying levels of freedom (e.g. only allow attribute transform, allow attribute transform plus morphology transform with a certain degree, fully allow both) for each starting point?

4. Can you rewrite the equations, especially 7-17, and move unnecessary details to the appendix to clear space for more experiments?

### Soundness
2

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
The paper addresses the problem of learning control policies for embodied agents living in a 3D environment. It proposes a method for the co-evolution of the behavior policy and the morphology of the agent. The authors use subequivariant graphs for the state representation to take advantage of the symmetries of the tasks with respect to certain transformations (e.g., rotation, translation) and reduce the complexity of the problem. They further propose to use subequivariant graphs to represent the agent's morphology. The paper experimentally shows on three different tasks subequivariance and morphology transformations improve performance of the agent.

### Strengths
Integrating subequivariant graph neural networks with morphology-behavior co-evolution is an interesting experiment. The experiments show that both morphology transformations and equivariance contribute to the performance improvement over standard graph neural networks.

### Weaknesses
The exposition of the motivations, the methods and the results should be improved. I provide some examples. In the summary of the contributions. 3DS-MB is defines as a "benchmark", in the rest of the paper as a "method". I could not find where the authors define which symmetries the network and the morphology are invariant to. From the figures it seems that the ant evolves in a radially-symmetric way (figure 2), but then in figure 10 it seems to be laterally symmetric.

I find the premise of the paper surprising, as the second sentence of the abstract is "While recent studies have highlighted the considerable benefits of geometric symmetry for tasks like learning to locomote, navigate and explore in dynamic 3D environments, its role within co-evolution setup remains unexplored". Then the paper cites, in the first sentence of the introduction, Gupta et al. [1] and Dong et al. [2], which both describe an evolutionary experiment simultaneously improving the agent's policy and morphology *imposing bilateral symmetry of the agent* (cf. Unimal designed described in the paper). Maybe the authors mean that the studying the role of symmetry was not the focus of the paper, but their wording suggests something else. I recommend to clarify how the author's approach to symmetry in co-evolution differs from or extends beyond the bilateral symmetry used in the cited papers, and if the symmetry they impose is only in the state representation or also in the morphology transformations.

It is unclear when reading the paper which components of the design are novel and which have been taken from previous work. For example, in the section "Morphology transform", no previous paper is mentioned, but several papers cited in the introduction define similar or identical transformations. Instead, the authors write "We divide the morphology transform stage into two sub-stages", implying that is an idea of this paper. In general, it is very difficult to evaluate this paper because the design choices are not introduced in view of the related works. Similarly, how does the subequivariant graph neural network described in this paper differ from the ones used in [3] and [4]?

When I first read the paper, I misunderstood a central aspect of the paper. In the introduction, the authors write "An essential aspect of our approach is ensuring that the evolution of the morphology remains invariant to geometric transformations". At this point, one would expect the morphology transformations to be constrained by some kind of symmetry. Figure 1 and 2 also reinforce this misunderstanding: the morphology on the right (with subequivariance) looks symmetric (radially and laterally), while the one on the left is asymmetric. Instead, it seems to be that, while the representation is symmetric due to the subequivariance of the graph, the morphology transformations are not (figure 10). The authors should make these aspects clearer.

The experimental results do not compare the methods with previously introduced algorithms, they are rather ablation studies. They remove subequivariance, morphology transformations or both. However, the authors mention several previous works about morphology-policy co-evolution. As the initial motivation of the paper is that these methods underperform in 3D environments, they should prove this with experiments.

Overall, while the results are promising, unfortunately I think the paper is not ready for publication in its current state.

### Questions
* When the authors speak about "Morphology Value", do they mean a value function mapping the morphology to the expected cumulative reward? I agree that this should not depend on transformations of the environment such as rotations or translations, but a value of the morphology should not depend on the environment state in the first place. Or do the authors want to learn a value function for a specific morphology when the agent is in a given state? This part needs to be better explained.

* Is the "Local Reference Frame Canonicalization" a novelty of this work? No reference is given in that section, as well as no explanation as to why this canonicalization is performed.

* In the humanoid, why are only the attributes of the body's segments modified, and not the morphology? I believe the morphology changes would not work with the humanoid and I believe the authors performed this experiment, but omitted it from the paper.

* Can you explain the learning curves of Sumo? Why do they decrease at a certain point? In the text you write "The results emphasize the critical impact of subequivariance, which proved more influential than morphology evolution alone in enhancing performance". However, in the figure you only show two learning curves, Ant and EvoAnt.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces a  benchmark for subequivariant morphology-behavior coevolution and employs  graph neural networks to effectively integrate geometric symmetry. Overall, the approach is generally sound.

### Strengths
1.The proposed method is both reasonable and meaningful for the co-evolution of morphology and behavior in 3D space.

2.The authors conduct extensive ablation experiments to validate the contributions of each module.

### Weaknesses
1.The main algorithmic contribution of this work is the introduction of geometric symmetry into the formulation of co-evolution. However, geometric symmetry is a widely recognized concept for enhancing the sample efficiency of interactive learning methods, such as reinforcement learning, making the contribution appear modest.

2.The paper claims to address the lack of spatial geometric information consideration in tasks, yet the navigation environments used in the experiments are relatively simple and lack significant geometric complexity. Real-world navigation tasks typically involve obstacles. The reviewers would appreciate seeing ablation studies in navigation scenarios with obstacles to further demonstrate the proposed method's effectiveness.

3.The co-evolution of morphology and behavior is tested on only two robots, a humanoid and a spider. Could the authors conduct experiments with additional robots, such as a half-cheetah?

### Questions
1.The importance of co-evolution and its practical applications should be clarified in the introduction, as it currently appears somewhat niche.

2.Figure 1 does not effectively convey the concept of subequivariance, and the depiction of successful and failed scenarios is confusing (e.g., why is the left scenario a failure and the right a success?).

3.Figures 7, 8, and 9 indicate that some methods continue to show improvement even after the training process reaches 100%. Why are results from additional training rounds not presented?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces Subequivariant Morphology-Behavior Co-Evolution in 3D Environments (3DS-MB). It further proposes a novel co-evolution approach named EquiEvo, which exploits the geometric symmetries within the proposed task environment to better navigate directional complexities and ensure invariant morphological evolution. Specifically, a local reference frame (LRF) is first predicted from original observations via subequivariant message passing mechanisms, and then the observations are projected into this LRF coordinate so that they become invariant. The authors validate the indispensability of subequivariance modeling for morphology-behavior co-evolution in complex 3D environments. The authors make non-trivial contributions, as they both propose to characterize the directional complexities in 3D environments and present an efficient and generalizable co-evolution framework to tackle this challenge.

### Strengths
1.This paper is concisely written and generally easy to follow. The authors clearly state their motivation, including (1) existing 3D benchmark environments lack a reflection of complex spatial geometric structures, and (2) existing co-evolution approaches insufficiently exploit the symmetries in these structures, hence greatly helping with the reader’s understanding of their contributions.

2.The authors present comprehensive experimental results. They not only demonstrate the effectiveness of subequivariance modeling, but also investigate its impact on different model components (such as actor and critic) and compare against hand-crafted normalization methods. The results regarding morphology-task mapping and morphology-behavior mapping are also quite interesting. 

3.I appreciate that the authors provide detailed proofs of the invariance of LRF canonicalization and EquiEvo.

### Weaknesses
1.The paper implicitly assumes some prior knowledge of subequivariant graph neural networks on the reader’s side. Some of the mathematical notations and formulae (such as the stack of equations on page 5) might need some further clarification so that they are more understandable. Specifically, the use of abstract group theory concepts without sufficient grounding in the context of the specific graph neural network architecture makes it difficult to follow the derivation of the subequivariant message passing mechanism. For instance, the precise meaning of the group action on the node features and edge attributes is not immediately clear, and the connection to practical implementation details is missing.

2.I find that the authors did not mention the architectures of the morphology transform policy and “conventional neural networks” involved in behavior control and value estimation. The exact process of morphology transform (such as the actions taken and attributes being transformed) is not explained either. If these design choices are identical to some previous work, I suggest that the authors cite the related papers so that readers could refer to them for more details. The lack of detail makes it difficult to reproduce the results and assess the impact of specific architectural choices on the overall performance. For example, are the morphology changes discrete or continuous? What is the dimensionality of the action space for the morphology transform policy? How does the network architecture for the actor and critic handle the variable morphology?

### Questions
1.Regarding Figure 5, is it that each pair of agents are trained simultaneously and competing against each other? There are some cases where the win rates of both opponents decrease with the training process. Could you further explain how this should be interpreted?

2.The authors did not mention any publicly accessible code repository in the paper or supplementary material. Do you have any plan to open source your code and environment? 

3.The baseline algorithms seem a bit simple, more like ablated versions of your proposed method. I wonder how your RL approach compares with evolutionary algorithms (EAs), such as Neural Graph Evolution, in terms of morphological evolution. From my understanding, the control algorithm that you propose could be readily combined with any of those EAs, serving as inner-loop fitness evaluation. Did you carry out any comparison like this? 

Thank you!

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
1

### Summary
Sorry I know nothing about this field so I can't give a reasonable review. please just ignore my review.

### Strengths
- The paper is well-written and easy to follow.

### Weaknesses
none

### Questions
none

### Soundness
3

### Presentation
3

### Contribution
3
