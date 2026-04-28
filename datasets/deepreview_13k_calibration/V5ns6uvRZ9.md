# Robustness Auditing for Linear Regression: To Singularity and Beyond

- Decision: Accept
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
It has recently been discovered that the conclusions of many highly influential econometrics studies can be overturned by removing a very small fraction of their samples (often less than $0.5\%$).
    These conclusions are typically based on the results of one or more Ordinary Least Squares (OLS) regressions, raising the question: given a dataset, can we certify the robustness of an OLS fit on this dataset to the removal of a given number of samples?
    Brute-force techniques quickly break down even on small datasets.
    Existing approaches which go beyond brute force either can only find candidate small subsets to remove (but cannot certify their non-existence)~\cite{broderick2020automatic, kuschnig2021hidden}, are computationally intractable beyond low dimensional settings~\cite{moitra2022provably}, or require very strong assumptions on the data distribution and too many samples to give reasonable bounds in practice~\cite{bakshi2021robust, freund2023towards}. 
    We present an efficient algorithm for certifying the robustness of linear regressions to removals of samples.
    We implement our algorithm and run it on several landmark econometrics datasets with hundreds of dimensions and tens of thousands of samples, giving the first non-trivial certificates of robustness to sample removal for datasets of dimension $4$ or greater.
    We prove that under distributional assumptions on a dataset, the bounds produced by our algorithm are tight up to a $1 + o(1)$ multiplicative factor.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies data-based robustness for linear regression. Given an OLS solution that predicts $Y$ from $X$ (based on dataset $(X_1, Y_1), \dots, (X_n, Y_n)$), target direction $e$, and $1 \leq k \leq n$, they estimate $\Delta_k(e)$, the maximum possible change along the direction $e$ in $\beta$, the solution to the OLS, that can be achieved by removing $k$ points from the dataset. In essence, $\Delta_k(e)$ measures the robustness of a linear regression to potential training-time adversarial attacks.

Their main contribution is an algorithm, ACRE, which computes upper and lower bounds $U_k$ and $L_k$ for $\Delta_k(e)$. ACRE operates by bounding the difference between $\beta_S$, the value of $\beta$ after restricting to a subset, $S$ of the data, and $\beta$ by expressing it with two terms: first, a combination of the residuals of the original regression, and second, a higher order term, that factors in matrix terms based on the dataset $X$.

Next, ACRE bounds each of these terms by reducing them to Maximum Subset Norm (MSN) problems. The MSN problem consists of computing a subset of vectors from a set of vectors with the largest possible $L_2$-norm of their sum. This problem, while still posing significant combinatorial difficulty, is subsequently solved by a Refined Triangle Inequality (RTI)-based method which essentially uses a greedy approach.

Their first theoretical result shows that the upper and lower bounds absolutely hold for any data-set. The quality of the solution, however, is based on the difference between $U_k$ and $L_k$. They then show that for exponentially tailed distributions, the ratio $\frac{U_k}{L_k}$ is at most $1 + O \left( \frac{d + k \sqrt{d}}{n} \right)$. 

This paper also includes an adaptation of their algorithm for regressions that involve categorical data called OHARE. For this algorithm, they show that for datasets satisfying certain technical properties, they can obtain a bound of $\frac{U_k}{L_k}$ of at most $1 + O\left(\frac{1}{\sqrt{\log n}}\right)$. They then experimentally validate this algorithm by demonstrating its effectiveness in the Nightlights study, where they obtain a provable lower bound on the minimum number of examples that need to be changed in order to reverse the main findings of the study. 

They also include audits of 13 other linear regressions.

### Strengths
This paper is well written and proposes a nice solution to a simple fundamental problem. Due to the challenging nature of this problem, their results still hinge on a reduction to an NP-complete problem. However, they are able to give performance bounds on their algorithm's tightness (both theoretically and experimentally), and crucially their algorithm improves over the naive approach (trying all subsets of size $k$) enough to provide meaningful audits of how robust the results from real-life linear regressions are.

