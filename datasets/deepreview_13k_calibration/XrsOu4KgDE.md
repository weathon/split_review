# Attributing Culture-Conditioned Generations to Pretraining Corpora

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 6, 8, 8, 8

## Abstract
In open-ended generative tasks such as narrative writing or dialog interaction, large language models are known to manifest culture biases, showing inadequate knowledge and producing templated generations on less prevalent cultures. Previous works suggest that such biased generations are due to the uneven representation of each culture in pretraining corpora of the language models. In this
work, we study how pretraining data lead to biased culture-conditioned generations via the lens of LLM memorization and generalization, in order to provide more insights on improving the pretraining data and the pretraining procedure of LLMs. We introduce the MEMOed framework (MEMOrization from pretraining document) which determines whether a generation for a culture is due to memorization or generalization. On culture-conditioned generations about food and clothing entities for 110 cultures, we find that for a culture with high frequency in pretraining data, the model can recall more memorized knowledge about the culture; for cultures appearing least frequently, none of their generations contain any entities memorized from pretraining. In addition, we discover that the model prefers generating about entities with extraordinarily high frequency regardless of the conditioned-culture, an indication of overmemorization, where the model demonstrates biases towards frequent terms in pretraining data regardless of its correctness. Our findings show that current LLM generations majorly consist of memorization and un-founded overmemorization. We hope that the MEMOed framework and our insights will inspire more works on attributing model performance on pretraining data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a framework, called MEMOED, to determine whether culture related entities, refered to as symbols, are resulted from memorization or generalization of LLMs based on the pretraining data. This study defines three categories of symbols, i) independent symbols, ii) culture-specific symbols, referred to as memorized symbols, and iii) symbols generalized across certain cultures, referred to as generalized symbols. Various experiments are conducted using OLMO on 110 cultures to understand how OLMO's performance is affected by memorization and generalization.

### Strengths
* This paper selects a good research problem, which is to understand how the frequencies of certain culture related concepts or entities in the pre-training data influence the model performance, in particular from the perspective of generalization and memorization.
* The high-level ideas to discuss about independencies, memorization and generalization are reasonable.
* The dataset covers over 100 cultures.

### Weaknesses
 * The definitions of the following concepts and their justification are unclear unclear to me.
    * What is a symbol? Do they cover all linguistic variations of the same entity or concept? For instance, if the concept is 'apple pie', would 'apple pies' or 'a pie made of apples' be considered the same symbol? The paper needs to clarify whether it considers only surface forms or also includes semantic variations.
    * How culture is defined? Why it is represented as a combination of country and natonality. The literature in social science has already defined culture. There could be more than one cultures in a country. Would a representation of country and nationality be overly simplied? For example, how would the model handle cultural differences within a country like India, which has significant regional variations in food and clothing?
    * How to justifiy the definition of memorization through Equation (1)? Why it makes sense? The paper does not provide a clear rationale for using the log ratio of culture-specific counts to the sum of other culture counts. What is the theoretical basis for this specific formulation? Why not use a more standard measure of term frequency or TF-IDF?
    * How generalization is defined and why? The paper needs to provide a more rigorous definition of generalization. Is it simply the absence of memorization, or is there a more nuanced criterion? The paper should clarify how it distinguishes between true generalization and spurious correlations.
* It lacks of justification of the formula for r(D, Q) in Page 5, as well as the measure for memorization. Why log ratio is preferred over the standard techniques, e.g. statistical dependencies? There are often various ways to convey an entity or a concept. How are linguistic variations captured with this measure? As this measure is used together with the contribution score and z-score to determine if a symbol is memorized. There is no empirical evidence or theoretical justification showing that this measure indeed meets the expectation. The use of a log ratio needs more justification compared to other statistical measures. The paper should also address how it handles the issue of polysemy, where a single word can have multiple meanings across different cultures. The current approach seems to assume a one-to-one mapping between symbols and concepts, which may not hold in reality.

### Questions
* There could be an alternative way to convey symbol and culture overmemorization, if the purpose is to show that certain entities occur more often in model outputs that those observed in the pre-training data.
* How do you ensure the quality of annotations using culture experts?
* How symbols are collected? Is there a systematic way to sample data from the 110 cultures?

### Soundness
2

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
3

### Summary
About culture-conditioned generations out of LMs, dealing with the issue that biased generations can be driven by pretraining corpus statistics.

They introduce a “symbol attribution framework” to determine if culture-conditioned symbols were memorized in training. They characterize symbols as independent, memorized, or generalized depending on whether they appear in a “culture’s generations” broadly, without a specific culture association, appear primarily in a small set, or if they appear broadly across cultures without presence in the pretraining corpora. 

