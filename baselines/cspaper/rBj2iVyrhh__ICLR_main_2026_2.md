---
job_id: c34b93c5-ae7f-482b-8724-56ecf1bd4156
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: rBj2iVyrhh.pdf
paper: Classifier-Constrained Alternating Training: Mitigating Modality Imbalance in Multimodal Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies multimodal representation learning and optimization for modality imbalance in supervised multimodal classification.

## Minimum Quality
Pass ✅. The submission includes the expected core components, namely abstract, introduction, related work, method, experiments with quantitative results, analysis, and conclusion. While I found several technical and empirical weaknesses, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, suspicious reviewer-targeting instructions, or other obvious manipulation attempts in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies modality imbalance in multimodal learning, with a particular focus on the claim that alternating training reduces encoder interference but still leaves a biased shared classifier that favors the faster-converging modality. To address this, the authors propose Classifier-Constrained Alternating Training (CCAT), a two-stage framework that first pretrains a shared classifier using bidirectional cross-attention and a modality-contribution regularizer, then freezes that classifier during modality-wise alternating training while attaching modality-specific LoRA modules and performing an additional sample-level update on severely imbalanced samples. Experiments on CREMA-D, Kinetic-Sound, and MVSA report improved multimodal and in several cases unimodal accuracies over a set of balancing and alternating-training baselines.

## Strengths
The paper tackles a real and important issue in multimodal learning. The framing, namely that encoder-level balancing does not automatically fix decision-layer bias, is a reasonable and practically relevant angle. In particular, the training dynamics motivation in Section 1 and the empirical contribution curves in **Figure 1** make the problem setup intuitive: even under alternating training, the modality-wise contribution gap remains large over training, which supports the authors’ claim that something persists beyond pure encoder interference.

The method is reasonably structured. The two-stage design, classifier pretraining followed by frozen-classifier alternating training with modality-specific LoRA adapters, is conceptually coherent. I also appreciated that **Figure 3** gives a reasonably complete high-level picture of the pipeline, including the first pass over modalities, the sample-level imbalance detection block, and the classifier-with-LoRA view in panel (c). Even though I have concerns about some details, the overall design is easier to parse thanks to that figure.

The empirical gains in **Table 1** are nontrivial on some datasets, especially on Kinetic-Sound, where CCAT improves over the best listed baseline by a visible margin in multimodal accuracy. On CREMA-D, the gain over LFM is also noticeable. The paper also includes an ablation in **Table 2**, and this is useful because it shows the full model consistently outperforming its simplified variants across the three datasets. That does provide some evidence that the final gains are not coming from only one isolated trick.

The paper goes beyond reporting only multimodal accuracy and also shows unimodal results in **Tables 1 and 2**. Given that the stated goal is to better preserve or improve weaker modalities, this is the right direction for evaluation. The t-SNE and clustering summary in **Figure 5** also tries to connect the frozen-classifier design to feature-space discriminability, which is at least aligned with the claimed mechanism.

## Weaknesses
1. **The core theoretical analogy between class imbalance and modality imbalance is much weaker than the paper suggests, and the derivation does not actually establish the claimed “unified theoretical framework”.**  
   In **Section 3.1, Equations (1) to (3)**, the paper moves from the standard cross-entropy gradient
   \[
   \frac{\partial \mathcal{L}}{\partial \mathbf{w}_j} = (\hat y_j - \mathbf{1}_{[j=y]}) \mathbf{f}
   \]
   to an analogy between minority-class suppression and weak-modality suppression. The issue is that the modality case introduces
   \[
   \mathbf{f} = \gamma_1 \mathbf{f}^{(1)} + \gamma_2 \mathbf{f}^{(2)}
   \]
   with \(\gamma_1,\gamma_2\) described as “implicitly learned modality utilization coefficients”, but these coefficients are never defined as part of the model, are not parameters of any explicit fusion rule during alternating training, and are not shown to exist in a mathematically identifiable sense. The argument therefore reads more like a post hoc interpretation than a derivation from the training objective.  
   This matters because the paper’s main motivation rests on this analogy. If the “classifier bias” story is central, the paper needs a much more precise statement of what is being biased, under what assumptions, and how freezing the classifier changes the optimization dynamics. Right now, the theoretical part over-claims. It gives intuition, not a proof of equivalence or even a solid reduction.

