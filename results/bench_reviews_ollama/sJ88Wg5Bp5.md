## Summary
ViDA proposes a dual-branch adapter for Continual Test-Time Adaptation (CTTA) that injects a "high-rank" and a "low-rank" bottleneck branch into a pre-trained backbone, with an uncertainty-driven Homeostatic Knowledge Allotment (HKA) module that fuses the two branches per sample. The method is evaluated on CIFAR10C/100C, ImageNet-C, and Cityscapes→ACDC, including DINOv2/SAM backbones, and reports consistent improvements over CoTTA/VDP/TENT.

## Strengths
- **Architecture-level motivation with quantitative support.** Sec. 3.1 backs the dual-branch design with adjacent-domain JS divergence (Fig. motivation(a)) and intra-class divergence (Fig. motivation(b)), plus CAM visualizations — more grounding than typical adapter papers, even if some conclusions overreach.
- **Broad empirical scope.** Results cover classification (CIFAR10C/100C, ImageNet-C with ResNet50 and ViT-Base), segmentation (Cityscapes→ACDC across 3 cycles), and two foundation backbones (DINOv2, SAM). The ACDC repeated-cycle trajectory (mIoU 61.1 → 62.2 → 62.3, Table 4) is a meaningful stability result where TENT and DePT degrade.
- **Clean component ablation.** Table 6 isolates each branch and HKA (5.1% / 4.6% / +5.1% combined / +2.2% HKA / IHKA worse), and the inverted-HKA control supports the directionality of the gating.

## Weaknesses

### Fatal
None.

### Major
- **The "no extra parameter / no inference cost" claim is incompatible with HKA.** Sec. 3.2 states the branches can be folded into the parent weights by re-parameterization, "which ensures no extra model parameter increase." But Eq. 5 makes $\lambda_h, \lambda_l$ depend on a per-sample MC-Dropout uncertainty $\mathcal{U}(x)$ requiring $m$ stochastic forward passes. Input-dependent fusion weights cannot be folded into parent weights, and Table 6 shows HKA contributes 2.2 of the 12.4 points. The headline efficiency framing is therefore inconsistent with the actual deployed system, and no FLOPs/latency measurement is reported with HKA enabled.
- **"High-rank" is misnamed; the mechanistic story is not what the construction implements.** Sec. 3.2 specifies $W^h_{up}\in\mathbb{R}^{d\times d_h}, W^h_{down}\in\mathbb{R}^{d_h\times d}$ with the stated constraint "$d_h \geq d$", but the example uses $d_h=128$ while ViT-Base has $d=768$ — i.e., $d_h<d$. Both "high-rank" and "low-rank" branches are in fact bottleneck adapters with different bottleneck widths. The qualitative story (high-rank captures domain-specific, low-rank captures domain-shared) is built on top of an inconsistency in the architecture spec, and there is no sweep over $d_h, d_l$ or an equal-parameter single-bottleneck control to show the effect is actually rank-driven rather than width/capacity-driven.
- **The DG experiment does not measure DG in the standard sense.** Sec. 4.5 invokes the LODO protocol (Zhou 2021; Li 2017), but the "10 source / 5 unseen" split (bri., contrast, elastic, pixelate, jpeg) is exactly the **tail** of the standard ImageNet-C corruption sequence used elsewhere, and the Source column matches the last 5 columns of Table 1. This is "stop adapting at corruption 10 and report on the rest," not multi-fold leave-one-domain-out. Contribution 4 (DG ability) is therefore not supported by the protocol that was run.

