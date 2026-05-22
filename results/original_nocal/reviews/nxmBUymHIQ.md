Now I have all the information needed. Let me produce the consolidated review.

## Summary

LoLoRA proposes a hybrid fine-tuning approach that updates the LoRA A matrix with gradient-free local Hebbian rules (HPCA) during the forward pass, eliminating the need to store input activations for that adapter, while B is trained via standard backpropagation. The paper provides theoretical justification (Theorem 4.4) showing that optimal frozen A is a nonsingular transformation of the top eigenvectors of the input covariance, motivating PCA-convergent local update rules. Experiments span GLUE (RoBERTa-large), math reasoning (LLaMA-3.1-8B on MetaMathQA), multimodal fine-tuning (LLaVA-v1.5-7B), and ablations (TinyLlama-1.1B).

## Strengths

1. **Clean theoretical characterization of optimal frozen A.** Theorem 4.4 proves that under a random linear regression model, the optimal frozen A is any nonsingular linear transformation of the top *r* eigenvectors of the input covariance. Theorem 4.5 shows the asymmetry — any full-rank B is equally good. This formalizes and generalizes the empirically-motivated EVA initialization and is a genuine intellectual contribution independent of the method.

2. **Competitive result on 8B-scale math reasoning with measured memory savings.** On LLaMA-3.1-8B fine-tuned on MetaMathQA (Table 3), LoLoRA HPCA achieves 82.9% accuracy on GSM8K Platinum — matching the best baseline (LoRA-FA EVA) and outperforming standard LoRA (82.1%) — while reducing peak extra memory from 30 GB to 26 GB (13% savings). This is the paper's strongest empirical result and demonstrates that eliminating activation storage for A does not necessarily hurt end-task quality.

3. **Comprehensive ablation of local update rules and initializations.** Table 6 systematically compares five local rules (HPCA, HPCA+SVD-first, AE, HPCA without centering, SoftHebb) across ranks 2/4/8 on TinyLlama. Table 5 compares four initialization strategies for LoRA-FA. This provides a useful empirical catalog: rules that converge to the PCA subspace (HPCA, AE) all perform similarly and consistently outperform SoftHebb.

4. **Online methods avoid a separate pre-training PCA pass.** As noted in Section 5.4, HPCA-based LoLoRA (uniform) does not require a separate incremental PCA pass before training, unlike EVA which needs a data-driven initialization step. The experiments show HPCA uniform matches LoRA-FA EVA on math reasoning (Table 3) and is close on LLaVA (Table 4) and TinyLlama (Table 6).

## Weaknesses

### Major

1. **The core novelty — online local updates during fine-tuning — is not shown to be beneficial.** Theorem 4.4 justifies PCA-based initialization (EVA), but does not imply that *continuing to update* A during training helps. The experiments consistently show that LoLoRA's online updates perform essentially the same as (or slightly worse than) simply freezing A after EVA initialization (LoRA-FA EVA). Compare:
   - Table 3: LoLoRA HPCA 82.9% vs LoRA-FA EVA 82.9% (tied)
   - Table 4: LoLoRA HPCA 2.93 perplexity vs LoRA-FA EVA 2.92 (LoLoRA slightly worse)
   - Table 5 vs Table 6: LoRA-FA EVA at r=8 gets 2.536; HPCA uniform gets 2.535 (essentially tied)
   
   The paper's strongest evidence for the method (online update) collapses to "it matches the frozen version of its own initialization." This gap between the theoretical motivation and the experimental validation is significant.

2. **Missing comparison against the most directly related baseline: Local LoRA (Key et al., 2023).** The paper discusses Local LoRA in Related Work (Section 2, line 55) as a method that also uses local updates for transformer fine-tuning. No experimental comparison is provided. Since Local LoRA shares the same core motivation (local learning for LLM fine-tuning without full backpropagation), this omission is a critical gap in the evaluation.

3. **Performance on GLUE does not support the "comparable to standard LoRA" claim.** On 8 GLUE tasks (Tables 1–2), LoLoRA HPCA underperforms standard LoRA on most tasks with meaningful gaps:
   - CoLA: 66.3 vs 69.6 (LoRA better)
   - MRPC: 89.9 vs 90.9 (LoRA better)
   - MNLI: 90.3 vs 90.8 (LoRA better)
   - QQP: 90.6 vs 91.7 (LoRA better)
   
   On several other tasks (RTE, STS-B, QNLI, SST-2) the results are within noise. The paper's summary statement (§5.1) acknowledges "classical LoRA remains the strongest overall," which conflicts with the abstract's "comparable to standard LoRA" framing. A method that is clearly worse on half the tasks in the primary NLU benchmark is not "comparable."

### Minor

1. **Memory usage vs LoRA-FA is slightly higher, not lower.** In Table 4, LoLoRA uses 24.1 GB of extra memory vs LoRA-FA's 23.9 GB. The paper acknowledges this in the Conclusion ("our method introduces a small amount of extra optimizer state for the local updates, unlike standard LoRA-FA"), but the abstract's phrase "further reducing the memory required for fine-tuning" is ambiguous about the comparison point. LoLoRA does reduce memory vs standard LoRA, but the narrative that it improves over LoRA-FA on memory is not accurate.

