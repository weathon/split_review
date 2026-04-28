# SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs

- Decision: Accept
- Avg Score: 6.40
- Scores: 6, 6, 6, 8, 6

## Abstract
Large language models (LLMs) have made significant advancements in various natural language processing tasks, including question answering (QA) tasks. 
While incorporating new information with the retrieval of relevant passages is a promising way to improve QA with LLMs, the existing methods often require additional fine-tuning which becomes infeasible with recent LLMs. 
Augmenting retrieved passages via prompting has the potential to address this limitation, but this direction has been limitedly explored.
To this end, we design a simple yet effective framework to enhance open-domain QA (ODQA) with LLMs, based on the summarized retrieval (\name{}).
\name{} helps LLMs predict more accurate answers for a given question, which are well-supported by the summarized retrieval that could be viewed as an explicit rationale extracted from the retrieved passages. 
Specifically, \name{} first constructs summaries of the retrieved passages for each of the multiple answer candidates. 
Then, \name{} confirms the most plausible answer from the candidate set by evaluating the validity and ranking of the generated summaries.
Experimental results on diverse ODQA benchmarks demonstrate the superiority of \name{}, with improvements of up to 4.6\% in exact match (EM) and 4.0\% in F1 score over standard prompting approaches. 
\name{} also can be integrated with a broad range of retrieval methods and LLMs. 
Finally, the generated summaries from \name{} show additional advantages to measure the importance of retrieved passages and serve as more preferred rationales by models and humans

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work studies retrieval augmentation via prompting, for the task of open-domain question answering. They propose a method based on "summarized retrieval" (SuRe). SuRe proceeds in a few steps. First, it retrieves top-k results with an off-the-shelf retriever. Second, it generates multiple candidate answers directly (not via decoding multiple completions). Third, it generates a conditional summary (of the retrievals) for each candidate answer. Lastly, it validates each summary (as faithful or not) and uses a pairwise comparison approach to select the most informative answer. The pairwise scoring approach is applied across all pairs and averaged.

On the Open-Domain QA tasks NQ, WebQ, 2Wiki, and HotpotQA, the authors report improvements of up to 4.4% in exact match over baselines. The authors conduct a human evaluation of the SuRe summaries (whose defining characteristic is being centered around a candidate answer, derived from GPT-4) against general-purpose summaries (derived from GPT-4 without answer candidates). Generic summarization wins 30.3% while SURE wins 37.4%. They ask human evaluators which summaries are more informative and better support the question-answer pairs, and observe higher preference for SuRe (Generic: 26.9% vs SuRe: 43.4%).

### Strengths
1. The proposed pipeline is relatively rich and well-executed.

2. The authors develop a number of thoughtful baselines and report extensive comparisons. While there's very limited comparisons to prior work directly, I do find that there's a lot of value in the set of curated baselines they develop, which can be compared apples to apples to the proposed method.

3. The results are consistently solid across several tasks, LMs, and retrievers. This is the hallmark of a solid idea. The results are never that strong overall (in isolation), but perhaps SuRe can probably be combined into a really strong 'sota' system in principle.

### Weaknesses
1. The authors assert in the abstract that retrieval augmentation via prompting "has been limitedly explored". While much more work is required to improve RAG methods that use prompting (or otherwise), few areas of modern NLP that have received more attention than RAG prompting. As a case in point, the authors build a method for "summarized retrieval", but I don't see citations to much prior work on considering summarization in the context of open-domain QA and prompting. For example, "Baleen: Robust Multi-Hop Reasoning at Scale via Condensed Retrieval" is the title of a paper at NeurIPS 2021, where the notion of _condensed retrieval_ seems fundamentally connected to _summarized retrieval_. For another example, "Open Domain Multi-document Summarization: A Comprehensive Study of Model Brittleness under Retrieval" is a recent task proposal. These are certainly different formulations of summarization at scale, but they are just two examples of a rich space considering summarization in open-domain contexts.


