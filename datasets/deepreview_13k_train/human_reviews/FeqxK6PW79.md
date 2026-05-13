# Analyzing Deep Transformer Models for Time Series Forecasting via Manifold Learning

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Transformer models have consistently achieved remarkable results in various domains such as natural language processing and computer vision. However, despite ongoing research efforts to better understand these models, the field still lacks a comprehensive understanding. This is particularly true for deep time series forecasting methods, where analysis and understanding work is relatively limited. Time series data, unlike image and text information, can be more challenging to interpret and analyze. To address this, we approach the problem from a \emph{manifold learning} perspective, assuming that the latent representations of time series forecasting models lie next to a low-dimensional manifold. In our study, we focus on analyzing the geometric features of these latent data manifolds, including intrinsic dimension and principal curvatures. Our findings reveal that deep transformer models exhibit similar geometric behavior across layers, and these geometric features are correlated with model performance. Additionally, we observe that untrained models initially have different structures, but they rapidly converge during training.
By leveraging our geometric analysis and differentiable tools, we can potentially design new and improved deep forecasting neural networks. This approach complements existing analysis studies and contributes to a better understanding of transformer models in the context of time series forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work the authors explore the use of manifold learning to attempt to illuminate the training and performance of transformer-based deep time-series forecasting. They utilize intrinsic dimension and mean absolute principal curvature to gain insights into behaviors across layers and training.

### Strengths
The authors take an interesting and somewhat novel (in terms of application task) to studying the behavior of transformer-based models for time-series forecasting. 

The reveal an interesting and consistent distribution of the principal curvatures across datasets and highlight a distinction between the behavior of transformer models for classification and regression.

Although difficult to decipher the connections at times, each of the core claims made at the end of the introduction are supported by the experimental results.

### Weaknesses
The first claimed result in the introduction is "during encoding, dimensionality and curvature either drop or stay fixed, and then, during
the decoding part, both dimensionality and curvature increase significantly." This is presumably supported in figures 2 and 3. However, there is no really compelling definition of "significant." The FEDFormer model, for example, ID does not appear to increase significantly but rather end at slightly lower values than at the initial layer. Figure 3 would benefit from the inclusion of errorbars.

While it may be a gap in the reviewer's understanding, the statement that "Indeed, regression models as TSF are expected to learn an underlying low-dimensional and simple representation while encoding. Then, a more complex manifold that better reflects the properties of the input data is learned during decoding" is not intuitively obvious from the results. Seemingly, the inverse relationship between MSE and ID suggests more faithful predictions on the test set but that does not immediately mean that it is capturing properties of the input data. For example, if the trends held for a synthetic time-series dataset based on a dynamical system representing a known manifold structure or where a ground-truth curvature was known, it would more strongly convince this reviewer.

While the reviewer appreciates that the authors still included ETTm1 in their plots, it does exhibit visually distinct behaviors that don't feel convincingly described away by stating that it is because it has fewer features. It would be helpful for a more comprehensive explanation of this either in the text or point to a discussion in the appendix. 

Other comments:
Including a vertical bar identifying the shift from encoder to decoder layers would make it more clear where the authors are identifying the trends that are intended to support the claims. 

Adding the correlation coefficient to Figure 5 would be appreciated.

It appears that the distributions of constant curvatures are converging. Do you have a hypothesis for what it is converging to and why (for each of the encoder and decoders)?

### Questions
The authors state "Indeed, regression models asTSF are expected to learn an underlying low-dimensional and simple representation while encoding." Why is this what one would expect?

Would one expect this behavior to hold for models with more layers? Why?

It appears that the distributions of constant curvatures are converging. Do you have a hypothesis for what it is converging to and why (for each of the encoder and decoders)?

