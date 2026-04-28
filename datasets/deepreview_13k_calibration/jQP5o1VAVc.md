# Scaling Autoregressive Text-to-image Generative Models with Continuous Tokens

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Scaling up autoregressive models in vision has not proven as beneficial as in large language models.
In this work, we investigate this scaling problem in the context of text-to-image generation, focusing on two critical factors: whether models use discrete or continuous tokens, and whether tokens are generated in a random or fixed raster order using BERT- or GPT-like transformer architectures.
Our empirical results show that, while all models scale effectively in terms of validation loss, their evaluation performance---measured by FID, GenEval score, and visual quality---follows different trends. Models based on continuous tokens achieve significantly better visual quality than those using discrete tokens. Furthermore, the generation order and attention mechanisms significantly affect the GenEval score: random-order models achieve notably better GenEval scores compared to raster-order models.
Inspired by these findings, we train~\name, a random-order autoregressive model on continuous tokens. \name~10.5B model achieves a new state-of-the-art zero-shot FID of 6.16 on MS-COCO 30K, and 0.69 overall score on the GenEval benchmark. We hope our findings and results will encourage future efforts to further bridge the scaling gap between vision and language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper explores scaling autoregressive models for text-to-image generation, focusing on two key factors: discrete vs. continuous token representations, and token generation order (raster vs. random). The results show that using continuous tokens and generating in random order lead to better image quality, especially at scale. The new Fluid model, which adopts these strategies, achieves state-of-the-art results on benchmarks like MS-COCO and GenEval.

### Strengths
Solid Scaling Analysis: The paper does a thorough job of laying out the scaling trends. The consistent improvements with random order and continuous tokens give a clear picture of what’s working.

Concrete study on Toke type and Scan order: The results convincingly show that generating tokens in a random order outperforms the traditional raster order, especially for tasks needing a good global structure. Additionally, switching to continuous tokens noticeably enhances image quality.

This is a solid empirical paper that offers important insights into scaling autoregressive models, mostly on scaling the MAR model (Li et al., 2024). The work holds relevance for both academia and industry, with the potential for meaningful social impact.

### Weaknesses
Methodology Largely Follows MAR (Li et al., 2024): The approach in this paper closely follows the method used in MAR, with some modifications to incorporate text condition. While these changes are valuable, the paper doesn’t go far beyond what MAR already established. Also, the discussion of scan order and token type is also a repeat of what has been done in the MAR paper.

Over-Reliance on Empirical Results: While the paper does a great job presenting empirical evidence, there’s a lack of theoretical explanation for why continuous tokens outperform discrete ones. The benefits are demonstrated, but there isn't much discussion on how continuous representations help in practice—whether it’s due to better gradient flow, more expressive capacity, or something else entirely. More in-depth analysis could add substance to the findings.

Scaling Analysis Could Be More Comprehensive: The paper primarily showcases large model almost for sure improve the performance. However, other important factors in scaling, such as the effect of dataset size, are not thoroughly explored. For instance, language model research, like Kaplan et al. (2020), investigates how increasing dataset size influences validation loss, providing insights into the relationship between data and model scaling. In contrast, all the experiments in this paper are conducted on the same subset of the WebLI dataset, leaving the impact of different data sizes unexamined.

### Questions
1.	Is there any specific differences compared to MAR paper?
2.	Any thoughts on why random order generation works better than raster? Why continuous better than discrete? Would love to see more reasoning beyond the empirical results.
3.	How does the training time compare across setups, especially when scaling up?
4.	In the inference time, how does the inference time step influence the model performance?
5.	Is the method scales well for image resolution? For example, finetune the model on a small, but large-resolution dataset. Current diffusion model often works well for much larger resolution like 512 and 1024. The 256^2 image generated in the paper is somehow limited for real application. 
6.	A very important question for me is not confirming the scaling law of AR-based model for image generation(always, larger compute give better results). Rather, we are interested in comparing the diffusion model and the AR in term of the speed of scaling. This paper somehow demonstrates Fluid scales better than causal, discrete-token AR model. If it is possible, a comparing with pure diffusion model is very important.
7.	Are there any failure cases for the model? 
8.	Not exactly a research problem, but will the code be open-sourced? Because this paper is mostly an empirical study, sharing the code and model would be the most important contribution than reading the paper. I personally think this is a key consideration when judging this paper.
One minor suggestion: While using a random scan order prevents the typical use of KV caching for causal sequences, an alternative could be to adopt a structured order, such as a grid-like pattern. This way, you could still cache info from nearby patches and keep some benefits of caching while generating the current patch.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper investigates the scaling behaviors of autoregressive models in text-to-image generation, focusing on key factors: token type (discrete vs. continuous) and generation order (random vs. raster). Experiment results demonstrate a power-law relationship between the validation loss and model sizes, and that continuous tokens with random-order generation yield the best performance on evaluation metrics. Leveraging these findings, the authors introduce Fluid, a 10.5B random-order autoregressive model with continuous tokens, outperforming previous models on benchmarks such as FID and GenEval.

### Strengths
- Achieve SOTA performance with zero-shot FID of 6.16 on MS-COCO 30K, and an overall score of 0.69 on the GenEval benchmark.
- The paper is well-organized and easy to follow, with robust training data, strategies, and solid experimental setups.
- Extensive experiments reveal clear relations between the four configurations of token types and generation order.

