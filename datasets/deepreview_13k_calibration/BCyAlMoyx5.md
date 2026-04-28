# Crosslingual Capabilities and Knowledge Barriers in Multilingual Large Language Models

- Decision: Reject
- Avg Score: 5.67
- Scores: 8, 6, 3

## Abstract
Large language models (LLMs) are typically \emph{multilingual} due to pretraining on diverse multilingual corpora. But can these models relate corresponding concepts across languages, effectively being \emph{crosslingual}? This study evaluates six state-of-the-art LLMs on inherently crosslingual tasks. We observe that while these models show promising surface-level crosslingual abilities on machine translation and embedding space analyses, they struggle with deeper crosslingual knowledge transfer, revealing a {\em crosslingual knowledge barrier} in both general (MMLU benchmark) and domain-specific (Harry Potter quiz) contexts. We observe 
that simple inference-time mitigation methods offer only limited improvement. On the other hand, we propose fine-tuning of LLMs on mixed-language data, which effectively reduces these gaps, even when using out-of-domain datasets like WikiText. Our findings suggest the need for explicit optimization to unlock the full crosslingual potential of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates how multilingual LLMs perform for actual cross-lingual tasks. This covers a wide range of tasks including machine translation but also several variations of multilingual tasks where different parts of the input (text, multiple choice options, questions) are translated into different languages. The authors show a consistent drop in performance when considering actual mixed language tasks and suggest simple fine-tuning strategies to remedy this drop.

### Strengths
- well written paper
- interesting outcomes. Not entirely surprising but still nice to see.
- solid methodological evaluation (but see my comment regarding choice of language below)

### Weaknesses
 - the languages considered are rather few and still relatively similar to each other: 2 germanic languages (English and German) and three romance languages (French, Italian, Spanish). In addition all languages are most likely very high resource (albeit not as high as English of course) during training of the different models. It would have been good to see languages that are rather different from the rest (Arabic or Chinese) maybe even low-resource (Bengali or Amharic).

 - while multilingual have been used it would have been interesting to also consider models that do explicitly use cross-lingual supervision during training such as ALMA or Tower.

### Questions
In Footnote 1 you say "This criterion allows the case when a small amount of parallel texts accidentally crawled from the web are mixed in the pretraining dataset, as it is nearly impossible to verify. We believe such presence, if it exists at all, would have negligible impact on the model given the size of the rest of the pretraining data."

A) How do you know that GPT 3.5 and 4 don't use parallel data explicitly during training?

B) While the parallel data might be small in comparison to the rest of the data, does that really mean it has a negligible impact on the model, considering the vast amount of parameters that could allow for quite a high degree of memorisation? Can you substantiate your claim a bit better (references or otherwise)?

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
Authors study multilingual abilities and extent of crosslingual transfer of decoder transformer language models, using three different methodologies: embedding-based, MMLU based and domain-specific. In embedding part authors collect embeddings of sentences in English, sentences, in which some of the input tokens were corrupted by masking the attention or randomly replacing them with different tokens from vocabulary of the model and sentences, in which words were randomly translated into a different language and calculate distances between English, corrupted and partially translated languages. General knowledge based evaluation is conducted by translating parts of the questions or answers from MMLU dataset into a different language. In domain-specific evaluation authors ask questions about Harry Potter series and apply same translation techniques as in general knowledge evaluation. First evaluation show that models have close embeddings after per token translations. Second evaluation shows that models are doing much worse on MMLU after partial translations of the answers. Third evaluation shows that applying translation to parts of the questions or answers from Harry Potter trivia the crosslingual barrier still exists. In later parts of the paper authors test different methodologies of overcoming this barrier, either by prompt engineering and doing few-shot prompting which has limited success and by finetuning selected models on WikiText-2 for general text knowledge and WikiText-103 for domain specific trivia, which improves the performance on both MMLU and HP-Quiz.

