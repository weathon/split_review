# Decomposition Polyhedra of Piecewise Linear Functions

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
In this paper we contribute to the frequently studied question of how to decompose a continuous piecewise linear (CPWL) function into a difference of two convex CPWL functions. Every CPWL function has infinitely many such decompositions, but for applications in optimization and neural network theory, it is crucial to find decompositions with as few linear pieces as possible. This is a highly challenging problem, as we further demonstrate by disproving a recently proposed approach by \citet{tran2024minimal}. To make the problem more tractable, we propose to fix an underlying polyhedral complex determining the possible locus of nonlinearity. Under this assumption, we prove that the set of decompositions forms a polyhedron that arises as intersection of two translated cones. We prove that irreducible decompositions correspond to the bounded faces of this polyhedron and minimal solutions must be vertices. We then identify cases with a unique minimal decomposition, and illustrate how our insights have consequences in the theory of submodular functions. Finally, we improve upon previous constructions of neural networks for a given convex CPWL function and apply our framework to obtain results in the nonconvex case.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper deals with the following problem: given a continuous piecewise linear (CPWL) function, decompose it as the difference of two convex CPWL functions. This line of research is motivated by the DC paradigm for nonconvex optimization.  In this work the authors consider decompositions that are compatible with a given polyhedral complex and are “minimal” (for the definition of minimality, see Definition 3.12). The authors show that the set of all decompositions forms a polyhedron (Theorem 3.5) and that minimal decompositions are at a vertex of this polyhedron(Theorem 3.13). Thus, a minimal decomposition can be found by enumerating the vertices. They also identify a few special cases where there is a unique vertex, so there is no need for enumeration. In terms of applications, in Section 5 they apply their results to submodular functions. In Section 6, they revisit the problem of representing a CPWL function by a ReLU neural network. Their main result there is Corollary 6.4, providing “a smooth tradeoff between size and depth”, for the special class of CPWL functions that are compatible with a regular polyhedral complex.

### Strengths
The problem of decomposing CPWL functions as the difference of convex CPWL functions is interesting. No finite procedure is currently known for finding a minimal decomposition. This work provides a new perspective, based on polyhedral geometry, that guarantees finite convergence, but in the special case where the factors have a fixed supporting polyhedral decomposition

### Weaknesses
The assumption that the DC decomposition should be with respect to a fixed polyhedral complex seems restrictive and perhaps unmotivated.

I feel that the paper is hard to read for non-experts in the area (e.g. many technical definitions with not many accompanying figures to help the reader-there are few, but mostly in the Appendix).

The main result in Section 6 (Corollary 6.4) for representing CPWL functions as NNs, is only applicable to CPWL functions that are compatible with a regular polyhedral complex. It is not clear whether this assumption is (1) natural and (2) easy to satisfy.  The existing decomposition results are applicable to any CPWL function.

### Questions
Page 1, Introduction: You write, “CWPL functions play a crucial role in ML.” If I understand correctly, this is the case because they are used as a test case for the universality theorems for NNs, where they can be concretely instantiated in terms of width, depth, etc. Is that correct, or are there more important applications? You do mention submodularity etc in the introduction, maybe elaborate on that somewhat?

page 1: Are there problems where fixing the supporting polyhedral partition in DC decompositions is a natural constraint? 

Page 2, Section 1.1: Please point to a specific Theorem as your “main technical result.” I guess that is Theorem 3.13?

Page 2, line 73: “cannot be easily simplified.” Explain why this is important. Also, when you say a “minimal” solution, what are you referring to?
Page 2, line 75: “simply enumerating” seems to indicate there are not that many of them. Please elaborate on this.

page 3. Please give a bivariate example of a CPWL function with two different compatible polyhedral complexes with a different number of maximal facets.

Page 4: Please provide a simple example (with a figure) of a polyhedral complex illustrating (some of) the definitions in Section 2. In particular, at least one example of a polyhedral complex, the refinement, and the balancing condition should appear in the main text. Perhaps use the median example in Section 2. For example, to understand the balancing condition, I had to draw a 3D cube, a trivial case of a 3-dimensional polyhedral complex. According to the definition, for any 2-dimensional face \sigma, we have a weight w(\sigma). Then, for any 1-dimensional face \tau and any 2-dimensional face containing \tau, we have the vector e_{\sigma/\tau}. The balancing condition says that if we sum up all these vectors scaled by their weight, we should get the zero vector.

