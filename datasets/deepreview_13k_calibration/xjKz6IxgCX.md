# SafeWatch: An Efficient Safety-Policy Following Video Guardrail Model with Transparent Explanations

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 8, 6

## Abstract
\vspace{-0.2em}
With the rise of generative AI and rapid growth of high-quality video generation, video guardrails have become more crucial than ever to ensure safety and security across platforms. Current video guardrails, however, are either overly simplistic, relying on pure classification models trained on simple policies with limited unsafe categories, which lack detailed explanations, or prompting multimodal large language models (MLLMs) with long safety guidelines, which are inefficient and impractical for guardrailing real-world content.
To bridge this gap, we propose \algname, an efficient MLLM-based video guardrail model designed to follow customized safety policies and provide multi-label video guardrail outputs with content-specific explanations in a zero-shot manner.
In particular, unlike traditional MLLM-based guardrails that encode all safety policies autoregressively, causing inefficiency and bias,
\algname uniquely encodes each policy chunk in parallel and eliminates their position bias such that all policies are attended simultaneously with equal importance.
In addition, to improve efficiency and accuracy, \algname incorporates a policy-aware visual token pruning algorithm that adaptively selects the most relevant video tokens for each policy, discarding noisy or irrelevant information. This allows for more focused, policy-compliant guardrail with significantly reduced computational overhead.
Considering the limitations of existing video guardrail benchmarks, we propose \datasetname, a large-scale video guardrail benchmark comprising over 2M videos spanning six safety categories which covers over 30 tasks to ensure a comprehensive coverage of all potential safety scenarios. 
We have conducted extensive experiments, showing that \algname outperforms all SOTA video guardrails on \datasetname by 28.2\%, and achieves a 13.6\% improvement on existing benchmarks, all while reducing inference costs by an average of 10\%.
\algname also demonstrates strong policy-following abilities and outperforms previous SOTAs by 5.6\% and 15.6\% in zero-shot generalizability to new policies and new prompting tasks.
Additionally, both LLM-as-a-judge and human evaluators confirm the high quality of the explanations provided by \algname.
Our project is open-sourced at \url{https://safewatch-aiguard.io}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents an MLLM-based video guardrail model that takes into account safety policies to provide a multi-label video content output including explanation, considering both the safety policies and the video content. The proposed model comprises two plug-and-play modules to improve latency of the guard rail model and mitigate positional biases by breaking down the safety guidelines. This work also introduces a benchmark for video guardrailing using multi-agent consensus and comparison across existing MLLMs.

### Strengths
- The paper addresses a critical topic by proposing guardrails for video MLLMs based on defined safety policies, which is timely and important with the rise of MLLMs.
- It introduces a baseline model built upon the InternVL2-8B backbone and leverages two plug-in modules to (1) improve latency during training and inference, and (2) reduce positional biases related to the policy order.
- The benchmark provides a comprehensive evaluation of existing MLLMs on video guardrailing tasks, demonstrating the model’s effectiveness across six safety policy categories, covering 30 subtopics.

### Weaknesses
 - Details about the training and testing splits within the benchmark are insufficient, leaving questions about data partitioning.
- The authors should clarify if any videos were discarded during dataset curation due to multi-agent discussion pipelines not reaching a consensus or human verification disagreements on final explanations. This clarification could shed light on the multi-agent approach's effectiveness in generating explanations that align with human perspectives, especially given video content's subjective nature.

### Questions
- SFT Baseline: Could the authors provide additional context for the "SFT baseline" mentioned in Figure 5?
- Inference Cost: What accounts for the increase in inference cost with additional few-shot examples, as illustrated in Figure 5?

### Soundness
3

### Presentation
4

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
SAFEWATCH is a new video moderation system that efficiently identifies harmful content and explains its decisions. It features two main innovations: PEPE (for parallel policy encoding) and PAP (for selective video analysis), both designed to make the system faster and more accurate. The researchers also developed SAFEWATCH-BENCH, a large dataset containing 2 million videos across six categories of harmful content, which they used to train and test their system.

### Strengths
1. The authors contribute a very large-scale benchmark for video security
2. The authors propose the PEPE algorithm, which can mitigate positional bias in the input
3. The authors propose the PAP algorithm, which maintains high recognition accuracy while reducing inference costs

### Weaknesses
1. The working mechanism of the PEPE algorithm lacks detailed theoretical explanation or experimental validation. The authors conduct ablation experiments to prove the effectiveness of the PEPE algorithm, but they don’t provide sufficient proof of its underlying principles. In lines 293-297, the authors claim that the PEPE algorithm can provide independent representations for each policy, which can alleviate the position bias problem in MLLM mentioned in lines 266-269. **However, regarding this claim, there are neither experimental designs nor mathematical proofs to support it. I have doubts about whether the mechanism behind the algorithm truly aligns with the authors' claims.** Specifically, the claim that PEPE allows for independent encoding of policies requires more rigorous justification. The ablation studies, while demonstrating performance improvements, do not sufficiently explain *how* PEPE achieves this independence. A detailed analysis of the attention weights or feature representations before and after applying PEPE is needed to validate this claim. Furthermore, the authors should provide a mathematical formulation of the PEPE mechanism to show how it mitigates positional bias, rather than relying solely on empirical results.
    
2. There is a lack of explanation regarding the effectiveness of the multi-agent propose-discuss pipeline mentioned in line 105. The authors mention in lines 105-106 that they use a novel pipeline for data annotation, but there is limited discussion about this pipeline. In the pipeline-related content, the authors do not cite any references, and based on my knowledge of related work, this pipeline has not been used in any previous work, making this the first work to employ this pipeline. Given this, **I am uncertain whether this pipeline can provide sufficiently high-quality annotation results**, and the authors have not provided any quality analysis of the annotation results. The description of the multi-agent pipeline is vague, lacking details on the specific roles of each agent, the communication protocols, and the criteria for reaching a consensus. Without a clear understanding of these aspects, it is difficult to assess the reliability of the annotation process. Furthermore, the authors should provide quantitative metrics to evaluate the annotation quality, such as inter-annotator agreement or comparison with human-annotated data.

### Questions
1. Could the authors design corresponding experiments and proofs to demonstrate that the mechanism producing the algorithm's effects aligns with their claims that the PEPE algorithm can "allow each policy to be encoded independently and in parallel" and that "equivalent positional embedding ensures that different policies are treated without bias"?
2. Could the authors provide some quantitative analysis of the annotation quality? Can this pipeline approach human-level annotation quality? Compared to annotation by a single LLM/VLM, what advantages does incorporating Multi-agent Discussion bring?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors of the paper propose a multimodal large language model (MLLM) called SafeWatch, designed to follow customized safety policies and provide multi-label video guardrail categorical outputs with answer explanations in a zero-shot manner. They also introduce SafeWatch-Bench, a large-scale video guardrail benchmark containing over 2 million videos spanning 6 safety broad categories and covering over 30 finer-grained risk categories to ensure comprehensive coverage of potential safety scenarios.

The technical contributions include:
- Model Design: The authors introduce two key plug-and-play modules: Parallel Equivalent Policy Encoding (PEPE) and Policy-Aware Adaptive Pruning (PAP). 
  - PEPE mitigates high latency from extensive input contexts and policy positional bias by dividing lengthy safety guidelines into independent chunks encoded in parallel with equal importance. 
  - PAP, on the other hand, reduces latency by selecting the most relevant visual tokens for each policy while discarding those with low relevance.

- Data: Each instance in SafeWatch-Bench is annotated with multi-label guardrail categories and detailed explanations. The dataset includes 2 million videos—both real-world and generative from various SOTA models—comprising an instruction-tuning set and a test set of 1K hand-selected, high-quality annotated videos across subcategories.

- Training strategy: The authors fine-tune InternVL2-8B with their modeling changes on this new data via three stages, i.e., multi-task training, adaptive-pruning training, and preference post-tuning. 
  - Stage 1: Only PEPE is trained during this stage on a large corpus of unsafe videos, as well as traditional VQA and captioning tasks on normal videos. 
  - Stage 2: Both PEPE and PAP are fine-tuned on guardrail tasks. 
  - Stage 3: Preference pairs are curated to enable the preference post-tuning.

### Strengths
1. Their model, SafeWatch, outperforms SOTA video guardrails on SafeWatch-Bench by 19.6% and on existing benchmarks by 15.4%, while reducing inference costs by an average of 25%. SafeWatch also demonstrates strong policy-following abilities, outperforming baselines by 20% in zero-shot adaptability to new policies. Additionally, both LLM-as-a-judge and human evaluators confirm the high quality of the explanations provided by SafeWatch.
2. The design choices are well-founded, following best practices for efficient MLLM construction.
3. This is an important area of study, with meaningful contributions (if these contributions are reproducible).

### Weaknesses
1. Missing Evaluation: The evaluation of the Safety-aware Event Sampling step is absent. This step should be crucial for model performance, as the authors used TransnetV2 to segment videos into safety-aware events, sampling a single frame per event for further MLLM processing. The lack of evaluation makes it difficult to assess the impact of this step on the overall performance of SafeWatch. It is unclear how well the event sampling captures the relevant information for safety analysis, and whether the selected frames are truly representative of the events they are supposed to represent.

2. Dataset Clarity: The dataset’s specifics and its exact use in model training remain unclear. For instance, there is no information on the average video length or the typical length of an explanation in SafeWatch-Bench. Additionally, the quality of the SafeWatch-Bench test set is not fully addressed, which is particularly important for an evaluation dataset. The absence of these details makes it difficult to assess the dataset's complexity and diversity, and whether it is sufficiently challenging to evaluate the model's capabilities. Furthermore, the lack of clarity on the test set's quality raises concerns about the validity of the evaluation results.

3. Reproducibility Concerns: Reproducibility in data collection and model training is questionable. For instance, Section 4.2 on "multi-agent consensus video annotation" provides a basic idea of the processes but lacks sufficient detail for replication (e.g., missing the prompts used, configurations such as the number of frames used for each model, etc.). Additional issues are noted in the "Questions" section. The lack of detailed information about the annotation process and model training makes it difficult for other researchers to reproduce the results and build upon this work. The multi-agent annotation process, in particular, needs more clarity on the prompts, model configurations, and the number of iterations required for convergence.

### Questions
1. Could you provide some evaluation results for Safety-aware Event Sampling? Currently, its effectiveness or limitations are unclear.
2. Is SafeWatch-Bench truly a video benchmark? Specifically, does it truly require reasoning across multiple frames for a model to achieve high performance?
3. It appears that humans do not directly provide annotations for SafeWatch-Bench; instead, annotations are model-generated, with human reviewers checking if re-annotation is necessary. In the caption for Figure 2, you mention that the 1K test set has high-quality annotations. Were these test set annotations created directly by humans, or were they produced via the multi-agent propose-discuss-consensus pipeline?
4. Could you describe how the preference pairs were curated for the preference post-tuning stage? Additionally, how were the challenging benign examples—those easily identified by humans but likely to mislead guardrail models—selected? A detailed explanation of these curation processes would be helpful.
5. What is the quality of the synthetic videos generated by the GenAI models? Are they accurately aligned with the unsafe prompts? Was any video filtering applied to filter out misaligned videos?
6. Could you clarify your model training data recipe? Are the unsafe videos used in stage-1 training and the guardrail tasks in stage-2 training drawn from the instruction-tuning dataset within SafeWatch-Bench? Additionally, how many samples are used for each stage, task, and dataset?
7. Which layers are tuned in the preference post-tuning stage?
8. In Table 3 of Appendix A.1, there is a column named "Temporal location". What does it mean?
9. What is the SFT Baseline mentioned in Figure 5 and Table 5?
10. It was claimed that prior datasets lack detailed descriptions of the videos, suggesting that SafeWatch-Bench offers a detailed description for each video. Is that correct?
11. There is unsafe content in SafeWatch-Bench. Will SafeWatch and SafeWatch-Bench be released? If so, how do you plan to ensure their proper use?

Minor comments:
Line 749 has placeholder text.

### Soundness
3

### Presentation
4

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
The paper proposed a safety aware video understanding benchmark, including 2M human verified videos. The unsafe scenarios are separated into 6 classes. The authors also design a pipeline for automatically data generation. For the video understanding model, the authors propose the Parallel Equivalent Policy Encoding and Policy-Aware Adaptive Pruning to encode the Safety Policy Guidelines and reduce the redundancy. The result of the trained model is good comparing to both close- and open- source models.

### Strengths
1. The proposed dataset is novel and the data curation procedure is well-organized.
2. The proposed Parallel Equivalent Policy Encoding and Policy-Aware Adaptive Pruning can effectively encode the Safety Policy Guidelines and reduce the redundancy of video tokens.
3. The results are good.

### Weaknesses
1. Dataset Construction: 
       (1) The release and separation of the dataset is a concern. The author can only provide links to publicly available sources and annotations. But it is common that the link may fail.I understand that this is something unavoidable, but it will undoubtedly reduce the frequency of use and impact of this dataset.
       (2) 2M videos for human verification is a huge effort, the authors don't provide any details of the procedure.

2. Model training：
      (1) Some of the training procedure is ambiguous, there should be more details about Preference Post-tuning procedure.

### Questions
1. The author mentioned that Human Verification is used for curating the 2M video benchmark. Can the authors make a detailed description of the Human Verification procedure?

2. More procedure should be enclosed in the appendix.

### Soundness
3

### Presentation
3

### Contribution
3
