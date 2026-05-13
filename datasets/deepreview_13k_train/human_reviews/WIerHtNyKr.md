# Adaptive Algorithm for Non-Stationary Online Convex-Concave Optimization

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
This paper addresses the problem of Online Convex-Concave Optimization, an extension of Online Convex Optimization to two-player time-varying convex-concave games. 
Our objective is to minimize the dynamic duality gap (D-DGap), a key performance metric that evaluates the players' strategies against arbitrary comparator sequences. 
Existing algorithms struggle to achieve optimal performance, particularly in stationary or predictable environments. 
We propose a novel, modular algorithm comprising three key components: an Adaptive Module that adjusts to varying levels of non-stationarity, a Multi-Predictor Aggregator that selects the optimal predictor from multiple candidates, and an Integration Module that seamlessly combines the strengths of both. 
Our algorithm guarantees a minimax optimal D-DGap upper bound, up to a logarithmic factor, while also achieving a prediction error-based D-DGap bound. 
Empirical results further demonstrate the effectiveness and adaptability of the proposed method.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Briefly, this paper studies the problem of Online Convex-Concave Optimization (OCCO) and contributes improved dynamic duality gap (D-DGap) performance bound, which is the counterpart of dynamic regret in the original Online Convex Optimization (OCO) problem. Their setting considers stationary, non-stationary and predictable environments. Their approach includes an Adaptive Module for non-stationarity, a Multi-Predictor Aggregator for predictability, and an Integration Module for combination.

### Strengths
**Originality:**
- The work is somewhat a novel combination of well-known techniques such as predictive updates, expert combination and dynamic learning.

**Quality:**
- The submission is generally technically sound.
- The claims are supported by theoretical analysis.
- The methods used are appropriate.
- This is a complete piece of work, with potential for further improvements. 

**Clarity:**
- The submission is generally clearly written.
- It is mostly well organized.

**Significance:**
- The others (researchers or practitioners) likely to use the ideas or build on them, since it has improved guarantees.
- It provides new conclusions through a somewhat unique theoretical approach of joint optimization.

### Weaknesses
**Originality:** 
- The tasks and methods are not new, and the exact novelties are unclear. Specifically, while the paper proposes a joint optimization framework, it's not evident how this fundamentally differs from existing approaches that combine adaptive learning with prediction mechanisms. The core components, such as the Adaptive Module and Multi-Predictor Aggregator, appear to be based on established techniques without significant modifications. The claimed novelty of the joint update mechanism in (3) needs more thorough justification and comparison against alternative methods for combining adaptive and predictive elements in online optimization.
- It is not clear how this work differs from previous contributions as the challenges in achieving the results are mostly missing. The paper does not adequately discuss the specific technical hurdles encountered in integrating the Adaptive Module and Multi-Predictor Aggregator, especially in the context of the OCCO problem. A more detailed analysis of the theoretical and practical difficulties in achieving the claimed D-DGap bounds would strengthen the paper's contribution.
- The related work may not be adequately cited as the experiments lack substantial comparisons. The paper primarily focuses on its own proposed method without a comprehensive comparison against a wide range of existing OCCO algorithms. This makes it difficult to assess the relative performance and advantages of the proposed approach.

**Quality:**
- The authors should be more careful about evaluating the strengths and weaknesses of their work, especially in the experiments. The experimental section lacks a detailed analysis of the limitations of the proposed method. For instance, the paper does not discuss the computational complexity of the joint optimization framework or its sensitivity to hyperparameter settings. A more critical evaluation, including potential drawbacks and failure cases, would provide a more balanced assessment.

**Clarity:** 
- It does not adequately inform the reader to reproduce the experimental results. The paper lacks sufficient detail regarding the experimental setup, including specific parameter values, dataset characteristics, and implementation details of the compared algorithms. Providing this information is crucial for ensuring reproducibility and allowing others to validate the findings.

