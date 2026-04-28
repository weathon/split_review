# Optimizing $(L_0, L_1)$-Smooth Functions by Gradient Methods

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract


## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a general understanding of the $(L_0, L_1)$-smooth function class, which has recently gained increasing interest due to its empirically observed connections to deep learning applications. They authors establish a parallelism between the classical optimization theory for $L_0$-smooth functions, and show how analogous inequalities and algorithm design strategies should be carried out with $(L_0, L_1)$-smooth functions. This includes the derivation of $(L_0, L_1)$-smooth version of the cocoercivity inequality, analysis of fixed-stepsize gradient descent method for convex and nonconvex cases, and analysis of gradient methods using normalized stepsizes, Polyak stepsizes, and Nesterov-type acceleration for convex functions.

### Strengths
As mentioned in the Summary section, this paper nicely demonstrates the parallelism of how the traditional techniques from smooth (convex) minimization should be properly interpreted and applied to the class of $(L_0, L_1)$-smooth functions. As a reader who is much more familiar with the classical optimization theory but not as much with the recent theory of $(L_0, L_1)$-smooth optimization, the paper was interesting, easily readable, and informative. It seems such viewpoint has not been provided previously with this level of clarity, and I think this work could serve as a solid reference for those future readers who are interested in this area. The algorithms and their convergence results the paper provides within various setups seem correct and competitive.

### Weaknesses
The primary weakness of the current version of the paper is the writing. While I think the technical contents are good, the writing does not seem to be polished carefully enough and should be managed before the publication. The general flow is okay, but there are many detailed points which I would recommend the authors to address; please refer to the Questions section. I would recommend acceptance of the paper provided that the writing issues get resolved.

Writing issues (in the order of appearance)
- In pg. 3, lines 108-109, it will be illustrative to explain in more detail in which aspects the authors' proof techniques differ from that of the work [1], cited as Gorbunov et al. (2024) in the manuscript. Also I think the authors should be more cautious about claiming that the proof is more "elegant" than something else. One possible suggestion is to emphasize their clearer parallelism with the classical theory, rather than to describe the value of this paper's framework with a subjective expression like "elegant".
- The statement of Lemma 2.2 involves the notation $\phi(t) = e^t - t - 1$, while its proof in the Appendix uses the symbol $\phi$ to denote something else. Please change it.
- The bound $\phi_* (\gamma) \ge \frac{\gamma^2}{2+\gamma}$ appears suddenly in the statement of Lemma 2.3, while the relevant discussion appears later in Section 3. I think this should be relocated to somewhere near Lemma 2.3.
- In pg. 4, lines 164-165, the meaning of the sentence "we present some examples to support the choice of generalized smooth assumption" is unclear.
- Proposition 2.6 and the subsequent discussion doesn't seem very relevant to the rest of the paper. To some readers this information could be valuable, but generally speaking, I even think the whole part can be moved to the Appendix without altering the flow of the paper. Also, please clearly define the expressions like "$M$-Lipschitz twice continuously differentiable" before using it.
- In line 183-184, there is dangling "for some" after the period.
- In Theorem 3.1, it should have been assumed/defined that $f^* := \inf f > - \infty$. In general, the authors did not properly state that they assume the existence of a minimizer $x^*$, etc. (in subsequent theorems regarding convex cases). Please be precise about these points.
- In the statement of Theorem 3.2, is $||x_0 - x^*||$ intended to be denoted as $R_0$?
- In pg. 6, in lines 297-298, it is not clear what the authors mean with "by using the preceding estimate and the update rule of the method". Only after reading the proof in the Appendix I could understand the technique deriving equation (20), and I still do not feel that the text surrounding the equation is successfully conveying the idea. If you intend to provide a high-level intuition, please be more precise and detailed. Also, note that the exponent 2 is missing in $R_{k+1}^2$ within (20), and in equation (43), the $g_k^2$ factors seem to be missing.
- Lines 304-310 provide an interesting insight on the complexity $\mathcal{O}(L_0 R_0^2 / \epsilon + L_1^2 R_0^2)$, but I think the complexity analysis does not clearly show that the constant $\mathcal{O}(L_1^2 R_0^2)$ complexity corresponds to the phase where the algorithm reaches the regime where $f$ behaves like a smooth function. (Which is in contrast with Section 6, where the algorithm is deliberately designed in this way.) Can this discussion somehow be made more precise?
- In Theorem 4.2, $R$ is used without being defined.
- I do not see any reason why Lemma 4.1 is introduced in pg. 7. I think a discussion on how (22) is utilized in the analysis is missing.
- In lines 349-350, the authors say "time-varying stepsizes can be eliminated", but this seems to be a conjecture (or at least, something that the authors do not formally prove) and I think it should be reworded. Please be careful about making such statement.
- In pg. 8, lines 378-380, the authors emphasize that their rate does not have an exponential dependency on $L_0, L_1$, but why does this worth emphasis? Are there prior work which analyzed gradient method with Polyak stepsizes in the same setup and obtained rate that involves $\exp (L_0), \exp (L_1)$? If so, please specify.
- In lines 400-401, the authors mention that "Our rate is better than $\mathcal{O}(L_0 R^2 / \epsilon + \sqrt{L / \epsilon} L_1 R^2)$", but where does this rate come from?
- In the beginning of Section 6 (and also the same for Sections 4, 5) please clearly specify in the first sentence introducing the setup that you are dealing with convex functions.
- It is weird that Algorithm 1 (which is not the algorithm that the authors develop) is packaged using the Algorithm environment, while the authors' algorithm (lines 427-431) isn't. 
- The Step 1 of the authors' algorithm in Section 6 requires to find a point $\bar{x}$ satisfying $f(\bar{x}) - f(x^*) \le \frac{L_0}{8 L_1^2}$. I think this requires either the knowledge of $f(x^*)$ or $R=||x_0 - x^*||$ (in order to determine when to stop). Is this understanding correct? If so, this is a limitation that should be clearly explained.
- Theorem 6.1 misses the convexity assumption in the statement. Also, it analyzes the AGMsDR algorithm with initial point satisfying  $f(x_0) - f(x^*) \le \frac{L_0}{8 L_1^2}$, but this is inconsistent with the $\bar{x}$ notation used in lines 427-431. I think this also comes from the problem of not highlighting their "procedure" as a separate algorithm with a proper name.
- In lines 477-478, should the two occurrences of $R$ be the same values? It seems like one is $||x_0 - x^*||$ and one is $|\bar{x} - x^*||$.
- In line 483, the authors again mention "not have an exponential dependency". Please cite a relevant prior work explaining why this is worth emphasis.
- It is not clearly defined what the figure labels like NGD, GD1, GD2, etc. precisely means. Even though it could be speculated if one reads through Section 7, this should be done somewhere, for example, within the figure caption.
- In Figure 2, please specify that you are using $L_0 = (\frac{p-2}{L_1})^{p-2}$ according to Example 2.4 (if this understanding is correct).

