# Visual Description Grounding Reduces Hallucinations and Boosts Reasoning in LVLMs

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 6, 6, 8

## Abstract
\vspace{-2mm}

Large Vision-Language Models (LVLMs) often produce responses that misalign with factual information, a phenomenon known as hallucinations. While hallucinations are well-studied, the exact causes behind them remain underexplored. In this paper, we first investigate the root causes of hallucinations in LVLMs. Our findings reveal that existing mitigation techniques primarily reduce hallucinations for visual recognition prompts—those that require simple descriptions of visual elements—but fail for cognitive prompts that demand deliberate reasoning. We identify the core issue as a lack of true visual perception in LVLMs: although they can accurately recognize visual elements, they struggle to fully interpret these elements in the context of the input prompt and effectively link this recognition to their internal knowledge, which is critical for reasoning. To address this gap, we introduce \textbf{Visual Description Grounded Decoding} (VDGD), a simple, robust, and \textit{training-free} method designed to enhance visual perception and improve reasoning capabilities in LVLMs. VDGD works by first generating a detailed description of the image and appending it as a prefix to the instruction. During response generation, tokens are sampled based on their KL divergence to the description, favoring candidates with lower divergence. Experimental results on multiple visual reasoning benchmarks and LVLMs demonstrate that VDGD consistently outperforms existing baselines  2\% - 33\%. Finally, we introduce VaLLu, a benchmark designed for comprehensive evaluation of the cognitive capabilities of LVLMs.edu. * denotes equal technical contribution.}
\vspace{-2mm}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors argue that the current LVLMs and hallucination mitigation decoding strategies lack visual perception capabilities. Through extensive analyses, the authors delve into such deficiency across cognitive and real-world benchmarks and categorize more detailed hallucination taxonomies beyond mere object hallucination: Language Hallucination / Vision Hallucinations / Style Hallucinations / IT Hallucinations. At the end, the authors introduce a new decoding strategy, VDGD, which prefixes the model's detailed descriptive response to the given input and truncates grounding of its intermediate responses to refine the final answers.

### Strengths
Through section 3 and 4, in this paper, the authors extensively explored hallucination issues across various benchmarks, models, and decoding strategies. The novel taxonomies beyond simple object hallucination are crucial to understand the current problems in hallucination research areas (particularly LVLM).

### Weaknesses
Even with the new hallucination categories, and new findings, their approach, VDGD, lacks of analyzing its effectiveness on the new hallucination categories they defined and limited for its computational costs due to successive response generation. The analysis of VDGD's performance is primarily focused on overall accuracy gains, without a detailed breakdown of how it mitigates each specific type of hallucination (Language, Vision, Style, IT) identified in the paper. This makes it difficult to ascertain whether the method is truly addressing the root causes of different hallucination types or merely improving overall scores through a general effect. Furthermore, the computational cost analysis is insufficient, lacking a detailed breakdown of the time spent on each stage of VDGD, particularly the initial caption generation and the subsequent grounding process. This makes it hard to assess the practical applicability of the method, especially for real-time or resource-constrained scenarios.

### Questions
1. How can hallucinatory results be mitigated using the proposed VDGD in the newly defined hallucination categories, compared to other decoding strategies? Analyses through section 3 and 4 are really intriguing, but the reviewer belives that there is significant gap to bridge such motivation and findings into the VDGD design.


2. The method of VDGD is limited to merely prefixing self-generated model response and relying on the first generated response that the model predicts (ironically this may include a lot of hallucinatory responses-even if limitation section mentioned this). Considering LLMs are more prone to hallucination snowballing rather than error correction, it is unclear where the performance gains are derived from. Unlike original contrastive decoding, VDGD cannot make logit corrections by counteracting with premature models and relies solely on vocabulary truncation.


3. Computational analyses should be conducted such as throughput or latency. Also, can this VDGD be seamlessly applied to beam search decoding? Then, how will be the result comparison?

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
This paper focuses on the cognitive reasoning aspect of hallucination in large vision language models. Through a set of analysis and experiments, it demonstrates that the core blocker of this issue is the difficulty of linking recognized visual concepts to the internal knowledge of LLM. Therefore, the paper further proposes a simple method that per-appendes the image description to the text instruction as the full instruction so that the model can better leverage its reasoning capacity. Evaluation shows that this method can achieve consistent performance improvement on reasoning-focused benchmarks.

### Strengths
1. The problem of cognitive reasoning in hallucination is interesting and seems to be under-explored in previous works.
2. The analysis is sufficient, solid, and easy to follow, yielding several interesting insights.
3. The proposed method, although appears to be very simple, is based on the analysis on "language grounding" in previous sections, which has a reasonable motivation of such design.
4. The method demonstrates consistent improvements across benchmarks.

