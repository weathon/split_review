Now I have a thorough understanding of the paper and can verify the claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper converts images to Scalable Vector Graphics (SVG) text and feeds them to LLMs (primarily GPT-4, also Vicuna) to perform visual tasks without a visual encoder. It evaluates across three task categories: visual reasoning on Sort-of-CLEVR, image classification under distribution shift (Colored-MNIST), and generative visual prompting. The results show that LLMs can answer visual reasoning questions at ~77% accuracy, exhibit strong OOD robustness (Vicuna+SVG achieving 92.9% on CMNIST-B vs 73.0% for ConvNeXt), and can generate/edit SVG images from prompts.

## Strengths

- **Novel use of SVG as a bridge between images and LLMs.** Converting images to XML-based vector graphics is an underexplored approach, and the paper provides a systematic evaluation across discriminative and generative tasks, going beyond the qualitative demonstrations in Bubeck et al. (2023). The paper is transparent about what it is doing and why.

- **Compelling OOD robustness result.** On Colored-MNIST-B (both foreground and background vary), Vicuna finetuned on SVG-converted MNIST achieves 92.9% accuracy versus 73.0% for ConvNeXt trained on PNGs (Table 2). This gap is large and suggests that the SVG representation does genuinely help models prioritize shape over color/background, which is a practically relevant finding.

- **LLMs can perform visual reasoning competitively without task-specific training.** GPT-4 with chain-of-thought achieves 76.7% on Sort-of-CLEVR vs. 81.7% for a trained Relation Network, and drops only to 71.7% under shape distribution shift while Relation Network collapses to 42.5% (Table 1). This is a non-trivial finding — it demonstrates that an LLM processing SVG text can match (and in OOD settings, surpass) explicitly trained models.

- **Breadth of exploration.** The paper covers visual reasoning, few-shot classification with distribution shift, and generative prompting, providing a broader picture than most prior work using text-based image representations.

- **Honest limitations section.** Section 4 candidly acknowledges SVG's loss of fine details for photographic content, prohibitive sequence lengths for detailed SVGs, and LLMs' struggles with low-level manipulations like rotation and scaling.

## Weaknesses

### Fatal

None.

### Major

- **The experimental design confounds input representation with model capability.** The central comparison in Section 3.1 pits LLMs receiving structured SVG descriptions (explicit coordinates, colors, shapes) against vision models receiving noisy pixels. Unsurprisingly, an LLM with chain-of-thought can parse explicit XML and compute spatial relations. The paper attributes this to LLMs having "much complex models" or "world models," but the evidence is equally consistent with the LLM simply reading explicit instructions embedded in the SVG code. The OOD generalization experiment in Section 3.2 has the same confound: SVG explicitly separates shape (path data) from color (fill attribute), while ConvNeXt must disentangle pixels. The robustness difference may reflect a cleaner input representation rather than LLM reasoning. The paper needs control conditions that isolate the LLM's contribution — for example, comparing LLM+SVG against a simple MLP or rule-based parser on the same SVG features — before attributing results to LLM "understanding."

- **Visual prompting experiments lack baselines.** Section 3.3 reports GPT-4's mIOU scores (38.2–83.5) on six synthetic tasks but provides no baselines whatsoever: no random-chance estimate, no rule-based script that directly manipulates SVG color/size attributes, no comparison against a smaller LM or even a non-LLM SVG parser. Without these, the reader cannot determine whether GPT-4 is performing non-trivial reasoning or simply reflecting the fact that these SVG transformations are mechanically straightforward (e.g., replacing a fill color value). The qualitative extrapolation examples (Figure 5) are interesting but presented without failure cases or quantification, making cherry-picking a concern.

### Minor

- **Small evaluation scale and no statistical rigor.** The visual reasoning evaluation uses only 120 examples (acknowledged as cost-driven), and the Mini-MNIST evaluation uses 100 images. No confidence intervals, error bars, or variance estimates are reported anywhere. Given the small samples, a 5–10% accuracy swing could change relative rankings. This does not invalidate the results but limits their precision.

