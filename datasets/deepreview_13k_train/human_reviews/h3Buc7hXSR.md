# Consistent Symmetry Representation over Latent Factors of Variation

- Decision: Reject
- Scores: 3, 6, 6, 3

## Abstract
Recent symmetry-based methods on variational autoencoders have advanced disentanglement learning and combinatorial generalization, yet the appropriate symmetry representation for both tasks is under-clarified. We identify that existing methods struggle with maintaining the $\textit{consistent symmetries}$ when representing identical changes of latent factors of variation, and they cause issues in achieving equivari-
ance. We theoretically prove the limitations of three frequently used group settings: matrix multiplication with General Lie Groups, defining group action with set of vectors and vector addition, and cyclic groups modeled through surjective functions. To overcome these issues, we introduce a novel method of $\textit{conformal mapping}$ of latent vectors into a complex number space, ensuring consistent symmetries
and cyclic semantics. Through empirical validation with ground truth of factors variation for transparent analysis, this study fills two significant gaps in the literature: 1) the inductive bias to enhance disentanglement learning and combinatorial generalization simultaneously, and 2) well-represented symmetries ensure significantly high disentanglement performance without a trade-off in reconstruction error, compared to current unsupervised methods. Additionally, we introduce less guidance-dependent validation results, extending our findings to more practical use. Our research highlights the significant impact of verifying consistent symmetry and suggests required future research for advancing combinatorial generalization and disentanglement learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper analyzes disentanglement learning and combinatorial generalization from the perspective of designing equivariant latent spaces. They define a desirable notion of “consistent symmetry”, which autoencoders trained to equivariantly encode data arising from “latent factors of variation” should satisfy, but show that several choices of latent space cannot satisfy this property. Instead, they propose a method, CMCS, which more carefully designs the latent space (on which the latent factors — modeled as a direct product of cyclic groups — are encouraged to act via addition by the loss function). Overall, it consists of mapping real-valued scalar latents to complex numbers, some kind of grid selection, a choice of action of the cycle group (the step size), and a loss function that encourages the group action on the latent space to be respected. Their method works well on experiments testing disentanglement learning and combinatorial generalization.

### Strengths
The authors show that previous approaches to disentangled representations lack the consistent symmetry property, so their results are relevant to existing literature. Moreover, they suggest a novel alternative, which outperforms previous work on their experiments in both the reconstruction loss and disentanglement learning. At a very high level, these seem like valuable and original contributions. However, as detailed below, the presentation of the work needs such improvement that I can’t really understand exactly what the consistent symmetry property even is, how trivial or non-trivial the impossibility results are, or what their method is doing. I hope the rebuttal will clarify these points.

### Weaknesses
1. The presentation of the paper is unfortunately very poor. For example, key concepts such as “combinatorial generalization” and “latent factors of variation” are used without explanation, or motivation. Related works are cited, but not explained or summarized, in the introduction. Figure 2 needs a more detailed caption. The presentation of concepts is not mathematically precise, which makes them nearly impossible to understand (see questions). For example, even the definition of Consistent Summary before Section 2.2 is difficult to parse. For this reason, it is possible I have not understand all of the contributions of the paper fully, and I hope the authors’ response will clarify. At the least, the paper would need to be very substantially rewritten (in my opinion) for it to be clear and precise enough for publication.
2. Since disentanglement and latent factors of variation are not motivated or defined, it is difficult to assess the significance of this work, or the novelty of the proposed method.
3. Other writing notes: the datasets should be explained briefly in the main body, not relegated to the appendix, to orient the reader before showing results — especially for a 10 page submission. This is important for evaluating the results. It would also be good to define “conformal” (unless I missed it somewhere).

