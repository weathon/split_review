## Summary

The paper proposes MEGA, a memory-efficient variant of 4D Gaussian Splatting for dynamic scenes. It reduces per-Gaussian color storage by replacing 4D spherical harmonics with a per-Gaussian DC color and a shared temporal/view-dependent AC predictor, and reduces the number of Gaussians through a temporal-viewpoint-aware deformation field plus opacity entropy regularization. The empirical results show very large disk-storage reductions relative to the original 4DGS baseline while maintaining roughly comparable rendering quality and real-time FPS, but several claims are overstated and the deformation design raises a substantive representation-consistency concern.

## Strengths

- **Very strong storage reduction relative to the original 4DGS baseline, with competitive quality.** On Technicolor, Table 1 reports 4DGS at 6107.07MB versus MEGA at 32.45MB, while PSNR improves from 32.07 to 33.57 and FPS from 55.26 to 83.14. On Neu3DV, Table 2 reports 3128.00MB for 4DGS versus 25.05MB for MEGA, with very similar average PSNR/LPIPS: 31.57/0.0573 for 4DGS versus 31.49/0.0568 for MEGA.
- **The DC/AC color decomposition is concrete, simple, and empirically well supported.** The method replaces the 144-parameter 4D SH color representation with a 3-parameter DC component plus a shared MLP predictor, and Table 3 shows that “w/ DAC” preserves or improves quality much better than the grid-based compact replacement: e.g., Birthday PSNR 31.60 for DAC versus 30.49 for grid, and Flame Steak 33.34 versus 31.07.
- **The paper evaluates on two relevant dynamic-scene benchmarks and reports multiple practical metrics.** The experiments cover Technicolor and Neural 3D Video, and the tables include PSNR, DSSIM, LPIPS, FPS, and storage, which are the right axes for a compression-oriented dynamic rendering paper.
- **The combined deformation/opacity mechanism does substantially reduce Gaussian counts in the reported ablations.** For example, on Birthday, Table 3 reduces 15.43M Gaussians / 308.65M parameters for DAC to 0.91M / 18.48M for DAC+Deformation+\(\mathcal{L}_{opa}\), while PSNR increases from 31.60 to 32.02. This is meaningful evidence that the method is not only compressing attributes but also reducing representation size structurally.

## Weaknesses

### Fatal

None.

### Major

- **The deformation field makes geometry view-dependent, which weakens the claim that MEGA is simply a compact 4D scene representation.** In Eq. (5), the deformation predictor is conditioned on the view direction \(\gamma(\mathrm{sg}(\boldsymbol d_v))\), and in Eq. (6) this predicted deformation is applied to the 4D center, scale, and rotations. Thus, not only color but also the Gaussian geometry changes with camera viewpoint. This may be effective for image synthesis, but it is a stronger modeling choice than compressing a view-independent dynamic 4D scene representation. The paper does not evaluate multi-view consistency or compare against a time-only deformation field, so it is unclear how much of the compression/quality gain comes from a coherent dynamic representation versus a compact view-conditioned renderer.

- **The headline compression ratios are not fully established under a common accounting protocol.** The paper states that, after optimization, MEGA parameters are stored in FP16 and then zip delta compressed, and the abstract claims approximately \(190\times\) and \(125\times\) reductions compared with 4DGS. However, the paper does not clearly state that the same FP16/lossless-compression protocol is applied to the 4DGS baseline and other Gaussian baselines in Tables 1–2. The results still show that MEGA is much smaller, but the precise headline ratios mix learned representation changes with serialization/compression choices unless all methods are measured under the same protocol or the table separates raw, FP16, and lossless-compressed sizes.

- **The ablation evidence for the entropy-constrained deformation mechanism is mixed.** Table 3 supports the DAC color representation well, and the final model often greatly reduces Gaussian count. However, the deformation+opacity combination is not uniformly quality-preserving: on Flame Steak, DAC+\(\mathcal{L}_{opa}\) obtains 33.45 PSNR with 2.76M Gaussians, while the final DAC+Deformation+\(\mathcal{L}_{opa}\) drops to 32.27 PSNR with 0.87M Gaussians, below the 4DGS baseline at 33.19. This does not invalidate the compression result, but it weakens the claim in Sec. 4.3 that the combination maintains 4DGS-comparable quality in general. A rate–distortion analysis would be needed to show that the final method is consistently on the best quality/storage frontier.

