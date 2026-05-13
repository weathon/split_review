# Embedding File Structure for Tabular File Preparation

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
We introduce the notion of file structure, the set of characters within a file's content that do not belong to data values.
Data preparation can be considered as a pipeline of heterogeneous steps with the common theme of wrangling the structure of a file to access its payload in a downstream task.
We claim that solving typical data preparation tasks benefits from an explicit representation of file structure.
We propose a novel approach for learning such a representation, which we call a structural embedding, using the raw file content as input.
Our approach is based on a novel neural network architecture, composed of a transformer module and a convolutional module, trained in a self-supervised fashion on almost 1M public data files to learn structural embeddings.
We demonstrate the usefulness of structural embeddings in several steps of a data preparation pipeline: data loading, row classification, and column type annotation.
For these tasks, we show that our approach obtains performances comparable with state-of-the-art baselines on six real-world datasets, and, more importantly, we improve upon such baselines by combining them with the structural embeddings provided by our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a model named RenEmb to embed the structure of the tabular data.

There are 3 components of the model, namely pattern tokenization, then structural transformer, and CNN.

### Strengths
The paper seems well written and clear. The target problem seems to have broad interest and very useful importance. The approach seems feasible to be used by many researchers.

### Weaknesses
The major concern of the paper could seem:

a) The model seems only BERT-style and there seems no comparison to real LLM's such as chatgpt. The comparison to LLM's should be a core result, as many researchers have observed the level of paradigm shift by those new LLM.

b) The 1st step of pattern tokenization could make use of structure data that exclude the text content. Would it be enhanced if we have both structure and text? For the new hybrid approach of RenEmb + Strudel, can you let us know the reason that two concatenated models seem more advanced than just 1 stage?

### Questions
Would the new method work for complex table, not full row and full column?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work introduces a transformer-based model framework designed to embed complex tables in a structurally aware manner. The process begins with pattern tokenization, followed by the use of structurally aware modules to capture the unique structural features of tables. The authors pre-train this framework on a dataset of 1M tabular files and evaluate its performance against state-of-the-art baselines.

However, the paper's contributions seem not so solid to me. The practice of employing structural features to encode structured text is not novel, as evidenced by prior research such as [1], and [2]. The authors' approach of utilizing a human-designed structural pattern tokenization to understand structures, followed by the use of basic modules for encoding, lacks technical novelty.

Moreover, recent debates have emerged regarding the optimal way to encode structured text: a structurally aware approach, or grounding and understanding structured text directly using text language models. The latter method has demonstrated superior performance and versatility across various structural forms, including tables, SQLs, and code, as shown in studies by [3] [4]. 

References:

[1] Li, Yulin, et al. "Structext: Structured text understanding with multi-modal transformers." Proceedings of the 29th ACM International Conference on Multimedia. 2021.

[2] Nassar, Ahmed, et al. "Tableformer: Table structure understanding with transformers." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.

[3] Roziere, Baptiste, et al. "Code llama: Open foundation models for code." arXiv preprint arXiv:2308.12950 (2023).

[4] Xie, Tianbao, et al. "Unifiedskg: Unifying and multi-tasking structured knowledge grounding with text-to-text language models." arXiv preprint arXiv:2201.05966 (2022).

### Strengths
1. The paper is written with clarity, and is easy to understand. 
2. RenEMB shows competitive performance with baselines on three diverse tasks. 
3. RenEMB provides unique solutions to a few stated problems with table representations, including dialect detection, and structural awareness. These experiments show that RenEMB exhibit good structural representation abilities.

### Weaknesses
1. My major concern is on technical novelty and whether the method is up-to-date and competitive with SOTA table understanding generalist LLMs, as stated in the summary.

2. On pattern encoding method: In Section 2.1, I believe the patterns are not applicable to a multilingual setting. For instance, there are no upper/lower letters in Chinese or Korean language. Also, the pattern would be the same for tables with shared headings over a few columns, as the format of your table 1, and one that does not share headings. 

3. On experiment settings: I am not sure if dialect detection and row classification constitute challenging tasks for table understanding. I believe more downstream tasks and finetuning analysis would be necessary. For example, what is the performance of tasks on TableQA
(WikiSQL, WikiTQ).

### Questions
Q1: What is the advantage of RenEMB over methods that directly tokenize tables with bpe and encode the tokenized text as transformers, a practice commonly used in training LLMs, as in Llama, GPT-3, Galactica? 

Q2: Can this method apply to multilingual setting or could be used as a general method accross different kinds of table formats and languages?

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a method RENEMB, which employs transformers and CNNs to extract structural information from sentences. They conduct experiments on dialect detection, table understanding, and column type annotation tasks to demonstrate the effectiveness of RENEMB.

### Strengths
1. The paper introduces RENEMB, which uniquely combines transformers and CNNs, to extract structural information from sentences.
2. RENEMB's effectiveness is demonstrated across multiple tasks - including dialect detection, table understanding, and column type annotation.

### Weaknesses
1. The problem definition in this paper is unclear. While the objective is to better represent the structural information of tabular files, a clear problem definition is absent. The final experiments are conducted on dialect detection, table understanding, and column type annotation tasks. What is the relationship between these three tasks and the paper's objective? Why were these specific tasks chosen?
2. The motivation is unreliable. The paper claims that previous methods primarily focused on semantic improvements while neglecting textual structural information. However, language models like BERT and GPT, during their pre-training phase, learn both semantic knowledge and structural information. Given this, is there still value in training a separate model solely for recognizing text structural information?
3. The paper asserts that "In solving the structural masking task, RENEMB has to learn the difference between special characters that belong within a cell (e.g., a comma delimiting the digits of a number) and those with a structural role (e.g., a comma as a cell delimiter)." However, the Structural Masking Modeling task simply instructs the model on where to output specific symbols; the model cannot differentiate the same symbol's different meanings based on its position.
4. The pre-training task "Same File Prediction" is not clearly described. Firstly, how is this logistic regression classifier obtained? Furthermore, the process of training BERT through this classifier isn't elaborated upon. Additionally, is the task of classifying whether two rows come from the same file reasonable? Different files might have rows with the same structure.
5. The paper lacks ablation studies. As a result, it's unclear how the two pre-training tasks and the CNN structure individually impact the final outcomes.
6. The paper presents a limited number of baseline methods, and they are relatively outdated(between 2019 and 2021). Additionally, the paper lacks analytical experiments to substantiate that the proposed method has learned superior textual structural information.

### Questions
Please see the comments in the weakness part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
