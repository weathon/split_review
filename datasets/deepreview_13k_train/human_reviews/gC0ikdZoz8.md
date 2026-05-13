# Continuous-Time Analysis of Adaptive Optimization and Normalization

- Decision: Reject
- Scores: 3, 6, 5, 3

## Abstract
Adaptive optimization algorithms, particularly Adam and its variant AdamW, are fundamental components of modern deep learning. However, their training dynamics lack comprehensive theoretical understanding, with limited insight into why common practices—such as specific hyperparameter choices and normalization layers—contribute to successful generalization. This work presents a continuous-time formulation of Adam and AdamW, facilitating a tractable analysis of training dynamics that can shed light on such practical questions.
We theoretically derive a stable region for Adam's hyperparameters $(\beta, \gamma)$ that ensures bounded updates, empirically verifying these predictions by observing unstable exponential growth of parameter updates outside this region. Furthermore, we theoretically justify the success of normalization layers by uncovering an implicit meta-adaptive effect of scale-invariant architectural components. This insight leads to an explicit optimizer, $2$-Adam, which we generalize to $k$-Adam—an optimizer that applies an adaptive normalization procedure $k$ times, encompassing Adam (corresponding to $k=1$) and Adam with a normalization layer (corresponding to $k=2$). Overall, our continuous-time formulation of Adam facilitates a principled analysis, offering deeper understanding of optimal hyperparameter choices and architectural decisions in modern deep learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a continuous-time formulation of Adam(W). The authors derive the continuous-time ODE to approximate the parameter dynamics of Adam(W) via a Taylor expansion. The main application of the theory is to predict the stable region of hyperparameters $(\beta, \gamma)$ in which the Adam update won't blow up. The authors also use a similar method to study the dynamics of scale-invariant networks and identify the so-called "meta-adaptive effect," which needs further clarification.

However, I am a bit suspicious regarding the theoretical results of the paper. Most of the derivations are non-rigorous and hand-wavy.  Furthermore, the experimental results lack diversity and scale.

Overall, I think the research direction is interesting and the results can be quite useful. However, the theoretical derivations lack rigor and clarity. I am afraid I don't feel comfortable to support acceptance of the paper in its current form.


------- update -----------
thanks for addressing some of the concerns and updating the paper + experiments; 
i raised my score to 5; but i echoed Reviewer GyMg's point, the paper would benefit from further refinement and resubmission.

### Strengths
* The paper proposes a framework to approximate the parameter dynamics of Adam(W), which could be potentially very useful.
* This framework can help estimate the stable region of hyperparameters $(\beta, \gamma)$, which can be helpful in practice for hyperparameter selection.
* The framework is relatively easy to understand.

### Weaknesses
 - The whole theoretical framework is non-rigorous and based on flawed derivations/assumptions.
    - I don't understand the crucial deviation in Section C, and it should be put in the main text.
    - First, why is $m$ differentiable, why can you drop the higher order (second derivative is bounded?) of it?
   -  Second, why is it $g(t_n)$ not $g(t_n - \eta^p)$? In the latter setting, you would need to have an extra term $g'(t_n)$ and an error term $g''(t_n)$?
   - I think these are crucial questions, on which the whole paper is based. I also don't know why we should expect a continuous formation of the dynamics of $m$ in the first place.

* The experimental results are not convincing enough. I would expect larger scale + more diversity experiments, given the theoretical results are not rigorous. 
   - The training steps ($n=100$ or $1500$) are too few. should consider $n= O(10k)$
   - The scale and diversity of the experiments are limited (a small transformer on Shakespeare). I would expect the authors to run experiments on a more realistic dataset, like a 20M-100M parameter model on a subset of C4 or similar.

### Questions
- It is unclear how to get equation 7. 

-  can you clarify what does META-ADAPTIVE EFFECT mean? 

- can you clarify why the exponential moving average ($\|W\|$ vs $\|u_W\|$) is significant and surprise ? 

- I don't understand this "η  ̈φ = O(η2) + O(λη)," , and why you can drop this term, which hasn't mentioned in the main text.

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
The author presents a continuous time analysis of Adam. They first present the continuous version of Adam and a corresponding differential equation (eq 4). With this formulation they present a bound on the parameter updates (eq 5) which depends on the adam hyperparamters. They find that this bound holds reasonably well in practice, which provides some justification for why certain Adam hyperparameters work well in practice. The authors also motivate why Adam+normalization behaves like adam applied multiple times, a method they call Adam-k. The authors provide some small-scale experiments with Adam-k, showing benefits for training on CIFAR10.

### Strengths
- The paper is well written and crisp.
- Continuous time analysis of Adam is interesting and novel (AFAIK, but I’m not an expert). Since Adam is an important algorithm, any analysis of it can be impactful.

### Weaknesses
 - Assumptions 1 and 2 are not very intuitive, at least not to me. Specifically, the assumption that the gradient of the loss function with respect to the parameters is scale-invariant seems strong and requires more justification. It's unclear under what conditions this holds true in practice, and how it might affect the analysis if violated. Similarly, the assumption that each entry in the weight matrix experiences the same amount of adaptive scaling is also not immediately obvious and needs further elaboration. The paper would benefit from a more detailed discussion of the implications of these assumptions and how they relate to the practical use of Adam.
- CIFAR10 results are not very convincing, it’s small scale. The experiments on CIFAR10, while demonstrating the potential of the proposed Adam-k method, are not sufficient to fully validate its effectiveness. The scale of the experiments is limited, and it is unclear how well these results would generalize to larger, more complex datasets and models. The paper would benefit from more extensive experiments on a wider range of tasks and architectures to provide more compelling evidence for the practical utility of Adam-k.

### Questions
- How tight is the bound of eq 5? Is there a corresponding lower bound?
- Can you add more experimental verification of Adam-k?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies Adam through the lens of Ordinary Differential Equations (ODEs). The authors utilize this continuous-time model to reveal aspects of Adam's dynamics in the **full-batch setup, i.e. no stochasticity in the gradients**. In particular, they provide theoretical arguments to identify a stability region for the hyperparameters $\beta_1$ and $\beta_2$, which characterizes the maximum size of the Adam updates. Importantly, they provide some experimental validation of their claims and offer a conjecture that correlates generalization to this region. Finally, they study the beneficial impact of scale-invariant architectural components and leverage their insights to introduce a new optimizer, dubbed k-Adam.

### Strengths
- **Originality:** The authors present a novel and quantitatively precise stability region for Adam's betas in the non-stochastic, continuous-time regime, filling a gap in the literature. While several papers discuss Adam’s performance under stochastic gradients, this work focuses on a deterministic model and provides insights under simplifying assumptions.
  
- **Quality:** The theoretical contributions are sound and grounded in ODE analysis. The derivation of a stability region for Adam is supported by both mathematical rigor and experimental validation. The authors maintain an interesting balance between theory and practical insight, though certain aspects (such as stochastic gradients) are left for future exploration.

- **Clarity:** The paper communicates its main theoretical contribution—the stability region for the betas—relatively clearly, though some sections (like the explanation of k-Adam and the role of normalization) could be refined for better comprehension.

- **Significance:** The work provides potentially valuable insights into the dynamics of Adam in a deterministic setting. If this stability region has practical relevance beyond full-batch training, it could offer a useful guideline for tuning $\beta_1$ and $\beta_2$. Additionally, the introduction of k-Adam as a new optimizer inspired by the theoretical results opens avenues for further exploration.

### Weaknesses
Since there is no predefined space to provide a "General Comment", I provide it here.

**Overall Comment:**
The paper addresses interesting and mathematically sound questions, but the manuscript quality is lacking in several areas. It needs substantial improvement, and I recommend **rejecting** the paper, with strong encouragement to resubmit once the following issues have been addressed. In particular, I highlight: i) Missing discussion of literature; ii) Missing discussion on contributions: What is the final product? How can this help practitioners? iii) Better visualizations are needed; iv) Unclear whether the continuous-time model was NECESSARY over the discrete-time setup; Unclear discussion regarding normalization; k-Adam does not seem to be properly justified nor properly tested.

I will now provide a "Detailed Feedback" that covers some weak points and incorporates some questions:

The following points are presented in the same order as they appear in the paper. Unfortunately, due to format alterations in the PDF, I cannot reference line numbers, but I will do my best to highlight clear landmarks:

1. **Literature Review:**
A review of the literature on continuous-time models for optimizers is crucial, with a particular focus on those that cover Adam. Notably, there is no citation of Malladi et al., who derive an SDE model for Adam, thus addressing the stochastic aspect, which is lacking in this paper.

2. **Limitations Section:**
A brief section outlining the limitations of the approach would be useful. Additionally, a subsection comparing the method to existing literature could provide more clarity.

3. **Merging Contributions:** In "1. Continuous-time formulation (Section 2)", why not merge these two points into a simpler one? It seems to me that you simply derived an ODE for Adam, which also entails the derivation of Adam's update.

4. **Better explanation and context:** Your main contribution seems to be the stability region for the betas. Parameter sets inside that region imply that the maximum increment of Adam is controlled, while outside of it, an exponential explosion is "predicted". i) While this is interesting, it is unclear if it is practically relevant. Does this give practitioners new insights on selecting the betas? Or are they always in the "safe region"? ii) Is it beneficial to avoid such explosions? Adam is often successfully used even when loss spikes are observed. iii) RMSprop and SignSGD are subcases of Adam: Are they covered by this framework? It seems that RMSprop is always in the stable region, so adding momentum to RMSprop might make it unstable. This is a peculiar observation, as momentum is usually thought of as a stability enhancer.

5. Is it possible that betas in the instability region could benefit from better tuning of the learning rate? I conducted a small experiment on a simple convex quadratic and identified your regions experimentally (via visual inspection, not by plotting your lines). I tested this with learning rates spanning three orders of magnitude and 100 values for each beta: 30,000 small runs. I observed that the stability region expands as the learning rate drops. Could you comment on this? Including a graphical representation for a cheap setup like the one described above would be helpful. If you need the details of my experiment, feel free to ask. Expanding this toy example to the stochastic setting while varying noise levels is also crucial: Could noise shrink the stability region? How does weight decay alter this region?

6. When discussing contribution (f), as well as later in the text, the exact contribution is unclear. Since this is a main point, it must be crystal clear.

7. Regarding contribution (g), it is unclear what advantages k-Adam has. While a high-level description is fine, more details are needed about k-Adam’s advantages, both theoretically and empirically.

8. **Eq. 2:** These formulas for $m$ and $v$ are simply the continuous-time versions of their discrete counterparts, which are already known. Are these surprising in any way? Do they reveal something that the discrete-time version does not?

9. **Eq. 4:** Is your second-order ODE equivalent to the formulation in terms of three first-order ODEs (see Eq. 3.3 of Barakat)? Is there an intrinsic advantage to this point of view?

10. **Eq. 4:** It seems that even if the RHS (e.g., $u(t)$) is set to 0, Adam would still follow a non-trivial second-order ODE that can likely be solved explicitly. This suggests some oscillatory dynamics. Could you elaborate? It seems odd that parameters would evolve even if Adam’s increments are 0.

11. **Figure 1:** I suggest using a color-blind-friendly palette and adding line markers. Rather than comparing the trajectories of some weight, you could calculate the average squared error between the entire trajectory of the real weights and that of the ODE and plot that instead. This would give a more global intuition. I also suggest plotting for longer time and different values of $p$.

12. **Max-update bound:** As highlighted earlier, elaborating more on RMSprop and SignSGD is key.

13. **Eq. 5:** Is this bound independent of the learning rate and $p$? My experiments suggest that the stability region enlarges with a smaller learning rate. Reorganizing this as a well-stated proposition might help.

14. **"We highlight that this bound is only possible because..."**: Specify that the reason why you can do this is actually because you do not use stochastic gradients. Also, was it absolutely necessary to use the continuous-time model for this bound, or could it have been derived from the discrete-time version expressions of $m$ and $v$?

15. **Figure 3:** The plots could benefit from reordering. Panel (c) is described before (a) in the caption. Clear legends and a color-blind palette would be helpful.

16. **Section 3.3:** Of course, if you leave the stability region, generalization will likely worsen. However, inside the region, is there a "monotonicity" effect? Is it the case that the further inside the region, the better the generalization? If so, can one always get some guidance in selecting the betas? This is a good point for future research.

17. **Section 4.2:** I’ve reread this multiple times, and it is unclear what the message of this section is. If there is a clear takeaway, I suggest highlighting it. Frame technical results as Lemmas, minimize references to the appendix by grouping them and provide a clear paragraph interpreting the results. Experimental validation is already present, which is good.

18. **k-Adam:** I struggle to see the takeaway from this discussion. First, I suggest removing the 2-Adam discussion currently found before Section 4.3. Otherwise, simply incorporate it into the following section where you properly describe k-Adam. Then, I question the purpose of i) introducing a new optimizer based on loosely justified intuition from Section 4.2, ii) not highlighting clearly its advantages over Adam, and iii) not evaluating it on state-of-the-art experiments. I wonder whether this should be in the main paper as a major contribution.

19. Finally, this analysis is conducted in a deterministic setting: How can it be generalized to cover stochastic gradients? I expect noise to interact in a non-trivial way with all the moving elements of these analyses.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors propose continuous ode approximations for the first and second-order moments $m_t$ and $v_t$. Based on these continuous ode approximations, the authors provide a theoretical guarantee for the stability of the update of Adam. Besides, the authors also demonstrate that the iterates of Adam is an exponential averaging of $m_t/\sqrt{v_t}$ when applied to a scale-invariant architecture. Based on this property, the authors propose a new variant of Adam with a normalization layer.

### Strengths
This paper contains some interesting empirical results.

### Weaknesses
1. This paper lacks sufficient novelty. Specifically, the conclusion that the update of Adam is bounded given specific exponential moving average rates—one of the major technical contributions of this work—has already been discussed in several prior studies [1, 2, 3, 4], utilizing the Cauchy-Schwarz inequality. Additionally, reference [2] provides a tight bound for the accumulated updates of Adam. Moreover, similar techniques involving continuous approximation for the momentum terms $m_t$ and $v_t$ have also been explored in [5, 6].

2. This paper lacks a thorough discussion of previous works. [6] provides a comprehensive analysis of Lion-K algorithms by constructing an ODE approximation of the dynamic system and establishing a Lyapunov function for this ODE system. By the specific pattern of  the Lyapunov function, they provide an interesting and novel analysis of each hyperparameter in the optimization problem. I believe this contribution is worth highlighting.

3. The assumptions presented in the paper are relatively problematic. Regarding assumption 4.1, while I agree that high-dimensional vectors tend to be nearly orthogonal, the statement that they are "approximately 0" does not imply they are exactly 0. For a rigorous mathematical derivation, the authors should provide a bound for this term and explain why it can be considered negligible in relation to the other terms, rather than simply omitting it as they have done in the current proof. As for assumption 4.2, it is quite unusual. If this assumption is valid, it implies that each coordinate of $v_t$ is equal, which results in the absence of a coordinate-wise adaptive learning rate effect. Under such an assumption, I fail to see any significant distinction between gradient descent with momentum and 'Adam'. Finally, the conclusion that $\|\dot W_t\|_2 \approx \|u_t\|_2$ based on these two assumptions might also be insuitable. As [2, 3, 7] demonstrated, Adam aligns more with $\ell_\infty$ norm instead of $\ell_2$ norm.

4. The scaling of Euler's approximation is inconsistent in this paper. In the derivation of ode approximation of $m_t$ and $v_t$, the authors choose the $\eta^p$ as the stepsize and omit all terms containing high order terms, while in the derivation of formula (4), the authors remain a term with coefficient $\eta^{2p}$.

### Questions
I suggest that the authors adjust their template since I do not find the indexes of lines in their manuscript.

### Soundness
2

### Presentation
2

### Contribution
1
