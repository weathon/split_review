# When Is Multilinguality a Curse? Language Modeling for 252 High- and Low-Resource Languages

- Decision: Reject
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Multilingual language models are widely used to extend NLP systems to low-resource languages.
However, concrete evidence for the effects of multilinguality on language modeling performance in individual languages remains scarce.
Here, we pre-train over 10,000 monolingual and multilingual language models for over 250 languages, including multiple language families that are under-studied in NLP.
We assess how language modeling performance in each language varies as a function of (1) monolingual dataset size, (2) added multilingual dataset size, (3) linguistic similarity of the added languages, and (4) model size (up to 45M parameters).
We find that in moderation, adding multilingual data improves low-resource language modeling performance, similar to increasing low-resource dataset sizes by up to 33\%.
Improvements depend on the syntactic similarity of the added multilingual data, with marginal additional effects of vocabulary overlap.
However, high-resource languages consistently perform worse in multilingual pre-training scenarios.
As dataset sizes increase, adding multilingual data begins to hurt performance for both low-resource and high-resource languages, likely due to limited model capacity (the ``curse of multilinguality'').
These results suggest that massively multilingual pre-training may not be optimal for any languages involved, but that more targeted models can significantly improve performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the effects of multilinguality in language model training. The authors take 250 languages, each with varying amounts of textual data, and train GPT2-style models in three sizes. For each, they study the effects of injecting multilingual data (of either related or unrelated languages) in various amounts. The findings are that, for low-resource languages, adding moderate amounts of multilingual data can aid target language performance, as long as model capacity is sufficient. Whereas for high-resource languages, multilingual training is consistently hurtful in the settings evaluated by the authors.

### Strengths
* An in-depth study of the effects of multilingual pretraining for small-ish language models. Ablation studies are solid, covering resource level, varying the amount of multilingual data that's injected, similar/dissimilar languages, the effects of syntactic/lexical/geographic similarity, and model size.
* Overall, this paper sheds light on the degree to which cross-lingual transfer can help. There is already evidence coming from the field of machine translation showing that high-resource language performance suffers in multilingual settings (e.g. by comparing the performance of languages such as English or Mandarin in massively multilingual MT models such as NLLB, arXiv:2207.04672, vs equivalent bilingual models). The authors of this paper take this a step further by providing a comprehensive evaluation across many languages and model sizes.
* The carefully chosen tokenization approach (section 5) and evaluation metric (section 4.3) allow for intuitive comparison of monolingual and multilingual models.

### Weaknesses
 * The model sizes are all on the small end. One can see from e.g. Figs. 3 and 5 that, as model size increases, multilingual pretraining hurts performance less and less (and actually becomes beneficial, in a few cases). The obvious next step would then be to grow model size further. While the authors do acknowledge this limitation, the fact that the observed benefits of multilingual pretraining seem to be highly dependent on model capacity makes it a significant concern, as the conclusions drawn from these smaller models may not generalize to larger, more practically relevant models. This limitation is particularly relevant given that the field is rapidly moving towards ever-larger models, and the trends observed here might not hold true in that regime.


### Questions
Do you expect these results to hold also for related tasks such as machine translation, speech recognition, etc.? Based on the current SOTA models for these related tasks, would you agree that the story is likely to be similar there too?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper trains up a huge number of monolingual and multilingual language models to study the effect of multilingual pretraining on language modelling performance. They covered over 250 languages and systematically vary monolingual dataset size, multilingual dataset size, linguistic similarity and model size. Their conclusions were already common knowledge. They show that adding multilingual training data improves low-resource language performance. They show that multilingual training hurts high-resource languages. They show that language similarity matters, more similar being better of course. Possibly more novel is that they show that for language similarity syntactic similarity matters - which is unexpected. But by syntactic similarity they mean the syntactic component of lang2vec which is taken from the WALS typological database so these are syntactic features collected by linguists not syntactic trees over the language. 

Overall the paper was very ambitious with the scale of the experiments (trained over 10000 language models - even if they were all very small up to 45M paramteres).  The problem was that I didn't learn much.

### Strengths
Thorough explorations of the experimental conditions
They come up with a way of measuring model performance which is comparable across the different languages: estimated model tokens measure.

### Weaknesses
Unsurprising results
The models themselves were all very small - up to 45M parameters. It is not clear if these conclusions still hold for larger models as LLMs tend to be in billions of parameters and scale has been shown to be crucial for various important abilities like zero-shot and in-context learning. The use of WALS typological features as a proxy for syntactic similarity is also a potential weakness. While WALS provides a broad coverage of languages, the features are high-level and may not capture the nuances of syntactic structures that are relevant for language model performance. The fact that the syntactic features are manually curated by linguists, rather than derived from actual syntactic trees, raises questions about their granularity and applicability to the specific task of language modeling. Furthermore, the relatively small impact of selecting most vs least related languages, as measured by their similarity metric, suggests that the chosen similarity metric may not be the most appropriate one for this task or that the effect sizes are simply small.

