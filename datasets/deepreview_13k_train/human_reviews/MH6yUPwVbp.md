# Fast and Space-Efficient Fixed-Length Path Optimization

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
Several optimization problems seek a path of predetermined length among network nodes that minimizes a cost function. Conventionally, such problems are tackled by dynamic programming (DP) applying a Bellman-type equation. A prominent example is Viterbi decoding, which returns the path in a Hidden Markov Model that best explains a series of observations, with applications from bioinformatics to communication systems and speech recognition. However, DP-based solutions (i) exhaustively explore a search space linear in both network size and path length in time quadratic in network size, without exploiting data characteristics, and (ii) require memory commensurate with that search space to reconstruct the optimal path. In this paper, we propose Isabella (Dijkstra-Bellman), a novel framework that finds optimal paths of predetermined length in time- and space-efficient fashion by a combination of best-first-search, depth-first-search, and divide-and-conquer strategies. The best-first-search component avoids the exhaustive exploration of the search space using a priority queue; the depth-first-search component keeps the size of that queue in check; and the divide-and-conquer component constructs the optimal path recursively and parsimoniously after determining its cost. We apply Isabella to Viterbi decoding, introducing algorithms that visit the most promising pathways first and control memory consumption. To emphasize the generality of Isabella, we also instantiate it with an algorithm for histogram construction. To our knowledge, no previous work addresses such problems in this manner. Our experimental evaluation shows our solutions to be highly time- and space-efficient compared to standard dynamic programming.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors consider the problem of finding a path of a predetermined length that minimizes a cost function in a search space. Traditionally, dynamic programming is used to solve such problems that calls for a lot of time and memory. The authors of this paper present more time and space efficient algorithms.

### Strengths
The problem considered in this paper has applications in many domains including bioinformatics, speech recognition, and communication systems. The authors propose a novel framework called Isabella to solve this problem. Isabella combines best-first search, depth-first search, and divide-and-conquer. Each of these techniques is very popular and the idea of combining all of these in the same framework is somewhat interesting. Also, the experimental results reveal that the proposed approach is effective.

### Weaknesses
The novelty of the proposed work is modest to some extent.

### Questions
None

### Soundness
3

### Presentation
3

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
Summary: The paper works on fixed-length path optimization problems. Specifically, the authors applied the proposed framework to Viterbi decoding and histogram construction problems. They claim contributions as follows: 1) the combination of the BFS (best-first-search) + DFS (depth-first-search) and divide-and-conquer is novel and has never been done previously, 2) experimental results show that their solutions are highly efficient in both time and space compared to the standard dynamic programming (DP) methods like Viterbi and its variants.

### Strengths
Pros: The authors picked the classic fixed-length path optimization problem which is highly related to the field of operations research and has an inherently fundamental impact. They work on the time and space improvements to DP, which has significant impacts on AI algorithms.

### Weaknesses
Cons: I outline my concerns on the technical aspect, and presentation aspect. I leave the experimental results for  further discussion due to my lack of hands-on experience with the two problems.

- On the technical aspect, the paper expands on solving dynamic programming in a Bellman "fashion". I believe that this topic is very well-studied [Bellman, R.(1952)][4]. In this paper, BFS prioritizes the promising subproblems, DFS maintains a short priority queue, and divide-and-conquer prevents exhaustive tabulating. Maybe this approach has never been done before, but I don't think it's highly technical.

The authors applied the framework by creating multiple algorithms. I argue that, for the BestFS, the authors replace the BreathFS component from the work [Young et al.][1], the bidirectional idea can be traced back to [Pohl][2], the divide-and-conquer application in Viterbi decoding is originated from [Ciaperoni et al.][3]. Therefore, I am a bit skeptical about the innovation of this work, although the authors claim that their approach has improved magnitudes on both time and space. 

