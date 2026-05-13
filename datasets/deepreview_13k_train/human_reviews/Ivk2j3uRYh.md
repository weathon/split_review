# Random Graph Asymptotics for Treatment Effect Estimation in Two-Sided Markets

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
In two-sided markets, the accurate estimation of treatment effects is crucial yet challenging due to the inherent interference between market participants, which violates the Stable Unit Treatment Value Assumption (SUTVA). This paper introduces a novel framework that leverages random graph asymptotics to model and estimate treatment effects under network interference in two-sided markets. By incorporating a random graph model, we handle two-sided randomization by modeling customer interference within the potential outcome function as a function of graph topology and equilibrium dynamics, while capturing listing interference through the random graph structure. Our new estimation process provides asymptotically normal estimators with robust theoretical properties, suitable for large-scale market scenarios. Our theoretical findings are supported by extensive numerical simulations, demonstrating the effectiveness and practical applicability of our approach in estimating direct and indirect causal effects within these complex market structures.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper tackles the challenging problem of estimating treatment effects in two-sided markets, a context where interference between market participants poses significant obstacles to causal inference. In which would violate the Stable Unit Treatment Value Assumption. The paper proposes a method that leverages random graph asymptotics to address these challenges.

### Strengths
1. The accurate estimation of treatment effects is essential but challenging due to network interference. 
2. The proposed method offers a novel solution by utilizing random graph asymptotics.
3. The numerical simulations demonstrate the practical applicability and effectiveness of the method.

### Weaknesses
1. The paper could benefit from a more detailed comparison with existing methods to highlight the advantages and limitations of the proposed method.
2. It would be better to add comparative experiments with existing methods in the experimental section.

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies treatment effect estimation in two-sided markets, specifically the listing markets. The market dynamics is the following. A customer arrives, forms consideration set using currently available listings ($a_\gamma(\theta)$), and choose one listing or not choosing at all based on the utility $v_\gamma(\theta)$. By assuming a Poisson process on costumers, the listing status is a continuous time markov chain. The equilibrium is used to define the potential outcome of listings. Also an interference structure based on graphs is imposed on the potential outcome in addition to the equilibrium structure. Asymptotically normal estimators for direct and indirect effects are proposed.

### Strengths
1. The listing dynamics is practical for many online platforms. The paper studies treatment effect estimation under the equilibrium effect of the platform, which is relevant for practical purposes.

### Weaknesses
1. It may be helpful to outline technical difficulties when extending Li and Wager's results to highlight the paper's theoretical contributions.

2. Unless I'm missing something, constant graphon function in Eq (1) is restrictive compared to the previous Li and Wager's results. If the paper is assuming constant graphon,

3. It is unclear how the proposed method compares to simpler model-based approaches, especially given the rich dynamics assumed. The estimators for direct and indirect effects seem directly borrowed from Li and Wager, and do not explicitly utilize the assumed market dynamics.

4. Line 380: "regularization assumptions" or "regularity assumption"?

5. Line 066: inconsistent citation format.

6. Line 167: may be better to repeat definition of Y_i here; it is definition is hidden in a long paragraph.

7. Line 225: i and j were used to index listings and buyers previously.

8. In Eq(2), is the form of potential outcome outcome function the assumption? Because after eq (2) it says "derivation", which is confusing. Also the meaning of the potential outcome function should be explained too. I believe it represents the steady-state utility the listings are generating. Also Eq (2) should be defined right after Section 2 to make it clear that the equilibrium described in Sec 2 is used to define potential outcomes.

9. In Eq (1), the RHS is the same for all theta_i, theta_j. Is it a typo? The original Li and Wager paper allows for general G if i'm not missing something. A constant graphon function restricts the class of treatment interference being modeled.

### Questions
Line 380: "regularization assumptions" or "regularity assumption"? 

Line 066: inconsistent citation format.

Line 167: may be better to repeat definition of Y_i here; it is definition is hidden in a long paragraph.

Line 225: i and j were used to index listings and buyers previously.

In Eq(2), is the form of potential outcome outcome function the assumption? Because after eq (2) it says "derivation", which is confusing. Also the meaning of the potential outcome function should be explained too. I believe it represents the steady-state utility the listings are generating. Also Eq (2) should be defined right after Section 2 to make it clear that the equilibrium described in Sec 2 is used to define potential outcomes. 

main questions

1. In Eq (1), the RHS is the same for all theta_i, theta_j. Is it a typo? The original Li and Wager paper allows for general G if i'm not missing something. A constant graphon function restricts the class of treatment interference being modeled.

2. Are there technical difficulties when extending results of Li and Wager to the listing dynamics?

