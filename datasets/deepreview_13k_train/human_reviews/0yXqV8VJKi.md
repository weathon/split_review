# Understanding Complexity in VideoQA via Visual Program Generation

- Decision: Reject
- Scores: 6, 6, 3, 6

## Abstract
We propose a data-driven approach to analyzing query complexity in Video Question Answering (VideoQA). Previous efforts in benchmark design have largely relied on human expertise to construct challenging samples. In this work, we experimentally demonstrate that humans struggle to accurately estimate which questions are hard to answer for machine learning models. 
    Our alternative, automated approach takes advantage of recent advances in code generation for visual question answering. In particular, we use generated code complexity as a proxy for the question complexity and demonstrate that it indeed shows a much stronger correlation with the models' performance, compared to human estimates. We then present a novel algorithm for estimating question complexity from code. It identifies fine-grained primitives which correlate with the hardest questions. These human-interpretable results lead to a number of discoveries about the key sources of complexity for VideoQA models. Finally, we extend our approach to generate complex questions for a given set of videos. This allows us to automatically construct a new benchmark, which is 1.9 times harder for VideoQA methods than existing manually designed datasets.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces an approach to analyzing and generating complex questions for Video QA. The authors propose the use of generated code complexity as a metric to evaluate question difficulty. They introduce "CodePlexity," a novel algorithm that analyzes generated code's structure and content to identify patterns that make questions challenging for ML models. This allows the creation of a new VideoQA dataset named "CodePlex-QA" which features more complex questions than existing datasets without relying on human expertise.

### Strengths
-	The paper introduces a novel and interesting approach using code complexity to evaluate question complexity.
-	The paper offers interesting insights into the differences in human evaluation, text-based and code-based evaluation.
-	The experiment results show clear empirical evidence to support the claims.

### Weaknesses
 - The paper represents subtrees in question code using simple one-hot encoding without additional processing, which might ignore the frequency of subtrees and their structural relationships. Additionally, this representation can be very sparse. How does this affect CodePlexity's performance?
- To what extent does the choice of code generation model affect the method's results? Would using different code generation models lead to identifying different patterns of complexity, and how might this impact the method's consistency?
- Since the method evaluates difficulty without considering visual information, there might be cases where code generation is challenging due to question ambiguity, but the task would be straightforward with visual context. Is CodePlexity truly measuring question difficulty, or is it primarily measuring code generation complexity?
- Most models evaluated in the paper are large video-language models built upon language model architectures. Since these models share similar language model foundations with the code generation approach, they might inherently struggle with the same types of questions that are difficult for code generation. Does this architectural similarity explain their correlated performance? How well would the method generalize to fundamentally different architectures that might employ different reasoning mechanisms?

### Questions
-	The paper represents subtrees in question code using simple one-hot encoding without additional processing, which might ignore the frequency of subtrees and their structural relationships. Additionally, this representation can be very sparse. How does this affect CodePlexity's performance?
-	To what extent does the choice of code generation model affect the method's results? Would using different code generation models lead to identifying different patterns of complexity, and how might this impact the method's consistency?
-	Since the method evaluates difficulty without considering visual information, there might be cases where code generation is challenging due to question ambiguity, but the task would be straightforward with visual context. Is CodePlexity truly measuring question difficulty, or is it primarily measuring code generation complexity?
-	Most models evaluated in the paper are large video-language models built upon language model architectures. Since these models share similar language model foundations with the code generation approach, they might inherently struggle with the same types of questions that are difficult for code generation. Does this architectural similarity explain their correlated performance? How well would the method generalize to fundamentally different architectures that might employ different reasoning mechanisms?

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
3

### Summary
This paper proposes a novel approach to analyzing and measuring question complexity in VideoQA by leveraging generated code complexity. The authors demonstrate that code-based metrics correlate better with model performance compared to human judgment and introduce CodePlexity, an algorithm for estimating question complexity. They use this to identify challenging patterns in VideoQA and automatically generate a new benchmark dataset, CodePlex-QA, which proves to be significantly more challenging than existing datasets.

