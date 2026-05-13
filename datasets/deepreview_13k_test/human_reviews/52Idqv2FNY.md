# Correlating and Predicting Human Evaluations of Language Models from Natural Language Processing Benchmarks

- Decision: Reject
- Scores: 8, 3, 5, 3

## Abstract
The field of natural language processing (NLP) historically evaluated language models using benchmarks with automated metrics. However, the recent advent of highly capable chat language models (LMs) has caused a tectonic shift from NLP benchmarks to human evaluations. The relationship between these two evaluation processes is unclear and underexplored for chat LMs. Broadly, to what extent are human evaluations and NLP benchmarks correlated with one another? How well can computationally inexpensive and automated benchmarks predict expensive and time-intensive human evaluations? Which benchmarks provide predictive signals for human preference for LMs? What role, if any, should benchmarks play in the era of chat LMs? To answer these questions, we conducted a large-scale study of the relationships between human evaluations and benchmarks. We show that benchmarks are broadly highly correlated with human evaluations, and we identify which benchmarks exhibit strong correlations with human evaluations and which do not. Having established that reliable correlations exist, we fit models to predict a language model’s human evaluation scores from its academic evaluation scores and provide evidence that such predictive models can generalize across LM scales.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper initially explores the correlation between NLP benchmarks and human evaluation. With the advent of increasingly capable LLMs, human evaluations have become a steady and major alternative choice to evaluate the efficacy, performance and capabilities of LLMs. An important question that generally arises with the choice is whether NLP benchmarks are useless since human evaluations are costly and time consuming and are not always a gold standard. Where do NLP benchmarks fall? This paper explores this question and also explores the possibility of predicting human evaluations from NLP benchmarks. 

Two key questions are asked:
- To what extent are human evaluations and NLP benchmarks correlated?
- How well can benchmarks predict expensive and time-intensive human evaluations?

The researchers use all the Llama chat-2 models (7,13,30 and 70B parameters) to establish this, which were trained on 2T tokens and fine-tuned using SFT and RLHF. Human evaluations are collected by evaluating the Llama2 chat models pairwise against ChatGPT 3.5 on dataset a of single-turn and multi-turn prompts, where responses are sampled from each model. 3 Human annotators independently provide a pairwise comparison on the Likert scale (1 to 7, where 1 means chat llama preferred and 7 means chatgpt 3.5 preferred). uThey end up doing a large-scale study spanning factual questions, language assistance, writing, procedural questions, reasoning and many more.  The Chat Llama 2 models are evaluated on many popular NLP benchmarks right from AGI Eval, Ai2 Reasoning Challenge, Big Bench Hard, Boolq, commonseqa, GSM8k, MMLU, MATH, QuAC, PiQA and many more. Standard evaluation processes are used. 

The findings revealed that NLP benchmarks are broadly highly correlated with human evaluations, with certain benchmarks showing particularly strong correlations. The most predictive benchmarks included specific subsets of MMLU (covering topics like nutrition, human aging, and sociology), portions of BIG Bench Hard, HellaSwag, ARC, RACE, PIQA, Natural Questions, QuAC, and CommonSenseQA. However, some benchmarks showed weaker correlations, including ETHOS, Kth Sentence, most of Inverse Scaling, OpenBookQA, COPA, SciBench, and SIQA.

Using overparameterized linear regression, the researchers successfully demonstrated that NLP benchmark scores could predict human evaluation scores with reasonable accuracy. Despite the small sample size of only four models, leave-one-out cross-validation showed promising results, suggesting that faster and cheaper NLP benchmarks might effectively predict slower, more expensive human evaluations in many cases.

The authors note several limitations, including the small sample size, the assumption of linearity in their predictive models, and potential limits to generalizability across different model families thus rounding up the study and paving the way for future work as well.

### Strengths
1] The question at the center of the paper -- "Correlation between NLP benchmarks and Human Evaluations," is an important central question to NLP evaluation in general. Human Evaluations are considered (somewhat so) the gold standard of evaluation but are extremely time-consuming and expensive to run; as models get more capable the human evaluations also get even more costlier because now we require experts to evaluate vs requiring less advanced folks earlier, but we can reliably construct more difficult benchmarks for models, so if these two things are correlated, perhaps lesser focus can be placed on human evaluations. 

2] Predicting Human Evaluations is a difficult task, and LLMs as judges are being increasingly explored as an alternative to human evaluations. The method in the paper also showcases some important insights into this process.

### Weaknesses
1] The small sample size brings into question the generalizability of these insights and results.

2] Only uses GPT-3.5 as the comparative model, no insight is provided into why this is the case? And also lacks any discussion of whether chatgpt 3.5 is a reasonable choice of a baseline. 

