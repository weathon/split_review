---
job_id: 4b74fbbe-101c-4775-96f7-4f451dce1fa7
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5Y4wvlp923.pdf
paper: Semantic Disentanglement Error: A Pluggable Mechanism for Balanced Contrastive Time-Series Representation
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on self-supervised contrastive representation learning for time-series.

## Minimum Quality
Pass ✅. The submission contains the required scientific sections, and although there are substantial issues in novelty, formulation, and empirical support, these are better handled through full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, manipulative instructions, or other signs of attempted interference with automated or human review.

# Expected Review Outcome:
## Summary
This paper studies semantic imbalance in contrastive time-series representation learning, with a focus on cases where dominant components such as trend suppress weaker components such as seasonality. The authors introduce a directional metric called Semantic Disentanglement/Separability Error (SDE) to quantify recoverability of one component from a composite embedding, and then use an asymmetry score derived from SDE to adaptively reweight seasonal and trend contrastive losses in a CoST-style framework. Experiments on synthetic mixtures and several forecasting benchmarks are presented to support the claim that the proposed weighting improves robustness under semantic skew.

## Strengths
The paper targets a reasonable and relevant problem. The observation that contrastive objectives can overemphasize dominant temporal factors and underrepresent weaker but meaningful components is plausible, and it is especially relevant for time-series where trend and seasonality often have very different amplitudes.

The proposed SDE metric is at least intuitively interpretable. The directional definition,
\[
\mathrm{SDE}_{\mathbf a,\mathbf b} = 1 - \cos\big(v(\mathbf a+\mathbf b)-v(\mathbf b),\, v(\mathbf a)\big),
\]
tries to operationalize whether one component is recoverable from a composite representation. Even though I have concerns about whether this is the right object to optimize, as a diagnostic probe it is easy to understand and potentially useful for controlled analysis.

The preliminary synthetic analysis in **Table 1** does illustrate a clear asymmetry pattern in TS2Vec: when the trend amplitude dominates, \(\Delta\) becomes positive and large, while the reverse regime produces negative \(\Delta\). That table is one of the more convincing parts of the paper because it directly connects the claimed issue, semantic imbalance, to a controllable factor, the amplitude ratio \(r\). If the rest of the paper were as careful as this controlled setup, I would be more positive.

The paper also has one practical angle that could matter if properly developed: the mechanism is intended to be “pluggable” on top of CoST, rather than requiring a completely new architecture. That kind of lightweight intervention can be valuable in practice, assuming the method is actually well specified and robust.

**Figure 1** succeeds at conveying the intended high-level pipeline. It makes clear that the authors want to measure asymmetry after obtaining seasonal and trend embeddings and then feed this asymmetry back into the loss weighting. As a conceptual diagram, it does help the reader understand the intended control loop.

## Weaknesses
I have substantial concerns about the paper’s technical precision, empirical support, and the degree to which the claimed contribution is actually established. Below I list the main issues in detail.

1. **The core method is inconsistently described across Sections 3 and 4, and these inconsistencies matter.**  
   In **Section 3.2-3.4 (Page 3)**, SDE is introduced as a property of a learned representation function \(v(\cdot)\) on actual signals \(\mathbf a\), \(\mathbf b\), and \(\mathbf a+\mathbf b\), and the adaptive weighting is presented as a direct modification of CoST’s two losses. However, in **Section 4.4.2 (Page 6)**, the paper changes the construction materially: \(v(\mathbf a+\mathbf b)\) is no longer the encoder output on the original signal, but the output of a separate MLP \(g_\phi([v(\mathbf a)\|v(\mathbf b)])\). This is not a cosmetic difference. It changes the semantics of SDE from measuring recoverability from the representation of the actual composite input to measuring consistency inside a learned fusion module. Those are different objects. If the MLP is introduced only in the experimental method, then the method section is incomplete. If the MLP is part of the actual proposal, then the main method section on **Page 3** is misleading. Right now the reader is left unsure what was actually implemented.

