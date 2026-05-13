# Can Knowledge Editing Really Correct Hallucinations?

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
Large Language Models (LLMs) suffer from hallucinations, referring to the non-factual information in generated content, despite their superior capacities across tasks. Meanwhile, knowledge editing has been developed as a new popular paradigm to correct the erroneous factual knowledge encoded in LLMs with the advantage of avoiding retraining from scratch. However, one common issue of existing evaluation datasets for knowledge editing is that \textbf{they do not ensure LLMs actually generate hallucinated answers to the evaluation questions before editing}. When LLMs are evaluated on such datasets after being edited by different techniques, it is hard to directly adopt the performance to assess the effectiveness of different knowledge editing methods in correcting hallucinations. 
Thus, the fundamental question remains insufficiently validated: \textbf{\textit{Can knowledge editing really correct hallucinations in LLMs?}} We proposed {\halluedit} to holistically benchmark knowledge editing methods in correcting real-world hallucinations. First, we rigorously construct a massive hallucination dataset with $9$ domains, $26$ topics and more than $6,000$ hallucinations. Then, we assess the performance of knowledge editing methods in a holistic way on five dimensions including \textit{Efficacy}, \textit{Generalization}, \textit{Portability}, \textit{Locality}, and \textit{Robustness}. Through {\halluedit}, we have provided new insights into the potentials and limitations of different knowledge editing methods in correcting hallucinations, which could inspire future improvements and facilitate the progress in the field of knowledge editing.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper focuses on the assessment of knowledge editing methods in correcting real-world LLM hallucinations. It introduces a new benchmark, HalluEditBench, which evaluates the effectiveness of these techniques specifically for addressing real-world hallucinations. HalluEditBench encompasses a large dataset of verified hallucinations across 9 domains and 26 topics, amounting to over 6,000 instances. The benchmark assesses knowledge editing methods across five dimensions: Efficacy, Generalization, Portability, Locality, and Robustness. Through this framework, the study provides insights into the limitations and strengths of seven established knowledge editing techniques across multiple LLM architectures, guiding further advances in knowledge editing methodologies.

### Strengths
The paper offers a foundational contribution to the study of hallucination correction in LLMs, posing a critical question that has been overlooked in the field: Can knowledge editing effectively address LLM hallucinations?

The authors’ approach demonstrates originality by establishing five distinct evaluation facets (Efficacy, Generalization, Portability, Locality, and Robustness), each of which extends beyond conventional measures to comprehensively assess knowledge editing impacts. These dimensions represent a significant innovation that could be widely adopted in broader LLM evaluations, potentially becoming standard practice for assessing post-training improvements in LLMs.

The experimental insights are both intriguing and impactful, with potential to influence not only the field of knowledge editing but also the broader post-training processes in LLM development.

The work presents a substantial and well-designed set of experiments that effectively support and validate the proposed evaluation metrics.

