# Generalization v.s. Memorization: Tracing Language Models’ Capabilities Back to Pretraining Data

- Decision: Accept
- Avg Score: 5.00
- Scores: 3, 8, 6, 3

## Abstract
The impressive capabilities of large language models (LLMs) have sparked debate over whether these models genuinely generalize to unseen tasks or predominantly rely on memorizing vast amounts of pretraining data. To explore this issue, we introduce an extended concept of memorization, \textbf{distributional memorization}, which measures the correlation between the LLM output probabilities and the pretraining data frequency. To effectively capture task-specific pretraining data frequency, we propose a novel \textbf{task-gram language model}, which is built by counting the co-occurrence of semantically related $n$-gram pairs from task inputs and outputs in the pretraining corpus. Using the Pythia models trained on the Pile dataset, we evaluate four distinct tasks: machine translation, factual question answering, world knowledge understanding, and math reasoning. Our findings reveal varying levels of memorization, with the strongest effect observed in factual question answering. Furthermore, while model performance improves across all tasks as LLM size increases, only factual question answering shows an increase in memorization, whereas machine translation and reasoning tasks exhibit greater generalization, producing more novel outputs. This study demonstrates that memorization plays a larger role in simpler, knowledge-intensive tasks, while generalization is the key for harder, reasoning-based tasks, providing a scalable method for analyzing large pretraining corpora in greater depth.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a "task-gram language model," built on n-gram co-occurrences, to trace task-specific data in pretraining corpora. Through experiments on translation, question answering, and reasoning tasks using Pythia models, the paper finds that memorization is predominant in simpler, fact-based tasks like factual question answering, while generalization is more critical for complex tasks requiring reasoning.

### Strengths
- The proposed task-gram model offers an alternative approach to evaluating LLM behavior by connecting output distributions directly with pretraining data.
- Experimental results reveal several interesting findings like how model size influences memorization versus generalization, showing that larger models tend to generalize more in complex tasks, an insight useful for understanding scaling effects.

### Weaknesses
 - The task-gram model can be insufficient in capturing the complexity of today's generative tasks with short input descriptions. These tasks often demand high levels of abstraction and creativity from the LLMs to infer extensive information from minimal data, a process that cannot be well represented through n-gram frequency metrics. I recommend evaluating on more complex tasks like code generation (e.g., HumanEval) and math reasoning (e.g., GSM8K).
- Using Spearman correlation between task-gram and LLM probabilities may conflate memorization with necessary task handling where n-gram overlap is essential. For example, high correlation in translation could reflect accurate language pairing rather than mere memorization. This might misinterpret critical task-related patterns as memorization.
- Overall, the findings indicate that different tasks exhibit varying levels of dependence on memorization, which is not novel or surprising, as already discussed in previous works like [1].
- Several methodological and experimental designs need clarification. See questions for details.

### Questions
1. In Figure 2, how are n-gram occurrences counted when a sentence contains multiple task-related n-grams? Specifically, are overlapping n-grams counted individually or merged, and how does this approach impact the interpretation of memorization levels in longer and more complex sentences?
2. For generative tasks with very short input descriptions, is this approach still applicable, and how does it handle sparse n-gram distributions?
3. How does the methodology account for task-related patterns that are critical for accuracy rather than memorization, such as translation?
4. The study shows that in knowledge-intensive MMLU tasks, memorization decreases as model size increases. Could this decrease be due to specific limitations in capturing rarer knowledge from larger models, or might it indicate a shift toward more generalized, inferential capabilities?
5. Appendix E states that alternative methods (e.g., NER models) for identifying n-gram pairs yielded inconsistent results. Could you elaborate more about your implementation and the results?
6. The experiment uses different cosine similarity thresholds across tasks (WMT v.s. TriviaQA and MMLU). How did you select these hyperparameters, and how sensitive are the results to these thresholds?
7. Some tasks might share similar patterns or data structures (e.g., QA and factual retrieval), could memorization from one task inadvertently support generalization in another? Does the study address potential cross-task memorization effects, especially for overlapping or semantically similar tasks in the training data? The task-specific n-gram approach may suffice to take these cross-task effects into account. 
8. Beyond the analysis and findings, can you propose a potential method for actively adjusting the balance between memorization and generalization within models to improve performance across tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper adds a thorough analysis of memorization vs generalization capability of LLMs taking into account the pretraining data. Using the Pythia model family and the Pile dataset, the paper proposes a task-based n-gram language model, which is built on downstream tasks, by extracting semantically related n-grams. This n-gram model is then used to compute correlation among seen/novel n-grams with the LLM output perplexity, to come up with a notion of distributional generalization. More correlated these metrics are (task n-gram vs LLM), the bigger the amount of memorization and vice-versa. The key contribution of the paper is this methodological approach, using which they show clear memorization and generalization aspect based on different downstream tasks.

