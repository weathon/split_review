- Decision: Reject
- Avg Score: 4.20
- Scores: 3, 6, 1, 5, 6
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes ResiDual, a Transformer variant that combines both Post-LN and Pre-LN residual connections (a "dual residual" architecture) through a Pre-Post-LN (PPLN) design. The central claim is that by fusing both residual paths, ResiDual simultaneously avoids gradient vanishing (the Post-LN problem) and representation collapse (the Pre-LN problem). The paper provides theoretical gradient bounds and representation-diversity proofs, and reports BLEU improvements over several baselines on IWSLT, WMT, and OPUS-100 translation benchmarks at multiple depth settings.

## Strengths

- **Clean, well-motivated architecture**: The dual-residual idea is simple and directly addresses the known complementary weaknesses of Post-LN (gradient vanishing) and Pre-LN (representation collapse). The method introduces no additional parameters over the vanilla Transformer.

- **Theoretical lower bound on gradient norm (Eq.~14)**: The paper proves that the gradient norm at each block is the *maximum* of the Post-LN and Pre-LN gradient components, establishing a formal lower bound that prevents vanishing. This is a concrete theoretical guarantee that neither single-residual variant can provide.

- **Theoretical proof that representation differences do not decay with depth (Theorem~4.2)**: The paper shows that $\mathbb{E}[|(\mathbf{x}_{k+1}-\mathbf{x}_k)_i|]$ is independent of $k$ in ResiDual, whereas it decays as $O(1/\sqrt{k})$ in Pre-LN (Corollary~4.1). This directly proves the representation-collapse advantage claimed for the architecture.

- **Analysis of Adam instability under vanishing gradients (Theorem~4.1)**: The paper computes the absolute condition number of the Adam update when gradients are zero, showing it can be as large as $\alpha\sqrt{d}/\epsilon \approx 3200$ for typical hyperparameters. This explains why gradient vanishing remains harmful even with adaptive optimizers — a genuinely novel theoretical contribution beyond prior work.

- **Consistent empirical improvements across multiple scales and depths**: On IWSLT (E12D12: 36.09 vs. 35.18 Pre-LN), WMT (E18D18: 27.65 vs. 27.30 B2T), and OPUS-100 (31.0 ALL, 18 layers, vs. 31.1 DeepNet with 100 layers), ResiDual shows systematic gains. Deep models where Post-LN fails to converge (E12D12, E18D18) train successfully.

- **Warm-up ablation (Table~5)**: The paper demonstrates ResiDual trains stably *without* learning-rate warm-up (35.76 BLEU, E6D6), while Post-LN fails entirely and Pre-LN drops by ~3 BLEU. This directly supports the claim that ResiDual inherits Pre-LN's training ease.

## Weaknesses

### Fatal
None.

### Major

- **Unclear whether IWSLT/WMT baselines were reproduced under identical conditions**: The paper states baselines are listed in Tables 1–2 without citations next to each number, and never explicitly states that these numbers were obtained by re-running each method in the same codebase with the same hyperparameters, preprocessing, and evaluation pipeline. For the OPUS-100 experiments, the authors explicitly cite external sources for some baselines (zhang2020opus100, wang2022deepnet), confirming cross-paper comparison in that case. For IWSLT and WMT, the reader cannot determine whether the gains over DeepNet, Admin, B2T, etc., are real or artifacts of different training configurations. This is fixable with a clear statement, but in the current version it undermines the central empirical claim. *(Evidence: Section 5.1 says "Our model is implemented using the FairSeq framework" but does not state that baselines were reproduced; OPUS-100 section line~413 explicitly notes "In addition to the original baselines provided by ~\citet{zhang2020opus100}, we also reproduced the 18-layer encoder and 18-layer decoder model" — the contrast in clarity is telling.)*

### Minor

- **No statistical significance or variance reporting**: All BLEU scores are single-run point estimates. Transformer training is sensitive to random seeds; differences of 0.1–0.5 BLEU can fall within noise. Several of the reported gains (e.g., 0.13 BLEU over Admin on IWSLT E6D6) are small enough that multiple runs would be needed to establish significance. *(Evidence: Tables 1–3 report only single values with no standard deviations or seed information.)*

- **OPUS-100 comparison to 100-layer DeepNet is cross-paper**: The paper notes ResiDual (18 layers, 31.0 BLEU) is "almost identical" to a 100-layer DeepNet (31.1 BLEU, cited from wang2022deepnet) and claims this "clearly demonstrates that our model can more effectively use deeper layers." This comparison is not controlled — different training pipelines, data preprocessing, and evaluation setups likely differ. While the observation is suggestive, it should be framed as a rough reference rather than evidence. *(Evidence: Line 416–417; DeepNet number cited from wang2022deepnet.)*

