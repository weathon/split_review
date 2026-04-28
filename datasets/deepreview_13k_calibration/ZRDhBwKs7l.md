# Concept Pinpoint Eraser for Text-to-image Diffusion Models via Residual Attention Gate

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Remarkable progress in text-to-image diffusion models has brought a major concern about potentially generating images on inappropriate or trademarked concepts. Concept erasing has been investigated with the goals of deleting target concepts in diffusion models while preserving other concepts with minimal distortion. To achieve these goals, recent concept erasing methods usually fine-tune the cross-attention layers of diffusion models. In this work, we first show that merely updating the cross-attention layers in diffusion models, which is mathematically equivalent to adding linear modules to weights, may not be able to preserve diverse remaining concepts. Then, we propose a novel framework, dubbed Concept Pinpoint Eraser (CPE), by adding nonlinear Residual Attention Gates (ResAGs) that selectively erase (or cut) target concepts while safeguarding remaining concepts from broad distributions by employing an attention anchoring loss to prevent the forgetting. Moreover, we adversarially train CPE with ResAG and learnable text embeddings in an iterative manner to maximize erasing performance and enhance robustness against adversarial attacks. Extensive experiments on the erasure of celebrities, artistic styles, and explicit contents demonstrated that the proposed CPE outperforms prior arts by keeping diverse remaining concepts while deleting the target concepts with robustness against attack prompts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes the Concept Pinpoint Eraser (CPE) approach for the purpose of addressing both erasure and preservation in Concept Erasure domain. Specifically, the paper first mathematically proves that modifying the linear mapping matrix of cross-attention cannot achieve both good erasure and preservation results. Then, the paper proposes nonlinear Residual Attention Gates (ResAGs), which are used to reduce the impact on irrelevant concepts. The paper trains ResAGs with novel erasing loss, attention anchoring loss, and adversarial training, and illustrates experimentally the excellent erasure effect, preservation effect, and robustness of the methods.

### Strengths
1. This paper elucidates the inadequacy of simply modifying the linear mapping matrix of cross-attention through a solid mathematical proof, which leads to a non-linear ResAgs module and a novel training loss function.
2. This paper conducts a large number of experiments, including character privacy, art style, NSFW content, etc., comparing many baseline methods.

### Weaknesses
1. The major weakness of this work is that the propose method may not work in open-source scenarios. Methods like ESD, UCE, RECE, etc. directly modify the UNet, and the LoRA of MACE can merge into the UNet, so all these changes can be directly applied to the UNet, and thus the user can't directly bypass these security mechanisms. CPE uses a non-linear add-on module, which cannot be merged to the UNet, so in the open-source scenario, the user can directly delete the code of the add-on module, thus skipping the security mechanism.

2.  Some parts are not presented clearly, which makes it difficult to follow. I have put the comments in the question section.

### Questions
1. From Table D.7, CPE uses hundreds of anchoring concepts to enhance retention. MACE only used 'a person' in the deletion of celebrities[1]. UCE, RECE only used the provided 1724 styles in the deletion of artistic styles. ESD, UCE, and RECE used only the empty text "", and MACE only used "a person wearing clothes" [ 2] in the deletion of NSFW concept. Can the authors explain whether the preservation effect of CPE comes from the methods proposed in the main text or from these numerous anchor concepts in the appendix?
2. For NSFW erasure, CPE erased 4 concepts, "nudity, naked, eratic, sexual" similar with  MACE. The more concepts that are deleted, the more effective the deletion tends to be. However, UCE, ESD, and RECE all remove only one word, "nudity", can the authors provide the results of removing only "nudity"?
3. From APpendix D.2, the authors set negative prompts for celebrities erasure. Was this negative cue word used in all baselines during the experimental comparisons?

### Soundness
3

### Presentation
2

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
This work proposes dubbed Concept Pinpoint Eraser by implementing Residual Attention Gates, improving both erasing and perserving performances. The study begins with a numerical analysis of the trade-off between these two aspects, given the current network structure. It then explores the addition of residual attention gates to address this dilemma. The effectiveness and robustness of the approach are evaluated through extensive quantitative and qualitative experiments. An ablation study is conducted to validate the effectiveness of each component.

