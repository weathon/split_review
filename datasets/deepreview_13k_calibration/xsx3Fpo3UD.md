# Advantage-Guided Distillation for Preference Alignment in Small Language Models

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Alignment techniques such as RLHF enable LLMs to generate outputs that align with human preferences and play an essential role in their effectiveness. However, their impact often diminishes when applied to smaller language models, likely due to the limited capacity of these models. Instead of directly applying existing alignment techniques to smaller models, we propose to utilize a well-aligned teacher LLM to guide the alignment process for these models, thereby facilitating the transfer of the teacher's knowledge of human preferences to the student model. To achieve this, we first explore a straightforward approach, Dual-Constrained Knowledge Distillation (DCKD), that employs knowledge distillation with two KL-divergence constraints from the aligned teacher to the unaligned student. To further enhance the contrastive effect, we then propose Advantage-Guided Distillation for Preference Alignment (ADPA), which leverages an advantage function from the aligned teacher to deliver more nuanced, distribution-level reward signals for the student's alignment. Our experimental results demonstrate that these two approaches appreciably improve the alignment of smaller language models and narrow the performance gap with their larger counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper explores how to enhance the effectiveness of small language models  to make their generated outputs more aligned with human preferences through preference alignment techniques. To address the issue that technologies like RLHF do not align well with human preferences on small language models, the paper proposes two methods: Dual-Constrained Knowledge Distillation (DCKD) and Advantage-Guided Distillation for Preference Alignment (ADPA). The experimental results show that both methods can significantly improve the alignment of small language models and narrow the performance gap with large models.

### Strengths
- The two methods proposed in the paper combine RLHF with distillation, providing insights into the preference alignment of small language models and solving problems that previous methods had not addressed. 
- The experimental section is well-designed, with numerous comparative and ablation experiments to verify the performance improvements of the methods. 
- The paper is well-written, with detailed descriptions of the two methods, including algorithm steps and formulas, which are easy to understand.

### Weaknesses
 - ADPA provides more nuanced guidance signals, but the additional computations introduced by fine-grained signals may increase the computational overhead, and the paper seems to lack specific quantitative metrics on this point.
- The experimental section utilizes a rather singular evaluation dataset, without providing results on a broader range of models, domains, and data. Additionally, there is a lack of experiments assessing the impact of teachers of varying proficiency levels on the results.

### Questions
- In Formula 11, $L_s$ seems to be undefined. Does it refer to $L_{SFT}$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the alignment of small language models. It points out that directly applying alignment techniques to small language models may not work well due to the limited capacity of these models. To this end, the authors present 1) a straightforward approach Dual-Constrained KD by integrating both positive and negative signals, and 2) an enhanced approach Advantage-Guided Distillation for Preference Alignment that involves a distribution-0level reward signal given by an advantage function. Extensive experiments with three teacher-student model settings demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper investigates the challenge of aligning small language models, the proposed methods are well-motivated and principal.

2. The ADPA method considers the distribution-level reward signal, which is an advancement compared to the previous KD methods.

3. The KD baselines are comprehensively compared, and the studied teacher-student settings are representative.

4. This paper is well organized and the presentation is decent.

### Weaknesses
1. Limited baseline of alignment methods. In Table 1, while the KD baselines are comprehensively compared, the alignment baseline only includes DPO.

2. Computation overhead of the KD methods. It is not clear whether the proposed methods (and other baseline KD methods) consume more training or inference resources compared to directly applying alignment techniques to the student models.

### Questions
1. I wonder if directly applying some advanced alignment methods to the smaller language models can present a competitive performance.

2. Could you elaborate more on the computational cost of the proposed methods v.s. directly applying alignment techniques?

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
3

### Summary
This works combines the concepts of RLHF and knoledge distillation to propose the advantage-guided distillation method for preference alignment. This realizes the impressive the performance improvement of the small models in the preference alignment stage.

### Strengths
1. The idea of improving the performance of small model in the preference alignment stage is interesting.
2. Advantage-guided distillation from the preference-aligned teacher model to the student model is novel for knowledge distillation.
3. The experiments are detailed and the presentation is good.

### Weaknesses
This is a good work. The proposed method is simple yet effective. I do not have additional concerns for it.

### Questions
1. Why experiment on  H2O-Danube3-500M and H2O-Danube2-1.8B-Base, given the availability of more popular models today, such as LLaMA-3.2-1B, Qwen2.5-0.5B . If the experiment on more popular models can be provided, the result will be more solid.

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
This paper explores knowledge distillation (KD) for LLMs during the preference alignment stage. It first introduces a simple baseline DCKD which applies Vanilla KLD-based KD on both the positive and negative examples. Then, the paper propose ADPA to enhance the contrastive signals of KD. Experiments show the effectiveness of ADPA and its components, suggesting the importance of leveraging the perference signals for KD.

### Strengths
1. How to leverage the preference signals for KD is an important but under-explored problem.
2. The methods are concise and easy to implement.
3.  The empirical results of ADPA is strong.

### Weaknesses
1. Although ADPA seems effective empirically, it is still unclear how the improvement is related to the motivation of the method. From Section 3.3 and Algorithm 1, it seems ADPA does not need the preference labels: only the prompts and the grouth truth reponses works for ADPA. How is ADPA related to preference alignment?
2. From Table 2, it seems that the reference teacher model is critical for the effectiveness of ADPA. It would be better to add more explanation on why the difference between $\pi_{dpo}$ and $\pi_{ref}$ should be considered, rather than $\pi_{dpo}$. Furthermore, what if $\pi_{dpo}$ is removed from Equation (11)? (to show the effect of $-\log \pi_{sft}$ alone)

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2