### Weaknesses
1. This method seems to be limited in science domain, e.g., chart understanding and reasoning. The underlying assumption of the method is that the image can be sufficiently described by texts. It might hold true for science images, e.g., one can easily describe a chart by enumerating all the involved data or simply transforming the chart figure into a table. However, for natural scenes with complex object categories, attributes, and relations, it is almost impossible to fully represent the image with texts. The evaluated benchmarks seems to be focused on such kind of data.
2. Based on my first point, I may suspect that the essential reason of the performance improvement comes from that chart figure is more intuitive for human eyes while text descriptions of data is more suitable for LLM to understand. It may has little relation with **cognitive reasoning**.
3. Also, based on my first point, we'd better not simply regard such science data as reasoning, there can be other forms of reasoning in natural scenes according to some related works [1].
4. The analysis, though informative, takes too much space, and it may have overlap with previous works [2]. For example, categorization of hallucination types in this paper is essentially based on the **cause** of hallucination, which has been discussed in previous works.
5. Moreover, the the experiments and investigation of the proposed method seems to be limited. It is better to involve more ablation studies.
6. The related works is somehow limited. I understand it might be constrained by the space, but it's important to review and discuss related works about hallucination, reasoning, benchmarks, and so on [2] [3].

### Questions
Please see weaknesses part.

### Soundness
3

### Presentation
4

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
This paper addresses the problem of hallucinations in LVLMs. Strictly speaking, the authors provide a way to understand the root cause of such hallucinations in LVLMs. They claim that existing approaches for hallucination mitigation only focus on the visual recognition aspect of the model, and do not dive further into understanding whether the model actually has cognitive skills, thus failing to mitigate hallucinations properly from such models. The authors first conduct a study to investigate the various causes of hallucinations in LVLMs. Then they introduce VDGD, a training-free method to mitigate said hallucinations from an LVLM, and finally propose VaLLu, a benchmark to evaluate cognitive reasoning capabilities of LVLMs.

### Strengths
1) The paper is well written and nicely presented.
2) The authors present a classification of different types of halluciantions
3) The authors recognize the gap between visual recognition capability of a model and ability to utilize it for cognitive tasks
4) The authors propose a training-free strategy to mitigate hallucinations

### Weaknesses
1) Sections 3.1 and 3,2 are not that informative about the failure of hallucination techniques on cognitive tasks. The claim in 3.1 that all methods boost performance on AMBER but not on other datasets is weak since even on AMBER, the relative performance increase is small, which is the same for other datasets as well. This goes against the claims of these two sections. The performance gains on AMBER, while present, are not substantial enough to strongly support the claim that existing methods are effective only on this dataset, especially considering the marginal improvements observed on other datasets. The lack of a clear and significant performance gap across datasets weakens the argument that current techniques are specifically tailored for visual recognition tasks and fail on cognitive tasks.

2) In section 3.3, in the algorithm, firstly, currently it says that it is a language hallucination if base rank is less than 0. How is a rank less than zero? I think it should be language hallucination if it does not fall inside the visual elements of the response. Moreover, I think you are using GPT-4 vision, and not just GPT-4 for this? Also, the visual content extraction itself will have hallucinations due to use of llama-3. Further, pushing everything first to IT hallucination definitely skews the outputs of visual and style hallucinations, it can be both. And so the results showing huge IT hallucination compared to the other two is misleading. The algorithm's reliance on a base rank less than zero for identifying language hallucinations is problematic, as ranks are typically non-negative. The method for classifying hallucinations, prioritizing information transfer (IT) hallucinations, introduces a bias that may inflate the count of IT hallucinations at the expense of visual and style hallucinations. The use of Llama-3 for visual content extraction may also introduce its own set of hallucinations, further complicating the analysis.

3) Experiment on 4.1 showing fall of rank as length of text prompt increases is nice, but it is also bound to happen since the textual context is getting added. This does not definitively prove that no image context is being attended to. Also, the rank difference between the two datasets is just 1. The observed decline in rank as the text prompt length increases does not conclusively demonstrate a lack of attention to image context, as the addition of textual context is a confounding factor. The relatively small rank difference between the two datasets further weakens the claim that image context is not being attended to.

4) The gpt-type metric the authors propose is claimed to have high correlation with the human responses. But in appendix we see that the other correlations are also quite high, with a normal benchmarks having a 0.92 correlation compared to author's 0.96. This marginal difference is not significant enough to claim for a new type of evaluation protocol. The proposed GPT-based evaluation metric, while showing a high correlation with human responses, does not offer a substantial improvement over existing benchmarks, given the marginal difference in correlation scores. The claim that this metric is a significant advancement over traditional evaluation protocols is not strongly supported by the presented correlation values.

### Questions
1. In Sections 3.1 and 3.2, you mention that existing hallucination mitigation techniques improve performance on AMBER but not on other datasets. Could you provide quantitative results for this to show this?

2. In Section 3.3, the algorithm indicates that a base rank less than zero signifies a language hallucination. Since ranks are typically non-negative, could you explain how a rank can be less than zero in this context?

