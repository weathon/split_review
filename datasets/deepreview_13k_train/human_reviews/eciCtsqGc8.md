# Interpretable Pre-Trained Transformers for Heart Time-Series Data

- Decision: Reject
- Scores: 6, 8, 8

## Abstract
Decoder-only transformers are the backbone of the popular generative pre-trained transformer (GPT) series of large language models. In this work, we employ this framework to the analysis of clinical heart time-series data, to create two pre-trained general purpose cardiac models, termed PPG-PT and ECG-PT. We place a special emphasis on making both such pre-trained models fully interpretable. This is achieved firstly through aggregate attention maps which show that, in order to make predictions, the model focuses on similar points in previous cardiac cycles and gradually broadens its attention in deeper layers. Next, we show that tokens with the same value, which occur at different distinct points in the electrocardiography (ECG) and photoplethysmography (PPG) cycle, form separate clusters in high dimensional space. The clusters form according to phase, as the tokens propagate through the transformer blocks. Finally, we highlight that individual attention heads respond to specific physiologically relevent features, such as the dicrotic notch in PPG and the P-wave in ECG. It is also demonstrated that these pre-trained models are straightforward to fine-tune for tasks such as classification of atrial fibrillation (AF), and beat detection in photoplethysmography. For the example of AF, the fine-tuning took 11 minutes of computer time, and achieved the respective leave-one-subject-out AUCs of 0.99 and 0.93 for ECG and PPG within the MIMIC Perform AF dataset. In addition, the fine-tuned beat detector achieved a state-of-the-art F1 score of 98\%, as well as uniquely providing a beat confidence level which acts as a signal quality estimator. Importantly, the fine-tuned models for AF screening are also fully explainable, with attention shifting to regions in the context that are strongly indicative of atrial fibrillation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces two interpretable pre-trained transformer models (PPG-PT and ECG-PT) adapted from the GPT framework for analyzing heart time-series data from PPG and ECG signals.  The authors demonstrate that these models develop interpretable attention patterns corresponding to physiologically meaningful cardiac cycle features.

### Strengths
- Interpretability analysis on physiological time series
- The model was tested on two types of physiological time series: PPG and single-lead ECG.

### Weaknesses
1. The model's novelty is questionable, as the PPG-GPT has previously been explored across multiple tasks (Chen et al., 2024). It will be helpful to specify how the current work differs from it.
2. The manuscript does not compare models on different PPG or ECG tasks compared to previous PPG-GPT (Chen et al., 2024). The comparison with one baseline per PPG and ECG is mentioned only in the appendix. Importantly, the models are compared on performance using different setups.
3. The experiments have not been performed across multiple runs, so the variability (std or IQR) of the performance is not clear. Consider 5-fold or 5 seeds.
4. Consider additional metrics, for example, sensitivity, specificity, false-positive rate, false-negative rate, and F1 score for AF.
5. The majority of the paper focuses on interpretability. However, it is difficult for the machine-learning community to validate clinical utility claims that require experience in reading ECG or PPG. Have you collaborated with clinical experts to validate the interpretability claims? Could you provide more evidence that the examples you have shown guarantee the presence of AF?

### Questions
1: You have considered very clean datasets and samples; seeing the behavior across different noisy scenarios would be highly important. Since we could achieve very high performance on high-quality data with an F1 score of 0.96 with DeepBeat (Torres-Soto et al., 2020).

2: Attention maps as an interpretability tool have been successfully explored (Zhao et al., 2023). It needs to be clarified that you did something new methodologically; it seems more of an application. For example, you have details on using the `findpeaks` function in Matlab, but it is poorly structured overall. It would be great if you would summarize the methodology as a pseudocode and suggest choices.

- Zhao, Haiyan, et al. "Explainability for Large Language Models: A Survey." arXiv preprint arXiv:2309.01029 (2023).
- Torres-Soto, Jessica, and Euan A. Ashley. "Multi-task deep learning for cardiac rhythm detection in wearable devices." NPJ digital medicine 3.1 (2020): 116.

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
5

### Summary
This manuscript presents a novel approach to representation learning for heart time-series data (typically PPG and ECG in this work) using generative pre-trained transformers (GPTs). The idea comes from the NLP domain where GPTs have shown remarkable capabilities in learning representations from text data, and the fact that the (pre-)training process for GPTs is very simple, only next-token prediction, also motivated this work, as claimed by the authors. The authors conducted a very detailed attention mechanism analysis to interpret the learned representations of the pre-trained GPTs.

