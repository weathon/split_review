# Convergence-Aware Multi-Fidelity Bayesian Optimization

- Decision: Reject
- Scores: 3, 6, 8, 8

## Abstract
Multi-fidelity Bayesian Optimization (MFBO) has emerged as a powerful approach for optimizing expensive black-box functions by leveraging evaluations at different fidelity levels.
However, existing MFBO methods often overlook the convergence behavior of the objective function as fidelity increases, leading to inefficient exploration and suboptimal performance. 
We propose CAMO, a novel Convergence-Aware Multi-fidelity Optimization framework based on Fidelity Differential Equations (FiDEs). 
CAMO explicitly captures the convergence behavior of the objective function, enabling more efficient optimization. We introduce two tractable forms of CAMO: an integral Automatic Relevance Determination (ARD) kernel and a data-driven Deep Kernel. Theoretical analysis demonstrates that CAMO with the integral ARD kernel achieves a tighter regret bound compared to state-of-the-art methods. Our empirical evaluation on synthetic benchmarks and real-world engineering design problems shows that CAMO consistently outperforms existing MFBO algorithms in optimization efficiency and solution quality, with up to 4x improvement in optimal solution.
This work establishes a foundation for tractable convergence-aware MFBO and opens up new avenues for research in this area.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
- The paper introduces CAMO, a Convergence-Aware Multi-fidelity Optimization framework leveraging Fidelity Differential Equations for optimizing expensive black-box functions. 
- CAMO addresses the often-overlooked convergence behavior of the objective function as fidelity increases, leading to more efficient exploration.
- The framework presents two kernel forms: an integral Automatic Relevance Determination kernel and a data-driven Deep Kernel.
- Theoretical analysis shows that CAMO with the integral Automatic Relevance Determination kernel achieves a tighter regret bound than current state-of-the-art MFBO methods.
- Empirical results indicate that CAMO consistently surpasses existing MFBO algorithms on benchmark functions and real-world problems.

### Strengths
- The proposed CAMO framework is aware of convergence, which is practically useful for real-world optimization problems.
- This work provides both theoretical and empirical results.

### Weaknesses
- The novelty of the proposed kernels is limited -- they are widely used in the context of Bayesian optimization.
- I can't agree with the multi-fidelity formulation; please see the Questions textbox.
- Some experimental details are missing; please see the Questions textbox.

### Questions
- I don't think that a fidelity level should be input to an objective function.  It cannot be an input variable to optimize.
- I can't agree with this sentence "The goal is to find the optimal solution ... while minimizing the total cost of evaluations."  From my understanding, $f(x, T)$ is not a (noiseless) ground-truth function.  Specifically, it also has an error with $T$ fidelity level.
- In Line 216, "random Fourier features" should be "the inner product of two random Fourier features"?
- For Figure 1, what is the function values?  Colorbars seem not correct; their values are zeros.
- In the caption of Figure 1, "high fidelity are" should be "high fidelity is" or "high fidelity levels are."
- 5 repetitions of experiments are too small.  Thus, many error bars are overlapped, which means they are not statistically meaningful much.
- I think that all experimental results for a particular benchmark should be started from the same simple regret if you provided the same random seeds.  They are significantly different.
- Please use \citep and \citet appropriately.

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
4

### Summary
This paper describes a new multi-fidelity BO (MFBO) framework called CAMO, which focuses on facilitating the convergence of the fidelity parameter. The key contributions of CAMO are two convergence-aware surrogates, including GP with an integral ARD kernel that facilitates linear FiDE, and deep kernel GP that approximates this condition. Both of these surrogates go well with prior MFBO objectives such as BOCA, cfKG, MF-EI, etc. Empirical results show synergy of CAMO with all these objectives. The paper also provides theoretical analysis of simple regret of BOCA using a GP surrogate with integral ARD kernel.

### Strengths
This paper provides a fresh take on the MFBO problem. I like that both the motivation and the solution are quite straight-forward, but fully backed up by theoretical justification & empirical results.

### Weaknesses
- In Fig. 2, several experiments were cut off before convergence. Could the authors provide regret up to 300 iterations to make sure? 
- How was the DKL trained to approximate Eq. (6)? Out of fairness, could the authors add a DKL-BOCA baseline where BOCA is given a DKL surrogate that was not trained to approximate Eq. (6)? Seems like the CAMO-DKL-BOCA variant achieves the best performance in most cases, so we probably want to make sure that this performance comes from CAMO, not DKL.
 
