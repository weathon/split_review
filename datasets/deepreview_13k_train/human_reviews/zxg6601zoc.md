# Re-Imagining Multimodal Instruction Tuning: A Representation View

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Multimodal instruction tuning has proven to be an effective strategy for achieving zero-shot generalization by fine-tuning pre-trained Large Multimodal Models (LMMs) with instruction-following data. However, as the scale of LMMs continues to grow, fully fine-tuning these models has become highly parameter-intensive. Although Parameter-Efficient Fine-Tuning (PEFT) methods have been introduced to reduce the number of tunable parameters, a significant performance gap remains compared to full fine-tuning. Furthermore, existing PEFT approaches are often highly parameterized, making them difficult to interpret and control. In light of this, we introduce Multimodal Representation Tuning (MRT), a novel approach that focuses on directly editing semantically rich multimodal representations to achieve strong performance and provide intuitive control over LMMs. Empirical results show that our method surpasses current state-of-the-art baselines with significant performance gains (e.g., 1580.40 MME score) while requiring substantially fewer tunable parameters (e.g., 0.03% parameters). Additionally, we conduct experiments on editing instrumental tokens within multimodal representations, demonstrating that direct manipulation of these representations enables simple yet effective control over network behavior.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a novel Multimodal Representation Tuning which can editing LMM representation and provide control. The paper introduces a representation editor $\phi$ based on linear representation hypothesis and interchange interventions, which can apply to different representations in LMM. The overall writing is clear. The experiments cover the comparison between the MRT and the other PEFT methods.

### Strengths
1.	The overall writing is clear.
2.	The idea is general and could be applied to many different applications. I think this would be of interest to people in the LMM community.
3.	The proposed method is simple yet effective.
4.	The experiments clearly show the improvement of the MRT over the PEFT.

### Weaknesses
1.	There are some typos. For example, ##hu2024bliva## in the "Multimodal Instruction Tuning" section of the related work.
2.	The ablation study is insufficient. I would expect more ablation experiments, such as applying MRT only to Visual Representation and Cross-modality Representation.
3.	There is too little theoretical analysis on why MRT is better than PEFT.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
3

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
This paper introduces Multimodal Representation Tuning (MRT), a parameter-efficient fine-tuning method to enhance controllability and interpretability in multimodal large language models (LMMs). MRT addresses the challenge of adapting LMMs effectively with fewer parameters by leveraging token-level multimodal representation control, achieving superior performance with up to 21 times fewer parameters than similar approaches. The authors explore and improve model behavior control through MRT, illustrating benefits in various multimodal perception and cognition benchmarks.

### Strengths
- MRT is intuitive, simple, and effective. It uses significantly fewer parameters while achieving strong results, making it suitable for resource-constrained applications.
- The approach provides granular control over the representation editing, enabling counterfactual output generation that enhances interpretability.
- The method is validated across multiple multimodal tasks, illustrating its effectiveness in diverse domains such as OCR, visual perception, and spatial reasoning.
- The paper is well-written and easy to follow.

### Weaknesses
 - The rank parameter is integral to MRT’s performance, but it currently requires manual tuning, which may limit practical adoption. While promising, the need for automated rank selection is highlighted as a limitation, suggesting a more autonomous rank-searching mechanism that could enhance usability.
- The empirical performance is decent, but could you elaborate on MRT's main contribution compared to ReFT instead of extending the interchange intervention idea into MLLM? Specifically, the paper needs to clarify how the token-level control offered by MRT provides a significant advantage over existing representation tuning methods, beyond simply applying the technique to a multimodal setting. The current explanation lacks a deep dive into the unique benefits of this fine-grained control in the context of MLLMs.
- Given its control over multimodal representations, MRT’s potential for misuse (e.g., manipulation of outputs) is acknowledged but not fully addressed in terms of mitigation strategies. Could you provide some examples of possible misuse of MRT utilizing controllability?

### Questions
1. Could the authors elaborate on any plans to automate the rank-tuning process within MRT to simplify its application?
2. Section 4.3 is particularly interesting to me. However, I think the attacker can easily break the controllability only by changing the order of the text instruction. Do you have any potential solutions and ideas on that?
3. Instead of simple image classification, are there other qualitative examples of counterfactual controls (e.g., VQA)?
4. Any analysis on which set of layers L to intervene on for visual / cross-modality / multimodal editor?
5. What are some insights on fine-tuning only prefix/suffix tokens of textual embedding in the multimodal editor?
6. Minor Errata
   1. L84: hu2024bliva looks typo.

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
3

