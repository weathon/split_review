# The Computational Complexity of Positive Non-Clashing Teaching in Graphs

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
We study the classical and parameterized complexity of computing the positive non-clashing teaching dimension of a set of concepts, that is, the smallest number of examples per concept required to successfully teach an intelligent learner under the considered, previously established model. For any class of concepts, it is known that this problem can be effortlessly transferred to the setting of balls in a graph $G$. We establish (1) the NP-hardness of the problem even when restricted to instances with positive non-clashing teaching dimension $k=2$ and where all balls in the graph are present, (2) near-tight running time upper and lower bounds for the problem on general graphs, (3) fixed-parameter tractability when parameterized by the vertex integrity of $G$, and (4) a lower bound excluding fixed-parameter tractability when parameterized by the feedback vertex number and pathwidth of $G$, even when combined with $k$.
Our results provide a nearly complete understanding of the complexity landscape of computing the positive non-clashing teaching dimension and answer open questions from the literature.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies the complexity of computing the positive non-clashing teaching dimension that can be interpreted as the smallest number of examples needed to teach an intelligent learner. The paper models the concept class as the set of all balls of a certain radius k in a graph. (A ball of radius k consists of all vertices at a distance at most k from a vertex v serving as the center of the ball.)

The paper shows that the problem of computing the positive non-clashing teaching dimension is NP-complete, even when k=2. Previously, the problem was known to be NP-complete in general but not for a constant k.

The second result are improved upper and lower bounds on the time to solve the problem, as a function of the number of vertices n, diameter of the graph d and the radius of the balls k. Both previous and new bounds are exponential time but the exponents have been improved. For example, the upper bound is improved from 2^{O(n^2 d)} to 2^{O(n d k log n)}.

The third set of results is about the fixed parameter tractability of the problem. Previous, it was known that the problem is tractable if the vertex cover number of the graph is constant. This paper improves this to the vertex integrity being constant. It also considers several other possible improvements (replacing vertex integrity by smaller graph parameters) and rules them out.

### Strengths
Clear improvement over previous work.
Comprehensive set of results, covering the complexity of problem from various angles.
Original technical ideas.

### Weaknesses
Not sure about the fit to ICLR in terms of topic, as the paper proves general complexity-theoretic results but does not consider specific classes of concepts for which the studied questions have interesting implications. The paper's focus on balls in graphs, while mathematically sound, lacks a clear connection to practical machine learning scenarios. The results, while technically impressive, seem somewhat detached from the core concerns of the ICLR community, which often prioritizes algorithms and models with direct applicability to learning problems. The hardness result, while interesting, does not provide any immediate insight into the design of more efficient teaching algorithms for relevant concept classes. The improved time bounds, while a theoretical advancement, do not translate to practical improvements in the context of real-world learning tasks. Similarly, the fixed parameter tractability results, while mathematically elegant, do not address the practical limitations of the problem in realistic settings.

### Questions
What would be concrete consequences of your results that would be interesting to ICLR audience?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present several complexity results on the computation of the teaching dimension in the model of non-clashing machine Teaching.
Recent results have appeared on the "strict" variant of the problem and the authors consider the more general case of the non-strict variant. For the strict variant they also strengthen the previous hardness result by showing NP-hardness also for deciding teaching dimension constant bounds. Under the ETH this is also extended to upper and lower bounds on an optimal algorithm complexity for the problem. 
For the non-strict variant they present new Fixed parameterized complexity results, with respect to less restrictive parameters (Vertex integrity vs vertex cover number used in previous analogous results for the strict variant). Finaly they show W[1]-hardness w.rt to other parameters.

### Strengths
Generalization to the non-strict model and strenthening of some hardness and FPT results. 
The complexity picture of the problem is neater than before.

### Weaknesses
The gap in the upper and lower bounds are significant. I do not think that is a strong result. The FPT results, while using less restrictive parameters, still seem to have a large gap between the parameterized complexity and the known NP-hardness results. The W[1]-hardness results, while interesting, do not pinpoint the exact complexity of the problem, leaving a significant gap in our understanding of the parameterized complexity landscape. The practical implications of the fixed-parameter tractability results are also not very clear, as the parameters used might be large in real-world scenarios.

### Questions
Are there results or ideas about approximation algorithms? Or hardness of approximation?

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
This paper investigates the computational complexity of determining the positive non-clashing teaching dimension for a set of concepts, focusing specifically on its representation as balls within a graph G. 
- The authors show NP-hardness for what is known to be the easier subcase of this problem, where all balls are considered (strict non clash). 
- They supplement this hardness result with a positive result for the more general case (non clash), showing fixed parameter tractability with respect to the vertex integrity of a graph, strengthening previous work which had shown fixed-parameter tractability with respect to the vertex cover number, which upper bounds the vertex integrity. 
- They complement the fixed-parameter tractability result with a hardness result that shows hardness of non-clash with respect to a number of natural alternative parameters: feedback vertex number, pathwidth, and teaching dimension, thus identifying vertex integrity as a key parameter for tractability.

