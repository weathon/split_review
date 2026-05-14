Now I have a thorough understanding of the paper and calibration anchors. Let me write the consolidated review.

---

## Summary

VIBEFACE presents a new face biometric dataset with 2,250 images and 1,550 videos from 50 participants, designed to fill a gap in eKYC-style video scenarios. The dataset balances gender (50:50), four racial groups (~25% each), and three age bands per ISO standards, with five acquisition sessions varying lighting and eyeglass occlusion across three consumer smartphones. Baseline evaluations on face detection and verification are reported, with demographic breakdowns.

## Strengths

- **Genuinely novel eKYC video scenarios**: The seven verification video scenarios (12–18: head rotation, tilting, blinking, expression change, mouth opening, face covering, sequential face touching) explicitly mimic real-world eKYC interaction protocols. No prior public dataset includes these compliance-driven video sequences, making this a real gap-filling contribution.

- **Deliberate and transparent demographic balancing**: The dataset achieves a 50:50 gender split, near-equal distribution across African (26%), Caucasian (26%), East Asian (24%), and South Asian (24%) groups, and age bands following ISO standards. Table 1 demonstrates that no prior comparable dataset simultaneously checks all balance criteria, and the paper is transparent about exact subgroup counts.

- **Ethical and legal rigor**: Data collection follows GDPR and AI Act standards, with informed consent, anonymized storage via randomized identifiers, and a controlled-access research license. This addresses the ethical concerns that caused the withdrawal of many large-scale face datasets and sets a responsible precedent.

- **Multi-condition acquisition with demonstrated impact**: The five sessions systematically vary lighting (artificial, flash, natural daylight, weak natural light) and eyeglass occlusion. The benchmark results in Tables 3 and 4 show meaningful performance degradation under glasses (session C) and weak natural light (session E), validating that the controlled variations stress models in realistic ways.

## Weaknesses

### Major

- **Verification evaluation is not a valid benchmark**: Section 4.2 reports only the genuine acceptance rate — the percentage of frames where similarity exceeds a fixed threshold of 0.5 — with no imposter comparisons whatsoever. A verification evaluation requires genuine vs. imposter trials, reporting FAR/FRR, ROC curves, or EER. Without imposter trials, there is no way to assess whether the threshold is meaningful or whether the models can actually discriminate between subjects. This means the verification results in Table 4 do not demonstrate the dataset's utility for verification benchmarking, which is a central claimed contribution. The detection benchmark (Section 4.1) is not similarly affected, but the paper's core claim of establishing a verification benchmark is unsupported by the current evaluation.

- **Fairness claims exceed what the sample size can support**: With 12–13 subjects per racial category and age-gender subgroups often containing only 2–4 individuals, subgroup estimates in Tables 3 and 4 are dominated by sampling noise. The paper claims to enable fairness auditing, but no confidence intervals or variance estimates are reported. Apparent differences between demographic groups (e.g., "MTCNN showed reduced detection performance among African subjects") cannot be reliably distinguished from noise with these sample sizes. The dataset may still be useful for fairness research as one component of a larger evaluation suite, but the paper's own fairness conclusions from its benchmark are unsubstantiated.

### Minor

- **Tension between motivation and collection setting**: The introduction motivates the dataset by describing eKYC as occurring "under unconstrained conditions — at home, in variable lighting, and across heterogeneous mobile devices." However, Section 3 reveals the data were collected in "a controlled studio environment" with "supervised operators" and preset lighting designs. While the paper is transparent about the studio setting, it never discusses how the controlled environment limits external validity relative to the unconstrained motivation, nor does it frame the dataset as complementary to in-the-wild data rather than a substitute. The lighting variations are designed rather than naturally occurring, and the supervised setting eliminates the user behavior variability that would occur in at-home eKYC.

- **No statistical reporting**: All results in Tables 3 and 4 are presented as point estimates without standard deviations, standard errors, or confidence intervals. Combined with the small sample, this makes subgroup comparisons non-interpretable. For a paper that emphasizes demographic fairness, reporting variance is essential.

- **Overclaimed conclusions**: The conclusion speculates about the dataset's potential for presentation attack detection (PAD) and deepfake detection without any supporting experiments. While these are plausible future uses, claiming them as contributions in the conclusion goes beyond what is demonstrated.

### Trivial

- The text presentation has minor parser artifacts (page number markers like `{0}`, `{1}`, etc.) that do not affect the paper's substance.

## Nice-to-Haves

- A discussion of how the studio-controlled setting relates to truly unconstrained eKYC and what complementary role the dataset could play alongside in-the-wild data would strengthen the framing.
- Score distribution histograms (genuine vs. imposter) would help the community assess model calibration on this data once a proper verification protocol is in place.

## Removed Points

These points are flagged to be removed — treat them with caution.

- **"Dataset too small for claimed demographic fairness evaluation (Structural)"** — MODIFIED and KEPT. The size concern is real, but the harsh critic's framing that it "cannot credibly support the claimed contribution of enabling fairness analysis" is too absolute. Many comparable datasets (OULU-NPU: 55 IDs, HQ-WMCA: 51 IDs, WMCA: 72 IDs) have similar or only slightly larger subject counts. The issue is not that 50 subjects is categorically too few for a face dataset of this type — it's that the paper's *fairness conclusions* from its own benchmark are unreliable given 12–13 per racial group. The dataset may still serve as a useful fairness testbed, particularly in combination with other resources. Moved from "Fatal/Structural" to "Major" with softened language.

