# Designing Mechanical Meta-Materials by Learning Equivariant Flows

- Decision: Accept
- Scores: 5, 6, 8, 5

## Abstract
Mechanical meta-materials are solids whose geometric structure results in exotic nonlinear behaviors that are not typically achievable via homogeneous materials. 
We show how to drastically expand the design space of a class of mechanical meta-materials known as \emph{cellular solids}, by generalizing beyond translational symmetry.
This is made possible by transforming a reference geometry according to a divergence free flow that is parameterized by a neural network and equivariant under the relevant symmetry group. 
We show how to construct flows equivariant to the space groups, despite the fact that these groups are not compact.
Coupling this flow with a differentiable nonlinear mechanics simulator allows us to represent a much richer set of cellular solids than was previously possible.
These materials can be optimized to exhibit desirable mechanical properties such as negative Poisson's ratios or to match target stress-strain curves.
We validate these new designs in simulation and by fabricating real-world prototypes.
We find that designs with higher-order symmetries can exhibit a wider range of behaviors.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper is unclear, but to the best I can understand, the authors investigate an approach to perform inverse design of mechanical metamaterials by utilizing crystallographic symmetry groups.

### Strengths
1) Methods to solve inverse problems in the sciences is an important open problem.  
2) Building models/methods that leverage symmetry is potentially interesting approach.

### Weaknesses
1) Lack of clarity.  Based upon the introduction, I have only a very vague idea of what the authors are proposing, or why they are proposing it.  Specifically, the problem setting is not clear, there is little/no discussion of existing methods to solve the problem, and the limitations of existing methods are also unclear.  These problems make it very difficult to review the work.    
a) Line 39: "Existing approaches to cellular solids..".  What is an "approach" to cellular solids referring to?...an approach to what? 
b) Line 45: What is "shape optimization"?  We're optimizing the shape for what purpose? This is machine learning conference, and this topic might not be clear to your audience (e.g., me). 
c) Line 48: The authors begin talking about their solution, but it is unclear at this point (i) what problem they're trying to solve, (ii) what approaches exist to solve this problem, and (iii) how using "flow" is going to mitigate these problems.  
d) Line 48:  What exactly is "flow" in this context?   I see there is a "Related Work" section at the end of the paper, and it cites three papers that the authors claim have studied "Neural network flows" in recent years, however, I looked at the most recent of these cited references, Cranmer et al. 2020, and the word "flow" is never mentioned.  It remains unclear to me what exactly the authors are discussing. 

2) The authors present some results with their approach, but there is no mention or comparison with any other existing approaches.

3) Line 44 - 47: The authors write "recent developments in machine learning of crystallographically-invariant functions (Adams & Orbanz, 2023) make it possible to construct unconstrained parameterizations that can be used for shape optimization. In this work we extend these models... "   The authors don't explain what "these models" are, or their limitations.   Few readers will be familiar with Adams & Orbanz, 2023, which is an arxiv paper from mid-2023 with 3 citations.   If your key contribution is to extend the work in Adams & Orbanz, then you need to explain precisely what they did, its limitations, and precisely how you'll be addressing those limitations.

### Questions
1) Could the authors explain more clearly what general problem they are trying to solve?  Presumably there is some data-driven learning problem so that this work is suitable for this research community: could the authors explain more clearly what it is?  

2) Why don't the authors discuss, or compare with, any other existing approaches for metamaterial design? There are a large number of data-driven inverse design approaches.  Perhaps there is a good reason, but given the problem I cited in (1), it is unclear to me. 

See the following reference for some examples, but there are many:  Ardizzone, Lynton, et al. "Analyzing inverse problems with invertible neural networks." arXiv preprint arXiv:1808.04730 (2018).

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores using symmetry preserving flows and a mechanical simulator in order to design new meta-materials with desirable properties. The authors demonstrate how to construct neural networks equivariant to space groups and show successful designs that exhibit good force-displacement responses and effective Poisson ratios. They also manufacture real world designs and validate the simulation results on them.

### Strengths
- Novel application of equivariant/invariant networks to meta-materials design
- The paper is clearly written and explains various meta-materials related terms for the unfamiliar reader.
- The authors describe, in great detail, the space groups and the construction of the symmetry preserving flows
- The experiments seem to show good results and the authors further experiment in the real world

### Weaknesses
I imagine that there could be multiple designs that satisfy the desired properties. However the proposed method doesn't seem to allow for generating multiple different valid designs as it is not a generative model. The space group and the desired property must first be fixed, and as the network trains, it converges to some design that optimizes the loss. There doesn't seem to be an easy way to generate multiple valid designs without training every time.

One other concern is that I wonder if this paper is suitable for this venue. As a reviewer who doesn't know much about meta-materials design, it is difficult for me to judge the impact of the proposed method and the results. The best I can tell about the results is that the manufactured design seems to match the simulation measurements.

### Questions
- Line 319: Is there any specific reason why such small networks were used?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents a method to design metamaterials by learning equivariant flows. The method is capable of designing materials for all 17 space groups in two dimensions.

### Strengths
The paper is well written and the presented approach is mathematically grounded. The problem of designing mechanical metamaterials is an active area of research. The work presented here involves metamaterials where the unit cell is a general porous structure where each point in the domain can be air $(\rho=0)$ or material $(\rho=1)$. This is a good focus at times when much of the work in the field is on strut-based lattice metamaterials.