### Strengths
1. To the best of my knowledge, this is the first work that applies generative pre-training to representation learning for heart time-series data, where previously contrastive learning methods were the most popular (also inherited from other domains like voice recognition). This is a novel and interesting idea.

2. The attention mechanism analysis is very detailed and provides a clear understanding of the learned representations, and how the transformer layers work on the heart time-series data.

### Weaknesses
1. The datasets used in the experiments are not comprehensive enough. The authors used the CinC2020 dataset, which is superseded by the CinC2021 dataset. The latter dataset is more comprehensive and contains more data. Moreover, there are other larger datasets available, such as the CODE-15% dataset (https://zenodo.org/records/4916206), etc.

2. The authors did not compare their method in their numerical experiments with other representation learning methods, such as contrastive learning-based methods (for example CLOCS (https://proceedings.mlr.press/v139/kiyasseh21a/kiyasseh21a.pdf)), to show the effectiveness of their method.

3. Not enough downstream tasks are conducted to evaluate the learned representations (or the pre-trained GPTs).

### Questions
See the "Weaknesses" section.

### Soundness
3

### Presentation
2

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
The paper aims to use generative pre-trained transformer (GPT) framework to predict next token for ECG and PPG signals with a focus in interpreting the decision-making of these large language models. This was done through observing the behavior of the attention heads in different transformer layers and aggregating them. The experiments reveal that the next token generation looks cycles in the nearest past more than that of the farthest past in the context. Qualitative interpretation reveals the ECG and PPG GPT models look into important signal components. These GPT models were fine tuned for a downstream task of atrial fibrillation classification with interpretation highlighting irregular occurrence of a beat w.r.t. the previous beat which is interesting. Overall, the problem formulation is logical, methods are well designed and explained, and the discussion clearly articulates the explainability the GPT models can offer.

### Strengths
- Related GPT based interpretation studies for ECG and PPG exists in literature, but the experimentation carried out in this study is rigour and systematic in revealing the explanations for firstly, the generation of next token and finally, extend the idea for a downstream classification task.

- The idea of decoding attention head for explanations are common in the CV and NLP domain, but extending it to physiological time-series can be seen a contribution.

- Data split follows a subject-wise separation to avoid data leak in training and testing.

### Weaknesses
Major:
- The explainability method of GPT models was shown to focus on previous cycles meaning that it can observe a beat w.r.t the previous one which is why the downstream task interprets well where distance between two consecutive beat is important criteria. However, this might not be the case for other common tasks such as sleep staging where the input in 30 second ECG or PPG signal and separating sleep stages such as wake, light sleep, deep sleep and REM sleep manifests from HR variability. Another experimentation for a downstream task would be interesting to see if the proposed explainability idea fits well to provide clinical domain specific interpretation, given the fact that GPT models were found to be useful in these downstream tasks. Specifically, the model's reliance on short-term dependencies may limit its applicability to tasks requiring longer temporal context, such as sleep staging, where the relevant features manifest over minutes rather than seconds. The current interpretation method, focusing on immediate past cycles, might not capture the more subtle, long-term variations in heart rate variability that are crucial for differentiating sleep stages. This raises concerns about the generalizability of the proposed approach to other clinically relevant tasks beyond beat-to-beat analysis.

- Few related GPT interpretability studies were referenced. More references should be included to have a broad picture based on GPT interpretablity. For example, 
a. Creswell, A., Shanahan, M., & Higgins, I. (2022). Selection-inference: Exploiting large language models for interpretable logical reasoning. arXiv preprint arXiv:2205.09712.
b. Ben Melech Stan, G., Aflalo, E., Rohekar, R. Y., Bhiwandiwalla, A., Tseng, S. Y., Olson, M. L., ... & Lal, V. (2024). LVLM-Intrepret: an interpretability tool for large vision-language models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 8182-8187).

Minor:
- Figure 3 captions needs to be corrected a-d.

### Questions
- 10 second segments were extracted from recordings from where tokens were generated, are these tokens represent whole segment data or beats were isolated to form tokens?

- The prediction or generation of tokens from GPT models is unclear. Experiment says a single token is generated for a given context length, then it needs to be clearly mentioned how the generation process continued to generate to produce, say Figure 1, of 15 second PPG or ECG data which was compared against the original signal?

### Soundness
3

### Presentation
4

### Contribution
3
