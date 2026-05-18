Now I have a thorough understanding of the paper and can verify all claims. Let me construct the final consolidated review.

## Summary

This paper studies the limitations of post-hoc temperature scaling for model calibration on classification distributions where class supports overlap. The authors prove that for ERM interpolators satisfying a local Lipschitz-like condition (\(\gamma\)-regularity), even oracle-optimal temperature scaling yields calibration error that degrades to no better than random as the number of classes grows. Conversely, they introduce and analyze \(d\)-Mixup (mixing \(d+1\) points), proving its calibration error is bounded independently of overlap. Experiments on synthetic Gaussian data (with \(d\)-Mixup) and image benchmarks CIFAR-10/100 and SVHN (with 2-point Mixup) confirm the qualitative pattern: Mixup-based training degrades far more gracefully than ERM+TS as overlap/label noise increases.

## Strengths

1. **First rigorous proof that temperature scaling provably fails on overlapping-class distributions.** Theorem \ref{generalerm} proves that for \(\gamma\)-regular ERM interpolators on distributions with constant class overlaps, even oracle-optimal temperature scaling has calibration error at least \(\Theta((1-\alpha-1/k)\log k)\), which asymptotically becomes no better than random. This provides a formal explanation for empirical observations that post-hoc scaling underperforms training-time methods.

2. **Novel theoretical analysis of \(d\)-Mixup with a positive result.** The paper introduces \(d\)-Mixup (mixing \(d+1\) points), characterizes its optimal predictions (Lemma \ref{infdmixopt}), and proves (Theorem \ref{generalmix}) that \(d\)-Mixup interpolators achieve constant calibration error independent of the overlap parameter \(\alpha\). This is a genuine theoretical contribution that goes beyond prior Mixup analyses which were limited to linear models and Gaussian data.

3. **Empirical validation spanning synthetic and real benchmarks.** The synthetic Gaussian experiments (Table \ref{tab:synthetic}) directly validate the theory: as class overlap increases (\(\mu\) decreases from 0.25 to 0.01), ERM+TS NLL skyrockets from 0.26 to 4.30 while \(d\)-Mixup variants stay below 0.83. The image experiments (Table \ref{tab:imageclass}) on CIFAR-10/100 and SVHN with synthetic label noise confirm the same pattern holds on realistic benchmarks, with Mixup's NLL increasing much more slowly than ERM+TS as noise grows.

4. **Clean theoretical framework with reusable definitions.** The formalization of ERM interpolators (Definition \ref{erminterpolator}), \(\gamma\)-regularity (Definition \ref{regularity}), and the general overlapping distribution class (Definition \ref{generaldist}) provide a foundation that future theoretical work on calibration can build upon. The empirical grounding of the interpolation property (Table \ref{tab:logits}) connects the theory to observed practice.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between \(d\)-Mixup theory and 2-point Mixup experiments.** The paper's central theoretical positive result (Theorem \ref{generalmix}) is proved for \(d\)-Mixup with \(d+1\) mixed points, yet the image experiments use ordinary 2-point Mixup. The paper acknowledges this gap (Remark, lines 145-147) and conjectures that "due to the structure of practical models... even mixing two points... is sufficient," but provides no analysis or experiment supporting this claim. The synthetic experiments do use \(d\)-Mixup (for \(d=2,4\)) and show it works, but the main empirical evidence on real images validates a different method than what the theory covers. This weakens the direct link between theory and the paper's most practically salient experiments.

2. **Asymmetric experimental comparison.** The image experiments (Table \ref{tab:imageclass}) and synthetic experiments (Table \ref{tab:synthetic}) compare ERM *with* temperature scaling against Mixup *without* temperature scaling. The paper states this explicitly (line 227). Without showing that Mixup+TS does not substantially improve over Mixup alone, or that ERM without TS is even worse than ERM+TS, the reader cannot cleanly separate the effect of training procedure from the effect of post-hoc scaling. The core claim that "training-time calibration may be necessary" would be significantly strengthened by including these control conditions.

### Minor

