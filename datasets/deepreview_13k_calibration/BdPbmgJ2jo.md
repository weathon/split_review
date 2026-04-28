# High-dimensional Asymptotics of VAEs: Threshold of Posterior Collapse and Dataset-Size Dependence of Rate-Distortion Curve

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 8, 6, 3

## Abstract
In variational autoencoders (VAEs), the variational posterior often aligns closely with the prior, known as posterior collapse, which leads to poor representation learning quality. An adjustable hyperparameter beta has been introduced in VAE to address this issue. This study sharply evaluates the conditions under which the posterior collapse occurs with respect to beta and dataset size by analyzing a minimal VAE in a high-dimensional limit. Additionally, this setting enables the evaluation of the rate-distortion curve in the VAE. This result shows that, unlike typical regularization parameters, VAEs face "inevitable posterior collapse" beyond a certain beta threshold, regardless of dataset size. The dataset-size dependence of the derived rate-distortion curve also suggests that relatively large datasets are required to achieve a rate-distortion curve with high rates. These results robustly explain generalization behavior across various real datasets with highly non-linear VAEs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the RD curves in VAEs from a function of dataset size and dimensionality. The authors suggest that the RD curves as a function of data complexity $\alpha$ (# data points / dim of data) and $$\beta, can be divided to three categories of overfitting, learning, and underfitting; In high $\alpha$ regime, smaller $\beta$ is needed in order to avoid over-regularizing the model.

### Strengths
- To the best of my knowledge, this is the first paper that studied RD curves in VAEs as a function of dataset size and data dimensions. This topic I think is a valuable topic of study and will indeed be of interest to the ICLR community. 

- The theory in the paper, to the best of my understanding, is sound. 

- The paper for the most reads well.

### Weaknesses
 - There is no study of the network capacity in this work. While I understand that this is theoretical work, the authors do make a claim that the same results hold for more complex networks. However, there are prior works that suggest that RD curves for different network capacities behave differently [1,2]. Could the authors comment on this? Specifically, the paper does not address how the depth and width of the encoder and decoder networks would impact the observed rate-distortion trade-offs. This is a critical omission, as the capacity of these networks directly influences their ability to learn complex data distributions and thus the shape of the RD curve.

- It is also not clear to me what is the message of the paper. It ofcourse makes sense that when you don't have a lotta data in high dimensions, you want to incorporate prior knowledge (such as regularization). Similarly,  when you have a lotta data, you don't need a lotta regularization as it is evident from all the recent DGMs. Furthermore, the $\alpha < 1$ is hardly interesting as it is almost never the case. So practically, what does this mean for people employing VAEs? What is the core message here? The paper lacks a clear articulation of how the theoretical findings translate into actionable insights for practitioners. The practical implications of the derived relationships between data complexity, regularization, and RD curves remain unclear, limiting the paper's impact.

- I do not think the experiments are strong enough to back the claims made in this paper. First, $\alpha$ should have been studied as a function of both $n$ and $d$ separately. Here, $d$ was kept fixed. Furthermore, the data choice here is extremely specific. I understand the design choice, but some controlled experiments on real-world datasets are also necessary before showing Figure 3 left with those specific values. The experimental setup needs to be more robust. The analysis should include variations in both the number of data points and the dimensionality of the data, rather than keeping one fixed. The reliance on a specific data distribution limits the generalizability of the findings.

### Questions
- Can you comment on how much the analysis is effected by the fact that $D$ is fixed?
- Are the RD curves computed for the training set or test set? These two curves can be widely different.  
- Do the authors mean overfitting by "overlearning"? If yes, I would say replace it with overfitting to avoid confusion :) 
- this is not clear to me but how did the authors at the values for Figure 3 Left? This is not seem to match other figures.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates several aspects of beta-linear-VAEs, including posterior collapse, the effect of different values for the beta parameters, the effect of training dataset size.
It also introduced two summary statistics, and using these statistics, the authors derived a phase diagram for VAE learning in terms of the beta values and the relative scale of the training dataset size.

### Strengths
- The paper studied an important aspect of VAEs and how the different parameters and choices can affect the performance.
- The empirical findings of the relation between generalisation error and the sample complexity as well as the beta parameter is interesting.

