# Self-rationalization improves LLM as a fine-grained judge

- Decision: Reject
- Scores: 5, 5, 6, 6, 3, 5

## Abstract
LLM-as-a-judge models have been used for evaluating both human and AI generated content, specifically by providing scores and rationales. Rationales, in addition to increasing transparency, help models learn to calibrate its judgments. Enhancing a model's rationale can therefore improve its calibration abilities and ultimately the ability to score content. We introduce Self-Rationalization, an iterative process of improving the rationales for the judge models, which consequently improves the score for fine-grained customizable scoring criteria (i.e., likert-scale scoring with arbitrary evaluation criteria). Self-rationalization works by having the model generate multiple judgments with rationales for the same input, curating a preference pair dataset from its own judgements, and iteratively fine-tuning the judge via DPO. Intuitively, this approach allows the judge model to self-improve by learning from its own rationales, leading to better alignment and evaluation accuracy. After just two iterations -- while only relying on examples in the training set -- human evaluation shows that our judge model learns to produce higher quality rationales, with a win rate of $62\%$ on average compared to models just trained via SFT on rationale . This judge model also achieves high scoring accuracy on BigGen Bench and Reward Bench, outperforming even bigger sized models trained using SFT with rationale, self-consistency or best-of-$N$ sampling by $3\%$ to $9\%$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents Self-Rationalization, a method that enhances the rationale generation capabilities of LLM judges, thus improving the RLAIF process. Aligned with the standard RLAIF framework, this approach samples multiple potential scores with associated rationales, curates data from these samples, and applies DPO for LLM refinement. By iteratively refining (e.g., through two iterations), this framework shows marked improvements over baseline LLMs and prior RLAIF methods.

### Strengths
- Self-refinement of LLMs through RLAIF is a significant research topic.
- Generating rationales for LLM judges enhances both performance and interpretability.
- The proposed approach refines and improves baseline LLMs.

### Weaknesses
 
**Limited technical novelty**

The concept of generating rationales for LLM judges (or reward models) has been explored in recent works [1,2]. Both papers were uploaded to arXiv in August 2024, making them concurrent studies; therefore, it is okay not to include experimental comparisons with them. However, given these existing works, it is essential to identify the unique contributions of this paper. Including a discussion on the pros and cons of different approaches would be valuable.

[1] Ankner et al. Critique-out-Loud Reward Models. arXiv 2024.
[2] Zhang et al. Generative Verifiers: Reward Modeling as Next-Token Prediction. arXiv 2024.

---
**Limited improvement in performance**

The performance gains are not significant, despite the additional computation involved in two iterative refinements, which include complex procedures for sampling scores and rationales. For example, in Fig. 2, the win rate of the proposed SRE over SFT is only 55%, a modest 5% improvement over a random guess. Similarly, the results in the tables appear limited. In Table 2, the improvement over single-stage DPO is minimal, raising questions about the effectiveness of the generated rationales. Additionally, in line 322, where it states, “We observe that $J_{SRE}$ performs significantly worse than $J_{SFT}$,” it should instead read significantly better, not worse?

---
**Writing could be further polished**

For instance, the first paragraph of the introduction introduces the concept of RLAIF, but the second paragraph revisits the limitations of RLHF, which feels redundant. These two paragraphs could be reorganized to convey distinct points. Other sections could also be reorganized. For example, in the Background section, it’s unclear why pointwise or pairwise assessments are emphasized as being so important.

### Questions
N/A

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
The paper introduces Self-Rationalization, a method to improve the performance of Large Language Models (LLMs) used as judges by enabling them to iteratively train on their own rationales. Through a process involving Direct Preference Optimization (DPO), the model generates multiple judgments for the same input, selects preferred rationales, and fine-tunes itself without additional human-labeled data. Experimental results show that Self-Rationalization outperforms existing baselines on several benchmarks, indicating that this targeted training enhances the model's judgment capabilities.

### Strengths
- This paper introduces a practical framework for enhancing the judgment capabilities of large language models (LLMs) through Self-Rationalization, an iterative self-training process. 
- The approach is both practical and resource-efficient, requiring no additional human-labeled data, making it broadly applicable to LLM-based evaluation tasks.

### Weaknesses
 - The baseline comparisons are insufficient, as the authors should evaluate the proposed method against more iterative self-improvement approaches (e.g., Self-Taught Evaluators) to provide a broader perspective on its effectiveness.
