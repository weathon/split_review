# Can LLMs Really Learn to Translate a Low-Resource Language from One Grammar Book?

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Extremely low-resource (XLR) languages lack substantial corpora for training NLP models, motivating the use of all available resources such as dictionaries and grammar books.
Machine Translation from One Book~\citep{Tanzer24-BenchmarkLearningTranslatea} suggests prompting long-context LLMs with one grammar book enables English--Kalamang translation, an unseen XLR language---a noteworthy case of linguistic knowledge helping an NLP task.
We investigate whether the book's grammatical explanations or its parallel examples are most effective for learning XLR translation, finding almost all improvement stems from the parallel examples.
Further, we find similar results for Nepali, a seen low-resource language, and achieve performance comparable to an LLM with a grammar book by simply fine-tuning an encoder-decoder translation model. We then investigate \textit{where} grammar books help by testing two linguistic tasks, grammaticality judgment and gloss prediction, and we explore what \textit{kind} of grammatical knowledge helps by introducing a typological feature prompt that achieves leading results on these more relevant tasks. We thus emphasise the importance of task-appropriate data for XLR languages: parallel examples for translation, and grammatical data for linguistic tasks.
As we find no evidence that long-context LLMs can make effective use of grammatical explanations for XLR translation, we suggest data collection for multilingual XLR tasks such as translation is best focused on parallel data over linguistic description.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The study presents a very thorough revision of the claim that prompting LLMs with grammar books of an unseen language enables the model to translate from/into that language. The main claim is that actually the translation examples in grammar books are the key support of handling the language, while grammatical explanations do not bring any improvement. For that purpose the work uses grammatical books for Kalamang and Nepali and presents contrastive experiments with several language models (Gemini, Llama 3.1, other more specific models), covering prompting, fine-tuning and LoRA. Besides splitting the grammar books into parallel examples and everything else the authors also include a list of words and other supplementary material. In addition to the task of translating, the grammatically judgement is also included, where grammatical descriptions are useful unlike with translation.

Although the study is narrowly targeted, it presents very clearly and exhaustively verified conclusions on the capability of LLMs, showing once again that their behavior is more akin to elaborate pattern matching, rather than comprehension and thinking.

### Strengths
* wide coverage of materials, models and approaches
* presented clearly (except for the complexity of results in Table 2) and convincingly

### Weaknesses
 * minor weakness: there are so many different models and comparisons that Table 2 is hard to understand, the reader has to go back and forth between the table and section 4.1 to remind, what the abbreviations mean -- perhaps there is a way to improve the readability?

### Questions
* would you expect different conclusions if the prompted / tuned LMs were much smaller?, what about larger models?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper evaluated whether LLMs can translate extremely low-resource languages using a grammar book. The findings reveal that parallel sentence examples are crucial for translation, while grammatical explanations offer little benefit. Tests on English-Kalamang and Nepali confirm that translation quality improves with parallel data rather than grammatical descriptions. For linguistic tasks like grammaticality judgment, a typological feature prompt is more helpful. The authors recommend focusing on parallel data collection over grammar descriptions for effective translation in low-resource languages.

### Strengths
1.  The paper showed a novel study that whether grammar books alone support translation for extremely low-resource (XLR) languages or not. By isolating grammar book components (e.g. parallel sentences vs. grammatical explanations), they illustrated a comprehensive evaluation, complemented by introducing typological prompts for linguistic tasks, a creative addition for XLR NLP.

2. By the controlled experiments across different closed-source (Gemini), open-source LLMs (Llama 3.2 8b), and NLLB NMT model, They found out that LLMs can't effectively learn from grammatical explanations for XLR MT in Kalamang and Nepali, relying instead on the parallel sentences. Also, We showed that fine-tuning NLLB model matches the performance of LLMs with long context. Additionally, LLMs can utilize grammatical information effectively when applied to suitable tasks, e.g. grammaticality judgment or IGT prediction, especially when enhanced with targeted grammatical data like our typological prompt, which achieves top performance on these linguistic tasks.