### Weaknesses
The paper discussed a list of different behaviours of VAEs, but it feels like they are rather loosely connected findings (i.e., the subsections in Section 6).

The findings themselves are interesting, but it is not surprising that changing one variable, such as beta or the number of training data, will lead to various changes in aspects like RD curves, posterior collapse. 

Therefore, I believe a more coherent story is important to connect the dots and make these findings more insightful.

### Questions
1. The signal recovery error feels like a definition of reconstruction error, and a distortion metric. What’s the difference between the signal recovery error and the distortion (D) of the RD curve in the paper?
2. Typo: Page 8 line 397: “summary statics” -> “summary statistics”

### Soundness
3

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
4

### Summary
This paper aims to analyze the solution learnt by a $\beta$-VAE w.r.t. (1) the parameter $\beta$, and (2) the training dataset size. The authors work in the high-dimensional asymptotic setting, and aim to characterize certain phenomena about the quality of the learnt solution by the VAE.

To do this, the authors theoretically analyze a linear VAE model (Eq (5)), in the high-dimensional asymptotic regime where $n,d \rightarrow \infty$ and $\frac{n}{d} = \alpha$ (sample complexity) stays finite, using the replica method as a heuristic to get around intractable calculations. This is presented in Section 5.

The asymptotic formulae are empirically verified in Section 6.1 and 6.2, on a synthetic data model of the spiked covariance matrix (Eq (4)). This is then used to draw interesting observations about the learning process and the quality of the learnt VAE solution. Figure 2 in particular shows many of the findings.

The authors then empirically show some of the findings (from the linear VAE setting) hold true for non-linear VAEs also, trained on real-world datasets like MNIST and FashionMNIST. This is presented in Section 6.5.

### Strengths
**Technical strengths**:
- The paper sharply characterizes high-dimensional asymptotics for learning the linear VAE (Eq (5)) under the spiked covariance model (Eq (4)) with the regularized $\beta$-VAE objective (Eq (6)).
- This is used to show interesting observations about the VAE learning process in Section 6.1 and 6.2. In particular, (1) Figure 2 shows a double-descent phenomenon w.r.to the sample complexity $\alpha$, with the reconstruction error (Eq (9)) peaking at $\alpha = 1$, and (2) Figure 2 also shows a long plateau in the reconstruction error for large values of $\beta$. This is backed by Claim 6.1 (in the large $\alpha$ limit) and lines 428-430 provide concrete guidance to practitioners about the risks of a large $\beta$ when training.
- Section 6.5 (and Figure 5) shows this on real-world datasets MNIST and FashionMNIST also, where the insight can be used to practically choose the "optimal" value of $\beta$ approximately equal to the noise ratio $\hat{\eta}$, which can be estimated using the training dataset.

**Presentation strengths**:
- The paper is largely well-written and easy to follow. The authors include relevant explanations in most places. For example, the choice of the spiked covariance model as the synthetic data generating process was backed by evidence in Figure 1 of MNIST following something similar.

### Weaknesses
 **Technical Weaknesses**:
- The main weakness is the fact that the theoretical results are not exact, since they have been developed using the replica method, which is a heuristic to get around intractable calculations.
- The authors work in the simple setting of $k = k^\star = 1$. If I understand correctly, this means the true latent space is $1$-dimensional. It would have been nice to see the synthetic experiments with $k^\star$ varying, say in $[1, 2, 4]$. In particular, what would the trend of $\varepsilon_g$ w.r.to $k^\star$ look like? It is unclear if the observed double descent phenomenon and the plateau in reconstruction error for large $\beta$ would hold for higher dimensional latent spaces. The analysis is also limited by the assumption that the latent space dimension $k$ matches the true latent dimension $k^*$, which is a strong assumption that may not hold in practice.
- Some of the claims can be better substantiated. For example, in the context of Figure 2, it would have been nice to see a plot of $\varepsilon_g$ w.r.to $\alpha$ for the optimal $\beta$ choice. Is that perhaps monotonically decreasing? (This is similar to the double-descent observations in literature, where using the optimal parameter leads to a monotonically decreasing curve instead of double-descent).

