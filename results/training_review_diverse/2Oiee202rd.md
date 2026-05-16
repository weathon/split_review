## Summary

This paper proposes PerceptionCLIP, a training-free, two-step zero-shot classification method for CLIP. Inspired by human visual perception, it first infers contextual attributes (e.g., background, orientation) from the image using CLIP's own scoring, then conditions the class prediction on those inferred attributes. The method is evaluated across 11 datasets and shows consistent improvements over simple template and prompt ensembling baselines, with particularly notable group robustness gains (19% worst-group accuracy gap reduction on Waterbirds).

## Strengths

- **Novel and well-motivated approach.** The idea of explicitly structuring CLIP prompts around contextual (class-independent) attributes, inferring them using CLIP itself, and then conditioning classification on them is a clean, training-free extension that goes beyond ad-hoc template design. This two-step pipeline is conceptually elegant and grounded in an analogy to human perception.

- **Controlled experiments validate the core mechanism.** The synthetic-transformation experiments on ImageNet (Table 1) provide clear causal evidence that conditioning on ground-truth contextual attributes improves accuracy, while wrong or random attributes do not. Grad-CAM visualizations (Figure 3) further confirm that correct conditioning shifts attention from spurious background features to core object features.

- **Demonstration that CLIP can infer contextual attributes without external supervision.** The ~74% binary inference accuracy on synthetic ImageNet transformations (Table 2) shows that CLIP possesses this capability without any additional training or external knowledge, which is a necessary precondition for the method's feasibility.

- **Compelling group robustness results.** The 19% gap reduction on Waterbirds and 7% on CelebA (with ViT-L/14) are practically meaningful. These results directly address a known weakness of CLIP — reliance on spurious correlations — and the improvements are larger than those typically reported for training-free debiasing methods.

- **Theoretical connection to prompt ensembling.** The paper shows that the single-step version of PerceptionCLIP mathematically coincides with prompt ensembling when attribute combinations are used as templates (Section 6). This provides an explanation for why prompt ensembling works and justifies a more systematic construction of prompts.

## Weaknesses

### Fatal
None.

### Major
- **No comparison to class-specific attribute methods.** The paper's related work discusses methods that use LLM-generated class-specific descriptions (Menon et al., Pratt et al.) and positions contextual attributes as a different dimension. However, no experiment compares PerceptionCLIP to any class-specific description method. Without this comparison, the reader cannot isolate whether the observed improvements come from using attributes at all or from the specific choice of *contextual* (class-independent) attributes. This is a structural gap in evaluation that makes it harder to assess the paper's distinctive contribution.

- **Manual construction of dataset-specific contextual attributes limits the generality claim.** The paper constructs attribute sets manually per dataset (e.g., *image source* for EuroSAT, *cuisine* for Food101, *background* for Waterbirds). While acknowledged, this is treated as a practical detail rather than a significant limitation. For the group robustness experiments, the known spurious feature (background/water) is explicitly included as an attribute, which raises questions about how the method would perform when the spurious feature is unknown. The paper's claim of a "general zero-shot method" is softened by this per-dataset engineering.

### Minor
- **Missing attribute inference accuracy on group robustness datasets.** The paper reports ~74% binary inference accuracy on synthetic ImageNet transformations but does not report CLIP's accuracy at inferring the spurious attribute (background for Waterbirds, gender for CelebA) on those specific datasets. Since the method's mechanism depends on correctly inferring these attributes, this is an evidential gap. The paper would be stronger by directly verifying that CLIP's attribute inference is reliable on the exact datasets where the conditioning is applied.

- **No error bars or variance estimates.** All results appear to be from single runs. Given that gains on several datasets are modest (1–3%), confidence intervals or multiple seeds would help assess whether the improvements are statistically meaningful. While single-run evaluation is not uncommon in zero-shot CLIP benchmarks, the group robustness results would particularly benefit from variance estimation.

- **Computational cost is not discussed.** The method computes CLIP(y,z;x) for every class-attribute combination. With 1000 classes and 10 attribute values, this is 10,000 forward passes per image. A brief analysis of runtime or scalability would help practitioners assess practical applicability.

