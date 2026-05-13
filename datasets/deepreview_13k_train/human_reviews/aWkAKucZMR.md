# ShuffleMTM: Learning Cross-channel Dependence in Multivariate Time Series from Shuffled Patches

- Decision: Reject
- Scores: 5, 8, 6, 3

## Abstract
Masked time-series modeling has widely gained attention as a self-supervised pre-training method for multivariate time series (MTS). Recent studies adopt a channel-independent (CI) strategy to enhance the temporal modeling capacity. Despite the effectiveness and performance of this strategy, the CI methods inherently overlook cross-channel dependence, which is inherent and crucial in MTS data in various domains. To fill this gap, we propose ShuffleMTM, a simple yet effective masked time-series modeling framework to learn cross-channel dependence from shuffled patches. Technically, ShuffleMTM proposes to shuffle the unmasked patches from masked series across different channels, positioned at the same index. Then, Siamese encoders learn two views of masked patch representations from original and shuffled masked series, simultaneously capturing the temporal dependence within a channel as well as spatial dependence across different channels. ShuffleMTM pre-trains the Siamese encoders to reconstruct the original series by incorporating cross-channel information with intra-channel cross-time information. Our proposed method consistently achieves superior performance in various experiments, compared to advanced CI pre-training methods and channel-dependent methods in both time series forecasting and classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of capturing cross-channel dependencies in multivariate time series pre-training. Unlike previous channel-independent methods, the proposed model, ShuffleMTM, masks a multivariate instance to create an original masked view and then shuffles the channels within each time step to generate a shuffled masked view. The original view serves as the query, while the shuffled view serves as the key and value in a cross-attention decoder, with the objective of reconstructing the original instance. Experimental results demonstrate that ShuffleMTM outperforms several channel-independent baselines in both forecasting and classification tasks. Additional experiments assess its performance in limited data scenarios, robustness, and other settings.

### Strengths
1. The paper is well-structured and accessible, making it easy to follow.

2. The focus on capturing cross-channel dependencies in multivariate time series pre-training is both important and relevant.

3. A capacity-robustness analysis is provided, offering insights into the model’s forecasting accuracy as well as its robustness, training-testing gap, and other performance metrics.

### Weaknesses
1. Some crucial parts about the proposed model is missing: how to adapt the pre-trained model to downstream tasks. Is the shuffled view utilized during fine-tuning? If not, it is unclear how the channel-independent encoder effectively captures cross-channel dependencies. Specifically, if the encoder processes each channel independently during fine-tuning and inference, it is unclear how information from other channels influences the prediction of a given channel. For example, if one were to replace all other channels with pure noise during inference, would the prediction of the target channel be affected? If not, it suggests that the model is not truly capturing cross-channel dependencies.

2. The proposed shuffling method is  not straightforward. Why not simply apply 2D attention, as done in Crossformer, to the masked patches, or flatten the time series into a 1D sequence and use self-attention? What specific advantages does shuffling offer over these approaches, aside from efficiency? The paper does not provide a clear justification for the choice of shuffling over more established methods for capturing cross-channel dependencies.

3. The ablation study could be improved. The following experiment should be included: removing the shuffled view by using the original view as the query, key, and value in the decoder, and comparing this configuration with the proposed method, which uses the original view as the query and the shuffled view as the key and value. This would isolate the impact of the shuffled view on performance.

4. In the forecasting task, the lookback window is fixed to 96, which is shorter than the future window to forecast. It would be valuable to assess the model’s performance with an extended lookback window. This is especially important for long-term forecasting tasks, where a longer historical context might be necessary.

5. Please explain Section 6.1 in detail, including:
 - How to comupte the "self-attention map" and "patch-correlation" in patch-level dependence paragraph as there is no cross-channel attention in the proposed method?
 - How to compute the "channel correlations in the raw time series" in channel-level dependence?

### Questions
Please see the Weaknesses section for detailed questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a simple strategy called ShuffleMTM for handling multi-channel time series. During pre-training, time series patches are randomly masked and shuffled across channels. Two views of each channel's univariate time series (the first is the one after random masking, and the second is after both random masking and shuffling) goes into a Siamese encoder followed by a decoder that aims to reconstruct the raw input time series. The paper demonstrates that ShuffleMTM works very well in practice.

### Strengths
- The proposed strategy is well-explained and very simple.
- The experimental results of Section 4 show that ShuffleMTM works quite well in practice.
- I think the experiments in Sections 5 and 6 are very helpful in checking on the robustness of ShuffleMTM to various conditions (such as limited data, missing data, hyperpameters) and in capturing patch-level and channel-level dependence.

### Weaknesses
 - While ShuffleMTM is fairly simple to describe, I think the key question in my mind is, from a theoretical viewpoint, what sort of cross-channel structure can be captured by the specific shuffling performed, and what sort of cross-channel structure can *not* be captured. I think discussing this in more detail would really strengthen the paper. Just to give a simple example, suppose that the patch size is 1 so that each patch is just a single time step, and that it turns out that the true underlying structure is that each time step depends on *previous but not the current* time step's information in other channels. If I understand ShuffleMTM correctly, it seems like the shuffling done by ShuffleMTM in this case would not be helpful in capturing the cross-channel structure? Or maybe I'm misunderstanding something about ShuffleMTM? In any case, what I'm trying to do here is to just try to think of a setting where ShuffleMTM wouldn't work well (I'd guess that the authors could come up with various examples).
- Figure 2 I think is very important and helpful, but it took me some time to figure out what I am looking at. I'd suggest making the caption more descriptive and maybe adding some text (or some sort of drawing over the diagram) to better explain what is going on. If I understand the figure correctly, each colored cell is a patch. Blue/pink/green correspond to three channels. Gray cells are masked. Only some columns are randomly shuffled (I'm inclined to suggest that you circle or box the columns that were chosen for random shuffling across channels). Meanwhile, the two views that are inputs to the Siamese encoder correspond in this case to channel 1's data (actually stating this to be the case would be helpful to the reader).
- The experimental results would benefit from having error bars reported (such as standard deviation across some fixed number of experimental repeats with different random seeds) in Tables 1-4 and Figures 4-6. If there is a concern about tables becoming too large, one solution is to just defer, for instance, MAE results (with newly added error bars) to the appendix and keep MSE results (with newly added error bars) in the main paper.

