Now let me carefully analyze the claims and verify each of the harsh critic's points against the actual paper text:

**1. AudioSet comparison claim**: The paper says "BirdSet surpasses AudioSet with over 6,800 recording hours (↑17%) from nearly 10,000 classes (↑18×)." The critic argues this is misleading because AudioSet's 527 classes span all audio domains while BirdSet's ~10,000 are fine-grained species within one domain. Let me check: The paper does clearly position BirdSet as a "domain-specific application in audio classification" (line 21) and compares itself to AudioSet in terms of dataset volume specifically. The related work section (line 173) says "While it is the only environmental audio classification dataset comparable in scope to BirdSet..." and "In contrast, BirdSet includes nearly 10,000 domain-specific classes..." So the paper does acknowledge the domain-specific nature. However, the abstract's "surpasses" language with raw numbers and percentage comparisons does invite a direct comparison that is indeed apples-to-oranges on the class dimension (10,000 fine-grained species vs 527 broad categories). The hours comparison is somewhat more defensible as both measure recording time. This is a valid concern about framing but not fatal.

**2. "Multi-purpose" claims**: The paper explicitly claims in contribution (2): "BirdSet serves as an extensive multi-purpose dataset in audio classification with evaluation use cases such as self-supervised learning, event detection, multi-label classification under covariate and domain shifts with noisy labels or few-shot, and active learning." The experiments only benchmark supervised multi-label classification. However, the paper uses the word "outline" in the abstract: "We benchmark six well-known DL models in multi-label classification across three distinct training scenarios and outline further evaluation use cases." The conclusion says "As the primary evaluation use case, we benchmarked supervised multi-label classification." So the paper does signal that the other use cases are outlined rather than experimentally validated. The claim of "multi-purpose" is a bit of an overreach given only one use case is demonstrated, but the paper is somewhat transparent about this. This is a moderate concern.

**3. ConvNext vs Perch claim**: The paper says "ConvNext consistently outperforms other models across datasets in the LT scenario...It often exceeds the SOTA model Perch." Looking at the actual data in Table 3:
- cmAP: Perch best on 4 of 7 test datasets (NES, UHH, NBP, SNE tied), ConvNext best on 4 (PER, HSN, SSW, SNE). Perch overall LT cmAP = 0.36 (tied with ConvNext).
- AUROC: ConvNext best on 5 test datasets (PER, UHH, HSN, NBP, SSW), Perch best on 2 (NES, SNE). Overall LT: ConvNext 0.85, Perch 0.84.
- T1-Acc: Perch best on 7 of 8 datasets. Overall LT: Perch 0.61, ConvNext 0.51.

The paper acknowledges that Perch "excels in retrieval tasks as reflected by the T1-Acc metric." But the "consistently outperforms" claim based on AUROC alone is indeed selective. The paper mentions "ConvNext's consistent performance, shown by the AUROC and cmAP metrics" — but Perch matches ConvNext on cmAP and dominates T1-Acc. This is a real but moderate framing issue.

**4. Logit restriction**: The paper states "During inference, we restrict the models' logits by excluding those unrelated to the species present in the test datasets" (line 279). It also references this as following related work (citing hamer2023). The critic is correct this introduces oracle knowledge. However, the paper partly acknowledges context: "Methods to manage subpopulation shifts include limiting logits to relevant species in test datasets~\citep{hamer2023}" in the adaptability section. The limitation is not explicitly flagged. This is a valid minor-to-moderate concern.

**5. Perch training data leakage**: The critic notes BirdNET was excluded for "potential test data leakage" but Perch (also trained on ~10,000 XC species) was included. The paper says "We also incorporate inference with Perch...and exclude BirdNET...due to potential test data leakage." This asymmetry is indeed worth noting. However, the nature of the leakage could differ — BirdNET is an end-to-end classifier that may have been trained on actual soundscape data from BirdCLEF, while Perch is used as a feature extractor with a separate classification head. Still, the paper does not explain this asymmetry, which is a moderate weakness.

