# Risk Quadrangle and Robust Optimization Based on $\varphi$-Divergence

- Decision: Reject
- Scores: 3, 3, 1, 5

## Abstract
The Fundamental Risk Quadrangle (FRQ) is a unified framework linking risk management, statistical estimation, and optimization. Distributionally robust optimization (DRO) based on $\varphi$-divergence minimizes the maximal expected loss, where the maximum is over a $\varphi$-divergence ambiguity set. This paper introduces the \emph{extended} $\varphi$-divergence and the extended $\varphi$-divergence quadrangle, which integrates DRO into the FRQ framework. We derive the primal and dual representations of the quadrangle elements (risk, deviation, regret, error, and statistic). The dual representation provides an interpretation of classification, portfolio optimization, and regression as robust optimization based on the extended $\varphi$-divergence. The primal representation offers tractable formulations of these robust optimizations as convex optimization. We provide illustrative examples showing that many common problems, such as least-squares regression, quantile regression, support vector machines, and CVaR optimization, fall within this framework. Additionally, we conduct a case study to visualize the optimal solution of the inner maximization in robust optimization.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper integrates the $\phi$-divergence distributionally robust optimization into the Fundamental Risk Quadrangle framework and presents the primal and dual representation of different elements in that quadrangle. They demonstrate how common cost functions including classification, regression and portfolio optimization are fit into the framework.

### Strengths
The paper provides a quite general connection between one generalized f-divergence DRO and the so-called fundamental risk quadrangle and applies to general cost functions.

### Weaknesses
# **Confusing Organization**
The paper’s organization makes it challenging to follow, especially for a theoretically-oriented work. Significant revisions would improve clarity and accessibility for a broader ML audience:

- **Length, Example-Driven Intro**: The first three pages focus heavily on two examples, with numerous mathematical formulas, but lack emphasis on the paper’s main contribution. The connections between the mean, quantile, and extended $\phi$-divergence quadrangle only become apparent after multiple readings, which detracts from the paper's utility. Specifically, the extensive use of equations (1.1) through (1.20) in these introductory examples overwhelms the reader without providing a clear roadmap of the paper's core theoretical contributions. A more concise introduction that highlights the key ideas and their significance would be more effective.

- **Overly Technical Sections**: Sections 2 and 3 are highly technical without sufficient explanatory context. Some definitions, such as Definitions 2.2, 2.3, and 2.4, are only referenced once in Definition 2.5 and are not essential to the main context. For instance, the specific conditions outlined in Definition 2.2 regarding the properties of the deviation measure D could be summarized more succinctly without sacrificing clarity. Moving these, along with Section 2.3 to the Appendix, would better suit a general ML audience.


- **Lack of Cohesion between Sections**: Many disjointed sections create a fragmented flow. Consider reorganizing the technical results by grouping related content (e.g., combining primal-dual discussions in Sections 3 and 4 and merging Sections 5 and 6 to illustrate concrete cost function examples). For example, the derivation of the primal representation in Section 4 could be directly linked to the dual representation presented in Section 3, highlighting the duality relationship more explicitly.

- **Insufficient Explanation of Theorems**: Each theorem would benefit from non-technical explanations to help readers understand its meaning and implications. Currently, the lack of such interpretations makes it difficult to grasp the practical relevance of the results. For instance, the purpose and utility of Propositions 7.1, 7.2, and 8.1 are unclear from a practical standpoint—why and when would these results matter?  A brief discussion of the implications of Theorem 3.1, particularly its connection to existing DRO frameworks, would greatly enhance its impact.

# Unclear Contribution 
The paper’s contributions, particularly in the examples and novel interpretations, are difficult to discern: 

- **Ambiguity in Examples**: It’s unclear what new insights the introductory examples provide. Established methods like CVaR-DRO (Example 3 in [1]) and chi-squared divergence DRO (Proposition 1 in [2]) already use duality forms, such as equations (1.14)–(1.17) and (1.2)–(1.5) being special examples. While the least squares and quantile regression examples appear novel, they lack clear interpretation. A discussion of how the robust model framework alters our perspective on these standard regressions and other cost functions would clarify the framework’s value (e.g., a new perspective?). For instance, how does the proposed framework provide a different or improved understanding of least squares regression compared to classical statistical interpretations?

