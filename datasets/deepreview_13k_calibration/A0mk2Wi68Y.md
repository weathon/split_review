# Enforcing Interpretability in Time Series Transformers: A Concept Bottleneck Framework

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
There has been a recent push of research on Transformer-based models for long-term time series forecasting, even though they are inherently difficult to interpret and explain. While there is a large body of work on interpretability methods for various domains and architectures, the interpretability of Transformer-based forecasting models remains largely unexplored. To address this gap, we develop a framework based on Concept Bottleneck Models to enforce interpretability of time series Transformers. We modify the training objective to encourage a model to develop representations similar to predefined interpretable concepts. In our experiments, we enforce similarity using Centered Kernel Alignment, and the predefined concepts include time features and an interpretable, autoregressive surrogate model (AR). We apply the framework to the Autoformer model, and present an in-depth analysis for a variety of benchmark tasks. We find that the model performance remains mostly unaffected, while the model shows much improved interpretability. Additionally, interpretable concepts become local, which makes the trained model easily intervenable. As a proof of concept, we demonstrate a successful intervention in the scenario of a time shift in the data, which eliminates the need to retrain.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In an effort to develop more interpretable time-series forecasting models, the authors have combined a transformer-based architecture (Autoformer) with a concept bottleneck approach. The concepts do not correspond to any a priori annotations bur rather are derived either from an autoregressive model or from sample timestamps.  The authors encourage the network to "reason" using these concepts by adding an additional term to the loss function that captures the similarity between the model's internal representations and the precomputed concepts. The balance between prediction error and representational alignment (in the cost function) with the concepts is regulated through a single hyperparameter. Furthermore, the alignment scores with the different concepts (as captured by CKA) seem to make intuitive sense for many of the datasets (electricity usage and time of day for example). Overall, this is an interesting approach to a timely problem in the field. That said, there are some open questions about the approach that need to be addressed.

### Strengths
- The goal of the paper, the presentation, and the implementation details are clear
- The approach does not require costly annotations for concepts and can (arguably) be applied to any time-series data

### Weaknesses
 - Looking at the qualitative results in Figure 9 and the summary in Table 1, this approach seems to do well for data that has a strong cyclical component (traffic and electricity). In fact, for all other datasets, the simpler AR model works best. How do you explain this? It seems like you get performance AND interpretability using an AR model, then why do you need a model with many more parameters? Maybe there are other datasets that could highlight the benefit of this approach (vs a simple AR based model) a little better? Perhaps I misunderstood something.
- It's hard to get an understanding of how the model is leveraging the concepts, especially since your results on hyper-parameter sensitivity (Table 5, Appendix F) are not the most intuitive; the first and second best settings of the alpha parameter are far apart (0.7 and 0.0). For pedagogical reasons, it might help to train the model on a synthetic dataset, constructed with the concepts (+noise) of your choice. Using a synthetic dataset might give the reader some more mechanistic intuition.

### Questions
- Is the optimal setting for the hyper-parameter dataset specific?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors develop a concept bottleneck model for time-series forecasting with the objective of improving interpretability. Concept bottleneck models are a pre-existing approach to interpretability whereby the model aims to predict a set of concepts first, and then only uses the predicted concepts for the final forecast.

Starting from the Autoformer architecture, the authors introduce two types of bottlenecks (an autoregressive forecast and a time-of-day prediction). To ensure all information passes through the bottlecneck, they then ablate the residual connections. Finally the training loss is an interpolation of the standard loss + a score based on the similarity score CKA of the model’s representations and interpretable concepts.

### Strengths
The strengths are as follows:

- The paper is well-written, and the idea is expressed clearly.
- The authors achieve what they set out to do: their model functions at the intended task.

### Weaknesses
The weaknesses of the paper are as follows:

- In reviewing the performance results in Table 1, as the authors themselves acknowledge there is no significant improvement in performance (as is to be expected given the algorithm, this is of course not an issue). The paper however lacks a comparative analysis of this interpretability against other methods that also offer interpretable time-series prediction: does their approach outperform others in that space?

- Although the concept is intriguing, it feels somewhat derivative, essentially applying concept bottlenecks to time-series forecasting. One immediate concern is the relative lack of novelty. This may not be a significant issue if there were more extensive analysis of the components in their approach, yet the exploration remains somewhat limited. Specifically, other proxy tasks for the interpretable concepts could have been explored, as well as other components (e.g. bottleneck location, similarity metric used, transformer models...).

- The authors note that the AR model outperforms other approaches. This finding is not unexpected given prior work (e.g., [1]), but further analysis is warranted. The key unanswered question, in my view, is how much of the absence of performance degradation is due to the strong proxy task provided by AR (i.e. is their model performing as well as the unaltered baseline only due to the strong signal provided by the AR subtask).

- The dataset selection is somewhat limited. The authors mention that the time-series analyzed in this study had strong linear characteristics, which likely explains the AR model's performance. This could motivate the use of more complex datasets to verify if the findings hold more broadly.

### Questions
Please refer to the weaknesses section above for questions.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a time series Transformer model to be more interpretable with concept bottlenecks using time features and simple autoregressive models as interpretable concepts.
* A training framework encouraging the similarity between transformer representations and pre-defined interpretable concepts using CKA.
* Application of Autoformer on the model was made and its performance was evaluated on 6 benchmark datasets.
* Demonstrate the capability of model intervention in case of temporal shifts.
* Extensive interpretation analysis supported by the visualization technique.

### Strengths
* Novel application of CBM to time series
* Creative use of CKA for concept alignment
* Integration with Autoformer architecture
* Novel intervention capabilities

* Comprehensive experiments on 6 datasets
* Detailed ablation studies
* Visualization of learned concepts
* Intervention demonstration