Some minor issues:
- Shaded confidence interval is quite hard to read. Red/orange curves with similar marker shapes are also not very color-blindness friendly. Not that I mind these issues, these are just suggestions to improve visual clarity of the paper.
- In Fig. 5, shouldn't SMAC3 query time (0.01) be at the 10^{-2} mark instead? Is this some rounding issue?
- I notice that the BOCA regret bound has a different second term that what was quoted in this paper. Specifically, the 2nd term is given by \sqrt{\Psi_{n^{\alpha}_{\Lambda}} (\mathcal{X})} / n^{2-\alpha}_{\Lambda} in the original text, whereas in this paper it is \sqrt{\Psi_{n_{\Lambda}} (\mathcal{X})} / n^{1-\alpha}_{\Lambda}. Probably won't affect the correctness of the proof, but should be fixed if it is a typo.

### Questions
Please see above

### Soundness
4

### Presentation
4

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
The authors concoct a methodology for multi-fidelity approximation appropriate for settings where the black-box converges to some "correct" value as the fidelity parameter is increased. They propose a kernel which implements this prior knowledge, investigate its impact on regret bounds, and illustrate the methodology on numerical experiments.

### Strengths
---

1) Clear presentation:
    i) Related work informatively and efficiently summarized.
    ii) logical layout
   iii) I think figure 1 does a great job illustrating the inductive bias of your new proposed kernel.

---

2) Comprehensive evaluation of methodology:
The authors provide numerical experiments on various synthetic and realistic case studies as well as a regret bound analysis.

---

3) Expansive numerical simulation settings:
Consideration of execution time is important, and though there is overhead to using the proposed method, it is on the same order of magnitude as BOCA.

### Weaknesses
---
Insufficient number of repetitions for the experiments.

The variance in performance of Bayesian optimization methods is far too great to use only 5 repetitions for the numerical experiments.
Considerably more would be required to be sure; on the order of 50 would be ideal. If this is not computationally feasible, there at least needs to be an improvement in the way the uncertainty is presented in the results. 


---
Figures difficult to read; let's use Figure 2 as a case study:

    i) some points are lying on top of each other; in particular on the top right function.

    ii) It's probably worth adding the name of the function to the title of the subplots; at the very least you need to tell us what order you are listing the functions in in the legend.

    iii) It's not obvious to me what the shaded regions indicate; perhaps standard deviation, but only of certain methods? Probably worth spelling out.



--- Some grammar/spelling/formatting issues I noticed (did not affect score; here only for your convenience):
Page 3 line 140: "NueralODE".

Line 202 "Given GP priors" repeated.

There are bad spaces following the "Park" function in several places; (Figure 2 caption, line 372).

### Questions
If the upper fidelity limit is not infinite, why do we expect it to converge? You say that convergence is particularly important when T is infinite (at the beginning of Section 4), but isn't it only the case that it's important then?


The setting of Kandasamy et al 2017, is such that there is a "true" function f which we wish to optimize. When you say that you use their acquisition function in section 4.4, what how do you proceed exactly? If I am reading them correctly, Kandasamy et al use the UCB evaluated at the true f. What do you use instead? f at the highest fidelity level?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose a novel multi-fidelity Bayesian optimization algorithm that, unlike prior work, incorporates the convergence behavior of models at different fidelity levels. By leveraging this convergence information, the algorithm reduces regret by minimizing unnecessary exploration of costly high-fidelity models, resulting in a more efficient optimization process.

### Strengths
- The paper is very well-written and accessible, even for readers unfamiliar with the topic, providing a clear and informative introduction to convergence-aware multi-fidelity optimization.

- The authors offer rigorous proofs for their propositions, lending strong theoretical support to their approach and demonstrating a well-established mathematical foundation.

- The paper includes thorough empirical evaluations, tested on standard benchmarks and extended to complex real-world applications, such as mechanical plate vibration and thermal conductor design, showcasing the model's practical value and robustness across diverse scenarios.

### Weaknesses
- A limitation section is needed.
- The authors mention that the benefits of using multi-fidelity approaches become significant when the cost increases more than linearly, noting that this is often the case. However, further explanation or references are needed to substantiate this claim.
- While the proposed method reduces regret by selecting sample points and fidelity levels more intelligently, it would be helpful to address any additional computational overhead introduced by these adjustments. Comparing the computational load of this approach with vanilla Bayesian Optimization or traditional MFBOs would clarify whether CAMO is less suited for certain tasks with strict runtime constraints.

- It seems that the implementation is not publically availabel.

Minor issues:
- in line 46: As the fidelity goes toward infinity, the number of the elements becomes **large**, and the time steps become **small**.
- in line 203: 'given GP priors' is repeated.

### Questions
- In Figure 7 why is the green plot (SMAC3) early stopped in the plots for regret-time? From the plot, it looks like if SMAC3 had given enough clock time could perform better and this suggests that there is extra overhead computation time for CAMO algorithm, is this true? 
- Are there any implementation challenge in comparison to the counterpart methods?

### Soundness
4

### Presentation
4

### Contribution
3
