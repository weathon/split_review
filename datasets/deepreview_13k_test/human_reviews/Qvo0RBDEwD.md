# Efficient Time Series Processing for Transformers and State-Space Models through Token Merging

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
Transformer architectures have shown promising results in time series processing. However, despite recent advances in subquadratic attention mechanisms or state-space models, processing very long sequences still imposes significant computational requirements. Token merging, which involves replacing multiple tokens with a single one calculated as their linear combination, has shown to considerably improve the throughput of vision transformer architectures while maintaining accuracy. In this work, we go beyond computer vision and perform the first investigations of token merging in \textit{time series analysis} on both time series transformers and state-space models. To effectively scale token merging to long sequences, we introduce \textit{local merging}, a domain-specific token merging algorithm that selectively combines tokens within a local neighborhood, adjusting the computational complexity from linear to quadratic based on the neighborhood size. Our comprehensive empirical evaluation demonstrates that token merging offers substantial computational benefits with minimal impact on accuracy across various models and datasets. On the recently proposed Chronos foundation model, we achieve accelerations up to \SI{5400}{\percent} with only minor accuracy degradations.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work presents a form of token merging to speed up transformers (and state-space models), particularly large and foundational models trained in the time-series domain. It generalises the token merging technique presented by Bolya et al at ICLR 2023 by allowing specifying the number of tokens to be merged (Fig 1, Sec 3), referred to in this work as "local" token merging.

Much of the work is dedicated to studying and analysing the method and presents insightful findings (Figs 2-7; 8-13). The experiments include five architectures on five datasets (many-to-many experiments). The method is shown to speed up inference, which increases with larger models and model architectures, with little to no deterioration in output quality (Tab. 1).

### Strengths
1. Firstly, this work addresses a problem relevant to the field in general: attempting to reduce computational complexity of the widespread transform-based and SSM models. Though similar efforts to this end have been made earlier, this work presents some interesting findings, such as choosing larger models with token merging are preferable to smaller ones without (Fig 3) and those trained with token merging scale better to longer observations (Fig 6).
2. The ability of this method to enable its application on models at inference time without having to retrain them with local token merging makes it very applicable. The improved output quality on some smaller models (Tab. 2) is an added strength.
3. This method shows speedup in training while performing comparably to a counterpart trained without token merging (L305). In addition, performance of models so trained without the token merging during inference not sacrificing accuracy is an added incentive to generally consider using this technique.

### Weaknesses
1. Obviously, as with the original token merging and its subsequent forms, this method inherits the one same major downside: that of somewhat degraded performance. The more tokens that are merged, the faster the model performs, but the quality of the also tends to decline, and this seems to be a tradeoff (Tab. 2)
2. Another weakness is induced by the nature of the problem: time-series. In order to ensure that tokens are merged while causal relationship between observations is maintaining, setting $k = 1$ in the decoder restricts it from merging a wider set of tokens.
3. Converse to Strength 1, while the relevance of this work is broad, little analysis is done with the representations learnt: namely, the possible use of other measures of similarity measures for merging and unmerging, and the resulting impact on downstream tasks.
    
    * For instance, if my understanding is correct (see Question 5), it would make more sense to use a quantitatively informed measure to choose tokens to further merge/retain as is, such as measuring the informativeness of tokens or using better heuristics for merging [4]

4. How would this technique translate to video such as human gait analysis or datasets like EPIC Kitchens [3], for example, all time-series? Is there a reason for not experimenting on videos which still offer the causal, time-series essence? Because, such datasets are sufficiently long temporally, offering to provide more insights into Fig 4. (A recent, relevant work [5] might be of interest).
5. Another serious weakness I find is lack of comparison to other token merging algorithms. Have the authors applied current merging algorithms ([1, 2]) to time series just for comparison?

### References

1. Xie, Enze, et al. "SegFormer: Simple and efficient design for semantic segmentation with transformers." Advances in neural information processing systems 34 (2021): 12077-12090.
2. Tran, Hoai-Chau, et al. "Accelerating Transformers with Spectrum-Preserving Token Merging." arXiv preprint arXiv:2405.16148 (2024).
3. Damen, Dima, et al. "Scaling egocentric vision: The epic-kitchens dataset." Proceedings of the European conference on computer vision (ECCV). 2018.
4. Choi, Joonmyung, et al. "vid-TLDR: Training Free Token merging for Light-weight Video Transformer." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.
5. Lee, Seon Ho, et al. "Video token merging for long-form video understanding." (2024).

