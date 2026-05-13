# Provably Efficient Linear Bandits with Instantaneous Constraints in Non-Convex Feature Spaces

- Decision: Reject
- Scores: 3, 5, 6, 3

## Abstract
In linear stochastic bandits, tasks with instantaneous hard constraints present significant challenges, particularly when the feature space is non-convex or discrete. This is especially relevant in applications such as financial management, recommendation systems, and medical treatment selection, where safety constraints appear in non-convex forms or where decisions must often be made within non-convex and discrete sets. In these systems, bandit methods rely on the ability of feature functions to extract critical features. However, in contrast to the star-convexity assumption commonly discussed in the literature, these feature functions often lead to non-convex and more complex feature spaces. In this paper, we investigate linear bandits and introduce a method that operates effectively in a non-convex feature space while satisfying instantaneous hard constraints at each time step. We demonstrate that our method, with high probability, achieves a regret of $\tilde{\mathcal{O}}\big( d (1+\frac{\tau}{\epsilon \iota}) \sqrt{T}\big)$ and meets the instantaneous hard constraints, where $d$ represents the feature space dimension, $T$ the total number of rounds, and $\tau$ a safety related parameter. The constant parameters $\epsilon$ and $\iota$ are related to our localized assumptions around the origin and the optimal point. In contrast, standard safe linear bandit algorithms that rely on the star-convexity assumption often result in linear regret. Furthermore, our approach handles discrete action spaces while maintaining a comparable regret bound. Moreover, we establish an information-theoretic lower bound on the regret of $\Omega \left( \max\{ d \sqrt{T}, \frac{1}{\epsilon \iota^2} \} \right)$ for $T \geq \frac{32 e}{\epsilon \iota^2}$, emphasizing the critical role of $\epsilon$ and $\iota$ in the regret upper bound. Lastly, we provide numerical results to validate our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the problem of stochastic linear bandits with instantaneous linear constraints, where the action set is not star-convex. Under an assumption on the action set that is weaker than star-convexity, they given an algorithm with $\tilde{O}(d\sqrt{T})$ regret.

### Strengths
The problem that this paper considers is a nice one (non-star-convexity in safe linear bandits). The requirement of star-convexity is a significant limitation in present works on safe linear bandits. The presentation is also good. Their use of visuals is quite effective.

### Weaknesses
Although I think the problem is important, this paper makes very little contribution to the literature. The core result is that they show $\tilde{O}(d\sqrt{T})$ regret under Assumption 3, which assumes that either (1) the constraint is not tight on the optimal point, or (2) a line segment in the direction of the optimal point and of sufficient length is within the action set. The results of Amani et al (2019) immediately show $\tilde{O}(d \sqrt{T})$ regret under condition (1). As for condition (2), the specific requirement is quite contrived and appears to be just a quirk of the analysis of Pacchiano et al (2021). I don't think this contribution alone is sufficient to justify another paper.

Additional points:
- The lower bound (Theorem 2) looks like it is essentially identical to that in Pacchiano et al (2021), and I would suggest adding discussion if/how it is different.
- I think that the related work section should probably be in the body of the paper (at least in part) and I would suggest adding [1].
- line 040: the paper writes that "the reward for an action in stochastic linear bandits is modeled as the inner product between a feature vector and unknown parameter." Really, it's that the *expected* reward is modeled as such.

### Questions
- How is the lower bound (Theorem 2) different from Pacchiano et al. (2021)?
- I would suggest that the authors are more precise in how they discuss their contributions with respect to the claim of "first result for non-convex action sets." Previous works have considered non-convex sets, including those that are star-convex (Moradipari et al, 2021), as well as discrete sets (Pacchiano et al, 2021). I understand what the authors meant (i.e. first for non-star-convex sets and round-wise constraint satisfaction), but I suggest more precision to avoid confusion.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers safety-constrained linear bandit problems under non-convex or discrete feature spaces. It introduces the Local Point Assumption, which assumes that the feature space is locally continuous or that the optimal action does not lie on the safety boundary. The paper develops the NCS-LUCB algorithm with a newly designed exploration bonus $b_t(a)$.

### Strengths
The algorithm employs double confidence intervals in conjunction with the exploration bonus $b_t(a)$, which seems interesting. Assumption 3 is also interesting as it captures the locally information. Additionally, the paper provides both upper and corresponding lower bounds, which strengthen the theoretical contributions.

