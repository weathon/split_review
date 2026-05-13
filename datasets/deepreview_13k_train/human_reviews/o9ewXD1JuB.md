# OLAPH: Improving Factuality in Biomedical Long-form Question Answering

- Decision: Reject
- Scores: 5, 6, 8, 6

## Abstract
In the medical domain, numerous scenarios necessitate the long-form generation ability of large language models (LLMs).
Specifically, when addressing patients' questions, it is essential that the model's response conveys factual claims, highlighting the need for an automated method to evaluate those claims.
Thus, we introduce \textbf{MedLFQA}, a benchmark dataset reconstructed using long-form question-answering datasets related to the biomedical domain.
We use MedLFQA to facilitate a cost-effective automatic evaluations of factuality.
We also propose \textbf{\textsc{Olaph}}, a simple and novel framework that utilizes cost-effective and multifaceted automatic evaluation to construct a synthetic preference set and answers questions in our preferred manner.
Our framework leads us to train LLMs step-by-step to reduce hallucinations and include crucial medical claims.
We highlight that, even on evaluation metrics not used during training, LLMs trained with our \textsc{Olaph} framework demonstrate significant performance improvement in factuality.
Our findings reveal that a 7B LLM trained with our \textsc{Olaph} framework can provide long answers comparable to the medical experts' answers in terms of factuality.
We believe that our work could shed light on gauging the long-text generation ability of LLMs in the medical domain.co/datasets/dmis-lab/MedLFQA}{https://huggingface.co/datasets/dmis-lab/MedLFQA}} are available.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a dataset MedLFQA for automatic evaluation of factuality long-form question-answering in the biomedical domain. The authors also proposed a training framework and claimed that this framework can optimize LLMs to reduce hallucination step-by-step. 
The study topic in this paper is important as the hallucination problem is critical when applying LLMs in the health domain. The manual evaluation and the dataset would be beneficial to the community. 
My main concerns are:
1. The MedLFQA sets the answers in MUST HAVE and NICE TO HAVE and then calculates the hallucination and comprehensiveness metrics by comparing the generated text and the reference text. Although automatic hallucination detection and quantization are difficult, and it is worth exploring automatic evaluation methods, it is not persuasive that the current setting can effectively serve as the hallucination metric. The problems are: a) this setting only evaluates a subset of hallucination; the LLM generated incorrect facts that outside of the MH and NH will not be taken into account in the metrics; b) The calculation of contradicts and entails are based on a fine-tuned BioBERT model, which brings uncertainty of the evaluation, especially on the medical domain. The metrics are highly affected by the performance of the fine-tuned BioBERT model, so a sensitivity analysis needs to be tested. In total, it is not persuasive that the current hallucination and comprehensiveness metrics are sufficient. 
2. It is no surprise that the proposed OLAPH framework can improve the three metrics (Word composition, Semantic Similarity, and Factuality), as these three metrics are directly optimized during the training (similar to the comparison that fine-tuned model is better than non fine-tuned). 
3. Question: In Table 5, when setting the alpha_3 as 1.0, the performance seems better than other smaller alpha_3 scores. So if we enlarge the alpha_3 over 1 (2,3,5 or more), will the model's performance continue to improve? Furthermore, it would be interesting to see the performance of the single loss function (i.e., set two other alpha as zero) to confirm which loss function contributes the most.

### Strengths
The study topic in this paper is important as the hallucination problem is critical when applying LLMs in the health domain. The manual evaluation and the dataset would be beneficial to the community.

### Weaknesses
1. The MedLFQA sets the answers in MUST HAVE and NICE TO HAVE and then calculates the hallucination and comprehensiveness metrics by comparing the generated text and the reference text. Although automatic hallucination detection and quantization are difficult, and it is worth exploring automatic evaluation methods, it is not persuasive that the current setting can effectively serve as the hallucination metric. The problems are: a) this setting only evaluates a subset of hallucination; the LLM generated incorrect facts that outside of the MH and NH will not be taken into account in the metrics; b) The calculation of contradicts and entails are based on a fine-tuned BioBERT model, which brings uncertainty of the evaluation, especially on the medical domain. The metrics are highly affected by the performance of the fine-tuned BioBERT model, so a sensitivity analysis needs to be tested, specifically with different NLI models and not just variations of BioBERT. In total, it is not persuasive that the current hallucination and comprehensiveness metrics are sufficient. These evaluation limitations need to be discussed in more detail, including the potential for error propagation from the NLI model.
2. It is no surprise that the proposed OLAPH framework can improve the three metrics (Word composition, Semantic Similarity, and Factuality), as these three metrics are directly optimized during the training (similar to the comparison that fine-tuned model is better than non fine-tuned). The optimization process essentially trains the model to align with the evaluation metrics, which is a circular process. The paper needs to address this circularity and provide a more robust justification for the observed improvements beyond direct optimization.


