# Learning Molecular Symmetry Breaking via Symmetry-adapted Neural Networks

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
E(3)-equivariant neural networks have achieved remarkable performance in molecular modeling. However, the equivariance constraint limits the model's effectiveness in learning tasks involving symmetry breaking, particularly those that violate the celebrated Curie principle. Relaxing the equivariance constraint is essential for addressing these challenges. In this paper, we explore the intricate symmetry relationships between an object and its spontaneously symmetry-broken outcomes. We introduce a relaxed equivariance based on the molecule's inherent symmetries. Additionally, we develop SANN -- a symmetry-adapted neural network architecture that learns symmetry breaking through equivalence classes of atoms. SANN decomposes the molecular point cloud into sets of symmetry-equivalent atoms and performs message-passing both within and across these classes. We demonstrate the advantages of our method over invariant and equivariant models through synthetic tasks and show that SANN effectively learns both equivariance and symmetry breaking in various benchmark molecular modeling tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a method to handle molecular modeling tasks that involve symmetry breaking—a phenomenon where a system transitions from a state with high symmetry to one with lower symmetry. Traditional equivariant models may struggle with spontaneous symmetry breaking (SSB) due to the constraints of equivariance. The proposed model decomposes molecules into symmetry-equivalent atom classes and performs message-passing within and across these classes. The paper also proposes a new symmetry-breaking measure (SBM) as a loss function to account for ambiguous outcomes in SSB. The author evaluate their model on synthetic tasks and molecular benchmark QM7-X.

### Strengths
The paper’s theoretical framework for spontaneous symmetry breaking (SSB), relaxed equivariance, and the proposed symmetry-breaking measure (SBM) is well-developed and accessible.

### Weaknesses
The significance of symmetry breaking in related fields, while highlighted, remains somewhat unclear. Both the number and scale of real-world experiments are limited. The authors attribute this to the lack of accessible datasets, but further evidence demonstrating the importance of symmetry breaking in relevant domains would strengthen the argument that this is not merely an edge case.

Convincing and concrete evidence of the importance of symmetry breaking and the paper's contributions would be demonstrated by improved performance on real-world tasks where most current state-of-the-art models struggle. However, the experimental evaluation on the real-world dataset, QM7-X, includes only Schnet and EGNN as baselines, omitting comparisons with many recent state-of-the-art equivariant models. This significantly weakens the empirical support for the contribution.

In addition, the weakness highlighted by my fellow reviewers raised my concern regarding the novelty of the work. E.g., the authors claimed that "we propose a new symmetry breaking measure (SBM)" and even listed this as the first point of the contribution in their initial submission. But Reviewer SA1v pointed out that this has already been proposed by previous work and wasn’t acknowledged. While this was corrected in the revised version, the novelty of the work is thus limited.

### Questions
Could the authors kindly provide more concrete evidence where symmetry breaking plays a critical role in molecular modeling tasks?

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
3

### Summary
The paper proposes a method to relax equivariance constraints in molecules by utilizing a canonicalization technique and a modified loss function. This approach targets scenarios where symmetry breaking occurs, specifically based on the Curie principle.

### Strengths
The paper effectively shows the advantages of its approach using synthetic tasks and QM7-X dataset, illustrating improvements over equivariant models.

### Weaknesses
 - The paper lacks evaluations and comparisons to a broader range of baseline models. While it compares its results against EGNN and SchNet, multiple equivariant models in the literature are not considered.

- The experimental setup and model evaluation could be expanded to include more benchmarks beyond QM7-X to fully assess the generalizability of the proposed approach.

- The claim that this is the first work that tackles symmetry breaking in molecules needs to be revised, considering some works in the literature (1, 2, 3), and the paper already cited on crystals (4). Furthermore, the statement 'the first explicit construction of equivariant neural networks that enable learning SB leveraging molecular inherent symmetries' is not fully supported given the existing literature.