3. The paper is well-written, coherent with comprehensive analysis.

### Weaknesses
1. While the paper effectively examines the Kalamang and Nepali languages, its findings may not generalize across the diversity of low-resource languages. XLR languages can vary significantly in structure, script, and available resources, and focusing only on these two could limit the applicability of the conclusions. It would be nice to do similar analysis on low-resource languages too.

2. The paper introduces typological prompts as a promising way to improve linguistic tasks but does not compare this approach against other techniques that incorporate linguistic typology (e.g., embeddings based on typological features from databases like [WALS](https://arxiv.org/abs/2010.03920))

### Questions
Please refer to the weaknesses.

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
4

### Summary
This paper examines the contribution of a grammar book to building a machine translation system for an extremely low-resource language, Kalamang, that LLMs cannot have seen in training. In Kalamang, there is also parallel sentences and a dictionary. The authors evaluate LLMs by placing different mixtures of these language resources into a long context and evaluate the model's ability for in-context learning with the goal of translating test samples to and from English. They find that the additional grammatical explanations contribute little, if anything, on top of the parallel sentences, which themselves help the LLM learn to translate Kalamang. They similarly find that for Nepali, a much higher-resource language (but still low) where models have likely seen some text for, parallel sentences contribute to improving MT but not the grammar book. They also show this when finetuning NLLB, a translation-specific model, and show that grammar is also token inefficient in ICL in comparison to parallel sentences.

### Strengths
1. The paper is very well organized and is very clear to follow
2. The paper properly investigates a research question, with few, if any, holes in their experimental design as far as I can find
3. The presentation of the experiments and results are clear and the findings align logically with the numerical results
4. The authors incorporate novel methods (as well as new datasets) to understand the importance of grammatical explanations for low-resource MT

### Weaknesses
1. In general, the biggest weakness of the paper is the significance of its findings:

a. It is already established that parallel data, the most directly related samples to the MT task, are the most effective to training MT models. In many languages, parallel data is in fact the only form of labeled data that exists. For Nepali and Guarani, for example, it feels obvious that a grammar book would not help given that Gemini and Llama have likely implicitly seen many Nepali and Guarani texts in pretraining (or other highly related Indo-Aryan languages with similar grammar).

b. I understand that, by nature of targeting extremely low-resource languages, there are very few available data sources for such an experiment. But generalizing these results past Kalamang seems questionable, especially given that there is a singular grammar book, presumably written by a very small number of people. If possible, this paper would be strengthened by a few more languages (more similar in task than Nepali). I would also suggest more context on grammar books themselves be provided and how frequent these are for extremely low-resource languages.

c. Title is a bit misleading in that it asks whether using grammar books are useful, all to prove that not really. The title moreso implies that the paper would show that grammar books are useful.

2. In comparison to ACL venues, ICLR attendees will typically have less linguistics background. I am concerned the discussion of more specific linguistics topics (e.g. interlinear gloss text, grammar & typology) might be not well suited for this audience. I will leave that to the AC to discern, but also advise authors modify the Related Work & Methodology section to take that into account.

### Questions
1. Line 44: how does the quantity of data available make Kalamang not unique ? I would better explain why the findings on Kalamang are relevant to many other languages
2. I would discuss the fact that you are using in-context learning (ICL) more clearly in the intro or even abstract
3. I would add more references to explain/justify the methodology in 3.3 and 3.5
4. Line 215: parallel data annotation is typically very rigorous; annotators have to follow specific instructions or for scraping, sentence alignment has to be in a particular way or else the sample is thrown out. How clean & consistent are the parallel samples that come from your heuristic filter ? How did you determine what was appropriately parallel examples vs an explanation when no Kalamang speakers were involved in the project ? I would add more details about this heuristic filtering process.
5. Notation for tables is confusing and takes a while to digest. It might be worth including quick natural language names like instead of Book_p, putting "Grammar Book, parallel subset"
6. Table2: how is Gemini able to do 11&13 ChrF when it has never seen Kalamang before ?

### Soundness
4

### Presentation
4

### Contribution
2
