# How to Train Long-Context Language Models (Effectively)

- Decision: Reject
- Scores: 5, 6, 6, 6, 6

## Abstract
We study \ctraining{} and \inst{} (\sft{}) of a language model (LM) to make effective use of long-context information.
We first establish a reliable evaluation protocol to guide model development---instead of perplexity or simple needle-in-a-haystack (NIAH) tests,
we use \alexedit{a broad set of} long-context \alexedit{tasks}, and we evaluate \alexedit{models} after \sft{} with instruction data as  this better reveals long-context abilities.
Supported by our robust evaluations, we run thorough experiments to decide the data mix \alexedit{for continued pre-training}, the instruction tuning dataset, and many other design choices. %
 We find that 
(1) code repositories and books are excellent sources of long data, but it is crucial to combine them with high-quality short data; 
(2) \alexedit{training with a sequence length beyond the evaluation length boosts long-context performance};
(3) for \sft{}, using only short instruction datasets yields strong performance  on long-context tasks.
Our final model, \textbf{\ours{}-8B}, \alexedit{which is initialized from Llama-3 and trained on 40B tokens,}
demonstrates state-of-the-art long-context performance among similarly sized models
at a length of 128K. %
\ours{} outperforms Llama-3.1-8B-Instruct on the majority of long-context tasks despite having seen only 5\% as many tokens during long-context training.
Additionally, \ours{} can effectively process up to 512K tokens, one of the longest context windows of publicly available LMs.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The main contributions of the paper are related to evaluations, data mix, and training recipe. 

Evaluation related contribution
* Using HELMET (an existing benchmark) instead of perplexity and needle in the haystack for evaluating long context expansion.
* The authors suggest evaluating LLMs for long context after SFT instead of after pretraining.

Data mix related contributions

* Carefully designed data mixtures like high quality code and books are important. 
* Additionally, the authors ablate the ratio of short context and long context data in the data mix to show that a very high fraction of long context data is detrimental to both long context and short context tasks.

Training recipe: 
* Training on more tokens improves performance of long context tasks
* Increasing pretraining context length beyond target context length can also help long context tasks.
* They also show that synthetic data during SFT can be harmful to long context benchmarks

They combine these improvements to develop a new model called ProLong which achieves better results than prior models on HELMET and NoCha (another long context benchmark).

### Strengths
* Careful examination of individual changes (data mix, sft etc.)
* Final recipe does provide a model that outperforms some of the existing models

### Weaknesses
The paper contributions are somewhat limited. The main contributions are around datamixing and training recipe. The authors make some interesting claims but unfortunately don't investigate these claims further. 

* The results on perplexity are a bit surprising. The authors show that increasing long context data results in perplexity improvements but long context tasks performance is lower. It would be really interesting to understand this further. Is the quality degraded due to the data mix? Or is the target eval task not correlated to the PG19 books dataset?
* The authors show that using synthetic data during SFT can lead to poor performance. It would have been helpful if the authors had verified that the generated data is correct prior to dismissing it. 
* Additionally, using a large model (say Llama 70B) for synthetic data generation could have been more interesting. Perhaps, this larger model would have generated data that can be used for SFT.
* The trends between SFT evaluation and pretrained model evaluation are not clear. In Figure 2, many of the benchmarks show similar trends before and after SFT, so it's hard to conclude that it is necessary to measure performance after SFT as the authors claim. 

The paper would also be stronger if the authors show that their methods generalize beyond just Llama 3 8b. Would the same set of techniques also expand context lengths effectively for other open source models?

### Questions
* How does this recipe scale? Would this recipe work for larger models? 
* Since the model is trained for 512k context length, it would be very helpful to understand the performance of the model at 512k context length tasks. Do any of the evaluations have such long context tasks? 
* The authors mention that the performance on short context tasks is important but don't report performance on these tasks for their final ProLong model. How does ProLong perform on short context tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a continual training recipe, including data curation and multi-stage context extension, that successfully equips the llama-3-8B-instruct model with long context ability up to 512K tokens.

### Strengths
- The model trained with the final recipe (ProLong) shows strong performance on long context benchmarks.

- The proposed data mixture can be a valuable contribution for the community.

### Weaknesses
 - Missing crucial baselines: The author should at least include a very baseline that applies the recipe of Fu et al. (2024) on the llama-3-8B model with 40B tokens to provide a fair comparison between the ProLong recipe and the Fu et al. (2024) recipe on both short and long context tasks. The Table 10 and 12 is not very informative because of lacking both fair comparisons and the short-context results.