- **LLaVA is listed as an analyzed method but its results are not reported or discussed.** The paper names LLaVA among the LLM methods in Section 3.1 but never presents its accuracy in Table 1 or explains its omission. If LLaVA results were poor, that is still informative and should be included or explained.

- **The paper's framing around "visual understanding" is imprecise.** The title and abstract claim LLMs can "understand images," but what is actually demonstrated is that LLMs can parse SVG text and answer relational questions about explicitly enumerated geometric objects. This is interesting and non-trivial, but it conflates reasoning about a symbolic scene description with the kind of perceptual understanding humans or vision models achieve from pixels. The conclusion's phrase "some ability understand and manipulate images" is more measured, but the overarching rhetoric leans toward a stronger interpretation than the evidence supports. A reframing around "symbolic visual reasoning via structured scene descriptions" would be more accurate.

### Trivial

None.

## Nice-to-Haves

- A comparison against LIFT (Dinh et al., 2022), which feeds pixel sequences as text, would help isolate whether SVG's structured format specifically helps or whether any text-based representation suffices.
- Testing on natural images (e.g., a subset of ImageNet converted to SVG) would clarify the practical scope of the approach, though the authors acknowledge SVG's limitations for photographic content.
- A comparison against multimodal models like GPT-4V on the same tasks would directly test whether SVG preserves task-relevant information compared to native image input.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The paper does not describe how Vicuna is finetuned on SVG text"** — The paper states that details are in the supplementary materials (line 102). Per instructions, appendix content is stripped by the parser.
- **"The prompt structure is described but not given in full"** — The paper describes the prompt structure; full verbatim prompts are a standard deferral to supplementary materials.
- **"Cherry-picking" accusations for qualitative results** — The critic's claim that "the ambiguity case shown could be cherry-picked" is speculative and not evidence-based.
- **Criticism that the paper "dismisses" LIFT** — The paper simply distinguishes its SVG-based approach from LIFT's pixel-value approach, which is a fair differentiation, not a dismissal.
- **"Missing comparison against LIFT's approach"** — This is a suggestion for improvement, not a weakness of the presented experiments.
- **Various formatting/style nitpicks and reproducibility complaints about undisclosed hyperparameters** — These either misunderstand the paper or concern details standardly deferred to appendices.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface issues the paper itself partially acknowledges (limitations of SVG for photos, cost constraints) and raise the central confound concern, which is the most useful critical insight: that the paper's framing systematically attributes to LLM reasoning what could be an artifact of SVG's structured representation. This is a valid point but one the paper could address with additional controls rather than a fundamental invalidation.

## Suggestions

1. **Add control experiments to isolate the LLM's contribution.** Compare LLM+SVG against (a) a rule-based SVG parser that extracts objects and applies simple heuristics for relational questions, and (b) a small MLP trained on SVG-derived features (e.g., number of paths, bounding box coordinates, color values). If the LLM significantly outperforms these baselines, the claim of LLM reasoning is strengthened.
2. **Add baselines to the visual prompting experiments.** Report random-chance mIOU, a simple script that copies color/size attributes from the source, and ideally a non-LLM SVG manipulation baseline.
3. **Reframe the contribution precisely.** The paper's strongest empirical finding is that LLMs can reason about structured SVG scene descriptions — this is a meaningful contribution on its own. The paper would benefit from dialing back the "visual understanding" language and instead emphasizing the more defensible claim about symbolic visual reasoning via SVG.
4. **Report confidence intervals or variance.** Even with 120 examples, bootstrap confidence intervals would give readers a sense of the uncertainty.

## Score and Decision

This paper tackles an interesting question with a creative approach and produces several genuinely interesting empirical results — particularly the OOD robustness findings. However, the central weakness is that the experimental design does not adequately disentangle whether the positive results come from LLM reasoning or from the privileged structured input (SVG), and the visual prompting experiments lack even basic baselines. These are substantial but addressable issues. As submitted, the evidence does not fully support the interpretive claims made.

**Score:** 5.5

**Decision:** Reject

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>