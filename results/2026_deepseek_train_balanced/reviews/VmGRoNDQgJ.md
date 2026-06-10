## Summary

This paper introduces Influencer Backdoor Attack (IBA), a backdoor attack on semantic segmentation where a trigger placed on *non-victim* pixels indirectly causes misclassification of all victim-class pixels (e.g., a Hello Kitty sticker on a road causes cars to be classified as road). Two techniques are proposed: Nearest Neighbor Injection (NNI), which places the trigger adjacent to victim pixels, and Pixel Random Labeling (PRL), which introduces random label noise on non-victim pixels during poisoning to improve attack success regardless of trigger-victim distance. Experiments on PSPNet, DeepLabV3, and SegFormer across Cityscapes and PASCAL VOC show the attack works, with the distance ablation being the strongest evidence.

## Strengths

1. **Novel threat model distinct from prior segmentation backdoor attacks**: Unlike Li et al. (2021) which statically places a black line at a fixed position, or Mao et al. (2023, OFBA) which places the trigger on the victim class itself, IBA allows trigger placement on any non-victim pixels and must indirectly influence victim pixels via context aggregation (Section 2). This is a more realistic scenario for applications like autonomous driving (e.g., a roadside sign causing cars to disappear), and the paper explicitly acknowledges this distinction.

2. **PRL maintains high ASR across arbitrary trigger-victim distances**: Table `exp:dis` shows that at 5% poisoning, PRL achieves ~91% ASR across all distance ranges (0–60 to 120–150 pixels), while NNI drops from 82.45% to 45.62% and Baseline drops to 54.74%. At 1% poisoning, the advantage is even starker: PRL maintains ~65–68% ASR across all distances while NNI collapses to 9.44% at far distances. This convincingly demonstrates that PRL solves the practical constraint of uncontrollable trigger placement — a problem no prior segmentation backdoor attack addressed.

3. **Systematic ablation of PRL label choices validates the design choice**: Figure 6 tests four relabeling strategies (null, fixed single class, all dataset classes, same-image classes) and shows that only the proposed same-image-class strategy yields continuous ASR improvement without degrading CBA/PBA. The null and single-class strategies even hurt ASR, confirming the design is non-trivial and empirically grounded.

4. **NNI demonstrates substantial robustness to pruning defense**: Table `tab:defense` shows NNI loses only 1.94% ASR when pruning 30/256 channels (from 95.46% to 93.52%), whereas Baseline drops 8.78% (from 93.04% to 84.26%). Under fine-tuning with 10% clean data, NNI retains 55.08% ASR while Baseline collapses to 7.70%. This quantifies a clear advantage under common post-processing defenses.

## Weaknesses

### Fatal

None.

### Major

1. **Real-world experiment uses model predictions as pseudo-ground-truth (circular evaluation)**: Line 216 states: *"We recorded videos, extracted 265 frames and processed them using benign DeepLabv3 model to obtain clean and poisoned labels."* The "ground truth" for the real-world scene is produced by the **same model architecture** (DeepLabV3) under attack, not by human annotation or an independent sensor. The reported ASR of 60–64% thus measures the *disagreement* between the backdoored model and the clean model on car pixels — not actual misclassification of true car pixels against ground truth. A backdoored model that makes slightly different errors than the clean model would appear to have high ASR under this protocol. This undermines the paper's claim of "real-world applicability" (abstract, line 217). The experiment could still be reported as a preliminary demonstration of trigger-induced prediction shift if the circularity is explicitly acknowledged, but as written the methodology does not support the claim.

2. **PRL's claimed mechanism ("better context aggregation") is asserted without supporting evidence**: The paper repeatedly claims PRL makes the model "learn a better context aggregation ability" (line 113) and "take more information from the contextual pixels" (line 113). The stated rationale is that random relabeling forces the model to "predict labels of other classes of the same image" (line 113). However, no analysis is provided that distinguishes this mechanism from a simpler alternative: the added label noise desensitizes the model to correct label assignments, making all pixel predictions less confident and therefore easier to flip by the trigger. The paper presents no attention maps, receptive field statistics, prediction entropy measurements, or controlled experiments (e.g., does PRL applied during *clean* training improve segmentation? A genuine context aggregation improvement should.) to support the claimed mechanism. Since PRL is one of the paper's two main technical contributions, this evidential gap leaves its explanatory story on speculative ground — the empirical result is clear, but the *why* is unvalidated.

