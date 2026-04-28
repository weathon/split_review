# JudgeLM: Fine-tuned Large Language Models are Scalable Judges

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Evaluating Large Language Models (LLMs) in open-ended scenarios is challenging because existing benchmarks and metrics can not measure them comprehensively.
To address this problem, we propose to fine-tune LLMs as scalable judges (\name) to evaluate LLMs efficiently and effectively in open-ended benchmarks. 
We first propose a comprehensive, large-scale, high-quality dataset containing task seeds, LLMs-generated answers, and GPT-4-generated judgments for fine-tuning high-performance judges, as well as a new benchmark for evaluating the judges. 
We train \name{} at different scales from 7B, 13B, to 33B parameters, and conduct a systematic analysis of its capabilities and behaviors. 
We then analyze the key biases in fine-tuning LLM as a judge and consider them as position bias, knowledge bias, and format bias.
To address these issues, \name{} introduces a bag of techniques including swap augmentation, reference support, and reference drop, which clearly enhance the judge's performance. 
\name{} obtains the state-of-the-art judge performance on both the existing PandaLM benchmark and our proposed new benchmark.
Our \name{} is efficient and the \name-7B only needs 3 minutes to judge 5K samples with 8 A100 GPUs.
\name{} obtains high agreement with the teacher judge, achieving an agreement exceeding 90\% that even surpasses human-to-human agreement\footnote{As a reference, the max agreement among humans in MT-bench~\citep{zheng2023chatbot-arena} is 82\%.}. 
\name{} also demonstrates extended capabilities in being judges of the single answer, multimodal models, multiple answers, and multi-turn chat.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper targets evaluating and building LLM's specifically for judging answer correctness on open-ended tasks. To do this, they construct a dataset which consists of llm answers across a variety of tasks along with GPT-4 generated judgements used as a ground truth (ground truth references responses are sometimes supplied). This dataset is used to train smaller LLMs to provide judgements with comparable accuracy to SOTA LLMs. They also discuss the biases that result from the LLM judge finetuning (position bias, knowledge bias, format bias) and propose methods to address them.

### Strengths
- The problem setting of building cheaper, scalable LLM judges is an important problem now that LLM-driven evaluation is becoming standard, and the provided benchmark will be incredibly valuable to the community
- This paper is easy to follow and provides a comprehensive analysis comparing JudgeLM to existing LLM judges on both accuracy and efficiency
- Improvements over previous LLM judges is impressive and provides a promising alternative to expensive closed source model judges

### Weaknesses
 - Knowledge bias is not a bias but rather a limitation of the LLM, and the proposed solution to this seems to be providing that knowledge via a reference (AKA making the out of distribution task in distribution). While I am not opposed to this solution, I would argue this is not a bias addressed but rather a universally known failure case of the model that the authors try to mitigate by training on more knowledge via reference examples - a universally known solution to address model knowledge gaps.
- While the validation set was manually checked and corrected by the authors, it does still rely on GPT generated outputs. This provides somewhat of an unfair evaluation as JudgeLM is trained on GPT generated judgements as well. Even with the human validation, there is a reasonable chance that if this dataset where annotated by a different LLM and produced different judgements, humans checking responses would also consider them reasonable. An unbiased way of annotating is for humans to provide judgements *without* knowing what the GPT judgement is. If the agreement between humans and the GPT judgements are similar, than I would consider this evaluation relatively fair across all judge models. 
- The authors did not provide clear evidence that this model is able to maintain good performance across tasks not in the training set. I suspect that the comparison to the PandaLM test set is showing this to some extent, but I did not see any prose on *how* these two datasets differ. What tasks are seen in PandaLM that arent seen in the JudgeLM dataset? If the authors can show that the task distribution is significantly different from the training set I would be satisfied

### Questions
- did you notice any favoring of GPT-4 answers by the JudgeLM? 
- What tasks are seen in PandaLM that arent seen in the JudgeLM dataset?

### Soundness
4

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
The paper proposes a scalable method for evaluating LLMs in open-ended tasks. It leverages a large, diverse dataset with tasks, LLM-generated answers, and GPT-4 judgments to fine-tune models that assess other models effectively. To mitigate biases such as position, knowledge, and format biases, the authors introduce techniques like swap augmentation, reference support, and reference drop. JudgeLM achieves high agreement rates with GPT-4, surpassing human-level consistency, and can judge multiple formats efficiently.

