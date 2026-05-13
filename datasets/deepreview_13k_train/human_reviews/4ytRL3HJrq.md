# Nova: Generative Language Models for Assembly Code with Hierarchical Attention and Contrastive Learning

- Decision: Accept
- Scores: 6, 3, 8, 5, 6

## Abstract
Binary code analysis is the foundation of crucial tasks in the security domain; thus building effective binary analysis techniques is more important than ever. Large language models (LLMs) although have brought impressive improvement to source code tasks, do not directly generalize to assembly code due to the unique challenges of assembly: (1) the low information density of assembly and (2) the diverse optimizations in assembly code. To overcome these challenges, this work proposes a \emph{hierarchical attention} mechanism that builds attention summaries to capture the semantics more effectively, and designs \emph{contrastive learning objectives} to train LLMs to learn assembly optimization. Equipped with these techniques, this work develops \emph{\ours{}}, a generative LLM for assembly code. \ours{} outperforms existing techniques on binary code decompilation by up to 14.84 -- 21.58\% (absolute percentage point improvement) higher Pass@1 and Pass@10, and outperforms the latest binary code similarity detection techniques by up to 6.17\% Recall@1, showing promising abilities on both assembly generation and understanding tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a way of training an LLM to improve its performance on tasks that require understanding of assembly code, in particular code decompilation, and assembly code similarity detection.

This is achieved by several contributions:
1. A multi-way, parallel corpus of programs written in C, as well as the corresponding assembly produced by `gcc` with different levels of optimization (0 to 3), used for further training of pre-trained LLMs.
2. A hierarchical attention mechanism, structured to summarize the content of each instruction into the representation of a single token. This mechanism is compatible with existing models.
3. Two auxiliary contrastive loss objectives: a "functionality" one that minimizes the distance between representations of the same original code, while maximizing the distance between representations of different code pieces, and an "optimization" one encoding the fact that further levels of optimization should increase the distance between program representations.

Two variants (with 1B and 6B parameters respectively) of a model trained with these changes, and further fine-tuned for the task of interest, show a large improvement over state-of-the-art.

### Strengths
Originality
--------------
1. While hierarchical attention mechanisms are not new, the design of this one is innovative in that: it takes into account the specific format and constraints of assembly instructions, and it accommodates for using regular tokens in the same sequence (e.g., natural text instructions).
2. The contrastive objective losses, as well, encode a priori knowledge of the underlying data: compilation stages preserve semantics, and optimization stages are sequential.

Quality
----------
The different contributions are overall sensible, and contribute to the performance of the model. Experiments are adequately designed, and support the conclusions of the paper. The additional experiments help understand the role of the different contributions, in particular their effect on how embeddings get clustered and the effect it can have on the final model's performance.

Clarity
---------
1. The paper includes most of the relevant information, either in the main text or appendix. Relevant literature is mentioned and cited.
2. Figures and examples make it much easier to understand the logic, especially Fig. 3.

Significance
-----------------
1. This work shows a significant improvement on benchmarks, sustained across model sizes, and adaptable to other models. This is an advancement on an important, developing field of machine learning applications.
2. Given that these improvements do not require any in-depth change (e.g., to the vocabulary) and are compatible with already pre-trained model make it easier to experiment with in different settings.

### Weaknesses
Quality
----------
1. One of the 3 motivating cases in the introduction, malware detection, is not evaluated or considered at all in the rest of the paper. I understand the scope of the paper needs to end somewhere, but it would have strengthened the paper to include experiments on such a dataset.
2. Details are missing in how the authors are certain that test data sets (both for decompilation and for similarity detection) do not overlap with any of the training data, including the pre-training data of DeepSeek-Coder, even inadvertently.
3. An additional ablation on $\textrm{Nova}_{-CL}$ would have helped see if there are any non-linear interactions between HA and CL.

