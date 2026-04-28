# Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
LLMs are an integral component of retrieval-augmented generation (RAG) systems. While many studies focus on evaluating the overall quality of end-to-end RAG systems, there is a gap in understanding the appropriateness of LLMs for the RAG task. To address this, we introduce \metric{}, a holistic metric that evaluates the trustworthiness of LLMs within the RAG framework. Our results show that various prompting methods, such as in-context learning, fail to effectively adapt LLMs to the RAG task as measured by \metric{}. Consequently, we propose \method{}, a method to align LLMs for improved \metric{} performance. The LLaMA-3 family, aligned using our method, significantly outperforms open-source LLMs of similar sizes on ASQA (\(\uparrow\)13.4), QAMPARI (\(\uparrow\)28.9), and ELI5 (\(\uparrow\)13.7). \method{} also significantly enhances models' ability to correctly refuse and provide quality citations. We also demonstrate the effectiveness of \method{} across different open-weight models, including the LLaMA series (1b to 8b), Qwen-2.5 series (0.5b to 7b), and Phi3.5 (3.8b).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Authors present a study of ‘grounded’ RAG in LLMs, i.e., a method for evaluating and aligning LLMs for RAG to increase the correctness of RAG, that LLMs cite the relevant literature and correct information, and identify when they do not have the necessary information to respond accurately (i.e., the “groundedness problem”). Using the direct preference optimization, the fine-tuned TRUST-ALIGN model approaches SOTA performance.

### Strengths
The paper is an original and significant contribution to the field of RAG in LLMs as it helps to mitigate the problems of citation hallucination or groundedness of claims.
The paper clearly articulates an extended experimental protocol, providing the rationale for its methodology. The findings are supported by the presentation of the results, and extensive appendices documenting the various steps of the study.

### Weaknesses
I cannot find any statement with regard to data validation by human reviewers. Despite the multiple steps involved in generating the training sets, it's unclear how the training data were validated. It would appear that the soundness of the generated dataset is reliant on the natural language inference engine and GTP-4 validation alone. It is claimed that many of the results are significant but I cannot find any statistical tests to support those claims.

1017 Collecting Quality Questions. The dataset construction begins by collecting a set of high- quality (challenging) and diverse questions from source datasets i.e. ASQA, QAMPARI, and ELI5—referred to as seed samples 
-> These are used in evaluation, doesn’t this violate the separation principle? I understand these were used as ‘seed samples’ but if these have semantically similar enough, what guarantees are there that the models are not just fitting to the testing data?

### Questions
1017 Collecting Quality Questions. The dataset construction begins by collecting a set of high- quality (challenging) and diverse questions from source datasets i.e. ASQA, QAMPARI, and ELI5—referred to as seed samples 
-> These are used in evaluation, doesn’t this violate the separation principle? I understand these were used as ‘seed samples’ but if these have semantically similar enough, what guarantees are there that the models are not just fitting to the testing data?

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
2

### Summary
The authors develop several new metrics for assessing LLM response groundedness in a RAG setting. These metrics comprise a holistic  groundedness/trustworthiness metric called Trust-Score. In addition, the authors develop a fine-tuning method called Trust-Aligne for increasing LLM response groundedness. The authors fine-tune several Llama, Qwen, and Phi models using this and other baseline methods, and they also compare the groundedness of the resulting models' responses to larger proprietary models prompted with ICL.

### Strengths
Originality: high. I don't think I've seen a thorough assessment of grounded refusals before.
Quality: moderate.
Clarity: moderate. The definition of Trust-Score is clear, nuanced, and well-motivated. The description of the dataset generation and fine-tuning process is also detailed and clear.
Significance: moderate.

### Weaknesses
Given that the best fine-tuned models only slightly out-performed GPT-4, it seems there are limited practical takeaways to be found for e.g. an application developer choosing and LLM. i.e. the practitioner is still well-justified in simply choosing a non-fine-tuned frontier model for their RAG application.

I found tables 2 and 3 very difficult to interpret, though mostly because it's not clear to me why the specific comparisons presented are valid or meaningful.

No confidence intervals are given.

### Questions
Why are the comparisons presented in Tables 2 and 3 meaningful? e.g. Trust-Score on LLaMA-3.2-3b fine-tuned with DPO compared to LLaMA-2-7b using FRONT? Why are comparisons not restricted to within-model?

Why is groundedness important in its own right if parametric knowledge can get the job done? If a model possesses the parametric knowledge to answer an otherwise un-answerable question, is "over-responsiveness" less an issue of hallucination than, say, poor instruction-following?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a metric called "trust-score" for assessing groundedness, alongside an alignment approach aimed at improving this metric. It provides a useful metric for advancing the groundedness of large language models (LLMs) for a variety of applications. I am actually surprised there has been no metrics like this for groundedness.

### Strengths
It provides a useful metric for advancing the groundedness of large language models (LLMs) for a variety of applications.

### Weaknesses
Minor Issue: The definition of the Trust Score, particularly the subscript notation, is somewhat unclear (and also in Figure 1). It might help to explore ways to improve readability.

Distinction Between Parametric Knowledge and Groundedness: Could you further discuss the practical implications of distinguishing between parametric knowledge and groundedness? While it adds rigor to make this distinction, to what extent would a user be concerned about whether information comes from parametric knowledge versus grounded sources? In which scenarios might this distinction be more critical?

