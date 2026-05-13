# RACH-Space: Reconstructing Adaptive Convex Hull Space with applications in weak supervision

- Decision: Reject
- Scores: 3, 3, 5, 5, 3

## Abstract
We introduce \emph{RACH-Space}, an algorithm for labelling unlabelled data in weakly supervised learning, given incomplete, noisy information about the labels. \emph{RACH-Space} offers simplicity in implementation without requiring hard assumptions on data or the sources of weak supervision, and is well suited for practical applications where fully labelled data is not available. Our method is built upon a geometrical interpretation of the space spanned by the set of weak signals. We also analyze the theoretical properties underlying the relationship between the convex hulls in this space and the accuracy of our output labels, bridging geometry with machine learning. Empirical results demonstrate that \emph{RACH-Space} works well in practice and compares favorably to the best existing label models for weakly supervised learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Assume a dataset of size $n$ for a $k$-class classification problem is available, with unknown true labels but accompanied by $m$ independent "weak signals" that, on average, outperform random guessing. Then, the primary objective of this paper is to estimate the true labels for this weakly supervised dataset using only the mentioned $m$ independent "weak supervisors". Specifically, the authors assume that for each data point $i \in [n]$, each of these $m$ weak supervisors can assign a vector of size $k$ where the $j$th component conveys information about the probability of $X_i$ belonging to class $j$ (resulting in a total of $m\times n\times k$ signals). The paper lacks rigorous mathematical modeling regarding how this "information" is collected, and it seems that the authors rely on unspecified heuristics in this regard. From my multiple readings of this part of the paper, it appears that the mentioned weak signals somehow act as probabilities.

The proposed algorithm in this work, called RACH-space, aims to estimate the true labels by linearly combining the vectors provided by the supervisors. The authors introduce an unclear $\ell_2$-minimization scheme for determining the optimal linear combination, which may potentially yield infinitely many solutions. The remaining theoretical section concentrates on constraining the solution space and ensuring the feasibility of the estimator. Towards the end, the authors present experimental results on several datasets, although I did not thoroughly analyze this part.

The paper suffers from issues of clarity and seems to provide limited theoretical contributions. The lack of substantial mathematical modeling concerning the problem makes it challenging to assess the achievements. Many sections are difficult to follow, and it's possible that I may have overlooked critical aspects of the work. At this point, I recommend rejection. However, I kindly request the AC to seek the opinions of other reviewers with more confidence scores.

### Strengths
- The primary problem in this paper, i.e., learning from weakly supervised datasets, is an interesting line of work.

### Weaknesses
- The paper's writing quality can be significantly improved. I have identified numerous grammatical errors and vague phrases that should be addressed to enhance the paper's overall readability. Additionally, the literature review section and the section explaining the motivations behind this work lack informativeness for similar reasons.

- The authors have not provided any information or context regarding the "weak signals" in $\boldsymbol{W}$. Consequently, it is not clear why one should seek a linear combination of the rows of $\boldsymbol{W}$ to approximate the true label vector $\boldsymbol{y}$. Additionally, the motivation and the mathematical procedure leading to the optimization problem in (3.5) remain unclear.

- The theoretical contribution of this work is quite limited and may not meet the standards of ICLR. However, the authors may have achieved success from an experimental perspective, although I did not thoroughly evaluate this aspect. Therefore, if other reviewers believe that the work represents a valuable experimental contribution, I am open to reconsidering my evaluation.

### Questions
Please see "Weaknesses" section.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce RACH-Space, a new classification tool within ensemble learning, ideal for situations with limited supervision (weakly supervised learning). It is easy to implement and doesn't make many assumptions about the data, using geometric interpretations of weak signal spaces. The contributions of the paper are:

1) RACH-Space, an efficient label model that provides synthetic labels for the raw dataset
2) The corresponding weakly-supervised learning algorithm
3) A theoretical analysis of the algorithm