### Strengths
- The idea to measuring question complexity using code generation is well-motivated
- The ablation studies and analysis are well-designed

### Weaknesses
 - All experiments are conducted on a single dataset (NExT-QA) for analysis. Therefore, it leads to the limited evaluation across different types of VideoQA tasks.
- The authors should discuss more how errors of code generation might affect the complexity metrics
- The human evaluation study uses only 150 questions, which is a relatively small sample
- We concern that the merging of subtrees that "always co-occur" could potentially miss important patterns in edge cases
- The manual filtering process for the generated dataset (removing 12% of questions) could introduce selection bias

### Questions
- Why the authors do not validate the proposed approach on other VideoQA datasets besides NExT-QA?
- How do errors in code generation impact the complexity metrics?
- Are there any important patterns that might be missed by your current subtree merging approach?
- What specific criteria were used to manually filter out the 12% of questions?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the author claims that the questions considered difficult are different from the actual difficult questions to current VideoQA models. Therefore, the authors propose a new metric: CodePlexity, to evaluate the difficulty of a VideoQA question. This metric is based on the recent visual programming methods, where a visual program of a question is generated and which complexity is evaluated. Based on this metric, the authors found that most models struggle with questions where multiple frames are included and frame order need to be take into consideration. Then based on the metric, the author proposes CodePlex-QA and claims that it is 1.9 times harder than existing benchmarks.

### Strengths
1. The paper proposes a novel metric to evaluate the complexity of the VideoQA problem and also proposes a CodePlex-QA that is more difficult for current VideoQA models. The idea of leveraging code to develop a new metric for question difficulty analysis is interesting.
2. The paper conducts thorough experiments on testing the correlation of the metric.

### Weaknesses
1. The criteria for what makes a question complex or challenging for models—especially compared to human intuition—seem speculative. Without more rigorous validation, it’s unclear whether the proposed complexity measures truly capture inherent question difficulty or just reflect the limitations of current VideoQA models. Also, the idea of identifying questions that are “easy for humans but hard for machines” is ambiguous. It seems plausible that any difference in difficulty may be more a result of model architecture and training rather than the intrinsic complexity of the question itself. The paper does not sufficiently explore the possibility that the CodePlexity metric is simply measuring the alignment of the question's structure with the model's inductive biases, rather than a fundamental property of the question itself. For example, if a model is primarily trained on single-frame reasoning, it's not surprising that multi-frame questions are difficult, but this doesn't necessarily mean the questions are inherently more complex.
2. Visual programming is a natural way (and probably the best way) to address the CodePlex-QA  task. The author didn't report how well the recent visual programming methods (Visprog, ViperGPT, CodeVQA), especially those on addressing complex logical questions (eg. RVP[1]) addresses the task.
3. The comparison between Next-QA and CodePlex-QA (Table2) is not convincing enough as previous works have shown that Next-QA have easy questions[2]. How is CodePlex-QA compared with Next-QA ATP-Hard split?

### Questions
1. What are the results of the recent visual programming methods on this task?
2. How complex is CodePlex-QA compared with Next-QA ATP-T/ATP-C split?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores a data-driven method for evaluating question complexity for Video Question Answering (VQA) by collecting the visual programs generated by ViperGPT. Then, they analyze the code outputs and leverage them to assess the difficulty of the questions in a VQA triplet.
Given the output code from the Visual Programming module (ViperGPT), they propose CodePlexity, an algorithm that parses the generated code via Abstract Syntax Trees (AST), and later identifies valid subtrees. These subtrees are then scored by correlating subtrees with difficult questions -- subroutines that hurt the VQA model performance. The authors use NExT-QA as the benchmark to analyze their proposed metric. 
Given this metric, they also propose a pipeline to generate difficult question-answer pairs for a set of videos from MOMA, ActivityNet (+Entities/Captions), Action Genome, and Charades. 
Finally, they compare the results of models SeViLA-ZS, InternVideo and VIOLET on their proposed new dataset (CodePlex-QA) against NExT-QA.

### Strengths
+ This paper is easy to read, the method is easy to follow and the qualitative examples help to illustrate the motivation of their work.

