# Deviation Ratings: A general, clone invariant rating method

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Many real-world multi-agent or multi-task evaluation scenarios can be naturally modelled as normal-form games due to inherent strategic (adversarial, cooperative, and mixed motive) interactions. These strategic interactions may be agentic (e.g. players trying to win), fundamental (e.g. cost vs quality), or complimentary (e.g. niche finding and specialization). In such a formulation, it is the strategies (actions, policies, agents, models, tasks, prompts, etc.) that are rated. However, the rating problem is complicated by redundancy and complexity of N-player strategic interactions. Repeated or similar strategies can distort ratings for those that counter or complement them. Previous work proposed ``clone-invariant'' ratings to handle such redundancies, but this was limited to two-player zero-sum (i.e. strictly competitive) interactions. This work introduces the first N-player general-sum clone-invariant rating, called \emph{deviation ratings}, based on coarse correlated equilibria. The rating is explored on several domains including LLMs evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this work, the authors address the problem of rating strategic interactions within a game-theoretic model. They propose a new rating scheme, called Deviation Ratings, which is clone-invariant (i.e., unaffected by repeated or similar actions) and is applicable to multi-player settings.

### Strengths
I do not see a clear strength in this work, apart from introducing a new game-theoretic rating system for multi-player settings with certain advantageous properties. However, this may not be a strong point, as similar concepts already exist in the literature. Furthermore, I am somewhat skeptical about the overall contribution, though I should note that I am not an expert in this field and would welcome the authors’ clarification regarding my concerns.

### Weaknesses
My primary concern is with the definition of the rating scheme itself. Strategies are evaluated based on the advantages of deviation strategies. However, since the rating is assessed under a correlated equilibrium, it would necessarily be negative (or $\leq \epsilon$) in the case of approximate CCE), which seems uninformative. Specifically, the deviation rating $r_p(a'_p)$ is defined as $ \sum_a \sigma^*(a) [G_p(a'_p, a_{-p}) - G_p(a)]$, where the second term $G_p(a)$ is constant with respect to $a'_p$. This constant offset makes the rating inherently non-positive, and it's unclear what information is gained by this offset, as the relative ranking of strategies would be the same without it. For example, the rating scheme in [1] appears more intuitive. It is possible I have misunderstood some details; could the authors clarify?

Additionally, the extension of Nash averaging to general multi-player environments seems to have already been explored in [1]. In particular, [1] defines a rating scheme called Payoff Rating, where a strategy is evaluated based on its expected payoff under the correlated equilibrium $\sigma$, conditioned on that strategy. This approach seems more direct and easier to interpret. As I am not deeply familiar with this area, could the authors further elaborate on the connection between these two results, as the relationship is not clearly highlighted in this paper?

Regarding the rating definition, the authors state that they aim to minimize deviation gains, but it’s not intuitive why one would seek to **minimize** the so-called **gains** of a strategy. It would seem more natural to maximize the gains of a strategy, or to minimize the losses. The current approach of minimizing deviation gains is not clearly motivated, and it's unclear why this is a desirable property for a rating scheme.


### Questions
- **Line 88**: Since the concepts of WSCE and CE, as well as their approximate variants, are not directly relevant to the scope of this work, it might be better to exclude them, as their current presentation adds more confusion than clarity.
- **Line 56**: Typo in "Yoa’s principle."
- **Line 70**: Typo in "for the strictest."
- **Line 103**: In the equation for Nash equilibrium as a product distribution, $\sigma_p(a_1)$ should be $\sigma_1(a_1)$.
- **Line 152**: The rating for Nash averaging can be simplified as there are only two players, so the product notation can be removed.
- **Line 170**: "one alternative to the payoff rating…" The authors in [1] define a rating called Payoff Rating, which employs the same idea of payoff-based rating, potentially contradicting the authors’ claim here. This paragraph does not clearly differentiate between the “mass rating” type and the Payoff Rating, and the term "mass rating" itself lacks a clear definition.
- **Line 197**: How are “deviation gain statistics” defined?
- **Line 225**: Strategies are evaluated based on a correlated equilibrium computed from the deviation **gains** of players’ "uncovered" strategies. Intuitively, some properties may fail here, as they would be inherently dependent on the notion of correlated equilibrium.