- Misleading evaluation: As in L174, the short-context performance is evaluated before SFT, while the long context performance is after SFT (As in L149). However, what people really care about is if the final model after SFT can have both good short and long-context performances.

- The paper claims counterintuitive conclusions but lacks in-depth analyses explaining why they happen. The author claims that training on longer than evaluation context can bring performance benefits (in L331), but it can be simply due to the fact of training on 4B more tokens, which can improve the instruction following ability because of the short data mixture. The author claims that the long synthetic SFT data does not improve performance but it can be simply because of using a weak 8B model for data generation. See more details in the Question section.

### Questions
- Why training on all long context data will harm the downstream long-context tasks? Is it because (1) the proposed ShortMix data actually contains lots of QA data from Fineweb-Edu and Stack Exchange which can improve instruction following (2) the curated long context data (code repos+books) does not have QA data, and training purely on it will harm the instruction following ability?
In Line 351, why use the llama-3-8B-instruct model to synthesize long context SFT data, instead of more powerful models such as lama-3-70B-instruct? I would assume an 8B model cannot accomplish these difficult tasks and can provide low-quality long-context SFT data.

- Could you also evaluate ProLong on some popular synthetic long-context benchmarks such as RULER? In this way, we can have a better understanding of the limitations of ProLong.

- The stage 2 training also doubled the batch size from 4M to 8M. Do you have an ablation study for it? Batch size ramp-up is believed to provide more accurate optimization trajectory and boost model convergences, therefore the performance gains from 512K length training may actually be from the batch size ramp-up instead of longer context.

- Could you also evaluate the final ProLong model on short-context tasks, and add comparisons with a llama3-8B-instruct model SFTed with UltraChat?

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
5

### Summary
This paper investigates the optimal recipe of training a long-context LLM from the data engineering perspective. The authors investigate the effects of data source, mixing proportion of long and short data, etc, and evaluate the trained models on realistic tasks beyond perplexity.

### Strengths
The paper gives a thorough investigation of data engineering for long context training across various aspects, covering long-short performance balance, SFT, and evaluation. This paper can potentially serve as a handbook for long context training. The paper is well-organized and easy to understand.

