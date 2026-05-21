---
job_id: b887cc5c-8eb4-403d-a07e-3a0293d6f21b
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: abgW71sKIt.pdf
paper: Rethinking Output Alignment for 1-Bit Post-Training Quantization of Large Language Models
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on post-training quantization for large language models, which fits general machine learning, representation learning for language, and efficient ML systems.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, methodological development, experiments with quantitative results, ablations, and conclusion; while there are important technical and empirical weaknesses, they do not rise to the level of a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions to reviewers, or other suspicious content aimed at automated review systems in the provided manuscript text and figures.

# Expected Review Outcome:
## Summary
This paper studies why naive output alignment can fail in 1-bit post-training quantization of large language models, especially under layer-wise calibration. The authors argue that accumulated activation mismatch and disruption of token interactions make standard activation-conditioned output matching unreliable, and they propose a selective output-alignment strategy that matches quantized outputs to full-precision targets while applying this only to the final fully connected layer in each block. The method also introduces an Attention Matrix Preservation (AMP) mechanism intended to preserve token similarity structure during quantization, and experiments on OPT and LLaMA families show improvements over prior 1-bit PTQ baselines such as PB-LLM, BiLLM, ARB-RC, and ARB-X.

## Strengths
The paper tackles a meaningful problem. Extreme 1-bit PTQ for LLMs is still very brittle, and understanding why output matching underperforms weight matching in this regime is a useful question rather than a cosmetic one.

I appreciated that the paper does not simply present a new recipe, but first tries to diagnose failure modes of prior output-matching approaches. In particular, **Figure 1** is a useful piece of evidence for the paper’s central claim: improving a layer-level output objective does not automatically improve block-level reconstruction. The figure makes the intended point concretely, namely that several layers in LLaMA-2-7B incur lower block loss with ARB than with ARB-X even when ARB-X is optimizing an ostensibly more direct objective. That diagnostic framing is one of the better aspects of the paper.

The accumulated-error analysis around **Figure 2** is also directionally helpful. The upper plots visually support the paper’s claim that activation-conditioned similarity can remain relatively favorable while the discrepancy to the full-precision target still grows with depth. Even though I have reservations about the exact interpretation, the figure does provide an intuitive motivation for replacing $\|\widehat{X}W-\widehat{X}\widehat{W}\|$ with $\|XW-\widehat{X}\widehat{W}\|$.

Empirically, the method appears consistently better than ARB-X and usually slightly better than ARB-RC in the main tables. In **Table 1**, for OPT models, the gains over ARB-X are clear and consistent across C4, WikiText2, PTB, and average QA accuracy. The comparison against ARB-RC is smaller, but still often favorable, for example OPT-2.7B and OPT-30B. In **Table 2**, the method also improves over ARB-X across all listed LLaMA settings and often edges out ARB-RC on C4 and WikiText2. This consistency across model families is a real positive.

The AMP ablation in **Table 3** is one of the more convincing experimental components. The gap on LLaMA-2-7B is large, suggesting the masking mechanism is not merely an implementation detail. The appendix **Figure 3** is aligned with that story and shows that AMP tends to reduce attention-score reconstruction error across layers.

The paper also has a practically appealing design goal. The method remains a PTQ procedure, avoids retraining, and according to the appendix does not add inference-time parameters or runtime overhead relative to the underlying binary model family.

## Weaknesses
I think the paper is promising, but the current version falls short of ICLR standards because several core claims are only partially supported, and the mathematical presentation is not yet reliable enough. Below are the main issues.