- The paper does not convincingly demonstrate the impact of rationales on enhancing judgment capabilities. As shown in Table 3, the performance gain from including rationales is modest (an increase from 72.0 to 74.0 on RewardBench). Additionally, when compared to the pairwise-trained Skywork-Critic-Llama-3.1-8B (which achieves 89.0 on RewardBench), the use of rationales does not offer a clear advantage.

### Questions
1. As described in line 258, the temperature is set to 1.0 when sampling predictions. Does this setting ensure a strong correlation between the generated rationales and scores? For instance, what is the distribution of scores when multiple scores are generated based on the same rationale? Could this affect the quality of preference pairs, where a high-quality rationale might receive an inaccurate score due to the high temperature, leading it to be incorrectly optimized as a negative example?
2. In line 252, why was weight-merging chosen over training on a mixed dataset?
3. In line 259, what is the reason for using different data quantities across the two iterations?
4. What impact would additional iterations have on the model's performance?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of this paper is to enhance the performance of LLM-as-a-judge, ensuring that high-quality responses receive higher scores and low-quality responses receive lower scores. 

The method is the first to improve the performance of the judge model by RLAIF: an iterative training process comprising SFT and DPO on self-curated preference data.
Specifically, the model is prompted to output rationales when evaluating each content, and multiple samples are taken for the same question. The preferences among different rationales are determined based on the whether the model’s judgments and the ground truth are aligned. This preference data is then used for two rounds of training, with the updated model regenerating the preference dataset after each round.

Experiments demonstrate a slight improvement in correlation with human or GPT4 scoring after applying this SFT+DPO training.

### Strengths
Originality: The paper introduces a new pipeline consisting of data curation and alignment training to enhance LLM's ability as a judge. It builds on existing judge models like Promethus and goes further by implementing RLAIF fine-tuning.

Quality: The paper considers multiple benchmarks including Reward Bench, BiGGen Bench, and Feedback Bench, and shows good performance against both comparable and larger models. 

Significance: overall, the paper has a potential impact for practitioners on the field of LLM-based evaluation as it implements the pipeline of RLAIF and shows its performance. This is particularly important for applications where understanding and alignment with human reasoning are critical. Furthermore, it reduces the reliance on extensive human-labeled data, making it a scalable alternative to traditional reinforcement learning from human feedback.

### Weaknesses
Clarity: the paper's presentation can be further improved by including more details. Please see the questions below.

Originality: The training dataset and the SFT training method is proposed by Promethus paper, and the pairwise/pointwise scoring functions and fine-grained criteria are also considered in this paper. The contribution of this paper related to method novelty lies on the heuristic used for preference selection.


Writing:

Q1: The paragraph starting at line 52 provides a vague explanation for the motivation, and the logical flow between sentences feels disconnected. Why does producing and reflecting on rationales enhance the LLM’s scoring ability? How do iterative generations and improvements of rationales lead to better alignment and calibrated evaluations? I suggest adding references or breaking down the logical chain in more detail to improve clarity.

Q2: The related works section is unclear in places. For example, in the caption for Table 1, what does “whether synthetic seed prompts need to be generated” mean? Does it refer to not needing an extra training dataset?

Q3: Which specific preference selection method is used in Tables 2 and 3? Is it the Correct-Answer Preference Pairing method? Additionally, starting from line 371, how is the margin defined? Is it determined by taking the highest scoring sample and selecting those with scores within a certain margin? If all samples’ score difference is below this margin, how are they handled? Are they discarded?

Q4: There are several incorrect uses of citations; for instance, in line 483, parentheses should not be used.

Q5: In the related works section, why does the subsection on LLM-as-a-judge and reward models emphasize DPO? Are there no methods that utilize RLHF?

Experiments:

Q6: How is the score distribution for the majority vote calculated in line 213?

Q7: What does the statement “use ground truth score to guide the selection” in line 293 mean?

Q8: In line 311, the statement “require fewer training samples and compute resources”—what models is this being compared to? Could more explanation be provided to support this claim?

Q9: What experimental evidence supports the claim in line 317 that long rationales can lead to external noise and complexity in token predictions?

Q10: Is the statement in line 322 reversed?

Q11: How much data was used for evaluation in Figure 2?

Q12: What specifically does “ground truth rationale” refer to in line 345?

Minor:

Q13: The citation for Kim 2023 and Kim 2024a in line 247 seems to reference the same work.

### Questions
Writing:

Q1: The paragraph starting at line 52 provides a vague explanation for the motivation, and the logical flow between sentences feels disconnected. Why does producing and reflecting on rationales enhance the LLM’s scoring ability? How do iterative generations and improvements of rationales lead to better alignment and calibrated evaluations? I suggest adding references or breaking down the logical chain in more detail to improve clarity.

