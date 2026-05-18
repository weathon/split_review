I've thoroughly read the paper and verified all reviewer claims against the actual text. Here is my consolidated review.

---

## Summary

This paper introduces a novel task — conditioning video generation on multisensory interoceptive signals (haptic forces, EMG, hand/body pose, gaze) — to achieve fine-grained control over simulated futures. The authors propose a multimodal feature extraction pipeline (MoE encoders + channel-wise cross-attention + softmax-based fusion) designed to align modalities while preserving unique information, plus an interaction regularization scheme (relaxed hyperplane projection) intended to capture causal structure. Experiments on the ActionSense dataset show the method outperforms text-conditioned and unimodal baselines, with comprehensive ablations and preliminary downstream applications in policy optimization and planning.

## Strengths

- **First to introduce multisensory interoceptive signals (haptic forces, EMG, hand/body pose) for generative simulation.** The paper states this clearly as a contribution (Section 1) and demonstrates through ablations (Table 1a) that combining all modalities yields better future frame prediction than any single modality. This is a genuinely new task formulation with practical motivation.

- **Proposed feature extraction paradigm explicitly designed to preserve unique per-modality information while achieving alignment**, unlike contrastive methods (ImageBind, LanguageBind) that maximize shared information and discard what is complementary. The ablation in Table 1d and comparison against these methods (Table 6a) support the design choice.

- **Comprehensive ablation studies across multiple axes**: contribution of each sensory modality (Table 1a), robustness to missing modalities at test time (Table 1b), fusion strategies (Table 1d), history horizon length (Table 1c), and the interaction module (Table 1d). This level of systematic evaluation is a genuine strength.

- **Demonstrated robustness to missing modalities at test time**, which is a practically important property for real-world deployment. The paper shows that a model trained on all modalities suffers minimal accuracy drop when individual modalities are withheld during inference.

- **Preliminary downstream applications** (goal-conditioned policy optimization and long-term planning) show the method can be integrated into robotic pipelines, providing evidence of practical utility beyond simulation quality metrics.

## Weaknesses

### Fatal
None.

### Major

- **Equation 1 (channel-wise cross-attention) is mathematically problematic as written.** The equation  
  \( z_{t,m,j} = \sum_i \frac{\exp(z_{x_{\bar{t},i}} \cdot z_{t,m,j})}{\sum_l \exp(z_{x_{\bar{t},i}} \cdot z_{t,m,l})} z_{t,m,j} \)  
  has the same variable \(z_{t,m,j}\) on both sides (a self-loop with no clear update step), and treats individual scalar dimensions as if they were vector tokens — the "dot product" between two scalars \(z_{x_{\bar{t},i}}\) and \(z_{t,m,j}\) is just multiplication, not a meaningful similarity measure between representation channels. The normalization sums over dimensions \(l\) of the *same* action vector rather than over anchor features, which does not match the described "cross-attention between anchor and action features." This is the core mechanism for aligning modalities to a shared latent space, and the description as written is incoherent. The surrounding text gives the correct intuition, suggesting this is likely a notational error, but the equation must be corrected before the method can be properly evaluated. This is the paper's most significant weakness.

### Minor

- **Unimodal baselines use the authors' own encoding pipeline rather than established unimodal methods**, making the comparison partly an ablation of input modalities under the same framework rather than a head-to-head comparison against specialized prior work. The paper acknowledges this limitation (line 136: "As there lacks direct baseline method that utilizes these action modalities for simulation, we use our own method for encoding these modalities") and does include external baselines for text (UniSim) and multimodal alignment (ImageBind, LanguageBind, Mutex). Nonetheless, the strongest claim — that multisensory data is strictly necessary — is somewhat tempered by the absence of established unimodal benchmarks that can be adapted to this task.

- **The interaction regularization module would benefit from direct latent-space validation.** The ablation in Table 1d shows that removing the module degrades performance, but does not confirm that the latent vectors exhibit the claimed geometric behavior (e.g., that the same interaction vector applied to different contexts produces similar relative change). A synthetic test or latent-space visualization (probing the vector directions/norms against ground-truth frame differences) would strengthen the claim that the improvement is due to the specific geometry rather than extra parameters or data-fitting.

- **Downstream applications are preliminary.** The policy optimization experiment uses a single task (one cooking scenario), and the planning experiment acknowledges error accumulation without quantitative evaluation. These are appropriate for a methods paper but the claims about enabling "general-purpose household robots" in the abstract are overstated relative to the evidence presented.

