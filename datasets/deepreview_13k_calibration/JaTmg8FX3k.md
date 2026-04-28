# Provably Efficient Multi-Objective Bandit Algorithms under Preference-Centric Customization

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Existing multi-objective multi-armed bandit (MO-MAB) approaches mainly focus on achieving Pareto optimality. However, a Pareto optimal arm that receives a high score from one user may lead to a low score from another, since in real-world scenarios, users often have diverse preferences across different objectives. Instead, these preferences should inform *customized learning*, a factor usually neglected in prior research. To address this need, we study a *preference-aware* MO-MAB framework in the presence of explicit user preferences, where each user’s overall-reward is modeled as the inner product of user preference and arm reward. This new framework shifts the focus from merely achieving Pareto optimality to further optimizing within the Pareto front under preference-centric customization. To the best of our knowledge, this is the first theoretical exploration of customized MO-MAB optimization based on explicit user preferences. This framework introduces new and unique challenges for algorithm design for customized optimization. To
address these challenges, we incorporate *preference estimation* and *preference-aware optimization* as key mechanisms for preference adaptation, and develop new analytical techniques to rigorously account for the impact of preference estimation errors on overall performance. Under this framework, we consider three preference structures inspired by practical applications, with tailored algorithms that are proven to achieve near-optimal regret, and show good numerical performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces multi-objective multi-armed bandit (MO-MAB) problems with user-specific preferences. Unlike traditional approaches focusing solely on achieving Pareto optimality, this Preference-Aware MO-MAB  framework emphasizes optimizing within the Pareto front based on individual user preferences. Three different user preference structures are explored: known, unknown, and hidden preferences. Tailored algorithms are proposed for each scenario, achieving provably efficient sub-linear regret bounds.

### Strengths
* The paper proposes a new Preference-Aware MO-MAB  framework and provides very illustrative examples to help the reader understand it. 

* Multiple different settings for the preference feedback are considered. This paper designed a tailored algorithm for each particular setting and provides comprehensive theoretical analyses. 

* Sublinear regrets are guaranteed under all considered settings.

### Weaknesses
While this paper appears interesting and promising, several concerns need to be raised, including issues related to the presentation, the novelty of the algorithms, and the solidity of the theoretical results. Please refer to **Questions** below.

* The main concern from this reviewer's point of view is the solidity of Theorem 5. When the preference is arbitrarily changed over time, how is it possible to find the best arm $a_t^*$ for each time before you know the preference?  Then the regret definition in Eq. (2) does not make sense for this setting. The regret $R(T) = O(\delta \log(T) + D^{1/3}T^{1/3})$ is highly skeptical as in this case, regret can be linearly increasing as $T$. Similar to the adversarial bandit setting where the rewards of each arm can be arbitrarily changed over time, the goal is never to find the best arm for each time, which is impossible. 

* My second concern is that Algorithms 1-3 differ only in the estimation of the preference feedback, and are quite similar to conventional basic bandit settings.  In terms of algorithm design, there is really no novelty in this paper, although it is acceptable if the methods demonstrate strong performance. The concern is that the reviewer cannot intuitively explain why this more challenging multi-objective optimization with two unknown vectors in this paper can achieve nearly the same regret (e.g., Theorems 2, 3, 4 ) as the basic bandit setting with one scaler optimization, given the fact that the algorithms are largely similar? I do not see any additional technique to address such challenges. Can you clarify this?  

* Could you explain the rationale behind using Eqs. (5), (8), and (9) for estimating preferences? What is the underlying reasoning for adopting this approach to preference estimation?  What is $c_{t-1}$ in Eq. (5)? 

* It is unclear whether Proposition 1 defines the regret as in Eq. (2), where preferences are considered, even though the algorithms in those references are preference-free. 

* Is that fair to compare with preference-free algorithms in terms of the regret considering preference? See lines 277-291 for a reference. 

* Though the main paper contains a substantial amount of theoretical results and no space for numerical results, it is recommended to have some key results in the main paper as well. 

