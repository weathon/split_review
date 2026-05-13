# Rotated Runtime Smooth: Training-Free Activation Smoother for accurate INT4 inference

- Decision: Accept
- Scores: 5, 5, 6, 8, 5

## Abstract
Large language models have demonstrated promising capabilities upon scaling up parameters. However, serving large language models incurs substantial computation and memory movement costs due to their large scale. Quantization methods have been employed to reduce service costs and latency. Nevertheless, outliers in activations hinder the development of INT4 weight-activation quantization. Existing approaches separate outliers and normal values into two matrices or migrate outliers from activations to weights, suffering from high latency or accuracy degradation. Based on observing activations from large language models, outliers can be classified into channel-wise and spike outliers.
In this work, we propose Rotated Runtime Smooth (\textbf{RRS}), a plug-and-play activation smoother for quantization, consisting of Runtime Smooth and the Rotation operation. Runtime Smooth (\textbf{RS}) is introduced to eliminate \textbf{channel-wise outliers} by smoothing activations with channel-wise maximums during runtime. The Rotation operation can narrow the gap between \textbf{spike outliers} and normal values, alleviating the effect of victims caused by channel-wise smoothing.
The proposed method outperforms the state-of-the-art method in the LLaMA and Qwen families and improves WikiText-2 perplexity from 57.33 to 6.66 for INT4 inference.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
A plug-and-play quantization method based on runtime smoothing and the rotation operation of activations has been proposed. Runtime smoothing is responsible for eliminating channel-wise outliers, while the rotation operation mitigate the gap between spike outliers and normal values, resulted by channel-wise smoothing. Experimenting with INT4 inference on different LLMs shows that the proposed method can reduce the perplexity compared to other approaches.

### Strengths
- Combining two exiting ideas in the Quantization literature to overcome both channel-wise and spikes outliers
- Comprehensive experiments with 3 different LLMs, including LLaMA, Qwen, Mixtral and Mistral models on WikiText-2 perplexity

### Weaknesses
Some notations need to be corrected. For example,
- Line 168: identity matrix and number 1 should be distinguished. $|.|$ the norm needs to be determined.
- Line 175: $absmax$ ---- > $abs(\max)$
- Equation (1): $\mathrm{X_j}$ needs to be defined as the columns of matrix $\mathrm{X}$.
- Equation(2): $/$ is not a valid operation for matrices. You need to write the formula as a multiplication with a diagonal matrix.
- line 214: The condition needs to be re-written: $s_j$ cannot be taken out of the sum.

Another issue is that the proposed method has been only tested for the  WikiText-2 perplexity. Can the approach is applicable for other modalities and tasks. For instance, ASR, speech translation, Image understanding, etc.

There is only a small improvement over QuaRot approach. I am wondering if your results are statistical significant?

### Questions
Please see my comments above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposes a quantization method for LLMs, utilizing a smoothing operation during runtime to mitigate the issue of spike outliers and normalize values. Experiments conducted under INT4 settings validate the effectiveness of this method.

### Strengths
1. The paper is clearly structured, making it easy to follow.
2. The method’s motivation is substantiated by experimental results, lending it credibility. In particular, the experiments in Section 4.5 demonstrate the minimal overhead introduced by the method, highlighting its practicality.

### Weaknesses
1. **Figure 1 is confusing and hard to interpret.** The differences between panels (a) and (b) are unclear, as they are on completely different scales despite both sharing the same $ W $ and $ X $. Additionally, have you quantized $ \hat{X} = X \text{diag}(s)^{-1} $? The elements in $ \hat{x} $ appear to be integers, though they should be floats.

2. **Some terms and phrases are difficult to understand.** For instance, the caption for Figure 2(c) uses the phrase "channel-wise consistency" without providing any explanation, making it hard to grasp. Similarly, in point (1), what exactly is meant by "unmatched scale" in Figure 1?

3. **The motivation closely resembles prior work.** For example, DuQuant [1] also begins by addressing layers with massive outliers (in this paper, it is named as "spike") and tackles both massive and normal layers. Similarly, the method in [2] addresses large activation outliers and provides more analysis on this topic than the present paper.

4. **Some claims lack theoretical or experimental support.** For instance, the claim that "smoothing scales depending on the calibration set are prone to being unmatched with online activations" would benefit from experimental results demonstrating the likelihood of such a mismatch.

5. **Some explanations are too brief.** For example, the term "reorder" is mentioned without much elaboration, described only as "reordering the activations and weights according to the magnitude of smoothing scales."

6. **The method lacks clarity in its description.** In Equation 3, $ \hat{X} $ and $ \hat{W} $ appear to be in INT4 format, while $ s_i $ is a float (assuming this is correct, as the authors do not specify). How are these terms compatible for multiplication? A DeQuantize operation may need to be included somewhere in Equation 4.

7. **The ablation study feels incomplete.** The method employs several components—reordering, online smoothing, etc.—but the impact of each isn’t fully explored.

