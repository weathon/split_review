Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper explores face recognition improvement from a feature-space perspective. It first shows via orthogonal decomposition that the "innovation" component of a superior model's feature (orthogonal to an inferior model's feature) retains discriminative ability, and that recombining a scaled innovation with the parallel component can outperform the original superior model. Motivated by this two-model observation, the paper proposes an intra-class incoherence constraint (IIC) within a knowledge distillation setup: a student network (same architecture as a strong teacher) is trained to minimize cosine similarity between its features and the teacher's, alongside a standard FR loss. Experiments on CASIA and MS1MV2 with ResNet50/100 backbones show consistent improvements over ArcFace, CosFace, MagFace, and AdaFace on multiple benchmarks (LFW, CFP-FP, CPLFW, AgeDB, CALFW, VGGFace2, IJB-C).

## Strengths

- **Novel concept of "innovation" with concrete empirical validation.** The orthogonal decomposition analysis (Eq. 1, Table 1) is a clean geometric demonstration: the innovation component of ArcFace orthogonal to CosFace's feature space achieves 95.23% on CPLFW vs. 95.15% for CosFace, while the parallel "pro-feature" degrades to 38.33%. This provides a verifiable basis for the claim that innovation carries useful discriminative information.

- **Consistent empirical gains across multiple benchmarks, backbones, and base methods.** Tables 3–5 report improvements that, while modest on saturated benchmarks like LFW, are more substantial on harder protocols: e.g., AdaFace + IIC improves from 89.20% to 90.83% on AgeDB (Table 3), and ArcFace + IIC improves from 70.75% to 72.27% at FPR=1e-6 on IJB-C (Table 5). The pattern holds across ArcFace, CosFace, MagFace, and AdaFace, suggesting the benefit is not specific to any one base method.

- **Ablation studies show the IIC term is the active ingredient.** Table 7 provides a critical control: loading teacher weights and training with only FR loss (no IIC) causes a performance *drop*, ruling out the trivial explanation that additional training alone drives the gains. Weight sensitivity (Table 6) shows marginal variation across γ ∈ {0.1, 0.5, 1.0}, indicating robustness rather than brittleness.

## Weaknesses

### Fatal
None.

### Major