### Strengths
The paper is overall well-written. Notations are correctly introduced and the relevant literature is duly cited.
The problem tackled by RACH-space is of great importance.

### Weaknesses
1) The contributions could be explicitly stated. It is unclear what is proved in the theoretical section.

2) Although I am not an expert in the field, I doubt the RACH-Space is particularly ground-breaking. More serious evidence on real world datasets should be added. For instance, you should test the RACH-Space algorithm on a histopathology dataset where it is common to face weakly-supervised learning problems.

### Questions
1) You state that "Majority Voting and RACH-Space assume that, on average, the weak labels are better than random". Could you discuss the validity of this assumption on real world datasets? Is it realistic to assume this?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduce RACH-Space for weak supervision. The method ultiizes a geometrical interpretation of weak labels and formulates the problem as a least squared problem. The paper overall has some interesting ideas and the experiments show good empirical results. However, there are some critical problems (e.g. writing, misclaims, experiment setup) that need to be addressed.

### Strengths
1. The paper proposes a novel method for label aggregation in weak supervision. As far as I know, the formulation seems to be new. 
2. The paper provides theoretical motivations and justifications for the proposed algorithm. 
3. Good experiment results are shown against baselines.

### Weaknesses
1. Writing can be improved. It’s better to give intuitions before presenting the equations. 
2. There are some unjustified claims. 
3. Experiment setup should be improved to avoid the possibility of cherrypicking.

### Questions
1. It’s very difficult to follow to paragraphs around equation 3.4 and 3.5. In the current form, some choices seem to be arbitrary. This is one example out from many: why do you define A=2W? Why not A=3W? I believe there are reasons and possibly principled reasons behind this, but I don’t get it from the current writing. It is mentioned in abstract that there is a geometrical interpretation. Maybe it’s helpful to introduce the geometrical interpretation first to give more intuition about the method before diving into math?
2. It seems the method heavily depends on “ average expected error rate”. How can one know average expected error rate without assuming the distribution of the error rate? How is average expected error rate defined in the paper?
3. The WRENCH dataset has 14 classification datasets, why four of the datasets were dropped in experiments? It’s the best to include all 14 datasets in order to avoid any possibility of cherry picking. 
4. It is mentioned “experiments are done in the original setup on WRENCH”, but if that’s the case, how come the results are different from the results reported in the WRENCH paper? In the WRENCH paper, MeTaL had better results than MV. Is the difference caused by dropping the 4 datasets?
5. The paper claims it make minimum assumptions as MV, i.e. only assuming weak labels are better than random. However, the proposed method actually implicitly makes more assumptions. For example, it selects the average expected error rate so that b/n is in a safe region. This is already a strong assumption on that one gets to select “average expected error rate”. As the average expected error rate is expected to a single point value. Another assumption roots in the least squared problem. Why not formulate as least absolution deviation problem? What implicit assumptions are you making to formulate the problem to be a least squared problem instead of least absolution deviation?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a classification method for ensemble learning and proves its effectiveness in weakly supervised learning. Specifically, given the data points and the weak signal matrix, this paper proposes a novel method to compute the label vector $\widetilde{\mathbf{y}}$ which approximates the ground truth $\mathbf{y}$. Then the problem is transferred to solving an optimization instance and finding the solution in a convex hull.

### Strengths
(1) The proposed optimization method for finding an approximate label vector is kind of novel.  
(2) The framework for weakly supervised learning connects machine learning and high-dimensional geometry.  
(3) The experimental results indicate the effectiveness of the proposed algorithm.