3. What are the data we observe to estimate treatment effects? Just the outcomes $Y$? If we additionally observe consumer types and values $v$ and consideration probability $\alpha$, how would a model-based approach behave compared to the proposed method? It could be that I'm missing something, to me both estimators for direct and indirect effects are directly borrowed from Li and Wager, and do not use the rich dynamics assumed. 
 
I would be happy to update score if the authors could sufficiently address these questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The manuscript has a rigorous mathematical framework for interference, and clear asymptotic properties. I liked the novel use of graphon models. Authors offer estimations for both direct and indirect effects with cariance adjustments for interference. The proposed methods is computationally tractable.

Aside from the rigor and nice theoretical set up, and for the scope of ICLR, I found the method challenging to use in real applications. The experimental setup require two-sided randomization and clean treatment assignment with complete tracking of interactions. This seems like a tall call, as in reality, we have multiple concurrent changes with partial observability. Also authors did not focus on a real wold domain, but the assumptions of poisson arrivals, multinomial logit choice, and xponential occupancy times often violated and replaced by seasonal/time-varying patterns, variable occupancy durations, and heterogeneous listing attributes. 

For such setting, I suggest discussing adaptations to observational setting with possible extensions:

- Incorporate propensity score methods

- Add covariate adjustment

- Model selection bias

Implementation:

- Match similar time periods

- Control for external factors

- Use proxy variables for unobserved confounders

Other than observational case, I also suggest discussing A/B Testing Framework, with some modification in design:

1. Simplified Treatment:

   - Single-sided treatment first

   - Gradual rollout

   - Clear control groups

2. Measurement:

   - Track spillover effects

   - Monitor market equilibrium

3. Analysis:

   - Compare with benchmark A/B estimates, and possibly with available real-world data

   - I also, like to see validation on the interference patterns (maybe in single market segment with limited time period?, what can be good diagnostic tests for interference?)

### Strengths
see summary

### Weaknesses
The manuscript has a rigorous mathematical framework for interference, and clear asymptotic properties. I liked the novel use of graphon models. Authors offer estimations for both direct and indirect effects with cariance adjustments for interference. The proposed methods is computationally tractable.

Aside from the rigor and nice theoretical set up, and for the scope of ICLR, I found the method challenging to use in real applications. The experimental setup require two-sided randomization and clean treatment assignment with complete tracking of interactions. This seems like a tall call, as in reality, we have multiple concurrent changes with partial observability. Also authors did not focus on a real wold domain, but the assumptions of poisson arrivals, multinomial logit choice, and xponential occupancy times often violated and replaced by seasonal/time-varying patterns, variable occupancy durations, and heterogeneous listing attributes. 

For such setting, I suggest discussing adaptations to observational setting with possible extensions:

- Incorporate propensity score methods

- Add covariate adjustment

- Model selection bias

Implementation:

- Match similar time periods

- Control for external factors

- Use proxy variables for unobserved confounders

Other than observational case, I also suggest discussing A/B Testing Framework, with some modification in design:

1. Simplified Treatment:

   - Single-sided treatment first

   - Gradual rollout

   - Clear control groups

2. Measurement:

   - Track spillover effects

   - Monitor market equilibrium

3. Analysis:

   - Compare with benchmark A/B estimates, and possibly with available real-world data

   - I also, like to see validation on the interference patterns (maybe in single market segment with limited time period?, what can be good diagnostic tests for interference?)

### Questions
see summary

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates a critical issue in two-sided markets that does not satisfy the Stable Unit Treatment Value Assumption (SUTVA). It introduces a novel framework that utilizes random graph asymptotics to model and estimate treatment effects under network interference in these markets.

### Strengths
- This paper addresses a significant issue with practical applications and academic value. 

- The introduced method is theoretically sound and supported by empirical validation, providing valuable guidance for future research on random graph asymptotics in two-sided markets.

### Weaknesses
 - My primary concern is the paper's limited contribution to the causal reasoning community. It appears to apply the methods and theories from [1] to the specific context of two-sided markets without offering unique technical advancements.

- Additionally, while the paper acknowledges its foundation in [1], it contains significant similarities in text, formulas, and figures, raising concerns about potential plagiarism.

- The main distinction from [1] lies in its application to two-sided markets. However, the lack of validation with real-world data, relying solely on simulations, further diminishes its contribution.

- If the authors can articulate the key differences between their work and that of [1], along with the significant challenges these differences present, and demonstrate how their method addresses these challenges with real-world validation in two-sided markets, I would reconsider my score.

### Questions
as above.

### Soundness
3

### Presentation
1

### Contribution
1