### Weaknesses
There is, of course, a gap between the theoretical bounds on $\frac{U_k}{L_k}$ and its behavior in practice (probably due to the nature of the assumptions needed to prove bounds on this quantity). Additionally, this algorithm is probably still not feasible for very large values of $k$. However, I do view this last weakness to be quite thoroughly addressed with the comprehensive empirical evaluation provided on real regressions.

### Questions
Do you have a comment on how to expand your theoretical tightness results to broader types of assumptions on $X$ and $Y$. In particular, can you show a more general (but perhaps weaker) bound on $\frac{U_k}{L_k}$.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents two algorithms, ACRE and OHARE, designed to audit the robustness of Ordinary Least Squares (OLS) regression models. This robustness is assessed by determining how removing a small subset of data points can alter the regression parameter vector. For detailed comments, please see strengths, weakness, questions section.

### Strengths
1) The paper addresses an interesting problem of auditing in linear regression. 
2) Rigorous theoretical analysis using interesting proof techniques like bounds via maximal subset sum norm (MSN) or knapsack-style dynamic programming.  
3) The authors have tried experiments on real datasets.

### Weaknesses
1) Line 22: Instead of saying hundreds of dimensions, the authors should specify the exact value of d and n. Later in the paper, the authors have specified that they assume n>>d. Hence, saying hundreds of dimensions sounds slightly misleading. 
2) Line 135: The authors claim no assumptions whatsoever on X and Y. Aren’t you assuming well-behaved in Definition 1 and also iid? Also, see line 159 about assumptions. The distinction between unconditional truth and tightness under assumptions is not clearly articulated, making it difficult to understand the scope of each theorem. The assumptions, even if mild, need to be explicitly stated for each result.
3) Line 253: Authors claim distributions with heavier tails than sub-exponential can still be well-behaved. 
While this is true, the authors should provide more information or intuition on which heavy-tailed distributions can specifically be well-behaved and which are not. For example, the counter-statement with some heavy-tailed distribution not being well-behaved can also be true. The lack of concrete examples makes it hard to assess the practical applicability of the claims.
4) Line 295: The authors believe that the error term 1/\sqrt(\log(n)) is nearly tight. Is there a formal proof for the tightness of the bound? The absence of a proof or even a sketch of the argument makes this claim difficult to evaluate.
5) Line 322: The authors claim that loose bounds suffice. Why? Are the proposed bounds loose? Because the authors have also claimed the bounds to be nearly tight. This is slightly contradictory. What are the challenges in deriving tighter bounds? The relationship between the looseness of the MSN bounds and the tightness of the robustness bounds is unclear and needs further explanation.
6) Line 374: The authors bound the first term using a greedy algorithm. What will the computational complexity be for that? Is this greedy step just for theoretical analysis? The computational cost of the greedy algorithm is not explicitly stated, and it's unclear if it's practical for large datasets.
7) Line 390: The authors assume the max eigenvalue of a matrix which is a function of T (an unknown variable or variable of interest). This is slightly unconventional. The dependence of the eigenvalue on an unknown variable T is unusual and requires more justification.
8) Line 399: Can the computational complexity be improved from O(n^2 d) to something better? The computational complexity of the algorithm is a concern, especially for large datasets, and potential improvements should be discussed.
9) Line 440: Typo: direct -> direction 
10) Line 441: The assumption on $e$ should be specified in the main theorem. The assumption on the vector e needs to be explicitly stated in the main theorem for clarity and completeness.
11) Line 497: The authors criticize existing works due to their reliance on semi-definite programming. Is the computational complexity of ACRE and OHARE better than existing works? A clearer comparison of the computational complexity with existing methods is needed to justify the proposed approach. 

Although the contributions are noteworthy, it is slightly challenging to follow the paper: 
1) It is tough to follow the story. The authors propose ACRE and then criticize it for proposing OHARE. The narrative flow is confusing, as the authors seem to undermine their own method.
2) Theorem 1.2 and 1.3 are presented even before describing the respective methods.  
3) This makes it tough to develop an intuitive understanding of theorems. For example, please explain the implication of bucket size from Theorem 1.3. What role does it play? What happens if all the bucket sizes are different or if all of them are the same? The lack of intuitive explanation for the theorems and the role of bucket sizes makes it difficult to understand the practical implications of the results.
4) It feels like the authors have tried to squeeze in a lot of information, breaking the story's flow.

