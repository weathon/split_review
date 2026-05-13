# An efficient implementation for solving the all pairs minimax path problem in an undirected dense graph

- Decision: Reject
- Scores: 1, 1, 1, 1

## Abstract
We provide an efficient $ O(n^2) $ implementation for solving the all pairs minimax path problem or  widest path problem in an undirected dense graph. It is a code implementation of the Algorithm 4 (MMJ distance by Calculation and Copy) in a previous paper. The distance matrix is also called the all points path distance (APPD). We conducted experiments to test the implementation and algorithm, compared it with several other algorithms for solving the APPD matrix.  Result shows Algorithm 4 works good for solving the widest path or minimax path APPD matrix.  It can drastically improve the efficiency for computing the APPD matrix.  There are several theoretical outcomes which claim the APPD matrix can be solved accurately in $ O(n^2) $ . However, they are impractical because there is no code implementation of these algorithms. It seems Algorithm 4 is the first algorithm that has an actual code implementation for solving the APPD matrix of minimax path or widest path problem in $ O(n^2) $, in an undirected dense graph.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The praper implements and experimentally tests an algorithm for computing minimax path distance that was proposed in paper Liu 2023. In my opinion the contribution of the paper is certianly below ICLR bar, as there are the following shortcomings:
- the paper is in area of exparimental algorithmis with no siginificant contribution to machine learning, 
- there is no siginificant contribution to algorithms, i.e., the paper just implents in a straight-forward way the algorithms and tests it, there is not technincal challange in this implementation, nor the tests introduce any nowel methodology,
- the paper makes false statement that previous quadratic time algorithms have not been impmemented - this is not true as even the orginal paper by Sibson from 1973 contains the Fortran implementation of the algorithm.

### Strengths
The paper does not contain any significant contribution.

### Weaknesses
 The praper implements and experimentally tests an algorithm for computing minimax path distance that was proposed in paper Liu 2023. In my opinion the contribution of the paper is certianly below ICLR bar, as there are the following shortcomings:
- the paper is in area of exparimental algorithmis with no siginificant contribution to machine learning, 
- there is no siginificant contribution to algorithms, i.e., the paper just implents in a straight-forward way the algorithms and tests it, there is not technincal challange in this implementation, nor the tests introduce any nowel methodology,
- the paper makes false statement that previous quadratic time algorithms have not been impmemented - this is not true as even the orginal paper by Sibson from 1973 contains the Fortran implementation of the algorithm.

### Questions
No questions.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
Given an undirected graph, this paper considers the problem of computing the minimax path problem between all pairs of vertices. For any path, let the bottleneck edge be the largest edge on the path. For all pairs of vertices, compute a path with the smallest bottleneck edge. The authors refer to a prior paper that suggests a simple spanning tree based algorithm to compute this bottleneck edge and also state that this algorithm has an execution time of O(n^2). The main contribution of this algorithm is in the implementation of this algorithm.

### Strengths
The problem of finding all pairs of minimax path is interesting and has applications within ML

### Weaknesses
while the problem is well motivated, finding an implementation for the algorithm is not very well motivated. It seems that no implementation existed before because the algorithms were not very efficient, and the algorithm of Liu is quite simple and efficient. The mere fact of coding that algorithm up is a simple classroom exercise it seems. If there are techniques used for going from the pseucode to the implementation, the authors have not described them, and it seems from the code that there are no such techniques.
Besides the above fundamental point, the write up could be polished, there are several grammatical mistakes.
abstract: "it is a code implementation of..." -> " this paper is a code implementation of the minimax path algorithm in Liu".
line 18:: works good -> works well.
line 106:: the sense -> the sign
in the related work it is good to note if there are any other papers like your paper where they implement an algorithm from a previous paper.

### Questions
NA

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper is about an implementation of an algorithm for all pairs minimax path problem in undirected dense graphs that works in $O(n^2)$ time. The problem asks to output the minimax distance between every pair of points s and t, where the minimax distance between s and t is the minimum of the maximum weighted edge in a path from s to t, over all the paths from s to t. The algorithm is from "Gangli Liu. 2023. Min-Max-Jump distance and its applications. arXiv preprint arXiv:2301.05994 (2023).", and essentially first finds an MST, and uses the fact that the minimax distance between any s and t is the maximum weighted edge on the st path in the MST. Then they use this fact to fill up an n by n matrix storing all these values. This paper basically codes this algorithm up.

### Strengths
the problem is well motivated in general.

