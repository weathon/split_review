# Complete and Lipschitz continuous invariants of graphs under geometric isomorphism in R^n

- Decision: Reject
- Scores: 6, 1, 8, 3, 5

## Abstract
Euclidean graphs embedded in R^n with unordered vertices and straight-line edges represent important real objects such as molecules whose atoms are connected by chemical bonds. Many real objects preserve their properties under any rigid motion from the special Euclidean group SE(n).Embedded graphs were previously distinguished under such rigid motion or geometric isomorphism in R^n.

Experimental noise motivates new Lipschitz continuous invariants so that perturbations of all vertices up to epsilon change the invariants up to a constant multiple of epsilon in a suitable metric, whose running time should polynomially depend on the number of unordered vertices. 

We developed new complete invariants that are stable under noise, form a natural hierarchy, and distinguish all chemically different graphs in the QM9 database of 130K+ molecules within a few hours on a modest desktop.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a hierarchy of invariants to characterize geometric graphs, from the very simple and efficiently computable, to a complete invariant that is Lipschitz-continuous with respect to node displacement that, however, has fairly high computational complexity ( O(m^{5.5}\log^3 m) ). The paper illlustrates the invariant's ability to characterize the chemical compounds in the QM9 database.

### Strengths
A nice and nicely written thoretical paper. Geometric graphs arise naturally in several domains and been able to characterize them is going to be useful to several pratitioners..

### Weaknesses
The evaluation is a bit limited, something that can be accepted from a fundamentally theoretical paper, but what is there is difficult to understand: the authors show the minimum distance between two different chemical compounds (inter-cluster distance), but without any indication of the intra-cluster distances (maximum distance between molecules with the same chemical composition, it is hard to see how easy the clustering problem would be.

Also the claim that "the new invariants have enabled a complete classification of all molecular
graphs in the QM9 database of 130K+ (130,808) molecules given with atomic 3D coordinates.
For graphs [...] with edges, such a practical classification was previously impossible" is a bit exaggerated, and a large literature was able to solve important classification problems on QM9 even with incomplete invariant representations.

The time complexity of the complete invariant (O(m^{5.5}\log^3 m)) can be daunting for larger problems.

### Questions
The authors mention the time complexity, but not the space requirements of the various proposed invariants. I believe it would be very helpful to specify those as well.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper studies the problem of producing an invariant of Euclidean graphs that gives rise to a metric but moreover is complete in the sense that the graph can be reconstructed from the invariant.  The desired properties of this invariant are characterized axiomatically in a fashion that ensures that the metric is useful for distinguishing graphs and computable.  After a brief review of some of the existing literature on this subject, the paper defines a new invariant (which is related to the "distance distribution" of each vertex) and studies its properties.  A numerical experiment on molecules from the "QM9" database validates the theoretical results.

### Strengths
The paper is technically sound.

### Weaknesses
The paper has a number of weaknesses:

1) It is very poorly written, and in particular the exposition is both bombastic and also lacks clarity in various places.

2) The comparison to existing methods (e.g., the Gromov-Hausdorff or Gromov-Wasserstein distances) is remarkably ungenerous; I do not think a reasonable assessment of the method is given.

3) It is not really motivated why a complete invariant is needed as opposed to just a metric.

4) The evaluation is limited; the importance of the QM9 database is not explained, nor is there any comparison to any other method for solving this problem.  And there are no real applications other than distinguishing molecules.

The problem of finding distances between metric spaces or point clouds or distributions is one that has a long history and for which there are many algorithms in the literature.  This paper does not seriously motivate the contribution it purports to make, nor does it engage with this literature in an honest way.

### Questions
1) Why do we want a complete invariant?

2) Why is this method better than, say, approximating the Gromov-Wasserstein distance using the new efficient approximation methods?  How do other methods perform on the data set used for evaluation?

3) What is the real application of such a metric on Euclidean graphs?  Distinguishing molecules sort of begs the question.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a new class of invariants for graphs that maintain desirable geometric properties that are defined algebraically, but additionally possess the property of Lipschitz continuity which is a form of stability that is useful when considering data arising from a random data generating process.

### Strengths
Overall, I found this paper to be a strong contribution though I am admittedly not very confident in some of the technical areas that this paper covers, mostly in terms of existing work and their limitations, though the background and literature appears to be complete.

The paper appears to be technically solid and is mathematically interesting.

The experiments were good, it was interesting to see the performance and scalability of the approach on a real-life relevant dataset.

Good overview on the limitations of the work, including future directions of research that can be carried to overcome them.