- **Comparative claims against the broader SOTA are overstated.** The paper is convincing relative to original 4DGS on storage, but the evidence does not support broad “new standard” or generally superior quality/speed claims. In Table 1, STG has better DSSIM and LPIPS than MEGA on Technicolor despite lower PSNR. In Table 2, STG has higher PSNR and much higher FPS than MEGA on Neu3DV, and E-D3DGS has much better LPIPS with only moderately larger storage. The paper should frame MEGA’s contribution as an excellent compactness/quality tradeoff relative to 4DGS, not as uniformly better across all quality, speed, and storage metrics.

### Minor

- **The paper emphasizes memory efficiency but primarily reports disk storage.** The motivation repeatedly mentions memory/storage constraints, but the experiments report model size on disk rather than peak GPU memory during training or rendering. Because MEGA introduces AC color and deformation MLPs evaluated during rendering, reporting runtime memory would clarify whether the method is also memory-efficient in the operational sense, not only compact on disk.

- **The storage contribution would be clearer with a component breakdown.** Since MEGA stores per-Gaussian parameters, AC/deformation MLP parameters, FP16 values, and zip-compressed outputs, a table separating these components would help readers understand which part of the reported gains comes from DAC, Gaussian count reduction, precision conversion, and lossless compression.

- **FPS comparisons are partially heterogeneous.** The paper states that Deformable 3DGS, E-D3DGS, STG, and 4DGS are reproduced on a single A800 GPU, while other baselines are copied from original papers. This is acceptable if used cautiously, but the paper should avoid strong speed-ranking claims across methods measured under different implementations/hardware.

- **The selected ablation set is small for a mechanism that can fail on one of four shown scenes.** The ablation covers two Technicolor and two Neu3DV scenes. Since Flame Steak shows a large degradation for the final deformation+opacity model, dataset-wide ablations or at least additional failure-case analysis would make the conclusions more robust.

### Trivial

None.

## Nice-to-Haves

- Compare time-only deformation against time+view deformation to separate dynamic-scene modeling gains from view-conditioned geometry warping.
- Add rate–distortion curves over storage/Gaussian count for MEGA variants and 4DGS variants, rather than reporting only a single operating point.
- Report Gaussian participation statistics across all evaluated scenes, since the motivation in Fig. 3 is based primarily on Birthday.
- Include qualitative/quantitative temporal consistency or multi-view consistency analysis, especially because the method changes geometry as a function of view direction.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Generic “important problem” strength.** The claim that reducing 4DGS storage is important is true but generic; it is not retained as a core strength without concrete evidence. The concrete storage/quality results are retained instead.
- **Pure reproducibility nitpicks about small implementation details.** Concerns such as not specifying every pruning interval or minor hyperparameter are not central enough to count as evaluation weaknesses, especially because the paper gives a reasonably detailed implementation section and says it follows the original 4DGS hyperparameter settings for several thresholds.
- **Formatting, notation, or typo-like issues.** Any issues caused by PDF extraction or minor notation inconsistencies are excluded under the review instructions.
- **Requests for missing related work.** These are not included because external completeness of citations cannot be reliably verified here.
- **Statistical variation / confidence interval concerns.** While repeated runs could be useful, single-run evaluation is common in large-scale neural rendering benchmarks; this is not treated as a substantive flaw.
- **Overly broad criticism that the method is not “memory-efficient” because it introduces MLPs.** The MLPs may affect runtime memory and should be measured, but the reported storage reductions are real and large, so this concern is kept only as a minor request for runtime-memory reporting rather than a rejection-level issue.

## Novel Insights

The most important synthesis is that MEGA appears to be a genuinely effective *compact renderer* for dynamic Gaussian scenes, but its most aggressive compression mechanism changes the semantics of the representation: view-conditioned color is standard, while view-conditioned geometry is a much stronger choice. This distinction matters because the paper’s empirical story is strongest when framed as “storage-efficient novel-view synthesis relative to 4DGS,” but weaker when framed as “compressing a coherent 4D scene representation” or “setting a new standard” across all quality/speed/storage axes.

## Suggestions

- Reframe the contribution more precisely: emphasize compact dynamic Gaussian rendering relative to 4DGS, and avoid claiming broad SOTA superiority unless supported across PSNR, DSSIM, LPIPS, FPS, and storage.
- Apply the same storage protocol to all Gaussian baselines, or report a breakdown with raw FP32 size, FP16 size, lossless-compressed size, and learned-representation savings.
- Add an ablation comparing deformation inputs: time-only, view-only, and time+view deformation; also evaluate multi-view consistency if geometry remains view-dependent.
- Add rate–distortion curves across storage/Gaussian count for 4DGS, DAC, DAC+\(\mathcal{L}_{opa}\), DAC+Deformation, and the final model.
- Analyze failure cases such as Flame Steak, where the final model loses more than 1 dB relative to DAC+\(\mathcal{L}_{opa}\).
- Report peak GPU memory during training/rendering and a storage breakdown for per-Gaussian parameters versus MLP parameters and compression effects.

