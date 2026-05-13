# On the onset of memorization to generalization transition in diffusion  models

- Decision: Reject
- Scores: 1, 3, 5, 5, 3

## Abstract
As the training set size increases, diffusion models have been observed to transition from memorizing the training dataset to generalizing to and sampling from the underlying data distribution. To study this phenomenon more closely, here, we first present a mathematically principled definition of this transition: the model is said to be in the generalization regime if the generated distribution is closer to the sampling distribution compared to the probability distribution associated with a Gaussian kernel approximation to the training dataset. Then, we develop an analytically tractable diffusion model that features this transition when the training data is sampled from an isotropic Gaussian distribution. Our study reveals that this transition occurs when the distance between the generated and underlying sampling distribution begins to decrease rapidly with the addition of more training samples. This is to be contrasted with an alternative scenario, where the model's memorization performance degrades, but generalization performance doesn't improve. We also provide empirical evidence indicating that realistic diffusion models exhibit the same alignment of scales.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper examines the transition from memorization to generalization in diffusion models as the number of training points increases. The authors model the training distribution as a Gaussian-smoothed version of the empirical distribution and define two regimes: memorization and generalization. The model is considered to be in the memorization regime if the generated distribution is closer to the smoothed empirical distribution and in the generalization regime if it is closer to the true population distribution. The paper uses Gaussian data and a linear diffusion model to compute the distances between the generated distribution, the Gaussian-smoothed empirical distribution, and the population distribution. Numerical simulations show that the transition to generalization occurs when the number of training samples $n$ becomes proportional to the data dimensionality $d$.

### Strengths
The paper addresses an important and timely problem: understanding when and how diffusion models transition from generalizing to memorizing their training data. This issue has substantial theoretical and practical implications. Understanding these regimes is crucial for real-world applications, particularly in ensuring that generative models do not inadvertently memorize and reproduce training data, which can lead to issues such as privacy violations.

### Weaknesses
As acknowledged by the authors themselves, this work is still in "draft" form (L410). In particular, it falls significantly short of publication standards, especially for ICLR. Below, I outline several critical issues.

1.  **Circular argument:** The central argument of the paper is circular. It defines generalization as the scenario in which the generated distribution is closer to the population distribution than the (smoothed) empirical one and then claims that the transition occurs when generalization arises. This definition predetermines the outcome, as the transition is defined by the very condition it seeks to identify. The core issue is that the paper does not provide an independent measure of generalization, instead relying on a comparison to a smoothed empirical distribution, which is itself a construct. This approach does not allow for a genuine investigation of the memorization-generalization trade-off.

2.  **Questionable modeling choices:** The choice to model the empirical distribution of the training set as a Gaussian smoothing of the actual empirical distribution is motivated solely by the divergence of the KL metric when using the empirical measure. Metrics like the Wasserstein distance are well-suited for comparisons with empirical measures. Furthermore, the chosen kernel variance (linked to the mixing time of Gaussian distributed points) appears to be unjustified and inadequate. The authors provide no clear justification for this specific choice, and it appears to be arbitrarily set. This choice directly impacts the results, as it dictates how closely the smoothed empirical distribution resembles the true empirical distribution. Paradoxically, this choice minimizes the distance to the population distribution, contradicting the goal of accurately modeling the empirical distribution. The smoothing operation effectively pushes the empirical distribution towards the population distribution, making it easier for the generated distribution to appear closer to the population distribution, thus biasing the results.

3.  **Trivial statement:** Section 2.3 essentially states that the distribution of points at late times is Gaussian, which is an expected outcome by construction. This does not warrant in-depth analysis. The fact that the distribution converges to a Gaussian at late times is a direct consequence of the diffusion process and does not provide any insight into the memorization-generalization transition. This section does not contribute meaningfully to the core argument of the paper.

4.  **Linear model limitations:** The paper uses a linear diffusion model arguing that a linear score function is justified because the score of a Gaussian is linear and at late time the distribution is Gaussian. Such a model can only generate Gaussian distributions and trivially requires $d$ points (in $d$ dimensions) to match the population score (see also point 6 below). This score model is strongly constrained in its expressive power and provably cannot fit the training distribution (nor its Gaussian smoothing), whose score is a weighted Gaussian convolution of the score of the single training points. Thus, **this model cannot properly memorize the training points**, contrary to the paper's claims (note that this is just due to an inadequate definition of memorization which does not require the generated distribution to be close to the training one). In fact, Biroli et al. (2024) explicitly link memorization to short times, where the score approximation of the authors is off. The linear model is fundamentally incapable of capturing the complex structure of the training data, limiting the conclusions that can be drawn from its analysis.

