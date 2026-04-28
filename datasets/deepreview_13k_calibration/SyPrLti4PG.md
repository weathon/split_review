# When predict can also explain: few-shot prediction to select better neural latents

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Latent variable models serve as powerful tools to infer underlying dynamics from observed neural activity. However, due to the absence of ground truth data, prediction benchmarks are often employed as proxies. In this study, we reveal the limitations of the widely-used 'co-smoothing' prediction framework and propose an improved few-shot prediction approach that encourages more accurate latent dynamics. Utilizing a student-teacher setup with Hidden Markov Models, we demonstrate that the high co-smoothing model space can encompass models with arbitrary extraneous dynamics within their latent representations. To address this, we introduce a secondary metric -- a few-shot version of co-smoothing. This involves performing regression from the latent variables to held-out channels in the data using fewer trials. Our results indicate that among models with near-optimal co-smoothing, those with extraneous dynamics underperform in the few-shot co-smoothing compared to 'minimal' models devoid of such dynamics. We also provide analytical insights into the origin of this phenomenon. We further validate our findings on real neural data using two state-of-the-art methods: LFADS and STNDT. In the absence of ground truth, we suggest a proxy measure to quantify extraneous dynamics. By cross-decoding the latent variables of all model pairs with high co-smoothing, we identify models with minimal extraneous dynamics. We find a correlation between few-shot co-smoothing performance and this new measure. In summary, we present a novel prediction metric designed to yield latent variables that more accurately reflect the ground truth, offering a significant improvement for latent dynamics inference.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper focuses on the evaluation method of neural latent-variable models (LVM). Neural LVM aims to learn representations of neural dynamics in a latent space. This space should be able to represent the ground truth hidden representation space. However, due to the lack of ground truth latent in neural signal data, people propose to evaluate the quality of learned latent via co-smoothing, which jointly estimates latent variables and predicts observations along held-out channels as evaluation metrics. With HMM synthetic data, the paper empirically shows that good co-smoothing performance does not ensure good latent, since the model can learn redundant information to have good prediction results. Therefore, the paper instead proposes the few-shot co-smoothing, which better separates good LVM from bad LVM. The paper further provides mathematical insights based on the prediction variance of co-smoothing and few-shot co-smoothing methods. Lastly, the paper adapts co-smoothing with cross-decoding to real data and shows good "accuracy".

### Strengths
1. The paper has a high-level storyline that is easy to follow: from the limitation of co-smooth, proposing new few-shot co-smoothing, reasons for few-shot co-smoothing to work, and how to adapt few-shot co-smoothing to real neural signals.
2. The paper covers both empirical analysis of existing methods, practical improvements based on the existing method, and mathematical interpretations of the proposed improvement.
3. The paper provides an honest discussion of limitations.

### Weaknesses
1. Writing of limited works is a bit messy: too many paragraphs, mixing related works with the introduction of the work's methodology and contribution. It would be clearer to provide clean related works as a background and only include a short emphasis on the uniqueness of this paper.

2. The writing in other parts is also a bit confusing and the paper seems to be finished in a rush, missing ","s in several positions: L118 after "forward-prediction", L122 after "During evaluation", L125 after "full time-window", L142 after "log-likelihood", etc, ... Let me know if I misunderstood these parts.

3. The paper lacks an explanation for choosing HHM as a synthetic data model to approximate real neural signals.

4. The paper lacks clarity and technical details, see Questions parts.

### Questions
1. L58: LVM is introduced without explanation, and the explanation is finally given in L113.

2. L118: "Data may be held-out in time, e.g forward-prediction or in space, co-smoothing (Pei et al., 2021)." Here, is "held-out in time" the same as "forward-prediction" of signal in the latent space or signal space? Besides, is "Data held-out in space" the same as "co-smoothing"? But what does "Data held-out in space" exactly mean?

3. L149: why is equation (5) "without direct access of $X_{\text {test }}^{\text {out }}$"? From the definition in (3) and (4), I feel $X_{\text {test }}^{\text {out }}$ is required.

4. In section 4, how to validate that the specific setting of HMM is a suitable synthetic data model that can reveal features of real neural signals?

5. In section 5, how to choose "k"? What about selecting "k" for real data, is there a principled rule?

I am willing to hear from authors and other reviewers in addressing my questions and concerns. I will change the score if others' comments solve my questions and convince me about the quality and importance of this work.

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
The paper studies the limitations of the commonly used co-smoothing prediction framework applied to latent variable models predicting underlying dynamics, specifically in the context of neural activity modeling. The authors provide synthetic teacher-student setup demonstrating how good performance in terms of co-smoothing does not imply learning the ground-truth latents. In the same setup, an additional prediction score termed few-shot co-smoothing is suggested leading to better correlation with true latents for models with high co-smoothing. In a real-world setup, the authors suggest a proxy metric assessing the similarity of a model’s latents to an unknown teacher, and show that their suggested score correlates with it.

I am relatively unfamiliar with the subject of the paper and prior work but found the presentation and ideas easy to follow.

### Strengths
* The paper is well organized and each section has a clear and consice statement.

* The teacher-student setup provides a convincing example of the problem with co-smoothing scores.

* The suggested solution of few-shot co-smoothing is simple and seems to be reasonably effective in the suggested setups.