**6. Standard deviations in main table**: The paper says "Refer to autoref{app:results} for more details and the standard deviations" — they exist but are in the appendix. This is a minor presentation concern, not a methodological flaw.

Now let me assess the Strength Finder's claims:

- "Dataset scale surpasses AudioSet" — I should modify this since the comparison is misleading as discussed.
- "First standardized, unified benchmark" — valid, well-supported by Table 1.
- "Eight geographically diverse test datasets" — valid, well-supported by Table 2.
- "Comprehensive multi-model, multi-scenario benchmark" — valid but partially undermined by the selective framing.
- "Public accessibility via Hugging Face" — valid.
- "Systematic challenge framing" — valid.
- "Multi-label evaluation protocol" — valid.

Let me now compose the final review.</think>Now I have all the relevant data verified against the paper. Let me compose the final review.

## Summary
BirdSet introduces a large-scale benchmark dataset for avian bioacoustics audio classification, comprising over 6,800 hours of focal training recordings from ~10,000 species (Xeno-Canto) and 400+ hours of strongly-labeled soundscape evaluation data across eight geographically diverse test sites. The paper benchmarks six deep learning models under three supervised multi-label training scenarios and provides the dataset on Hugging Face with an open codebase.

## Strengths
- **First standardized, curated benchmark addressing fragmentation in avian bioacoustics**: Table 1 systematically catalogs 18 prior publications, demonstrating inconsistent dataset combinations, non-overlapping train/eval splits, and non-reproducible custom XC subsets. BirdSet resolves this with curated training data (XCL/XCM), a unified test collection, standardized eBird taxonomy labels, and Hugging Face hosting—a genuine structural contribution to the field (§2.1, §3).

- **Well-motivated train/test distinction between focal and soundscape recordings**: Drawing a clear line between focal recordings (suitable for training) and soundscape recordings (suitable for evaluation) and providing both in one collection directly addresses the real methodological gap where prior work either tests on training-domain focal data or uses non-public custom subsets (§2.1, line 42).