### Weaknesses
The paper could benefit from providing a more comprehensive description of the dataset construction process, which currently lacks sufficient detail. There is limited information on how domains and topics were sampled or selected from the knowledge source. The paper does not indicate whether the dataset predominantly features popular entities or long-tail entities (e.g., [Sun et al., 2023](https://arxiv.org/abs/2308.10168)), which may impact the generalizability of findings across different distributions of knowledge. I would suggest the authors provide information on the criteria used for selecting domains and topics and an analysis of the distribution of entity popularity in the dataset.

Since the dataset is built from Wikipedia/Wikidata, which are frequently updated, there is potential for temporal mismatches between the dataset and the LLMs. For instance, some LLMs may have been trained on earlier versions, while others may align with more recent data. The authors might need to quantify and analyze the potential extent of outdated or inconsistent information across different LLMs to strengthen the paper’s validity, or propose a method to estimate the temporal alignment between the dataset and each LLM's training data.

As mentioned in the paper, the hallucinations can happen differently for (1) different models, (2) pre-trained/fine-tuned in different periods, (3) different prompt input, etc. The generalization ability of the benchmark may be limited. Since LLMs' knowledge evolves with new releases, a focus on the dataset construction pipeline could add long-term value beyond the static dataset. The authors should emphasize the utility of their dataset construction pipeline, which might hold greater long-term value than the static dataset itself. I would suggest the authors to provide a detailed description of their dataset construction pipeline, including any code or tools used, to enable reproducibility and extension of their work.

### Questions
In the dataset construction section, it is mentioned that Wikipedia was selected as the factual knowledge source, yet the triples were said to be retrieved using the Wikidata Query Service. Given that Wikipedia and Wikidata are distinct resources with content gaps, could the authors clarify where the dataset primarily comes from? Also, since Wikidata is actively edited, please report the version of the dump used for reproducibility.

For completeness, when citing FT-L, it would be helpful to include both Meng et al., 2022, and the original work by Zhu et al., 2020.

Given that 5 out of the 7 knowledge editing techniques evaluated have reported results on GPT family models in their original studies, including at least one GPT model in this study would provide a more comprehensive baseline and strengthen the comparability of results.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
As LLMs are now in productive use for a variety of tasks, the demand for the reliability of their output is growing. However, it is well documented that language models do not always provide reliable facts as output, partly because they usually remain at the level of knowledge of their training and some facts change over time, and partly because it is known that language models can also provide output that is not fact-based. These so called hallucinations are a major problem and various suggestions have already been made as to how models can be prevented from hallucinating.
Knowledge editing methods, for example, are used to update the existing knowledge of a model. This involves updating facts in the form of knowledge triplets by exchanging the object. These methods can also be used for corrections and have already been successfully used to correct the knowledge of models with the corresponding data sets / knowledge bases.
However, as the authors of the article correctly point out, these corrections do not take into account what the models were hallucinating about before they were corrected, but can only determine a general improvement.
Therefore, they create a data set of hallucinations from three models and compare the results of current knowledge editing techniques for five different aspects.
The results of the experiments are as interesting as they are sobering: None of the techniques delivers consistently good results for all models and under all aspects, but the divergent results lead to interesting insights.

### Strengths
A major strength of the paper is clearly that the results presented show  that the effectiveness of knowledge editing techniques can vary greatly and is not necessarily as great on actual hallucinations of the LLMs as the experiments on the previous existing data sets show. The fact that the domain of the fact and the model itself have a decisive impact on the  efficiency (and other scores) is an important point and should be taken into account. The article convincingly and clearly demonstrates that none of the techniques tested can claim to be a satisfactory solution for updating knowledge from diverse domains and from all types of language models and thus for preventing hallucinations. The results are clearly presented and well analyzed throughout. The authors' approach and their experiments are comprehensible and explainable.

### Weaknesses
I missed the authors answering the question from the title of the article more conclusively or at least clearly addressing it again in their conclusion, as this question can basically be answered in the negative (at least in part) based on the results presented. There is also no corresponding outlook. The summary is therefore somewhat abbreviated.
Although the structure of the paper is good and clearly laid out, the section on related work seems like an appendix. It could be moved to before the second section, especially as it cites the knowledge editing techniques in particular, which are then described and classified in more detail in section 2. I would also suggest moving Figure 2 to the Appendix. Although the statistics of the data set are of course useful information, it is not so important for the understanding of the article itself whether  the data for Llama2-7B contains 26 hallucinations on the topic "health - medication" vs. 27 on the topic "health - symptom". The figure is also somewhat small for this wealth of information.
The question-answer pairs based on the hallucinations were generated  with GPT-4o, the prompt is documented in the appendix. Although only tasks such as paraphrasing were required, GPT-4o could in the worst case hallucinate itself or deliver incorrect results. Unfortunately, it is not clear and discussed whether this has been ruled out in case I have not overlooked this.
minor remarks: 
•	Typo “overfiting”, page 4, section 2.3
•	MIT license file not proper anonymized

### Questions
•	Were the question-answer pairs generated by GPT-4o checked manually for correctness?
•	Are the benchmark results still comparable if it may not be possible to draw a similar distribution of hallucinations across the various subject areas for a specific model?

### Soundness
4

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
3

### Summary
While knowledge editing aims to correct these inaccuracies without full retraining, existing evaluation datasets often do not verify if LLMs generate hallucinated responses before editing. The authors present HalluEditBench, a benchmarking framework that evaluates knowledge editing methods against a dataset of over 6,000 hallucinations across 9 domains and 26 topics. Performance is assessed on five dimensions: Efficacy, Generalization, Portability, Locality, and Robustness. The findings offer insights into the strengths and limitations of various editing techniques, contributing to advancements in the field.

### Strengths
S1. This paper presents HalluEditBench, a benchmarking framework that evaluates knowledge editing methods against a dataset of over 6,000 hallucinations across 9 domains and 26 topics. This facilitates future research on leveraging knowledge editing techniques to mitigate hallucinations in LLMs.

S2. This paper introduces some novel insights, such as: The current assessment of knowledge editing could be unreliable; The manifestation of hallucination depends on question design; Editing methods marginally improve or degrade pre-edit Portability Scores, implying LLMs may not really reason with edited knowledge in multi-hop questions.; Efficacy does not have a noticeable correlation with Locality; Parameter-preserving knowledge editing methods such as ICE and GRACE potentially have low Robustness.

S3. The paper is well-organized and has good readability.

### Weaknesses
W1. The paper mentions that existing datasets for knowledge editing fail to verify whether knowledge editing methods can effectively correct hallucinations in large language models. The paper should provide at least one example to illustrate the shortcomings of other benchmarks in this regard. For instance, it could include statistics from other datasets or highlight differences in dataset construction methods compared to the approach proposed here, underscoring the innovations introduced by this work in hallucination detection. This would help clarify the paper’s contributions.

W2. Secondly, when presenting certain insights, the paper should include some speculation on the causes of these insights to enhance their plausibility and persuasiveness. For example, in Section 3.1, the differing performance of the FT-M method on two distinct datasets, and in Section 3.2, the significant drop in the GRACE method's performance on the generalization metric

### Questions
The paper should place greater emphasis on why existing benchmarks fail to validate the effectiveness of knowledge editing methods in addressing hallucinations. Additionally, it should provide a deeper analysis of the insights presented.

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
This work addresses the prevalent issue of hallucinations in LLMs, where non-factual information is generated despite their impressive performance in various tasks. Knowledge editing has emerged as a solution to correct factual inaccuracies in LLMs without requiring complete retraining. However, current evaluation datasets often do not verify whether LLMs actually produce hallucinated outputs before editing, limiting the ability to assess how well these methods address hallucinations. The authors propose HalluEditBench, a comprehensive benchmark specifically designed to evaluate knowledge editing techniques in correcting real-world hallucinations. The benchmark features a large, diverse dataset spanning 9 domains, 26 topics, and over 6,000 hallucinations, and evaluates methods based on five dimensions: Efficacy, Generalization, Portability, Locality, and Robustness. The paper offers insights into the strengths and weaknesses of current knowledge editing methods, which could drive further advancements in the field.

### Strengths
This paper provides a significant contribution by developing a comprehensive and well-structured benchmark tailored to the real-world issue of hallucinations in LLMs. The HalluEditBench framework not only fills a critical gap in current evaluation methodologies but also presents a rigorous, multi-dimensional approach for assessing knowledge editing techniques. Its extensive dataset and focus on practical evaluation criteria (e.g., Efficacy, Generalization) ensure its relevance and applicability in real-world scenarios. This research has the potential to foster future innovations in knowledge editing, addressing a key challenge in improving LLM reliability.

### Weaknesses
1. The benchmark proposed in this paper seems to only evaluate specific models, meaning that when models are updated or replaced, the data will need to be reconstructed. If this is indeed the case, it represents the biggest flaw of this work, making the benchmark impractical.
2. The introduction of the five scores lacks formulas explaining how they are calculated, and the purely textual description makes it difficult to understand.
3. The depth of analysis throughout the paper is insufficient, as it only summarizes and briefly discusses the experimental results. I suggest adding a section that analyzes the reasons behind the limitations of existing editing methods (e.g., why Locality Scores of editing methods except FT-M and ICE are unsatisfactory and why ICE and GRACE potentially have low Robustness).
4. When the authors or the publication are included in the sentence, the citation should not be in parenthesis using \citet{} instead of \citep{} (e.g., Line#52, Line#148).
5. Some grammatical errors, e.g., the last sentence in the Abstract should not include 'at', and Line#132 should use 'a knowledge editing operation' instead of 'an knowledge editing operation'. Please carefully review your text to ensure there are no additional grammatical errors.

### Questions
1. In Figure 4, why is the Generalization Score of GRACE less than 0 in some cases (e.g., types except 'mc' for Llama2-7B)?
2. ICE and GRACE demonstrate good Efficacy Scores, but their Accuracy is not shown in Table 1. I’m curious about how effective their edits are.
3. Are the five scores in the evaluation all newly proposed in this paper? There are no references to previous evaluation work in Section 2.2.

### Soundness
3

### Presentation
3

### Contribution
2
