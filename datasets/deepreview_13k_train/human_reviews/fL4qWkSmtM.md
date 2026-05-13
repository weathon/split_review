# What is Wrong with Perplexity for Long-context Language Modeling?

- Decision: Accept
- Scores: 8, 6, 6, 6, 8

## Abstract
Handling long-context inputs is crucial for large language models (LLMs) in tasks such as extended conversations, document summarization, and many-shot in-context learning. While recent approaches have extended the context windows of LLMs and employed perplexity (PPL) as a standard evaluation metric, PPL has proven unreliable for assessing long-context capabilities. The underlying cause of this limitation has remained unclear.
In this work, we provide a comprehensive explanation for this issue. We find that PPL overlooks key tokens, which are essential for long-context understanding, by averaging across all tokens and thereby obscuring the true performance of models in long-context scenarios. To address this, we propose \textbf{LongPPL}, a novel metric that focuses on key tokens by employing a long-short context contrastive method to identify them. Our experiments demonstrate that LongPPL strongly correlates with performance on various long-context benchmarks (e.g., Pearson correlation of -0.96), significantly outperforming traditional PPL in predictive accuracy. Additionally, we introduce \textbf{LongCE} (Long-context Cross-Entropy) loss, a re-weighting strategy for fine-tuning that prioritizes key tokens, leading to consistent improvements across diverse benchmarks. In summary, these contributions offer deeper insights into the limitations of PPL and present effective solutions for accurately evaluating and enhancing the long-context capabilities of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper modified standard PPL and CE (cross entropy) loss, by weighting more to key tokens in long text. The key tokens are identified through a long-short context constrastive method. The experiments demonstrate the LongPPL correlates long-context capabilities of LLM, thus a good metric. Similarly, applying LongCE loss in long-context fine tuning shows improvement on long-context benchmarks.

### Strengths
The idea is simple and seems working well.

### Weaknesses
n/a

### Questions
1. I wonder how would fine tuned model perform on normal context length benchmarks, will it remain roughly at the same level or regress a bit?
2. How long is considered as "long-context". In experiments, 32k is used. I wonder how much this method would affect on other context lengths.
3. can we use equation (5) directly for LongCE instead of (8). so only differentiate on key tokens, would that be doable?

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
4

### Summary
The paper critiques the use of perplexity (PPL) as a standard metric for evaluating large language models (LLMs) on long-context tasks, arguing that PPL’s averaging across all tokens fails to capture the importance of "key tokens" critical for understanding long-context dependencies. To address this, the authors introduce Log Probability Gain (LPG) and Log Probability Values (LPV) to identify these key tokens, leading to LongPPL—a refined metric that emphasizes these crucial tokens, thus providing a better measure of long-context performance. Additionally, they propose LongCE, a re-weighting strategy applied during fine-tuning that bolsters the model's ability to handle long-context tasks through an expectation-maximization (EM) approach. Although LongCE adds computational overhead, the authors show that it consistently outperforms traditional cross-entropy (CE) across various settings.

### Strengths
This paper conducts a fine-grained analysis to investigate why perplexity (PPL) fails to capture long-context capabilities in LLMs. Few previous studies focus on re-weighting tokens to improve long-context performance; this work addresses this directly by re-weighting tokens based on their dependence on long-context information, providing a more fundamental and targeted solution.

### Weaknesses
Some settings in the figures lack clear explanations, which affects the reliability of the figures and the conclusions drawn from them. For example, in Figure 2, the specific prompt lengths for each data point are not provided, making it difficult to interpret the statement, "Each point represents the results obtained from testing at a specific prompt length."
Although the correlation arguments seem promising and qualitatively sound, they would benefit from added statistical rigor, such as p-values from hypothesis testing to confirm the significance.
The naming of Log Probability Gain (LPG) and Log Probability Values (LPV) is not intuitive, which may hinder understanding and adoption of these concepts.
Additionally, the experiments are conducted with a sequence length of 32K, a length considered relatively manageable by recent research. Testing on longer sequences could introduce challenges that may not align with current trends, potentially impacting the generalizability of the results
Lastly, the criteria for selecting experimental models are not clearly defined, which introduces some ambiguity regarding the rationale behind the choice of models used in testing.

