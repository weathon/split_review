## Summary

This paper introduces FASTer, a framework for efficient autoregressive Vision-Language-Action (VLA) modeling. It comprises FASTerVQ, a transformer-based residual vector quantization action tokenizer that encodes action chunks as structured "images" with non-uniform semantic patchification, and FASTerVLA, a VLA model using block-wise autoregressive (BAR) decoding with a lightweight action expert. The paper reports SOTA results across 9 benchmarks, 5 embodiments, both simulation and real-world settings, achieving 97.9% on LIBERO and 87.9% on Simpler-Bridge while delivering faster inference than competing approaches.

## Strengths

- **Exceptionally broad evaluation spanning 9 benchmarks, 5 embodiments, simulation and real-world settings.** Table 1 compares against 12+ baselines on LIBERO and Simpler-Bridge; Figure 4 extends to six additional environments (VLABench, GalaxeaManisim, xArm real-world, R1Lite bimanual, R1Lite WBC). FASTer achieves 97.9% on LIBERO and 87.9% on Simpler-Bridge (12.9% above the next-best model π₀-FAST-D). This breadth substantially exceeds typical VLA evaluations.

- **Compelling cross-backbone demonstration of the tokenizer bottleneck thesis.** Figure 7 shows FASTer improves InternVL3.5-2B from 79.35% to 96.65% (+17.3 percentage points), PaliGemma2-3B from 93.5% to 94.8%, and Qwen2.5-3B from 91.3% to 95.4%. The massive InternVL gain is particularly striking—it transforms the weakest baseline into the strongest—and directly validates that action tokenization quality is the primary bottleneck for autoregressive VLAs.

- **Detailed inference efficiency analysis with per-component breakdown.** Table 2 provides measured wall-clock times on RTX 5090, showing 112ms total on LIBERO vs 197–556ms for π₀-FAST, and dramatic gains on high-DoF WBC (237ms vs 1,100–3,000ms for π₀-FAST). The observation that image encoding dominates (72–128ms out of 112ms) provides genuinely useful insight about diminishing returns of action compression.

- **Well-motivated action patchifier with non-uniform dimension grouping.** Section 3.1 describes partitioning action dimensions by physical semantics (e.g., end-effector position, orientation, gripper state grouped separately), addressing the highly non-uniform data distributions across action dimensions. This is supported by performance gaps in Figure 6.

- **Cross-embodiment generalization with clear data-scaling evidence.** Figure 8 shows training on single-arm delta-EEF trajectories and testing on unseen embodiments (Droid joint-velocity, Galaxea absolute joint-position, Aglex delta joint-position) with VRR improving from 0.394→0.78 and 0.663→0.9 as data scales from S to L.

## Weaknesses

### Fatal

None

### Major

- **No error bars or multi-seed evaluation anywhere in the paper.** The headline improvement on LIBERO is 97.9% vs π₀.5's 96.8% (1.1 percentage points). On VLABench (Figure 9), differences between π₀, π₀.5, FAST+, and FASTer are similarly small (roughly 2–3 points). Robotics success rates are inherently stochastic due to initial condition randomization, sensor noise, and simulator stochasticity. Without variance estimates, it is impossible to determine whether these marginal gaps are stable across runs or fall within run-to-run noise. This concern applies to virtually every comparison in the paper and directly affects whether the central SOTA claims are credible. The harsh critic correctly identifies this as "not a minor reporting gap—it directly affects whether the paper's central claims of SOTA performance are credible."

- **Codebook size asymmetry in the headline comparison.** FASTerVQ uses 4096 codes while FAST uses 2048 (Table 8 states "FASTerVQ (100% of 4096)" vs "Fast (48% of 2048)"). The paper does include size-controlled comparisons (FASTer(S), FASTer(L)) in Figure 5 as VRR tokenizer analysis, but these are not presented as policy performance in the main Table 1. The headline comparison therefore benefits from a larger codebook; a controlled policy comparison would strengthen the central claim.

### Minor

- **BAR loss vs. attention mask appears inconsistent.** Eq. 3 defines the BAR loss as conditioning each block token c_{j,i} on C_{<j} only (preceding blocks), but Figure 3c caption explicitly states "tokens within each block attend to preceding and intra-block tokens." If the attention mask permits intra-block attention but the training loss treats block tokens as conditionally independent, this approximation should be stated and justified.

- **BAR contributes modest incremental gains over FASTer w/o BAR.** Figure 7 shows BAR adds only 0–1.65 points on LIBERO across backbones (PaliGemma 94.00→94.80, Qwen2.5 95.40→95.45, InternVL 96.30→96.65). The paper should be more explicit that the headline contribution is primarily FASTerVQ rather than the full FASTer system.

- **FAST+ baseline used in multiple figures but not explicitly defined in the main text.** FAST+ appears in Figures 5, 9, and 10 without a clear main-text definition. It appears to reference Pertsch et al. (2025), but should be explicitly stated.

## Nice-to-Haves

