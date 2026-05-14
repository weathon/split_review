Now I have a thorough understanding of both the paper and the calibration anchors. Let me synthesize the final review.

---

## Summary

This paper identifies and addresses several practical issues in the emerging online-map-based motion prediction protocol: (1) existing nuScenes splits create a train–validation distribution gap under two-stage training, (2) online mapping models have a limited perception range that leaves many agents without map context, and (3) standard metrics (ego-only, including static agents) are non-discriminative. The authors propose **OMMP-Bench**, featuring a new spatially disjoint three-way data split, refined evaluation metrics targeting moving non-ego agents split by distance from the ego vehicle, and a boundary-free baseline that uses deformable attention over image features to provide environmental context to agents beyond the map boundary. Experiments span multiple online mapping models (MapTR, MapTRv2-CL) and motion prediction backbones (HiVT, DenseTNT) with several integration methods.

## Strengths

- **Well-motivated identification of the perception-range mismatch.** Tables 2–3 convincingly demonstrate that extending online map range drastically degrades map accuracy (mAP drops from 0.124 to 0.014 for MapTR at 100×100m), while ground-truth maps at larger range do improve motion prediction. This is a genuine, previously overlooked practical problem in the protocol.

- **Concrete benchmark improvements with demonstrated impact.** The new spatial split eliminates the train–val gap, yielding a clear minADE improvement (0.6308 vs. 0.6839, Table 1). The refined metrics show that static agents are trivially predictable (minADE ~0.002, Table 6) and that methods improving ego prediction can degrade on non-ego agents (e.g., MapTRv2-CL+DenseTNT shows 4.0% minADE *increase* for far non-ego agents under unc/bev, Table 7), validating that the new metrics are more discriminative.

- **Useful ablation on map element types.** Table 5 quantifies which semantic categories matter for motion prediction, showing centerlines are most informative while combining all types yields best performance. This provides actionable guidance for online mapping model design.

- **Comprehensive evaluation across model combinations.** The benchmark integrates two online mapping models, two motion prediction backbones, and four integration methods (base, unc, bev, img), providing a broad baseline for future work.

## Weaknesses

- **The img baseline description is underspecified, hindering reproducibility.** Section 3.3 (lines 434–450) contains garbled/truncated text ("We donate the image features...", missing definition of IT(i) in Equation 1, unclear how deformable attention is integrated into the motion prediction architecture, what the feature backbone is, which layers are trained vs. frozen, and the training objective). While the code release commitment partially mitigates this, the paper text itself should be self-contained enough to understand the method.

- **The validation set is small (86 scenes) with no variance estimates.** Table 7 reports single-point metrics without standard deviations or confidence intervals. The 12.7% minADE improvement for far agents—the paper's headline result—could be unstable given the small subset size. Reporting sample counts per group and variance would substantially strengthen the conclusions.

- **The claim that prior splits caused "misleading conclusions" is not fully substantiated.** Table 1 shows absolute performance differences between split configurations but only for a single method combination (MapTRv2-CL+HiVT). To justify the strong language about "misconceptions" and "mis-usage," the paper should demonstrate that method *rankings* change under the old vs. new splits, not just absolute scores. The subsampled default split (Split 4: minADE 0.6373) actually approaches the proposed split's performance (Split 1: 0.6308), suggesting the ranking issue may be less severe than claimed.

- **NuScenes-only evaluation limits generality claims.** The paper acknowledges this is because only nuScenes provides all required modalities (raw camera + HD maps + trajectories), but the benchmark's conclusions about splits and metrics are necessarily dataset-specific until validated elsewhere.

- **The "misconceptions" framing is stronger than the evidence supports.** Training a motion predictor with online maps generated on the map model's training set is a standard two-stage transfer setup, not inherently a methodological error. The spatial overlap issue (from Yuan et al., 2024) and the train–val gap are real concerns, but calling them "misconceptions" and "misunderstandings" overstates the case. The refined metrics (non-ego agents, close/far split) are sensible extensions, not corrections of errors.

## Detailed Assessment of the Harsh Critic's Concerns

- **"Unfair comparison of the img baseline":** This concern is **overstated**. The img baseline uses image features from the online mapping model's own backbone—the same sensor data all methods ultimately depend on. The benchmark rules (Appendix A) explicitly permit using "any outputs or features produced by the online mapping model, such as online maps, BEV features, or image features." The img method's value proposition is precisely that image features can provide environmental context where decoded maps cannot reach. This is a legitimate design exploration, not an unfair comparison. The methods are compared under the same protocol rules.

- **"Insufficient demonstration about splits":** Partially valid. See weakness about ranking changes above.

- **"Incomplete baseline specification":** Valid, as noted in the first weakness above.

## Overall Assessment

OMMP-Bench makes a timely and practically valuable contribution to an emerging evaluation protocol (established only in 2024). The identified issues—perception-range mismatch, train–val gap from two-stage training, and non-discriminative metrics—are real and well-motivated. The proposed solutions (spatial split, refined agent selection and grouping, the img baseline concept) are sensible and supported by experiments. The ablation on map element types provides useful guidance. The main weaknesses are addressable: the img baseline needs a clearer description, confidence intervals should be reported, and the strong language about "misconceptions" should be tempered or better justified by showing ranking changes. On balance, this is a solid benchmark paper that would benefit the research community.

---

### Anchor comparison for calibration:
- **DrivingGen (6.50, Accept Poster):** More comprehensive benchmark (diverse data, 14 models, multiple new metrics). OMMP-Bench is narrower in scope but similarly well-motivated.
- **Stability Under Scrutiny (4.67, Accept Poster):** Single-metric benchmark for online HD mapping, accepted. OMMP-Bench is more multi-faceted (split + metrics + baseline) with comparable experimental breadth.
- **Car4Cast (4.50, Reject):** Novel dataset/benchmark for LLM-based motion forecasting, rejected for limited scope and missing inputs.
- **Revisiting SD Map Motion Prediction (4.50, Withdrawn/Reject):** Related topic (map-based motion prediction), rejected for incremental engineering contributions.

All anchor papers cited above: DrivingGen, Stability Under Scrutiny, MMHU, Car4Cast, Revisiting SD Map Motion Prediction, STM4D, MTG-RPD.