2. **Several mathematical definitions are underspecified or inconsistent, especially around the contribution score and its use across the two stages.**  
   The contribution score is central to both pretraining and sample-level retraining, but the formalization is shaky. In **Equation (5)**, the mutual information estimate is written as
   \[
   \mathrm{MI}(\mathbf{z}_i^m,\mathbf{f}_i) = \log(N) + \mathbb{E}_{\mathcal D}\left[\log \frac{\exp\langle \bar{\mathbf f}_i,\bar{\mathbf z}_i^m\rangle}{\sum_i \exp\langle \bar{\mathbf f}_i,\bar{\mathbf z}_i^m\rangle}\right].
   \]
   There are multiple problems here. The indexing in the denominator is ambiguous, because the same \(i\) is reused inside and outside the expectation. It is unclear whether the denominator sums over all negatives in the batch, the full dataset, or all samples except \(i\). The estimator resembles an InfoNCE-style lower bound, but the sampling protocol is not specified. Without knowing the negative set and normalization precisely, the quantity is not reproducible and its scale is hard to interpret.  
   Then in **Equation (6)**, the paper applies a softmax over the two modality MI values to produce \(c_i^1,c_i^2\). This is not itself problematic, but it means the contribution score is a relative two-way normalized quantity, not an absolute estimate of modality reliance. Later, **Section 3.3** says that after pretraining, the contribution computation “follows the same decision-level fusion used in the inference stage”, unlike the cross-attention fusion in stage one. However, no new equation is provided for this second-stage contribution computation, even though the underlying representation and fusion mechanism have changed. So the paper uses the same notation \(c_i^m\) for at least two different constructions without formally defining the second one.  
   This matters because the threshold-based secondary update in **Algorithm 1** depends entirely on these \(c_i^m\) values. If the metric is unstable or differently defined across stages, the retraining subset may not reflect what the paper claims.

3. **There are specific equation-level errors and notation issues that undermine confidence in the technical presentation.**  
   In **Equation (7)**, the regularizer is written as
   \[
   \mathcal{L}_{\text{reg}}=\frac{\text{i}}{N}\sum_{i=1}^{N}|c_{i}^{1}-c_{i}^{2}|.
   \]
   The prefactor \(\frac{i}{N}\) is almost certainly a typo for \(\frac{1}{N}\), but as written it is mathematically incorrect because \(i\) is also the summation index. This is not a harmless cosmetic issue, because the regularizer is part of the stage-one objective.  
   There are related notation inconsistencies elsewhere. In **Equation (10)**,
   \[
   \hat{y}_{i}^{m}=\mathrm{Softmax}\left(\mathrm{Cls}(\mathbf{z}_{i}^{m})+\mathrm{LoRA}_{m}(\mathbf{z}_{i}^{m})\right),
   \]
   the LoRA output is added to the classifier output, which implies \(\mathrm{LoRA}_{m}(\mathbf{z}_{i}^{m})\) lives in the logit space. But **Equation (9)** defines LoRA as
   \[
   \mathrm{LoRA}_m(\mathbf z_i^m)=\mathbf B^m \mathbf A^m \mathbf z_i^m,
   \]
   which looks like a low-rank residual in feature space. The paper needs to clarify whether LoRA is attached to the classifier weights, to the classifier input features, or directly to the logits. **Figure 3(c)** visually suggests a classifier-level adaptation, but the equation suggests feature transformation and the implementation description remains vague.  
   Also, the appendix contains another likely inconsistency in the bidirectional attention block, where **Appendix Equation (19)** uses \(\mathbf z_i^1 + \mathbf a_i^2\) in the audio-to-visual branch, where one would expect \(\mathbf z_i^2 + \mathbf a_i^2\). I am not basing my score on appendix correctness, but this reinforces the impression that the math and notation were not carefully checked.