Q2: The related works section is unclear in places. For example, in the caption for Table 1, what does “whether synthetic seed prompts need to be generated” mean? Does it refer to not needing an extra training dataset?

Q3: Which specific preference selection method is used in Tables 2 and 3? Is it the Correct-Answer Preference Pairing method? Additionally, starting from line 371, how is the margin defined? Is it determined by taking the highest scoring sample and selecting those with scores within a certain margin? If all samples’ score difference is below this margin, how are they handled? Are they discarded?

Q4: There are several incorrect uses of citations; for instance, in line 483, parentheses should not be used.

Q5: In the related works section, why does the subsection on LLM-as-a-judge and reward models emphasize DPO? Are there no methods that utilize RLHF?

Experiments:

Q6: How is the score distribution for the majority vote calculated in line 213?

Q7: What does the statement “use ground truth score to guide the selection” in line 293 mean?

Q8: In line 311, the statement “require fewer training samples and compute resources”—what models is this being compared to? Could more explanation be provided to support this claim?

Q9: What experimental evidence supports the claim in line 317 that long rationales can lead to external noise and complexity in token predictions?

Q10: Is the statement in line 322 reversed?

Q11: How much data was used for evaluation in Figure 2?

Q12: What specifically does “ground truth rationale” refer to in line 345?

Minor:

Q13: The citation for Kim 2023 and Kim 2024a in line 247 seems to reference the same work.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Self-Rationalization as an iterative training process aimed at improving the evaluation capabilities of large language models (LLMs) when used as judges. Self-Rationalization trains the LLM by generating multiple rationales for the same input and creating preference pairs, with one judgment selected as superior. These pairs are then used for DPO fine-tuning, helping the model learn from its own rationale and score generation. They show that this method leads to improvement in rationale quality and scoring accuracy without additional human feedback, as demonstrated across multiple benchmarks.

### Strengths
1. The paper is written well and the experiments are comprehensive for the scope of this submission. 
2. It introduces a practical approach for model alignment using self-generated rationales and DPO, minimizing reliance on human-labeled data. Unlike similar methods like Self-Taught Evaluators, it applies DPO to paired rationales, which is a sensible choice for optimizing preference alignment.

### Weaknesses
1. Although the model generates multiple rationales per input, there is no exploration of how the diversity of these rationales affects model performance. Ablation studies showing the impact of rationale diversity (e.g., varying the number or quality of rationales) on alignment and scoring accuracy would offer valuable insights into the robustness of the approach. Specifically, it's unclear whether simply generating more rationales, even if they are similar, is beneficial, or if a specific level of diversity is required for optimal performance. The paper should investigate the impact of different sampling strategies on the diversity of generated rationales and how this affects the final model's evaluation capabilities. For example, the authors could explore using different temperature settings or nucleus sampling parameters to control the diversity of the generated rationales and analyze the correlation between rationale diversity and evaluation performance.
2. Rather than relying solely on high-temperature sampling to produce rejected rationales, using prompts to vary rationale quality and accuracy could generate a broader range of challenging responses, enhancing the training data. The current approach may not be generating sufficiently diverse or challenging negative examples, which could limit the model's ability to learn robust evaluation criteria. The authors should explore the use of specific prompts designed to elicit incorrect or low-quality rationales, such as prompts that encourage the model to make common reasoning errors or to generate rationales that are inconsistent with the input. This would allow for a more controlled and targeted generation of negative examples, potentially leading to better model performance.
3. Exploring different model families and parameter sizes could improve the generalization and robustness of the results, showing how well the approach scales across varying model architectures and capacities. The experiments are limited to a single model family and size, making it difficult to assess the general applicability of the proposed method. It is important to investigate whether the method is equally effective across different model architectures and scales, or if it is sensitive to specific model characteristics. For example, the authors could evaluate the method on smaller models to see if the benefits of self-rationalization are maintained with less capacity, or on larger models to see if the performance gains continue to scale.

### Questions
Please refer to weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work proposes Self-Rationalization for an iterative training scheme to achieve self-improving language models. Specifically, the authors show that training instances for the LLM-as-a-Judge task for self-evaluation can be obtained by oversampling and post-filtering of rationale trajectories after SFT even when no external preference dataset exists. In particular, they show that approaches such as majority voting, which is widely utilized in existing Chain-of-Thought research, can be used as a post-filtering approach to construct the LLM-as-a-Judge dataset, and also score margin-based filtering is effective. This work further demonstrated that preference dataset construction with rationale is possible without an external dataset even in a relatively limited model size environment (<10B).

