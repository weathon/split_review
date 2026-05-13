# Why Does the Effective Context Length of LLMs Fall Short?

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Advancements in distributed training and efficient attention mechanisms have significantly expanded the context window sizes of large language models (LLMs). However, recent work reveals that the effective context lengths of open-source LLMs often fall short, typically not exceeding half of their training lengths. In this work, we attribute this limitation to the left-skewed frequency distribution of relative positions formed in LLMs pretraining and post-training stages, which impedes their ability to effectively gather distant information.
To address this challenge, we introduce \underline{S}hif\underline{T}ed \underline{R}otray position embedd\underline{ING} (\method). \method shifts well-trained positions to overwrite the original ineffective positions during inference, enhancing performance within their existing training lengths. 
Experimental results show that without additional training, \method dramatically improves the performance of the latest large-scale models, such as Llama3.1 70B and Qwen2 72B, by over 10 points on popular long-context benchmarks RULER and InfiniteBench, establishing new state-of-the-art results for open-source LLMs. Compared to commercial models, Llama 3.1 70B with \method even achieves better performance than \texttt{GPT-4-128K} and clearly surpasses Claude 2 and Kimi-chat.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors present STRING (Shifted Rotary position embedding) which proposes to shift the position relevance of tokens during inference. With STRING, the authors are able to demonstrate improved performance of 10+ points on RULER, and IB for LLAMA 70B. The authors further train a tiny-llama 1.3B model to demonstrate the effectiveness and compare STRING with SOTA models. The authors also discuss the implementation of STRING with modification to flash attention.

### Strengths
Thank you for submitting your paper to ICLR. I thoroughly enjoyed reading your paper, especially it is very well written. 
1. The paper observes "left-skewed position frequency distribution" - a bias in the position indices required to answer a relevant question being towards the shorter end. For example, on SlimPajama, the authors observe that the frequency of position indices used to model relationships between distant tokens (distances
≥1024) is less than 20%, and for even longer distances (≥1536), it drops below 5%.
2. The authors also demonstrate interesting findings, such as "larger training context window consumes fewer tokens to achieve the same context length". Although it's only been tested on tinyllama (1.3B) so weather scaling laws hold is an open problem.

### Weaknesses
1. The authors acknowledge in part (3) of 4.1 that "Applying Eq. 3 disrupts the model’s ability to capture
local relationships because it alters the relative positions between neighboring tokens" but I'm not fully convinced if the heuristic of "W" is sufficient to allevate this concern. While emperically the experiments suggest so, I'd have liked to see a slightly more detailed study on the impact of altering the relative positions between neighboring tokens.

### Questions
The results in the paper for the 1.3B Tiny-llama and the commercial models are impressive on the long-context benchmarks. However, assuming the "system" to mean the LLM and STRING combination will be used together, I'd also like to see benchmarks for short-context lengths - especially around coding (MBPP, Humaneval), tool-use (BFCL), and Reasoning (GSM-8K, MATH). If not for all, atleast for 1/2 models to reason if there are any trade-offs. I'm especially curious for coding and tooling benchmarks, since they need to adhere to syntax, which might be compromised by the re-positioning. 

Since you have implemented STRING, what is the latency overheads (and impact on throughput) vis-a-vis vanilla RoPE?

### Soundness
3

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
4

### Summary
This paper reveals the possible reasons why current LLM can't maintain good performance with long-context task even the training has involved such corpus. According to the analysis on the left-skewed frequency-distribution, the paper proposes a training-free method (STRING) to mitigate the position bias. By replacing infrequent long-range position index to frequently trained positions during inference, their method enhances the long-context capability without requiring additional training. The experiment results on multiple long-context benchmarks demonstrate the effectiveness of STRING.

### Strengths
1. The exploratory analysis about the left-skewed frequency-distribution of position index is insightful, and can help the community understand the potential reasons why the long-context problem exists in current methods.

2. The proposed method is intuitive and simple to implement, which seems effective simultaneously.

3. The presentation of the paper is very clear,  and the analysis together with the method description are easy to follow,

### Weaknesses
1. The parameter S and W needs to be set manually, which maybe improved by an automatic algorithm to obtain a better performance.

### Questions
It is shown that the most distant position S indexes can be ignored during inference to obtain a better performance, have you conducted investigation whether it is the same case for training? Can decreasing the longest context window in training directly yields a better performance in inference?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper suggests that large language models (LLMs) struggle to handle dependencies over long distances due to the skewed occurrence of relative distance towards shorter ranges while training. The authors propose STRING, a simple method that re-uses more frequently occuring positions for distant tokens, avoiding the use of under-utilized long-distance positions. Through extensive evaluations on long-context benchmarks, they demonstrate that STRING can improve the performance of SOTA models within their pre-trained context windows.

### Strengths
1. The paper is clearly written and easy to follow.
2. The proposed method is simple and effective. In particular, it improves the performance of existing LLMs within their pre-trained context window.
3. The proposed method can be easily deployed. STRING does not require any additional training and can therefore be easily applied to existing LLMs. The authors also provide a way to make the method compatible with FlashAttention, enabling fast and efficient inference.

### Weaknesses
1. Observation (1) in Section 3 (line 216) is overstated, as training with longer context involves larger computation demands due to the quadratic nature of self-attention. For fair comparison, training efficiency should be compared with the same amount of computation, instead of the number of consumed tokens. The authors should clarify that while a larger context window might require fewer tokens to reach a certain effective context length, the computational cost is not necessarily lower, and could in fact be higher due to the increased attention matrix size.
2. STRING looks more like an empirical workaround to avoid using less-frequent positions, rather than a fundamental solution for the problem. The method does not address the underlying issue of why models struggle with long-range dependencies, but rather provides a way to circumvent the problem by re-using more frequent positions. This raises concerns about the generalizability of the approach to scenarios where such position re-use might introduce unintended biases or limitations.

### Questions
1. Can this method also be useful for context extrapolation? I understand that the primary focus of the paper is to improve performance within the pre-trained context window, but I believe this is also a large understated benefit of your method.

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
3

### Summary
This paper discusses how current LLMs use only a portion of their maximum context length due to issues in handling distant information. The authors identify the root cause as a left-skewed distribution in the model's relative positions during pretraining and post-training. 

To address this, they introduce a new method called Shifted Rotary Position Embedding (STRING), which adjusts well-trained positions during inference to improve performance without extra training. 
Experimental results show that STRING enhances the context length usage of open-source models like Llama 3.1 70B and Qwen2 72B by over 10 points on benchmarks like RULER and InfiniteBench. STRING's effectiveness even surpasses commercial models like GPT-4-128K, Claude 2, and Kimi-chat.

### Strengths
The paper is well-structured, with clear organization, understandable tables, and figures, effectively addressing an important topic in LLM development.

The empirical analysis of position frequency on the training data is thorough (However, I recommend providing additional explanation regarding the meaning of the plot in Figure 1 in the Appendix for further clarity) .

The method has been evaluated on/against quite a few LLMs.

### Weaknesses
1. The code is missing; the provided GitHub link leads to a 404 error.

2. The analysis in Section 3 is intriguing, but the results are limited to small-sized LLMs. It remains uncertain whether the same findings apply to medium- and large-sized LLMs.

### Questions
1. Where can we find your implementation of STRING?

2. Are error bars available for the tables in the experiments? If space is limited, could they be included in the Appendix to give readers a better understanding of the variability in the results?

3. Regarding the improved results shown in the experiments, could you provide more insights into why and how STRING performs effectively? Additionally, are there any scenarios where STRING might not perform as well?

### Soundness
2

### Presentation
3

### Contribution
2