1. **The mathematical derivation is inconsistent in several places, and this matters because the method is presented as closed-form optimization.**  
   The most serious issue is that the notation around the Gram matrices and cross-covariance matrices is not handled consistently across **Equations (2) to (8)** and Appendix B. In **Equation (2)** on **Page 5**, the paper writes
   \[
   \mathcal{L}(X,l)=\|\widehat{X}W-\widehat{X}\widehat{W}\|_F^2=\operatorname{Tr}[(W-\widehat{W})^\top S (W-\widehat{W})],
   \]
   and then states “where $\widehat{S}=\widehat{X}^\top \widehat{X}$ is the Gram matrix of the quantized activations.” This is internally inconsistent, because the trace form should involve $\widehat{X}^\top \widehat{X}$, not a generic $S$, unless $S$ is explicitly defined as $\widehat{S}$. The paper does not do this cleanly.  
   A similar issue appears in **Equation (5)**, where
   \[
   \alpha_c^*=\frac{\operatorname{Diag}(B^\top \operatorname{diag}(\alpha_r)SW)}{\operatorname{Diag}(B^\top \operatorname{diag}(\alpha_r)\widehat{S}\operatorname{diag}(\alpha_r)B)},
   \]
   with $S=\widehat{X}^\top X$. This is now a cross-term, not the same matrix as the one used above. Then in **Equation (6)**, the paper defines
   \[
   N=\operatorname{diag}(\alpha_r)S\operatorname{diag}(\alpha_r),
   \]
   which would only be symmetric if $S$ were symmetric, but here $S=\widehat{X}^\top X$ is generally not symmetric. Yet the later row-wise binary update seems to rely on a quadratic form that usually assumes a symmetric interaction matrix. This is not a small typo. If $N$ is not symmetric, the row-wise discrete update formula and its claimed optimality become much harder to justify.  
   The appendix compounds the confusion. In **Appendix B, Eq. (16)**, the expansion uses $\widehat{S}$ in the first term and $S$ in the cross-term, but the underbrace labels are garbled and in at least one place appear incorrect. The derivation for $B$ also flips between symbols in a way that makes it difficult to verify what objective is actually being optimized. Because the paper’s method depends on these closed forms, the lack of notational hygiene directly weakens confidence in correctness.

2. **The AMP formulation is under-justified and, as written, mathematically odd.**  
   In **Section 4.1**, the paper defines
   \[
   \max \mathcal{L}_{AMP}=\|(\widehat{X}\widehat{W}\widehat{W}^\top \widehat{X}^\top)\odot(XWW^\top X^\top)\|,
   \]
   then rewrites it as a trace product in **Equation (9)**. Several problems arise here. First, the norm on the Hadamard product is unspecified, so the objective is not fully defined. Second, the passage from the Hadamard-product norm to the trace expression is not explained and is not generally equivalent without further assumptions. Third, if the intent is to preserve token similarity matrices, a more direct objective would typically compare them with a discrepancy such as Frobenius norm or cosine loss, rather than maximizing an unnormalized correlation surrogate.  
   The masking rule in **Equation (10)** is also hard to interpret. The paper says it assigns an AMP mask as the sign of the gradient with respect to each parameter, but the resulting masks are used in **Equation (11)** as if they were binary selectors between old and newly refined parameters:
   \[
   \alpha_r=\alpha_r*(1-M^r)+\alpha_r^* * M^r,
   \]
   and similarly for $\alpha_c$ and $B$. However, the mask is defined using `sign`, which naturally yields values in $\{-1,0,1\}$, not in $\{0,1\}$. If $M^r=-1$, the update becomes $\alpha_r(1-(-1))+\alpha_r^*(-1)=2\alpha_r-\alpha_r^*$, which is clearly not a selector. So either the implementation uses a thresholded $\{0,1\}$ mask and the equation is wrong, or the stated update is not what is actually run. This is a concrete, important issue, not a stylistic one.

3. **The core claim that selective application to the final FC layer is the right design is only weakly established in the main paper.**  
   The main text says in **Section 4.2** that output alignment is restricted to “only the last fully connected layer of each block, since it has the most direct impact on the block loss.” But this design choice is not sufficiently justified in the main paper itself. The evidence that this is the best layer choice appears only in the appendix (**Table 5**), whereas in the main paper it is presented almost as a principle. Even in the appendix, the evidence is limited to only two models, one LLaMA and one OPT, with modest margins on OPT and larger margins on LLaMA.  
   This matters because selective application is one of the main algorithmic contributions. If the method’s effectiveness depends strongly on a hand-picked layer choice, then the paper should either establish a clearer criterion for deciding where output alignment helps, or at least show that the choice is robust across more architectures and scales. Right now, the method is part insight and part heuristic.