**Significance:** 
*(Key Weakness)*
- The submission does not seem to address a difficult task in a better way than previous work. The hardness of the task and improvement over the literature could be much better explained. While the paper claims improved D-DGap bounds, it does not sufficiently demonstrate the practical significance of these improvements. A more thorough discussion of the limitations of existing methods and how the proposed approach overcomes them is needed.
- The results seem to be lackluster in importance, as the difference from the existing literature seems incremental. The paper does not provide a compelling argument for the practical impact of the claimed theoretical improvements. For instance, it's unclear whether the improved D-DGap bounds translate to significant performance gains in real-world applications.
- It fails to demonstrate how it advances the state of the art in the experimental analysis. The experimental evaluation does not convincingly demonstrate the superiority of the proposed method over existing approaches. The lack of comprehensive comparisons and the limited analysis of the results make it difficult to assess the practical significance of the claimed contributions.

### Questions
**Questions:**
- Is your main novelty the joint optimization in (3)?
- Line 59: what exactly do you mean by non-stationarity?
- Line 67: what do you mean by approximating? This and the following parts need clearer wording.
- Line 86: shape?
- Line 288: where did $O(T)$ term disappear, and also where did the coefficient $16$ come from?

**Major Suggestions:**
- Line 199: the value of $C_T$ in Proposition 2 is ambiguous, given the nature of $x_t$, $y_t$ in minimax analysis. The subsequent intuition is also consequently lacking. Please correct these.
- Line 505: in Figure 2, the difference with the existing literature seems negligible besides Case II, where your algorithm has advantages after utilizing appropriate predictors. Please explain the shortcomings of the existing literature.

**Minor Suggestion:**
- Line 98: if $C_T$ is a bound on $P_T$, why is it incorporated in this bound?
- Line 311: Clarify what the $\mathcal{F}_t$ function represents.

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
3

### Summary
The paper considers a "dynamic duality gap" objective for online convex-concave optimization (carrying the OCO dynamic regret definition over to the OCCO setting in a natural way). It derives an algorithm which both achieves the near-minimax dynamic regret bound for this problem, and achieves near-constant regret when the setting is stationary. More generally, the algorithm is capable of taking in multiple predictions of the objective function and achieving performance close to the best one (while maintaining its minimax dynamic regret bound). The efficacy of the algorithm is verified on several synthetic experiments, and is compared --- with favorable results --- against the performance existing time-varying game-solving method of Zhang, Zhao, Luo, and Zhou (NeurIPS 2022).

### Strengths
Overall, I believe that this is a good contribution to the literature on solving convex-concave time-changing games/saddle point problems. 

I tend to agree with the authors' stated assessment that given the previous state-of-the-art time-varying game solving method of Zhang, Zhao, Luo, and Zhou, it is a-priori not trivial to e.g. incorporate the recent advances in optimistic adaptive/dynamic algorithms to improve Zhang et al's method's performance in stationary/not fully adversarial environments while obtaining the minimax dynamic regret guarantees. This paper addresses this challenge by developing a natural algorithmic scheme with good dynamic regret performance and the ability to obtain optimal performance in stationary settings.

In terms of the overall assessment on the technical side, in my opinion the main technical contribution of the paper can be found in its "integration module", which specifies how to reduce the aggregation of the dynamic regret predictions and other available predictions to a fixed point problem. The "adaptive module" and "the multi-predictor aggregator" are useful but relatively generic components, and the main insight in relation to these two modules is that porting them from the OCO setting into the OCCO setting ends up giving meaningful adaptive/dynamic guarantees in this setting as well. Overall, to sum up the strong sides of this paper: 

+ By appropriately formulating the dynamic duality gap definition, the paper demonstrates how to appropriately port OCO dynamic regret/meta-aggregation insights into the more involved OCCO setting, without losing the tight minimax rate of dynamic regret algorithms like ADER from the OCO setting. 

+ The authors put in the effort to state the framework in a modular way: they separate out the parts where an OCO dynamic regret algorithm like ADER, an expert-aggregation algorithm, and a fixed-point algorithm are applied. This may help with future refinements of, and practical improvements to, the analysis.

### Weaknesses
The paper appears to provide sound statements and proofs, and is overall solidly written. That being said, I am a bit tentative/unconvinced regarding the following several points, which I would appreciate if the authors could clarify:

- In regards to the regret bound terms that involve \rho (i.e., the terms that promise performance not worse than that of the predictors h), the way \rho is currently defined is as the max-norm deviation between h and f over all arguments (x, y). While this is of course already a nontrivial guarantee, but it seems a bit crude, and I believe the result would be strengthened, and made more OCCO-compatible, if a saddle-point specific metric of distance between f and h were considered (e.g., something along the lines of dist(h, f) = max{max_x |h(x, y*(x)) - f(x, y*(x))|, max_y |h(x*(y), y) - f(x*(y), y)|}, where x*(y) is the best-response of the first player to y and where y*(x) is the second player's best-response to x). A quick glance at eq (10) in the appendix suggests that this would not be an easy change to make in the analysis (and in fact even tightly replacing the metric \rho by an L1 or L2 style metric looks like it wouldn't be trivial either?).

- In terms of the modular framework itself, I am still not fully convinced about the arguments that were presented in-text about why the meta-aggregation mechanism (i.e. the "integration module") had to be designed in this bespoke way where the meta-layer variables v, w have to interact (in the interdependent update equations (3a) and (3d)) with the predictor(s) h that are being aggregated, and --- moreover --- these predictors h themselves have to interact with the adaptive module predictions \bar{x} and \bar{y}. Why is it impossible to break both of these interdependencies to make things completely modular --- e.g., along the lines of turning equation (3a) into the following form free of both the w, omega, and of the \bar{x}_t, \bar{y}_t variables: (\hat{x}_t, \hat{y}_t) = arg min_x max_y h_t(x, y)  + <regularization terms with B_\phi and B_\psi>?

- The experimental section overall was designed reasonably well, but a few aspects merit addressing/clarifying. (a) It says: "our algorithm consistently outperforms Zhang et al", which appears to be an overstatement: In cases I and III, the performance of both methods on the D-DGap plot is very similar, and only in case II do we see a significant difference (for all three levels of nonstationarity). Given the stronger guarantees of the new algorithm, I don't doubt that it can outperform Zhang et al's in many settings, but to make that point well-substantiated, more experiments need to be shown. (b) Also, for the sake of transparency, I am wondering how much more compute time does the new algorithm use compared to Zhang et al's? (I do not consider it strictly necessary to report this in the paper, though if the runtime is somehow comparable (which I don't a-priori expect due to the bulky procedure in each round) then mentioning this in the manuscript would of course be favorable to the current paper.) (c) Is there any meaning behind the 1/ ln(t+1) scaling in the level-ii comparator?

### Questions
Please see the several questions integrated in the weaknesses section above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper addresses the problem of online convex concave optimization, where the objective is to minimize the dynamic duality gap. They propose a modular algorithm comprising of three components and guarantee a minimax optimal duality gap upper bound up to a logarithmic factor. They also provide some empirical results to further demonstrate
the performance of the proposed method.

### Strengths
S1 - The paper is generally well written and well presented.

S2 - The technical claims in the paper are generally well explained.

S3 - Experiments are a plus.

### Weaknesses
W1 - Comparisons to the existing literature are not enough. While the related works are comprehensive, their relation and comparison to your work is lacking.

W2 - The role of each module in the algorithm seems ambiguous at times.

W3 - The problem definition is poorly explained especially for a newly proposed performance metric.

### Questions
Q1 - Eq 1 is weird in that it is an equality but for every u_t and v_t, is it a function of them?

Q2 - While i understand that the duelity gap is an important metric, its role as a performance metric seems dubious.

Q3 - Where in the algorithm does your main novelty reside? It mainly seems like an amalgamation of existing techniques.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers the problem of online convex-concave optimization, which can be seen as an adaption of online convex optimization (OCO) in the two-player game setup. For this problem, the authors first show that when both players run an Ader or Ader-like algorithm, the proposed dynamic duality gap can be bounded as the dynamic regret (which is a two-player version in the game setup). Consequently, the authors consider further enhancing the results with prediction-error-based guarantees, which are usually called optimistic online learning in the OCO setup. Finally, the authors investigate the case where only one prediction sequence (optimism sequence) could perform poorly and consider combining multiple optimism with learnable weights to obtain a more robust prediction sequence. By doing this, they can further enhance the results to the minimum of the prediction error of all possible optimism and the dynamic regret. Finally, empirical studies validate the effectiveness of the proposed method.