### Strengths
- The paper is exceptionally well written - I found it very enjoyable to read it end to end. 
- The methodological contribution is strong and makes sense to compute correlation between task specific n-grams and LLM perplexity. This method can likely be extended to multiple different tasks easily, with the caveat of the availability of the pretraining data distribution.
- While memorization vs generalization debate has a long list of papers in the literature, this paper makes an important contribution by computing the statistics _at scale_ by considering full pretraining data distributions.
- The contributions builds upon relevant literature ($\infty$ gram and WIMBD).
- Good choice of downstream tasks tested, ranging from translation, to factual to math.

### Weaknesses
 - Perhaps some more downstream datasets could have been considered apart from MMLU, as it is known the dataset contains several annotation issues [1]. Specifically, the reliance on MMLU introduces a potential bias, given its known issues with annotation quality and the possibility that models might exploit these flaws rather than demonstrating genuine generalization. The argument of MMLU requires more reasoning than generalization due to math is also not completely answerable. It would be interesting to dive into that question using GSM8k, given recent results point more to memorization issues [2]. The current analysis does not fully disentangle whether the observed performance on MMLU is due to genuine reasoning or memorization of specific patterns within the dataset.
- Not much of a weakness per se, but a limitation (which the authors duly acknowledge) that the results are conditional on the Pile dataset. This limits the generalizability of the findings, as the observed memorization and generalization patterns might be specific to the characteristics of the Pile dataset. It would be beneficial to see if similar trends hold for models trained on different pretraining corpora, which could reveal whether the observed phenomena are universal or dataset-specific.

### Questions
- In the definition of task-gram language model, what happens when the corresponding n-gram of the denominator is rare or absent? I assume you filtered them out from the computation, but wondering what is the % of n-grams you had to drop per dataset.
- How does your setup account for the synonyms of the n-grams? This is probably going to be more of an issue for smaller datasets such as MMLU, and can likely be a confound to the results?
- In your opinion, does the varying amount of samples in test datasets pose as a confound? Since MMLU is the smallest dataset, perhaps one experiment could be done by taking bootstraps from WMT and TriviaQA in the same sample sizes?
- Not sure I follow the reasoning behind using *both* $\infty$-gram and WIMBD. Wouldn't this add a bias? Curious how plots change by using only one or the other.
- For TriviaQA results, any insight on why does $\infty$-gram reduces with scale? 
- Here is a hypothetical scenario: suppose if you add the task data progressively into the LLM training (by finetuning), then the task-n-gram probability can be controlled from 0 to max smoothly. Since this is finetuning, the model will be more incentivized to memorize the data aggressively. What kind of distributional generalization curves you would expect to see?


## Suggestions

- From a cursory glance i missed that Figure 3 scales of MMLU knowledge and reasoning are different, which is important to highlight in my opinion. I understand making a single axes removes the ability to show the trend (stuff will be a straight line), but if there is a way to visually highlight the range of scales it would be great.
- Section 2 can have a small plot showing the expected trend of memorization vs generalization, to ground the readers how to interpret the later plots.
- Typo: L499 - ~pertaining~ -> pretraining

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a framework for measuring the correlation between the outputs of an LLM and n-grams present in its training data.

To that purpose, they first propose a task-gram language model, which approximates the distribution of task-related data in the model's training data. They then define the distributional memorization metric (and its complementary metric, the distributional generalization) as the correlation between the probabilities of the task-gram language model and the probabilities predicted by the LLM on test data.

In the second part, the authors measure the distributional memorization/generalization of a series of LLMs of increasing size on three different tasks requiring increasing generalization capabilities. They show that the model's performance increases with the number of task-related n-grams found in the pretraining data, and that knowledge-intensive tasks rely on memorization, while reasoning-intensive tasks rely on generalization. The authors cross-check their findings by using a gradient-based method to measure the influence of training n-grams in the model outputs, which yields results that are consistent with the previous findings.

### Strengths
The paper focuses on the important question of the generalization-memorization tradeoff and proposes a concrete and clearly defined metric to measure it on a given LLM, which is valuable for future research.

