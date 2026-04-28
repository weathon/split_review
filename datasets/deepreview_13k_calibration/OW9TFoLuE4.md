# Phase-Driven Domain Generalizable Learning For Nonstationary Time Series Classification

- Decision: Reject
- Avg Score: 3.80
- Scores: 5, 3, 3, 5, 3

## Abstract
Monitoring and recognizing patterns in continuous sensing data is crucial for many practical applications.
These real-world time-series data are often \emph{nonstationary}, characterized by varying statistical and spectral properties over time. This poses a significant challenge in developing learning models that can effectively generalize across different distributions. In this work, based on our observation that nonstationary statistics are intrinsically linked to the phase information, we propose a time-series learning framework, \method{}. It consists of three novel elements: 1) phase augmentation that diversifies non-stationarity while preserving discriminatory semantics, 2) separate feature encoding by viewing time-varying magnitude and phase as independent modalities, and 3) feature broadcasting by incorporating phase with a novel residual connection for inherent regularization to enhance distribution invariant learning. Upon extensive evaluation on 5 datasets from human activity recognition, sleep-stage classification, and gesture recognition against 10 state-of-the-art baseline methods, we demonstrate that \method{} consistently outperforms the best baselines by an average of 5\% and up to 13\% in some cases. Moreover, \method{}'s principles can be applied broadly to boost the generalization ability of existing time series classification models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a phase augmentation method to improve the robustness of the time-series prediction. The method is based on the Hilbert Transform, which does not change the magnitude response. Therefore, it is claimed that this augmentation can diversify the dataset while preserving discriminative features. Experiments are conducted on several datasets.

### Strengths
The domain generalization for time-series data is interesting. The experimental results verify the effectiveness of the proposed method. The organization is clear, although some details are not introduced clearly.

### Weaknesses
My primary concern/question is, why changing the phase would preserve discriminative features. The implicit assumption is that the response is mainly determined by its magnitude. But without introducing how y is generated, it looks confusing to say that phase augmentation preserves discriminative features. Specifically, the paper lacks a clear explanation of the relationship between the phase of a time-series signal and the underlying class labels. It's not immediately obvious why manipulating the phase, while keeping the magnitude constant, would not significantly alter the signal's semantic content, potentially leading to a loss of discriminative information. For instance, in many signal processing applications, phase carries crucial information about the timing and alignment of signal components, and arbitrary changes could disrupt these relationships. The paper should provide a more detailed justification for why the proposed phase augmentation is a valid approach for preserving discriminative features.

Besides, the model assumes piecewise constant distribution in Eq. (1). Is it able to relax this assumption? It seems that many previous methods do not assume this, e.g., Diversify. The assumption of piecewise constant distribution is quite restrictive and may not hold for many real-world time-series datasets, especially those with complex or rapidly changing dynamics. The paper should discuss the limitations of this assumption and its potential impact on the performance of the proposed method. Furthermore, it would be beneficial to explore alternative distributional assumptions or demonstrate the robustness of the method to deviations from this assumption. The choice of window size for the STFT, which directly relates to the piecewise constant assumption, needs more justification and analysis. How does the performance of the method vary with different window sizes, and what are the implications for different types of time series?

Third, the theoretical part seems redundant. Its connection to the method is weak. Removing this part also makes the method self-motivated.

### Questions
Have you compared your method with the Diversify method in the augmentation step?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This article describes a data augmentation procedure to create new time series using the magnitude and phase information of the short-term Fourier transform (STFT). The authors also propose to separately encode the magnitude and phase, and specific architecture ("phase residual feature broadcasting") to perform downstream tasks (such as classification).

### Strengths
The study of non-stationary time series is an important topic in real applications. The proposed approach is an interesting addition to the augmentation strategies that create new time series with similar dynamics.

### Weaknesses
There are many inaccuracies in the manuscript, making it difficult to follow.
- Many definitions and statements are not mathematically sound.
  * Equation 1: Left-hand size is a function, and right-hand side is a random variable.
  * Definition of HT: It should be HT(x)(t) and not HT(x(t)) unless the authors mean that HT operates on a real value.
  * $\mathbf{x}= \{ x_0,\dots,x_t,\dots \} \in\mathbb{R}$
  * Definition of $\mathcal{D}_{\bar{U}}$ in Theorem 2.5
