# Min-K%++: Improved Baseline for Pre-Training Data Detection from Large Language Models

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
The problem of pre-training data detection for large language models (LLMs) has received growing attention due to its implications in critical issues like copyright violation and test data contamination. Despite improved performance, existing methods (including the state-of-the-art, Min-K%) are mostly developed upon simple heuristics and lack solid, reasonable foundations. In this work, we propose a novel and theoretically motivated methodology for pre-training data detection, named Min-K%++. Specifically, we present a key insight that training samples tend to be local maxima of the modeled distribution along each input dimension through maximum likelihood training, which in turn allow us to insightfully translate the problem into identification of local maxima. Then, we design our method accordingly that works under the discrete distribution modeled by LLMs, whose core idea is to determine whether the input forms a mode or has relatively high probability under the conditional categorical distribution. Empirically, the proposed method achieves new SOTA performance across multiple settings (evaluated with 5 families of 10 models and 2 benchmarks). On the WikiMIA benchmark, Min-K%++ outperforms the runner-up by 6.2% to 10.5% in detection AUROC averaged over five models. On the more challenging MIMIR benchmark, it consistently improves upon reference-free methods while performing on par with reference-based method that requires an extra reference model.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a method, Min-K%++, designed to detect pre-training data in LLMs by identifying local maxima in the model’s conditional distributions. The proposed approach theoretically grounds pre-training data detection in maximum likelihood training, showing that training instances often exhibit distinct distributional patterns. From the empirical experiments, it demonstrate that Min-K%++ achieving competitive performance on benchmarks like WikiMIA and MIMIR, with notable improvements over prior methods, particularly in challenging settings.

### Strengths
The originality of Min-K%++ lies in its focus on identifying local maxima to detect training data, moving beyond heuristic-based methods by leveraging theoretical insights from maximum likelihood training. The quality of the experiments is high, covering multiple benchmarks and various model sizes, showing consistent improvements over state-of-the-art baselines. The clarity is adequate in explaining the methodology and motivation, though some sections could benefit from clearer illustrations. The significance is evident, as pre-training data detection can enhance model transparency and accountability, which are critical in LLM applications.

### Weaknesses
The novelty of Min-K%++ is somewhat limited, as it builds incrementally on the existing Min-K% methodology rather than introducing a transformative approach. Additionally, the paper does not provide sufficient information about the computational resources required for implementing Min-K%++, which makes it difficult to assess the method’s feasibility on different hardware configurations or scales. While the benchmarks are well-chosen, a comparison with broader language tasks would better illustrate Min-K%++'s general applicability.

### Questions
- What is the computational overhead of Min-K%++ compared to baseline methods, and is it feasible for real-time applications?

- Would Min-K%++ perform well on diverse language corpora with complex semantics or high paraphrasing, or would adjustments be needed?

- Could you explain the theoretical choice of $\mu_{x<t}$ and $\sigma_{x<t}$ as calibration factors, especially in improving detection sensitivity in noisy settings?

### Soundness
4

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
4

### Summary
This paper provides a MIA (Membership Inference Attack) method to detect whether data was used to train models, building upon previous MIN-K methods. Instead of using absolute logit likelihood values, they propose subtracting the mean of previous token likelihoods to identify how far the current value deviates from the previous distribution. This method shows improvements over MIN-K on two benchmarks, WIKIMIA and MIMIR, across different models.

### Strengths
- The research topic is important and worth more work for it.
- I love the motivation based on ISM objects, but sadly it seems that this does not lead to a well-established method based on this.

### Weaknesses
 - The theoretical connection between Section 4.1's gradient conditions ($\frac{\partial \log p(x)}{\partial x_i} = 0$ and $\frac{\partial^2 \log p(x)}{\partial x_i^2} < 0$) and the proposed normalized score method ($\frac{\log p(x_t|x_{<t}) - \mu_{x_{<t}}}{\sigma_{x_{<t}}}$) for min-k% token selection needs clearer explanation. The current presentation shows a gap between the theoretical motivation and practical implementation. Specifically, the link between the ISM object's hidden dimension and the probability of a token is not clearly established. The argument that training data forms a local maximum is not sufficiently connected to the proposed method. The conclusion that trained examples have high perplexity is too shallow, and the ISM object section does not provide a strong theoretical foundation for the method. A more direct connection, such as observing patterns in the final layer token hidden state before the decoding head, would be more convincing.

- The justification in lines 256-263 regarding the method's effectiveness on rare or difficult-to-learn training texts requires stronger argumentation. For rare texts, distinguishing between untrained and rare samples remains challenging regardless of whether using direct scores or mean-subtracted scores. The same applies to inherently difficult-to-learn texts. This limitation needs to be addressed more explicitly. While the argument that the predicted distribution across the vocabulary could be near uniform for rare or difficult texts is reasonable, it does not fully address the core issue of distinguishing between untrained and rare samples. The method's ability to detect training data despite low absolute values of $\log p(x_t|x_{<t})$ needs more empirical validation.

