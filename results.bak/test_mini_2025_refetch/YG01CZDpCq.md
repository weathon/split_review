Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes APPLe (Adaptive Prompt Prototype Learning), a method that uses multiple GPT-3-generated descriptive prompts per class as prototypes for CLIP-based classification, with an adaptive attention mechanism to weight prototypes and a prototype decorrelation loss. The method has a training-free version (APPLe*) that simply uses the multiple prompts without fine-tuning, and a training-based version that fine-tunes the prompt embeddings and attention matrix on base classes. Experiments across 11 datasets and multiple settings (base-to-new generalization, few-shot learning, domain generalization, image retrieval) show consistent improvements over existing prompt-tuning baselines like CoOp, MaPLe, and PLOT.

## Strengths

1. **Clear and well-motivated idea with strong illustrative example.** The paper identifies a genuine limitation of single-prompt methods (e.g., "a photo of an apple pie" fails to cover the visual variance within a category) and provides a concrete running example (Figure 1) showing how different descriptive prompts match different images of the same class. The apple pie example effectively communicates why multiple prototypes help.

2. **Comprehensive evaluation across 11 datasets and four settings.** The paper evaluates on base-to-new generalization (Table 1), few-shot learning (Figure 3), domain generalization (Table 2), and image retrieval (Table 4). This breadth is comparable to or exceeds that of top prompt-tuning papers (CoOp, MaPLe) and demonstrates consistent improvements — e.g., +2.79% harmonic mean over MaPLe on 11 datasets, with particularly large gains on challenging datasets like FGVC Aircraft (+7.38% HM) and DTD (+7.29% HM).

3. **Training-free version (APPLe*) provides a strong baseline and cleanly demonstrates the value of multiple prompt prototypes.** APPLe* (+3.83% new-class average over zero-shot CLIP) shows that simply using diverse GPT-3 prompts with the proposed inference formulation outperforms all training-based single-prompt methods on new classes. This is a genuine empirical finding.

4. **Figure 4 provides clean evidence that multiple prototypes mitigate overfitting.** When fine-tuning with a single prototype, new-class accuracy drops below zero-shot CLIP. With more than 3 prototypes, it rises above. This controlled experiment directly validates the paper's core motivation.

## Weaknesses

### Major

1. **Ablation study shows the learning components contribute negligibly to new-class generalization — the paper's central claim is not supported by its own data.** 

   From Table 3 (ImageNet):
   - Training-free multiple prototypes with attention: **New = 71.88**
   - Full model (training + attention + both losses): **New = 72.12**
   - **Gain from all learning components: +0.24% on new classes**, compared to +3.49% on base classes.

   The paper's title, abstract, and framing emphasize generalization to unseen classes ("Don't Paint Everyone with the Same Brush," improved new-class performance). Yet the ablation data show that the training, attention mechanism, and losses almost exclusively improve base-class accuracy while providing negligible benefit for unseen classes. The +3.66% new-class improvement over MaPLe in Table 1 is driven primarily by the use of multiple GPT-3 prompts (which the training-free APPLe* already has), not by the learned components that constitute the paper's claimed technical contribution.

   This is a significant gap between narrative and evidence. The paper would be more honest if it reframed the contribution as improving base-class accuracy while maintaining generalization, or focused primarily on the training-free multiple-prototype approach.

2. **Missing direct comparison to the most relevant baselines — GPT-3-prompt-only CLIP with equal logit averaging.**

   The paper acknowledges in Section 2 that Menon & Vondrick (2022) and Pratt et al. (2023) also use GPT-3-generated prompts for zero-shot CLIP classification, but neither is included as a baseline in any experiment. The training-free APPLe* uses GPT-3 prompts with a specific inference formulation (weighted averaging + closest-prototype), but the paper does not isolate whether its inference design adds value over simple logit averaging across the same set of prompts. Without this comparison, the reader cannot assess whether the *adaptive attention* or the *inference formulation* provides the improvement, or whether the improvement is simply due to using multiple descriptive prompts — a phenomenon already documented in prior work.

### Minor

3. **"Adaptive attention" is a misleading name for what is learned.** The attention matrix W ∈ ℝ^{C×K} is a set of per-class, per-prototype weights that are learned globally and applied uniformly at inference — it is *not* input-adaptive or per-sample. The term "adaptive" typically implies conditioning on the input, which this mechanism does not do. The paper should clarify this naming choice.

4. **The decorrelation loss (Eq. 4) is simply an L2 penalty on the per-prototype cosine similarities.** Since ∥cos*∥₂ for a scalar reduces to |cos*|, this is an L1 penalty on the logit magnitudes within a class. The paper describes it as suppressing "co-occurrence of multiple prototypes," but the mathematical form is a standard sparsity regularizer. The description overclaims the novelty of this loss.

5. **Fixed hyperparameters λ₁=λ₂=3 across all datasets without sensitivity analysis.** The paper states these values are "consistently set to 3 for all experiments in all datasets" without ablation or sensitivity study to justify this choice. Given that the objective combines three losses, the relative weighting is consequential.

6. **No confidence intervals or statistical significance reported.** Given that many few-shot gains are small (e.g., 0.12% at 16 shots) and the critical ablation differences are tiny (+0.24% on new classes), error bars would help assess whether these differences are meaningful or within noise.

### Trivial

