# Is Knowledge in Multilingual Language Models Cross-Lingually Consistent?

- Decision: Reject
- Scores: 5, 8, 6, 5

## Abstract
Few works study the variation and cross-lingual consistency of factual knowledge embedded in multilingual models. However, cross-lingual consistency should be considered to assess cross-lingual transferability, maintain the factuality of the model’s knowledge across languages, and preserve the parity of language model performance. We are thus interested in analyzing, evaluating, and interpreting cross-lingual consistency for factual knowledge. We apply interpretability approaches to analyze a model’s behavior in cross-lingual contexts, discovering that multilingual models show different levels of consistency, subject to either language families or linguistic factors. Further, we identify a cross-lingual consistency bottleneck manifested in middle layers. To mitigate this problem, we try vocabulary expansion, additional cross-lingual objectives, and adding biases from monolingual inputs. We find that all these methods boost cross-lingual consistency to some extent, with cross-lingual supervision offering the best improvement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates cross-lingual factual consistencies for language models, in particular for multilingual encoder-only models like XML-r and multilingual encoder-decoder models like mT0.

Their investigation proceeds along a number of dimensions, including distances between languages as well as a number of mitigation strategies. While the mitigation strategies offer some improvements, cross-lingual supervision directly leads to the largest benefits.

### Strengths
Addressing cross-lingual factual consistency is an important problem, which is investigated from several angels.

### Weaknesses
My main problem with this paper is the choice to trigger/prompt cross-lingual knowledge through code-switching. This seems a very unnatural choice, given that the models were never exposed (unless by coincidence) to code-switched data. I have serious doubts that the outcomes tell us a lot about the cross-lingual capabilities of these models. Why not use Translations of cloze prompts to measure consistency? I am aware of the fact that code-switching has been used to train multi-lingual models (e.g., mRASP) and that it is beneficial to induced shared representations across languages, but I don't see why this would sense for evaluation.

### Questions
While you look into differences between languages, to what extent does the amount of data used during pre-training impact cross-lingual consistency?

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
3

### Summary
The paper explores knowledge consistency across languages in multi-modal encoder type LLMs by testing on a cloze task with  parallel triples in 52 languages focused on referencing tasks. The paper uses several metrics: consistency metrics, consistency evolution, subset-object attention, and a slightly modified version of a metric called IG^2 to measure levels of cross-lingual consistency. The paper finds that multi-lingual models show different levels of consistency depending on the "differences" among pairs of languages, based on geographical distance, language family and use of similar or different scripts. To obtain better consistency in knowledge across languages, they experiment with some mitigation techniques and find that adding monolingual examples to bias, and adding multi-lingual vocabulary and pre-training with aligned words improve results.

### Strengths
Knowledge consistency across multiple languages is important if multi-lingual language models are to be used with confidence in tasks across languages. This paper uses existing metrics to compute knowledge inconsistency in language pairs. The results clearly show that language family and the scripts used matter in the measures of consistency. Similar languages show more consistency, and dissimilar languages shows less consistency. Languages using similar scripts, (i.e., likely similar family and geographical close languages) show higher consistency also. The paper also develops ways to reduce inconsistent knowledge using monolingual biases and appropriate pre-training.

### Weaknesses
The fact that knowledge consistency across languages is higher if they are in the same language group or use the same script seems somewhat self-evident, although it is nice to find experimental evidence for the same. The paper works with one multi-lingual reference-oriented code-switched dataset. It also experiments with only one encoder-only model, although two sizes of it.

### Questions
What are the types of references the dataset has? Some examples will be nice. Do some reference types work better than others? Some examples will be nice in the appendix. What is the alignment objective? Is there no need for analysis of subject-verb attention  and/or object-verb attention? Can any meaningful comparison be performed with methods published in other relevant papers?

### Soundness
3

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
The submission asks whether the masked language models encode factual knowledge consistently across different languages. In the experiments, the authors propose to use a popular world knowledge dataset: mLAMA. Specifically, they use prompts with subjects translated into German, Indonesian, Tamil, and Arabic. Then, they compare the output distributions of the models for prompts in different languages, interpreting similar ranking of tokens as evidence of knowledge consistency.

Subsequent analysis uses a range of interpretability methods to identify the layers and attention patterns that are important for knowledge consistency. Furthermore, the study shows that particular design choices: larger subword vocabulary and using word alignment objectives in multilingual training benefit consistency across languages.

