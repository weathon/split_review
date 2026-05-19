- Decision: Accept
- Avg Score: 5.40
- Scores: 6, 6, 6, 6, 3
Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes ReViWo, a framework that learns view-invariant representations (VIR) for visual robotic manipulation by decomposing images into view-invariant and view-dependent components using a dual-encoder autoencoder with a cross-reconstruction objective. The VIR serves as the state representation for training a world model (COMBO) and policy via offline RL. The method is evaluated on Meta-world and PandaGym simulation environments and a real-world ALOHA robot, demonstrating robustness under two types of viewpoint disturbance: novel camera installation positions (CIP) and continuous camera shaking (CSH).

## Strengths

- **Cross-reconstruction objective enforces disentanglement by construction**: Eq. 3 trains the autoencoder to reconstruct a target image using the VIR from one image and the VDR from a different viewpoint of a different state. This architectural design forces the two encoders to specialize — the VIE must capture what is invariant across viewpoints (task state), while the VDR captures viewpoint-specific information. Figure 7 confirms that the decoder can correctly compose state from one image with viewpoint appearance from another, providing direct evidence that the disentanglement works as intended.

- **Consistent and large-margin robustness across two distinct types of viewpoint disturbance**: In Figure 4, ReViWo maintains high success rates under both novel camera positions (e.g., Drawer Open CIP 93.9 vs. COMBO 0) and continuous camera shaking (e.g., Window Close CSH 89.4 vs. COMBO 4.4), while all baselines (COMBO, MVWM, BC) degrade severely. The margin is substantial — often 50–90 percentage points — making the robustness claim empirically grounded despite some variance.

- **t-SNE evidence validates that VIR clusters by task state across novel viewpoints**: Figure 6 shows that ReViWo's VIR produces tight clusters for the same state viewed from six novel viewpoints, while MVWM and VAE representations are widely dispersed. This directly supports the claim that the learned representation captures task-relevant state information that is stable across viewpoint shifts, and that the robustness is attributable to the representation itself.

- **Ablation confirms the contribution of both the world model and unlabeled data integration**: Table 3 shows that ReViWo with the world model outperforms ReViWo w/o world model (CQL) on most tasks (e.g., Window Close CIP 91.1 vs. 71.1), demonstrating the value of the world model component. Table 2 shows that incorporating Open X-Embodiment data (without view labels) boosts performance on several tasks (e.g., Window Close CIP from 65.6 to 91.1), indicating practical scalability beyond simulator data.

## Weaknesses

### Fatal
None. The core claims are supported by evidence; the issues below are addressable through revisions.

### Major

- **The contrastive loss and the unlabeled-data weighting factor are underspecified, harming reproducibility**: The paper mentions $\mathcal{L}_{\text{Contrastive}}$ in Eq. 3 and describes its intent in prose ("encourages $z_s$ consistent across identical states and varies across different states") but provides no equation, loss function type (InfoNCE, triplet, margin-based, etc.), or implementation details. Similarly, the weighting factor for unlabeled Open X-Embodiment data (mentioned in Section 3.2) is introduced to prevent the VDE from encoding all information, but its value and formulation are never specified. Both components are central to the method's operation, and their absence makes the approach not reproducible as-is.

- **The real-world evaluation tests only a behavior-cloning variant (ReViWo-BC), not the full world-model + RL pipeline**: The paper's title ("Learning View-invariant **World Models**") and abstract describe a pipeline that trains a world model on VIR and learns a policy through interaction with it. However, the real-world experiments (Table 1) use behavior cloning on VIR representations, with no world model or online RL training. The paper frames this as "preliminary evidence" and is transparent about the implementation, but the discrepancy between the claimed contribution and the real-world evidence is significant: the full method — world model and RL — is validated only in simulation. A clearer scope statement distinguishing what was validated where would be appropriate, ideally in the title or abstract.

- **Key architectural details for integrating VIR with COMBO are missing**: COMBO is designed for low-dimensional state inputs, but VIR is a patch-level feature sequence of dimension $M \times C$. How these patch-level features are flattened, pooled, or otherwise fed into COMBO's MLP-based dynamics and reward models is never described. The reward model is mentioned ("trained by supervised learning") but its architecture and training details are absent. This gap matters because the way VIR is consumed by the downstream world model could affect performance significantly.

### Minor

- **The negative ablation results (Open X-Embodiment hurting Door Open CSH, world model hurting Drawer Open CSH) are acknowledged but not analyzed**: The paper attributes the declines to "the diverse and unstructured nature" of Open X-Embodiment data and the world model's "difficulty in accurately predicting the next state" under shaking. These are plausible hypotheses, but no analysis (e.g., measuring distribution mismatch in the first case, or comparing world model prediction errors across tasks in the second) is provided. Without this, the reader cannot assess whether these are fundamental limitations or implementation artifacts.