### Strengths
The paper demonstrates a novel approach to scaling LLM evaluation by fine-tuning models as judges, creating a comprehensive system that addresses biases inherent in model evaluations. This creative combination of fine-tuning techniques with practical augmentation methods (swap, reference support, reference drop) removes limitations from prior works that struggled with consistent, scalable evaluation in open-ended tasks. 

The quality of the work is solid, backed by a large-scale, carefully curated dataset, including GPT-4 judgments and human validation, which strengthens the empirical basis of the results. In terms of clarity, the paper effectively communicates its methodology and contributions. 

Given the increasing role of LLMs across various fields, there is pressing need for scalable, unbiased evaluation frameworks. JudgeLM’s seems a valuable tool in AI evaluation, with potential impact on future benchmarks and research in LLM development.

### Weaknesses
The improvements seem The dataset, although extensive, primarily relies on GPT-4 for initial judgments, which may inadvertently transfer GPT-4’s specific limitations to JudgeLM. A more diverse range of teacher models such as Claude could minimize over-reliance on any single model’s limitations, making JudgeLM’s judgments more adaptable. This reliance on a single model for generating the training data introduces a potential bias, where JudgeLM may learn to mimic GPT-4's specific evaluation style rather than developing a more generalized understanding of quality. Furthermore, the paper does not explore the impact of different prompt styles on the GPT-4 judgments, which could also introduce variability and bias into the training data. This could lead to JudgeLM performing well on tasks similar to those used to train GPT-4 but potentially underperforming on tasks that require different evaluation criteria or perspectives.

### Questions
Given that JudgeLM reportedly surpasses human-to-human agreement, how does it handle cases where human judgments may rely on subjective or context-dependent insights? Could the authors discuss potential scenarios where JudgeLM might still fall short of human evaluators in nuanced judgments, and possibly include or consider adding complex tasks to explore this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces JudgeLM, a scalable framework for evaluating LLMs by fine-tuning models as judges, using a dataset of LLM-generated answers and GPT-4 judgments. This framework addresses evaluation biases such as position and format biases through techniques like swap augmentation and reference drop. The authors show that JudgeLM achieves high alignment with the GPT-4 judge and is more efficient than comparable methods.

### Strengths
- JudgeLM’s ability to process up to 5K samples in 3 minutes on an 8-GPU system is impressive, and it supports multiple use cases including single-answer and multimodal evaluations.
- The swap augmentation and reference-based adjustments offer a nice way to mitigate biases that impact LLM judgments, contributing to more reliable scoring across scenarios.
- The JudgeLM dataset, with its human-verified judgments and optional reference answers, is a notable contribution.

### Weaknesses
 - The model's robustness under varied task complexities or unseen domains is not extensively tested (e.g. math/coding/reasoning task). Additional benchmarks or diverse human annotations would reinforce its generalizability.
- The study acknowledges that scaling up the judge dataset is costly and currently relies on GPT-4 outputs. Exploring alternative sources or synthetic judgment data could be beneficial.

### Questions
- Can JudgeLM’s performance be reliably extended to evaluate answers in different languages or domain-specific contexts (e.g., math, coding, legal or medical)?
- How does the model handle cases where the reference answer may introduce bias rather than mitigate it?

### Soundness
3

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
A high-quality judge LLM should ideally demonstrate the following features: strong agreement with ground truth (often human annotations, though GPT-4 judgments are acceptable in some cases), consistency to diverse input formats (resilience to various biases), inference efficiency, scalability with data and parameter size, and generalization across scenarios.   
JudgeLM, as presented by the authors, offers an effective approach to optimizing these aspects:

1. **Achieving High Agreement**: The authors collect a diverse, high-quality dataset at scale through a structured pipeline (though the pipeline itself is not entirely novel).
2. **Achieving High Consistency**: To mitigate three critical biases—position, knowledge, and format biases—the authors employ three straightforward yet effective data augmentation methods: swap augmentations, reference support, and reference drop. This augmentation not only enhances consistency but also boosts agreement.
3. **Enhancing Efficiency**: The authors adopt a “grading, judging, and reasoning” pattern, as opposed to an explanation-first (CoT) approach. This method achieves a balance, trading slight reductions in agreement and consistency for increased efficiency and flexibility.
4. **Scalability**: Experimental results demonstrate JudgeLM’s scalability, as tested across varying model and data sizes. The 33B JudgeLM model even exceeds its generalist teacher, GPT-4’s agreement on a human-labeled validation set.
5. **Generalization**: JudgeLM exhibits promising generalization across various judging tasks (e.g., math problems, code generation) and diverse benchmarks (e.g., human-annotated, multimodal, and retrieval-based benchmarks).

