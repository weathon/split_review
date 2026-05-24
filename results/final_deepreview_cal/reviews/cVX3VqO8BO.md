Now let me write the consolidated review.

---

## Summary

UniHM proposes a unified framework for generating dexterous hand manipulation sequences from open-vocabulary language instructions and RGB-D observations. The pipeline combines three components: (1) a morphology-agnostic VQ-VAE tokenizer with a shared codebook that maps heterogeneous hand kinematics into a common discrete latent space, (2) a vision-language model (Qwen3-0.6B) that generates manipulation token sequences conditioned on language, object point clouds, and target trajectories, and (3) a physics-guided Gauss-Newton refinement stage that enforces contact, generative, and temporal priors. The system is trained on human HOI datasets (DexYCB, OakInk) without teleoperation data and evaluated on both benchmarks and real-world tasks.

## Strengths

- **Novel integrated framework for language-conditioned dexterous manipulation.** UniHM is the first system to combine a shared-hand tokenizer, a VLM, and physics-based refinement into a single pipeline that produces multi-step dexterous manipulation sequences rather than static grasps. This addresses a genuine gap in the literature, where prior language-guided methods are predominantly pose-centric.

- **Physics-guided dynamic refinement with demonstrated impact.** The frame-by-frame Gauss-Newton optimization with contact energy (Eq. 11–13), generative prior (Eq. 14), and temporal regularizers (Eq. 15) is well-specified and validated. Table 4 shows that removing this module increases MPJPE from 61.40 to 65.78 on seen objects and degrades FID from 31.24 to 33.57, confirming it meaningfully improves physical plausibility.

- **Progressive masking curriculum effectively reduces exposure bias.** The paper transitions from teacher-forced training to fully autoregressive generation via a masking schedule (Eq. 10). Table 4 shows removing this curriculum substantially degrades performance (MPJPE 73.41 vs. 61.40, FID 44.87 vs. 31.24), providing clean evidence for its effectiveness.

- **Learning from human video data eliminates teleoperation dependency.** The system trains on retargeted HOI data from DexYCB and OakInk and achieves 50–65% real-world success rates on dynamic tasks (Table 3), demonstrating that robot-collected demonstration data is not required — a meaningful practical contribution.

## Weaknesses

### Major

- **Baseline comparisons are structurally unfair, undermining the quantitative claims.** UniHM receives an object point cloud (from PointSAM) and a target trajectory (from CLIPort) as inputs; the baselines (TM2T, MDM, FlowMDM, MotionGPT3) are text-to-motion models that generate from language alone without access to scene geometry or planned trajectories. The paper states baselines are "post-process[ed] with our physics-guided refinement to ensure a fair comparison" (Section 4.3), but this addresses only the output side, not the input asymmetry. The performance gap in Tables 1–2 therefore cannot be attributed to the VLM or tokenizer specifically — it may largely reflect access to perception-derived spatial information that the baselines lack. No experiment controls for this by, e.g., giving baselines the same CLIPort outputs or ablating the perception module's contribution against a fixed-perception baseline.

- **The cross-morphology tokenizer — a core claimed contribution — is not independently validated.** The abstract and contributions list prominently claim that the shared codebook "improves cross-dexterous hand generalization and scalability to new morphologies." However, the paper reports no VQ-VAE reconstruction error per hand type, no cross-hand pose translation accuracy (despite Eq. 6 claiming translation is "straightforward"), and no ablation comparing the shared codebook against per-hand codebooks. The only evidence comes from downstream task results, but those are confounded by the CLIPort module and physics refinement. The morphology-agnostic claim rests on an untested assertion.

- **No evaluation of instruction following.** All quantitative metrics (MPJPE, FOL, FPL, FID, Diversity) measure motion quality against retargeted ground truth — i.e., how closely the generated hand pose sequence matches a reference. None assess whether the generated sequence actually fulfills the language command (e.g., whether the hand successfully grasps the specified object versus moving past it). For a paper whose headline contribution is language-conditioned manipulation, this omission is significant. The real-world success rate (Table 3) partially addresses this but lacks the detail to serve as a systematic instruction-following evaluation.

### Minor

- **HOIGPT is cited as directly relevant but omitted from experiments.** The related work (Section 2.2) describes HOIGPT as a model that "extends token-based generation to long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences." Despite this direct relevance, it is not included as a baseline. The paper justifies the baseline selection by characterizing prior work as targeting "static grasp poses," but this characterization does not clearly apply to HOIGPT. Including it — or explaining its exclusion — would strengthen the evaluation.

- **Real-world experiments lack supporting detail.** Table 3 reports success rates as percentages without trial counts, variance estimates, number of objects, or a clear definition of what constitutes "success" for each task category. The baselines (MDM + Dex-Retargeting, MotionGPT3 + Dex-Retargeting) again lack scene perception, making the comparison uninformative about the VLM's contribution specifically. These issues limit the interpretability of what is otherwise a valuable real-world demonstration.

- **CLIPort and VLM architecture details are thin.** The CLIPort module — which generates the target trajectory and object point cloud critical to the system — is described only as "CLIPort-style" (Section 3.3), with no architecture, training data, or training procedure specified. Similarly, the MLP-based trajectory encoder and the VLM's input token layout receive no dimensional or structural detail. While CLIPort is a known reference architecture, a paper whose pipeline critically depends on it should specify how it is instantiated.

### Trivial

- None identified that carry evaluation weight.

## Nice-to-Haves

