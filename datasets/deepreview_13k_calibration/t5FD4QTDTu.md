# Generalizable autoregressive modeling of time series through functional narratives

- Decision: Reject
- Avg Score: 4.80
- Scores: 8, 3, 5, 3, 5

## Abstract
\vspace{-3mm}
  Time series data are inherently functions of time, yet current transformers often learn time series by modeling them as mere concatenations of time periods, overlooking their functional properties. In this work, we propose a novel objective for transformers that learn time series by re-interpreting them as temporal functions. We build an alternative sequence of time series by constructing degradation operators of different intensity in the functional space, creating augmented variants of the original sample that are abstracted or simplified to different degrees. Based on the new set of generated sequence, we train an autoregressive transformer that progressively recovers the original sample from the most simplified variant. Analogous to the next word prediction task in languages that learns narratives by connecting different words, our autoregressive transformer aims to learn the Narratives of Time Series (\ours) by connecting different functions in time. Theoretically, we justify the construction of the alternative sequence through its advantages in approximating functions. When learning time series data with transformers, constructing sequences of temporal functions allows for a broader class of approximable functions (e.g., differentiation) compared to sequences of time periods, leading to a 26$\%$ performance improvement in synthetic feature regression experiments. Experimentally, we validate \ours~in 3 different tasks across 22 real-world datasets, where we show that \ours~significantly outperforms other pre-training methods by up to 6\%. Additionally, combining \ours~on top of existing transformer architectures can consistently boost the performance. Our results demonstrate the potential of \ours~as a general-purpose dynamic learner, offering a viable alternative for developing foundation models for time series analysis.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Narratives of Time Series (NoTS), a transformer-based framework that reinterprets time series data as temporal functions, capturing both local and global properties of time series through a novel pre-training objective. The authors introduce three main innovations:

Progressive Functional Degradation: NoTS generates simplified versions of time series by applying degradation operators that progressively smooth the signal. Each degradation level creates a coarser function, enabling the model to learn time series as a sequence of simplified functions rather than individual time points, preserving the functional structure over time.

Autoregressive Transformer with Next-Function Prediction: Inspired by next-word prediction in NLP, NoTS trains the transformer to reconstruct the original time series from its degraded variants. By predicting the next function in a sequence, each step adds more information, allowing the model to capture nuanced temporal dependencies across multiple scales.

Adaptation via Channel and Task Adaptors: NoTS includes adaptable modules to handle different time series tasks and varying channel structures, which improves model generalization and reusability across datasets. These adaptors support context-aware adaptation and help the model perform well with minimal parameter updates, making it versatile across tasks.

Experiments and Analysis:
The authors begin by presenting a theoretical analysis that shows standard transformers struggle to generalize when applied to time series tasks that involve complex operations, such as differentiation, due to their reliance on discretized data. Specifically, the authors prove that transformers encounter high approximation errors when attempting to model certain mathematical operations (e.g., differentiation) on time series. Authors also prove that their proposed method viewing time series data as continuous functions in "function space" rather than as discrete can enable the transformer to better capture the underlying properties of the time series.

NoTS is evaluated on both synthetic and real-world time series datasets, covering tasks such as classification, imputation, and anomaly detection. NoTS demonstrates strong performance across diverse datasets, outperforming established baselines such as masked autoencoders and next-period prediction models. Ablation studies further validate the importance of each component, and scalability experiments indicate that NoTS’s performance improves predictably with model size, in line with power-law trends seen in other fields like NLP.

### Strengths
- The borrowed functional narrative approach is innovative for time series modality, addressing key limitations in time series modeling due to discretization. By leveraging function-based degradations, NoTS effectively captures temporal relationships, making it a strong framework for autoregressive analysis.

- Clear theoretical grounding in approximation theory supports the functional degradation and autoregressive prediction framework. Visualizations (e.g., degradation sequences) help convey complex concepts effectively.