### Questions
Writing issues (in the order of appearance)
- In pg. 3, lines 108-109, it will be illustrative to explain in more detail in which aspects the authors' proof techniques differ from that of the work [1], cited as Gorbunov et al. (2024) in the manuscript. Also I think the authors should be more cautious about claiming that the proof is more "elegant" than something else. One possible suggestion is to emphasize their clearer parallelism with the classical theory, rather than to describe the value of this paper's framework with a subjective expression like "elegant".
- The statement of Lemma 2.2 involves the notation $\phi(t) = e^t - t - 1$, while its proof in the Appendix uses the symbol $\phi$ to denote something else. Please change it.
- The bound $\phi_* (\gamma) \ge \frac{\gamma^2}{2+\gamma}$ appears suddenly in the statement of Lemma 2.3, while the relevant discussion appears later in Section 3. I think this should be relocated to somewhere near Lemma 2.3.
- In pg. 4, lines 164-165, the meaning of the sentence "we present some examples to support the choice of generalized smooth assumption" is unclear.
- Proposition 2.6 and the subsequent discussion doesn't seem very relevant to the rest of the paper. To some readers this information could be valuable, but generally speaking, I even think the whole part can be moved to the Appendix without altering the flow of the paper. Also, please clearly define the expressions like "$M$-Lipschitz twice continuously differentiable" before using it.
- In line 183-184, there is dangling "for some" after the period.
- In Theorem 3.1, it should have been assumed/defined that $f^* := \inf f > - \infty$. In general, the authors did not properly state that they assume the existence of a minimizer $x^*$, etc. (in subsequent theorems regarding convex cases). Please be precise about these points.
- In the statement of Theorem 3.2, is $||x_0 - x^*||$ intended to be denoted as $R_0$?
- In pg. 6, in lines 297-298, it is not clear what the authors mean with "by using the preceding estimate and the update rule of the method". Only after reading the proof in the Appendix I could understand the technique deriving equation (20), and I still do not feel that the text surrounding the equation is successfully conveying the idea. If you intend to provide a high-level intuition, please be more precise and detailed. Also, note that the exponent 2 is missing in $R_{k+1}^2$ within (20), and in equation (43), the $g_k^2$ factors seem to be missing.
- Lines 304-310 provide an interesting insight on the complexity $\mathcal{O}(L_0 R_0^2 / \epsilon + L_1^2 R_0^2)$, but I think the complexity analysis does not clearly show that the constant $\mathcal{O}(L_1^2 R_0^2)$ complexity corresponds to the phase where the algorithm reaches the regime where $f$ behaves like a smooth function. (Which is in contrast with Section 6, where the algorithm is deliberately designed in this way.) Can this discussion somehow be made more precise?
- In Theorem 4.2, $R$ is used without being defined.
- I do not see any reason why Lemma 4.1 is introduced in pg. 7. I think a discussion on how (22) is utilized in the analysis is missing.
- In lines 349-350, the authors say "time-varying stepsizes can be eliminated", but this seems to be a conjecture (or at least, something that the authors do not formally prove) and I think it should be reworded. Please be careful about making such statement.
- In pg. 8, lines 378-380, the authors emphasize that their rate does not have an exponential dependency on $L_0, L_1$, but why does this worth emphasis? Are there prior work which analyzed gradient method with Polyak stepsizes in the same setup and obtained rate that involves $\exp (L_0), \exp (L_1)$? If so, please specify.
- In lines 400-401, the authors mention that "Our rate is better than $\mathcal{O}(L_0 R^2 / \epsilon + \sqrt{L / \epsilon} L_1 R^2)$", but where does this rate come from?
- In the beginning of Section 6 (and also the same for Sections 4, 5) please clearly specify in the first sentence introducing the setup that you are dealing with convex functions.
- It is weird that Algorithm 1 (which is not the algorithm that the authors develop) is packaged using the Algorithm environment, while the authors' algorithm (lines 427-431) isn't. 
- The Step 1 of the authors' algorithm in Section 6 requires to find a point $\bar{x}$ satisfying $f(\bar{x}) - f(x^*) \le \frac{L_0}{8 L_1^2}$. I think this requires either the knowledge of $f(x^*)$ or $R=||x_0 - x^*||$ (in order to determine when to stop). Is this understanding correct? If so, this is a limitation that should be clearly explained.
- Theorem 6.1 misses the convexity assumption in the statement. Also, it analyzes the AGMsDR algorithm with initial point satisfying  $f(x_0) - f(x^*) \le \frac{L_0}{8 L_1^2}$, but this is inconsistent with the $\bar{x}$ notation used in lines 427-431. I think this also comes from the problem of not highlighting their "procedure" as a separate algorithm with a proper name.
- In lines 477-478, should the two occurrences of $R$ be the same values? It seems like one is $||x_0 - x^*||$ and one is $||\bar{x} - x^*||$.
- In line 483, the authors again mention "not have an exponential dependency". Please cite a relevant prior work explaining why this is worth emphasis.
- It is not clearly defined what the figure labels like NGD, GD1, GD2, etc. precisely means. Even though it could be speculated if one reads through Section 7, this should be done somewhere, for example, within the figure caption.
- In Figure 2, please specify that you are using $L_0 = (\frac{p-2}{L_1})^{p-2}$ according to Example 2.4 (if this understanding is correct).

