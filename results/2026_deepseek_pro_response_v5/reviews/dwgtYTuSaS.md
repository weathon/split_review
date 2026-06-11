Now let me do the final comparison. My round-2 anchors give me:

- **VidEgoThink (4.40)**: Ego4D-derived benchmark. Our paper is stronger — we have a working method with ablation, not just a benchmark showing models fail. Above this.
- **StreamingBench (5.75)**: Streaming video benchmark with 13 MLLMs evaluated. Pure benchmark, broader evaluation. Our paper has benchmark + method. Comparable but our method is thinner. Slightly below.
- **EgoVideo (6.00)**: Method + data pipeline with novel architecture (motion adapter), SoTA across multiple benchmarks. Our paper is clearly below this — no novel architecture, method components from prior work.

The paper lands around **5.0** — a borderline paper with a useful benchmark and well-motivated task formulation, held back by thin method novelty and weak EPIC-KITCHENS in-stream results.

---

## Summary
This paper introduces Continuous Online Action Detection (COAD), a task formulation extending online action detection (OAD) to enable models to continuously learn from streaming video after deployment using single-pass, causal updates without storing data. The authors curate Ego-OAD, a 263-hour, 87-class egocentric OAD benchmark derived from the Ego4D Moment Queries split, and propose three training strategies — state continuity, orthogonal gradient projection, and non-uniform loss weighting — adapted from prior work. Experiments on Ego-OAD demonstrate improved out-of-stream generalization, while EPIC-KITCHENS results show limitations in in-stream adaptation.

## Strengths

- **Ego-OAD fills a clear gap in egocentric OAD resources.** With 87 action classes, 22,991 instances, and 263 hours of geographically diverse egocentric video (Section 3), Ego-OAD substantially expands beyond EPIC-KITCHENS, which is limited to kitchen environments. The multi-label, temporally grounded annotation format (36% of instances overlap) captures realistic action co-occurrence patterns relevant to wearable deployment.

- **Well-motivated task formulation with clean evaluation protocol.** The argument that offline-trained OAD models need continuous adaptation for real-world wearable deployment is persuasive (Section 1). The three-way split protocol (pretraining / in-stream / out-of-stream) adopted from Carreira et al. (2024a) cleanly separates adaptation from generalization, and the learning curve analysis (Figure 4) shows COAD steadily approaching the IID upper bound.

- **Label efficiency demonstrated under realistic constraints.** At stride 128, the model receives a ground-truth label only once every ~68 seconds yet maintains meaningful out-of-stream generalization (Section 5.4, Figure 3). This is practically significant for deployment on resource-constrained wearables where dense annotation is unavailable.

- **Rigorous component ablation with clear conclusions.** Table 3 systematically isolates the three COAD components. The non-uniform loss is the heavy lifter (4.2 out-of-stream mAP, 8.3% Top-5 Recall), orthogonal gradient helps recall (4.5%), and state continuity provides marginal gains. The paper honestly reports these unequal contributions.

## Weaknesses

### Fatal
None.

### Major

- **Limited method novelty — components are from prior work and unequally important.** All three COAD components are drawn directly from prior work: state continuity follows naturally from streaming constraints, orthogonal gradient projection is from Han et al. (2025), and non-uniform loss weighting is from An et al. (2023). The ablation (Table 3) reveals severely unequal contributions: state continuity contributes approximately 0.1 mAP on both in-stream and out-of-stream, which is negligible and within noise. The non-uniform loss is the heavy lifter (4.2 out-of-stream mAP), but this component is entirely from prior work. The orthogonal gradient helps Top-5 Recall (4.5%) but only ~0.7 mAP. The paper's method contribution is primarily the specific combination for OAD, and the most critical component is borrowed.

- **EPIC-KITCHENS in-stream adaptation is weak, limiting generality claims.** On EPIC-KITCHENS (Table 2), COAD's in-stream adaptation is flat or negative: Action mAP drops from the pretrained-only 9.6 to 7.9; Verb in-stream mAP matches pretrained-only at 29.0 (zero gain); Noun in-stream mAP is 3.9 vs. 3.8 pretrained-only. The paper attributes this to "fine-grained nature of the actions and annotations" (Section 5.3), which is a post-hoc explanation lacking any diagnostic analysis (e.g., label distribution shift, per-class breakdown). While out-of-stream generalization does improve on EPIC-KITCHENS, the failure of in-stream adaptation on the most widely-used egocentric benchmark calls the method's generality into question. The paper's conclusion that EPIC-KITCHENS "validates the effectiveness of COAD" (Section 6) overstates the evidence.

- **No comparison to any existing OAD architecture.** The paper surveys LSTR, TeSTra, IDN, GateHub, and others (Section 2) but compares only against the same GRU-based detection head (from An et al., 2023) with and without COAD training. The paper argues that RNNs are chosen because Transformers are "less suitable for real-time deployment on resource-constrained devices" — but provides no latency, memory, or FLOP measurements to support this claim. Consequently, the reader cannot assess whether COAD's benefits are specific to the GRU architecture or would transfer to other OAD backbones.

### Minor

- **The in-stream mAP trade-off is downplayed.** In Table 1, w/o COAD outperforms COAD on in-stream mAP (39.0 vs. 36.8, ego pretraining). The paper frames this as COAD "maintaining robust performance across both domains," which is generous — it is more accurately a trade-off where COAD sacrifices in-stream mAP for out-of-stream gains. The Top-5 Recall numbers partially offset this (COAD wins both metrics out-of-stream and in-stream at 89.3 vs. 86.7), making the picture mixed rather than uniformly favorable.

