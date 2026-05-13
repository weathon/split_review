# Pricing with Contextual Elasticity and Heteroscedastic Valuation

- Decision: Reject
- Scores: 3, 6, 6, 6

## Abstract
We study an online contextual dynamic pricing problem, where customers decide whether to purchase a product based on its features and price. 
We introduce a novel approach to modeling a customer's expected demand by incorporating feature-based price elasticity, which can be equivalently represented as a valuation with heteroscedastic noise.
To solve the problem, we propose a computationally efficient algorithm called "Pricing with Perturbation (PwP)", which enjoys an $O(\sqrt{dT\log T})$ regret while allowing arbitrary adversarial input context sequences. We also prove a matching lower bound at $\Omega(\sqrt{dT})$ to show the optimality regarding $d$ and $T$ (up to $\log T$ factors).
Our results shed light on the relationship between contextual elasticity and heteroscedastic valuation, providing insights for effective and practical pricing strategies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors face the problem of contextual dynamic pricing in a heteroscedastic environment. The authors face this applicative problem by proposing a new theoretical framework. They provide a lower bound on the expected regret for the setting. Then, the authors provide an algorithm, for which they discuss the upper bound, which matches the lower bound up to log factors. The authors also provide a numerical validation of the solution.

### Strengths
The work faces a problem of interest from the applicative point of view. 

The relevant literature is properly discussed.

### Weaknesses
The presentation can be improved, in particular from the introductory part.

The main concern is about the theoretical analysis of this paper. Indeed, an important focus of this work is related to heteroscedasticity, which is its differential part w.r.t. existing literature. However, this phenomenon is not highlighted in the analysis. For example, in Thr 4.5, the authors retrieve a bound in which such a phenomenon is not highlighted, and the result presented is already present in the literature. Furthermore, the result presented is known for a setting that is simpler than the one presented in this paper, so it holds in this scenario.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper unifies the ``linear demand'' and the ``linear valuation'' by proposing a new demand model where each item has a feature-dependent price elasticity. The authors devise an effective online optimization algorithm that can achieve a nearly optimal regret bound. Some numerical simulations are conducted to empirically show the effectiveness of the proposed approach.

### Strengths
S1. A new demand model for the contextual pricing problem.

S2. The proposed algorithm has a regret bound close to the theoretical lower bound.

S3. Numerical simulations are conducted.

### Weaknesses
W1. Although the proposed demand model extends existing models by considering the feature-dependent price elasticity, the proposed model and online algorithm still rely on linear forms of elasticity and valuation. Remember ICLR is a deep learning conference. A potentially more suitable treatment may be substituting the linear functions with a neural tangent kernel and then devising online algorithms correspondingly. Specifically, the paper could explore how the feature space impacts the effective dimensionality when using a kernel method, and whether the regret bounds can be improved by leveraging the properties of the kernel. The current linear model seems restrictive given the conference focus.

W2. What is the major technical challenge if we replace the uniform \alpha with a feature-dependent price elasticity? The authors may want to discuss more the impact of introducing feature-dependent price elasticity terms on algorithm design as well as regret analysis. It's not clear from the current presentation why this extension is non-trivial. For instance, how does the adversarial nature of the context sequence interact with the feature-dependent elasticity, and what specific challenges does this pose for exploration-exploitation strategies? A more detailed explanation of the technical hurdles would be beneficial.

W3. As the authors mention in Ethic issues, personalized pricing may have fairness issues. Therefore, it is essential to discuss how to deal with the cases when we add some fairness regularization terms or fairness constraints to the optimization problem. The paper should consider how different notions of fairness, such as group fairness or individual fairness, could be incorporated into the optimization framework, and how these constraints would affect the regret bounds and the overall performance of the algorithm. This is crucial for real-world applicability.

W4. Still about personalized pricing. As the objective is purely the interest of the platform, I would like to see discussions or experimental results on how the personalized pricing algorithm affects customer well-being metrics such as consumer surplus. The paper should include a discussion on the trade-offs between platform profit and consumer welfare, and possibly explore alternative objective functions that balance these competing interests. This would provide a more comprehensive view of the impact of the proposed approach.

