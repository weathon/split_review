# Investigating Language-Specific Calibration For Pruning Multilingual Large Language Models

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
Recent advances in large language model (LLM) pruning have shown state-of-the-art (SotA) compression results in post-training and retraining-free settings while maintaining high predictive performance. However, previous research mainly considered calibrating based on English text, despite the multilingual nature of modern LLMs and their frequent use in non-English languages. In this paper, we set out to investigate calibrating the pruning of multilingual language models for monolingual applications. We present the first comprehensive empirical study, comparing different calibration languages for pruning multilingual models across diverse languages, tasks, models, and SotA pruning techniques. Our results offer practical suggestions, for example, calibrating in the target language can efficiently retain the language modeling capability but does not necessarily benefit downstream tasks. Through further analysis of latent subspaces, pruning masks, and individual neurons within pruned models, we find that while pruning generally preserves strong language-specific features, it may fail to retain language-specific neuron activation patterns and subtle, language-agnostic features associated with knowledge and reasoning that are needed for complex tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the calibration of pruning multilingual language models for use in specific languages, focusing on the impact of choosing a calibration language. While recent LLM pruning techniques achieve high compression without retraining, they often rely on English-based calibration, which may not suit multilingual models used in non-English contexts. 

Through a comprehensive study, the authors compared different calibration languages across tasks, models, and pruning techniques, finding that calibration in the target language preserves language modeling abilities but doesn't consistently improve downstream task performance. Their analysis reveals that pruning generally maintains language-specific features but struggles with complex, language-agnostic aspects needed for knowledge and reasoning tasks. They suggest avoiding reliance on perplexity or English performance metrics for assessing pruned models' performance in other languages.

### Strengths
* This paper tackles essential issues related to the model pruning in multilingual settings.

* The motivation of this paper is clearly described.

* This paper revealed several significant findings, such as calibrating in the target language can efficiently retain the language modeling capability but does not necessarily benefit downstream tasks.

* This paper conducts a deeper analysis of the inner representations of pruning masks and individual neurons, revealing that while pruning generally preserves prominent language-specific features, it may struggle to retain language-specific neuron activation patterns and subtle, language-agnostic features related to knowledge and reasoning, both of which are essential for complex tasks.

### Weaknesses
This paper identifies several issues related to the choices of calibration language that influence the downstream performance of pruned models. However, it lacks discussion or proposals for alternative methods to address these issues. While the paper makes several contributions indeed, it would be more comprehensive if it included potential solutions to the issues it highlights. Currently, I am not very confident that this paper is eligible to be published in a high-standard conference like ICLR, as it primarily presents observations from their experiments.

* This paper is limited by its exclusive focus on a 50% pruning setting. The lack of exploration into varying pruning ratios, especially higher compression rates that are of interest for larger models, leaves a gap in understanding the broader applicability of the findings. For instance, the behavior of calibration languages at 80% sparsity, which is relevant for deploying large models, remains unaddressed.

* In Section 4.1, it states, "There are a few exceptions. For instance, when evaluating Llama-3 pruned with Wanda on Chinese, Russian calibration performs best in terms of perplexity (23.6), slightly outperforming Chinese calibration (24.4)." The paper does not provide a clear explanation for these observations. The fact that Wanda appears to yield poorer results in the target language compared to SparseGPT is not sufficiently analyzed. The underlying mechanisms that cause this degradation are not explored, leaving the reader without a deeper understanding of the differences between pruning methods.

* In the discussion in Section 5.3, I find the statement, "This indicates that pruning introduces LAPE noise, shifting the LAPE score distribution and creating new language-specific (low LAPE) and agnostic (high LAPE) neurons," somewhat unclear. The results for 20% sparsity appear more diverse than those for 50% sparsity. If my interpretation is correct, the statement may be overstated or could misinterpret the observation. If I misunderstand something, please let me know.