Choice of Models in Figure 2 (Steps 4–6): Why are different models used in Steps 4 (GPT-4) and Steps 5–6 (LLaMA-2-7B)? Is it because Step 5 requires fine-tuning? However, fine-tuning is also possible with GPT-4 via API, correct? If the decision was driven by the use of DPO for alignment in Step 6, could you clarify the rationale for these model choices?

Method Clarification (Line 271): Could you elaborate on the methodology for selecting documents similar to those containing gold claims but still irrelevant to the query?

Comparative Baseline (Line 359): What results would you observe if compared to a simple instruction-based baseline? For instance, Baseline 1 could involve instructing the model explicitly to avoid over-responding.

Clarification on SFT Model (Line 387): Regarding the SFT model, do you mean fine-tuning with the trust-align dataset, specifically with only positive responses (r+)? Please clarify if so.

### Questions
Choice of Models in Figure 2 (Steps 4–6): Why are different models used in Steps 4 (GPT-4) and Steps 5–6 (LLaMA-2-7B)? Is it because Step 5 requires fine-tuning? However, fine-tuning is also possible with GPT-4 via API, correct? If the decision was driven by the use of DPO for alignment in Step 6, could you clarify the rationale for these model choices?

Method Clarification (Line 271): Could you elaborate on the methodology for selecting documents similar to those containing gold claims but still irrelevant to the query?

Comparative Baseline (Line 359): What results would you observe if compared to a simple instruction-based baseline? For instance, Baseline 1 could involve instructing the model explicitly to avoid over-responding.

Clarification on SFT Model (Line 387): Regarding the SFT model, do you mean fine-tuning with the trust-align dataset, specifically with only positive responses (r+)? Please clarify if so.

### Soundness
3

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
3

### Summary
This paper examines the trustworthiness of LLMs within the RAG framework. The authors introduce a unified evaluation metric, TRUST-SCORE, designed to assess both response truthfulness and attribution groundedness, ensuring that model outputs are based on retrieved documents rather than on the model's internal parametric knowledge. Additionally, the authors propose a new alignment method, TRUST-ALIGN, to enhance LLM trustworthiness according to the TRUST-SCORE metric, demonstrating improvements over baseline approaches such as in-context learning when also evaluated with the proposed metric.

### Strengths
The paper is well-written, with a relevant set of experiments to evaluate the meaningfulness of the proposed metric and alignment method across various datasets, and model configurations. The inclusion of ablation studies and additional results allows for a deeper understanding of the method's impact.

The rationale behind each term in the proposed metric is clear and grounded in prior research, making it easy to interpret the components individually and understand their contributions to the final score. This breakdown helps readers see how each part of the metric contributes to the final score, making it easier to understand which factors are driving the results. Such clarity is particularly valuable for RAG models where responses must be both accurate and grounded in retrieved documents rather than relying on the model's internal knowledge.

### Weaknesses
The results in Table 2 are hard to interpret. The best DPO values come from different model sizes depending on the dataset, which makes it hard to draw general conclusions about which configuration works best overall. Additionally, it’s unclear how reliable the TRUST-SCORE is as a standalone measure, since its value can end up high simply due to averaging across metrics., rather than showing a clear advantage in each metric. This approach can lead to "metric gaming," where high performance in one sub-metric can boost the final score even if other terms don’t improve much, which might overstate the model’s actual abilities. For example, PostCite TRUST score of 22.28 in row 2 of Table 2 under QAMPARI is higher than other baselines, despite having an EM score of zero.

Another problem is that while FRONT seems to be the strongest baseline, we don’t have results for it across different model sizes and families, particularly those where DPO performs best in Tables 2 and 3. This makes it challenging to judge how beneficial TRUST-ALIGN really is.

Lastly, the paper doesn’t clearly explain how the proposed alignment method is different from previous SFT and DPO methods mentioned in the related work section, leaving some ambiguity around what’s truly novel here.

### Questions
> L246: “The positive response corresponds to an answer that encompasses expected gold claims for q and corresponding citations referring to the documents.”

**Q1:** If the response contains partial gold claims or partial citations, is it included in the dataset? If so, as + or -?

> L277:  “we fine-tune LLaMA-2-7b on the source datasets, creating $M_{sft}$ (Appendix E.1).”

**Q2:** It's not clear how fine tune is performed and the appendix does not clarify that. Is the fine tuning task next token prediction? If so, how are questions, documents and answers stitched together?

**Q3:** Why does TRUST-ALIGN without refusal HT increase the $F1_{rg}$ score in the ELI5 dataset in Table 4? Is this a typo (see 2nd item in the list of typos below)? 

**Q4:** I understand the importance of disentangling parametric knowledge from grounded knowledge for the purpose of this study, but in practice, one would leverage both. If I understand correctly, the alignment method proposed by the authors could be used to reduce hallucination. How do the metric and alignment method introduced in this work generalize to real-world scenarios?

## Typos:

L282: 19K. Figure 2 says 20K and 50% of 40K is 20K.

L449: the difference is 0.48% for QAMPARI and -0.78% for ELI5.

### Soundness
3

### Presentation
3

### Contribution
3
