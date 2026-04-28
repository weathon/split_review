# CITING: Large Language Models Create Curriculum for Instruction Tuning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5

## Abstract
The recent advancement of large language models (LLMs) has been achieved through a combo of instruction tuning and human alignment. However, building manually crafted instruction datasets and performing human alignment become the bottleneck for scaling the development of LLMs. In this paper, we exploit the idea of leveraging AI models in lieu of humans as the teacher to train student LLMs. Our method is inspired by how human students refine their writing skills by following the rubrics and learning from the revisions offered by their tutors. Specifically, we employ a teacher LLM to create a curriculum for instruction tuning of the student LLM, namely \textbf{C}urriculum \textbf{I}nstruction \textbf{T}un\textbf{ING} (\method). It encompasses two main steps: (1) the teacher LLM crafts the rubrics for evaluating the answers corresponding to various types of questions, and (2) the student LLM learns to follow the rubrics and perform self-correction from the revision made by the teacher. We further iteratively carry out it to embody the procedure of \method. We compare \method to a series of state-of-the-art baselines on four datasets. Our method demonstrates strong improvement in terms of articulate, in-depth, and comprehensive by GPT-4 evaluation. Specifically, it achieves an average winning rate of 79.4\% over SFT, 73.4\% over RLHF, 78.1\% over RRHF, and 76.3\% over RAFT, respectively.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel approach named Curriculum Instruction TunING (CITING) for the development and scaling of Large Language Models (LLMs). Instead of a heavy reliance on human-crafted instruction datasets and human alignment, CITING employs a teacher LLM to guide and train student LLMs. This methodology mirrors the traditional tutor-student dynamic, where students refine their skills using rubrics and revisions. The process entails the teacher LLM offering evaluation criteria, with the student LLM subsequently learning to self-correct based on these guidelines. Experimental findings indicate that CITING surpasses contemporary leading methods like RLHF across several benchmarks.

### Strengths
1. The Curriculum Instruction TunING approach is innovative. Using teacher LLMs to guide student LLMs, which mirrors the tutor-student relationship, is a fresh perspective in this field.

2. The paper delineates a meticulously crafted methodology, ranging from rubric design with the teacher model to the iterative fine-tuning of the student LLM.

3. The narrative is lucid, providing a thorough explanation of the CITING methodology.

### Weaknesses
1. Over-reliance on Teacher LLM: There's a potential risk if the teacher LLM possesses biases or inaccuracies, as it could transfer these shortcomings to the student LLM. Consequently, the effectiveness of CITING is largely contingent on the quality and resilience of the teacher LLM. The paper does not discuss any mechanisms for mitigating this risk, such as methods for identifying and correcting biases in the teacher's evaluations or incorporating diverse teacher models to reduce reliance on a single source of guidance. This lack of robustness in the face of a potentially flawed teacher model is a significant concern.

2. Test Phase Limitations: During the test phase, the model's potential might be constrained by the extent of criteria it can retrieve from a fixed corpus. The paper does not explore the impact of the fixed criteria corpus on the model's ability to generalize to unseen problems, especially those that might require nuanced or novel evaluation criteria. The reliance on a pre-defined set of criteria could limit the model's adaptability and performance in real-world scenarios where the range of problems is not fully known in advance.

3. Evaluation Metrics: The paper predominantly emphasizes the winning rate for comparing with other techniques. Yet, in scenarios like QA or RC, shouldn't the method also be evaluated using standard metrics? While a winning rate provides a high-level comparison, it does not offer a detailed understanding of the model's performance on specific tasks. Standard metrics like F1 score, precision, recall, or ROUGE scores would provide a more granular view of the model's strengths and weaknesses in QA and RC tasks, allowing for a more thorough comparison with existing methods.

### Questions
1. How does CITING address potential biases or inaccuracies if the teacher LLM possesses them?

2. During the test phase, how does the model overcome the limitations of retrieving criteria from a fixed corpus?

3. Beyond the winning rate, have other standard metrics been considered for evaluating CITING, especially in QA or RC scenarios?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes an instruction tuning method, which first employs a teacher LLM to craft the rubrics for evaluating the answers to various types of questions, and then trains the student LLM to follow the rubrics and perform self-correction from the revision by the teacher. The authors have shown its effectiveness on four datasets, comparing with several baseline methods.

### Strengths
**Clarity**

- The presentation of this work is clear and easy to follow. 
- The method is simple and effective and has shown clear improvement over baselines.

### Weaknesses
My main concern about this work is about novelty and clarity. Even though the method proposes using criteria as a guidance to augment instruction tuning data, the overall method, still, can be viewed as a complex version of data distillation. Recently there have been tons of works proposing pretty similar ideas, such as Orca [1], WizardLM [2], MAmmoTH [3], etc., which all leverage data augmentation (guided by certain criteria/score function, etc.). It might be good to compare CITING with these methods, or at least discuss why the contribution of this work is significant.

I'm not fully convinced about the method of how you assign quality scores to the generated data. In Section 3.2, why does the fact that the candidate instructions have their embeddings near those of rubrics mean that the candidates are legit? In terms of the Appendix, the so-called rubrics are basically some descriptions or requirements of a certain task --- do we really need a complex pipeline like CITING or we can simply include them as the "system message" in the few-shot examples (for augmentation)?

Also, there is no code and data uploaded as supplementary materials, which causes some difficulties for me to fully understand your method.