- Experimental results show NoTS’s robustness across diverse tasks and datasets, with context-aware adaptors allowing minimal retraining. These adaptors facilitate handling different channel mappings and task-specific nuances, enhancing practical application.

### Weaknesses
 - The paper lacks an analysis of how sensitive NoTS is to the choice of the degradataion operators or guidance on selecting appropriate ones. This dependence could impact performance if the degradations are not well-suited to certain datasets or applications. The ablation study could be improved by including more ablation tests on this aspect.

- While NoTS is evaluated on classification, anomaly detection, and imputation, it lacks experiments on long-horizon forecasting tasks, which are crucial for assessing a model’s ability to capture long-range dependencies and temporal features (as highlihted in the intro). This addition would also reinforce the paper’s motivation, presented in the introduction, which critiques patch-based transformer architectures focused on forecasting tasks (e.g., Moirai and Lagllama).


### Questions
- Could the authors provide an analysis on how sensitive NoTS is to the choice of degradation operators? Specifically, how does the performance vary when different types of degradation operators are used, or when the balance between local and global smoothing is adjusted?
- Is there any guidance the authors could offer on selecting suitable degradation operators for different datasets or applications? A more detailed ablation on this aspect would clarify the robustness of NoTS across varying conditions.
- Is there any limitations sourced from the pretraining objective that stops authors testing on the forecasting task? If not do the authors plan to evaluate NoTS on long-horizon forecasting tasks? Given that capturing long-range dependencies is highlighted as a core strength in the introduction, an assessment on forecasting (especially long-range) would provide valuable insights.
- Could the authors provide an analysis of how NoTS’s performance contribution varies with increasing time series lengths? Understanding how NoTS scales with longer time series would be valuable for assessing its capability to capture long-range dependencies and its potential applications to extended temporal data.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a pre-training method for time series data called Narratives of Time Series (NoTS). NoTS frames time series modeling by considering time series samples as a sequence of functions rather than a sequence of time periods. NoTS utilizes degradation functions to generate augmented variations of a time series signal. These augmented signals have varying degrees of simplification and together form a sequence that is used to train an autoregressive transformer. The authors provide theoretical justification for framing time series as functional sequences, showing that this approach can approximate a broader class of functions compared to traditional segmentation into periods. The authors validate NoTS on a variety of tasks, including classification, anomaly detection, and imputation, using both synthetic and real-world datasets.

### Strengths
- Originality: the notion of "Narrative of Time Series" by predicting the "next function" in a functional decomposition of the time series is interesting and modestly novel. However, it is strongly patterned after the N-BEATS decomposition (see below), and links and connections to this earlier literature should be made.
- Quality: The experimental results are interesting, although the validity of results is called into question (below).
- Clarity: The paper is at times hard to follow, in particular with respect to notational sloppiness and shortcuts taken in detailing the model.

### Weaknesses
 - Eq. 1 is sloppily written for the case $i=1$