### Weaknesses
 - This paper ablated two types of existing technologies, with their scaling behaviors. The experiments are well-designed, and the authors' observations appear reasonable. However, some additional insights are needed.
- I appreciate the authors' efforts in sharing extensive experimental results, but providing an actionable conclusion would add more value than observations alone. If the authors could provide insights or equations that can guide future training of large-scale text-to-image models—such as identifying optimal settings when constrained by FLOPs, image samples, or model size—it would significantly benefit the field.

### Questions
- My questions arise naturally from the "Weaknesses", I believe the authors may have more insights beyond the experiments results provided.
  - What underlying factors drive the observed correlation between metrics and the linear relationship between validation loss and the metrics?
  - What should be considered the most "human-aligned" evaluation criterion for future research?
  - More analysis of the benefits of the continuous tokens and random-order prediction should be explained, especially during the scaling up, e.g., why does random-order prediction yield a larger loss but better visual quality?
- Similar to the "Scaling Law" curves in the language model community, an ablation on the number of training examples across the four configurations could be beneficial.
- Is there any "Emergence" phenomena during training, such as a sudden increase in metric scores?
- I would consider raising my scores if these points are addressed.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work investigates the performance of autoregressive models in generating high-quality images from text prompts, focusing on the use of continuous versus discrete tokens and the impact of token generation order. The authors find that models using continuous tokens produce superior visual quality compared to those with discrete tokens, indicating that continuous representations capture more nuanced information. Additionally, they reveal that random-order generation outperforms fixed raster-order generation, highlighting the significance of the token generation sequence on image quality. Employing various evaluation metrics, the study compares its results with leading diffusion models and autoregressive models, reporting favorable outcomes. Overall, the research provides empirical insights into the scaling behavior of text-to-image generation models, emphasizing the importance of token representation and generation strategy in enhancing autoregressive models' capabilities for high-resolution image synthesis.

### Strengths
1. The writing in the article is clear and easy to understand. 

2. The improvements to the original autoregressive model, such as continuous token and random generation order, are both insightful and empirically effective techniques. These empirical results provide crucial experimental evidence that supports some of the fundamental beliefs about autoregressive image generation.

### Weaknesses
1. Although this article is the first to compare the roles of token representation and generation order together in the autoregressive image generation, the techniques it examines are not novel or originally proposed by the authors. For instance, line 189 notes that the continuous token method is derived from a prior work, and line 287 mentions that the implementation of random order also originates from an earlier study. This work does not optimize or update the technical details of these methods. I highly appreciate the article’s empirical study on autoregressive image generation, but the scope seems limited to experimental evaluation of existing techniques without introducing new methods or innovations.

2. Autoregressive image generation still lacks a standardized technical framework, and both its training and inference processes remain complex and non-standardized. The approach involves various technical details beyond just token representation and generation order. I highly appreciate the authors' efforts to highlight these two factors amidst the complexity. However, different token representations and generation orders introduce other technical variations, making it challenging to ensure absolute fairness in comparisons. For example, the use of a diffusion head for continuous tokens, while not applied to discrete tokens, introduces a potential confound. This limitation may prevent us from making strictly definitive claims based on the comparative results.

### Questions
1. In the experimental results presented in Figure 6, it seems that with the minimal number of parameters, continuous tokens do not outperform discrete tokens. Would the authors be able to provide further analysis on why this might be the case?

2. In the implementation of continuous tokens, an extra diffusion head is used, whereas no comparable diffusion structure is applied for discrete tokens. If possible, could the authors conduct further ablation studies to examine the impact of this diffusion head?

3. The authors also mention that these techniques vary not only in performance but in efficiency as well. Would it be possible to provide a more detailed comparison of inference efficiency?

### Soundness
3

### Presentation
3

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
This paper proposes an auto-regressive text-to-image generation model. The authors specifically explore two aspects, namely random order v.s. raster order and continuous token v.s. discrete token. Through experiments, the authors conclude that random order with continuous tokens is better. Evaluation on MS-COCO and GenEval benchmarks indicate better performance compared with previous diffusion-based and auto-regressive-based models.

### Strengths
1. This paper successfully scales previous auto-regressive models based on continuous tokens up to the text-to-image setting, which is more complicated and hard-to-train than class-conditioned models.
2. The quantitative results are good given the results in Tab. 1.
3. The paper is well-written and I am able to fully follow the authors' writing.

### Weaknesses
1. It seems that the novelty is limited. The applied techniques are essentially the same as those proposed in [a], which can hardly bring readers new technical insights. The overall feeling of the paper is more like a technical report instead of a research paper.
2. The resolution used in the paper is 256x256, which is relatively small compared with recent models. The training and evaluation of models at this resolution might not reflect the challenges and performance at higher resolutions, thus limiting the practical significance of the findings.
3. Also, I am not sure whether the comparison in Tab. 1 is fair because different systems may have been trained on different resolutions. This makes it difficult to assess the true performance gains of the proposed model.
4. LlamaGen [b] can serve as a recently proposed baseline for comparisons.
5. Lack of qualitative comparisons and efficiency comparisons with recent models. Readers can hardly get the strengths of the proposed model against state-of-the-art ones.

### Questions
See weaknesses.

### Soundness
4

### Presentation
4

### Contribution
2
