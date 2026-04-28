# LARP: Tokenizing Videos with a Learned Autoregressive Generative Prior

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 6, 8

## Abstract
We present \systemm, a novel video tokenizer designed to overcome limitations in current video tokenization methods for autoregressive (AR) generative models. 
    Unlike traditional patchwise tokenizers that directly encode local visual patches into discrete tokens, \system introduces a holistic tokenization scheme that gathers information from the visual content using a set of learned holistic queries. 
    This design allows \system to capture more global and semantic representations, rather than being limited to local patch-level information.
    Furthermore, it offers flexibility by supporting an arbitrary number of discrete tokens, enabling adaptive and efficient tokenization based on the specific requirements of the task.
    To align the discrete token space with downstream AR generation tasks, \system integrates a lightweight AR transformer as a training-time prior model that predicts the next token on its discrete latent space.
    By incorporating the prior model during training, \system learns a latent space that is not only optimized for video reconstruction but is also structured in a way that is more conducive to autoregressive generation. 
    Moreover, this process defines a sequential order for the discrete tokens, progressively pushing them toward an optimal configuration during training, ensuring smoother and more accurate AR generation at inference time.
    Comprehensive experiments demonstrate \systems strong performance, achieving state-of-the-art FVD on the UCF101 class-conditional video generation benchmark. \system enhances the compatibility of AR models with videos and opens up the potential to build unified high-fidelity multimodal large language models (MLLMs).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces LARP, a novel method for tokenizing videos for autoregressive (AR) generative models. LARP employs a holistic approach to capture global video information more effectively and incorporates an AR prior model to enhance video generation quality. The method demonstrates strong performance in generating high-quality videos and holds potential for developing models capable of integrating both video and language.

### Strengths
1. This paper introduces a novel method for video tokenization that moves beyond traditional patchwise encoding, making it both interesting and innovative.

2. The paper provides a comprehensive set of experiments, including video reconstruction, class-conditional video generation, and video frame prediction, effectively demonstrating LARP's capabilities across different tasks.

3. LARP achieves state-of-the-art FVD scores on benchmarks like UCF101, indicating that it is a competitive approach in the field of video generation.

### Weaknesses
1. The overall computational cost and complexity of training LARP, especially with the AR prior model, may be a concern.
2. It remains unclear how stable the training process is over longer periods or under different training regimes.
3. The paper may not sufficiently discuss scenarios in which LARP underperforms or fails, which is essential for understanding the model’s limitations.

### Questions
How does the training process scale with larger datasets or more complex video content?
What are the hardware requirements for training and deploying LARP?
Are there specific types of videos or scenarios where LARP may underperform, and if so, what are they?

### Soundness
2

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
The submission introduces LARP, a novel video tokenizer designed to optimize video tokenization for autoregressive (AR) generative models. The approach deviates from traditional patch-wise tokenizers by adopting a holistic strategy, which captures global and semantic representations of video content. This unique structure allows for adaptive tokenization, with a focus on enhancing AR compatibility through an integrated lightweight AR prior model. The experimental results show state-of-the-art performance in video generation benchmarks, particularly in UCF-101 and K600 datasets, establishing the proposed method as a competitive alternative for high-fidelity video synthesis.

### Strengths
* The proposed method addresses an interesting and important topic with great potential for multimodal LLMs - how to tokenize videos into a sequence of tokens more suitable for LLM learning.
* The introduced AR prior model is a simple yet effective method to produce tokens more friendly for autoregressive generation.
* Experiment results demonstrate the effectiveness of the proposed method in reducing the gap between generation quality and reconstruction quality, highlighting better learnability of the produced tokens.
* State-of-the-art performance is presented on the UCF benchmark, with K600 results outperforming AR baselines and ablation studies verifying key design choices.

### Weaknesses
 * While results have been presented on class-conditional generation and frame prediction tasks, the benefit or penalty from using the proposed method on other tasks such as video editing and stylization remains unclear. 
* While not being applied to videos before, the holistic token approach appears similar to [1] on images. The differences other than the AR prior part need to be clarified.

### Questions
* What are the differences between the proposed holistic tokenization approach and [1] beyond the AR prior part? Could the authors clarify from the aspects of input/output format, model architecture, training objective, etc.?
* Would the holistic tokens hurt the appearance preservation capabilities in editing tasks such as inpainting and outpainting?
* In the K600 frame prediction benchmark, what is the input to the LARP encoder at inference time? Could the authors clarify how to handle 5-frame condition with the patch size described in Sec. 4.1?

[1] Yu et al. An Image is Worth 32 Tokens for Reconstruction and Generation. arXiv 2406.07550

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
This paper presented a novel video tokenization technique for autoregressive video generation. It leveraged several query embeddings to gather information from input videos, which enabled the tokenizer to capture more global representations and support arbitrary number of tokens. It further integrated a lightweight autoregressive transformer model as a prior during training of the tokenizer, which can result in a better latent space for downstream autoregressive video generation. This paper also presented experimental results on the effectiveness of the proposed tokenizer when applied to video generation tasks.

