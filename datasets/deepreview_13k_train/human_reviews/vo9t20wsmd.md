# Faster Cascades via Speculative Decoding

- Decision: Accept
- Scores: 3, 6, 8

## Abstract
Cascades and speculative decoding are two common approaches to improving language models' inference efficiency. 
Both approaches 
involve
interleaving models of different sizes, 
but via fundamentally distinct mechanisms:
cascades employ a \emph{deferral rule} that invokes the larger model only for ``hard'' inputs,
while speculative decoding uses \emph{speculative execution} to primarily invoke the larger model in parallel verification mode.
These mechanisms offer different benefits: empirically, cascades offer better cost-quality trade-offs, often even outperforming the large model, while theoretically, speculative decoding offers a guarantee of quality-neutrality. 
In this paper, we leverage the best of both these approaches by designing new 
\emph{speculative cascading} techniques that implement their deferral rule through speculative execution. We characterize the optimal deferral rule for our speculative cascades, and employ a plug-in approximation to the optimal rule. 
Experiments with Gemma and T5 models on a range of language benchmarks show that our approach yields better cost-quality trade-offs than cascading and speculative decoding baselines.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduced new speculative decoding variations by combining two techniques: speculative decoding and cascade language models. This is achieved by applying cascade rules on the token level. Experiments showed that the proposed method achieves faster decoding and performs better when the temperature is high.

### Strengths
- The proposed method is lightweight and does not require supervised fine-tuning. 
- The paper flows naturally and is easy to read and understand overall.

### Weaknesses
 - The reasoning behind the designs of the loss functions in Equations (3) and (8) is unclear. 
- The experimental design seems unfair and the improvements are limited. SpecCascade [Token] uses top tokens, while the other methods are evaluated with vanilla sampling at a temperature of 1. Sampling methods like Top-K and Top-P can lead to better performance by avoiding out-of-distribution tokens. To ensure a fair comparison, baseline methods should also use Top-K or Top-P sampling. Given the experiment in Figure 5, which shows that SpecCascade does not improve over lossy SD when T=0, I doubt whether the proposed method offers meaningful enhancements other than inserting a logic removing out-of-distribution tokens. 
- The evaluations in Table 2 and Figure 2 use gamma=5, which is not optimal; speculative decoding typically requires hyperparameter tuning for the best results. 
- The sub-figures in Figure 3 (and other figures with sub-figures) are not properly aligned.

### Questions
1. What is the ground truth (mentioned in lines 76, 156, 166, etc) in this paper? Why would you optimize toward the ground truth probabilities?
2. Line 353, what is OPT?
3. What hardware is used for the experiment? How are the models implemented? 
4. What is SpecDecode [Token] in Figure 3?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work investigates the integration of two front-ended inference strategies: model cascades and speculative decoding. It introduces a novel decoding strategy called speculative cascading. This method combines the strengths of both strategies to achieve a more favorable cost-quality trade-off during inference. Experiments with Gemma and T5 models across  various benchmarks (e.g., summarization, translation, coding, and reasoning) demonstrate the effectiveness of this method, which yields better cost-quality trade-offs than cascading and speculative decoding baselines.

### Strengths
1. The paper addresses a promising and challenging research direction by combining model cascades with speculative decoding.  Recent studies have shown interest in integrating speculative decoding with advanced techniques, such as contrastive decoding [1], to accelerate inference while enhancing the generation quality of LLMs. Speculative cascading complements these efforts by exploring model cascades in speculative decoding. Through both empirical and theoretical analyses, this work innovatively integrates various deferral rules within a speculative execution framework, which is non-trivial and could provide valuable insights for the the academic community.
2. The design of speculative cascading is thorough and well-motivated. The authors provide a clear exposition of the theoretical foundations for both model cascades and speculative decoding, which they summarize effectively in Table 1. Speculative cascading is systematically crafted to leverage the strengths of each of these techniques.
3. The authors conduct extensive experiments with the Gemma and T5 models, carefully detailing experimental settings and effectively validating the efficacy of speculative cascading. The results demonstrate that speculative cascading achieves better cost-quality trade-offs compared to conventional cascades and speculative decoding methods.
4. The manuscript is clearly written, with a well-structured narrative, compelling motivation, detailed analyses, and transparent demonstrations that enhance its readability and impact.

