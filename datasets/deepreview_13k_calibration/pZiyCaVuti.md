# LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 8, 6, 3

## Abstract
Recent large language model (LLM)-driven chat assistant systems have integrated memory components to track user-assistant chat histories, enabling more accurate and personalized responses. However, their long-term memory capabilities in sustained interactions remain underexplored. This paper introduces \BENCHMARK{}, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. With 500 meticulously curated questions embedded within freely scalable user-assistant chat histories, \BENCHMARK{} presents a significant challenge to existing long-term memory systems, with commercial chat assistants and long-context LLMs showing 30\% accuracy drop on memorizing information across sustained interactions. We then present a unified framework that breaks down the long-term memory design into four design choices across the indexing, retrieval, and reading stages. Built upon key experimental insights, we propose several memory designs including session decomposition for optimizing value granularity, fact-augmented key expansion for enhancing the index structure, and time-aware query expansion for refining the search scope. Experiment results show that these optimizations greatly improve both memory recall and downstream question answering on \BENCHMARK{}. Overall, our study provides valuable resources and guidance for advancing the long-term memory capabilities of LLM-based chat assistants, paving the way toward more personalized and reliable conversational AI.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
the paper proposes LONGMEMEVAL, a comprehensive benchmark designed to evaluate five core long-term memory abilities of chat assistants: information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention. Based on that, the present a unified framework that breaks down the long-term memory design into four design choices across the indexing, retrieval, and reading stages. Built upon key experimental insights, they propose several memory designs including session decomposition for optimizing value granularity, fact-augmented key expansion for enhancing the index structure, and time-aware query expansion for refining the search scope. Generally, i think this is a good paper and demonstrates some insightful observations via comprehensive experiments.

### Strengths
1. the proposed benchmark is valuable, being diverse, scalable and practical.
2. the experimental results are solid and comprehensive and the analysis is insightful such as the choices of key, value and query expansion.
3. the presentation and organization is relatively clear and easy-to-understand.

### Weaknesses
1. lots of human intervention is required to ensure the quality of dataset, such as line 248
2. most of experiments are conducted using gpt4o and llama3.1 8b instruct models. there is no comprehensive analysis about exsiting models.

3. according to (c) in figure 3, it seems there are no answer located in 7 8 9 10 round.
4. in figure6, what motivate you to list multi-session subset independently? and why not analyze this in later experiemnts?
5. why some experiments use both llama 3.1 70b and 8b instruction model, and some only use 8b model?

other typos

1. the answer in (a) of figure 2 is wrong?
2. best performance of llama 3.1 70b when value = session on table 2 is wrong?
3. typo in line 468

### Questions
1. according to (c) in figure 3, it seems there are no answer located in 7 8 9 10 round.
2. in figure6, what motivate you to list multi-session subset independently? and why not analyze this in later experiemnts?
3. why some experiments use both llama 3.1 70b and 8b instruction model, and some only use 8b model?

other typos

1. the answer in (a) of figure 2 is wrong?
2. best performance of llama 3.1 70b when value = session on table 2 is wrong?
3. typo in line 468

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper evaluates long-term memory abilities in dialogue tasks from extraction, multi-session reasoning, temporal ability, knowledge management, and abstention. They found that it's a challenge for existing LLMs to perform sustained interaction with those chat histories. To tackle this issue, this paper presents a unified framework to redefine the process when treating long-term memory. Beyond that, extensive experiments show optimizing in the new proposed framework can improve memory recall and QA ability in their benchmark. The key point of this work is to divide the pipeline workflow into single parts when facing long-term memory dialogue situations. They create larger data to make the long-term memory better represented, then make the model perform better.

### Strengths
1. It divides the memory workflow into three phases: indexing, retrieval, and reading. This segmentation not only helps to conceptualize the entire process but also lays the groundwork for systematically improving each stage. Then this paper further enhances this workflow. These modifications represent a thoughtful approach to refining how information is indexed, retrieved, and read from long-term memory. The process is sound and convincing.

2. This paper did a comprehensive evaluation across different existing models and provided detailed insights into how various models perform differently depending on the task—some models excel at reading (i.e., interpreting memory), while others are better at understanding or processing the retrieved information.