### Weaknesses
In my view, the statements of the assumptions and their explanations are not clear and needs more elaboration. Please see the questions below for details.

- **Necessity and Correctness of Assumption 2**: To me the assumption 2 seems unnecessary, or could there be an error in its statement?  Here are some observations:
  - This action yields initial estimates of θ and γ as zeros.
  - In the toy example on non-convexity bias (line 403), the action set does not include $a_0 = [0,0]^{\top}$.
  - In the experiment described on line 491, the action set also does not include $a_0 = [0,0]^{\top}$.
  - In Lemma 7 (line 877), it is stated that $|\|\phi(a_t)\||\geq \epsilon$ but  $a_0$ does not satisfy this condition.

- **Question about Assumption 3**
  - The first condition in Assumption 3 seems intuitively too strong. If we have the circle $||a_1||_2= 1$ in our action space, it results in a smaller safe circle within the action space. However, aren't two basis safe actions sufficient to estimate $\theta$ and $\gamma $ accurately? Are all the actions within this smaller safe circle necessary for the proofs and experiments? If so, is there a toy example that the algorithm won't work with only two basis safe actions?
  - Constraints on $L$ and $\tau$: When $L$ is very large (e.g., 100) and $\tau$ is very small (e.g., 0.01), how does the condition $L - \epsilon \leq 1$ hold in the second condition? Does this imply there are constraints on the relationship between $L$ and $\tau$? Could the authors provide more details or adjust the assumption accordingly?

- Could the authors elaborate on "What is the correct strategy?" Specifically, how is $b_t(a_1) = r^* - \tfrac{1}{3} = \tfrac{2}{3}$ derived? This seems different from equation (3).

- **Computational Issues:** I feel the proposed algorithm cannot be implemented to more general settings than discrete action space and have the following questions.
  - **Non-Discrete and Non-Convex Cases:** How does the proposed method computes the line 6 of Algorithm $a_t$ the non-convex non-discrete cases, such as when in action sets contains non-convex continuous regions? 
  - **Convex Cases:** Even in convex regions, as $b_t(a)$ in (3) takes much complicated form, is the optimization problem in line 6 of Algorithm $a_t$ still a convex program as in linear bandit problem that can be approximate efficiently?

### Questions
- **Necessity and Correctness of Assumption 2**: To me the assumption 2 seems unnecessary, or could there be an error in its statement?  Here are some observations:
  - This action yields initial estimates of θ and γ as zeros.
  - In the toy example on non-convexity bias (line 403), the action set does not include $a_0 = [0,0]^{\top}$.
  - In the experiment described on line 491, the action set also does not include $a_0 = [0,0]^{\top}$.
  - In Lemma 7 (line 877), it is stated that $||\phi(a_t)||\geq \epsilon$ but  $a_0$ does not satisfy this condition.

- **Question about Assumption 3**
  - The first condition in Assumption 3 seems intuitively too strong. If we have the circle $||a_1||_2= 1$ in our action space, it results in a smaller safe circle within the action space. However, aren't two basis safe actions sufficient to estimate $\theta$ and $\gamma $ accurately? Are all the actions within this smaller safe circle necessary for the proofs and experiments? If so, is there a toy example that the algorithm won't work with only two basis safe actions?
  - Constraints on $L$ and $\tau$: When $L$ is very large (e.g., 100) and $\tau$ is very small (e.g., 0.01), how does the condition $L - \epsilon \leq 1$ hold in the second condition? Does this imply there are constraints on the relationship between $L$ and $\tau$? Could the authors provide more details or adjust the assumption accordingly?

- Could the authors elaborate on "What is the correct strategy?" Specifically, how is $b_t(a_1) = r^* - \tfrac{1}{3} = \tfrac{2}{3}$ derived? This seems different from equation (3).

- **Computational Issues:** I feel the proposed algorithm cannot be implemented to more general settings than discrete action space and have the following questions.
  - **Non-Discrete and Non-Convex Cases:** How does the proposed method computes the line 6 of Algorithm $a_t$ the non-convex non-discrete cases, such as when in action sets contains non-convex continuous regions? 
  - **Convex Cases:** Even in convex regions, as $b_t(a)$ in (3) takes much complicated form, is the optimization problem in line 6 of Algorithm $a_t$ still a convex program as in linear bandit problem that can be approximate efficiently?