2. The authors focus on 'zero-shot prompting', but I do not find a convincing justification for presenting this limitation as a 'remarkable' feature. Zero-shot prompts are not necessarily indicative of generality (if anything, a decent few-shot prompt specifies the task more precisely and is empirically not unlikely to be more robust across LMs, counter to the assertion by the authors). While I'm not opposed to the need to eliminate some angles from a large experimental endeavor, I do wonder how useful SuRe is if the QA component had access to a few examples of the task. (This overall may explain, for instance, why chain of thought performs so poorly in the evaluations.)

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method to improve open-domain QA by making a summary of the retrieved passages. To create good summaries, candidates are first generated by an LLM, which are then used to condition the generation of summarties. The method is compared with a naive augmentation with all the retrieved passages and a generic summarization, as well as several existing approaches such as reranking, CoT, etc. The proposed method is shown to perform better on several datasets.

### Strengths
The idea of creating a summary of the retrieved passages centered around the possible answers is very interesting. This may solve the problem of noise information contained in the passages and help dealing with long passages. This idea has not been explored previously.
The approach relies on prompts to LLM, so it can be used with any LLM without fine-tuning it. This may be a generally feasible approach in many application contexts.
The experimental results are convincing. It demonstrates the a answer-oriented summary is better than a generic summary, and better than no summarization. The advantage of the approach is properly shown. In addition, the method is also shown to outperform the existing methods.

### Weaknesses
The performance of the method may strongly depend on the prompts used. While the paper demonstrates that appropriate prompts can help create a good summary for improving QA, there are still questions about what prompts should be used. I wonder if the authors have tested several alternative prompts before choosing the ones used.
Fig 3 is unclear. What are "the corresponding two conditional summarizations"?

### Questions
See comments in Weakness.

### Soundness
3 good

### Presentation
3 good

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
This work introduces Summarized Retrieval (SURE) to enhance the performance of Open-Domain Question Answering (ODQA) using retrieval-augmented Language Models (LLMs). The goal is to provide more well-grounded answers with LLMs by generating summarizations of retrieved passages, which serve as explicit rationales for the answers. By constructing multiple summarizations for each possible answer candidate, LLMs can then focus on context relevant to the candidate and provide more discriminative viewpoints for the question. Experiments are conducted on multiple QA datasets showing that SURE improves across all of them.

### Strengths
The idea of constructing the summaries of the retrieved passages for the potential answer candidates is somehow simple yet effective. The paper shows significant improvements across various datasets.

### Weaknesses
While SURE shows interesting results, there are some points that in my opinion should be clarified/improved before publication:
- It is unclear how this approach can scale. SURE may work well in experiments, but in real-world applications, the number of relevant passages can vary greatly and the various steps in SURE can become extremely costly, limiting the usefulness of this approach. Specifically, the repeated summarization of passages for each answer candidate could lead to significant computational overhead, especially with a large number of potential answers and retrieved documents. The paper does not provide a clear analysis of the computational complexity of the proposed method, making it difficult to assess its practical applicability.
- The evaluation metrics are based on term overlaps and they might not capture all dimensions of model performance. Other factors like response coherence, relevance, and efficiency should also be considered, especially in the case of LLMs. The use of EM/F1 scores, while standard for some datasets, may not fully reflect the quality of LLM-generated answers, which often exhibit nuances beyond simple term matching. The paper should explore metrics that better capture the semantic correctness and fluency of the generated responses.

### Questions
- Why limit the evaluation to only EM/F1 and not consider LLMs approaches for automatic evaluation?
- Why only short-answer datasets? Have you considered long-answers? What would change in that case?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Summarized Retrieval (SURE) for open-domain QA. First, it generates answer candidates from retrieved passages  with LLMs. Then, for each candidate answer, it conditionally summarizes the retrieved passages in order to focus on extracting the candidate-relevant contexts. Then those answers are ranked by a weighted score of instance-wise validity score and pairwise informativeness score. Experimental results show that SURE significantly outperforms the baselines on multiple datasets and LLM configurations. Detailed ablation studies are also performed.

