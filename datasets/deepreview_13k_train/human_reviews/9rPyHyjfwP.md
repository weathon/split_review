# Domain-Agnostic Molecular Generation with Chemical Feedback

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
The generation of molecules with desired properties has become increasingly popular, revolutionizing the way scientists design molecular structures and providing valuable support for chemical and drug design. However, despite the potential of language models in molecule generation, they face challenges such as generating syntactically or chemically flawed molecules, having narrow domain focus, and struggling to create diverse and feasible molecules due to limited annotated data or external molecular databases.
To tackle these challenges, we introduce \textsc{MolGen}, a pre-trained molecular language model tailored specifically for molecule generation. Through the reconstruction of over 100 million molecular SELFIES, \textsc{MolGen} internalizes structural and grammatical insights. This is further enhanced by domain-agnostic molecular prefix tuning, fostering robust knowledge transfer across diverse domains. Importantly, our chemical feedback paradigm steers the model away from ``\textit{molecular hallucinations}'', ensuring alignment between the model's estimated probabilities and real-world chemical preferences. Extensive experiments on well-known benchmarks underscore \textsc{MolGen}'s optimization capabilities in properties such as penalized logP, QED, and molecular docking.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents MolGen, a domain-agnostic molecular generation model, and its application in generating molecules using the SELFIES molecular language. The paper discusses the ability of MolGen to discern essential substructures and compares it with other molecular generation approaches using the SMILES language. The paper also introduces a self-feedback mechanism to mitigate "molecular hallucinations" and improve the generation of molecules with desired properties.

### Strengths
1. The paper is well-structured with clear writing and is supported by rich and lucid illustrations.

2. The application of SELFIES, as opposed to SMILES, is more concise and effective in deep generative models, facilitating the analysis of generated results. 

3. The paper delves deep into the concept of 'Molecular Hallucinations' and attempts to address it, which is a beneficial discussion for the field of molecule generation.

### Weaknesses
1. Although an ablation study was conducted to check the self-feedback paradigm, there was no ablation experiment carried out to assess the use of SELFIES over SMILES. Instead, only a comparison was made between Chemformer and MolGen. Technically, a SELFIES-based MolecularLM implemented on BART does not seem irreplaceable. Given that many works involving molecule generation are still based on SMILES (such as MoMu, MolT5), the effectiveness of SELFIES in the work lacks further experimental verification. Specifically, the paper lacks a direct comparison of a BART-based model trained on SMILES versus one trained on SELFIES, holding all other factors constant. This would isolate the impact of the molecular representation on the model's performance, which is critical for justifying the choice of SELFIES.

2. The significance of the 'domain-agnostic molecular prefix tuning' step is questionable. It seems to be merely a measure to avoid overfitting in the overall model. Whether synthetic molecule generation and natural product generation in drug discovery can be considered two different tasks, and whether other dataset partitioning methods would have similar effects, are not explained. Therefore, the comparison of molecular distribution learning in the paper lacks persuasiveness. The paper does not provide a clear rationale for why this specific partitioning is necessary or if it provides any advantage over random partitioning or other methods. Furthermore, the lack of analysis on the impact of different dataset splits on the model's performance makes the claim of domain-agnostic prefix tuning less convincing.

### Questions
1. It would be highly beneficial if the authors could conduct further experiments to address the issues raised in the 'Weaknesses' section of this review.

2. Given that molecule generation typically needs to cater to a variety of requirements, have the authors considered other metrics beyond penalized logP, QED, and binding affinity for two human proteins? More persuasive experiments addressing a broader range of molecular properties could significantly enhance the applicability and robustness of the proposed model.

3. The correspondence between the attention scores and the specific molecular structures in Figure 8 and Appendix Figure 5 is not very intuitive. The current figures do not convincingly demonstrate that the SMILES-based PLM is focusing attention on less relevant positions. It would be beneficial if the authors could revise this figure to improve its clarity and interpretability, thereby aiding readers in better understanding the model's inner workings.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents MOLGEN, a new pre-trained molecular language model dedicated to molecule generation. By reconstructing over 100 million molecular SELFIES, MOLGEN has gained in-depth knowledge of molecular structures and grammar. This understanding is amplified by the domain-agnostic molecular prefix tuning, ensuring better knowledge transferability across a wide range of domains. A crucial feature of the model is the self-feedback mechanism, which safeguards against "molecular hallucinations" by ensuring that the model's estimated probabilities align with real-world chemical propensities. Comprehensive evaluation on established benchmarks highlights MOLGEN's superior performance in properties like penalized logP, QED, and molecular docking. Further analysis confirms its adeptness in accurately capturing molecule distributions, discerning intricate structural patterns, and efficiently exploring the chemical space.

