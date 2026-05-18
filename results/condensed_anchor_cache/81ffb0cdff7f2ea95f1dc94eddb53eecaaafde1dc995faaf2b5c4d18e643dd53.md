- Decision: Accept
- Scores: 6, 6, 6, 8

## Merged Review

### Summary

The paper introduces Alchemy, a symbolic mutation framework that expands Lean’s Mathlib from ~110k theorems to over 6M by applying rewrite (rw) and apply tactics to existing theorems – replacing term, hypothesis, or goal with an equivalent or antecedent – and then augmenting proofs with a `have` statement to reverse the mutation. After continual pretraining on the augmented corpus and supervised finetuning on (state, tactic) pairs, models show absolute pass-rate improvements: up to ~5% on the LeanDojo benchmark (2.69% on random split, 4.22% on novel_premises with DeepSeek Coder) and 2.5% on the out-of-distribution miniF2F benchmark (reaching 36.48%). Reviewers agree on the novel direction, clear presentation, and the importance of addressing data scarcity, but they differ on the significance of the gains and the generality of the method. Reviewer4 (rating 8) is notably more positive than the other three reviewers (ratings 6), praising the experimental validation on the novel_premises split and the novelty of the approach, while still noting diversity and conversion issues.

### Strengths

- **Originality**: The idea of synthesizing new theorem statements through rewrites and applies from an existing library is new (Reviewers 1, 2, 4). It is a good attempt to augment human-written formal data, though conceptually similar to earlier “from scratch” symbolic generators (Reviewer 1).
- **Technical correctness and robustness**: Symbolic mutations guarantee the generated theorems are correct by construction (Reviewer 3). The extraction and modification of Lean data is nontrivial and implemented soundly (Reviewer 2).
- **Catering to a key problem**: Data scarcity is widely considered a core issue in neural theorem proving; Alchemy produces an order-of-magnitude larger corpus (110k → 6M) directly in the symbolic space, addressing a clear bottleneck (Reviewers 2, 3).
- **Clear exposition**: The paper is well‑written, with a clear motivation and easy‑to‑follow description of the mutation methodology (Reviewers 1, 2, 4).
- **Experimental support**: The consistent gains (positive differences across nearly all splits and backbones) validate the utility of the generated data (Reviewer 1, 4). Reviewer 4 (the most positive) particularly stresses the >4% improvement on the novel_premises split, demonstrating effectiveness on harder cases.
- **Self‑acknowledgment of limitations**: The paper transparently discusses the computational cost and the limited diversity of generated theorems (Reviewer 3).

### Weaknesses

- **Marginal improvement compared to the scale of data and to SOTA**:  
  Despite generating 6M new theorems, absolute gains are small – 2.5% on miniF2F (36.48%) and 0.62‑4.7% on mathlib splits (Reviewer 1, 3). Relative improvement is not compelling, and the performance is far below SOTA models (e.g., DeepSeekProver, InternLM Prover >60% on miniF2F) (Reviewer 3). This suggests the generated theorems may be too similar to the originals or lack genuine mathematical novelty (Reviewer 1, 3, 4). Even Reviewer 4, who is overall positive, notes that the diversity problem “may result in a lower improvement on the harder benchmark miniF2F.”

- **Confounded evaluation setup (baselines, training‑test overlap, gradient steps)**:
  1. The baseline only does (state, tactic) finetuning on Mathlib, whereas the proposed method also includes continual pretraining. An ablation on “continual pretraining on Mathlib without augmentation, then finetuning” is missing (Reviewer 2).
  2. Train‑test overlap is a concern:  
     – The continued pretraining dataset may include theorems from the LeanDojo test set or premises used in the novel_premises split. No details are given on how overlap was prevented (Reviewer 2, 3).  
     – The data augmentation may use premises that are considered “novel” in the novel_premises split, thus undermining the purpose of that split (Reviewer 2).
  3. Because finetuning is run for a fixed number of epochs, the augmented dataset yields more gradient updates than the baseline; results may change if the baseline is trained for the same number of steps (Reviewer 2).

- **High computational cost**:  
  The rw mutation took 14 days on 512 CPU nodes (or 4,096 cores, Reviewer 3) and the apply mutation 7 days on 2,048 cores (Reviewer 2, 3). This limits reproducibility and practical scalability, and no substantial innovations to reduce cost are provided (Reviewer 2).

- **Limited depth and diversity of generated theorems**:  
  Only one‑step rewrites and applies are used; proofs are augmented merely by reversing the mutation via a single `have` statement (Reviewer 2). More steps (e.g., >1 rewrite) or advanced tactics (simp, linarith) are not explored, which may restrict the variety of new concepts (Reviewer 2, 3). Reviewer 4 suggests showing depth statistics to evaluate diversity, and notes the method “mainly expands existing theorem by combining other theorems.”  

- **Lack of quality or diversity metrics for the synthetic corpus**:  
  Beyond correctness by construction, there is no analysis of mathematical significance, redundancy, or coverage of the 6M generated theorems. It is unclear whether they reinforce existing knowledge or genuinely broaden the model’s understanding (Reviewer 1, 3). Reviewer 3 specifically asks for metrics that assess the “mathematical value or diversity” of the generated theorems.

- **Narrow applicability**:  
  The approach relies on a rich library of existing equivalences and antecedent theorems; it is not clear how it could transfer to domains without such well‑developed libraries (Reviewer 1).

- **Unexplained conversion ratio and generation failures**:  
  Only 37% of the generated candidate theorems pass the Lean type‑checker. Since the mutations are symbolically sound, a much higher ratio would be expected; the paper does not explain the failures (Reviewer 1, 4). This is a concrete concern about the quality of the generation pipeline.

- **Unclear why each technique helps on the unseen_premises split**:  
  No intuition or analysis is given for why the rw or apply mutations specifically benefit the harder out‑of‑domain setting (Reviewer 2).

- **Questions that double as missing ablations or analyses**:  
  - Which specific theorems in miniF2F were newly proved by Alchemy‑trained models? (Reviewer 3)  
  - Can the synthesis process be optimized to reduce runtime? (Reviewer 3)  
  - How is data contamination handled during evaluation/generation? (Reviewer 3)  
  - Is a framework like Alchemy the correct direction for tackling IMO‑level problems? (Reviewer 1)