4. **The empirical gains over the strongest baseline are relatively modest, and the evaluation does not fully support the strength of the claims.**  
   In **Table 1**, the gains over **ARB-RC** are small in many entries. For example, on OPT-13B C4, the improvement is from 15.07 to 14.71; on WikiText2 from 13.10 to 12.84; on PTB from 19.09 to 18.85; and AveQA from 55.01 to 55.06. Similar patterns appear for larger models. In **Table 2**, on LLaMA-3-8B the gains over ARB-RC are also small on C4 and WikiText2, and on PTB the margin is larger but the absolute perplexities are extremely high.  
   The paper is aware of this issue, because on **Page 8** it states that the perplexities can become so large that the metric “cannot provide a meaningful evaluation.” But that admission undercuts some of the headline empirical narrative. If PTB is effectively saturated and unusable in some settings, then these rows should not be emphasized in support of superiority. More broadly, the method is clearly stronger than ARB-X, but the case that it materially advances the state of the art beyond ARB-RC is more incremental than the paper’s framing suggests.

5. **Important experimental details that affect scientific confidence are missing or pushed out of the main paper.**  
   For a PTQ paper, calibration protocol details matter a lot, yet the main text omits several specifics. The number of calibration samples, whether calibration data are fixed across all methods, the exact zero-shot evaluation pipeline, whether hyperparameters were tuned per architecture, and how many optimization iterations are used are not clearly specified in the main paper. Some of this is partially clarified in the appendix, but the main paper should stand on its own enough to assess fairness and reproducibility.  
   This is especially important because the method includes an extra hyperparameter $k$ and selective layer choices. The appendix **Table 8** shows some sensitivity to $k$, particularly for LLaMA-2-7B, but the main paper barely mentions this. Without clearer protocol disclosure, it is difficult to judge whether the reported gains reflect a robust method or careful tuning relative to baselines.

6. **The attention-preservation story is plausible, but the evidence is still somewhat indirect and architecture-specific.**  
   The argument in **Section 3.3** treats token similarity matrices as a proxy for attention behavior. That is defensible as a heuristic, but it is not the same as preserving actual attention logits or attention probabilities. The manuscript repeatedly talks about “attention mask” degradation, yet what is actually measured in **Figure 2** and **Figure 3** is similarity drift in output representations or reconstructed attention-score surrogates. The terminology overstates what has been shown.  
   Moreover, **Table 3** indicates AMP has a dramatic effect on LLaMA-2-7B but only a tiny effect on OPT-6.7B. That asymmetry is interesting, but the paper’s explanation, tied to RMSNorm versus LayerNorm on **Page 9**, is only a hypothesis. Since AMP is a main contribution, it would be much stronger to include direct evidence for this architecture-dependent claim, rather than a post hoc speculation.

7. **Some figures support the paper’s intuition, but they are not quantitative enough to fully validate the proposed decisions.**  
   **Figure 1** shows many layers where ARB beats ARB-X in block-level loss, but the figure is essentially a colored bar sequence over layer indices. It does not report the magnitude of the differences, the block identities, or uncertainty across data samples. Since one of the central claims is that naive layer-wise output alignment can harm block-level quality, magnitude matters. A tiny difference and a large difference are treated identically in the current visualization.  
   Similarly, **Figure 2** qualitatively shows divergence trends, but the paper uses this to motivate a rather specific change in objective and an AMP mechanism. A more convincing analysis would directly compare ARB-X, the proposed output-error objective without AMP, and the full method on the same curves. As is, the figure diagnoses ARB-X but does not by itself validate that the proposed remedy is the right one.