They use document SNR, minimum token distance, and minimum sentence distance as metrics.
- document snr is the log probability ratio of counts of culture-referent n-grams to others
- minimum token distance is the length of the shortest span of tokens between one referring to the culture and one to the symbol
- minimum sentence distance uses sentences instead of tokens in the above

They use these functions to construct a heuristic for whether a training document shows the memorizable relationship. They then characterize concepts as being overmemorized, and compare the presence of these statistics in the training data & outputs as a predictor to the agreement of human annotators that these relationships are reflective.

They claim that “traceable generalization”, ie., concepts that are not closely related according to their metrics in training data are nonetheless successfully generated, are not correlated to “memorized” concepts for a culture. There’s one or the other, for example “Mexico” contains specifically memorized queries, while Trinidad has none.

**Edit**: I have responded to the authors rebuttal, and modified my "weaknesses" section. I think the technical contributions are sound, so I have bumped my soundness up to 4 (even though I still am a bit troubled by the scope of the experiments). However, I feel that the presentation of this work is severely flawed, particularly wrt how a reader has to piece together what the experimental methodology was while reading the results. So, I am keeping my presentation score at 2 (though I contemplated dropping it to 1). I will keep my overall score at weak accept---I don't think this paper is ready but if it were to get accepted, interested researchers would be able to make their way through it. I would strongly recommend that the authors consider edits for clarity that address my complaints here in the CR if it does get accepted.

### Strengths
Interesting and useful topic to address.

Mildly interesting results; though I am a little unsure about the claims (see weaknesses).

Approach may generalize, not only to memorization of cultural relationships but also to memorization of other facts/information conditioned on context.

### Weaknesses
Presentation of relatively shallow experiments, ~limited technical novelty~, and limited scale of experiments.

~I’m not fully convinced about these definitions that are used to characterize the memorization classes; how do we know that having these statistics over some threshold means that a concept is “memorized” vs just being consistently generated?~

**EDIT:** I understand the paper better after the authors' explanations and edits. I change my mind regarding the technical novelty (which is an unfair complaint to even have in the first place even if it were accurate)

That being said, I stand by my complaint about the small scale of experiments: while many symbols are generated, and a basically comprehensive set of countries are tested, **only two prompts are used to elicit these outputs.**

Over all, my biggest complaint about the paper didn't make it in to my review, but it's the **poor presentation of the method**. I believe it is a serious problem that key details of the experiments such as "how many prompts? how many cultures? how were the symbols extracted from the outputs?" are not clearly lain out before the results. Additionally, the presentation of the methods suffers from a lot of superfluous mathematical notation that clouds clarity, with symbols that once again aren't introduced until *after* an equation is read, requiring considerable backtracking.

### Questions
This review is a little low confidence; I'm open to changing my mind.

Please clarify any misunderstandings I have, and elaborate on my concern about the definitions?

Why were the classes of concept chosen?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper describes MEMOED (MEMOrization from pretraining document), a framework designed to classify cultural symbols in LLM-generated text as either memorized or generalized.

### Strengths
1. Novel framework and the new problem of analyzing cultural memorization: The paper develops a systematic approach to determine if cultural symbols generated by an LLM are due to memorized data or generalization. This is a novel problem and the approach is sound and elegant.
2. Good Analysis across Cultures: The study uses data for 110 cultures on topics like food and clothing - the analysis is interesting and the conclusions are interesting as well.

### Weaknesses
Reliance on a Single Model: The analysis focuses solely on the OLMo-7B model and its pretraining dataset, Dolma. It is unclear from the analysis how the conclusions would vary on other models or models of other sizes. The lack of analysis on other models limits the generalizability of the findings. For instance, models trained on different datasets or with different architectures might exhibit different memorization patterns, and it is not clear if the observed correlations would hold. Furthermore, the analysis does not explore how model size affects the memorization of cultural symbols. It is possible that larger models with greater capacity might memorize more cultural information, or that smaller models might rely more on generalization. 

It is not clear to me how the definitions of what constitutes memorization (e.g. training document classification)  might change the analysis?

### Questions
Is it possible to do this analysis on several OLMo models?

There are some typos: and and (320)

### Soundness
4

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
4

### Summary
This paper introduces a novel symbol attribution framework to determine whether symbols in LLM generations, conditioned on a culture, result from memorization of pretraining data. The authors' thorough analysis shows that high-frequency symbols are easily memorized but independent of any culture regardless of their correctness. Additionally, by showing the imbalance between the memorization of high-frequency and low-frequency cultural symbols, this paper underscores the need for improved pretraining data and methods to mitigate cultural biases.

