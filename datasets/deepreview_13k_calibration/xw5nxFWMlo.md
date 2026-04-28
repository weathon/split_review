# Retrieval meets Long Context Large Language Models

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8, 6, 8

## Abstract
Extending the context window of large language models~(LLMs) is getting popular recently, while the solution of augmenting LLMs with retrieval has existed for years.
The natural questions are: \emph{i) Retrieval-augmentation versus long context window, which one is better for downstream tasks?}~\emph{ii) Can both methods be combined to get the best of both worlds?}
In this work, we answer these questions by studying both solutions using two state-of-the-art pretrained LLMs, i.e., a proprietary 43B GPT and \llama. 
Perhaps surprisingly, we find that LLM with 4K context window using simple retrieval-augmentation at generation can achieve comparable performance to finetuned LLM with 16K context window via \emph{positional interpolation} on long context tasks, while taking much less computation.
More importantly, we demonstrate that retrieval can significantly improve the performance of LLMs regardless of their extended context window sizes. 
Our best model, retrieval-augmented {\llama} with 32K context window, outperforms GPT-3.5-turbo-16k and Davinci003 in terms of average score on nine long context tasks including question answering, query-based summarization, and in-context few-shot learning tasks.
It also outperforms its non-retrieval {\llama}-32k baseline by a margin, while being much faster at generation.
Our study provides general insights on the choice of retrieval-augmentation versus long context extension of LLM for practitioners.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the comparison between retrieval-augmentation and long context extension for LLMs across various downstream tasks. It demonstrates that retrieval-augmentation can improve the performance of LLMs irrespective of context window size. They also reveal that shorter context window LLM with retrieval-augmentation can perform close to longer context LLM finetuned via positional interpolation, while taking much less computation.

### Strengths
1. The paper delves into the significant yet underexplored problem of retrieval-augmentation versus extended context windows, presenting a comprehensive study that spans a variety of popular long-context tasks to compare the two methods.
2. The findings that a "shorter context window LLM with simple retrieval-augmentation at inference can perform on par with a longer context LLM fine-tuned through positional interpolation," and that "retrieval can enhance the performance of LLMs regardless of their context window size," offer valuable insights for future research endeavors.

### Weaknesses
1. The authors attribute the superior performance of retrieval-augmented long context LLMs (e.g., 16K and 32K) over the 4K context LLM in a top-5 setting to the 'lost-in-the-middle' phenomenon. However, since the 'lost-in-the-middle' conclusions have not been widely recorganized, conducting an ablation study would be instrumental in supporting this hypothesis. Specifically, the authors should investigate whether the performance degradation is due to the model's inability to effectively utilize information in the middle of the context window, or if it is caused by other factors such as the retrieval of less relevant documents in the top-5 setting. A controlled experiment where the position of the relevant document is systematically varied would provide more conclusive evidence.
2. The authors use LLM performance metrics to infer the efficacy of different retrieval modules (Table 4). However, it is questionable whether a retrieval system with better LLM performance necessarily correlates with enhanced retrieval capability. The authors should incorporate some form of automated evaluation or a case study on retrieval performance to substantiate this. For example, metrics such as precision, recall, and F1-score on the retrieved documents could be used to directly assess the quality of the retrieval modules, independent of the LLM's performance. Furthermore, analyzing the types of documents retrieved by each module and their relevance to the query would provide a more detailed understanding of their strengths and weaknesses.

### Questions
1. The OpenAI GPT series also offers variants with different context lengths (e.g., GPT-3.5-turbo, GPT-3.5-turbo-16k). Including their results in Table 2 and examining whether the conclusions still hold would be beneficial.
2. Regarding the results presented in Table 2, it is unclear how the best retriever was determined. Is a better-performing retriever module always associated with improved LLM performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This research paper compares two methods of handling context in large language models (LLMs); extending the context window and retrieval augmentation. The main contributions of this study are as follows;

