# On Re-Encoding Short-Term Memory of Large Language Models in Conversations

- Decision: Reject
- Scores: 3, 6, 3, 3, 5

## Abstract
Large language models (LLMs), such as GPT-4, are adept at generating coherent and fluent responses within conversational contexts. 
However, there has been a paucity of comprehensive research exploring LLMs to dynamically update their knowledge in response to corrections of misinformation provided by users during dialogue sessions. 
In this paper, we present a novel framework termed Knowledge Editing In Conversation (KEIC), along with an accompanying dataset, devised to assess the efficacy of LLMs in aligning the user update in an in-context setting, given the previous chat history containing a false statement that conflicts with the subsequent user update.
Through in-depth investigations, we observe that the contemporary LLMs exhibit a modicum of proficiency in this task.
To enhance their in-context knowledge editing abilities, we propose a structured strategy to handle the information update for LLMs in a multi-turn conversation.
We demonstrate that our approach is effective and suggest insights for research communities in this emerging and essential issue.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores whether LLMs can gracefully recover from false information presented in context when a correction is subsequently issued by the user. The authors connect this setting to the phenomena of memory re-encoding (MRE) from psychology. To study this task, a new benchmark KEIC is proposed that builds on top of CoQA by introducing conflicting statements into conversations through an annotation process. The authors propose various prompting-based methods for LLM-based MRE and also a more expensive deletion method that utilizes an LLM to identify and delete portions of the chat history that contradict the corrected information. The paper also includes an extensive evaluation on KEIC with a wide range of open and closed-source models. The authors claim that their benchmark will aid in the development of chatbots that are adaptable and conducive to long-term single-user usage.

### Strengths
1. The paper studies a relevant topic of faithfulness over contexts that are growing increasingly large as new models are deployed.
2.  The authors draw some interesting and unexpected conclusions from their results including that GPT-4o tends to be "stubborn", often not adapting as readily to corrected information in the context compared to GPT-3.5. 
3. The cost evaluation and analysis is relevant given the need for LLMs to analyze long contexts and is thorough.

