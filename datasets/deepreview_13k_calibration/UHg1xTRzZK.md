# Boosting LLM Translation Skills without General Ability Loss via Rationale Distillation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 6, 3

## Abstract
Large Language Models (LLMs) have achieved impressive results across numerous NLP tasks but still encounter difficulties in machine translation. Traditional methods to improve translation have typically involved fine-tuning LLMs using parallel corpora. However, vanilla fine-tuning often leads to catastrophic forgetting of the instruction-following capabilities and alignment with human preferences, compromising their broad general abilities and introducing potential security risks. These abilities, which are developed using proprietary and unavailable training data, make existing continual instruction tuning methods ineffective. To overcome this issue, we propose a novel approach called \textbf{RaDis} (\textbf{Ra}tionale \textbf{Dis}tillation). RaDis harnesses the strong generative capabilities of LLMs to create rationales for training data, which are then “replayed” to prevent forgetting. These rationales \emph{encapsulate general knowledge and safety principles}, acting as \emph{self-distillation targets} to regulate the training process. By jointly training on both reference translations and self-generated rationales, the model can learn new translation skills while preserving its overall general abilities. Extensive experiments demonstrate that our method enhances machine translation performance while maintaining the broader capabilities of LLMs across other tasks. This work presents a pathway for creating more versatile LLMs that excel in specialized tasks without compromising generality and safety.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper proposed rationale distillation, with a purpose on improving LLM-based models translation performance while keeping the general instruction-following abilities. The method first generates the explanation of the translation and use the synthetic data for fine-tuning along with the translation pairs.

### Strengths
The paper successfully did what they proposed, improving the translation performance with the proposed method can significantly reduce the damage in general instruction-following tasks.

### Weaknesses
1. The paper's goal is good —it aims to generalize translation models based on LLMs to other domains such as conversational tasks. However, the attempt to balance both translation quality and generalization does not yield a model that is truly useful, placing the paper in an awkward position. For example, RaDis performs substantially worse than its backbone model on conversations and instruction following, and its translation performance is inferior to that of translation-specific models. While I acknowledge that comparing RaDis with ALMA in terms of translation is not entirely fair due to differences in models and training data, this raises another issue: the model's performance is highly dependent on the backbone model. Consequently, RaDis cannot be effectively applied to low-resource languages like Icelandic, which were excluded from the training data. Achieving effective machine translation in LLMs requires substantial effort in multilingual pretraining and alignment; without this, English-centric LLM translation performance is less interesting. Despite the paper's claims of keeping both translation high performance and retaining generality, the translation quality is not top due to the high dependency of the backbone model, and the performance on other tasks is also worse.

2. Inference speed: Regarding inference speed, if the model is trained to output both a reference and an explanation, does this mean the generated output always includes both, requiring the user to extract the translation from the combined output? If so, this could significantly reduce inference speed. It would be beneficial to see a comparison of inference speeds and an analysis of how many additional tokens the model generates compared to translation-specific LLMs.

3. Missing baselines: A fundamental baseline would involve training on a combined dataset of translation parallel data and instruction-following data. Using synthesized data may be unnecessary given the abundance of existing data that can be combined with parallel data. However, I did not find results corresponding to this baseline in the paper. Including such comparisons would strengthen the evaluation and provide a clearer understanding of the model's performance relative to more straightforward approaches.

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
The paper introduces RaDis (Rationale Distillation) -- a self-distillation technique to help instruction-tuned language models learn new tasks without losing their general capabilities or compromising safety alignment. The method first generates rationales - explanations for the instruction-response pairs of the target task using the same language model and these rationales serve as replay data that help retain the original capabilities by fairly capturing the data distribution. The generated rationales and instruction-response pairs are then used for subsequent training of the same language model on the new task. The authors conduct experiments for the task of machine translation and demonstrate that it improves the translation proficiency of models while preserving its overall performance on other tasks.

### Strengths
1. The authors propose a straightforward method for LLMs to learn the translation task (in this study) without losing prior abilities by combining standard fine-tuning on reference translations with self-distillation on generated rationales.

2. The experimental results demonstrate translation improvements across 4 language pairs on 2 different models.

3. The authors study various aspects of the proposed method to understand the influence of these aspects on downstream and overall performance.

### Weaknesses
1. The paper only focuses on improving translation proficiency in LLMs without losing existing capabilities. However, I think the proposed method is more general and can work for other tasks. It should also be experimented on other tasks (e.g. summarization, open-ended QA, MQM annotation, etc) for a more comprehensive study.

2. In section 5.2, the authors compare the Mistral 7B model (student) with rationales generated from different models. However, this comparison may not be fair and it might be more appropriate to compare the rationale generation from a bigger model within the same family. For instance, the Llama 3 7B model (student) with rationales generated from Llama 3 70B. Could you clarify the reasons for not using models from the same families (e.g. Llama 3)?