The idea of starting out with an initial model with well-behaved connected topology and morphing it into a flowed model is important – for a well-behaved flow, one will not end up with defective topology and disconnected patches of material (as opposed to what one might obtain by using fully generative models such as diffusion).

Part of having a well-behaved flow is ensuring it is volume-preserving. The authors incorporated an idea from the literature in which a divergence-free flow is obtained as vector whose components are appropriately arranged partial derivatives of a scalar function. This enables to set an original relative density $\bar{\rho}$ which is then preserved by the flow.

### Weaknesses
1. The presented approach is in 2d which has limited relevance as we often want materials with 3d structure (not extrusions of 2d cross-sections)

2. The emphasis on validation with real-world prototypes is only tangentially relevant to the presented work.
E.g. in abstract: “We validate these new designs in simulation and by fabricating real-world prototypes.” There are two statements to unpack:
    1.  validate these new designs in simulation - this is not really validation since the training loop already involves the differentiable simulator
    2. validate these new designs by fabricating real-world prototypes – this is not really the validation of the presented equivariant flows, but rather a validation that the differentiable mechanics simulator captures real-world behaviour of the structures

    Overall please change the way in which such claims are formulated:
        (i) any claimed “validation of simulations with respect to target behaviour” is only a test that the target behaviour is within the expressive power of the framework. It would be interesting to push this to the limit – for instance, what would happen if you tried to design for tension while setting as the target the same stress-strain curve which you use in compression?
        (ii) “validation by manufacturing real-world specimens” is only a check of the ability of the differentiable mechanics simulator to capture real-world behaviour of the structures.

3. One limitation identified in section 7 for scaling up to 3d structures is the lack of efficient/fast solvers and the high number of degrees of freedom. In section 5 it is mentioned that 25000 degrees of freedom were needed for force-displacement experiments. Please include the convergence study with respect to mesh resolution (accuracy/stability vs time per iteration vs number of DoFs)

### Questions
The following typos were found:

-	125: grammar of the sentence “In the case…”
-	354: “preserved”
-	531: grammar of the sentence
-	849: grammar: “vector field has to degrees”

Please compress the pdf; the current version has 27.5MB. It can be compressed without noticeable loss of quality to ~3MB.

Please make it clear in Fig.1 (visually or in caption) that the columns of (b) correspond to a single sample while rows are different stages of deformation

Please show in the plots examples of the behaviour for cases when the target was not obtained (Design under uniaxial compression for symmetry groups other than p1, Design under uniaxial tension for p1 and $\beta=1.5$)

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a machine learning framework that efficiently tackles the inverse design of two-dimensional cellular solids. By training a neural network to learn a symmetry-preserving flow, they could expand the design space of a class of mechanical metamaterials, known as cellular solids, into more generalized isometries. Their approach ensures that the solution avoids disconnected regions and the associated numerical challenges. Moreover, they demonstrate that such neural flows are divergence-free, enabling the preservation of the total volume while focusing solely on optimizing the geometry. The effectiveness of their approach is validated  through simulations and the fabrication of real-world prototypes.

### Strengths
- This paper demonstrates how to expand the design space of cellular solids beyond translational symmetry using symmetry-preserving flow. It also provides detailed derivations and proofs.
- This paper leverages a neural network to construct the symmetry-preserving flow and optimizes materials to achieve desirable mechanical properties. The effectiveness of the approach has been validated through simulations and real-world fabrication.

### Weaknesses
 - The contributions and related work are not clearly presented. Does this optimization formulation for extending the design space already exist, but cannot be effectively solved by classical optimization methods, or is it first introduced in this paper? Are there any other formulations or approaches that can also extend the design space of cellular solids? If so, why is this formulation considered superior to others?
- My main concern is the motivation of using a neural network for such design problem. Many other machine learning methods could also satisfy the conditions outlined in Theorem 2 and the loss function. Why is the neural network preferred? There is no justification, proof, or experimental comparison to support this choice of neural networks as a proxy model.  This issue downsides this paper quality significantly. I strongly suggest the authors provide strong motivation from this aspect.

- It appears that the neural network is not always Lipschitz-continuous or ($k+1$)-times continuously differentiable. Is there any proof supporting this, or did you relax the constraint based on certain assumptions?
- It is highly suggested to compare the proposed approach to other machine learning alternatives. These models can also satisfy the conditions outlined in Theorem 2 and offer greater interpretability compared to MLP. 
- How did you determine the configuration of the neural network? Does the configuration—such as the number of hidden neurons, layers, or the choice of activation function—affect the simulation accuracy? Additionally, which components of the neural network play the most critical role in the simulation performance? Whether the learned function exactly meets the constraint stated in Theorem 2?

### Questions
- It appears that the neural network is not always Lipschitz-continuous or ($k+1$)-times continuously differentiable. Is there any proof supporting this, or did you relax the constraint based on certain assumptions?
- It is highly suggested to compare the proposed approach to other machine learning alternatives. These models can also satisfy the conditions outlined in Theorem 2 and offer greater interpretability compared to MLP. 
- How did you determine the configuration of the neural network? Does the configuration—such as the number of hidden neurons, layers, or the choice of activation function—affect the simulation accuracy? Additionally, which components of the neural network play the most critical role in the simulation performance? Whether the learned function exactly meets the constraint stated in Theorem 2?

### Soundness
2

### Presentation
2

### Contribution
2