8. **The performance is underwhelming.** The proposed method does not appear to outperform SpinQuant [3] or DuQuant [1], even though it uses online quantization, whereas SpinQuant and DuQuant are offline methods.

Minors: 
1. In Equation 4, $ c_{i,j} $ should be $ s_{i,j} $.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper extends SmoothQuant [Xiao 2023] by:
 - Performing Quip-like [Tseng 2024] rotation before activation smoothing;
 - Obtaining smoothing scale in runtime and not merging it into weights;

### Strengths
The paper is generally well-written, with a comprehensive ablation study (RRS vs RS and RRS vs SmoothQuant) demonstrating the effectiveness, which is well motivated by the preliminary section.

### Weaknesses
The paper lacks an evaluation on the clock-time (instead of the operation count) overhead introduced by the method. This is a concern given that the method determines activation smoothing scale during runtime.

### Questions
See Weaknesses

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
The authors were the first to highlight that channel-wise and spike outliers cause unnecessary distributional expansion in the quantization of large language models (LLMs).

The authors proposed a concise and effective technique called Rotated Runtime Smooth, which reduces these outliers to ensure that the activation distribution for LLM quantization remains compact.

The authors functionally explained, along with the methodology, how Runtime Smooth addresses channel-wise outliers and Rotated Smooth effectively handles spike outliers.

The authors demonstrated effective performance improvements across various LLM models using this approach.

### Strengths
The authors focused on addressing channel-wise and spike outliers for the first time, which highlights a novel problem-solving approach and demonstrates significant performance improvements.

The methodology of Rotated Runtime Smooth (RRS) is simple, intuitive, and provides a clear and straightforward explanation of how it addresses each issue effectively.

By making their code publicly available, the authors have supported further research and made a valuable contribution to the ICLR community.

### Weaknesses
The explanation of the methodology is insufficient: For example, in Figures 1 and 4, which aim to explain Runtime Smooth, it is difficult to gain a proper understanding. The main text also lacks adequate explanation of these figures.

For instance, in Figure 4, while the activation and weight reorder process for Runtime Smooth is presented, there isn’t enough explanation about why this process does not alter or distort the final result. Similarly, in Figure 1, it is unclear what the value of s represents (in relation to the equations in the text) and how exactly it reduces channel-wise outliers and effectively resolves the victim issue caused by spike outliers.

These examples highlight the need for a more detailed and clear description of the methodology, possibly in the appendix. This would help ensure that readers can thoroughly understand the method. While the high-level intuition is conveyed, the reproducibility of the method should be clearly delivered to readers through the paper itself, without relying on the availability of the code.

It is essential to discuss why this study is limited to INT4. The limitations and advantages should be clearly articulated. For example, there is no comparison with recent trending quantization techniques, such as One-bit LLM. A thorough investigation of related work is necessary, and efforts should be made, at least indirectly, to demonstrate the applicability and effectiveness of the proposed method in relation to these latest quantization techniques. https://arxiv.org/abs/2310.11453

### Questions
Please refer to my comment for Weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a quantization technique designed to address outliers during Large Language Model (LLM) quantization, particularly for aggressive scenarios like W4A4 quantization. The method employs two steps: 1) mitigating channel-wise outliers through rotation, and 2) implementing online smoothing to further handle spike outliers. The authors demonstrate promising accuracy results across several benchmarks.

### Strengths
- The authors provide a comprehensive analysis of activation distribution patterns, offering well-reasoned solutions for each identified challenge.
- They proposed a training-free approach that outperforms existing training-based methods on some benchmarks, reducing engineering complexity and showing potential for practical applications in industry scenarios.

### Weaknesses
 - Limited novelty: The core methodology is primarily based on existing approaches like [Smooth quantization](https://arxiv.org/abs/2211.10438 ) and [QuaRot](https://arxiv.org/abs/2404.00456 ), while the reordering technique shows overlap with existing research such as [ATOM](https://arxiv.org/abs/2310.19102) and [LLM.int8()](https://arxiv.org/abs/2208.07339).
- The experimental evaluation is limited in scope, focusing on common sense QA tasks. To better validate the method's effectiveness, the paper would benefit from:
    - More comprehensive comparisons with training-based methods like [SpinQuant](https://arxiv.org/abs/2405.16406) on more complex tasks, like [MMLU](https://arxiv.org/abs/2009.03300)
    - Detailed kernel performance comparisons with related research like [Qserve]( https://arxiv.org/abs/2405.04532), and [ATOM](https://arxiv.org/abs/2310.19102)

- Several aspects of the paper's presentation could be improved:
    - Figure 1: Show the challenges of existing methods, suggest adding visual explanations demonstrating how the proposed RRS technique addresses these challenges
   - Figure 1(b): Highlight the activation grouping methodology in the diagram
   - Figure 2(b): Provide a more detailed explanation of the probability metrics
   - Figure 6: Add clear y-axis labels and justify the unusual batch size choices (>1000).
   - Figure 9: Verify if the orange label represents `u > 8` instead of `u < 8`

### Questions
Please refer the last item of Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