Minor:
- There are a number of English grammar issues and typos. For example, in the first sentence of the introduction (line 33), the word "traffics" is used incorrectly. Perhaps this part of this first sentence can be reworded as "including energy, transportation, and medicine" (note that "medicines" here should be singular). At line ~66-67, "Unlike previous methods that recovers" should say "Unlike previous methods that recover". I'd suggest proofreading the paper carefully and using, for instance, a grammar checker.

### Questions
Please address the weakness points raised.

### Soundness
3

### Presentation
3

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
This paper proposes a simple time series masking modeling method based on a Siamese network and a specially designed decoder. It establishes the relationship between masked patches within a channel and shuffled patches across channels at the patch level, enabling learning of both intra-channel and inter-channel temporal dependencies. This approach demonstrated superior performance on the main temporal analysis task.​

### Strengths
- The proposed method effectively models temporal correlations and dependencies within and across channels through a simple yet effective masking approach.
- Comprehensive experiments and analyses support the method.

### Weaknesses
 - Limited generalizability: The method relies on a channel-independent time series model as the backbone, limiting its applicability to more advanced temporal models, especially those that inherently model inter-channel relationships. Specifically, the method's reliance on processing each channel independently before any cross-channel interaction limits its ability to leverage sophisticated inter-channel modeling techniques that operate directly on the multivariate series. This is a significant limitation, as many state-of-the-art methods utilize attention mechanisms or graph neural networks to capture complex relationships between channels from the outset, which this approach cannot easily integrate.

- The motivation of the paper could be more precisely stated. The CI method does not completely ignore inter-channel modeling; Rather, they construct these relations implicitly rather than explicitly, as multiple channels are simultaneously optimized in a single iteration. The current framing suggests that CI methods completely ignore inter-channel dependencies, which is not entirely accurate. A more nuanced explanation is needed to highlight the specific limitations of implicit inter-channel modeling in CI methods and how the proposed approach explicitly addresses these limitations at the patch level.

### Questions
- **Main Experiments**: 

Effectiveness should be validated on larger datasets. Numerous masking and generative pre-training methods, such as Moirai [1] and Timer [2], have achieved notable results on large-scale time series data. Comparisons of these approaches could shed light on the effectiveness of this mask modeling approach as data size scales, and whether it holds advantages over other unsupervised pre-training paradigms in larger data scenarios.​

- **Ablation Study**: 

The performance of ShuffleMTM is most likely affected by the masking ratio and the number of channels. The masking ratio controls the potential shuffled candidate locations, while the number of channels determines the diversity of patch replacements. A more detailed examination of their relationship is recommended. For example, on high-channel datasets (such as Traffic and ECL), it would be beneficial to explore how model performance changes with increasing masking ratios.

​Another ablation experiment could evaluate the effect of enforcing that the current position in one channel is always replaced by another channel during shuffling.​

[1] Unified Training of Universal Time Series Forecasting Transformers

[2] Timer: Generative Pre-trained Transformers Are Large Time Series Models

### Soundness
3

### Presentation
2

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
This paper proposes a simple method to improve the multivariate time series self-supervised learning paradigm. In order to capture cross-channel dependencies, it proposes method named ShuffleMTM, which first shuffle unmasked patch along the channel dimension for data processing, and secondly performs information extraction based on cross attention based on the original mask sequence and the shuffled mask sequence.

### Strengths
1. The problem is clearly defined and the method is clear and simple；
2. Experimental results show that although this method is simple, it brings certain gains on some data sets.

### Weaknesses
1. This paper lacks novelty. Except for the shuffle operation on the unmasked time series , the use of Siamese network does not give me a bright feeling. At the same time, as the author expressed, part of the work differs from patchstst in that the linear layer is replaced by the transformer decoder structure, which seems to be an operation driven by experimental results and has nothing novel.
2. This paper claims to enhance the prediction ability of multivariate time series by capturing cross-channel dependencies. However, in Table 1 we can find that the experimental results do not seem to prove this point. It is also a data set with strong channel correlation, and the weather dataset shows Good results, however, the electricity dataset and traffic dataset performed poorly. Firstly, experimental results prove that this method cannot capture cross-channel dependencies well. Secondly, it cannot prove that the improvements to other data sets are based on cross-channel information. Gains from extraction.
3. The method proposed in this paper has problems in the reasoning stage. In the training and verification stage, some data operations can indeed be performed through shuffle to improve model performance. However, in the reasoning stage, if the random seeds are different each time, then for the same input, due to the uncertainty of other channel patches introduced by the shuffle operation, the output results are inconsistent each time, which is unacceptable in real scenarios.
4. In the robustness exploration experiments based on different proportions of missing values, all selected baseline methods, including this paper, showed that as the proportion of missing values increases, the performance first decreases, and then the performance increases. The author does not give a reasonable explanation for this phenomenon.

### Questions
See Weaknesses

### Soundness
1

### Presentation
2

### Contribution
1
