# Sufficient Context: A New Lens on Retrieval Augmented Generation Systems

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 3, 8

## Abstract
Augmenting LLMs with context leads to improved performance across many applications. Despite much research on Retrieval Augmented Generation (RAG) systems, an open question is whether errors arise because LLMs fail to utilize the context from retrieval or the context itself is insufficient to answer the query. To shed light on this, we develop a new notion of sufficient context, along with a way to classify instances that have enough information to answer the query. We then use sufficient context to analyze several models and datasets. By stratifying errors based on context sufficiency, we find that proprietary LLMs (Gemini, GPT, Claude) excel at answering queries when the context is sufficient, but often output incorrect answers instead of abstaining when the context is not. On the other hand, open-source LLMs (Llama, Mistral, Gemma) hallucinate or abstain often, even with sufficient context. We further categorize cases when the context is useful, and improves accuracy, even though it does not fully answer the query and the model errs without the context. Building on our findings, we explore ways to reduce hallucinations in RAG systems, including a new selective generation method that leverages sufficient context information for guided abstention. Our method improves the fraction of correct answers among times where the model responds by 2--10\% for Gemini, GPT, and Gemma.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work analyzes how LLM behavior differs for question answering with and without sufficient context. A context C is considered sufficient to answer a question Q if it supports an answer A in C. The authors make it a point to ensure that the ground truth answer does not matter in the definition of sufficient context.

First, the authors collect an evaluation set of 115 (question, context, answer) triplets (from 3 QA datasets) and annotate them for sufficiency. A set of autoraters is evaluated on the task of judging sufficiency. Gemini 1.5 Pro (1-shot) achieves an F1 score of 93% on evaluating sufficiency. For the rest of the analysis, Gemini 1.5 Pro (1-shot) labels examples as having sufficient/insufficient context.

Next, the paper analyzes how context sufficiency differs for different QA datasets. (Question, context) triples are collected for 3 popular QA datasets: FreshQA, HotpotQA, and Musique. Contexts are either gold snippets from the dataset (for Musique) or retrieved with a dense retriever. Results show that sufficiency does not increase significantly after the first 6000 tokens of context. FreshQA has the most sufficient per query while the context is sufficient for only about 45% of the questions from Musique and HotPotQA.

Next, the paper analyzes how context sufficiency affects the accuracy of Retrieval Augmented Generation systems. They study the behavior of 4 API-based QA models.
1. The accuracy of QA models is higher when given sufficient context than without. However, even without sufficient context, the models answer the query about 35% of the time.
2. When given sufficient context, models have a low abstention rate and relatively higher error rate.
3. When given insufficient context, the abstention and hallucination (error) rates both increase.

The authors show a qualitative breakdown of the questions the QA models answer correctly with insufficient context.

Finally, the paper studies ways to use the "context sufficiency predictor" for a well-calibrated QA model. The sufficiency predictor can be used as a signal for selective prediction. This provides some gains over using just the self-reported model confidence especially with a worse QA model. Fine-tuning the QA models to abstain (either on random contexts or contexts predicted to be insufficient) improves the ability to abstain but does not improve overall QA accuracy.

---

