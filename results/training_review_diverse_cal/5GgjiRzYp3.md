Now I have a thorough understanding of the paper and the reviews. Let me produce the consolidated review.

## Summary

This paper introduces 3D Intention Grounding (3D-IG), a new task where AI agents must detect objects in 3D scenes solely from free-form human intention text (e.g., "I want something to support my back") without referential cues. The authors contribute: (1) the Intent3D dataset with 44,990 intention texts over 209 object classes from 1,042 ScanNet scenes, constructed using GPT-4 with careful filtering and manual cleaning; (2) comprehensive baselines spanning expert models (BUTD-DETR, EDA), a foundation model (3D-VisTA), and an LLM-based model (Chat-3D v2); and (3) IntentNet, a method incorporating Verb-Object Alignment, Candidate Box Matching, and Cascaded Adaptive Learning. IntentNet outperforms all baselines by large margins (e.g., +11.06 Top1-Acc@0.25 on the test set).

## Strengths

1. **Well-motivated and clearly differentiated new task.** The paper provides a clean conceptual distinction between 3D Visual Grounding (which relies on human-provided references naming category/attributes/location) and 3D Intention Grounding (where the model must infer the target solely from intention text). This distinction is clearly illustrated in Fig. 1 and defended throughout. The task fills a genuine gap — existing 3D-VG assumes the user can observe and reason about the scene, which may be infeasible in many real-world scenarios.

2. **Large-scale, carefully constructed benchmark (Intent3D).** The dataset construction pipeline (Section 3.2) is systematic and principled: three filtering criteria (common, non-trivial, unambiguous objects), two-stage GPT-4 prompting designed to avoid category/location leakage, and manual cleaning. The resulting diversity (1,568 distinct verbs, 2,894 distinct nouns) significantly exceeds what would be expected if intentions were trivial paraphrases of category names, supporting the claim that the data captures genuine intention language.

3. **IntentNet achieves large and consistent gains.** On the test set, IntentNet achieves 58.92 Top1-Acc@0.25 and 44.01 AP@0.25, outperforming the second-best baseline (BUTD-DETR) by +11.06 and +12.60 absolute points, respectively. The gains are consistent across both val and test sets and across both Top1-Acc and AP metrics. The ablation study (Table 4) confirms each component contributes meaningfully — removing verb alignment drops Top1-Acc@0.25 from 58.34 to 53.09, and removing the cascaded adaptive learning drops it to 57.39.

4. **Comprehensive baseline coverage.** The paper evaluates four methods spanning three paradigms (expert models trained from scratch, a pretrained foundation model fine-tuned, and an LLM-based model both zero-shot and fine-tuned). This provides a thorough picture of where existing techniques fall short on the new task and highlights that the challenge is not trivial for any existing approach.

5. **Clear ablation studies with qualitative support.** The ablation removes one component at a time from the full IntentNet, and each removal produces a measurable performance drop. The qualitative examples (Fig. 5) visually demonstrate how specific failures arise from missing specific components (e.g., the model without Verb2Obj maps "add" to the wrong target), making the contribution of each component concrete.

## Weaknesses

### Major

1. **The dataset's explicit removal of multi-category ambiguity narrows the task's scope more than the paper acknowledges.** Section 3.2 (criterion 3) states that objects are filtered when multiple categories could satisfy the same intention (e.g., both "TV" and "Monitor" could satisfy "display my chart"). This is a deliberate design choice and the paper is transparent about it. However, this filtering removes the very scenario that constitutes the hardest and most distinctive reasoning challenge in intention grounding: disambiguating between plausible but different object categories that could fulfill the same need. With this filter, the task reduces to: (a) map an intention to a single unique category, then (b) detect all instances of that category. Step (a) is a text-to-category mapping that does not require reasoning about scene content to resolve inter-category competition, and step (b) is standard detection. The paper's framing ("automatically observe, reason and detect the desired target") overstates what the dataset demands. The authors should explicitly acknowledge this limitation, reframe the scope as a simplified starting point, and discuss whether future versions could include ambiguous annotations with multiple valid target categories. This does not invalidate the paper's contribution (the task is still meaningfully different from 3D-VG), but it is a structural limitation that affects how the contribution should be interpreted.

2. **Missing training details for baselines weaken the comparison.** The paper reports that IntentNet is trained for 90 epochs with a specific LR schedule (Section 5.2, line 261–263). However, it does not report how many epochs the baselines (BUTD-DETR, EDA, 3D-VisTA, Chat-3D-v2) were trained, whether the same checkpoint selection criterion (best AP@0.5 on val) was applied uniformly, or whether any hyperparameter tuning was performed for baselines on the Intent3D validation set. The paper states baselines "follow their configuration on ScanRefer" — but ScanRefer is a different task with different data distribution and complexity. Without this information, a reader cannot assess whether the reported gaps partly reflect training length disparities rather than architectural advantage. This is a significant methodological gap in an otherwise thorough evaluation.

### Minor

