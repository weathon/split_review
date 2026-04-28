# Conformal mapping Coordinates Physics-Informed Neural Networks (CoCo-PINNs): learning neural networks for designing neutral inclusions

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
We focus on designing and solving the neutral inclusion problem via neural networks. The neutral inclusion problem has a long history in the theory of composite materials, and it is exceedingly challenging to identify the precise condition that precipitates a general-shaped inclusion into a neutral inclusion. Physics-informed neural networks (PINNs) have recently become a highly successful approach to addressing both forward and inverse problems associated with partial differential equations. We found that traditional PINNs perform inadequately when applied to the inverse problem of designing neutral inclusions with arbitrary shapes. In this study, we introduce a novel approach, Conformal mapping Coordinates Physics-Informed Neural Networks (CoCo-PINNs), which integrates complex analysis techniques into PINNs. This method exhibits strong performance in solving forward-inverse problems to construct neutral inclusions of arbitrary shapes in two dimensions, where the imperfect interface condition on the inclusion's boundary is modeled by training neural networks. Notably, we mathematically prove that training with a single linear field is sufficient to achieve neutrality for untrained linear fields in arbitrary directions, given a minor assumption. We demonstrate that CoCo-PINNs offer enhanced performances in terms of credibility, consistency, and stability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper aims to improve how physics-informed neural networks (PINNs) solve the problem of modeling neutral inclusions, with the goal of inverse design. An "inclusion" is a deviation from the background medium in a field-solution problem, e.g., the heat equation.  Such inclusions result in perturbations of the surrounding field, which may be undesirable.  When a linear field is applied but the inclusion does not perturb the field, this is called a "neutral" inclusion.  This desirable property can sometimes be achieved by designing a coating for the interface bewteen the inclusion and the surround.  The goal of this paper is to modify PINNs so they can better model this kind of behavior and then also use them for inverse design of the interface.

The main idea is to use a conformal map on the exterior of the inclusion and thereby warp it in a way to more easily apply PINNs to complicated inclusion geometries; the map being conformal is desirable for reasoning about neutrality under linear applied fields.  The conformal map itself is fit a priori based on the inclusion geometry using methods from another paper.  A secondary point of the paper is using a Fourier basis rather than a neural net to represent the interface function.

The experiments investigated the quality and consistency of the solution on neutral inclusion problems for which an analytic solution is available.

### Strengths
The neutral inclusion problem is interesting.  Using a conformal map to warp space to make it easier to handle complicated geometries is a good (and well studied) idea.  Doing this for PINNs is reasonable.

### Weaknesses
The paper is not structured well.  It took me a long time to figure out what the paper was doing.  It did not do a good job explaining what neutral inclusions are to someone who is not already familiar with the concept.  Figure 1 was not illuminating in this regard.  Overall, this left me with some substantial uncertainty about whether I understood it.

I was a little disappointed when I realized that the conformal map is not part of the machine learning setup.  That's not to say that what the paper did is the wrong way to solve the problem, but the message of the paper ends up being fairly modest: "Do Choi & Lim (24) before using a PINN."

Conformal mappings to simplify solutions to PDEs is a well studied idea.  I don't know much about neutral inclusions specifically, but even for that problem a quick search reveals papers that use conformal maps, just not for PINNs.

The experiments are all on problems for which an analytic solution is available, which makes it difficult to motivate using a neural network.  I appreciate that this is valuable as one aspect of understanding the performance of the method, but the paper would be much stronger if it solved problems that demand numeric solutions and then, very importantly, compared to conventional numerical approaches.  A recent review paper has highlighted poor motivation and baselines in papers on PINNs:

McGreivy, Nick, and Ammar Hakim. "Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations." Nature Machine Intelligence (2024): 1-14.

In other words: it is not sufficient to compare your method to other PINNs. In the case of inverse problems, it's natural to ask for comparisons to adjoint approaches.

### Questions
How does this perform on problems that require numerical solutions?

What is the computational cost of the method relative to conventional numerical methods?

Out of curiousity: are spatially-varying coatings of the form studied here physically plausible?  Would they usually be done by, e.g., varying the thickness of a homogenous coating material?