### Questions
1. Is the main reason perplexity fails due to its inability to correctly identify answer/key tokens?
2. Could you clarify what "task-aware" means in this context? Does it refer to distinctions between short-context and long-context tasks, or could it apply to other task definitions as well?
3. You mention that "even though the Llama-3.1 model we use is only 8B in size, it still obtains LongPPL with a strong correlation, suggesting high compatibility with powerful long-context models, even with smaller parameter sizes." Are you implying that LongPPL would show higher correlation with larger models? If so, could you explain why?

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
2

### Summary
The authors state that perplexity metrics (PPL) are insufficient for evaluating the long-context capabilities of large language models (LLMs) because PPL considers both answer and non-answer tokens, resulting in perplexity scores that do not correlate with LongBench scores. To address this, the authors propose two new metrics, LongPPL and LongCE, which extract key tokens from the model output with the help of a relatively strong model as the evaluator. LongPPL is used as an evaluation metric for LLMs in long-context text, while LongCE serves as a loss function when fine-tuning LLMs on long-context tasks.

### Strengths
- The introduction of LongPPL and LongCE represents an innovation in the evaluation and fine-tuning of LLMs for long-context tasks. These metrics address the limitations of traditional perplexity and Cross Entropy loss, providing more accurate and task-relevant assessments of model performance.
- The concepts presented by the authors are easy to understand, including the motivation and method. The figures greatly help in understanding the concepts and the experiments.

### Weaknesses
 - LongPPL metric relies on a relatively strong model (medium-sized Qwen2-72B-Instruct) as an evaluator to identify key tokens. This dependence may limit the applicability of the metric in scenarios where such a strong model is not available or practical to use. The reliance on a large model for key token identification introduces a potential bottleneck, especially in resource-constrained environments, and the paper does not sufficiently explore the impact of using smaller models for this task, which could affect the robustness and generalizability of the metric.
- The additional computational cost associated with identifying key tokens may still be significant. This could be a barrier to adoption in resource-constrained environments. The paper acknowledges the overhead but does not fully quantify the practical implications, particularly in terms of wall-clock time and energy consumption, which are crucial for real-world applications. The computational cost of LongPPL, involving multiple forward passes, needs a more detailed analysis, especially when compared to the single forward pass required by traditional perplexity metrics.

### Questions
- How does the performance of LongPPL and LongCE change when using a weaker model for key token identification? Have you tried using the same model for both evaluation and key token identification?
- The paper discusses the overhead of using LongCE in LLM fine-tuning compared to the original Cross Entropy. How does the evaluation time of using LongPPL compare to traditional perplexity (PPL) metrics?

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
This paper proposes a new metric LongPPL and a new training objective LongCE. The LongPPL is calculated over selected tokens that satisfy the following conditions when evaluated with an evaluator model: (a) the tokens have higher probability conditioned on long context than short context (b) the tokens are predicted with high probability. Results show that the proposed metric better correlates with long-context downstream tasks than standard perplexity. The proposed LongCE loss adapts the standard focal loss by reweighting the tokens based on their performance given long and short context. Results demonstrate that models finetuned with LongCE achieve better long-context downstream task performance.

### Strengths
- This paper proposes a new metric LongPPL which better correlates with long-context downstream performance.
- This paper proposes a new training objective LongCE tailored for improving long-context performance.

### Weaknesses
 - The proposed LongPPL is limited by the evaluator model. Concretely, the validity of the evaluation is strictly bounded by the maximum effective length that an evaluator model can reliably handle. Additionally, the two thresholds, which depend on both the evaluation data and the evaluator model, can further complicate the evaluation process. These limitations weaken the universality of the proposed metric.
