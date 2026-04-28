# See What You Are Told: Visual Attention Sink in Large Multimodal Models

- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 3, 6, 6

## Abstract
Large multimodal models (LMMs) "see" images by leveraging the attention mechanism between text and visual tokens in the transformer decoder. Ideally, these models should focus on key visual information relevant to the text token. However, recent findings indicate that LMMs have an extraordinary tendency to consistently allocate high attention weights to specific visual tokens, even when these tokens are irrelevant to the corresponding text. In this study, we investigate the property behind the appearance of these irrelevant visual tokens and examine their characteristics. Our findings show that this behavior arises due to the massive activation of certain hidden state dimensions, which resembles the attention sink found in language models. Hence, we refer to this phenomenon as the visual attention sink. In particular, our analysis reveals that removing the irrelevant visual sink tokens does not impact model performance, despite receiving high attention weights. Consequently, we recycle the attention to these tokens as surplus resources, redistributing the attention budget to enhance focus on the image. To achieve this, we introduce Visual Attention Redistribution (VAR), a method that redistributes attention in image-centric heads, which we identify as innately focusing on visual information. VAR can be seamlessly applied across different LMMs to improve performance on a wide range of tasks, including general vision-language tasks, visual hallucination tasks, and vision-centric tasks, all without the need for additional training, models, or inference steps. Experimental results demonstrate that VAR enables LMMs to process visual information more effectively by adjusting their internal attention mechanisms, offering a new direction to enhancing the multimodal capabilities of LMMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates "visual attention sinks" in LMMs. The authors pointed out that LMMs often allocate disproportionate attention to certain visual tokens, termed "visual sink tokens," regardless of their relevance to the corresponding text. This paper proposes Visual Attention Redistribution (VAR), a method that identifies and reallocates attention from these sink tokens to more pertinent visual information, enhancing model performance across various vision-language tasks. The authors demonstrate VAR's effectiveness without requiring additional model training.

### Strengths
1. The identification of visual attention sinks draws parallels with attention sinks in language models, providing a novel insight into the functioning of LMMs.
1. Overall well written and easy to follow. Fig 1 and Fig 2 provide a clear and strong motivation. Fig 3-5 also provide a step-by-step motivation and the design choices of the proposed method.
1. The method improves performance across multiple benchmarks, including general vision-language tasks, visual hallucination tasks, and vision-centric tasks.
1. The paper evaluates VAR on a wide range of benchmarks and conducts a series of quantitative and qualitative analyses, validating the effectiveness of the proposed VAR method.

### Weaknesses
1. The reviewer's biggest concern is about the determination of hyperparameter $\rho$. According to the paper and Fig 7(b), it is benchmark-dependent. Furthermore, a poorly chosen $\rho$ can lead to performance worse than the baseline performance. This parameter greatly limited the applicability and generalizability of the proposed method.

2. The tuning of $\rho$ on the benchmarks to find the best value is problematic and is against the principle of machine learning.

### Questions
1. Do newer LMMs with anyres and with visual encoder tuned jointly also have the characteristic of visual attention sinks? Do the observation and analyses generalize across LMMs with different language models and sizes?

1. In Fig 8, it looks like LLaVA + VAR has more visual sink tokens qualitatively.

1. Please include the reference of LLaVA-1.5-HD-13B.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper explores the phenomenon of visual attention sinks in large multimodal models (LMMs). It identifies that these models often allocate high attention weights to irrelevant visual tokens during text-image processing, similar to "attention sinks" observed in language models. This issue results in diminished attention to crucial visual information, which can hinder the model’s multimodal understanding. To address this, the authors propose a method called Visual Attention Redistribution (VAR), which reallocates attention from irrelevant "sink" tokens to relevant visual tokens. The VAR approach first identifies image-centric attention heads that naturally focus on visual content, then redistributes the excess attention from sink tokens to strengthen attention on the actual image content.

### Strengths
- Insightful Identification of Visual Attention Sink: The authors make an important discovery by identifying the phenomenon of visual attention sinks in LMMs, showing that these models often allocate high attention weights to irrelevant visual tokens. This observation highlights a key inefficiency in multimodal attention mechanisms and contributes to a deeper understanding of model behaviors.

