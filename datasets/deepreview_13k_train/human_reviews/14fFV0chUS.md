# TRACE: Temporal Grounding Video LLM  via Causal Event Modeling

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Video Temporal Grounding (VTG) is a crucial capability for video understanding models and plays a vital role in downstream tasks such as video browsing and editing. 
To effectively handle various tasks simultaneously and enable zero-shot prediction, there is a growing trend in employing video LLMs for VTG tasks. However, current video LLM-based methods rely exclusively on natural language generation, lacking the ability to model the clear structure inherent in videos, which restricts their effectiveness in tackling VTG tasks. To address this issue, this paper first formally introduces \framework framework, which represents videos as sequences of events, and predict the current event using previous events, video inputs, and textural instructions. Each event consists of three components: timestamps, salient scores, and textual captions. We then propose a novel task-interleaved video LLM called \alg to effectively implement the \framework framework in practice. 
The \alg processes visual frames, timestamps, salient scores, and text as distinct tasks, employing various encoders and decoding heads for each. Task tokens are arranged in an interleaved sequence according to the \framework framework's formulation.
Extensive experiments on various VTG tasks and datasets demonstrate the superior performance of \alg compared to state-of-the-art video LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes a new method for Video Temporal Grounding (VTG) tasks, named TRACE. TRACE uses a causal event modeling framework to represent videos as a sequence of events with timestamps, salient scores, and textual descriptions. The paper designs a task-interleaved video large language model to address the limitations of traditional video LLMs in handling the inherent structure of videos. The TRACE model utilizes different encoders and decoding heads to process visual frames, timestamps, and text inputs, enabling more effective event sequencing and causal modeling. Experimental results demonstrate that TRACE achieves state-of-the-art zero-shot performance on various VTG tasks and, after fine-tuning, can match the performance of traditional non-generative, task-specific models.

### Strengths
1. The paper proposes TRACE, a framework leveraging causal event modeling to generate structured video representations through large language models (LLMs). This approach addresses structural gaps in video data, making it valuable for multi-modal research and practical applications in video analysis.
   
2. TRACE maximizes the potential of pre-trained LLMs by adopting causal event modeling, which decomposes video inputs into frames and aligns them with textual prompts. The temporal segmentation and alignment methods allow videos to be broken down into events with associated timestamps, salient scores, and captions. This granularity is crucial for precise video event parsing and presents a significant step forward in video understanding with LLMs.

3.TRACE outperforms the existing Video-LLMs on three pivotal Video Temporal Grounding (VTG) benchmarks—Charades-STA, QV Highlights, and YouCook2—underscoring its efficacy and robustness in handling video temporal grounding tasks. This achievement underscores TRACE's ability to accurately capture and model the intricate temporal dynamics across a spectrum of video datasets.

### Weaknesses
1.	While causal event modeling is presented as a core contribution of this work, the related work section does not address any prior research on similar methodologies. It would be helpful to clarify whether comparable approaches have been explored in the field of video understanding, or if this approach is entirely novel within this domain. Providing this context could strengthen the argument for the method’s originality and situate it more clearly within existing research.

2.	It is unclear whether compressing visual features to 8 tokens is sufficient for preserving critical information in complex video scenes. The paper does not provide an analysis or experimental results on the trade-off between the number of tokens and model performance, which would be valuable in understanding the potential impact of this compression choice.

3.	There are several grammatical and spelling errors throughout the manuscript, which impact readability and may detract from the paper’s clarity. For example: Line 22: "processes" should be corrected to "process". Line 44-45: The phrase "...which,..." should be rephrased, and "lacks" should be changed to "which lack".

### Questions
No additional questions. Please see the "Weaknesses" section for areas needing clarification.

### Recommendations for Improvement:
- **Refine Prompt Design Explanation:** Providing specific strategies or insights on prompt design tailored for VTG tasks would enhance the paper's originality and usefulness for future researchers.
  
- **Explore Custom Scene Parsing Techniques:** Introducing refined parsing methods could strengthen TRACE's robustness and accuracy in multi-modal alignment.

This structured feedback should provide the authors with a comprehensive view of the strengths and areas for enhancement in their paper on TRACE.

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
3

### Summary
The paper introduces a task-interleaved video LLM, TRACE, which incorporates a newly-designed causal event modeling framework for VTG task. The TRACE employs multiple encoders for different inputs, while the task tokens are arranged in an interleaved manner. TRACE demonstrates SOTA performance on various VTG datasets compared to previous video LLMs.

### Strengths
1. The presentation and illustration are quite clear and easy to follow.
2. The motivation of causal event modeling is quite intuitive and the design is straightforward and yet effective.
3. The zero-shot performance is superior compared to previous video LLM methods.