### Questions
Why do you think that selecting most related vs least related had relatively little impact?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper evaluates the impact of multilingual pre-training on language modeling performance across 250 languages, both high-resource and low-resource. The authors find that while adding multilingual data to the training dataset can improve performance for low-resource languages, it can also hurt performance for high-resource languages. They also find that the benefits of multilingual pre-training depend on the syntactic similarity of the added languages, with marginal additional effects of vocabulary overlap. Based on the obtained results, the authors suggest that massively multilingual pre-training may not be beneficial for any languages involved, but that more targeted models can significantly improve performance.

### Strengths
1. Pre-train a massive number (over 10000) of monolingual and multilingual language models for over 250 low-resource and high-resource languages to provide concrete evidence for the effects of multilinguality on language modeling performance in individual languages.

2. Through the carried out experiments, this work clarifies the already-known effects of multilingual pre-training on low-resource and high-resource languages. For example, it shows that adding multilingual data improves low-resource language modeling performance, similar to increasing low-resource dataset sizes by up to 33% while the high-resource performance degradations when adding multilingual data can be similar to reducing high-resource dataset sizes by over 85%. And that the improvements depend on syntactic and lexical similarities of the added multilingual data.

### Weaknesses
1. I found it a strong (unsupported/contradicting) claim when the authors argue that "the multilingual pre-training may not be beneficial to any languages involved". Because the obtained results already show that low-resource languages clearly benefit from multilinguality and that the high-resource performance degradation reduces as the model size increases. Providing supportive arguments regarding this claim might be useful.

2. While the authors carried out a dramatic number of experiments, they do not provide detailed reasons why such a huge amount of computing resources would be needed. I assume selecting a set of languages that represent specific scenarios would be enough to get supportive results. And that could help in securing some resources that could be used to evaluate relatively larger language models which could have probably given a different picture of the results.

3. The performance of most LLMs is often assessed through downstream task performance since the pre-training loss cannot always fully explain downstream performance (https://proceedings.mlr.press/v202/liu23ao.html). I am wondering why the evaluation of LLMs on downstream tasks was not included.

4. In the first line of page 6, it was mentioned that a total of 8454 multilingual language models were pre-trained while in the abstract it was mentioned that over 10000 models were trained. Is that a typo?

**Minor:**
Possible formatting issue: in the current ICLR paper format, the titles of the table should be at the top of it instead of the bottom.

### Questions
Please, check the weakness section.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an extensive of controlled experiments to figure out how language performance in each language is related to (1) the size of monolingual data, (2) the added multilingual dataset size, (3) linguistic similarity of the added languages, and (4) model size. The authors pretrained more than 10,000 models over 250 languages under different settings. The authors drew various conclusions according to their experiments and showed that massively multilingual pretraining may only be beneficial for some languages, while more targeted models, e.g., monolingual models, may perform much better.

### Strengths
- The paper is highly motivated and is generally easy to follow.
- The authors conducted extensive and controlled experiments.
- The results are interesting and may shed light on the massively multilingual pretraining.

### Weaknesses
 - The major weakness of the paper is that the size of all models is very small, and therefore some of the findings might not be transferred to larger models. In the experiments, the authors also show that when the model is larger, the degradation is mitigated compared with smaller models. However, it is UNREASONABLE to train many models that have the same size as, e.g., XLM-R. Therefore this is only a concern but not a suggestion to do more experiments.

- I found some parts of the papers are a bit repetitive. For example, the first and the second paragraphs in the introduction section have extensive similar claims. The authors should improve the flow of writing to reduce such redundancy.

### Questions
- In the paragraph "Multilingual tokenizers", the author mentioned that the target language and the added multilingual datasets are tokenized separately. And the size for multilingual vocab is set to 32K tokens, which is the same as the monolingual tokenizer. Is this a limitation since 32K tokens might not be enough to support ten languages (especially when the scripts of the ten languages are different)?

- In the very interesting part of "Syntactic similarity of added languages drives results", the authors mentioned that abstract linguistic similarity might be more beneficial than surface-level similarity. I was wondering how conceptual similarity [1] would hold in this case. Could the authors give any thought to this?

- The authors mentioned that the degradation is even slightly larger when the added languages are "similar" to the target languages. This sounds a bit counter-intuitive. Could the authors give some possible explanations?

[1] https://arxiv.org/pdf/2305.08475.pdf

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
