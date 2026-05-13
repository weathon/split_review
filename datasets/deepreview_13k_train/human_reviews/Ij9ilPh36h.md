# The Hyperfitting Phenomenon: Sharpening and Stabilizing LLMs for Open-Ended Text Generation

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
This paper introduces the counter-intuitive generalization results of overfitting pre-trained large language models (LLMs) on very small datasets. In the setting of open-ended text generation, it is well-documented that LLMs tend to generate repetitive and dull sequences, a phenomenon that is especially apparent when generating using greedy decoding. This issue persists even with state-of-the-art LLMs containing billions of parameters, trained via next-token prediction on large datasets. We find that by further fine-tuning these models to achieve a near-zero training loss on a small set of samples -- a process we refer to as hyperfitting -- the long-sequence generative capabilities are greatly enhanced.
Greedy decoding with these Hyperfitted models even outperform Top-P sampling over long-sequences, both in terms of diversity and human preferences.
This phenomenon extends to LLMs of various sizes, different domains, and even autoregressive image generation. We further find this phenomena to be distinctly different from that of Grokking and double descent. Surprisingly, our experiments indicate that hyperfitted models rarely fall into repeating sequences they were trained on, and even explicitly blocking these sequences results in high-quality output. All hyperfitted models produce extremely low-entropy predictions, often allocating nearly all probability to a single token.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper discovers a new phenomenon in fine-tuning LLMs on tiny datasets, which they term Hyperfitting as it's closely connected to overfitting. Surprisingly, while overfitting indeed increases validation perplexity, the model performs much better in open-text generation as rated by human evaluation. They find that models even perform comparably to those with 10x larger parameters in open-ended generation tasks. The phenomenon is demonstrated across three different models and three validation datasets across different domains in text generation. Additionally, they also conduct preliminary experiments in autoregressive image generation and observe similar effects. The authors also find that the fine-tuned models tend to generate a more diverse context, which may help mitigate the common repetition issue in long-text generation.

### Strengths
- The paper is well-written and easy to follow
- The phenomenon is novel and quite surprising, especially its implication in reducing the repetition issues. The paper opens up a new perspective in understanding repetition in text generation. 
- I enjoyed reading the experiment results presented in the paper. E.g., the experiments in Section 6.2 present an interesting finding that the model fine-tuned on News performs better in human evaluation than the ones fine-tuned on Fiction and Wiki. This result is surprising given that Fiction, with its inherently diverse and creative language, might be expected to enhance performance more. This finding invites further exploration into how different training domains impact model generation quality.

### Weaknesses
 - The experiments focus on relatively small models, with the largest at 8B parameters. Since Hyperfitting is studied on small datasets, extending the analysis to larger models could provide insights into whether this phenomenon scales and is influenced by model capacity.
- A related issue is that the models are only evaluated in a limited range of datasets, which may not fully capture the phenomenon’s applicability across domains and tasks. For example, it would be useful to see how Hyperfitting behaves in specialized domains such as legal summarization [1], medical transcription [2], or dialogue summarization [3]
- Some implementation details appear to be missing. E.g. are training and evaluation results averaged over different random seeds to ensure consistency? Moreover, are all parameters updated during fine-tuning? If so, does the phenomenon also exist in parameter-efficient fine-tuning, e.g. LoRA [4]?

### Questions
Please refer to the weaknesses part.

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
This work studies a surprising phenomenon that occurs when a modern LLM is overfit to a small text corpus finding that a model's greedy decoding capabilities are actually improved in various ways rather than degenerating as one might expect. They observe that after training a model to near zero loss on the small target corpus, while these models become poor "language models" for other held out text (poor validation loss), in _generative_ evaluation scenarios, "hyperfitted" models produce better outputs according to human judges and exhibit higher diversity in their completions as compared to the base models from which they are derived. They also perform similar experiments with autoregressive image generation models and observe similar effects. They present and analyze an explanation for these observations focusing on the "sharpening" of the model's predictive distribution and ablate the effect of the dataset and training curricula on these phenomena.

### Strengths
1. Work explores an interesting phenomenon and presents it as "curious" without resulting to hyperbolic/"hype"-y language.
2. Contextualization in prior work is relatively complete.
3. A variety of diversity measures are used to examine the difference in output distributions caused by "hyperfitting" in a wholistic manner.
4. The human preference evaluation is a strong test for impact of hyperfitting, and the results for the hyperfitted models are promising -- the recovery of the 7B and 8B models to near equivalence in preference to ground truth completions is surprising.
5. In the event one wanted to use a hyperfitted model in practice, the "citation-blocking" mechanism is a simple and practical solution to the increased generation overlap with the small training corpus that hyperfitting causes.

### Weaknesses
1. There is only a focus on the impact to open-ended generation (continuation/completion) and not enough focus on utility. There are no conversational benchmark scores like AlpacaEval or MT-bench, nor knowledge intensive benchmark scores such as for MMLU or other tasks available in suites like the lm-eval-harness. The absence of these evaluations makes it difficult to assess the practical relevance of the observed 'hyperfitting' phenomenon. While the paper demonstrates increased diversity and human preference in open-ended generation, it remains unclear if these benefits translate to more structured tasks or real-world applications where specific outputs are expected.
2. Use of base models only in this particular case is an issue since it might reveal more about the observation and hypothesized mechanism being presented if instruction tuned models were included in the analysis. The study's focus on base models limits the generalizability of the findings. It is possible that the observed effects of hyperfitting are specific to models trained solely on next-token prediction and might not apply to instruction-tuned models which have undergone additional training stages. This raises questions about whether the 'sharpening' of the predictive distribution is a phenomenon that would also be observed in models that have already been optimized for specific tasks or conversational abilities.
3. Diversity and length are not equal to output quality or utility, and this equivalence both implicit in the analysis as well as explicitly stated a few times. The paper's analysis frequently conflates diversity and length with overall output quality and utility. While the authors demonstrate that hyperfitted models produce more diverse and longer outputs, it is not clear that these outputs are necessarily more useful or of higher quality. The human preference evaluation is a step in the right direction, but it is still a limited measure of overall utility. A more comprehensive evaluation would consider metrics that directly assess the usefulness of the generated text in specific contexts.