### Strengths
**S1**. This paper introduces a novel symbol attribution framework to determine whether the symbols in LLM generations, conditioned on a culture, result from memorization of pretraining data.

**S2**. The authors provide a nuanced categorization of symbols based on their memorization/generalization levels and a thorough analysis of their relationship with the pretraining data.

**S3**. Their findings demonstrate how LLMs fail to represent cultures that are low-frequency in the pretraining data, calling for improved pretraining data and methods.

### Weaknesses
 **W1**. The study is limited to only one pretraining corpus and one LLM, which is understandable given the scarcity of open resources.

**W2**. This study relies on searching for symbols in culture-conditioned generations within the pretraining data and provides a relational analysis. However, it does not guarantee that the selected training documents are causally decisive for the symbols in question. Incorporating influence functions [1] could provide insights into causal relationships. While the computational cost might be an issue, they could be applied to a subset of the dataset or specific experiments.

**W3**. Lines 427-430 require further explanation. What do these correlations imply? Specifically, the relationship between the ratio of document counts and the number of cultures for which an independent symbol is generated needs more clarification. The current explanation is insufficient to understand the underlying mechanism.

**W4**.  While this study highlights the existing problems with underrepresented cultures in pretraining corpora from a new perspective, it fails to address or propose potential directions for solving these issues. Without this, the paper remains another verification of known problems, which is still valuable but not particularly groundbreaking. The authors should discuss how their findings could inform improved pretraining data/methods or mitigation strategies that do not require changes in pretraining.

### Questions
**Q1**. In Figure 1, the top-down order does not match the numerical order. Why are memorized symbols shown at the bottom?

**Q2**. In Figure 3, what does "overgeneralization" refer to? It is not mentioned in the text. Do you mean "overmemorization" instead? The same applies to the caption of Table 3.

**Q3**. How are culture-referring n-grams defined for the Document-Signal to Noise Ratio?

**Q4**. Why do the memorization classification criteria differ for cases where n(C_G) > 5 and n(C_G) < 5?

**Q5**. What do the bold texts represent in the "topic modeling keywords" column of Table 3?


**Typos**:

- Line 345: "none-memorized" should be "non-memorized."
- Lines 106-107: "for less prevalent symbols" -> "for less prevalent cultures."
- There is inconsistent use of "memorisation" and "memorization" throughout the text. It would be better to use one consistently.

### Soundness
3

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
2

### Summary
This paper introduces a novel framework called MEMOED, designed to analyze how pretraining data contributes to cultural biases in large language models (LLMs). The framework distinguishes between knowledge generated through memorization and generalization. By focusing on cultural topics such as food and clothing across 110 different cultures, the authors demonstrate that models tend to overmemorize symbols from highly represented cultures, while underperforming in generating culture-specific symbols for less represented ones. Through a detailed analysis of the OLMo-7B model, the paper offers a systematic method to trace how pretraining data influences model outputs, highlighting the limitations of current LLMs in producing diverse, culturally accurate generations and stressing the need for improved pretraining procedures to address these biases.

(Note: My review has been revised by an LLM for improved grammar.)

### Strengths
- The paper makes a significant contribution by addressing cultural biases in LLMs, and the MEMOED framework provides a valuable tool for tracking these biases.
- The study covers a broad scope, examining 110 cultures, which enhances the depth of the analysis.
- The concept of overmemorization introduced by the authors is intriguing and may have broader implications beyond cultural biases, potentially applying to other LLM phenomena.
- The paper opens up the possibility of examining cultural biases in multilingual LLMs across different languages, which could be an interesting direction for future research.

### Weaknesses
While the methodology appears sound, my only concern is the limited scope of the study, which focuses solely on the OLMo-7B model. As a result, the findings might be seen as a case study specific to this model. It would strengthen the paper if the authors included analyses for at least one additional LLM to broaden the generalizability of their findings. The current analysis does not explore how architectural differences between models might influence the observed memorization and generalization behaviors. For example, models with different attention mechanisms or layer configurations could exhibit varying degrees of cultural bias, and this is not addressed in the current study. Furthermore, the paper does not delve into the potential impact of varying pretraining dataset compositions on the observed cultural biases. It is possible that the specific data sources used to train OLMo-7B might disproportionately represent certain cultures, leading to the observed overmemorization. Without exploring other models trained on different datasets, it is difficult to isolate the effect of the model architecture from the effect of the pretraining data.

### Questions
- Do the authors have any plans to propose methods for mitigating the cultural biases identified in this work?
- Comment: I recommend adjusting the notation for subscripts, such as $d_{TOK}$. It currently appears a bit unnatural, and applying italics to the subscript, such as d_{\textit{TOK}}, would enhance clarity.

### Soundness
3

### Presentation
3

### Contribution
3