Page 4: Why is the balancing condition required only for n-2 dimensional faces? Why do we not care about smaller faces?

Page 4: It’s probably easy, but I couldn’t see it. Can you provide an example of a convex CPWL function with two different compatible partitions?

Page 4, line 188: Give an example of the number of pieces. E.g., the number of pieces for the median function is 6, correct?

Page 4, line 188: Same for affine components. For the median, it is 3, correct? Also, in terms of notation, shouldn’t that better be \(\text{aff}(\mathcal{P})\) or something like that?

Page 4: What is the relationship between k, q and n? Knowing this is also important for the representation results in Section 6.

Page 5, line 241: Recall that w are weights for codimension 1 faces.

Page 5, line 247: You write that Figure 1 illustrates the different parameterizations of the median function according to Lemma 3.2. I was trying to understand what that means. I guess the numbers on the figure are the weights on each edge, and the only “n-2” face for which we need to check the balancedness conditions is the origin, and this is indeed balanced. But how does that illustrate the isomorphism from Lemma 3.2?

Page 5, line 250: Have you defined “regular complex”?

Page 5, definition 3.4: Could it be that although f is compatible with P, it has a DC decomposition where f and g are not compatible with P? That is, are the decompositions studied here a restricted class?

Page 6, definition 3.12: I forgot what was meant by “pieces” here? It is the minimum number of facets in a compatible decomposition. Apparently, this is already used in the literature, but maybe a better term could be used?

Page 6, line 302: Typo.

page 6, Theorem 3.13. I may have missed this but have you argued that the decomp polyhedron always has an extreme point? 

Page 7, proposition 4.1: The word “function” appears twice.

Page 7, line 371: What is proposition B.3?

Page 9, line 468: Typo “certing.”

Page 9, line 450: “this simple fact…” it is not clear what that means, please explain. Are Theorems 6.1 and 6.2 constructive? Would we be required to know the parameters q and k and their specific representations as CWPL functions?

Page 9, Theorem 6.3: Writing q = k in the theorem statement makes it look like an assumption (which is not the case).

Page 10, Corollary 6.4. This result is only applicable to CPWL functions that are compatible with a regular polyhedral complex. Maybe I missed it, but can you discuss whether this assumption is natural and/or easy to satisfy.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the fundamental problem of decomposing a continuous piecewise linear (CPWL) function into two convex CPWL functions. This is a rather challenging problem with a long history and important practical applications. The authors adopt a novel perspective to tackle this problem: investigating the space of admissible convex CPWL functions while fixing the underlying pieces. The main contribution is a series of structural results concerning the geometric properties of the so-called (and new) decomposition polyhedra, which are connected to the space of admissible convex CPWL functions. With these structural results, the authors demonstrate some implications for submodular functions and for constructing neural networks according to a given convex CPWL function. Moreover, they refute a recent conjecture on algorithms for computing CPWL functions in the literature.

### Strengths
The DC representation of a general CPWL function is an old but fundamental problem with many applications in various engineering fields. This paper proposes an interesting perspective on how to understand and compute the DC components from a given CPWL function. Although I did not have time to check all the proofs in detail, the paper is generally well written, and the results are interesting. In particular, I appreciate the idea of fixing the underlying pieces and the clean characterization of the DC components.

### Weaknesses
While the pieces are assumed to be fixed in advance (which is, of course, a limitation, as also explicitly noted by the authors), I believe this work has great potential to motivate further investigation into both the theoretical and algorithmic aspects of the decomposition problem. 