### Questions
W2

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates a context-based dynamic pricing problem, where customers decide whether to purchase a product based on its features and price. The authors adopt a novel approach to formulating customers’ expected demand by incorporating feature-based price elasticity. The paper provides a matched regret bound for the problem.

### Strengths
Generally speaking, from my point of view, the paper is well written. I really enjoy reading the discussions the authors make, including the relationship between two different formulations and Section 4.1.1. The technical part is solid. The idea of perturbation, though not completely novel, is quite interesting.

### Weaknesses
1. In my opinion, the work by Ban and Keskin [1] warrants a more thorough discussion and acknowledgment. Their research appears to be the first to explore heterogeneous price elasticities in a linear context formulation. I believe that a more in-depth discussion of [1] is necessary, particularly when introducing the formulation. Specifically, the authors should elaborate on the similarities and differences between their approach and that of [1], highlighting the novel aspects of their model while acknowledging the foundational contributions of [1].

2. While I understand that assuming a known link function is a common practice and a reasonable starting point, I believe that exploring an unknown link function could significantly enhance the paper's impact. The authors could either incorporate this into their analysis or provide a detailed discussion of the challenges and potential benefits of considering such a scenario. The rationale for this suggestion stems from the work of Fan et al. [2], which investigates a problem with an unknown noise distribution. Given the equivalence of the two formulations, it seems plausible to consider a version without a known link function. A thorough discussion of this aspect, even if not directly addressed in the current work, would demonstrate a deeper understanding of the problem space and its complexities.

3. Regarding the Perturbation technique, similar concepts have been explored in the dynamic pricing literature, such as in the work by Nambiar et al. [3]. It appears that the primary reason for requiring a known time horizon $T$ is to calculate $\Delta$. Nambiar et al. [3] propose dynamically adjusting the perturbation's magnitude, which could potentially allow the current algorithm to operate without prior knowledge of $T$. A more detailed comparison with this approach, clarifying whether the current method can be adapted to eliminate the need for a known $T$, would be beneficial. If my understanding is incorrect, a clear explanation of the distinctions and limitations would be helpful.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studies an online dynamic pricing problem by considering a novel model with feature-based price elasticity.  The authors provide a novel algorithm, ``Pricing with Perturbation (PwP)," that efficiently solves this pricing problem and obtains near-optimal regret, which matches the lower bound of regret up to log terms.

### Strengths
1. The presentation is clear. Beginning with the introduction part, the paper clearly lists its comparisons and generalizations from previous work. Later in the main text, the intuition of the algorithm is also well described. The assumptions made in the paper are also clearly listed and justified.

2. The novelty of the algorithm and its technical contributions are sound. The proposed Pricing with Perturbation (PwP) algorithm is smart and can efficiently solve the problem of a lack of fisher information.

3. Discussions on potential extensions of the work are discussed in detail in the appendix.

### Weaknesses
1. The motivation for this contextual price elasticity seems unclear.

2. Certain assumptions, such as $x^\top \eta$ having a positive lower bound, lack a real-world explanation. Specifically, while a positive elasticity is generally expected, the assumption that it is *always* bounded away from zero by a constant $C_\beta$ for all contexts $x_t$ is quite strong and requires more justification. It's not clear why the price elasticity could not approach zero for some contexts, which would still be consistent with the law of demand.

3. Lack of applying this framework to real-data studies

### Questions
1. Can the authors present certain real-world motivations for this contextual price elasticity? e.g., why is it reasonable to rely on the context $x_t$, and is it reasonable to assume that for all $x_t$, $x_t^\top \eta$ is positive all the time? 

2. About the linear assumption on $x_t^\top \eta$, can this be generalized to some non-linear function of $x_t$? Also, when $x_t$ is stochastic, can the assumption of $x_t^\top \eta>0$ be relaxed to $E[x_t^\top \eta]>0$, where $E[\cdot]$ is the expectation over $x$?

3. Can the authors provide a real-world (or semi-real) data study? on evaluating the performance of algorithms in real-life situations.

4. In terms of the presentation of simulation results, could the authors present log-log plots and compare them with the $1/2 log T$ curve? Since it would be hard to see the regret order if they are not presented in this way,

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
