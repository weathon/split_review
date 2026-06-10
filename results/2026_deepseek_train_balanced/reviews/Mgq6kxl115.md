## Summary

This paper proposes Diffusion Bridge Network (DBN), a method to accelerate deep ensemble inference by training a conditional diffusion bridge (based on the I2SB framework) that maps the logit distribution of a single ensemble member to the logit distribution of the full ensemble. By applying progressive distillation, inference is reduced to a single source-model forward pass followed by a single-step diffusion evaluation. Experiments on CIFAR-10, CIFAR-100, and TinyImageNet with ResNet architectures show that DBN achieves better accuracy-to-FLOPs trade-offs than its predecessor Bridge Network (BN) and standard distillation baselines.

## Strengths

1. **Direct logit-space transport eliminates the need for low-loss subspace construction.** Unlike Bridge Network, which requires learning Bezier-curve low-loss subspaces between every pair of ensemble members (Section 2.1), DBN uses the I2SB formulation to directly map a single source model's logit distribution to the full ensemble logit. This avoids the quadratic growth in bridge networks and the extra training cost of subspace fitting (lines 28–31, 113).

2. **Superior accuracy-to-FLOPs tradeoff versus the prior state-of-the-art (BN).** On CIFAR-10 and CIFAR-100, a single DBN achieves "almost DE-3 performance" while BN "struggles to achieve even DE-2 performance with more computational costs" (line 223). The relative FLOPs of "ResNet + 1 DBN" is 1.166 versus "ResNet + 2 BNs" at 1.411 (Section 4.2, line 243). DBN continues to improve accuracy up to ~9 target ensembles while BN saturates at ACC 92.0% and DEE 2 (Fig. 4 discussion, line 243).

3. **Progressive distillation collapses the multi-step diffusion to a single step.** The paper adapts progressive distillation (Salimans & Ho, 2022) to the diffusion-bridge setting (Eq. 9, lines 163–170), enabling inference with a single evaluation of the score network. Without this step, the multi-step ancestral sampling of the diffusion bridge would negate the computational savings. The single-step inference procedure is concretely specified in Eqs. 10–11 (lines 175–179).

4. **Honest empirical capacity characterization of a single DBN.** Section 4.3 (Fig. 5, lines 253–257) explicitly measures how many ensemble members a single DBN can effectively represent, showing it learns "slightly less than three ensembles" vs. BN's cap at two. This quantitative guidance is useful for practitioners deciding how many DBN modules to deploy.

5. **Shared-source multi-DBN composition avoids redundant computation.** When a single DBN reaches its capacity limit, Section 3.5 (lines 181–188) proposes composing multiple DBNs that share the same source model $\theta_1$, so adding extra DBNs does not require recomputing the source feature extractor — a practical engineering design that minimizes additional inference cost.

## Weaknesses

### Fatal
None.

### Major
1. **Poor calibration is noted but neither analyzed nor mitigated, despite being a core motivation for deep ensembles.** The paper transparently states that DBN "shows poor ECE scores even with high performance in the other uncertainty metrics" (Section 4.1, line 223). This is a significant issue: one of the primary reasons to use deep ensembles is improved uncertainty quantification and calibration. The paper offers no analysis of *why* ECE degrades, no attempt to mitigate it (e.g., by temperature scaling the DBN output, adjusting the diffusion noise schedule, or analyzing whether calibration loss is inherent to the diffusion approximation), and no discussion of how this limits practical utility. For a method whose abstract advertises "maintaining accuracy and uncertainty scores," degraded calibration is not a side detail — it directly undercuts the claim that ensemble *behavior* (not just point predictions) is preserved.

2. **The temperature distribution `p_temp` is a critical design choice that is never specified.** The method's source distribution (Eqs. 124–125) is defined as `Z_1 = z_1 / T` where `T ~ p_temp`. This temperature randomization serves two claimed purposes: (i) converting the deterministic source logit into a distribution (required by I2SB), and (ii) preventing the diffusion bridge from collapsing to the identity solution. Both the *shape* of `p_temp` (uniform? log-normal? categorical over a fixed set?) and its *range* are left unspecified. There is no ablation study showing how sensitive results are to this choice. The entire method's behavior depends on this distribution producing the right amount of stochasticity — too little and the bridge collapses to copying the source, too much and the signal is destroyed. This is a concrete reproducibility concern.

