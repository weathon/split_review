# Painting with Words: Elevating Detailed Image Captioning with Benchmark and Alignment Learning

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Image captioning has long been a pivotal task in visual understanding, with recent advancements in vision-language models (VLMs) significantly enhancing the ability to generate detailed image captions. However, the evaluation of detailed image captioning remains underexplored due to outdated evaluation metrics and coarse annotations. In this paper, we introduce DeCapBench along with a novel metric, DCScore, specifically designed for detailed captioning tasks. DCScore evaluates hallucinations and fine-grained comprehensiveness by deconstructing responses into the smallest self-sufficient units, termed primitive information units, and assessing them individually. Our evaluation shows that DCScore aligns more closely with human judgment than other rule-based or model-based metrics. Concurrently, DeCapBench exhibits a high correlation with VLM arena results on descriptive tasks, surpassing existing benchmarks for vision-language models. Additionally, we present an automatic fine-grained feedback collection method, FeedQuill, for preference optimization based on our advanced metric, demonstrating robust generalization capabilities across auto-generated preference data. Extensive experiments on multiple VLMs demonstrate that our method not only significantly reduces hallucinations but also enhances performance across various benchmarks, achieving superior detail captioning performance while surpassing GPT-4o.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Image captioning is an important task that has recently been explored using VLMs to generate detailed captions. Traditional metrics or coarse annotations may not be ideal to evaluate the performance of detailed image captioning. 

This paper proposes evaluation metric for detailed captioning tasks, considering both hallucination and comprehensiveness. A public benchmarks has been proposed. The paper also introduces FEEDQUILL, a scalable method for fine-grained feedback collection by decomposing and verifying responses. Experimental results seem reasonable.

### Strengths
To address the problem of evaluating the performance of detailed image captioning, this paper proposes a new evaluation metric to take both hallucination and comprehensiveness into consideration. It also constructed an evaluation benchmark using the proposed evaluation metric to the ImageInWords images and their corresponding hyper-detailed image captions. The experimental results seem reasonable.

### Weaknesses
To generate benchmark for detailed image captioning, 400 images from ImageInWords dataset are used to generate benchmark with the proposed evaluation metric. Only 400 images seems a very small subset. The uniqueness of the proposed benchmarks needs to be further clarified.

The performance of the proposed method does not always achieve the best results. More explanations and justifications are expected.

The organisation of the paper can be further improved. It would be good to have a self-contained version rather than leave some important content in appendix. 

Some notations are not clearly defined. For example, in 4.1, the definition of the fraction of correct units seems not easy to be understand.

### Questions
To generate benchmark, why only 400 images are selected? How these images are selected? 400 images seems very small subset. 

Why LLaVA models are used as base model? It will be good if more popularly used models can be investigated to demonstrate the effectiveness of the proposed fine-grained feedback collection.

The decomposition in section 4.1 seems similar as that in 3.1.

### Soundness
3

### Presentation
2

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
This paper proposes a DeCapBench together with a DCScore and FeedQuill preference optimization method to evaluate and improve the ability of detailed image captioning. More specifically, DCScore is implemented in an F1 score style to asses the hallucination and comprehensiveness of the output captions. The introduced detailed captioning benchmark DeCapBench is further conducted to evaluate the captioning capability of VLMs. In addition, this paper also proposes a fine-grained feedback collection method to formulate the reward function for model alignment. The experimental results demonstrate extensive comparisons and results against multiple closed- and open-sourced approaches.

### Strengths
1. Evaluating detailed image captioning remains a challenging task since current mainstream captioning datasets (e.g., COCO) only contain relatively coarse-grained and short captions. Since most of the metrics for image captioning rely on ground-truth captions, designing a metric to properly assess the quality and hallucination degree of the output captions is crucial, especially in the multimodal LLM era.
2. The proposed fine-grained feedback as the reward function and the PPO-based alignment framework is reasonable and technically sound.
3. The quantitative comparisons and experimental analysis are comprehensive, and the performance of the proposed method is promising.
4. The overall paper is well-structured and easy to follow.

### Weaknesses
1. The explanation of the DCScore evaluation process is not entirely clear. Please see the questions below.
2. When evaluating the effectiveness of FEEDQUILL with various VLMs, only LLaVA-family models are utilized. Why aren't any non-LLaVA-family models (e.g. InternVL-2-8B) used in Table 6?

About DCScore  
Step 1 of the evaluation process is unclear to me.
1. Who are the “human experts”? What’s the definition of “experts” in this paper?
2. Why are the decomposers for generated captions and ground-truth captions different (LLM vs. human experts)? Can LLM be used for both?  

Step 3  
3. Is the goal of this step to compensate for the missing details in the ground-truth captions?
What’s the difference between $P_{true}$ and $Q$?

About DECAPBENCH  
4. How are the 400 high-quality, human-curated public detailed captions chosen? Is there any criterion for this selection?