- Section 2.1: there should be more rigor in the notation. The paper mixes discrete and continuous time, and does not specify how discrete time indices map onto functional arguments in continuous time. For instance, the notion of a "calendar" containing this mapping could be introduced. 
- Since the functional representation of time series is so important to the paper, Section 2 lacks a survey of the rich literature on the topic, e.g. from the Gaussian processes literature (e.g. https://proceedings.neurips.cc/paper/2007/hash/81e74d678581a3bb7a720b019f4f1a93-Abstract.html ) and classical statistics (e.g. “Functional Data Analysis” by J.O. Ramsay and B.W. Silverman (1997)).
- The proposed decomposition is strongly reminiscent of the N-BEATS approach, which is not acknowledged. The paper should contrast and compare their proposed approach to N-BEATS:
```
@inproceedings{
Oreshkin2020N-BEATS:,
title={N-BEATS: Neural basis expansion analysis for interpretable time series forecasting},
author={Boris N. Oreshkin and Dmitri Carpov and Nicolas Chapados and Yoshua Bengio},
booktitle={International Conference on Learning Representations},
year={2020},
url={https://openreview.net/forum?id=r1ecqn4YwB}
}
```
- Line 142: "Typically, each dataset has its unique channel-wise relationships" ==> not clear what this sentence means. The notion of 'channel' is not rigorously defined in the context of the functional representation. It is unclear if this refers to different time series within a multivariate dataset, or something else.
- If the discrete-time signal is obtained by sampling at irregular intervals or contains missing data, discuss how convolution operations would work for the degradation function. The paper assumes regularly sampled data, but this is not always the case in real-world scenarios. The authors should address how their method handles such situations, or explicitly state the limitations of their approach.
- Line 256: "encoder produces groups of tokens from each signal" ==> not clear how the signal is chunked into tokens in the first place. Is it through a PatchTST-like mechanism, or some other approach? The paper lacks detail on the tokenization process, which is crucial for understanding how the time series data is fed into the transformer.
- Lines 264-265: The specifics of this model should be given (perhaps in appendix), or a citation provided. The overall data flow, ranging from tokenization, encoder, decoder is very hand-wavy and hard to follow. The paper needs to provide a more detailed description of the model architecture, including the specific layers and their configurations.
- Lines 282-283: The argument made to explain the addition of the latent consistency term is not clear and should be further explained. The motivation for this loss term is not well-justified, and the paper needs to provide a more intuitive explanation of its purpose.
- Section 3.3, test-time adaptors: it is not clear whether these adaptors enable zero-shot handling of new time series, or if adaptor fine-tuning is required. The paper should clarify the role of the adaptors and whether they require any training on the target dataset.
- Eq. (3) specifies that the absolute error is used as the training loss. This makes the model sensitive to the scale of the time series — if the series are not scale-normalized, training will overweight series with the largest absolute magnitude. Further, section 5.2 does not discuss this issue, which calls into question the validity of experimental results. The paper does not address the potential impact of different scales in the time series data on the training process and results.

### Questions
- Line 142: "Typically, each dataset has its unique channel-wise relationships" ==> not clear what this sentence means.
- If the discrete-time signal is obtained by sampling at irregular intervals or contains missing data, discuss how convolution operations would work for the degradation function.
- Line 256: "encoder produces groups of tokens from each signal" ==> not clear how the signal is chunked into tokens in the first place. Is it through a PatchTST-like mechanism, or some other approach? 
- Lines 264-265: The specifics of this model should be given (perhaps in appendix), or a citation provided. The overall data flow, ranging from tokenization, encoder, decoder is very hand-wavy and hard to follow.
- Lines 282-283: The argument made to explain the addition of the latent consistency term is not clear and should be further explained.
- Section 3.3, test-time adaptors: it is not clear whether these adaptors enable zero-shot handling of new time series, or if adaptor fine-tuning is required.
- Eq. (3) specifies that the absolute error is used as the training loss. This makes the model sensitive to the scale of the time series — if the series are not scale-normalized, training will overweight series with the largest absolute magnitude. Further, section 5.2 does not discuss this issue, which calls into question the validity of experimental results.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces NoTS, a novel pre-training framework that reinterprets time series data through a functional lens. The framework constructs alternative sequences through two types of degradation operators: local smoothing (using averaging kernels with lengths $p_k$) and global smoothing (using sinc functions with frequency cutoff values $0.5p_k$), which create progressively simplified variants of the original signal while preserving functional properties.

The pre-training works by training an autoregressive transformer to recover increasingly detailed versions of the signal. A channel-independent encoder first converts each degraded signal $S_k$ into token groups $R_k$, then the transformer predicts the next resolution level using previous levels, with a decoder reconstructing the predicted signals. The training combines an AR reconstruction loss comparing $S'_{k+1}$ with $S_k$ and a latent consistency term for the original signal.

For real-world deployment, NoTS uses channel adaptors (linear layer, retrainable channel tokens) and task adaptors (prompt tuning, task-specific linear layers) requiring <1% new parameters while maintaining 82% performance. Experiments across 22 datasets spanning classification, anomaly detection, and imputation tasks are evaluated.

### Strengths
1. Reformulates time series modeling from a functional perspective and introduces degradation operators to create multiple views.
2. Proposes autoregressive modeling between resolution levels instead of traditional next-time-point prediction.
3. Provides function approximation analysis for transformer limitations on time series.

### Weaknesses
1. Limited Scope of Evaluation
- While the paper's focus on generalizable time series modeling, the crucial forecasting task is missing. The next-time-point prediction paradigm has clear connections to dynamic evolution, but the benefits of resolution-based prediction for forecasting tasks remain unexplored. This gap makes it difficult to fully assess the method's practical advantages. Specifically, the paper does not address how the functional degradation approach aligns with the temporal dependencies crucial for forecasting, and whether the learned representations effectively capture these dependencies. The lack of evaluation on standard forecasting benchmarks like those in the Time Series Forecasting Library (TSFL) further limits the assessment of its practical utility.
- Performance improvements are moderate except for classification tasks. The reported gains in anomaly detection and imputation are not substantial enough to demonstrate a clear advantage over existing methods. The paper should include a more thorough comparison with state-of-the-art methods in these areas to better contextualize the performance of NoTS.
- Limited datasets for imputation task. The ETT datasets are homogenous, and the model’s performance should be evaluated across other commonly used datasets as well, like Electricity and Weather. The lack of diversity in the imputation datasets makes it difficult to assess the generalizability of the approach. The paper should include datasets with varying characteristics, such as different sampling rates, noise levels, and data distributions.
- Limited ablation studies on key components. It would be better to show the impact of different degradation operators, degradation levels, and frequency cutoff points $p_k$ and diverse real-world datasets as well. The paper lacks a systematic analysis of how the choice of degradation operators and their parameters affects the performance of the model. For example, the impact of varying the kernel sizes for local smoothing and the cutoff frequencies for global smoothing should be explored in detail. Furthermore, the interaction between these parameters and different datasets should be investigated.
2. Minor parts:
- Technical clarification is needed on loss alignment choices, embedding usage for downstream tasks, and prompt tuning plan. The paper does not provide sufficient detail on how the embeddings from the pre-trained model are used for downstream tasks. For example, it is unclear whether the embeddings are directly used or if additional layers are trained on top of them. The prompt tuning strategy also lacks clarity. The paper should elaborate on the structure and organization of the prompt tokens, and how they are integrated into the model.

### Questions
1. Which embeddings from the pre-trained model are used for downstream tasks? 
2. While following Jia et al. (2022), the adaptation of visual prompt tuning to time series data requires a more detailed explanation. Time series-specific prompt token structure and organization should be elaborated.
3. Please justify the alignment of $S_{k+1}'$ with $S_k$ in the loss function rather than $S_{k+1}$. The alternative of matching with $S_{k+1}$ should be discussed.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a novel approach to time series analysis by treating data as functions of time. It introduces a pre-training framework called NoTS, which uses degradation operators to create augmented data, allowing an autoregressive transformer to learn interrelationships among functions. Experimental results show that NoTS outperforms existing methods across various tasks on synthetic and real-world datasets. Additionally, a lightweight model, NoTS-lw, is introduced, achieving high performance with minimal training parameters. Overall, the work emphasizes the benefits of a functional perspective in enhancing time series modeling.

### Strengths
The method shifts the focus from traditional time series modeling to viewing data as functions of time, which enhances the understanding of temporal dynamics. The NoTS framework effectively utilizes degradation operators to create augmented data, improving the learning process for autoregressive transformers.

### Weaknesses
While the paper demonstrates the effectiveness of the NoTS framework across various tasks and datasets, the experimental validation is primarily focused on a limited number of synthetic and real-world datasets. This raises questions about the generalizability of the findings. The performance of the proposed method in more diverse and complex scenarios, such as high-dimensional time series or those with significant noise, remains untested. Expanding the range of datasets and tasks could provide a more comprehensive evaluation of the model's robustness and adaptability; The introduction of degradation operators and the functional perspective may complicate the implementation of the NoTS framework. Practitioners may find it challenging to adapt the proposed methods to their specific use cases without a deep understanding of the underlying theory. This complexity could limit the accessibility of the framework for researchers and practitioners who are not well-versed in advanced time series modeling techniques, potentially hindering its adoption in real-world applications; Although the paper discusses the scalability of the NoTS-lw model, it does not provide extensive insights into how the framework performs with significantly larger datasets or more complex models. The scalability of the approach in terms of computational efficiency and memory usage is crucial for practical applications, especially in industries dealing with large-scale time series data. Without thorough analysis and benchmarks on scalability, it is difficult to ascertain whether the proposed methods can be effectively utilized in resource-constrained environments or for large-scale deployments.

### Questions
1, How does the NoTS framework compare to traditional time series modeling techniques in terms of interpretability and ease of use for practitioners who may not have a strong background in advanced machine learning methods?

2, What specific strategies could be implemented to enhance the scalability of the NoTS framework for large-scale time series datasets, and how might these strategies impact the performance and computational efficiency of the model?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes NoTS, a novel autoregressive pre-training method for time series. NoTS reinterprets time series as sequences of temporal functions generated by applying degradation operators of varying intensity levels to the original time series. The authors propose a "next-function prediction" task analogous to the next-word prediction task in language modelling and demonstrate the superior performance of NoTS on synthetic and real-world datasets.

### Strengths
* The proposed approach of next function prediction for time series pretraining is novel and very interesting. The authors motivate their method very well. The authors bring a very different perspective for modelling time series.
* The implementation of their approach with degradation operators is also well-theoretically justified. The authors theoretically show that degradation operators avoid the problem of discontinuities when time series are broken up into functions.

### Weaknesses
 * Clarity: I am unable to understand many parts of the paper due to unclear presentation; especially relating to the empirical evaluation of the method.  

* Evaluation: The protocol used for evaluation in Sec 5.2 is very much unclear. There are several references to Wu et al (2022) but the authors should not expect a reader to look into another paper, especially for the protocol of experimental setup, and the paper should be self-contained. I don't understand the protocol used even after looking into the paper. Do you pretrain on another dataset? If so, which dataset?

* Insufficient details on the training time, cost etc: It would be important to add the cost of using the architecture, both during pretraining and finetuning. In terms of training time / inference time / number of parameters etc.

### Questions
* Line 104: "giving a consistent performance boost when performing dataset-specific pre-training" - I don't understand what is dataset-specific pretraining. I have only heard of pretraining on a large dataset, and then dataset specific adaptation. Please clarify.

* Line 123: "trained while maintaining 82% average performance" - average performance on what? is it the pretraining dataset? it should be made clear.

* Line 294: "In time series domain, it is common to encounter datasets with new channel graphs or new tasks at test time. To apply the pre-trained weights in such situations, we build two types of adaptors" - you should give evidence (cite a paper) or provide an example for the first sentence. I don't understand what is meant by "encountering new channels at test time". 

* Line 303: "We initialize and append prompt tokens to the transformer architecture along with data tokens following the deep visual prompt tuning plan as detailed in Jia et al. (2022)". Again, the authors should not expect a reader to look into another paper for such a crucial aspect of the model. I did not understand this part; the authors must explain the mechanism better.

* How sample-efficient is your model (does it do well few-shot)? Experiments like these can potentially substantiate your contribution.

* Why not test on the forecasting task too, which is, equally or maybe even more important than classification/imputation tasks?

### Soundness
2

### Presentation
2

### Contribution
2
