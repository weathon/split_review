# Strong Model Collapse

- Decision: Reject
- Scores: 8, 8, 8

## Abstract
Within the scaling laws paradigm, which underpins the training of large neural networks like ChatGPT and Llama, we consider a supervised regression setting and establish the existance of a strong form of the model collapse phenomenon, a critical performance degradation due to synthetic data in the training corpus. Our results show that even the smallest fraction of synthetic data (e.g., as little as 1\% of the total training dataset) can still lead to model collapse: larger and larger training sets do not enhance performance.  We further investigate whether increasing model size, an approach aligned with current trends in training large language models, exacerbates or mitigates model collapse. In a simplified regime where neural networks are approximated via random projections of tunable size, we both theoretically and empirically show that larger models can amplify model collapse. Interestingly, our theory also indicates that, beyond the interpolation threshold (which can be extremely high for very large datasets), larger models may mitigate the collapse, although they do not entirely prevent it. Our theoretical findings are empirically verified through experiments on language models and feed-forward neural networks for images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies model collapse, which relates the performance degradation of ML models due to synthetic training data. For linear regression and random projections model, the authors establish scaling laws that characterize this degradation, as a function of the proportion of the synthetic data as well as the quality. Their findings suggest that larger models become more susceptible to this degradation. Experiments pertaining to training GPT-2 with synthetic data are used to demonstrate validity of their results beyond the limited theoretical models.

### Strengths
- The paper is very well written; the problem statement and the contributions are clearly established. 
- The theoretical results seem sound and intriguing, and I appreciate the authors efforts to present simplified examples to help the reader understand the implications better.
- The findings seem to transfer to practical learning settings fairly well.

### Weaknesses
 - Model Assumptions: I am unsure of the modelling of synthetic data and how well it translates into practice. Specifically, the authors model synthetic data using a label shift, assuming that the data (X) marginal remains the same. However, it seems unrealistic for autoregressive training (a key experiment in the paper), where the input tokens for next token generation come from the synthetic distribution. The label shift assumption, while simplifying the analysis, might not fully capture the complexities of autoregressive models where the input sequence itself is a mix of real and synthetic data, potentially leading to a domain shift in addition to the label shift. This is particularly concerning as the model is trained on sequences where the input distribution changes over the course of generation, which is not accounted for by the theoretical framework.
- Experimental Details: The theoretical results establish a strong dependence on the quality of synthetic data. However, the experiments with real data (MNIST/GPT-2) do not provide quantitative metrics to measure the degradation in the synthetic data source (either accuracy of MNIST classifier or perplexity/goodness scores of the trained GPT-2 generator), which makes it hard to ascertain which paradigm (in fig.1) the experiments align best with or what level of degradation in practice results in the observed trend. Without these metrics, it is difficult to assess the extent to which the observed model collapse is due to the quality of the synthetic data versus other factors. For instance, the MNIST experiment lacks a clear measure of how the synthetic labels' quality impacts the final model performance, making it difficult to validate the theoretical predictions.
- Minor Issues
    - Typos: Line 225 (v \in R^{m}), line 299 (synthetic data P2), line 398 (represented by stars)
    - Suggestions for Clarity:
        - Akin to theorem 1, is it possible to present a simplified version of theorem 2 for the general audience? As it is, definition 2 and theorem 2 are hard to digest just on their own.
        - Line 481, before stating the result, can the authors explain in words the process of iterative mixing proposed in Ferbach et al., 2024? It would make the manuscript more self-contained.  
    - Missing Citation: Line 424, for the MNIST dataset, please include the citation for "Gradient Based Learning Applied to Document
 Recognition", LeCun et al, 1998 
    - Visualization: For fig.1, please consider changing the y-axes test error to the same scale. Right now, it is hard to compare the error values or the slope in subplot 1 to those in 2 and 3.

### Questions
- Model Assumptions: Regarding the label shift assumption, what are the authors thoughts on how the results would change if the domain shift were to be accounted for as well? 
- Experimental Setup: 
    - I understand that it might not be computationally feasible for GPT-2 in the given timeframe, but could the authors provide an ablation on the MNIST experiment with regards to the quality of synthetic data? That is, models trained on labels taken from increasingly worse synthetic classifier and the corresponding trends. 
    - Minor: Regarding the GPT-2 experiment, if BabiStories is itself synthetic, why not use TinyStories as real data and BabiStories as the synthetic dataset for training the models, as opposed to creating a new GPT generator?

### Soundness
3

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
This paper considers the questions: is model collapse inevitable when training with synthetic data? Are larger models more prone to collapse than smaller ones? The paper concludes that model collapse is inevitable if training with some non-zero about of synthetic data. Larger models may suffer more from model collapse in the low quality data setting. The paper contains theoretical analysis for linear models and random projection models, and empirical results for GPT-2 models trained on the BabiStories dataset.

### Strengths
- The paper shows model collapse in theoretical settings of the linear and random projection models
- The paper shows nice alignment between the experiments and theoretical analysis (eg Fig 3)

