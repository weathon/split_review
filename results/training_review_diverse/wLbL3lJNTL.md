Now I have all the information I need. Let me compile the final consolidated review.

---

## Summary

This paper studies representation learning for reinforcement learning from multiple sensors (images and proprioception). Building on Recurrent State Space Models (RSSMs), the authors propose combining contrastive losses for high-dimensional image observations with reconstruction losses for low-dimensional proprioception, and evaluate this design across both variational and contrastive predictive coding paradigms. The core empirical contributions are a large-scale evaluation across four task suites (Standard DMC, Video Background, Occlusions, and a new Locomotion suite) plus a realistic mobile manipulation task, systematically comparing joint representations against concatenation baselines and several SOTA image-only methods.

## Strengths

- **Joint representations with mixed objectives consistently outperform concatenation baselines across multiple challenging domains.** In the Occlusion suite (Fig. 3), Locomotion suite (Fig. 4), and OpenCabinetDrawer (Fig. 5), Joint(CPC+R) and Joint(CV+R) significantly outperform all Concat baselines. This comparison is clean because both joint and Concat methods use the same image-level loss (contrastive or reconstruction) and thus the same data processing. The results are reported with IQM and 95% CIs (Agarwal et al., 2021).

- **Joint representations improve model-based RL when contrastive image objectives are required, substantially closing the gap between model-free and model-based performance.** In Video Background (Fig. 2) and Occlusion (Fig. 3), model-based Joint(CV+R) improves dramatically over fully-contrastive counterparts and nearly matches model-free performance. The paper explicitly demonstrates that joint representations enable learning of stable long-term dynamics that contrastive image-only representations struggle with (Section 4 Discussion).

- **Large-scale evaluation across diverse task suites with multiple difficulty levels, including two visual modalities (RGB and depth) on a realistic manipulation task.** This breadth goes well beyond prior work on RSSM-based representations, which typically focuses on one or two domains. The OpenCabinetDrawer experiments with both constant and changing backgrounds using both color and depth images provide realistic validation.

- **The qualitative analysis (saliency maps and occlusion-free reconstruction, Fig. 6) supports the claim that joint representations focus on task-relevant aspects.** Joint(CV+R) saliency maps concentrate on the agent rather than video backgrounds, and Joint(CPC+R) captures both cart position and pole angle in occlusion tasks where image-only approaches fail.

## Weaknesses

### Fatal
None.

### Major

- **The comparison between mixed-loss methods (Joint(CV+R), Joint(CPC+R)) and the pure-reconstruction baseline (Joint(R+R)) is confounded by image augmentation.** The paper states (line 104): "Following prior work (Srivastava et al., 2021; Deng et al., 2022), we include cropping-based image augmentation *for contrastive approaches*." Joint(R+R) does not receive this augmentation. Because it uses reconstruction for images (which typically struggles with cropped reconstruction targets), the design choice is grounded in prior work, but it nevertheless means that every comparison between Joint(CV+R)/Joint(CPC+R) and Joint(R+R) conflates the loss choice with the presence or absence of augmentation. This is most consequential for the Locomotion suite (Fig. 4), where the paper specifically highlights that Joint(CPC+R) "outperforms image reconstruction (Joint(R+R)), which is noteworthy as the Locomotion suite tasks do not explicitly contain distracting elements." Without an augmentation-controlled ablation, the reader cannot determine whether the benefit on Locomotion comes from the mixed-loss design or simply from a data augmentation trick that the baseline lacks. The paper's core claim (ii) — "Combining contrastive approaches for images with reconstruction for low-dimensional signals can significantly improve performance" — is partially supported by clean comparisons (mixed-loss vs. pure-contrastive Joint(CV+CV)/Joint(CPC+CPC) where augmentation is matched), but the specific claim that mixed-loss outperforms pure-reconstruction rests on confounded evidence.

### Minor

- **The novelty framing modestly over-claims relative to the technical contribution.** The paper presents a "general framework" and "novel combination," but what is implemented is a straightforward per-modality choice between existing variational objectives (Eq. 3) and existing CPC objectives (Eq. 4), both previously proposed for RSSMs. The core value lies in the *empirical demonstration* that per-modality loss selection matters and in the systematic evaluation — this is a genuine and useful contribution, but framing it as a fundamentally new method is overstated. The paper would be stronger by more clearly positioning itself as a systematic empirical study with design lessons.