- The state-of-the-art landscape has evolved beyond Min-K. Recent methods like [ReCall](https://arxiv.org/pdf/2406.15968) have demonstrated significant improvements, achieving nearly 20% performance gains over Min-K on the WIKIMIA benchmark. Including comparisons with these newer methods would strengthen the paper's relevance. While Min-K was among the first to apply MIA for data contamination detection, its limitations based on its underlying assumptions should be acknowledged. The lack of comparison with more recent state-of-the-art methods significantly impacts the evaluation of the proposed method's effectiveness.

- The MIMIR benchmark results, where most methods show minimal performance differences, warrant further discussion. The assumption that reference-based methods should naturally outperform reference-free approaches needs reconsideration, as these references differ from ground-truth evaluations. Therefore, achieving comparable performance to reference-based methods could serve as compelling evidence for method validation. The paper should explore why reference-based methods do not show a clear advantage on the MIMIR benchmark and discuss the implications of this finding for the proposed method.

### Questions
I think conceptually we should have several groups of data to be classified, and these groups should be 'imagined' by researchers who are truly spending time looking at the *pattern of pre-training corpora*. Given a pre-trained chunk $s = \langle s_1,s_2,...,s_n\rangle$ with n tokens, we need to consider the false positive and false negative rates of proposed methods to identify:

1. Subportions of text $s' = \langle s_i,...,s_j\rangle$
2. Rare sequences versus untrained sequences
3. Rare tokens $s_i$ within a sequence

I am concerned that there are many nuances here, and these methods seem to capture them not very effectively.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a methodology for pre-training data detection, Min-K%++. They reduce the problem as identification of local maxima. Their method achieves state of the art results across multiple settings.

### Strengths
The paper is well written and it is easy to follow.

The paper shows the best results (or second best when reference models are used for the MIMIR benchmark) reported on the existing benchmarks, and compares with 6 established baselines for MIA task.

Figure 2 and Figure 3 in the paper provide a very good  summary of  the idea that the paper follows (first the concept of local maxima for identification of training examples, and second how it contrasts with prior work that solely looks at token probability).

### Weaknesses
Line 323: any additional benchmarks you could think of designing for this task? there are new open source LLMs for which the training data is also provided. I think the paper could be stronger if it is not only relying on existing benchmarks for MIA task, and devises its own.

I think the paper could improve if you clarify why MIMIR and WIKIMIA are the right datasets to measure this for the models used for evaluation. Line 347 and 352 touch on it but do not expand on why the current models have not seen the entire set. I am more curious about WIKIMIA for recent models, and how they are comparable as they are trained at different times.

Line 147. Is Wang et al . 2022 the right ppaer to cite to refer to auto-regressive LLM maximum log likelihood training?

I wonder if the findings in this paper may merit a discussion and a mention in comparison to what is presented in yours. https://arxiv.org/pdf/2212.04037, thoughts?

Line 328: could you elaborate how the paraphrased inputs are created for the WIKIMIA dataset? How is it ensured that the paraphrases are accurate?

Line 460: why focus on WIKIMIA and Llama-13B ?

### Questions
Line 147. Is Wang et al . 2022 the right ppaer to cite to refer to auto-regressive LLM maximum log likelihood training?

I wonder if the findings in this paper may merit a discussion and a mention in comparison to what is presented in yours. https://arxiv.org/pdf/2212.04037, thoughts?

Line 328: could you elaborate how the paraphrased inputs are created for the WIKIMIA dataset? How is it ensured that the paraphrases are accurate?

Line 460: why focus on WIKIMIA and Llama-13B ?

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
5

### Summary
This paper presents a novel pretraining data detection method, theoretically identified as the optimal solution. It reframes the data detection problem as one of identifying local maxima, utilizing average and standard deviation metrics rather than relying on reference models. Experiments across two benchmarks and five models highlight the effectiveness of MinK++.

### Strengths
1. The motivation is clear and makes sense, which has been demonstrated by theoretical analysis.
2. The method is very simple and effective, which impresses me.
3. The experiments are very solid across two benchmarks, 5 models, and 6 baselines, which also highlights the effectiveness of MinK++.
4. The writing is good and easy to follow.

### Weaknesses
The work is very solid and has no more significant weaknesses.

1. It would be better to add some impactful works of 2024 in related works, including `A Careful Examination of Large Language Model Performance on Grade School Arithmetic` [1] and `Benchmarking Benchmark Leakage in Large Language Models` [2].

### Questions
I came across the DC-PDD paper [1], which concluded that MinK++ performs worse than MinK on their PatentMIA Benchmark. I'm curious to understand the reasons behind this. If you have the time and are willing to share your thoughts, I would greatly appreciate it. Of course, I understand if you're too busy and can't respond.

[1] Pretraining Data Detection for Large Language Models: A Divergence-based Calibration Method. https://arxiv.org/pdf/2409.14781

### Soundness
4

### Presentation
4

### Contribution
4
