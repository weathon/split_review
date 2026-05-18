- Decision: Reject
- Scores: 3, 3, 5, 3

## Merged Review

### Summary
The paper proposes RAG\(^C\), a method for copyright protection of knowledge bases in retrieval-augmented generation (RAG) by embedding watermarks in chain-of-thought (CoT) reasoning instead of final outputs. The approach involves generating verification questions with target CoTs, optimizing watermark phrases under a black-box setting, and using a pairwise Wilcoxon test for ownership verification. Experiments are conducted on diverse benchmarks. Reviewer scores are 3, 3, 5, 3; Reviewer 3 is notably more positive about the approach, while the other three raise substantial concerns about clarity, practicality, robustness, and missing comparisons.

### Strengths
- The paper is well-structured and well-written, making it easy to follow (Reviewer 1).
- The approach of embedding watermarks in the CoT space is novel and provides harmless copyright protection without impacting final output correctness, preserving model utility/fidelity (Reviewers 1, 2, 3, 4).
- It highlights the necessity of copyright protection for RAG knowledge bases and, according to Reviewer 2, is the first harmless protection method.
- The ownership verification method using hypothesis testing (pairwise Wilcoxon test) is effective and minimizes false positives (Reviewer 3).
- The paper provides a solid theoretical foundation with rigorous experimental validation on benchmark datasets (Reviewer 3).
- The problem is important for the increasingly common RAG setting (Reviewer 4).
- Extensive testing shows resilience against adaptive attacks, making the approach potentially practical (Reviewer 3). (Note: other reviewers question the robustness – see Weaknesses.)

### Weaknesses
- **Motivation and scenario clarity**: The motivation is unclear, and the security scenario lacks practical detail. Reviewers request elaboration on why avoiding incorrect answers during verification is necessary (Reviewer 1) and why the defender would release the protected knowledge base rather than an attacker stealing it (Reviewer 2). Reviewer 4 questions why simply adding fictitious watermark entries would not satisfy requirements and whether adversaries could remove all added CoT elaborations.
- **Method description lacks clarity**: Figure 1 is not adequately explained; the optimization of the Watermark Phrase via Equations (2) and (3) needs more detail (Reviewer 1). Equation (4) appears inconsistent with its textual description (Reviewer 1). Definition 1 does not explicitly indicate which variable represents the degree of harmfulness (Reviewer 2). The paper contains typos, e.g., “watermark phase(s)” and “retriver” (Reviewer 2).
- **Complexity vs. simpler alternatives**: Reviewer 2 argues the method is unnecessarily complex; prior poisoning-based methods could simply use objective or unusual questions rarely asked and implant unique answers in the knowledge base without affecting final outputs.
- **Robustness concerns**: Under adaptive attacks, accuracy drops to >0.52 and >0.38 (Table 7). Since ownership verification is a binary problem (random guessing 50 %), these results raise questions about effectiveness (Reviewer 2). Missing robustness against insertion/deletion/substitution/paraphrasing attacks on retrieved entries or generated responses (Reviewer 4).
- **Threat model is problematic**: The assumption that “adversaries intend to ‘steal’ and misuse the protected knowledge base released by the defender” may be unrealistic; a strong attacker could steal the entire knowledge base without the defender releasing it (Reviewer 2).
- **Missing comparisons with related methods**:
  - No comparison with membership inference attacks (MIAs) adapted for RAG (e.g., “Is My Data in Your Retrieval Database?” Anderson et al., 2024), which are harmless and do not modify outputs (Reviewer 2).
  - No comparison with direct text watermarking methods applicable to RAG, e.g., the “Waterfall” framework (Lau et al.) for robust and scalable text watermarking (Reviewer 4).
- **Dependency on suspicious LLM’s retriever**: The paper does not clarify whether the defender needs to know the suspicious LLM’s retriever. The evaluation considers only certain retrievers; the effect of other retrievers is unexplored (Reviewer 2).
- **High-level contribution obscured by low-level details**: The focus on intricate details may overwhelm readers, making it difficult to grasp the overall impact (Reviewer 3).
- **Risk of generating incorrect CoTs**: Modifying CoT reasoning can produce flawed or inconsistent CoTs, which is as undesirable as incorrect outputs. The paper does not adequately explain how inaccuracies in CoTs are prevented from propagating to final answers (Reviewer 3).
- **Unclear scope of detection**: It is not clear whether the watermarking approach detects unauthorized use across different scenarios (pretraining, fine-tuning, as well as RAG) (Reviewer 3).
- **Missing experimental evaluations**:
  - No evaluation of cases where inputs without the watermark phrase still generate the target CoT text (Reviewer 1).
  - No analysis of TPR-FPR or AUROC for the verification process, which are important metrics for watermark verification (Reviewer 4).
  - No evaluation on benchmarks beyond factual Q&A that involve reasoning, where CoT might affect performance (Reviewer 4).
- **Harmful Degree metric**: It is unclear whether it is evaluated over verification questions only or the entire database. If only over verification questions, what are the disadvantages of directly inserting new fictitious entries as backdoor watermarks? (Reviewer 4).