# Tight Rates in Supervised Outlier Transfer Learning

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 6, 5

## Abstract
A critical barrier to learning an accurate decision rule for outlier detection is the scarcity of outlier data. As such, practitioners often turn to the use of similar but imperfect outlier data from which they might \emph{transfer} information to the target outlier detection task. Despite the recent empirical success of transfer learning approaches in outlier detection, a fundamental understanding of when and how knowledge can be transferred from a source to a target outlier detection task remains elusive. In this work, we adopt the traditional framework of Neyman-Pearson classification---which formalizes \emph{supervised outlier detection}---with the added assumption that one has access to some related but imperfect outlier data. Our main results are as follows: 
\begin{itemize} 
\item We first determine the information-theoretic limits of the problem under a measure of discrepancy that extends some existing notions from traditional balanced classification; interestingly, unlike in balanced classification, seemingly very dissimilar sources can provide much information about a target, thus resulting in fast transfer.

\item We then show that, in principle, these information-theoretic limits are achievable by \emph{adaptive} procedures, i.e., procedures with no a priori information on the discrepancy between source and target outlier distributions. 
\end{itemize}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper adopts the traditional framework of Neyman-Pearson classification to formalize supervised outlier detection of transfer learning. The added assumption is that one has access to some related but
imperfect outlier data. The authors first determine the information-theoretic limits of the problem. Next, they also show that, in principle, these information-theoretic limits are achievable by adaptive procedures.

### Strengths
1. The outlier detection in transfer learning is an interesting and valuable topic in the learning community.

2. The literature part is very clear.

3. The structure of the paper is easy to follow.

4. The setup of the paper is clear

5. The paper provided solid theoretic results on the minimax bounds and rates.

### Weaknesses
1. Only finite-sample results are provided. There is no further analysis of asymptotic properties on the large dataset.

### Questions
1. If the size is large, will the results have special asymptotic properties?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides a rigorous theoretical analysis of transfer learning in outlier detection. It first considers a simplified setting in which the optimal outlier classifier is the same between source and target distributions to illustrate how outlier detection differs from standard classification. The paper then addresses the much more difficult setting in which the outlier classifiers could differ, proposing an adaptive algorithm with a theoretical guarantee.

### Strengths
- The paper is very well-presented.
- The theory is compelling and elegant.
- I think that the "same optimal classifier" setting between source and target distributions seems unrealistic (e.g., the setting of Figure 1) but I can see why from a theoretical standpoint, analyzing this simpler setting is a good starting point and already there are interesting insights, especially in contrasting this outlier setup to traditional classification.
- The extension of the transfer exponent to the outlier setting is a valuable contribution.

### Weaknesses
 - As far as I can tell, this paper does not actually follow the ICLR LaTeX template. For instance, the margins don't appear correct? Please fix this.
- There are no numerical experiments. I think this paper would improve dramatically with experimental results, especially on real data, and especially on showing how well the adaptive method in Section 4.8 works in practice.
- Detailed discussion of how applied researchers address this outlier transfer problem in practice would be helpful to provide some point of reference (even if these existing approaches lack guarantees): for instance, even getting a rough understanding of whether there are common conceptual ideas used would be helpful or if actually the methods are just completely different (if so, maybe some discussion of what the key conceptual differences are would be helpful).

### Questions
See "weaknesses".

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the outlier transfer problem, that is, the problem of transfer learning under the setting of outlier detection or rare class classification. The objective of the Neyman-Pearson classification problem, which formalizes the rare class classification problem, is to achieve low classification error on the rare class, while keeping the classification error on the common class under a threshold. However, in practice, we usually have only limited amount of or even none data from the target rare class, but some data from a related source rare class. This is where transfer learning comes into play. The goal of this paper is to theoretically understand when and how the knowledge from a source class can improve the classification performance on a target class under the setting of rare class classification.

The authors first show that at the population level, under certain assumptions, all the solutions to the source Neyman-Pearson classification problem are also solutions to the target Neyman-Pearson classification problem. Then the authors turn their attention to the finite-sample setting. The authors first define the outlier transfer exponent, which is a notion of discrepancy between source and target under a hypothesis class. With that discrepancy, the authors give a minimax lower bound on the target-excess error, which measures the difference between the expected error of the solution obtained by transfer learning and of the optimal solution. Furthermore, the authors propose an algorithm that does not need any prior knowledge of the discrepancy between the source and target class distributions.

### Strengths
1. The paper studied an important practical problem.

### Weaknesses
(1) A lower bound on the target-excess error is not as informative as an upper bound. Is it possible to derive an upper bound on the target-excess error under appropriate conditions?

(2) The algorithm proposed in Section 4.8 requires as input the VC dimension of the hypothesis class. However, in practice, the exact VC dimension may be unknown. Could you please give some practical suggestions on using this algorithm when the exact VC dimension is unknown?

(3) The notation in inequality (4.1) is a little redundant. Since $h_{S, \alpha}^*$ is a solution to the source problem, the difference between the expected error of any $h$ in the hypothesis class and of $h_{S, \alpha}^*$ w.r.t. the source distribution must be non-negative. So, there is no need to use the max function.

(4) The theoretical results mainly rely on the previous techniques.

(5) There is no experiment.

### Questions
There are several typos, including:

(1) Page 4, in the 5th line in Section 3, the source and target problem are denoted by the same notation.

(2) Page 4, in the last line, the LHS and RHS of the second to last inequality are the same.

(3) Page 6, in the 5th line in Section 4.3, $n_S$ should be $n_T$.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