2. **LLaVA perplexity gap.** On LLaVA-v1.5-7B (Table 4), LoLoRA HPCA achieves 2.93 perplexity, which is worse than both standard LoRA (2.90) and LoRA-FA EVA (2.92). While all methods are close, this means the method does not consistently match baselines across settings.

3. **No breakdown of local optimizer memory cost.** Algorithm 1 includes an Opt_loc with state for A, but the paper reports only peak memory without component-level breakdown. The Conclusion mentions "a small amount of extra optimizer state" without quantifying it, making it difficult to assess the memory-accuracy trade-off.

4. **"Outperforms standard LoRA-FA in two out of three experimental setups" (Conclusion) is imprecise.** On GLUE (the first setup), LoLoRA HPCA is generally *worse* than LoRA-FA uniform across most tasks (Tables 1–2). The claim is technically true only if "standard LoRA-FA" refers to LoRA-FA with EVA initialization (which LoLoRA slightly beats on GLUE), but this is not what "standard" typically means.

### Trivial

- None beyond standard presentation improvements.

## Nice-to-Haves

- **Direct "local update vs freeze after EVA" ablation.** The cleanest test of whether online adaptation helps would be: initialize both LoLoRA and LoRA-FA with EVA, then compare updating A vs freezing it. The paper does not include this experiment; Table 6 starts local rules from uniform initialization, not EVA.
- **Quantify the memory overhead of the local optimizer state** to let readers assess the memory trade-off directly.
- **Measure input covariance shift during fine-tuning** (e.g., cosine similarity of top eigenvectors before/after training) to test whether the non-stationarity that motivates online updates actually occurs.

## Removed Points

These points from the source reviews are removed with justification:

- *"The theoretical analysis does not connect to the actual experimental setting" (original framing as fatal)* — Retained as Major #1 above. The critic's framing as a completely fatal disconnect was excessive; the theory does connect to the method (it motivates the HPCA rules), but the *experimental validation* of the online update advantage is missing. Demoted from fatal to major accordingly.
- *"LoLoRA uses more GPU memory than LoRA-FA (24.1 vs 23.9 GB in Table 4). The claimed 'further reduction' over LoRA-FA is not realized—in fact, it is strictly worse."* — The abstract's "further reducing" compares to standard LoRA, not to LoRA-FA. Re-reading the abstract: "To maximize memory savings, one can freeze matrix A... but this often degrades performance. In this work, we mitigate this trade-off... This approach maintains performance comparable to standard LoRA while further reducing the memory required for fine-tuning." The comparison is against standard LoRA, where the reduction is genuine (30→26 GB, 24.6→24.1 GB). Retained as Minor #1 with corrected framing.
- *"The 'FREE_MEMORY(z)' step frees the input z, but u = Az is still stored for B's backward pass—this is standard in LoRA-FA as well."* — This is factually correct about the mechanism but does not constitute a weakness; the paper never claims to eliminate *all* activation storage, only the storage of z for A's backward pass. Both LoRA-FA and LoLoRA store u for B's backward pass, so this is standard behavior, not a flaw.
- *"The remark that 'the same local-update trick can avoid storing input activations' (Conclusion) is precisely what LoRA-FA already does."* — LoRA-FA avoids storing activations by freezing A (no gradient needed for A). LoLoRA avoids storing activations by computing local updates during the forward pass (which also don't need stored activations). The mechanism differs. LoRA-FA simply *freezes* A; LoLoRA *updates* A without stored activations. This is a meaningful difference in the method.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations primarily converge on a central issue the paper partially acknowledges: the online local updates do not outperform a good static initialization (EVA), which undercuts the claimed advantage of the method over a simpler baseline. The theoretical contribution stands independently but is not leveraged into a demonstrated practical win.

## Suggestions

1. **Reframe the contribution.** The paper's strongest contribution is the theoretical characterization (Theorem 4.4) combined with the demonstration that local PCA-convergent rules can match EVA initialization *without* requiring a separate pre-training PCA pass (Section 5.4). The headline should be about making EVA-style initialization unnecessary through online local updates, not about outperforming frozen baselines or standard LoRA.
2. **Add the missing Local LoRA baseline** to the experimental comparison to complete the evaluation.
3. **Include a "freeze after EVA" vs "continue updating after EVA" ablation** to explicitly test whether online adaptation provides any benefit beyond initialization.

## Score and Decision

The paper contains a clean theoretical result and a thorough ablation study, and it achieves competitive results on math reasoning with measurable memory savings. However, the central methodological claim — that online local updates during fine-tuning provide a meaningful advantage over freezing — is not supported by the experiments. The theory justifies initialization, not online adaptation, and the baselines (LoRA-FA EVA) match or beat the proposed method across all settings. The missing comparison against the most directly related prior work (Local LoRA) further weakens the evaluation. These issues are structural enough that the paper's headline claims are not established.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>