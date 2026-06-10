Now I have enough calibration. Let me finalize my assessment and write the review.

**Round 1 bracket**: 5.5–7.5 (based on comparison with prior version at 5.0, DiffMove at 6.2, Point Set Diffusion at 7.0)

**Round 2 narrowing**: The paper is clearly improved over its prior version (5.0), addresses broader claims than DiffMove (6.2, Reject), and has a novel insight enabling cross-city generalization. However, single-run evaluation and technical novelty are below stronger accepted papers like Point Set Diffusion (7.0). **Final bracket: 6.0–7.0.**

The paper's empirical improvements are large (4× KL), the generalization capability is genuinely novel, and the evaluation is comprehensive. But the single-run protocol and missing canonicalization ablation keep it from the top tier. **Final score: 6.5.**

Here is the complete review:

---

## Summary
This paper introduces TDDM (Temporal Deaggregation Diffusion Model), a diffusion-based trajectory generation framework that factorizes generation into spatial occupancy priors (marginal distributions over geographical occupancy) and temporal dynamics via canonicalization, enabling a single model to generalize across regions and cities without retraining. Evaluated on three GPS trajectory datasets spanning Beijing, Porto, and San Francisco, TDDM achieves ~4× lower symmetric KL divergence than the best baselines and demonstrates zero-shot cross-city generalization — a capability no prior method exhibits.

## Strengths
- **Novel spatial-temporal factorization with strong empirical validation**: The core insight — separating *where* people move from *how* they move via spatial priors — is cleanly formalized (Eqs. 1–5) and directly validated by the ablation (Table 2): removing spatial priors degrades KL_sym from 0.277 to 1.334 (~5× increase) while TSTR remains unchanged, confirming that spatial priors drive distributional alignment while temporal dynamics suffice for per-sample quality.
- **Large, consistent improvements across all distributional metrics**: TDDM achieves KL_sym of 0.277 vs. 1.153 (Diffusion-TS) and JS of 0.059 vs. 0.198 across three datasets spanning different continents and mobility patterns (walking/biking in Beijing, taxi in Porto and San Francisco), indicating gains are not specific to one failure mode or data source.
- **Zero-shot cross-city generalization**: Table 3 shows TDDM trained on Porto generates trajectories for Beijing and San Francisco with KL_sym of 0.335 — *better* than training on 25% of the target city's data (0.545). This is a qualitative advance over existing methods, none of which can do this.
- **Comprehensive standardized benchmark**: Six complementary metrics covering fidelity (TSTR), distributional alignment (KL, JS), proportionality (Density, Trip Error), and structural preservation (Pattern Score) across three cities on different continents, with standardized preprocessing applied to all models equally.
- **Informative ablation on region size** (Table 2): Smaller regions (1×1 km) slightly improve Pattern (0.930 vs. 0.917) but dramatically worsen Length error (0.150 vs. 0.004), validating the 3×3 km design choice with concrete evidence.

## Weaknesses

### Fatal
None

### Major
- **Single-run evaluation without variance reporting**: Tables 1 and 2 explicitly state "Models are trained, sampled and evaluated once per dataset." While the large-magnitude improvements (KL_sym: 0.277 vs. 1.153; JS: 0.059 vs. 0.198) would almost certainly survive multiple seeds, smaller margins — TSTR (0.011 vs. 0.013), Length error (0.004 vs. 0.003), Pattern (0.917 vs. 0.907) — are within plausible run-to-run noise. The reported TSTR standard deviations (±0.006, ±0.005) are across datasets (three cities), not across independent training runs. This weakens the paper's claim to consistent SOTA across *all* metrics, even though the core contribution (large KL/JS improvements) remains robust.

### Minor
- **Internal inconsistency in normalized coordinate range**: Section 3 prose and Equation 2 specify normalization to [-1, 1]^D (lines 121, 123, 131), consistent with scaling factor s = 2/width(r_c). However, Algorithm 1 line 6 states "Normalize X_r to [0, 1]^D" (line 185), Algorithm 2 line 11 says "Transform x_0 from [0, 1]^D" (line 210), and the algorithmic explanation also uses [0, 1]^D (line 169). If the two spaces are used for different components, this needs explanation; if it is a notational slip, it should be fixed throughout. Important for reproducibility.
- **Missing canonicalization ablation**: Table 2 ablates spatial priors and region size but not the canonicalization (similarity transform) itself — the mechanism underlying the paper's strongest claim (cross-region generalization). An experiment removing rotation or scaling would clarify whether the full similarity transform is necessary or if simpler normalization suffices.
- **KL_speed not defined in main text**: KL_speed appears in Tables 1, 2, and 3 but is absent from the main text's evaluation measures section (Section 4). The paper says "See Appendix E for details on all six measures," but this metric is not mentioned in the main text description.