### Questions
* This is not a significant weakness, but it is interesting if findings in this paper also appear in slightly different model architectures, such as GPT-2 (an older model) and MoE models like Mixtral. Do the authors have any thoughts on this perspective? If so, could they offer any insights or evidence on whether these findings might generalize to a broader range of architectures?

* From my understanding, this paper employs a 50% pruning setting across all experiments. Is there a specific reason for choosing only this pruning ratio? If not, how might results and findings vary with a different pruning ratio? For instance, for larger models (e.g., 70B), many researchers may be very interested in exploring higher compression rates.

* In Section 4.1, it states, "There are a few exceptions. For instance, when evaluating Llama-3 pruned with Wanda on Chinese, Russian calibration performs best in terms of perplexity (23.6), slightly outperforming Chinese calibration (24.4)." Do the authors have any hypotheses about these observations? For instance, Wanda appears to yield poorer results in the target language compared to SparseGPT. What aspect of Wanda might be responsible for this degradation?



* In the discussion in Section 5.3, I find the statement, "This indicates that pruning introduces LAPE noise, shifting the LAPE score distribution and creating new language-specific (low LAPE) and agnostic (high LAPE) neurons," somewhat unclear. The results for 20% sparsity appear more diverse than those for 50% sparsity. If my interpretation is correct, the statement may be overstated or could misinterpret the observation. If I misunderstand something, please let me know.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper presents a comprehensive empirical study on language-specific calibration for post-training pruning of multilingual Large Language Models (LLMs), using LLaMA-3 and Aya-23 as the base models, and applying Wanda and SparseGPT as the pruning techniques. The authors found that calibrating in the target language effectively retains language modeling capabilities, though it does not necessarily improve performance on downstream tasks. Additionally, the paper provides a detailed analysis of latent subspaces, pruning masks, and individual neurons within the pruned models to examine the effects of pruning on both language-agnostic and language-specific neurons, where language-agnostic features failed to be retained.

### Strengths
S1. The paper presents comprehensive experiments to investigate both language-specific and language-agnostic features, covering multiple calibration languages, models (LLaMA-3 and Aya-23), and pruning techniques (Wanda and SparseGPT). This study evaluates a wide range of metrics—including perplexity, downstream task performance, signal-to-noise ratio, and pruning error—extending the analysis to neuron-level effects and latent subspaces.

S2. The paper provides insights not previously found in English-focused pruning studies, revealing the distinct impacts of pruning on multilingual LLMs.

### Weaknesses
W1. While the paper includes extensive experimentation, the analysis of results feels somewhat limited, as many findings are inconclusive, especially in Section 4. Specific examples include:
- Calibrating on the target language itself **generally** yields the best pruning performance and the lowest perplexity.
- Calibrating using the target language **typically** results in acceptable performance on downstream tasks, though not consistently the best.
- Pruning **can** shift which languages the model performs best or worst on
- Employing bilingual and multilingual calibration sets **occasionally** improves performance on downstream tasks, compared to monolingual calibration.
- The performance patterns and findings from the smaller models **do not consistently hold** true on their bigger counterparts.
- **No pruning technique consistently** performs best in all tasks.

The insights presented in the paper are informative but lack conclusive takeaways, which limits actionable takeaways for the readers. Going back to the introduction introduced in the paper, to my understanding, it still remains unclear how to calibrate pruning to optimize the post-pruning performance of multilingual LLMs on tasks in non-English languages. I think providing a more in-depth analysis by either explaining why certain findings remain inconclusive or making stronger, more definitive claims would significantly enhance the paper. For instance, identifying specific linguistic factors that influence when language-specific calibration is effective, or pinpointing consistent patterns under particular conditions, would add depth.

W2. The paper did not propose any method or framework to address the observed limitations from their empirical experiments. This gives the work a preliminary feel, as it primarily presents observations without actionable solutions. Introducing even a preliminary solution could have increased the practical impact of the findings, bridging the gap from exploratory analysis to offering actionable guidance for pruning multilingual models.

