# Probing the contents of text, behavior, and brain data toward improving human-LLM alignment

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Large language models (LLMs) are traditionally trained on massive digitized text corpora; however, alternative data sources exist that may help evaluate and improve the alignment between language models and humans. We contribute to the assessment of the role of data sources in human-LLM alignment. Specifically, we present work aimed at understanding differences in the informational content of text, behavior (e.g., free associations), and brain (e.g., fMRI) data. Using representational similarity analysis, we show that word vectors derived from behavior and brain data encode information that differs from their text-derived cousins. Furthermore, using an interpretability method that we term representational content analysis, we find that, in particular, behavior representations better encode certain affective, agentic, and socio-moral dimensions. The findings highlight the potential of behavior data to evaluate and improve language models along dimensions critical for human-LLM alignment.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper is a novel effort at understanding how different data sources (particularly, brain data and behavioural data in addition to text data) can contribute towards human-LLM alignment. The paper also identifies norms for which behavioural data could be more appropriate than textual data.

### Strengths
- The paper identifies the need for non-text related data in brain-LLM alignment
- The paper unifies a number of different norm-categories, but also a large number of textual, behavioural, brain datasets for this purpose.
- The paper performs RSA and RCA to understand the utility of these categories, which are reasonable and appropriate metrics.

### Weaknesses
 - My fundamental issue with the paper is the lack of training pipelines for evaluating these new datasets in a new RLHF or other model, which the authors also note. Unsure of the novelty here, beyond the data aggregation + comparison metrics. Should this paper be in the datasets and benchmarks track? For example, the authors ask 2 research questions, one of which is "b) are these differences useful from the perspective of human-model alignment" and I don't see this question answered in the paper, since no training pipelines were used to verify their claims about the actual utility of behavioural data. Even though they show that behavioural data can capture certain norms better than text data, it's unclear if this difference is significantly important for LLM-human alignment. Could the authors:
* Train an RLHF pipeline on the text+behavioural data and compare it to SOTA LLMs today. Start with a base LLM, train a reward model to rank responses based on the text + behavioural data, fine-tune the base model to produce responses that will be scored highly by the reward model using an RL algorithm such as Proximal Policy Optimization (PPO). Conduct quantitative and qualitative evals on the reward model as well as the final fine-tuned LLM . For example, quantitative evals could be to look at reward values in the RM and logit/surprisal/perplexity values in the policy-tuned LLM and compare them to the text-based RLHF baselines. Qualitative evals could look at reward values on N generations to the same input, as well as standard generations on the final LLM. The final policy-tuned LLM could also be evaluated on standard LLM benchmarking tasks to validate its performance based on, say, the affect-related norms/social norms. The SocKET Benchmark (https://arxiv.org/abs/2305.14938) could be appropriate here.

Minor:
 - This is unsurprising in the case of text, which has been the dominant source for pretraining today’s unprecedentedly human-like language models. (Please CITE)
- Some of these categories (e.g., affective, agential, Social/Moral are likely crucial for human-LLM alignment, though their relevance will, of course, vary depending on one’s ultimate alignment
goals. (Vague. Please CITE)

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper compares word embeddings with behaviour-based and brain-based word norms and tries to characterise their differences using a framework called representational content analysis (RCA) introduced by the authors. The authors first collect a large set of word representations from previous work based on text, behaviour, and brain. The authors then use representational similarity analysis (RSA) to measure the similarity of these word representations and find considerable differences between them. Finally, the authors propose RCA as an approach to interpret the differences.

### Strengths
The paper studies an interesting problem of comparing and contrasting word representations derived from text, behaviour, and brain. There has not been much work along this direction, to the best of my knowledge. In this sense, the work may provide new insights to the research community.

### Weaknesses
I have two major concerns with the work. First, there is a gap between the initial motivation of the work, which is human-model alignment, and the approach taken, which affects the soundness of the work assuming that human-model alignment is the ultimate goal of this work. This is because the paper focuses on comparing word representations derived from text with those derived from behaviour or brain. However, the behaviours of LLMs are probably dependent much more on the parameters of the deep neural network architecture than static word embeddings. It is not clear to me how the findings from this paper that characterize the difference between word embeddings and behaviour-based or brain-based word representations can be used for human-LLM alignment. If the authors could elaborate on how research outputs from this work can be applied for human-LLM alignment, it would strengthen the motivation.

Second, the paper is not easy to follow, which makes it hard to judge its soundness, especially for the proposed RCA. It seems the authors expect the readers to be familiar with existing behaviour representations and brain representations such as what they represent and how they are derived. The authors also expect readers to be familiar with RSA. Also, for the newly proposed RCA, it seems there is not any formal definition of this method. The description in Section 3.3 focuses on implementation details, but what does RCA take in as its input and what does it produce as its output?

### Questions
- It is stated that prospective data for human-model alignment can be grouped into three types: text, behaviour, and brain. Is this a widely adopted understanding? Besides the cited paper Roads & Love 2023 (which, based on its title, does not seem to be related to human-model alignment), are there other references supporting this claim?
- In RSA, how is the transformation from M_1 to \hat{M}_1 learned or derived? Can you elaborate more on the intuition that it is based on the dissimilarities between the rows of M_1 and M_2?
-  What is the input to RCA? What is its output?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper investigates differences in text, behavior, and brain vector representations. For the text representation, the authors use or train fastText, GloVe, and CBOW word embeddings. For the behavior and brain representations, the authors leverage various behavioral datasets and brain datasets, such as EEG data. The authors also construct human-rated word properties across 27 categories, collectively named psychNorms. Experimental results show that these representations tend to cluster based on representational structure rather than the learning algorithm. Using psychNorms, the authors further explore relationships between specific categories in psychNorms and each representation by measuring the R^2 score.

### Strengths
The main strength of this paper lies in its exploration of interesting findings across multiple types of representations. The concept is sound and straightforward, with potential applicability to other modalities.

### Weaknesses
One primary concern involves overclaiming, particularly regarding large language models (LLMs). The authors use fastText, GloVe, and CBOW word embeddings and refer to these as LLMs. However, while definitions of LLMs vary, these models are generally not considered large by 2024 standards. One paper, for instance, suggests that models like GPT-3, which can solve few-shot tasks through in-context learning, meet the LLM criteria, whereas smaller models like GPT-2 do not [1]. Additionally, in the second paragraph of the Introduction, the authors mention “optimizing for next-token prediction” as a training method of LLMs, which does not accurately describe fastText, GloVe, or CBOW. Thus, the results presented here may not reflect human-LLM alignment as suggested. The use of the term 'LLM' is misleading, and the paper's claims about alignment with LLMs are not well-supported by the models used. Furthermore, the analysis relies on relatively simple word embeddings, which might not capture the complex semantic relationships that are typically associated with LLMs. The paper would benefit from using more advanced models that are more representative of current LLM capabilities. There are missing elements in Table 1, such as “?” symbols and Footnote 1.

### Questions
- Who annotates the psychNorms metabase? Are they psychology experts, and how are the categories defined?
- What is the significance of the finding that the similarity between text and brain representations is 0.06 points higher than that between brain and behavior? Why is this an interesting result?
- How would multi-modal models that jointly incorporate text, behavior, and brain representations affect alignment between modalities? Such models might make alignment easier to detect since they learn these relationships directly.
- It would be helpful to highlight the results more prominently in the figures. Due to the current size, they are difficult to interpret and understand the results.
- There are missing elements in Table 1, such as “?” symbols and Footnote 1.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The study conducts a similarity comparison of 10 text, 10 behavior, and 6 brain representations, presenting significant and consistent differences among these data types. The findings suggest that behavior data could be a valuable addition to text in LLM training, with the potential to improve LLM performance and human alignment.

### Strengths
I find the idea of the paper very interesting! I always wanted to explore word representations from different data sources, like behavior and brain. While the approach here is largely theoretical, it lays a foundation for future studies to explore these ideas in practical applications with widely used LLMs. Moreover, the Psychnorms metabase (if presented and described comprehensively) is a valuable contribution since it collects diverse behavioural word properties.

### Weaknesses
Overall, the paper is engaging and easy to follow, but certain points lack comprehension and would benefit from additional clarifications. As someone familiar with many of the datasets used, I find the presentation of these resources somewhat incomplete, and I am not sure how reliable are the results/claims of this work. Providing further clarifications and adding an Appendix describing the content and preprocessing of the datasets, would be a good start to address some of the following concerns.

Starting from the data collection and preprocessing: 

PsychNorms is the metabase of what you call “behavioral word properties”. I would suggest providing further details of the metabase statistics and what it contains, the total size of the vocabulary, and a brief discussion on the norms, their overlap, etc. Table 1 provides a high-level overview but it would enhance the paper's clarity to provide further details. For example, for the THINGS database, it would be helpful to clarify that it is a "neural network trained on similarity judgments for real-world images". I recommend creating an Appendix and adding there additional information per representation.

Regarding the “brain” representations, it seems you used the CogniVal vectors provided by Hollenstein, 2019.  Did you use the Harry Potter, Alice and Pereira words? Please provide further details in the Appendix. The CogniVal database provides 100, 500, and 1000 random voxels. How do you make sure they indeed encode semantic information and not random brain signals? I suggest that to obtain word-level representations from neuroimaging data, the authors consider applying a Gaussian distribution over the fMRI voxels at the specific timestamp corresponding to each word, as demonstrated in [this study by Li et al., 2023](https://openreview.net/pdf?id=ZobkKCTaiY). Alternatively, word-level fMRI datasets are available, such as [Mitchell et al., 2008](https://www.science.org/doi/10.1126/science.1152876) and [Anderson et al., 2013](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00043/43388/Visually-Grounded-and-Textual-Semantic-Models). 

Additionally, the details of processing the representations remain unclear. Did you perform any additional training on the vectors? The asterisk in the Figure 1 caption suggests, "*trained as part of this research" but no further information is provided. Moreover, the supplementary materials include only the *psychNorms* dataset and some notebooks, but without output examples, making it difficult to understand your implementation. How did you address the dimensionality or feature differences across modalities? For instance, CogniVal provides different feature dimensions for each dataset within fMRI, EEG, and eye-tracking data (e.g., *ucl_scaled.txt* has 5 features, *gecoscaled* has 7, and *dundeescaled* has 14). Did you use PCA or any other technique for dimensionality reduction?

Finally, it would be helpful to indicate the final vocabulary size for each representation, considering it is restricted to the intersection with the combined norm, behaviour, and brain vocabularies.

Regarding the methodology/results: 

- Lack of clarity: RCA is not fully comprehensive. I recommend the authors to clarify how they evaluate and make sure Representational Content Analysis works as it should. Is it dependent on dimensionality variations? It is also not clear how you identify and measure the psychological information in the representations. I suggest providing further details about your implementation in the Appendix.

- Overclaiming: You need to soften your claims in some parts of your work regarding how the brain does not present a promising resource for human-model alignment. This finding might be affected by the random voxel representations you used from the CogniVal dataset. There seems to be a data type bias, probably as a result of the preprocessing that the data creators used to create the representations, so this is why the type of data has a more significant effect on representational structure than the choice of the learning algorithm. 
This is briefly mentioned in lines 318-319 but is not highlighted as much as it should be.

The titles(claims) of subsections 4.2, and 4.3 do not seem to fully represent the content of the sections (figures and analysis of results). For 4.2, since you use the psychNorms metabase as targets there might be a bias in text&behavior compared to text&text? Also, it seems to me that the title of this subsection is misleading: 4.2 BEHAVIOR DATA CAN RIVAL TEXT IN PSYCHOLOGICAL BREADTH AND DEPTH. Why breadth and depth? The difference is approximately 0.1 between the text and behaviour data and only on 7 out of the 27 norm categories. Regarding 4.3, the main finding is that “Text & Behavior” (descriptively) has higher similarity than “Text & Text”, but the title is “4.3 BEHAVIOR CAPTURES UNIQUE PSYCHOLOGICAL VARIANCE” (probably this refers to the "Text & Behavior, on the other hand, tends to perform better on affect-related norms"?). 

Minor: Both subsections start with “The *last* section revealed/hinted that..”. It is confusing to the reader what you refer to as last. If you refer to the previous subsections, I would suggest replacing *last* with *previous*.

### Questions
1. Thanks for providing the supplementary material, but since the data folder is partially empty it is hard to reproduce your work. It would be more helpful to actually see the notebook outputs, for example, what is the len(name_combs)? It would help the reader to get an estimate of how many final representations you compare. Figure 1 is the original size of the vocabularies, but you only use the overlap to run the experiments and present your results. Could you please provide further dataset/representation details or motivation as to why you have decided not to do so?

2. For people not familiar with the psychological norm datasets used, there is confusion between the behavioural and psychological norms. Could you please explain how “the behavior representations encode psychological information of equivalent or even superior reach and quality in comparison to their text-based cousins”? How do you measure that representations encode a broad range of psychological information? 

4. By reading your paper it is not clear what is included in what behavioral dataset. Could you explain what is this out-of-the-box behavior representations in lines 186-187: “We use a mixture of out-of-the-box behavior representations and those we train ourselves”. 

5. There is also a need to further explain the footnotes 3 and 4. I suggest having further details of the data and your implementation in the Appendix, as this could help handle those obscurities.

6. Since you already use the THINGS dataset, was there a reason for not using the fMRI, EEG, or MEG representations from https://things-initiative.org/ ?

7. Did you try to visualize some examples from your results as a qualitative check? I would recommend visualizing concrete word examples in a t-sne plot so that the readers can actually get an illustration of the correlation between the representations. For example, the word “x” is present both in the word embeddings, the Psychnorms, and the brain representations. Visualizing some examples can also help in the approximation of the relation between the representations and their data types. 

8. It seems to me that in some parts, there is no clear distinction between correlation and performance. For some claims you should consider replacing “outperforms” or “superior/higher performances” with “there is a higher correlation” or “higher similarities”.

8. Minor improvements for paper clarity: 

- Please fix the references throughout the text to avoid having **?** instead of the corresponding reference or citation.
- Please rephrase or further clarify lines 101-102: “Furthermore, because the representations are at the individual word level, they can be directly probed using widely available word ratings (norms)”.

### Soundness
2

### Presentation
2

### Contribution
3