### Strengths
- The paper is clearly written, and answers a number of open questions in the area of machine teaching by strengthening existing results on both the hardness of strict-non-clash, and the fixed-parameter tractability/hardness of non-clash. 
- While I am not very familiar with this area, these strengthenings seemed significant in that they show hardness for the easiest subcase of the problem, thus providing a very strong and previously unknown hardness result, and additionally introduce a novel parameter that seems to capture the tractability of the problem given that a combination of other related parameters still render it intractable. 
- The proof techniques needed to solve these problems are highly non-trivial, relying on a delicate reduction to 3-sat in the case of the NP-hardness result, and a complicated equivalence class argument in the case of the fixed-parameter tractability result. 
- I carefully checked the correctness of the proof of Theorem 1 and was satisfied, but due to the length, have to defer to other reviewers for comments about the correctness of the other proofs.

### Weaknesses
 - As someone unfamiliar with the area of machine teaching, I felt that some of the introduction/preliminaries relied too heavily on assuming familiarity with previous work, and would have benefitted from additional explanation within the paper to make it more standalone. In particular, I would have liked a bit more discussion on the equivalence between arbitrary concept classes and balls in graphs. I wasn't even sure what arbitrary concept class meant in this case (binary? finite domain?), and how the distinction between strict-non-clash vs non-clash would map to concept classes. 
- While I was convinced by the novelty/significance of the results, I would defer to someone more knowledgeable about this area on this point, as well as more generally the significance of the question of positive-non-clashing teaching dimension. 
- I feel like the related work could have been more substantial, perhaps discussing related problems in other areas of theory/machine learning. 
- Minor note: There is a typo in the first sentence of section 5

### Questions
- How do these questions of teaching dimension relate to questions studied in one-way communication complexity or sample compression? 
- How does allowing for non-positive examples in the teaching set change the hardness of the problem?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies and obtains several theoretical results for the non-clashing teaching dimension of a concept class. The positive, non-clashing teaching dimension of a class $\cal C$, somewhat similar to VC dimension, is the minimum integer $k$ such that the following holds. For each concept in the class there is a unique set of examples associated with it of size up to $k$, so that for every two sets $S_1, S_2$ of examples (for different concepts $C_1, C_2$), the symmetric difference between $S_1$ and $S_2$ is non-zero.

This notion can equivalently be formulated using balls in graphs, where each concept corresponds to a ball of some radius around some vertex (note that some concepts can strictly contain others, e.g., a ball of radius 2 and a ball of radius 1 around the same vertex). The paper obtains several results about this graph theoretic concept:

1. An NP-hardness result for a strict variant of the non-clashing dimension. It is shown that even determining whether the dimension is at most 2 is NP-hard, resolving a question of Chalopin et al. (COLT 2024).

2. Tighter upper and lower bounds improving upon the aforementioned Chalopin et al. work. The upper and lower bound from the aforementioned work are $2^{O(n^2 d)}$ and $2^{\Omega(n d)}$ where $d$ is the graph diameter, and the current work obtains upper and lower bound of $2^{O(ndk)}$ where $k$ is the non-clashing dimension.

3. Parametrized results obtaining complexity that depend polynomially on $n$ and exponentially on parameters like the vertex integrity. There are also hardness results for well known parametrized notions such as path-width, and by extension, treewidth and cliquewidth.

From the technical perspective, the proofs are rather intricate (especially the lower bound ones, which use careful reductions). I did not verify the full details but the proofs seem believable.

### Strengths
- Novelty: new results on an emerging learning concept, which address open problems from the recent literature.

- Mathematical proofs seemingly of significant depth.

- The paper is generally well written.

### Weaknesses
 - Somewhat limited scope, this is a graph theoretic concept that has not been of interest outside a theory sub-community (and as such might be less suitable for a wide audience conference like ICLR).

- The studied notion seems somewhat "too pessimistic to be interesting". There is an exponential lower bound on the running time even prior to this work (which was improved by this work). The parameterized complexity upper bounds, although new, depend on parameters that seem to be very large, probably linear in $n$, in "realistic" graphs. For instance, the vertex integrity parameter, while theoretically interesting, is often close to the number of vertices in many practical graph structures, thus rendering the parameterized results less useful in those cases. The results are therefore largely theoretical with limited practical implications.



### Questions
What do you think about the practical applicability of this non-clashing teaching notion? What is the next set of results that would allow the community to better appreciate this notion?

### Soundness
4

### Presentation
3

### Contribution
2