### Strengths
1. Experiments with embeddings of the models are interesting and give some insight into how models encode meaning of partially translated sentences.

2. Experiments with general purpose knowledge can be used to better understand multilingual capabilities of trained models. 

3. Mixup-version of MMLU, when provided, will be useful to do better multilingual evaluations, since the language perturbations can successfully combat the test leakage.

4. The text is clear and understandable.

### Weaknesses
1. Models, selected on line 100, are not multilingual. Llama-3-8B was explicitly stated as a monolingual model, focusing only on English, with usage in other languages described as out-of-scope use. Multilinguality was only stated in 3.1’s model card. Same can be said about Llama-2-7B and Llama-2-13B. Mistral-7B is not explicitly stated to be multilingual, either. Given both multilingual evaluations and community reports, it is safe to say that these models do not exhibit strong multilingual capabilities. Authors additionally evaluate Mixtral 8x7B and Aya-23-8b, which are explicitly stated to be multilingual models and have some knowledge in selected languages (en, fr, de, es, it), but they are mostly ignored in the main part of paper, instead focusing on Llama-2 and Llama-3. To my mind this is a big misstep, since bad performance of the selected models could be incorrectly generalized to truly multilingual models.

2. Domain specific evaluations are being done on the Harry Potter series of books, which was translated to different languages with varying quality. This raises the question of how well the terms described in the books are translated: for instance, tha name of Neville Longbottom is translated to Italian as Neville Paciock, which retains the connotation of clumsiness, but does not sound similarly and does not preserve the meaning of long bottom with the English version, to Chinese as Nàwēi Lóngbādùn, which does not retain the connotation since it’s a simple transliteration and to Russian as Nevil Dolgopups, which both does not retain the clumsiness connotation, meaning or common sound/tokens. This raises concerns if the arguments presented in the paper (e.g. knowledge learned in one language can be translated to other languages) can be checked via Harry Potter trivia.

3. All of the selected models almost certainly have seen the original books, dumps from HP Wiki or Wikipedia and blog posts about Harry Potter in non-English languages, so it may have leaked into the training data for all of the languages. The inability to measure the extent of this data leakage makes it unclear whether the observed performance in different languages is due to genuine crosslingual transfer or simply a result of English data leakage during pretraining, significantly impacting the interpretability of the results.

4. It is common knowledge that both instruction and preference tuning causes catastrophic forgetting, which leads to models being better at instruction following, safety and answer formatting, but worse at parametric knowledge. From the list of the described models we can see that only Llama-2, Llama-3, Mixtral-8x7b, Zamba-7b and Mistral-7b models are available as base models, with GPT-3.5, GPT-4, Aya-23 being instruction tuned models. It is not explicitly stated, which versions of the models are used – pretrained or finetuned, Thus, some clarification is required, since it directly influences the amount of multilingual capability of the models. If these are instruction tuned models, further finetune of them on Harry Potter dataset could lead to catastrophic forgetting, thus perturbating the models’ scores and if these are base models, direct comparison between Aya-23 and llamas, for instance, presents a potential inconsistency in methodology.

5. The phenomenon of crosslingual knowledge barrier (e.g. limited multilinguality capabilities of the model) is well known, so the main contribution of the paper lacks originality.

### Questions
1. It would be very beneficial if the authors of the paper would use different languages, such as Chinese, Hebrew, Russian or Hindi, since these languages have a much lower amount of shared tokens with English, which is selected as the most highly resourced language in the training mix of all selected models. This would give us insight into how the applied methodology translates into languages, which the model has a harder time training due to lesser overlap between dictionaries.

2. Please, repeat your evaluations using a different set of models, such as Mistral-Nemo-12B, Qwen-2.5-7B, Command-R and LLaMA-3.1-8B which are multilingual by design. Claims of multilinguality of these models are supported by extensive multilingual evaluations both by model authors and community members.

