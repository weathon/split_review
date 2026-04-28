# #InsTag: Instruction Tagging for Analyzing Supervised Fine-tuning of Large Language Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Foundation language models obtain the instruction-following ability through supervised fine-tuning (SFT).
Diversity and complexity are considered critical factors of a successful SFT dataset, while their definitions remain obscure and lack quantitative analyses.
In this work, we propose \modelname, an open-set fine-grained tagger, to tag samples within SFT datasets based on semantics and intentions and define instruction diversity and complexity regarding tags.
We obtain 6.6K tags to describe comprehensive user queries.
We analyze popular open-sourced SFT datasets and find that the model ability grows with more diverse and complex data.
Based on this observation, we propose a data selector based on \modelname to select 6K diverse and complex samples from open-source datasets and fine-tune models on \modelname-selected data.
The resulting models, \lmname, outperform open-source models based on considerably larger SFT data evaluated by \textsc{MT-Bench}, echoing the importance of query diversity and complexity.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents InsTag, a method to quantify and select/prune sft dataset from a large dataset pool. The authors propose to utilize ChatGPT to tag the intent/topic of the data samples, and use the number of tags to represent complexity and tag coverage for diversity. These metrics are simple from both concept and practice perspectives. The authors give interesting analysis of existing datasets by adopting these two metrics. In the experiments, InsTag automatically selects 6K sft examples and the resulting model achieves comparable performance to WizardLM and Vicuna that are trained on 10x more data examples.

### Strengths
1. The proposed data measurement and data selection methods are simple, both concept-wise and practice-wise. 
2. The experimental results are strong – TagLM is the only model that achieves such high performance on MT-bench with <10K data examples as far as I know.  
3. The proposed approach can be utilized to measure existing datasets, as shown in Figure 2 which are interesting.  
4. Table 4 indicates that more sft data does not necessarily give better performance and InsTag is able to select the effective ones.

### Weaknesses
1. Evaluation is a bit weak, MT-Bench scores are the only metric used across entire paper – other datasets such as AlpacaEval and human evaluation could further strengthen the claims in the paper.  It would be beneficial to see how the model performs on a wider range of tasks, including those that test different aspects of language understanding and generation. For example, evaluations on datasets focusing on reasoning, common sense, or factual knowledge could reveal potential limitations of the proposed approach. The lack of these evaluations makes it difficult to assess the generalizability of the findings.
2. While I appreciate that the authors distill a local tagger in Section 5, it is unknown how much SFT performance would be sacrificed by using the tags from this local tagger. The strong results on Table 3 is from ChatGPT tagger if I understand correctly, and it may be too expensive to use ChatGPT in practice when we have a large data pool to measure. The paper does not provide sufficient detail on the local tagger's architecture, training process, or performance compared to the ChatGPT tagger. This makes it difficult to assess the practical implications of using the local tagger in real-world scenarios. Specifically, it would be helpful to know the precision and recall of the local tagger, and how these metrics correlate with the final SFT performance.

### Questions
NA

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the diversity and complexity of supervised data in the alignment process of large language models. It proposes InsTag, an open-set instruction tagging method, which can conveniently evaluate the diversity and complexity of human instructions. Based on this, the authors design a method of selecting human instructions, which can make the model achieve better performance with less supervised training data.

### Strengths
1. This paper proposes an automatic method to evaluate the diversity and complexity of human instructions. 
2. Based on the proposed InsTag, this paper further presents a method of selecting human instructions, which can potentially reduce the cost of the alignment phase of large language models.

### Weaknesses
 1. Selecting more diverse and complex samples is an existing idea, and this article is more similar to the implementation and application of this idea.
2. The definition of complexity seems a little strange. Is there any explanation from other papers? If not, I hope the authors can give a more detailed explanation for it.
3. The author is recommended to verify the performance of the proposed method on more benchmarks.

### Questions
The description of InsTagger in Section 5 seems too brief. Can you provide more detailed explanations, such as why it was designed and further influences.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study illustrates how GPT-4's open-ended topic tagging capability can be instrumental in quantitatively assessing the diversity and complexity of various Instruction Fine-Tuning (IFT) datasets. 
Specifically, the complexity of an IFT dataset is gauged by the average number of tags per data point, while its diversity is measured by the proportion of unique tags in the dataset relative to the total number of tags recognized by GPT-4. 
Utilizing these novel quantitative metrics, the researchers compared distinct IFT datasets to discern their unique features. 
The research further suggests that employing these metrics to filter data can enhance the effectiveness of instruction fine-tuning.
Experimental results in the paper demonstrate the importance of enhancing the diversity and complexity of data points when tuning language models to align with human instructions.