My comments are as follows:
* L200, in the definition of $\mathcal{P}_f^n$, I don't think the set {$x:g_i(x)=\max_j g_j(x)$} must be full dimensional. This may depend on the representation of $f$ given in L199. Also, $k=q$ may not be true, as claimed in L202. Specifically, if $f$ is represented as the maximum of affine functions, some of these affine functions might be redundant, meaning their active regions do not have full dimension, or even be empty. This would lead to a situation where $k$ (the number of affine functions in the representation) is strictly larger than $q$ (the number of maximal cells in the polyhedral complex).
* As for regular polyhedra complex, I understand the usage of the existence of convex CPWL in the proof of theorems. I'm curious about the irregular case and it will be very helpful to provide some details or examples to illustrate the existence of irregular polyhedra complex. It would be beneficial to include a discussion on how the structural results might be affected or adapted when dealing with irregular complexes. For example, do the decomposition polyhedra still retain similar geometric properties, or are there significant deviations?
* Some notation are used before defined in the whole paper. For example, in Proposition 3.3, it seems the function $w_f$ is not defined until the proof of Proposition 3.2. This makes it difficult to follow the logical flow of the arguments and requires the reader to jump ahead to understand the notation.
* L184, in the definition of CPWL functions, I think you need to require $f$ to be continuous. Without continuity, the definition would allow for functions with discontinuities at the boundaries between the linear pieces, which is not the standard definition of CPWL functions.
* L1283, what is $\phi$ defined here? The definition of $\phi$ seems to be missing, making it impossible to understand the proof.
* In the proof of Proposition 3.3, I suggest providing more details to justify the equivalence claimed in line 1360. Intuitively, this is correct, but in convex geometry, counterintuitive phenomena can occur, so a rigorous and formal argument would be desirable. The equivalence between local convexity around the interior of facets and global convexity needs a more detailed explanation, especially considering the potential for non-smooth behavior at the boundaries of these facets.
* L752, the function $h$ may not be convex as claimed. The current definition of $h$ involves a summation of terms that could potentially lead to a non-convex function, especially if the coefficients $\lambda_i$ are not handled carefully.
* L180, add a period.
* L146, "wit" should be "with".

### Questions
See above.

### Soundness
3

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
3

### Summary
The paper studies the problem of decomposing a given continuous piecewise linear function into the difference of two convex piecewise linear functions. Especially, the authors investigated the problem of finding such a decomposition with the least linear pieces. To tackle this,  a few new theoretical results were proposed and proved. After fixing the polyhedral complex, they study the geometrical properties of such decompositions. Specifically, they show that a minimal solution must be a vertex and hence can be obtained by a simple enumeration. The results can be applied to relu network with 1 hidden layer, statistics functions, submodular functions, and the construction of neural networks.

### Strengths
1. The paper presents an innovative approach by linking decomposition problems with polyhedral geometry, leading to the concept of decomposition polyhedra. This is a very novel idea and may inspire many interesting future works. 

2. The theoretical analysis of the paper is very solid, providing us with a deep understanding of CPWL decomposition problem. 

3. The paper is well-written and well-organized, clearly stating the main contributions and their applications.

4. The applications to ReLU activation, submodular optimization, neural network design, are very interesting.

### Weaknesses
The main weakness of the paper is that as stated in Limitations section of the paper. The paper mainly focuses on the development of theories, but does not provide practical implementations and applications of their results.



### Questions
1. Definition 3.12. The definition for the minimal decomposition seems same as the Pareto optimality in multi-objective optimization. 
2. Hyperplane functions introduced in Def 3.16 satisfy the assumptions. These are functions generated by a ReLU network with 1 hidden layer. Just wondering, does the result also hold for general ReLU networks with more layers? 
3. In theorem 3.18, what is the exact meaning of **minimizer**? It is also better to include an explicit linear programming problem described in Theorem 3.18.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper studies decomposition of continuous piecewise linear (CWPL) functions into difference of two convex CWPL functions with as few linear pieces as possible.
The contributions of the paper include:
i. A proof that the minimal solution must be vertices of a certain polyhedron which is a set of decompositions. This polyhedron arises as an intersection of two translated cones.
ii. A construction for a unique minimal decomposition for certain CWPL functions in dimension 2 by Tran & Wang (2024) does not extend to higher dimensions.
iii. Applications of the decomposition to submodular function optimization and neural network construction.

### Strengths
Paper is well-written. The problem studied is challenging.

### Weaknesses
The obvious limitation is that the underlying polyhedral complex is fixed.
There are no bounds shown for the number of pieces in the minimal decomposition. Would it be related to the notion of monomial complexity ? A discussion would be interesting.

### Questions
N/A

### Soundness
4

### Presentation
4

### Contribution
3