### Strengths
1. This paper introduces a language model designed for molecule generation, adeptly capturing deep structural and grammatical insights through the reconstruction of over 100 million molecular SELFIES. 

2. The paper is well-written and easy to follow. Figures and Tables are very good. 

3. Compared to previous baselines, the proposed approach showcases impressive performance. Through comprehensive experiments, the paper convincingly demonstrates that SELFIES is a superior molecular representation to SMILES for 2D molecule generation tasks. This paper also provides very insightful discussions, which can help to understand the model behaviors.

### Weaknesses
What potential limitations might the self-feedback mechanism introduce in molecular generation?

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces MolGen, a molecule language model with 700M parameters built on the Bart architecture. Unlike its predecessor, Chemformer, MolGen employs SELFIES representations for molecules, ensuring 100% validity in molecule generation. Additionally, the paper presents a fine-tuning technique called 'self-feedback,' which aligns MolGen's generation probabilities with the chemical properties of the generated molecules.

The proposed method has shown significant improvement over previous methods. However, I have some major concerns on the paper's presentation, see the weakness section for details.

### Strengths
* The model shows significant improvements in the compared benchmarks, including distribution learning, targeted molecule discovery and constrained optimization.
* The proposed pretraining method is simple and plausible.

### Weaknesses
The submission contains significant issues, including the misuse of two major concepts and some questionable claims. Given the centrality of these concepts to the paper's overall argument, I recommend that the paper is not suitable for publication in its current form.

* **Concept Misuse: Molecular Hallucination:** The authors introduce the notion of "molecular hallucination" as the generation of molecules that do not exhibt the desired properties or follow human preferences. The term appears to be a misnomer, as it does not align with the traditional understanding of "hallucination" in the NLP domain. In NLP literature, hallucination generally refers to the generation of fictitious or nonexistent entities or events [1,2,3]. Conversely, the authors assert that their "hallucinated" molecules are chemically valid, meaning they are neither fictitious nor nonexistent. Therefore, the use of the term "hallucination" could be misleading and should be reconsidered for clarity and conceptual consistency. The related works on hallucination are missing, which further weakens the argument.
* **Concept Misuse: Self-feedback:** The authors refer to their fine-tuning approach as the "self-feedback paradigm." However, the proposed method is more like "**external-feedback**", instead of "self-feedback". In short, the proposed fine-tuning method is to align the molecule generation probabilities to chemical property scores **that are measured by an external model**. Given this external dependency, the term "external-feedback paradigm" would be a more accurate and descriptive name for the fine-tuning method. The core issue is that the feedback signal is not intrinsic to the model itself, but derived from an external source.
* **Missing Ablation Study:** MolGen is pretrained in two phases. In the second phase, MolGen is adapted on two datasets using a method called domain-agnostic molecular prefix tuning. After reading the submission, it remain unclear to me how the second phase can help other downstream tasks. Moreover, the ablation study on the second pretraining phase is missing. It is also unclear how is the proposed prefix tuning method compared against other parameter efficient tuning methods, like LoRA? The lack of ablation makes it hard to assess the contribution of the second pretraining phase.
* **Unclear Figures:** 
  * What are the x-axis of the two subfigures on the right of Figure 7? 
  * What are the x-axis and y-axis of the two subfigures on the right of Figure 8?
  * What are the x-axis of the Appendix Figure 2?

