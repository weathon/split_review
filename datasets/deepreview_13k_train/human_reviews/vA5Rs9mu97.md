# Compressed Online Sinkhorn

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
The use of optimal transport (OT) distances, and in particular entropic-regularised OT distances, is an increasingly popular evaluation metric in many areas of machine learning and data science. Their use has largely been driven by the availability of efficient algorithms such as the Sinkhorn algorithm. One of the drawbacks of the Sinkhorn algorithm for large-scale data processing is that it is a two-phase method, where one first draws a large stream of data from the probability distributions, before applying the Sinkhorn algorithm to the discrete probability measures. More recently, there have been several works developing stochastic versions of Sinkhorn that directly handle continuous streams of data. In this work, we revisit the recently introduced \textit{online Sinkhorn algorithm} of \cite{mensch2020online}. Our contributions are twofold: We improve the convergence analysis for the online Sinkhorn algorithm, the new rate that we obtain is faster than the previous rate under certain parameter choices. We also present numerical results to verify the sharpness of our result. Secondly, we propose the \textit{compressed online Sinkhorn algorithm} which combines measure compression techniques with the online Sinkhorn algorithm. We provide numerical experiments to show practical numerical gains, as well as theoretical guarantees on the efficiency of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper deals with computing entropic regularized optimal transport distances between continuous distribution. Traditionally, one draws samples from the continuous distribution and then computes these distances between discrete distribution by constructing an $n^2$ sized cost matrix. However, the focus has shifted on finding the distances between continuous distributions directly. The challenge in doing so is that how one can compactly represent the continuous dual functions in a discrete manner. Mensch and Peyre introduced the online Sinkhorn where they primarily showed how to execute the Sinkhorn algorithm by representing the continuous duals compactly and showed how the dual functions converge to the optimal ones. 

There are two main contributions of this paper. First, the authors provide an updated convergence rate for the online Sinkhorn algorithm (after correcting an existing inaccuracy in the work of Mensch and Peyre). They also conduct experiments to suggest that their bound may be tight for certain distributions.

Second, the sample size grows polynomially as the algorithm progresses. To make it more space efficient, they provide a compression mechanism to represent the distributions leading to certain gains in experiments.

### Strengths
The problem of estimating dual potentials for OT on continous distribution is a difficult one. For this reason, despite being incremental in nature, I think the result may be important.

### Weaknesses
On the negative side, I had a hard time appreciating the five different assumptions made in the paper. I couldn’t quite tell whether they were necessary or they were made as a matter of convenience. Specifically, while Assumption 1 regarding cost regularity is standard for optimal transport, the necessity of the specific step-size choices in Assumption 2 is not clear. It would be helpful to have a more detailed justification for why these particular step-size schedules are required for the convergence proof. Furthermore, the batch size criteria in Assumption 3, while related to Monte Carlo accuracy, needs more explanation as to why this specific relationship is crucial for the overall algorithm's performance. The interplay between Assumptions 4 and 5, which are linked to the error term $O(t^{b-a})$, also needs further clarification. It's not immediately obvious why these specific conditions are necessary to control the error and how they relate to the Online Sinkhorn error. A more intuitive explanation of these assumptions and their impact on the algorithm's convergence would be beneficial.

Also, the paper is written in a way that makes it only accessible to people who are familiar with previous work (and not for folks who may have a good understanding of the optimal transport problem but lack familiarity with online Sinkhorn). I’m still not able to fully appreciate the result and understand within the landscape of existing algorithms (including time, space and sample complexities etc) for approximating continuous optimal transport. A discussion on this would be good.

### Questions
NA

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The Sinkhorn algorithm for entropy-regularized optimal transport is well-known, but very computationally complex. The present paper considers two online variants of this method. The first one comes from a Mensch and Peyré: the bound here is sometimes worse, sometimes better, but the present paper claims (convincingly) through theory and simulations that the previous bound was wrong. The second variant is a compressed version of online Sinkhorn where the random samples are compressed eg. via quadrature techniques.

### Strengths
The idea of compressing measures seems very interesting from an algorithmic point of view. The analysis is quite simple. (See below, however.) The previous bound for the first algorithm does seem to have been incorrect.