7. **Typo in Section 5:** "PLOT respectively gained 1.86%, 1.0%, 0.50%, 0.51%, and 0.12% performance boost over PLOT" — should read "APPLe respectively gained... over PLOT."

8. **Ablation table formatting is hard to read** due to repeated checkmarks without clear row separation.

## Nice-to-Haves

- A comparison to Menon & Vondrick (2022) or Pratt et al. (2023) using the same set of GPT-3 prompts with simple logit averaging would cleanly isolate the contribution of the paper's inference mechanism.
- A sensitivity analysis of λ₁ and λ₂ would strengthen the training setup.
- The prompt generation details (GPT-3 prompt template, temperature, filtering) should be provided (likely in the missing appendix).

## Removed Points

- **Criticism that the paper cannot demonstrate its learned components add value over a "simple, known baseline":** This is partially kept as Major weakness #2 but downgraded from "fatal" because the ablation (Table 3) already provides a training vs. no-training comparison, even if it doesn't include the specific Menon & Vondrick baseline. The key issue (Major #1 — that the learning components barely improve new classes) is independently verifiable from the paper's own data.

- **Criticism about parameter count fairness vs MaPLe:** The paper does not claim parameter efficiency, and the method's parameter count is an expected consequence of using multiple prototypes. This is not a meaningful weakness without evidence that the extra parameters cause overfitting or that a comparable increase would benefit MaPLe similarly.

- **Criticism about missing training details (learning rate, optimizer, epochs):** These are standard details deferred to the appendix, which is removed by the parser. Not a weakness of the paper itself.

- **Strength Finder claim that "ablation study is well-designed":** Overruled by weakness evidence. The ablation's format is messy, and the critical finding (learning components add +0.24% on new classes) undermines rather than supports the paper's claims. Moved here to avoid presenting misleading strengths.

- **Strength Finder claim that "consistent superiority in few-shot learning at very low data regimes":** Partially retained but weakened — the gains at 16 shots are 0.12%, and no confidence intervals are provided. The strength is real at 1-2 shots but overstated by the Strength Finder.

## Novel Insights

Beyond the paper's own contributions, a notable synthesis emerges: the paper inadvertently demonstrates that for CLIP-based classification, *the prompt content matters far more than prompt learning*. The training-free APPLe* (using GPT-3 prompts without any parameter updates) outperforms all training-based single-prompt methods on new classes. This suggests that the field's focus on learning continuous prompt vectors (CoOp, MaPLe, etc.) may be addressing the wrong bottleneck — the real headroom may lie in richer prompt design rather than prompt optimization. The paper's evidence for its specific learning components (adaptive attention, decorrelation loss) is weak, but the broader finding that multiple descriptive prompts dramatically improve CLIP's generalization is robust and practically valuable.

## Suggestions

1. **Reframe the contribution honestly.** The paper should clearly separate two contributions: (a) the finding that multiple GPT-3 prompt prototypes significantly improve CLIP's zero-shot performance (well-supported), and (b) the learning components (attention, losses) that mainly improve base-class accuracy while preserving generalization (modestly supported). The title and abstract should reflect this.

2. **Add a direct comparison to GPT-3 prompt averaging.** Use the same set of K prompts with uniform averaging as a baseline. This takes one line in a table and would resolve the most serious methodological concern.

3. **Emphasize the critical role of ℓ_max and ℓ_dec.** The ablation shows that training + attention without these losses collapses new-class accuracy to 63.57 — the losses are clearly preventing severe overfitting. This is a more compelling story than what the paper currently tells.

4. **Rename "adaptive attention"** to "learned prototype weighting" or similar, since the weights are not input-adaptive.

5. **Add confidence intervals** for the key comparisons, especially the ablation results where the new-class differences are small.

## Score and Decision

**Initial bracket (Round 1):** 5.0 – 7.0 (based on calibration anchors in the middle band: CARPRT at 5.75/Rejected, DeMul at 6.4/Accepted, FuDD at 6.0/Accepted).

**Narrowing (Round 2):**
- **NDLmZZWATc.md (DeMul, avg 6.4, Accepted Poster):** Most comparable paper — multi-prompt + LLM distillation. Also has marginal gain from its weighting component (+0.1%). Our paper has broader evaluation scope but a more significant gap between claims and evidence.
- **g6rZtxaXRm.md (FuDD, avg 6.0, Accepted Poster):** LLM-generated descriptions for CLIP. Clean, well-executed work with minor incrementalism concerns. Our paper has a stronger technical contribution but weaker evidence tying the contribution to the claimed benefit.
- **fRpAUgKJhT.md (CARPRT, avg 5.75, Rejected):** Prompt reweighting with marginal gains. Rejected. Our paper has larger absolute gains and a more novel approach, but shares the pattern of overclaiming relative to evidence.
- **eE2PXlNydB.md (ClusPro, avg 6.0, Accepted Poster):** Clustering-based prototypes. Well-structured, clear contribution. Our paper is comparable in quality but has a larger evidence gap.

**Final position:** The paper sits between the accepted DeMul (6.4) and the rejected CARPRT (5.75). It is stronger than CARPRT in scope and absolute gains, but weaker than DeMul in terms of evidence matching claims. The core empirical finding (multiple prompts help CLIP) is solid and practically useful, but the paper overstates the contribution of its learning components. Score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>