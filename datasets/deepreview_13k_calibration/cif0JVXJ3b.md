# Qualifying Knowledge and Knowledge Sharing in Multilingual Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 3, 5

## Abstract
Pre-trained language models (PLMs) have demonstrated a remarkable ability to encode factual knowledge. However, the mechanisms underlying how this knowledge is stored and retrieved remain poorly understood, with important implications for AI interpretability and safety. In this paper, we disentangle the multifaceted nature of knowledge: successfully completing a knowledge retrieval task (e.g., “The capital of France is __”) involves mastering underlying concepts (e.g. France, Paris), relationships between these concepts (e.g. capital of), the structure of prompts, including the language of the query. We propose to disentangle these distinct aspects of knowledge and apply this typology to offer a critical view of neuron-level knowledge attribution techniques. For concreteness, we focus on Dai et al.'s (2022) Knowledge Neurons (KNs) across multiple PLMs, testing 10 natural languages and unnatural languages (e.g. Autoprompt).
Our key contributions are twofold: (i) we show that KNs come in different flavors, some indeed encoding entity level concepts, some having a much less transparent, more polysemantic role , and (ii) we uncover an unprecedented overlap in KNs across up to all of the 10 languages we tested, pointing to the existence of a partially unified, language-agnostic retrieval system. To do so, we introduce and release the mParaRel dataset, an extension of ParaRel, featuring prompts and paraphrases for cloze-style knowledge retrieval tasks in parallel over 10 languages.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents a valuable investigation into knowledge representation within pre-trained language models (PLMs), specifically exploring how these models encode and retrieve factual knowledge. The authors introduce a fine-grained typology of knowledge that separates various aspects, such as entity concepts, relationships, and prompt structures. By examining the Knowledge Neuron (KN) framework across multiple PLMs, they reveal that not all neurons are monosemantic; rather, a significant portion exhibit polysemantic behavior, with only certain neurons specialized for specific concepts or relationships. 

The study’s empirical findings, derived from a range of models (e.g., BERT, Llama 2, and mBERT) and 10 languages, uncover substantial overlap in knowledge representation, suggesting a cross-linguistic, language-agnostic retrieval system. The authors also introduce the mParaRel dataset, an extension of ParaRel in 10 languages, enhancing the scope of knowledge retrieval evaluation. These contributions imply that language models may benefit from shared multilingual training, offering insights into efficient expansion to new languages. 

Overall, the paper provides a thoughtful critique of neuron-level attribution techniques, indicating that future PLM training could optimize for unique linguistic characteristics rather than relearning factual knowledge for each language.

### Strengths
Originality: This paper is highly novel, introducing a new typology for analyzing knowledge in PLMs that challenges the Knowledge Neuron hypothesis of monosemanticity. By revealing polysemantic behaviors in neurons, the study provides a nuanced view of knowledge representation, paving the way for a broader understanding of how PLMs encode concepts and relationships.

Quality: The study is well-executed, with a solid experimental design across a variety of PLMs and languages. The release of the multilingual mParaRel dataset further enhances the quality and replicability of this work.

Clarity: The paper is clearly organized, especially in detailing the methods and experimental results, making the findings accessible to readers.

Significance:
This work has considerable impact, as it suggests that knowledge in multilingual models may be stored in a language-agnostic manner, meaning retraining for each language might be unnecessary. This insight holds potential for more efficient multilingual model training, especially for low-resource languages, and offers a promising direction for leveraging neuron-level analysis in PLMs to improve model interpretability and efficiency.

### Weaknesses
P9 L468: The formula $(\text{number of languages})^{-\alpha}$ is introduced, but the value and explanation of $\alpha$ are not provided. It would help to describe this parameter to make the formula more rigorous. Specifically, the lack of context around the range of possible values for $\alpha$ and how it is empirically determined leaves a gap in understanding the model's behavior. For instance, is $\alpha$ a hyperparameter tuned for each model, or is it a fixed value? The paper should clarify the process of selecting or deriving this value.

P9 L468-469: Assuming $\alpha$ is between 0 to 1, both $(\text{number of languages})^{-\alpha}$ and $p^{\text{number of languages}}$ decay as the number of languages increases. How can we be confident that the curve shown in Fig. 4c follows the former form and not the latter? A brief explanation of how the curve was fitted to these two functions would be helpful, as it directly impacts one of the major conclusions that KNs are multilingual. The paper needs to detail the fitting procedure, including the optimization method used, the loss function, and the criteria for selecting the best fit. Without this, the conclusion that the decay follows a power law rather than an exponential decay is not fully supported.


### Questions
P4 L163-164: "we apply our analysis to the earliest of these methods by way of illustration." Could you please specify which is "the earliest" of these methods?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores how multilingual language models encode and share knowledge across languages. Specifically, the authors categorize Knowledge Neurons (KNs) into two subtypes: relation neurons and conceptual neurons. They investigate to what extent these neurons exist, their contributions to knowledge retrieval, and their impact on downstream tasks. The paper introduces mParaRel, a multilingual variant of ParaRel, to facilitate experiments across ten languages. The authors find that while most KNs do not adhere to a clearly defined role, some KNs do serve specific functions. Their findings suggest that many KNs are shared across languages, indicating a partially language-agnostic retrieval mechanism in multilingual models.

