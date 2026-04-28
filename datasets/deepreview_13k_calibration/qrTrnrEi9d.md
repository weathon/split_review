# Translation and Fusion Improves Zero-shot Cross-lingual Information Extraction

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
\noindent
Large language models (LLMs) combined with instruction tuning have shown significant progress in information extraction (IE) tasks, exhibiting strong generalization capabilities to unseen datasets by following annotation guidelines.
However, their applicability to low-resource languages remains limited due to lack of both labeled data for fine-tuning, and unlabeled text for pre-training.
In this paper, we propose TransFusion, a framework in which models are fine-tuned to use English translations of low-resource language data, enabling more precise predictions through annotation fusion. 
Based on TransFusion, we introduce GoLLIE-TF, a cross-lingual instruction-tuned LLM for IE tasks, designed to close the performance gap between high and low-resource languages.
Our experiments across twelve multilingual IE datasets spanning 50 languages demonstrate that GoLLIE-TF achieves better zero-shot cross-lingual transfer over the base model.
In addition, we show that TransFusion significantly improves low-resource language named entity recognition when applied to proprietary models such as GPT-4 (+5 F1) with a prompting approach, or fine-tuning different language models including decoder-only (+14 F1) and encoder-only (+13 F1) architectures

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a simple yet effective approach for improving cross-lingual transfer with a focus on Information Extraction (IE) tasks such as NER, relation extraction, and slot filling. The idea is to leverage an external Machine Translation (MT) system such as NLLB (or any other similar MT system) to translate data from low-resource languages to English, and then leveraging the translation data as additional signal/context for making predictions. The second key ingredient of the approach is the idea of bypassing the alignment step for IE task, where the 'trick' is to first do annotations on the example translated to English before predicting annotations in the target language, where the former seems to be crucial to enable good performance, as verified by an ablation study. In general, this simple idea does provide benefits across a range of IE tasks and languages. Moreover, the authors show the usefulness of the approach on IE tasks with unseen annotation sets, and they show how a similar approach can be applied both to decoder-only models (which are in the main focus of the paper), but also to encoder-style models as well.

### Strengths
- A simple idea which is well motivated and well explained the paper, with a good coverage of IE datasets and languages, and good side analyses (e.g., ablation studies, error analyses).
- This idea can be easily combined even with API-gated models without fine-tuning for some quick wins on different IE tasks. Given its simplicity, the entry point to try out the model is quite low (which is a plus).
- The experimental work can be easily reproduced by other researchers.

### Weaknesses
 - I have concerns about the actual novelty of the work (as advertised in the paper). The use of external MT systems to create some 'silver data' as well as to help with cross-lingual transfer is definitely not a novel idea, and has been tried many times before. We do have many examples of work that explore translation-based cross-lingual transfer for low-resource languages, such as:
-- https://aclanthology.org/2023.emnlp-main.242
-- https://aclanthology.org/2024.naacl-long.298/
-- https://aclanthology.org/2023.emnlp-main.399
- In fact, some of the key baselines are missing from the paper (e.g., improved 'translate-test' baselines as in the aforementioned work)
- Also, it is not new to use external MT systems to enable multilingual instruction-tuning, here are just a small selection of papers:
-- https://aclanthology.org/2024.findings-eacl.90.pdf
-- https://arxiv.org/abs/2407.09879
-- https://aclanthology.org/2024.findings-acl.136.pdf
I would like to see a much broader discussion on how exactly the proposed approach is different and novel here.

- Only one model (GOLLIE-7B) is used as the main baseline model. It would be beneficial to try out the same approach with additional open-weights model (e.g., LLama-3) and also vary the size of the model to verify the impact of model size as well and whether some gains might diminish with larger models. Is it possible to also run some experiments with, say, 70B models from some standard families such as Llama? What about Gemma 2 9B?

- The focus of the work is on IE task simply because of the idea on how to improve the results via generating annotations for the example translated to English first - this seems to me as another hint that this is the only real novelty of the work, as in other 'non-IE' tasks the work would not bring much novelty. I would like to see an extended discussion here. Is the same method applicable to non-IE tasks that require sequence labels such as the 'niche' NLP tasks of POS tagging and dependency parsing? Would the method bring any performance gains to NLU tasks that are typically used to evaluate cross-lingual transfer in some previous research such as NLI on AmericasNLI and XNLI or QA on TydiQA?

### Questions
- The main novelty of the work seems to be this idea of generating annotations of the example translated to English before annotating the original sentence (as also discussed under "Weaknesses"). Can the authors comment on the increased cost of this approach and if there is a way to cut the cost of additional generation?