### Weaknesses
1. This work was generated by human-AI talk. However they did not mention how they control the hallucination and other issues when talking to AI chatbots (i.e., repeating problems, proportion of effective dialogue turns, etc.)

2. The proposed five aspects to evaluate long-term memory should be discussed more (Which aspect contributes more? Do different aspects have overlaps? What if one aspect performs better but another one fails?).

### Questions
Please give feedback to Weaknesses -> No.1 and No.2.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the problem of long-term dialogues. To study this problem, this work constructs LongMemEval, a new benchmark for evaluating five long-term memory capabilities of chat assistants, including information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention.  Experimental results on this new benchmark indicate significant challenges in existing LLMs on long-term dialogues. Furthermore, the authors propose a new framework, consisting of several designs, such as session decomposition, fact-augmented key expansion, and time-aware query expansion. Further results show that these designs can improve both memory recall and downstream question answering.

### Strengths
1. Long-term dialogue is an important problem in the era of LLMs, which also lacks of comprehensive problem formulations. This work formulates several core memory capabilities in this problem.
2. Construct a new challenging benchmark for studying this problem.
3. Propose a unified framework for improving the long-term dialogue capabilities in LLM-based conversational systems.

### Weaknesses
1. The construction of history sessions is not well motivated. The constructed history could be very noisy and the temporal order is just random. Not sure what is the motivation behind this messy historical session construction.
2. The proposed framework is actually a combination of several existing design. 
3. There are too many terms to remember in this work, which hampers the readability of this paper.
4. It would be better to include some long-term memory models to make a comparison for better presenting the challenge of the proposed benchmark and the effectiveness of the proposed framework.

### Questions
1. Why is the proposed framework called a "unified" framework? It is very pipeline, not unified. 
2. Since the timestamp is randomly assigned, how to guarantee the evaluation of temporal reasoning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a 500 LongMemEval dataset focusing on evaluating five crucial long-term capabilities of LLMs: (single-session) information extraction, multi-session reasoning, knowledge update, temporal reasoning, and abstention. 
The authors define each conversation as a key-value pair, where the key is the "time index" and the value is the corresponding chat.
They propose a three-stage framework for indexing, retrieval, and reading.
The framework has four control points: key (in the indexing stage), value (in the indexing stage), query (in the retrieval stage), and reading strategy (in the reading stage).
They conduct experiments to test their framework using LongMemEval on GPT-4o and Llama-3 (70B and 8B).

### Strengths
1. This paper aims to tackle a problem of LLM from the time perspective, which may be a useful method.
2. Apart from the single-session, the knowledge update and the temporal reasoning are known issues in contemporary LLMs.
3. They study these phenomena in the long-context, long-term scenario.

### Weaknesses
 This paper has several drawbacks regarding presentation, soundness, and contribution.

TL;DR, the major weaknesses are as follows (see **Details** below for further elaboration):

**Weakness 1.** [Presentation and Soundness] **This paper lacks careful proofreading, as it contains an unusually high number of typos and inconsistent writing. The numerical rounding is also confusing.** For example, in the third contribution, the authors report improvement is 7% ~ 11% in Line 99, but it's 6.7% ~ 11.4% in Lines 480-481 (should report the exact value or *at least* add the term "around" in Line 99). **Additionally, the flow in each section is not strongly connected, requiring significant revision to reach a publishable standard. Many tables and figures need substantial revisions and adjustments. The authors also need to be crisp in their writing.** For one thing, in the main content, the "result and discussion" of their proposed framework only spans two pages (Sections 5.2 to 5.5), including two tables and one figure. Without these, the text is roughly a page only in the main paper, which is insufficient for the ICLR community.

**Weakness 2.** [Presentation and Soundness] The LongMemEval dataset should be tested on other papers' existing baselines (with external systems like RAG). However, no "baseline section" is mentioned in this paper, and I cannot find the baseline mentioned in the "experimental setup" in Section 5.1 as well as in Tables 2 and 3 and their titles (e.g., "K = V is the baseline from xxx paper"). Hence, it is challenging to understand the prior works' baselines based on each individual's assumption. If non-familiar readers try to search for the "baseline" keyword, they will find it only appears once in the second contribution (in Line 95). After jumping to Section 5.3, they cannot find the recent papers conducting LLM with RAG baselines within this section either. If no comparable baselines are suitable for this task, see S2 below for suggestions.