Did you consider, or could you add, results from a synthetic, well-understood dataset?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
- The paper discusses the estimation of curvature quantities in data representations using the Curvature Aware Manifold Learning (CAML) algorithm. Such algorithm takes neighborhood information and an estimate of the unknown intrinsic dimension (ID) of the data.
- The paper also discusses the application of CAML to deep forecasting models and analyzes the intrinsic dimension and mean absolute principal curvature profiles across layers. 
- The analysis is conducted on various datasets and architectures, providing insights into the geometric features of deep forecasting models.

----
Thanks for the rebuttal, but I would remain the same score.

### Strengths
- The paper explores the estimation of curvature quantities in data representations using the Curvature Aware Manifold Learning (CAML) algorithm.
- The paper investigates the geometric properties of data manifolds across layers and provides insights into the intrinsic dimension (ID) and mean absolute principal curvature (MAPC) profiles.
- The correlation between the intrinsic dimension in the final layer and model performance is explored, providing valuable insights for model evaluation and comparison.

### Weaknesses
 - Theoretical contribution is limited in this paper. ID is computed by other paper (TwoNN method), and MAPC ( we employ the curvature aware manifold learning (CAML) technique). Thus, both important tools of this paper is borrowed from other paper. 
- Experimentally, the paper only briefly mentions the potential reasons for the observed behavior of the models but does not delve into a thorough discussion of the implications and practical implications of the findings. This could limit the broader understanding and application of the research.

### Questions
- What is the main theoretical contribution of this paper, if exists.
- What is the main take-home message of the findings from this paper and why it is important.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the geometric properties of the latent representations of deep transformer models for time series forecasting. The authors assume that the latent representations output by each layer of the model lie on a low-dimensional manifold. They estimate the intrinsic dimension (ID) and mean absolute principal curvature (MAPC) of the manifold based on latent representations extracted from the multiple Autoformer and FEDformer models trained with different random seeds on electricity, weather, and traffic datasets. The main observations are: 1) the dimensionality and curvature of the representation manifold either drop or stay fixed in the encoder layers, but then increase significantly in the decoder layers. This phenomenon is consistent across different models, datasets, and forecast horizons; 2) The intrinsic dimension in the final layer is correlated with the model performance; 3) Compared to the untrained models, the ID and MAPC of the representation manifolds change significantly during training, but converge quickly.

### Strengths
- Originality: The paper is the first to study the geometric properties of the latent representations of SOTA deep models for time series forecasting. The observations are interesting and may lead to new insights about the behavior of the investigated models.
- Clarity & Quality: The background, methodology, and results are clearly presented. The paper is easy to follow.
- Significance: The paper is relevant to the ICLR community because it studies the geometric properties of the **learned representations** in SOTA deep TSF models. There are too many TSF papers that focus on the model architectures but ignore what the models have learned. This paper presents a new methodology for analyzing these models.

### Weaknesses
 - My first concern is why Autoformer and FEDformer were chosen as the models to be analyzed. The title of the paper is "Analyzing Deep Transformer Models for Time Series Forecasting via Manifold Learning", but both Autoformer and FEDformer go far beyond the standard transformer architecture. They are not even based on the standard auto-regressive decoder. Given the complexity of these models, it is hard to tell whether the observations are specific to these models due to their design choices or generalizable to other deep transformer models. I am not convinced that the observations are generalizable because of the high complexity of the chosen models.

- Given the high dimensionality of the latent representations, I am not sure whether the estimated intrinsic dimension and curvature information are reliable. The authors should provide some justification for the reliability of the estimates. For example, why is the estimated intrinsic dimension of the first layer close to 1 for Autoformer in Figure 3? This is surprising.

- The methodology part of this work is almost identical to Kaufman & Azencot, 2023. The content in Appendix D.2 & D.3 is almost a copy of Section 3 of Kaufman & Azencot, 2023. I am not sure whether this is OK.

