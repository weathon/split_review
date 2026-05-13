# To FP8 and Back Again: Quantifying Reduced Precision Effects on LLM Training Stability

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
The massive computational costs associated with large language model (LLM) pretraining have spurred great interest in reduced-precision floating-point representations to accelerate the process. As a result, the BrainFloat16 (BF16) precision has become the de facto standard for LLM training, with hardware support included in recent generations of accelerators. This trend has gone even further in the latest processors, where FP8 has recently been introduced. However, prior experience with FP16, which was found to be less stable than BF16, raises concerns as to whether FP8, with even fewer bits than FP16, can be a cost-effective option for LLM training. We argue that reduced-precision training schemes must have similar training stability and hyperparameter sensitivities to their higher-precision counterparts in order to be cost-effective. However, we find that currently available methods for FP8 training are not robust enough to allow their use as economical replacements. This prompts us to investigate the stability of reduced-precision LLM training in terms of robustness across random seeds, learning rates, and datasets. To this end, we propose new evaluation techniques and a new metric for quantifying loss landscape sharpness in autoregressive language models. By simulating incremental bit reductions in floating-point representations, we analyze the relationship between representational power and training stability with the intent of aiding future research into the field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors explores what happens when large language models (LLMs) are trained using FP8 precision, meaning only 8 bits are used for floating-point numbers. FP8 is theoretically cheaper, but it introduces significant instability compared to BF16, the precision currently preferred for these models. The authors introduce a new metric to measure training stability by examining "loss landscape sharpness," which helps predict when training might diverge. They found that FP8 limits the range of hyperparameters that work, reducing its potential cost-savings. Overall, FP8 isn’t quite suitable yet for full-scale LLM training without further stabilization methods.

### Strengths
1. It’s got this new loss landscape sharpness metric that basically acts like an early-warning system for training issues, spotting instability before it even shows up in the loss curve which helps predict when training might go off-track.

2. Unlike some of the latest studies that stick to small-scale models, this paper actually dives into FP8 precision with full-size LLMs, so the findings are more practical and closer to real-world training needs.

3. They tried out reducing bits both on exponent and mantissa, making it unique since other papers usually just mess with mantissa bits, giving a fuller picture of how bit reduction affects training stability.

4. The paper shows in real-world training that FP8 doesn’t handle hyperparameters as well as BF16, which limits its ability to actually save money in training, something that hasn’t been looked into much in other studies.

5. By using TinyLlama for their experiments, this study connects the theory of low-bit precision with real stability checks, giving a strong framework for researchers wanting to make low-precision training more stable in LLMs.

### Weaknesses
 - The study mostly measures training stability by focusing on loss landscape sharpness and tracking divergence in training loss, which is useful but doesn’t fully reveal how well the model would perform on real-world tasks like NLP benchmarks. This narrow focus on training metrics rather than practical testing limits the broader application of the findings in real scenarios.

- They mention computational limits for testing with exponent bits, so they mainly tried reducing bits without exploring the impact of increasing them. Some recent research suggests adding exponent bits could help stabilize FP8, leaving an area of potential solutions unexplored.

- Because running full-scale experiments is costly, they used smaller models like TinyLlama to approximate larger ones. But recent studies point out that these smaller models don’t always behave the same as big ones like GPT-3, so the results might not directly translate to large-scale models.

### Questions
- In Figure 6, where MS-AMP was applied to nanoGPT with and without the LM head in FP8, what does the observed performance degradation indicate about the LM head’s role in stability? And how do the loss trends compare to BF16 training based on the exponential moving averages?

- Table 1 shows loss landscape sharpness values for Llama v2 7B models at different precisions (E8M3 to E8M7) over various training steps; how do these sharpness trends reveal the model's progress towards loss divergence, and are there any specific sharpness thresholds that clearly predict instability?

- The stability of E8M5 configurations is tested under different learning rates in Figure 9, showing more frequent loss spikes at higher rates—how does this pattern of sharpness changes affect hyperparameter tuning in low-precision training, and what insights do these learning rate sensitivities give for FP8 compared to BF16?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a new metric to evaluate the training instabilities of LLMs when reducing the floating precision of the model's weights. The paper introduces a novel loss landscape metric based on the previously proposed Keskar et al. (2017). However, the paper's novel metric is computed on the last token's logits rather than on the model's input for the computation. Thanks to this change, the computational cost of computing the metric is significantly reduced since the metric has to be computed only once for each measurement. This choice is motivated by the autoregressive decoder-only model's last token, which receives inputs from all other tokens. 

By proposing this novel metric, the paper investigates the cost-effectiveness and impact of reducing the model's floating point precision. The paper analyzes the impact of reducing the model's weight precision regarding training instabilities by conducting an ablation study. They conducted experiments by simulating incremental bit reduction of the mantissa or exponent bits of the model's weights.

### Strengths
The proposed metric is an effective, computationally cheap, proxy measure of the underlying training instability. The paper clearly shows in Figure 8 and Table 1 that the proposed metric can detect the training divergence before it occurs for the E8M5 and compare the results with other reduced floating-point precision (for example) 

The paper's outcomes confirm previous findings that neural network training is more sensitive to exponent bit reductions than to mantissa bits.

### Weaknesses
The paper proposes a novel and computationally cheap metric to detect training divergence based on the work of Keskar et al. (2017). However, the paper does not compare the performances or computational costs of previously proposed methods in the literature. Also, the paper does not consider or compare methods exploiting the gradient or the internal activations of the model to detect training divergences.  