1. The researchers conducted experiments using two state-of-the-art LLMs, a proprietary 43B GPT and LLaMA2 70B on seven tasks related to long context question answering and summarization.
2. The results demonstrate that retrieval significantly improves the performance of both 4K) and long (16K/32K) context LLMs. Surprisingly LLMs, with a context size of 4K, when combined with retrieval perform close to LLMs with a context size of 16K without incurring additional overhead.
3. It is also shown that extending the context window and retrieval augmentation complement each other. The performing model, LLaMA2 70B 32K enhanced by retrieval outperforms ChatGPT 3.5.

To summarize this paper provides insights into the combination of retrieval techniques and long context strategies for constructing improved language models (LLMs). The key findings indicate that retrieval is beneficial regardless of the context window size and extending the context window alongside retrieval augmentation offers reinforcing solutions, than competing ones.

### Strengths
This research study aims to examine and compare two approaches, for improving Large Language Models (LLMs); extended context utilization, and retrieval mechanisms. The authors utilize two LLMs with 43 billion and 70 billion parameters, which allow for better integration of context. Through experimentation, they assess the performance of these models across challenging datasets related to long context Question Answering and summarization.

The research provides insights demonstrating that retrieval mechanisms offer performance benefits regardless of the context length. Additionally, the study highlights how these two techniques complement each other. The paper is skillfully written, presenting an explanation of its motivation, background, experimental methodology, and analytical framework. The introduction effectively places the research in the context of work on long-context understanding, efficient attention mechanisms, and retrieval augmentation. This establishes a foundation for the study.

The authors thoughtfully compare their findings with research, including benchmark models like ChatGPT. This offers a view of the progress made in this field. Furthermore, the paper raises questions about comparing context understanding and retrieval as strategies for enhancing LLMs encouraging further exploration in this area. The extensive original experiments conducted contribute significantly to our understanding of these methods, within the community.

Overall the results of the study are highly significant, for the research community as they shed light on the effects of combining retrieval and long context.

### Weaknesses
Most studies primarily focus on improving models during inference with attention given to examining the impact of training methodologies.
There is a lack of analysis when it comes to integrating context and retrieval techniques like determining the ideal number of retrieved passages.
Experiments have not yet been conducted on contexts, which span 64,000 tokens and this could pose additional challenges.
There is a need, for evaluations against advanced methods in long context modeling and further benchmarking is necessary.
The experiments section would be more informative if it provided information about characteristics and task formats.
The related work section should clearly highlight the contributions of this study compared to work like LongBench.
There is a discussion regarding the implications and limitations associated with the techniques being investigated.
It's important to note that previous research has explored the concepts of context and retrieval. This study should acknowledge and build upon existing literature.
There are opportunities to explore approaches in combining retrieval and context that merit investigation.
Further validation is required to assess the suitability of these techniques, for contexts.

### Questions
The paper mentions another study called LongBench that reached conclusions regarding the impact of retrieval, on context models. It would be beneficial if the authors could further analyze the differences that led to these opposing observations.

Have you tried training the retriever and LLM from start to finish of just adding augmentation during inference? How does the performance compare in cases?

When retrieving passages how do you determine the optimal number to use? Does performance level off. Decline with many passages?

For context models like those with 64K or 128K tokens do you believe retrieval would still provide benefits?. Does its value decrease after a point?

Could you provide analysis and examples that demonstrate the phenomenon you hypothesize as "lost in the middle"?

Are there any approaches besides using long context and retrieval augmentation that you could compare to? For example memory or hierarchical attention.

Although the paper focuses on QA and summarization it would be interesting to see if similar conclusions apply to tasks.

Have you considered examining the impacts and limitations of building larger LLMs? A brief discussion, on this topic would be valuable.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies tasks that require reading / reasoning over long documents, and considers two commonly used approaches: retrieval augmentation and long-context LLMs. By experimenting on 7 long-context tasks from the Scroll and LongBench benchmarks, this paper first compares the two solutions and finds that a retrieval-augmented LLM with standard context windows can perform close to long-context LLMs. It further shows, contrary to the finding of a contemporary paper, that retrieval helps improves the LLM performance regardless of the context-window size. As a result, their best-performing model, a retrieval-augmented Llama2-70B-32K (Llama 2 finetuned to 32K context window with positional embedding interpolation) outperforms ChatGPT-3.5 on 5 of the 7 tasks.