### Strengths
- The proposed method is straightforward, intuitive, and simple to implement.
- The study demonstrates that metrics driven by the statistical analysis of automatically generated tags—specifically complexity and diversity—can effectively probe the characteristics of IFT datasets.
- This work provides further empirical evidence that the quality, rather than the quantity, of IFT datasets is crucial for aligning language models successfully.

### Weaknesses
 - The primary mechanism of the proposed method is dependent on the automated, open-ended tagging capability of GPT-4; therefore, there is a risk that the analysis in this paper might be influenced by any inherent biases present within GPT-4. Specifically, the reliance on a single model for tagging introduces a potential single point of failure and limits the robustness of the analysis. The tags generated by GPT-4 might not be universally applicable or might reflect specific biases in its training data, which could skew the diversity and complexity metrics.
- Further examination of data instances categorized by the proposed metrics would be advantageous. Specifically, exploring the semantic or syntactic traits defining IFT datasets identified as diverse and complex by these metrics would be informative. It is unclear what specific textual features correlate with high or low complexity and diversity scores. A deeper analysis of the linguistic characteristics of the tagged data is needed to validate the proposed metrics.
- The presented work is largely empirical, which may raise concerns within the community regarding the foundational grounding of its results. The absence of a theoretical framework to explain why the proposed metrics correlate with instruction fine-tuning effectiveness makes it difficult to generalize the findings beyond the specific datasets used in the study.

### Questions
- The proposed method appears to be sufficiently versatile to extend beyond instruction fine-tuning applications. Could you provide additional examples where the efficacy of this method could be demonstrated?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a method for automatically tagging instruction data with labels based on query intent, using ChatGPT to generate queries and applying various rules to normalize and aggregate related tags together. The authors analyse existing datasets using the tagging method, finding that a higher average number of tags, and higher diversity correlate with good performance, matching prior work examining instruction datasets. They then use the tags as a data selection method (maximising complexity and diversity based on the tags), and find they can train a strong model with as few as 6,000 examples. Finally, they ablate their data selection method and find that increasing diversity and complexity improves performance, while increasing dataset size only improves performance up to a point (around 6,000 examples).

### Strengths
- The tagging method is interesting, and well-validated both as an analysis and as a selection method. The use of ChatGPT as a tagger, and the rules used to simplify the generated tags, are novel and effective.
- The data selection method appears well-validated, and achieving strong results with only 6,000 examples is impressive. The method outperforms a random selection baseline and other popular open models such as Vicuna and WizardLM.
- The analyses of performance against complexity, diversity, and dataset size are useful, providing useful guidelines for future researchers in data collection and selection.

### Weaknesses
 - The method’s reliance on a strong tagging model (in this case, ChatGPT) is not explored, despite a very brief mention of training a distilled tagger model at the end of the work. It would be interesting and useful to see how well this method works with openly available models, or over a variety of different quality models (e.g. how does using GPT-4 as a tagger compare? How about Vicuna? etc.). Specifically, the impact of tag quality on the final model performance should be investigated, as noisy or inaccurate tags could lead to suboptimal data selection. The paper should explore the trade-offs between tagger model size, computational cost, and the final model's performance.
- The tag-based analysis is somewhat restrictive, as discussed in section 4.3. It would be interesting to take the semantics of the tags themselves into account somehow, since (a) some tags may be closer to each other and so overlap in terms of diversity, and (b) certain tags may express queries that are naturally more complex than others (e.g. ‘solve’ vs ‘inquiry’ tags). The current diversity metric treats all tags as equally distinct, which may not accurately reflect the underlying semantic relationships between them. Furthermore, the complexity metric, based solely on the number of tags, may not capture the true complexity of an instruction, as some tags may inherently represent more complex tasks than others. For example, a single tag like 'multi-hop reasoning' might indicate higher complexity than several tags related to simple information retrieval.
- MT-bench evaluation involves a relatively small number of questions (80), which may be easier to cover with 6,000 examples. I wonder how well the TagLM model would perform with more questions (e.g. the alpacaEval setting, which has 800 examples), or on more traditional benchmarks such as MMLU, Big Bench, etc. In general, it would be interesting to see if the selection method is biased towards certain capabilities compared to others. The evaluation should be expanded to include a more diverse set of benchmarks to assess the generalizability of the proposed method. The current evaluation may not fully capture the model's performance across various tasks and domains.

### Questions
- Does the average number of tags per instance correlate well with human intuitions of complexity? 
- How well does your distilled tagger perform if used as a tagger for data selection? Did you test with different models?
- How does TagLM perform over other benchmarks (e.g. MMLU, HumanEval)? Are there any particular capabilities or skills it seems to underperform in compared to baselines?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
