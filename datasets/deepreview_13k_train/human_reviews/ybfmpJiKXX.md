# AIMS.au: A Dataset for the Analysis of Modern Slavery Countermeasures in Corporate Statements

- Decision: Accept
- Scores: 6, 8, 5

## Abstract
Despite over a decade of legislative efforts to address modern slavery in the supply chains of large corporations, the effectiveness of government oversight remains hampered by the challenge of scrutinizing thousands of statements annually. While Large Language Models (LLMs) can be considered a well established solution for the automatic analysis and summarization of documents, recognizing concrete modern slavery countermeasures taken by companies and differentiating those from vague claims remains a challenging task. To help evaluate and fine-tune LLMs for the assessment of corporate statements, we introduce a dataset composed of 5,731 modern slavery statements taken from the Australian Modern Slavery Register and annotated at the sentence level. This paper details the construction steps for the dataset that include the careful design of annotation specifications, the selection and preprocessing of statements, and the creation of high-quality annotation subsets for effective model evaluations. To demonstrate our dataset's utility, we propose a machine learning methodology for the detection of sentences relevant to mandatory reporting requirements set by the Australian Modern Slavery Act. We then follow this methodology to benchmark modern language models under zero-shot and supervised learning settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the use of Large Language Models (LLMs) to identify specific actions companies have taken to combat modern slavery and distinguish these from ambiguous corporate statements. To support this analysis, the paper presents a new dataset comprising around 6,000 modern slavery statements sourced from the Australian Modern Slavery Register, with annotations at the sentence level.

### Strengths
Below, I outline the key strengths of the paper: 

1. The dataset introduced in this paper could prove invaluable for legal professionals, offering a detailed resource for examining modern slavery statements. Furthermore, the annotation guidelines proposed have the potential to be adapted and applied to similar documents across different countries. 
2. The task of distinguishing between specific countermeasures and vague claims addressed by this paper is particularly noteworthy due to the common human difficulty in making such distinctions. The authors demonstrate that Language Models perform reasonably well in this respect, suggesting that these models can be effectively used to support human decision-making processes.

### Weaknesses
The weaknesses are as follows: 

1. I am concerned about the annotation quality of the dataset. The paper notes that 50 statements were annotated by two expert annotators in lines 240-242, but it lacks details on annotator agreement, the total number of sentences annotated, and other relevant metrics on this smaller set. Specifically, it is unclear what the exact annotation task was, whether it was a multi-label classification or a span identification task, and how the annotators were instructed to resolve disagreements. Without this information, it is difficult to assess the reliability of the dataset. Furthermore, the paper should clarify whether the 50 statements were selected randomly or based on some criteria, as this could introduce bias into the evaluation.
2. The paper does not provide a detailed quantitative and qualitative analysis of Large Language Model (LLM) performance. Specific questions remain unaddressed, such as whether certain words or phrases correlate with LLM outputs or how the distribution of relevant sentences identified by LLMs compares to those identified by annotators. For example, it would be helpful to see a confusion matrix to understand the types of errors the LLMs are making. Additionally, it would be useful to know how many different prompts were tested on the LLMs to better understand the models’ responsiveness. The paper should also explore the impact of different prompt formulations on the LLM's performance, including variations in wording, instructions, and examples. It is also unclear if the same prompt was used for all models or if model-specific prompts were developed.

### Questions
I have outlined some questions in the weaknesses section. Additionally, I am curious about the authors' choice not to use traditional metrics such as Fleiss’ Kappa to evaluate inter-annotator agreement.

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
The paper describes an approach to construct a manually annotated dataset for modern slavery countermeasures detection and analysis in text based in Australia.  It also benchmarks modern language models including SLMs and LLMs in  zero-shot and supervised learning settings.

### Strengths
-	The paper is clearly written and well-organized
-	The targeted domain/problem is unique yet very important and the proposed approach can be extended to other similar/relevant use cases
-	Experiments cover variety of setups, different types of SLMs and LLMs and with fine-tuning.