3. Perhaps designing another evaluation dataset for domain specific knowledge, based on something like some local company guidelines or university campus rules and translating it into different languages would make a much stronger point to support the claims, since it would not exhibit translation artifacts.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper claims to investigate the cross-lingual knowledge barrier for four high-resource non-English languages by examining benchmark score variability under different translation scenarios for six LLMs. However, it suffers from several weaknesses, including:

- A lack of detail regarding how sentence embeddings are obtained to demonstrate explicit cross-lingual capabilities. And no justification for the chosen probability settings.
- Uncontrolled experiments that do not sufficiently prove that the results are due to the cross-lingual knowledge barrier rather than the performance of the languages in non-knowledge related tasks.

In the rest of the paper, the authors evaluate well-established methods to improve the multilinguality score. Their proposal to construct a fine-tuning dataset comprising examples from multiple languages, particularly at the sentence level, aims to achieve better scores compared to English fine-tuning. However, I believe this outcome is completely expected and does not represent a significant contribution.

### Strengths
- The paper demonstrates that a cross-lingual knowledge barrier exists for four non-English languages through experiments evaluating how much benchmark scores vary when the benchmarks are translated under different scenarios.

- The authors assess well-established methods to improve the multilinguality score and propose constructing a fine-tuning dataset that comprises examples from multiple languages, particularly at the sentence level, to achieve better scores in multilinguality.

### Weaknesses
 - L26-36: The first figure presents a poor example. Why couldn't it simply be the same question in both English and French? Additionally, why is there a need to create a knowledge that does not exist, so it can not be tested out as an example?

- L104: The authors state, “such presence, if it exists at all,” regarding parallel sentences on the web. It would be interesting to know how papers that mine billions of parallel texts from the web feel about this statement (e.g., https://arxiv.org/abs/1911.04944).

- L137: The paper mentions obtaining sentence embeddings from the LLM; however, it does not detail how this is done. Since these are decoder-only models with causal attention, how are the embeddings of the tokens aggregated? Is it the last token, or are they weighted? (see section 3.1 of https://arxiv.org/pdf/2410.05873 for a background on the different techniques)

- L134-142: There are many variables concerning probabilities, yet there is no explanation for why these specific values were chosen.

- L158-159: The statement “This underscores the explicit cross-lingual capabilities of multilingual LLMs” lacks clarity regarding the rationale and conclusions drawn. With a lower probability (0.16 vs. 0.8), tokens were randomly selected from the vocabulary. Now, the distribution of these two (cosine similarities between the original and mixed translated sentence embeddings versus the original and random token-replaced sentence embeddings) varies significantly. Many variables are involved here: do the random tokens from the vocabulary come only from all writing systems or just Latin? How are the embeddings computed, and why were these probabilities chosen? Although I acknowledge the existence of cross-lingual capabilities, I am not convinced by the authors' experiment.

- L199-200: There is no experiment/evaluation/audit demonstrating how valid these translations are.

- L247: Conclusion 1 does not necessarily indicate a knowledge transfer problem. In English-centric LLMs, it is expected that performance will be better in English. Simply stating that English performs better in an English-centric LLM does not imply that knowledge cannot be transferred; rather, it suggests that performance in the secondary language may be low, even in language understanding tasks. The authors selected languages where LLMs typically perform better (but is it on the level of English?), so it is not surprising that they cannot fully grasp the knowledge of English. If the authors had chosen low-resource languages, we might observe even lower performance, which could indicate that the LLM lacks substantial knowledge of those languages to begin with than other knowledges.

For the rest of the paper, the authors evaluate well-established methods to improve the multilinguality score. Their proposal to construct a fine-tuning dataset comprising examples from multiple languages, particularly at the sentence level and achieve better scores compared to English fine-tuning. However, I believe this outcome is completely expected and does not represent a significant contribution.

### Questions
See weaknesses part especially L137, L134-142, L158-159, L199-200.

### Soundness
2

### Presentation
2

### Contribution
1