- It is unclear to me what happens if a language is unseen by NLLB. Will the proposed method still work or not (and to what extent)? There were some approaches (e.g., see https://aclanthology.org/2023.emnlp-main.242) that proposed easy adaptations of NLLB to unseen languages - it probably makes sense to try out such approaches as well. 

- Given that the evaluation datasets used in this work are quite standard, I would recommend providing also additional reference points (i.e., current state-of-the-art scores) from the literature. This would help the reader to grasp not only the gains over the baseline GOLLIE model (and GPT-4) but also situate the results in a wider context of work on those datasets.

- The authors empirically verify that varying the MT model does not have a profound impact on performance. Can the authors discuss why this observation might hold - is it the inherent limitation of the MT system (e.g., it cannot cover some low-resource languages well regardless of its size) or the inherent advantage of the MT system? Is it also related to simplicity/complexity of the task chosen for this experiment?

- How do language properties (beyond its 'resourceness') affect performance? Can we see some patterns based on language proximity/distance to English?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
### Summary:
This paper proposes a solution called TransFusion (TF) for Information Extraction (IE) tasks in low-resource languages such as African languages with access to only high-resource (en) IE annotated data. It has two key parts 1/ a simple update to the incumbent model GoLLIE's prompt: At inference time, the low resource text input is translated to English and then the model is instructed to first annotate this english text and then "fuse" the final annotations on the low-resource language input. 2/ Fine-tuning GoLLIE for the above inference. For this, high resource (en) data is used and annotations are projected on the translated text. This gives 4-way tuples of the text as well as annotations in both languages. This is used to finetune GoLLIE to do translate, annotate, fuse.

The paper also discusses training data preparation, the modeling formulation and how an LLM's autoregressive decoding is used to execute on this modeling objective. Finally, results are comprehensively shown on a wide variety of languages and datasets where GoLLIE with TF has distinctly better results. Additionally, the paper also shows a stronger baseline than GoLLIE which first translates the en data to target language(s) and uses that to finetune GoLLIE. 

### Overall Recommendation:
My overall recommendation is a soft accept currently. This is mainly because one of the key parts of the finetuning data is currently unclear (as asked in the questions). If that can be simply addressed and/or explained clearly, this paper does have the potential as it solves a wide swath of IE tasks cross lingually.

### Strengths
## Quality:
1. Overall the proposal is a simple prompting and Chain-of-thought (CoT) trick. It is clearly defined, motivated and explained from data generation to training fully as seen in Sec 3.1. 
2. Clear ablation study
3. Good stronger baseline addition with TransTrain
4. Very extensive experiments, appendix visualizations and results. This also includes manual error analysis.
5. Also shows improvements when built with GPT-4. 
6. Good error analysis to the last section of the paper.  

## Significance:
This method establishes a clear path for performing information extraction (IE) with generative or encoder-only models, showing a clear tradeoff and presenting easily usable recipes for many low-resource African languages. This would be very impactful for various applications. 


## Coherence and Clarity
1. The formulations on page 3 help set expectations on the model before jumping into the LLM prompting. This is very useful to fully understand the proposal.  
2. Related work is clearly organized by themes and presented with a comparison to the proposed work.

### Weaknesses
 1. The novelty of the cross lingual transfer and alignment usage is stated with just 2020+ references. This is overstating the novelty. For example: Structured Prediction as Translation between Augmented Natural Languages (Paolini et al): would be very apt to relate to as it also does IE with generative models. 
2. The clarity around the finetuning data formation and some of the formalisms as pointed out in Q1 below is lacking. See questions below for details for where the paper can be improved


### Questions
1. Can you clarify the notations on pages 3 and 4? Specifically, on page 3, src refers to english and tgt/trans refers to the low resource language. On page 4, L173, trans refers to the english examples. Is this understanding correct? I believe this is because Page 3 is talking about generating the training data which translates **from** English, while Page 4 talks about the inference time workflows (as used in finetuning) where the input example is translated **to** English. 
2. L238-L241 are very confusing. From here, it seems somehow that en data has 19k examples and translated data has another 891. Figure 8 in Appendix also shows the same. However, so far in Section 3.1, L145-151 clearly state that all finetuning/training TF data has to be 4-way parallel. So, what do we mean by just 891 translated examples? Don't the 19k in English also need to have translations and spans mapped as labels?
3. The difference between Trans-Train and GoLLIE-TF is that while both use the same 4-way parallel data, Trans-Train only finetunes in the original GoLLIE style using the translated data pairs (x, y) while GoLLIE-TF uses the 4-way data to finetune the task of translate/annotate/fuse. Is this accurate? If so, can you make this explicit inline?
4. Since you were cost-limited per L229, how did that impact the standard test set sizes that you need to run tests on for a fair comparison with literature?
5. Why do you not compare the fusion step alongside standard rule based aligners?

### Soundness
3

### Presentation
2

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
This work introduces a new framework to deal with information extraction in the context of zero shot cross-lingual approaches on low resource regimes. The framework, called TransFusion, consists in two parts i) rely on a high resource language model that that is fed with the translation of the source part in the original language and ii) to fuse the response in the high resource language and the portion on the low resource one training a model to predict an answer based on both inputs.
The framework is applied to the existing English-based model, GoLLIE, to produce GoLLIE-TF, a model to deal with cross-lingual information extraction for low resource languages.
The resulting model is run on a variety of datasets, covering tasks such as NER, Slot detection and relation extraction on up to 50 different languages.