### Strengths
- This paper investigates a widely-interested problem, long-context modeling, and compares two most popular solutions, long-context LLMs and retrieval-augmented LLMs. Its results and insights are hence of considerable interest to the research community.

- The paper is clearly written, and the experiments are relatively extensive. In particular, it achieved positive results showing retrieval augmentation and long-context LLMs can be complementary to each other, contradicting negative results from an earlier work. Furthermore, it experiments with rather capable SoTA LLMs such as Llama2-70B, instead of much smaller "toy" LLMs, making their results more convincing and useful.

### Weaknesses
 - While this paper presents a useful empirical study, it does not introduce any new technique. Combining retrieval augmentation and long-context LLM is a straightforward idea, and the two being complementary to each other, though encouraging, is not very surprising.

- If I understand correctly (I find this part of the writing unclear, see Question 1 below and correct me if my assumption is wrong), the retrieval corpus is the collection of the context documents from each evaluation dataset (or maybe even each example). This may be a key reason why retrieval is more helpful in this work. In reality, for most of the tasks, it is impossible to assume to have perfectly relevant retrieval corpora (i.e. gold contexts from the test set), and the helpfulness of retrieval would dramatically decrease if the retrieval corpus mismatches the evaluation data.
As a result, the method considered in this paper is more tailored for one type of task, essentially reading comprehension of long documents, because the assumption that gold contexts, albeit long, are provided at test time. It would be more interesting to also explore the "open" settings where the gold context is not necessarily given.

### Questions
1. What's your retrieval corpus? Do you use the same corpus for all tasks? Or do you use the collection of gold contexts for each dataset as the retrieval corpus for that task? (If so, do you build a single index using contexts from all splits including the training and test set?) Or, do you build a separate index for each example using the chunks from the provided gold context for that example?
Sorry if I missed it, but I wasn't able to find any details on the retrieval corpora you used in your experiments.

2. It seems the evaluation tasks are all "closed-type", meaning the gold context is given at inference time. Is this the case? If so, how would retrieval be further helpful if the gold context is already provided? Is it because for certain tasks, the provided gold context can be too long and the relevant parts may have been truncated?

3. In Table 4, it is interesting that using the same top 5 retrieved chunks, DRAGON works better with 32k LLM while Contriever works better with 4k LLM. Any insights into what caused this? Have you tried reversing the order of the retrieved chunks?

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
The paper presents a detailed comparison of different methods of handling long contexts by 1) using retrieval augmentation 2) increasing the context length of LLMs using positional interpolation. The papers conducts experiments on 7 datasets and show that retrieval can significantly improve the performance of LLMs. The paper also shows results on increasing the number of retrieved context and compares different retrievers.

### Strengths
The paper performs comprehensive experiments on two LLMs with up to 32K context, demonstrating the benefits of retrieval even for long context models. The paper gives good insights about retrieval augmentation confirming a simple but effective alternative to expensive context scaling of huge models. The paper is well-written and easy to understand.

### Weaknesses
The paper has limited novelty. The majority of the paper compares to longer context LLM finetuned via positional interpolation, it may be better to have some results with the other context expansion techniques and with models that are natively trained with larger context lengths to possibly remove that source of error. The paper also lacks a thorough investigation into the impact of chunking strategies on retrieval performance. While a chunk size of 300 words is mentioned, the rationale for this specific choice and its potential impact on the variability of retrieved context lengths is not sufficiently explored. The paper would benefit from a more detailed analysis of how different chunking methods (e.g., fixed-size token chunks, semantic chunks) affect the quality and consistency of retrieved context, especially given the observed variance in top-k context lengths.

### Questions
If the chunking is 300 words (tokens ?), why is there so much variance in the top-5, top-10, shouldn't the top-5 context length consistently be around 1500 tokens? If the variability is due to chunking based on words and not tokens, why is that the case ? and why was 300 specifically chosen?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors systematically study the effectiveness of utilizing retrieval-augmentation and long-context tension in LLMs for downstream tasks. They conduct experiments using two large foundational models and evaluate their performance on seven downstream tasks that require longer context understanding. Compared to a previous study (Bai et al. 2023),  this work employs larger LLMs, leading to a different conclusion: retrieval significantly enhances the performance of LLMs, regardless of the size of their context window. Furthermore, the authors observe that larger models, such as LLaMA2-70B, tend to benefit more from retrieved evidence.

