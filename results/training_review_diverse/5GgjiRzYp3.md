Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces 3D Intention Grounding (3D-IG), a new task where AI agents must detect objects in 3D scenes based solely on human intention text (e.g., "I want something to support my back") rather than referential descriptions that name the target category, attributes, or location. The authors construct the Intent3D dataset (44,990 intention texts, 209 classes, 1,042 ScanNet scenes) using ChatGPT with carefully designed prompts, establish baselines across three method families (expert models, foundation model, LLM-based model), and propose IntentNet — a method that introduces Verb-Object Alignment and Cascaded Adaptive Learning to handle the unique structure of intention language.

## Strengths

- **Novel task formulation with clear practical motivation**: The paper identifies a genuine gap — current 3D-VG requires the human to observe and reason before providing a reference, which is impractical when users are visually impaired, engaged in intensive activities, or otherwise unable to articulate referential descriptions. 3D-IG shifts this reasoning burden to the AI, which is a meaningful and well-motivated redefinition.

- **Large-scale, linguistically diverse dataset**: Intent3D contains 44,990 texts with 1,568 distinct verbs and 2,894 distinct nouns (Figure 2), demonstrating far richer language diversity than existing referential 3D-VG datasets. The construction pipeline (object selection with three filtering criteria, prompt design that explicitly forbids category/location/attribute disclosure, manual cleaning) is well-documented and produces texts that genuinely require independent reasoning.

- **IntentNet's Verb-Object Alignment directly addresses the linguistic structure of intention language**: Unlike referential language where the target is typically a single noun, intention language requires understanding multiple verb–object pairs. IntentNet models this explicitly through verb position prediction ($L_{vPos}$), query-verb contrastive learning ($L_{vSem}$), and verb-modulated query-object alignment ($L_{voSem}$). Ablation (Table 4) confirms removing Verb drops Top1-Acc@0.25 from 58.34% to 53.09%, establishing its critical role.

- **Strong and consistent quantitative improvements across multiple metrics and thresholds**: IntentNet outperforms the best baseline (BUTD-DETR) by +11.22% Top1-Acc@0.25 and +8.05% Top1-Acc@0.5 on the val set, with similar margins on the test set (+11.06% and +10.84%). The method also achieves substantial AP gains (e.g., 27.60% AP@0.5 on test vs. the next best at 13.46%), demonstrating robustness across confidence thresholds rather than just top-1 accuracy.

- **Comprehensive baseline coverage**: The paper evaluates four baselines spanning three distinct methodological families (expert models BUTD-DETR/EDA, foundation model 3D-VisTA, LLM-based model Chat-3D-v2 in both zero-shot and fine-tuned settings), providing a thorough and informative benchmark for the new task.

## Weaknesses

### Fatal

None.

### Major

- **Dataset quality is insufficiently validated given its reliance on ChatGPT generation**: The manual cleaning step is described qualitatively (filtering "gibberish," discarding failed generations, recreating ambiguous cases, regenerating repeats) but never quantified — how many samples were discarded or regenerated, what error types occurred at what rates, and what fraction of the final 44,990 texts required intervention? More critically, there is no human evaluation of the intention-to-object mapping. Without measuring inter-rater agreement on whether a given intention text unambiguously maps to its intended target, the benchmark risks measuring how well models memorize ChatGPT's associations rather than genuine intention understanding. For a dataset that is one of the paper's primary contributions, this level of validation is essential and currently absent. The paper should include at minimum: (i) quantified cleaning statistics, (ii) a human agreement study on a representative sample (200–300 texts) reporting accuracy and ambiguity rates.

### Minor

- **The task distinction from 3D Visual Grounding could be more crisply articulated**: The paper distinguishes 3D-IG from 3D-VG conceptually (Figure 1: human does the reasoning in 3D-VG vs. AI does the reasoning in 3D-IG) and operationally (the prompt explicitly forbids category, location, and attribute mentions). However, the paper does not provide explicit **linguistic criteria** for what makes an expression "intention" vs. "reference," nor does it analyze whether existing 3D-VG datasets contain any intention-like language (even if mixed with referential cues). A sharper definition and a small-scale analysis of existing 3D-VG data would help readers assess the true novelty of the task. This does not undermine the contribution — the dataset construction ensures the practical difference — but the conceptual framing would benefit from more precision.

