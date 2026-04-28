# Interference Among First-Price Pacing Equilibria: A Bias and Variance Analysis

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 5, 8

## Abstract
Parallel A/B testing is a practical method for testing multiple treatments in ad auction platforms simultaneously. 
During a parallel A/B test, the whole market is partitioned into several submarkets, and within each submarket an independent A/B test is run.
However, interference among submarkets is present, incurring bias in the estimate. 

In this paper, using the framework of first-price pacing equilibrium (Conitzer et al., 2022), we view the market equilibrium in auction platforms as a function of the level of interference. 
At a high level, we propose to approximate the market without interference with a first-order expansion from the interfered market, thus removing first-order bias. 
We derive a consistent and asymptotically normal estimator for this first-order surrogate. We demonstrate our theory in parallel A/B testing both theoretically and experimentally.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers A/B testing in online marketplaces, where interference arises because items can be recommended to advertisers in both the control and the treatment groups. The paper adopts the first-price pacing equilibrium (FPPE) framework from prior work [Conitzer et al., 2022], and analyzes how the equilibrium (i.e., pacing parameters \beta and the total revenue) changes as a function of the level of contamination/interference. The paper proposes a first-order bias correction by Taylor expansion and proves consistency and asymptotic normality guarantees under certain regularity conditions. The paper conducts semi-synthetic experiments to demonstrate the effectiveness of the proposed estimators (where the distributions come from real data).

### Strengths
Interference is a well-known, important, and practical problem in A/B testing of online marketplaces. The paper meaningfully extends prior work on pacing equilibria by considering how interference affects the results. The paper provides rigorous theoretical guarantees, complemented by preliminary semi-synthetic experiments.

### Weaknesses
While I find the formulation and assumptions proposed in the paper reasonable, I think the paper can benefit from a discussion on limitations. For example, a natural alternative model is not to partition items into a good set and a bad set, but instead assume an item can be "good" for some groups but "bad" (interference) for other groups. The paper may also discuss other types of interference that the proposed approach does not cover, etc.

===
Additional minor comments:

1. I think the claim in the abstract on demonstrating "the effectiveness of this approach on real experiments on advertising markets at Meta" is an overstatement. I think the paper should make it clear that only semi-synthetic experiments are performed.

2. While I understand citing unpublished work is optional, I think the paper can benefit from citing the following paper:
Zhu, Cai, Zheng, and Si. "Seller-Side Experiments under Interference Induced by Feedback Loops in Two-Sided Platforms". arXiv, 2024.

3.  I find the term "buyer" confusing, as "buyers" can be understood as users who make purchases or sellers who bid for ads. I prefer the terminology of advertisers vs. users introduced in other parts of the paper.

4.  I don't understand details of the experiment in Fig 1. What're the axes? Are these ratios of the two experimental designs? How are two experiments paired? What is the guardrail metric? Also a 79% agreement compared to the 81.5% optimal agreement appears pretty good to me. Is the paper trying to address the remaining 2.5% of the cases?

5.  In Paragraph L87-118, two graphs are introduced. One is a bipartite graph between advertisers and users, from which a graph for advertisers is derived for clustering ("the edge weight between a pair of advertisers..."). It would be helpful to clarify they are not the same graph.

6.  Paragraph L54-63: "Sec" -> "Fig"

### Questions
1. The theoretical guarantees heavily rely on the parameter \eta for the error in estimating the Hessian. Could the authors comment on the the rate \eta for the proposed finite differencing Hessian estimator proposed in the paper? 

2.  Does the guarantee on the revenue in Theorem 4 generalize to estimating other quantities that are a functional of the parameters \beta?

3. Providing a discussion on limitations and addressing my minor comment #4 above would be helpful.

### Soundness
3

### Presentation
3

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
This paper studies how to estimate market equilibria in each submarket when there is interference across submarkets. The authors consider the first-price pacing equilibrium (FPPE) model where each buyer uses a single pacing multiplier to shade values. For each submarket, some items outside would also attract the buyers in this submarket, which is unavoidable since we are unable to find completely isolated submarkets. From the modeling point of view, the supply is contaminated by another distribution. The authors first propose a debiased surrogate, which can approximate the limit FPPE in the uncontaminated market based on the limit FPPE in the contaminated market, and then prove that it has only a small error due to the removal of the first-order bias. Then, since the finit FPPE will converge to the limit FPPE in probability, the above estimator can be applied to the actual dynamic market with a slight modification. The authors also present two asymptotic normality results to further demonstrate the superiority of the estimator. Experiments on semi-synthetic data show that the proposed estimator is indeed less biased in terms of pacing multipliers and revenue.

