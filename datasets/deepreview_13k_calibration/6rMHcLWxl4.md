# Towards World Simulator: Crafting Physical Commonsense-Based Benchmark for Video Generation

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 6, 5, 5

## Abstract
Text-to-video (T2V) models like Sora have made significant strides in visualizing complex prompts, which is increasingly viewed as a promising path towards constructing the universal world simulator. Cognitive psychologists believe that the foundation for achieving this goal is the ability to understand intuitive physics. However, the capacity of these models to accurately represent intuitive physics remains largely unexplored. To bridge this gap, we introduce \bench, a comprehensive \textbf{Phy}sics \textbf{Gen}eration \textbf{Bench}mark designed to evaluate physical commonsense correctness in T2V generation. \bench comprises 160 carefully crafted prompts across 27 distinct physical laws, spanning four fundamental domains, which could comprehensively assesses models' understanding of physical commonsense. Alongside \bench, we propose a novel evaluation framework called \eval. This framework employs a hierarchical evaluation structure utilizing appropriate advanced vision-language models and large language models to assess physical commonsense. Through \bench and \eval, we can conduct large-scale automated assessments of T2V models' understanding of physical commonsense, which align closely with human feedback. Our evaluation results and in-depth analysis demonstrate that current models struggle to generate videos that comply with physical commonsense. Moreover, simply scaling up models or employing prompt engineering techniques is insufficient to fully address the challenges presented by \bench (e.g., dynamic physical phenomenons). We hope this study will inspire the community to prioritize the learning of physical commonsense in these models beyond entertainment applications

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Although T2V models have shown great progress in generating good media-level content, this paper challenges their capability to become the real world simulator. This paper first proposes a PhyGenBench, 160 T2V prompts composed of several physics categories, then proposes a hierarchical framework to evaluate semantic alignment and physics commonsense alignment. It shows that current models, even ones with large scales, struggle with physical commonsense.

### Strengths
(1) This paper handcrafts T2V prompts in a fine-grained way.
(2) This paper provides a carefully designed pipeline to conduct the evaluation of physics commonsense.

### Weaknesses
(1) The paper lacks decent novelty in terms of benchmark and evaluator itself. The way it constructs the evaluator heavily relies on several generative models. For example, using GPT4o to do information extraction and create questions sometimes brings about hallucination. Also, using VLMs in different stages can also lead to hallucination. Since it is a complex pipeline composed of different stages, error propagation might happen.

(2) The comparison with other baselines is unfair. The comparisons with other baselines are biased. Although they acknowledge that alternative auto-evaluators lack robustness, they do not demonstrate whether their own auto-evaluator performs effectively on prompts from different benchmarks as part of a generalization analysis. Typically, like concurrent work, these kinds of auto-evaluators are tailored to specific prompt distributions. Basically, the generalization of the reward modeling for world simulators should be enough for another paper.

(3) The number of prompts engaged in this paper are limited, which might be a weak signal for evaluating the video generation models as a world simulator.

### Questions
(1) What is the efficiency of using your auto-evaluator? Could you provide an estimation?

(2) Could you provide some error analysis on the bad cases where PhyGenEval is opposite to the human eval? Maybe this can provide some insight on how to further improve the reward modeling of world simulators.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors focus on the evaluation of text-to-video models. To this end, they propose a new benchmark as well as a new evaluation method. Named PhyGenBench, the dataset of prompts evaluate intuitive physics in subcontexts such as mechanics, optics, thermal dynamics, and material properties. Alongside this benchmark is PhyGenEval, an automated eval pipeline where a VLM is combined with GPT-4o to generate evaluative questions and answers. The authors compare PhyGenEval against human evaluations. They also perform some initial experiments with contemporary video models on their proposed benchmark.

### Strengths
1. Current generative models of video have serious issues with intuitive physics, and the research community needs a good benchmark to evaluate this capability. The proposed benchmark dataset can serve as a very important dataset for the community.

2. Evaluating intuitive physics can be difficult, and PhyGenEval might be a promising method to automate evaluation without the need for human raters. 

3. The quantitative evaluation of current video models on the benchmark is a strong contribution and shows the need to improve these models in the realm of intuitive physics.

### Weaknesses
While PhyGenEval is an interesting approach to automating evaluation on the benchmark, I assert that the approach has some issues and should not be adopted by the community at this moment as a standard evaluation; human raters should be used:

1. The pipeline is not reliable enough, the PCA correlation results are only around .7 - .8

2. The pipeline relies on proprietary models such as GPT-4o and may be difficult to reproduce with open models.

### Questions
I believe PhyGenBench is an excellent contribution for the research community, but the PhyGenEval as described is problematic for the reasons listed above. Is it possible that PhyGenEval be described as a potential approach for automated evaluation to be iterated on in subsequent research, with PhyGenBench + human evaluation as the main contribution?

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper discusses the limitations of current text-to-video (T2V) models like Sora in accurately representing intuitive physics, which is essential for creating a universal world simulator. Understanding intuitive physics is foundational for such a simulator, yet T2V models' performance in this area remains under-explored. To address this gap, the authors introduce PhyGenBench, a Physics Generation Benchmark designed to test T2V models' grasp of physical commonsense and provide a comprehensive assessment of models' understanding of physics.