### Questions
How did you implement RLHF? There is no official implementation of that and your method has shown significant improvement over RLHF. Could you upload your code if possible (or point to some open-sourced implementation you are using)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a method to train large language models using AI feedback instead of human feedback. The method, called Curriculum Instruction TunING (CITING), uses a teacher LLM to create rubrics and revisions for different types of instructions, and a student LLM to learn from them. The paper shows that CITING outperforms existing methods on four datasets in terms of articulation, depth, and comprehensiveness.

### Strengths
1. This paper proposes a novel method to train large language models using AI feedback instead of human feedback, which reduces the cost and difficulty of scaling LLM development.
2. This paper introduces curriculum instruction tuning, which leverages a teacher LLM to create rubrics and revisions for different types of instructions, and a student LLM to learn from them. This is an interesting use case of LLM as a planner for training another LM.
3. This shows that CITING outperforms existing methods on four datasets in terms of articulation, depth, and comprehensiveness.

### Weaknesses
1. The technical novelty may be limited. The method is also complicated.
2. This paper does not evaluate the robustness or generalization of CITING to unseen or adversarial instructions. This could be an issue as the teacher model only teaches in-domain curriculums. I'd like to see discussion on this.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes an alternative to RL-based methods (e.g.: RLHF) for improving the quality of generations from instruction-tuned models by distilling preferences from other language models and using them in a supervised finetuning setup. Particularly, a teacher LLM is used to improve a student LLM by 1) generating a rubric (or criteria for good responses) for each instruction in an instruction-tuning dataset, and 2) iteratively rewriting the student's response given the rubric and the current response.

The student is initialized by training it on the instruction tuning dataset using SFT and then continued to be trained to rewrite its responses given the targets from the teacher. At inference time, a rubric is retrieved from the set generated for the training data, and an iterative process is followed to generate the student's response.

This process is used to train a Llama-7B model on the Alpaca dataset, and it is evaluated against SFT, RLHF,  RRHF (Yuan et al., 2023; RLHF with ranking instead of pairwise preferences) and RAFT (Dong et al. 2023; use reward model to select training data) in terms of win-rate according to GPT-4 on a held-out subset of Alpaca, reading comprehension, factual knowledge, and commonsense datasets.

### Strengths
Exploring alternatives to RL algorithms using sparse feedback to improve LM generations is highly relevant and timely. This paper presents some good ideas, particularly using feedback from other LMs in the form of rubrics as rewrites, that can contribute to this research area.

### Weaknesses
Algorithm: The student is trained as a response rewriter given a rubric during the iterative process. This raises the following concerns:

- Because of this formulation the student model requires a rubric and a version of the response to rewrite at inference time. The dependence on additional inputs might impact the generalizability of the student model as obtaining. Particularly, the rubrics generated for the training data may not generalize to the new instructions at inference time. The reliance on a retrieved rubric introduces a potential bottleneck, as the quality of the generated response is now contingent on the relevance and accuracy of the retrieved rubric. A mismatch between the training rubric and the inference instruction could lead to suboptimal performance. Furthermore, the method does not specify how to handle cases where no suitable rubric exists in the training set for a given instruction, which could further limit its generalizability.
- Moreover, the inference process is required to be iterative due to this algorithm, and hence requires additional compute. The iterative nature of the inference process introduces significant computational overhead, making the method less efficient than direct generation approaches. Each iteration requires the student model to process the rubric and the current response, which can be time-consuming, especially for longer sequences. This computational cost may limit the practical applicability of the method in resource-constrained environments.
- Since the student is initialized using SFT on the instruction tuning dataset, the initial draft responses produced by the model may be of good quality, but continuing to train it to be a rewriter might affect the original instruction following capabilities. An evaluation of the original drafts produced by the student after the iterative training might be helpful. The continued training as a rewriter could lead to a degradation of the model's ability to generate responses from scratch, as it becomes increasingly specialized in modifying existing text. This could result in a model that performs well in the iterative rewriting process but underperforms when generating responses without a prior draft. It is important to evaluate the model's performance on both tasks to fully understand its capabilities and limitations.

One solution to address the concerns above could be to train a separate rewriter (conditioned on the rubric and the previous responses), and iteratively finetune the student model only on the instruction following task (i.e., not condition its outputs on the rubric and previous responses)

Baselines: This paper proposes multiple changes compared to the current RL from feedback setup for improving instruction tuning models: having the teacher generate a rubric, continued training of models with SFT, curriculum learning with minimal rewrites given by a teacher. These are all orthogonal improvements and can be evaluated separately. The current evaluation setup conflates these changes. I propose the following additional baselines:
- Effect of continued training: Simply train the student model with additional SFT steps, and do not use a teacher model at all. The current comparison between CITING and SFT is not entirely fair because CITING uses additional training steps.
- Effect of the rubrics: Use the teacher model to generate a rubric and train the student model with additional SFT steps also conditioned on the rubric.
- Fairer comparison with RLHF: RLHF might perform better with better pairwise preference data. A good baseline would be to generate rewrites from a teacher model and use them to train a reward model and perform RLHF.

### Questions
- The details of the baselines are missing. How exactly are the RLHF models trained? Do they use preferences on the same 1000 instances used for CITING?
- How do you ensure that the teacher minimally edits the student responses in the CITING algorithm? Do you actually see that the edits are minimal?
- How do you select the number of iterations at training time and inference time in CITING?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