- **New interpretations in Sec 6**: The interpretation in Section 4 results are unclear. Much of this material appears to be standard in DRO literature or from standard DRO duality, and the equivalence in equations (6.4)–(6.6) is not sufficiently justified. In terms of examples, Specifically, terms $R_{\phi, \beta}$ in (6.4), (6.7), (6.10) are not clearly explained. If these are defined based on Sec 3, should’t they follow directly from the Definition 3.1? Besides, I am struggling to find the connections between this and the risk quadrangle framework. If the intent is to show this framework is more general, then the authors should provide concrete examples illustrating this generality and explain why aspects like negative $Q$ values are important. For example, a detailed explanation of how $R_{\phi, \beta}$ relates to the specific $\phi$-divergence being used and how it impacts the robust optimization problem would be beneficial.

# General Comments
- **Suitability for ICLR**: Given its current form, I am uncertain about this paper’s suitability for an ML-focused conference like ICLR. The risk quadrangle framework may be too theoretical for a general ML audience, and the connection to robust optimization is unclear in terms of practical ML relevance.
- **Notations**: The paper’s notation can be streamlined. For example, similar terms like $Q_{\phi, \beta}^R$ (Line 39), $Q_{\phi, \beta}^V$ (line 104), $Q_{\phi,\beta}$ (Lie 288) represent similar concept. A unified notation would improve readability.

### questions:
 See the weakness above and another clarification question:

- Between Line 94 and 100, what is the choice of $\lambda$ here, it should be $\sqrt{\beta}$ right?

### Questions
See the weakness above and another clarification question:

-	Between Line 94 and 100, what is the choice of $\lambda$ here, it should be $\sqrt{\beta}$ right?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The Fundamental Risk Quadrangle (FRQ) is a risk management framework introduced by Rockafellar and Uryasev in 2013. It integrates risk management, statistical estimation, and optimisation, providing a unified approach and broader interpretation of these problems.

By introducing specific quadrangles (i.e. a quartet of risk, deviation, regret, and error measures) based on $\varphi$-divergence, the authors demonstrate how Distributionally Robust Optimization (DRO) can be incorporated into the FRQ framework.

The authors first derive dual representations of the quadrangle elements, providing a robust optimization perspective on certain classification, regression, and portfolio optimization problems. They then develop the primal representations, which offer tractable formulations—specifically as convex optimization problems—of the dual representations.

Finally, the authors provide examples of classical problems that fall within this framework.

### Strengths
The FRQ framework provides interesting link between various problems in learning and risk management. 
The authors further this link by proposing a unified way of looking at some of those problems.

### Weaknesses
I found the paper very hard to read:
- The introduction opens with two extended examples but lacks a pedagogical introduction to the FRQ framework, which may be unfamiliar to the learning community;
- The paper lacks coherence, with many paragraphs consisting of sequences of juxtaposed sentences;
- The purpose/message of the paper is hard to grasp;

The paper's contribution appears limited. The authors propose a general method for incorporating DRO into the FRQ framework using $\varphi$-divergences. However, the three main examples presented in Section 5 have been well-studied in the literature, making it unclear what is novel and what was previously established.

### Questions
- The dual representation provides a robust optimization (RO) interpretation of the quadrangles elements. Then the authors link RO with DRO in the last paragraph of Section 3. Could the authors explain more precisely this link? In particular, line 318-319, What do they mean by "$Q$ is the Radon-Nikodym derivate $dP_0/dP$"? In particular, what are the distributions $P$ and $P_0$ in this case? It seems to me that for the condition $\mathbb{E}[\varphi(Q)] \leq \beta$ to be expressed as $D_\varphi(P || P_0) \leq \beta$ we would need Q to be distributed according to $P_0$.

- Are the examples presented in the introduction well-known in the literature? If so, could the authors provide relevant references? (Or at least provide a proof in appendix).