3. The algorithm seems to classify instances as information transfer (IT) hallucinations first, which might influence the distribution of hallucination types. How do you ensure that this approach doesn't skew the results, particularly the higher incidence of IT hallucinations compared to visual and style hallucinations?

4. In Section 4.1, you observe a decline in rank as the text prompt lengthens, suggesting reduced attention to image context. Given that longer prompts naturally introduce more textual context, how do you differentiate between the model's reliance on textual versus visual information in this scenario?

5. Your proposed GPT-based evaluation metric shows a correlation of 0.96 with human responses, while existing benchmarks have a correlation of 0.92. Considering this marginal difference, what advantages does your metric offer over traditional evaluation protocols?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a comprehensive and extensive analysis on object hallucination. It proposes VDGD, a method that generates descriptions first, which are then used as prompts for a second inference. During decoding, KLD is calculated with the pre-generated descriptions to identify highly deviant candidates. The authors curate several datasets and introduce the VaLLu benchmark for a comprehensive hallucination evaluation.

### Strengths
### S1. The paper is well-structured and comprehensive, providing a smooth overall flow.

### S2. The analysis is in-depth and offers interesting insights.

### S3. The VaLLu benchmark has the potential to serve as a comprehensive benchmark for evaluating hallucinations in models.

### Weaknesses
### W1. While the idea is simple and effective, a significant drawback is the latency. The proposed method requires generating long descriptions even for short responses (e.g., in Fig. 8, a single token output would typically be very fast in a baseline method, but the proposed method is much slower). Therefore, it is important to include a latency analysis (e.g., average inference time, throughput) compared to simpler decoding-based hallucination mitigation methods [1,2,3] and baseline LVLMs, especially since many recent training-free methods perform a single inference. The latency analysis should consider the overhead of generating the intermediate description and the subsequent prefill phase, which involves a significant number of tokens, making it potentially much slower than methods that directly generate the final response. A detailed breakdown of latency for each step of the pipeline is crucial to understand the computational cost. Furthermore, the specifics of the “small captioning model” need clarification, including its architecture and computational requirements.
[1] Don’t Miss the Forest for the Trees: Attentional Vision Calibration for Large Vision Language Models, Arxiv 2024.  
[2] Seeing is Believing: Mitigating Hallucination in Large Vision Language Models via CLIP-Guided Decoding, Arxiv 2024.  
[3] RITUAL: Random Image Transformations as a Universal Anti-hallucination Lever in LVLMs, Arxiv 2024. 

### W2. Using the description from the first inference as a prompt for the second inference appears to act like a form of Chain-of-Thought (CoT) prompting. The authors should explicitly discuss how VDGD relates to or differs from Visual CoT methods [4,5,6], and compare several aspects (e.g., performance, computational requirements, applicability to different types of tasks). Comparisons or references to recent Visual CoT methods will strengthen the paper. The discussion should include how the proposed method's approach to generating intermediate descriptions compares to methods that generate scene graphs or visual tables, and how these different intermediate representations affect the final response. A more comprehensive comparison, even if not fully experimental, is needed to contextualize the contribution.
[4] Compositional Chain-of-Thought Prompting for Large Multimodal Models, CVPR 2024.    
[5] Beyond Embeddings: The Promise of Visual Table in Visual Reasoning, EMNLP 2024.   
[6] Visual Evidence Prompting Mitigates Hallucinations in Multimodal Large Language Models, OpenReview.  

### W3. While each individual analysis is interesting, the overall flow feels somewhat disjointed. The paper presents a categorization of hallucinations and provides extensive explanations for each category, but there are no corresponding experimental results or analysis showing how the proposed method specifically addresses or improves each of these hallucination categories. This lack of connection between the categorization and the method’s effectiveness on each type of hallucination weakens the coherence of the paper. The authors should include a specific analysis or set of experiments demonstrating how VDGD performs on each category of hallucination they've identified. This would help tie together the theoretical framework and the practical application of their method. It is important to show how the method's performance varies across different hallucination types, which would strengthen the paper's claims.

### W4. While the in-depth analysis is appreciated, the paper sometimes feels overloaded with content, which can distract from the core focus. At times, it is difficult to follow, and the connection between earlier sections and the methodology feels weak. The dense content also limits the space for method-related experiments, with only one experiment table included in the main paper. Most experiments have been relegated to the appendix, suggesting the need for better content management. The paper would benefit from a more focused presentation of the core methodology and its experimental validation, with less emphasis on the extensive analysis, which could be streamlined or moved to supplementary material.

### Questions
### Q1. While this does not affect my score, I believe the terms “perception” and “recognition” should be interchanged in the paper. Perception refers to the basic observation of visuals, while recognition is a more complex process based on what has been perceived. However, the paper appears to use these terms in reverse, which could cause some confusion for readers. 

Ref: https://en.wikipedia.org/wiki/Visual_perception

### Soundness
3

### Presentation
3

### Contribution
3
