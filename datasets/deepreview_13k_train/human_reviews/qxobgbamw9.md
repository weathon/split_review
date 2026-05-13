# Output Alignment: A Top-down Approach to Length Generalization

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Recently, large language models have exhibited impressive performance and surprising emergent properties. However, their abilities remain constrained by the preset context window of the Transformer architecture, and they continue to struggle with length generalization. In this work, we propose a new perspective on length generalization by focusing on the output distribution rather than the input, as most prior studies have done (e.g., through positional encodings or data structure). First, through case studies on simple synthetic tasks, we highlight the importance of **output alignment**---the consistency of output distributions across sequences of varying lengths. We then extend this observation to natural language tasks and introduce a metric named Long-Short Misalignment to quantify output alignment, finding a strong correlation between this metric and length generalization performance. Based on these insights, we propose a regularization loss during training that improves output alignment. Extensive experiments confirm the effectiveness of this approach. Overall, our work provides a novel perspective for understanding and enhancing length generalization in large language models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new view of achieving length generalization of LLMs by the output distribution adjustment/alignment. It identifies output alignment, the consistency of output distributions across varying sequence lengths, as a key factor in length generalization. The authors introduce the Long-Short Misalignment metric to quantify this alignment and demonstrate its strong correlation with models' performance on long-context tasks. Hence, they propose a regularization loss based on this metric, which, when incorporated into training, significantly improves models' ability to handle longer sequences. The evaluation is conducted on language modeling (Redpajama and PG19) and LongBench, where the proposed method demonstrates certain effectiveness.

### Strengths
1. Considering that inputs of variable lengths significantly vary the output of LLMs, the view of achieving length generalization by addressing the output distribution gap between short and long inputs is novel and makes sense.

2. The evaluation of language modeling and LongBench demonstrated the effectiveness of the proposed misalign loss and verified the authors' postulation.

### Weaknesses
1. In your settings, the short input is usually the truncated local context window of a long input, and the output distribution from the short input would serve as the "ground truth" distribution in SCE loss in Eq. (5). However, if the output relies on previous context information that's been removed, the output distribution given short input is also divergent and even wrong. For such a situation, the alignment may mislead the long-context output distribution and limit the capabilities (the model may tend to attend to local context only).