- The key token selection of LongPPL is motivated by observing large gains in log probability of the ‘answer’ tokens in LongEval, a retrieval-based synthetic test. It raises the question of whether the gains primarily come from the improved prediction of less frequent n-grams that re-appear later in the context, as studied by [1][2]. If so, the motivation of leveraging an evaluator model is obscure since one can simply evaluate those re-occurred n-gram tokens, which are much more convenient to find and overall a more universal setup than LongPPL. 
- The LongCE loss should be compared with the standard focal loss [3] baseline to understand if it is really necessary to add the contrasting term of long and short context perplexity. The standard focal loss does not require extra forward pass for computing short context log probability, thus can potentially improve training efficiency. 
- The LongCE loss seems to improve mostly the retrieval-based test (LongEval), however, demonstrate little gains on RULER, which has a few non-retrieval tasks, and almost zero improvement on LongBench, which contains quite a few non-retrieval tasks (Figure 7). It is unclear to what extent the proposed method benefits non-retrieval tasks.

### Questions
- Why does finetuning with LongCE demonstrate such different results for mistral-7b and llama2 on RULER, with one hardly improving (<1) and one significantly improving (~10)?
- Why does figure 6 only contain correlation between longPPL and longbench score? What is the correlation between standard PPL vs longbench score?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper first tries to understand why perplexity metric fail to reflect long-context ability of LLMs. For instance it has been shown that perplexity of LLMs shows almost no correlation with their long-context performance measured on a dataset such as Longbench.

Authors show the reason is because perplexity is computed over all tokens of the answer to a query, wether this tokens are ‘key’ or not to answer to the query. Consequently, perplexity computed equally over all tokens do not represent long-context performance. Therefore,  computing ppl by averaging only on key tokens (instead of all tokens)  avoid this dilution and correlates better with long context benchmarks scores such as the ones measured on Longbench.

A longPPL measure that takes into account this observation is proposed by the authors, where they compute perplexity by averaging solely on the selected key tokens.
But how do the authors extract the ‘key’ tokens from the natural text in the answer to a query ? 
 This is done by introducing a simple and elegant metric which consists in computing the difference - for each token x - of the probability p(x/long_context) and p(x/shortened_context). This metric called LPG score, measures the improvement of prediction accuracy induced only by the long-context => a high value indicates that long context plays an important role in the prediction of x, so x is a key token and should be taken into account to compute LongPPL (and it should not be taken into account - for compute the PPL - otherwise). 

Building on this finding, they develop an efficient long-context training strategy by prioritizing key tokens. Specifically, they introduce the LongCE (Long-context Cross-Entropy) loss, which assigns higher weights to key tokens, identified dynamically by the model itself.
Experiments across various LLMs demonstrate that fine tuning a model using the LongCE  loss consistently outperforms traditional CE loss, across multiple LLMs and multiple long context benchmarks.

### Strengths
-Paper very clearly presented and very progressive, starting from identifying a problem, explain why it occurs and propose an efficient solution for it

- convincing explanation on why PPL is not a good indicator of quality for long context LLMs (with illustrations on a long context benchmark)

-Fine tuning with longCE loss leads to improvements on several long context benchmarks and for several LLMs ; very convincing results

### Weaknesses
 -I don’t fully agree this the claim « the evaluation of long-context capabilities still heavily relies on perplexity (PPL) as the de facto metric » as we see now most papers relying on long-context benchmarks or use the needle-in-the-haystack test to evaluate long-context LLMs

-The reference to ppl is not the good one (Bengio did not invent perplexity!), you should credit people who actually were the first to introduce this metric. Perplexity was originally introduced in 1977 in the context of speech recognition by Frederick Jelinek, Robert Leroy Mercer, Lalit R. Bahl, and James K. Baker. See https://en.wikipedia.org/wiki/Perplexity

-I’d like to learn more about the computational implications of calculating LongPPL and LongCE, especially since the LPG score needs to be computed for each token (see my question below). I'm particularly curious about the costs associated with LongCE, as described in Section 3.2. While the Implementation details of LongPPL in the Appendix were helpful, I still want to understand more about how computationally expensive this process is.

### Questions
-computed longPPL and longCE (as opposed to PPL) must be more costly; how much more costly (especially a you need to compute the LPG score for each token at training time) ?

-do you fine tune with longCE only or with a combination of CE and longCE ?

-what about using the needle-in-the-haystack test for your evaluation of long context models ?

### Soundness
4

### Presentation
4

### Contribution
4
