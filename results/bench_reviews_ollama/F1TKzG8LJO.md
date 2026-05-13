## Summary
RT-Trajectory proposes conditioning a manipulation policy on coarse 2D (or 2.5D, with height encoded in a color channel) end-effector trajectory sketches overlaid on the initial camera image. Training labels are produced automatically via hindsight projection of proprioceptive end-effector poses; at inference, sketches can come from human drawings, hand-video extraction, LLM Code-as-Policies waypoints, or image-generating VLMs. On 7 held-out manipulation skills the policy reaches 67% (2.5D) vs. 26% (RT-1-Goal), 16.7% (RT-1), and 11.1% (RT-2).

## Strengths
- The hindsight labeling pipeline (Sec. 3.2) is genuinely practical: trajectory labels are obtained automatically from proprioception and calibrated camera intrinsics/extrinsics, with no manual annotation, and the conditioning is fused into the RT-1 tokenizer by adding zero-initialized input channels — a clean architectural integration that allows reuse of any existing teleop dataset.
- Demonstrating that a single policy accepts very different trajectory sources at inference time (drawings, hand-video extraction, LLM-generated linear waypoints, image-gen VLM) without retraining (Tables for human-video and CaP; qualitative VLM results in Sec. 4.3) is a meaningful interface contribution and shows the sketch format is not bound to a particular UX.
- The 2.5D height-channel extension is well-motivated and ablated against the 2D variant (Sec. 4.2), with the gap concentrating on height-sensitive skills like Pick from Chair — consistent with the claim that the channel encodes useful geometry rather than acting as a generic regularizer.
- The Fréchet-distance motion-similarity analysis (Sec. 4.5) is more substantive than is typical for this kind of paper and at least attempts to quantify whether evaluation trajectories are novel relative to training; the semantic-composition and first-interaction-height analyses are useful framing.

## Weaknesses

### Fatal
None. The contributions are real even if the framing is contestable.

### Major
- **Conditioning modality vs. conditioning information content are conflated in the headline comparison.** RT-Trajectory receives a near-complete spatial specification (end-effector path, gripper open/close markers, and in 2.5D the picking height) drawn by a human who has already solved the geometric and timing structure. RT-1/RT-2 receive only language; RT-1-Goal receives only an end-state image. The 67% vs. 26% gap therefore measures, in significant part, how much task-relevant signal the human put into the conditioning image, not the intrinsic generalization advantage of the modality. A fair contrast would include a language- or goal-conditioned baseline that also receives some spatial hint (target waypoint, bounding box). Sec. 4.5 itself acknowledges that some "unseen" skills retrieve very similar training motions, which is consistent with the policy being closer to a learned trajectory follower than a task generalizer. This does not invalidate the paper but it does mean the "task generalization" framing in the abstract and conclusion is not as cleanly supported as stated.
- **Interaction-marker contribution is not isolated.** The markers explicitly tell the policy *when* to close/open the gripper — a non-trivial part of any pick/place task — yet the only ablation in the main text is 2D vs. 2.5D. An ablation separating trajectory curve alone, +interaction markers, +height, +temporal color grading would be necessary to attribute the gain correctly to "trajectory sketches" as a representation rather than to the gripper-timing supervision baked into the same image.

### Minor
- **RT-2 underperforms RT-1 (11.1% vs. 16.7%) without discussion.** A stronger language-conditioned baseline doing worse than the weaker one on the unseen set deserves at least a hypothesis (adversarial choice of unseen skills, mis-tuning, sample noise). Leaving it silent weakens the language-baseline comparison.
- **IK Planner comparison is narrow.** The IK planner already reaches 71–83% on CaP-prompted Pick/Open Drawer and beats RT-Trajectory on Open Drawer (Table for CaP). This is the cleanest evidence about what the learned policy adds beyond trajectory tracking, and with only two skills the conclusion that the policy contributes scene-conditioned adaptation is supported only weakly. The "adapts to object orientation" claim in Sec. 4.3 is asserted rather than quantified.
- **Statistical power is thin per skill.** 64 trials across 7 unseen scenarios is roughly 9 trials per skill; with no per-skill confidence intervals, the per-skill breakdown the unseen-skill claim depends on is hard to interpret precisely. Single-run real-robot eval is standard, so this is a soft concern, but reporting at least bootstrap intervals on the aggregate would help.
- **Sec. 4.5's Fréchet analysis measures executed rollouts, not query/conditioning trajectories.** The argument that the *input distribution* contains novel motions would be cleaner if the analysis were run on the sketches themselves; the current measurement is somewhat circular (successful rollouts trace novel paths because successful rollouts were the ones the human sketch guided correctly).
- **The "emergent" visual prompt-engineering capability (Sec. 4.4) is qualitative only.** Framing iterative re-sketching as an emergent capability without measurement is suggestive rather than evidential.

