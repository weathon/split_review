# Integrating Planning into Single-Turn Long-Form Text Generation

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 8, 3, 5

## Abstract
Generating high-quality, in-depth textual documents, such as academic papers, news articles, Wikipedia entries, and books, remains a significant challenge for Large Language Models (LLMs). 
In this paper, we propose to use planning to generate long form content.  To achieve our goal, we generate intermediate steps via an auxiliary task that teaches the LLM to plan, reason and structure before generating the final text.  Our main novelty lies in a single auxiliary task that does not require multiple rounds of prompting or planning.
To overcome the scarcity of training data for these intermediate steps, we leverage LLMs to generate synthetic intermediate writing data such as outlines, key information and summaries from existing full articles. 
Our experiments demonstrate on two datasets from different domains, namely the scientific news dataset~\textit{SciNews} and Wikipedia datasets in~\textit{KILT-Wiki} and~\textit{FreshWiki}, that LLMs fine-tuned with the auxiliary task generate higher quality documents.  We observed +2.5\% improvement in ROUGE-Lsum, and a strong 3.60 overall win/loss ratio via human SxS evaluation, with clear wins in organization, relevance, and verifiability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents an approach to integrate planning into single-turn long-form text generation using Large Language Models (LLMs). The authors propose generating intermediate steps through an auxiliary task that teaches LLMs to plan, reason, and structure content before final text generation. To address the scarcity of training data for intermediate steps, the authors leverage LLMs to create synthetic intermediate writing data from existing full articles. Experiments on the SciNews and Wikipedia datasets demonstrate that fine-tuning LLMs with this auxiliary task results in higher quality documents, with improvements in ROUGE scores and human evaluation metrics.

### Strengths
The authors have validated the effectiveness of their method through both automated metrics and human evaluation, showcasing the method's practical utility.

### Weaknesses
1. There is significant room for improvement in the writing style and structure of the paper. For example, Sections 4.1, 4.2, and 5.1 are overly verbose and could benefit from a more concise presentation, with implementation details potentially moved to the appendix. The organization of the paper is somewhat disjointed, failing to highlight key points effectively. For instance, the second task introduced in section 4.3 is mentioned as ineffective in the experiments (Table 2); thus, its inclusion in the methodology section seems unnecessary.
2. The methodology lacks novelty. The experiments are limited in scope and content, especially considering the paper could benefit from a more streamlined language.

### Questions
1. I am curious about the impact of this training method on the model's performance in generating short texts.
2. If we directly guide the model to first generate intermediate steps and then the full article, how does its effectiveness compare to the FT w/ I, Output w/ I method? Is the reasoning time roughly the same for both? For broader application, I believe the former might be better; however, considering efficiency, FT w/ I could be more suitable.
3. What is the difference between the loss calculated for the second task mentioned in section 4.3 and the first task in terms of the $y_i$ part?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes to fine-tune LLMs to generate long-form content directly in a single pass through a pre-writing auxiliary task that teaches the LLM to plan, reason and structure. They leverage Gemini Ultra to generate the training data for this auxiliary task, namely generating synthetic summaries, outlines and key informations from full articles. Three training paradigms are used to fine-tune the model. To mitigate the possible hallucinations when generating synthetic data, they have a sinusoidal scoring function to assess the adherence to length and structure, and a hallucination model for coherence between the synthetic data and original article. Improvements are shown in Rouge-LSUM, and 3.6 win/loss ratio in organization, relevance and verifiability.

### Strengths
- Very well-written paper! The proposed method is explained in a clear way, with the difference of other objectives (generating in multiple turns) distinguished.
- The proposed method’s intermediate steps are all in scope, and all intuitively should help with full document generation. They also try to mitigate hallucinations by using a score function of coherence and completeness to choose the highest overall quality. As confirmed by both automatic metrics as well as human/LLM as judge metric, the method constantly performs better than the baseline.
- The ablation is relatively thorough. The authors compare against different evaluation/training paradigms, different mixture of training data, and single-turn / multi-turn inference.

### Weaknesses
 - For evaluation metrics, although human and auto SxS are used, only 50 articles are rated by human. Furthermore, the LLM that is used to generate the synthetic data is used as the rater. As suggests by some previous work (Panickssery et al. 2024), for example, LLM raters might be able to recognize and favor their own generations. Therefore, there are chances that the model that is trained on additional Gemini Ultra generated data might be favored more than zero-shot.
- Length impact — it seems that for SciNews, the news report is 694 tokens, but the LLM is allowed to generate no more than 4k tokens, and for Wikipedia dataset, FreshWiki’s length is less than 3k words, and the LLM is allowed to generate no more than 6k tokens. Although there is no comparison against the groundtruth documents, is it possible that some method generates more/less tokens and thus is favored by either Rouge scores or SxS raters?
- The paper only tested the Gemini family models.