## Score and Decision

**Assessment by axis.**  
Originality is good: the DC/AC color replacement and entropy-constrained deformation are meaningful adaptations to 4DGS compression. The research question is important and practically relevant. The empirical support is strong for storage reduction relative to original 4DGS, but less strong for the precise headline compression ratios, the claimed deformation mechanism, and broader SOTA claims. Experimental soundness is mostly adequate but missing fair/common storage accounting, rate–distortion curves, and a key time-only deformation control. Clarity is generally good, though the paper should more explicitly discuss the implications of view-dependent geometry. The value to the community is meaningful, especially for dynamic Gaussian compression, but the overclaiming and representation-consistency issue prevent a stronger score.

**Calibration anchors considered.**

- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/okD9dbifxa.md`, avg 5.83 — dynamic/4D Gaussian work with useful ideas but concerns; MEGA has stronger compression evidence but similar overclaim/validation issues.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dkrEoT68by.md`, avg 6.00 — accepted dynamic Gaussian reconstruction anchor; MEGA is comparable in contribution strength but has more serious accounting/semantic concerns.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/c1RhJVTPwT.md`, avg 6.50 — Swift4D, a compact dynamic Gaussian method accepted despite concerns about decomposition and generalization; MEGA is similarly relevant but somewhat more problematic due to view-dependent geometry.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/xy9yv5siYQ.md`, avg 5.25 — dynamic Gaussian reconstruction with weaker setup; MEGA is stronger empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/DCandSZ2F1.md`, avg 6.50 — accepted 3DGS compression with strong results and some methodology/ablation concerns; MEGA is close but has a more central representation concern.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/PbheqxnO1e.md`, avg 7.00 — high-scoring Gaussian compression with strong storage results; MEGA’s results are impressive but less cleanly supported.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/dHYwfV2KeP.md`, avg 5.75 — accepted locality-aware Gaussian compression; MEGA fits around this borderline-to-accept range.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/JbRM5QKRDd.md`, avg 6.25 — entropy-constrained Gaussian/video compression anchor; MEGA has comparable motivation and results but weaker mechanism isolation.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/1PZt5nFlzH.md`, avg 5.00 — compression paper with strong claims but missing rate-size exploration and insufficient ablations; MEGA shares some weaknesses but has stronger top-line empirical gains.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/m3KuuE2ozw.md`, avg 6.00 — 3DGS compression with fair-comparison and ablation concerns; MEGA is similar in severity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/P2Fjm0nIit.md`, avg 4.33 — NeRF compression rejected for limited novelty and incomplete cost/storage breakdown; MEGA is substantially stronger because the compression gains against 4DGS are large and directly demonstrated.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ZWi6RpT4mJ.md`, avg 3.50 — weak compression/INR anchor; MEGA is clearly above this due to stronger experiments and relevance.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/POFrdKvpea.md`, avg 7.00 — high-scoring neural field compression; MEGA is below this because its claims require more careful accounting and controls.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/2prShxdLkX.md`, avg 6.75 — high-band dynamic Gaussian anchor; MEGA is somewhat below due to conceptual ambiguity.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/nkeF3iRJRo.md`, avg 5.00 — medium dynamic-scene Gaussian anchor; MEGA is stronger empirically.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/ylgg2RE7ub.md`, avg 4.00 — low-band dynamic Gaussian paper with limited novelty/experimental design concerns; MEGA is clearly stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/zFfZEQHUiv.md`, avg 4.00 — low-band pose-free dynamic neural field/Gaussian anchor; MEGA is above this due to clearer contribution and results.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/hrXt6Fdl2P.md`, avg 2.60 — low-scoring free-viewpoint video compression anchor; MEGA is far stronger.
- `/home/wg25r/split_review/datasets/deepreview_13k_calibration/GSckuQMzBG.md`, avg 3.00 — low-scoring NeRF/inverse-graphics compression anchor; MEGA is far stronger.

Relative to these anchors, this paper sits above the low and medium rejected compression papers because it has a clear method and very strong 4DGS-relative empirical reductions. It is below the cleaner accepted 6.5–7.0 Gaussian compression anchors because the view-dependent geometry design, storage-accounting ambiguity, and mixed deformation ablation directly affect the paper’s central framing. I would place it at the borderline accept/reject boundary, leaning slightly positive because the practical contribution is substantial and the main storage result relative to 4DGS remains meaningful even if the exact ratio is adjusted.

MY FINAL SCORE: <pineapple>6.0</pineapple>  
MY FINAL DECISION: <orange>Accept</orange>