### Questions
Primary:
1. Relating to the weakness about lack of benchmark scores, what do the differences in MMLU or other leaderboard tasks look like? I know Tinyllama scores too poorly to measure on many tasks, but the 7B and 8B models should have non trivial base performance. I suspect that since hyperfitting seems to destroy the ability of the model to properly assign loss values to val data (eg. no longer is a good "language model" in the technical sense of the term), this will impact these types of benchmarks. If benchmark scores after hyperfitting are near chance or even just significantly degraded, try reformulating the tasks as a generative evaluation and checking the hyperfitted model again.
2. Relating to the weakness about only including base models, did the authors run any experiments with instruction tuned versions of these same base models? I hypothesize that hyperfitting to these stories or news datasets effectively seems to do some of the work that all of the post training process normally accomplishes. Whatever this unqiue style of training does, seems to sort of take the model out of LM p(x) mode and into generator f(x)->y mode. So... what happens when you try to "hyperfit" an already post-trained model? Does it get worse/better/remain unchanged wrt the diversity analyses presented and the benchmark scores noted in prior comments?

Minor:

3.  In Table 3, what do "@1/3/5 Prob" mean? They are not defined anywhere and this table has no descriptive caption.

4. TTR seems to be a measure from linguistics and child language acquisition research, please define this inline in the sentence in which it is first used. Alternately use some self-evident description like "ratio of unique n-grams" for n=1 and other values. Also, Self-BLEU considers up to what n-value in this analysis? Generally, discussion and analysis of n-gram diversity and n-gram copying rate from training data might be more interpretable.

### Soundness
4

### Presentation
4

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
The paper introduces the hyperfitting phenomenon, where overfitting pre-trained LLMs on a small dataset until it achieves near-zero training loss enhances the LLMs' long-form generation capabilities, yielding higher-quality texts that are preferred by humans, despite the models achieving significantly worse validation losses. In particular, the paper finds this phenomenon across models hyperfitted on Fiction-Stories dataset, these models rarely repeat training sequences and produce low-entropy predictions. The paper takes an approach to explain this phenomenon with the concept of top-rank encouragement, where hyperfitting prioritizes desirable tokens in the top ranks of predictions, resulting in improved text quality.

### Strengths
1. The paper is well written and easy to follow.
2. The discovery of the hyperfitting phenomenon is interesting, and the paper includes sufficient experiment to support this.
3. The explanation on the hyperfitting phenomenon is convincing.

### Weaknesses
1. I'm not quite sure what specific applications this phenomenon has, because LLM practitioners rarely use pretrained base models directly for generation tasks. Generally, they first perform SFT (supervised fine-tuning) and then use chat models for generation. However, this paper does not compare the generation quality between hyperfitted models and chat models.
2. Although this paper shows hyperfitting can improve the generation quality, its impact on the model's internal knowledge, hallucination, and other factors has not been studied in the article. I suggest that the authors test the effects of hyperfitting on model performance using datasets like MMLU and GSM8K.

### Questions
Please refer to weaknesses

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
This paper focuses on the problem of repetitive generation results with large language models (LLMs) under greedy decoding strategy. Specially, this paper introduces a newly-observed phenomenon called *hyperfitting*, which helps to eliminate the repetition problem. This is achieved by finetuning the LLM on a separated small dataset untill achieving minimal loss. This paper runs abundant experiments to show that, hyperfitting can efficiently increase the token diversity as well as human preference for greedily generated text, with a side effect that the conditional token probability distributions are generally sharpened. Also, such hyperfitting phenomenon is observed in popular LLMs such as Llama 3.1, and even in image generation models (ImageGPT).

### Strengths
* The introduced hyperfitting phenomenon is interesting, and there may be some potential application scenarios.
* There are abundant analytic experiments in this paper to support the widespread existence of the hyperfitting phenomenon in LLMs, as well as demonstrating the side effects of hyperfitting.

### Weaknesses
The main weakness of this paper lies in its weak contribution. Though the introduced hyperfitting phenomenon is attractive, this paper failed to convey crucial conclusions concerned by readers. Neither did this paper reveal the key reason why such phenonmenon exists and how it works, nor did it validate its advantages in practical downstream tasks. The experiments only answers how the hyperfitted model behaves, but did not answer why. I noticed there are some results for downstream tasks in Tab. 6, however, I found the results are even worse for hyperfitted models, and the experimental setup has its limitations (no comparison with other random decoding strategies, which are more practical in my point of view).

Either of the following suggestions can help for improving this paper:
1. Explore the key reasons why hyperfitting works for eliminating the repetition problem, as well as why hyperfitting results in sharped predictions.
2. Demonstrate the advantages of the hyperfitting technique under a variety of realistic downstream tasks, and compare with non-greedy decoding strategies.

### Questions
1. There seems to be a contradiction between line284 "never appear in the hyperfitting dataset" and line301 "neither occur in the training data", which is right?
2. Is the finetuning dataset a subset of the training datasets?
3. What if one apply random decoding with hyperfitted model? Will the generation results be similar to greedy decoding (because of low entropy)?

### Soundness
3

### Presentation
3

### Contribution
2