### Questions
1) Line 79: The authors talk about crossing a decision boundary. In terms of the regression problem addressed in the paper, a decision boundary is slightly inappropriate. It suits better for classification problem. 
2) Line 158: ACRE and OHARE are claimed to produce nearly matching upper and lower bounds. When do they (ACRE and OHARE) produce the same bounds, and when do they perform differently? 
3) Line 267: ACRE and OHARE are proposed for n>>d. What happens for the more interesting case when n is comparable to d or a high dimensional setting? 
4) Line 352: The norm is not specified in the equation. Is it Euclidean? 
5) Line 385: The authors assume the knowledge of the population covariance matrix.  What is the approach when it is unknown? 
6) Line 464: The authors use a greedy algorithm to obtain the bound. What is the computational complexity?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents two algorithms, ACRE (Algorithm for Certifying Robustness Efficiently) and OHARE (One-Hot aware Algorithm for certifying Robustness Efficiently), for certifying the robustness of Ordinary Least Squares (OLS) regression to sample removal in the dataset with upper and lower bounds. The first algorithm is shown to work for continuous features and the second one with a mixture of categorical and one-hot encoded features.
Given a dataset with features $X_1,...,X_n \in \mathbb{R}^d$ and labels $Y_1,...,Y_n \in \mathbb{R}$, the algorithms provide bounds on how much the OLS coefficients can change when removing $k$ samples. The authors call the maximal discrepancy between the OLS with full dataset and the one where $k$ data points are removed $\Delta_k(e)$ along the direction $e$.

The algorithms provide upper and lower bounds $U_k, L_k$ such that $L_k \leq \Delta_k(e) \leq U_k$, where $\Delta_k(e)$ represents the maximum possible change in the projection of $\beta$ onto direction $e$ when removing $k$ samples. The bounds are proven to be (logarithmically) tight under mild distributional assumptions. One main characteristic of the algorithm is Minimal Subset-sum Norm bounding.

The authors provide some empirical analysis of the efficiency of these algorithms and an explanation of the correctness of ACRE.
The analysis is based on the decomposition of $\beta - \beta_S$ into linear order and higher-order terms where $\beta_S$ is the OLS estimator after the removal of samples.

### Strengths
* The authors provide an implementation in their anonymous repository. The algorithm proposed by them is able to run on consumer grade machines for datasets of sizes of order $n = 10^{4}$.
* The main text provides an excellent introduction to ACRE, explaining the idea behind its definition. The connection to MSN (Maximal Subset-sum Norm) is clearly explained.

### Weaknesses
 * The clarity of the paper is a central issue. In Section 3, the intuition for the actual definition of the algorithm explains the setting and assumptions under which the result is obtained, and the authors believe the algorithm's work is not precise. 
The connection between theoretical guarantees and practical performance needs to be better explained. for example Theorem1.2 and 1.3 could be tested in varying the numbers $n,d$ used for Table 1

* The process of obtaining the values in Table 1 needs to be clearly explained, and the table needs to be clearer. For example, while the algorithms output bounds $(U_k, L_k)$ for each $k$, how these translate to the final numbers reported needs to be clarified. The comparison methodology with baseline methods needs more detail. Any form of cross-validation missing from the experimental results

* Additional experiments can be conducted to strengthen the results.
Performance could be assessed under different types of data distributions using synthetic datasets with known ground truth.
Comparison could also be made with simple baselines (e.g., random sampling).

### Questions
* How sensitive are the bounds values $U_k$ and $L_k$ to the choice of MSN-bounding algorithm?
* How do the algorithms perform when the assumptions about data distribution are violated? In lines 252-253, the authors mention that the result is valid also without the exponential decaying tail assumption. Have the authors tried the algorithm on PowerLaw synthetic data?

### Soundness
2

### Presentation
2

### Contribution
2