### Questions
1. I don’t understand Figure 2. Are the red arrows supposed to indicate inequality? Why are they different shades of red? The only difference between the left, inconsistent case and the right, consistent case are the arrow colors and the labels on the group elements, but I don’t understand the significance of these differences.
2. I don’t understand the definition of Consistent Symmetry. Is it a specific group element? A property of a model? Mathematically, what does it mean? Intuitively (eg with a concrete example), what does it mean? Perhaps it would also be helpful to formally define “representing the cyclic semantics of a dataset with consistent symmetries”. What is the “pair of latent factors”?
3. Is it possible to define consistent symmetry in terms of the equivariance of $\Lambda$, by choosing the right group (perhaps $G_F \times G_z$ and group action?
 4. How realistic is the assumption that the group acting on the latent factors of variation is the direct product of cyclic groups, especially of known dimensionality and number? 
5. One could imagine a latent factor of variation changing with respect to permutations, $S_n$. Assuming it doesn’t cover 100% of cases, would either the impossibility results or the improved method by extensible to a direct product of different groups?
6. At a high level, what is it about the proposed method that circumvents the impossibility result of Theorem A.9 (which also uses the action of addition)? 
7. What is the proof technique behind the impossibility results? Is there intuition that can be put in the main body of the work? 
8. What exactly is the fixed codebook and fixed grid doing? A figure might be helpful. 
9. What does conformal mean in this context? Why is it a useful property for the mapping to have?

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
The paper proposes a method for learning disentangled representations in variational autoencoders by enforcing consistent symmetry representations through conformal mapping to circular latent spaces. The authors identify limitations in existing approaches using matrix exponentials, vector addition, and surjective mappings, and propose a solution using the Cayley transform to map latent vectors to the unit circle. The method is evaluated on three datasets (dSprites, 3D Shapes, and MPI3D) and shows improvements in both disentanglement metrics and combinatorial generalization tasks.

### Strengths
The paper is generally well-written with clear figures, and makes a good connection between theoretical framework and experimental validation. 

- Identifying the importance of consistency in how transformations are represented
- Attempting to bridge disentanglement and combinatorial generalization through symmetry
- Provides a concrete solution for maintaining cyclic behavior in latent spaces
- The Cayley transform implementation, while overcomplicated, is mathematically valid for their restricted setting
- The experiments have comprehensive evaluation using multiple metrics
- Clear demonstration of improvements in their specific setting
- Good ablation studies showing the impact of different components

### Weaknesses
The theoretical framework is limited to independent cyclic symmetries, and the mathematical treatment contains several confusing or incorrect formulations. While the paper shows promising results for simple cyclic transformations, it carefully avoids more challenging cases like coupled symmetries or full 3D rotations, where the proposed method would face fundamental topological limitations.
If the paper would admit to these restrictive simplifications, it could be presented as a first step for cases where single latent dimensions represent disentangled reps.
In detail, my issues are: 

1. Theoretical Framework:
- The mathematical treatment of Lie groups and their actions is confused, particularly in their handling of $GL'(n)$ and matrix exponentials
- The fundamental assumption that symmetries must act on single dimensions is too restrictive and ignores basic topological constraints (e.g., impossibility of faithfully representing $SO(3)$, i.e. symmetries of 3D objects, through independent $SO(2)$ actions, i.e. the largest compact group that can act on a single latent dim.)
- The "conformal mapping" solution is unnecessarily complicated for what is essentially just mapping to circular latent spaces

2. Limited Scope and Misleading Presentation:
- The method only handles independent cyclic symmetries, but this crucial limitation isn't clearly acknowledged
- Dataset choice carefully avoids challenging cases (like full 3D rotations) that would reveal the method's limitations
- Presents as a general solution for symmetries in latent spaces when it's actually quite restricted

3. Novelty and Positioning:
- Insufficient discussion of prior work on group actions in latent spaces
- Doesn't clearly position their contribution relative to existing symmetry-based approaches
- The core idea of using group actions for consistent representations isn't novel (Caselles-Dupré et al "Symmetry-based disentangled representation learning requires interaction with environments." NeurIPS 2019), though their specific implementation for cyclic groups is

4. Technical Issues:
- Several confusing or incorrect mathematical formulations, particularly in Section 2 (see below) 
- The proofs about limitations of existing methods are flawed due to overly restrictive assumptions
- The "consistent symmetry" definition could be much more simply stated

5. Experimental Validation:
- Results are only shown for cases that fit their restricted framework
- Missing experiments with more challenging symmetries (e.g. more general 3D rotations). 
- No comparison with methods specifically designed for handling group actions

### Technical Issues details

1. Mathematical Formulation Problems:
- Proposition 2.1 and related theorems contain serious mathematical confusions:
  * Mix up elements of Lie groups with elements of Lie algebras
  * Write nonsensical equations like $e^g z = eIgz + v'$ where exponentials are applied inconsistently
  * Attempt to exponentiate group elements rather than Lie algebra elements
  * Fail to properly distinguish between matrix exponential and scalar exponential

2. Flawed Analysis of Matrix Groups:
- Their critique of using $GL(n)$ ignores well-known solutions in Lie theory:
  * Don't consider proper compact subgroups like $O(n)$ where cyclic behavior is natural
  * Miss the fact that elements of $\mathfrak{so}(n)$ can easily generate cyclic groups via exponential map
  * Make unnecessarily strong claims about limitations without considering standard constructions

3. Restrictive Definition of Disentanglement:
- Their requirement that group actions affect single dimensions only is mathematically naive:
  * Ignores fundamental topological obstructions
  * Cannot represent natural symmetries like $SO(3)$ which require coupling between dimensions
  * Confuses independence of factors with independence of dimensions

4. Overcomplicated Solutions:
- Their "conformal mapping" solution is an elaborate way to implement simple circular topology
- The proofs about limitations of existing methods could be greatly simplified if they stated their assumptions clearly
- The mathematical machinery introduced is disproportionate to what's actually being done (mapping to $S^1$)

### Questions
1. Why do you require symmetry transformations to act on single dimensions of the latent space? This seems unnecessarily restrictive and rules out many natural symmetries (like 3D rotations) that inherently couple multiple dimensions. Have you considered defining disentanglement in terms of independent factors rather than independent dimensions?

2. In Proposition 2.1 and surrounding theorems, your treatment of matrix groups and exponential maps is unclear. Could you clarify:
   - What exactly is $GL'(n)$ and how does it relate to the Lie algebra $\mathfrak{gl}(n)$?
   - Why do you apply exponential maps to group elements rather than Lie algebra elements?
   - How do you justify the equation $e^g z = eIgz + v'$?

3. Your experiments with 3D shapes use very restricted rotations (15 discrete values). Have you considered testing your method on datasets with full SO(3) rotations? This would seem important given that many real-world applications involve unrestricted 3D transformations.

4. Your framework seems to work well for cyclic, independent transformations, but many real-world symmetries don't decompose this way. Have you explored how your method might be extended to handle more general group actions, or is the restriction to independent cyclic groups fundamental to your approach?

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
3

### Summary
This paper addresses the challenge of achieving consistent symmetry representation, where identical semantic transformations are represented consistently via an isomorphism $\Gamma: G_F \to G_z$, where $G_F$ denotes the group of cyclic semantic transformations and $G_z$ represents its corresponding representation. The authors argue that conventional symmetry-aware representation methods, such as matrix Lie groups, vector addition, or surjective mappings, do not ensure the consistent symmetry representation. To address this, they introduce Conformal Mapping for Consistent Symmetries (CMCS), a method that maps latent variables to the complex plane using conformal mappings, thereby establishing a cyclic group action on a fixed grid (a codebook for symmetries). The proposed model operates under three scenarios: ground truth (where the symmetry information is accessible), supervised, and semi-supervised (where symmetry information is extracted from labels). Experimental validation on standard benchmarks like dSprites and 3D Shapes demonstrates that CMCS outperforms baseline models in both combinatorial generation and disentanglement learning tasks.

### Strengths
The paper is well-motivated and interesting. It demonstrates that the inductive biases frequently used in previous symmetry-aware representations are insufficient to satisfy the consistency symmetry condition, and proposes how to efficiently improve them.
***
The proposed method, CMCS, appears novel. I find the use of conformal mapping to represent real space latent variables in the complex plane and define group action through this approach to be sufficiently novel and technically sound. The conformal mapping-based representation suggested by the authors seems promising, with various potential applications, and I would like to rate it highly for novelty. However, as I have not exhaustively reviewed related literature, this evaluation may be subject to adjustment.
***
The experimental results of this paper leave me with mixed feelings. The main methodology of this paper is based on ground truth-based or supervised/semi-supervised learning, yet it is primarily compared with unsupervised learning methods, which gives a somewhat unfair impression (e.g., Table 2). However, the paper’s main claims are effectively demonstrated experimentally, specifically (1) that existing approaches for handling symmetry (e.g., GL(n)) are not sufficiently efficient (e.g., Table 3) and (2) that the proposed CMCS can go beyond the Pareto front in the reconstruction-dismantlement trade-off (e.g., Figure 7).

### Weaknesses
The proposed method relies heavily on guidance (ground truth or labels) for learning symmetry, raising questions about the fairness of comparing it with other unsupervised learning-based approaches. Although the authors propose a semi-supervised method, they still assume that 50% of the data is labeled, significantly higher than the label proportion typically used in most semi-supervised and unsupervised learning studies.

### Questions
Could the authors evaluate the performance variation of CMCS-Semi by adjusting the accessible label ratio $p$? I believe demonstrating robust performance even at a low $p$ would strengthen the authors' claims significantly.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper discusses the problem of symmetry-based representation learning. It argues that existing methods cannot obtain *consistent symmetries*, as defined in Section 2.1, and proposes the use of conformal mapping between the real space and the angle space to learn consistent symmetries.

### Strengths
The paper targets an interesting problem, symmetry-based representation learning. It develops a method to achieve disentanglement into single dimensions for each of the cyclic variation factors, which requires additional care in constructing a bijective mapping between the real space and the angle space.

### Weaknesses
The authors discuss some limitations of some previous works in disentangled representation learning in Section 2.1-2.2. However, as far as I could understand, the authors seem to have some fundamental misunderstanding about the settings and assumptions in these related works. Such misunderstanding leads to conclusions e.g. in Prop 2.1, Thm 2.2, and Thm 2.3, which do not make any sense to me. In particular,
* L107: the authors assume that the latent space can be decomposed into single dimensions $Z_i = \mathbb R$, each of which is acted on by a separate group $G_i$. This is not the setting in Higgins et al (2018), or any of the other related works mentioned in L138 (Miyato et al 2022, Marchetti et al 2023). The standard setup is that $Z = \oplus Z_i$, where each $Z_i$ can be a **multi**-dimensional vector space and is acted on by a group $G_i$. **My main objection to this paper is about this setup, and most of my following comments are related to this.** If I've misunderstood it, or if the authors think this should indeed be the correct setting to consider, please point it out before all others and I'm happy to have further discussion.
* Prop 2.1, Thm 2.2-2.3: Under the assumption in L107, it goes without saying that there is not a valid and nontrivial group action (for a cyclic group) on the latent space $Z = {\mathbb R}^{\oplus n}$. This is not a limitation of the general linear group, but rather how you have chosen to construct the latent space. Just consider the simplest case when there is only one factor of variation, $Z = \mathbb R$ and $G = SO(2)$. There is no nontrivial $G$-action on $Z=\mathbb R$, but the problem no longer exists if you allow a 2-dimensional latent space $Z=\mathbb R^2$. Also, the exponentiation of a group element ($\exp(g)$) in L145 does not make sense.
* To sum up the previous point, although Prop 2.1, Thm 2.2-2.3 might be correct, it does not offer any insight because it is based on a quite limiting assumption about the structure of the latent space, which is not used in any other related work. Also, these statements have been made in an unnecessarily complicated way with lengthy proofs, while they only reveal a self-evident fact.
* Thm 2.4: same as above - you simply cannot represent a cyclic group in $\mathbb R$. Besides, Thm 2.4 states that "if the group action is defined as $\alpha(g, z_i) = g + z_i$, which is not even a valid definition of group action of a cyclic group ($\alpha(g_1g_2, z) \not= \alpha(g_1, \alpha(g_2, z))$). I also don't find any evidence in Hwang et al (2023) that group action is defined as such vector addition.
* Cor 2.5: I don't know how to read it because symbols like $\mathcal Y$ and $\Gamma'$ are not defined nearby or in the symbol table.

Then, the method is developed based on the assumption that each single dimension in the latent space has to correspond to a factor of variation. Based on this setup, I do believe the method makes sense and addresses the limitations of this setup. However, as I've pointed out earlier, all these efforts may not be necessary since we can decompose the latent space in another way. The most straightforward solution is to replace each component $\mathbb R$ with $\mathbb R^2$ or possibly $\mathrm{SO}(2)$, which does not require constructing the conformal mapping to a complex space and mapping it back to $(\pi, \pi]$. Many other related works take a similar approach to this [1,2,3]. These works should be discussed in more detail and compared through experiments in the revised paper if possible.

The experiment results look great at first sight. However, it seems that all comparisons are still made under the limiting setup that each factor of variation can only be represented in one dimension. I feel this would limit the capability of the baseline models. It would be great to compare with some other related works that do not enforce this limitation [1,2,3].

* L120: How you describe the concept of inconsistent symmetry seems a bit confusing to me. I think for a specific task we have a fixed symmetry group $G$, and the difference is really just the different group actions on different spaces. E.g. the group acts on $F$ through an action $\alpha_F$, while it acts on $Z$ with a different action $\alpha_Z$. The current notation ($g_z', g_z''$) may suggest there are different groups and group elements, which may not be the clearest way to explain it.
* L125: Following the point above, confusion arises when you define the consistent symmetry as $g_z = \Gamma(g_F)$. But why can't this also represent the inconsistent symmetries shown in Figure 2? Concretely, $F = \{F_0, ..., F_3\}$, $Z = \{Z_0, ..., Z_3\}$, $G_F = \{ g_F^0, g_F^1, g_F^2, g_F^3 \} $ and $G_z = \{ g_z^0, g_Z^1, g_Z^2, g_Z^3 \}$. $g_F^k$ acts on $F$ by $F_i \mapsto F_{i+k}$, where $+$ is the addition modular $4$. Similarly, $g_z^k$ acts on $Z$ by $z_i \mapsto z_{i+k}$. These actions are both regular, and $\Gamma$ is simply $g_F^k \mapsto g_z^k$, which is irrelevant to how $z_i$'s are positioned on the circle in Figure 2.
* L138: GL(n) stands for general linear group. The term "general Lie group" is misleading.
* L141: "Let assume..." --> "Assume..."
* L143: The notation $GL'(n)$ does not make sense to me.
* L145: The exponential map is rarely, if ever, denoted by a bold $\mathbf e$. Use $\exp$ or simply $e^\cdot$ for matrix exponential.
* L750: $\mathfrak g$ is commonly used to refer to the Lie algebra, instead of its elements.
* Eq (8): why does the group action output a row vector? Shouldn't it be $\alpha(g, \mathbf z) = g\mathbf z$, as in Proposition A.1?
* Tab 2&3: The metrics (beta-VAE, FVM, MIG, DCI) are not explained.

### Questions
* Can you explain the differences between your experiment results and those reported in MAGANet? E.g. the results in Table 1 (dSprite), do not match those in Table 1 in the MAGANet paper.

### Soundness
1

### Presentation
1

### Contribution
1