- A failure case analysis (e.g., where the physics refinement diverges, or where the VLM misinterprets the instruction) would add depth.
- Computational cost and runtime for training and inference would help assess practical deployability.
- An ablation replacing the 0.6B VLM with a larger model, or comparing to fine-tuning a larger LLM, would strengthen the data-efficiency claim.

## Removed Points

These points are flagged to be removed, treated with caution:

- **"CLIPort is a black box making the method unreproducible — this is a fatal methodological gap."** Overstated. CLIPort is a known reference architecture; the paper describes its functional role (RGB-D + instruction → trajectory + point cloud). The lack of architectural detail is a real but minor weakness, not a fatal flaw. Retained as Minor above.

- **"The abstract overstates the contribution as 'first framework for unified dexterous hand manipulation guided by free-form language commands.'"** The paper's literature review substantiates that prior language-guided dexterous works target static grasps, not dynamic sequences. The "first" claim, while debatable at the margin, is reasonable given the evidence presented. Removed.

- **"The introduction asserts learning from human videos as a key advantage, but the pipeline relies on retargeted HOI data, not raw video."** The paper is clear that it uses retargeted HOI sequences from DexYCB and OakInk, not raw video. The "learning from video" phrasing refers to the source data being human-captured video datasets. This is a terminology preference, not a weakness. Removed.

- **Demand for confidence intervals or larger-scale benchmarking.** Neither is standard practice in this subfield; the paper follows community norms with its 80/20 split and standard deviation reporting in Tables 1–2. Removed.

- **"The physics refinement effect is modest."** Table 4 shows removing it increases MPJPE by ~4 points, a non-trivial degradation. The critic's characterization is inaccurate. Removed.

## Novel Insights

Beyond the paper's own contributions, the review process surfaces an important methodological tension: when a perception front-end (CLIPort) provides spatial information to a generative model, disentangling the contributions of perception versus generation requires controlled ablation that neither this paper nor its closest comparators (HandsOnVLM, HAMSTER) consistently perform. Designing a "perception-only" lower bound — e.g., a heuristic policy that uses the same CLIPort outputs without the VLM — would be a valuable evaluation standard for this emerging class of perception-augmented manipulation models.

## Suggestions

- **Add a perception-ablated baseline**: Run UniHM's CLIPort + PointSAM to produce trajectories but replace the VLM with a simple trajectory-following policy (e.g., fixed-grasp heuristic). This would isolate the VLM's contribution above the perception module.
- **Evaluate instruction following**: Design a simulator-based check for whether the generated sequence actually executes the commanded task (e.g., object displacement, lid opening), and report success rates alongside motion-quality metrics.
- **Validate the tokenizer**: Report VQ-VAE reconstruction error per hand morphology, cross-hand translation accuracy, and an ablation of shared vs. per-hand codebooks on at least one downstream metric.
- **Include HOIGPT or explain its exclusion** from the experimental comparison.
- **Specify CLIPort instantiation** (architecture variant, training data, training procedure) and VLM input encoding details.

## Score and Decision

**Bracketing round**: The topically closest anchors were HandsOnVLM (6.33, rejected — hand trajectory prediction with VLMs, similar evaluation gaps), HAMSTER (6.00, accepted — hierarchical VLA, cleaner evaluation), and CrayonRobo (5.20, rejected — visual prompting for manipulation, limited evaluation). UniHM's ambition exceeds CrayonRobo's but its evaluation gaps are more consequential than HandsOnVLM's or HAMSTER's. Initial bracket: 5.0–6.0.

**Narrowing round**: Compared against CrayonRobo (5.20), UniHM offers substantially more technical depth (three novel components, two benchmarks, real-world results) and is clearly stronger. Compared against HandsOnVLM (6.33), UniHM shares similar weaknesses (missing baselines, metric limitations) but adds the significant issue of structurally unfair comparisons that HandsOnVLM did not face. Compared against HAMSTER (6.00), UniHM is more ambitious but less rigorously evaluated.

The paper sits between CrayonRobo and HAMSTER: stronger than the former due to its technical scope and evidence base, but weaker than the latter due to evaluation gaps that directly undermine its core quantitative claims. The unfair baseline comparison, unvalidated tokenizer claim, and absent instruction-following metric are addressable but collectively represent a substantial gap between claimed and demonstrated contributions.

**Anchors referenced across all rounds**:
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| wl1Kup6oES | 3.00 | 1 (bracket) | Visual pre-training for manipulation — much narrower scope, weaker evidence. UniHM is stronger. |
| KBSHR4h8XV | 3.33 | 1 (bracket) | Early Fusion VLA — smaller contribution, rejected. UniHM is stronger. |
| AJQuTFd9es (HandsOnVLM) | 6.33 | 1,2 | VLM for hand trajectory prediction — most topically similar. UniHM has similar gaps but adds unfair comparison issues. UniHM is weaker. |
| h7aQxzKbq6 (HAMSTER) | 6.00 | 1 | Hierarchical VLA — cleaner evaluation, accepted. UniHM is weaker on rigor. |
| Aqfwhna1D7 (CrayonRobo) | 5.20 | 2 | Visual prompting for manipulation — less ambitious, rejected. UniHM is stronger. |
| NxoFmGgWC9 | 5.50 | 2 | Video generative pre-training — different domain. Roughly comparable quality. |
| 9pKtcJcMP3 (VLP) | 7.00 | 1,2 | Video language planning — stronger methodology, accepted. UniHM is clearly weaker. |
| n64NYyc6rQ | 6.20 | 2 | Tokenization in MLLMs — different domain. Not directly comparable. |

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>