### Trivial
- **"Unconditional" terminology**: The paper describes the task as "unconditional trajectory generation" (Section 2, line 81; Section 4.1, line 247), yet the method is explicitly conditioned on spatial priors H. The paper would benefit from more precise language (e.g., "distribution-level conditioned generation") to avoid confusion.

## Nice-to-Haves
- Brief computational cost comparison (wall-clock training time, memory) between TDDM (transformer encoder) and baselines (UNets, RNNs) would contextualize the performance gains for practitioners.
- A brief mention in the main text of how preprocessing (map matching, GPS noise re-addition) affects absolute metric values — the appendix (Table 9) addresses this, but a sentence in Section 4.2 would help.

## Removed Points
These points are flagged to be removed, treat them with caution:
- The harsh critic's concern about "zero-shot" framing requiring target data (Algorithm 2 line 3) is noted but is not a flaw — the method genuinely does not retrain or finetune on target data. "Zero-shot" in this context accurately describes the model ε_θ's behavior, even though aggregate spatial priors must be computed from target data.
- Concern about baselines potentially benefiting from more careful tuning: the paper uses the same preprocessing for all models and this is a standard experimental protocol. Without concrete evidence of suboptimal baseline configurations, this is speculation.
- The "w/o spatial prior + rejection" row in Table 2 as unexplained: the paper defers to the appendix, which is standard practice.

## Novel Insights
The most novel finding beyond the method itself is that training on Porto generalizes better to other cities than training on 25% of the target city's data for distributional metrics (KL_sym 0.335 vs. 0.545). This suggests that certain cities may serve as unexpectedly strong "universal source" datasets — rich, dense trajectory data from a single representative city can outperform sparse local data for distributional alignment, which is practically valuable and somewhat counterintuitive. The honest discussion of where transfer fails (Length error increases to 0.06–0.11, reflecting city-specific distance distributions) adds nuance.

## Suggestions
- Add 3–5 random seed runs per configuration with standard deviations in the main results table. Even if small-margin improvements don't survive, the large KL/JS improvements almost certainly will, and transparency would significantly strengthen the paper.
- Add a canonicalization ablation (e.g., no rotation, no scaling) to Table 2 to isolate the contribution of the similarity transform.
- Fix the [0,1]^D vs [-1,1]^D inconsistency throughout.
- Add KL_speed to the main text evaluation measures description.

## Calibration Anchors

| Anchor | Path | Avg Human Score | Round | Comparison |
|--------|------|-----------------|-------|------------|
| DynamicsDiffusion (molecular trajectories) | kKXIYUi8ff | 3.00 | 1 | Generic diffusion application, no novel spatial factorization or generalization |
| STDM (spatio-temporal diffusion) | 2orBSi7pvi | 3.00 | 1 | Time-series diffusion without spatial-temporal factorization or cross-domain transfer |
| TF-score (diffusion forecasting) | RDLvnUJ5JZ | 3.00 | 1 | Forecasting-only, no generative evaluation or generalization |
| DiffPath (road network path generation) | 1o3fKLQPRA | 4.50 | 1 | Path generation without cross-region generalization or spatial priors |
| Deep Temporal Deaggregation (prior version) | dDdxbdhMsY | 5.00 | 1, 2 | Prior version of this paper — lacked ablations, fewer metrics, no cross-city baselines |
| Large Trajectory Models (STR) | r125wFo0L3 | 5.00 | 1 | Motion prediction/planning, different task and evaluation |
| Synthetic Datasets (spatio-temporal PDE) | qq0zZMC4SM | 5.00 | 2 | PDE-based synthetic data, different domain and approach |
| DynST (transferable traffic forecasting) | vXSCD3ToCS | 4.60 | 2 | Traffic forecasting benchmark, different task |
| DiffMove (trajectory recovery) | VRFotuGLfM | 6.20 | 1, 2 | Trajectory recovery (not generation), narrower scope than TDDM |
| Conditional Variational Diffusion | YOKnEkIuoi | 5.80 | 2 | Novel diffusion formulation but different domain |
| Diverse Pedestrian Movements | DydCqKa6AH | 6.75 | 2 | Pedestrian generation, comparable quality but different domain |
| Point Set Diffusion | 4anfpHj0wf | 7.00 | 1, 2 | Novel diffusion framework for point processes — broader technical novelty than TDDM |
| Conditional Diffusion (neurodegeneration) | 9UGfOJBuL8 | 7.33 | 2 | Strong conditional generation but different domain |
| Fluid Simulation Diffusion | uKZdlihDDn | 7.60 | 1 | Strong contribution with novel GNN architecture, broader technical novelty |

**Bracket**: Round 1 placed the paper between 5.5 and 7.5. Round 2 narrowed to 6.0–7.0. The paper is clearly better than the prior version (5.0) and DiffMove (6.2, narrower scope), comparable to PedGen (6.75) but with more comprehensive evaluation, and slightly below Point Set Diffusion (7.0) which introduces broader technical novelty. The single-run evaluation is the main factor preventing a higher score.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>