2. The models in experiments are trained based on CLEX. CLEX and some similar methods (e.g., YaRN) would dynamically adjust the frequency of RoPE according to the input length. In your implementation (line #376 to #404), the long and short inputs would be incorporated into one sentence, which would make the "short output distribution" be accessed based on "long RoPE frequency". Such short output distribution may deviate from the naive one and potentially affect the model's capabilities.

3. The evaluation length is up to 8K, which may be insufficient for a method designed for length generalization. I believe the evaluations over longer sequences may help to validate the effectiveness of the proposed method.

4. Section 3 seems to be redundant. The motivation and the proposed method are straightforward but the case study in section 3 is somewhat difficult to follow.

### Questions
Please refer to the weaknesses.

### Soundness
2

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
3

### Summary
This paper presents a novel approach to enhancing length generalization in large language models by focusing on output alignment (i.e., the consistency of output distributions across sequences of varying lengths), a departure from the more commonly explored input-focused strategies. The authors introduce a metric termed Long-Short Misalignment, which is shown to have a  correlation with length generalization performance. Additionally, the paper proposes a regularization loss aimed at improving this alignment and a reparameterization technique (OutRep) to explicitly align output distributions across different sequence lengths. Experimental results are provided to show that these techniques improve length generalization capabilities in both synthetic and natural language tasks.

### Strengths
1. Novel Perspective: The focus on output alignment as a means to improve length generalization is a fresh perspective that diverges from traditional input or positional encoding-based methods. This unique angle provides a valuable contribution to the ongoing discourse on enhancing transformer model capabilities.

2. Clear Presentation: The paper is well-written, with a clear presentation of ideas and experimental results.

### Weaknesses
1. Theoretical Issues: The theoretical proof of Theorem 3 could be problematic given the problematic definition of length generalization loss in the appendix (see detailed questions below), which weakens the theoretical soundness of the proposed approach. The empirical analysis cannot fully support the claim that minimizing the Long-Short Misalignment metric could lead to better length generalization  (see detailed questions below).

2. Computational Complexity: The implementation of the Long-Short Misalignment metric as a regularization loss introduces additional computational overhead. Moreover, the implementation details and complexity analysis, including their impact on model performance, are not adequately provided, which limits understanding of its scalability. Specifically, the paper lacks a detailed breakdown of the computational cost associated with calculating the Long-Short Misalignment metric, such as the number of floating-point operations (FLOPs) and memory usage, and how these scale with sequence length and batch size. Furthermore, the paper does not discuss the potential impact of this overhead on training time and resource consumption, which is crucial for assessing the practical applicability of the proposed method.

3. Lack of Comparison with Other Length Generalization Approaches: The paper does not provide a direct comparison between the proposed output alignment approach and other length generalization approaches (e.g., positional encoding-based approaches). Such a comparison would be beneficial to understand the relative strengths and weaknesses of the proposed method compared to existing approaches. For instance, it is unclear how the proposed method compares to techniques like positional interpolation or learned positional encodings in terms of both performance and computational efficiency. A more comprehensive comparison would involve evaluating the proposed method alongside these existing techniques on a range of tasks and sequence lengths.

### Questions
1. Encouraging LLMs to be less sensitive to small input sequence length variations, given that the semantic meanings of these input sequences are very similar, is essentially a form of robustness. However, when input sequence length differences are significant, encouraging output alignment may not be appropriate, as the outputs are expected to differ substantially. In your regularization term computation, when you sample l1 and l2 from the interval [ltrain / 2, ltrain], could you conduct an ablation study examining how different sampling ranges |l1 - l2| affect performance?

2. The mathematical equation for length generalization loss (Eq. 43) defined in Theorem 3 in the appendix is problematic. It doesn't explicitly compare model performance across different input lengths. A more reasonable definition you might consider is Egen_{long inputs} / Egen_{short inputs} - 1, where Egen is your original definition (Eq. 43). Could you incorporate this definition into your analysis and discuss how it might affect the theoretical results and empirical findings?

3. In Tables 2 and 3, it might not make sense to compare the proposed approach with the baseline approach by setting the same training steps since the proposed approach requires more computation. Could you provide a comparison based on total computation time or FLOPs rather than training steps, which would give a more accurate picture of the efficiency-performance tradeoff?

4. Table 1 shows that more powerful LLMs, which achieve better evaluation scores on some long-context benchmarks, also tend to have smaller Long-Short Misalignment scores. However, it is insufficient to conclude that a smaller Long-Short Misalignment metric directly leads to better length generalization ability based solely on these results. Could you conduct additional experiments or analyses to establish a more direct link?

5. Can you compute the length generalization loss and add it to Tables 2 and 3 to better demonstrate that the proposed approach leads to improved length generalization?

6. There is a lack of details on the sampling strategies and complexity analysis of the Long-Short Misalignment regularization term computation, including their impact on model performance. Could you provide more information on these aspects?

7. How does the proposed output alignment technique compare with other length generalization approaches (e.g., positional encoding-based approaches)?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the challenge of length generalization in LLMs. Instead of focusing on input structure or positional encoding, the authors present a novel approach centered on the output distribution to enhance length generalization. They highlight the concept of output alignment and introduce the Long-Short Misalignment metric to measure and quantify the consistency of output distributions for varying sequence lengths. Empirical results from synthetic tasks and natural language tasks validate their approach, demonstrating that output misalignment significantly impacts model performance on longer sequences. The paper further proposes a regularization loss based on their metric, which improves length generalization as shown through extensive experiments.

### Strengths
1. The paper is well-written and easy to follow. The explanations and the illustrations are clear.
2. The proposed output alignment method for improving LLMs' length generalization is novel. The long-short misalignment regularization loss can be beneficial for future long-context LLM training.
3. The long-short misalignment loss is an interesting and useful probe for long-context LLM performance.

### Weaknesses
1. Although the authors include extensive theoretical analysis of the proposed metric and method, the proofs of the theorems are based on some very strong assumptions, which need to be justified. More details in the Questions part.
2. The analysis of the synthetic tasks and the natural language tasks seems disjointed. The cause of the errors is different for these two types of tasks. This makes the OutRep method proposed in Section 3.2 seem unrelated to the rest of the paper and has a very limited use case on only non-pretrained small models. It would be beneficial to make a stronger connection between Section 3.2 and the following sections.
3. The experiments show that a higher regularization coefficient can negatively affect performance. More analysis is needed to mitigate the risk of over-regularization.

### Questions
1. The proof of Theorem 1 is based on an autoregressive expression (Eqn 9). However, it is unclear why self-attention can be reformulated in this way. Also, it seems like Assumption 1 assumes that the function $K$ can disregard part of the input context. In an extreme situation where $l_{train}$ is very small, this assumption means that $K$ neglects a large portion of the prompt. Could you please elaborate more on the validity of Eqn 9 and Assumption 1?
2. Assumption 2 assumes that a Transformer model is Lipschitz continuous. However, this is not true for Transformers. Please refer to [1].
3. Regarding the long-short misalignment regularization, in a situation where $l_{train}$ is small, will the model learn to neglect some proportion of the input at the front?
4. Some key references are missing. For example, the mean prediction task is similar to the parity counter task in [2], and there has been similar length extrapolation analysis on synthetic tasks in [3].
5. In Line 400, the sequences should overlap by $l_{extra}$ tokens.

[1] Hyunjik Kim, George Papamakarios, and Andriy Mnih. 2021. The Lipschitz Constant of Self-Attention. ICML.

[2] Bingbin Liu, Jordan T Ash, Surbhi Goel, Akshay Krishnamurthy, and Cyril Zhang. 2022. Transformers Learn Shortcuts to Automata. ICLR.

[3] Suyuchen Wang, Ivan Kobyzev, Peng Lu, Mehdi Rezagholizadeh, and Bang Liu. 2024. Resonance RoPE: Improving Context Length Generalization of Large Language Models. ACL Findings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents output alignment as a method for enhancing the length generalization performance. The author initiates with the observation that the output space is significant in length generalization as demonstrated by a synthetic task. Through both theoretical and experimental analyses, the author validates that the output space has an impact on performance. The paper then proceeds to propose an approach for constructing a robust output space for natural language tasks. The performance of the proposed loss is advantaged by the experiments.

### Strengths
The strength is evident:
1. A novel perspective from the output space of the Language Learning Model (LLM) when addressing the length generalization problem rather than the common input space analysis.
2. A well-defined synthetic task is proposed to drive the motivation and is strongly supported by theoretical analysis and experiments.
3. The proposed training loss is straightforward to implement and brings a relatively significant improvement to the length generalization performance.

### Weaknesses
The weaknesses are as follows:

1. There is a lack of understanding regarding the design of mean value prediction tasks. Given that 0 and 1 have an equal probability (as indicated on line 143), does this imply that both 0 and 1 have a probability of 0.5? If so, does it mean that predicting 0.5 under a length of 50 would yield an approximate test loss of 0.005? Despite the actual test loss being around 0.001, this design appears suboptimal. The core issue is that the mean prediction task, as designed, seems too simplistic. The model could potentially achieve low loss by simply predicting a value close to 0.5, regardless of the input length, without actually learning any meaningful relationship between input length and output. This raises concerns about the validity of using this task to motivate the need for output alignment.

2. The distinct scaling behavior in mean and length is highly evident, particularly when a feed-forward layer is added to predict a scalar of the length. Predicting out-of-distribution values is a well-known challenge. Since the input and weight have fixed scales, but the output is expected to be scalable with respect to the length, the synthetic tasks seem rather explicit. This is not necessarily a weakness but rather emphasizes the need to clarify the purpose of such a preliminary experiment, which will be my next question. The issue is that the synthetic task seems almost pre-engineered to highlight the problem it's meant to address. The length prediction task, where the output is directly proportional to the input length, is a very specific case that may not generalize well to other scenarios. The scaling behavior is so obvious that it's unclear if the model's failure is due to a genuine lack of generalization ability or simply an inability to extrapolate beyond the training range.

3. The question arises as to how the synthetic task is actually related to natural language cases where the misalign loss is proposed. The only connection observed is “output space matter”. However, there appears to be a fundamental difference in “the output space/output distribution/output alignment” between the two scenarios. In the former case, it is more of a “scale/magnitude” issue. As the scale of x is changed to logx or 1/sqrt(x), the scale/magnitude becomes less out-of-distribution when scaling the length. In contrast, in the natural language case, it is primarily an “actual distribution” issue since the “scale/magnitude” does not change significantly. While both cases can be understood, the connection between them remains unclear. From this perspective, the term “misalignment” seems to be misused. The author could provide further clarification. The core problem is that the paper uses the term 'misalignment' to describe two very different phenomena: a scaling issue in the synthetic task and a distributional shift in the natural language task. The connection between these two is not clearly established, and the use of the same term for both could be misleading. It's unclear if the proposed method is addressing the same underlying issue in both cases, or if it's simply a coincidence that it improves performance in both.

4. The experiment appears to be relatively weak. For natural language tasks, the author only evaluates it on LongBench, and the performance improvement is marginal. There are two potential ways to enhance the robustness of the results. Firstly, conducting experiments on more tasks such as Need-in-a-haystack, InfiniteBench, BABILong, etc. Secondly, analyzing the generations of the baselines and the proposed methods and providing randomly sampled output samples to show that the use of the additional loss is demonstrably better.

### Questions
Small issues in writing:

1. L150,  ... embedding used, the test loss dramatically...  => ... embedding used, the test loss of length prediction task dramatically... 
2. L298-L299, A bit confusing about sufficies.

### Soundness
2

### Presentation
4

### Contribution
3
