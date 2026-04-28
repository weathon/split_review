# Large Pre-trained time series models for cross-domain Time series analysis tasks

- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 3, 5, 5, 3

## Abstract
Large pre-trained models have been vital in recent advancements in domains like language and vision, making model training for individual downstream tasks more efficient and provide superior performance.
However, tackling time-series analysis tasks usually involves
designing and training a separate model from scratch leveraging training data and domain expertise specific to the task.
We tackle a significant challenge for pre-training a foundational time-series model from multi-domain  time-series datasets:
extracting
semantically useful tokenized inputs to the model
across heterogenous time-series from different domains.
We propose Large Pre-trained Time-series Models (\model) that introduces a novel method of \textit{adaptive segmentation}
that automatically identifies optimal dataset-specific
segmentation strategy during pre-training.
This enables
\model to perform similar to or better than domain-specific state-of-art model
when fine-tuned to different downstream time-series analysis tasks and under zero-shot settings.
\model achieves superior forecasting and time-series classification results
taking up to 40\% less data and 50\% less training time
compared to state-of-art baselines.
Code: \url{www

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces an effective framework for pre-trained time series models and demonstrates strong empirical performance on diverse forecasting and classification tasks. The adaptive segmentation technique is a key contribution enabling learning from heterogeneous time series data.

### Strengths
Originality:

The idea of pre-training time series models on diverse datasets from multiple domains is highly original and innovative. This enables knowledge transfer and improves efficiency similar to language and vision domains.

The adaptive segmentation module for handling diverse time series dynamics during pre-training is a creative technique and novel contribution.

Clarity:

The paper is clearly structured and easy to follow. The problem context, proposed method, experiments and results are presented logically.

Technical details are clearly explained and intuition behind design choices is well-articulated.

Tables and graphs effectively summarize key quantitative results.

Significance:

This work makes important strides towards general pre-trained models for time series, which might have high impact if the quality is good enough.

The ideas could inspire more research into techniques for pre-training on diverse time series data.

### Weaknesses
This paper has some obvious limitations which may lead the reviewer tend to reject it:

The model architecture used is quite straightforward - just a transformer encoder. Exploring more sophisticated temporal modeling architectures, such as those incorporating recurrent layers or attention mechanisms with explicit temporal biases, could be beneficial. The current approach risks not fully capturing complex temporal dependencies present in time series data.

More in-depth analysis into the effect of pre-training like how the adaptive segments evolve could provide useful insights. For example, visualizing the learned segment boundaries across different datasets and analyzing the statistical properties of these segments (e.g., length distributions, variance) could reveal the underlying patterns captured by the model.

Ablations only evaluate the removal of components, could also analyze additions like other SSL tasks. The paper should explore other self-supervised learning tasks beyond masking and last token prediction, such as contrastive learning or predictive coding, to determine if these can further improve the learned representations.

Hyperparameter sensitivity analysis is limited - how do factors like segment score thresholds affect performance? A more thorough analysis of the sensitivity of the model's performance to the segment score thresholds is needed. This should include a systematic exploration of different threshold values and their impact on downstream task performance.

Though diverse, the pre-training datasets are still limited to a few domains. Expanding the data diversity could help. The current pre-training datasets, while diverse, may not be representative of all real-world time series data. The authors should consider including datasets from other domains, such as healthcare or industrial processes, to improve the generalizability of the model.

Theoretical analysis on how pre-training and adaptive segmentation provide benefits is lacking. The paper lacks a theoretical justification for the effectiveness of the pre-training and adaptive segmentation approach. A formal analysis, even if simplified, could provide insights into the conditions under which the proposed method is expected to be effective.

Comparisons to more sophisticated domain-specific models like those using additional covariates would be informative. The paper should compare the proposed method against state-of-the-art domain-specific models that utilize additional covariates, such as weather data or economic indicators, to better understand the limitations and potential of the proposed approach.

Analysis of computational requirements for pre-training is needed, especially regarding scaling up. The paper should provide a detailed analysis of the computational resources required for pre-training, including memory usage and training time, and discuss the scalability of the approach to larger datasets and models.

Testing on a wider range of time series analysis tasks like anomaly detection could help show broad utility. The paper should evaluate the proposed method on a wider range of time series analysis tasks, such as anomaly detection or time series imputation, to demonstrate the versatility of the learned representations.

Lack of analysis of any negative societal impacts or limitations of the approach.

Lack of baselines: for PEMS-Bays and METR-LA, we have STGNN, StemGNN, GraphWavenet and so on; for ETT dataset, we have PatchTST, FEDformer. Timesnet and so on. The lack of such important baselines makes this paper hard to position.

The word of "multi domain" is overused: the reviewer don't see the specific module for multi domain setting. However, the "a separate segmentation module for each dataset domains to capture varied sizes of segments that differ across datasets" in page 3 Section 3.1 limits the ability of generalization on this model.

### Questions
See Weekness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a model which can be pre-trained on multiple time-series from diverse domains and can perform a wide range of tasks. Their proposed model is trained by masking a proportion of time segments. The authors argue that uniform length segments cannot scale across datasets and tasks.

### Strengths
The paper attempts to pre-train a model which can solve multiple tasks on multiple time-series from diverse domains. To the best of my knowledge, this is amongst the first few studies which attempts to do this, demonstrating promising performance. 

I also appreciate that the authors compare their methods with some domain specific baselines.

### Weaknesses
I would encourage the authors to address the following to improve their paper: 

1. **Reproducibility:** While the code is available, many hyper-parameters important to reproduce the results are not mentioned in the manuscript. (1) As an example, the authors do not mention the proportion of time segments that they mask during self-supervised learning ($\gamma$). This is a critical parameter that significantly impacts the learned representations. The lack of this parameter makes it difficult to reproduce the results. (2) The number, length, ranges, number of channels etc. of time-series use for pre-training and evaluation are not mentioned either. Without these details, it's impossible to replicate the experimental setup. For instance, are the time series normalized? What is the range of values? Are the time series of different lengths, and if so, how are they handled? (3) Furthermore, the authors compare "training time (minutes) till convergence" but fail to mention the compute infrastructure, what kind of time (wall clock?) are they measuring. The type of hardware used (CPU, GPU, memory) and the specific time measurement (wall clock, CPU time) are crucial for a fair comparison. 
2. **Clarity:** The paper is unclear and many statements are not rigorously or scientifically define. For e.g., (1) the authors claim in Section 3.2, that their segment score function measures "how good the given segment is for the dataset", but do not clarify what the notion of goodness is? The notion of goodness is also not immediately clear as the authors use a hyperbolic Tangent function as the scoring function. The connection between the score and the quality of the segment for pre-training is not established. (2) The authors invoke $g(i, j)$ for the first time in Equation 4. Consequently, it appears to me it seems that the paper was put together in a hurry, without careful proof-reading. Also see Questions. 
3. **Claims:** The authors claim that variable sized segmentation is a key contribution of their work, but they only compare with time-step level segmentation. While they cite PatchTST, they do not compare with fixed length time-series segmentation, and hence it is unclear whether the contribution leads to significant gains over what seems to work (i.e. uniform time-series segmentation). A comparison with fixed-length segmentation methods is essential to justify the complexity of the proposed variable-length approach. 
4. **Baselines:** Some state-of-the-art forecasting baselines are missing, e.g., PatchTST and TimesNet from ICLR 2023, along with statistical forecasting methods such as AutoARIMA, AutoTHETA, AutoETS, Naive etc., and non-transformer-abed deep learning methods such as N-HITS and N-BEATS. The lack of these comparisons makes it difficult to assess the true performance of the proposed model. 
5. **Experimentation:** (1) A pre-trained model should be able to solve tasks without any fine-tuning, especially since all the training parts of the datasets are observed during pre-training. The authors should provide zero-shot results to demonstrate the generalizability of the pre-trained model. (2) For smaller datasets, a large model trained from scratch is destined to under fit. Since the authors have not mentioned the size of the model, beating LPTM trained from scratch on a small dataset can be attributed to the model being too big for a small dataset. A smaller model might very well learn from scratch. The authors should experiment with different model sizes to show that the pre-training is indeed beneficial and not just an effect of model size. 

Minor: 
1. Please fix the capitalization of the datasets. The diseases should be capitalized. 
2. Pease fix the citations using \citep or \cite, and \citet, whichever is appropriate.

### Questions
1. What is the size of the model? How many layers of transformer? What is the number of heads? What is the size of embeddings? 
2. What is $g(i, j)$ in Equation 4?
3. What is $\gamma$? How are the segments sampled? 
4. What are the key differences between this work and "PEMs: Pre-trained Epidemic Time-Series Models."?  
5. See questions in Weaknesses

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel method for pre-training time series models to be used in a wide range of downstream tasks.
The method relies on a segmentation of the input time series into possibly overlapping segments that are further encoded using self-attention.
A segment selection strategy is used to focus on most informative parts of the time series, and automatically select segment lengths.

### Strengths
The proposed method relies on a simple yet interesting idea that is to extract important segments of varying lengths from time series such that each segment will be treated the way a token is processed in standard NLP pipelines.
The high-level presentation of the method is rather accessible (though the technical details are much harder to grasp due to problems with the notations, see below) and the experiments tend to validate the choices that are made.

### Weaknesses
There are many mistakes in the notations that make it hard (or even impossible) to fully grasp what is done at places.
Below is a list of such issues:
* I do not understand the rationale behind Eq (4)
    * Why taking the log of the SSL loss? If the SSL loss tends to 0 (which is probably what one targets at the end of training), then its log will have large gradient values, hence leading to unstable training
    * What is $g(i, j)$ in Eq. 4? Do you mean $s(i, j)$? If so, why summing $\log(\mathcal{L}_{SSL})$ with the sum of scores?
    * Why does the score rely on $z_i$ (is it $z_i$ or $z^{(i)}$ by the way?) and $z_j$ but not the full sequence of $z$ between indices $i$ and $j$, since recurrent units are known to have hard time catching long-term dependencies (even GRU units, to some extent)
    * In Sec. 3.2, you write:
        > The score s(i, j) for a subsequence from time-stamp i to j denotes how good the given segment is for the dataset.
        * I do not understand this sentence. What does ``how good'' mean in this context?
        * Also, given that the loss that is optimized operates on the aggregation of all scores, it is not clear how it could enforce large scores for selected segments
* The use of $h(i)$ in Fig 1 is misleading, since it looks like $h(i)$ is the hidden representation for the $i$-th segment whereas in the text $h(i)$ is said to be the index of the last timestamp for the segment starting at time $i$, and it is said that some of these segments are pruned out, hence indices of the remaining segments should not be adjacent.

### Questions
Some questions are asked in the "Weaknesses" section, below is a list of additional ones:
* The text refers to "aggregation" but not much is said (in Sec 3.2 at least) on which aggregation function is used, why?

* How does your method compare to state-of-the-art methods (ie. ROCKET, COTE variants, etc.) that do not use pre-training on the given classification tasks?

>  While retrieving the optimal S(y(1...t)) is an interesting combinatorial optimization problem, [...]

Could you elaborate a bit more on this interesting combinatorial problem, does it have known solutions? Do you have a way to assess if your approximation is a reasonable one or not?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a cross-domain/dataset self-supervised learning approach to pre-train a time series model. They perform masked reconstruction with a Transformer architecture, introducing a dataset specific segmentation module to transform time series data into intermediate representations which are subsequently fed into the Transformer model. They pre-train the model on 7 datasets from various domains, and evaluate on forecasting and classification tasks.

### Strengths
This paper tackles the ambitious problem of cross-domain/dataset pre-training for time series to learn a general model for time series tasks. They successfully pre-train such a model across a variety of datasets, and show decent performance across tasks and datasets.

### Weaknesses
1. Writing can be greatly improved. Abstract should be 1 paragraph. Mathematical notation is not clear -- many variables are not defined.
2. Empirical comparisons are somewhat lacking. More recent baselines can be included (PatchTST, TimesNet for forecasting, CoST for self-supervised forecasting). More evaluation metrics can be presented (MAE, sMAPE, ...).
3. The usefulness of the model is diminished with the dataset specific segmentation module. The model is unable to perform zero-shot forecasting or prediction tasks.
4. Codebase in given link is incomplete. No script for training / predictions. README is empty, without instructions.

### Questions
-

### Soundness
2 fair

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a time series pre-training framework that leverages the concepts of patching and masked token reconstruction, both of which have been extensively studied and utilized in time series modeling. The authors specifically put forth an adaptive patch resampling aimed at better aligning time series patterns across various domains. While this paper is well-structured in general, the core contributions and technical novelty appear to be constrained. Some assertions within the manuscript lack sufficient evidence (refer to my detailed comments below). Additionally, the overall presentation could benefit from further refinement. On the experimental front, related & important baselines are absent and the main experiemntal setting is ill-defined. While time series pre-training holds potential and merits exploration, I believe this work requires substantial improvements before it is fit for publication.

### Strengths
- The motivation for time series pre-training is well established; I agree with the authors regarding the overall narrative.
- The proposed patch resampling is technically feasible, and the ablation studies demonstrate the effectiveness of this design.
- The overall pre-training & fine-tuning pipeline is well structured, with two important time series analytical tasks (i.e., forecasting and classification) undertaken.

### Weaknesses
 - The overall technical novelty is limited. The primary contribution of this work lies in the concept of patch scoring, as presented in Eq. 2, and the subsequent two paragraphs. The overarching design can be seen as an extension of PatchTST. In the realm of time series pre-training, several recent studies, such as SimMTM, have delved into the concept of masked patch reconstruction.

- The experimental settings are ill-defined. While this work emphasizes cross-domain adaptation, the evaluation datasets (& domains) substantially overlap with the source datasets (& domains) used in pre-training. I do not think this is a valid evaluation protocol for cross-domain adaptation.

- The presentation could benefit from further refinement. For example, Fig.1 offers limited information, and upon examining just this figure and its caption, I have several related questions unsolved. Furthermore, numerous claims and technical assertions are not adequately backed by evidence or in-depth discussion. Please refer to the questions I've enumerated below for further clarity.

- The claim that individual timestamps lack semantic meaning is not sufficiently justified. While individual time steps might not always capture high-level patterns, they certainly encode information about the signal's state at a given moment, similar to how individual tokens in NLP can carry semantic meaning, even if not complete. The analogy to NLP is not well-considered, and the argument needs more nuance.

- The method for combining data samples from different domains for pre-training is not clearly defined. The authors do not specify how they determine the optimal mix of data from various domains to maximize the pre-training effectiveness. This lack of detail makes it difficult to assess the robustness of the pre-training process.

- The paper does not adequately address how the proposed patch scoring mechanism (Eq. 2) would handle out-of-distribution samples from domains not seen during pre-training. The scoring function is trained on specific domains, and its effectiveness on completely novel domains is questionable. This is a critical limitation for real-world applications where data distributions can shift significantly.

- The term "how good" in the paragraph following Eq. 2 is vague and lacks a precise definition. The authors need to clarify what criteria they use to determine the "goodness" of segments. This ambiguity makes it difficult to understand the objective of the scoring function.

- The discussion on the differences between random masking and last token masking is superficial. The authors do not provide a deeper analysis of the impact of these masking strategies on the learned representations. A more thorough discussion of their respective advantages and disadvantages is needed.

- Fig. 1 remains unclear. The choice of GRU over a linear projection for the patch embedder is not adequately justified. The mechanisms of patch scoring and pruning are not well-explained. The meaning of h(1) to h(R) is ambiguous, and the self-supervised optimization process is not clearly illustrated. These issues make it hard to grasp the overall architecture and its training process.

- Several critical baselines, such as PatchTST, SimMTM, and TimesNet, are absent. Additionally, it would be advantageous to evaluate using datasets from domains not encountered during pre-training.

### Questions
**Questions & Detailed comments**

1. I question the validity of the claim, "... unlike text data, each individual timestamp may not provide enough semantic meaning about local temporal patterns of the time series." In natural language processing, doesn't a single token also sometimes fail to convey the full semantic information of a sentence?

2. Regarding the construction of the pre-training set, how is the optimal combination of data samples from different domains determined? I found no discussion on this in the experiment section.

3. How can Eq.2 effectively handle "out-of-distribution" samples from domains that were not encountered during pre-training?

4. I'm not sure about what the authors intend by "how good" in the paragraph following Eq.2.

5. In section 3.3, what are the fundamental differences between random masking and last token masking in time series pre-training? Is there any deeper analysis or extended discussion available?

6. Fig1 is confusing. After reviewing Fig1 and its caption, I have several related inquiries: Q1: Why choose GRU over a linear projection as the patch embedder? Q2: How do patch scoring and pruning operate? Q3: What do you intend by h(1) to h(R)? Q4: Where is the self-supervised optimization highlighted?

7. Several critical baselines, such as PatchTST, SimMTM, and TimesNet, are absent. Additionally, it would be advantageous to evaluate using datasets from domains not encountered during pre-training.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor
