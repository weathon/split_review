# An End-to-End Model For Logits Based Large Language Models Watermarking

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
The rise of large language models (LLMs) has increased concerns over source tracing and copyright protection for AI-generated content (AIGC), highlighting the need for advanced detection technologies. Passive detection methods usually face high false positives, while active watermarking techniques using logits or sampling manipulation offer more effective protection. Existing LLM watermarking methods, though effective on unaltered content, suffer significant performance drops when the text is modified and could introduce biases that degrade LLM performance in downstream tasks. These methods fail to achieve an optimal tradeoff between text quality and robustness, particularly due to the lack of end-to-end optimization of the encoder and decoder. In this paper, we introduce the first end-to-end logits perturbation method for watermarking LLM-generated text. By jointly optimizing the encoder and decoder, our approach achieves a better balance between quality and robustness. To address non-differentiable operations in the end-to-end training pipeline, we introduce an online prompting technique that leverages the on-the-fly LLM as a differentiable surrogate. Our method demonstrates superior detection robustness, consistently outperforming state-of-the-art (SOTA) methods by 1.2\%, 4.0\%, and 5.5\% across 3 LLMs, averaged over 6 types of text distortions. Simultaneously, our approach achieves exceptional text quality, as evidenced by reduced text perplexity and improved performance in the downstream tasks with a margin of 19.2\% and 3.03\%. Our method can be easily generalized to different LLMs. The code is available in supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose an end-to-end optimized watermarking method for large language models to enable the detection of AI-generated content. The goal is to enhance the robustness/text quality trade-off of current LLM watermarking methods. The challenge is that many operations, such as generating sequences of text, are not differentiable. The authors overcome this issue by using the well-known Gumbel-Softmax trick to backpropagate through the text-generating process. To enhance robustness, the authors incorporate a paraphrasing model during the optimization method, and they develop cross-LLM adapters to train on one LLM and deploy it to other LLMs. They show robustness against six text modification attacks and improved text quality.

### Strengths
- The method works well and allows adapting against paraphrasing attacks during optimization. 

- The authors thoroughly evaluate their approach by including experiments on robustness, detectability and impact on runtime during inference. 

- The paper is clear in its presentation and presents the proposed ideas well. 

- The cross-LLM inference adapter is a great idea, and I have not seen one before for trainable watermarking methods.

### Weaknesses
 - The results from Figure 5 in their current form are not reproducible and lack transparency. I believe it should be a scatter plot that includes the quality degradation, and the authors should state the hyperparameters for each approach used for paraphrasing (e.g., the prompt used for paraphrasing).

- Abdelnabi et al. [A] have previously proposed end-to-end watermarking for LLMs. They also use the Gumbel-softmax trick to differentiate through the text generation process. The authors should consider citing this work.

- Figure 7, showing the difference in token distribution for the top 50 tokens, is difficult to interpret. It looks like the distance to the non-watermarked text is quite large (especially compared to KGW). Also, the choice of using 400 non-watermarked/watermarked samples is unclear. I think it would be better to plot detection accuracy against the size of the training dataset.

- It is well known that perplexity is an unreliable metric used to measure text quality [C]. I was surprised that the authors did not include watermarked samples in their Appendix. There is a known problem: training LLMs with Gumbel-softmax is unstable and can lead to poor results for text generation [D]. Could the authors please show watermarked samples and (potentially) include a limitation section on current challenges when using this optimization method?

### Questions
- I do not understand why the prompt between non-watermarked and watermarked texts needs to differ (footnote 3 on page 9). Why can't the attacker re-use the same prompts when querying non-watermarked texts?  

- In Figure 2, I am unclear how the authors calculate the distance $L_{sem}$ between the watermarked and non-watermarked texts $X_{wm}, X_{nwm}$. Since both sequences will differ in the sampled tokens, they will diverge throughout the generation process if sampled for many tokens. Then, calculating this semantic distance will be meaningless as you cannot effectively align $X_{wm}, X_{nwm}$. Also, it appears unreasonable that the averaged similarity over many contexts will be a meaningful measure of the overall similarity between two sequences. I would appreciate the authors elaborating on this point and providing more context

- The description of the online text editing module is a bit confusing to me. Do the authors also use Gumbel-softmax for the online text editor, or do they pass $X_wm$ directly to the decoder $D$ contrary to what is shown in Figure 1? Since the text generation process from the online text editor $N$ is not necessarily differentiable unless you use some trick, end-to-end training from the detector's prediction back to the encoder won't be possible. I would appreciate it if the authors could elaborate on this point.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In this paper, the authors present a novel logit-based watermarking pipeline for text generation. Their approach incorporates Gumbel-Softmax for sampling and an online prompting technique for adversarial edits, allowing the encoder and decoder to be trained in an end-to-end fashion. The method achieves state-of-the-art detectability under various attacks while maintaining high-quality generated text.

### Strengths
- The paper includes an extensive section on experiments, including many state-of-the-art methods and attack scenarios.
- The results for overall detectability and text quality look promising.
- The encoder and decoders are small, so although an extra watermark encoder and decoder have been introduced, the generation and detection are very efficient.