- Effective Attention Redistribution Technique: The proposed Visual Attention Redistribution (VAR) method is both innovative and practical. By reallocating attention from sink tokens to relevant visual tokens, VAR improves focus on key image content, enhancing multimodal model performance without additional training or inference overhead, making it easily applicable across different LMMs.

- Broad Experimental Validation Across Tasks: The paper rigorously validates VAR across a range of multimodal tasks, including visual question answering, visual hallucination reduction, and spatial understanding tasks. This broad evaluation demonstrates the robustness and adaptability of the method, showcasing its effectiveness in various vision-language scenarios.

### Weaknesses
 - The results in Figure 4(a) are essential for validating the effectiveness of the sink token filtering strategy, yet they are challenging to interpret. If the randomly selected tokens are drawn from all input tokens, comparing them with visual sink tokens becomes less fair, making it difficult to substantiate the filtering's effectiveness. Conversely, if the random tokens are sampled exclusively from visual tokens, the experimental results appear unreasonable. Even without visual input, the model’s accuracy on the POPE benchmark should remain above 50%, yet the figure shows a final result of 0. Furthermore, when $\tau < 10$, the tokens being pruned are predominantly standard visual tokens. Despite this, a significant difference in F1-Score persists between the two pruning strategies, contradicting the results seen when $\tau > 10$. Without a clear explanation of the experimental findings in Figure 4(a), the credibility of the sink token filtering strategy is undermined.

- The scope of the attention redistribution strategy remains ambiguous. Specifically, which tokens are targeted by this strategy? In practice, attention redistribution could apply to both input instruction tokens and output tokens, but the implementation should align with the analytical findings. If the strategy is applied only to specific tokens, it is crucial to specify how these tokens are selected; if applied to all output tokens, the analysis should demonstrate stable consistency in the attention assigned to sink tokens. However, this consistency is not currently evident in the analysis.

### Questions
1. In Figure 1, does the attention map show the attention scores between visual tokens and a specified text token, or between visual tokens and the output token?

2. In the experiment shown in Figure 4(a) on the POPE benchmark, are the "random tokens" randomly selected from only the visual tokens? If not, and they are instead selected from all tokens, wouldn’t this comparison be unfair? If the tokens are indeed chosen only from visual tokens, how is it possible that the model's predictions drop to zero when masking all visual tokens? On the POPE dataset, LLaVA can maintain over 50% accuracy even without image input, so this experimental result is difficult to understand.

3. Regarding the selection of image-centric attention heads, is the VAR strategy applied to all text tokens, or only to specific text tokens, or only to output tokens? If the experiment aligns with the analysis that VAR strategy only applied to specific object token, like "clock" in "Is there a clock in this image?", how are these particular tokens identified? If applied to all text tokens, is the visual token sink phenomenon consistent across all text tokens, which seems unlikely?

4. During inference, is the attention redistribution performed layer by layer? Specifically, does the forward pass first obtain original results, identify image-centric attention heads, then update attention weights, and proceed with attention weight redistribution in the next layer? 

If the author can address my second and third questions, I will raise my rating.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies the phenomenon of visual sink tokens in large multi-modal models. That is, the model allocates high attention scores to visual tokens irrelevant to the corresponding text, and these visual tokens consistently appear in fixed locations. This paper finds that visual sink tokens have high activations in specific dimensions, which provides a way to distinguish them from normal tokens. Furthermore, the paper proposes to recycle the attention to meaningful tokens, helping to improve model performances on a wide range of tasks.

### Strengths
1. The presentation is really good, first analyzing the property and effects of visual sink tokens, then providing a solution based on these investigations. The figures are also nice to explain relevant concepts and methods.
2. While the phenomenon of sink tokens has been discussed in language models[1] and vision models[2], this paper further extend it to multi-modal models.
3. The proposed method is simple yet effective. The model can be modified without further training.

[1] Xiao, Guangxuan, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis. "Efficient Streaming Language Models with Attention Sinks." In The Twelfth International Conference on Learning Representations.

[2] Darcet, Timothée, Maxime Oquab, Julien Mairal, and Piotr Bojanowski. "Vision Transformers Need Registers." In The Twelfth International Conference on Learning Representations.