About FEEDQUILL  
5. In the related work section, the paper mentioned that using GPT-4v to collect preference data could pose risks of bias and unreliability as the preference judgment of GPT-4v is not manually verified. As FEEDQUILL also leverages multiple VLMs to collect preference pairs, aren't the collected data also likely to be influenced by these models' bias and unreliability?

About experiments  
6. Do other non-LLaVA VLMs, e.g. InternVL-2-8B, trained with the FEEDQUILL-collected preference data also show superior results on downstream tasks?  
7. How many FEEDQUILL preference data are used for training in the last row of Table 2?

Minor comments  
8. Line 319: "..., responses with fewer hallucinations are often inherently less helpful." Is this sentence correct?  
9. Typo in line 334: "In To fully exploit the characteristics ..."

### Questions
Please refer to the Weaknesses. The following is a minor question.

1. This paper mainly considers LLaVA to be the VLM. Are other commonly used multimodal LLMs, such as VILA or InternVL-2, also applicable to this proposed RL alignment framework?

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
This paper introduces a new metric DCScore and a new benchmark DECAPBENCH to evaluate the detailed image captioning capabilities of  VLMs. DCScore is designed to measure both the hallucination and comprehensiveness of generated captions. To calculate DCScore, ground-truth and generated captions are first broken down into primitive information units. Then, the primitive information units from the generated captions are compared with those from the ground-truth captions. In addition, GPT-4o is utilized to judge whether each primitive information unit from the generated captions corresponds to the image. Based on these results, a precision score and a recall score are derived, representing non-hallucination and comprehensiveness, respectively. Empirical study shows that DCScore is more aligned with human judgments than previous image captioning evaluation metrics. By combining the proposed DScore and 400 high-quality and detailed image-caption pairs, the benchmark DECAPBENCH is established.
The paper also proposes FEEDQUILL, an automatic fine-grained feedback collection method to collect preference data for model training. This method breaks down each response into primitive information units, ensembles multiple VLMs to score these units, and constructs preference data from these scores. Experiments demonstrate that models trained using FEEDQUILL outperform those trained with other preference data.

### Strengths
1. A novel metric for evaluating detailed image captions and an automatic feedback collection method are proposed. The proposed metric aligns more closely with human judgments and can measure hallucination and comprehensiveness. The proposed feedback collection method is able to construct better preference data without human annotators than previous preference data collection methods.
2. The experiments show that the proposed FEEDQUILL generalizes much better than other preference data when LLaVA models are used. In addition, the model trained with FEEDQUILL has better performance on various downstream benchmarks, demonstrating its effectiveness in enhancing models' image captioning capabilities.
3. The paper is well-written and organized.

### Weaknesses
[Metric - DCScore]
1. Why are non-descriptive captions included as a part of this metric? 
2. This metric appears to rely on paid API (i.e., GPT-4o) for its evaluation process. It would be advantageous if the metric could also be adapted to work with open-source VLMs as alternatives to GPT-4o.

[Benchmark - DeCapBench]
1. The testing dataset in DeCapBench consists of only 400 samples. How does this compare to other visual data hallucination quality sets, such as HallusionBench [1]

[Method - FeedQuill]
1. In table3, there is a lacked experiment to compare the FeedQuill with the simplest cross-entropy loss (i.e., image caption loss) using the same PPO-finetuned dataset. A comparison of FeedQuill with cross-entropy loss on hallucination-measured datasets, such as mmHal-V and DeCapBench, would be valuable.
2. In addition to MSCOCO, OpenImages, and ShareGPT4V, what other datasets are included in fine-tuning the VLM with PPO?
3. Is the preference score $c_r$ a scalar value? If so, why is it necessary to train an additional reward model $R_{\phi_r}$ to generate the $r_{r_t}$ in Algo 1? Could the $c_r$ be directly used as a part of reward?


### Questions
About DCScore  
Step 1 of the evaluation process is unclear to me.
1. Who are the “human experts”? What’s the definition of “experts” in this paper?
2. Why are the decomposers for generated captions and ground-truth captions different (LLM vs. human experts)? Can LLM be used for both?  

Step 3  
3. Is the goal of this step to compensate for the missing details in the ground-truth captions?
What’s the difference between $P_{true}$ and $Q$?

About DECAPBENCH  
4. How are the 400 high-quality, human-curated public detailed captions chosen? Is there any criterion for this selection?

About FEEDQUILL  
5. In the related work section, the paper mentioned that using GPT-4v to collect preference data could pose risks of bias and unreliability as the preference judgment of GPT-4v is not manually verified. As FEEDQUILL also leverages multiple VLMs to collect preference pairs, aren't the collected data also likely to be influenced by these models' bias and unreliability?