### Soundness
2

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
This paper investigates safe linear bandits in non-convex feature spaces, expanding the arm space from star-convex to local-point. The primary innovative technique is the newly proposed bonus term in Equation (4).

### Strengths
1. The paper is well-written, particularly in its comprehensive discussion of key points.

2. Providing both upper and lower bounds simultaneously enhances the completeness of this work and renders the newly proposed assumptions more convincing.

### Weaknesses
1. Expanding the arm space from star-convex to local point assumption offers limited contributions.

2. The technological innovation primarily lies in the newly proposed bonus term (4).

### Questions
1. The lower bound is of order $\Omega(1/\iota^2)$, while the upper bound is of order $O(1/\iota)$. This appears to be contradictory, as $1/\iota^2 > 1/\iota$. Could you please clarify this discrepancy?

2. Lines 324-328: Please provide a more detailed explanation of why $\alpha\phi(a_*) \in \phi(A_t)$ implies that the distance between $\alpha\phi(a_*)$ and $\phi(A_t)$ is less than $g_t^1(a)$.

3. How did you find Assumption 3? Were there any related works that inspired this assumption?

Although I am familiar with bandits, I have not yet encountered safe bandits. Therefore, I will adjust my score based on discussions and feedback from other reviewers.

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
This paper extends the stage-wise safe linear bandits to the non-convex spaces. Compared with the prior work Pacchiano et al. (2024), which studies the stage-wise safe linear bandits under the assumption that the arm set is convex, this paper finds the limitation of the algorithm LC-LUCB when the arm set is a non-convex spaces. By redesigning the bonus term in the confidence radius, the improved algorithm NCS-LUCB is capable of dealing with non-convex arm set.

### Strengths
- The paper is clear and is easy to follow.
- The problem of the bonus term in the previous literature in the context of non-convex arm set is well explained via examples and the intuition for the new bonus term is also clear.
- Both problem-independent upper bound and lower bound are provided, showing the importance of the parameters $\epsilon,\iota$ in the problem.

### Weaknesses
 **Majors**:
- In Line 376, the BOB method is only **adopted** by Zhao et al. (2020), and it is firstly **proposed** by [1]. 
- The technical contribution is limited. While the introduction of the new bonus term can be important, the rest of the analysis is quite standard.
- The proposed bonus term consists of $\iota$, which appears in Assumption 3 and is not known in practice. While it mentions the BOB technique [1] may be adopted to solve, it does not further investigate on it. As the design of the bonus term is the main technical contribution of this paper and the parameters $\iota$ plays an important role in the bounds, it is expected that the authors can provide a complete solution towards the bonus design.

**Minors**:
- It would be great to show some more complex examples (at least in the experiment). As this paper deals with linear bandits, the proposed examples, including the toy examples and the experimental examples, are composed by arms along the axis, making them quite similar to K-armed bandits (with minor additional setups).

### Questions
- In Assumption 1, it is assumed that $\max(\|\theta^*\|, \|\gamma^*\|) \leq \sqrt{d}$. Is it possible to bound it by other notations, e.g., $B$? In this case, the dependence on this quantity can be better reflected in the final regret bound.
- Is it possible to provide problem-dependent upper and lower bounds, consisting of the reward and cost gaps?
- According to Pacchiano et al. (2024), the minimax lower bound for the convex case is $\max \left( \frac{d \sqrt{T}}{8 e^2}, \frac{1 - r_0}{21 (\tau - c_0)^2} \right)$ which is of order $\Omega(d\sqrt{T})$. And Theorem 2 suggests the minimax lower bound in the nonconvex case is $\max \left\\{ \frac{1}{27} \sqrt{(d - 1) T}, \frac{1 - 2\epsilon}{\epsilon} \left( \frac{1 - \iota}{\iota} \right)^2 \right\\}$ which is of order $\Omega(\sqrt{dT})$. It is expected that the nonconvex case is a harder problem, thus, the lower bound should be larger. Can the author comment on this? In addition, how does $\tau$, the threshold on the cost, influence the lower bound?
- Is it possible to show the price (additional regret) for the nonconvexity in the arm set, compared to the convex arm set case?
- Can the authors kindly compare  this work with Amani et al. (2019), Pacchiano et al. (2024), and Moradipar et al. (2021)?

### Soundness
3

### Presentation
3

### Contribution
2