- The number of evaluation trials/episodes for each benchmark should be stated in the main text rather than only in the appendix.
- A brief analysis of why FAST achieves only ~10% on the WBC task (Figure 4) would strengthen the paper's thesis—this near-total failure dramatically supports the tokenization bottleneck argument, but the paper doesn't discuss the mechanism (token count? variable-length issues? codebook collapse?).
- The specific σ values used for the primary VRR comparisons in Figures 5 and 6 should be more explicitly stated for reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The harsh critic's concern about including weaker baselines (Octo-Base, OpenVLA, MiniVLA, VQ-VLA) in Table 1: Every paper includes a range of baselines from weak to strong; the π₀-family comparisons are the critical ones, and they are present. This is standard practice.
- The criticism about FAST's WBC failure "deserving more explanation" is a nice-to-have, not a substantive weakness.
- Formatting nitpicks about benchmark enumeration.

## Novel Insights

The paper's key insight—that action tokenization is the primary bottleneck for autoregressive VLAs, and that a well-designed neural VQ tokenizer can simultaneously improve reconstruction quality AND inference speed—is strongly supported by the InternVL cross-backbone result (79.35%→96.65%) and the WBC inference comparison (237ms vs 1,100–3,000ms). The observation that image encoding dominates inference time (72–128ms out of 112ms total) is an underappreciated finding that reframes where optimization effort should be directed in VLA pipelines.

## Suggestions

- Add 3-seed results for key comparisons (Table 1, Figure 4) to establish that marginal SOTA gains are stable.
- Promote the controlled comparison (FASTer(S)/FASTer(L) vs FAST with matched data and codebook sizes) to a main-text policy performance table.
- Clarify Eq. 3 to accurately reflect whether intra-block conditioning is used during training or whether block tokens are treated as conditionally independent.

## Reporting: Calibration Anchors

**Round 1 bracket: 6.5–7.5**

Anchors retrieved across all rounds:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| gwZ90hFSL2.md (Chinese NLP humanoid robots) | 1.00 | 1 | Irrelevant topic, rejected — clearly below FASTer |
| Uj0h13lVrR.md (KL Divergence GFlowNets) | 1.00 | 1 | Unrelated, deeply flawed — below FASTer |
| KBSHR4h8XV.md (Early Fusion VLA) | 3.33 | 1 | Similar VLA topic but limited evaluation, rejected — below FASTer |
| oyXoGJQlUf.md (GRAIL) | 3.00 | 1 | Different approach, limited scope — below FASTer |
| MI0UiWeqOl.md (Poly-Autoregressive) | 2.33 | 1 | Rejected, different domain — below FASTer |
| IqGVIU4rvM.md (VQ-VAE + Diffusion tokenizers) | 2.50 | 1 | Rejected, image tokenization — below FASTer |
| Lr8IIc1rB8.md (Autoregressive Action Sequence Learning) | 4.00 | 1 | Similar topic, 3 sim + 1 real, limited novelty, rejected — below FASTer |
| PPDheO2z5v.md (Actra VLA architecture) | 3.67 | 1 | Similar VLA topic, limited eval, rejected — below FASTer |
| sAOtKKHh1i.md (Subwords as Skills) | 5.00 | 1 | Related tokenization idea, rejected — below FASTer |
| iVxxgZlXh6.md (LLaRA) | 5.25 | 1 | VLM for robot policy, accepted but limited real-world — below FASTer |
| VYOe2eBQeh.md (LAPA) | 5.83 | 1 | VLA pretraining, accepted — comparable topic, narrower scope than FASTer |
| p01BR4njlY.md (Solving New Tasks from Video) | 5.75 | 2 | Accepted, video knowledge transfer — less comprehensive than FASTer |
| h7aQxzKbq6.md (HAMSTER) | 6.00 | 1 | Hierarchical VLA, accepted — narrower evaluation than FASTer |
| lFYj0oibGR.md (VLM as Robot Imitators) | 6.50 | 1 | VLM policy, accepted — simpler method, less eval breadth |
| 9pKtcJcMP3.md (Video Language Planning) | 7.00 | 1 | Accepted, strong multi-platform eval — comparable quality to FASTer |
| 9ehJCZz4aM.md (Concept-Guided Policies) | 7.25 | 2 | Accepted, compositional IL — fewer benchmarks than FASTer |
| meRCKuUpmc.md (Predictive Inverse Dynamics) | 7.50 | 2 | Accepted, strong empirical work — comparable tier |
| wM2sfVgMDH.md (Diffusion-Based Planning) | 7.50 | 2 | Accepted, autonomous driving — different domain |
| pZISppZSTv.md (CLoSD) | 7.50 | 2 | Accepted, character control — different domain |
| pISLZG7ktL.md (Data Scaling Laws) | 8.00 | 1 | Accepted, massive real-world study (40k demos, 15k rollouts) — above FASTer |

**Analysis:** FASTer is clearly above the rejected papers (3–4) and lower-scoring accepts (5.25–6.0) like LLaRA and HAMSTER, which have narrower evaluations and smaller contributions. It is comparable to Video Language Planning (7.0) and Concept-Guided Policies (7.25), which share strong empirical breadth. FASTer's evaluation scope (9 benchmarks, 5 embodiments) matches or exceeds these 7.0+ anchors, and its cross-backbone demonstration is particularly compelling. However, the lack of error bars and small margins on key benchmarks prevent it from reaching the 7.5+ tier of papers like Predictive Inverse Dynamics (7.5) or Data Scaling Laws (8.0), which have larger-scale validation or more rigorous empirical protocols. The initial bracket was 6.5–7.5; Round 2 narrowed this to 7.0–7.5, and the final score lands at 7.0.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>