### Weaknesses
1. While the paper compares TRACE with other video LLMs, it presents limited comparison and may not adequately address how it stands against traditional non-generative and task-specific models.
2. The extent to which TRACE can be applied to other types of video tasks beyond VTG is unclear. Its design may be highly specialized, which could limit its applicability across diverse video understanding tasks. Authors should present more results on other video-understanding tasks since the design seems generalizable by building such causal event relations.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the task of Video Temporal Grounding (VTG) and introduces TRACE, a task-interleaved Video-LLM designed for enhanced VTG performance. The authors highlight limitations in current Video-LLMs, which rely solely on natural language generation without considering the inherent temporal structure of videos. To address this, they propose a novel causal event modeling framework, decomposing videos into sequences of events defined by timestamps, salient scores, and textual captions. Extensive experiments on datasets such as Charades-STA, QVHighlights, and YouCook2 demonstrate the superior zero-shot performance of TRACE compared to existing Video-LLMs.

### Strengths
1) Video Temporal Grounding (VTG) is a crucial task, yet current Video-LLMs underperform in this area. Techniques aimed at improving temporal grounding for these models are highly valuable to advance the field.
2) The causal event modeling framework fits well with the next-token prediction paradigm of large language models (LLMs), offering an intuitive way to model video structures in sequential tasks.
3) TRACE demonstrates consistent performance improvements over prior Video-LLMs across three key VTG benchmarks (Charades-STA, QVHighlights, and YouCook2), underscoring its effectiveness.

### Weaknesses
1) While the motivation for TRACE is clear, the use of multiple task-specific heads may limit the model’s generalization. A primary appeal of Video-LLMs lies in their ability to handle a variety of tasks without specific fine-tuning. TRACE’s focus on VTG may narrow its versatility, making it less effective for general video understanding tasks. In most cases, lightweight VTG-specific models with stronger performance could be more suitable for VTG scenarios.
2) Some clarity is not clear. For example, the paper does not adequately explain slot-based compression, which is not a widely known technique. Moreover, compressing each frame to just 8 visual tokens might lead to significant information loss, raising concerns about the trade-off between efficiency and accuracy. The paper does not provide sufficient justification for using slot-based compression over other established methods like Q-Former or 2D average pooling. Furthermore, the chosen compression rate of 8 tokens per frame seems arbitrary and lacks a thorough analysis of its impact on performance.
3) It is unclear whether the same set of number tokens is used for both timestamps and scores. If so, this could blend the two types of information, contradicting the authors' claim (lines 45–46) that the model preserves the distinct structure of video events. The lack of clarity regarding the tokenization process for timestamps and scores raises concerns about the model's ability to effectively differentiate and utilize these distinct types of information.

### Questions
See Weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a new Video Temporal Grounding (VTG) method that addresses the shortcomings of existing LLM in handling VTG tasks by modeling causal events.

### Strengths
The author first employs a causal modeling method in the grounding of VLLM, achieving causal probability modeling through the sequence of input tokens. This approach will provide inspiration for future work on video understanding tasks using VLLM.

### Weaknesses
1. **Autoregressive modeling.**

One of my major concerns is that the authors have only used the earlier events $e_{1:k-1}$ in their modeling of causal relationships between events through autoregression, without incorporating the equally known $e_{k+1:K}$. I believe this approach may be unreasonable since it is likely that the same events may occur earlier while the current event is different due to unrelated pretexts. However, this issue can be avoided by modeling different subsequent events simultaneously. Besides, most current video understanding researchers have modeled multiple events by utilizing all contextual events that occur before and after them [1-4]. This may require the authors to provide further explanation.

[1] Liang C, et al. Visual abductive reasoning[C]. CVPR 2022.

[2] Lam T E, et al. CausalChaos! Dataset for Comprehensive Causal Action Question Answering Over Longer Causal Chains Grounded in Dynamic Visual Scenes. NeurIPS 2024.

[3] Chen T, et al. MECD: Unlocking Multi-Event Causal Discovery in Video Reasoning. NeurIPS 2024.

[4] Du Y, et al. Towards Event-oriented Long Video Understanding. ArXiv 2024.

2. **Inference speed.**

The authors have adopted a form similar to autoregression, and I would like to understand if there is a time overhead in comparing their model's inference speed to that of current mainstream LLMs.

3. **LLM backbone.**

I noticed that the authors used Mistral-7B as the LLM backbone, however, in other comparison methods, Timechat used LLaMA-2, while HawkEye, Momentor, and VTimeLLM used Vicuna. I would like to know if the authors have conducted experiments with LLaMA-2 or Vicuna as the LLM backbone, to ensure that the superior performance is not due to the better LLM backbone but rather the causal modeling.

### Questions
My main concern is with the autoregressive modeling approach, and if the authors can provide a reasonable explanation, I am willing to consider raising my score, as I believe this work could provide inspiration for future work.

### Soundness
3

### Presentation
3

### Contribution
3