- Are there any problems for which the proposed approach offers new primal/dual formulations?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper introduces an extension of the Fundamental Risk Quadrangle (FRQ), a framework that connects risk management, statistical estimation, and optimization. Within this framework, distributionally robust optimization (DRO) based on φ-divergence aims to minimize the worst-case expected loss, where the maximum is taken over a φ-divergence-defined uncertainty set. The authors present the extended φ-divergence and the extended φ-divergence quadrangle, integrating DRO into the FRQ framework. They derive both primal and dual representations for the quadrangle elements, including risk, deviation, regret, error, and statistic. The dual representation allows for interpreting tasks like classification, portfolio optimization, and regression as forms of robust optimization driven by extended φ-divergence. Meanwhile, the primal representation offers tractable convex formulations for these robust optimization problems. Through examples, the paper demonstrates how common problems—such as least-squares regression, quantile regression, support vector machines, and conditional value-at-risk (CVaR) optimization—fit within this unified framework. A case study is also provided, visualizing the optimal solution in the inner maximization problem of robust optimization.

### Strengths
The paper attempts to unify DRO with an existing general stochasric optimization framework (FRQ), which is of theoretical interest.

### Weaknesses
The paper is extremely hard to read, mostly because it consists of a sequence of incoherent/not well motivated definitions and results. While I feel that the paper might have merit in terms of the topic it aims to study, I believe the authors should consider (1) restructuring the paper in a major way, making it readable and coherent, and (2) possibly resubmitting this work to a journal or some other venue allowing for longer articles -- it really feels like they tried to stuff as much material as possible in ten pages, with a very poor result in terms of presentation. Here are some more specific comments:

1. In general, the authors should avoid the $a(b)$ notation to mean $a\times b$, and should reserve it to mean "$a$ is a function of $b$"

2. Page 2, when the authors introduce some key concepts, becomes almost unreadable. What do these concepts mean? The authors basically just present a wall of hard-to-read math;

3. Page 3 is also quite hard to read -- it presents too much math without any context;

4. The paper continues in the same style as the previous two points, till the very end.

### Questions
Although of minor importance compared to my major concerns outlined above, here are two questions:

1. In the illustrative example on Large Margin Distribution Machine, what is $\sigma(\cdot)$ ? From usage below, I guess it denotes the standard deviation of a random variable, but that's not clear at a first reading;

2. On page 2, talking about linear regression, do the authors mean $\Vert \cdot \Vert$ to be the $L^2$-norm for random variables?

To be clear, I think there's many more such points that need clarification/revision throughout the text, but I think this is best left to a future major restructuring effort to put the paper in better shape.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper studies how distributional robust optimization (DRO) can be integrated into the fundamental risk quadrangle (FRQ) framework. It derives a dual and a primal formulation and presents many examples.

### Strengths
The paper offers many interesting reformulations for various optimization problems.

### Weaknesses
I found the structure of the paper very confusing and hard to follow, and I am afraid that many of its important points are just not coming through. Without any word in the introduction the paper jumps into "demonstrating examples", and the reader is left without motivation until section 1.2 which appears only on the 4th page. Also, sections 7 and 8 show results without discussion or motivation.

There are many typos and weigh sentences, some examples:
- I guess "negative" should not be there for "negative asset returns", or why do you only consider negative ones?
- There is $\lambda$ and $\beta$ in the description of the Mean Quadrangle on page 2, I guess there should be some relationship between the two.
- "A specific case of the extended $\varphi$-divergence quadrangle is called $\varphi$-divergence quadrangle ..."
- "The next theorem proves the dual representation of the extended $\varphi$-divergence quadrangle." while the "extended $\varphi$-divergence quadrangle" is a definition, it needs no proof.

The equivalence of (1.6) and (1.7) does not look correct to me as the former is independent of $\beta$ while the latter is not. In particular, if you choose $\beta = 0$, then Q = 1 almost surely and the objective value of (1.7) is zero while (1.6) might not be. Could you comment on this, is there anything missing here?

### Questions
The equivalence of (1.6) and (1.7) does not look correct to me as the former is independent of $\beta$ while the latter is not. In particular, if you choose $\beta = 0$, then Q = 1 almost surely and the objective value of (1.7) is zero while (1.6) might not be. Could you comment on this, is there anything missing here?

### Soundness
3

### Presentation
2

### Contribution
2