I can see the improvements from the experiments, but I also believe that combining $\textit{the best}$ of various methods will always end up with certain improvements. The question is, why is the combination important to the field, why is the combination unique and innovative?

- Is there any particular reason to bring up Semirings and Dioids? If so, which aspects of the work do these concepts contribute to? I can see the only usage is in the descriptions of the algorithms. If so, it's very unnecessary to include them as a part of the paper. Dynamic programming could be explained in a few sentences without losing any promotion of the major contributions. On this one, please correct me if I explicitly missed anything.

- For standard MINT, is there any "major" difference with Dijkstra? Except 1) the cost function for path, 2) fixed length. (I understand the scenario is on HMM and we aim to maximize the log prob of Viterbi Path)

- Then, on the presentation aspect, I briefly list out the issues I noticed:
1) MINT -- Is this an abbrev. that has been formally defined? Or, do we just directly use it as the name?
2) The algorithm blocks are not well-written. Maybe consider using algorithmicx/algorithm2e, and try to avoid mixing math expressions with normal text? The format is strange, i.e., in Alg. 3, the if conditions should use some line breaks to trim the extra lengths.
3. Fig.2: y-axis is not showing the full range.
4. Fig.2: the last semicolon, what does it mean by "axes in log scale"? Does it mean that both x and y axes are log scaled? How do the authors apply the log-scale to the axes? 
5. The abbrev. "D&C" is only used at its declaration.
6. In the definition of "MINT Bound" (the end of p.5), what does "til" mean? I guess it's the abbrev. of "till", right?
7. Sec. 3.4: "V-optimal(V for variance)" should be explained at the first appearance.

### Questions
Please refer to the weakness section, my questions are well stated.

### Soundness
2

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
3

### Summary
This paper proposes time- and space-efficient algorithms for finding a minimum-cost path having predetermined hop length. Their algorithms combine best-first-search to reduce the computation time and depth-first-search to reduce required space. The applications of this problem include the decoding of hidden Markov models (HMM), which is typically solved by Viterbi algorithm that is a famous dynamic programming (DP) algorithm, and V-optimal histogram construction, which is also typically solved by DP. Experiments show that the proposed algorithms are indeed more time- and space-efficient than the ordinal DP algorithms.

### Strengths
The proposed algorithms are extensively tested with both synthetic and real datasets with various parameters. These experiments show that the proposed methods is both time- and space-efficient in solving fixed-length path optimization. It is also favorable that the proposed algorithms works extremely well for the real instances since it visits only a small fraction of search states.

### Weaknesses
Presentations of this paper have two major issues, which prevent me from understanding the whole algorithm correctly and thus cannot review whether the described algorithm is correct.

The first issue is around the depth-first strategy to achieve linear space complexity. The procedures for achieving linear space complexity is described in the last two paragraphs of Section 3.1 and Section 3.3. While the former only describes the abstract of used ideas (divide-and-conquer and depth-first-search), the latter explains the procedures to achieve linear space complexity. However, I cannot understand this description because some undefined terms arise. For example,
- (l.345) ... and produce all its derivatives on demand via a DFS traversal ... : What is "derivative"? And, what "on demand" means?
- (l.348) ... The paths DFS explores identify and pass on middle pairs as usual ... : What is "middle pairs"? Is it the same with "middle frame"?
- (l.349) By virtue of this DFS operation, ... : What is the "virtue" of DFS?
In addition, there are no step-by-step explanations or pseudocodes for these procedures, that makes the understanding of this part much difficult. Thus, the authors should describe either a step-by-step explanation or pseudocodes for these procedures.