5.  **Inconsistent results:** Indeed, when testing on non-linear diffusion models (see Fig. 4), the results are inconsistent. Notably, the supposed memorization-to-generalization transition is not supported by the authors' own metrics, as the probability that the generated distribution is closer to the population distribution remains high ($>0.8$), regardless of the number of training samples. This inconsistency undermines the validity of the proposed framework, as the transition is not consistently observed across different model types.

6.  **Inconsistent limits:** In the proportional regime, i.e., $n \simeq d$, or when $n \ll d$ – that the authors discuss from Sec. 3 – the results in Sec. 2 do not hold, as they require $n$ to grow exponentially with $d$. The analysis in Section 2 relies on assumptions that are not valid in the regimes explored later in the paper, leading to a disconnect between the theoretical analysis and the empirical results. This inconsistency raises concerns about the generalizability of the findings.

7.  **Practical application oversight:** The final comment of the paper on potential practical application is also problematic and too naive, as it does not take into account the quality of generations, which is crucial in practical scenarios. The paper focuses solely on the distance between distributions, neglecting the perceptual quality of the generated samples, which is a critical aspect in real-world applications. A model might be close to the population distribution in terms of a metric, but still produce poor quality samples.

8.  **Neglect of the number of parameters:** The study fails to address how the degree of overparameterization influences memorization behavior, despite its known importance (e.g., Yoon et al., 2023). Instead, the focus on an overly simplistic linear model, which inherently lacks the capacity to memorize, overlooks this essential aspect. The number of parameters in the model is a crucial factor in determining its capacity to memorize the training data, and the paper's failure to address this is a significant oversight.

9.  **Superfluous equations:** The paper contains a significant amount of math (see, e.g., Eq. (21)) which is not well explained or linked to the empirical findings. Many equations are presented without clear motivation or connection to the experimental results, making it difficult to understand their relevance and impact.

10. **Figures:** The figures lack essential labels and color codes, making them difficult to interpret. Error bars or standard deviations are missing, and the use of linear scales (instead of log scales) is inadequate for illustrating trends. The Hellinger distance in Figure 2(b) decreases by only 0.02, which is insufficiently significant to justify the conclusions. The lack of clear labels and error bars makes it difficult to assess the statistical significance of the results. The use of linear scales obscures the trends, especially when dealing with quantities that vary over several orders of magnitude.

11. **Writing quality:** The writing is weak, with numerous grammatical errors and poorly constructed sentences.

### Questions
None.

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work analyzes into how diffusion models transition from replicating training data to generalizing from the learned data distributions. This transition is mathematically characterized as the point where the ETG (Error Training to Generated) is less than the EOG (Error Original to Generated). This is a sensible a new novel view of generalization, and the paper provides some analysis based on linear diffusion models.

### Strengths
This work considers an important problem of analyzing the conditions that allow a diffusion model to generalize beyond memorizing the training data.

### Weaknesses
The analysis of this work is limited to linear diffusion models, and there is almost no experimental validation justifying the relevance of the linear toy model with respect to the practical deep learning setups. While the paper introduces the ETG and EOG metrics, the analysis is confined to a very narrow setting, making it difficult to assess the practical implications of the theoretical results. The theoretical analysis also does not feel sufficiently surprising and novel enough to warrant a publication at ICLR. The core idea of comparing errors on training data versus generated data, while sensible, does not lead to any particularly deep or unexpected conclusions within the linear model framework. There is not much in the paper, so there is perhaps not much to criticize. In my view, the magnitude of the contribution is clearly below the publication expectation of ICLR.

### Questions
.

### Soundness
4

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper investigates the transition from memorization to generalization in diffusion models as the training set size increases. It defines this transition mathematically with a Gaussian kernel approximation to the training dataset. The study demonstrates a sharp transition in generalization performance when the training set size equals the input dimension for the data from an isotropic Gaussian distribution. Empirical evidence indicates that this phenomenon holds for real diffusion models, where training scale influences memorization and generalization behavior.

### Strengths
The paper provides a rigorous analysis to distinguish memorization and generalization regimes in diffusion models, particularly under the assumption of Gaussian-distributed training data.
It observes a distinct transition point when the number of training samples equals the input dimension, which is a compelling theoretical finding that may inspire further study in model behavior with scaling datasets.