8. **The paper’s novelty relative to existing compensation/refinement-style 1-bit PTQ methods is somewhat narrower than advertised.**  
   The method builds directly on ARB-RC parameterization and alternation, changes the target from activation-conditioned output to full-precision output, adds a mask-based attention heuristic, and applies the objective selectively. That can still be publishable, but it is more of a focused refinement of an existing family than a substantial methodological departure.  
   This matters for overall contribution because the empirical gains over ARB-RC are often small, and the paper does not convincingly establish that the new pieces generalize beyond the specific setup studied here.

9. **Presentation quality in the method section is uneven and occasionally sloppy enough to obstruct verification.**  
   There are multiple wording and notation issues: on **Page 6**, Equation (4) writes $\mathcal{L}(X,L)$ while the earlier equations are indexed by layer $l$; on **Page 17**, Algorithm 1 uses duplicate arguments “procedure OUR-RC(W, S, S, T, k)” with both Gram matrices labeled $S$; lines 3 and 4 again define both as $X^\top X$; and lines 16 to 21 in the algorithm appear duplicated or corrupted. Those are not fatal on their own, but together they give the impression that the algorithm and derivations were not sufficiently cleaned up. For a paper whose main selling point is a supposedly efficient closed-form optimization procedure, that hurts credibility.

## Questions
1. In **Equations (10) and (11)**, is the AMP mask actually binary in implementation, i.e. in $\{0,1\}$, or is it truly the sign in $\{-1,0,1\}$? Please clarify the exact update rule used in code. If it is thresholded to binary, please rewrite the equations accordingly. If not, please explain how negative masks avoid producing extrapolation updates such as $2\alpha-\alpha^*$.

2. Please provide a clean derivation for **Equations (5) to (8)** with consistent definitions of
   \[
   \widehat{S}=\widehat{X}^\top \widehat{X}, \quad S_{xx}=X^\top X, \quad S_{\widehat{x}x}=\widehat{X}^\top X,
   \]
   or similar notation. In particular, which matrix enters the quadratic term for the $B$ update, and how is row-wise optimality justified if that matrix is not symmetric?

3. Can the authors provide a main-paper ablation, not only an appendix one, comparing output alignment applied to different layer types within a block, or alternatively a principled criterion for selecting the final FC layer? This would increase confidence that the selective design is not simply a tuned heuristic.

4. The paper argues that AMP preserves attention behavior, but the current evidence is mostly based on token similarity proxies. Could the authors provide direct measurements on attention logits or attention probability matrices, at least for a representative model such as LLaMA-2-7B? That would materially strengthen the causal interpretation.

5. Since the gains over **ARB-RC** are often modest in **Tables 1 and 2**, could the authors report variance across calibration subsets or random seeds? If the improvements are stable, that would make the contribution more convincing. Right now, many margins are small enough that robustness matters.

6. Please clarify all evaluation protocol details in the main paper: calibration set size, number of optimization iterations, whether $k$ is fixed across all models, whether any architecture-specific tuning was used, and the exact zero-shot evaluation setup. These details are important for assessing fairness.

7. In **Figure 1**, can the authors quantify the block-loss differences rather than only indicating which method wins by color? A version with magnitudes or summary statistics would make the claim much stronger.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the paper as written. The work studies model compression and deployment efficiency, and I did not identify dataset, privacy, or human-subject issues in the main paper that would require separate ethics review.

## Soundness Rating
2: fair. The paper has a sensible motivation and nontrivial experiments, but the mathematical formulation and algorithm description contain enough inconsistencies that I cannot fully trust the claimed closed-form optimization without clarification.

## Presentation Rating
2: fair. The paper is readable at a high level, and the motivation is understandable, but notation, equations, and algorithm descriptions are not polished enough for a method paper whose contribution depends on those details.

## Contribution Rating
2: fair. There is a useful empirical refinement here, especially against ARB-X, but the gains over the strongest baseline are often small and the methodological advance feels more incremental than the paper’s framing suggests.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper asks a worthwhile question and presents some useful analysis, but the current version has too many unresolved issues in the math and too limited a validation of the key design choices for me to support acceptance with confidence.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I carefully checked the main technical formulations and the empirical tables, but some ambiguities in the paper make full verification difficult.