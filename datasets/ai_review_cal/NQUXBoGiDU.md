- Decision: Reject
- Avg Score: 3.75
- Scores: 1, 3, 5, 6
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes Spiking CenterNet, a fully spiking neural network architecture for object detection on event data. The model combines a spiking adaptation of CenterNet (heatmap-based detection without NMS) with an M2U-Net decoder that uses binary skip connections. The paper also applies knowledge distillation from a non-spiking ANN teacher to the SNN student, claiming this as the first use of KD for spiking object detection. Experiments on the GEN1 automotive dataset show the model outperforms prior fully-spiking detectors (Cordone et al.) in mAP while using less energy, though it lags behind the partially-spiking EMS-ResNet (Su et al.) which uses non-spiking residual connections.

## Strengths

- **Outperforms prior fully-spiking detectors with better energy efficiency**: Table 1 shows the proposed SNN with KD achieves 0.229 mAP, exceeding Cordone et al.'s 64-ST-VGG+SSD (0.203 mAP) and DenseNet121-24+SSD (0.189 mAP). Energy per time step (0.619 mJ without KD) is substantially lower than both prior fully-spiking works (2.097 mJ and 1.557 mJ). This directly supports the claim of outperforming comparable previous fully-spiking work while using less than half the energy.

- **First application of knowledge distillation to spiking object detection**: Section 2.3 confirms no prior work combines KD with SNN-based object detectors. The approach is clearly described in Section 3.3 — a straightforward MSE-based distillation on the heatmap outputs — and the paper shows it improves mean mAP by 1.8 points and reduces variance.

- **Clean, fully spiking architecture that avoids non-spiking operations**: The model replaces residual connections with binary skip connections (concatenation rather than addition), merges BatchNorm into convolution for inference, and eliminates non-binary operations between layers. Figure 2 shows the spiking expansion block design. The Discussion (Section 5) explicitly contrasts this with Su et al.'s approach which uses non-spiking residual connections.

- **NMS-free design enables full temporal utilization**: CenterNet's heatmap peak extraction replaces costly NMS (Section 3.1). Averaging head outputs over time steps makes the model robust to varying time-step counts, as shown in the ablation study (Figure 3).

- **Rigorous evaluation**: Reporting mean and std over 5 seeds, ablation on time steps (fixed and variable windows), and transparent acknowledgment of trade-offs (KD increases firing rate from 10.8% to 17.4%).

## Weaknesses

### Fatal
None.

### Major
- **Temporal asymmetry in the KD setup undermines the evaluation**: The non-spiking teacher is trained on **20 ms windows** (single time step), while the SNN student is trained on **100 ms windows** (5 time steps of 20 ms each). The teacher therefore receives 5× less temporal information. The paper notes this asymmetry in the implementation details (line 236: "we instead sample 20 ms for its training to keep the information per time step similar") but never discusses how this limits the teacher's quality or the distillation benefit. If the teacher had access to the same 100 ms window, the KD gain (currently a modest 1.8-point mean mAP improvement) could be larger — or the comparison could reveal different dynamics. This is a methodological gap that needs explicit discussion or experimental remediation.

### Minor
- **Abstract framing overstates comparative positioning**: The abstract claims the model "significantly outperforms comparable previous work" without specifying "fully spiking." Since Su et al. (2023) achieve 0.286 mAP with 9.3M params — higher than the proposed 0.229 mAP — a reader could reasonably interpret "comparable previous work" to include all prior SNN-based detectors. The paper transparently acknowledges Su et al.'s higher mAP in the Discussion (line 309) and grays them in Table 1, but the abstract and introduction would benefit from precision: the contribution is state-of-the-art *among fully spiking detectors*.

- **Parameter disparity vs. Cordone not discussed**: The proposed model (12.97M params) outperforms Cordone's 64-ST-VGG+SSD (2.88M params) but with 4.5× more parameters. The paper never acknowledges that some of the performance gain may be attributable to capacity rather than architectural advances. While the paper's focus is energy efficiency (not parameter efficiency), the comparison should at least note this caveat.