### Weaknesses
1. The analysis is based on simplified assumptions (Gaussian-distributed data and the SDE process), and the finding may relate more to concepts around mixing time rather than specific diffusion model behavior, a bit hard to translate to more complex, real-world data or standard loss functions like score-function matching. The reliance on isotropic Gaussian data significantly limits the applicability of the theoretical results. The analysis does not account for the complex, high-dimensional structure present in real-world datasets, where data often lie on low-dimensional manifolds. Furthermore, the use of a simplified SDE process may not fully capture the intricacies of practical diffusion model training, which often involves more complex noise schedules and architectures. The connection to mixing time, while potentially relevant, is not thoroughly explored, and it's unclear how this relates to the observed memorization-generalization transition in the context of diffusion models.

2. The conclusion may be misleading, for example, the transition point is only related with the input dimension. However, people observe memorization when the dataset size is several order larger than the input dimension (the input image dimension would be ~1e5,  the dataset size 1e7 for imagenet). Moreover, how is the transition related to the data complexity, like facial data is much simpler than the natural images? The paper's claim that the transition point is solely determined by the input dimension is not well-supported by empirical evidence from real-world datasets. The observation that memorization occurs at dataset sizes far exceeding the input dimension in practical scenarios, such as training on ImageNet, directly contradicts the paper's findings. The analysis also fails to consider the impact of data complexity on the transition point. For instance, the transition point for simpler datasets like facial images might differ significantly from that of more complex datasets like natural images, a factor not accounted for in the current theoretical framework.

3. Notation not explained: $x.\nabla$, $\langle y \rangle_{\pi_t}$, $\langle y_i y_j \rangle_{\pi_t}$, etc.

### Questions
There is ambiguity about whether the transition observed is dependent on the input dimension or the intrinsic dimensionality of the data, which may impact the generality of the conclusions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper examines the transition from memorization to generalization in diffusion models as the training set size increases. The authors introduce a novel mathematical framework to define and study this transition, identifying when diffusion models stop merely replicating training data and begin to produce novel outputs that resemble the underlying data distribution. Key contributions include a new metric for measuring the transition and empirical evidence that supports the theory in realistic diffusion models.

### Strengths
The paper's originality is evident in its novel approach to defining and measuring the memorization-to-generalization transition. The writing is clear. This work has the potential to influence future research directions and practices in training diffusion models, especially regarding the phase transition from memorization to generalization.

### Weaknesses
1. The assumption of isotropic Gaussian distribution seems too strong. The gap between the real-world data and this assumption is notable.
2. More experimental details could be provided to explain the empirical results (more elaborated figures etc.).

3. Figure 4 looks confusing to me. From the left figure, it seems that E_{TG} and E_{OG} are both decreasing at a similar rate, without crossing each other, which is quite different from the illustrated figure in Figure 1(c). How does it make the transition from memorization to generalization?

### Questions
**1.** The figures could be better. For example, labels could be added to Figure 3 to clearly describe what the blue and red curve means respectively.

**2.** Figure 4 looks confusing to me. From the left figure, it seems that E_{TG} and E_{OG} are both decreasing at a similar rate, without crossing each other, which is quite different from the illustrated figure in Figure 1(c). How does it make the transition from memorization to generalization?

**3.** Could the assumption of isotropic Gaussian be loosened to non-isotropic Gaussian, or be generalized to Gaussian mixture? It seems that the current assumption is too strong that it has a notable gap from practice.

**4.** Is there a way people can quantify the time of transition in practice based on your analysis? For example, can these metrics of error be well-estimated asymptotically or non-asymptotically?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the memorization-to-generalization transition of a linear diffusion model in the case where the underlying distribution is Gaussian. They provide quantitative analysis of sample complexity (train set size) threshold for which the model-generated distribution from the linear diffusion model for Gaussian distribution starts to become closer to the underlying distribution than the train set distribution.

### Strengths
The authors provide a solid statistics-based discussion on the Gaussian data & linear diffusion model scenario.

### Weaknesses
My main concern is that the paper lacks a key result or message that (at least potentially) has meaningful implications on large-scale diffusion model training. Another problem is that the paper's presentation is sloppy in many aspects and makes the paper unnecessarily difficult to read through. To me, this paper seems to require a lot of development and re-organization to be ready for publication.

1. One of the main contributions that the authors claim is to identify the pattern of transition from memorization to generalization. However, while this heavily relies on the properties of data distribution, their theoretical analysis only considers the Gaussian distribution. It is entirely unclear whether the same pattern would be observed from real datasets. For example, in the abstract the authors say "This is to be contrasted with an alternative scenario, where the model's memorization performance degrades, but generalization performance doesn't improve.", but I think such regime can be found with real datasets (see, e.g., [1]).