### Weaknesses
The bounds depend on a constant $\kappa$ that can be quite small. The proofs are fairly straightforward.

Proof writing leaves a bit to be desired and I had trouble following some arguments.

1) The constant $\kappa$ and the fact that it is at most $1$ are explained for the first time
2) I believe the Lipschitz constant in Lemma 4 (with the notation employed) should be $L$, or maybe the formula for $T_\beta$ is missing a $1/\epsilon$ factor in the exponent. 
3) The last equality in the first math display in page 13 should probably be an upper bound.

### Questions
See the above points where I had trouble.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper adds a compression step on top of the online sinkhorn algorithm of Mencsh and Peyré in regimes in which some measure compression can be perform. They show two such compression schemes: gaussian quadrature and to Fourier moments compression. They analyze the method theoretically and provide numerical evidence of its lower runtime while the observed error empirically is comparable to the one of the uncompressed method.

### Strengths
The authors provide two settings for which their compression can be implemented: Gaussian quadrature and Fourier moments compression.

They fix a minor error in a proof of a previous paper on online Sinkhorn.

Numerical evidence is presented.

The paper is well written.

### Weaknesses
The experiments are done in settings of very low dimensionality. For the one of greater dimension (d=5), the uncompressed method starts to look quite better.



### Questions
I wonder if what I mentioned above regarding the uncompressed method working better and better with increasing dimension is a general trend.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Sinkhorn is a popular algorithm for calculating entropic-regularised OT distances. However, before applying the Sinkhorn algorithm to the discrete probability measures, one should first draw a large stream of data from the probability distributions. This situation has been improved by online Sinkhorn method, which continuously samples data from two probability distributions in batches and iteratively computes the results. This paper revisits the recently introduced online Sinkhorn algorithm of $Mensch\ \& \ Peyre \ (2020)$ and rises two improvements. 

1. This work presents a new convergence rate for the the online Sinkhorn algorithm, which is faster than the previous rate under certain parameter choices.

2. Under two new assumptions, the authors propose the compressed online Sinkhorn algorithm which combines measure compression techniques with the online Sinkhorn algorithm. Under certain parameter values, the new algorithm theoretically has a faster speed and smaller error than the previous online Sinkhorn algorithm.

The authors also provide experimental results to show the numerical gains of these two improvements.

### Strengths
1. The authors provide clear theoretical analysis for the issues present in  Mensch and Peyre  (2020)  and their new method.
2. The presentation of the results are clear.

### Weaknesses
1. The authors do not discuss the performance of the algorithm in high-dimensional situations. Real-world data often has a high dimensionality (such as datasets of images and amino acid sequences), but the authors do not discuss cases where $d > 5$. In \textbf{section A.5.2}, for data of dimension $d$, the compression error is $O(\frac{|\log m|^{d}}{m})$, which may too large in high-dimensional situations (i.e., assumption 4 with a large coefficient for $O(m_t^{-\zeta})$). In fact, in the experimental part,  Figure 2(c), when d=5, the online Sinkhorn algorithm already has lower error than the new compressed online Sinkhorn algorithm.

2. The Algorithm 2 proposed by the author improves the speed compared to the original online Sinkhorn algorithm by using measure compression technique to compress $u_t$ and $v_t$ from $n$ atoms to $m$. However, there is a trade-off between accuracy and speed. According to assumption 4, the smaller the value of $m$, the faster the algorithm but the larger the error. The article seems to lack a detailed discussion on this matter, such as how to choose an appropriate batch size $m_t$ when solving actual OT problems.

3. The experimental sections lack the application of the algorithm on real-world data and more complex distributions.

### Questions
The new convergence rate of the proposed online Sinkhorn algorithm in this paper is better than the original rate when $a > -b$. Additionally, Algorithm 2 proposed in this paper is theoretically more efficient than Algorithm 1 when $\zeta > \frac{3(a-b)}{4a+1}$. However, the paper lacks an explanation on how to choose specific values for parameters $a$, $b$, and $\zeta$, which makes the experiments in this paper somewhat less persuasive. Please explain why specific parameter values are chosen in the experiments.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