- **"Collection environment contradicts unconstrained motivation (Methodological gap)"** — WEAKENED. The paper does explicitly state the collection was in a controlled studio (Section 3). The tension is a framing issue, not a methodological error or hidden fact. Moved from Major to Minor.

- **"No statistical reporting"** — KEPT but downgraded. This is a valid point but is a Minor issue; many dataset benchmark papers in this area report point estimates without confidence intervals. It compounds the sample size concern but is not itself a major flaw.

- **Formatting nitpicks and typos** — REMOVED per hard rules. Parser artifacts are not author errors.

## Novel Insights

The paper's most interesting observation is that the specific combination of eKYC action protocols (head rotation, blinking, face touching) with systematic lighting and occlusion variations creates a stress test that reveals substantial performance gaps not visible under standard frontal-image benchmarks. For instance, ArcFace verification rates drop from near-perfect on frontal images (FV: 1.000 in session A) to ~0.50 on off-angle views (OAV: 0.509 in session A) — a finding that highlights how much standard benchmarks may overstate real-world verification reliability. This insight is practically valuable for practitioners building eKYC systems, even if the absolute numbers need proper verification protocol validation.

## Suggestions

- **Redesign the verification evaluation**: The single most important revision is to implement genuine vs. imposter comparisons and report standard verification metrics (ROC, EER, TAR@FAR). Without this, the verification benchmark claim cannot be evaluated.
- **Add bootstrap confidence intervals** to Tables 3 and 4 to make subgroup comparisons interpretable given the limited sample.
- **Reframe the motivation** to acknowledge the controlled setting and position the dataset as a complement to (not replacement for) in-the-wild data, or at minimum discuss the implications of studio collection for external validity.
- **Tone down fairness claims** in the abstract and conclusions to match what the sample size can support; frame the dataset as enabling *future* fairness research rather than conclusively demonstrating algorithmic bias.

## Scoring

I evaluated originality, importance of the research question, whether claims are well supported, soundness of experiments, clarity of writing, and value to the research community.

**Originality**: The eKYC video scenarios are genuinely novel — no prior public dataset offers these compliance-driven action sequences. This is a real contribution.

**Importance**: The research question (providing a dataset for eKYC-style evaluation) addresses a practical gap in biometrics research with clear industry relevance.

**Claim support**: The central claim of establishing a verification benchmark is unsupported due to the absence of imposter evaluation. The dataset itself is well-described and ethically collected, but the benchmarking claims are not adequately backed.

**Soundness**: The verification evaluation is fundamentally incomplete. The detection evaluation is reasonable. The demographic fairness conclusions are unreliable given sample size and lack of variance estimates.

**Clarity**: The paper is generally clear about its dataset construction and demographics, though the tension between motivation and collection setting is never addressed.

**Value to community**: The dataset could have niche value for eKYC-related research, particularly for PAD and action-protocol studies, but the current paper does not establish its utility as a verification benchmark.

### Anchor comparison

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| FaceID-6M (`yTq81RcKaw.md`) | 3.50 | Large-scale dataset paper with curation-only novelty; had narrow evaluation and poor ethics. VIBEFACE has stronger ethical handling and more focused novelty (eKYC actions) but much smaller scale and a flawed verification evaluation. Roughly comparable overall. |
| LabInsect-48K (`ojcyMKpbyk.md`) | 3.00 | Dataset paper with classification/detection/segmentation benchmarks; similar issues with evaluation rigor. VIBEFACE has a comparable contribution profile — a novel dataset with benchmark demonstrations that have significant gaps. |
| FaceCoT (`771P34sqnn.md`) | 3.50 | Dataset + method paper with incomplete evaluation (no quantitative interpretability metrics, missing ablations). VIBEFACE has a similar profile of a good idea with insufficient experimental validation. |
| Adaptive Calibration (`7iwqu82yOC.md`) | 2.50 | Method paper with weak evaluation. VIBEFACE is stronger — it has a genuinely novel dataset contribution even with evaluation flaws. |
| FaceMoE (`O4f1NdXtdM.md`) | 5.00 | Method paper with solid contribution and correctable gaps. VIBEFACE is weaker — its evaluation gap (missing imposter trials) is more fundamental than FaceMoE's correctable issues. |
| BANZ-FS (`GMR9BUsPbq.md`) | 7.00 | Dataset paper with large scale (35K+ instances), rigorous multi-task benchmarks, and clear gap-addressing contribution. VIBEFACE is substantially weaker — smaller scale, flawed evaluation, and overstated claims relative to evidence. |
| DeepfakeBench-MM (`nA8vLqvBRJ.md`) | 4.00 | Dataset paper with reasonable scale and benchmarks, moderate novelty. VIBEFACE has more focused novelty but weaker experimental validation. |
| FVBench (`yxGPF62JUz.md`) | 4.00 | Benchmark paper with metric issues. Comparable evaluation rigor concerns. |

The paper is closest to the 3.0–3.5 range. The verification evaluation being fundamentally incomplete (no imposter trials) is the central factor pulling the score down. The dataset itself has genuine novelty (eKYC scenarios) and strong ethical practices, which prevent it from falling into the 2.5 range. But the core benchmarking claim is not adequately supported, and the fairness conclusions are unreliable given the sample size. Among the anchors, it sits most naturally alongside FaceID-6M (3.50) and LabInsect-48K (3.00), with evaluation issues more severe than FaceID-6M's but a more focused contribution. I place it at **3.0**.

MY FINAL SCORE: <pineapple>3.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>