1. **No analysis of spaCy parser accuracy for verb-object extraction.** The Verb-Object Alignment pipeline (Section 4.3) depends on spaCy POS tagging and dependency parsing to generate training labels for $L_{vPos}$ and the verb-object links used in $L_{voSem}$. Any parser errors propagate into the loss computation as noisy supervision. The paper does not report the parser's accuracy on the dataset, the frequency of parsing failures, or whether the model is robust to such noise. Given that intention texts are free-form and can have complex syntax, this is a blind spot. The ablation shows verb alignment is valuable (5-point drop when removed), suggesting the signal survives noise, but an explicit analysis would strengthen the method.

2. **Cascaded Adaptive Learning is empirically effective but conceptually thin.** The mechanism (Section 4.4) uses a factor $f(x) = \text{sigmoid}(x) + 0.5$ to always amplify later losses when earlier ones are nonzero. The paper motivates this through an "intrinsic priority logic" but does not explain why always *increasing* lower-priority loss weights (rather than, say, curriculum learning or scheduled weighting) is the correct approach. The ablation shows it helps (+0.95 Top1-Acc), but the mechanism remains a heuristic without deeper analysis (e.g., training curves showing the order in which losses decrease with/without cascading). This does not harm the paper's contribution but weakens the claimed "principled" framing.

3. **Qualitative results only compare ablation variants, not baselines.** Figure 5 shows how removing each IntentNet component affects predictions, which is informative. However, the paper does not show qualitative comparisons against the best baselines (BUTD-DETR or 3D-VisTA). Seeing where these baselines fail (e.g., do they detect wrong categories? wrong locations? miss instances entirely?) would help the reader understand what the performance gap actually means in practice.

4. **No limitations discussion.** The paper lacks a section discussing failure cases, dataset biases (e.g., ChatGPT-generated text may have systematic artifacts such as formulaic phrasing), or the generalization to other 3D datasets (e.g., ARKitScenes, Matterport3D). This is common for a first benchmark paper but should still be addressed.

### Trivial

None.

## Nice-to-Haves

- An analysis of spaCy parsing accuracy on the dataset and the model's sensitivity to parsing errors.
- Training curves showing loss trajectories with and without cascaded adaptive learning.
- Reporting recall@k metrics for the multi-instance detection setting.
- A discussion and path toward handling multi-category ambiguous intentions in future work.
- Qualitative side-by-side comparisons of IntentNet vs. the best baseline methods showing failure modes.

## Removed Points

- **Harsh critic's claim that "the 11–12 point gaps... are partly attributable to the fact that IntentNet includes components (by design) that the baselines lack"** — This is circular: asking that baselines be augmented with the authors' novel components and then compared to the same method without those components is asking for a trivial self-comparison. The proper evaluation (which the paper provides) is: existing methods vs. new method with its new components. The ablations isolate the component contributions within IntentNet itself.

- **Harsh critic's suggestion that baselines should include "a version of BUTD-DETR or EDA with the verb-object alignment loss"** — This would essentially be IntentNet without other components, which is already partially covered by the ablations. Requesting this as a baseline comparison conflates "ablation study" with "baseline evaluation."

- **Strength Finder's claim that Cascaded Adaptive Learning is a "principled multi-objective optimization scheme"** — The mechanism is a heuristic (sigmoid-based scaling), and the paper's own framing ("inspired by Focal Loss") is honest about this. Calling it "principled" overstates the contribution. The strength remains as "novel and empirically effective" but the "principled" framing is dropped.

- **Harsh critic's "Other Observations" point about Top1-Acc being inappropriate** — The paper also reports AP, which is the more standard detection metric and is insensitive to the Top1 issue. Both metrics are reported and show consistent trends.

## Novel Insights

None beyond the paper's own contributions. The reviews surface useful refinements (ambiguity filtering narrows scope; baseline training details are missing) but do not reveal a fundamentally new perspective on the work that the authors themselves have not already touched on.

## Suggestions

1. **Reframe the task scope honestly.** Acknowledge explicitly that the current dataset filters out multi-category ambiguity, making 3D-IG in its current form a "single-category intention grounding" benchmark. Propose multi-category ambiguous annotations as future work. This strengthens rather than weakens the contribution by showing the authors understand their own dataset's limitations.

2. **Report training epochs and validation-based early stopping details for all baselines.** Add a column or footnote showing the number of epochs each baseline was trained and confirm that all methods used the same checkpoint selection criterion (best AP@0.5 on val).

3. **Add a brief analysis of spaCy parsing quality.** Report what percentage of intention texts have correct verb identification and verb-object dependency extraction, and discuss whether the model tolerates noisy labels (e.g., by comparing performance when using gold vs. parser-extracted labels on a small subset).

4. **Include at least one qualitative comparison against a top baseline** (e.g., BUTD-DETR or 3D-VisTA) in the main paper or appendix, alongside the ablation visualizations already present.

5. **Add a Limitations section** discussing failure modes, dataset biases from GPT-4 generation, and the scope of the filtered ambiguity.

## Score and Decision

The paper introduces a genuinely new task with a solid dataset and a method that clearly outperforms adapted prior work. The weaknesses are real but manageable: the ambiguity filtering is a scope limitation (not a fatal flaw), and the missing baseline details are fixable. The contribution — a new task, a benchmark dataset, and a strong baseline method — merits acceptance as a first step toward 3D intention grounding.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>