### Summary
This paper introduces a method for tuning large multi-modal models (LMM) in a efficient but effective way so that it can achieve similar performance to full fine-tuning, with an additional objective of having a controllability. The key idea of this paper is based on a prior technique that learns parameters that edits the representations. The main contribution of this paper is to make use of this technique for efficient tuning of LMMs, and the experiments show that this idea indeed is helpful and the paper did a good job of investigating the effect of various design choices.

### Strengths
- Motivation is clear
- Intuitive and simple idea that works well
- Extensive analysis/ablation on the design choices

### Weaknesses
Experiments on controllability is interesting but not conclusive. For instance,
- What would happen if you don't use ROI and do train with all tokens?
- What would happen if you fine-tune other baselines for this setup?
- What would happen if you use a sentence that has a same semantic meaning to 'Is the object an e in the image?' but with different structure and words, after fine-tuning? Would the model still be controlled as intended?

Additional weaknesses are:
- Figure 5 on the optimization landscape is interesting but I'm not sure how it is cherry-picked. Would there be a way to make this claim be supported by some metrics or more figures?
- Main method section feels a bit redundant to me, not much of a difference between each subsection. It could be nice to think of a better way to re-structure, remove redundancy, and think of a way to clearly explain what differences exists

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
5

### Rating Number
5

### Confidence
5

### Summary
This paper adopted the parameter-efficient fine-tuning method Representation Tuning to the multimodal large language model domain. This paper used different representation editors for the vision encoder, LLM, and cross-modality projectors to optimize the visual representation, cross-modality representation, and multimodal representation. Experiments on several MLLM and image classification benchmarks show the efficiency and effectiveness of the proposed method. The paper further conducted controllability studies on image classification benchmarks to show the possible controllability of the proposed methods. Extensive ablation studies are furhter discussed for the designs of several hyper-parameters of the proposed method.

### Strengths
1. This paper provides a promising and efficient PEFT method for MLLMs as an alternative to the commonly used LoRA-based methods.
2. The ablation studies are comprehensive for a better understanding of the proposed method and hyper-parameter design choices.

### Weaknesses
1. The paper directly adapts the representation learning method in LLM to the MLLM in a rather straightforward way thus the technical contribution is limited.
2. The benchmark selection for comparisons is not comprehensive and convincing enough. MME is a relatively small-scale MLLM benchmark that has non-trivial variances. The paper should include more comprehensive and commonly used multimodal benchmarks like SEED, MMBench, MMMU, GQA, VQAv2, ChartQA, and DocVQA for more convincing comparisons.
3. The performance of other methods might have some problems. In Table 1 of this paper, the lora baseline is significantly worse than the full-finetuning one, but according to LLaVA's results (https://github.com/haotian-liu/LLaVA/blob/main/docs/MODEL_ZOO.md), the performances should be similar. Besides, the proposed method adds tunable parameters in the vision encoder while other baselines use frozen vision encoders. Baselines with unfrozen vision encoders should also be added for comparison.
4. As the proposed method brings additional parameters and time costs in the inference phase, the efficiency advantage of the proposed method should be clearly verified in the training phase, including GPU memory usage and training speed comparisons,
5. To validate the generalization ability of the proposed method, the authors should include experiments with different vision encoders + different LLM types and sizes.
6. Although the paper claimed that the proposed method brings more interpretability and controllability to MLLMs compared with common practices, it is hard to see how could the method really help the interpretability and controllability of MLLMs. The controllability study is too customized with human priors and provides little help for MLLM controllability in the general case.

### Questions
1. In Sec 3.2 Cross-modality Representation part, it says that the projector integrates representations from each layer of the visual encoder. Does this mean you combine vision features in different layers in the vision encoder as the final vision input for LLM?
2. What is the reason for applying prefix and suffix editors on textual tokens, as the prefix and suffix of different textual prompts at the same position might have very different semantics and meanings? Wouldn't this be harmful for the claimed interpretability and controllability?

### Soundness
2

### Presentation
2

### Contribution
2