### Weaknesses
1. Insufficient references. There is a work [1] on sink tokens in vision models that is not cited or discussed.
2. Insufficient discussion on sink tokens. Sink tokens have been observed in different kinds of models, including language models, vision models, and multi-modal models. What's the relationship between sink tokens in different kinds of models? Are they just similar phenomenons, or are there special properties of multimodal models? Moreover, previous works claim that sink tokens exist because of excessive attention scores, so why does it work to recycle these attention scores? From the experiment perspective, the paper is also encouraged to apply previous methods to multi-modal models.
3. Heavy hyper-parameter tuning for specific tasks. It seems that different tasks are highly sensitive to the selection of $\rho$. Then is there a train/val/test dataset split? If not, are these hyper-parameters tuned according to the test set? Will these hyper-parameters overfit the test set?

### Questions
1. As mentioned in the weakness, the paper should discuss the relationship between sink tokens in language models and vision models, from the perspective of token properties, emerging mechanisms and proposed methods.
2. How does the method determine which layer to apply VAR? The supplementary shows that there are less visual sink tokens in the first layer. However, the experiments say that VAR is not applied to the last layer. That does not sound reasonable.

### Soundness
4

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors introduce the phenomenon of visual attention sinks and, through visual analysis, propose that visual attention sink tokens are typically unrelated to the main visual subject information. Furthermore, they demonstrate through experiments how to automatically identify visual sink tokens. Based on this finding, the authors propose a method that utilizes attention budgets to redistribute attention weights. Extensive experiments have shown that this method optimizes both the general visual capabilities of models and the issue of hallucination.

The paper makes two main contributions:
1. It introduces the phenomenon of visual attention sinks and analyzes the behavior of LVLMs.

2. The proposed method enhances the performance of LVLMs with low cost.

### Strengths
1. The writing in this paper is very clear, smoothly transitioning from the introduction of the visual attention sink phenomenon to its analysis and the subsequent methodological approach.

2. The concept of visual attention sink proposed in this paper is indeed a direction worthy of deeper exploration within the realm of LVLMs.

3. The experiments in this paper cover a comprehensive range of content and consistently achieve stable improvements across various tasks.

4. The method proposed in this paper is an optimization based on the attention mechanism, making it generalizable and applicable to most LVLMs for experimentation.

### Weaknesses
1. The phenomenon of visual attention sink appears to be similar to the summary tokens proposed in OPERA[1]. Summary tokens imply that higher attention weights are assigned to tokens without semantic information, such as ',' and '\n'. The visual sink token seems to suggest that within visual tokens, there are also some tokens that play a similar role to summary tokens.

2. The analysis of the visual attention sink phenomenon lacks experimental validation. For more specific explanations, please refer to Question 1.

3. Although the author's evaluation experiments cover a comprehensive set of benchmarks, there is a lack of evaluation across more LVLMs and a detailed analysis of the experimental results. For more specific explanations, please refer to Question 2.

### Questions
1. Regarding the questions of visual attention sink:

   1.a. I have previously experimented with removing the <bos> token, and the attention sink phenomenon still persisted in the first token. Therefore, I am curious whether new tokens will become visual sink tokens after redistributing the attention weights.

   1.b. The author has visualized tokens with high attention weights in the text, and indeed, for these cases, the visual sink tokens are unrelated to the main subject of the image. However, I believe it is still necessary to prove the trend of visual sink tokens being unrelated to the main subject of the image on a large-scale dataset based on segmentation data.

   1.c. In Table 4.a, the selection of random tokens does not seem to be related to $\tau$, so I want to confirm whether two masked methods with the same $\tau$ value mean that the same number of tokens are masked.

2. Regarding the questions of experimental results:

   2.a. The author only chose LLaVA and VILA for evaluation, but the training data for LLaVA is much smaller compared to high-performance open-source models. Therefore, it is necessary to add one or two such models for evaluation, such as Qwen2-VL and InternVL2.

   2.b. LLaVA-HD has several times more image tokens compared to LLaVA, so I speculate that the author's model should perform better on this backbone. However, from Table 1, it appears that the improvement of the proposed method on LLaVA-HD is not as significant as on LLaVA.

If the author can address these concerns, I will consider raising the score. Additionally, I believe that further analysis on how to utilize this phenomenon during model training could enhance the impact of the article.

### Soundness
3

### Presentation
3

### Contribution
2