**Weakness 3.** [Presentation and Soundness] **The authors claim this paper presents a *unified* framework, as shown in Figure 5, but without a formal mathematical definition, it is difficult to justify whether this is indeed true.** For example, how does the proposed framework encompass the existing RAG frameworks? Moreover, it is also hard for other future researchers to follow/revise/expand their ongoing work, particularly the four control points (CP) in Figure 5. Take the conducted CoN experiment (Section 5.5) as an example: The connection between the case when CoN is applied and Figure 5 is unclear. This figure is not illuminating, and the imprecise definition will let the readers interpret this paper on their own. Note that each separated component can be visualized and formalized in a better way (see Figure 1 in [0] and [1] for visualization; see also Section 3.1 in [1] for formalization). In addition, this paper only displays general terms without an explicit example to showcase their framework in Figure 5, whereas it is common for various RAG papers (see [2] and [3]).

**Weakness 4.** [Contribution] **As for the dataset comparison, LongMemEval needs justification to significantly distinguish it from other related works, such as task-oriented dialogues (as stated in Line 50) and other QA-based datasets (see C2 below).** Specifically, several question types are highly similar to (that is, can be leveraged by) those existing datasets, especially the single-session scenarios. Nonetheless, they are missing in the references. Hence, further analysis is necessary regarding why not to leverage their datasets.

# Details

## Presentation (P)

**P1. The contexts need to be reorganized to provide a clear flow.**

* As shown in Figure 2, the dataset construction pipeline is (a) Question Construction $\rightarrow$ (b) Evidence Session Construction $\rightarrow$ (c) History Construction. However, the (a) and (b) steps are merged into a single "paragraph" in Line 241 (within Section 3.2: LongMemEval: Benchmark Curation), while the (c) step has its own single "subsection" (Section 3.3: History Compilation).

* In the main paper, the results and discussion of their proposed framework only have two pages (Sections 5.2 to 5.5), including the two tables and a figure. More analysis should be moved to the main content. For instance, I find Table 7 in Appendix C informative, so perhaps the authors could consider moving this to the main content.

* There is a discrepancy between Section 4.2 and Figure 5. In Section 4.2, the authors use "CP 1: Value" and "CP 2: Key" as the paragraph title. However, it is "CP 1: Key" and "CP 2: Value" in Figure 5. 

* What is NL in Figure 7? I think it is natural language (as opposed to JSON format), but "NL" is not a common abbreviation and is not mentioned in the main content either. Moreover, this figure reports the result on LongMemEval_s, yet it is not mentioned in Figure 7 and Section 5.5. 

**P2. The figures/tables do not follow the order or ICLR format. Many of them require adjustment in format and location in this paper for better reference.**