- **The Concat baselines are underspecified.** The paper says it "concatenates proprioception to image representations" (line 110) but does not clarify whether the RSSM receives both modalities during training (with proprioception added again at the policy head) or whether the RSSM only processes images. These two designs have different representational capacity — if the RSSM never sees proprioception, it cannot model temporal dependencies that require proprioceptive feedback, which could explain the gap between Concat and Joint. A brief architectural description would resolve this.

- **The β-KL weight for CPC methods is mentioned (Eq. 4, line 79) but its value is not reported** nor its sensitivity discussed. Given prior work's finding that this term is critical for preventing collapse in CPC-style objectives (Srivastava et al., 2021), the omission is relevant for reproducibility. (This detail may appear in the appendix, which is stripped by the parser.)

### Trivial

- **The split of DMC state dimensions into "proprioceptive" vs. "non-proprioceptive" entries is explained with one example (Ball-in-Cup Catch) but not fully specified for all seven tasks.** A table in the appendix or main text would aid reproducibility.

## Nice-to-Haves

- **Analysis of *why* joint representations close the model-free vs. model-based gap for contrastive methods.** The paper's current explanation ("joint representations allow learning of stable long-term dynamics") is somewhat superficial. Measuring model prediction error, latent dynamics quality, or mutual information between latent states and true states under each method would strengthen the result.
- **An ablation that augments Joint(R+R) with cropping** (or justifies rigorously why cropping cannot be applied to reconstruction) would resolve the central confound. If the augmentation cannot be applied, a comparison on Standard Images (where reconstruction works well) with both methods unaugmented would partially address the concern.
- **Training a joint RSSM with reconstruction for all sensors *with* image augmentation** would test whether the per-modality loss choice matters beyond the effect of the joint architecture itself.

## Removed Points

- The claim that the paper should "compare to an approach that fuses modalities into a single latent with reconstruction for all sensors while using augmentation for the image encoder." This is a specific version of the augmentation-controlled ablation that is already covered in Nice-to-Haves. The underlying concern is addressed by the Major weakness above.
- The suggestion to analyze the model-free vs. model-based gap more deeply. This is a reasonable request for deeper insight but not a flaw in what the paper already demonstrates. Moved to Nice-to-Haves.
- The criticism that the model-free vs. model-based comparison is "incomplete." The paper does provide a clear empirical finding and a plausible explanation; asking for deeper mechanism analysis is a future-work suggestion, not a weakness of the presented results.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a genuine experimental confound (augmentation asymmetry) that the paper's own narrative does not flag, but this is a methodological concern rather than a novel insight about the problem.

## Suggestions

1. **Run Joint(R+R) with cropping augmentation** (or a controlled proxy) to deconfound the comparison between mixed-loss and pure-reconstruction approaches. This is the single highest-impact improvement.
2. **Clarify the Concat RSSM training architecture** — does the RSSM receive both modalities during training, or only images? Report this in a sentence.
3. **Report the β value** for CPC methods (and ideally its sensitivity) in the main text or a table.
4. **Provide the full proprioception split** for all DMC tasks in a table, in the main text or appendix.
5. **Tone down novelty claims** and reframe the paper as a systematic empirical study demonstrating when and why per-modality loss selection matters for multi-sensor RL — this is actually a *stronger* pitch than claiming a new framework.

## Score and Decision

The paper makes a solid empirical contribution — joint representations consistently outperform concatenation across diverse and challenging domains, the evaluation is thorough, and the finding that per-modality loss choice matters is practically valuable for the RL community. However, the central comparison between mixed losses and pure reconstruction is confounded by asymmetric augmentation, which limits the strength of the paper's core claim (ii). This is addressable with additional experiments, and the paper's other contributions (joint > concat, mixed > pure-contrastive) rest on cleaner evidence.

I recommend a borderline accept with major revision to address the augmentation confound and the underspecified baselines.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>