### Questions
The authors claim this is the first work that tackles symmetry breaking in molecules. I think this needs to be revised, considering some works in the literature (1, 2, 3), and the paper already cited on crystals (4).

1. Presilla, Carlo, and Jona-Lasinio, Giovanni. "Spontaneous symmetry breaking and inversion-line spectroscopy in gas mixtures." Physical Review A, vol. 91, no. 2, Feb. 2015

2. Goryachev, A.B., and Leda, M. "Many roads to symmetry breaking: molecular mechanisms and theoretical models of yeast cell polarity." Molecular Biology of the Cell, vol. 28, no. 3, Feb. 2017

3. Langer, Marcel F., Pozdnyakov, Sergey N., and Ceriotti, Michele. "Probing the effects of broken symmetries in machine learning." 2024

4. Wang, Rui, Hofgard, Elyssa, Gao, Han, Walters, Robin, and Smidt, Tess E. "Discovering Symmetry Breaking in Physical Systems with Relaxed Group Convolution." 2024

### Soundness
2

### Presentation
3

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
It is worth noting that this paper lies primarily outside my area of research. Consequently, I will refrain from making strong judgments on its novelty and significance, as I am less familiar with this specific field and its literature.

This paper addresses spontaneous symmetry breaking (SBB) in AI-driven molecular modeling tasks. It introduces a novel loss function designed for SBB scenarios, which accounts for the inherent ambiguity in symmetry-breaking outcomes. To achieve relaxed equivariance, the paper proposes a specific canonicalization of the learnable model. Additionally, it presents a new message-passing framework, the Symmetry-Adapted Neural Network (SANN), that passes messages within and across sets of symmetry-equivalent atoms, respectively, followed by aggregation of information to capture the global features of molecules. Finally, several experiments on synthetic tasks are conducted, showing that SANN significantly outperforms the tested baselines.

Overall, I recommend acceptance and would consider raising my score even further if the authors successfully address my feedback.

### Strengths
* Well-written with a clear and logical structure
* Effective and informative figures and illustrations
* Provides solid background on the algebraic foundations relevant to this work
* Introduces an innovative message-passing framework

### Weaknesses
 * Stronger baselines should be considered. For instance, many approximate equivariant models are now available and may perform significantly better on SBB tasks compared to strictly equivariant counterparts.
* Depending on the symmetry group, calculating the symmetry-breaking measure in Equation 3 might not be straightforward by simply evaluating the metric \( m(x,y) \) for each element in the group. How would this measure be computed in such cases? Or does this paper only consider finite groups? This needs to be clarified in the discussion.
* Although the paper is well-structured and provides essential foundational context, it lacks an explanation of why the proposed message-passing framework can address spontaneous symmetry breaking. This point requires further discussion in the paper.
* The figures illustrating symmetry-breaking concepts are excellent. An additional illustration that explains the proposed message-passing mechanism would also be very helpful.

Minor Issues
* Define the Earth Mover’s Distance, as it may be unfamiliar to some in the ML community.
* Further motivation for the proposed SANN architecture would be beneficial. For example, why is self-attention introduced only in the third part, rather than earlier in the message-passing process?

### Questions
How are the underlying graphs in the experiments constructed? Are they based on nearest neighbors, and what influence does the radius parameter have on performance? Clarification on this in the paper would be beneficial.

Additional questions are noted under the Weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to examine the problem of symmetry breaking with equivariant neural networks in molecular regression tasks. For symmetric molecules, equivariance will force the output to have the symmetries as the input to the neural network, which sometimes limits the ability of a neural network to perform certain predictions. To tackle this problem, the authors propose to use adapted loss functions that are invariant to input stabilizers. They also suggest using relaxed equivariant prediction networks for this setting, which can be obtained through canonicalization. In practice, this is achieved with a canonicalization scheme based on asymmetric units. Experiments show that method used can break symmetries better than a combination of an equivariant neural network and an MLP and that the invariant loss helps significantly with learning.