### Strengths
- A novel framework is proposed to enhance open-domain QA with LLMs where the candidate answer can be better grounded on retrieved passages.
- The experiments are well-conducted and the performance improvement is significant and consistent.
- The paper is very well-written.

### Weaknesses
 - The proposed method could be expensive considering eq 4-6.

### Questions
The paper is clearly written. No more questions from me.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presented a new design, named SuRE, of combining retrieval and prompting to improve LLM's Open Book QA quality. It starts with retrieving relevant documents about the question, then generates a list of candidate answers with vanilla retrieval-augmented generation (RAG) prompting. The key contributions then follow. It prompts LLMs to produce a per-candidate summary of the retrieved documents to support the candidate. Then, LLM-based point-wise and pair-wise critiques are used to assess the quality of the per-candidate supporting summary. The candidate with the most sound supporting summary is chosen as the final answer. This is based on an intuition that the supporting summary for a correct candidate is usually of higher quality.

The paper designed experiments to show the quality gain of SuRe, which surpasses vanilla RAG and other recent algorithms of improvement. It also showed that the improvement is consistent with different retrieval algorithms and LLMs. Ablation study is run to understand the contribution of different part of SuRE. The paper thus concludes that SuRe is an effective way to improve retrieval-based open book QA without the need to finetune the underlying LLM.

### Strengths
- Writing and clarity. The paper is mostly well-written, easy to follow, and free of grammar / formatting errors.
- Comprehensive experiment design. The paper tested SuRe with different datasets, retrieval algorithms and LLMs as those factors could have a big impact on the outcome.
- Reviewer particularly likes the way the paper listing all research questions explicitly at the beginning of the experiment section with reference to corresponding tables and figures: clear and easy to follow.

### Weaknesses
Here the Reviewer tries to order the weakness by their priority.

- The title and initial claim in the abstract are too broad. They almost sound like a claim of re-inventing RAG. Abstract called out of hallucination and grounding, but it's not specifically studied in the paper, at least not more than just exact-match rate and F1 scores. It would be better if the authors make the title and abstract more specific to the contribution.

- Efficiency and cost, which is an important shortcoming of SuRe, is not discussed. During the process, SuRe makes a significant amount of calls to the underlying LLM. They are both slow and costly (in direct money terms in the case of calling commercial APIs). It would be useful to show the comparison and let any potential users know the cost of the quality gain.

- Ablation study is poorly designed. Reviewer is expecting a study where each of the key component of SuRe  is removed (ablated). However the paper showed the results of each one individually added. The subcomponents are not 1 to 1 mapped to SuRe either. For example what is MCQ and how it maps back to SuRe? Some readers may figure it out eventually but it's hard for the Reviewer to get it in a short time.   

- Need to be specific about "limitedly explored" when talking about previous work. A potential reader should not need to guess or read the whole reference paper to understand where the limits of the previous exploration are in the author's view.

See more trivial comments related to weakness in the Questions section.

### Questions
- Section 1 paragraph 2: "implicitly forced to use the retrieved information without additional training". The Reviewer didn't get it. Do you mean use or not use?

- Numbers in the experiment section: It's better to give some confidence interval of the EM/F1 numbers since they are obtained on a smaller sample (500, if the Reviewer recalls correctly).

- Section 4.3: Expand "MCQ" and explain what Robinson et al (2023) did. Readers should not have to read a reference paper if they don't want to dive deeper.

- Figure 4 (a): The shape of the point is hard to read, and only using the red-blue color to distinguish lines could be a problem for color-blind people. (Reviewer appreciates the effort of adding patterns to (b) and (c) so color is not the only discriminator). 

- Last paragraph of Section 4. Reviewer suggest adding the number of human-preference samples (84) here, saving readers a trip to the Appendix.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