- When doing the ADF test, the authors should provide the p-values instead of the raw statistics, which are not interpretable.
- In Definition 2.2, is there a connection between $S_{i} $ and $\mathcal{X}_{{S}}$?
- The definition of non-stationarity differs from what can be found in the literature. Usually, the definition of (2nd order or weak) stationarity is given, and non-stationary time series are time series that do not satisfy this definition.
- The authors introduce a beta divergence, which is not the usual one [1]. Furthermore, it does not satisfy the properties of a divergence. Also, Equation 9, on which the theoretical analysis relies, must be clearly stated (not all terms are defined).
- There needs to be more clarity between the claims and what the proposed methodology can achieve.
  * The authors claim that PHASER is designed for domain adaptation, but which proposed mechanism contributes to domain adaptation?
  * The augmentation strategy takes a non-stationary time series and returns another non-stationary time series. None of the methodology's other components are designed for non-stationary time series. The authors should be more specific about why the whole pipeline is adapted for non-stationary time series.
  * The feature broadcasting mechanism is described purely from an implementation standpoint. There should be a more intuitive explanation of what it does, with some evidence or relation to the literature.
- There is extensive literature on time series classification [2]. The choice of baselines needs to be more motivated as standard methods were excluded. Also, close to half of the baselines are from non-published articles.
- There are poorly formulated sentences which can be surprising for readers ("the joint distributions […] are similar but distinct.", "diversify non-stationarity," "DFT is applicable for signals that are stationary and periodic."

### Questions
See my comments in the section above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper presents a new network for nonstationary time series classification with domain generalization capabilities. The new network is based on a separate processing of the phase of the signal, which is extracted using the HT and employed in parallel to the processing of the magnitude of the signal. The advantages of the approach are demonstrated through experiments on several benchmarks.

### Strengths
- To the best of my knowledge, incorporating phase information in this manner for the purpose of time-series classification is new.
- The empirical evaluation is extensive, showing improvements over other methods across several benchmarks from different application domains.

### Weaknesses
 - The proposed approach, which adds phase information using the HT that in turn is processed in parallel with the signal's magnitude, is relatively simple. On its own, this may not be sufficient to justify publication in ICLR.
- The theoretical justification in Section 2.5 is unclear, and Theorem 2.6, in particular, is unconvincing. Numerous features of a signal, other than the phase, could exhibit changes in "nonstationary statistics”. Additionally, the term "nonstationary statistics" is used frequently throughout the paper but is not clearly defined.

### Questions
- I would like to ask the authors to clarify the meaning of their theoretical results, specifically a clearer explanation of Theorem 2.6 and a formal definition of "nonstationary statistics”.

### Soundness
2

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
The paper presents the PhASER (Phase-Augmented Separate Encoding and Residual) framework, designed to enhance domain-generalizable classification for nonstationary time series data. Recognizing the challenges posed by varying statistical and spectral properties in real-world applications, the authors propose a novel approach that leverages Hilbert Transform for phase augmentation, allowing for diversification of nonstationarity while preserving the discriminative semantics of the data. The framework consists of three key components: (1) phase augmentation through Hilbert Transform, (2) separate encoding of time-varying magnitude and phase responses, and (3) a broadcasting mechanism that incorporates phase information via residual connections to promote domain-invariant learning. Extensive evaluations across five datasets, including sleep-stage classification and human activity recognition, demonstrate that PhASER consistently outperforms state-of-the-art methods by an average of 5% and up to 13% in certain cases. The findings suggest that the principles of PhASER can be broadly applied to improve the generalizability of existing time-series classification models, addressing the critical need for robust pattern recognition in nonstationary environments.

### Strengths
This paper presents a commendable contribution to the field, demonstrating significant strengths. I believe it has two primary advantages:

1. Enhanced Generalization Across Domains: The PhASER framework effectively addresses the challenges posed by nonstationarity in time series data by leveraging phase information obtained through the Hilbert Transform. This methodology enables the model to learn domain-agnostic representations, thereby enhancing its ability to generalize across various distributions and minimizing the effects of domain shifts frequently encountered in real-world applications.

2. Robust Feature Integration: By separately encoding magnitude and phase responses, PhASER improves the integration of time-frequency information. This dual encoding strategy enables the model to more effectively capture the dynamic characteristics of time series data, resulting in enhanced classification performance. Furthermore, the implementation of a residual broadcasting mechanism reinforces the model's capability to retain critical features while mitigating the impacts of nonstationarity.

### Weaknesses
While this paper makes valuable contributions to the field, it also has some notable shortcomings.  I would like to highlight three primary concerns:
1. The paper employs the Hilbert Transform primarily because it effectively extracts phase information from signals and possesses non-parametric properties, making it particularly useful for handling nonstationary time series.  However, wavelet transform offers significant advantages in processing nonstationary signals, especially in time-frequency analysis and multi-resolution feature extraction.  Therefore, why is wavelet transform not utilized in this context?
2. The paper highlights the importance of phase information in the classification of nonstationary time series.  Could you elaborate on how phase information influences the model's learning process?  What specific roles does phase information play in different application scenarios?
3. Image augmentation techniques, such as rotation, may significantly impact the input frequency and phase modalities, particularly when processing time series data.  How can I determine the extent of these transformations to enhance performance without compromising the characteristics of the original data?

### Questions
The authors present their ideas with remarkable clarity; however, I have one question: Could the authors provide a more detailed explanation of the benefits of the Phase-driven Residual Broadcasting method employed in this study, particularly in comparison to other multimodal fusion approaches? What specific advantages does it offer in this context?

### Soundness
2

### Presentation
2

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
This paper proposes a framework for the classification of non-stationary time series based on the frequency domain. The framework consists of three steps. First, the data is augmented using the Hilbert transform. Second, a feature extraction step follows, where the magnitude and phase representation of the input data are calculated based on the STFT. Finally, a neural network is used for further feature extraction and the final classification. 
The key contributions of the paper are the introduction of the "PhASER" framework and extensive empirical experiments, including an ablation study.

### Strengths
- The combination of Hilbert transform for data augmentation, STFT for feature extraction and the proposed neural network for classification seem unique in the literature.
- Classification of non-stationary time series is a highly relevant task. The results seem promising. 
- The empirical evaluation is extensive and the ablation study sheds light onto the importance of each step of the framework.

### Weaknesses
 - The mathematical formulations are not precise; the basic definitions seem flawed. For example, the notation $Pr_{x\sim\mathcal{D}_x}(x)(t)$ in Def. 2.1 is unclear, and the equation (1) resembles a location-scale model, but its probabilistic interpretation is not well-defined. The relationship between the LHS (a probability) and the RHS is not clear, particularly regarding the ranges of $\mu_t$, $\sigma_t$, and $z$. Furthermore, the exclusion of stationary time series in Def. 2.1 is problematic, as many real-world signals can exhibit stationary or near-stationary behavior, and the method's performance in such cases is not discussed. The definition of the domain generalization problem in Def. 2.2 lacks clarity, especially regarding the source domains $\mathcal{X}_S$ and $\mathcal{Y}_S$, the independence of samples, and the process of drawing samples from specific source domains. The connection between $Pr(X_S, Y_S)$ and $Pr(X_{S_i}, Y_{S_i})$ is also not well-defined. The use of $D_U$ to denote any potential unseen target domain, without specifying if it is fixed or variable during optimization, introduces ambiguity. Finally, the non-standard composition of functions $F \circ g$ as $g(F(x))$ is confusing.
- No theoretical guarantees of expected accuracy, true positive/negative rate etc. are provided. The paper lacks any formal analysis of the proposed method's performance, such as convergence rates, generalization bounds, or error analysis. This omission makes it difficult to assess the theoretical validity and reliability of the proposed approach.
- The baseline models used are not really suitable: The baseline methods are domain generalization algorithms for non-time-series-data, and the used time series models were proposed for other tasks than classification. Strong state-of-the-art classification models for time series are missing. The choice of baselines does not allow for a fair comparison with existing time series classification methods, especially those designed for non-stationary data. The absence of established time series classification benchmarks makes it difficult to assess the true contribution of the proposed method.
- Literature on non-stationary time series is abundant (also for classification). In this context, especially the generalization of stationary time series to local stationarity seems important. Further, classification methods from "functional data analysis" are relevant as well. The paper fails to adequately address the existing body of literature on non-stationary time series analysis, particularly the concept of local stationarity and relevant classification techniques from functional data analysis. This omission weakens the paper's contextualization and justification.
- The ablation study seems to suggest that using only the Hilbert transform (and omitting steps 2 and 3) yield similar results. Yet, all the differences seem minimal and could be due to randomness. No quantiles, standard deviation, or similar are reported, so it remains open how useful the steps really are. The lack of statistical rigor in the ablation study, such as reporting standard deviations or confidence intervals, makes it difficult to draw meaningful conclusions about the contribution of each step in the proposed framework. The minimal differences observed could be due to random fluctuations, and the absence of proper statistical analysis undermines the validity of the ablation study.

### Questions
- Def. 2.1: What does the notation $Pr_{x\sim\mathcal{D}_x}(x)(t)$ mean?  The RHS of equation (1) looks like the common location-scale model. The LHS is a probability (in \[0, 1\]), are the values of the RHS expected to be in \[0, 1\] as well? What does this mean for $\mu_t, \sigma_t$ and $z$?
- Def. 2.1 excludes stationary time series. How well is the proposed method expected to work if the time series is indeed stationary?
- Def. 2.2: 
	- What are $\mathcal{X}_S$ and $\mathcal{Y}_S$? 
	- Are the samples independent? 
	- How is determined from which source domain(s) $\mathcal{S}_j$ a sample $(x_i, y_i)$ is drawn from? 
	- What is defined in "Definition 2.2"? 
	- Eq. (2) suggests that each observation $(x_i, y_i)$ comes from a single source, how is $Pr(X_S, Y_S)$ related to $Pr(X_{S_i}, Y_{S_i})$?
	- $D_U$ might denote "any potential unseen target domain". Is it fixed, so the optimization is well-defined, or could it be vary? 
	- The composition $F\circ g$ is interpreted as $g(F(x))$, which is not standard (usually: $(F\circ g) (x)=F(g(x))$) 
- L108: "Note that the joint distributions of different source domains are similar but distinct" -> In which sense are they similar?
- L180: What is the explicit effect of the phase shift on the distribution? Of course the data looks different, but what about its distribution? (partially answered with Thm. 2.6)
- L186: Why can we assume that the time series $x$ is characterized by a deterministic function? This seems counterintuitive considering that time series are usually modeled as random
- L200: So essentially, for each time series $x(t)$, we get a second (phase-shifted) time series $\hat{x}(t)$?
- L225: What is the distribution of $p_i$? How can it be uniformly distributed on the non-negative integers (and not a finite subset)? Why should the window length $W_i$ be random at all?
- What is the overall intuition of the "magnitue-phase separate encoding"? Why is it assumed to work better than using the signal in the time domain (or the original signal concatenated with its phase shifted version)?
- Def. 2.3: What does it mean for a domain to be built on an input variable?
- Theorem 2.5: How is the risk defined?
- L343: How is it good that the distribution is changed? Is the distribution of the Hilbert-transformed output similar to the original data from some domain? If not, it seems counterintuitive that by adding "different data", the classification tasks should be simplified.
- Baseline Methods: Why are no strong baseline methods for time series classification used?
- The only reported metric is the accuracy. Are the datasets balanced, so the accuracy is a reasonable choice? 
- Why is the "Related Work" section at the end of the paper? This seems to be non-standard.
- L508: "Our study is the first to rigorously address the impact of non-stationarity on time-series out-of-distribution classification" -> This is the first time that OOD classification is mentioned in the paper, how is this addressed?

### Soundness
2

### Presentation
1

### Contribution
2