### Trivial
- The taxonomy in Fig. 1 ("what to do" vs. "how to do it") implicitly concedes that sketches sit on the "how" side; the paper would read more cleanly if it returned to this when claiming generalization parity with goal/language methods.

## Nice-to-Haves
- A language-plus-waypoint or language-plus-bounding-box baseline to disentangle "conditioning modality" from "added spatial information."
- An adversarial-sketch study: does the policy follow an impossible or scene-inconsistent trajectory, and at what point does scene perception override the sketch? This would directly probe the tracker-vs-generalizer question.
- Per-skill variance and inter-drawer agreement (multiple humans drawing the same scene) to quantify how robust the method is to sketch quality.
- Failure-mode breakdown of the 33% unsuccessful trials by cause (bad sketch, bad tracking, perception error).

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Harsh critic's claim that the "Pick from Chair" 2.5D result "encodes the answer in the input."* The height channel encodes height, which is genuinely the relevant geometric cue — encoding a cue that helps with a height-sensitive task is the intended design, not a structural cheat. This is more a restatement of the conditioning modality's expressiveness than a flaw; weakened and folded into the framing concern above.
- *Strength Finder's "rigorous motion-novelty analysis substantiates out-of-distribution generalization."* Kept partially as a strength but downgraded because, as the harsh critic correctly notes, the Fréchet analysis is run on executed rollouts and so does not fully substantiate input-distribution novelty.
- *Strength Finder's "thoughtful trajectory representation design with clear ablations."* The ablation is 2D vs. 2.5D only and does not isolate interaction markers vs. color grading; calling this "clear ablations" overstates the evidence, so removed as a standalone strength.

## Novel Insights
None beyond the paper's own contributions. The strongest cross-cutting observation surfaced in review — that a trajectory-conditioned policy occupies an awkward middle ground between an IK tracker and a generalizing policy, and that fairly attributing generalization requires baselines with matched information content — is a real conceptual takeaway that the paper would benefit from acknowledging, but it is a critique of the existing setup rather than a new contribution.

## Suggestions
- Reframe the contribution from "task generalization beyond language- and goal-conditioned policies" to "a practical, expressive interface for specifying motions, with hindsight labeling making training scalable." This more accurately reflects what the evidence supports and is still a substantial contribution.
- Add at least one baseline that receives auxiliary spatial information (e.g., a target waypoint or click point) on top of language or goal images, on the same 7 unseen skills.
- Run the explicit ablation: curve only / + interaction markers / + temporal grading / + height, to attribute the 2.5D headline to specific design choices.
- Address the RT-2 < RT-1 anomaly directly, even if just with a one-paragraph hypothesis and an additional small comparison.
- Apply the Fréchet analysis to the *query* sketches as well as the executed rollouts.

## Overall Assessment
- *Originality:* Moderately high. Trajectory-sketch conditioning is a meaningfully different representation choice from language/goal-image, and the hindsight-labeling + tokenizer integration is novel in combination.
- *Importance:* The question (better conditioning modalities for generalist policies) is central to current robot learning.
- *Claim support:* Mixed. The headline 67% vs. 26% number is real but oversold as "task generalization" given the asymmetric information the conditioning supplies.
- *Soundness of experiments:* Adequate for the field; real-robot eval, reasonable trial counts, but thin on ablations isolating which signal in the sketch image is doing the work.
- *Clarity:* Good — the architecture and labeling pipeline are clearly explained.
- *Value to the community:* High as an interface paper; moderate as a generalization paper.

This is a solid systems-and-interface contribution with a framing problem and an under-ablated representation, not a fundamentally flawed paper.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>