### Questions
The proposed method generates a rationale for each sample in the training set. Did you experiment with ablating whether you need a rationale for each sample to be included in the training set? How well does the proposed method perform when rationales aren’t available for every sample in the training set? What is the tradeoff between having rationales for all samples versus just a subset of *k* samples (e.g., 10%, 20%, 50% and 100% samples with rationales)?

### Soundness
4

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
This paper proposes a novel method, RaDis, which uses self-generated rationales for sequence-level distillation. It can preserve the model's capabilities in general domains and safety while fine-tuning downstream tasks, addressing the problem of catastrophic forgetting. The paper conducts machine translation experiments on two 7B-sized models to illustrate the effectiveness of the method, and the analysis section provides the detailed observation of the experimental results.

### Strengths
1. This paper proposes a novel method, RaDis, which has a clear and straightforward motivation, and the writing is easy to follow.
2. The experimental results demonstrate that this method is effective and significantly surpasses the related baselines.

### Weaknesses
1. This method effectively maintains the generalization ability and safety of the models during downstream task fine-tuning. However, most translation performance degrades compared to the original fine-tuning baseline, which will limit its applicability in real-world scenarios. Additionally, the comparison of translation performance between the backbone and RaDis in lines 81-83 is unfair and the comparison with the vanilla fine-tuned model is more reasonable and informative.
2. Considering the baseline distillation methods (SeqKD and SDFT) largely relies on the generation quality of the teacher model, it is necessary to conduct the experiments with teachers with better capacity, especially for SeqKD, which is rarely used in self-distillation manner.
3. In the analysis section, the explanations on the performance of RaDis with three different teachers needs a more detailed analysis, similar to that in Table 4. Particularly, it is necessary to clarify why the machine translation performance and the general performance yield contrasting conclusions (e.g., the self-generated setting achieve best general performance and the worse translation performance among the three settings).
4. Typo: line 507, “SDFT greatly enhances” -> “RaDis greatly enhances”

### Questions
1. In the context of machine translation, the emphasis on faithfulness over diversity suggests that paraphrasing references may not efficently enhance translation performance, which aligns with the primary experimental results presented in Tables 1 and 2. Consequently, to facilitate a more equitable comparison between RaDis and SDFT, as well as to explore the potential of RaDis in other tasks, it is essential to evaluate their corresponding performance on logical reasoning tasks, including OpenFunctions, GSM8K, and HumanEval.
2. See the weeknesses.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces Rationale Distillation (RaDis), a new approach for fine-tuning Large Language Models (LLMs) on machine translation (MT) tasks. Unlike traditional fine-tuning methods that rely solely on parallel corpora, RaDis uses LLM-generated rationales to enhance MT performance while maintaining the LLM’s general capabilities, such as instruction-following and reasoning.

### Strengths
RaDis is both straightforward and effective, leveraging the language model itself to generate explanations (rationales) for fine-tuning. Experimental results demonstrate that this method preserves the model’s general abilities while enhancing MT performance, although its MT performance remains slightly below established baselines like ALMA.

### Weaknesses
Firstly, the proposed method lacks novelty from my perspective, as leveraging LLMs to generate data from their own distribution for continual fine-tuning has been extensively explored in prior research (e.g., various PPO/DPO variants along with works on chain-of-thoughts that prompt LLM to generate reasoning trace, etc.,). Moreover, based on my experiences with machine translation (MT) and reinforcement learning with human feedback (RLHF), the generative quality of a 7B model is often unreliable, typically requiring filtering processes (i.e., from a reward model). Incorporating all rationales generated by the LLM without any scoring, filtering, or grounding is likely to reinforce the model's own hallucinations. Even if this approach preserves the model’s instruction-following abilities, the practical utility of such fine-tuning remains questionable.

Secondly, the rationales derived from a translation dataset may lack diversity. A comparison or discussion with existing work, such as TOWER [1], is necessary. TOWER achieves high MT performance by utilizing parallel corpus and diverse instruction-following datasets during fine-tuning, which appears more effective on benchmarks (and the idea is more straightforward than rationales generation). Therefore, I believe another baseline that simply uses parallel data for fine-tuning + diverse instruction-following dataset for preserving the model's pretrained ability is needed.

### Questions
1. some comparison and discussion on previous work like TOWER will be useful.
2. I am curious if there is any analysis of the generated rationales’ quality. I see in Table 4 there are some categorization but are all the generated responses relevant? I doubt that a 7B model can give very high-quality rationales for all translation pairs in the training data.
3. I like the analysis in section 5.2 and it actually resonates with my points in weakness. Fine-tuning model on its self-generated response is most helpful to preserve its instruction-following ability. However, I believe simply using all self-generated rationales is also limited. I am wondering if any on-policy-based mechanism for rationales generation is tried.
4. Overall, I find the experiments comprehensive but the improvement is not very surprising. The experiment also lacks an obvious baseline: using a combination of parallel corpus for MT and instruction-following dataset for preserving general ability (like the approach used in TOWER)

### Soundness
2

### Presentation
3

### Contribution
2