The author's work is well-written and structured, clear, and easy to read. The experimental methodology is sound, with some possible flaws and limitations described in the appendix.

I appreciate the fact that the authors confirmed their findings using the gradient-based method and that they checked for possible cross-contamination of the training dataset.

### Weaknesses
My main concern regarding this work is that the distributional memorization/generalization metrics depend on a large number of hyperparameters (choice of dataset and embedding model, cosine similarity thresholds), but although the authors justify some of the choices they made regarding those, they do not measure how sensitive the metrics are to the value of those parameters. While I understand that the proposed method is computationally expensive, I believe that this needs to be addressed to assess the relevancy and usefulness of the proposed metric and strengthen the author's claims. In addition, some choices are unclear. For example, different values are picked for the 5-gram threshold choices for WMT compared to the other datasets, but this is not justified.

A smaller point of criticism is that the authors define distributional generalization as the divergence between the distribution of the LLM’s output and that of the pretraining data. While necessary, this criterion is insufficient: for example, smaller LLMs tend to fall into degenerate/repetitive distributions which do not conform to natural language syntax, and would therefore obtain a high generalization score. Performing fluency measurements or qualitative discussion of the results would help with this aspect.

An editing mistake seems to appear in the paper in Def. 3 : "we define the extent of an LLM distributional memorize the pretraining corpus".

### Questions
- Appendix: The example n-grams in Figure 5 appear to contain stop words, while those in Figures 6-8 do not. Could the authors clarify whether stop word removal was performed when mining n-gram pairs? Since this seems to be the most computationally expensive part of this work, limiting the number of obtained pairs may help with scaling. More generally, my intuition is that systematic enumeration of all n-gram pairs is probably superfluous. Have the authors considered performing NER-based filtering post-mining?

- In Figure 2, the smaller models are depicted to obtain a ~10% accuracy on MMLU, which is below random chance, when the number of N-grams in the training set is 150. Do the authors have any qualitative insight on why this may be happening?

- The Pile was checked for potential overlaps with the training datasets using exact n-gram matches with n > 14. As this value is quite large, especially if stopwords were removed, could the authors explain why this particular value was chosen?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper explores the debate between generalization and memorization in LLMs. It assesses how model outputs correlate with pretraining data frequencies, and proposes a task-gram language model to capture task-specific data distributions.

### Strengths
The paper provides a thorough investigation of the interplay between memorization and generalization in LLMs. Evaluates models on a range of tasks (translation, factual QA, reasoning), providing insights into how different tasks influence memorization and generalization.

### Weaknesses
1. This paper, published at the ICML 2024 Workshop on Foundation Models in the Wild, does not present significant new insights or findings. The contributions appear incremental and may not substantially advance the current understanding in the field.

2.  The conclusion that "factual question answering shows an increase in memorization with increasing LLM size" is not novel. Prior research has extensively demonstrated factual knowledge are stored in the neurons of FFNs. The increasement of factual answering task is due to having more neurons in the lareger models.

[1] Knowledge Neurons in Pretrained Transformers

[2] Transformer Feed-Forward Layers Build Predictions by Promoting Concepts in the Vocabulary Space

[3] Do Localization Methods Actually Localize Memorized Data in LLMs?

[4] Locating and editing factual associations in GPT

[5] Calibrating factual knowledge in pretrained language models

3. Lack of practical implications. It is not clear about the practical implications of its findings for improving LLM training and deployment strategies.

4. Despite covering diverse tasks, the study heavily relies on specific datasets like The Pile and utilizes Pythia models. This reliance may limit the generalizability of the findings to other datasets and model architectures.

5. The paper uses the MMLU benchmark to assess reasoning capabilities. However, MMLU is designed to evaluate a model's understanding ability across 57 subjects, including elementary mathematics, history, computer science, and law, and can not effectively reflect reasoning ability. For demonstrating reasoning skills, datasets like MGSM would be more appropriate.

6. The use of WMT-09 raises concerns due to its age and the potential for data contamination, where overlap between training and test data might exist. It is advisable to use more recent datasets, such as WMT23 or WMT24, to avoid these issues and ensure that the evaluation reflects the model's true capabilities.

7. Relying solely on Spearman correlation as a primary metric may not fully capture the nuances of memorization and generalization in language models. The paper should include additional experiments or provide mathematical justification to demonstrate why Spearman correlation is an appropriate and sufficient metric for measuring these aspects.

### Questions
see weakness.

### Soundness
2

### Presentation
2

### Contribution
2
