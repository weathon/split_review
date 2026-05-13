# Analyzing Neural Scaling Laws in Two-Layer Networks with Power-Law Data Spectra

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Neural scaling laws describe how the performance of deep neural networks scales with key factors such as training data size, model complexity, and training time, often following power-law behaviors over multiple orders of magnitude. Despite their empirical observation, the theoretical understanding of these scaling laws remains limited.  In this work, we employ techniques from statistical mechanics to analyze one-pass stochastic gradient descent within a student-teacher framework, where both the student and teacher are two-layer neural networks. Our study primarily focuses on the generalization error and its behavior in response to data covariance matrices that exhibit power-law spectra. 
For linear activation functions, we derive analytical expressions for the generalization error, exploring different learning regimes and identifying conditions under which power-law scaling emerges. Additionally, we extend our analysis to non-linear activation functions in the feature learning regime, investigating how power-law spectra in the data covariance matrix impact learning dynamics. Importantly, we find that the length of the symmetric plateau depends on the number of distinct eigenvalues of the data covariance matrix and the number of hidden units, demonstrating how these plateaus behave under various configurations. In addition, our results reveal a transition from exponential to power-law convergence in the specialized phase when the data covariance matrix possesses a power-law spectrum. This work contributes to the theoretical understanding of neural scaling laws and provides insights into optimizing learning performance in practical scenarios involving complex data structures.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the learning dynamics of committee machines trained on random data with power law covariance structure. They utilize a hierarchy of order parameters which they can analytically close for linear activation functions. They obtain scaling laws with training observations $\alpha$ (also time for online learning) and model size $N$ when trained on spectra with $L$ distinct eigenvalues. The authors show a number of interesting effects including the disappearance of learning plateaus when $L$ increases and a transition from exponential convergence (for isotropic covariates) and power law convergence for large $L$. The authors demonstrate their derived theory is accurate for linear networks. They also examine the specialization transition from their hierarchy of ODEs and argue that the escape time scales inversely with $L$.

### Strengths
This paper studies an important problem, namely the theoretical origin of neural scaling laws, and studies this in nonlinear two layer committee machines. For linear activations, they can obtain very precise learning curves in terms of the spectrum. They obtain power law exponents for both training time $\alpha$ and number of student features $N$. For nonlinear networks, they predict escape times for the specialization transition in terms of $M,L$.

### Weaknesses
While the paper introduces a very promising approach of utilizing a hierarchy of order parameters to deal with power law structured covariates, most of the closed form theoretical predictions require restricting to the linear activation case. However, these results are also of interest. There are some remaining questions and issues, which if answered/addressed, could cause me to increase my score.

1. Are most power laws derived under the assumption of random teacher vectors $T$? Can analysis be performed for a fixed realization of the teacher $T$?
2.  In Figure 3, how is the CIFAR-5M plot made? Are the true target labels from the dataset used or is an artificial teacher network used? If the target is generated from a synthetic teacher in this Figure, do the authors think they can use their theory to predict the learning curves for the true labels?
3. Could some of the plots like Figure 6 be plotted on log-log scale to see that the power law exponent depends on $\beta$?
4. In the linear network case, does the committee machine *learn features*? The neural tangent kernel for the committee machine with linear activations would be constant over training. 
5. How sensitive are the solutions in the committee machine to the initialization of the student weights?

### Questions
1. Are most power laws derived under the assumption of random teacher vectors $T$? Can analysis be performed for a fixed realization of the teacher $T$?
2.  In Figure 3, how is the CIFAR-5M plot made? Are the true target labels from the dataset used or is an artificial teacher network used? If the target is generated from a synthetic teacher in this Figure, do the authors think they can use their theory to predict the learning curves for the true labels?
3. Could some of the plots like Figure 6 be plotted on log-log scale to see that the power law exponent depends on $\beta$?
4. In the linear network case, does the committee machine *learn features*? The neural tangent kernel for the committee machine with linear activations would be constant over training. 
5. How sensitive are the solutions in the committee machine to the initialization of the student weights?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors investigate neural scaling laws in a two-layer student-teacher network, where the data spectrum is generated to have L distinct eigenvalues following a power-law distribution. The authors use one-pass stochastic gradient descent with MSE loss. First, the authors derive analytical expressions for the generalization error in the case of a linear activation function and establish a condition for power-law scaling. Then, for non-linear activation functions, where plateaus may emerge, they derive expressions to predict both the height and width of these plateaus and investigate the asymptotic solution. For large $L$ and the number of hidden units $M$, the width exhibits an elegant scaling law of $\sim M^{2}/L$

### Strengths
The paper is well-written overall. The arguments are well-founded, the text is concise and clear, and the authors skillfully focus on essential points in the main text, leaving detailed calculations for the appendix. All of the derived analytical results are verified by numerical simulations. The contribution, particularly the investigation of the properties of the plateau, appears to be quite solid as well.