### Weaknesses
I have no familiarity nor experience with chemical data, so this concern may not make sense, but it appears to me that molecule structure is something quite well-defined with a clear construction where randomness is probably not that important (it could be rather naïve thinking, but if the conditions aren't right for a molecule to form, then it won't form so there needs to be some inherent stability to the setting anyway, so the contribution of Lipschitz continuity as an important property doesn't seem to be practically that relevant here).  So, while the results look quite impressive in the experimental application, it's not immediately obvious to me that this is an interesting application area to demonstrate the result.

The paper could be better written, the writing style feels colloquial to me (contractions typically aren't used in formal papers).  The style is also less typical of computer science conference papers where there is typically a clear bullet point list of the contributions of the work.

### Questions
- I may have missed it, but would it be possible to have a concrete experimental example/experimental comparison against existing work and what breaks down if the Lipschitz contribution that the work is proposing doesn't hold?  This would better illustrate why this result is needed.
- Is there any intuition on how the contribution benefits other application areas other than molecule classification?
- It is briefly mentioned at the end of the paper that the work might extend to more general cases with other data structures, however, it would be interesting to understand the current setting but under more complex assumptions, such as graphical models.  Is there any intuition available on how to develop and adapt the results under of nodes/edges (e.g., how would the constant change)?  Could the results contribute to the area of causal inference?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a hierarchy of invariants of Euclidean graphs embedded in $R^n$ under isometries in $R^n$. In particular, the authors present a novel invariant that is complete and Lipschitz-continuous (w.r.t. a metric constructed on the space of invariants). The invariant is thus stable w.r.t. small perturbations of the node positions. They demonstrate that the hierarchy of invariants can be used to distinguish all chemically different molecules in the QM9 dataset by treating the molecules as Euclidean graphs (discarding atom types).

### Strengths
* The posed problem and its individual aspects is stated clearly and motivated decently well.

* The proposed invariants seem to be technically valid and solve the posed problem (though I didn’t check any of the proofs in the appendix).

### Weaknesses
 * The construction of the invariants higher up in the hierarchy CR, CD, NCD is not motivated well. Why was the CR triple chosen like this? Specifically, why are the distance matrix D(A), the relative distance matrix R(G;A), and the sign(A) chosen as the components of CR? The paper states that these components are sufficient to reconstruct a vertex and edge, but it does not explain why these specific components are necessary or how they are derived from first principles. Why does a nesting make sense? The paper mentions that nesting is needed to uniquely identify edges, but it does not explain why this specific form of nesting is chosen, nor does it explore alternative nesting strategies. Why does one choose a base sequence? The choice of a base sequence is presented as a given, but the paper does not discuss the implications of different base sequence choices on the resulting invariant. Why is a subset chosen up to the dimensionality of the embedding space? What is its influence? The paper states that any point in R^n is uniquely determined by n+1 distances to n+1 fixed points, but it does not explain why the base sequence is limited to the dimensionality of the embedding space, nor does it discuss the implications of this choice on the completeness of the invariant.

* The definition of NCD is unclear, in particular l. 266-268 which seem to explain the nesting. Could there be a typo? How are the CD that are defined through CR (l.265) related to the CD that are defined through nesting l. 267? The relationship between the CD defined through CR and the CD defined through nesting is not clear, and the paper does not provide a clear explanation of how these two definitions are related. To clarify the construction, I would suggest to explain at the example of Fig.3 how to obtain NCD(G; 2). The paper should provide a step-by-step explanation of how NCD(G; 2) is constructed for the example in Fig. 3, including the specific calculations and choices made at each step.

* The motivation for the construction of the metric is also missing. Why does one consider the strength? The paper introduces the concept of strength without explaining its purpose or how it relates to the overall goal of constructing a Lipschitz-continuous metric. Regarding the max metric $M_\infty$ (Def. 4.3), why does one take the maximum over the 3 different distance measures? The paper does not explain why the maximum is taken over the three different distance measures, nor does it discuss the implications of this choice on the properties of the metric. It is unclear why the metric is not defined as a sum or another combination of these measures.

* The practical value of the novel invariant is unclear: The authors claim that it can be used as an informative embedding or as input for chemical property prediction (even tough the atom types are completely discarded). This is a strong statement an should be justified by a more expressive experiment than Fig. 6, e.g., considering more interesting chemical properties known for the QM9 dataset than number of atoms. If the invariant can only be used to discern molecules from different isometry classes, I wonder if not a simpler procedure suffices, e.g. a point cloud based approach plus a naive connectivity check. The paper should provide a more comprehensive evaluation of the invariant's practical value, including experiments on more complex chemical properties and comparisons to simpler methods. The current experiments do not demonstrate that the invariant offers a significant advantage over existing approaches.

* Formal problems in definitions:

  - The NCD is defined for $1 \le h \le n$ (Def. 3.5). but in example 3.6 $h=0$ is used.

  - Def. 4.1 of the strength requires $n$ points in $R^n$. However, in Def. 4.3 the strength is also used for base sequences of length $h < n$.

### Questions
* To construct an invariant for Euclidean graphs, why does it not suffice to use a distances-based invariant for point clouds with negative pairwise distances between non-adjacent nodes? Please elaborate further on the statement in l. 413-414.

* Are there no (perhaps not L-continuous) related methods to compare against?

* How does the presented approach relate to the following work: Nigam, Jigyasa, et al. "Completeness of atomic structure representations." _APL Machine Learning_ 2.1 (2024)?

* why does condition 1.1c) imply continuity as state in l.105?

* Can the invariant distinguish mirror images? I suspect not, since the construction is purely based on distances. If not, Problem 1.1 and other places which talk about “rigid motion” should be rephrased into related by $E(n)$ transformations (rigid motions and reflections).

* Is there a way to incorporate (invariant) node features like atom-types?

Minor points:

* I suspect a typo in def 3.4 (l.322) since the proposed metric is not symmetric in (G, A) and (F, B).

* definition where possible in formulae so there is less ambiguity. (like Def 4.3)

* l. 297 is unclear, I suspect what is meant is that the points are linearly dependent.  
* l. 325 typo “above on”

* In Def 4.4 it seems to be missing that the collection of edges is chosen such that each vertex has degree 1 in order to guarantee a matching.

* I suggest not to use boxes at the end of definitions and examples (the boxes are typically reserved for proofs only).

* In l.244 use \ rather than minus to denote the difference of sets.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In "Complete and Lipschitz continuous invariants of graphs under geometric isomorphism in R^n", the authors propose a Lipschitz-continuous representation of geometric graphs embedded into Euclidean space. The representation distinguishes all graphs which are not related by orientation-preserving isometries and is computable in polynomial time in the number of points m for a fixed dimension n. The authors achieve this via the introduced nested centred distribution, which is recursively constructed from representations ("Centred Distributions") for marked subsets of the point set.

### Strengths
* The paper introduces a provably complete and Lipschitz continuous invariant of geometric graphs.
* The invariant is computable in polynomial time for a fixed ambient dimension, which is the case for many geometric graphs.
* The proof for the Lipschitz continuity basically falls from the well-chosen definition.
* The first part of the paper contains many examples highlighting the strength of different invariants.

### Weaknesses
 * There is very little intuition provided as to why this is the correct way to construct the invariant. In particular, an explanation of why we have to set n=h to get a complete invariant.
* Many things in this paper happen with the reader only understanding why they happen later. The roadmap for constructing our metric should be made much clearer already in the beginning. In the current state of the paper, we only learn on page 7 from Theorem 4.7 that the earlier introduced nested centred distribution will play the central role in this paper. This is mirrored in many other definitions, where the reader only understands later why they were useful definitions and presented at this particular point in the paper. I had to read the paper twice to understand it. (Admittedly, this is something Schopenhauer requested from readers of his book. I however don't believe that this is a good guiding principle for ICLR papers.)
* While the paper is technically solid in general, there are many minor technical issues in the definitions or the wording, see my minor comments below.
* It is not easy to follow the main part of the paper. In particular, the definitions of the nested bottleneck metric and the nested centred distribution provided are not, combined with the following notational problem: The definition of the centred distribution depends on the order h, i.e. CD_{h-1}(...) is defined differently than CD_{k-1}(...) for other k. However, this implicit order h does not appear in the notation. For example CD^h_{k} would solve this problem.
* There are over 8 different acronyms used throughout this paper. I understand that space does not permit to write these out every single time, but having them written out once in every definition they are used would greatly improve the readability of the paper. Furthermore, some important terms like R(G;A) and D(A) are missing from the lookup table 1.

* Line 26+: The definition of Euclidean graphs is a bit imprecise. You want your vertex set to be a subset of R^n, and this is basically all you need for a definition. Taking the geometric interpretation of edges into this makes it more complicated: Do you allow for overlapping edges? For a third vertex v to be contained in an edge? Do you consider G\subset R^n? What is actually the data of a geometric graph? Are the edges subsets of V^2, or of R^n?
* 59 up to 6 permutations -> up to all permutations
* 60 The space of triangular graphs is not the triangular cone, rather it can be represented by the triangular cone.
* Figure 2: "One isometry class of all isometric triangular graphs" -> this is not well defined, you mean the class of all triangular graphs isometric to a reference graph.
* 80 "Alternatively" -> Equivalently
* Problem 1:
	* There should be not whitespace in front of the colons.
	* You should define an abstract space S in which your invariant lives.
	* Then b) just reduces to stating that S is a metric space w.r.t. to a metric d and is Lipschitz continuous w.r.t to a certain metric on the space of geometric graphs.
	* Throughout the theorem, you use I to denote both: 1. the invariant mapping from the space of all geometric graphs to S and 2. a value I(G) in S on a geometric graph G.
	* I think that the notation G\subset R^n is confusing: there are multiple graphs geometric graphs which have the same underlying set in R^n.
* Line 94: DNA is not a good metaphor here. The geometry of proteins can vary although they are constructed from the same DNA.
* I don't think the meaning of line 98 is clear from the context.
* Line 103: You did not define unbounded graphs.
* Line 107: What means "preventing brute-force attempts" in this context? Maybe you could word that differently so I could understand it.
* Line 120 $Dot$->$\dot$
* I don't think the last sentence of the paragraph "Ordered clouds" is clear from the context. Specifically, the sentence "Energy potentials written as infinite series of spherical harmonics, are often considered complete representations of atomic environments, which holds in the limit but not for a finite size" is not clear.
* Line 127: The O(n) should be completely in the exponent.
* I don't think the last sentence of the paragraph "Unordered clouds" is clear from the context.
* Paragraph "Equivariants" Please introduce T_f
* The meaning of the first two sentences on page 4 are not clear at all to me.
* Line 175: I don't get the idea of the navigation metaphor.
* Definition 3.1: 
	* I believe p and q become p_i and p_j later in the definition?
	* What does "has" mean in this context. Is it defined like this?
	* c) are we talking about the unordered rows OF D(G), or are the D(G)'s the rows themselves as stated in the definition.