2. **The optimization objective is underspecified and potentially unstable.**  
   The weighted loss on **Page 3 / Page 6** is
   \[
   \mathcal L = (1+\gamma\Delta)\mathcal L_{\text{season}} + (1+\gamma'(-\Delta))\mathcal L_{\text{trend}}.
   \]
   But the paper never explains how \(\Delta\) is computed during training, at what frequency, from which samples, and with what stopping of gradients if any. Is \(\Delta\) computed per instance, per batch, or as an EMA over the training set? Since SDE depends on cosine similarity between learned embeddings, the batch-level variance could be high. Moreover, there is no guarantee that \(1+\gamma\Delta\) and \(1-\gamma'\Delta\) remain positive. From **Table 1**, \(\Delta\) can exceed \(1\) in magnitude, and the paper gives no clipping, normalization, or bounded transform such as \(\tanh\). With sufficiently large \(\gamma\) or \(\gamma'\), the method could assign negative coefficients to one of the losses, which would be a serious optimization pathology. This is not a minor implementation omission, it affects whether the objective is even well-defined.

3. **The mathematical justification for SDE is weak, and the claimed interpretation is not well defended.**  
   The paper states on **Page 3** that a small \(\mathrm{SDE}_{\mathbf a,\mathbf b}\) indicates the contribution of \(\mathbf a\) is “linearly recoverable” from the composite embedding. That is much stronger than what the equation actually shows. The quantity
   \[
   v(\mathbf a+\mathbf b)-v(\mathbf b)
   \]
   being directionally aligned with \(v(\mathbf a)\) does not establish linear recoverability in any rigorous sense, especially when \(v\) is a nonlinear encoder and the embeddings may have arbitrary scaling and anisotropy. At best, it is a heuristic analogy to vector arithmetic. The paper cites word embeddings for inspiration, but that is not a derivation. If the intended claim is diagnostic rather than formal, the wording should be much more careful. As written, the paper over-interprets the metric.

4. **There is notation drift and naming inconsistency around the central quantity, which makes the exposition look undercooked.**  
   The title and abstract use “Semantic Disentanglement Error,” while **Section 3.2 (Page 3)** calls it “Semantic Separability Error,” and **Section 4.1 / 4.3 (Pages 4-5)** calls it “Semantic Decomposition Error.” All three abbreviate to SDE, but these are not the same phrase. This is not merely stylistic. When the central contribution changes names across sections, it becomes harder to tell whether the authors regard it as a disentanglement metric, a separability metric, or a decomposition metric. The paper needs one definition and one interpretation.

5. **The empirical evidence does not convincingly support the strong claims made in the text.**  
   The narrative around **Table 3 (Pages 6-7)** says the proposed method yields “consistently lower SDE values and superior forecasting accuracy,” but the table does not report SDE values at all. It reports only MSE/MAE. This is an explicit mismatch between the text and the presented evidence. If SDE is central to the claim that the method balances semantics, then the paper must show SDE before and after weighting on the real datasets, not just on the synthetic TS2Vec setup in **Table 1**. Without that, the paper never actually demonstrates that CoST+APW improves the quantity it is supposedly designed to optimize.

6. **Even on forecasting, the results in Table 3 are far from “consistently” better, and some entries directly weaken the paper’s case.**  
   **Table 3** contains several rows where CoST+APW is not the best method, sometimes not even close. On **Electricity**, the proposed method is clearly worse than CoST, TS2Vec, and TNC at horizons 168, 336, and 720 in both MSE and MAE. On **Weather**, APW is worse than TS2Vec and TNC at 24, 48, 336, and 720 in MSE, and often worse in MAE as well. Even on ETTh1/ETTh2 there are ties or reversals. This does not support the broad claim of superior forecasting accuracy. At best, the method helps on some datasets and horizons, particularly ETTm1. The paper should say that honestly and then analyze when and why the method helps or hurts. Right now the conclusions oversell a mixed table.

7. **The comparison is too narrow relative to the claimed scope of the contribution.**  
   The main paper compares against TS2Vec, TNC, and CoST. Since the proposed method is explicitly an add-on to CoST and framed as a general mechanism for balanced contrastive learning, the most important evidence would be stronger ablations within the CoST family and, ideally, tests of plug-and-play behavior on more than one backbone. As presented, the method is only instantiated on CoST, and even there, the paper does not isolate the effects of the new MLP fusion module versus the APW weighting. This is crucial because **Section 4.4.2 (Page 6)** introduces an MLP-based composite embedding, which is itself a nontrivial architectural change despite the “without architectural changes” framing in the abstract. If gains are due to the MLP rather than the weighting, the paper’s main claim changes substantially.

8. **Key ablations are missing, especially for the proposed components and hyperparameters.**  
   There is no ablation over \(\gamma\) and \(\gamma'\), no study of whether clipping or normalizing \(\Delta\) is required, no comparison of per-batch versus dataset-level asymmetry estimates, and no analysis of the fusion MLP depth/width. There is also no ablation removing the MLP while keeping APW, or keeping the MLP while disabling APW. Since the method as implemented in **Section 4.4** appears to contain both ingredients, the paper does not tell us which part is actually responsible for the observed changes. This is a serious gap for a paper whose contribution is largely methodological.

9. **The “pluggable” claim is overstated given the actual description.**  
   The abstract says the approach can be integrated into frameworks like CoST “without architectural changes.” But **Section 4.4.2** explicitly adds a learnable MLP \(g_\phi\) to create the composite embedding. That is an architectural change. If the MLP is optional, the paper should say so and provide results without it. If it is required, then the abstract is inaccurate. This contradiction affects how readers interpret the practical significance of the method.

10. **The experimental protocol lacks enough detail to assess rigor and reproducibility.**  
   **Section 4.1 (Page 4)** lists optimizer, learning rate, batch size, and epochs, but many critical details are absent. For instance: how are validation splits used; how are hyperparameters \(\lambda\), \(\gamma\), and \(\gamma'\) selected; what augmentations are used for each method; are results averaged over multiple seeds; are the reported numbers from linear probing, end-to-end fine-tuning, or some standard forecasting head; and what exact decomposition and pooling operations are used in practice? The lack of variance bars or standard deviations is particularly problematic because many improvements over CoST in **Table 3** are very small, often at the third decimal place.

11. **The direct SDE-regularization experiment in Table 2 is under-analyzed and weakly motivated.**  
   **Table 2 (Page 6)** shows that adding SDE regularization to TS2Vec mostly hurts performance. That negative result is actually useful, but the paper does not do enough with it. Why does this fail? Is it due to noisy decomposition, a bad proxy objective, or conflicting gradients? Since the final method still depends critically on SDE, just in a different role, this failure should lead to a deeper analysis. Instead, the paper gives only a brief hypothesis that SDE “fails to provide constructive optimization gradients.” That may be true, but the paper does not support the claim with gradient analysis, training curves, or any concrete evidence.

12. **The synthetic decomposition setup is too idealized to justify claims about real-world semantics.**  
   In **Section 4.2 and 4.3**, trend is obtained by low-pass filtering and periodicity as a residual, with synthetic mixtures of trend and sinusoid. That is acceptable for a controlled probe, but it is a very narrow model of time-series semantics. On real multivariate benchmarks, “seasonality” and “trend” are not clean additive components, and residuals can include noise, transients, and regime changes. Since the whole proposal hinges on reweighting based on semantic imbalance, stronger real-data analysis is needed to establish that the computed SDE is meaningfully tied to actual trend/seasonal factors rather than artifacts of the decomposition choice.

13. **Figure 1 is conceptually helpful but also exposes an oversimplification of the method.**  
   The seesaw-style visualization in **Figure 1** communicates that \(\Delta\) “balances” seasonal and trend losses, but it also hides essentially all of the hard parts: how SDE is computed from actual embeddings, whether \(\Delta\) is scalar per batch or dataset, whether the coefficients are bounded, and how the added fusion mechanism interacts with the two branches. In other words, the figure works as a cartoon, but it highlights the gap between intuitive story and precise algorithm. For a paper whose main contribution is a training-time weighting mechanism, I would have expected a more explicit algorithmic diagram or pseudocode.

14. **The paper’s positioning against prior work is incomplete and somewhat muddled.**  
   The paper argues that existing methods lack mechanisms for semantic balance, but CoST already decomposes seasonal and trend representations and uses frequency-aware contrastive learning. The delta from CoST is therefore not the introduction of decomposition or dual-view learning, but the particular SDE-based adaptive weighting, plus possibly the fusion MLP. The paper should position itself much more narrowly and honestly as an adaptive reweighting extension to CoST, rather than as a broader diagnosis of three “fundamental limitations” of current self-supervised time-series learning. That framing reads too sweeping for the evidence provided.

Overall, the paper has an intuitive motivation, but the current version does not yet meet the bar for a clean, convincing ICLR contribution. The main issue is not that the idea is impossible, it is that the present writeup leaves too many unanswered methodological questions while the experimental evidence is mixed and sometimes inconsistent with the paper’s own claims.

## Questions
1. In the final implemented method, what exactly is \(v(\mathbf a+\mathbf b)\)? Is it the encoder output on the original input sequence, as suggested in **Section 3.2**, or the MLP output \(g_\phi([v(\mathbf a)\|v(\mathbf b)])\), as stated in **Section 4.4.2**? Please clarify which definition is used in all experiments.

2. How is \(\Delta\) computed during training in practice? Per sample, per batch, per epoch, or via a moving average? Do gradients flow through \(\Delta\), or is it treated as a detached statistic? A precise algorithm or pseudocode would materially increase confidence.

3. How do you ensure the weights \(1+\gamma\Delta\) and \(1-\gamma'\Delta\) remain nonnegative and numerically stable? If you clip or normalize \(\Delta\), please state the formula. If not, please justify why negative weights cannot occur under your chosen hyperparameters.

4. Please provide the missing ablation that separates the effect of the fusion MLP from the APW weighting. At minimum, I would want to see: CoST, CoST+MLP, CoST+APW without MLP if possible, and CoST+MLP+APW.

5. Since the paper repeatedly claims lower SDE on real datasets, can you report actual SDE numbers for CoST and CoST+APW on ETT, Electricity, and Weather? Right now **Table 3** does not contain this evidence.

6. Can you provide variance over multiple random seeds for **Table 3**? Several improvements over CoST are very small, while some degradations are substantial. Without seed variation, it is difficult to tell which differences are meaningful.

7. The Electricity and Weather results in **Table 3** appear to contradict the claim of broadly improved forecasting. Can you explain when APW helps and when it hurts? Is the method primarily useful only under certain types of semantic skew?

8. In **Table 2**, direct SDE regularization degrades TS2Vec. Do you have evidence, beyond the brief hypothesis in the text, for why SDE is useful as a diagnostic but not as a regularizer? For example, gradient-scale analysis, optimization trajectories, or sensitivity to \(\lambda\) would be helpful.

9. The central term “SDE” is expanded in three different ways across the paper. Please standardize the terminology and clarify whether you intend this as a disentanglement metric, a separability metric, or a decomposition metric.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns arise from the submission based on the paper content. The work is a methodological study on time-series representation learning and does not appear to involve sensitive human-subject data, privacy-sensitive deployment claims, or harmful application framing in the main paper.

## Soundness Rating
2: fair. The core intuition is plausible, but the paper leaves important parts of the objective and implementation underspecified, and the empirical evidence only partially supports the main claims.

## Presentation Rating
2: fair. The high-level story is understandable, but there are substantial clarity issues, including inconsistent terminology, method description drift between sections, and overstatements relative to the reported tables.

## Contribution Rating
1: poor. The paper contains an interesting diagnostic idea, but the actual scientific contribution is not convincingly established beyond a modest adaptive extension to CoST, with mixed empirical support and limited methodological isolation.

## Overall Rating
2: Reject, not good enough. The motivation is reasonable and the synthetic SDE analysis is somewhat interesting, but the submission in its current form is too under-specified and empirically inconsistent for ICLR. The method description has nontrivial contradictions, the main claims are stronger than what **Table 3** supports, and key ablations needed to attribute gains to the proposed mechanism are missing.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the equations, figures, and tables carefully, though a few implementation details are missing from the paper and therefore cannot be fully verified.