### Strengths
1. **Strong Motivation**: Training a judge LLM for efficient, effective evaluation of LLMs in open-ended benchmarks is highly valuable, as it enhances privacy, consistency, and cost-effectiveness.
2. **Thorough Exploration of Key Research Questions**: The paper addresses significant questions around agreement, consistency, efficiency, scalability, and generalization for LLM-as-judge models.
3. **Solid Experiments**: A convincing ablation study supports the effectiveness of data augmentation strategies, and the “grading, judging, and reasoning” pattern retains significant agreement and consistency benefits while improving efficiency.
4. **Open-Sourced Code and Dataset**: The code and dataset are readily accessible and user-friendly, enabling further research and reproducibility.

### Weaknesses
1. **Assumption of GPT-4 Judgments as Ground Truth**: Although GPT-4 is a common choice for cost-effective labeling, it would be beneficial if the authors could further substantiate its reliability before using it as a standard. Specifically, while GPT-4 is known for strong performance, its biases and potential inconsistencies, especially in complex reasoning tasks, are not fully understood. A more rigorous analysis, perhaps comparing GPT-4's judgments against a smaller set of expert human annotations across diverse tasks, would strengthen the validity of the training data.
2. **Suboptimal Training Query Distribution**: While the authors highlight the diversity and quality of the training data by statistics, further optimization of the ideal data distribution for training judge LLMs would add depth. What constitutes a more ideal queries distribution? For example, the distribution of user queries collected in Chatbot Arena reflects a large volume of real user queries, which is one of the reasons Chatbot Arena has become such a well-recognized benchmark. If we align the queries distribution in the training data more closely with the distribution of actual user queries, the resulting Judge LLM would evaluate samples more fairly,  drawing on the philosophy behind MixEval/MixEval-X paper.
3. **Potential Overclaiming**:
    - Bias Analysis: In Section 4, while the paper discusses “position bias” and “knowledge bias,” these concepts are well-established in prior literature. The novel contribution here lies in addressing “format bias,” so the phrase “shed light on three key biases” could overstate the novelty. It might be more precise to note that this work builds on previous discussions of position and knowledge biases while introducing and addressing format bias as a new focus.
    - Scalability Comparison: In Appendix 4, the authors mention JudgeLM’s scalability as a differentiator from PandaLM. While PandaLM also explores different model sizes (up to 70B), JudgeLM offers a more granular analysis of scalability. It would clarify the novelty here to acknowledge PandaLM’s scalability exploration but emphasize JudgeLM’s finer scalability insights.
4. **Paper Structure**: Despite the solid research content, the paper’s organization could benefit from a clearer structure, such as arranging sections by key research questions.

### Questions
1. In Table 3, why is JudgeLM able to judge answers in parallel, while PandaLM cannot? The authors mention certain “engineering optimizations for parallel judging”; Please provide specific details about these engineering optimizations, such as the parallel processing techniques used or any architectural changes that enable parallel judging. This would help readers better understand the efficiency advantages of JudgeLM over PandaLM.
2. In both the Abstract and the Introduction, the authors emphasize that JudgeLM achieves an agreement exceeding 90%, surpassing *human-to-human agreement*. Could you clarify this comparison? My understanding is that this primarily reflects strong internal consistency within JudgeLM’s evaluations, yet the emphasis seems to be on JudgeLM’s superior performance beyond consistency alone. If so, I suggest to provide a direct comparison between JudgeLM-to-human agreement and GPT-4-to-human agreement. This would help clarify whether JudgeLM's performance truly surpasses human-level agreement or if it's primarily a measure of internal consistency. Or if not so, feel free to correct me :)
3. In the Limitations section, the authors only mention the need to further scale up the judge dataset, which I find somewhat trivial. I recommend considering discuss more improvements to the dataset, such as refining the data distribution to real user quires. This could enhance JudgeLM’s performance in areas where the current data may lack diversity or balance. Please refer to my comments in the weaknesses section for further insights.

I will increase the score if all these concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
3
