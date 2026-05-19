# Learning-Augmented Frequent Directions

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
An influential paper of Hsu et al. (ICLR'19) introduced the study of learning-augmented streaming algorithms in the context of frequency estimation. A fundamental problem in the streaming literature, the goal of frequency estimation is to approximate the number of occurrences of items appearing in a long stream of data using only a small amount of memory. Hsu et al. develop a natural framework to combine the worst-case guarantees of popular solutions such as CountMin and CountSketch with learned predictions of high frequency elements. They demonstrate that learning the underlying structure of data can be used to yield better streaming algorithms, both in theory and practice.

We simplify and generalize past work on learning-augmented frequency estimation. Our first contribution is a learning-augmented variant of the Misra-Gries algorithm which improves upon the error of learned CountMin and learned CountSketch and achieves the state-of-the-art performance of randomized algorithms (Aamand et al., NeurIPS'23) with a simpler, deterministic algorithm. Our second contribution is to adapt learning-augmentation to a high-dimensional generalization of frequency estimation corresponding to finding important directions (top singular vectors) of a matrix given its rows one-by-one in a stream. We analyze a learning-augmented variant of the Frequent Directions algorithm, extending the theoretical and empirical understanding of learned predictions to matrix streaming.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper discusses the problem of online learning of frequent directions given a stream of vectors. In particular, they also consider the learning-augmented problem, where one has access to a predictor that provides estimate of which directions are frequent. They also address the problem of frequent items, since this a special case of the frequent direction problem, where item i is associated to the standard vector e_i.

The contribution of the author is two-fold. They first study the problem of frequent directions using power-law distributed data (i.e., in this case the singular values of the input matrix A, that is given online row by row, follow a power law or Zipfian distribution). To this goal, they analyze the Frequent Direction Algorithms (Ghashami et al., 2016) in this setting (Theorem 3.3). Additionally, they also shows that if one has access to a perfect learning oracle, the expected error of the algorithm can decrease. As a special case, they also shows that a variation of this algorithm (based on the Misra-Gries algorithm, that is the 1-dimensional variant of the frequent direction algorithm), allows to solve the (learning-augmented) frequent item problem with Zipfian distribution law of the frequency. In particular, they retrieve the results of the previous work with a simple deterministic algorithm, compared to previous work that is based on CountMin sketch and is randomized.

### Strengths
The paper is within the algorithms with prediction framework, that was subject to a considerable amount of research in the last years. The paper studies a new problem in the algorithms with prediction framework: learning-augmented frequent directions. 

One of the main strength of the algorithm is that they are also able to recover, with a simple algorithm, results of the previous work for the special case of frequent items.

Another strength of the paper is that it is extremely well-written. The technical section is easy to follow. The results look correct.

Due to the simplicity of the algorithm, clarity of exposition, and the relevance of the results, I believe this paper provides a good contribution.

### Weaknesses
The paragraph on robustness 361-366 is not clear. It seems that they constraint the oracle to provide still a lot of valuable information. I believe it would be better to provide instead sufficient conditions required on the oracle to still obtain the approximation guarantees of Thm 3.4 (or resp., Thm 3.2). It seems to me that appendix E shows that one can accomodate an arbitrary bad oracle (Theorem E.1) using a modification of the algorithm. Unless I am missing something, I believe this is more important than the robustness paragraph 361-366, and should be maybe included in the main paper.

Pages 15-28 contains a sequence of plots with virtually almost no-text (Figure 53 seems a very high number of figures). I think it would be better to select some plots that are then discussed with text to express a message, or summarize the information in a different and more concise manner.

### Questions
See weakness.

The lower bound of Thm.1  and Thm.3 seems specific to the algorithm that is used. Is there any lower bound that applies for any algorithm, given an input sequence that satisfies the Zipfian law assumption?

### Soundness
4

### Presentation
3

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
This paper presents a theoretical and empirical study of learning-augmented streaming algorithms, focusing on frequency estimation and its extension to matrix streaming. The authors introduce a learning-augmented variant of the Frequent Directions algorithm and demonstrate both theoretical improvements and practical benefits when combining learned predictions with traditional streaming algorithms.

### Strengths
1. The paper provides a clear theoretical analysis of both learning-augmented Misra-Gries and Frequent Directions algorithms. Achieves state-of-the-art bounds for learning-augmented frequency estimation with a simpler, deterministic algorithm

2.  Successfully extends learning-augmented techniques from frequency estimation to matrix streaming

3. Comprehensive experimental evaluation on real-world datasets. Shows 1-2 orders of magnitude improvement over baseline algorithms and very close to SVD algorithm which is memory intensive.

### Weaknesses
1. Limited diversity in the prediction models used. More comparison with other learning-augmented streaming algorithms would strengthen the evaluation


2. Could benefit from ablation studies on prediction quality vs. performance

### Questions
1. Is there a fundamental trade-off between space usage and prediction accuracy?
2. How does the performance vary with different stream lengths?
3. How does the approach scale to very high-dimensional data?

### Soundness
2

### Presentation
2

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
This paper studied the learning-augmented frequent directions, which is a natural generalization of the frequency estimation problem in a stream of elements. The frequency estimation problem asks the following question: we are given a stream of $n$ items that below to at most $d$ distinct elements, what is the additive error we could get for the estimation with a limited memory $m\ll \min(n,d)$. Learning-augmented frequency estimation, which additionally assumes a (potentially erroneous) oracle that returns a predicted frequency of each element *and* the Zipfian distribution of the elements, has been extensively studied in recent years. The state-of-the-art error bound was given by ACNSV [NeurIPS’23] for frequency estimation.

This paper asked if we want to generalize the frequency estimation in high-dimensional applications. Here, a natural setup is to have multiple $d$-dimensional vectors $A_1$, $\cdots$, $A_n$. Furthermore, the following aspects are defined for the generalization.
- To generalize the notion of frequency estimation error, the paper used a notion of the error of vector projection to the singular vectors of the matrix formed by $A=[A^T_1, A^T_2, \cdots, A^T_n]^T$. 
- To generalize the distribution assumption of Zipfian distributions, the paper used the notion of the square of the $i$-th largest singular values of the matrix $A$ being inversely proportional to $i$.
- To generalize the frequency prediction, the paper introduced an oracle that directly predicts orthogonal frequency directions, which are the ``right rows’’ an optimal algorithm should have used.

The paper showed that (learning-augmented) frequency estimation can be reduced to the (learning-augmented) frequent direction problem defined above. This justifies the claim that this problem is a *natural* extension of the frequency estimation counterpart.

The paper obtained a frequent direction algorithm with $O(\log{m}\cdot \frac{\log{d/m}}{\log^{2}{d}}\cdot \frac{\||A\||^2_{F}}{m})$ additive error for $m$-memory algorithms even without predictions (by taking advantage of the ‘Zipfian’ distribution of the matrix).  For algorithms with predictions, the error bound becomes $O( \frac{1}{\log^{2}{d}}\cdot \frac{\||A\||^2_{F}}{m})$, assuming the prediction is at least accurate on a constant fraction of the predicted frequency directions. The paper further generalized their results to the frequency estimation problem, showing that it is possible to recover the best bound for the frequency estimation problems using the new algorithm.

### Strengths
My overall opinion of this paper is quite positive: it is well-motivated and well-written, and it contains quite some results that could be interesting to a wide range of audiences both in machine learning and algorithms in general. Barring some lower-order exposition issues, the paper is generally easy to follow, and the technical idea, while simple, is quite neat. As such, the paper is a clear acceptance from my perspective.

### Weaknesses
I do not see any major weakness in the paper. Some comments for expositions:
- The column indexing of the SVD in algorithm 1 is not as clear as it could be. I suggest having a notation section that lists all the notations you use in the paper.
- Calling the lemma statement of Liberty [Arxiv’22] a ‘fact’ is perhaps overly trivializing the significance of the lemma. I would say to call it a ‘proposition’ (I know it’s a one-line proof, but still :)).
- The discussion about the robustness in the main paper is perhaps too sketchy. I understand that you have a more detailed discussion in the appendix; however, I think it’d be helpful if you could expand the discussion.

### Questions
In the experiment, you used SVD as a benchmark. Can you give the error bound for storing all vectors in $A$ and run SVD? In particular, does the error also scale with $\||A\||^2_{F}$?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work revisits the problem of learning-augmented frequency estimation and provides simplified, improved, and generalized results. In the classic frequency estimation problem, we wish to estimate the number of occurrences of an item in a stream up to some small error. In the “learning-augmented” setting, we assume that some oracle tells us the most frequent items, which allows for better algorithms. Furthermore, the stream is also assumed to follow a Zipfian distribution, that is, there is a clear choice of “most frequent items” so this assumption is actually useful. Prior work on this subject, such as the work of Hsu et al. (2019), uses randomized algorithms based on CountMin, CountSketch, and related constructions. The current work shows that the Misra-Gries algorithm, a classic deterministic algorithm for frequency estimation, actually obtains sharp guarantees for this problem. Furthermore, this work also generalizes this to the vector setting, where the stream items are vectors and the desired output is estimates to the singular vectors of the stream viewed as a matrix. In this setting, Misra-Gries corresponds to the frequent directions algorithm, and the authors obtain similar guarantees.

### Strengths
The paper is remarkably well written. Every time I wanted to ask a question to the authors, I felt like it was almost immediately answered in the following text. The contribution is also solid, and gives a clean improvement to prior work on this subject. The experiments were also insightful, and showed how an initial estimate of the top singular values can be used as the “learned frequent directions” for use in the learned frequent directions algorithm. In hindsight, this seems pretty similar to related ideas in numerical linear algebra about using a coarse estimate of the top singular components when designing algorithms for matrix estimation tasks, such as https://arxiv.org/abs/2010.09649 and https://arxiv.org/abs/1511.07263. Connections to such works might be interesting to include.

### Weaknesses
The only complaint is that the paper is pretty much a combination of existing and known ideas. However, it is a high quality implementation of such a study and adds valuable information to this literature.

### Questions
None at this time.

### Soundness
4

### Presentation
4

### Contribution
3