### Questions
- Given the claimed intrinsic dimension is so low, is it possible to visualize the latent representations in a 2D or 3D space? This may help us better understand the geometric properties of the latent representations.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work analyzes transformer-based timeseries forecasting (TSF) deep neural networks from a manifold learning perspective. Specifically, the authors analyzes the behaviour of a few transformer-based models for TSF task using the intrinsic dimension (ID) and mean absolute principal curvature (MAPC) from the study of geometric features of Riemannian manifolds. The authors show that the studied architectures share similar ID and MAPC profiles for a few different datasets. Additionally, the authors showed that the final ID is positively correlated with performance; and presented how the geometry profiles change along with the training process.

### Strengths
- The presented work uses the manifold learning technique to study TSF models, which is a good contribution to the field. This is because (i) the testing set might not always be available as stated by the authors; (ii) Specifically for timeseries applications, the testing set might not be representative enough to describe the model’s performance, as real-world datasets in timeseries are less generalizable and not as large-scale as image or language datasets to comprehensively evaluate the model's performance.
- Good related work summary of manifold learning analysis.

### Weaknesses
Major weakness:
- **Lack of insights to timeseries.** The presented work, although bridges the gap of using manifold learning analysis to study TSF models, lacks insights to timeseries datasets. Specifically, timeseries datasets have their unique properties and challenges, e.g. sampling rate of the timeseries; tokenization layer (specifically, if the token is the aggregation of timeseries across different channels, as the channel-independence property studied in [1, 2, 3]; what is the proper length of the token as mentioned in [1]). The studied group of model architecture, which is transformer, is also not representative enough for timeseries applications, as many linear models [4] and previously, CNN-based models [5] has good performance on the studied task. Overall, this has limited the contribution of the proposed work.
- **Lack of studied architectures.** The selected architectures Autoformer and Fedformer are out-of-dated and contain specific components. E.g. Fedformer uses frequency-analysis to decompose the frequency information (or seasonal trends) in timeseries. The Informer mentioned in appendix helps with this lack of architectures, yet I am not sure about the `Transformer’ mentioned in appendix. What are the specs of this transformer architecture? One important aspect of timeseries study is the spatiotemporal relationship in sequences (that are fed into the transformer); as well as the input dimension of the tokenization layer. How are those selected and how the analyzed properties differ across such choices? The choice of these specific models limits the generalizability of the findings. The analysis should consider a broader range of architectures, including those that do not rely on specific components like frequency decomposition, to determine if the observed geometric properties are consistent across different design choices.
- **Over-claimed contributions.** In conclusion section: “Our results indicate a fundamental difference between classification and regression models: while the former networks shrink the ID significantly to extract a meaningful representation that is amenable for linear separation, regression models behave differently” this contribution seems overclaimed. It is unclear if the behaviour (ID's correlation w performance) is unique to timeseries forecasting or if it is general to all regression/generative tasks. It is also unclear if the reason of such behaviour is due to that the task is a regression task (specifically, it is possible that all timeseries tasks e.g. classification also gives such behaviour). A related question would be that: Does that mean e.g. a generative model in vision also gives better performance when the ID is higher? This contribution should not be claimed if the authors do not fundamentally reveal/prove this correlation.

Minor weakness:
- In the related work section, analysis of transformers: “While in general they question the effectivity of transformer for forecasting, new transformer-based approaches continue to appear (Zeng et al., 2023), consistently improving the state-of-the-art results on common forecasting benchmarks.” Zeng et al., 2023 claims that a linear-based modeling approach outperforms transformer-based modeling approaches, and does not present a transformer architecture by itself. It is unclear to me if the citation here is appropriate.
- “Namely, we discard data from the red and blue trajectories” Please refer to Figure 1 in text for this sentence for clarity.
- Can the authors break down this sentence? “We hypothesize that significantly deeper and more expressive TSF models as was in (Nie et al., 2023) and is common in classification (He et al., 2016) may yield double descent forecasting architectures (Belkin et al., 2019)."

### Questions
As above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