2. A similar, additional weakness emerges from assuming the linear diffusion model, where the sampling procedure does not take into account the numerical discretization procedure of SDE/ODE, which is the central component of score-based generative modeling. They do provide a simple experiment using more realistic architecture and sampling procedure, but it does not necessarily indicate that the paper's finding applies to the nonlinear sampling procedure because the underlying data distribution is isotropic Gaussian (in this case, all levels of noised distributions are Gaussian and the corresponding score functions linear. Therefore, linear and nonlinear sampling procedures do not seem fundamentally different, if not identical).

3. The observation that rapid decrease in $E_{OG}$ is aligned with generalization seems like a direct implication of definition, and is not surprising. Why is this an interesting finding?

- In page 3, line 150, the authors write "Suppose we know ... $\rho(0,x)$ exactly." and then describe the score-based sampling procedure. However, the presentation is misleading because knowing $\rho(0,x)$ exactly does not necessarily enable the score-based (diffusion model) sampling. It rather requires the knowledge of $\rho(T,x)$ and the score functions $s(t,x)$.
- In page 4, line 174, the authors write "original distribution $\rho_O(x)$ inferred from $N \gg n$ samples". What does this mean? While they seem to use the notation $N$ for the first time here, it is not even properly defined, and it is unclear what $\rho_O$ precisely is and why it should be distinguished with $\rho$.
- The authors do not explicitly state that the samples $x_k$ belong to $\mathbb{R}^d$, which will confuse the readers.
- In page 4, line 196, I do not understand what the limit $n \to \infty$ with $\alpha = \log n / d$ fixed means. Here they are considering the limits of $Z_1$ and $Z_{1^c}$, which rely on $x_1 \in \mathbb{R}^d$. Then, does it make sense to take the limit while $d$ is changing?
- In line 197, what does $Z_{1^c} = e^{-d/2}/n$ mean? Isn't the left hand side dependent on $x$? Is $\mathcal{O}$ missing?
- What is the precise meaning of $\approx$ symbol in equation (10)?
- What does the notation $\mathcal{O}(\cdot, \cdot)$ in equation (11) mean?
- In page 5, equation (14), $y_i, y_j$ appears suddenly. Are they the train set samples? If so, they should have been specified earlier. It is very confusing because in the previous page, the train samples were denoted as $x_k$.
- In page 6, the meaning of lines 298-301 is unclear.
- In page 7, line 337-338, the definition "The diffusion model is considered to be memorizing the training data when the probability that $\Delta > 0$ ..." is confusing. The diffusion model already relies on the train data, but the probability is with respect to the randomness in train data. It does not make sense to discuss the memorization of an individual diffusion model in this way. I think this should rather be the property of the _dataset_, not the _model_.

### Questions
- In page 3, line 150, the authors write "Suppose we know ... $\rho(0,x)$ exactly." and then describe the score-based sampling procedure. However, the presentation is misleading because knowing $\rho(0,x)$ exactly does not necessarily enable the score-based (diffusion model) sampling. It rather requires the knowledge of $\rho(T,x)$ and the score functions $s(t,x)$.
- In page 4, line 174, the authors write "original distribution $\rho_O(x)$ inferred from $N \gg n$ samples". What does this mean? While they seem to use the notation $N$ for the first time here, it is not even properly defined, and it is unclear what $\rho_O$ precisely is and why it should be distinguished with $\rho$.
- The authors do not explicitly state that the samples $x_k$ belong to $\mathbb{R}^d$, which will confuse the readers.
- In page 4, line 196, I do not understand what the limit $n \to \infty$ with $\alpha = \log n / d$ fixed means. Here they are considering the limits of $Z_1$ and $Z_{1^c}$, which rely on $x_1 \in \mathbb{R}^d$. Then, does it make sense to take the limit while $d$ is changing?
- In line 197, what does $Z_{1^c} = e^{-d/2}/n$ mean? Isn't the left hand side dependent on $x$? Is $\mathcal{O}$ missing?
- What is the precise meaning of $\approx$ symbol in equation (10)?
- What does the notation $\mathcal{O}(\cdot, \cdot)$ in equation (11) mean?
- In page 5, equation (14), $y_i, y_j$ appears suddenly. Are they the train set samples? If so, they should have been specified earlier. It is very confusing because in the previous page, the train samples were denoted as $x_k$.
- In page 6, the meaning of lines 298-301 is unclear.
- In page 7, line 337-338, the definition "The diffusion model is considered to be memorizing the training data when the probability that $\Delta > 0$ ..." is confusing. The diffusion model already relies on the train data, but the probability is with respect to the randomness in train data. It does not make sense to discuss the memorization of an individual diffusion model in this way. I think this should rather be the property of the _dataset_, not the _model_.

### Soundness
2

### Presentation
1

### Contribution
1