The second issue is that the details of the algorithm are given only for the specific problems such as HMM decoding and histogram construction and not given for the Isabella framework, thus questionable whether Isabella is applicable for the other problems. As far as I understand, these problems share the components (items 1--7) in lines 141--153. Thus, from the name "Isabella framework" I expect that applying these components automatically yields efficient algorithms such as "Standard XXX", "Bidirectional XXX", "XXX Bound", and "XXX-LS". However, this is not the case within the presentation of the paper; "Standard MINT", "Bidirectional MINT", "MINT Bound", and "MINT-LS" are derived, afterwards "Standard TECH" are derived, and then TECH variants are derived by analogy to MINT variants. Thus, I suspect that we cannot derive these variants for the other problems sharing the components (items 1--7). To alleviate this issue, I recommend that, if possible, first the step-by-step explanations or the pseudocodes based on the Isabella framework (assuming the components in lines 141--153) is given first, and then the algorithms for specific algorithm are derived by substituting the components (items 1--7).

Minor comments:
- Firstly I cannot understand what are the triangle marks associated with a fraction in the second and fourth plots are; please note that they are just legends.

### Questions
- The above comment is based on my understanding that the common procedure can be described on the Isabella framework like, e.g., "Standard Isabella", "Bidirectional Isabella", "Isabella Bound", and "Isabella-LS". Is this true? If not, please provide why this is called "framework".
- What is the filled area in the right part of Figure 4?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies algorithms for finding the highest probability chain along a Hidden Markov Model (HMM), a problem known as Viterbi Decoding. The focus is on HMM with fixed length $L$ (the algorithmic approach relies on $L$ being known). Let us denote the number of internal states in each of the $L$ layers by $n$.

The classical approach for solving problems of this type is based on dynamic programming. The idea is to iterate the following for $L$ rounds: for each internal state, compute the highest probability reaching this state as the maximum, over all $n$ states of the previous layer, of the probability of reaching each state times the probability of the edge between them. The computational cost for a single node in a single layer is $O(n)$ (for a total of $O(n^2 L)$ for all nodes in all layers), but the space complexity is $O(1)$ for each node since we need to memorize paths (so the total space is a possibly prohibitive $O(nL)$. There is also a simple solution with this kind of memoization, but its running time is $O(n^2 L^2)$. The question is whether one can do much better, and it was answered to the positive by recent works of Ciaperoni et al. (SIGMOD 2022 & Interspeech 2024). They obtained an algorithm with runtime roughly $O(n^2 L)$ and space $O(n)$. 

The current paper obtains another algorithm for Viterbi decoding (and a related problem of histogram construction). To my understanding it has similar worst case guarantees to Ciaperoni et al., but the main "claim to fame" of the paper is better practical applicability due to adaptivity to beyond worst case structure of the specific problem instance. Specifically, the algorithm run bidirectionally, both forward and backward, running a Dijkstra type algorithm from each side plus existing techniques in the literature. The algorithmic idea is that for realistic instances, we expect the subset of close to optimal paths to meet much faster than the progress of most other paths, which effectively prunes away a lot of the slowly proceeding paths.

The authors provide a couple of algorithms based on these insights -- one that is competitive in terms of running time and the other that optimizes on space (guarantees are similar to the SOTA as described in the first paragraph). They show the empirical performance of the algorithm as compared to the vanilla Viterbi algorithm.

### Strengths
- A new, practical algorithm for Viterbi decoding, an interesting problem with a variety of applications.

- Convincing experimental results (in the supplementary) against existing algorithms.

### Weaknesses
 - The paper does not contain a good formal discussion of the running time and space bounds, nor theoretical explanation for the good performance on realistic instances.

- The main experimental results are for synthetic random graphs, and for some reason only compare the new algorithms to vanilla Viterbi, and not, say, to SIEVE variants (Ciaperoni et al.). It does look that the supplementary contains additional interesting experiments - I suggest the authors to restructure the experimental section, and perhaps put more focus on it (and less on the different variants of the algorithm).

### Questions
- Can you state clearly the running time and space complexity of each of your variants of the algorithm?

- What kind of theoretical analysis do you think can help explain the claimed good practical performace on realistic instances?

### Soundness
2

### Presentation
3

### Contribution
3