### Weaknesses
 - The result on generation diversity is not great as the proposed method has the lowest diversity among all other methods. Even though this doesn't affect the results on the benchmarks, I think this might be a bad feature for certain tasks, like synthetic data generation.
- The proposed method is training-based not like some of the baselines. The method might suffer OOD issues that the distribution of the prompt at the inference time is quite different from the training.
- The proposed method used a classifier for detection, and this does not give us an interpretable result like a p-value. This might also be bad if we want to control the false positive rate during detection.

### Questions
- I wonder how expensive is the training especially the requirement for the GPU memory. If I understand it correctly, the forward looks like: first token logits -> encoder -> sample the first token -> second token logits -> encoder -> sample the second token -> ... So we recursively call the encoder for n times if we generate n tokens. Would the computational graph be huge? Especially you also have to sample some tokens from the online text editor later. I wonder how did you train it exactly.
- As I mentioned above, the method might suffer OOD issues. Would the encoder/decoder trained on WikiText-103 still be effective for other datasets? 
- Another thing that confuses me is that: where do you show the results for cross-llm inference? I noticed you mentioned: "To train our end-to-end model, we chose OPT-1.3B as the online LLM for efficiency." Does this mean results for llama models are the transfer inference results? Or this is for the online text editor.

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
The authors present an end-to-end training-based text watermarking method aimed at achieving an optimal trade-off between text quality and robustness, leveraging the logits-based watermarking framework introduced by Kirchenbauer et al. Specially, they jointly train additional encoder to generate logits perturbation to shift the tokens’ probability distribution and additional decoder to extract the watermarking signals from the text. In addition, the authors introduce distortion module, address the non-differentiable operations in the end-to-end training pipeline, and consider the generalization to different LLMs.

### Strengths
* A distortion module is helpful to enhance the robustness.

### Weaknesses
 *  Insufficient coverage of relevant related work
* Inadequate explanation of key methodological design choices
* Evaluation on outdated LLM architectures
* Limited adaptive attack evaluation
* Unclear figure captions (specifically Fig. 2)

### Questions
### **Comparative Analysis**

* The paper briefly mentions other training-based methods (UPV, SIR) but lacks detailed comparison
* Please provide in-depth analysis of architectural differences and performance variations between this work and existing training-based approaches

### **Efficiency and Generalization**
* The cross-model inference time overhead is significant - what optimizations are possible?
* How does the method handle LLMs not included in the cross-model converter?
* What is the failure mode analysis?

### **Evaluation Scope**
* Evaluation should include more recent LLMs (e.g., Yi, Qwen)
* Need broader testing across model architectures and scales

### **Related Work and Claims**

* Notable omission of generation-based watermarking methods (e.g., AWT [1], REMARK-LLM [2])
* The "first end-to-end framework" claim requires more careful qualification

[1] Adversarial watermarking transformer: Towards tracing text provenance with data hiding

[2] REMARK-LLM: A robust and efficient watermarking framework for generative large language models

### **Security Analysis**

* How does the method perform against adaptive attacks where adversaries have full access to the system?
* Need evaluation of undetectability and robustness when attackers can obtain paired watermarked/unwatermarked samples

### **Architecture Choices**
* Please justify the selection of LSTM as the decoder backbone
* What alternatives were considered and why were they rejected?

### Soundness
3

### Presentation
3

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
This paper proposed an end-to-end optimization framework for achieving better trade-off between the robustness and the text quality. The authors validate the effectiveness of the proposed framework with comprehensive experiments on popular LLMs.

### Strengths
1. The proposed end-to-end method is original, and extensive experiments have been conducted to evaluate its quality, detectability, and robustness.

2. The presentation is well-structured, making the paper easy to follow.

### Weaknesses
1. Unclear motivation. The authors claimed “However, these existing approaches still fail to achieve an optimal trade-off between text quality and robustness”. However, the authors have missed an important line of works regarding the distortion-free watermark (Kuditipudi et al., 2024; Christ et al., 2024), which suggested we can embed watermarks into LLMs without affect the generation quality. Thus, the there is generally no trade-off between the text quality and robustness, and the claim in the paper is wrong.

2. Limited contribution. Comparing to the previous works (Liu et al., 2024b; Huo et al., 2024), which also share an encoder-decoder structure for logits-based watermarking, the proposed method only introduce a jointly training network for achieving better trade-off between text quality and robustness. As the reviewer has pointed out in weaknesses 1, the trade-off generally does not exist. Thus, the contributions of the proposed method are unclear.

3. The experimental results also cannot support the motivation of “achieving better trade-off between text quality and robustness”. In Figure 7. The KGW watermark has significantly better quality than the proposed watermark, although the detectability and the robustness of KGW are poor. In order to claiming the proposed method has achieved better trade-off than KGW, the authors should show the superior of the proposed method on all quality, detectability, and robustness axis. Besides, in Figure 5, we can also see that the proposed method does not always outperform the baselines in all scenarios.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2
