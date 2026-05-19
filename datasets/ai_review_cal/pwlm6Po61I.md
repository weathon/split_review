- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6
Now I have a thorough understanding of the paper and both reviews. Let me construct the consolidated review.

---

## Summary

This paper investigates whether off-the-shelf LLMs (GPT-4) can perform visual understanding tasks when images are converted to SVG, a text-based XML representation of shapes, lines, and colors. The authors evaluate on three families of tasks: visual reasoning (Sort-of-CLEVR), out-of-distribution classification (Colored-MNIST variants), and generative visual prompting (synthetic shape transformations). The core finding is that LLMs processing SVG can achieve competitive performance on these tasks and show some robustness to distribution shifts.

## Strengths

1. **Interesting and timely research question.** The paper probes whether LLMs—which have never been trained on visual data—can process visual information when given a suitable textual bridge (SVG). This contributes to the ongoing debate about whether LLMs learn "world models" that extend beyond pure text.

2. **Comprehensive evaluation across multiple visual task families.** Rather than testing on a single task, the paper covers visual reasoning (Sort-of-CLEVR), OOD classification (Colored-MNIST), and generative visual prompting. This breadth gives a more complete picture of what SVG-as-bridge enables.

3. **GPT-4 with chain-of-thought achieves high accuracy on visual reasoning and shows robustness to distribution shifts.** In Table 1, GPT-4-CoT reaches 87.5% in-distribution on Sort-of-CLEVR and maintains strong performance under shape and color shifts (where trained models degrade notably). This demonstrates that structured SVG descriptions combined with LLM reasoning can handle relational questions and generalize beyond training distributions.

4. **Style and content extrapolation results are genuinely interesting.** Section 3.3.1 shows that GPT-4 can infer stylistic conventions from SVG examples (e.g., letter styles) and identify mathematical operations applied to SVG number pairs, producing coherent outputs. These qualitative demonstrations go beyond simple color/size changes and suggest richer reasoning capabilities.

## Weaknesses

### Major

- **Confounded comparisons undermine the strongest comparative claims.** The paper states that GPT-4-CoT "surpasses the performance of a model explicitly trained for this task" (Relation Network) and that "SVG representation shows better performance compared to the closed-set trained model." However, these comparisons confound input modality with model architecture: the LLM receives explicit SVG code with named shapes, coordinates, and colors, while the trained models receive raw pixels. The LLM's task is closer to structured query parsing and arithmetic than to "visual understanding." Similarly, in Table 2, fine-tuned Vicuna (on SVG) is compared to ConvNeXt (on pixels) — the different input modalities make it impossible to attribute the performance gap to any particular capability of the LLM. The paper partly acknowledges this framing ("the best case scenario might be when images...have the locations of certain shapes embedded in their XML code") but the claims are worded more strongly than the evidence supports.

- **Small evaluation set (120 examples) for the visual reasoning task with no confidence intervals.** The central comparative claim about Sort-of-CLEVR rests on 120 test examples, with no error bars, standard deviations, or multiple trials reported. For a claim that a zero-shot LLM "surpasses" a method explicitly trained on this task, the evidential base is thin — moderate sampling noise could change the method ordering. The authors acknowledge API costs as the reason, but this does not mitigate the evidential gap for a headline claim.

- **No baselines reported for the visual prompting task (Table 3).** The paper reports GPT-4's mIOU on six transformation tasks (color, size, color+size combinations) but provides no reference point — neither the original baselines from Bar et al. (2022) nor simple heuristics (e.g., copy the query shape and apply the average color shift). Without baselines, it is unclear whether the reported mIOU values (e.g., 73.7 for size-color) represent genuine capability or are unremarkable.

### Minor

- **The tasks are simple synthetic graphics where SVG provides an explicit, near-complete description of all relevant attributes.** Sort-of-CLEVR uses six objects with two shapes and six colors; MNIST digits are simple strokes; the visual prompting tasks involve basic shape transformations. Converting these to SVG produces clean XML where positions, shapes, and colors are directly named as attributes. The LLM's job is substantially easier than any pixel-based vision task—it reduces largely to parsing structured data and performing elementary operations. The paper partially acknowledges this (Section 4 discusses SVG's limitations with photographs and fine detail) but the broader claim about LLMs "understanding images" outpaces what the experimental setup can demonstrate.