* Should follow the ICLR format and place the table title on top (see Tables 1, 2, and 3). 
* Tables and Figures are placed on page "i" but first mentioned on page "i+1." For example, Table 1 is first mentioned on page 3 (Line 146) but placed on page 2. For another example, Figure 2 is first mentioned on page 5 (Line 242) but placed on page 4.
* As shown in Figures 2, 3, and 4, it really confuses me to place (a), (b), and (c) at the end. Take Figure 3 as an example: 
```
LongMemEval challenges chat assistants through its diverse question types (a), emphases on multi-session reasoning (b), 
and diverse evidence locations within sessions (c).
```
It should be:
```
LongMemEval challenges chat assistants through its (a) diverse question types, (b) emphases on multi-session reasoning, 
and (c) diverse evidence locations within sessions.
```
* The column separator line is inconsistent (Tables 1 and 3). 
* In Table 1, can the authors explain why you do not use "# data" but "# Q"?
* In Line 83, the term session has a different meaning compared to Table 1 (session means the total number of LongMemEval dataset in "with 500 sessions"). 
* The text in Figure 2 is small. Moreover, the "Answer: 5" is wrong in Question Construction (should be 50).
* In Figure 3-c, the round index 7 ~ 10 is "invisible," compared to the "barely visible" number of sessions = 6 in Figure 3-b. If they do have "height," perhaps insert the numeric values above these bars.
* In Figure 4-b, two "Llama-3.1 8B Instruct" are presented in both w/o CoN and w/ CoN. Which one is 70B? 
* Moreover, no explicit evaluation metric (accuracy) is found in Figure 4-b and its caption. While the authors mention "... compared to answering the questions based on only ...," this makes readers need to first observe it is the question answering task, then refer to Section 3.3 to conclude that this table is indeed using accuracy (but not Recall@k and NDCG@k).
* In Figure 5, presenting "key 4," "value chunk 2," etc. without a simple example is hard to grasp the idea. This should be done by showing different color blocks in "legend" (just like Figure 3) and providing a concrete example (possibly re-use the examples in the previous figures). Additionally, Figure 5 does not visualize a "smooth" pipeline; there is a break between the"(1) indexing" process and the "(2) retrieval and (3) reading" process. Specifically, there is no connection between the "key 4 and key 2" and the data storage system.

**P3. Too much emphasis on many terms and two (or more) adjectives to describe certain words.** Specifically, the overuse of "\textit" and compound words (excluding common words in NLP like long-term). While I could understand that the authors want to emphasize the *scenario* they aim to test and *why* not conduct more experiments etc., it further adds the difficulty to grasp the main point in this paper. The texts in italics are already overwhelming even without these. Below are several sentences that may distract the readers:

* In Lines 287-288: This design allows us to simulate *realistic* and *extensible* user-AI chat histories with *minimal conflicts*.
* In Lines 319-320: ... we compare this *online* memory evaluation with *offline reading*, where GPT-4o is prompted to answer with the complete history provided as context. (Note: online is already in italics in Lines 80 and 183)
* In Line 426: Using LongMemEval_m, we compare different value choices in a *budget-aware* manner.
* In Line 430: The only exception is with *multi-session reasoning* questions, where fact decomposition consistently improves performance. (Note: multi-session reasoning is already mentioned and abbreviated as MR before)
* In Lines 476-477: To address this need, we introduce a simple yet effective *time-aware indexing and query expansion* scheme. (Note: "time-aware indexing and query expansion" is already in italics in Line 400; moreover, "time-aware indexing and query expansion" first appears in Line 98, but only time-aware is in italics)
* The authors spend 6 lines mentioning that this paper is inspired by the needle-in-the-haystack test (in Lines 292-297); however, it is already stated in the Introduction Section (in Lines 77-78). In my opinion, the authors should remove this paragraph and elaborate more on either (1) the framework formulation or (2) other experiments that the authors found worth noting in the main content (for instance, Table 7).
* As for the over-use of adjectives/compound words, please refer to Lines 72-79 as an example (others are scattered in the main content, particularly in the Introduction):
```
We introduce LongMemEval, a comprehensive, challenging, and scalable benchmark designed to assess the long-term memory capabilities of chat assistants. LongMemEval consists of 500 human-curated, high-quality questions to test five core memory abilities: (...). Each question requires recalling information hidden within one or more multi-turn task-oriented user-AI dialogues that are LLM-simulated and human-edited. Inspired by the “needle-in-a-haystack” test (Kamradt, 2023), we design an attribute-controlled pipeline to compile a coherent, extensible, and timestamped chat history for each question.
```


## Soundness (S)

**S1. The proposed unified framework is not formalized.** See Weakness 3 above.

**S2. The authors do not compare their proposed framework with other similar baselines such as LLM with RAG or external systems.** While the authors do report 97 data using proprietary LLMs (ChatGPT and Coze) in the pilot study, this subset of data is 5x smaller than the original size of the data (500), not to mention the conversation sessions are extremely short, which is mentioned in Lines 317-318: approximately 10x shorter than LongMemEval_s. What's more, the distribution does not even really match the original LongMemEval_s dataset (see Lines 1030-1034 in Appendix B). Is there at least an implicit baseline comparison between your and other works in this paper in some way (see Weakness 2 above)? Are the works mentioned in Line 393 the baselines?