* Comparable performance to baseline
* Interpretable predictions
* Intervention capabilities for temporal shifts
* Domain-agnostic approach

### Weaknesses
 * Single model architecture (Autoformer)
* Further research is needed to apply CBM to other types of predictive models
* Selection of interpretable concepts relies on heuristics
* Limited analysis of statistical significance
* No comparison to other interpretability methods

* Potential information leakage not fully addressed
* Limited analysis of concept quality
* No theoretical guarantees
* Trade-offs not fully explored


* In Table 1, the simple AR model outperforms the Autoformer with bottleneck in 4 out of 6 datasets. Since the AR model is inherently interpretable, these results may suggest that the proposed method is less effective than expected. The authors could consider adding more complex datasets to strengthen the experimental evaluation.

### Questions
* Is there a qualitative or quantitative comparison of the proposed method with other XAI techniques?

* The results of the intervention experiment are intriguing, but the purpose of this experiment remains somewhat unclear. Could the authors provide a more detailed analysis, discussion, or examples to clarify this?

* How were the specific interpretable concepts (AR model and time features) chosen? Were other concepts considered?

* How do you validate that the learned concepts are truly interpretable and meaningful? Have you conducted any user studies with domain experts?

* Why was Autoformer specifically chosen as the base architecture?
Would the approach work similarly with other transformer variants?

* What is the impact of bottleneck location on performance and interpretability? Was there a systematic study of different locations?

* How sensitive is the training to the CKA loss weight α? Are there guidelines for selecting this parameter?

* What is the computational overhead of the bottleneck compared to standard Autoformer? How does this scale with sequence length?

* How do you quantitatively evaluate the quality of interpretations? Are there metrics beyond CKA scores?

* How generalizable is the intervention approach to other types of shifts? What are the limitations?

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
This paper proposes a framework to enforce interpretability in time-series forecasting Transformers by adapting the Autoformer model with a concept bottleneck approach. The framework aligns the model’s representations with interpretable concepts, such as a surrogate AR model and time-based features, using Centered Kernel Alignment (CKA). This structure aims to make parts of the Autoformer model more transparent, allowing practitioners to interpret the model’s reasoning and make targeted interventions if needed. The paper demonstrates that the proposed framework maintains interpretability with a minimal performance trade-off across six time-series datasets.

### Strengths
1. Novel Interpretability Framework: This work contributes a new direction in Transformer interpretability by combining Concept Bottleneck Models (CBMs) with the Autoformer, explicitly aligning model representations with interpretable concepts. 

2. Few Performance Trade-offs with Useful Intervention Property: Table 1 shows that while the Autoformer with bottlenecks generally has a slight performance trade-off, the interpretability improvements may be valuable in settings where transparency is essential. Additionally, the “Intervention” experiment (Lines 480-485) demonstrates a practical application of the framework, where a temporal shift intervention shows the model’s adaptability to new data distributions, a useful feature in evolving environments.

4. Potential Balance of Interpretability and Complexity: By modifying only a single layer to incorporate the concept bottleneck and aligning some heads with interpretable concepts, the framework achieves interpretability without overhauling the Transformer architecture. This approach makes the Autoformer’s components "easily intervenable," according to the authors, providing a possible solution for practitioners needing complex forecasting models with interpretable checkpoints.

### Weaknesses
1. Limitations in Granular Interpretability: CKA encourages global alignment of the bottleneck representations with the predefined concepts, which may not capture fine-grained temporal patterns that are essential in many time-series applications. In the CKA analysis (Figure 3), alignment scores reflect similarity with concepts on a broad level but do not offer insights at specific time intervals or for anomalies. This setup could limit interpretability for users who need detailed, time-specific insights. Extending the interpretability framework to capture these localized patterns would make the model’s insights more actionable. For instance, the framework may struggle to identify a sudden spike in a time series if that spike is not a dominant feature across the entire series, as the CKA score would average over the whole sequence, potentially masking the localized importance of the spike. This limitation is particularly relevant in anomaly detection tasks where precise temporal localization is crucial.

2. Interpretability Evaluation Metrics: The interpretability evaluation relies mainly on CKA scores and qualitative visualizations. Although CKA scores indicate alignment between model representations and interpretable concepts, they do not provide a full measure of "practical interpretability" from an end-user perspective. Incorporating metrics that measure interpretability in terms of clarity or usefulness for decision-making could make the framework’s impact clearer and more valuable. For example, a user-based study could evaluate how easily practitioners can understand the model's decisions and how effectively they can use the provided interpretations to make informed interventions. Metrics such as the time taken to understand the model's output or the accuracy of interventions based on the model's interpretations would provide a more direct measure of practical interpretability.

3. Applicability Across Different Models: Although the framework is applied to the Autoformer model, extending it to other more performant Transformer-based time-series models would confirm its generalizability. While the authors mention this as a possible future direction (Lines 530-531), this limits the scientific contribution of the work. The current implementation does not address whether the concept bottleneck approach can be effectively integrated into models with different architectural designs or attention mechanisms. This is a critical limitation as the effectiveness of the proposed approach may be tied to the specific architecture of the Autoformer. For example, models with more complex attention mechanisms might not be as easily aligned with the chosen interpretable concepts.

4. Model diagrams (Figure 1 and 2) and the CKA scores (Fig 3) could be presented more clearly. They often require frequent referrals back to the text and legend.

### Questions
1. Justification for Concept Bottleneck over Post-Hoc Methods: Could you clarify the specific advantages of using the concept bottleneck framework over post-hoc interpretability methods like SHAP, LIME, or attention-based visualizations in this time-series context? An expanded discussion would help in understanding the unique benefits of your approach for interpretability.

### Soundness
3

### Presentation
3

### Contribution
3