**References**  
[1] Game Theoretic Rating in N-player General-Sum Games with Equilibria

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a new game-theoretic rating method for strategies in N-player, general-sum settings, called "deviation rating", which is clone-invariant. The authors provide an algorithm for computing the rating efficiently with linear programming and conduct experiments to evaluate the proposed rating method on three applications, namely Shapley’s game, LLM rating, and model improvement.

### Strengths
+ The paper proposes a clone-invariant rating method that is applicable to N-player general-sum strategic interactions, with proofs on existence, uniqueness, and other properties.
+ Extensive experiments over a wide range of applications.

### Weaknesses
 - Insufficient implementation details: computational resources, LP solver, actual number of iterations needed (with respect to Algorithm 1), runtimes, etc.
- Presentations: There should be some outline for the paper and transitions between sections. Also, in the abstract, an overview on deviation rating as well as its evaluation (as in Section 5) is missing.
- The related work section is still missing, which is crucial for contextualizing the contributions of this paper among existing literature. Specifically, the paper should compare and contrast the proposed method with existing rating methods, especially those that are also game-theoretic inspired, and discuss how they address the issue of repeated strategies (clone-invariance) in N-player general-sum games.

### Questions
Please include the missing implementation details and polish the paper presentations, and if possible, please add a dedicated Related Work section (where existing rating methods as listed in Section 3.2 and other relevant lines of work are more thoroughly discussed).

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper focuses on the problem of rating different strategies in a normal-form game. According to the authors, many real-world multi-agent or multi-task evaluation scenarios can be modeled as normal-form games, including, for example, the evaluation of large language models, which motivates the study. Prior work on this topic has either focused on two-player zero-sum games or has not been clone-invariant. The authors claim that clone invariance, i.e., copying strategies does not change the ratings, is an important desideratum for the rating scheme. The authors then propose a new rating scheme that is clone-invariant and satisfies a set of other desirable properties. The proposed rating scheme is evaluated in several environments, including rating strategies in simple tabular games, evaluating large language models, and evaluating strategies in well-known benchmark games. The authors claim that the evaluation results show the merits of the proposed rating scheme.

### Strengths
1. The preliminary and related work sections are well-written and provide a good overview of the existing work.
2. In the theoretical sections, the results are clearly stated and sound.
3. The environments used for evaluation are diverse and cover a wide range of scenarios.

### Weaknesses
I have two major concerns about this paper that prevent me from recommending it for acceptance:

1.  **Evaluation.** Other than the stated desiderata, it is not clear to me why the proposed rating scheme is better than existing ones. The results in the evaluation section (Figures 2 and 3) do not seem to demonstrate that the proposed rating scheme is better than existing ones. For example, in Figure 2(a), the proposed rating scheme and the benchmarks perform similarly to me, and there are no quantitative measures of their performance to compare them. From my perspective, the motivation for clone invariance is not so strong that it can be used as the main criterion for evaluating the rating scheme.
2.  **Interpretation of the results.** In the introduction, the authors frame the results in a way that suggests that the results are relevant to many real-world multi-agent or multi-task evaluation scenarios. However, since the evaluation fails to convince me that the proposed rating scheme is even better than existing ones, the relevance of the results to real-world scenarios is further weakened. For example, even if one can interpret the results in Figure 3(a) as showing that the proposed rating scheme is better than the benchmarks in reducing the equilibrium gap, there are much better ways to do this, such as using no-regret learning algorithms.

**Post rebuttal:** The authors clarified the motivation for clone invariance in the rebuttal in a compelling way. Moreover, the authors emphasized a potential use case, and accounted for the lack of quantitative evaluation. I have increased my rating, but lowered my confidence for this paper. Given the current form, I believe this paper needs significant reframing for readers to understand its motivation and value. I will be okay with this paper being accepted if the authors would revise the paper according to the detailed discussion we had.

### Questions
1. How can the authors demonstrate that the proposed rating scheme is better than existing ones?
2. Why is the proposed rating scheme relevant to real-world scenarios? Can you provide more concrete examples?

### Minor comments

1. Line 56: "Yoa’s Principle" -> "Yao’s Principle".
2. Line 111: "Rankings can be inferred from ratings, and are therefore more general" - Did you mean the other way around?
3. Line 132: "$\tilde{G}(a_p, a_{-p})$" - Should be "$\tilde{G_p}(a_p, a_{-p})$"?

### Soundness
4

### Presentation
2

### Contribution
1