### Weaknesses
The main problem with the manuscript is that the setting is quite narrow - exact degeneracy of the covariance eigenvalue, 2nd layer neurons are all untrainable and *identical*, only one nonlinear activation tested, etc. It is not clear how robust these results are to to even slight variation of the setting. IMHO, This is the main point that would determine the impact of this work.

Clearly, it is very difficult to extend the analytical results beyond the setting described by the authors, but it would strengthen the manuscript considerably if the authors investigated numerically the robustness of their results. Since the networks are relatively small, this should be easy to do. Concretely, to what extent do the conclusions hold when:
  - $K\neq M$?
 - The weights of the 2nd layer are not identical?
- The covariance is only almost degenerate?
- Other (and more common) nonlinear activations are used?

(even a subset of these would be useful, but as I wrote above, the experiments are not challenging)

### Questions
- In Sec. 4.3 the authors model some learning behavior by training only $N_{l}$ of the student vector. Could the authors clarify the intended learning behavior they are simulating? Specifically, what motivates the use of $N_l$ in this context? Could you clarify the content of the statement "each entry of the student
vector directly corresponds to an eigenvalue"? This should be clear to the reader without referring to the appendices.

- Fig. 5: To enable a quantitative comparison with the derived expressions, could the authors include the width of the plateau (Eqs. (12) and (15)) in the figure?

- Can the authors give more intuition about the underlying cause for the existence of the plateau, and for the scaling law of the escape time? It is a bit hard to infer it from the analytical derivation, and a heuristic/intuitive/hand-wavy explanation for this it would be helpful.

- There is a bit of missing discussion regarding the generalization of the results. Are they specific to this particular setup, or do we expect some of these results to apply in other scenarios? For instance, how would the findings change i?

- Line 209: To avoid confusion, consider renaming $\alpha=p/N$, since it is already used as the time in the rest of the paper.

- Around line 222: Have the authors mistaken the minimal polynomial with the characteristic polynomial?

### Soundness
4

### Presentation
4

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
The authors analyze the dynamics of learning a two-layer neural network with single-pass SGD, in the limit of large data dimension, for data with a power-law covariance spectrum. For linear regression, they derive an expression for the rate of decay of the error with time, which matches previous results in the literature in related settings. In non-linear cases, they analytically determine the length of the plateau in the learning dynamics, and in particular how it depends on the number of distinct eigenvalues in the spectrum.

### Strengths
The paper is very well written, results are clearly exposed and connected to related works. Abundant and clear numerical experiments are provided to support the main results.

The question explored is interesting. To the best of my reading, the main technical contributions are
- Establishing the rate of decay of linear regression for one-pass SGD, which happens to match previous full-batch results, e.g. Bordelon and Pehlevan (2022), Bahri et al (2024). The model and training are much simpler than in those papers, but I believe this particular case has not yet been covered in the literature, although I am not completely familiar with it.
- Generalizing the escape time analysis of Biehl (1996) to structured data, again to the best of my understanding of the literature. In particular, the result that the length of the plateau decreases with the number of eigenvalues is an interesting one.

I have a number of concerns, which I detail in the following sections. Overall, I think the paper is sound, although I have not checked the derivations in detail, and am overall in favor of acceptance if my concerns are addressed by the authors.

### Weaknesses
I have a number of observations and questions. I regroup my main concerns in this section, and leave the more minor points for the next.

- l.191 I have strong doubts about this statement. I believe preactivations are always Gaussian, as linear combination of the Gaussian inputs. The Gaussian Equivalence principle is needed when discussing the post-activations. Please correct me if I'm wrong.

- l. 417. Is a $l$ missing somewhere, why does the variance not depend on it ? Furthermore, it seems to me the variance scales as $1/N$, which does imply self-averaging. I do not understand the author's claim that higher-order overlaps do not self-average, which is linked to the result that $M$ distinct plateaus are present for the dynamics of e.g. the $R$ overlap. Further clarification would be very helpful.

### Questions
- l.190 Is a squareroot missing, i.e. should it be $\xi^\mu (\sigma)^{l/2}J_i$ ? It does not seem consistent with l. 194 otherwise.

- l.223 Shouldn't each term in parenthesis in the characteristic polynomial be to the power $N/L$ ? I might be missing something, further clarification would be helpful.

Minor comments and recommendation.

- Plotting the predicted slope for the power law (l.314) and the associated window of validity in Fig. 2 (right) would be a very compelling illustration of the theory.

- I believe the scaling of $\tau_{esc}\sim M^2/L$  to be one of the most interesting results of the work. I would be curious to see a plot where the escape time is experimentally measured, alongside this predicted rate, to illustrate and support this finding, but this is just a recommendation.

- In the continuation of the last point, could the authors provide more intuition why the length of the plateau decreases (increases) with $L$ ($M$)?

### Soundness
3

### Presentation
3

### Contribution
2
