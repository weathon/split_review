# Language Repository for Long Video Understanding

- Decision: Reject
- Avg Score: 5.50
- Scores: 8, 6, 5, 3

## Abstract
Language has become a prominent modality in computer vision with the rise of multi-modal LLMs. Despite supporting long context-lengths, their effectiveness in handling long-term information gradually declines with input length. This becomes critical, especially in applications such as long-form video understanding. In this paper, we introduce a Language Repository (\ours) for LLMs, that maintains concise and structured information as an interpretable (i.e., all-textual) representation. Our repository is updated iteratively based on multi-scale video chunks. We introduce write and read operations that focus on pruning redundancies in text, and extracting information at various temporal scales. The proposed framework is evaluated on zero-shot visual question-answering benchmarks including EgoSchema, NExT-QA, IntentQA and NExT-GQA, showing state-of-the-art performance at its scale.

\keywords{Large Language Models \and Long-form Video}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a video modeling method called LangRepo, which forms a text data organization strategy. The method performs well on four datasets, demonstrating its effectiveness.

### Strengths
1. The newly proposed concept of using concise text as a representation for video reveals why current captioning-based long video understanding methods perform well, which is enlightening.
2. The authors conducted observations and various ablation experiments to demonstrate the effectiveness of their approach.
3. Experiments on multiple datasets show consistent improvements compared to the most similar related work, LLoVi.

### Weaknesses
1. The usage of log-likelihood is not fair, as other models do not utilize it, especially on the IntentQA dataset.
2. The experiments on long videos are not sufficient. NeXT-QA and NeXT-GQA are not typical long video benchmarks. At least the long split in VideoMME[1] should be incorporated. Otherwise, the authors should not stress long videos in the title, since textual representation for videos is also valuable for short videos. 
3. The observation experiment in Table 1 is hard to interpret; it would be helpful if the token sequence length were provided.

### Questions
N/A

### Soundness
3

### Presentation
3

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
The paper focuses on the problem that LLM's ability of long-term information gradually declines with input length, which is an important and interesting problem to study. The authors propose a textual-only video representation approach to deal with the information decay problem. Specifically, the overall pipeline contains read and write operations. Writing operation describes the video content with texts and stores. Reading operation read the description and summarize the content for text QA to finish VQA in an all-textual approach. Though the all-textual video question answering has been explored in recent literatures, such Language-Repo approach remains interesting. The experiments show the superiority of the method on long-video benchmarks, such as EgoSchema, NExT-QA, IntentQA and NExT-GQA.

### Strengths
1. Using language as an intermediate modality to deal with long-term information decay in LLM makes sense and sounds interesting. This could be a popular trend and this work would play an important role. However, the authors should do a detailed literature review and thorough discussion of this trend.
2. The code and implementation of the methods is provided which will greatly ease the reproduction process.
3. While in a zero-shot setting and no video pretraining is required, the proposed method achieves promising results on all the involved long video benchmarks.

### Weaknesses
1. The idea of transforming visual content to texts and performing efficient question-answering has been explored in image [1] and video [2][3] domains. There should be a separate subsection in related work to discuss this trend and the difference, which is critical.
2. Reasonability of experiments in Table 1: the authors argue that by varying the input length into QA-LLM (such as Mistral-7B), it can derive the conclusion that longer text input produces worse performance. However, this requires several strict assumptions: first the captions in different lengths contain evenly distributed and all adequate video content information. If it is not, it could be the QA benchmark bias to derive the performance changes, that the answers are hind in the fixed part of the video (say the early part of the captions/videos); Secondly,  the input to Mistral-7B is long enough to trigger the information decay issue. I am doubting if the input is video caption only, the input context length might not be sufficient to discuss long-term information processing decay.
2. As illustrated in Figure 4, the group operation is not conducted in a strict temporal order (like t=2 is grouped with 26-28 and 37). Will there be a negative impact on temporal sensitive tasks and errors in describing action/event orders?
3. Experiments - Proved by SUM-shot[2], the all-textual approach should be performing well, as well as in short video understanding. Comparison should be included on MSRVTT-QA and ANet-QA (which is missing in current long video experiments).
4. Experiments - Extremely long videos: there have been several emerging long video benchmarks, such as Video-MME, Event-Bench and ShortFilms. It would be great and more promising to provide results on these benchmarks and do a comparison/discussion to discuss the potential of dealing with extremely long videos (which should work, given the motivation and design pipeline of LanguageRepo).
5. It would be interesting to explore how vision-language hallucination rate varies. Short video LLMs + Texts vs. Long video LLMs. Will the intermediate modality increase or decrease the hallucination? This is not mandatory but I think is interesting to explore.
6. Formulation in Eq10 should be improved. The use of $\texttt{vqa}$ here would be confusing.
7. Table 6 (g) shows the oracle captioner achieved 69.2 on EgoSchema sub-set. It means the performance upper bound of the method. It might not be a good signal for an extendable framework. Please make further discussion.
8. It is important to ensure the Eq10 process can parse the formated video content and won't lead to long-context information processing decay issues. Please make analysis and explainations.