How about a systematic approach to language selection for calibration or a metric-based framework to guide pruning objectives could significantly elevate the paper’s contributions? For instance, defining an optimal selection strategy for calibration languages or samples, tailored to different model objectives (such as maximizing language-specific vs. language-agnostic features), would provide some practical value. Alternatively, developing a metric to assess the "quality" or effectiveness of pruning based on targeted goals (like preserving language modeling capability versus general reasoning) would offer structured guidance. Such methods could help refine pruning approaches for Wanda/SparseGPT in multilingual models, providing a roadmap for choosing calibration data and pruning techniques that align with specific goals.

### Questions
Aside from the issues raised in the weaknesses, I noticed some typos, and the tables presented are challenging to interpret. Here are some suggestions:
- In Section 4.1, the method for reading the table is not immediately explained. I only found instructions on interpretation in Section 4.2 (first paragraph), where it describes comparing entries "column-wise" based on evaluation languages, which are the "column headers". It would be helpful to mention this earlier to improve readability.
- Since much of the analysis compares the best and worst performances, how about highlighting only the most relevant entries in the main paper tables? For example, if most analyses are focused only on the best entry in each column, highlighting only these would guide readers instead of reading all different colors. The heatmap presentation could be moved to the Appendix for readers who want broader information.
- In Figure 1, the labels "Fig (b)" and "Fig (c)" appear to be intended as "Fig (a)" and "Fig (b)," respectively. Also, explicitly indicating which part is Fig (a) and Fig (b) would enhance clarity.
- Similarly, when discussing Figures 2 and 3, how about using alphabetical identifiers (e.g., (a), (b), (c), etc.) as in Figure 1? Referring to parts of the figures by identifiers rather than phrases like "left-most," "bottom-right," or "left side" would reduce potential ambiguity.

Additionally, regarding multi-language calibration, how were the calibration samples allocated? Was the sample size $128 * \text{the number of languages}$? Also, what sampling strategy was used, and were other sampling strategies considered?

### Soundness
3

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
This paper presents an empirical study on calibrating the pruning of multi-lingual language models. Different settings are investigated, which includes a comparison of languages, tasks, pruning techniques and models. The findings show that calibration in the target language for post-training pruning is beneficial for retaining the language modelling capability. However, it does not necessarily benefit downstream tasks. An analysis of the preservation of language-specific and language-agnostic features is conducted through latent subspaces and pruning masks.

### Strengths
- This paper addresses an important problem of language-specific calibration for pruning multilingual LLMs. To my knowledge, this hasn't been investigated in sufficient detail before.
- The experiments are thorough and cover different dimensions of the calibration problem on standard multilingual tasks (MKQA, MMLU).
- The paper is well-written and the results are presented clearly. 
- The findings are significant, as they offer useful guidelines to practitioners for the selection of calibration data for post-training pruning to achieve better performance.

### Weaknesses
 - The observation that performance patterns in smaller models do not consistently translate to larger models (e.g., Llama-3 70B and Aya-23 35B) suggests the presence of additional unexplored factors. Since pruning is potentially more useful in reducing the size of larger models and allows them to be used in resource-constrained environments, further analysis regarding this point would be important for the overall completeness of this study.

- Minor issues:
    - The question on 275-277 can be restructured for clarity.
    - Minor typo (line 346): poist -> posit

### Questions
- How does changing the number of inputs in the calibration set (which is 128 currently) affect the values in Table 1? Can we expect better performance as the calibration examples increase?
- Presenting a few qualitative examples (in the appendix) for the finding that 'pruning impairs the reasoning capability' would help understand the problem more clearly.
- Section 4.5 states that the performance patterns from the smaller models do not consistently hold true on their bigger counterparts. Can the authors hypothesize what additional factors might be contributing to this difference in performance on the bigger models?

### Soundness
4

### Presentation
4

### Contribution
4