### Weaknesses
 - I think more justifications to decisions made in proposed approach are needed:
        
	- Line 238 – 242: more discussion and justifications are needed to explain the need for such different subsetting and annotation approaches. 
	- Please justify/further discuss the quality of the OCR tools used.
- Since the dataset is the main contribution of the work, details on its annotation process should be moved to main text. For example:

	- 11 questions are mentioned in paragraph starting from line 285, examples of these questions and potential answers should be added in main text. 

	- In line 305 ++ it isn’t enough to mention a company did the annotation. What are the characteristics of annotators (other than being fluent English speakers)? How was training exactly done? these are core details to establish dataset quality.
	- How was the dataset split for train and test?

### Questions
-	Related work can be shortened, the paper is already covering both an introduction and background (around half of the paper is just introductory pages). This is especially important given that most related work isn’t specifically targeting the exact problem at hand.
-	Did you annotate all statements/docs mentioned starting from line 250? 
-	I suggest better formatting and maybe a figure to describe the process starting line 319. There are many numbers, sub-steps etc and it is hard to keep track.
-	There are several IAA measure (e.g., Cohen Kappa), why use the percentage of agreement?
-	Please move details on task definition to the main text, this is an important part of the work and should be made more clear.
-	Line 431: why limit the prompt design to C2? The results in figure 3 shows numbers for all criteria, making that sentence confusing.
-	I suggest adding results for un-finetuned Llama 2. The great effectiveness it is showing compared to GPT-4o is surprising and contradicting with existing literature comparing closed models to Llama 2.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces AIMS.AU, a new benchmark containing 5,731 corporate modern slavery statements for LLMs to assess whether they meet the requirements of the Australian Modern Slavery Act. It details the construction and annotation process. The author benchmarks it over both fine-tuned open (BERT, DistilBERT, Llama2) and closed (GPT3.5-turbo, GPT4o) LLMs and finds zero-shot prompting LLM’s results aren’t comparable to fine-tuned LLMs, indicating dataset’s usage to fill the gap in corporate compliance analysis.

### Strengths
1. The coverage of the dataset is extensive in terms of year and corporate entity (covering 7,270 entities’ statements from 2019 to 2023 after the establishment of Australian Modern Slavery Act). 

2. The dataset focuses on a specific field that could have significant social impact (but limited to Australia as generalizability is not shown) as it manages to enhance LLMs ability to assess modern slavery countermeasures in corporate statements.

### Weaknesses
1. The presentation of this paper is subpar. It relies too much on text and does not take advantage of tables or figures. Some important information is either missing or in the Appendix instead of the main paper. See detailed comments in the "Questions" section below. 

2. Experiments are limited (order in priority). 
   - It only includes closed LLM in the setting of zero-shot prompting LLMs. The comparison between zero-shot open LLM and fine-tuned open LLM is interesting to see.

   - Few-shot and chain-of-thought prompting are missing. Closed instruction finetuned LLMs takes advantage of prompting techniques. It would be interesting to see how much improvement they will make using these two prompt fashions.

   - It only includes Llama-2-7b. Comparison between different size open-weight LLMs before and after fine-tuning is interesting to see.

   - Not benchmark the recent open-weight LLMs (like Llama-3)

3. The broad impact of this dataset is limited. The criteria for LLMs to identify is very specific to the Australia Modern Slavery Act. Can the learnings be transferred to "UK Modern Slavery Act 2015" which is similar? 

4. Benchmark task doesn’t take full advantage of the dataset. The author can formulate a better task to benchmark LLMs or VLMs. There is image information in the dataset which could potentially contribute to classification accuracy.

### Questions
1. Typos in line 174: “CCalifornia” --> “California”

2. A figure depicting the annotation process would be helpful and easier to follow and understand.

3. I suggest putting Section3: related works in the later part of the paper so that important sections (Dataset Description and Benchmark Experiments) will come earlier.

4. The temperature of LLMs is not reported. 

5. Llama-2's size, which is important, is not revealed in the main paper. 

6. The regular expressions to convert text into sentences and extract LLMs’ responses are not revealed.

### Soundness
2

### Presentation
3

### Contribution
2