### Questions
1. In experiment Table 1, what is the specific input of Mistral-7B, and how long is the input? It is important to show how to obtain 1X, 0.5X and 2X captions. What about prompting VLLM to generate descriptions in different lengths (complexity)?
2. How do you get the video chunks? Even sampling frames or via some semantic approach, such as shot detection. For each video clip, how to use image LLaVA to obtain a caption set for videos?
3. What if using powerful LLM as an oracle for QA, e.g., Gemini and GPT to replace the models in Table 6a.
4. The input description is highly formated and seems long and redundant (might be inevitable, since the video is split into chunks and does separate text summarization). How to ensure the LLM can parse such format and won't trigger the long-context information decay issue?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper introduces a Language Repository (LangRepo) for LLMs, addressing the challenge of decreased effectiveness with longer inputs. LangRepo maintains concise and structured information, updating iteratively with multi-scale video chunks. It includes operations to eliminate redundancies and extract information at various temporal scales. The framework demonstrates state-of-the-art performance on zero-shot video question-answering benchmarks.

### Strengths
1. The authors propose an iterative approach with progressively longer chunks, enabling LangRepo to learn high-level semantics and extract stored language information at various temporal scales. This seems beneficial for LLMs in understanding video content.
2. The figures in the manuscript effectively illustrate the pipeline of the method and provide clear examples of entries in LangRepo, making it easy to follow.
3. Extensive experiments on various video question-answering datasets validate the impressive performance of LangRepo.

### Weaknesses
1. Table 1 shows that longer input captions can reduce LLM accuracy.  Adding details like frame rate, caption length, downsampling methods, and the effects of adjusting frame rates, rather than just subsampling or replicating captions, would make the findings more convincing. Specifically, it's unclear if the observed performance degradation is due to the increased number of tokens or the altered temporal structure of the captions. The lack of control over these variables makes it difficult to isolate the cause of the performance drop.

2. The authors use CLIP to group redundant text. However, as seen in the example from Figure 4, some non-redundant sentences are quite similar to grouped ones, differing only in terms like "man X" and "Person C," which are semantically very similar, raising concerns about CLIP's ability to distinguish them. Additionally, it's unclear how CLIP's similarity threshold is set for grouping, as there are no ablation experiments shown. What's more, directly using LLMs for grouping might be more effective, and a quantitative comparison could be beneficial. The current approach lacks a clear justification for the choice of CLIP over other methods, and the sensitivity of the grouping process to the similarity threshold is not explored.

3. If a more effective VLLM or LLM is used, would LangRepo achieve consistent performance improvements? Specifically, the effectiveness of LangRepo with captions extracted by different VLLMs, and whether captions extracted by LangRepo perform better across various LLMs, requires further validation. The paper does not explore the interaction between the quality of the input captions and the performance of LangRepo, nor does it investigate the scalability of the approach with more powerful language models. This leaves open the question of whether the observed gains are specific to the chosen models or generalize to other architectures.

### Questions
See weakness above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents a Language Repository for LLMs, which generates multi-scale summaries for the video input and applies in long video understanding. The authors evaluate the proposed LangRepo on EgoSchema, NExT-QA, IntentQA and NExT-GQA benchmarks.

### Strengths
1. The authors include enough relevant papers in the related works section. 
2. The authors provide a detailed ablation study.

### Weaknesses
1. The contribution of novelty is concerning. In this paper, the authors propose a summarization-based method based on the dense caption from LLoVi [1] paper. However, the original LLoVi paper already proposes a summarization prompt which significantly improves the performance of long video QA tasks. But in this paper, the authors do not have any discussion on this point in related work or any other sections. Also, the “Grouping redundant text” section is similar to the “Caption Digest” in the LifelongMemory[2] paper. The authors should provide strong evidence of the paper’s novel contribution compared to the existing works.

2. The need for complicated textual operation is questionable. In this paper, the authors only showcase the results on open-source LLM on a 7B/13B scale and the EgoSchema fullset results are significantly lower than the proprietary LLMs models (even comparing to the same scale open-source VLMs, like InternVideo2, is lower). The potential need of the summarization module is only because the LLM backbone is weak and could not take in the dense caption list. Thus, the authors should validate the effectiveness of the proposed framework on strong proprietary LLMs and have fair comparison with those methods.

3. The use of “Log-likelihood classifier” is confusing and creates unfair comparison. The authors mention that the Log-likelihood classifier is only used for EgoSchema dataset and improves significantly to the subset performance. In that case, since most methods in the main tables are using the lower-performance “generative classifier”, the use of this classifier creates unfair comparisons for the most related works. Also, the results on the EgoSchema subset are significantly lower than the subset (over 20%), this is not intuitive since the subset is just a part of the full set. Could the authors elaborate more on this?

4. The evaluation of “long video” is not sufficient. The authors provide results on NExT-QA, IntentQA and NExT-GQA benchmarks, however, the average video length of these dataset is only about 44 seconds, which is considerably short. The authors should provide results on more than 10 minutes to hour long video benchmarks to showcase the effectiveness of the proposed method on long videos.

5. The efficiency of the proposed method is very concerning. Since the multi-round summarization process is quite slow, and in Table 6.f, compared to the baseline approach LLoVi, LangRepo consumes 70% more time per video-query pair, using 85 seconds to process a 180 seconds video from egoschema. The authors should also show the detailed split of times using on captioning/summarization/question-answering etc..

### Questions
All questions from the weaknesses, and: 

1. The comparison in the right part of Figure 1 is concerning, since the methods like VideoAgent only uses only 8.4 frames, the authors should take the caption/frame numbers into account (also main tables). 
2. Could the authors test the model with the more advanced and larger LLMs, like qwen-72B or LLaMA-3.1-70B? 
3. Could the authors provide comparison results in main table using "generative classifier" for the proposed method as well for fair comparison?

### Soundness
2

### Presentation
2

### Contribution
1