3] Perhaps a granular analysis of what makes a benchmark more correlated? Is there something common in the correlated benchmarks? This would also pave the way to designing and determining better benchmarks.

### Questions
1) Why chatgpt 3.5? Could you justify the choice of this model? Why was chatgpt 3.5 the model chosen for comparison, is it a reasonable choice for a baseline? 

2) Could you generally talk about the distribution of the Likert scale that you got from the pairwise evals? Was there anything at all in which chatgpt was substantially better and generally chosen? (Assumption here that I suppose llama-2 would be usually better than chatgpt 3.5 in all cases)

3)  if these outputs were obtained from Chatgpt 3.5, which API was it received from, and what was the exact cutoff (e.g., ChatGPT-3.5-0604, etc.)?

4) Pairwise evals ultimately show revealed preferences and model choice between two outputs. Do you think this translates to human evaluation directly on model outputs (not comparisons) on NLP parameters like coherence, semantic relevance, factual relevance, etc.? Could you comment on the choice of pairwise evals?

5) Just a general question about related work: is there no related work? (while this correlation aspect might not have been explicitly studied), Studies have considered which of them is better in MT, summarization, and other NLP areas. Can you provide a more comprehensive overview of related work, including studies that have compared human evaluations and benchmarks in specific NLP tasks like MT/Summarization, and contextualize this work in the broader field?

6) Could you conduct a detailed analysis of features/characteristics shared by highly correlated benchmarks? I think that would help a lot in designing benchmarks in the future.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies the relationships between the evaluation results of automated NLP benchmarks and those of human evaluation. It mainly revolves around two research questions: how well human evaluations and NLP benchmarks are correlated with each other, how well NLP benchmarks can predict human evaluation. Specifically, the authors develop a set of 1917 prompts organized by areas, categories, and subcategories, selects four LLMs from Llama 2 family, gets their reponses to the prompts, and conducts a large-scale pairwise human evaluation. The evaluation results of the four models on many automated NLP benchmarks are also derived. Then, the paper analyzes the correlations between human evaluation and automated NLP benchmarks and finds that they are highly correlated in most cases. Furthermore, the authors decompose the correlation matrix into rank-one components and demonstrate the communities between human evaluations and NLP benchmarks. Finally, the authors tried to fit a regression model to predict the human evaluations with automatic evaluation results as inputs.

### Strengths
- The research question of this paper—the relationship between evaluation results from automated NLP benchmarks and human evaluations —is generally important and meaningful. Recently, numerous automated benchmarks and human evaluations have emerged separately, but there has been little research on the relationship between them.
- This paper covers many automated NLP benchmarks and includes a large-scale human evaluation, which lends a certain level of generality to its results.

### Weaknesses
Although the idea of this paper is beneficial, many obvious flaws diminish its value.

- This study uses only four LLMs, which is too few. This leads to
  - The correlations between automated NLP benchmarks and human evaluation are calculated merely from two four-dimension vectors, which is unreliable 
  - Insufficient experiments for predicting human evaluation from automated NLP benchmarks, despite cross-validation conducted in the paper

- The paper lacks key details, including but not limited to how the prompt set used in human evaluation is obtained, the human evaluation process and its reliability (e.g. inter-annotator agreements), details of how the correlation is calculated (what is ~150 evaluation process?), the settings for linear regression. This not only creates difficulty in understanding but also raises doubt about the rigor of this study.

- The presentation of the paper could be improved. For instance, the font sizes in Fig 3, the upper part of Fig 4, and Fig 6 are too small, making it hard to read.

### Questions
- More LLMs should be covered in this study. I understand the computational cost during inference and the cost in human evaluation, but four LLMs are definitely too few to support subsequent experiments.
- I do need more details of the human evaluation in your study. What makes me most confused is the selection of the prompts. Why don't you use the same question sets as those of automated NLP benchmarks? If there are too many, you can sample from each dataset. Now there is a mismatch between the prompts (questions) in human evaluation and automated NLP benchmarks and the mapping relationship is not clear. Even if ignoring the mismatch issue, you should provide the number of prompts per area and categories used in human evaluation.
- The experiments of one-rank decomposition in Section 3.3 need to be further explained. Can you better state your motivation of conducting this decomposition and what insights can we draw from that?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work attempts to explore the correlation or consistency between common NLP automatic evaluation benchmarks and human evaluations in analyzing and comparing the capabilities of language models. They cover a wide range of datasets and conduct experiments on four different sizes of Llama 2 models and GPT-3.5, employing human annotators to provide evaluation data. They find that there is a high correlation between automatic benchmarks and human evaluations, and they identify which benchmarks show stronger correlations. Furthermore, they also fit models to predict human evaluation scores of language models from academic evaluation scores.