### Minor
1. **Training cost is excluded from the efficiency comparison.** The paper frames its contribution as reducing computational cost, but the entire quantitative comparison (FLOPs, #Params) considers only *inference*. Training a DBN requires training a diffusion model (I2SB-style score network) on top of already-trained ensemble members. The conclusion acknowledges that "diffusion models demand a long training time" (line 282), but this is never quantified or compared to baselines. If training FLOPs were included, the picture could shift materially. This does not invalidate the core inference-efficiency claim but leaves the reader without a complete picture of the practical trade-off.

2. **No error bars or variance estimates reported.** For a comparison involving multiple trained models and random seeds (ensembles), reporting standard deviations over runs is standard practice in the field. The absence of any variance information makes it difficult to assess whether reported differences between methods are statistically meaningful.

3. **Evaluation is limited to three image classification benchmarks with ResNet architectures.** Deep ensembles are used across domains (regression, segmentation, NLP, molecular prediction), and the DBN framework — operating on logit and feature spaces — is domain-agnostic in principle. Yet there is no evidence the method transfers. Additionally, there is no out-of-distribution (OOD) detection evaluation, which is one of the principal use cases for deep ensembles and where preserving ensemble behavior matters most.

### Trivial
None.

## Nice-to-Haves
- An ablation study on the `p_temp` distribution (different shapes and ranges) would strengthen reproducibility and help readers understand the method's sensitivity.
- Adding OOD detection experiments (e.g., CIFAR-10 vs. SVHN, CIFAR-100 vs. TinyImageNet-crop) with AUROC metrics would convincingly demonstrate that DBN preserves ensemble uncertainty behavior, not just point predictions.
- Reporting training FLOPs or wall-clock time (even a rough estimate) would give readers actionable information about the practical trade-off.
- A brief diagnosis of the ECE degradation — e.g., does temperature scaling on the DBN output recover calibration, or is the degradation inherent? — would substantially strengthen the paper.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **"BN's quadratic growth is overstated"** (harsh critic): The paper states "the number of BNs to be constructed grows quadratically" (line 28). This is factually correct — with M models, M(M-1)/2 BNs are needed. The critic's point about inference vs. training cost is their own interpretation; the paper does not misrepresent BN. **Removed**: not a valid criticism of the paper.
- **"The I2SB background section is overly detailed"** (harsh critic): This is a presentation preference / style nitpick, not a substantive criticism. **Removed** per formatting/style rules.
- **"Missing table data in parsed text"** (harsh critic): The classification results table is included via `\input{tables/classification}` which is stripped by the parser. The text summary (line 223) provides key results. **Removed**: parser artifact.
- **"DEE metric limitations not discussed"** (harsh critic): The paper cites DEE from Ashukha et al. 2020 as one of several metrics. The critic's concern about known pitfalls is speculative and not specific to this paper's usage. **Removed**: no concrete evidence that DEE is misused here.
- **Strength Finder's generic framing of problem importance**: Removed per instruction to drop strengths that are generic, superficial, or lack specific content. Only the concrete, evidence-grounded strengths are retained above.

## Novel Insights
None beyond the paper's own contributions. The reviews surface no synthesized insight that the paper itself does not already contain or imply.

## Suggestions
1. Diagnose and address the calibration degradation. Report ECE broken down by confidence bin, test whether temperature scaling on the DBN output recovers calibration, and discuss whether the loss is inherent or mitigable.
2. Specify `p_temp` explicitly in the main text (not just the appendix) and provide an ablation showing how results vary with different temperature distributions and ranges.
3. Add OOD detection experiments (AUROC/AUPR) on standard benchmarks to substantiate the claim that DBN preserves ensemble uncertainty.
4. Report training FLOPs or GPU-hours for DBN and all baselines, even as a rough estimate.
5. Include error bars or standard deviations (at least across 3 runs) for all main reported metrics.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>