### Strengths
1. Differentiating conceptual neurons and relation neurons is a meaningful theoretical advancement in studying knowledge representation.

2. The mParaRel dataset is a valuable contribution to multilingual probing research.

3. The experiments provide sufficient support for the paper's central claim regarding the individuality and shareability of knowledge neurons across languages.

### Weaknesses
1. The contribution of the paper is not novel or different from the lines of work in multilingual knowledge probing, where they all indicate that there exist language-agnostic and language-specific neurons such as [1][2][3]. None of the works were cited or discussed here. 

2. The authors rely on threshold-based methods to classify neurons as either conceptual or relational, but variations in thresholds produce different neuron classifications. This makes the claim unrobust: line 208 "When the thresholds become more restrictive, the number of neurons with well-defined roles decreases". There needs to be more effort in verifying that the relation neurons are indeed representing perform identical relational functions across languages.

### Questions
What are your insights regarding the differences in knowledge-sharing levels among various language pairs? Figure 4 indicates that Spanish shares more knowledge with Danish and Dutch than with French or Italian, which belong to the same Latin family. Do you observe any cross-model similarities related to this finding?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigated the knowledge representation mechanism of language models based on knowledge neuron. Specifically, by investigating knowledge neurons across different instantiations, prompts and languages, they find that 1) knowledge neurons exhibit different flavors, some encoding entity-level concepts, others with a more polysemantic role. 2) part of the knowledge neurons are shared by certain languages. 3) some knowledge neurons of certain LMs are shared between natural and unnatural prompts (specifically autoprompt).

### Strengths
- The findings and conclusions of this paper contribute to researchers' understanding of the knowledge storage mechanisms in LMs, thereby facilitating further in-depth research in the future.
- The proposed multilingual dataset can benefit future relevant studies.
- This paper offers several interesting perspectives for analyzing the knowledge mechanisms of LMs.

### Weaknesses
 - My primary concern regarding this paper is the **reliability and generalizability of its conclusions**.
  - All analyses are based on the knowledge neuron (Dai et al. 2022), a gradient-based algorithm initially proposed for encoder-only models. However, the authors did not verify whether their conclusions hold with other knowledge attribution methods (e.g., ROME, SAE). This significantly limits the applicability of their corresponding conclusions.
  - In their analysis of Relation Neuron and Concept Neuron, the authors subjectively define the selection of relevant knowledge neurons through threshold values. Consequently, the identified knowledge neurons are significantly affected by the chosen thresholds, making it uncertain whether these neurons genuinely encode the information as claimed by the authors. To address this, **the authors should incorporate more intuitive and precise analytical methods to ascertain the reliability of the identified neurons**. For instance, they could investigate whether perturbing these neurons affects the model's expression of a specific concept without impacting other concepts.
  - For a probing study, the authors should incorporate more recent and larger models, considering that LLaMA-2 has already been released for over a year. Additionally, it would be beneficial to conduct a more in-depth analysis of the consistency and differences in conclusions across different models.
  - Regarding the authors' analysis of different prompt types, they considered only a single prompt search algorithm (AutoPrompt). However, since both AutoPrompt and KN are gradient-based methods, the reliability of the corresponding conclusions is questionable.

### Questions
See Weakness

### Soundness
2

### Presentation
2

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
In this paper, the authors provide a new perspective to refine the concept of "knowledge" by introducing the Concept Neurons and Relation Neurons. The authors also construct a multilingual version of the ParaRel dataset called mParaRel to analyze the language-agnostic knowledge neurons.

### Strengths
The analysis of knowledge storage and retrieval mechanisms for large language models is very important. This paper introduces concept neurons and relation neurons to study the knowledge mechanism of large language models, which helps to further explain large models. Besides, the authors create a dataset called mParaRel covering 10 languages, which helps to further analyze the internal mechanisms of multilingual large language models.

### Weaknesses
1. The authors should conduct more comprehensive experiments to demonstrate the accuracy of the localized concept neurons and relationship neurons. The stability or reliability of the experimental results is not sufficiently addressed. Specifically, the paper lacks a rigorous analysis of how the identified neurons respond to variations in input, such as paraphrased sentences or slightly altered contexts. The consistency of neuron activation patterns across different instances of the same concept or relation needs further investigation. A more thorough exploration of the sensitivity of these neurons to noise or adversarial examples would also strengthen the findings.

2. Compared to their previous work, the authors extend the discovery of language-agnostic knowledge neurons from 2 languages to 10 languages, while this contribution is somewhat limited. The paper does not adequately explore the nuances of cross-lingual knowledge representation. It is unclear whether the identified neurons truly capture language-agnostic concepts or if they are merely encoding superficial similarities in the training data. A deeper analysis of the semantic overlap and differences in how these neurons are activated across different languages is needed to justify the claim of language-agnostic knowledge representation.

### Questions
1. Why not use the change rate of output probability as an evaluation metric, when manipulating concept neurons or relationship neurons? The change rate of output probability has been adopted by previous work (Dai et al. 2022).

2. Does the findings of this article apply to larger scale models? It would be better if a larger model could be analyzed, but it may be limited by computational resources.

### Soundness
3

### Presentation
2

### Contribution
2