### Strengths
This work shows that even if an external preference dataset does not exist, it is possible to build a preference dataset for iterative update through a relatively small-sized model with rationale and appropriate post-filtering. In particular, major voting on scores is possible even for instructions where it is difficult to determine an exact match for an answer, so it is possible to learn LLM-as-a-Judge for instructions in various domains.

### Weaknesses
As a preliminary study, [1] already reported that LLM-as-a-Judge can be trained iteratively without the seeds, but it is better to pre-filter the model-generated judgments that do not match human decisions for training efficiency. This suggests that complete AI-built preference datasets may not initially contain meaningful preference signals compared to filtered datasets using a small number of human preference decisions. However, this work does not include an analysis of whether oversampling of the rationale trajectory is efficient enough to bypass filtering with this external human preference. Without such justification, this work can be evaluated as lacking analysis for further research from [1].

### Questions
The experimental results in Table 4 show that curating the preference dataset through pairs with large margins has meaningful impacts on downstream performance, suggesting that the relative betterness in pairs is more important than the individual scores of the responses. Also, studies using pointwise assessment, such as [1], report that as training progressed iteratively, most responses were “capped” at the maximum possible scores, making it difficult to make significant pairwise differences anymore. In contrast, self-improving approaches, which use pairwise assessment, such as [2], may be relatively better on this problem, but there are no discussions about these studies. Was there any experimental evidence of choosing pointwise assessment towards pairwise assessment in this work?

[1] Meta-Rewarding Language Models: Self-Improving Alignment with LLM-as-a-Meta-Judge (Wu et al., 2024)  
[2] Aligning Large Language Models by On-Policy Self-Judgment (Lee et al., 2024)

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper trains an LLM-as-judge model to generate both point-wise  and pairwise assessments. The model is fine-tuned on a training dataset that has a context, response, the rating of the response and the rationale (chain of thought reasoning) used to arrive at the rating. Upon training the model, a subset of the training data is sampled and for each datapoint, multiple generations of rationale and score are obtained. These generations are used to create the preference data for DPO. This iterative DPO is performed twice. 

A preference pair for the DPO is created  using the following techniques: (1) Amongst all the generations, the generation whose score matches the ground truth is taken as the chosen judgement and any of the incorrect one is taken as the rejected one. (2) The generations whose score is the mode are considered as the chosen ones while the others are considered as the rejected ones.  (3) A meta-judge is asked to rate either the rationales or the scores. Its rating is used to create the preference pairs where for each pair, the chosen judgement is rated higher than the rejected judgement. Several preference pairs are created for each datapoint.

### Strengths
They are able to take custom criteria and generating rating in accordance to it. Their evaluation datasets for point-wise comparison are very extensive and compare over multiple domains. They also empirically demonstrate that the iterative DPO helps in generating good quality rationales when compared to SFT.

### Weaknesses
1. This paper's ideas are heavily borrowed  from the self rewarding LLMs. That paper also uses rationale and scores to train a base LLM-as-a-judge model. After that it creates preference data based on the model's generations and performs iterative DPO. The main difference is that the self rewarding LLMs model is designed to only generate pairwise judgement and is trained in a multitask fashion to perform both LLM-as-a-judge and to follow instructions. While your paper uses the seed training data to create the preference data, the self rewarding paper asks the model itself to generate synthetic data. Though the initial model used in self-rewarding paper is a llama2 70B model, the algorithm can be applied to llama 3.1 8B model as well. Despite these variations, the basic methodologies remain the same in both the works. Thus, the novelty of this paper is fairly limited. Can you please describe the contributions of this paper when compared to the self rewarding LLMs paper.

2.  Given that the model was trained on both pairwise and point-wise comparison tasks, please include evaluations for pairwise comparison task on datasets such as RewardBench, PreferenceBench, InstruSum [1], HHH [2]  etc. Include https://huggingface.co/NCSOFT/Llama-3-OffsetBias-8B and a llama 8 version of self rewarding LLMs also as a baseline in addition to Skywork-Critic-Llama-3.1-8B.

### Questions
1. Why did you perform model merging? What were the challenges with multi-task training the initial model to perform both the tasks?
2. What is the time taken to train a self-rationalizing model vs the other baselines?

### Soundness
3

### Presentation
3

### Contribution
2