Clarity
---------
The overall organization of the paper could be improved. Many times, a concept, method, or setting is used in context before being formally explained. For instance:
1. If the "Related Work" section is positioned earlier, it would help introduce the baseline models (DeepSeekCoder, LLM4Decompile) that are used in the previous "Results" section, as well as attention mechanisms, including LongCoder's, also used earlier.
2. When describing the new datasets, it should be clear much earlier that "source code" really means "C code" (in the caption of Table 1, for instance), "assembly" is X86 assembly (or maybe X86-64? that's not so clear), that only `gcc` is considered as a compiler, and whether each "program" actually means a full executable program, or if it includes functions as well.
3. Similarly, the contrastive losses mention "the embedding" of a function, which is quite ambiguous in transformers, especially if the model family (encoder-decoder?) is not mentioned.
4. There is also a lot of ambiguity in notation, or the semantics of different objects. For instance:
    * Do Table 1, and Appendix A.2, refer to the original "AnghaBench" and "The-Stack" datasets, or the new datasets constructed by the authors in Section 2.1? Maybe it would be better to name the new ones.
    * In Functionality CL, l. 208 says it "optimizes Nova with the constraint", but a constraint is not a loss or objective. l. 215, "constraints can be trained" do not really make sense. It's also not obvious how the loss defined at l. 220 actually implements (a relaxation of) these constraints. It's also not explained if the sum over $f_i \in F$ is actually done over all the million embeddings in the corpus, or how it's implemented in practice.
    * K is introduced in Section 2.5, and then in 3.3., but we don't know what kinds of values will be used in practice. Also, Table 2 uses "Pass@K", but that's not the same K.
    * In captions of Fig. 4 (b) and (d), the tables are more "designs" than "implementations"
    * In Fig. 4 (b), the 1-4 indices are unfortunate as, for instance, $O0_3$ reads a lot like `-oO3`
    * The equations at l. 220 and l. 266 have a really similar form, but the use of indices $i$ and $j$ is swapped between the two, making it a bit harder

Significance
-----------------
The results are somewhat limited by the use of a single assembly language, and a single compiler, but this is acknowledged and does not seem like a fundamental limitation.

Minor points
-----------------
l. 461: "cauclated" -> "calculated"?

In the bibliography:
- Vaswani et al. is actually from 2017, not 2023 (though the arXiv version has had an inconsequential update in 2023), and a venue should be indicated (I'd suggest NeurIPS rather than arXiv)
- Other articles are missing a venue or source
- Several articles have incorrect capitalization in the title due to the lack of curly braces, e.g., use `{CodeT5}` to avoid it being rendered as "Codet5".

### Questions
1. Why do the evaluation for code similarity detection use cosine similarity (l. 321) when the objective (l. 212) uses the l2 distance?
2. What is the underlying metric for the Pass@k in the decompilation evaluation? Exact match, or some more lenient equivalent? It seems wrong to use exact match when, for instance, variable names would be arbitrary.
3. In Table 4, the second row is exactly the "Nova-1B" row of Table 2, but I was under the impression that "Nova-1B" was more than just "DeepSeekCoder + Nova's attention", in particular the additional training data, and CL objective. Are the numbers off, or the caption, or did I miss something?
4. When creating the assembly datasets (Appendix A.1), why go all the way to compiling executables, then using `objdump` for disassembling, with the associated possibilities of failure, rather than dump the assembly in the first place with `gcc -S`?
5. Do you have preliminary results, citations, or intuition behind the "normalizing" step of the assembly language performed in Fig. 6, in particular the addition of spaces? Is that necessary?

Minor points:
1. In the numerator on l. 265, is $f_j^q$ supposed to be $f^q$? or $f_j^p$ for which the substitution wouldn't apply?
2. l. 300, how many samples do the GPT models perform, then, to be able to compute the Pass@10 in Table 2?

Edit after discussion and update
--------------------------------------------
The overall clarity has improved, and additional information was provided.
Most questions have been answered, so I'm raising my score.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Nova, a generative language model specifically crafted for understanding and generating assembly code. Nova integrates hierarchical attention mechanisms with contrastive learning to effectively capture the semantics of code. The hierarchical attention mechanism focuses on intra-instruction, preceding-instruction, and inter-instruction relations, while contrastive learning ensures that functionally equivalent code, even with different optimizations, is similarly represented. The model is evaluated on two key tasks: decompilation (recovering high-level source code from assembly) and binary code similarity detection (BCSD) (measuring the similarity between binary code functions). Nova shows superior performance in both tasks, excelling in decompilation by accurately generating source code from optimized assembly, and achieving high recall in BCSD by effectively identifying similar code across different optimization levels.

### Strengths
1. This paper is well-structured and easy to follow. Concepts such as hierarchical attention and contrastive learning are clearly explained.
2. The paper proposes a new method for encoding assembly code by using a Hierarchical Attention Mechanism to effectively capture the semantics of assembly instructions, while employing Contrastive Learning to ensure that functionally equivalent assembly code, even at different optimization levels, is represented similarly. This novel combination allows the model to robustly understand and learn from diverse assembly code structures.
3. The paper conducts a broad range of experiments across multiple tasks and datasets, providing comprehensive evidence of the model’s effectiveness.
4. Despite its specialized focus on assembly code, Nova's hierarchical attention is compatible with standard self-attention mechanisms, allowing it to seamlessly integrate and benefit from advancements in base models and code generation models.

### Weaknesses
1. Unclear motivation for introducing several inductive bias by Hierarchical Attention Mechanism. While the added attention mask inductive bias shows promising results in the BCD task, its impact in the BCSD task is minimal. This discrepancy raises questions about why the inductive bias performs well in one task but fails to offer significant improvements in the other. Furthermore, the paper does not explore alternative attention mechanisms or provide a detailed analysis of why the chosen hierarchical structure is optimal for both tasks. The lack of ablation studies on different attention mask configurations further weakens the justification for the specific design choices.

2. Lack of Design Discussion. The paper lacks sufficient discussion on key design components like Preceding-Instruction Attention and Optimization Contrastive Learning (CL). Without Preceding-Instruction Attention, the attention design is quite similar to CodeART, raising questions about the novelty and contribution of the approach. The paper does not address how Preceding-Instruction Attention handles control flow instructions like `jmp`, which can cause the preceding instruction to be non-contiguous in the assembly code. This omission raises concerns about the robustness of the proposed attention mechanism in realistic scenarios. Additionally, the paper does not provide a clear rationale for why the chosen contrastive learning approach is superior to existing methods, such as InfoNCE or triplet loss, particularly in the context of decompilation.

3. The paper argues that preceding-instruction attention helps avoid reuse of the same register (e.g., "eax") immediately after it is used in the previous instruction. However, this motivation is questionable because it does not explain how further subsequent instructions are prevented from reusing the same register. A more straightforward solution could be achieved with inter-instruction attention, as it can attend to all previous instructions, which raises the concern of functional overlap between preceding-instruction attention and inter-instruction attention, thus potentially making the preceding-instruction attention redundant.

4. While Nova-1B and Nova-6B are much larger than CodeART, their performance gains in BCSD are limited. For example, in the k=100 case, CodeART sees a 17% improvement over JTrans with attention regularization, but Nova's improvement is only marginal, from 0.76 to 0.78 (as shown in Table 12). This suggests that adding hierarchical attention and other inductive biases provides limited benefits when scaling the model, and Tables 11-14 show that removing hierarchical attention does not lead to significant performance drops, questioning its overall necessity. And also in Table 5, the improvement brought by contrastive learning is much higher than the Hierarchical Attention.

5. In the paper's analysis of attention distribution (Figure 10), the standard attention frequently converges on the first token, a phenomenon known as attention sink [1]. This behavior is also evident in the analysis of hierarchical attention (Figure 10(c, d)), where each token strongly attends to the first token within its attention mask, specifically the [INST-(x-1)] token, which represents the summary of the previous instruction. But it is not common when human try to interpret the functionality of each individual instruction. Furthermore, the justification for the Hierarchical Attention Mechanism —which selectively uses specific attention heads to represent the best attention maps—is somewhat ad hoc and lacks a clearer rationale.  

6. The Hierarchical Attention Mechanism introduced in this paper represents a strong inductive bias; however, the underlying insights behind this inductive bias are not clearly explained. Additionally, the mechanism bears a striking resemblance to the Attention Regularization used in CodeART, with the primary difference being the absence of Preceding-Instruction Attention in CodeART. The effectiveness of this additional attention component has also been called into question earlier in the reivew, casting some doubt on its true contribution to the overall performance.

7. While the use of contrastive learning aligns well with the BCSD task—improving performance by ensuring that functionally similar binaries, even across different optimizations, are represented similarly—it's less clear how this objective enhances the model's ability in decompliation. The training goal focuses on increasing the similarity of tokens from the same function but compiled with different optimization settings. However, this doesn't seem directly aligned with the ultimate goal of recovering executable source code, which requires more precise structural and semantic understanding beyond just token similarity across optimization levels. It would be greatly appreciated if the authors could provide some intuition as to why this approach can lead to improvements in decompliation.

8. The authors introduced a novel optimization contrastive learning approach for the BCSD task, which had not been previously applied in the previous works, which commonly use the InfoNCE loss (line 220) or the triplet loss. As it is not discussed with deeper detail in the paper, it raises the question of whether these gains are substantial enough to justify the added complexity and whether this approach could be effectively generalized to improve other models in BCSD tasks.

### Questions
1. The paper argues that preceding-instruction attention helps avoid reuse of the same register (e.g., "eax") immediately after it is used in the previous instruction. However, this motivation is questionable because it does not explain how further subsequent instructions are prevented from reusing the same register. A more straightforward solution could be achieved with inter-instruction attention, as it can attend to all previous instructions, which raises the concern of functional overlap between preceding-instruction attention and inter-instruction attention, thus potentially making the preceding-instruction attention redundant.
2. While Nova-1B and Nova-6B are much larger than CodeART, their performance gains in BCSD are limited. For example, in the k=100 case, CodeART sees a 17% improvement over JTrans with attention regularization, but Nova's improvement is only marginal, from 0.76 to 0.78 (as shown in Table 12). This suggests that adding hierarchical attention and other inductive biases provides limited benefits when scaling the model, and Tables 11-14 show that removing hierarchical attention does not lead to significant performance drops, questioning its overall necessity. And also in Table 5, the improvement brought by contrastive learning is much higher than the Hierarchical Attention.
3. In the paper's analysis of attention distribution (Figure 10), the standard attention frequently converges on the first token, a phenomenon known as attention sink [1]. This behavior is also evident in the analysis of hierarchical attention (Figure 10(c, d)), where each token strongly attends to the first token within its attention mask, specifically the [INST-(x-1)] token, which represents the summary of the previous instruction. But it is not common when human try to interpret the functionality of each individual instruction. Furthermore, the justification for the Hierarchical Attention Mechanism —which selectively uses specific attention heads to represent the best attention maps—is somewhat ad hoc and lacks a clearer rationale.    
4. The Hierarchical Attention Mechanism introduced in this paper represents a strong inductive bias; however, the underlying insights behind this inductive bias are not clearly explained. Additionally, the mechanism bears a striking resemblance to the Attention Regularization used in CodeART, with the primary difference being the absence of Preceding-Instruction Attention in CodeART. The effectiveness of this additional attention component has also been called into question earlier in the reivew, casting some doubt on its true contribution to the overall performance.
5. While the use of contrastive learning aligns well with the BCSD task—improving performance by ensuring that functionally similar binaries, even across different optimizations, are represented similarly—it's less clear how this objective enhances the model's ability in decompliation. The training goal focuses on increasing the similarity of tokens from the same function but compiled with different optimization settings. However, this doesn't seem directly aligned with the ultimate goal of recovering executable source code, which requires more precise structural and semantic understanding beyond just token similarity across optimization levels. It would be greatly appreciated if the authors could provide some intuition as to why this approach can lead to improvements in decompliation.
6. The authors introduced a novel optimization contrastive learning approach for the BCSD task, which had not been previously applied in the previous works, which commonly use the InfoNCE loss (line 220) or the triplet loss. As it is not discussed with deeper detail in the paper, it raises the question of whether these gains are substantial enough to justify the added complexity and whether this approach could be effectively generalized to improve other models in BCSD tasks.

[1]: Efficient Streaming Language Models with Attention Sinks

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents Nova, a generative language model specifically designed for assembly code, addressing unique challenges posed by the low information density and diversity in assembly syntax due to compiler optimizations. Nova introduces a hierarchical attention mechanism and employs contrastive learning to improve the model's understanding of assembly semantics across diverse optimization levels. Trained on a large assembly corpus, Nova outperforms existing techniques in tasks like binary code decompilation and binary code similarity detection, showing  improvements in Pass@1 and Recall@1 rates over state-of-the-art models.

### Strengths
1. Clear Writing and Novel Application: The paper is well-written and easy to follow. The idea of applying hierarchical attention to assembly code is interesting and novel. While hierarchical attention is commonly used in NLP tasks, applying this mechanism to assembly code is, to the best of my knowledge, unprecedented.

2. Promising Results: The evaluation results are promising. Nova demonstrates substantial improvements in both decompilation accuracy and similarity detection compared to existing models, validating its approach with strong experimental evidence.

### Weaknesses
Generalizability: The model is trained exclusively on x86 assembly code, which may limit its generalizability to other assembly languages, such as ARM or MIPS.

Realism of Evaluation Settings:

(1) The decompilation prompt requires optimization level information, but it is unclear if this information is accessible in stripped binaries.

(2) For baseline models like GPT, fine-tuning with additional data isn’t necessary, raising questions about the fairness of the comparison. If GPT were given a few-shot learning setup or fine-tuned using OpenAI’s API, could it still be outperformed by the proposed approach?


Related Work: The paper omits discussion of several relevant works, which could provide a broader context for its contributions.

[1] Debin: Predicting Debug Information in Stripped Binaries. CCS 2018

[2] {DIRE}: A Neural Approach to Decompiled Identifier Renaming. ASE 2019

[3] Learning to Reverse DNNs from AI Programs Automatically. IJCAI 2022

[4] Asm2Vec: Boosting Static Representation Robustness for Binary Clone Search against Code Obfuscation and Compiler Optimization. S&P 2019

[5] Neural Network-based Graph Embedding for Cross-Platform Binary Code Similarity Detection. CCS 2017.

[6] ecompiling x86 Deep Neural Network Executables. Security 2023.

### Questions
For binary similarity detection, compilers may inline functions or eliminate them altogether. How does your approach handle such scenarios?

If additional information (e.g., execution traces) were provided to GPT, or if iterative interaction with GPT were allowed, could the proposed approach still outperform a GPT-based model?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a generative model, Nova, tailored for assembly code tasks. Nova employs a hierarchical attention mechanism and is trained using contrastive learning objectives. This paper evaluates its effectiveness on two assembly code tasks.

### Strengths
Strengths:
+ The topic is interesting and important, addressing large language model (LLM) comprehension of assembly code.
+ The paper is well-structured and easy to follow.

### Weaknesses
Weaknesses:
- Comparison may be unfair due to different fine-tuning practices.
- Evaluation of individual components is insufficient.
- Generalization assessment is lacking.
 
(1) Unfair Comparison: Nova is evaluated on two tasks, with fine-tuning applied specifically for each. However, the baseline models (such as Table 2) do not undergo the same fine-tuning for the tasks, leading to a potentially unfair comparison. The baselines, particularly the large language models, are evaluated using few-shot prompting, which is a different paradigm than fine-tuning. This difference in evaluation methodology makes it difficult to isolate the true contribution of the proposed model.
 
(2) Component Evaluation: Nova’s hierarchical self-attention mechanism consists of three components, yet the paper lacks detailed performance assessments for each part. Despite a reasonable design, their individual impact remains unexamined. The paper should provide a more granular analysis of how each component contributes to the overall performance, potentially through ablation studies or other controlled experiments. Without this, it's hard to justify the complexity of the proposed architecture.
 
(3) Contrastive Learning Objectives: The contrastive learning objectives contain two distinct components. Further evidence is necessary to substantiate the utility of each objective. Additionally, the contrastive learning approach depends on the available optimization levels. Handling unseen optimization levels at inference should be discussed. The paper should also explore the sensitivity of the contrastive learning performance to the choice of hyperparameters and the specific negative sampling strategies used. The lack of such analysis makes it difficult to assess the robustness of the approach.
 
(4) Normalization Process: In the data collection section, a normalization step is applied, but its relevance or benefit to Nova’s training is unclear. The paper should provide a clear rationale for this normalization, explaining how it improves the model's ability to learn from assembly code. Without this, the normalization process appears arbitrary.
 
(5) Results across different optimization levels should be explored—e.g., training on O0, O1, O2 and testing on O3.
 
(6) Random Sampling in BCSD Task: The BCSD task employs random sampling, yet statistical results are missing. Reporting such results would reduce the impact of randomness on performance claims. The paper should include confidence intervals or standard deviations to quantify the variability in performance due to random sampling.

### Questions
Please check my concerns in the weakness section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents Nova, a generative LLM for assembly code. To effectively learn from assembly with low information density, it uses a novel hierarchical attention mechanism which combines intra-instruction attention, preceding-instruction attention and inter-instruction attention. It further utilizes contrastive learning to better learn the semantics of assembly code from different optimization levels. The authors demonstrate the superiority of Nova over the baselines on binary code decompilation and code similarity detection tasks.

### Strengths
1. LLMs for binary code is an important topic to study
2. This work proposes new methods to train Nova based on the properties of assembly code, which is clearly motivated.
3. The proposed models show a clear improvement in binary code decompilation.

### Weaknesses
1. The comparison on code similarity detection may not be fair. For example, CodeArt uses 12 transformer blocks with 768 hidden dimensions, whose size is smaller than Nova-1B. The authors should compare Nova with the baseline under a similar size with the same pre-training data to demonstrate the superiority of Nova on code similarity detection. For the current result, we can find that compared with CodeArt, Nova actually does not show a significant improvement (e.g. both are 0.64 for Nova-1B under K=500). So it is in question whether Nova is indeed better for code similarity detection.
2. The experiments for Comparison with Techniques Handling Long Input are confusing. Specifically, it has the following problems:

a) What is "Nova’s Fine-Tuning" in Table 3? It seems Nova does not have something special in terms of fine-tuning. Does it just mean fine-tuning with hierarchical attention or also with Nova's pretraining as suggested in Line 360? 

b) What is the average token length for downstream tasks before truncation? The authors want to claim Nova is better at solving long input challenges. But I see from the Appendix that Nova uses the input length as 1024 tokens during pre-training and 2048 for fine-tuning. It may be hard to claim this length to be "long-context". Considering that assembly code should be much longer than source code and Granite-3B-Code-128K can handle 128K input tokens at most, have you tested in the benchmarks where the input context is longer, e.g. 8k/32k/128k?

3. The presentation of the paper can be improved. Specifically, a) Line 281 is unclear. The authors should clearly state that their pre-training contains two stages and the loss in Line 240 is used in the second stage. b) The ablation study should be separated into new subsections instead of mixing with Section 4.1 c) The equations are not numbered.

### Questions
1. See weakness 1,2 
2. Could you provide more details about how to construct $F$ in practice used in Functional CL?
3. The authors state that hierarchical attention is only applied to half of the attention head. Since different attention heads can learn different features, I wonder if this setup is robust to the selection of the attention heads?
4. Would the pre-trained models (Nova-1B, 6B) be public available?

### Soundness
2

### Presentation
2

### Contribution
3