* Line 197: What does local distribution mean?
* Line 207 and the rest of the paper: What is the motivation behind introducing PDD's and the other terms?
* Line 233: Please remind the reader of what the first k columns correspond to.
* Line 236: Counter-examples to what?
* Line 237: in the n\times n matrix -> in a n\times n matrix? Or about which matrix are we talking here? And the determinant has the sign sign(p_1,...,p_n), right?
* Definition 3.3: Please introduce p_0=0 more explicitly, this is easily overread. Furthermore, you reference to the points p_1, ...,p_n by "vectors", "vertices", and "points", which is confusing.
* Definition 3.5:
	* "and the center of mass" -> "with the center of mass"
	* As discussed above, you need to fix your notation and introduce the final order h to the formula for centred distributions CD_k^h
	* can you streamline this definition? 
* Figure 3: Please mention in which direction the arrows face? Do the colours on the right have any meaning? I found the left part of the figure very hard to understand. (I only understood after I completely understood the definitions.) Can you add more explanation to this and make it more clear, which part of the diagram symbolises which part of your theory?
* Definition 4.1: You are confused about the dimensions of your objects: You start the definition by indexing points from 1 to n, but later switch to indexing points from 0 to n. I would assume that the n-dimensional simplex contains n+1 points, which seems to agree with the second part of the definition.
* Please introduce terms like p before you use them.
* Lemma 4.2: You should define epsilon and then make explicit on what the lambda_n depends. (Just on n, I would suppose)
* Line 315: If you define the metric L_\infty here, it should sound like a definition.
* Definition 4.3:
	* You write that your graphs "have" base sequences. A base sequence does not belong to the data of a geometric graph, hence wording this as "have" is confusing.
	* The term with the absolute value: This should be symmetric in A and B.
	* It is not clear whether this definition works. You want to define a metric between CR's, yet you use your knowledge of  A and B to compute this metric. You would need to prove that this does not depend on the choice of A and B, if they lead to the same CR.