[1] Gorbunov et al., Methods for Convex $(L_0,L_1)$-Smooth Optimization: Clipping, Acceleration, and Adaptivity.

### Soundness
4

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
The paper studies gradient methods for solving problems with (L0, L1)-smoothness, a recent class of functions developed by Zhang et al. (2019). Novel convergence results are established in this paper, including tighter bounds on function growth and the complexity bound for finding near stationary points in both nonconvex and convex cases. Some new methods with different step sizes are also examined.

### Strengths
1. The paper is well-written and easy to follow. The analysis is thorough and offers many insights for research in optimization.

2. I appreciate the comparison between this paper and Gorbunov et al. (2024), which is comprehensive and particularly crucial for readers.

3. I have attempted to implement some of the suggested algorithms and found that the analysis presented here is essential for practical use, especially when the optimal step size in equation (11) is given explicitly.

### Weaknesses
The following are some major concerns about the paper.

1. The numerical experiments are conducted only on simple functions. I suggest that the authors significantly improve this section by employing more diverse examples, particularly in nonconvex cases. For examples, could the authors consider loss functions from deep learning models or other challenging nonconvex optimization problems from applications?

2. If I have not overlooked anything, the current paper does not discuss the difficulties of deriving the convergence properties for (L0, L1)-smooth functions compared to L-smooth functions, nor how the authors overcome these challenges. Can the author discuss key challenges in analyzing (L0,L1)-smooth functions compared to L-smooth functions, and to highlight any novel theoretical tools or techniques they developed to overcome these challenges.

3. I do not find Proposition 2.6 impressive, as the results are rather predictable, and the proofs seem straighforward. 

4. The authors mention that "we cannot guarantee that the class is closed under all standard operations, such as the summation". Can you provide a concrete counterexample showing that the sum of two (L0,L1)-smooth functions is not necessarily (L0,L1)-smooth? If so, are there any additional conditions that could guarantee the sum remains in this function class?

5. The authors claim that the estimate in (4) is tighter than those presented in previous works. Can you provide a numerical example or theoretical argument demonstrating how your estimate in (4) is tighter than previous bounds? Is it possible to prove that this bound is optimal, or are there cases where it could potentially be improved further?

### Questions
See weakness

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
The author(s) present non-asymptotic convergent analyses of various types of gradient methods on convex and non-convex functions satisfying $(L_0, L_1)$-smoothness, which is a type of generalized smoothness assumption that has gained some interests recently in machine learning community.

They derive a series of first-order upper bounds, implied by the generalized smoothness assumption, which are tigher bounds than previous works. Furthermore, they derive similar lower bounds when the functions are convex.

Using these newly derived bounds, they present a convergent analysis on non-convex functions, which matches the current best-known rate of this function class up to absolute constants.

For convex functions, however, they derive better-than-existing convergent rates for different gradient methods of this particular function class.

Finally, they experiment with a simple $||\mathbf{x}||^p / p$ function, where the constants $L_0$ and $L_1$ can be known in advance.

### Strengths
To me, one of this paper's main strengths/contributions is the derivation of tighter first-order upper and lower bounds. The bounds will undoubtedly help any further work on analyzing this particular function class.

In Theorems 3.2 and 5.1, the author(s) is able to dispense $L$-gradient Lipschitz, which was additionally assumed in the previous works Koloskova et al 2023, while improving the current existing rate.

The overall flow of the paper is well-presented.

### Weaknesses
1. Numerical results can be strengthened by providing more experiments. The current experiments are limited to a simple $||\mathbf{x}||^p / p$ function, which does not fully demonstrate the practical implications of the theoretical findings. More diverse and complex experiments, including real-world datasets and different types of objective functions, are needed to validate the proposed methods.

2. For Theorem 3.1, while the rate is better than that of Hubler et al 2024, the dependency on $L_0$ and $L_1$ in the step-size is a concern. The result in Hubler et al 2024 does not have this dependency, which makes their method more practical in cases where these constants are not known or are difficult to estimate. This limits the applicability of Theorem 3.1 in practice.

3. (line 269) The statement "By Theorem 3.1, the smallest number K of iterations required to achieve ..." is incorrect. It is possible to choose an initial point such that $||\nabla f(x_{0}) || < \epsilon_{\mathbf{g}}$, in which case $K = 0$, violating the claim. The correct wording should be "By Theorem 3.1, obtaining the stationary point requires at most ... ". The current wording is misleading and needs to be revised.

4. (Theorem 5.1) The presentation of the theorems should be consistent. It is recommended to present the result in the form of "$K \geq $," similar to other theorems, to maintain uniformity and clarity.

5. $||\mathbf{x}_0 - \mathbf{x}^*||$ is inconsistently denoted as both $R_0$ and $R$, e.g., in Theorem 3.2. This lack of consistency in notation can cause confusion and should be addressed.

6. (line 257) "absolte" should be corrected to "absolute".

7. (eq. 14) The inequality should be $... \geq \frac{||\nabla f(x)||^2}{2L_0 + 3L_1||\nabla f(x)||}$, i.e., there is no 2 in the numerator, as per Lemma B.1. The current equation is incorrect.

8. (line 641) $s$ should be defined as $s := \nabla f(x) - \nabla f(y)$. Otherwise, the sign in the inequality at line 643 is incorrect. The current definition leads to an inconsistency in the subsequent inequality.

9. (line 648) Change $\phi^*(\gamma)$ to $\phi_*(\gamma)$ to maintain consistency with the notation used elsewhere in the paper.

10. (line 651) Some of the gradients should be of variable $y$, not just $x$, i.e., $\nabla f(y)$. The current notation is incomplete and should be corrected.

### Questions
1. Another way to dispense of the dependency of the constants $L_0$ and $L_1$ in the step-size is to perform backtracking line-search, which also guarantees descents in the objective function value. Can the given new bounds (Lemma 2.2, 2.3) improve the rate derived by Hubler et al 2024?

2. For Theorem 6.1, empirically, is there any way to tell when to switch to AGMsDR? That is, can we tell that we are in a local region?

3. Have you tried experimenting with a softmax function, which I believe the constants $L_0$ and $L_1$ can be analytically evaluated? This example will provide more insights than the simple function $||\mathbf{x}||^p$.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper examines the extension of a certain optimization method to a broader smoothness assumption, specifically $L_0,L_1$-smoothness. While it broadens the class of functions to be minimized, the authors manage to recover convergence rates comparable to those of the standard $L$-smooth case, albeit with an additional term that does not depend on the final accuracy.

### Strengths
- For convex problems, authors improves existing results by achieving $O( L_0R^2 / \varepsilon + L^2_1 R^2)$
- Normalized gradient method and gradient method with Polyak stepsizes, which do not require the knowledge of the parameters $L_0$, $L_1$ and have the same rate as above
- Accelerated method with $O( \sqrt{L_0R^2 / \varepsilon} + L^2_1 R^2)$

### Weaknesses
 - Lack of analysis  for stochastic case is significantly limiting practical value of the work
- Accelerated method requires a line search (minor)
- The second part of the second question from below
- The accelerated method, AGMsDR, relies on a two-stage approach, which introduces practical limitations. The first stage requires knowledge of $L_0$ and $L_1$ (or at least their ratio and an upper bound on $L_0$ and $L_1$) to determine the number of steps. This is in contrast to standard gradient descent which only requires a single parameter, $L$, such that $L \geq L_0$ and $L \geq L_1$. This reliance on additional parameters makes the accelerated method less practical than the non-accelerated methods.
- The contribution of the tighter bounds in Lemma 2.2 is not clearly demonstrated. While the authors claim the bounds are tighter, the practical impact on the final convergence rates, especially in terms of constant factors, is not explicitly shown. It is not clear if these tighter bounds lead to a significant improvement in the final bounds or if they only provide a theoretical advantage in the derivation of optimal step sizes. The lack of concrete examples makes it difficult to assess the real-world benefit of these tighter bounds.

### Questions
- As a contribution authors listed in line 54 "tighter bounds on descent inequalities". But in line 58 authors "achieve the best-known" rate for non convex functions. I am curious if the tighter bounds actually helps to improve convergence. I would expect improving the rate, if they actually help. As far as I understand, the tighter bounds are supposed to help for the non-simplified stepsize version and some logarithmic improving factor should appear. Am I right? Could the authors answer this question by providing rates with their tighter bounds and with non-tight bounds?
- Acceleration does not seems fair. By initially running non-accelerated method authors enter the area where $\|\|\nabla f(x) \|\|\leq \frac{L_0}{L_1}$, making the right hand side of the generalized smoothness condition (line 121) $L_0 + L_1|\|\nabla f(x) \|\| \leq 2L_0$, that corresponds to the standard smoothness assumption. 
   - In the standard $L$-smooth case there exist accelerated methods without line search (e.g. Similar Triangles Method), that keep iteration bounded ($\|\|x^k - x^* \|\|  \leq R \cdot const$), so I am expecting such methods stay in the area. Can the line search be avoided in your analysis? Or what is it crucial role? 

  - The term  $L^2_1 R^2$ corresponds to the number of iteration to enter the area with bounded gradient. Then the authors in fact deal with the standard $2L$-smooth case, while obtaining the other term. This observation is consistent with non-accelerated methods, considered in the paper. I would like to note, that acceleration in fact is used only in the area where the standard $2L$-smooth case takes place, and does not help to enter the area faster. In other words I would say that the contribution in fact is -- a bound on the number of oracle calls to enter this area. And I am expecting this bound to be improved in the accelerated case. Don't get me wrong, but I could not consider the convergence of AGMSDR in the standard $2L$-smooth case as a contribution. I would like authors to address my concerns, and clarify about their contribution to this part. Is it an application of the authors result of non-accelerated method to bound the number to enter the area with bounded gradient? 

I would like to comment on the scores. Taking the above questions into account, I currently accept the contributions related to first-order methods. The results are new and significantly improve previous rates. But they rely on the only basic result -- descent inequalities. The rest is an application of the new inequalities to the well-known methods. That is why I consider the contribution as limited. I open for a discussion and the authors are likely to expect higher scores if my concerns are convincingly addressed, especially about the area with bounded gradient.

### Soundness
3

### Presentation
3

### Contribution
3