### Weaknesses
1. **MRE:** The connection to MRE is quite tenuous. Since MRE seems to involve updating memory, this phenomenon seems most similar to the knowledge editing literature, where model parameters are updated. The paper does not provide a comprehensive review of MRE, nor does it illustrate concrete connections between the task and MRE. The authors should explain why the community should be interested in *in-context* MRE given the large amount of model editing research which explores similar ideas from a more analogous standpoint i.e. brain encoding new information and models encoding new information in parameters.
2. **Benchmark Limitations:** KEIC only consists of dialogues in CoQA with a Yes/No answer. From the example in Figure 4, it also seems like the questions are quite simple and closely related to the corrected information e.g. "young / old lady" and "Is Sarah old?". These choices make KEIC seem quite limited. For instance, the benchmark does not seem to consider how corrected information alters deductive reasoning and inferences e.g. if "Mary had blue and yellow paint" is corrected to "Mary had blue and purple paint", then the answer to "Can Mary make green paint?" changes from yes to no. Additionally, conversations in CoQA tend to be quite short. If the goal of this task is to understand how chatbots deal with corrected information over truly long contexts, a dataset that contains long conversations with topic switches should be studied such as [TopiOCQA](https://arxiv.org/pdf/2110.00768).
3. **Concerns with Evaluation:** The evaluations in section 5 do not address whether performance on questions unrelated to the modified information changes as corrected information is introduced.
4. **Notational Problems:** There is an excessive amount of notation in this paper. I would recommend that the authors rewrite sections in natural language and use notation sparingly. Some specific problems are outlined below:
   * Often there are two notations used for the same object. For instance, in 2.3 the authors refer to a turn with the $T_i$ notation, when they previously used the $(u_i, b_i)$ convention.
   * Alternatives in notation are presented for readability (e.g., dropping the indices of $R$, $Q$, and $A$), but often hamper understanding and flow given how frequently they are proposed. The authors also use notation involving subscripting $T$ such as $T_f , T_u, T_i, T_p, T_c, T_v, T_r, T_d$. This notation is overbearing and quite difficult for the reader to keep track of. I would encourage the authors to instead denote phases and methods explicitly with natural language.
5. **Clarity / Writing:** The writing is quite confusing, especially in the introduction. For instance, in the introduction, the authors claim that "Recall" is an effective technique for MRE, but Recall had not yet been mentioned nor explained and could easily be confused with the recall metric. Section headings could be much more descriptive. For instance, Section 2.2 is titled "Fact" when it contains information about the representation of facts in relation form. Finally, the KEIC benchmark seems to be one of the main contributions, but most details about its construction and annotation are relegated to the Appendix.

### Questions
1. What is the purpose of the proof section in Appendix D? Is the main takeaway that if the proposed methods in Section 3 worked perfectly, then questions would be perfectly answered?
2. For the deletion method, did the authors try having LLMs rewrite the inconsistent turns in the conversation instead of deleting them? This might be a better strategy since a turn may contain some relevant information to an answer even if some other information is incorrect.
3. For the deletion method, how was the inconsistency of a turn determined by an LLM?
4. How do models adapt answers when multiple facts are corrected in a single conversation?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper examines the scenario where context that appears previously in an ongoing conversation with a LLM is corrected by the user and evaluates whether the LLMs can reflect the corrected context in their responses. The authors formalize this scenario as the Knowledge-editing in-conversation (KEIC) framework and refer to the phenomena of knowledge update as memory reencoding (MRE). Specifically, KEIC and MRE refer to non-parametric and in-context knowledge editing i.e., the model parameters are not updated and the model’s behavior is influenced through prompting only. The authors of this paper collect a dataset for evaluating KEIC in contemporary LLMs through four different update methods. The dataset is collected by asking human annotators to edit a fact in the CoQA dataset, which is the updated knowledge. Accordingly, the ground truth answer to the corresponding Yes/No question in the CoQA dataset is updated. With this dataset, the authors propose four update methods: One-Time Correction (OTC), Recall, Verification and Deletion under two different settings i.e., Correction After Mistake (CAM) where the update is applied right after the incorrect fact is presented in the conversation and Correction Before Asking (CBA) where the update is applied right before asking the corresponding Yes/No question. Results are presented for various GPT, Gemma, LLaMA and Vicuna models. Updates are applied through 15 correction templates mined from Daily Dialog. Results show that the Deletion-based update method is most effective, but the Recall-based update method has the best trade-off between effectiveness and token-efficiency. Moreover, the CBA works better than CAM, which is expected because of the proximity of the update tokens to the QA tokens in the auto-regressive model. Surprisingly, gpt4o models are less reactive to these update methods than GPT3.5 models. Overall, there is room for improvement in KEIC in contemporary LLMs.

### Strengths
**Interesting topic in LLM conversational memory and well-written paper**: The scenario of KEIC is an interesting, if not one of the most important, topics in the domain of conversational memory of LLMs. The authors do a great job of formalizing the KEIC process, which serves as a framework for effectively thinking about in-context knowledge editing.


**Dataset contribution**: The authors contribute an important dataset that contains conversations with edited knowledge and corresponding questions. It is a sizable dataset and can be further extended to questions beyond the Yes/No format in a semi-synthetic manner by leveraging the KEIC framework for future work. 


**Extensive results**: The authors present several plausible settings, methods and conduct extensive experiments under these settings, showing crucial gaps in the performance of current LLMs. Importantly, these experiments provide further evidence that LLMs are not 100% proficient at attending to context, which can prohibit their deployment in error-sensitive situations. Some of these results are surprising and worth investigating further i.e., GPT4o performs worse than GPT3.5 in the OTC setting.

### Weaknesses
 **Limited Generalizability of Results**: The correction templates adopted by the authors (and listed in Appendix B) indicate that the knowledge updates that are present in the collected dataset are of a single kind i.e., fixing errors in previously reported events. This leaves out some other highly-plausible knowledge editing scenarios in conversations such as (1) temporal change in knowledge i.e., previous knowledge was true at that time but it has now evolved to a different state (such as change in Presidents) (2) evolving of user preferences or opinions (such as a change in music taste or other user preferences like name) etc. This also stems partly from the scope of the CoQA dataset which has a format of two participants discussing a passage from news or fiction. Further, the authors do not make the distinction between real-world facts and narrative fiction in this dataset. It is unclear from the results if it is hard to edit knowledge in an in-context manner if that knowledge is present in the parametric memory of the model (it is also entirely possible that GPT models are trained on the CoQA models and so this data exists in their parametric memory).

**Doubts about the persistency of the KEIC scenario**: Since this problem of models underperforming in the OTC scenario can be traced back to the issue of LLMs not attending to their context correctly, I am unsure if this will continue being a problem if it can simply be fixed by better positional encodings, training data, attention architectures in oncoming versions of LLMs.

**Additional Results**: There are three aspects missing from the Results section: 

(1) Since the KEIC problem is a reflection of how good LLMs are at attending to their in-context memory, it warrants analysis in terms of the length of the input. For example, does the update % change with longer distance between the $T_{u}$ (update turns) and $T_{i}$ test turns. Similarly, does the update % vary with longer distance between $T_{e}$ (error turns) and $T_u$?

(2) Some of the correction templates improve coreference resolution at the update step while other don't. How would the results look for one template vs. the other? On that note, is there one or more templates that consistently stay in the top-1,3,5 results?

(3) It would be great to see results from some of the latest open-source models such as LLaMA 3.1, OlMo, and perform analysis on the attention weights is possible.


**Confusing Jargon**: The authors have introduced some terms that may be prohibitive in understanding the results correctly. For instance, the reported metric is 'Update %' in Figure 5. It is unnecessary since it has already been made clear that the metric is simply the accuracy of the Yes/No question. I would suggest that the authors stick to 'Accuracy' to reduce confusion. Another example is the use of 'Recall' for a method, which is a frequently used term for evaluation metrics. Using this term as a method makes for confusing reading. Another term is 'Previous Phase' which really refers to the 'Irrelevant turns'.

### Questions
- Who do you think that MRE is a standalone problem that should be studied and not merely a different sub-perspective of the conversational memory problem that could be potentially solved, for example, by using RAG + external memory module or better long-context modeling approaches?

- Suggestion to separate CBA and CAM results in figures to allow the reader to consider both settings individual in terms of the four proposed methods.

See Weaknesses for other suggestions.

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
This paper introduces an in-context memory re-encoding process for large language models (LLMs), allowing memory updates and probing through conversational in-context prompts.
To achieve this, the authors created a dataset comprising {background context (a story), pairs of probing Q&A in a human-AI conversational format, and a final probing question}.

The paper details four in-context prompt memory updating types:

1. One-Turn Correction (OTC): The human corrects the LLM immediately after an error is made.
2. Verification: The LLM first answers a probing question, followed by a human verification question to confirm the accuracy.
3. Recall: The LLM rewrites the entire story after human correction, followed by probing.
4. Deletion: The LLM removes any sentence in the story that contradicts newly updated information.

The paper evaluates these memory-updating prompt schemes across different LLMs.

### Strengths
- Introduces a comprehensive dataset for studying in-context memory updating.
- Proposes four distinct prompting methods for updating memory in LLMs.

### Weaknesses
The paper has several issues, despite arguing for the importance of in-context memory editing over parametric knowledge editing:

1. While the task setting is intriguing, it seems more like adversarial question answering in a long-term conversational context (i.e., questions that are designed to trick the model into providing wrong answer) than true memory editing. Context-level memory editing would ideally involve managing an external database that saves and updates facts or events within the conversation. The current approach primarily tests the model's ability to handle conflicting information within a single turn, rather than demonstrating a persistent update to its knowledge base. The corrections introduced do not seem to lead to lasting re-encoding of information, which is a key aspect of memory editing.

2. There is a discrepancy between the dataset and the examples in Figures 1 and 3. The figures suggest memory editing in a human-to-human conversational context, while the dataset primarily involves single-turn stories and human-AI QA-style probing. This inconsistency makes it difficult to understand the practical application of the proposed memory editing framework. The use of varying dialogue formats across different figures creates confusion and makes it difficult to consistently interpret the task setting. To reduce potential reader confusion, I recommend that the authors use real data examples as motivating illustrations, better aligning the figures with the dataset's actual structure.

3. The authors used 15 different memory-updating prompts but only one prompt for memory probing. Exploring prompts that focus on recent information or limit historical context could yield more convincing results. The current probing method does not adequately test the model's ability to prioritize recent corrections over older information. For example, a prompt that explicitly asks the model to answer based on the most recent correction would provide a more direct evaluation of the memory update process.

### Questions
None

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates large language models' (LLMs) ability to integrate corrections made during a conversation, a process termed as Memory Re-Encoding (MRE). The authors introduce the Knowledge Editing in Conversation (KEIC) dataset, derived from CoQA, by introducing corrections mid-conversation to test LLMs' adaptation to updated information. Four correction methods—One-Turn Correction (OTC), Verification, Recall, and Deletion—are proposed, with Deletion emerging as the most effective in experimental evaluations on various LLMs, followed by Recall and OTC.

### Strengths
- The paper addresses the important challenge of enabling LLMs to incorporate corrections seamlessly, an essential feature for reliable conversational AI.
- The authors’ structured approach to enhancing MRE is interesting.
- Up to section 2, the paper is well-written and easy to follow.

### Weaknesses
 - The KEIC dataset may lack diversity in conversational flow.
    - Stories are consistently positioned at the start of each dialogue, which simplifies real-world conversational dynamics.
    - Both stories and conversations are brief, with only yes/no questions, potentially narrowing the scope of the model's evaluation. Expanding question types could offer richer insights with minimal adjustments in answer evaluation.
    - Correction utterances appear only adjacent to the story or directly preceding the question.
 - The experiments could benefit from a deeper analysis of how model performance varies with factors such as:
    - The distance between the corrected story and the question.
    - The position of correction utterances relative to the question.
 - Sections 3–5 could be clearer. Please refer to the questions in the Questions section. I will raise my score if misunderstandings due to unclear explanations are addressed.

### Questions
- Are CAM and CBA the only configurations for correction placement? Testing additional positions for corrections (i.e., various places between the correction and the question) could reveal valuable insights into positional effects on model performance.
- Line 314: Is the “update” baseline the original CoQA? The phrase "we directly replace the old fact in the story with a new one" suggests the original story is used without an explicit correction within the conversation.
- Table 1: Why does Deletion require more computational resources in the CAM setting compared to the CBA setting?
- Lines 354–357: This passage is difficult to follow. It would be helpful to reference Figure 9. What does "The goal of evaluating the former approach aligns with that of our baseline with no update phase" mean? Perhaps, this unclarity is related to my question about line 314.
- Line 374: The concept of "top-K upper bound performance" requires clarification and further explanation. Please provide a clearer definition.
- Lines 377–378: The statement regarding the “best five out of 15 correction utterances” is confusing. The definition suggests that performance should increase with higher K values since any of the top-K templates should trigger a correct response. However, the performance in the plots fluctuates or even declines as K increases.
- Figure 5: Does the statement “the baseline with no update phase has 56.5% of update” mean that GPT’s performance on the original CoQA is only 56.5%?
- Table 2: The terms "Update/No Update/Upper Bound" in the caption are not clearly defined, particularly “Upper Bound.”
- Line 452: The poor performance of GPT-4 and GPT-4o is quite unexpected. Please share some specific examples of failure cases.
- Line 464: The paper suggests that the Recall method outperforms OTC. Could this simply be due to Recall positioning the updated story closer to the question than in OTC?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work studies the Memory Re-Encoding  (MRE) task, which tries to correct the misinformation in the existing dialogue histories on the fly. Consequently, this work proposes a Knowledge Editing In Conversation (KEIC) framework to measure the adaptability of LLMs.

This work is beyond my research scope,  so my opinions may not be accurate.

### Strengths
1. The proposed framework KEIC can be used in correcting many general misinformation types (hallucination, notorious, etc.).

2. The proposed framework KEIC does not need to tune the model parameters.

3.  A very detailed and comprehensive problem analysis.

4. This work has built a high-quality dataset.

5. Four model-agnostic MRE methods are proposed and strong experiments are conducted.

### Weaknesses
1. The organization and notations should be improved. The current readability is somewhat lacking. For example:

- Line 147-148:  the mixture of $r$ and r. The distinction between the relation 'r' in normal text and the fact '$r$' in italics is not immediately clear and could lead to confusion, especially when these are used in close proximity. A more consistent notation is needed to improve clarity.
- The arrangement of Figures is not very good.  The texts on the $n$ page always require checking a figure that appears on the $n-2/3$ page. This disrupts the reading flow and makes it difficult to follow the arguments presented in the text. The figures should be placed closer to their first mention in the text.

2. The proposed methods involve many additional processes. Three advanced methods cost much more tokens (Table 1. #Input Tokens) , which may subsequently worsen the latency. The increased token usage for the advanced methods raises concerns about their practical applicability in real-time conversational systems. The additional processing steps also add complexity to the overall system.

3. Experiments may lack performance evaluation on the general metrics. For example, using BLEU ROUGE to evaluate the quality of the generated dialogues. While exact match is suitable for yes/no questions, the lack of general dialogue quality metrics makes it difficult to assess the overall impact of the proposed methods on the fluency and coherence of the generated dialogues.

### Questions
How does the proposed method affect the general performance of related tasks?

### Soundness
3

### Presentation
2

### Contribution
3