### Strengths
- The work tackles an interesting problem with potentially important applications. The problem of symmetry breaking of equivariant neural networks has been discussed before, but not particularly its implications on molecular prediction tasks.
- The paper is mostly clear and easy to understand. The figures are also welcome and useful

### Weaknesses
 **Major**
1. *Novelty and acknowledgment of previous work*
- I think there is generally an issue with this paper in terms of claiming novelty for things that were proposed in previous works and correctly acknowledging previous contributions.
- The most important case of this is the loss function Eq.3, which was already proposed and discussed by Xie and Smidt 2024. This is not acknowledged and is claimed to be an original contribution of the paper. The paper should be updated to not claim that this is an original contribution, and to correctly acknowledge Xie and Smidt 2024.
- The paper "Symmetry breaking and equivariant neural networks" (Kaba and Ravanbakhsh 2023) introducing relaxed equivariance as a solution to the symmetry breaking problem is also not mentioned although related. It should be mentioned and discussed.
- It also seems to me that there are instances in the paper where appropriate citations is not given to the right papers. For example, Baker et al. 2024 did not introduce either canonicalization or relaxed equivariance, yet the way in which the paper is cited seems to suggests that.
- I generally suggest to expand the related works section to discuss what solutions were previously proposed to the symmetry breaking problem and how the proposed one differentiates itself from these methods. For example, it is said that "[other] approaches are not applicable to learning symmetry breaking". What does that mean and how is that so, given the proposed method is based on canonicalization which is one of these other approaches?
2. *Incomplete experimental evaluation*
- I found that the baselines specifications was incomplete. I did not see explained in the paper what SchNet + MLP or EGNN + MLP means in terms of implementation. The fact that these models struggle on all tasks seems to indicate that they are simply not appropriate baselines. I suggest that the authors instead compare with Hofgard 2024 et al. or Lawrence et al. 2024 instead.
- An simple baseline that the should be compared against is simply symmetry breaking by adding noise to the inputs and then using an equivariant neural network.
3. *Regarding the method*
- The loss eq.3 seems of limited usefulness in practice. First it requires to find the stabilizer of all inputs, which may be costly. Second, and more importantly, its computation involves a potentially expensive optimization procedure especially if the stabilizer is large. Note that these limitations were already mentioned by Xie and Smidt 2024, I therefore find surprising that they are not at least discussed here. I think these limitations should be discussed as well as providing an analysis of computational cost.

**Minor**
- I did not find Figure 2 completely clear, what symmetry exactly is broken?
- The introduction mentions "crystal material melting" as an example of symmetry breaking. I think this is confusing/not accurate. Melting restores symmetry and does not break it. I suggest the authors precise this or use another example instead.
- Section 6.1 mentions "the Heisenberg uncertainty principle" as reason for why molecules are in constant motion and why the normal modes are of interest. I don't think that this is accurate, I suggest that the authors remove this reference.

### Questions
- I don't understand exactly why EMD was chosen as loss function and how it is computed.
- Could the authors explain how the QM7-X dataset was curated. What proportion of the data was retained? How does the method compare with baselines on the full dataset?
- As discussed in the paper and in previous work, canonicalization is sufficient to break symmetry. The additional clustering procedure based on equivalence classes is therefore not related to the symmetry breaking problem. I am therefore questioning the necessity of that design choice, what is the motivation? It is also necessary to perform ablation studies to understand the impact of that choice on result compared to simply using a message passing scheme.
- The term "non-functional" is used a few times? What is meant by that?
- I find the first paragraph of page 5 confusing. In particular, the statement "these outputs shared the same reduced symmetry" is not clear since the symmetry groups are not the same. They are conjugate, but that is the case for any objects in the same orbit. The fact that the rectangles in the example share the same symmetry is an accident, you could imagine a similar example with triangles where this would not be true anymore.

### Soundness
3

### Presentation
2

### Contribution
2