### Weaknesses
(1) The background is not very clear, especially for the weak signal matrix $\mathbf{W}$. For example, where does the matrix $\mathbf{W}$ come from?   
(2) Some preliminaries are missing. Why the expected error rate $\epsilon_i$ is equal to $\mathbb{E}[\mathbf{w}_i - \mathbf{y}]$? Does each row of $\mathbf{W}$ kind of represent the label vector $\mathbf{y}$?   
(3) As stated in this paper, the computation of $\mathcal{H}_1$ takes time $O((nk)^{\lfloor \frac{m}{2} \rfloor})$ which is prohibitive in practice. The author divided $\mathbf{W}$ into several parts and took their average to reduce the value of $m$. Although the author claimed that this does not make a negative impact on the performance, it cannot convince me since no persuasive proof is provided.

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a novel convex-hull-based method for weakly supervised learning. The proposed method is simple and works under a minimal assumption.

### Strengths
1. The proposed method is novel, as far as I know.
1. The proposed method outperformed other existing methods on average in the numerical experiments.

### Weaknesses
Overall, the presentation of the paper needs essential improvement in the problem-setting explanation, including the introduction section.
1. The definition of "weakly supervised learning" in this paper is not clear, which makes it challenging to understand the motivation of the paper and which applications it might have. The authors referred to some papers in the first and second paragraphs in the introduction section (Shin et al., 2015), (Mintz et al., 2009),  (Chen & Batmanghelich, 2020), and (Karamanolakis et al., 2021). Also, the authored mentioned (Ratner et al., 2016). Although those papers use the phrase "weakly supervised learning," the specific problem settings that they are tackling are different from the authors' formulation in Section 1.1. Hence, the authors are more responsible than usual to state the problem setting in a self-contained and rigorous manner, so that readers can understand which symbols correspond to which data in real applications and what types of assumptions are imposed. 
1. The authors do not mention the link between $\\mathbf{W}$ and $\\mathbf{y}$. If there is no clear link between $\\mathbf{W}$ and $\\mathbf{y}$, we do not need to call the problem setting "weakly supervised learning" since $\\mathbf{W}$ is no longer a supervision.
1. As above, since the problem setting itself is unclear, readers cannot understand the importance of the area and this paper or discuss whether the proposed method is reasonable or not. I encourage the authors to make the assumptions and motivations clearer, ideally in the introduction section.
1. The RACH-space's main idea is not written in the Introduction section, which significantly decreases the readability. I strongly encourage the authors to explain in the introduction section what is the main idea of the proposed method and why the idea solves the issues of existing methods.
1. The definition of the *Majority Voting* is unclear.

### Questions
1. In which application cases, your problem setting in Section 1.1 is applicable? Could you provide specific examples? Specifically, in which case do we have multiple weak supervising signals?
1. The expected error is defined as $\\mathbf{E} [\\mathbf{w}\_\\mathbf{i} - \\mathbf{y}]$. I assume $\\mathbf{E}$ indicates the expectation operator, but what is the random variable of which we consider the expectation here? Also, you are interested in the difference between $\\mathbf{w}\_\\mathbf{i}$ and $\\mathbf{y}$. Does it mean that you assume the value of $\\mathbf{w}\_\\mathbf{i}$ is close to $\\mathbf{y}$? I do not see such assumptions in the paper. 
1. If you assume the value of $\\mathbf{w}\_\\mathbf{i}$ is close to $\\mathbf{y}$ and you are interested in the error between them, why can the error be negative? Don't you need to consider the squared or absolute error or the cross entropy, which is a more natural choice for one-hot vector prediction? 
1. Related to that, you mentioned "Note, Majority Voting and RACH-Space assume that, on average, the weak labels are better than random." Here, what does *better* mean? Could you mathematically define it?
1. Also, if you assume the value of $\\mathbf{w}\_\\mathbf{i}$ is an estimate of $\\mathbf{y}$, why the range of each entry of $\\mathbf{W}$ is $\\mathcal{R}$, which implies it can take any real value outside of $[0, 1]$? Is it a typo?
1. You mentioned many times *Majority Voting* but you do not define *Majority Voting*. What is that? Also, why do you not use *Majority Voting*? Why don't you compare your proposed method with the *Majority Voting*?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair
