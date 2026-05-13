# Stochastic Polyak Step-sizes and Momentum: Convergence Guarantees and Practical Performance

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Stochastic gradient descent with momentum, also known as Stochastic Heavy Ball method (SHB), is one of the most popular algorithms for solving large-scale stochastic optimization problems in various machine learning tasks. In practical scenarios, tuning the step-size and momentum parameters of the method is a prohibitively expensive and time-consuming process. In this work, inspired by the recent advantages of stochastic Polyak step-size in the performance of stochastic gradient descent (SGD), we propose and explore new Polyak-type variants suitable for the update rule of the SHB method. In particular, using the Iterate Moving Average (IMA) viewpoint of SHB, we propose and analyze three novel step-size selections: MomSPS$_{\max}$, MomDecSPS, and MomAdaSPS. For MomSPS$_{\max}$, we provide convergence guarantees for SHB to a neighborhood of the solution for convex and smooth problems (without assuming interpolation). If interpolation is also satisfied, then using MomSPS$_{\max}$, SHB converges to the true solution at a fast rate matching the deterministic HB. The other two variants, MomDecSPS and MomAdaSPS, are the first adaptive step-sizes for SHB that guarantee convergence to the exact minimizer without prior knowledge of the problem parameters and without assuming interpolation. The convergence analysis of SHB is tight and obtains the convergence guarantees of SGD with stochastic Polyak step-sizes as a special case. We supplement our analysis with experiments that validate the theory and demonstrate the effectiveness and robustness of the new algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper introduces Polyak step size to Stochastic Heavy Ball method. To do this, authors consider iterate moving-avergage viewpoint of stochastic heavy ball method. With slight modification of the step size adjustment technique, authors propose three new step size selection: one is based on regular Polyak step size for SGD, and the rest - on decreasing versions of Polyak step size for SGD. The resulting algorithms do not need knowledge about any of problem parameters and converge either to exact solution in non-interpolated regime or to the area of solution in interpolated regime. Convergence rates match the existing state-of-the-art results.

### Strengths
Authors propose a connection between both Polyak step size and adaptive Polyak step size with stochastic heavy ball method, which seems like an important result for optimization community. The proposed technique does not need any knowledge about problem parameters, which makes methods easier to implement. Theoretical convergence results show that proposed methods either outperform or perform on the same level with existing state-of-the-art algorithms while sometimes mitigating some of the issues of these algorithms. Finally, experimental results show either similar or better performance on both synthetic and real problems in comparison with existing analogs.

### Weaknesses
The Section 3 is written in rather overwhelming way. After each theorem goes a paragraph, mentioning some special cases and how the provided result matches the results from other existing works, which is rather hard to comprehend for a new reader. You could change these paragraphs to small tables with small supporting captions. This should take about the same size as the paragraph in text, although it would be much more evident. Additionally, after every theorem follows a lot of corollaries, that again consider some special cases. It is easy to get lost in so many special cases. I think, some of these corollaries can also be moved to appendix, leaving some mention about them in the main part. Since the main result is introduction of Polyak step size and adaptive Polyak step size to SHB, it should be the central point of main part of the paper. 
Overall, despite the seemingly good results, considering everything above and some suggestions in Question part, I think the main text needs polishing and not ready yet for publication. Specifically, in Section 3.1, the assumption regarding the finite optimal objective difference is embedded within the text rather than being explicitly stated as a separate assumption, making it difficult to quickly identify the core assumptions. Furthermore, in Corollary 3.4, the crucial detail that a constant step size is being considered is not explicitly mentioned, which could lead to confusion for readers who have not thoroughly read the preceding paragraph. This lack of explicit labeling and separation of assumptions and conditions hinders the readability and accessibility of the results, especially for readers who are not deeply familiar with the specific problem setting.

### Questions
## Questions
1. Am I correct, that by "interpolated regime" you mean that noise variance is zero and we have determenistic case?
1. Figures 8 and 9. In first figure you have orange color for your method, in the second - blue. This is confusing, please, fix the order of the plots in all the figures for consistency. Also in Figure 8 you do not use the name of your particular algorithm. Please also check, that these issues are fixed for all other figures.
1. Lines 382-383. What do you mean by "saddle connection"?

## Suggestions
1. Please, add explicit assumptions in the text about interpolation and smoothness etc., that you use in the theorems in some section like "Preliminaries". Sometimes it is hard to follow, whether you mean interpolation or bounded variance and it is hard to find them in the text.
1. Please, increase font size in the figures.

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
3

### Summary
This paper extends the recently developed Stochastic Polyak Stepsize (SPS) to incorporate the Pokyak momentum. In particular, the paper analyzes three SPS variants, vanilla SPS, DesSPS, and AdaSPS, and gets convergence guarantee for their momentum variants: MomSPS, MomDesSPS, and MomAdaSPS. Extensive numerical experiments demonstrate the practical performance of the proposed methods.

### Strengths
The paper is well-written and solid, with details and intuitions clearly explained to the readers. Moreover, extensive experiments validate the practical performance of the proposed stepsizes.

### Weaknesses
Although the paper is a solid work, my foremost concern is its limited technical novelty.

1. Limited technical contributions

   SPS [1], DesSPS [2], and AdaSPS [3] considered in this paper are already present in the literature, and the contribution of the paper only lies in showing the feasibility of incorporating momentum into these existing stepsizes. While the extension to momentum is not trivial, the core algorithmic ideas remain largely unchanged from the original SPS variants. The analysis, while technically sound, primarily adapts existing proof techniques to the momentum setting, lacking significant conceptual breakthroughs.

2. Strong assumptions

   The analysis of MomSPS imposes a constraint on $\beta$, and the analysis of two other stepsizes needs bounded iterates. Although the authors claim these are standard assumptions, they do not usually appear in the literature for SHB methods. The bounded iterates assumption, in particular, is quite restrictive and limits the practical applicability of the theoretical results. Specifically, the convergence guarantees are only valid within a bounded region of the parameter space, which may not always be the case in real-world scenarios. The constraint on $\beta$ for MomSPS also raises concerns about the robustness of the method, as it might require careful tuning of this parameter to ensure convergence.

### Questions
**Questions**

1. The comparison after Corollary 3.4 looks unclear to me. In particular, the results in [6] can achieve $O(1/\sqrt{K})$ convergence in the presence of noise by taking $\alpha =O( 1/\sqrt{K})$ (Theorem 1, [6]) , while SPS cannot achieve exact convergence. Could you elaborate more on this comparison?
2. Momentum in stochastic optimization is often shown to achieve certain variance reduction effects [4, 5]. Do you think this can help improve dependence on $\sigma^2$ in the convergence analysis of MomSPS?

**Minor issues**

1. Line 55

   has efficiently analyzed => has been efficiently analyzed.

2. Line 400, 410

   Please be consistent with step size and step-size.

3. Line 1098

   Definition C.2. Smoothness requires a two-sided bound $|f(x) - f(y) - \langle \nabla f(y), x- y\rangle | \leq \frac{L}{2}\\|x - y\\|^2 $. Concave functions without Lipschitz continuous gradient can satisfy the given one-sided bound.

**References**

[1] Nicolas Loizou, Sharan Vaswani, Issam Hadj Laradji, and Simon Lacoste-Julien. Stochastic polyak step-size for sgd: an adaptive learning rate for fast convergence. In *International Conference on Artificial Intelligence and Statistics*, pages 13061314. PMLR, 2021.

[2] Antonio Orvieto, Simon Lacoste-Julien, and Nicolas Loizou. Dynamics of sgd with stochastic polyak stepsizes: truly adaptive variants and convergence to exact solution. *Advances in Neural Information Pro- cessing Systems*, 35:2694326954, 2022.

[3] Xiaowen Jiang and Sebastian U Stich. Adaptive sgd with polyak stepsize and line-search: robust convergence and variance reduction. *Advances in Neural Information Processing Systems*, 36, 2024.

[4] Cutkosky, Ashok, and Francesco Orabona. Momentum-based variance reduction in non-convex sgd. *Advances in neural information processing systems* 32, 2019.

[5] Gao, Yuan, Anton Rodomanov, and Sebastian U. Stich. Non-Convex Stochastic Composite Optimization with Polyak Momentum. In *Forty-First International Conference on Machine Learning*, 2024.

[6] Liu, Yanli, Yuan Gao, and Wotao Yin. An improved analysis of stochastic gradient descent with momentum. *Advances in Neural Information Processing Systems* 33, 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors introduce new step-size schedules which are inspired by stochastic Polyak step-size (SPS) for the Stochastic Heavy Ball (SHB) momentum optimization method. The authors present convergence rates for each of their step-size selections showing that SHB can converge to the true solution at a fast rate when interpolation is satisfied and converge to the minimizer adaptively when interpolation is not satisfied.

### Strengths
The paper effectively integrates SPS with SHB, an approach previously applied to SGD in the existing literature. The proposed methods are validated both theoretically and empirically by demonstrating their convergence rates and conducting relevant experiments.

### Weaknesses
Gaining understanding of SHB within SPS framework and establishing a convergence rate is a valuable contribution. However, identifying the specific settings or problem types where the proposed method is most effective would provide a more comprehensive and practical understanding of its applicability. Based on my current understanding of the methods, from a theoretical perspective, there does not appear to be a clear advantage for incorporating momentum within the SPS framework.

In the convex setting, the paper indicate that no momentum produce the best convergence rate (line 354), the convergence rate in Theorem 3.5 and Theorem 3.6 deteriorate when $\beta$ increases. Hence, within the SPS framework, which specific settings or problem types momentum should be employed instead of relying solely on SGD?

The assumption of bounded iterates in Section 3.2 constitutes a strong condition, which may not hold even for quadratics without additional constraints. In the absence of this assumption, is it possible to derive meaningful theoretical results for the MomDecSPS and MomAdaSPS methods?

### Questions
In the convex setting, the paper indicate that no momentum produce the best convergence rate (line 354), the convergence rate in Theorem 3.5 and Theorem 3.6 deteriorate when $\beta$ increases. Hence, within the SPS framework, which specific settings or problem types momentum should be employed instead of relying solely on SGD?

The assumption of bounded iterates in Section 3.2 constitutes a strong condition, which may not hold even for quadratics without additional constraints. In the absence of this assumption, is it possible to derive meaningful theoretical results for the MomDecSPS and MomAdaSPS methods?

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
3

### Summary
This paper studies stochastic Polyak step-size for SHB. Three step size selections are proposed and associated convergence guarantees are developed. Specifically, using the MomSPSmax stepsize, the SHB is proved to converge to a neighborhood of the solution, if the objective function is convex and smooth. Moreover, another two stepsizes, I.e., MomDecSPS and MomAdaSPS, are proposed for non-interpolated SHB, which guarantee that SHB iterates converging to the exact solution. Finally, numerical experiments are presented to show the effectiveness of the proposed methods.

### Strengths
1.The writing and exposition are clear.

2.The proposed methods are practical to implement and have theoretical improvements compared with existing works.

### Weaknesses
Most of techniques are from existing literature. The authors did not explain the difficulty of applying the Polyak step-size to SHB compared with the SGD. This makes the technique used in this paper look like a direct generalization of Loizou et al. (2021)

### Questions
None.

### Soundness
3

### Presentation
3

### Contribution
3