The paper does not consider different training hyperparameters from those reported at the end of the first paragraph of the "Method" section.

### Questions
- Could you maybe compare your proposed metric to the metric proposed in Keskar et a. (2017) or other SOTA metrics in terms of computational costs and early detection of training instabilities? 

- Could you maybe run the experiments on more training schedules (i.e., initial learning rate, learning rate) than the ones mentioned in the first paragraph of the Methods section to verify the consistency of your observed results? 

- Could you maybe include the results (i.e., a table or plot) showing the failure of training with lower exponent bits (e.g. E7E7)?

- Could you maybe verify the two suggestions (i.e., high-precision initial training stages and higher precision for sensitive layers and vice versa for less sensitive layers) proposed in the last paragraph of the "Discussion" section as possible training stabilization techniques?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the feasibility of using reduced-precision floating-point representations, specifically FP8, for large language model (LLM) training to enhance computational efficiency. While BF16 has become standard due to its balance of precision and performance, FP8 poses challenges in stability. The authors propose a new metric to quantify loss landscape sharpness, aiding in predicting training stability. They analyze the effects of reducing mantissa and exponent bits, finding that exponent bit reduction significantly impacts model performance. The contributions include a novel approach to evaluating training stability and insights into the trade-offs of using lower precision in LLM training.

### Strengths
-The motivation of this paper is compelling, particularly the concern regarding the stability of FP8 compared to FP16 and BF16. This raises important questions about the cost-effectiveness of FP8 for LLM training. A deep analysis and understanding of the effects of low-bit training can significantly benefit the research community by providing valuable insights.
-The introduction of a new metric for quantifying loss landscape sharpness is good. This analytical framework could be beneficial for the research community.

### Weaknesses
My primary concern with this paper is the confidence in the experimental validation, especially given the smaller scale of the models used. Theoretically, we understand that reduced precision can affect model convergence. However, my intuition suggests that as models grow larger and datasets become more extensive and of higher quality, the models' robustness improves, potentially mitigating the impact of low-bit precision. This phenomenon is also observed in low-bit post-training quantization, where larger models are less affected by quantization. I am uncertain if the observed effects would persist in larger models.

As this paper is based on MS-AMP. The MS-AMP paper, which tested with 7B, 13B, and 175B models on more diverse datasets, concluded that FP8 training loss is consistent with FP16. This seems contradictory to the findings of this paper. Is there a difference in experimental settings, or did I miss something?

### Questions
-Many previous works have proposed techniques to address numerical instability, such as precision decoupling and automatic scaling in MS-AMP. Were these techniques or similar techniques applied in your experiments, particularly in the simulations conducted in sections 4.2 and 4.3?

-I'm unsure about the data quantity and quality used in this work, as the experimental settings aren't clearly described. For instance, it's unclear what dataset was used in Figure 6, and the training steps don't intuitively reflect how many tokens were trained.

### Soundness
2

### Presentation
2

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
The paper investigates training using low precision, specifically the FP8 datatype. It examines the stability of FP8 training across various seeds and initializations, revealing loss spikes during certain training phases. To further understand these issues, the authors analyze training stability by simulating different numbers of mantissa bits. Finally, they propose a method to assess loss sharpness and predict potential training divergence.

### Strengths
The paper suggest a sharpness metric to help to check where a model training will diverge  The the authors claims that the proposed method is more suitable for autoregressive models. I think that comparison to previous method, showing cases where the proposed method works better than previous one in autoregressive models is a must.

### Weaknesses
I think the weaker part of the paper is the experiment section, mainly  the main MS-AMP experiment (section 4.1). - which is the main motivations for all the paper.
The authors claims that in all cases FP8 training is not able to get the same results as the baseline (BF16) counterpart. We can find 2 papers - from Microsoft (https://arxiv.org/pdf/2310.18313) and Intel (https://arxiv.org/pdf/2409.12517) showing that is is possible to train LLM in FP8 - I suggest the authors to investigate the gap between their paper and these.

The paper suggest a sharpness metric to help to check where a model training will diverge  The the authors claims that the proposed method is more suitable for autoregressive models. I think that comparison to previous method, showing cases where the proposed method works better than previous one in autoregressive models is a must.

### Questions
1) Please add comparison to previous sharpness metric, showing why the proposed method is more suitable for autoregressive models.
2) Does the bit reduction experiments include scaling when reducing the exponent bits. If not, I suggest to add it- I believe in that cases we will see completely different conclusions.
3) How do you implement the experiment of reducing mantissa bits? For the exponent it is well explained in the paper (clipping). Moreover, the author claim their method of masking is an imperfect approximation - can you please explain what is the gap? How do you show this gap is not critical.

4) Please try to clarify why the authors are not able to converge FP8 training while 2 previous papers are able to converge.


===================================================================

Rebuttal:

Dear Authors,

Thank you for taking the time to address the questions and concerns raised.

Unfortunately, I believe the primary issue remains unresolved. The authors attribute the divergence in their FP8 training to the use of an open-source dataset. However, Intel’s paper demonstrates successful FP8 convergence using open-source datasets as well. Additionally, while the authors suggest that Intel’s findings support their claims, I believe this is not accurate. In Intel’s work, the divergence is attributed to the use of the SwiGLU activation function, which is not employed in this paper (as nanoGPT uses the GeLU activation function).

Furthermore, I believe that the absence of scaling and the bias introduced by the bitmask in the mantissa (which could be critical during the backward pass) may significantly impact the conclusions drawn in this paper.

I will maintain my score.

### Soundness
2

### Presentation
2

### Contribution
2
