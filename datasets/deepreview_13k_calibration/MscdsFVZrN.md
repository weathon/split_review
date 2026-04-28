# ALLaM: Large Language Models for Arabic and English

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 3, 8, 8

## Abstract
We present \model{}: \textbf{A}rabic \textbf{L}arge \textbf{L}\textbf{a}nguage \textbf{M}odel, a series of large language models to support the ecosystem of Arabic Language Technologies (ALT). \model{} is carefully trained considering the values of \emph{language alignment} and \emph{knowledge transfer} at \emph{scale}. Our autoregressive decoder-only architecture models demonstrate how second-language acquisition via vocabulary expansion and pretraining on a mixture of Arabic and English text can steer a model towards a new language (Arabic) without any catastrophic forgetting in the original language (English). Furthermore, we highlight the effectiveness of using parallel/translated data to aid the process of knowledge alignment between languages. Finally, we show that extensive alignment with human preferences can significantly enhance the performance of a language model compared to models of a larger scale with lower quality alignment. \model{} achieves state-of-the-art performance in various Arabic benchmarks, including MMLU Arabic, ACVA, and Arabic Exams. Our aligned models improve both in Arabic and English from their base aligned models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces ALLAM, a large language model for Arabic and English. The authors demonstrate the effectiveness of their training and alignment strategy for achieving state-of-the-art performance on several Arabic benchmarks.

### Strengths
Focus on Arabic Language: The paper specifically addresses the need for high-quality language models for Arabic, a language with a significant number of speakers worldwide and relatively fewer resources compared to English.  This focus fills a gap in the current landscape of large language models.    

Comprehensive Training and Alignment Strategy: The authors employ a thorough approach to training and aligning ALLAM. They experiment with different data mixtures, vocabulary expansion techniques, and use both supervised fine-tuning and preference training to achieve optimal performance.    

State-of-the-art Performance: ALLAM achieves state-of-the-art results on various Arabic benchmarks, demonstrating the effectiveness of the proposed techniques.  The authors also show that their model maintains or enhances English performance compared to the base Llama-2 model.    

Exploration of Second Language Acquisition: The paper investigates the use of second language acquisition techniques for LLMs, which is a promising area of research.  The authors show how pretraining on a mixture of Arabic and English text can lead to effective learning of Arabic without catastrophic forgetting in English.    

Detailed Methodology: The paper provides a detailed description of the training methodology, data curation process, and evaluation setup.  This transparency allows for reproducibility and facilitates future research in the field.   

Commitment to Openness: The authors express their intention to make the ALLAM models openly available to the community, which promotes collaboration and further development of Arabic language models.

### Weaknesses
The authors should clearly state the originality of their work. While the paper builds on existing techniques such as second language acquisition for LLMs, it is not clear what specific novel components are being introduced. Is it the particular training recipe, the alignment strategy, or the focus on Arabic? A clear statement of originality is essential for establishing the contribution of this work.

Error Analysis:
The error analysis presented is currently insufficient. The authors need to go beyond simply stating that some evaluations provide more signal than others. A deeper dive into the types of errors made by the model on different benchmarks is necessary. What are the common patterns in incorrect predictions? Are there specific linguistic constructs or knowledge domains where the model struggles? Addressing these questions will provide valuable insights into the limitations of ALLAM and potential avenues for future research.


Additional Areas for Improvement:
Motivation for changing training data distribution: The authors mention changing the training data distribution for the 30B model. The motivation behind this change is not entirely clear and should be elaborated upon.
Fair comparison of models: The paper touches upon the difficulty of comparing models due to variations in training data size, architecture, and other factors. While comparing to larger models is a reasonable approach, the authors could consider additional metrics or analyses to further ensure a fair comparison.
Instruct model vs. base model results: The authors justify reporting results for the instruct model instead of the base model. However, providing some comparison or insights into the performance difference between the base and instruct models could be beneficial.

### Questions
...

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a series of LLMs for Arabic adapted from Llama2 as well as training from scratch.  The paper gives technical details of the pre-training, alignment and evaluation of these models.

### Strengths
The paper gives the details of the training of Arabic LLMs, including training from scratch and contunue training from Llama2.  The result Arabic LLMs achieve SoTA on Arabic benchmarks.