On the other hand, *if the nature of this dataset is that no prior baselines are suitable for comparison, then the authors should test their framework using more LLMs to benchmark the LongMemEval dataset for future researchers and demonstrate its effectiveness across various LLMs.* 
In this scenario, to strengthen the method, it would be necessary to (a) run the experiments multiple times (see [4]) or (b) enlarge the existing LongMemEval dataset. This paper only has 500 data and experiments on two LLMs in its current state: GPT-4o and Llama 3 (70B and 8B). If the budget is an issue, testing other small LLMs (e.g., below 7B) is also a welcome contribution.

**S3. Regarding the soundness in Figure 4-a, the authors only test the closed-source LLMs with a memory system once in a small (97) data.** While the authors already mention (multiple times) that they are interested in testing "*online* interactions with chatbot", this topic further narrows down to a very specific setting. Moreover, as these LLM-based memory systems do not have a snapshot (nor do they release a technical report demonstrating the robustness of their memory systems on various reasoning tasks), including this potentially immature result in the main content could be a problem for future reference (despite the evaluation time mentioned in the footnote), because these systems would be constantly improved over time without any notification, increasing the difficulty in terms of reproducibility.

**S4. The dataset contains only 500, which is rather small. Moreover, many questions focus on *single-turn* sessions (31%; see Figure 3-a).** As these settings are constantly tested in previous long-term/short-term datasets (see Contribution C2 below), the authors should create a dataset with more "multi-session, knowledge update, and temporal reasoning" for current LLMs.

**S5. In Figure 1, the definition of those question types is unclear.** Specifically, in Figure 1, why not treat the "knowledge-update" as a "multi-session" example, and vice versa? Moreover, after adding the time and date in each session, they can also be generalized to the "temporal-reasoning." The authors do not define these types of questions clearly and only use "The other types of questions are multi-session (MR), knowledge-update (KU), and temporal-reasoning (TR)" in Lines 236-237, and yet the distribution of question types is distinctly shown in the pie chart in Figure 3-a.

## Contribution (C)

**C1. Could the authors explain why it is necessary to differentiate "human-AI" and "human-human" conversations?** Am I missing something in this paper? If so, could you kindly explain why you are interested in the user-AI setting and further differentiate this in Table 1? For instance, is there a significant difference between them when training an LLM or in some tasks that prefer user-AI datasets over human-human ones? 

**C2. Prior works of task-oriented dialogues (TOD) are missing, such as the MultiWoZ dataset [5].** On the other hand, the AirDialogue dataset [6] has a more narrower scope. **As a result, there may be an issue in Lines 48-50**: *Many datasets focus solely on human-human conversations (Xu et al., 2022a; Maharana et al., 2024; Kim et al., 2024), while others omit task-oriented dialogues, which represent a significant portion of chat assistant usage.* **As for the Related Work, there is another issue in Lines 142-144** (*Despite these advancements, existing QA-based benchmarks overlook several memory capabilities critical to long-term user-assistant interactions: synthesizing information across numerous sessions, recalling assistant-side information, ...*) **because the CoQA dataset [7] encompasses these two issues.** The model needs to refer back to the conversation history. Lastly, **the SituatedQA dataset [8] $-$ related to temporal context and retrieval $-$ is missing in the Related Work.**

### Questions
Please address the concerns/questions in the above presentation (P1-P3), soundness (S1-S5), contribution (C1-C2), and the following other questions.

Other:

1. The Ethics Statement is missing. 

* Since the LongMemEval dataset and the pilot study require human annotators, the ethics statement *should* be included, even though they are not as strongly recommended as the Reproducibility Statement. Moreover, given that this paper studies a three-stage framework for improving a chatbot's long-term memory, could this be exploited by malicious users to produce harmful results? I cannot find it in the appendix, however. 

2. Do the authors include the Limitations section? If not, then is this work thoroughly studied? What are the future work? 

3. What is the temperature used in this paper? What is the version of GPT-3.5 turbo tested in Figure 4-a?

4. In Figure 4-a, do the author have insights regarding why gpt-4o-mini is better than gpt-4o?

