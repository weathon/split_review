# Decompose Time and Frequency Dependencies: Multivariate Time Series Physiological Signal Emotion Recognition

- Decision: Reject
- Avg Score: 3.67
- Scores: 3, 3, 5

## Abstract
In this study, we proposed a transformer based end-to-end solution to capture the relationship between the physiological signals and affective changes. We first convert the physiological signal emotion recognition prediction task to a sequence-to-sequence multivariate time series prediction task. We utilize the state-of-the-art (SOTA) self-attention mechanism to decompose the physiological signals into separate frequency domain and time domain representations, and capture the channel dependencies via Two-Stage Attention (TSA). Meanwhile, we implement the multitask learning framework to better predict the valence and arousal affective states individually. We evaluate our system on the Continuously Annotated Signals of Emotion (CASE) dataset used in the Emotion Physiology and Experience Collaboration (EPiC) challenge, and our proposed system outperform all the challenge participants in all four test scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, the authors propose a transformer-based solution for physiological signal emotion recognition, by converting the recognition task to a multivariate time prediction task. The authors decompose the signals into separate time and frequency domain representations using self-attention mechanisms and capture channel dependencies. The proposed system outperforms other participants in the Emotion Physiology and Experience Collaboration challenge.

### Strengths
1. The authors utilizes some state-of-the-art mechanisms, such as wavelet and Fourier attention, to decompose the physiological signals into separate frequency domain and time domain representations.
2. The authors introduce a two-stage attention mechanism to capture the dependencies between signals. This addresses the challenge of having both cross-time and cross-dimension dependencies and improves the model's ability.

### Weaknesses
1. There should be more ablation studies to prove each component in the proposed method works. Specifically, the impact of each attention mechanism (wavelet, Fourier, two-stage) and the effect of different encoder/decoder configurations should be investigated individually. The lack of such analysis makes it difficult to assess the true contribution of each component.
2. The related work section introduces some references and attention mechanisms that the authors used, without the information about the following compared works. It is unclear how the authors' approach compares to existing methods in the specific task of physiological signal emotion recognition, beyond the challenge leaderboard. A more thorough discussion of the state-of-the-art is needed.
3. The replace of the MSAs in the encoder should have evidence to prove its rationality and efficiency, so as the frequency and time domain TSA in the decoders. The rationale behind these architectural choices is not sufficiently explained or justified. The paper lacks a clear explanation of why these specific replacements and configurations were chosen over alternatives, and there is no empirical evidence to support their effectiveness.
4. Many simple formula notations are cumbersome, for example, we have long been familiar with the attention mechanisms. The excessive use of detailed formulas for standard attention mechanisms clutters the paper and reduces readability. The paper should focus on the novel aspects of the proposed method rather than providing unnecessary details on well-established concepts.

### Questions
Please refer to the weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This study proposes a new method to analyze the link between physiological signals and emotional changes. By using a transformer-based model, the authors shift the focus from emotion recognition to predicting sequences of multivariate time series data. They employ a two-stage attention mechanism to process these signals, and through multitask learning, improve the prediction of two emotional states: valence and arousal. The model, when tested on a specific dataset, outperformed other methods from a related challenge in all evaluated scenarios.

### Strengths
The authors achieved SOTA performance on the EPiC challenge dataset.

### Weaknesses
1. I am having trouble seeing the contributions of this paper. It seems like the authors have used an existing model and fitted it on a new dataset. The authors have not tested whether the model is generalizable to other affective datasets. If authors could point out some key aspects of the papers contributions a bit more clearly it would be greatly appreciated. 
2. The interpretability of the results seem a bit lacking. Why does the author's proposed method outperform other participant's methods? Additionally, table 1 has a row labeled "Scenario level." Could the authors clarify what this means?