### Strengths
1. I can understand that A/B test design is indeed a very important issue in the industry. Since buyers will use strategic behaviors to counter the platform's strategy or mechanism, a/b testing is the most effective way to test the platform's strategy/mechanism. However, the vanilla a/b test setup will bring about the issue of mutual influence between a/b groups, which may interfere with the experimental results.

2. The theoretical proof in the paper is non-trivial and very solid. The authors have proved from many aspects that the estimator can indeed converge well to the limit FPPE in the uncontaminated market, which the platform hopes to observe.

### Weaknesses
Overall, this paper is hard to parse. The flow of this paper is not clear enough to assist readers well. The abstract and introduction of this paper both start with a/b testing, but the contribution part does not mention it. It was not until page 6 that I began to realize what the authors are doing. After reading the paper several times, I finally understood the authors' real contribution.

According to my understanding, the real question is how to study the impact of different strategies/mechanisms on market FPPE. The method proposed by the authors is to find relatively isolated submarkets as a/b groups, and then construct an estimator to eliminate cross-market interference. As far as I know, the former is a method that has been adopted in the industry (of course, the issue of cross-market interference remains), while the latter is tailor-made for the FPPE model. Therefore, the focus of this paper's contribution should actually be on FPPE rather than ab test design. In fact, even if all ab test parts are removed, this will still be a complete paper that studies how to approximate the limit FPPE of an uncontaminated market using contaminated data.

Since the estimator in this paper cannot be directly extended to other scenarios, I suggest that the authors should not emphasize the proposal of a novel ab test framework, but use the research on FPPE as the background to introduce challenges and solutions.

### Questions
NA

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes an estimation technique for A/B test revenue by modeling budget interference between two experiments as a mixture of distributions.

At first, the paper is hard to follow for readers unfamiliar with the FPPE formalism, such as myself. Even though I am familiar with advertising systems and budget pacing mechanisms. A lot of symbols and concepts to grasp. However, once I familiarized myself with the relevant cited background, the explanation of modeling of budget interference using a mixture of distribution makes sense, and I believe it's an important concept that this paper introduces.

The experimental section is quite shallow, but I believe that since the paper is focused on rigorous theory, extensive experiments are less important in such a paper.

However, there are many weaknesses of this paper, described below in the weaknesses section, that make me believe this paper requires additional work to make it ready for publication. The largest problem is, I believe, that the theoretical framework of an equilibrium does not appear to model real-world marketplaces with ever-changing pacing factors. However, the paper presents the technique as something applicable in practice, and no attempt is made to close this gap. More weaknesses appear in the weakness section.

### Strengths
- aims to solve an extremely important practical problem
- Introduces an interesting theoretical framework of modeling "budget interference" using a mixture of distributions.
- makes a good job explaining *why* such a modeling is reasonable.

### Weaknesses
 - real budget pacing systems, from my experience, do not operate with constant pacing factors. But the FPPE theory assumes each buyer has one specific pacing factor defined by the equilibrium. There is no explanation in the paper for how this framework actually models the real world of dynamically changing pacing factors, and this limits the usefulness of the estimators in practice. If it is possible to apply the framework to such a dynamic system, there is no explanation in the paper for *how* to do it. So overall, there is no motivation explaining why the equilibrium framework is useful.
- the notation is extremely hard to follow. Typically there is a difference between how vectors, scalars, sets, random variables, and matrices are denoted. For example, vectors by boldface, matrices as upcase-bold, and so on.. It requires a lot of mental effort to follow all the symbols and concepts in the paper, which makes it practically unreadable to audience unfamiliar with the FPPE framework
- a paper aims to show us how to debias the revenue metrics in A/B tests, but it does *not* derive a debiased estimator for the revenue. only for the budget pacing factors. For such an important concept, I'd assume there should be at least a corollary for how the revenue estimator can be computed from the estimated pacing factors, and an explanation for why this estimator is also debiased (it's not obvious that a function of a de-biased estimator is also de-biased in the same sense).

### Questions
- is the decomposition into submarkets part of the contribution or not? It appears as something important, but it's in the introduction, rather than being in the main paper. Why? Please clarify this. If this is a contribution, it should be explicitly evident and not appear in the introduction. If it is not, this should be explicit in the paper, maybe with proper citations.
- Please explain - why is the equilibrium framework applicable in practice, given the changing nature of pacing factors?

### Soundness
3

### Presentation
3

### Contribution
3