### Weaknesses
This is mainly a technical report rather than a research paper.  I do not see novel ideas or methods proposed.

### Questions
none

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents a ALLaM: a family of large language models for Arabic and English, based on LLama-2 family of models.

The paper shows a method that can customize an existing LLM (like Llama) to acquire a much better performance at another language that was not included at all the original training of the model, without destroying the LLM's performance on previous language (i.e. second language acquisition).

The paper shows that second language acquisition can be done by augmenting the model in two major steps: 1-vocabulary expansion, and 2- carefully pre-training on mixture of new language and old language. This way the second language acquisition is not accompanied by catastrophic forgetting of the original language.

The paper includes a lot of experiments and comparisons with different baselines, including training from scratch. Showing that their second language acquisition method beats training from scratch. Many evaluations, both automated and human-evals are included in the paper.

### Strengths
Originality: As far as I know, this is not the first work to fine-tune llama-based models for Arabic or other language acquisition. In my opinion, the main originality source in this paper might be the data curation effort, and the vocabulary expansion and continual pre-training without loss of original language. For example, the finding that initializing the embedding of the new tokens from averages of smaller tokens in the original tokenizer is an very useful finding and I expect to see it being used more in the future.

Quality: The effort spent in human evaluation and curation of the data is notable, and I hope this dataset gets released, at least partially for the research community to build on. The comparison against other Arabic-enabled LLMs are also very comprehensive and useful.

Clarity: While many typos and non-standard terminology exist and are highlighted in the weaknesses section. The paper is still mostly easy to follow and read. The description of the datasets and training/evaluation procedure is particularly clear and concise.

Significance: Arabic is definitely an excellent language choice for this exploration of second language acquisition, given that the original LLama2 family of models do not train on Arabic at all (as shown in Table 10 in the original Lama2 report), and that means that the tokenizer and model are not very well trained for Arabic. Also, Arabic is definitely an underserved language in the LLM, especially given the size of its native speakers population (fifth most in the world, roughly 400M people).

### Weaknesses
Even though the paper is mostly well-written, it's littered with typos, non-standard terminology and missing references:
- "Fertility rate": very confusing term, it's not really a rate, and is usually referred to "fertility score": https://arxiv.org/pdf/2310.08754 
- Figure 8 is not referenced anywhere as far as I can see.
- line 475: missing reference
-  line 294: missing reference
- line 291: lower case "we"
- line 072: training of "these" 
- lines 151-153: DA identification is a hard task ... classifying the data to DA is not very difficult (opposite claim)  
- line 155: in-house in-house  

- I would have loved to see some newer Arabic models like Silma included in the comparisons for this paper, or a comparison against the models in the huggingface Arabic leaderboard.

### Questions
- How many Arabic tokens already existed in the LLama2 backbone, and how many were added after the expansion?

- Why did the training mix change for the 34B model specifically? (lines 286-292) 

- I would be interested to compare allam against Silma Arabic llms

- Please consider evaluating on more dataset like AlGhafa benchmark or including ALLAM on the huggingface Arabic leaderboard.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper describes the process for building ALLAM, an LLM trained on Arabic and English. Details about the training data and each stage of the training process are presented. Various evaluations are performed, including both automatic benchmarks like Arabic MMLU and human evaluation.

### Strengths
This is a timely paper, as many research groups are working on building LLMs for languages other than English. The paper presents useful details on their experience and will serve as a good reference.

### Weaknesses
There are no major weaknesses in my opinion. I would recommend adding discussing about other efforts in building LLMs for non-English languages and explaining how yours compare, i.e. moving some of the Related Work into the main paper. Especially it would be useful for the reader (who isn't referring to the appendix) to know about Jais and any other Arabic-centric model.



### Questions
1. Page 3 says 4T English tokens then and 5.2T tokens for 30B pre-training. It was a bit confusing what is the 5.2T. Also Table 1 lists English as 660B tokens from mixed corpora -- is this a subset from the 4T English Only column?

2.  Fig 5/6: for my display, there are black lines in the legend (e.g. Arabic/English MMLU) but only red/orange lines in the figure.

3. I am curious if you have considered using something other than Llama2 as your base model. If so, why did you pick Llama2 in the end?

### Soundness
4

### Presentation
4

### Contribution
3