### Questions
Question: In table 5, when set the alpha_3 as 1.0, the performance seems better that other smaller alpha_3 scores. Why not to enlarge the alpha_3 over 1 (2,3,5 or more) to test the model performance? Furthermore, it would be interesting to see the performance of the single loss function (i.e. set two other alpha as zero)

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
This paper aims to improve factual accuracy of large language models (LLMs) in generating long-form answers within the biomedical domain through two main contributions.
The authors first introduce MedLFQA, a benchmark dataset designed to facilitate the automatic evaluation of factual claims in LLM responses.
Next, the paper proposes OLAPH (Optimizing Large language models' Answers with Preferences of mitigating Hallucination) framework, which iteratively trains LLMs to reduce hallucinations and incorporate essential medical information by leveraging synthetic preference sets derived from cost-effective, multifaceted automatic evaluations.
Experimental results demonstrate that a 7B parameter LLMs trained with OLAPH can generate responses with improved factuality comparable to those of medical experts.

### Strengths
+  The paper addresses an important problem in the medical domain, where factuality is crucial for patient safety and trust in medical AI systems.
+ The paper is clearly written with well-structured presentation, clear visualizations, and illustrative examples.
+  The introduction of MedLFQA as a unified benchmark for evaluating factuality in biomedical LFQA is a valuable contribution to the field.
+ The effectiveness of OLAPH is comprehensively validated with thorough analyses, comparisons with proprietary models, and evaluation using metrics independent of the training process,

### Weaknesses
 + The novelty of the proposed OLAPH framework is limited, as it mostly follows the standard preference optimization process (SFT and DPO)

 + The paper should address the convergence properties of OLAPH: Is convergence guaranteed? How do the number and types of evaluation metrics influence convergence rates?
+ Can the evaluation criteria for the qualification of generated data in section 3.2 be used as preference criteria for preference optimization process in section 4.2?
+ Why does the paper follow cross-validation approach for experiments instead of the traditional train/test split approach?

### Questions
+ The paper should address the convergence properties of OLAPH: Is convergence guaranteed? How do the number and types of evaluation metrics influence convergence rates?
+ Can the evaluation criteria for the qualification of generated data in section 3.2 be used as preference criteria for preference optimization process in section 4.2?
+ Why does the paper follow cross-validation approach for experiments instead of the traditional train/test split approach?

### Soundness
3

### Presentation
3

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
the paper introduces MedLFQA dataset to evaluate long-form answers in biomedical contexts. The authors generated this dataset by combining multiple existing datasets to enable comprehensive assessment. This fills a gap in the automated evaluation of LFQA in a domain where factual accuracy is critical. Also, the authors propose & evaluate OLAPH framework on word composition, semantic similarity, factuality- using benchmarks and metrics like FACTSCORE. This framework shows improvements (in factual accuracy) for 7B small parameter models. This study is a novel attempt to reduce hallucinations in medical responses.

### Strengths
The paper shows an innovative approach to enhancing the factual accuracy of long-form biomedical question answering. This work also creatively combines current techniques in preference-based learning and factual consistency checks to improve medical domain answers, addressing key limitations in factuality and response quality in prior research. This work is good in quality of methodological design. They have detailed each step in OLAPH’s alignment process making it easy for others to build on top of it. The evaluation approach is also comprehensive as they used well known metrics. The paper is clearly written and answers major questions readers (at least I) may have. The significance of OLAPH lies in its potential to impact the application of LLM in healthcare. Medlfqa dataset can help other researchers in developing and evaluating factually accurate medical response systems.

### Weaknesses
The framework instroduced in this study is using GPT-4 to generate must-have and nice-to-have statements in medlfqa. My concern is that it may introduce biases or inaccuracies into the dataset. Although the researchers show that GPT-4-generated responses are close to human-curated answers, i did not find a critical analysis of where synthetic statements might diverge from medical experts.

Also, i think the study framework is a good step towards medical LLMs, but it does not cover the framework's behavior for a domain-specific case like disease diagnosis or recommendation of treatment.

### Questions
1. Were there specific medical domains or types of questions where synthetic responses diverged from expert standards?
I think it would be helpful if you could discuss any plans to validate the quality of synthetic data using a diverse set of generative models to assess robustness.

2. As we know, medical knowledge advances over time. So, I am curious to understand how you plan to deal with the challenges of maintaining factual relevance if your framework/dataset is deployed over a longer period?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This research paper introduces OLAPH, a framework designed to improve the factual accuracy of long-form question answering in the medical domain. The authors address the challenge of hallucinations in large language models (LLMs) by utilizing a cost-effective and multifaceted automatic evaluation system to generate synthetic preference sets. These sets guide the LLMs in prioritizing factuality, semantic similarity, and word composition. 

To facilitate automatic evaluation, the authors introduce MedLFQA, a reconstructed benchmark dataset that includes long-form answers and crucial statements derived from existing biomedical question-answering datasets. Through experiments, the authors demonstrate that even 7B LLMs, trained with OLAPH, can generate answers comparable to GPT-4 and medical experts in terms of factuality.

### Strengths
1. the data set collection follows good practice with human verification (high agreement).
2. method is clearly explained.
3. experiments are thorough (though I have questions and suggestions below).
4. most part of the paper is well written and easy to follow.

### Weaknesses
1. The method itself (OLAPH) is not really "novel" as the authors claim - the general frameworks has been used in many post-training of LLMs such as Llama and Claude models. I suggest softer contribution claims here.
2. Some claims are not very rigorous - see my questions below.
3. The final analysis can be made clearer.

### Questions
1. For the analysis of or RQ 3, what's exactly experimental setup? I am not getting why you will need to supply domain knowledge here, and since you train multiple models in RQ 1 and 2, which models did you end up using for this?
2. In Figure 5, if using SFT leads to initial drop of performances, have you try to remove it? And what would the impact be?
3. Line 235 - 236, this may simply suggest that answers in K-QA is terrible, not necessarily that GPT-4 answers are good. Do you have more analysis here?
4. Line 248 - 252, I am not 100% convinced by this claim. Could it be that annotators are biased to believe whatever the model generates?
5. Line 282 + 283, do you use statements as SFT targets too? If so, what's the data format?

### Soundness
3

### Presentation
3

### Contribution
2