### Strengths
The approach is effective and can be applied in a variety of configurations, i.e in decoder only models, on a large pretrained model like GPT-4 to be used zero shot on even on an encoder only model.
The work makes a good effort in covering several low resource languages from available datasets.
The approach improves over GPT-4 and for translate-traine baselines in most of the languages.

### Weaknesses
Although the approach is relatively simple and straightforward it is not clearly explained on the paper and requires a thorough reading to understand it (see below).
One of the salient points of this paper could also be considered a drawback. TransFusion has been shown to be flexible enough to be used in three different scenarios, each one of them having some minor differences in implementation. One could argue these three "flavours"of TransFusion are, in fact, different models (see below)

### Questions
* Figure 1 could have shown more clearly the fact that the initial portion of the text is translated into English, ran on an english-based model and then with its output and the portion in the original language, the output is predicted. None of these aspects (nor the fact the TransFusion module is trained separately) is shown in this image. 

* Please fix the reference "Team et all, 2023", which took the "Gemini Team" as the name of the first author, and "Team" as its last name

* Although it's not an issue, a better presentation would have completely filled the 10 pages in the submission.
 
* line: 419  "lagnauge"

* line 423 fix double parenthesis. Authors might be referring about two varieties of Tagalog, from Philippines and from Uganda

* Authors might like to stress the fact that the different configurations of TransFusion are, indeed, different usages of the same approach.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The study proposes a translation and fusion (TransFusion) method as an extension to Gollie for zero-shot cross-lingual information extraction.
- The method involves appending translated target language instances to the input prompt. The model is prompted to perform information extraction in English first, which serves as a reference label to improve information extraction performance in the target language.
- For encoder-only language models this entails a two-step approach, where a model fine-tuned in English is used to provide the reference labels for the translated text first. The translated text with the reference labels is then concatenated with the inputs in the target languages and used for the final prediction outcome of the target language data. For decoder-only models, the two steps are combined in one prompt by providing instructions to first generate reference labels in English and then perform the task in the target language.

### Strengths
- The evaluation results suggest performance gains for low-resource languages in comparison to GPT-4, regular Gollie and translate-train baselines.
- The performance benchmarks includes various information extraction tasks across 12 datasets and low-resource languages. Specifically the performance benchmark on low-resource languages shows promising performance benefits for prompting decoder-only and fine-tuning encoder-only models.
- The authors provide ablation studies evaluating the contribution of the annotation in English and the impact of different sizes of machine translation models.

### Weaknesses
 - The benchmarks lack the translate-test baseline. The annotations of the translated English text are not formally included in the evaluation. This evaluation would provide insights in the contribution of the “fusion” step of the framework and should be included for both GPT-4 and Gollie.
- The proposed method lacks innovation. Providing annotated translations in the input prompt to enhance multilingual performance has been explored in related work [1,2]. Furthermore, the engineering approach to cross-lingual information extraction lacks detailed evaluation of each individual component.
- The discussion of the additional computational complexity introduced through machine translation and annotation process is not included in the main body of the paper (included in Appendix Table 7).

### Questions
- Did you consider skipping the translation step during inference for the fine-tuned Gollie-TF? It would be interesting whether training on translation + fusion already results in performance improvements without the need to translate and annotate the test data.
- In lines 48 you mention that your TransFusion method trains language models on tools usage (MT model), however your method does not integrate an interactive use of the MT model. Can you elaborate this description?

### Soundness
3

### Presentation
3

### Contribution
2