### Soundness
3

### Presentation
2

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
The authors developed a Conformal Mapping Coordinates Physics-Informed Neural Networks (CoCo-PINNs) to solve the neutral inclusion problem. The theoretical analysis is thorough.

### Strengths
The theoretical analysis is thorough on the PINN aspect.

### Weaknesses
The results on the inverse part are not very impressive. The primary goal of this inverse problem is to determine the inclusion's geometry. However, the geometry identification results of Classical PINNs and CoCo-PINNs are quite similar, which is insufficient to demonstrate the proposed method's effectiveness in addressing the inverse problem. The comparison between Classical PINNs and CoCo-PINNs lacks a quantitative analysis of the computational overhead. Furthermore, the study does not explore the performance of the proposed method with more complex inclusion geometries, limiting the practical applicability of the approach.

### Questions
1. In the neutral inclusion problem, the primary goal of this inverse problem is to determine the inclusion's geometry. However, the geometry identification results of Classical PINNs and CoCo-PINNs are quite similar, which is insufficient to demonstrate the proposed method's effectiveness in addressing the inverse problem.
2. What is the overhead of Classical PINNs and CoCo-PINNs for this problem.
3. What are the inclusion geometries for training.
4. Can the proposed method be applied for more complex inclusion geometries.

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
3

### Summary
The paper introduces a new framework called CoCo-PINNs, which combines mathematical analytical methods with the Physics-Informed Neural Networks (PINNs) approach to solve the neutral inclusion problem using neural networks. The authors point out that traditional PINNs using neural networks face challenges with this problem and propose representing the interface function using series expansions instead of neural networks.

### Strengths
1. Numerical results demonstrate that the method offers improved credibility, consistency, and stability compared to classical PINNs.  

2. Utilizing series expansions to represent inverse parameters not only improves the accuracy of the solutions but also provides valuable analytical insights.  

3. An additional advantage of the method is its ability to operate effectively without the need for training data to solve the neutral inclusion problem.

### Weaknesses
1. The paper primarily focuses on two-dimensional problems. The lack of extensive validation in higher dimensions may limit the immediate applicability of the proposed method to more complex real-world situations. In my view, the method's reliance on the Riemann mapping theorem in complex space restricts it to 2D problems, making its extension to 3D cases unfeasible.

2. Although the paper claims improved performance over classical PINNs, it would benefit from a more detailed comparative analysis with other state-of-the-art methods. As the reviewer is not an expert in this field, the introduction's overview of related work is appreciated. However, it seems to reference many effective methods without explicitly including a discussion of PINNs. Furthermore, the choice of classical PINNs as a baseline is questionable, as it has not been established as a standard method for solving the neutral inclusion problem. It would be more convincing to compare against a method that has been validated for this specific problem, if one exists.

3.  Some sections lack clarity. Please refer to the following Questions part for further elaboration.

### Questions
1. Line 170,The method requires the explicit formulation of the mapping $\Phi$, correct? Are we able to obtain this explicit formulation for any interface, or are there specific conditions that must be satisfied?

2. Equation 1,Could the paper clarify which of the following terms are known and which are unknown and need to be solved? I also suggest moving the condition in line 166, stating that $u$ and $H$ are equal in the exterior region, to an appropriate position at the beginning. Additionally, it would be helpful to provide several examples of $H$.

3. Theorem 1 states that \(u - H\) can be represented by a series. Why, then, is the interface function \(p\), rather than \(u\), parametrized by a series? Is there a connection between Theorem 1 and the proposed method, or is Theorem 1 only used to assess the performance of the PINNs?

4. For Theorem 2: what does it mean for a domain $\Omega$ to be neutral? Could the paper provide a detailed and rigorous definition?

5. In Section 4, all considered interfaces are defined by the conformal map. Is this a necessary condition for the proposed method? It would be helpful to clarify this point.

6. The considered $H$ functions are all 2D linear functions. Is this a necessary condition for the proposed method? It would be helpful to clarify this point.

### Soundness
3

### Presentation
3

### Contribution
3