### Strengths
- This paper presented an inspiring message that properly considering the downstream video generation tasks when training video tokenizers can result in much better generation performance.
- Extensive experiments and ablations demonstrated the effectiveness of incorporating the autoregressive prior to tokenizer training.

### Weaknesses
 - There are several typos in the paper:
    - line 270: “back to the continues” -> “back to the continuous”
    - line 459: “hilighting” → “highlighting”
- More ablation studies can be conducted to analyze the effectiveness of holistic video tokenization and autoregressive generation further, as detailed in the Questions section.


### Questions
- As claimed and validated in the paper, an autoregressive prior is critical to improve generation performance. In this paper, it is implemented by leveraging an additional autoregressive transformer model. As presented in line 251, this paper used a transformer encoder architecture as a video tokenizer. If this transformer encoder is replaced by an encoder-decoder structure, will it serve as an autoregressive prior?
- Could the authors further explain why an autoregressive prior during tokenizer training can lead to better generation performance? An argument is that, lower autoregressive prior loss does not necessarily lead to better generation performance, since in an extreme case, if all the tokens are the same, then the autoregressive prior loss can be extremely low, but the codebook will collapse and the downstream generation task will definitely fail.
- This paper introduced the holistic video tokenization technique implemented by query-based transformers. Without this holistic video tokenization technique, the autoregressive prior can also be applied to the “patch tokens” as in Figure 2 (a). Despite the flexibility of supporting an arbitrary number of discrete tokens, the claim of “global and semantic representations” seems not validated in the paper. Are there experimental results supporting this claim?
- Table 1 shows the reconstruction comparison among different tokenizers. With 1280 tokens, the rFVD of MAGVIT-v2 is 8.6. With 1024 tokens, the rFVD of LARP-L-Long is 20. Since the tokenizer presented in the paper can support an arbitrary number of discrete tokens, what will the rFID be if 1280 tokens are used?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a video tokenizer for autoregressive (AR) generative models. The authors find that existing tokenizers use only patchwise tokenization without effective ordering, and face the design gap between reconstruction and AR generation. To address both limitations, they propose a new tokenizer with two key designs: (1) holistic tokenization that gathers information with learnable queries; (2) a lightweight AR transformer that optimizes the latent space for AR generation. Based on the proposed tokenizer, the authors trained a set of AR video generative models that achieve competitive performance on the Kinetics-600 and UCF-101 datasets.

### Strengths
* The paper is generally well written and easy to follow.
* The authors provide an insightful analysis of the two limitations of AR tokenization, and the proposed tokenizer with AR prior effectively addresses these limitations.
* Extensive quantitative and qualitative results are presented to support the effectiveness of the proposed method in video generation.

### Weaknesses
 * The first contribution (holistic tokenization) is similar to TiTok [1] in that they both use learnable queries to tokenize the input data into a 1d sequence. This somewhat weakens the contribution of the paper. It would be better if the authors could detail their design differences in this part and justify the advantage of these differences through experiments. Specifically, the paper should clarify the differences in the query initialization, the attention mechanism used to aggregate information, and the specific loss functions used to train the tokenizer. A detailed comparison of these aspects with TiTok [1] would strengthen the novelty claim.
* For the second contribution (AR prior model), there is no analysis of its accuracy or generalizability. Otherwise, it seems to me difficult for a small 21.7M AR model to predict the next tokens in a highly complex video latent space. The previous work VideoPoet [2] and Video-LaVIT [3] all require a 7B+ LLM to achieve this. The paper should include an analysis of the AR model's prediction accuracy on held-out data, and also explore the impact of varying the AR model's capacity on the overall generation performance. Without these analyses, it is difficult to assess the true contribution of the AR prior.
* Since the work focuses on generation performance, it would be better to introduce more metrics other than FVD, such as FID and IS. These metrics are also commonly used on UCF-101 and will significantly increase the soundness of the paper. The paper should also provide a clear justification for the choice of FVD as the primary evaluation metric, and discuss the potential limitations of relying solely on this metric. A more comprehensive evaluation using multiple metrics would provide a more robust assessment of the proposed method.
* There is a lack of intuitive analysis of the learned AR prior and latent space in the paper. Adding additional visualizations of the token ordering (e.g., by heatmap) would help readers understand how it actually works in the overall procedure. Otherwise, readers can only infer its functionality by looking at the performance improvement. The paper should also provide visualizations of the latent space, such as t-SNE plots, to show the distribution of tokens and their relationship to video content. This would give a better understanding of the learned representations.

### Questions
* My main question after reading the paper is: The video data is already nicely ordered by timestamps, why not use this ordering directly for tokenization? Does the learned tokenizer reflect this natural order in its latent space? If not, I think the video tokenizer might be suboptimal.

### Soundness
2

### Presentation
2

### Contribution
3