- **Energy comparison with Su et al. lacks full accounting**: The paper correctly notes that Su et al. exclude their first coding layer's energy (line 311), but does not attempt to estimate or bound what that excluded cost would be. Since Su et al. report 0.393 mJ (partial) vs. the proposed model's 0.999 mJ, an apples-to-apples estimate is needed to substantiate the claim that the comparison is "difficult" — the gap is large enough that even doubling Su et al.'s reported energy would still favor their method.

- **Missing ablation: M2U-Net decoder vs. original CenterNet decoder**: The paper replaces CenterNet's transposed convolutions with M2U-Net's upsampling but never directly compares them in an ablation. This makes it impossible to isolate the contribution of the decoder choice to the overall performance and energy savings.

### Trivial
- **α hyperparameter selection is under-documented**: The paper states "We choose α=1 after initial experiments" (line 184) but provides no details on what was tested or how sensitive results are to this choice.
- **Learning rate asymmetry between ANN and SNN is noted but not justified**: ANN uses 1e-3 while SNN uses 1e-4. The paper does not mention whether these were independently tuned or what the tuning process was.

## Nice-to-Haves

- **Train the ANN teacher on the same 100 ms window** (either as a single aggregated frame or as a multi-step ANN). This would give a fairer test of KD's potential and would tighten the internal logic of the experimental design.
- **Report inference latency / FPS** on relevant hardware. Energy is only one dimension of edge deployment.
- **Quantify heatmap quality improvement** beyond visual inspection (e.g., entropy, false positive rate).
- **Compare against a fully-spiking version of Su et al.'s architecture** to clarify whether the performance gap is due to the fully-spiking constraint or other design choices.
- **Ablate the M2U-Net decoder** directly against CenterNet's original deconvolution-based decoder.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. Harsh critic's speculation that "with a stronger teacher (trained on full 100 ms), the gain might be larger, or it might vanish" — speculative, not verifiable from the paper as written. The core observation (temporal mismatch) is retained in Major weaknesses; the speculation about counterfactual outcomes is removed.
2. "Su et al.'s energy is likely lower even accounting for the excluded layer" — speculative without a specific estimate of the first coding layer's energy cost. The weaker version (incomplete accounting) is retained in Minor weaknesses.
3. "The comparison in the abstract and results claims is misleading" — overwrought framing. The paper is transparent in the body; the issue is precision, not deception. Reframed as a minor precision issue above.
4. Generic concern about "45nm technology... whether the relative advantage holds under newer technologies" — applies to all SNN energy papers using this methodology, not specific to this paper.
5. Strength Finder's "avoids expensive NMS" is kept but noted as a direct adaptation of CenterNet rather than a new mechanism — still a valid supporting strength since prior SNN detectors used NMS.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the temporal mismatch in the KD setup as the most significant actionable concern, which the paper itself mentions in passing but does not analyze or discuss.

## Suggestions

1. **Address the temporal mismatch directly**: Either re-train the ANN teacher on 100 ms windows (with matching temporal information) or add a dedicated experiment/discussion section that analyzes how the 20 ms vs. 100 ms asymmetry affects the KD results. This is the single highest-leverage improvement for the paper.
2. **Tighten the abstract and introduction**: Replace "comparable previous work" with "comparable fully-spiking previous work" or equivalent to avoid any ambiguity about the comparison scope.
3. **Add an ablation study comparing the M2U-Net decoder to CenterNet's original deconvolution decoder** — this would isolate a specific architectural contribution.
4. **Discuss the parameter disparity** in the Results or Discussion section to preempt concerns about capacity-driven gains.
5. **Provide an estimated upper bound** on Su et al.'s energy including their first coding layer, even if approximate, to make the energy comparison more informative.