### Strengths
This paper considers a meaningful problem of achieving dynamic regret and optimistic bounds in the setup of two-player convex-concave games. The presentation is clear and easy to follow. Although I did not check the detailed proof, I believe that the proofs are correct thanks to the clear presentations by the authors.

### Weaknesses
My concern mainly lies in the technical contributions. Since I am kind of familiar with dynamic regret minimization and optimistic online learning, I found the technical contributions of this work somewhat limited.

1. The results in the adaptive module can be easily attained by using Ader for both players and the dynamic duality gap, in this case, can be decomposed into the summation of the dynamic regret of each player. The authors also acknowledge this.

2. For the integration module, although the equations on page 5 look complicated, they are mostly actually a two-player extension of the optimistic online mirror descent. For example, (3a) and (3d) are actually the optimistic step that uses the optimism ($H_t$ and $W_t$, $W_t$ is actually an optimism since it consists of the prediction $h_t$). And (3b), (3c) are the update step that uses the true loss information $f_t(\cdot)$. This is very similar to the one-player optimistic online mirror descent [1]. And Theorem 3, 4, 5 are not surprising to me since Theorem 3 is actually the optimistic bound, Theorem 4 is the regret bound attained by using Hedge (or clipped Hedge) as the meta-algorithm, and Theorem 5 combines the two theorems as mentioned earlier together.

3. The third multi-predictor aggregator is also not very surprising to me because it actually uses the technique of learning over multiple optimism. For example, the technique appears in the Section 4 "Learning The Predictable Processes" in [1]. As a result, this parts seems to be a direct extension from my point of view.

I have one question about the upper and lower bounds in the adaptive module. In my opinion, the dynamic regret measured by $P_T$ is meaningful since the variation of the $u_t$ and $v_t$ sequences reflect the difficulties of the learning problem. However, the quantity $C_T$ is less meaningful for me because $x_t^\prime$ actually depends on $y_t$ (also for $y_t^\prime$), showing that $C_T$ is in fact *algorithm-dependent*. As a result, one cannot justify how good the bound measured by $C_T$ is since $C_T$ relies on the algorithm. 

Also, I agree that the lower bound for $P_T$ is correct, as explained by the authors after Proposition 2 and the lower bound indicated in the one-player setup. However, I am confused about the lower bound for $C_T$. As I said before, $C_T$ is algorithm-dependent. However, a lower bound should hold for all possible algorithms. Why could an algorithm-dependent quantity appear in a lower bound? Or maybe this lower bound only holds for this specific algorithm? In the latter case, the authors should revise the statement of Proposition 2 to state clearly that this lower bound only holds for Ader-like algorithms but not for all possible algorithms. I am looking forward to the authors' reply on this issue.

### Questions
I have one question about the upper and lower bounds in the adaptive module. In my opinion, the dynamic regret measured by $P_T$ is meaningful since the variation of the $u_t$ and $v_t$ sequences reflect the difficulties of the learning problem. However, the quantity $C_T$ is less meaningful for me because $x_t^\prime$ actually depends on $y_t$ (also for $y_t^\prime$), showing that $C_T$ is in fact *algorithm-dependent*. As a result, one cannot justify how good the bound measured by $C_T$ is since $C_T$ relies on the algorithm. 

Also, I agree that the lower bound for $P_T$ is correct, as explained by the authors after Proposition 2 and the lower bound indicated in the one-player setup. However, I am confused about the lower bound for $C_T$. As I said before, $C_T$ is algorithm-dependent. However, a lower bound should hold for all possible algorithms. Why could an algorithm-dependent quantity appear in a lower bound? Or maybe this lower bound only holds for this specific algorithm? In the latter case, the authors should revise the statement of Proposition 2 to state clearly that this lower bound only holds for Ader-like algorithms but not for all possible algorithms. I am looking forward to the authors' reply on this issue.

### Soundness
2

### Presentation
3

### Contribution
2