- **Sensitivity to the annotation function α is acknowledged but not analyzed.** The paper uses a distribution over descriptions to mitigate sensitivity to phrasing, but provides no analysis of how different phrasings or description distributions affect results. A concrete example or small ablation would clarify this practical consideration.

### Trivial
None.

## Nice-to-Haves

- An ablation where a fixed, generic attribute set (e.g., {background, orientation, lighting, color}) is applied across all datasets, to test whether the method's generality holds without per-dataset engineering.
- A comparison showing whether conditioning on *all* available attributes (including potentially irrelevant ones) degrades performance, or whether the method naturally ignores irrelevant attributes.
- An analysis of runtime or practical scalability to help readers assess deployment feasibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **The criticism that "the paper should clarify whether experimental results reflect the two-step or the single-step version":** The paper clearly describes both versions, shows the simplification from two-step to single-step (lines 300–303), and separately evaluates temperature-based intervention (Section 7.1, Table 2). This is adequately clarified.
- **The criticism that "Table 4 does not specify which attributes were used for each dataset":** The paper includes a table of contextual attributes via `\input{tables/factors_distri}` which exists in the original submission. The parser stripped this, but it is present in the paper.
- **The criticism about synthetic transformations being "limited to attributes that can be applied globally via image processing":** These are proof-of-concept experiments; the paper also evaluates on real-world attributes (background, gender, cuisine) in the main experiments.
- **The criticism about ClassAttr vs PureAttr not being systematically compared:** The paper reports both methods achieve ~74% accuracy on the attribute inference task (Table 2), providing a direct comparison on that task.
- **The criticism that conditioning on "wrong attribute values" is an unfair comparison:** This is an ablation study, not a baseline comparison. The paper explicitly positions it as ablation ("last two are for ablation") to show the specificity of the benefit.
- **The criticism requesting prompt-tuning baselines (WaffleCLIP, DCLIP):** These methods are in a different class (they require training or per-dataset tuning). The paper's baselines (simple template, 80-template ensembling) are the standard zero-shot comparisons for CLIP.

## Novel Insights

The reviews surface a tension that the paper does not fully confront: the method's success on group robustness tasks depends on knowing *which* contextual attribute is spurious and explicitly conditioning on it. On Waterbirds, the known spurious feature (background) is used as the contextual attribute. This makes the group robustness evaluation somewhat circular — the method works because the attribute the authors chose to condition on happens to be the exact one causing the bias. A more compelling evaluation would show the method reduces spurious correlations even when the spurious attribute is *not* known in advance, by conditioning on a broad set of contextual attributes and relying on the marginalization to down-weight the spurious one. The paper's current design does not test this stronger claim.

## Suggestions

1. **Add a comparison to class-specific description methods** (Menon et al., 2022; Pratt et al., 2022). A simple reimplementation using GPT-generated class descriptions would isolate whether the benefit is from the use of attributes at all or from the specific choice of contextual attributes. This is the single most important addition.
2. **Report CLIP's attribute inference accuracy on Waterbirds and CelebA** directly, to verify the claimed mechanism on the exact datasets where it matters most.
3. **Test the method with a fixed, generic attribute set** (e.g., {background, orientation, lighting}) across domain-specific datasets without per-dataset engineering, to demonstrate generality more convincingly.
4. **Add confidence intervals or standard deviations** (at least for the group robustness and main zero-shot results) to establish statistical significance.

## Score and Decision

**Originality:** 7/10 — The two-step inference of contextual attributes from CLIP itself, without training, is a genuinely novel angle on zero-shot classification.

**Importance of question:** 7/10 — Improving CLIP's zero-shot performance and reducing spurious correlations are practically important and well-motivated.

**Claims well supported:** 6/10 — The core claims are supported by evidence, but the missing comparison to class-specific methods and the manual attribute construction leave significant gaps.

**Soundness of experiments:** 5.5/10 — The controlled experiments are well-designed, but the evaluation lacks error bars, omits a relevant baseline family, and does not verify the mechanistic claim on the group robustness datasets.

**Clarity of writing:** 8/10 — The paper is clearly written, the method is well-explained, and the motivation from human perception is compelling.

**Value to community:** 6/10 — The core insight is useful and the group robustness results are practically relevant, but the community value is limited until the generality claims are more rigorously evaluated.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>