Scores changed from 8 -> 6. See reasoning [here](https://openreview.net/forum?id=Jjr2Odj8DJ&noteId=fVAH86Vrwz) and [here](https://openreview.net/forum?id=Jjr2Odj8DJ&noteId=a0bQQDrq6s).

--- 

Final Update After Rebuttal
---

I'm satisfied with the author responses. I am changing my score back to 8. Ideally, this comes with the caveat: I think the core argument of the paper and findings have value, but I believe that the final version of the paper needs detailed discussions based on the author-reviewer discussion.
- Clear discussions of the different QA benchmarks and their impact. This will address issues of why different findings are not directly comparable and the nuances of why certain QA datasets behave differently.
- The final version of the paper should include a **quantitative count** of the different ways the QA models are correct given insufficient context. This would also better answer questions about automated metric reliability (rather than anecdotal evidence)

### Strengths
- The presentation of the paper is clear and easy to follow.
- Appropriate evaluations are used at each stage. The sufficiency predictor is first evaluated and then used for later analysis.
- The paper reports findings of unexpected model behavior with and without sufficient context, which are valuable to the community.
    - It is interesting that Gemini 1.5 Pro does not abstain very often even on passages that Gemini 1.5 Pro has labeled has having insufficient evidence (as autorater)

### Weaknesses
1. Some details in the paper are vague. While they don't obstruct understanding, they may obstruct reproducibility [see Questions]
2. While the paper spends a lot of time analyzing the case of correct answer with insufficient context, the opposite case of incorrect answer with sufficient context is equally interesting and warrants exploration
3. The qualitative evaluation does not attempt to quantify any of the error types. For example, how prevalent is the "Autorater error" [see Questions]

### Questions
1. The autorater is evaluated on single-hop QA datasets like PopQA, FreshQA, Natural Questions, and EntityQuestions. The rest of the paper analyzes QA performance on the FreshQA (in-domain) and potentially out-of-domain HotpotQA and Musique datasets. Can the automatic judgments be trusted out-of-domain?
2. Following up: since you observe rater error in Table 2, what is the estimated prevalence of this category?
3. One other potential mechanism of the correct answer given insufficient context is that there are only one/few entities of the expected type (given the question) in the context. Is this mechanism never observed?
4. What is the context source for FreshQA? Is it the labeled sources? If so, are there no examples of insufficient sources for FreshQA questions in the automated evaluation dataset?
5. Lines 185-190: Remark about ambiguous queries: It is unclear to me why the given example illustrates how ambiguous queries are handled. My understanding is that ambiguous queries have unclear interpretations, not the context.
6. Do you plan to release the sufficient context dataset? If not, how do you ensure the following: "very challenging, including single- and multi-hop questions, as well as adding highly related information in the context even if it is not sufficient"

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
This work asks why LLMs hallucinate when integrated into RAG systems. They carefully define "sufficient context", i.e. whether the retrieved context unambiguously supports some answer for a question, while making sure their definition is appropriate for various types of RAG systems, e.g. multi-hop reasoning. They then develop an "autorater" prompt for this quality, which they validate on a set of 115 hand-labeled and challenging data points. Using this autorater, they analyze the performance of an off-the-shelf retrieval system (REPLUG) across datasets and then analyze the performance of different LLMs in RAG, exploring their behavior (correct answers vs. abstaining vs. hallucination) when sufficient context is or isn't available. Overall, they find that models abstain less with RAG and hallucinate whether sufficient context is available or not. They build a small set of reasons answering questions correctly despite insufficient context, e.g. when it's due to models using parameteric knowledge when faced with incomplete multi-hop information. Leveraging their autorater, the authors explore a number of approaches for creating a tradeoff between tuning abstention, e.g. only answering when context is clearly sufficient and the system is confident in high-stakes applications, while relaxing that (to answer more questions) elsewhere.

### Strengths
1. The paper is well-written and easy to follow.
2. The analyses are genuinely insightful and offer a number of non-trivial findings, as included in my summary.
3. The autorater, its validation set, the analyses approach, and the method proposed for trading selectivity vs. coverage are all likely to be valuable resources for future work.

### Weaknesses
1. How sensitive is the analysis to the choice of REPLUG and/or E5 as retriever components? The paper glosses over the IR subsystem here in an extreme way. Most of this information is simply not presented. For example, I have to read the results in Figure 2 as essentially an evaluation of REPLUG, but they could also be read as (and appear to be presented as) analyses of the datasets themselves. Is REPLUG able to handle multi-hop queries? I am not aware that it's a multi-hop retriever at all, so the choices here, while still plausible, are lacking in justification.

2. How good is the autorater? The paper includes table 1 but to my knowledge does not directly refer to it; and overall, the paper doesn't seem to offer a convincing discussion of this, given how essential the autorater is to the analysis and methods. Will the 115 data points be released? There's some risk of circularity here. What makes large LLMs so prone to hallucination if one could trust that a simple prompt could reliably discover these cases?

3. Given that the autorater is not perfect, and given the subtle nature of its job (as discussed in the Remarks under the definition of Sufficient Context), how correlated are autorater mistakes with determinations of Correct/Hallucination in Figure 3?

### Questions
See Weaknesses.

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
3

### Summary
The paper studies the performance of LLMs with retrieval-augmented context. In particular, the paper analyses how often the retrieved context is sufficient for answering a question. It then analyses how the behaviour of LLMs changes depending on whether the retrieved context is sufficient or not, i.e. in how many cases the LLM hallucinates, abstains, or answers correctly. Furthermore, the paper shows that checking for sufficiency can be used to "teach" an LLM to abstain (either by directly using the sufficiency prediction in combination with LLM-generated confidence metrics, or by fine-tuning a model to abstain).

### Strengths
Retrieval-augmentation is a popular and promising method to improve the performance of LLMs. Previous work has shown, however, that there are issues with this approach, especially if the retrieved context is not helpful and/or too long. The analysis in the paper contributes to the study of these effects.

The paper is easy to follow and some of the experimental results may be useful to some practitioners.

### Weaknesses
As the paper acknowledges in the related work section, there is a substantial amount of work that has already analysed the performance of RAG systems in relation to the quality of the retrieved context. The paper claims to study this topic through "a new lens", but the specific aims of the paper are not really clear. What is it really that this paper shows that wasn't already known? Perhaps a more explicit formulation of hypotheses/research questions that have not yet been answered could help here. In its current form, the paper reads like a preliminary exploratory analysis of LLM performance, rather than a mature contribution that is ready for publication.

The notion of "sufficient context" is central to this paper, but it is not actually defined in a very precise way. First, the definition (line 157) is rather "circular": to determine if a context is sufficient, we need to determine if it allows us to infer the answer, but that actually depends on the capabilities of the LLM. The definition is also confusing, as it talks about "plausible answers" rather than the actual answer. I think what is meant is that a context can be sufficient even if the answer it contains is incorrect. In any case, this point needs a lot more discussion. There are further issues, for instance, the definition assumes that an answer can be inferred up to 4 inference hops. Why 4? 

To assess which contexts are sufficient, the paper relies on LLM-generated assessments. This is a key limitation, and the current analysis should be expanded with a human-annotated experiment. Indeed, currently, the paper does not actually study the impact of contexts being sufficient, but rather the impact of an LLM thinking that the context is sufficient. Even if the LLM that predicts sufficiency is different from the one used for generating the answer, this kind of dependency on LLMs may clearly affect the results.

There are lots of minor issues with the writing and with formulations being imprecise.

* The abstract contrasts the behaviour of closed models with open-source ones. But isn't the contrast rather between larger and smaller models?
* The example in Remark 2 is of an ambiguous context rather than an ambiguous query.
* The example in Remark 3 is of an ambiguous query rather than an ambiguous context
* Lines 225-228: where are these results shown?
* Table 2: I believe the explanation on the first row should be "some chance" and the explanation on the second row should be "50% chance"
* Line 384: sufficient -> insufficient

### Questions
What can we really conclude without manual validation of the auto-rater predictions?

Is the difference between context sufficiency and NLI based methods really that significant (for practical purposes)?

What are the key insights that your analysis has revealed that weren't known from previous work?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel framework for understanding context sufficiency in Retrieval-Augmented Generation (RAG) systems, where retrieval of external context aims to improve Large Language Model (LLM) accuracy and reliability. The authors define “sufficient context” as context providing enough information for a model to answer a query without additional details. They introduce a sufficient context autorater to classify instances based on this metric, allowing for systematic error analysis across several proprietary and open-source LLMs. Key findings suggest that proprietary models (e.g., Gemini, GPT) often generate incorrect answers without abstaining when context is insufficient, while open-source models are more likely to hallucinate or abstain even when context suffices. The authors propose a selective generation technique to reduce hallucinations by leveraging sufficient context signals, showing improvements of up to 10% in response accuracy among Gemini, GPT, and Gemma.

### Strengths
1. Novelty of Sufficient Context Concept: The paper addresses a fundamental gap in RAG literature by formalizing the concept of “sufficient context.” This is essential for evaluating how well LLMs make use of retrieved information, especially when distinguishing between sufficiency and insufficiency.

2. Methodology and Rigorous Analysis: By creating a sufficient context autorater and testing it across proprietary and open-source models, the paper presents a solid empirical foundation. The detailed experiments on multi-hop and open-book QA datasets (e.g., Musique-Ans, HotPotQA, FreshQA) are impressive, particularly in showing how context sufficiency affects model performance.

3. Impact on Hallucination Mitigation: The proposed selective generation framework that combines sufficient context labels with model confidence offers a practical approach to reduce hallucinations. This approach is adaptable across different LLM architectures, which is an important contribution for model deployment.

4. Evaluation Metrics and Generalization: The paper extensively evaluates its autorater and selective generation framework across various datasets and models, which provides strong evidence of generalizability. The careful selection of open and proprietary models, and focus on multi-hop reasoning tasks, enhance the robustness of the conclusions.

### Weaknesses
1. Clarification on the Autorater’s Design and Reliability: The paper could better explain the autorater’s design, particularly regarding criteria used in challenging multi-hop contexts. Additional qualitative examples could help clarify how the autorater discerns sufficiency, especially when dealing with ambiguous or incomplete context.

2. Limitations in Practical Deployment: While the selective generation framework demonstrates significant accuracy improvements, there is limited discussion on computational overhead. For example, implementing a selective generation method based on sufficient context may require high processing power for real-time applications, particularly with large models and datasets.

3. Impact of Retrieval Quality: Although the paper acknowledges that retrieval quality can affect context sufficiency, the experiments do not address how different retrieval strategies impact results. Comparing RAG performance using advanced retrieval techniques, like iterative or corrective retrieval, would strengthen the argument that improving sufficiency is an independent aspect of model improvement.

4. Scope Beyond QA Tasks: The paper focuses on QA, but RAG systems are used across various tasks, including summarization, which the authors briefly mention. A future direction could involve validating sufficient context’s relevance to other NLP tasks, which would enhance the paper’s broader applicability.

5. Explain Model-Specific Findings in More Detail: The differential behavior of models, such as Gemini’s reduced abstention rate and GPT’s lower accuracy without RAG, would benefit from additional discussion. These findings highlight variations in model handling of retrieval, and more insight here could guide further model-specific improvements.

6. Consideration of Confidence Thresholds: The selective generation approach could further explore confidence thresholds to find an optimal balance between abstention and accuracy. Including ablation studies or sensitivity analyses on confidence levels would make this method more practical for different application contexts.

### Questions
1. How is "sufficient context" defined for multi-hop reasoning?
Clarify the specific criteria or thresholds the autorater uses, especially for complex multi-hop queries.

2. How does the autorater handle ambiguous or conflicting contexts?
What rules are applied when contexts contain contradictory or unclear information?

3. How does retrieval quality impact context sufficiency and model performance?
Could improved retrieval reduce hallucination rates by providing more sufficient contexts?

4. What are the computational demands of the selective generation framework?
Is it feasible for real-time applications, particularly with large models?

5. Is the sufficient context framework applicable beyond QA?
Could this framework be useful for other retrieval-augmented tasks, like summarization?

### Soundness
3

### Presentation
3

### Contribution
3