### Strengths
- The work presents a clear-cut research question about multilingual knowledge consistency and proposes a relatively simple experimental setting to address it.  

- The experimental results are followed by a detailed analysis to identify the components and attention mechanisms contributing to knowledge sharing across languages.


- The authors compare XLM-Roberta results with models of similar architecture but differing in specific aspects: XLM-V with a larger vocabulary and XLM-Align using word alignment objective. The survey concludes that these design choices improve cross-lingual consistency.

### Weaknesses
 - The paper makes the wrong assumption about English and Indonesian being related languages. In fact, the languages are significantly typologically different, but they both are written with Latin script.
My suspicion is that the proposed experimental setting can inadequately boost consistency for languages using Latin script because named entities (from mLAMA) in such languages have the same or similar orthographical forms. To address the concern, the authors could analyze the effect of writing script on consistency in more detail and consider alternative task formulation, e.g., with the whole prompt translated (and transliterated) into the target language.  

- Chaotic notation makes the setting hard to understand. Especially section 2 contains multiple instances of notation that are not properly defined (e.g., {...}^{l1} or I^{\S^{l1}}). The methodology description should be clarified, I suggest including a specific example from a dataset.

- The work only considers masked language models, while most newer models are causal. I do not agree with the justification for discarding causal LMs referring to their “inherent hallucination problem” (sic). Please note that masked language models have also been shown to be prone to hallucinations, e.g. by Myaney, Narayan et al. 2020.

### Questions
- Why do you claim that scaling is not a promising strategy for consistency based on the observed bottlenecks in mid-upper layers?  I do not see evidence of that based on the experimental setting.


- How do you treat the cases when the prediction in the original language is wrong? Should we then assign a positive score to the model prediction that repeats wrong predictions in another language?

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
This paper investigates the cross-linguistic consistency of multilingual models. To do this, the authors use the zero-shot cloze-task retrieval format enabled by the mLAMA dataset. However, the task is slightly modified because the prompts are mixed in several languages: the model must not complete the prompt “The capital of England is ___” but “The capital of Grande-Bretagne is ___”. So the words “England” and “Grande-Bretagne” here co-refer to the same underlying concept and should be treated identically by a cross-linguistically consistent model. To measure this consistency, the authors propose several metrics, such as accuracy at rank 1, weighted accuracy at rank 5, but also more precise metrics such as attention analysis or the IG² score.

The XLM-R and mT0 families of models are studied. The main findings are that the models possess a cross-linguistic consistency that is impacted by geographical proximity, language family and writing script. The authors then propose a more in-depth analysis, looking at the consistency score layer by layer and identifying a bottleneck in the intermediate layers.

Finally, the last part of this paper focuses on attempts to improve this consistency in the light of previous findings. To this end, the authors propose several techniques: biasing the model by removing attention or modifying FFN activations, but also by expanding the vocabulary or adding a supervised word alignment training objective. These last two methods are interesting as a direction for future work.

### Strengths
- The theme of this paper is very interesting and important.
- Many metrics are introduced, enabling in-depth analysis.
- Use of causal methods to improve and verify their findings a posteriori.

### Weaknesses
 - Figure presentation: labels/titles should be larger, e.g. Figure 2 shows the same legend and title 3 times, which could be unified in the same graph (or as a table).
- The task definition section is understandable, but I think it needs some rework. In particular, it could benefit greatly from examples as notations are introduced. Finally, I had trouble understanding the baseline: here again, an illustrated explanation would be welcome.
- There are no error bars, yet the effects sometimes seem small (e.g. Figure 2). For example, the differences noted in Figure 5 are subjective and could be more clearly measured. Without clearer statistics, my conclusions from Figure 6 are opposed to those of the authors: I have the feeling that the interventions haven't changed anything, or even degraded consistency!
- Related work is a little light and could be fleshed out further

### Questions
1) Have you controlled for the fact that similar languages will sometimes have the same token for proper nouns, thus artificially skewing consistency? For example, “Paris” is spelled the same in French and English, but differently in Chinese.
2) Why not use the baseline for Figures 2, 7 and 10?
3) Why did you choose a code-mixed set-up? It's an out-of-distribution scenario, which can lead to strange behavior that's not representative of reality?
4) Why did you just look at the sum of the IG²s, thus losing information at neuron level, when you could have looked directly at whether the same neurons activated (using an overlap coefficient, for example)?

### Soundness
2

### Presentation
2

### Contribution
3