* **Novelty:** This is not the first molecule language model pretrained using molecule's SELFIE representations. [4] is also pretrained using SELFIES. The relevance and diffierence to [4] should be discussed. The authors need to clearly articulate the novelty of their approach compared to existing methods using SELFIES representations.
* **Dubious claims:**
  * In the second paragraph of introduction, the authors argue that previous works `are limited by their heavy reliance on task-specific tuning`. However, the proposed method also relies on a fine-tuning stage for downstream tasks. This claim is not well-supported given that the proposed method also requires fine-tuning.
  * In the third paragraph of introduction, the authors claims that `almost all previous studies have focused primarily on synthetic molecules, neglecting natural products`. However, the literature review to support this claim is missing. This assertion needs stronger evidence.
  * The opening paragraph of Section 2.2 describes a scenario where a molecule has one substructure that is effective for a specific task but is counteracted by another, ineffective substructure. However, it remains unclear how the proposed method addresses this issue. The mechanism by which the proposed method mitigates this problem is not clearly explained.
  * In the second paragraph of the introduction, the authors claim that `the brittleness of SMILES may lead to a high proportion of generated chemically invalid strings`. Are there any citation to support this claim?

### Questions
* Is the synthetic dataset in Section 3.1 referring to ZINC250K? If it is, directly use the name ZINC250k can improve the clarity.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a pre-trained molecular language model called MOLGEN to generate molecules from SELFIES with self-feedback. Specifically, MOLGEN contains two pre-training stages: 1) molecular language syntax learning using the BART model; and 2) domain-agnostic molecular prefix tuning using two sets of tunable prefix vectors in multi-head attention layers. Then, the authors use a self-feedback paradigm to align the pre-training language model with the anticipated chemical preferences in the downstream phase (i.e., the authors align the model’s probabilistic rankings of diverse molecular responses with preference rankings observed in actual chemical contexts).

### Strengths
Strengths:

- This paper is well organized and written.

- A two-stage domain-agnostic molecular pre-training model based on BART with SELFIES is proposed. Then, a self-feedback paradigm is used to alleviate the molecular hallucination problem.

### Weaknesses
Weaknesses:
- The experiment is incomplete. I suggest that the authors conduct more comprehensive experiments (i.e., baseline comparisons and ablation studies) to demonstrate the effectiveness of the proposed MOLGEN model. For example,
    - $\bf baseline~comparison$: most of the baseline models in the experiment are from before 2022 (e.g., JT-VAE (2018), GCPN (2018), GraphAF (2020), and GraphDF (2021)). I suggest the authors to compare more latest baselines to validate the MOLGEN. The current baselines do not represent the state-of-the-art in molecular generation, making it difficult to assess the true advancement of the proposed method. Specifically, the lack of comparison with transformer-based models that have shown strong performance in sequence generation tasks is a significant gap.
    - $\bf ablation~study$: the authors only performed ablation study on the self-feedback mechanism. In Eq. 8, the authors used the "soft" label to smooth the one-hot distribution (Eq. 2) into the target distribution. This is one of the contributions of the paper. The effectiveness of the "soft" label also needs to be verified in the ablation study. Also, the hyper-parameter "$\alpha$" controls the balance of the two losses and has an important impact on the performance of the model. How to choose a and the effect of different $\alpha$ on the model performance should also be demonstrated in the experiments. The ablation study should also include an analysis of the impact of the prefix vectors on the model's performance.

- The description of the model (Section 2) is not clear. More details need to be presented. For example,
    - Does the "$l$" in the paragraph above Eq. (1) indicate the total number of SELFIES in the dataset? Is it the same as the "$l$" in "two sets of "$l$" tunable prefix vectors" above  Eq. (3)? The current description is ambiguous and makes it difficult to understand the dimensionality of the prefix vectors and their relationship to the input data.
    - What do the two tunable prefix vectors refer to, and why are these two vectors used in multi-head? How to prove that the performance is improved after using them? The explanation of the prefix vectors is insufficient. It is not clear how these vectors are initialized, how they interact with the attention mechanism, and why two separate vectors are needed for keys and values. A more detailed explanation of their role and a justification for their design choices are needed.

### Questions
Questions:

- Please see the above.
- In the sentence "Finally, we encode the corrupted SMILES using a bidirectional model..." above Eq. (1), should it refer to "SMILES" or "SELFIES"?
- How $(S_i, S_j)$ pair in $\bf S^{*}$ are selected?

- Some typos:
    - Figures 2 and 3 have opposite locations.
    - It would be preferable to replace "ours" in tables 1, 2 and 3 with "MOLGEN". In addition, both "MOLGEN" and "MolGen" appear in the context, which should be consistent.
    - The masking and start tokens are denoted by "[MASK]" and "[S]" in the context, but are "[Mask]" and "[s]" in Figure 3. Consistency is needed.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