### Questions
1. Piggybacking on Strength 3, L305 shows speedup in training Autoformer. Is
   this a general trend for all architectures (that have been experimented
   with)?
2. Have other measures of similarity been experimented with (L1, L2, etc)?
3. L021: What is the reason behind suggesting that the local token merging is
   domain-specific? Wouldn't allowing 1 < k < l/2 and relaxing the requirement
   that the tokens must be subsequent make the local ToMe still relevant to
   other domains?
4. Would it be fair to say that Sec 5.5 and Fig 5 support the suggested
   hypothesis provided the datasets (ETTh1, etc) are ridden with considerable
   noise? If this question is invalid, L402/403 that applying token merging plus
   Gaussian leading to the best result is confusing: if on the one hand the
   filter seems to exacerbate the results, and on the other ToMe improves it,
   how come a combination yields the best result?
5. L190: What is meant by "the most recent token"? The token corresponding to
   the latest positional encoding? If that assumption is true, wouldn't it be
   profitable to merge based on a priority, where older tokens are forced to
   merge first?
6. L199: I might have missed this, but if unlike Bolya and Hoffman, how is
   "split a merged token into two neighbouring identical ones" done?

### General comments

* I quite like the separation of the meat of local merging away from the
  experiments. But I found the paragraph from 228-238 somewhat disorganised.
  Starting with "We utilise different merging strategies in transformer encoders
  and decoders" would have make the paragraph clearer to read further. It might
  make a coherent writeup for this paragraph to have generic statements
  (L233-236) in the beginning and specific details afterwards. [This is merely a
  suggestion and not part of any review assessment].

### Soundness
3

### Presentation
4

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
The authors propose an efficient, customized token-merging strategy tailored for time-series processing in transformer and state-space models. Unlike the "global" token-merging methods used in image domains, the proposed "local" token-merging approach is more efficient and better preserves the causality crucial to time-series tasks. Experimental results demonstrate the efficiency of the proposed method with minimal performance drop across various datasets. Additionally, the method shows the applicability in practical experiments for both transformer-based and state-space model (SSM) approaches.

### Strengths
The method is simple, efficient, and effective. Experimental results demonstrate its superior acceleration across datasets and its applicability to both small-scale and large-scale models. Additionally, I appreciate the ablation study, which effectively illustrates the merging patterns and highlights where the proposed method succeeds or falls short.

### Weaknesses
My main concerns lie with the clarity of the writing. It is unclear how the authors merge the tokens—are they using averaging, max-pooling, or another method? I believe this should be explained and ablated, especially in relation to temporal issues and handling time-position embedding during token merging. These aspects are not sufficiently clear. Additionally, the authors mention an "unmerging" technique, but it is also unclear how this process is conducted

Furthermore, it is essential to conduct an ablation study on the parameter k to demonstrate the robustness of the proposed method.

### Questions
1. See the weakness.
2. I like the dynamic merging results it indeed can improves the FLOPS but I wonder whether it can improve throughputs or latency? The authors should validate it. Besides, it should be able to combine with merging during training setting since the k even can be learned during training.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces local token merging, a dimensionality-reduction method for very long sequences that can be used to lower the computational cost of training and/or inference in such domains.
Compared to prior work in token merging, the proposed method can be constrained to a local radius (which allows fine-grained control over the computational complexity of the merging process itself), and can be performed in causal manner to support autogressive decoding.
The experiments apply the proposed local token merging to a variety of Transformer and non-Transformer models across a variety of time-series datasets (long sequences but low feature dimensionality), and show that substantial speedup can be achieved at little-to-no detriment to the model accuracy, even when local token merging is only applied during inference.

### Strengths
The presentation of the motivation, proposed method, and experiments is clear and easy to understand. The experiments are thorough for the presented scope, evaluating the proposed method across a variety of model architectures/sizes, and datasets/domains. I appreciate the investigation into why local token merging sometimes improves model performance, as this may seem surprising from a first glance.

### Weaknesses
The proposed method does not feel like a significant contribution towards the broader goal of more efficient modeling of very long timeseries data. The paper demonstrates the effectiveness of local token merging compared to global token merging, but the experiments/discussion do not effectively place it into the broader context.

I contextualize the proposed method with prior work into two ways:

(1) Methods that can be applied to existing models with no additional training. In this category, I can see the appeal of local token merging, as the experiments show a substantial reduction in computational cost at similar prediction accuracy. However, it seems to me that if applying local token merging is effective in this fashion, then that is an indication that the underlying signal does not contain very much "useful" information (could be either low entropy or low signal-to-noise ratio). This calls into question how broadly applicable this technique can be, if it can only be applied to certain types of data (even within a particular category like "timeseries data"). The comparison between local token merging and gaussian smoothing (Section 5.2; When does token merging improve model performance) exemplifies this point, as local token merging can be viewed as an "adaptive smoothing filter", whereas the gaussian filter requires a fixed window size. Even if it has limited applicability, local token merging could still have be a useful contribution, but then some insight into when/why it is applicable would be helpful to understand its impact.

(2) Methods that are incorporated during training. From this lens, local token merging can be viewed as a particular type of adaptive pooling layer. However, once the model architecture is in scope, then the set of alternatives to local token merging becomes very larger, and the experiments conducted in the paper are not sufficient to evaluate learned token merging in this context. I am particularly curious about more expressive/universal methods like learned tokenizers (continuous VAE for diffusion models [1], discrete autoencoders for multimodal LLMs [2, 3]), which offer significant compression with near-lossless reconstructions. There even exist tokenizers where the degree of compression/dimensionality reduction can be adaptive [4, 5]. One could imagine training a tokenizer (either continuous or discrete) on the timeseries datasets evaluated in this paper, and such a tokenizer could learn a compression algorithm tailored to the timeseries domain, and could employ domain-specific reconstruction metrics analogous to the perceptual losses [6] typically used for images/video. This could potentially outperform local token merging, and the cost of tokenizer training & inference is typically much less than that of the base model.

[1] R. Rombach, et al. High-Resolution Image Synthesis with Latent Diffusion Models. CVPR 2022.

[2] L. Yu, et al. MAGVIT: Masked Generative Video Transformer. CVPR 2023.

[3] D. Kondratyuk, et al. VideoPoet: A Large Language Model for Zero-Shot Video Generation. ICML 2024.

[4] Q. Yu, et al. An Image is Worth 32 Tokens for Reconstruction and Generation. arxiv: 2406.07550.

[5] W. Yan, et al. ElasticTok: Adaptive Tokenization for Image and Video. arXiv:2410.08368.

[6] R. Zhang, et al. The Unreasonable Effectiveness of Deep Features as a Perceptual Metric. CVPR 2018.

### Questions
Following the discussion from the the "weaknesses" section:

(1) How can we understand when local token merging will perform well or not? Are there properties of the target dataset/domain that are particularly amenable or hostile to local token merging? Does this change when it is applied only during inference vs also during training?

(2) When training is in scope, how does local token merging compare against other model architectures (e.g. tokenizer + Transformer) that similarly reduce the effective input dimensionality? Depending on the results, what is the broader significance/utility of token merging?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a token merging technique for time series analysis aimed at improving efficiency. Compared to the global token merging technique (e.g., ToMe), the proposed method reduces merging complexity from quadratic to linear.

### Strengths
The paper proposes a token merging scheme for time series analysis and uses extensive experiments to demonstrate the efficiency improvements. Overall, the structure of the paper is clear, and the writing is well-done.

### Weaknesses
1.	Originality: The proposed token merging method is straightforward, and similar techniques have been explored in previous works, such as Crossformer (https://openreview.net/forum?id=elZoduqPe8) and CARD (https://openreview.net/forum?id=MJksrOhurE). The claim in the abstract that this paper "performs the first investigations of token merging in time series analysis" seems inaccurate.
2.	Complexity: The linear complexity regarding tokens applies only to the token merging process (which is also the case for existing token merging schemes), rather than to the entire model. This limits the contribution of the paper.
3.	Method: The method section seems too brief and lacks sufficient details, such as how the tokens are merged—are they concatenated or summed?
4.	Experiments:
(1) The naïve token merging method merges k neighboring tokens. Why not compare it with the proposed method?
(2) Large pre-trained models: The proposed method is primarily tested on Chronos. What about other large pre-trained models, such as Timer? 
(3) Small models: Regarding efficiency, why not compare with linear-based or CNN-based forecasters (e.g., DLinear)?
(4) Table 1: The base models presented do not seem to include the latest models. What about CARD (ICLR 2024) or Leddam (ICML 2024)?

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
