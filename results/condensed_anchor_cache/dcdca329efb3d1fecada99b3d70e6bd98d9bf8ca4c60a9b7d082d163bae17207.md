- Decision: Reject
- Scores: 3, 5, 3

## Merged Review

### Summary
The paper proposes SLiM, a one-shot LLM compression method that combines symmetric quantization, sparsity, and saliency-guided low-rank approximation, together with an efficient fine-tuning recipe. It aims to reduce memory and inference cost without retraining. Reviewers note novelty in retaining LoRA during inference and in the saliency-guided low-rank adapter, but raise concerns about unclear motivations, missing comparisons, lack of joint optimization justification, and insufficient reporting of model size and acceleration.

### Strengths
- **Novel low-rank adapter and saliency guidance**: The idea of retaining LoRA in inference-time compression is innovative; the use of saliency to guide low-rank optimization is novel (R1, R2). The low-rank adapter design itself is considered novel (R2).
- **Symmetric quantization method**: The proposed symmetric quantization minimizes quantization error without altering weights, reducing computational and memory overhead (R3).
- **Accuracy improvements**: SLiM achieves up to 5.4% improvement for 2:4 sparsity patterns and up to 5.8% with fine-tuning over state-of-the-art methods (R3). Experimental results show improved accuracy under the same pruning and quantization scheme (R2).
- **Fine-tuning efficiency**: The fine-tuning recipe significantly reduces time/resources – e.g., a 13B model fine-tuning reduced from 36 days to 14 hours on an H100 GPU (R3).
- **Inference feasibility**: The paper demonstrates the time efficiency of the approach through inference efficiency analysis (R1).

### Weaknesses
- **Unclear motivation for key equations**: The derivation of Equation 8 is unclear – while aiming to cancel compression errors, the significance function \(F\) does not seem directly related to those errors (R1). The additive noise assumption for combining quantization and pruning errors (L205-L206) lacks theoretical and experimental support; the interaction of errors could easily lead to non-additive effects (R3). The additive invertible saliency function is introduced without explanation (R2).
- **Missing comparisons**:  
  - The proposed low-rank adapter is not compared with previous low-rank adapters, making its advantage unclear (R2).  
  - No comparison with advanced joint strategies for sparse quantization, such as JSQ (R1).  
  - The paper does not consider more advanced quantization methods that outperform GPTQ (R3).  
  - Alternative significance measures (AWQ, SparseGPT) are not considered (R1).  
  - No comparison with methods like OBS that already account for weight importance (contradicting a claim in Section 3.2) (R1).
- **Incomplete experimental evaluation**:  
  - Model size statistics are missing – SLiM adds LoRA layers with rank \(r=0.1\) (significant overhead) but the extra parameter count and theoretical operations are not reported (R1).  
  - Actual acceleration performance is not reported (R2).  
  - Memory footprint of the compressed model and inference efficiency are not analyzed (R3).  
  - The evaluation metrics used in Tables 1–3 are not specified (R2).
- **Loose coupling of techniques**: The combination of quantization and pruning appears straightforward and loosely coupled; joint optimization has unanswered questions (R2). The pruning approach is not explained, and formula descriptions for \(E_S\) are missing (R1).
- **Potential merging issues**: Merging quantized sparse weights with low-rank adapters could cause overflow and disturb the 2:4 structured pruning – these problems are not addressed (R2).
- **Lack of ablation**: Why does not pruning weights in LQ-LoRA lead to significantly higher error? (R1). Why is the quantization impact not considered in the Inference Speedup discussion? (R1). Does the proposed quantization method produce zero values? (R2).
- **Presentation details**: The specific method for quantization scale determination (L199-L202) needs more detail; some background can be shortened or moved to supplementary (R3). The paper did not propose a new pruning method but claims results under a pruning-only scheme (R2, question – but note that this point appears as a question, not a weakness; however it raises a concern about attribution.)

**Note on disagreement**: One reviewer (R2, score 5) is more positive, emphasizing the novelty of the low-rank adapter and the experimental accuracy gains, while the other two reviewers (scores 3 and 3) are more critical, pointing to missing comparisons, weak theoretical justification, and insufficient evaluation. This contrast is especially visible in the assessments of novelty (R2 finds contribution higher) and the rigor of the experimental setup.