# Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models

- Decision: Accept
- Scores: 6, 6, 8, 5

## Abstract
Instruction-tuned language models (LM) are able to respond to imperative commands, providing a more natural user interface compared to their base counterparts.
In this work, we present Promptriever, the first \emph{retrieval} model able to be prompted like an LM.
To train \modelname,
we curate and release a new instance-level instruction training set from MS MARCO \cite{msmarco}, spanning nearly 500k instances. \modelname not only achieves strong performance on standard retrieval tasks, but also follows instructions. We observe:
(1) large gains (reaching SoTA) on following detailed relevance instructions (+14.3 p-MRR / +3.1 nDCG on FollowIR), (2) significantly increased robustness to lexical choices/phrasing in the query+instruction %
(+12.9 Robustness@10 on InstructIR), and
(3) the ability to perform hyperparameter search via prompting to reliably improve retrieval performance %
(+1.4 average increase on BEIR). 
\modelname demonstrates that retrieval models can be controlled with prompts on a per-query basis, setting the stage for future work aligning LLM prompting techniques with information retrieval.\extrafootertext{{\color{brickred}$^\ast$} Work performed during an internship at Samaya AI

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Currently, retrievers are only able to retrieve texts similar to input queries, mostly with text similarity. In this paper, the authors present Promptriever, the first retrieval model able to be prompted with textual instructions. 

For example, the users can pass in complex instructions to filter the passages to be relevant to a specific topic or exclude certain categories of passages.

To do so, the authors create and release a synthetic dataset of query-passage relevance pairs augmented with instructions. They use the MS MACRO dataset and generate instructions using Llama-3-70B, which includes diverse length formats and styles. Then, they use GPT-4o to generate the instruction negative passages. The Promptriever is then trained on the augmented data. 

As a result, the Promptriever maintains strong retrieval scores in standard settings. Compared to the original RepLlaMA, it also follows instructions better. The authors also perform multiple ablations such as the instruction-negatives.

### Strengths
1. The motivation is strong and the story is convincing. The authors identify the retrievers' current lack of instruction-following abilities to motivate the method. They help to bridge the gap by introducing Promptriever.
2. The experiment performance is promising and shows improvements in various datasets.
3. The ablation studies are sufficient and necessitate the needs of the different training components.

### Weaknesses
See questions.

### Questions
1. Can you list out some use cases where the promptriever is used in scenarios such as RAG? How would it perform?
2. It would be nice to see some qualitative examples of Promptriever compared to traditional retrievers, besides the example in the intro.
3. You mentioned in L240 that cross-encoders perform best due to their significant compute advantage. Could you list out the compute resources required by different baselines and Promptriever?

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
In this paper, the authors introduce an instruction-aware retriever named Promptriever, which can be prompted like an LM. They build a dataset for training such a retriever based on MS MARCO. They conduct experiments based on the dataset, and reveal several interesting conclusions.


Pros:
- The problem discussed in the paper, i.e., building instruction-following IR models, is interesting. 
- The problem definition is clear. The proposed method is easy to follow.
- Experimental results verify the effectiveness of the proposed method.


Cons:
 - The dataset is generated solely based on MS MARCO. It would be great if more datasets could be considered, especially for the test. BEIR should also be considered for the zero-shot scenario.
- It would be great if the definition of instructions in IR could be clearly defined. For example, given the example "Which type of volcano eruption has not been seen?", the authors claim that the volcano types and formation can be added as additional instructions. I wonder why these are treated as additional instructions but not part of the original information need (i.e., the original queries).
- More details about the experimental setup should be provided. For example, are the baseline models trained using similar assessment data (with instructions in the queries)?
- Better baseline models should be added. For example, we can generate query rewrites via LLMs and then retrieve documents using the rewritten query (converting the NLP-like instruction into keyword-like queries).

### Strengths
Pros:
- The problem discussed in the paper, i.e., building instruction-following IR models, is interesting. 
- The problem definition is clear. The proposed method is easy to follow.
- Experimental results verify the effectiveness of the proposed method.

### Weaknesses
 Cons:
 - The dataset is generated solely based on MS MARCO. It would be great if more datasets could be considered, especially for the test. BEIR should also be considered for the zero-shot scenario.
- It would be great if the definition of instructions in IR could be clearly defined. For example, given the example "Which type of volcano eruption has not been seen?", the authors claim that the volcano types and formations can be added as additional instructions. I wonder why these are treated as additional instructions but not part of the original information need (i.e., the original queries).
- More details about the experimental setup should be provided. For example, are the baseline models trained using similar assessment data (with instructions in the queries)?
- Better baseline models should be added. For example, we can generate query rewrites via LLMs and then retrieve documents using the rewritten query (converting the NLP-like instruction into keyword-like queries).

### Questions
- How are the baseline models trained? Are they using similar assessment data (with instructions in the queries)?

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
4

### Summary
The paper introduces Promptriever, a bi-encoder model that enriches the per-instance query context within prompts. To train this model, per-query instructions and instruction negatives are synthetically generated. The authors evaluate Promptriever across various scenarios, including instruction-following datasets, in-domain retrieval, and out-of-domain retrieval. The model not only surpasses previous bi-encoders but also achieves performance comparable to state-of-the-art cross-encoder retrievers, showcasing its effectiveness in handling free-form language prompts.

### Strengths
- The paper introduces a novel idea by challenging the assumption that the same instruction can be applied uniformly across queries.
- The authors curate a training dataset that serves as a solid resource for providing detailed, per-instance instructions.
- I particularly liked the analysis in Section 5, which addressed several questions I had while reading the methodology and experimental results sections.

### Weaknesses
 - The generated instructions are only used during model training. It would have been insightful to hold out a dev or test split to evaluate how the model performs on this dataset.
- For BeIR, the use of generic instructions feels too broad. Task-specific instructions, such as those in TART, might have been more effective and better aligned with the goals of the paper.

### Questions
- For out-of-domain retrieval, what is the rationale behind selecting the best score out of 10 prompts, rather than fixing a prompt or reporting an average score?
- Could the authors provide some qualitative examples illustrating how Promptriever performs across different categories in Table 6?
- In Table 11, simpler prompts like “Think carefully about relevance” seem to yield strong performance. Why might these simpler prompts outperform other more detailed ones that closely match the training data?

### Soundness
4

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
The paper presents Promptriever, an innovative retrieval model that incorporates instruction-following capabilities akin to LLMs. By curating a new instruction training set from MS MARCO, the authors developed a bi-encoder retriever that adjusts its responses based on natural language instructions, demonstrating substantial improvements in retrieval tasks. Specifically, Promptriever achieves state-of-the-art results on instruction-following retrieval tasks, showing significant robustness to query phrasing and the ability to perform hyperparameter search via prompting. This model sets a new precedent for future work in aligning LLM prompting techniques with IR systems.

### Strengths
- The focus on enabling retrievers to understand human instructions aligns well with the current demand for more intuitive and adaptable search technologies, marking a significant advancement in retrieval systems.
- The methodological approach of not requiring human annotations is notable, offering a scalable and cost-effective solution for training retrieval systems.
- The clarity of the paper and its comprehensive details support replicability and transparency, which are crucial for advancing research in this area.

### Weaknesses
My main concern is about the **experiments**.
- The t-test is not conducted on the experimental results. In IR, it is very important to validate whether the improvement is significant.
- The use of varying amounts of training data for different models (Promptriever vs. RepLLaMA) raises concerns about the fairness and validity of the comparative performance analysis.
- The performance improvement on in-domain retrieval is very marginal. I guess the instruction-tuning process may affect the original retrieval performance.
- In Table 5, the selected baselines are not strong on BEIR benchmark. For example, E5-mistral has achieved 56.9 on BEIR. I think the authors should compare their methods with more advanced baselines.
- A minor suggestion: please use `` and ‘’ (two single quotes) to generate double quotes in LaTeX.

### Questions
Please consider to address my concerns in Weaknesses.

### Soundness
3

### Presentation
4

### Contribution
3