- **Key quantitative results (Tables 3a, 6a, 1a–d) are embedded as images rather than machine-readable text or LaTeX tables**, making it difficult to verify exact numerical values from the text alone. While the numbers are present in the figures, presenting them in text form would improve scrutability.

- **The self-supervised reconstruction loss \(\mathcal{L}_{\mathrm{SSL}}\) is not ablated.** It would be useful to know how much the reconstruction objective contributes to feature quality versus the cross-attention and fusion components.

### Trivial

- None.

## Nice-to-Haves

- Direct latent-space analysis of the interaction module (e.g., measuring whether the cosine similarity between interaction vectors correlates with ground-truth frame differences across context frames).
- Ablation of the self-supervised reconstruction loss \(\mathcal{L}_{\mathrm{SSL}}\).
- Reporting key comparative numbers (MSE, LPIPS, FVD for main comparisons) in a text table in addition to figure-based tables.
- Additional random seeds for the main experiment to estimate variance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Quantitative evidence is not present"** (Harsh Critic #2): The reviewer implies numbers are entirely missing, but the paper does contain quantitative results in embedded figure-tables (Table 3a, 6a, 1 series). The reviewer acknowledges this ("Even if the figures were present in the original submission"). The issue is one of presentation format, not absence of evidence. Downgraded from "critical" to minor weakness above.

- **"Writing contains multiple editing artifacts"** (Harsh Critic Other Observations): Artifacts like "6.5" and "(moved from end of sec. 2.2)" are parser artifacts from the extraction pipeline, not errors in the original submission. Removed per formatting-artifact rule.

- **"Evaluation setup conflates method comparison with architectural advantage"** (Harsh Critic #3): The reviewer claims the unimodal comparison is not a fair comparison against established methods. The paper transparently explains why existing unimodal methods (e.g., Karras et al.) cannot be applied to this setting and uses the same encoding pipeline for all conditions, which holds the architecture constant and makes the modality comparison valid. The paper also includes external baselines (UniSim for text, ImageBind/LanguageBind/Mutex for multimodal fusion). The reviewer's concern is partly addressed by the paper's own discussion and the presence of external baselines.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation emerging from this review is a methodological tension the paper identifies but does not fully resolve: generative simulation requires a representation that is *both* aligned across modalities (so information can combine) *and* preserves unique per-modality information (so complementary signals are not collapsed). This is fundamentally different from cross-modal retrieval, where alignment is the sole objective. The paper's proposed solution (channel-wise anchoring without contrastive loss + softmax fusion) is a reasonable first attempt at balancing these competing demands, but the mechanism by which the representation avoids the "one-to-many mapping problem" described in Section 3.2 while still achieving alignment is underspecified — especially given the issues with Equation 1. This tension between alignment and preservation is likely to be a recurring challenge for any future work on multimodal conditioning for generative models.

## Suggestions

1. **Fix Equation 1.** Replace the current scalar-channel formulation with a properly specified attention operation. If the actual implementation is standard vector-level cross-attention between projected action features and the anchor, write it as such. If a channel-wise operation is genuinely intended, provide a clear derivation and reference to prior work using similar schemes, and remove the self-loop on \(z_{t,m,j}\).

2. **Add a synthetic validation of the interaction module.** A simple experiment: take pairs of similar but distinct context frames, apply the same learned interaction vector, and measure whether the resulting frame-difference vectors have similar relative direction and magnitude (as claimed in Figure 2's conceptual diagram).

3. **Tone down the "general-purpose household robots" claim** in the abstract. The experiments use 64×64 video from 5 subjects on one dataset; the results are a proof-of-concept for a new task, not a deployable system.

4. **Convert key tables to LaTeX** for better readability and verification.

5. **Ablate \(\mathcal{L}_{\mathrm{SSL}}\)** to show the reconstruction loss's contribution independently of the cross-attention and fusion components.

## Score and Decision

This paper introduces a genuinely novel and well-motivated task, with thoughtful experimental design and thorough ablations. The idea of using multisensory interoceptive signals for generative simulation is timely and practically relevant. The core weaknesses — the problematic Equation 1 and the overstated generality claims — are individually addressable but together make the paper unsuitable for acceptance in its current form. Equation 1 is central to the method description and, as written, is incoherent; this must be corrected before the work can be properly evaluated. With a corrected method description, latent-space validation of the interaction module, and toned-down claims, this could become a strong contribution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>