* Line 324: Please specify the nodes of this graph.
* Definition 4.5: It would be great if this definition could be streamlined. The last part again suffers from the problem that you want to define a metric between NCD's, yet you access the points of the graphs used to construct the NCD's.
* Line 473: What part of this sentence is the heading?
* Line 521: There seems to be something wrong with this sentence.

### Questions
# Questions:

1. You claim that your NCD's have a vectorisation. Is this vectorisation unique and/or canonical? How can one compute this?
2. Are there any proofs of the minimal possible distance between two different geometric graphs?

# Minor comments:
* Line 26+: The definition of Euclidean graphs is a bit imprecise. You want your vertex set to be a subset of R^n, and this is basically all you need for a definition. Taking the geometric interpretation of edges into this makes it more complicated: Do you allow for overlapping edges? For a third vertex v to be contained in an edge? Do you consider G\subset R^n? What is actually the data of a geometric graph? Are the edges subsets of V^2, or of R^n?
* 59 up to 6 permutations -> up to all permutations
* 60 The space of triangular graphs is not the triangular cone, rather it can be represented by the triangular cone.
* Figure 2: "One isometry class of all isometric triangular graphs" -> this is not well defined, you mean the class of all triangular graphs isometric to a reference graph.
* 80 "Alternatively" -> Equivalently
* Problem 1:
	* There should be not whitespace in front of the colons.
	* You should define an abstract space S in which your invariant lives.
	* Then b) just reduces to stating that S is a metric space w.r.t. to a metric d and is Lipschitz continuous w.r.t to a certain metric on the space of geometric graphs.
	* Throughout the theorem, you use I to denote both: 1. the invariant mapping from the space of all geometric graphs to S and 2. a value I(G) in S on a geometric graph G.
	* I think that the notation G\subset R^n is confusing: there are multiple graphs geometric graphs which have the same underlying set in R^n.