### Weaknesses
The most prominent weakness of this work is that it only provides an implementation of the existing method of the previous paper of Liu (arXiv 2023). I think the implementation itself can be considered as a significant contribution when the original algorithm has some difficulties in implementing and they are tackled by some novel or dedicated techniques. However, the implemented algorithm (Figure 1(a)) is much simpler that seems to be easily implemented, and actually it is implemented by short Python codes (Figure 1(b)). We do not find any implementation techniques in Section 3; Section 3 consists of just an explanation for the existing method of Liu. This means that obtaining simple algorithm that is easy for implement has already been done in the previous work. Thus, I think this is not a significant contribution.

Another weakness of this work is that it is never compared empirically with the existing (and traditional) O(n^2) algorithm. In the conclusion, the authors claim that the SLINK algorithm of Sibson (1973) is difficult to implement by quoting the conversation with other people. However, we easily find some SLINK implementations such as https://github.com/battuzz/slink and https://github.com/jackyust/SLINK_CLINK . Moreover, the paper of Sibson also has a FORTRAN implementation of his algorithm. Thus, it is questionable that the SLINK algorithm is hard to implement. At least, the authors should try to implement SLINK and compare it with the proposed implementation.

Minor comments:
- The citations should be enclosed with brackets. Maybe you use \citet{...} instead of \citep{...}, don't you?
- Tables 1 and 2 are significantly wider than the paper width; please fit these tables into the paper width.

### Questions
I fundamentally don't see the point in this paper, it seems that all the heavy work and clever ideas were due to the Liu paper. Your correspondence in the conclusion section talks about a paper that was written before Liu, and I believe that implementing that would be hard, but it doesn't mean that implementing Liu's algorithm is hard. Implementing Liu's algorithm seems like a homework exercise, and please clarify any obstacles in doing this.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Given a weighted graph and a vertex pair, the minimax path problem is to compute a path between the given vertex pair such that the maximum weight of the edges in the path is minimized. All pairs minimax path problem seeks to compute the maximum weight of the minimax path for every vertex pair. This paper implements a fast algorithm for the all pairs minimax path problem, which is proposed in the previous paper. Experiments show that their implementation is indeed faster.

### Strengths
Judging from the manuscript, this is the first implementation for $O(n^2)$ time algorithm for the all pairs minimax path problem. Because this algorithm works for any graph including dense graph (where $m=\Theta(n^2)$), this is actually an optimal algorithm.

### Weaknesses
The most prominent weakness of this work is that it only provides an implementation of the existing method of the previous paper of Liu (arXiv 2023). I think the implementation itself can be considered as a significant contribution when the original algorithm has some difficulties in implementing and they are tackled by some novel or dedicated techniques. However, the implemented algorithm (Figure 1(a)) is much simpler that seems to be easily implemented, and actually it is implemented by short Python codes (Figure 1(b)). We do not find any implementation techniques in Section 3; Section 3 consists of just an explanation for the existing method of Liu. This means that obtaining simple algorithm that is easy for implement has already been done in the previous work. Thus, I think this is not a significant contribution.

Another weakness of this work is that it is never compared empirically with the existing (and traditional) O(n^2) algorithm. In the conclusion, the authors claim that the SLINK algorithm of Sibson (1973) is difficult to implement by quoting the conversation with other people. However, we easily find some SLINK implementations such as https://github.com/battuzz/slink and https://github.com/jackyust/SLINK_CLINK . Moreover, the paper of Sibson also has a FORTRAN implementation of his algorithm. Thus, it is questionable that the SLINK algorithm is hard to implement. At least, the authors should try to implement SLINK and compare it with the proposed implementation.

Minor comments:
- The citations should be enclosed with brackets. Maybe you use \citet{...} instead of \citep{...}, don't you?
- Tables 1 and 2 are significantly wider than the paper width; please fit these tables into the paper width.

### Questions
Since the APPD matrix contains O(n^2) elements, explicitly computing APPD matrix in O(n^2) time is an optimal algorithm. Thus, I want to consider a variant of this problem: given a graph $G$ with $n$ vertices and $m$ edges, we preprocess $G$ to build a data structure $D$ that can answer the minimax path distance of any vertex pair in reasonable time. For relatively dense graphs, where $m=o(n^2)$ and $m=\omega(n)$, we can expect to lower the preprocessing time or space requirement below $n^2$ at the cost of query time of $D$. Do you know any existing works for this problem?

### Soundness
1

### Presentation
2

### Contribution
1