- **The Cascaded Adaptive Learning mechanism is empirically effective but its design choices are under-explained**: The method uses $f(x) = \text{sigmoid}(x) + 0.5$ to scale each loss by the preceding loss value, with a manually defined priority chain ($L_{vPos} \rightarrow L_{vSem} \rightarrow L_{voSem} \rightarrow L_{box}$). The connection to Focal Loss is tenuous (Focal Loss down-weights easy examples per-sample based on predicted probability; here, a scalar loss value scales another loss irrespective of per-example difficulty). No ablation is provided for the sigmoid offset hyperparameter (0.5), nor are simpler alternatives (fixed weighting, linear decay) compared. The ablation (Table 4, row d vs. e) shows a modest 0.95-point gain on Top1-Acc@0.25 but a notable 3.9-point gain on Top1-Acc@0.5 — the paper would benefit from analyzing *why* the improvement is concentrated at the stricter IoU threshold. This is a minor concern because the mechanism does improve results, but its design is currently a black-box heuristic.

- **No accuracy analysis of the spaCy dependency parsing**: The Verb-Object Alignment module crucially depends on spaCy's part-of-speech tagging and dependency parsing to extract verb positions and verb-object pairs (line 196). Parsing errors on free-form, diverse intention text would cascade into noise in the training signals for $L_{vPos}$, $L_{vSem}$, and $L_{voSem}$. Reporting parsing accuracy on a sample of the dataset would improve reproducibility and help users understand potential failure modes.

### Trivial

- **No limitations or failure cases section**: The paper concludes abruptly (Section 6) without discussing scenarios where IntentNet performs poorly (e.g., ambiguous intentions, rare objects, scenes with many similar instances). This would be a valuable addition, especially for a new task.

## Nice-to-Haves

- **A simple two-stage baseline** that (i) classifies the intention text into an object category (e.g., using a text encoder trained on the 209 fine-grained classes) and then (ii) detects all instances of that category using a pretrained 3D detector. This would separate intention understanding from detection and reveal whether the primary difficulty is in mapping intention to category, localizing multiple instances, or both. Such a baseline would help readers gauge where IntentNet's Verb-Object Alignment actually contributes.

- **Comparison with simpler alternatives for the cascaded adaptive learning** (e.g., fixed weighting, linear decay, or gradient normalization) to better justify the specific design choice.

- **Statistical significance reporting** (variance across runs) would be good practice, though the large performance gaps make this less critical.

## Removed Points

- **"The test set derives from ScanNet's val split" criticism**: The paper explicitly acknowledges this in Section 3.3 (line 130: "Our train set comes from ScanNet's train split, while the val and test sets are derived from its val split"). This is transparently disclosed, not a weakness. Removed per rule: factual correctness.
- **"LLM-based model's low AP may be due to ad-hoc confidence scoring"**: The reviewer acknowledges this as a limitation of the baseline, not a flaw in the paper. The paper already discusses this (line 319: "due to hallucination problems in the LLM..."). Removed per rule: the paper already addresses this.
- **Strength about Cascaded Adaptive Learning being "principled"**: Conflicts with the verified weakness that the mechanism is under-justified. Per rule: when strength and weakness disagree, weakness wins. Dropped.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension worth noting: the paper's core contributions are the task and dataset, yet the dataset quality validation (the primary concern) is the least-developed part of the paper, while the method (IntentNet) — arguably secondary to the task definition — is more thoroughly evaluated. Addressing dataset validation would significantly strengthen an already sound contribution.

## Suggestions

1. **Quantify the data cleaning process**: Report the number/percentage of samples discarded, regenerated, and manually corrected, along with error type categories. This establishes trust in dataset quality.
2. **Conduct and report a human agreement study**: For a random sample of 200–300 intention texts, have multiple annotators identify the intended target object and report inter-rater agreement and ambiguity rates. This grounds the task's difficulty and validates that the intention-to-object mapping is reasonably unambiguous.
3. **Sharpen the task definition**: Provide explicit linguistic criteria for what constitutes an "intention" expression vs. a "referential" expression. Consider annotating a subset of 3D-VG benchmarks to demonstrate that intention-like language is absent or rare there.
4. **Analyze spaCy parsing accuracy on a sample of intention texts** to quantify the noise introduced into Verb-Object Alignment training signals.
5. **Add a limitations/discussion section** covering failure cases, ambiguous intentions, and scenarios where IntentNet struggles.

## Score and Decision

The paper introduces a genuinely new task and a large-scale dataset, proposes a well-motivated method that substantially outperforms adapted baselines, and provides a comprehensive evaluation. The main concern is insufficient validation of dataset quality (the ChatGPT-generated texts), which is a significant gap for a dataset-centered contribution but fixable with additional analysis. The task novelty and methodological weaknesses are minor and do not threaten the core contribution. 

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>