4. **The experimental evidence is suggestive, but it is not strong enough to fully validate the central mechanistic claim about classifier bias.**  
   The main claim is not merely that CCAT improves accuracy, but that freezing a pretrained classifier acts as an “unbiased decision anchor” that prevents structural preference toward dominant modalities. However, the evidence for this specific mechanism is indirect. **Figure 1** shows modality-wise contribution curves for MLA, but the figure does not include CCAT, so it diagnoses the problem but does not show that the proposed method actually fixes the diagnosed persistence. That is a missed opportunity, because the whole paper hinges on this exact phenomenon.  
   Similarly, **Figure 5** presents t-SNE visualizations and clustering scores comparing MLA, a non-fixed classifier, and CCAT. The direction is reasonable, but t-SNE is not strong evidence of a corrected decision boundary, and the figure appears to be shown only for one dataset. The text claims improved separation, especially for fear and sad classes, yet it is difficult to infer a robust causal story from a 2D projection. If the paper wants to make a classifier-centric claim, more direct diagnostics would be needed, such as tracking class-wise margins, classifier weight drift, modality-specific calibration, or explicit decision-boundary statistics over training.

5. **The baseline set is incomplete for the specific claim the paper is making, especially around decision-layer balancing and newer alternating-training variants.**  
   The paper compares against several strong multimodal imbalance baselines in **Table 1**, including MLA, MMPareto, and LFM. That is good. But once the paper’s novelty is framed as a classifier-level or decision-layer intervention on top of alternating training, the comparison set should be more targeted. The current experiments mostly show “better than a selected baseline set”, not “better than the most relevant neighboring approaches to this exact idea”.  
   This matters for contribution assessment. The paper is not just proposing another balancing method; it is arguing that prior alternating methods miss a classifier-side failure mode. Then the empirical section should confront methods that also operate at the decision layer or explicitly rethink balancing beyond encoder-only updates. As written, the positioning is weaker than it should be, and the novelty looks narrower.

6. **The ablation in Table 2 is helpful, but it does not isolate the main hypothesis cleanly enough.**  
   **Table 2** removes Fix, Alt, Sec, and LoRA one at a time, but there is no ablation for the stage-one pretraining regularizer itself, namely the modality-contribution regularization in **Equation (7)**. Since the paper argues that this step produces an “unbiased initial classifier”, one would want to compare at least: pretrained classifier with and without the regularizer, frozen versus unfrozen after the same pretraining, and perhaps frozen random or jointly trained classifiers.  
   Also, the ablation outcomes themselves raise questions. On Kinetic-Sound, removing LoRA changes multimodal accuracy from 79.29 to 78.77, which is relatively modest. On CREMA-D, removing freezing still gives 82.80, meaning the gains are present but not overwhelmingly diagnostic of the stated mechanism. In other words, the table supports that all components help, but it does not strongly validate that classifier freezing is the unique driver of the effect.  
   This matters because the paper’s title and framing put the classifier-constrained aspect at center stage.

7. **Hyperparameter selection and sensitivity analysis are not convincing enough for a method with several moving parts.**  
   The paper tunes LoRA rank \(r\) and threshold \(\beta\) by validation search, reporting **Table 3** and **Figure 4**. This is a start, but the sensitivity analysis is thin. In **Table 3**, the best \(r\) varies by dataset, with MVSA preferring \(r=8\) and the others preferring \(r=2\). The spread is not trivial, which suggests sensitivity. In **Figure 4**, the validation accuracy curves over \(\beta\) are relatively noisy and dataset-dependent. Yet there is no discussion of robustness, variance, or whether nearby settings materially change the ranking against baselines.  
   This matters because CCAT adds at least three delicate ingredients, stage-one contribution regularization, frozen classifier with modality-specific LoRA, and thresholded secondary updates. If these gains depend heavily on per-dataset tuning, the method is less generally persuasive than the paper claims.