1. **Assumption for Theorem \ref{generalmix} not summarized in main text.** Theorem \ref{generalmix} depends on "Assumption \ref{mixdist}" which is not defined in the provided text. While the paper gives some contextual cues (lines 208-209) about needed restrictions (spacing between non-overlapping classes, constraints on mixing skewness), the scope of the positive result cannot be fully assessed from the main text alone. A brief summary of what this assumption requires would make the theorem self-contained.

2. **Empirical justification for \(\gamma\)-regularity is incomplete.** Table \ref{tab:logits} empirically justifies the interpolation condition (large logit separation on training points), which is reasonable. However, \(\gamma\)-regularity — the local Lipschitz-like condition that is equally central to the negative result — is not empirically verified. The paper would be stronger with evidence (or a reference) showing that overparameterized networks satisfy this property near training points, rather than leaving it as a plausible assumption.

### Trivial

1. The universal constant \(L\) in Definition \ref{regularity} (\(\gamma\)-regularity) is never instantiated or discussed; a brief remark on its relationship to network Lipschitz constants would help.
2. The proof sketch for Theorem \ref{generalerm} mentions a sphere radius \(r\) with volume \(k/(2MN)\), but the transition from this \(r\) to the parameter \(\gamma\) in \(\gamma\)-regularity is not explained in the main text.
3. The synthetic experiments use \(d=2,4\) in 300-dimensional space with \(d\)-Mixup; whether the benefit arises from the mixing constraints themselves or from the problem being effectively low-dimensional is not discussed.

## Nice-to-Haves

- Include Mixup+TS and ERM without TS in both synthetic and image experiments to cleanly separate training effects from post-hoc scaling effects.
- Provide some theoretical or empirical argument connecting 2-point Mixup to the neighborhood constraints of \(d\)-Mixup for the specific model class used (ResNeXt-50), even if informal.
- A brief discussion of whether \(\gamma\)-regularity is known to hold for overparameterized neural networks after training, with references.

## Removed Points

- **"Warm-up 1-D distribution has artificial spacing of \(k\) between pairs of classes"**: The paper explicitly addresses this (line 159), stating the spacing is only to simplify the \(d\)-Mixup analysis and is unnecessary for the negative results. The reviewer's concern is already resolved by the paper itself.
- **"Definition 2 (\(\gamma\)-regularity) has a complex probabilistic formulation"**: This is a subjective presentation preference, not a substantive weakness. The definition is technical but precise, which is appropriate for a theoretical paper.
- **"Missing appendix / Assumption \ref{mixdist} should be stated"** (as a claim that the assumption is missing): The assumption exists in the appendix (stripped by parser). However, the request that it be *summarized* in the main text is kept as a Minor weakness above.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily validate and identify gaps in the paper's existing claims rather than introducing new perspectives.

## Suggestions

1. Address the \(d\)-Mixup / 2-point Mixup gap. The most impactful fix would be to provide a theoretical argument (even heuristic) that the class of models used in practice (overparameterized neural networks) cause 2-point Mixup to approximate the neighborhood constraints of \(d\)-Mixup. Alternatively, demonstrate that \(d\)-Mixup with small \(d\) (e.g., \(d=2\) mixing 3 points) works on image benchmarks, even with some underconfidence.
2. Add Mixup+TS and ERM without TS to the experimental tables. This would be a small experimental addition that cleanly separates the effect of training procedure from post-hoc scaling.
3. Include a brief summary of Assumption \ref{mixdist} in the main text so Theorem \ref{generalmix} is self-contained.
4. Add a note or reference on whether \(\gamma\)-regularity has been verified or is expected to hold for trained neural networks.

## Score and Decision

**Score:** 6.5 — The paper makes a genuine theoretical contribution with clear negative and positive results, supported by carefully designed experiments. The main weaknesses are the gap between the \(d\)-Mixup theory and the 2-point Mixup image experiments, and the asymmetric experimental design. These are real but addressable and do not invalidate the paper's core claims. With the suggested additions, this would be a strong paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>