- **Quantitative metrics for view-invariance are absent**: The t-SNE visualization (Figure 6) is qualitative and supports the claim, but a quantitative metric — such as the Fisher criterion (ratio of between-viewpoint variance to within-viewpoint variance of VIR), mutual information between VIR and viewpoint, or viewpoint classification accuracy from VIR — would strengthen the claim that VIR is truly view-invariant, especially given small sample sizes in the visualization.

- **No statistical significance testing**: Results are reported with error bars over four seeds, but no significance tests (e.g., paired t-tests across seeds) are performed. Given that some gains — while large — could have overlapping error bars on specific tasks, statistical validation would help solidify the comparisons.

- **PandaGym results are not fully presented in a clear figure**: The paper states evaluation on PandaGym environments but Figure 4 appears to primarily show Meta-world tasks. If PandaGym results exist, they should be reported with the same level of detail as the Meta-world results.

- **The claim that prior work has not achieved "complete and effective decoupling" is strong and unsupported**: This phrasing appears in the introduction. The paper does not define "complete decoupling" quantitatively, and ReViWo itself does not claim perfect decoupling. This language could be softened without weakening the contribution.

### Trivial
- Eq. 3 has a typo ("Contrasive" instead of "Contrastive").
- Section 3.2 contains an apparent formatting artifact: "function $(1-\tt t i m e s t e p)$" is garbled.
- "Intergration" (Section 3.2) should be "Integration".

## Nice-to-Haves
- Adding a baseline that also uses view labels (e.g., VAE with supervised contrastive loss over viewpoint, or a multi-view VAE conditioned on view embedding) would strengthen the claim that the *specific architectural decomposition* — not just the availability of view labels — drives robustness. This is not a necessary condition for acceptance but would make the contribution more compelling.
- A discussion of how the 20 viewpoints are selected (random grid, stratified sampling, etc.) would improve clarity.
- Reporting all PandaGym tasks individually would make the evaluation more complete.

## Removed Points

- **"Unfair comparison due to asymmetric use of view labels" (from Critical Issues)**: The critic claims the comparison is unfair because ReViWo uses view labels while baselines do not. However, the paper is not claiming "using view labels is better" — it is proposing a *specific architectural method* (dual-encoder cross-reconstruction) that requires view labels by design. Comparing against standard methods (VAE-based COMBO, MVWM) that do not use view labels is standard practice: it tests whether the proposed method beats the current state of the art. The paper acknowledges the reliance on view labels as a limitation, and the suggestion to add a view-label-aware baseline is a nice-to-have, not a required fairness fix. The critic's claim that view labels are "entirely responsible" for gains is speculative and unsupported by the paper's evidence (e.g., the cross-reconstruction mechanism is architectural, not merely label-supervised).

- **"Positional embeddings computed with function (1−timestep) is confusing" (from Section-by-Section notes)**: This is a PDF-parser formatting artifact and not present in the original submission. Removed per Hard Rules.

- **Criticisms about missing appendix content, missing proofs, or missing references**: Removed per Hard Rules — these sections are stripped by the PDF parser.

- **The claim that "the results are weaker than claimed" with the specific percentage numbers**: The critic's complaint about success rates being 60% with ±20% error bars is accurate but doesn't invalidate the claims. The paper acknowledges these limitations. The critic's framing as a fatal flaw is disproportionate; moved to Minor tier (covered under negative ablation analysis).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the underspecification of key loss terms and the simulation-only validation of the full pipeline, but these are gaps to fix, not novel observations about the method itself.

## Suggestions

1. **Formally define $\mathcal{L}_{\text{Contrastive}}$** with an equation (InfoNCE or triplet-style) and specify the weighting factor for unlabeled data. This is essential for reproducibility.
2. **Clarify how VIR (patch-level $M \times C$ features) is consumed by COMBO's MLP** — is it flattened, pooled, or processed via a small adapter network? Also specify the reward model architecture.
3. **Add a quantitative metric for view-invariance** (e.g., Fisher criterion on VIR clusters, viewpoint prediction accuracy from VIR).
4. **Scope the real-world contribution clearly** — if only BC was validated on hardware, say so in the title/abstract, or add the full pipeline to the real-world experiment.
5. **Analyze the negative ablation results** with quantitative evidence (e.g., measuring world model prediction error on Drawer Open CSH vs. other tasks) to distinguish fundamental limitations from hyperparameter issues.