### Weaknesses
- The evaluation beyond ppl is good and there are some previous studies [1] proprose ppl is not proper for evaluating long-context performance. However, it is kind of confused if the evaluation can serve as a "contribution" of this paper? It seems the paper just adopt the HELMET benchmark (I don't think the decision is a contribution as most long-context works have adopted some realistic benchmarks like LongBench [2] and InfiniteBench [3]).

- The paper proposed short-context instruction tuning is sufficient for achieving good performance. The study is conducted by mixing partial long synthetic instruction data. The authors found that the incorporation of long synthetic data would degrade the long-context performance.  As our understanding in short-context scenario, data quality is (most) essential for SFT [4]. However, the synthetic long-context data (generated by LLaMA-3-8B) is probably of low quality. So I think this study only demonstrates that long synthetic data is not good enough for improving long-context performance. BTW, have you compared the long-context performance before and after SFT? LLaMA 3.1 technical report [5] proposed the long-context performance would degenerate with short instruction data only after SFT. I wonder if this point holds here.

- I believe summarization is a vital and basic long-context ability, however, there is a significant performance drop in the summarization task after ProLong's training (compared to naive LLaMA-3.1). Is this due to the lack of some long data types/sources in training data (books and code only)? The information in long books and codes may be distributed without summarizing. I feel like arxiv/wikipedia  (which you only use in shortmix) are good data sources for summarization, as they naively contain an abstract section. The authors can consider including more data sources with ablations (as that in Table 4).

- Would you consider reporting results on more benchmarks like RULER [6] and InfiniteBench [3]? HELMET is a good but new benchmark while some experiences (e.g., the degeneration of long-context performance when using short instruction data only.) are acquired from evaluation on some older benchmark. More results would help us align the findings.

### Questions
See weaknesses above.

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper study the problem of how to effectively adapting a short-context language models to be long-context. The paper first starts with identifying deficiency in widely used perplexity and Needle-In-A-Heystack test and establishing a reliable evaluation protocol for long-context LLM by adopting HELMET, which covers diverse range of realistic long-context applications. 
The authors also advocate for (1) checking model performance after supervised finetuning (2) ensuring that model performance on short-context tasks is not compromised after long context training. For long context data curation, the authors provide best practices for (1) data mixture in long-context data (2) quantity ratio between long and short context data (3) choosing high-quality short-context data. 
Next, the paper discuss the impact of scaling training tokens and context length on both long and short task performance. Finally, the recipe ends with exploration on the choice of SFT data, pointing out that short-context instruction data can yield strong long-context result. The resulting long-context model ProLong as well as associated code and data are open-sourced.

### Strengths
1. The paper is very well structured and written, and is easy to follow.
2. The paper thoroughly explored important components and provide useful observations for long-context language models development, including training recipe and evaluation protocol. From the evaluation perspective, the authors underscore the importance of using diverse and realistic long-context tasks rather than relying on conventional perplexity-based and needle-in-a-haystack-like benchmarks. The preservation of short-context performance is also highlighted. From the training perspective, the authors conducted experiments and found empirically effective choices of data mixture, data ratio, and data quality.
3. The ultimately trained model, ProLong, achieves strong long context performance at 10B parameter level.
4. The assets associated with this paper could serve as useful resources for the research community and are open-sourced.

### Weaknesses
1. The choice of long-context evaluation benchmark(HELMET) seems arbitrary. The authors should discuss the rationale behind selecting HELMET instead of other long-context benchmarks, such as LongBench, Infinite Bench, etc.
2. The training-free length extrapolation methods compared in the paper is limited. The experiments would be more solid if more advanced training-free extension methods are incorporated, e.g., SelfExtend and ChunkLLaMa.
3. There exists other community-tuned long-context LLMs initialized from LLaMa-3-8B-Instruct, e.g., gradientai/Llama-3-8B-Instruct-Gradient-1048k. As they claim their training process only consume 1.4B tokens, it would be more convincing to include such models as strong baselines.

### Questions
See Weakness above.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper addresses the challenges involved in training language models (LMs) to make effective use of long-context information. It proposes a systematic methodology that goes beyond traditional evaluation metrics, such as perplexity, to train models capable of handling long-context inputs more effectively. The authors introduce ProLong-8B, a model initialized from Llama-3 and trained on 40 billion tokens, demonstrating state-of-the-art performance for long-context tasks.

### Strengths
1.  The study highlights that training on a mix of both long and short-context data sources is key to achieving good performance across tasks. The authors show that using long-context data like code repositories and books, balanced with high-quality short-context data, preserves both long and short-context abilities of the model.
2.  The extensive ablation experiments provide meaningful insights into effective training practices. For instance, the paper reveals that training only on long-context data negatively impacts overall performance and that including high-quality short-context data is essential for optimal results.
3. The resulting ProLong-8B model achieves strong performance on long-context tasks compared to similarly sized models

### Weaknesses
1. **Misalignment Between Title and Content**: A significant portion of the paper focuses on data engineering rather than providing comprehensive training methodologies for long-context language models, which does not fully align with the promise of the title. To better align with the title, the paper could have included more discussions on training techniques, such as **pose: efficient context window extension of LLMs via positional skip-wise training** and **CLEX: Continuous Length Extrapolation for Large Language Models**. Additionally, incorporating experiments involving different rotary position encoding methods and synthetic data, such as **LongSkywork: A Training Recipe for Efficiently Extending Context Length in Large Language Models**, would provide a more thorough exploration of how to train long-context LLMs.

2. **Benchmark Justification**: In Section 2, the necessity of introducing a new benchmark is not clearly justified, especially considering that many of the tasks overlap with existing benchmarks like **RULER**. Providing more rationale for the benchmark's uniqueness？

3. **Lack of Explanation**: In Section 3.2, the authors note that previous techniques (using long text) deteriorate short-context performance, but they do not provide a satisfactory explanation for this phenomenon. Without a clear rationale, the motivation for mixing in short-context training data remains weak.

4. **Insufficient Explanation of Data Mixture Ratios**: The paper proposes two mixture ratios—one for combining long-context data sources (books and repositories) and another for mixing long and short-context data. While the experiments show the effectiveness of these ratios, there is no clear explanation of why these particular proportions work. 

5. **Lack of Comparison with Short-Context Performance Task**: The final experiments lack a comparison with short-context performance tasks. Including such comparisons would provide a more holistic evaluation of the model's performance.

### Questions
The paper's contributions are not clearly defined in terms of their nature, like technical report？ If the paper aims to contribute as a methodological study on data engineering, the novelty seems insufficient, as it mainly provides data mixture ratios without in-depth justification or exploration. On the other hand, if it aims to be an experimental study, the lack of diverse experiments and limited comparisons with other training approaches weakens its claims of novelty.

### Soundness
1

### Presentation
4

### Contribution
2