### Strengths
- The findings from these extensive empirical experiments are intriguing and have the potential to serve as inspiration for future research in this domain.
- The authors demonstrate that retrieval and extended-context approaches can significantly benefit LLMs, especially when they are of extremely large size.
- The study incorporates further analyses that clarify the impact of factors such as the number of chunks, context length, and retrievers on the performance of downstream tasks.

### Weaknesses
 - While the idea is straightforward, the novelty is limited. 
- The 70B model consistently exhibits improvement when utilizing retrieval or longer context. In contrast, the 43B model shows inconsistent improvement. Consequently, drawing a definitive conclusion regarding when to employ retrieval in relation to specific downstream tasks and model sizes becomes challenging.
- Given that the conclusion differs from prior work that utilizes smaller models, establishing an apple-to-apple comparison demonstrating instances where the same example could fail in the smaller model but succeed in the larger model would enhance the persuasiveness of the findings.

### Questions
- Do you observe different conclusions when using a smaller LLM (i.e., Llama2-7B and ChatGLM2-6B) as in Bai et al. 2023?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The concept of augmenting language models with retrieval has been widely explored for several years. Recently, there has been a growing interest in expanding the context window of transformers and large language models (LLMs). This research paper focuses on two key research questions related to retrieval augmentation and context window extension:

1. Which approach is more effective for downstream tasks - retrieval augmentation or a longer context window?
2. Is it possible to combine these methods to achieve better results?

To address these questions, the authors of this paper examine two pretrained LLMs - a 43B GPT model trained by themselves and LLaMA2-70B. Through extensive experimentation, they find that a shorter context window LLM with simple retrieval augmentation during inference can yield comparable results to a longer context LLM that is fine-tuned using positional interpolation in two specific downstream tasks, namely question answering and query-based summarization. Additionally, the authors note that retrieval can significantly enhance the performance of LLMs, regardless of the size of their context window. The findings of this study offer valuable insights to practitioners, helping them make informed decisions regarding the choice between retrieval augmentation and extending the context window of LLMs.

### Strengths
1. This paper has a clear motivation and investigates a significant topic on large language models (retrieval augmentation versus context window extension). Existing research effort on this topic is limited, except [1]. Instead of using black box API in [1] (e.g. GPT-3.5-Turbo), this paper trained their own 43B GPT model for comparisons. 
2. This paper is well-written and the presentation is clear;
3. Extensive experiments have been conducted on 7 downstream long context tasks, including single and multi-document question answering and query-based summarization. Two different sizes of LLMs and Three different retrievers are examined on eight tasks.


Reference: 

[1] Longbench: A bilingual, multitask benchmark for long context understanding. Arxiv 2023

### Weaknesses
1. The authors of this paper mainly focus on larger LLMs, specifically those with more than 40B parameters. They include two specific LLMs in their study: the 43B GPT and the 70B LLaMA. It is worth noting that most existing efforts in this field only report results on smaller models, such as the 7B model. It would be beneficial if the authors could further investigate the relationship between the size of the LLMs and the tradeoff between retrieval and the context window. The authors propose hypotheses to explain why concurrent work has produced different findings, particularly regarding the usefulness of retrieval for the Llama2-7B-chat-4k model with a 4K context window. It would be better if the authors could provide empirical evidence to support these hypotheses.

2. In terms of context window extension, this paper only utilizes the method mentioned in reference [2] for both LLMs. It would be interesting to explore whether the findings would be influenced by different methods of extending the context window.

3. This paper focuses primarily on question answering and summarization tasks, in contrast to Longbench[1], which encompasses a variety of tasks, including few-shot learning, synthetic tasks, and code completion.

4. The paper lacks a discussion on potential limitations and future directions. For instance, the authors do not address the potential limitations of combining retrieval augmentation and context window extension, such as the possibility of exacerbating the "lost-in-the-middle" phenomenon [3]. While one of the key findings of this study is that combining retrieval and long-context techniques improves LLM performance, the authors could suggest avenues for future research on how to better integrate these techniques together.

### Questions
See above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