- **Theoretical analysis relies on strong simplifying assumptions**: The representation-collapse proof (Theorem~4.2) assumes block outputs $\mathbf{f}_k$ are i.i.d. Gaussian and independent of $\mathbf{x}_k$. In practice, $\mathbf{f}_k$ depends on $\mathbf{x}_k$ through attention and FFN computations, so the independence assumption does not hold. The paper would benefit from acknowledging this limitation and discussing whether the conclusion holds more generally. The empirical Figure~2 supports the theory, but the theoretical section should be more candid about its scope. *(Evidence: Lines 314–315: "assume $\fx[k] \sim \gaussian{0}{\sigma^2\mI}$ independently for all $k\in[N]$".)*

- **Initialization of dual residual tensor $\mathbf{x}^d$ not specified**: The paper introduces the dual residual tensor $\mathbf{x}^d$ (Eq.~4) but does not state its initialization (presumably zero). This should be stated for reproducibility. *(Evidence: Section 3.2 introduces $\mathbf{x}^d$ but never specifies its initial value.)*

### Trivial

- The $\epsilon$ parameter in the Adam description (line 353) is left as "$\epsilon=$" with no value specified.

## Nice-to-Haves

- Including a brief discussion of how the theoretical conclusions might change when the independence/Gaussian assumptions are relaxed would strengthen the theoretical contribution's credibility.
- Specifying the exact number of warm-up steps used in the "with warm-up" experiments would aid reproducibility.
- The OPUS-100 comparison to DeepNet would be more informative if the authors could provide a controlled DeepNet-18 baseline trained in the same pipeline.

## Removed Points

These points were flagged in the reviews but are removed with justification:

1. **"Figure 2 is only a placeholder / needs to be inspected"** — The figures are embedded in the original PDF submission and were stripped by the text-extraction parser. This is a tool artifact, not a paper flaw. The paper text clearly references Figure~2(a) and (b) and describes their content.
2. **"Missing related works"** — I cannot verify the existence of missing citations without external sources. The cited related work (DLCL, Admin, DeepNet, B2T, T-Fixup, ReZero) appears adequate.
3. **"Missing appendix details / proofs"** — The appendix is stripped by the parser from all papers; it exists in the original submission.
4. **Generic reproducibility nitpicks about undisclosed hyperparameters** — The paper specifies the optimizer (Adam with $\beta=(0.9, 0.98)$), learning rate scheduler (inverse sqrt with warm-up), framework (FairSeq), and preprocessing pipelines. The level of detail is standard for this field.
5. **Criticism about the gradient bound "not being rigorous"** (from harsh critic) — The lower bound in Eq.~(14) follows directly from the architecture's dual-gradient structure; it is a valid bound even if not derived from a formal optimization framework. This is standard for theoretical analysis in architecture papers.

## Novel Insights

The harsh critic and strength finder both correctly identify the paper's core contribution: a simple architectural change that provably resolves two known and opposing failure modes (gradient vanishing vs. representation collapse). A genuinely novel observation emerges from reading them together: the paper's Adam-condition-number analysis (Theorem~4.1) is the primary theoretical innovation *beyond* the existing Post-LN/Pre-LN literature, yet it is somewhat underutilized. The harsh critic notes it is "tangential" to ResiDual's gradient behavior, but the strength finder correctly identifies it as a standalone contribution explaining why warm-up is needed for Post-LN even with Adam. This suggests the paper could better integrate the Adam analysis as a direct argument for why a gradient-lower-bound architecture (ResiDual) is practically beneficial, rather than presenting it as a separate observation.

## Suggestions

1. **Clarify baseline origin**: Add an explicit sentence in Section 5.1: "All baseline methods in Tables 1–2 were re-implemented and trained in the FairSeq framework under identical hyperparameters, preprocessing, and evaluation pipelines." If some numbers are cited, put the citation next to each in the table.

2. **Add variance estimates**: Report mean and standard deviation over at least 3 random seeds for the main experiments, or at minimum for the comparison between ResiDual and Pre-Lon/Post-LN.

3. **Acknowledge theoretical limitations**: Add one sentence after Theorem~4.2 stating: "The analysis assumes independent Gaussian block outputs; in practice $\mathbf{f}_k$ depends on $\mathbf{x}_k$, but the bound provides intuition consistent with the empirical results in Figure~2."

4. **Frame the OPUS-100/DeepNet comparison more carefully**: Replace "clearly demonstrates" with "suggestively indicates" or similar, and note the comparison is across different experimental pipelines.

5. **Specify $\mathbf{x}^d$ initialization** and the $\epsilon$ value used in Adam.