- **No variance estimates or error bars.** No standard deviations, confidence intervals, or run-to-run variance are reported. Given that single-pass training on ordered streams can be sensitive to data order, this omission makes it difficult to assess whether small gains (e.g., the 0.1 mAP from state continuity) are statistically meaningful. While large-scale benchmarks often report single-run results, the streaming single-pass setting makes variance more relevant than in standard IID evaluation.

- **Orthogonal gradient analysis is shallow.** The paper applies one-step gradient decorrelation (Eq. 4.5) from Han et al. (2025) without discussing why projecting onto only the immediately preceding gradient is sufficient, or how this compares to alternatives (e.g., projecting onto a buffer of past gradients).

### Trivial
None.

## Nice-to-Haves

- Quantify the deployment efficiency argument: report actual latency and memory numbers for the GRU head vs. a representative Transformer on comparable hardware to substantiate the architectural choice.
- A more rigorous diagnosis of the EPIC-KITCHENS in-stream failure (e.g., label distribution shift analysis between pretraining and in-stream splits) would make the limitation informative rather than merely acknowledged.
- Release the Appendix A curation details (label grouping procedures, inter-annotator agreement statistics) for the Ego-OAD benchmark to establish trust in the ground truth.

## Removed Points
These points are flagged to be removed, treat them with caution.

- **Harsh Critic claimed union labeling "amplifies label noise" producing ground truth "no single human would endorse."** REMOVED — the paper explicitly acknowledges the ambiguity (Section 3: "While this strategy captures a richer range of human interpretations, it also amplifies label ambiguity") and describes manual grouping to mitigate it. The appendix details were stripped, making this a speculative concern rather than a verifiable weakness.

- **Harsh Critic characterized EPIC-KITCHENS as "COAD's in-stream adaptation fails across the board."** REFRAMED — out-of-stream improvements are genuine and consistent across Verb, Noun, and Action. The in-stream weakness is real but "fails across the board" is overstated; Verb and Noun are essentially flat rather than failing. Retained as a Major weakness about limited in-stream adaptation.

- **Strength Finder claimed state continuity as a core strength citing Table 3 differences.** REMOVED — the ablation numbers cited (76.0% → 75.8% out-of-stream Top-5, 89.3% → 89.2% in-stream) show differences of 0.2% and 0.1%, which are negligible. Cannot be listed as a strength when the evidence shows near-zero effect and conflicts with the verified weakness.

- **Strength Finder claimed "rigorous decomposition of adaptation vs. generalization" as a core strength.** DEMOTED — the three-way split is a protocol adopted from Carreira et al. (2024a), not a novel contribution. Retained as a supporting strength of evaluation design.

- **Harsh Critic's "Table 4 placement is confusing."** REMOVED — this is a minor presentation preference, not a substantive weakness.

## Novel Insights
None beyond the paper's own contributions. The paper's most insightful finding is the adaptation–generalization trade-off mapped in Figure 3: higher learning rates improve in-stream adaptation at the cost of out-of-stream generalization, and COAD's components (particularly non-uniform loss and orthogonal gradients) shift this frontier outward rather than merely navigating it differently.

## Suggestions

- Reframe the paper more explicitly as a benchmark + baseline contribution rather than a method contribution, given the limited novelty of the training strategies.
- Add at least one existing OAD architecture (e.g., LSTR) as a baseline on Ego-OAD, both with and without COAD training, to establish benchmark difficulty and assess whether COAD training benefits generalize beyond the GRU head.
- Provide a diagnostic analysis of why in-stream adaptation fails on EPIC-KITCHENS — e.g., analyze whether the label distribution in the in-stream split differs from the pretraining set, or whether specific action classes account for the drop.
- Report variance estimates (standard deviation over multiple runs or different stream orderings) to ground the interpretation of small ablation differences.

## Score and Decision

**Anchor comparison:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| PrAViC (jawV7vhGHw) | 4.25 | R1 | Our paper is better executed with clearer methodology and ablation |
| VidEgoThink (Z5nqeTH24j) | 4.40 | R2 | Our paper has a working method + benchmark, not just a benchmark showing failures |
| CLDyB (RnxwxGXxex) | 5.67 | R1 | Similar structure; our paper has a concrete dataset but thinner method |
| StreamingBench (qnAZqlMGTB) | 5.75 | R1 | Our paper adds a method to the benchmark but has weaker evaluation breadth |
| EgoVideo (P6G1Z6jkf3) | 6.00 | R2 | Clearly stronger — novel architecture, SoTA results, comprehensive evaluation |

**Bracket:** Round 1 placed the paper between VidEgoThink (4.40) and EgoVideo (6.00). Round 2 narrowed this: the paper is clearly above VidEgoThink (4.40) but clearly below EgoVideo (6.00), and slightly below StreamingBench (5.75). The benchmark and task formulation are genuine contributions, but the method is thin with the critical component (non-uniform loss) borrowed from prior work, state continuity contributes negligibly, EPIC-KITCHENS in-stream adaptation is weak, and there are no comparisons to existing OAD architectures. A borderline paper at the accept/reject threshold.

**Final Score: 5.0**

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>