- **The comparison between Vicuna (fine-tuned on SVG) and ConvNeXt (fine-tuned on pixels) in Table 2 confounds model and modality.** While the paper's motivation is to test whether SVG "prioritizes shape over color," the experimental design cannot isolate whether the advantage comes from the SVG representation itself, the different model architecture, or the massive pretraining of Vicuna. An ablation where ConvNeXt or a comparable model is trained on *rendered* SVG images would help disentangle these factors.

### Trivial

- Table 2 is described as evaluating "Mini-MNIST dataset, which comprises 100 images" for GPT-4, but it's unclear whether this is the same 100 images used across settings or a subset. Clarify the evaluation sizes.

- The paper mentions "LVM" (large vision model) and "LLM" somewhat interchangeably in the introduction but never defines LVM clearly.

## Nice-to-Haves

- **A controlled comparison within the same modality** — e.g., training a small Transformer on SVG tokens from scratch and comparing to GPT-4 — would strengthen the attribution of the LLM's success to its reasoning capabilities rather than just the structured input format.
- **Confidence intervals or bootstrapped error bars** on the 120-example visual reasoning results, and ideally a larger evaluation set, would substantially increase confidence in the comparative claims.
- **Ablation experiments** — e.g., feeding the LLM an inferior text-based representation (raw pixel values as in LIFT) or a degraded SVG — would isolate the benefit of SVG's structural encoding.
- The vicuna fine-tuning details, prompts, and SVG conversion specifics are referenced as supplementary; those should be included in any camera-ready version for reproducibility.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The SVG conversion algorithm for MNIST is not described"** and **"Sample prompts are not shown"** and **"Vicuna fine-tuning details not reported"** → The paper explicitly states these are in the supplementary materials. The parser strips supplementary sections from all papers; they exist in the original submission.
- **"Missing related works"** → Per policy, missing related works should not be mentioned as we cannot verify their absence.
- **"Exact SVG code for a Sort-of-CLEVR image is not given"** → Not standard practice to include full SVG code for every image; this is a presentational nitpick.
- **"No discussion of computational cost"** → This is a nice-to-have suggestion, not a weakness.
- **"Testing on harder datasets"** (from Strengthening section) → Scope-creep; the paper is an initial exploratory study on synthetic data and acknowledges this limitation.
- **Certain strengths from Strength Finder** — The strength "Explicit differentiation from prior representation choices" is generic framing (the paper does what it claims, but this is not an empirical strength). The claim about "Style and content extrapolation beyond simple transformations" is concrete and kept above.
- **"Prompt sensitivity not discussed"** → This is speculative (no evidence the results are brittle) and falls outside the paper's scope as an initial exploration.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's central observation — that the comparisons are confounded because the LLM receives structured SVG code while baselines receive pixels — is a valid methodological critique but does not constitute a novel insight about the paper's findings; it is an accurate description of a limitation the paper partially acknowledges but does not fully grapple with. The strength finder's observations support the paper's own framing without adding new perspective.

## Suggestions

1. **Calibrate the claims to match the evidence.** The paper's most valuable finding is that LLMs can do reasonably well on synthetic visual tasks when given SVG — a genuine and interesting empirical observation. However, claims about "surpassing" trained models, "understanding images," or possessing "complex world models" are not adequately supported given the confounded comparisons. Reframing the paper as an exploratory study of *what SVG-as-bridge enables* rather than as a demonstration that LLMs beat vision models would better match the evidence.

2. **Add baselines for the visual prompting task.** Without any reference point (not even simple heuristics), Table 3 reports numbers in a vacuum. Adding results from Bar et al. (2022) or a trivial copy-paste baseline would significantly strengthen this section.

3. **Include error bars or multiple trials** for the small-sample visual reasoning results. Even bootstrapped confidence intervals from the 120 examples would help the reader assess reliability.

4. **Add a controlled comparison on the same input modality** — e.g., train a small Transformer directly on SVG tokens — to disentangle whether the LLM's success is due to its reasoning capability or simply the expressiveness of SVG as an input format.