### Weaknesses
1. **Fairness of Comparison**: In Table 2, the authors report minimal latency when matching the quality of a large model, as well as the best quality metric achievable without exceeding the latency of LLMs for each method. However, it is unclear if these comparisons are entirely fair. For instance, it would be helpful to know if the results for BiLD were reported under similar configurations, ensuring a consistent basis for comparison. Specifically, were the same block sizes and temperature parameters used across all methods, and was the trade-off parameter swept in a consistent manner? The lack of clarity on these details makes it difficult to assess the true relative performance of speculative cascading.
2. **Applicability of Speculative Cascading**: Figures 2 and 3 suggest that the quality of speculative cascading can be significantly affected by relative latency. The manuscript would benefit from a more detailed discussion on optimizing the cost-quality trade-off during inference. Specifically, guidance on configurations for maximizing speed-ups while maintaining quality or improving quality without exceeding the latency of the original LLMs, would enhance understanding and practical applicability. The paper should explore how to choose the threshold parameter α to achieve specific latency or quality targets, and discuss the sensitivity of performance to this parameter.
3. **Quality Improvement of Speculative Cascading**: As shown in Figures 2 and 3, the quality improvements of speculative cascading are relatively modest across several tasks, including WMT 5-shot, GSM8K 8-shot, WebQ 1-shot, and NaturalQA 1-shot with Gemma models. This limited improvement in quality may constrain the broader applicability of speculative cascading. Additional discussion on scenarios where speculative cascading performs optimally would provide valuable context for readers. It would be beneficial to analyze the characteristics of tasks or datasets where the method shows the most significant gains, and conversely, the scenarios where it underperforms.

### Questions
Most of my primary concerns are outlined in the weaknesses section above. Here is an additional minor concern:

- In line 527, the authors state, “a lower rejection rate directly translates to a lower latency.” It would be helpful to provide a direct demonstration of this relationship, showing the correlation between latency and rejection rate for clarity.
- As I am not a specialist in the theoretical domain, I cannot fully assess the accuracy of the theoretical analysis presented in this manuscript. My opinion on this aspect may change after reading insights from other reviewers or engaging in further discussions.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies way to interleave two adaptive computation methods: cascading and speculative decoding. The authors present a framework that combines both methods, and aims to enjoy the benefits of both approaches. They also derive theoretical guarantees as to the optimal deferral rule for their method. The key idea is replacing the target distribution in speculative decoding with a different distribution, which takes both the small and large distributions into account. Experimental results on various benchmarks show that the best two variants lead better speed-accuracy tradeoffs compared to either approaches.

### Strengths
- An interesting and intuitive approach: in cascading, the small model can sometimes outperform the larger one. In contrast, in speculative decoding, the model is guaranteed to match the large model quality, but is typically faster. By combining them, the authors allow for fast decoding, with potential improvement, which leads to overall higher speedup.
- Some of the claims are clever. I particularly like the intuition that only considering the confidence of the small model is sub-optimal, and we should also take the large model's confidence into account, and how this could be implemented in speculative decoding (Remark 2).
- The best proposed method (SpecCascade [Token]) seems to outperform all baselines quite consistently.

### Weaknesses
 * I had some trouble following section 4.3. A roadmap/intuition would have been helpful. In particular, I did not fully understand the role of Lemma 3, and the overall takeaway from this section. Specifically, it's unclear how the closed-form expression for the rejection rate directly translates into a practical deferral rule. The connection between minimizing the rejection rate and optimizing the overall speed-accuracy tradeoff is not sufficiently clear. It would be helpful to see a more detailed explanation of how the derived equations lead to a tangible implementation.

- The experiments section was also a bit hard to follow. It starts with outlying the different deferral rules, and then presents the baselines. It seems both parts are somewhat overlapping. It would be helpful to merge them and discuss the link between the two, and particularly not have a paragraph separating the two. The current structure makes it difficult to understand how the different deferral rules are actually used in the baselines and the proposed methods, and how they compare to each other.

- It is not entirely clear from table 2 which lines are the current work and which are previous work. I think only the last two lines are new, but the line separating the different groups appears before the last four lines. Also, the name SpecDecode (which hints of the current work) also appears earlier (SpecDecode [Lossy]). I think this name stems from the new perspective presented in this work, but it is still quite confusing and makes evaluating the results challenging. I would suggest clearly separating existing and new methods both visually (within the table) and by name to avoid confusion.



### Questions
- The intuition behind 4.4 (the first paragraph in that section) is not entirely clear to me. Can you please explain in more detail the problem you are trying to address here?

### Soundness
4

### Presentation
3

### Contribution
3