About experiments  
6. Do other non-LLaVA VLMs, e.g. InternVL-2-8B, trained with the FEEDQUILL-collected preference data also show superior results on downstream tasks?  
7. How many FEEDQUILL preference data are used for training in the last row of Table 2?

Minor comments  
8. Line 319: "..., responses with fewer hallucinations are often inherently less helpful." Is this sentence correct?  
9. Typo in line 334: "In To fully exploit the characteristics ..."

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
This paper propose:
1. DCScore: a metric to evaluate both hallucination and comprehensiveness


2. DeCapBench: an image captioning benchmark (contains only testing dataset) for hallucination evaluation


3. FeedQuill: a method to mitigate hallucination in vision-language models (VLMs), which consists of the following steps:
  - (1) Collect the responses from VLMs. 
  - (2) Employ LLM to decompose the responses into primitive information units. 
  - (3) Use an off-the-shelf VLMs to verify the correctness of each information units. 
  - (4) Label data as positive or negative based on the verification scores.
  - (5) Train a reward model with preference dataset constructed in (4).
  - (6) Fine-tune the target VLM to generate less hallucinated and more enriched captions through PPO.

Finally, several vl benchmarks are achieved as SOTA performance.

### Strengths
- Mitigate the hallucination issues in VLM is crucial, especially in the detailed image captioning task.
- The proposed metric DCScore sounds reasonable, is provided with a comprehensive comparison with previous metrics (e.g., Faithscore and RLAIF-V), and is demonstrated high consistency with human evaluation.
- The conducted experiments and related ablation studies are extensive.

### Weaknesses
1. Section 3.2 does not introduce the instructions provided to human annotators for scoring image captions. Disclosing the task instruction for annotators is crucial; if the basis for scoring largely aligns with the design of an automated metric, the metric will likely benefit in correlation assessments.
2. DCScore relies on the hyper-detailed human captions in the ImageInWords dataset. However, as "a picture is worth a thousand words," reference descriptions might not fully reflect all the semantics of an image, while the model may describe image details that are correct but not mentioned in the reference caption.
3. The proposed metric conceptually resembles prior works like FaithScore and RLAIF-V (I am delighted to see this discussed in Appendix). The divide-and-conquer approach and evaluation using LLMs is not novel. Collecting preference data for model optimization is also a consensus in the research community. While I see no other obvious flaws, **I am not fully convinced of the overall contribution**.

### Questions
Please answer my questions in “weaknesses” section.

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
This work introduces a specialized metric (**DCScore**) and a benchmark (**DeCapBench**) for detailed image description evaluation. The core idea is to break down the reference and generated caption into the "smallest self-sufficient units", and then quantify the precision and recall of information units conveyed by the generated caption. The authors demonstrate that the new metric and benchmark achieve the best consistency with human evaluations. In addition, based on a similar concept, the authors propose a method (**FeedQuill**) for automatically constructing preference data for RLHF. Extensive experiments validate that the collected preference data can train a strong image captioning model.

### Strengths
1. This paper introduces a new metric and benchmark for evaluating the quality of detailed image captions. Correlation analysis with human evaluations indicates that these new assessments are effective and superior.
2. This paper presents an efficient method for collecting preference data and demonstrates that such data can be used to build more effective image captioning models.
3. The experiments are comprehensive. The authors’ claims are well-supported by substantial experimental evidence, and they have conducted detailed ablation studies, providing valuable best practices for the community.
4. The paper is well-written with clear figures and tables, effectively conveying information.

### Weaknesses
1. Section 3.2 does not introduce the instructions provided to human annotators for scoring image captions. Disclosing the task instruction for annotators is crucial; if the basis for scoring largely aligns with the design of an automated metric, the metric will likely benefit in correlation assessments.
2. DCScore relies on the hyper-detailed human captions in the ImageInWords dataset. However, as "a picture is worth a thousand words," reference descriptions might not fully reflect all the semantics of an image, while the model may describe image details that are correct but not mentioned in the reference caption.
3. The proposed metric conceptually resembles prior works like FaithScore and RLAIF-V (I am delighted to see this discussed in Appendix). The divide-and-conquer approach and evaluation using LLMs is not novel. Collecting preference data for model optimization is also a consensus in the research community. While I see no other obvious flaws, **I am not fully convinced of the overall contribution**. I look forward to being further convinced by the authors and other reviewers.

### Questions
1. The main experiments employ LLaVA-Onevision-7B. Why was this setting not maintained consistently in other experiments? For instance, the ablation study “Preference Data for Reward Model” used LLaVA-1.5-7B, and the “Source of Response” experiments used LLaVA-1.5-13B.
2. In Appendix A.1.1, the authors claim that DCScore accounts for non-descriptive elements, unlike other metrics. Could the authors further explain why it is important to consider **non-descriptive** elements in **image captioning** tasks, which aim to generate descriptions for images?

### Soundness
4

### Presentation
4

### Contribution
3