**Minor notes on the typos I found**
- Line 146, $H$ is probably the "negative log-likelihood" instead of just "likelihood". I stress this because it is important whether we want to minimize or maximize $H$.
- Line 189, "Spectrum" of the covariance matrix, instead of "Spectral". This typo is present in many places throughout the paper (for eg, Fig 1(b)), would appreciate if it can be cleaned up.
- Line 214, "Note that" instead of "Noted that".
- Line 224, $\lambda \in \mathbb{R}_{+}$ maybe instead of  $\lambda \in \mathbb{R}$? I *assume* practitioners use a non-negative regularization parameter.

### Questions
- What is the main challenge that the replica method allows you to get around? Would be nice to provide some insight into this. Or perhaps a toy example of the usage of replica method demonstrating what are its benefits and why is it used in this particular context.
- What is the main reason to introduce the metric $\varepsilon_g$ in Eq (9)? How is it different than the distortion $D$?
- In Figure 3, what does "overlearning" mean? From the description in section 6.2, it seems it is the same as overfitting? If so, would be good to name it that way instead of introducing a new term.

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
5

### Summary
This paper explores the influence of the β hyperparameter in a β-VAE, particularly regarding its impact on the posterior collapse phenomenon and the Rate-Distortion (RD) curve, from an information-theoretic perspective. Using a Spiked Covariance Model (SCM), the authors identify three phases (regularized, learning, overlearning) based on β and sample complexity α = n/d . The results suggest that high values of β inevitably lead to posterior collapse, regardless of data volume, and propose that the optimal β correlates with noise
strength ˆη in high-complexity settings. Experiments on MNIST and Fashion-MNIST datasets partially validate these claims.

### Strengths
• Information-Theoretic Perspective: A thoughtful analysis of β-VAE’s Rate-Distortion properties.
• Insight on Hyperparameter Tuning: Suggests an optimal β based on sample complexity, a novel angle.
• Focus on an Underexplored Hyperparameter: Thorough analysis of β’s role in posterior collapse.

### Weaknesses
• Over-Simplified Model and Limited Scope: Most analysis centers on a linear VAE with low latent dimensions (e.g., dimension 1), which reduces the generalizability to real-world settings. Minimal insight into non-asymptotic or intermediate regimes. The focus on a single latent dimension, while simplifying analysis, neglects the complex interactions and dependencies that arise in higher-dimensional latent spaces, which are critical for capturing rich data representations. This simplification limits the applicability of the findings to practical scenarios where latent spaces are typically high-dimensional.
• Limited Novelty: The core claim that “high β is detrimental” is already known. While it validates an intuition, the work lacks a new method or paradigm. Moreover, it is unclear that the posterior collapse phenomenon occurs ”often” as stated in the abstract, especially when the latent dimension increases. The observation that high β values lead to posterior collapse is not novel and has been extensively discussed in prior literature. The paper does not introduce a new approach or technique to address this issue, nor does it provide a significantly deeper understanding of the underlying mechanisms beyond what is already known. The claim that posterior collapse is a frequent occurrence, particularly in higher latent dimensions, is not sufficiently supported by the analysis.
• Minimal Experiments: Only FID scores on two datasets (MNIST, Fashion-MNIST), without broader validation on diverse or complex data, and lacks sensitivity analysis (for small changes on the value). The experimental validation is limited to two relatively simple datasets, MNIST and Fashion-MNIST, which do not adequately represent the diversity and complexity of real-world data. The absence of experiments on more challenging datasets, such as those with high-dimensional inputs or complex dependencies, raises concerns about the generalizability of the findings. Furthermore, the lack of sensitivity analysis, which would examine the impact of small changes in the β hyperparameter, further limits the practical implications of the study.
• Identifiability of Ground Truth Model: As is, the ground truth model does not seem to be identifiable (it is when dividing by √θ). This hinders the reliability of the analysis. The lack of identifiability in the ground truth model introduces ambiguity in the parameter estimation process. The model's parameters cannot be uniquely determined from the data, which compromises the reliability and interpretability of the analysis. The scaling issue with √θ further complicates the model's interpretation and may lead to erroneous conclusions.

### Questions
1. Could you explore the performance of this model in transitional or non-asymptotic regimes to reflect real-world data scenarios?
2. Is your analysis still valid for datasets with complex spectrums?
3. Could you clarify the derivation in Equation (9), especially the expectation notation?

### Soundness
2

### Presentation
3

### Contribution
2
