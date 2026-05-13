# AuroraCap: Efficient, Performant Video Detailed Captioning and a New Benchmark

- Decision: Accept
- Scores: 8, 8, 6, 6, 6

## Abstract
Video detailed captioning is a key task which aims to generate comprehensive and coherent textual descriptions of video content, benefiting both video understanding and generation. In this paper, we propose \model, a video captioner based on a large multimodal model. We follow the simplest architecture design without additional parameters for temporal modeling. To address the overhead caused by lengthy video sequences, we implement the token merging strategy, reducing the number of input visual tokens. Surprisingly, we found that this strategy results in little performance loss. \model~shows superior performance on various video and image captioning benchmarks, for example, obtaining a CIDEr of 88.9 on Flickr30k, beating GPT-4V (55.3) and Gemini-1.5 Pro (82.2). However, existing video caption benchmarks only include simple descriptions, consisting of a few dozen words, which limits research in this field. Therefore, we develop \benchmark, a video detailed captioning benchmark with over one thousand carefully annotated structured captions. In addition, we propose a new LLM-assisted metric \metric~for bettering evaluation, which adopts a divide-and-conquer strategy to transform long caption evaluation into multiple short question-answer pairs. With the help of human Elo ranking, our experiments show that this benchmark better correlates with human judgments of video detailed captioning quality. Code, docs, weight, benchmark and training data are all avaliable at \href{https://rese1f.io/aurora-web/}{website}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
Towards the video detailed captioning task, this paper conducts comprehensive research including the introduction of a new model called AuroraCap, a novel dataset VDC and a novel evaluation metric VDC-Score. For AuroraCap, authors apply the token merging strategy on large models. Extensive experiments have been conducted to verify the effectiveness of AuroraCap, and the necessity of VDC and VDCScore. This work contributes significantly to advancing the field of detailed video understanding.

### Strengths
1.	This paper is well-written.
2.	The proposed benchmark VDC is large-scale and diverse, which contains short, background, main object, camera and detailed captions. 
3.	The average length of captions in VDC exceeds previous datasets, to facilitate the research of understanding and also generation of long videos. 
4.	Very extensive experiments.

### Weaknesses
1. The paper is not very easy to follow, owing to many tables and figures. 
2. For all the compared captioning models, are they trained under the same schema? If true, which one setting is chosen among different settings presented in Figure D5 and Figure D6?
3. In Table 6 – Table 8, what does the accuracy mean? 
4. For VDCScore, it is hard to evaluate which score is better among VDCScore, VDD, CIDEr and maybe CLIP-based score, RefCLIP-S[1] and RefPAC-S[2].

### Questions
1. How many GPU hours have been consumed on this research?
2. Will you publish the data, the pre-trained model with weights and also the training recipes?
3. In the future, I believe the VDC benchmark will facilitate more research on the video, including classification, video generation, etc.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces AuroraCap, an LLM-based video captioning model that uses token merging to reduce visual tokens. AuroraCap is evaluated across multiple image and video captioning datasets. To assess models' ability to generate detailed captions, the paper also proposes a new benchmark, Video Detailed Captioning (VDC), along with an LLM-assisted metric, VDCscore. VDC includes over 1,000 annotated structured captions, while VDCscore transforms long captions into multiple short question-answer pairs. Various existing models are evaluated on the VDC benchmark.

### Strengths
* The presentation of the paper is clear. It's easy to follow.
* The proposed VDC benchmark is a valuable contribution to the community. The detailed video captioning capability of video LLMs is an area that has been relatively underexplored, and introducing VDCscore adds a meaningful component to the evaluation pipeline. The evaluation process of VDCscore aligns well with human reasoning process.
* Extensive experiments are conducted.

### Weaknesses
 * Certain aspects of AuroraCap are not fully explored. For instance, while it performs well on the ANet dataset in video QA tasks, it performs poorly on MSVD, which is typically an easier benchmark. What might be causing this discrepancy? The paper should delve deeper into the architectural differences or training data biases that lead to such varied performance across datasets with seemingly similar question-answering tasks. Specifically, an analysis of the types of questions and the complexity of the visual scenes in each dataset would be beneficial.
* Unfair comparison:
  * Table 2 refer to the baseline models as the SoTA methods on image captioning benchmarks under zero-shot setting. However, I believe there are other LLM-based models with stronger captioning performance. For example, the BLIP family—BLIP2 [1], which achieves a 121.6 CIDEr score on NoCaps (val set), and InstructBLIP [2], which is even stronger. It would be beneficial to clarify the criteria used to select these baselines. The paper needs to justify why specific models were chosen as baselines, especially when there are other models with superior zero-shot performance. A more comprehensive comparison with a wider range of state-of-the-art models is needed to accurately position AuroraCap's performance. This should include models that have demonstrated strong zero-shot capabilities on similar benchmarks.
  * Similar concerns apply to the video captioning and video QA task comparisons. The selection of baseline models for video captioning and video QA tasks also appears to be limited. The paper should include a wider range of recent models, particularly those that have shown strong performance in zero-shot settings. A more thorough comparison would provide a clearer picture of AuroraCap's relative strengths and weaknesses.
* I notice that the VDCscore relies heavily on the use of GPT-4o:
  * As also pointed out by other work [3], different versions of GPT can affect the results of GPT assisted evaluation heavily. Although I may have missed it, I did not see which version of GPT-4o was used for the evaluation in the paper. Standardizing the evaluation method is essential for consistency in future studies. The paper needs to explicitly state the exact version of GPT-4o used for evaluation, including any specific parameters or settings. This is crucial for reproducibility and comparability with future work. Furthermore, the potential impact of different GPT versions on the VDCscore should be investigated and discussed.
  * Given the multiple variables that can influence GPT-assisted evaluation, and since VDCscore already uses phrased answers, what are the potential drawbacks of using an automatic metric based on, e.g. n-gram matching, to evaluate the final score? Could a variant of VDCscore be devised that assesses final triplets (i.e., <question, correct answer, predicted answer>) without relying on GPT? The paper should explore alternative evaluation metrics, such as n-gram based methods, to assess the final triplets. This would provide a more objective measure and reduce the reliance on LLMs for evaluation. A comparison of these metrics with VDCscore would be valuable to understand the potential biases introduced by GPT-4o.
* minor: Several instances of "BELU" should be corrected to "BLEU"; small grammar errors like in line 203: "are only contains" --> "only contain"

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1.This paper proposes AURORACAP, a video captioner based on a large multimodal model. AURORACAP follows a simple architecture design without additional parameters for temporal modeling. To address the overhead caused by lengthy video sequences, it implements a token merging strategy, reducing the number of input visual tokens with little performance loss. AURORACAP shows superior performance on various video and image captioning benchmarks. 
2.Existing video caption benchmarks only include simple descriptions, so the authors develop VDC, a video detailed captioning benchmark with over one thousand carefully annotated structured captions. 
3.The authors also propose a new LLM-assisted metric VDCSCORE for better evaluation, which transforms long caption evaluation into multiple short question-answer pairs.

### Strengths
1.the proposed AURORACAP shows good performance. Using bipartite soft matching method to merge similar token is novel and show potential on token reduction.  
2.VDC with detailed video caption is good contribution for video captioning research community, and authors provide the detailed description of dataset curation. 
3.the proposed metric VDCscore is a good improvement for captioning task evaluation with novelty. 
4.Paper is in good writing for understanding.

### Weaknesses
1.AURORACAP: there is no description of the AURORACAP's 1.3M pretraining data. We could't conclude the reseasons for the good peroformance of AUROREACAP. Could authors provide details on:

a. The sources and types of data included in the 1.3M pretraining dataset

b. Any preprocessing or filtering steps applied to this data

c. How this pretraining data compares to datasets used by other models?

This information would help readers better understand the factors contributing to AURORACAP's performance.

2.VDCSCORE: the potential stability issue of the metric.

a. Is there a fixed number of question-answer pairs generated for each caption, or does it vary?

b. If it varies, how do the authors ensure consistency in the metric across captions of different lengths or complexities?

c. Did the authors conduct any experiments to test the stability of the metric with varying numbers of question-answer pairs?


3.VDCSCORE: miss detailed information in the Elo Ranking. Could authors provide details on:

a. The specific dataset used for the Elo Ranking comparison, including its size and composition

b. The criteria used for selecting this dataset for the comparison

c. How this dataset relates to or differs from the VDC benchmark?


4.VDCSCORE：some quality problems of caption are about the repetition or grammar errors. Does this metric could evaluate these types of quality?

a.How does VDCSCORE handle linguistic aspects of caption quality, such as repetition and grammatical errors?

b.Were any specific measures incorporated into the metric to detect and penalize such issues?

c.Could the authors provide examples or experiments demonstrating how the metric performs on captions with these types of linguistic problems compared to human evaluation?

### Questions
the questions are listed above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes AURORACAP, a video captioner based on a large multimodal model that utilizes a token merge strategy to support lengthy video sequences. The authors also introduce VDC, a video detailed captioning benchmark featuring over one thousand carefully annotated structured captions. Finally, the authors validate the effectiveness of their model through a divide-and-conquer approach across multiple benchmarks, including the newly introduced VDC and various metrics, including human Elo ranking.

### Strengths
1. This work introduces the application of a token merging strategy for video understanding, demonstrating through extensive experiments that it can utilize only 10% to 20% of the visual tokens compared to the original tokens generated by ViT, with only a marginal drop in performance across various benchmarks.
2. The proposed VDC benchmark addresses dimensions that are lacking or insufficient in existing benchmarks, such as rich world knowledge, object attributes, camera movements, and, crucially, detailed and precise temporal descriptions of events.
3. This paper is well-structured and includes intuitive figures that effectively illustrate the work.

### Weaknesses
1. There is a lack of novelty regarding the token merging strategy, as similar attempts have already been made in Chat-UniVi[1], which validated the effectiveness of this approach on video understanding benchmarks. Furthermore, the divide-and-conquer validation of the model essentially constructs Video QA based on video detail captioning, a method that has also been explored in [2].
2. It would be beneficial to evaluate the token merging method's stability on longer video sequence benchmarks, such as Egoschema[3] and VideoMME[4].

### Questions
1. Why do the authors train their model on general tasks while naming it a captioner? It seems more reasonable to refer to it as a general model while emphasizing its captioning capabilities.
2. Why does GPT-4V have the lowest CIDEr score on the Flickr benchmark? I believe the authors need to verify whether a fair comparison was conducted, including aspects such as the prompts used during evaluation. I do not consider this to be a reasonable outcome.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces AuroraCap, a video captioning model based on LMM, along with VDC, a detailed captioning benchmark, and VDCScore, an evaluation metric designed for long captions. AuroraCap handles video sequences with lower visual token numbers by the token merge strategy, outperforming state-of-the-art models, even including GPT-4V and Gemini-1.5 Pro.  VDC addresses the limitations of existing video captioning benchmarks by providing over one thousand videos with detailed, structured captions. since existing metrics are insufficient to evaluate detailed captioning performance, they develop a new LLM-assisted metric VDC-SCORE, that breaks down long captions into short question-answer pairs, ensuring better alignment with human judgments.

### Strengths
1. Despite adopting a simple architecture design consistent with LLaVA, AuroraCap achieves remarkable results on captioning tasks with its three-stage training recipe.
2. AuroraCap combines the Token Merging strategy, significantly reducing the number of visual tokens input and thereby improving inference efficiency.
3. This paper also presents VDC, a detailed video description benchmark, which includes over one thousand structured descriptions, providing detailed annotations for videos from multiple perspectives.
4. To accurately evaluate the model’s detailed captioning capabilities, the paper introduces VDCScore. This metric uses a divide-and-conquer strategy to break long captions into short QA pairs and employs LLM assistance for scoring. This approach avoids the challenges traditional metrics face with long captions and mitigates potential hallucination issues associated with using LLM evaluations.
5. Compared to existing models, AuroraCap achieves excellent performance in both image captioning and video captioning tasks.
6. The paper also explores the impact of the visual token kept ratio on model performance, demonstrating that with the token merging strategy, fewer visual tokens can still maintain high performance.

### Weaknesses
1. **Spatial Token Merging:** AuroraCap only performs spatial token merging within frames and does not implement temporal token merging between frames, which could further enhance inference efficiency. The lack of temporal merging is a missed opportunity to reduce redundancy across frames, especially in videos with slow-moving scenes or static backgrounds. This could lead to unnecessary computational overhead during inference.
2. **Static Token Merging:** It seems that for different visual inputs, the number of visual tokens remains consistent by setting a visual token kept ratio. However, this ‘static’ token merging strategy is unreasonable for tokens with varying levels of informativeness. A fixed ratio may discard crucial tokens in complex scenes while retaining less informative tokens in simpler scenes, thus limiting the model's ability to adapt to varying visual content.
3. **Unclear Training Strategy:** It is not clear whether the token merging strategy was used during training. Additionally, the impact of using different token merge ratios during training on inference performance is not clear. The absence of details regarding the training process, particularly how token merging is incorporated, makes it difficult to assess the robustness and generalizability of the model. The lack of experimentation with different token merge ratios during training also raises concerns about the model's sensitivity to this hyperparameter.
4. **Performance in Video Question Answering:** Although AuroraCap demonstrates leading performance in captioning tasks, its advantages in video question answering tasks are not apparent, which is perplexing. The discrepancy in performance between captioning and question answering suggests that the model may not be effectively leveraging its visual understanding capabilities for tasks requiring more complex reasoning.

### Questions
1. **Training Strategy Clarity:** Was the token merging strategy used during AuroraCap’s training phase? How does varying the token merge ratio during training impact inference performance?
2. **Performance in Video Question Answering:** What factors limit AuroraCap’s performance in video question answering compared to captioning tasks?
3. **Token Merge Curve on VDC** As shown in Figure 6, why does retaining all visual tokens not lead to the highest VDCScore?

I will consider raising my score if the authors can further address my concerns.

### Soundness
3

### Presentation
3

### Contribution
3