### Questions
1. Have the authors considered doing an ablation study on which physiological signals may be contributing the most to the performance? 
2. The authors mention that they "capture the relationship between physiological signals and affective changes." Could you clarify to me how this relationship is captured with this model?
3. This paper was submitted to the "Primary Area: applications to neuroscience & cognitive science." I am having a bit of trouble seeing this paper's contribution to this area. Could the authors clarify this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces an end-to-end physiological signal emotion recognition model, and it achieved first place in all four tracks of the EPiC Challenge. Building upon the FED-Former, the model incorporates Two-Stage Attention (TSA) to capture temporal dependencies in the data. The paper implements multi-task learning for valence and arousal prediction tasks. The main contributions of the paper are as follows: 1. It proposes an end-to-end emotion recognition model based on physiological signals. 2. It enhances the FED-Former model to capture temporal dependencies between data. 3. The model performs exceptionally well across four tasks: Across-time scenario, Across-subject scenario, Across-elicitor scenario, and Across-version scenario.

### Strengths
#originality:
This paper demonstrates a good level of originality. Firstly, it addresses a problem in the field related to long-term time series forecasting in the time domain. Secondly, the proposed solution is simple yet effective. Although its overall structure is quite similar to FED-Former, the use of Two-stage Attention proves to be innovative and efficient. Furthermore, it performs well in scenarios across all four tasks, highlighting the model's originality.

#quality:
The quality of this work is relatively mediocre, mainly due to issues with experimental rigor, especially the lack of comprehensive model comparisons and tasks. Although the paper shines in terms of the model's performance, conducting more comparisons with traditional tasks would significantly enhance the paper's quality. The methodological rigor and reliability require improvement. There are also concerns regarding the overall presentation of results, figures, and tables, as there is a lack of graphical representation, and the experimental results are relatively limited.

#clarity:
The clarity of this paper is relatively good, but there is still room for improvement. The content is well-structured, with logical connections throughout. However, there are some drawbacks: 1. The representation of certain letters is not very intuitive and may lead to confusion. 2. There is a lack of illustrations, making the descriptions less visually informative. 3. In the 'METHODOLOGY' section, the explanation of sequence length is somewhat disjointed and may not be easily understood by readers. 4. The description of the resolution DSW embedding is not very clear.

#significance:
The limited experimental results are a significant factor affecting its impact. If there were more comprehensive experimental results, this paper would have a significant impact. It has made a substantial contribution to the field by addressing the capture of long-term temporal dependencies in the time domain through an end-to-end model. While the preprocessing stage may pose some challenges, the practical utility of the model surpasses that of a simple machine learning classification model. It also avoids the need for complex feature engineering.

### Weaknesses
1. The originality of the model's architecture is somewhat limited. Despite its focus on temporal considerations, it relies on a frequency domain model, and its fundamental structure closely resembles that of FED-Former. The core innovation, Two-Stage Attention (TSA), while effective, is grafted onto an existing framework, raising questions about the novelty of the overall approach. The paper does not sufficiently explore alternative architectures or justify the choice of building upon FED-Former, especially given the focus on time-series data where other temporal models might be more naturally suited.

2. The model's real-world applicability raises questions. While it exhibits strong performance in just four tasks from a single competition, it lacks comprehensive comparisons with other existing models, making its effectiveness less persuasive. The evaluation is limited to the EPiC challenge, and the absence of comparisons with established time-series models or other physiological signal emotion recognition methods leaves the reader unsure of the model's relative strengths and weaknesses. The paper needs to demonstrate its generalizability by evaluating on diverse datasets and comparing against a broader range of baselines to establish its practical utility.

### Questions
Questions:

In the methodology section, could you elaborate more on the sources and rationale behind your ideas, rather than merely describing the structure? In the EXPERIMENT SETTINGS section, could you provide specific details about your experiment's hyperparameters to facilitate model reproducibility for readers?

Suggestions:

To enhance the paper, start by conducting experiments on a broader spectrum of datasets to evaluate the model's performance and establish its feasibility. Make an effort to include comparative analyses with other existing models wherever applicable. Additionally, aim to incorporate more visual aids to offer a more lucid representation of your concepts. Given the numerous symbols within your paper, improving the intuitiveness of these notations is essential.


---------After rebuttal--------------
Thank the authors for providing the rebuttal. I have read the rebuttal and the other reviews. Based on the limited originality and the insufficient ablation studies as pointed out by other reviews, I decreased my rating to marginally below the acceptance threshold. Please consider the reviews and the rebuttal carefully for another submission.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good