### Strengths
The motivation and research questions of this work are very interesting and significant. Considering that language models are becoming increasingly powerful, many traditional NLP benchmarks may have lost their discriminative power, leading researchers to turn to human evaluations, which are more costly and harder to reproduce. By analyzing the consistency between NLP automatic evaluation benchmarks and human evaluations, this work aims to identify highly consistent benchmarks to simulate human evaluations, thereby reducing evaluation costs. Their experiments cover a large range of datasets and settings, including constructed various categories of human evaluation data and many common NLP automatic evaluation benchmarks, demonstrating a very comprehensive effort.

### Weaknesses
Although the research topic of this work is meaningful, it is also actually very complicated and corresponds to a more challenging analysis process. Even though the work has tried to handle the experimental data and present corresponding results as macroscopically as possible, their experimental analyses remain confusing and fail to help readers capture the main points. From Figure 1 onward, the clarity and readability of the charts decline rapidly, and by Figure 6, it becomes nearly impossible to extract any information as the fonts are extremely small and the visualized results are poorly presented.

Some analytical settings in the paper are unclear or somewhat unreasonable. For example, in line 149, what does the "evaluation process" refer to, and why are approximately 150 combinations calculated in total? What do they represent? Additionally, if I understand correctly, it seems unfair to compare human evaluation results across mixed task types with different NLP automatic evaluation benchmarks that may focus on testing certain different abilities.

### Questions
Please refer to Weaknesses.

### Soundness
4

### Presentation
2

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
This paper studies the relationship between NLP benchmarks and human evaluation results and aims to understand what roles NLP benchmarks should play in the era of LLM. They conduct human evaluations on four Llama 2 chat models and calculate the correlation between human evaluation results NLP benchmarks, spanning from open-domain QA, MMLU, and safety/adversarial datasets. They find that most NLP benchmarks correlate well with human evaluation results, and it is possible to predict human evaluation results based on scores on NLP benchmarks.

### Strengths
- This paper studies a very important problem: whether scores on NLP benchmarks correlate with human evaluation results. This can potentially guide researchers to construct better benchmarks
- This paper studies the possibility of using NLP benchmarks to predict human evaluation results. Considering the efforts of human evaluation, the problem studied in this paper can help us develop LLMs faster.

### Weaknesses
- The experiment parts are highly unclear and hard to comprehend. It is unclear how the correlations are calculated between human evaluation and NLP benchmark scores. There is even no **Experiment Setup** section in this paper, and the part that most looks like the experiment setting is the first seven lines of Section 3. After repeatedly reading those lines, I still cannot understand how the correlations are calculated. Precisely,
    - How do you aggregate the scores of different shots?
    - Why do you aggregate the results of different shots?
    - What is the number of shots?
    - How is the prompt formatted?
    - How are the demonstrations in the few-shot selected?
    - Where does the number *150* on Line 148 (page 3) come from?
    - How is the human evaluation conducted? How many samples are there in the single-turn and multi-turn dialogues? How are the topics selected? What is the distribution of the data?
    - If the paper only uses four models, is the correlation coefficient calculated using only the benchmark scores of 4 models and the human evaluation results of the models? This means we are only calculating the correlation coefficient between two sets for numbers with only four elements in each set. 

- There are only four models used in this paper: the four chat models in Llama-2 with different numbers of parameters. The abilities of those models are very distinct, so it is easier for human evaluators or NLP benchmarks to distinguish the strengths of these models. A more challenging and realistic scenario is to consider more LLMs whose abilities are more diverse.

- The figures in the paper are terribly and poorly formatted. Those figures do not seem like they are designed to be read. The font sizes in the figures are too small to read and clustered together. I need to zoom in to 400% on my computer to see the words.

- Section 3.3 is highly unclear, without explaining what the *communities* this section is discussing and with no experiment settings that allow the readers to understand what is happening now. 

Considering that the experiment setting is highly unclear and the results are poorly presented, it is impossible to evaluate the contribution of this work. The paper requires major refinement. However, the paper studies an important problem, and I encourage the authors to keep working on this topic.

### Questions
- Q1. How do the authors conduct the experiment using the Llama-2-30b model?  In fact, there is no 30b model in the LLama2 series, and I assume the authors are referring to the Llama-2-34b model. However, even Llama-2-34b-chat (or the base model) is not officially released, so I wonder how this paper conduct experiments using Llama-2-34b-chat.

### Soundness
2

### Presentation
1

### Contribution
1