*It is also recommended to include a table or a dedicated section to discuss the differences and similarities among all the algorithms and their respective regret orders. The prefactors are currently vague and difficult to understand.

### Questions
* The main concern from this reviewer's point of view is the solidity of Theorem 5. When the preference is arbitrarily changed over time, how is it possible to find the best arm $a_t^*$ for each time before you know the preference?  Then the regret definition in Eq. (2) does not make sense for this setting. The regret $R(T) = O(\delta \log(T) + D^{1/3}T^{1/3})$ is highly skeptical as in this case, regret can be linearly increasing as $T$. Similar to the adversarial bandit setting where the rewards of each arm can be arbitrarily changed over time, the goal is never to find the best arm for each time, which is impossible. 

* My second concern is that Algorithms 1-3 differ only in the estimation of the preference feedback, and are quite similar to conventional basic bandit settings.  In terms of algorithm design, there is really no novelty in this paper, although it is acceptable if the methods demonstrate strong performance. The concern is that the reviewer cannot intuitively explain why this more challenging multi-objective optimization with two unknown vectors in this paper can achieve nearly the same regret (e.g., Theorems 2, 3, 4 ) as the basic bandit setting with one scaler optimization, given the fact that the algorithms are largely similar? I do not see any additional technique to address such challenges. Can you clarify this?  

* Could you explain the rationale behind using Eqs. (5), (8), and (9) for estimating preferences? What is the underlying reasoning for adopting this approach to preference estimation?  What is $c_{t-1}$ in Eq. (5)? 

* It is unclear whether Proposition 1 defines the regret as in Eq. (2), where preferences are considered, even though the algorithms in those references are preference-free. 

* Is that fair to compare with preference-free algorithms in terms of the regret considering preference? See lines 277-291 for a reference. 

* Though the main paper contains a substantial amount of theoretical results and no space for numerical results, it is recommended to have some key results in the main paper as well. 

*It is also recommended to include a table or a dedicated section to discuss the differences and similarities among all the algorithms and their respective regret orders. The prefactors are currently vague and difficult to understand.

### Soundness
2

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
This paper studies the multi-objective multi-armed bandit (MO-MAB) problem. Different from the existing works that focus on the Pareto optimality, this work studies a preference-aware MO-MAB problem. To tackle this problem, the authors model the overall-reward as the inner product of the arm reward and the user preference. For this model, the authors give a comprehensive study under three preference structures, with corresponding algorithms that achieve provable sublinear regret regret. Finally, the theoretical results are validated by experiments.

### Strengths
1. The authors propose a natural preference-aware MO-MAB problem and conduct a systematic study with several different settings, considering both unknown rewards and/or preferences as well as the corruption and non-stationary settings.
2. The presentation is very clear and easy to follow. Almost all settings are illustrated with intuitive examples to motivate each setting.

### Weaknesses
Although the authors give a comprehensive study over a wide range of settings,  each setting can be easily reformulated or mapped as existing MAB settings, where leveraging existing approaches such as UCB/LinUCB with slight modification yields the result of the current paper. The core is to use the scalarization function to weight each objective and the scalarization function is modeled as a (unknown) preference vector. As such, the current study seems to be a wide combinatorial of separate pieces but lacks theoretical depth, which delivers few interesting and insightful intellectual merits.

### Questions
One interesting question is to study the case where only the overall reward can be observed or the case where the independence assumption does not hold. With discussions on these new settings, this paper can make more interesting and novel contributions to the community.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper extends the MO-MAB setting (Pareto bandits) to the setting where a fixed arm from the pareto front is the best action conditioned on user preferences. These user preferences are at the core of the novelty and the work is the first to introduce this additional structure on top of MO-MAB. The inclusion of user preference is motivated by the fact that different users weigh different metrics of a recommendation differently. For example, some users may care more about price, and others may care more about quality. 

Different progressively more complex scenarios are considered in the work for user preference. First the case where user preferences can be observed directly are considered. Then the case where user preferences are stochastic but stationary and observed after taking an action are considered. Next the case where preferences are non-stationary but punctuated by breakpoints are considered. Finally the case of hidden preference is considered.