- **Geographically diverse test suite enabling generalization evaluation**: The seven test sites (PER, NES, UHH, HSN, NBP, SSW, SNE) span multiple continents with varying class balance (Pielou's J from 0.54 to 0.78 in Table 2), and Table 3 confirms substantial performance variation across datasets (e.g., cmAP ranges 0.12–0.63 across test sets for EfficientNet in LT), validating that this diversity meaningfully stress-tests model robustness.

- **Practical accessibility**: Hosting on Hugging Face with unified metadata and an extensive codebase is a concrete improvement over AudioSet's manual retrieval process and the ad-hoc data processing required by prior avian work (§3, contribution (6) in the Introduction).

- **Multi-model, multi-scenario benchmark yielding actionable findings**: Six models across three training scenarios (LT, MT, DT) with three threshold-free metrics reveal useful patterns: large-scale training (LT/MT) outperforms dedicated fine-tuning (DT); general-domain pre-trained models (AST, W2V2) underperform domain-specific large-scale training; and the three metrics capture different model strengths (Table 3, §5.2).

## Weaknesses

### Fatal
None.

### Major
- **The "surpasses AudioSet" framing conflates incommensurable quantities**: The abstract claims BirdSet "surpasses AudioSet" citing ↑17% hours and ↑18× classes. AudioSet's 527 classes span the entire audio domain (speech, music, environmental); BirdSet's ~10,000 classes are fine-grained taxonomic subdivisions within a single biological domain. More classes in a domain-specific taxonomy does not constitute "surpassing" a universal ontology—it reflects a different kind of granularity. The paper itself explicitly positions avian bioacoustics as a "domain-specific application in audio classification" (line 21) and acknowledges that focal recordings "do not represent entire acoustic environments" and "are usually weakly labeled without specific vocalization times" (line 42). The raw numbers and percentage comparisons in the abstract and Figure 1 thus invite a misleading apples-to-oranges comparison. The paper would be stronger if it framed the contribution as complementing AudioSet (a domain-specific resource at comparable scale with superior evaluation coverage) rather than "surpassing" it.

- **The "multi-purpose" designation overreaches what is experimentally demonstrated**: Contribution (2) in the contributions box claims BirdSet is a "multi-purpose dataset" with use cases including self-supervised learning, event detection, few-shot learning, and active learning. The experiments only benchmark one use case: supervised multi-label classification across three training scenarios. While the abstract uses the word "outline" for additional use cases and the conclusion identifies SSL as future work, the contributions box and conclusion both restate "multi-purpose" as an established property. For a benchmark paper, claiming versatility while demonstrating only one task creates a gap between what is claimed and what is shown. The paper should either demonstrate at least one additional use case experimentally or soften the claim to "designed to support multiple use cases, with supervised multi-label classification demonstrated here."

### Minor
- **Selective reporting of model comparison between ConvNext and Perch**: Section 5.2 states "ConvNext...consistently outperforms other models across datasets in the LT scenario. It often exceeds the SOTA model Perch." This is true for AUROC (ConvNext best on 5/7 test sets), but the paper underrepresents Perch's clear advantages: on cmAP, Perch and ConvNext tie at 0.36 overall; on T1-Acc, Perch dominates with 0.61 overall vs ConvNext's 0.51, winning on 7/8 datasets including by large margins (0.66 vs 0.45 on NES; 0.57 vs 0.44 on UHH). The paper acknowledges Perch "excels in retrieval tasks as reflected by the T1-Acc metric" but then attributes this to a "simpler EfficientNet architecture" rather than treating it as a substantive finding. For a benchmark paper, neutral and complete characterization of metric-dependent tradeoffs between models is important (Table 3, line 366).

- **Logit restriction during inference introduces oracle knowledge without explicit limitation acknowledgment**: The evaluation protocol restricts models' logits "by excluding those unrelated to the species present in the test datasets" (line 279). This gives models prior knowledge of the candidate species set, which would not be available in real-world PAM deployments. The paper notes this follows prior work (citing hamer2023) and discusses logit restriction in the adaptability section, but does not flag it as a limitation in §6. Its impact on absolute performance numbers should be acknowledged there.

- **Asymmetric treatment of potential data leakage between BirdNET and Perch**: BirdNET is excluded from evaluation "due to potential test data leakage" while Perch—which was also trained on ~10,000 species from Xeno-Canto—is included (line 279). There may be legitimate reasons for this asymmetry (e.g., BirdNET may have been trained on the actual BirdCLEF soundscape test data), but the paper does not provide this justification, leaving readers unable to assess whether Perch's results reflect genuine generalization or overlapping training data (§4.1, line 279).

### Trivial
- The NBP row in Table 2 appears to have a parsing-damaged entry (line 260 reads "92 & 51" without a dataset label), making the exact number of classes for that dataset ambiguous in the parsed version.

## Nice-to-Haves
- An unrestricted inference experiment (without logit restriction) would demonstrate how much oracle knowledge helps and provide a more ecologically valid performance baseline, strengthening the benchmark's claim to evaluate "real-world" conditions.
- A class-overlap analysis between training (XCL/XCM) and test datasets would help users distinguish memorization from generalization and assess leakage risk.
- An SSL pre-training experiment (e.g., wav2vec 2.0 on XCL) would substantiate the frequently-cited SSL use case.
- Reporting key standard deviations in the main text (they are deferred to the appendix per line 279) would strengthen confidence in claims about consistent model differences.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **"6,800 hours of weakly-labeled focal recordings are qualitatively different from AudioSet's 5,800 hours, so the hours comparison is also misleading"**: The harsh critic extends the apples-to-oranges critique to the hours comparison. However, both datasets measure recording duration in hours, and the paper explicitly distinguishes focal vs. soundscape recordings. The hours comparison is more defensible than the class comparison; the real issue is the "surpasses" framing overall, captured in the Major weakness above.

- **"The paper should choose one framing—either complement or replace AudioSet"**: This overstates the problem. The paper's discussion in §2.1 and the related benchmarks section does treat BirdSet as complementary to AudioSet (noting AudioSet is "universal-domain" while BirdSet is "domain-specific"). The issue is the misleading abstract framing, not a fundamental contradiction between sections.

- **"Curation process underspecified for reproducibility—what quality filters were applied?"**: This is a minor reproducibility nitpick. The paper provides extensive detail on taxonomy unification, event detection via bambird, processing at 32kHz, and references the appendix for more details. Standard dataset papers need not specify every filter.

- **"The bambird event detection model's accuracy is not reported"**: This is a minor implementation detail. The detected events are provided as flexible training data, and users can choose to use or ignore them. Not reporting the detector's accuracy is not a methodological flaw in the benchmark itself.

- **"eBird taxonomy unification is mentioned but not detailed"**: Same as above—deferred to appendix, not a benchmark design flaw.

- **"Request for failure mode examples / spectrogram visualizations"**: This is a nice-to-have, not a weakness.

- **"Report standard deviations in main results table"**: This is trivial; the paper explicitly states where to find them and this is a presentation choice, not a methodological gap. Moved to Nice-to-Have.

- **Strength Finder claim: "Dataset scale surpasses AudioSet in key dimensions"**: This "strength" directly conflicts with the verified Major weakness about the misleading AudioSet comparison. The dataset's scale IS a genuine strength, but the "surpasses" framing is misleading—removed as a strength in favor of a more accurate characterization.

## Novel Insights
The paper's most insightful contribution is the demonstration that model rankings are metric-dependent in avian bioacoustics: ConvNext leads on AUROC (discrimination), Perch leads on T1-Acc (retrieval/identification), and they tie on cmAP. This suggests the field needs multi-metric evaluation precisely because different deployment scenarios (species detection vs. single-species identification) reward different model properties—a nuance that single-metric benchmarks would miss.

## Suggestions
- Reframe the "surpasses AudioSet" language as "provides a domain-specific resource at comparable scale with substantially more evaluation coverage" to avoid the apples-to-oranges comparison.
- Either add at least one experimental demonstration of a second use case (e.g., SSL pre-training on XCL) or change "multi-purpose dataset" to "dataset designed to support multiple use cases" in the contributions.
- In §6 Limitations, explicitly acknowledge the logit restriction as reducing ecological validity and note the asymmetric treatment of BirdNET vs. Perch regarding potential data leakage.
- Present the ConvNext vs. Perch comparison more neutrally by leading with the metric-dependent result rather than declaring one model the winner.

## Evaluation
**Originality**: The dataset collection itself is a curation effort rather than a novel algorithmic contribution, but the standardization and benchmark design address a genuine gap. **Research question importance**: High—the fragmentation problem in avian bioacoustics is real and well-documented by Table 1. **Claim support**: Partially undermined by overclaiming in framing (AudioSet comparison, multi-purpose designation) and selective model reporting. **Soundness of experiments**: Solid for the primary use case (supervised multi-label classification), though limited in scope relative to claims. **Clarity**: Good overall with clear structure. **Community value**: High—a publicly accessible, standardized benchmark with diverse test sets would be immediately useful.

## Score and Decision

The dataset resource itself is a valuable contribution that addresses a real need, and the core experimental work is sound. However, the paper substantially overclaims: the "surpasses AudioSet" framing is misleading, the "multi-purpose" label is aspirational for most listed use cases, and the ConvNext-vs-Perch framing is selectively favorable. These are addressable framing issues rather than fundamental methodological flaws, but they are significant enough to weigh against acceptance as-is. The dataset contribution stands on its own merits without needing inflated comparisons.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>