* Line 94: DNA is not a good metaphor here. The geometry of proteins can vary although they are constructed from the same DNA.
* I don't think the meaning of line 98 is clear from the context.
* Line 103: You did not define unbounded graphs.
* Line 107: What means "preventing brute-force attempts" in this context? Maybe you could word that differently so I could understand it.
* Line 120 $Dot$->$\dot$
* I don't think the last sentence of the paragraph "Ordered clouds" is clear from the context.
* Line 127: The O(n) should be completely in the exponent.
* I don't think the last sentence of the paragraph "Unordered clouds" is clear from the context.
* Paragraph "Equivariants" Please introduce T_f
* The meaning of the first two sentences on page 4 are not clear at all to me.
* Line 175: I don't get the idea of the navigation metaphor.
* Definition 3.1: 
	* I believe p and q become p_i and p_j later in the definition?
	* What does "has" mean in this context. Is it defined like this?
	* c) are we talking about the unordered rows OF D(G), or are the D(G)'s the rows themselves as stated in the definition.
* Line 197: What does local distribution mean?
* Line 207 and the rest of the paper: What is the motivation behind introducing PDD's and the other terms?
* Line 233: Please remind the reader of what the first k columns correspond to.
* Line 236: Counter-examples to what?
* Line 237: in the n\times n matrix -> in a n\times n matrix? Or about which matrix are we talking here? And the determinant has the sign sign(p_1,...,p_n), right?
* Definition 3.3: Please introduce p_0=0 more explicitly, this is easily overread. Furthermore, you reference to the points p_1, ...,p_n by "vectors", "vertices", and "points", which is confusing.
* Definition 3.5:
	* "and the center of mass" -> "with the center of mass"
	* As discussed above, you need to fix your notation and introduce the final order h to the formula for centred distributions CD_k^h
	* can you streamline this definition? 
* Figure 3: Please mention in which direction the arrows face? Do the colours on the right have any meaning? I found the left part of the figure very hard to understand. (I only understood after I completely understood the definitions.) Can you add more explanation to this and make it more clear, which part of the diagram symbolises which part of your theory?
* Definition 4.1: You are confused about the dimensions of your objects: You start the definition by indexing points from 1 to n, but later switch to indexing points from 0 to n. I would assume that the n-dimensional simplex contains n+1 points, which seems to agree with the second part of the definition.
* Please introduce terms like p before you use them.
* Lemma 4.2: You should define epsilon and then make explicit on what the lambda_n depends. (Just on n, I would suppose)
* Line 315: If you define the metric L_\infty here, it should sound like a definition.
* Definition 4.3:
	* You write that your graphs "have" base sequences. A base sequence does not belong to the data of a geometric graph, hence wording this as "have" is confusing.
	* The term with the absolute value: This should be symmetric in A and B.
	* It is not clear whether this definition works. You want to define a metric between CR's, yet you use your knowledge of  A and B to compute this metric. You would need to prove that this does not depend on the choice of A and B, if they lead to the same CR.
* Line 324: Please specify the nodes of this graph.
* Definition 4.5: It would be great if this definition could be streamlined. The last part again suffers from the problem that you want to define a metric between NCD's, yet you access the points of the graphs used to construct the NCD's.
* Line 473: What part of this sentence is the heading?
* Line 521: There seems to be something wrong with this sentence.

### Soundness
3

### Presentation
2

### Contribution
3