Also, the paper presents PhyGenEval, a new evaluation framework that uses advanced vision-language and large language models in a hierarchical structure to assess physical commonsense accurately. This dual framework allows for large-scale, automated evaluations aligned with human feedback.

Overall, the paper is well-written and propose a great benchmark for video generation evaluation.

### Strengths
The paper is well-written and the contributions are very clear. The proposed benchmark for video generation models focuses on evaluate the physical understanding of video generation models, which is crucial and not well-studied. The evaluation strategy is clear and comprehensive.

### Weaknesses
I mainly have two questions about the paper.

1) As PhyGenEval uses VLMs for scoring, I would like to know the effect of different VLMs. For example, GPT-4o for closed-source models and InternVL-2, LLaVA-Video, Oryx, these open-source models that can understand videos. I'm wondering if these models can consistently evaluate the generated videos, which may be an interesting question and I think it should be discussed in the paper to show a more comprehensive understanding of the proposed evaluation pipeline.

2) As the evaluation pipeline needs a lot of retrieval, I'd like to know the success rate of retrieval with GPT-4o. It is crucial for the overall evaluation and I hope the author can provide more details about how to ensure the retrieval is correct.

### Questions
As stated in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces PhyGenBench, a new benchmark for evaluating the physical commonsense capabilities of Text-to-Video (T2V) models, particularly their understanding of intuitive physics. It includes prompts across 27 physical laws within four domains: mechanics, optics, thermal, and material properties. To evaluate performs on this benchmark, the authors propose PhyGenEval, a hierarchical evaluation framework using advanced vision-language models (VLMs) and large language models. Experimental results reveal that current T2V models lack robust physical commonsense, underscoring the gap between these models and true world simulators.

### Strengths
- This paper clearly have great novelty. It focus on intuitive physics is unique and addresses an important gap in T2V evaluation.
- PhyGenEval's three tiered framework (key phenomena detection, order verification, and overall naturalness) thoroughly assesses physical realism.
- By getting more attention on the gap in physical commonsense, the benchmark provides great insights on how to improve video generation models to become a real world simulator.

### Weaknesses
 - The paper includes extensive comparisons to demonstrate PhyGenEval’s effectiveness, suggesting that a two-stage evaluation strategy may align more closely with human judgments for both InternVideo2 and GPT-4-o. Line 965 also notes that alternative open-source models achieve a high correlation coefficient with human evaluations. However, it appears that the main results rely on a specific version of GPT-4-o, which is not explicitly mentioned. As a benchmark, would future users need to evaluate all baselines and methods on updated versions of GPT-4-o to ensure fair comparisons? While the paper suggests that evaluation costs are minimal, I am concerned that this reliance on a specific model version may affect consistency. Have the authors considered using other LVLMs in place of GPT-4-o?
- Certain T2I models may perform poorly on specific prompts. I am not fully convinced that the proposed evaluation method can robustly handle these lower-quality videos.
- The issue of hallucination in large language models (LLMs) does not appear to be addressed in the evaluation protocol, potentially impacting the reliability of the benchmark. It would be beneficial if the authors considered this factor in their assessment framework.

- The author promised more human evaluation results in Appendix C.2 but this result seems under Appendix C.1. The writing seems to be confusing. Also between line 899 and 905, I believe the annotation should be done more rigorously. I am expecting carefully validate results from human annotators or I think the results can be noisy. I think showing the instructions to the human annotators can be particularly helpful.

### Questions
- What is "the final score is calculated as 0 according to 4.2" (line 292)? Is the example in Figure receive 0 after this physical commonsense evaluation?

- It seems like the entire evaluation rely on closed sourced LLM: GPT-4o. If in the future, GPT-4o becomes unavailable, how should people compare results?

- some typos such as we pue more detailed (line 410), Appendix C.2 (line 418)

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes PhyGenBench and PhyGenEval. PhyGenBench is a benchmark with about 160 text prompts used to evaluate models' video generation ability on physics-related text prompts. PhyGenEval is an evaluation framework of PhyGenBench, used to automatically assess the video quality of physics laws, via GPT-prompted questions and VLM perception.

### Strengths
- The topic is novel and interesting. Evaluating physics in AI-generated videos is really important. This paper is the first one on this topic as far as I know.

- Experiments show that PhyGenEval is closer to human value.

### Weaknesses
 - The PhyGenBench is a dataset with 160 text prompts. As a comparison, for the works mentioned in this paper, VideoPhy has 688 prompts with 36.5k human annotations, and DEVIL has more than 800 prompts. Only 160 text prompts may not represent the full complexity of physics law.

- In PhyGenEval, the overall score is set on a four-point scale, but even the top-performing video generation model scores only 0.5 on average. That means the model gets a 0 score in more than half of the test cases. This suggests that the evaluation metric might be overly strict, potentially limiting its effectiveness in distinguishing between models. Such stringent scoring could reduce the benchmark’s ability to accurately reflect model performance differences.

- Since the topic is related to evaluating the physics in generative models, I think it is better to add some discussion on physical reasoning benchmarks in related works, which has been a heated debate topic, such as SuperCLEVR-Physics[1], ContPhy[2], Physion[3] and so on.

### Questions
See Weakness above.

### Soundness
2

### Presentation
3

### Contribution
2