8. **The inference and training mismatch is acknowledged, but not fully resolved or quantified.**  
   In **Section 3.3**, the authors correctly note that the classifier is pretrained on fused features \(\mathbf f\), then later applied to unimodal features \(\mathbf z^m\), which induces a distribution mismatch. The proposed fix is modality-specific LoRA. This is a sensible engineering patch, but the paper does not quantify how much mismatch remains, how LoRA alleviates it, or whether the frozen classifier actually remains a stable “anchor” rather than becoming a partially bypassed module through LoRA corrections.  
   **Figure 3(c)** is useful here because it shows the classifier weights receiving modality-specific A/B adaptation blocks, but the paper does not clearly state whether these updates preserve the same decision geometry or effectively learn new modality-specific heads around a frozen shared core. Without stronger analysis, the paper’s narrative can be read in two ways: either the frozen classifier anchors fairness, or the modality-specific LoRAs simply reintroduce flexible classifier adaptation in disguise.

9. **Presentation quality is mixed, and several wording and notation issues make the paper harder to trust than it should be.**  
   There are many small but cumulative issues: “underlying similar” in **Section 3.1**, “trainingpipeline” on **Page 6**, the malformed regularizer in **Equation (7)**, missing equation references for the second-stage contribution score, and some awkward or overstated claims such as “profound theoretical isomorphism” on **Page 4**. These do not make the paper unreadable, but they do affect confidence, especially because the method hinges on careful distinctions between fusion-space pretraining and unimodal alternating optimization.  
   The figures help, but some textual explanations around them are not as rigorous as the claims they are supposed to support.

## Questions
1. The paper’s main conceptual claim is that the classifier becomes structurally biased toward dominant modalities during alternating training. Can the authors provide a more direct empirical diagnostic of this phenomenon under both MLA and CCAT, for example tracking modality-specific margins, classifier weight movement, or contribution trajectories for CCAT in the same style as **Figure 1**? This would materially increase my confidence in the mechanism.

2. Please clarify the exact definition of the contribution score \(c_i^m\) in stage two. In **Section 3.3**, the text says the computation is no longer based on the cross-attention fusion from stage one, but instead follows the same decision-level fusion used at inference. What is the exact formula in this second stage? How is it related to **Equations (5) and (6)**?

3. In **Equation (5)**, what is the exact negative set used in the MI estimate? Is the denominator over the batch, over the full dataset, or over sampled negatives? Please rewrite the expression with unambiguous indexing. Right now it is difficult to reproduce.

4. In **Equations (9) and (10)** and **Figure 3(c)**, where exactly is LoRA applied? Is it a low-rank residual on the classifier input, a low-rank update to classifier weights, or a logit correction term? A more explicit parameterization would help, ideally with tensor shapes.

5. Can the authors add an ablation that isolates the stage-one regularizer in **Equation (7)**, namely pretraining the classifier with and without the contribution-balancing penalty, while keeping the rest of CCAT unchanged? This would directly test whether the “unbiased initial classifier” claim is empirically justified.

6. For **Table 1**, please clarify whether all baselines were reproduced under the same encoder backbones, training budget, and evaluation protocol, especially for the unimodal numbers. The note in **Section 4.1** hints that unimodal evaluation protocols differ by method, which could complicate interpretation.

7. Since **Figure 5** is used to support the frozen-classifier argument, can the authors provide the same analysis on more than one dataset, or add a quantitative metric tied more directly to decision-layer bias than t-SNE clustering quality?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns arise from the paper as presented. The work focuses on multimodal classification methodology and standard benchmark datasets.

## Soundness Rating
2: fair. The paper has a plausible method and some solid empirical signals, but the central mechanism is only partially supported, and several equations/objectives are underspecified or inconsistent.

## Presentation Rating
2: fair. The structure is understandable and the figures/tables are useful, but the paper contains enough notation errors, ambiguities, and imprecise explanations to materially limit clarity.

## Contribution Rating
2: fair. The classifier-freezing plus modality-specific adaptation idea is interesting, and the results are promising, but the paper does not yet make a sufficiently well-validated or sharply positioned contribution for ICLR main track.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper addresses a meaningful problem and reports promising results, but the current version overstates its theoretical grounding, leaves important mathematical and implementation details ambiguous, and does not yet provide sufficiently direct evidence for its main classifier-bias claim.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is still possible that some implementation details are clearer in supplementary material than in the main text.