### Weaknesses
I'm a bit unclear on the takeaway from the experimental results with GPT2. Specifically, the paper seems to make mixed claims for the case of large models beyond the interpolation threshold; it is said that large models may mitigate the collapse beyond the interpolation threshold and that large models tend to amplify collapse beyond the interpolation threshold in the experimental results. The discussion around the interpolation threshold and its relation to model size and number of training tokens is not sufficiently clear, leading to confusion about the conditions under which larger models help or hurt. The paper should clarify the specific mechanisms by which model size interacts with the amount of synthetic data and the interpolation regime to affect model collapse.



### Questions
- For the empirical results, it is said that the curves are expected to plateau in Fig 5. Can this be shown empirically by further scaling?
- Can the double descent phenomenon be showed more clearly in the experimental results?
- Separately, I would be interested in more analysis specifically in the high quality data setting, ie what can be said about the amount of model collapse as the synthetic distribution approaches the real distribution?

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
4

### Summary
This paper studies the model collapse phenomenon in a supervised regression setting. The authors study whether model collapse is inevitable or whether proper mixing strategies can mitigate it. They also study the connection between model size and robustness to model collapse.

*Setup and tools*: The theoretical analysis focuses on linear models and random projection models (simplification of neural networks). The authors derive their proofs using linear pencils and operator-valued free probability theory (OVFPT).

*Contributions*: The authors provide two main theoretical results: 1) they show that even the smallest fraction of synthetic data can lead to model collapses where increasing the model's size does not improve the performance. This is dubbed "strong model collapse". 2) They study the impact of the model's size on the severity of the collapse and show that bigger models are more prone to model collapse when the distribution shift between synthetic and real data is important. They also show that an interpolation threshold exists (model size = sample size) beyond which larger models are more robust to collapse. This is akin to a double descent phenomenon. The theoretical results are experimentally verified on synthetic data and the authors also conduct experiments with neural networks on MNIST and GPT2-small on BabyStories data that corroborate their results.

### Strengths
- The problem tackled by the authors is of great interest for the training of large-scale generative models.
- I find the derivation of the proof elegant and the usage of the OVFPT novel in this setting.
- The derived results are insightful and well-analyzed by the authors, along with the empirical validation on synthetic data that helps to convey their implications to real-world scenarios.
- The authors conduct experiments on real data with (small) neural networks and LLMs that corroborates their theoretical analysis.
- The paper is well-written and logically structured, making it easy to follow the authors' arguments and methodology.

### Weaknesses
1) Could the authors detail more the key steps/ideas of the proofs in the main paper (paragraph **Proving Theorem 1**)? I believe such tools could be beneficial to the reader, even in other applications. Specifically, while the use of linear pencils and operator-valued free probability theory (OVFPT) is mentioned, the actual mechanics of how these tools are applied to derive the results are not sufficiently clear. For instance, how exactly does OVFPT allow for the analysis of the limiting spectral properties of the random matrices involved, and how do these spectral properties then translate into the observed model collapse behavior? A more detailed explanation of these steps would greatly enhance the accessibility and impact of the theoretical contributions.
2) Could the authors discuss the estimation of the quality of synthetic data (parameter $c^2$) on the real applications with MNIST and BabiStories? How would one assess it when training a large-scale model like an LLM  or a VLM? The paper uses a parameter $c^2$ to represent the quality of synthetic data, but it's unclear how this parameter is determined in practice, especially for complex datasets like MNIST and BabiStories. The connection between the theoretical parameter and the practical quality of synthetic data needs to be more explicit. Furthermore, the paper should discuss the challenges in estimating this parameter when dealing with large-scale models like LLMs and VLMs, where the notion of 'quality' is more nuanced and difficult to quantify.
3) Could the authors discuss in more length the "cost" of approximating neural networks as random projections? In particular, what is lost in terms of generality, does it approximate any architecture (e.g., can LLMs be studied in the NTK or infinite-width limit?) The paper's reliance on random projection models, while analytically tractable, raises questions about the generalizability of the results to more complex neural network architectures. The authors should discuss the limitations of this approximation, particularly in terms of capturing the feature learning capabilities of neural networks. It is also unclear whether the random projection model can approximate the behavior of neural networks in different regimes, such as the Neural Tangent Kernel (NTK) or infinite-width limits, and whether the results can be extended to architectures commonly used in LLMs.

### Questions
See weaknesses.

I list the potential typos found in the text below. *"a-->b"* means I think a should be replaced by b.

*Section 2.2*
- Paragraph **Random Projection Models** (l224 & l225 ): it seems that dimensions of $S, x, v$ do not match. According to previous notations, $x \in \mathbb{R}^d$ implies $S \in \mathbb{R}^{m \times d}$ (instead of $d \times m$ as it is currently (l224)) and $v \in \mathbb{R}^m$ (instead of $v \in \mathbb{R}^k$ as it is currently (l225)).

*Section 3.1*
- Paragraph **Example: The Isotropic Case** (l299): *"the synthetic data $P_1$"* --> it should be *"the synthetic data $P_2$"*

*Section 3.2*
- Paragraph **Are Larger Models More Prone...** (l398 & l401): *"represented by crosses"* --> it should be *"represented by stars"* (l398). I am not sure but according to Figure 1 *"for both high-quality and low-quality (squares)"* --> it should be *"for both very high-quality and high-quality (squares and diamonds)"* (l401)

### Soundness
4

### Presentation
4

### Contribution
3