### Questions
- Although it might not impact the baseline comparison because there are no comparison against groundtruth data, for Wikipedia dataset, is there any possible data contamination?
- What does multi-turn inference mean in line 432? Is it prompt LLM to generate each intermediate first then generate the full document?
- Why is the coherence & organization for Wikipedia models win ratio bad? Is it because more hallucinations appears? Does this mean that the hallucination mitigation is less effective on Wikipedia data?

### Soundness
3

### Presentation
4

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
In this paper, the authors propose integrating planning into single-turn long-form text generation using Large Language Models (LLMs). The approach involves an auxiliary task, generating intermediate steps, to enhance coherence and structure in the finally generated text. The authors construct training data by leveraging LLMs to generate synthetic intermediate writing data based on the full articles. Experiments demonstrate improved quality and coherence in long-form documents generated by LLMs fine-tuned with this method.

### Strengths
Pros:
* The paper is well-written and easy to follow.
* The construction of the training data is automatic, leveraging off-the-shelf LLMs to generate synthetic intermediate writing data based on the full articles, which saves the expensive cost of manual annotation. 
* With the auxiliary task at training time, the model can learn to generate more coherent and structured long-form text in a single pass.

### Weaknesses
Cons:
* The paper lacks a comparison with previous work like ProGen (Tan et al., 2021), Ex$^3$ (Huang et al., 2024), etc. The invloved baseline training and prompt setups are too simple to demonstrate the superiority of the proposed approach. Specifically, the absence of a comparison with multi-stage approaches like ProGen [1] is a significant oversight, as it is not clear if the single-turn approach offers a genuine advantage over a carefully optimized multi-stage pipeline. The baseline model's performance should be more thoroughly investigated, including ablations on different prompt strategies and training configurations.
* Besides the cohenrence and structure, the approach in this paper appears to be more efficient and faster than the previous work. The paper lacks metrics to measure the efficiency and speed of the proposed approach compared to previous work. The paper should include metrics such as inference time, training time, and memory usage to support claims of efficiency. A comparison of these metrics against existing methods would be essential to validate the practical benefits of the proposed approach.
* The offline metrics used in the paper are not sufficient to evaluate the *cohenrence* and *structure* of the generated text. While ROUGE scores provide a basic measure of lexical overlap, they are inadequate for assessing the higher-level qualities of coherence and structure. Human evaluations are a step in the right direction, but the paper should also consider more robust automated metrics that are designed to capture these aspects, such as discourse-level metrics or metrics based on semantic similarity and logical flow.

### Questions
1. In line 38-40, the author mentioned that the proposed approach enables us to fully leverage the token-level attention mechanism in the decoding process. How does the token-level attention mechanism is fully used in the decoding process? How does it ensure the coherence and consistency of the generated document? These are not clear to me.
2. Compared to the previous work involving multi-turn generation passes, does the proposed approach have any advantages in terms of the length of the generated text? Can the proposed approach generate longer and better text than the previous work?

### Soundness
2

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
This paper proposes a training approach that enhances long-form writing capabilities in LLMs by incorporating pre-writing stages through auxiliary training tasks. In addition to the conventional end-to-end training for direct output generation, the approach includes two intermediate tasks: generating an outline from the input and creating a complete article based on both the input and outline. The model is trained using a mixture of these tasks. During inference, the model can either generate a full article directly or follow the intermediate steps before producing the final output. The method is evaluated on the SciNews and Wikipedia datasets, with both automated metrics (ROUGE and LLM evaluations) and human assessments demonstrating that LLMs fine-tuned with these auxiliary tasks deliver improved outputs.

### Strengths
- This paper studies an important task of long-form text generation. Incorporating auxiliary tasks to improve long-form writing performance is interesting;
- Both automatic and human evaluations on two datasets prove the effectiveness of the method;
- The analysis, particularly the findings in Table 2, is interesting and may offer insights to future research.

### Weaknesses
 - The proposed approach is similar to [1], which also employs multitask training for long-form generation. Clarifying the distinctions between the two methods would enhance the paper;
- Only one LLM (Gemini) is used in the experiments. Including recent open-source LLMs, such as LLAMA3, would strengthen the results' validity, especially as fine-tuning smaller LLMs is often more feasible in practical applications;
- Evaluation is another concern. ROUGE primarily measures word overlap; including more advanced metrics, such as BERTScore, would provide a deeper assessment. Additionally, LLM-based evaluations currently focus on overall quality, lacking fine-grained aspects. Faithfulness and factuality are also absent;
- Sample outputs and error analysis are not provided, which limits understanding of common issues and qualitative insights.

### Questions
- Is there an analysis of output length across different generation methods?
- Has the quality of the generated outlines been evaluated?
- For human evaluations, what is the inter-annotator agreement score?

### Soundness
3

### Presentation
3

### Contribution
2
