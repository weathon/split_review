# DeciMamba: Exploring the Length Extrapolation Potential of Mamba

- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 3, 3, 8

## Abstract
Long-range sequence processing poses a significant challenge for Transformers due to their quadratic complexity in input length. %
A promising alternative is Mamba, which demonstrates high performance and achieves Transformer-level capabilities while requiring substantially fewer computational resources. %
In this paper we explore the length-generalization capabilities of Mamba, which we find to be relatively limited. Through a series of visualizations and analyses we identify that the limitations arise from a restricted effective receptive field, dictated by the sequence length used during training. To address this constraint, we introduce \methodname, a context-extension method specifically designed for Mamba. %
This mechanism, built on top of a hidden filtering mechanism embedded within the S6 layer, enables the trained model to extrapolate well even without additional training. Empirical experiments over real-world long-range NLP tasks show that \methodname can extrapolate to context lengths that are 25x times longer than the ones seen during training, and does so without utilizing additional computational resources. %
We will release our code and models. %


\vspace{0.5em}
\hspace{.5em}
\includegraphics[width=1.45em,height=1.png}\hspace{.75em}
{\fontsize{8.5pt}{11pt}\selectfont
\parbox{\dimexpr\linewidth-7\fboxsep-7\fboxrule}{\raisebox{0.5em}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new method to extend the context length of Mamba. The authors start with an explanation of why Mamba in its original form cannot extend the context length. They propose viewing the S6 block as applying an “attention operation” (Section 2) and based on these attention weights, they compute the Mamba mean distance to measure the effective receptive field of Mamba (Section 3). They basically show that the ERF decreases as the context length at inference time increases and that the main culprit is the fast decrease of the sum of discretization steps. To tackle this issue, they introduce Decimamba, a filtering mechanism that discards tokens of lesser importance (Section 4). They finally show on multiple information retrieval benchmarks that the method better performs on long contexts than Mamba.

### Strengths
Overall, I like this paper, I think that Mamba is a very appealing method due to its low inference cost and getting methods that allow extending the context length for Mamba is a very important question. I appreciate the fact that the authors considered diverse benchmarks and the gap between Mamba and Decimamba is pretty consistent in some cases. I also appreciated the scientific approach in the paper that consists in isolating  the problematic component in Mamba and proposing a method to alleviate the issue.

### Weaknesses
I have a few concerns regarding this paper that I list below: 

- **Hyperparameter choices**: I agree with the fact that the fast decay of the sum of the discrete time steps may explain the lack of length generalization. However, the approach looks a bit hacky in that it introduces multiple novel hyperparameters: the decay factor, the maximal length of the sequence after the first decimating later and the number of layers to decimate. And it does not seem very clear how to make these choices without a gridsearch?
- **Ablations**: have you tried to do an ablation with respect to the number of layers to be decimated or with respect to the decay rate? 
Writing should be improved: I found the decimation strategy in Decimamba (Section 4) pretty hard to follow. I think that this should be better explained. 
- **Tasks where Decimamba offers much higher gains?**: we see that Decimamba leads sometimes to big improvements (Squad and Passkey retrieval) but on Multi-Document QA, the decay of Mamba seems to also be important. Do you have an explanation/intuition of the type of tasks where Decimamba leads to substantial improvements?



Minor points:

**Improving the introduction**: I think the author should maybe better explain the Decimamba method in the introduction (and maybe add Figure 5 to the introduction?). 
- **Lack of length generalization of Mamba**: I was a bit confused about the fact that the authors were surprised by the lack of length generalization of Mamba. I agree with the authors that compared to Transformers, the context cache (the hidden states) do not grow with the context length and thus Mamba can scale the context length to infinity. However, this state is **bounded** and thus the model cannot store all the information it may need . In an information retrieval setting, when the number of documents is large, it is easy to imagine that Mamba has trouble deciding which tokens to store. Anyway, this all to say that the authors should maybe highlight that one of the factors explaining the poor length generalization is the small state space size. I think that this is aligned with the method proposed by the authors in that it looks to decimate some non-important tokens that may be captured in the hidden state.
- **Influence of hidden state size on length generalization**: one thing that i am curious about is: have you tried to study the length generalization of models of similar scale but with one of the models having a bigger state space?
- **Comparison with Transformers**: have you tried to run Transformers in the benchmarks of Section 5? Just curious to see the gap of DeciMamba with Transformers.
- **Out of memory**: Maybe I would add a comment saying that the OOM happens in Figure 6 because the complexity at **training time** is O(L). Most people may have in mind the complexity of Mamba at inference time, that is independent of the context length and may be confused by the OOM you encounter. 
- **Typo**: In equation (8), i think the letters "j" and "L" were swapped. It should be $d(L,j)$.

### Questions
I asked my questions in the weakness section.

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
This paper investigates Mamba's length extrapolation capabilities through a systematic analysis approach. The authors introduce the Mamba Mean Distance metric as a novel way to quantify and analyze Mamba's ability to model long-range dependencies. Their findings reveal inherent limitations in Mamba's capacity to handle longer sequences effectively. To address this challenge, they propose a selective token processing mechanism leveraging the delta t parameter from the Mamba formula. This approach intelligently filters tokens by retaining those with larger delta t values, effectively aligning the input complexity with Mamba's modeling capacity. The method is specifically designed for the prefilling phase and demonstrates promising improvements in Mamba's long-text processing capabilities.

### Strengths
- The investigation of token importance scoring in the context of Mamba represents a valuable contribution to the field, especially given the growing interest in alternatives to attention-based mechanisms
- The method achieves substantial improvements while maintaining implementation simplicity, making it readily applicable in practical scenarios

### Weaknesses
 - Limited scope of application: The method's restriction to the prefilling phase significantly limits its practical impact, especially considering the increasing demand for both long-text prefilling and generation in modern applications
- Potential information loss: The token discarding approach may have unintended consequences in scenarios requiring comprehensive context understanding. This is particularly problematic in tasks like document question-answering, where discarded tokens during prefilling might be crucial for subsequent generation phases
- Incomplete solution to fundamental limitations: While the approach provides a practical workaround, it doesn't address the underlying limitations of Mamba in processing long sequences. A more thorough analysis of the Mamba Mean Distance metric could potentially lead to more fundamental solutions

### Questions
- The relationship between distance and performance shown in Fig 1 appears counterintuitive. If Mamba struggles with long-distance relationships, why does the performance degradation manifest primarily in middle lengths rather than showing a clear diagonal boundary from top-left to bottom-right between the red and green regions? Could this suggest a more complex underlying mechanism?
- Given the increasing importance of long-text generation in applications like complex reasoning and creative writing, have the authors explored possibilities of extending this method beyond prefilling to support long-text generation scenarios? It would be benefitial to discuss any challenges the authors foresee in extending the approach to generation tasks.
- The experimental setup shows variations in model selection across different figures and analyses (e.g. Fig 3 and Fig 4). Could the authors provide more detailed justification for these choices and discuss how they might impact the generalizability of the findings?
- Regarding the Mamba Mean Distance results in Fig 4, the findings don't definitively prove that Mamba's long-text capability decreases with length, as this metric wouldn't necessarily scale linearly with sequence length. Are there similar studies for attention-based architectures?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents the limitations of Mamba in terms of length generalization and proposes an algorithm that combines token dropping with the Mamba architecture to effectively enhance its length generalization capabilities.

### Strengths
1. The proposed method is straightforward and can be directly combined with Mamba to improve the length generalization abilities.
2. The authors analyze the shortcomings of Mamba in terms of its length generalization abilities.

### Weaknesses
1. The experimental results are limited. The authors only combine the method with the Mamba model and verify the effectiveness of their method. It would be more convincing if the method can be validated on a broader range of SSM-based and linear-attention-based models.
2. The experimental results are not satisfactory. As shown in Table 1, DeciMamba fails to achieve more than a 10% LongBench score on most datasets. In contrast, models with a context window size of only 4k, as reported in the original LongBench paper, often perform better (e.g., Llama-2-7B-chat has an average score of 31 on English tasks). Additionally, for simpler long-context tasks like Passkey, the authors mention that DeciMamba requires fine-tuning to handle them effectively.
3. The presentation of the paper could be improved. For instance, proper citation formats (\citep and \citet) should be used; table captions should appear above the tables; and in Table 1, the DeciMamba entry is missing the LB score for the LCC dataset.
4. The proposed method has significant limitations. It requires sorting the delta values and retaining the top k tokens, meaning that DeciMamba must process all tokens simultaneously to obtain their delta information. This undermines the core advantage of Mamba, which is its ability to process input sequentially like an RNN. Consequently, DeciMamba loses the characteristic of processing each token/chunk recurrently. Furthermore, this implies that DeciMamba's token dropping strategy can only be applied during the pre-filling stage and cannot benefit the decoding stage's token dropping.

### Questions
Please refer to the Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the question of how to understand and address the limitations of length generalization capabilities of the Mamba architecture. The paper introduces ERF, the effective receptive field, and shows that Mamba is biased towards sequence lengths seen during training. The authors then introduce DeciMamba to extend length generalization capabilities by limiting the number of tokens that the S6 layer processes.

### Strengths
- The paper introduces the phenomenon of "limited effective receptive field" which could be useful for future work studying the Mamba architecture
- The proposed design is well motivated by the identified ERF phenomenon
- The proposed architecture shows consistent improvement over Mamba in long context range experiments
- The paper includes effective visualizations, especially Figure 2

### Weaknesses
 - Most of the related work on length generalization is for transformers. Is there any work on this for SSMs? I'm not sure exactly where this falls in the literature.

 - How does the DeciMamba architecture compare to Mamba at short context length tasks? Ie, is there a tradeoff between performance on short and long context tasks?

### Questions
- How does the DeciMamba architecture compare to Mamba at short context length tasks? Ie, is there a tradeoff between performance on short and long context tasks?

### Soundness
4

### Presentation
4

### Contribution
4