- **The loss function does not implement what the motivation claims.** The paper motivates IIC as encouraging *orthogonality* between student and teacher features (innovation = component orthogonal to the teacher's feature). However, the actual loss \(L_{dissim}\) is defined as the cosine similarity of \(f_T\) and \(f_S\) (lines 107, 115). Minimizing \(L_S = L_{FR} + \gamma L_{dissim}\) pushes cosine similarity *down* (toward −1, i.e., anti-correlation), not toward 0 (orthogonality). The paper provides no discussion of why anti-correlation would be preferable to orthogonality, nor does it consider alternatives such as absolute cosine similarity or squared cosine similarity. This mismatch means the claimed mechanism ("learning orthogonal innovation") is not what the training objective actually enforces. The empirical gains may arise from a different, unidentified mechanism (e.g., feature decorrelation or a regularization effect), and the paper's central conceptual framing is therefore unreliable.

- **The logical leap from the two-model decomposition to the single-model IIC is unsubstantiated.** In the two-model setting (Section 3.1, Fig. 1(a)), innovation is defined relative to a *weaker* model's feature space (CosFace), and it can be concretely decomposed, measured, and recombined. The paper then jumps to a single-model setting where the teacher is a *strong* model, and the student is pushed to be dissimilar to it. The justification for why pushing away from a strong model should yield useful (rather than degrading) features is never established. The analogy does not transfer: in the two-model case, the orthogonal component is informative precisely because it captures what the superior model has that the weaker one lacks; in the single-model case, there is no weaker reference model to define what "innovation" means. The paper asserts (line 86) that innovation has two characteristics—orthogonal to \(a\) and improving accuracy—but never shows that the IIC-trained student's features satisfy either property in a measurable way (beyond a brief, unquantified mention in the ablation, line 181).

### Minor

- **The claim of doing "the opposite" of traditional FR is overstated.** The paper states (line 197) that "This paper does the opposite" of increasing intra-class correlation. But the student's loss still includes a standard FR loss (\(L_{FR}\)) that enforces intra-class compactness. IIC adds a dissimilarity constraint on top; the net effect is a trade-off, not an inversion. The paper provides no analysis of the resulting intra-class vs. inter-class feature distribution (e.g., cosine similarity statistics, effective margins), so the "opposite" framing is misleading.

- **The control experiment in Table 7 lacks sufficient detail to fully rule out fine-tuning effects.** The paper reports that loading teacher weights and training with only \(L_{FR}\) causes a slight performance drop (Table 7). However, it does not specify whether this control uses the same learning rate schedule, number of epochs, and data ordering as the IIC run. Since the "feature augmentation" hypothesis (Section 4.2) hinges partly on this comparison, the missing details are a gap, though a minor one given the clear directional result.

- **The "feature augmentation" hypothesis is supported by only one small-scale experiment.** The claim that IIC acts as a form of feature augmentation (Section 4.2) is validated using only 1/10 of MS1MV2 with a single method (AdaFace). While the results are suggestive, the paper would benefit from testing this hypothesis on other methods or at larger scale.

### Trivial

- The paper's reference to Shin et al. (2022) correctly identifies that prior work uses attention similarity for same-size distillation. The positioning is adequate for a conference paper, but the connection to feature decorrelation methods from self-supervised learning (e.g., Barlow Twins) is not discussed—this is a minor omission rather than a flaw.

## Nice-to-Haves

- **Replace the cosine similarity minimization with a loss that explicitly enforces orthogonality** (e.g., minimize the absolute or squared cosine similarity), or justify why anti-correlation is acceptable. This would align the method with the motivating geometry.
- **Provide direct evidence of the student's orthogonal component.** Perform the same orthogonal decomposition used in the two-model analysis (treat student as "superior" relative to teacher) and measure the recognition accuracy of the student's innovation component, as the paper hints at in the ablation (line 181) but does not quantify.
- **Visualize the feature space.** A t-SNE plot or cosine similarity distribution between teacher and student features (same-identity vs. different-identity) would clarify what IIC actually does to the representation geometry.
- **Compare with simple regularizers.** Adding feature noise, dropout, or a feature decorrelation loss on batch features would help isolate whether IIC's benefit is specific to dissimilarity from the teacher or a generic regularization effect.

## Removed Points

These points are flagged for removal — treat with caution.

1. **IoT device footnote (line 14):** The garbled footnote text about IoT devices and healthcare is clearly a PDF extraction artifact (parser corruption of what was originally a mathematical caption). The reviewer acknowledges this may be a formatting issue. Removed as a parser artifact, following hard rules on formatting nitpicks.

2. **Typos/grammar concerns:** Comments about "careful proofreading" based on the garbled footnote. Removed as parser artifacts.

3. **"Method not yet released / cannot be independently verified":** The harsh critic questioned reproducibility. The paper cites publicly available checkpoints ("parameters of the teacher network are downloaded from their official offered checkpoints if available," line 146). Removed per hard rules: cited entities are assumed to exist.

4. **Training from scratch with IIC as a necessary control:** The reviewer asks to compare IIC-trained student to a model trained from scratch with IIC without teacher initialization. This is infeasible by design — IIC requires a pre-trained teacher to compute \(f_T\). Removed as practically impossible.

5. **Weight sensitivity implying IIC is "ignored":** The reviewer speculates that marginal differences across γ values could mean the loss is "essentially ignored." However, Table 7 shows that removing IIC (γ=0) causes a performance drop, confirming IIC is active. Marginal differences across non-zero γ indicate robustness, not irrelevance. Removed as factually incorrect inference.

6. **Missing appendix/proofs references:** Any complaints about missing appendix content. Removed per hard rules (parser strips appendices).

7. **Related work on Barlow Twins/VicREG:** The suggestion to compare with self-supervised decorrelation methods. This is a reasonable direction for future work but does not constitute a weakness of the current paper — the paper operates in a supervised distillation paradigm, not self-supervised learning. Moved to Removed Points.

8. **Criticism that "the paper does not report multiple runs or statistical significance":** This is standard practice in face recognition benchmark papers at this scale. Single-run evaluation on these benchmarks is the norm. Downgraded and removed per soft rules on field-appropriate methodology.

9. **Sentence-level pedantry:** Claims that individual sentences are "not supported" when the overall argument is coherent. Removed as nitpicking.

## Novel Insights

The most interesting observation in the paper — and one largely separable from the IIC proposal — is the geometric demonstration in Tables 1–2. The finding that the innovation component of a superior model (orthogonal to an inferior model's feature space) retains discriminative ability, and that re-scaling it can produce features that beat the original superior model, is genuinely non-trivial. It suggests that different FR models may have complementary blind spots that can be exploited through vector operations in feature space. This idea is worth separately developing, even if the IIC extension has conceptual problems.

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the paper around what the experiments actually show.** The empirical finding — that training a student to be dissimilar to a teacher (alongside a standard FR loss) can improve recognition — is defensible as an empirical contribution even without the orthogonal-decomposition motivation. Drop the claim that IIC "learns innovation orthogonal to the teacher" unless the loss is changed to enforce orthogonality. A more honest framing would describe IIC as a regularization strategy that prevents feature collapse during fine-tuning.

2. **Fix the loss function to match the claimed mechanism.** If the goal is truly orthogonal features, replace \(L_{dissim} = \cos(f_T, f_S)\) with \(L_{dissim} = |\cos(f_T, f_S)|\) or \(\cos^2(f_T, f_S)\) so that the gradient pushes toward 0 (orthogonality) rather than −1 (anti-correlation).

3. **Add quantitative analysis of the teacher–student feature relationship.** Report the distribution of cosine similarities between teacher and student for same-identity pairs, and perform the orthogonal decomposition of student features relative to teacher features to confirm that the learned features have an orthogonal component that is discriminative (potentially reusing the methodology from Section 3.1).

4. **Tone down the "opposite" framing.** Acknowledge that IIC is an additive constraint on top of standard FR training, not a replacement. The current language in the conclusion is misleading.

## Score and Decision

**Score: 4.5/10** — The paper has a genuine empirical finding (IIC improves multiple FR baselines) and a novel geometric observation about feature decomposition. However, two major conceptual problems undermine the paper's claimed contribution: (1) the loss function does not implement orthogonality despite claiming to do so, and (2) the logical transfer from the two-model decomposition to the single-model IIC is unjustified. The theoretical framing is therefore unreliable, and the empirical results, while positive, lack the mechanistic explanation the paper asserts. The paper would require major revisions — including reframing the contribution and fixing the loss — before it could be accepted.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>