### Minor
- **Stale/incomplete baseline coverage on headline tables.** Sec. 2 names EcoTTA, RMT, SATA, DePT, and prompt-based methods, but Tables 1–3 omit most of these in most cells (e.g., EcoTTA appears as a single ResNet50 mean with all per-corruption cells "-"; RMT/SATA absent from the CIFAR/ImageNet-C ViT tables). On ResNet50 ImageNet-C the gain over CoTTA is only 1.5 points (62.7 → 61.2).
- **No variance reporting.** All four benchmark tables are single-run point estimates. CTTA gains of 1.5–3% (CIFAR/ACDC) are within the range typically masked by seed/order variability. (Single-run is common in this subfield but is a real weakness given how close some baselines are.)
- **Adapter initialization is under-specified and potentially leaky.** Sec. 4.1 says "we train adapters for several iterations on classification datasets (e.g., ImageNet) to initialize." When the downstream task is ImageNet→ImageNet-C, the data used, the duration, and whether baselines get a comparable warm start are not stated.
- **HKA sensitivity is unexamined.** $\Theta=0.2$ is hard-coded, Eq. 5 is non-smooth at the threshold, and the fusion weights flip discontinuously around it. No sensitivity analysis over $\Theta$ or the MC-Dropout sample count $m$, and no analysis of how often per-sample flips occur.
- **$\mathcal{H}$-divergence argument is loose.** The JS approximation is computed between *adjacent target domains*, not between source and target as in Ben-David. Small adjacent JS is consistent with both "domain-shared features" and "collapsed representations"; the conclusion that this evidences domain-shared knowledge needs a control.
- **Foundation-model setup asymmetry.** Sec. 4.4 fine-tunes a classification head on top of SAM for the source row but does not do the analogous operation for the ViT-Base baseline; the CoTTA −4.3/−0.1 numbers under DINOv2/SAM are unexplained, leaving open whether CoTTA was retuned.

### Trivial
- DINOv2 and SAM citations are swapped in Sec. 4 (the paper cites SAM for DINOv2 and vice versa).

## Nice-to-Haves
- Equal-parameter single-bottleneck adapter control to disentangle "two-branch" from "extra capacity."
- True multi-fold LODO with held-out domains that are not the tail of the training sequence.
- Latency/FLOPs measurement with HKA (MC Dropout, $m$ passes) enabled, alongside an HKA-free "deployable" variant if re-parameterization is to be claimed.
- Per-domain accuracy trajectories for HKA vs. inverted-HKA vs. fixed-$\lambda$.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- Harsh critic's framing that the small ResNet50 ImageNet-C margin (1.5 over CoTTA) is "within typical CTTA noise" — kept as a Minor variance concern, but the absolute claim "comparison favors the proposed method by default" is overstated without a specific noise estimate.
- Strength Finder's generic point that the "problem is important" / sycophantic framings — removed for being non-specific.
- Strength Finder's "inference-time efficiency via re-parameterization" — removed because it conflicts with a verified Major weakness (Issue 1).
- Strength Finder's "domain generalization on unseen corruptions" — removed because the protocol used does not measure DG (verified Major weakness).

## Novel Insights
None beyond the paper's own contributions. The reviews surface internal inconsistencies in the paper rather than novel observations about CTTA.

## Suggestions
- Either drop the "no extra parameter at inference" claim or report a separate fold-able variant where $\lambda$ is fixed at deployment.
- Rename "high-rank" to "wider bottleneck" (or actually instantiate $d_h \geq d$) and add a $d_h, d_l$ sweep plus an equal-parameter single-branch ablation.
- Re-run DG with multi-fold leave-one-domain-out where the held-out set does not coincide with the tail of the corruption sequence.
- Report mean ± std across at least 3 seeds and 2–3 corruption orderings on the headline tables, and add missing baselines (RMT, SATA, EcoTTA, DePT) where source code is available.
- Add sensitivity over $\Theta$ and $m$, and a per-sample flip-rate plot.

---

**Evaluation by axis.** *Originality:* moderate — dual-branch adapter with uncertainty gating is incremental over CoTTA/VDP/AdaptFormer. *Importance:* the CTTA setting is well-motivated. *Claim support:* mixed — empirical gains are real but the headline "no-extra-parameter" and "DG" claims are not supported by the actual construction/protocol. *Soundness of experiments:* broad scope but single-run, with internally inconsistent architecture spec and a DG protocol that is not LODO. *Clarity:* generally readable; motivation section is the strongest. *Value to community:* the dual-branch + uncertainty fusion recipe is reusable, but two of the four stated contributions are over-claimed.

The method is a reasonable empirical contribution and the gains over CoTTA/VDP are non-trivial on ViT-Base ImageNet-C (+6.6) and ACDC (+3.3 mIoU). However, two of the four stated contributions (re-parameterization / no extra parameter; domain generalization) are not actually supported by the construction or protocol used, and the central "high-rank vs. low-rank" mechanistic story rests on a spec that contradicts itself. These are addressable in revision but are substantive enough to weigh against acceptance in current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>