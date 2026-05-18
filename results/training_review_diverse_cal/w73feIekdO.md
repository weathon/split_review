Now I have a thorough understanding of the paper and can verify each claim against the source. Let me write the consolidated review.

## Summary

This paper proposes a method for real-time video tracking and 3D map creation on low-end single-board computers by clustering motion vectors extracted from standard video encoders. The key algorithmic contribution is a coreset construction (Algorithm 1: SEG-CORESET, Algorithm 2: CORESET) that reduces the continuous segment-clustering problem (Problem 1) to a weighted-point clustering problem with provable $(\epsilon,k)$-coreset guarantees (Theorem 2.9). The empirical evaluation reports very fast runtimes—over 1,400 fps for tracking on a laptop and 94 fps on a Le Potato board—and a speedup over the ORB-SLAM pipeline for map creation on a Raspberry Pi Zero. The paper spans theory (coresets for integrals over segments) and practice (real-time vision on commodity hardware).

## Strengths

1. **Provably efficient coreset for segment clustering (Theorem 2.9).** The paper gives a rigorous statement (Theorem 2.9) that Algorithm 2 outputs an $(\epsilon,k)$-coreset of size $O(k'\log^2 m / \epsilon^2)$ with high probability, where $m = 8kn(20k)^{r+1}/\epsilon$. This provides a formal data-reduction guarantee for the continuous-segment fitting problem, which is the algorithmic foundation of the approach. The proof generalizes Feldman & Schulman (2012) from finite point sets to infinite point sets lying on segments, and Har-Peled (2006) from discrete to continuous integrals.

2. **Impressive real-time performance on low-end hardware.** The empirical results directly support the paper's central practical claim: on a Le Potato single-board computer, the tracking algorithm processed 400 frames at 94 fps (tracking alone) and 23 fps including I/O. On a standard laptop, it achieved >1,400 fps for tracking alone. These numbers are genuinely noteworthy and demonstrate the method's potential for extremely resource-constrained settings.

3. **Practical 3D map creation on Raspberry Pi Zero outperforms ORB-SLAM in speed.** Section 4 shows that on a Raspberry Pi Zero, the proposed method achieved 11.1 fps for map creation versus 6.6 fps for the ORB-SLAM pipeline—a practical speedup on the same low-end hardware, using motion vectors as features.

4. **Privacy-preserving design.** The method operates solely on motion vectors rather than RGB pixel data, providing a degree of privacy preservation that is explicitly noted and is a genuine advantage over RGB-based approaches.

## Weaknesses

### Major

1. **Empirical evaluation lacks critical rigor to support the central practical claims.** The tracking experiments are purely qualitative: the Big Buck Bunny test (Section 3.1) reports no quantitative tracking metrics—no precision, recall, center location error, overlap, or any standard object-tracking benchmark measure. The paper acknowledges a failure mode (wrong direction when objects enter the frame) but does not measure its frequency, severity, or conditions. There is no comparison to any lightweight tracking method (e.g., simple optical-flow baselines, correlation filters, or even a baseline that clusters raw motion-vector endpoints without the coreset). The low-end board test (Section 3.2) pre-extracts motion vectors on a laptop and transfers them, so it is not a genuine end-to-end validation on the target hardware. The map-creation experiment (Section 4) reports only runtime with no quantitative reconstruction accuracy (e.g., no comparison of map quality to ORB-SLAM or ground truth). Without error bars, ablation studies, or any quantitative accuracy assessment, the paper does not demonstrate that the method is reliable or competitive for actual tracking or mapping tasks.

2. **Mismatch between "provably good" framing and what is actually proven.** The abstract calls this a "provably good tracking algorithm." What is actually proven is that the coreset construction (Theorem 2.9) approximately preserves the segment-clustering loss function (Problem 1) for every set of $k$ weighted centers. The connection from this loss guarantee to computer-vision tracking quality is not established—the "provably good" claim addresses the coreset's approximation of the mathematical objective, not whether the resulting clusters correspond to correct object tracks. The paper would be more accurate and credible if it framed the theoretical result as a provably good coreset for segment clustering, and positioned the tracking method as a practical heuristic built on that coreset.

3. **No comparison to relevant baselines.** The only comparison made is runtime against YOLOv8 (a detector, not a tracker), which conflates different tasks. There are no comparisons to: (a) any lightweight tracking method that runs on CPUs (even simple baselines like clustering raw motion-vector endpoints without the coreset), (b) any compressed-domain tracking approach, or (c) any method on the same low-end hardware for the same task. Without these comparisons, the reader cannot assess whether the coreset-based approach offers any advantage over simpler alternatives.

### Minor

4. **Theoretical novelty is not clearly articulated in the main text.** Algorithm 1 (SEG-CORESET) is presented as an embedded figure rather than as pseudo-code in the text, and the description of its novelty is limited to stating that it "bound[s] the contribution to the sum of each point ... constant for all the points on the segment" by "generalizing previous work from Rosman et al. (2014)." The nature of this generalization and what makes it nontrivial beyond a Riemann-sum-like discretization is not explained in sufficient detail for the main text to stand alone. The VC-dimension parameter $d^*$ (Definition 2.4) is introduced but never concretely instantiated for the chosen distance function $D$, so the size bounds remain non-concrete.

5. **Key methodological choices are unjustified.** The coreset size of 10 per segment, the threshold for uniform subsampling (1000 vectors), and the choice of $k=2$ (tracking) or $k=10$ (mapping) are stated but never ablated or justified. A simple ablation comparing the full coreset pipeline to uniform random sampling (or no sampling at all) would isolate the coreset's empirical benefit.

6. **Low-end board experiment is not fully end-to-end.** The Le Potato test (Section 3.2) extracts motion vectors on a laptop beforehand due to Arm architecture limitations. This means the runtime figures for the board do not include the motion-vector extraction step, which the paper itself notes is a significant cost (over 80% of runtime for the mapping experiment). The claim of real-time feasibility on low-end hardware is therefore partially unvalidated.

### Trivial

- None that survive the removal of parser artifacts and pure formatting issues.

## Nice-to-Haves

- A quantitative tracking evaluation on a standard benchmark (e.g., OTB, VOT, or a self-collected labeled video) reporting overlap, center error, or precision-recall would substantially strengthen the paper.
- An ablation that replaces the coreset with uniform random sampling (same number of points per segment) would isolate the coreset's contribution to tracking quality or speed.
- Running the full pipeline end-to-end on the target low-end board (including hardware-accelerated motion-vector extraction) would validate the real-time claim on actual hardware.
- A comparison to at least one simple baseline (e.g., tracking the centroid of all motion vectors, or clustering endpoint positions without the coreset) would contextualize the method's value.

## Removed Points

- **Criticism about missing related works (lightweight trackers, compressed-domain tracking):** Removed per rule about missing related works (no external sources to confirm existence).
- **Criticism about proof being in the appendix:** Removed per rule that the parser strips appendix sections from all papers.
- **Criticism about "tracing" vs "tracking" terminology:** Removed as a formatting artifact / parser issue.
- **Criticism about Algorithm 1 being "only" an image:** The algorithm is presented as an embedded figure. While it would be preferable to have pseudo-code in text, this is a presentation choice, not a substantive omission given the detailed caption and textual description.
- **Criticism that "there is no analysis connecting the k-means approximation on the coreset points to the original segment-clustering problem":** This is factually incorrect in the context of coreset theory. A coreset's defining property is that it preserves the loss for every model up to $(1\pm\epsilon)$, so running any $(1+\alpha)$-approximation algorithm (like k-means++) on the coreset yields a $(1+\epsilon)(1+\alpha)$-approximation for the original problem. This is standard and does not need re-proving. The real gap, kept above, is between the segment-clustering loss and CV tracking accuracy.
- **Criticism about the YOLOv8 comparison being "inappropriate":** While YOLOv8 is a detector and not a tracker, the paper uses it solely as a runtime/compute-efficiency comparison point on the same video and hardware—this is a reasonable (if limited) benchmark of computational speed.
- **Formatting/style nitpicks and structural observations:** Removed per rules.

## Novel Insights

The reviews surface a tension inherent in papers that bridge coreset theory and practical computer vision: the strength of the coreset guarantee (approximate preservation of a mathematical loss) operates at a different level than what practitioners expect from a "provably good tracking algorithm" (reliable detection and following of objects across frames). This gap is not unique to this paper—it arises whenever theoretical approximation guarantees for abstract problems are presented as guarantees for downstream application tasks. The paper would benefit from explicitly acknowledging this and setting reader expectations accordingly.

## Suggestions

1. **Reframe the "provably good" claim.** Distinguish between the provable coreset guarantee for Problem 1 and the heuristic nature of the overall tracking pipeline. This would make the paper more honest and prevent reviewers and readers from holding the empirical evaluation to a standard the theory cannot meet.

2. **Add a quantitative tracking evaluation.** Even a simple metric—percentage of frames where the cluster center falls within a manually annotated bounding box, or a comparison against a naive baseline (e.g., always predict the previous cluster center shifted by the mean motion vector)—would dramatically improve the empirical credibility.

3. **Add an ablation comparing coreset sampling to uniform random sampling.** This directly tests whether the theoretical coreset structure provides any practical benefit over a simpler baseline.

4. **Report map quality for the 3D mapping experiment.** At minimum, provide a comparison of the reconstructed map's alignment with the ground-truth environment or with the ORB-SLAM output, not just runtime.

## Score and Decision

The paper has a genuine theoretical contribution (coreset for segment clustering) and impressive raw runtime numbers. However, the empirical evaluation is too weak to support the practical claims: it lacks quantitative accuracy metrics, baseline comparisons, ablation studies, and a genuine end-to-end test on target hardware. The "provably good" framing also overstates what the theory actually guarantees (segment-clustering loss approximation, not tracking accuracy). In its current form, the paper does not convincingly demonstrate that the method is reliable or competitive enough for practical use. Major revisions—particularly a proper quantitative evaluation—would be needed.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>