On top of the novel structure, the contributions of the work are a UCB-style algorithm for each kind of user-preference setting. They also analyze all the UCB variants and provide an upper bound on regret for each of these settings.

### Strengths
The work is well motivated by the limitations of the pareto bandit framework. They make a good case for their augmentations of the MO-MAB problem and provides several real-world examples to motivate their proposed structure. The presentation of the various variants of this structure is concise, well articulated, and backed by good visual representations. A principled algorithm is presented to solve the problem for each of the cases. Further these UCB-style algorithms are analyzed and order wise logarithmic instance dependent upper bounds on regret have been shown for them.

### Weaknesses
1. Some experiments should be included in the narrative of the main paper along with a discussion that contextualizes the baselines. Please consider adding an experiment comparing prior MAB-approaches listed in the literature (S-UCB, S-MOSS, Pareto-UCB, Pareto-TS) into the main paper. What I would be most interested to see is how and why these approaches that are agnostic to user preferences are configured for comparison. The how is already answered in Appendix A.1.1 however the why should also be addressed from a practitioner's point of view. While tests on synthetic data would also be informative, a test on a real dataset would be especially compelling since this would reveal the practical advantages or practical limitations of the PRUCB approach.
Currently there are no experiments in the main paper and there is no discussion of when and why a practitioner should use the UCB approach of this work as opposed to some other approach for solving their problem. Adding these experiments will address this limitation.

2. The authors might consider the generality of the assumptions in this work a strength but they seem unnecessary for some kinds of applications in the paper. See question 2.

### Questions
1. Please clarify the key differences between your setup in Section 5 and contextual bandits, or discuss the implications if the setup is indeed equivalent to contextual bandits in this case. I also request a more detailed explanation of how the approach differs from or extends contextual bandits in this specific scenario. This is in context to Remark 3.1 as well.

2. Perhaps modelling user preferences as quality constraints might be a better solution from a sample efficiency perspective? I am thinking of the MAB with cost subsidy paper by Sinha et al. (2021) for example which could with less structure address the problem example at the end of page 3 which reads: "For example, a user may prefer a 10 dollar meal with good taste over a 9.5 dollar meal with poor taste, even though cost is a priority." by imposing a "quality constraint" on taste.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the MO-MAB framework, integrating user preferences. It first introduces a formalization of the Preference-Aware MO-MAB and subsequently presents four algorithms tailored to different levels of knowledge regarding user preferences.

### Strengths
1. This paper provides a comprehensive examination of the various forms of preferences.

2. The use of multiple figures throughout the paper enhances clarity and readability.

### Weaknesses
1. This paper proposes a variety of algorithms and theorems; however, it demonstrates minimal innovation, relying largely on straightforward applications of existing methods. Specific observations are provided below.

2. **Algorithm 1** appears redundant. The primary challenge in bandit problems is the parameter estimation under uncertainty; assuming a known preference does not add any complexity when compared to single-objective bandit problem.

3. **Algorithm 2** addresses stationary preferences where the expectation of preference is constant. Given the independence of reward and preference, there does not seem to be any technical difficulty in managing this scenario.

4. **Algorithm 3** is designed for non-stationary preferences. The sliding window approach employed here is a well-established technique for adapting to dynamic environments in bandit settings. Additionally, the "Restart" method from [1] offers a simpler solution for this type of problem.

5. **Algorithm 4** addresses hidden preferences, whose expectation is fixed. This algorithm estimates the hidden preference by using multiple rewards as features and overall-rewards as reward—another mature approach in the field of bandit algorithms.

6. **Proposition 1**: For preference-free algorithms, it is straightforward to construct an example with a regret bound of $O(T)$ due to conflicting objectives. For instance, consider two arms with expected rewards of $[0,1]$ and $[1,0]$; it is evident that, for any bandit algorithm, the regret for at least one objective is $\Omega(T)$. Does your proof offer any technical novelty? If so, please highlight this aspect.

### Questions
Please refer to weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2