5. Do the authors touch upon the NDCG metric in the discussion section?

6. In Lines 419-420, are the timestamps sorted by ascending or descending order? Do the authors evaluate the performance when the timestamps are not sorted in the preliminary experiments?

7. In Table 2, why K = summary and K = V + summary experiments are not included in this paper? Is it because of the budget-aware manner? Moreover, why is the numeric value (0.590) in QA performance using Llama-3 (70B) in bold? It is smaller than the corresponding value when K = V (0.592).

8. The rounding is confusing.

* In the third contribution (Line 99), the authors report improvement is 7% ~ 11%, but it's 6.7% ~ 11.4% in Lines 480-481. Moreover, the result is for GPT-4o LLM, and this improvement does not hold when Llama-3.1 (8B) is used, as stated in Lines 482 (*We also find that the effectiveness of this method depends on using a strong LLM*). Nevertheless, this strong prerequisite is not mentioned in Line 99, which could be a bit misleading regarding the "7% ~ 11%" improvement.

* Can the author provide how to compute the numerical values in Line 467 (*This approach, particularly when using user facts, yielded an average improvement of 4% in retrieval metrics and 5% in final accuracy across all models.*)? Specifically, how to get the result of a 5% improvement in Table 2? Is it $1/3 * [(0.714-0.670)/0.670 + (0.584-0.570)/0.570 + (0.490-0.464)/0.464] = 0.04875$, then 4.9% rounds to 5%? If so, why **only** use Top-5 in GPT-4o and Top-10 in Llama-3.1 (70B and 8B)? Because I can get the 4% result in retrieval metrics if I average all the improvement in "Recall@5, NDCG@5, Recall@10, and NDCG@10": $1/4 * [(0.732-0.706)/0.706 + (0.620-0.617)/0.617 + (0.862-0.783)/0.783 + (0.652-0.638)/0.638] = 0.0411$ (4.1%); however, when I try to average all the top-5 and top-10 improvement in these LLMs (6 entries), it does not match 5%.

* Similar to the previous question, can the authors list the steps when computing the average metric in Lines 480-481? How can we get the 11.4% and 6.7% results from Table 3? Is there any additional rounding method involved after the computation?

9. Are Figure 4-b and Figure 7 related in any sense? If so, please explain the following questions.
* There is a discrepancy between Figure 4-b and Figure 7. Specifically, the oracle of GPT-4o is 0.924 and Llama-3.1 (*70*B, I guess) is 0.848 in Figure 4-b, and they can be found in Figure 7 (JSON + CoN). However, the oracle of Llama-3.1 (8B) is 0.710 in Figure 4-b, which is the natural language with CoN (NL + CoN). Since the JSON input format is not mentioned in Section 3.5, the authors should report when the input format is NL but not JSON. 
* In this vein, if I understand correctly, how can we derive the oracle of those LLMs w/o CoN from Figure 7? These values are not identical (I thought it could be done by looking at NL + Direct Prediction).
* Is it a coincidence that Llama-3.1 (8B) has no improvement when CoN is used?

10. Other typos and suggestions:
* To improve the clarity of this paper, including a simple, concrete example in Figure 5 (or mentioned in Sections 4 and 5) would be beneficial. Otherwise, readers must refer to Appendix D (in Figures 11 and 12) to know what keyphrases/user facts/query expansion is exactly.
* The term "round" is not precisely defined in this paper (see Line 377: decomposing sessions into individual rounds). I only find the session is defined in Section 3.1. For instance, can a session be decomposed into 2 (i.e., user and chat assistant) rounds? If more rounds ($>$ 2) are possible, how do you handle this process in this paper?
* cross-session $\rightarrow$ multi-session (for consistency). Note that other words need to be revised for consistency, yet it is too cumbersome to list all of them.
* In Line 65 (verb missing): ... Finally, we the coverage of five core ...
* In Line 138, the em dash is inconsistent.
* In Line 161, RAG is not mentioned in retrieval-augmented generation but is later used in Sections 5.2 and 5.3.
* In Lines 375-376, should use \citep.

### Soundness
2

### Presentation
1

### Contribution
3