### Weaknesses
 * Evaluations in section 7 rely on a metric, cross-decoding error, defined by the authors themselves and argued for in the text. No prior work pointing to the validity of the score is provided, see further questions below.

* Since correlation in section 7 is not perfect, and due to the above, further empirical verification of the method, with either additional datasets and/or models, is missing. The lack of perfect correlation, even with the proposed proxy metric, raises concerns about the generalizability of the conclusions. Specifically, it's unclear if the few-shot co-smoothing score would consistently identify models with latent representations closer to the true underlying dynamics across diverse datasets and model architectures. This is especially important given the potential for the cross-decoding metric to be sensitive to specific model families or hyperparameter choices. Furthermore, the current evaluation does not explore the sensitivity of the few-shot co-smoothing score to the number of shots used, which could impact its reliability in different scenarios.


### Questions
* My main questions revolve around evaluations in section 7 and the cross-decoding metric used as ground truth:
   * Can the authors provide the performance of the cross-decoding score in the synthetic setup where the latent variables are known? can one use it to choose a model with latent representation closest to the ground truth?
   * In the general case and assuming no computational constraints, is this metric supposed to be superior to scores from few-shot cosmoothing and can this be verified empirically?
   * Even if the assumption on cross-decoding as a proxy to the ground truth is correct - selecting from a pool of models that differ by hyperparameters can be highly dependent. Is it possible to select jointly from a pool of different architectures? .e.g, LFADS, STDNT.

* In section 3 can you clarify which notation (bold/regular) refers to vectors/tensors/scalars? I could not understand from the text.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper focuses on latent variable models (LVMs) for inferring neural activities (neural spikings). Conventional approaches in this field rely on co-smoothing, which jointly estimates the latent variables and predicts observations. This work hypothesizes that, accurate prediction via co-smoothing ensures that LVMs captures the true latent structure, while the reverse may not be true. This claim is justified using an example of discrete-time Hidden Markov Model (HMM). To overcome the aforementioned limitation, this paper proposes an alternative metric called few-shot co-smoothing, which reduces the number of data (trials) used for regression. Experiments on real neural data are conducted with two SOTA methods to validate the effectiveness of the advocated metric.

### Strengths
1. The writing of this paper is good, and the illustration figures are clear. 

2. The example provided in Section 4 and corresponding observations are interesting.

### Weaknesses
Major concerns:

1. The proposed few-shot co-smoothing is based on empirical observations on a simple HMM model. It would be highly beneficial if theoretical results regarding extending this analysis to more generic cases can be provided. In the current manuscript, it is hard to conclude for which family of problems and under what conditions the proposed metric can be effective. It is unknown whether and how few-shot co-smoothing will also help when the relationship between the latent variables and observations becomes complicated. Specifically, the paper does not address how the complexity of the observation model (i.e., the function mapping latents to observations) affects the efficacy of few-shot co-smoothing. For instance, if the observation model is a deep neural network, the relationship between the latent space and the observations might be highly non-linear and difficult to capture with a simple regression, potentially invalidating the core assumptions of the proposed metric.

2. The relationship between the claim, "good prediction guarantees that the true latents are contained within the inferred ones, but not vice versa", and the example provided in Figure 1.DE is unclear. In my understanding, both $\mathcal{D}_{\rm S\rightarrow T}$ and $\mathcal{D} _{\rm T\rightarrow S}$ are utilized to assess whether "the true latents ($z_T$) are contained within the inferred ones ($z_S$)". The paper has not clearly explained their differences, and what each metric indicates. Furthermore, Appendix B leverages multinomial regression to "align" two multinomial distributions and then measure their KL distance. Why is multinomial regression performed with a logistic model rather than other models? It is also possible that two distributions are close under certain mapping but logistic model fail to identify this mapping. To measure the distance between two distributions, there can be some other alternative approaches such as optimal transport. The rationale behind this design choice needs further clarification. The choice of using a logistic model for multinomial regression, without exploring alternatives or justifying its suitability, raises concerns about the robustness of the alignment process and the validity of the subsequent KL divergence calculation.

3. Experiments are not sufficiently convincing due to the lack of quantitative comparisons. Section 7 showcases $\mathcal{D}_{\rm S\rightarrow T}$ and $\mathcal{D} _{\rm T\rightarrow S}$ when applying few-shot co-smoothing to SOTA LVMs. However, it remains unknown how mismatched the latents can be with co-smoothing, and how this will affect the prediction performance of the model. The paper lacks a clear baseline comparison showing the degree of latent mismatch when using standard co-smoothing and how this mismatch correlates with prediction performance. Without such a comparison, it's difficult to assess the practical benefits of the proposed few-shot co-smoothing metric.

4. No supplementary files or codes are provided, making it hard to verify the reported results.

Minor comments:
1. In line 111, "representing" should be "represents".

2. In line 142, add a comma after "log-likelihood".

3. "Figure 1B" in line 159 should be corrected to "Figure 1C".

4. The cross references for equations are not in correct formats; "\eqref" should be used instead of "\ref".

5. The abbreviations for "Figure" are not consistent throughout the paper. For instance, lines 234, 241, and 244 respectively adopts "fig.", "Fig.", and "FIG".

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2