### Strengths
1. To my knowledge, there are no significant flaws in the proofs of theorems; the work appears solid and reliable. 
2. The experiments demonstrate the effectiveness of this approach, and the performance gains are compelling enough to validate the work, even though it shows weaker results on certain erasing tasks. 
3. Additionally, the ablation study confirms the effectiveness of each component.

### Weaknesses
1.The robustness training seems to be a separate endeavor from the residual attention gates, while adversarial training acts more as a supplementary effort to enhance ResAGs. The robustness evaluation is directly performed on the model assessment. Does this indicate that the robustness of the model achieved through direct training is weaker than that of other models?
2. Given the proof, the addition of an extra term could be represented by various architectures. However, why do ResAGs demonstrate superior performance? This comparison is missing and not addressed in the discussion or experiments.
3. A concise algorithm description is recommended to enhance understanding of the training processes.

### Questions
1. The first and second weaknesses need to be addressed to ensure a thorough assessment of the proposed model.
2. The third weakness involves minor editing to enhance the overall presentation.

### Soundness
3

### Presentation
4

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
This paper focuses on unlearning specific target concepts from a pre-trained text-to-image diffusion model. It first proves that finetuning the query and key matrices in cross-attention layers, a method used in many prior works, may not preserve non-target concepts in the model. Building on this study, this paper introduces a non-linear additive module called Residual Attention Gate (ResAG), designed to selectively adjust the cross-attention layer weights for the target concept only. Combined with the proposed attention anchoring loss and adversarial training, the unlearned diffusion model is able to erase the target concept while preserving the remaining concepts.
Empirical results show that the overall framework achieves an optimal balance between erasing target concepts and preserving non-target ones across various domains. In addition, ablation studies confirm the effectiveness of each proposed component in both erasing and preserving concepts.

### Strengths
1. The theoretical analysis of finetuning cross-attention layers is solid and sound.  
2. The experimental results show that the proposed CPE successfully preserves the remaining concepts while erasing the target concept better than previous methods across various domains.  
3.  Each component in CPE is reasonable and shown to be effective in the ablation study.  
4. The paper is well-organized and easy to follow.

### Weaknesses
1. The assumption for the theoretical analysis of the proposed ResAG raises some concerns. According to the paper, Equation 4 holds if the modes of samples can be detected and if $||f(E)||^2_F$ is small for remaining concepts. How can one determine the modes of samples? Additionally, what threshold for $||f(E)||^2_F$​ is considered "small enough" to effectively protect the remaining concepts? The paper's explanation of detecting modes as classifying concepts based on their embeddings is not entirely clear. For instance, if the target concepts are "Andrew Garfield", "Bill Clinton", and "Keanu Reeves", it's unclear how the 'modes' would be defined for each of these, especially considering that the text embeddings for each name would likely form a distribution rather than a single point. Furthermore, the function $f(E)$ is described as responding to the full concept embeddings, but the concern remains about how it would differentiate between similar tokens across different concepts, such as the word "Bill" in "Bill Clinton" and "Bill Murray".


### Questions
Multiple typos in the proof of Theorem 1 (Appendix B)  
1. In the statement of Theorem 1, "Let $\tilde{W}^h_k$ and $\tilde{W}^h_k$ be the updated weights of $W^h_k$ and $W^h_k$." One of $\tilde{W}^h_k$ should be $\tilde{W}^h_v$ and one of $W^h_k$ should be $W^h_v$.  
2. Line 795, "$|| \sum^{H}_{h=1} f_1(\tilde{W}^h_k E)f_2(\tilde{W}^h_v E) - f_1(W^h_v E)f_2(W^h_k E) ||_2$". The first term should be $f_1(\tilde{W}^h_v E)f_2(\tilde{W}^h_k E)$.
3. Line 798, same typo as above  
4. Line 808, $L_{W^i_o, W^i_v} M$ should be $L_{W^h_o, W^h_v} M_1$

### Soundness
3

### Presentation
3

### Contribution
3