+ Leveraging Visual Programming outputs as a proxy for assessing the difficulty of a given task is an underexplored domain -- in software engineering, an active area of study is the correlation between the code complexity and difficulty of the task. This is an open problem, and this paper proposes an interesting generalization of this task.

+ Decomposing the output code from the VP module via ASTs, and identifying subtrees that decrease performance via scoring, may give an interesting angle for generating an interpretable pipeline to analyze subprocesses that might be hurting the models' performance. In principle, this looks like an interesting approach and a viable metric for VP-based methods.

### Weaknesses
 - Visual Programming (VP) is an interpretable framework for several visio-linguistic tasks, however, VP may output very simple code for a quite complex task, yielding false positive or false negative hard cases, and VP might not be reliable -- for a very complex task, the output code could be simple; the LLM might regard it as a simple task, but it's actually the opposite
In addition, VP falls short against end-to-end models (e.g., ViperGPT acc. is 60% vs SeViLa (finetuned) acc. is 73.8%) -- given its underperformance, it is hard to justify the use of its outputs as a proxy for evaluation of complexity. It is also hard to justify using VP for measuring task complexity and then evaluating on end-to-end models.

- Disregarding visual inputs: "Text-based metrics (above) perform worse than the code-based ones (below), and our approach demonstrates the highest correlation with the models’ performance."  -- this completely ignores the visual modality, which seems problematic.

- The authors claim: "In summary, we discovered that VideoQA methods struggle with fine-grained temporal reasoning and lack spatio-temporal, object-centric representations. This is in accord with prior studies" [3] -- however, those studies regard both visual and language modalities for assessing temporal reasoning in video QA, giving high importance to the video part.

- Human evaluations: Figure 6: We ask human annotators to provide the relative ordering of three provided questions
according to the estimated complexity of answering the question about an unseen video -- how to correctly assess the complexity of the task without looking at the video?

- Experimental setup:
Baselines [1] focus on grammar and text only. BERT and GPT-4 also focus on text only.

- Generalizability: ViperGPT is the VP module used in this paper, however, VP has significantly progressed. Different methods leverage multiple LLMs, there has been extensive problem decomposition and iteration that impact the code outputs. Further experiments with other VP approaches might be required to ensure generalization. Similarly, the proposed metric and dataset is only compared against NExT-QA. Other benchmarks might be necessary to validate the proposed metric and dataset (e.g., MVBench [2] compiles a collection of datasets (with subsets of samples from a diverse range of sources), which includes spatio-temporal analysis, spatial action, object, position, scene, count, attribute and cognition).

- For dataset generation, the authors compare their pipeline with [4] -- however, an important step for EgoSchema is the manual curation of the whole dataset in the final step -- details for this step is not further detailed in this paper.
Furthermore, as a comparison, EgoSchema consists of over 5000 human curated multiple choice question answer pairs, spanning over 250 hours of real video data -- significantly larger than the 1981 samples -- what is the length of each video sample?

### Questions
- SeViLA "leverages a single image-language model (BLIP2) to tackle both temporal keyframe localization and question answering on videos" How the findings in this paper generalize to models that take multiple video frames for VQA? (e.g., VideoChat2 [5], Video-LLaVA [6])?

- NExT-QA uses videos from VidOR [7] -- CodePlex-QA use videos from MOMA, ActivityNet, ActivityNet-Entities, ActivityNet-Captions), Action Genome, and Charades. Why not using the same videos, or at least the same source video dataset (VidOR)?

[5] Li, Kunchang, et al. "Mvbench: A comprehensive multi-modal video understanding benchmark." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2024.

[6] Lin, Bin, et al. "Video-llava: Learning united visual representation by alignment before projection." arXiv preprint arXiv:2311.10122 (2023).

[7] Xindi Shang, Donglin Di, Junbin Xiao, Yu Cao, Xun Yang, and Tat-Seng Chua. Annotating objects and relations in user generated videos. In ICMR, pages 279–287, 2019

### Soundness
3

### Presentation
3

### Contribution
2
