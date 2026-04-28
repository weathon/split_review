# FactBench: A Dynamic Benchmark for In-the-Wild Language Model Factuality Evaluation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Language models (LMs) are widely used by an increasing number of users, underscoring the challenge of maintaining \farima{factuality} across a broad range of topics. We first present \system (\textbf{V}erification and \textbf{E}vidence \textbf{R}etr\textbf{I}eval for \textbf{F}actualit\textbf{Y} evaluation), a pipeline to evaluate LMs' \farima{factuality} in real-world user interactions. 
\system considers the verifiability of LM-generated content and categorizes content units as \texttt{supported}, \texttt{unsupported}, or \texttt{undecidable} based on the retrieved evidence from the Web.
Importantly, factuality judgment by \system correlates better with human evaluations than existing methods. 
Using \system, we identify ``hallucination prompts'' across diverse topics, i.e., those eliciting the highest rates of \farima{incorrect and inconclusive} LM responses. These prompts form \dataset, a dataset of \farima{1K} prompts across \farima{150} fine-grained topics. Our dataset captures emerging factuality challenges in real-world LM interactions and can be regularly updated with new prompts. 
We benchmark widely-used LMs from GPT, Gemini, and Llama3.1 family on \dataset, yielding the following key findings: 
\textbf{(i)} Proprietary models exhibit better factuality, \farima{with performance declining} from \texttt{Easy} to \texttt{Hard} hallucination prompts. 
\textbf{(ii)} Llama3.1-405B-Instruct shows comparable or lower factual accuracy than Llama3.1-70B-Instruct across all evaluation methods due to its higher subjectivity that leads to more \farima{content labeled as} \texttt{undecidable}.
\textbf{(iii)} Gemini1.5-Pro shows a significantly higher refusal rate, with over-refusal in 25\% of cases.
\farima{Our code and data are publicly available at \href{https://huggingface.co/spaces/launch/factbench}{https://huggingface.co/spaces/launch/factbench}.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents FACTBENCH, a dynamic benchmark dataset for evaluating the factuality of language model (LM) responses in real-world user interactions. The authors introduce a two-step process to curate the benchmark: (1) collecting verifiable and useful prompts from an in-the-wild LM conversation dataset, and (2) using VERIFY, a factuality evaluation pipeline, to measure the appropriateness of these prompts based on whether they elicit unfactual responses from strong LMs. The resulting FACTBENCH contains 985 hallucination prompts across 213 topics. The authors also benchmark several widely-used LMs on FACTBENCH and find that proprietary models exhibit better factuality than open-weight models, and VERIFY achieves the highest correlation with human judgments compared to other factuality evaluation methods.

### Strengths
1. FACTBENCH is a novel dynamic benchmark that captures evolving factuality challenges in real-world LM interactions, addressing the limitations of existing static benchmarks.

2. VERIFY, the factuality evaluation pipeline, considers the verifiability of generated content and introduces an "undecidable" label for ambiguous cases, providing a more robust framework for assessing factuality.

3. The authors release human-annotated factuality data on 5,519 content units, which can serve as a valuable resource for future research on factuality evaluation.

### Weaknesses
1. The usefulness evaluation criteria and scoring process are not well-justified. More details are needed on how these criteria were determined and how the scores from two LMs were combined.

2. The VERIFY pipeline uses a single LM (Llama3-70B-Instruct) for key tasks such as unit extraction, labeling, and decontextualization. The potential bias introduced by relying on a single model is not adequately addressed.

3. The evaluation of FACTBENCH is limited to a small set of LMs. A more comprehensive evaluation involving a wider range of models would strengthen the paper's claims.

4. The weighting factor α in the Hallucination Score is set to 0.5 without much explanation. A sensitivity analysis or ablation study on this hyperparameter would be informative.

### Questions
N/A

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
3

### Summary
The authors propose FACTBENCH, a dynamic benchmark for evaluating language model factuality in real-world scenarios by using prompts that often provoke hallucinations. They also present VERIFY, a pipeline that assesses factuality by categorizing responses as supported, unsupported, or undecidable, based on retrieved web evidence. The experiments show that VERIFY can achieve the highest correlation with human judgments.

### Strengths
1.	This study addresses a growing concern in the factuality of LM-generated content, especially in the context of hallucinations. 
2.	FACTBENCH is an innovative, dynamic benchmark that adapts to new factuality challenges. And VERIFY is an innovative factuality evaluation approach that achieves more precise, human-aligned assessments. 
3.	Extensive experiments across multiple models show that VERIFY aligns closely with human judgments.

### Weaknesses
1.	Only three speakers were hired for annotation, with relatively low inter-annotator agreement (Cohen’s Kappa scores of 0.52 and 0.55). The difference in factuality labeling between VERIFY and Factcheck-GPT is minor in Table 2 (≤ 0.01 for Factual labels), and VERIFY's performance is noticeably lower in Tables 1 and 3, suggesting potential limitations in annotation reliability and robustness.
2.	While FACTBENCH is described as dynamic, the paper lacks specifics on its update process, such as the conditions under which prompts are added or removed, the frequency of updates, and criteria for integrating new prompts.
3.	The paper provides limited discussion on key hyperparameters, such as α used in the hallucination score and the number of evidence retrieval rounds in VERIFY.

### Questions
1.	What factors influenced the decision to categorize prompts into three tiers?
2.	Why was a topic model-based approach (BERTopic) chosen over a general clustering method? Given that BERTopic parameters can affect clustering quality, how were these parameters tuned, and might they influence the final benchmark results? 
3.  See the weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces FactBench, a dynamic benchmark designed to evaluate the factual accuracy of large language models (LMs) in real-world contexts. FactBench continuously updates its dataset of prompts to capture scenarios where LMs are likely to generate hallucinations, addressing the limitations of existing static benchmarks. Additionally, the VERIFY framework is presented as a factuality assessment pipeline that categorizes LM responses based on evidence-supported verification categories, demonstrating higher alignment with human evaluations.

### Strengths
● The paper proposes a benchmark across multiple topics with varying difficulty levels.
● It offers an interesting categorization of hallucinations, distinguishing between context-independent and context-dependent statements, which could facilitate finer-grained hallucination detection in future studies.
● A new weighting factor is introduced to account for unsupported and undecidable units, adding robustness to hallucination scoring.
● The VERIFY framework shows good alignment with human judgment, particularly in handling nuanced cases.

### Weaknesses
● The experimental design could be improved; using VERIFY to classify data and then evaluate it may introduce circularity in the results.
● The VERIFY method lacks innovation in hallucination detection, particularly in terms of recall, which is essential in high-stakes fields like medical and encyclopedic contexts where hallucinations must be minimized.
● Difficulty ratings for prompts based solely on scores from multiple large models are unconvincing; a broader and more comprehensive classification method is needed.

### Questions
● Could you explain in detail how Llama3-70B was used to determine whether the data was verifiable?
● Why did you choose 0.5 as the weighting factor for the hallucination score? Might this choice impact the correlation of VERIFY with human preferences?

Comments:

Overall, this paper makes meaningful contributions to the development of factuality evaluation methods for LMs, particularly in establishing a dynamic benchmark that could adapt to future model advancements. However, improvements in experimental design, verification transparency, and difficulty categorization would enhance the robustness and generalizability of the findings.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces VERIFY, an automatic factuality evaluation pipeline that assesses language model (LM) responses by verifying and categorizing content units based on web evidence. Using VERIFY, the authors built FACTBENCH, a benchmark of 985 prompts across various topics and difficulty levels to evaluate LMs' accuracy in real-world settings. Results show that VERIFY aligns closely with human judgment, establishing it as a reliable method for assessing factuality in LM outputs.

### Strengths
The task of factuality evaluation is extremely important in large language models (LLMs), as ensuring the factual accuracy of model outputs is crucial for their reliability in real-world applications. The proposed approach of categorizing LM-generated content into "supported," "unsupported," or "undecidable" represents a novel and rigorous method, distinguishing this work from previous studies that often lack this level of granularity. This categorization allows for a more nuanced understanding of model limitations and strengths in factual reasoning. Furthermore, the authors carefully selected datasets and established comprehensive baselines, ensuring that their comparisons across methods are both fair and robust.

### Weaknesses
(1) Building FACTBENCH requires multiple steps, yet each step relies on relatively simple, heuristic approaches, which may limit the novelty and robustness of the benchmark in capturing nuanced factuality challenges.

(2) The lack of qualitative analysis for ambiguous samples or Tier 1 (Hard) prompts leaves gaps in interpreting how VERIFY handles especially difficult cases. Providing a more detailed examination of these prompts and their handling would enrich the analysis.

(3) While VERIFY’s methodology is strong in categorizing factuality, it is relatively limited in interpretability when applied to complex or context-dependent responses. Expanding on how VERIFY’s outputs could be used to provide actionable feedback for model improvement or on how it handles responses with interdependent factual claims would increase its utility and depth.

### Questions
(1) There is a typo on line 305: it references Table 2 when it should be Figure 2.

(2) The high refusal rate observed in Gemini1.5-Pro, especially in the Hard tier, is mentioned briefly in the paper. Could the authors provide more details for these refusals and any insights into how different refusal categories might impact the overall factuality evaluation? Also, in cases where refusals were misclassified or unjustified, did the authors investigate how these instances were distributed across prompts or tiers?

(3) Did you verify whether calculating the score using the Hallucination Score as defined in Eq. 1 is indeed meaningful?

### Soundness
2

### Presentation
2

### Contribution
3