### Minor

3. **Full quantitative results (PBA, CBA) across the claimed evaluation scope are not tabulated**: The paper claims experiments on "PSPNet, DeepLabV3 and SegFormer" and "PASCAL VOC 2012 and Cityscapes" (abstract). However, the only detailed table reporting ASR, PBA, and CBA together (Tab. `deep_cs_baseline`) covers only DeepLabV3 on Cityscapes. Results for VOC and for PSPNet/SegFormer are shown only in Figure 4 (ASR plots) and described narratively (line 151). While the main ASR trend is visible in the figure, the absence of tabulated PBA and CBA for other model×dataset combinations makes it harder to verify that benign accuracy is preserved across all claimed settings. A table for VOC would substantiate the generalization claim.

4. **Defense evaluation is narrow and the narrative could better contextualize absolute effectiveness**: The paper tests only two defenses (fine-tuning and pruning). Fine-tuning with 10% clean data reduces baseline ASR from 93.04 to 7.70 (a 92% reduction) — the baseline IBA is highly vulnerable to even simple fine-tuning. NNI's ASR drops from 95.46 to 55.08 (42% reduction) under the same defense. The paper frames NNI as "more robust," which is true relative to baseline, but both attacks are substantially degraded by a standard, simple defense. The paper acknowledges exhaustive defense adaptation is out of scope (line 265), but the framing could better contextualize the *absolute* effectiveness of the defenses rather than emphasizing only the relative ranking.

### Trivial

None.

## Nice-to-Haves

- A sweep over the PRL relabeling count hyperparameter (currently fixed at 50,000) with ASR/PBA/CBA jointly reported — Figure 6 shows only ASR for the label-choice ablation, not full metrics across relabeling counts.
- Variance/error bars for the main results table (Tab. `deep_cs_baseline`) to enable meaningful comparison of small differences between methods, since the distance experiment already reports mean and std of 3 runs.
- Clarify in Algorithm 1 that the pseudocode returns the eligible injection area and distance map, but the selection of the single injection point (line 89: "the pixel with the smallest distance value is selected") is not reflected in the pseudocode logic.

## Removed Points

- **"No quantitative comparison with prior segmentation backdoor attacks (Li et al. 2021, Mao et al. 2023)"** — The paper correctly identifies that these works use fundamentally different trigger designs (fixed-position black line; trigger on victim class itself). Comparing ASR across fundamentally different threat models with different trigger designs, trigger sizes, and placement constraints is not a straightforward apples-to-apples comparison. The paper's contribution (IBA with non-victim pixel trigger) is a different attack vector from these prior works. This is scope creep rather than a missing baseline. **REMOVED.**

- **"The broken LaTeX reference on line 185"** — This is a PDF/parser artifact. The original submission does not have this issue. **REMOVED.**

- **"PRL relabeling quantity sensitivity"** framed as a core weakness — The paper does not show a full sweep over the 50,000-pixel hyperparameter with all metrics, but Figure 6 does vary the count and shows ASR trends. Demoted to Nice-to-Have. **MOVED.**

- **"Existing backdoor attacks like BadNets... classification models have a sample-agnostic goal" cited as unclear — Not a weakness, this is correct background context. **REMOVED.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the real-world experiment**: Either (a) obtain human-annotated ground truth for the 265 frames, or (b) clearly acknowledge the circularity and reframe the experiment as a proof-of-concept demonstration of trigger-induced *prediction shift* (i.e., the backdoored model disagrees with the clean model specifically when the trigger is present) rather than a rigorous evaluation of real-world attack success.

2. **Validate the PRL mechanism**: Provide mechanistic evidence — for example, measure prediction confidence/entropy on non-victim pixels with and without PRL, or test whether PRL applied during training of a *clean* model (without any backdoor trigger) improves or degrades segmentation performance. If PRL genuinely improves context aggregation, it should help clean segmentation; if it just desensitizes the model, it should hurt it.

3. **Add a table for VOC results**: A table reporting ASR, PBA, and CBA for DeepLabV3 on PASCAL VOC (analogous to Tab. `deep_cs_baseline`) would substantiate the claim that IBA generalizes beyond Cityscapes.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>