Now let me run calibration searches to anchor the score.Now I have sufficient information to write the final review. Let me synthesize everything.

---

## Summary

UniHM proposes a three-stage framework for language-conditioned dexterous hand manipulation: (1) a Unified Hand-Dexterous Tokenizer using a shared VQ-VAE codebook across heterogeneous hand morphologies via cross-hand distillation; (2) a Qwen3-0.6B VLM trained with a progressive masking curriculum to generate manipulation token sequences; and (3) a physics-guided Gauss–Newton refinement enforcing contact, generative, and temporal priors to produce physically feasible trajectories. The system is evaluated on DexYCB and OakInk benchmarks and in real-world trials on a dexterous robot hand.

---

## Strengths

- **Progressive masked training demonstrably reduces exposure bias.** Table 4 shows removing masked training degrades MPJPE from 61.40 to 73.41 and FPL from 12.15 to 14.42 on DexYCB (seen), demonstrating the curriculum's concrete impact on sequential accuracy.
- **Physics-guided refinement improves physical plausibility.** Ablation (Table 4) confirms consistent metric gains when refinement is active: MPJPE drops from 65.78 to 61.40, FPL from 15.35 to 12.15, and FID from 33.57 to 31.24 on DexYCB seen, justifying the Gauss–Newton formulation.
- **Well-formulated energy-based refinement.** The contact energy (Eqs. 11–13), generative HOI prior (Eq. 14), and temporal smoothness prior (Eq. 15) are clearly specified and mathematically grounded with an asymmetric continuous penalty and Levenberg–Marquardt damping.
- **Real-world results show substantial improvement over baselines.** Table 3 shows UniHM achieves 65% Grab success on seen objects versus 20–30% for MDM/MotionGPT3 with Dex-Retargeting, and 60% on unseen objects versus 5–45%, supporting practical usability.

---

## Weaknesses

### Fatal
None.

### Major

- **Comparison baselines are out of domain — the main quantitative result is weakly supported.** Tables 1 and 2 compare against TM2T, MDM, FlowMDM, and MotionGPT3, all of which are full-body human motion generation methods (e.g., "a person walks forward") rather than dexterous hand manipulation methods. None of these were designed for finger-level hand-object interaction. Meanwhile, Section 2.2 explicitly cites HOIGPT (Huang et al., 2025) as doing "long 3D hand-object interaction, learning a bidirectional mapping between text and HOI sequences" — essentially the same task as UniHM — yet it is entirely absent from the comparison. Beating out-of-domain motion generation methods on a hand manipulation benchmark does not establish state-of-the-art within the dexterous manipulation literature, and the paper's own related work section identifies the more relevant class of methods.

- **The Unified Tokenizer's central claimed capability has no direct evaluation.** The paper claims the tokenizer enables "cross-morphology transfer": given a MANO pose, decode it with any robot-hand decoder via Eq. (6). Table 4's ablation does not include a "w/o Unified Tokenizer" (i.e., per-hand VQ-VAEs with no shared codebook) condition, making it impossible to assess whether the morphology-agnostic codebook contributes beyond architectural cleanliness. No cross-hand transfer fidelity experiment is reported, and codebook utilization per hand type is not measured. This directly undermines the second bullet-point contribution stated in the introduction.

- **Applying the authors' physics refinement to baselines is not a controlled comparison.** Section 4.3 states: *"Because prior action-generation baselines lack explicit physical-feasibility guarantees, we post-process their outputs with our physics-guided refinement to ensure a fair comparison."* The refinement (Eqs. 11–18) was co-designed around the VQ-VAE's output space and assumes dexterous-hand kinematic structure. Applying it to outputs from full-body motion models (different joint parameterizations, different semantic structure) is not a neutral post-process. This confounds what is attributable to the upstream generator versus the refinement — an ambiguity the ablation is supposed to resolve but does not for baselines. Further, this treatment is inconsistent with Table 3, where baselines use "Dex-Retargeting" instead.

### Minor

- **FID feature extractor is unspecified.** The FID values differ by an order of magnitude between DexYCB (31–56) and OakInk (204–337), strongly suggesting different feature spaces or normalization. Without specifying the extractor, the FID metric is not reproducible or interpretable across datasets, and cross-dataset comparisons are meaningless.

- **Table 3 reports success rates without trial counts.** "65%," "60%," etc. are reported with no indication of how many trials they are computed from (10 trials? 20?). With small trial counts typical of real-robot experiments, confidence intervals would dominate the differences shown. This makes Table 3 difficult to interpret as quantitative evidence.

- **The diversity–accuracy tradeoff introduced by masked training is not discussed.** Table 4 shows "w/o Masked Training" achieves substantially higher Diversity (73.09 vs. 39.62 on DexYCB seen; 74.88 vs. 42.70 unseen), while full UniHM achieves better position-error metrics. This means masked training significantly narrows the output distribution. Users of this system should understand this tradeoff, but the paper does not acknowledge it.

### Trivial
- The claim to be "the first framework for unified dexterous hand manipulation guided by free-form language commands" is asserted without a precise argument distinguishing it from HOIGPT (which generates "long 3D hand-object interaction" sequences from text, per Section 2.2). This should be clarified, not left as an unargued assertion.

---

## Nice-to-Haves

- Include at least one domain-relevant baseline from the dexterous manipulation literature (e.g., HOIGPT, Multi-GraspLLM) in Tables 1–2, even if the comparison cannot cover all metrics. This would place the paper's claims on firmer ground.
- Add a "w/o Unified Tokenizer" (per-hand independent VQ-VAEs) ablation to Table 4 and a cross-morphology transfer experiment to directly validate Eq. (6).
- Specify the FID feature extractor and provide trial counts for Table 3.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Strength: "State-of-the-art generation accuracy on standard benchmarks."** This conflicts with the verified weakness that the baselines are out-of-domain. The numeric improvements (e.g., MPJPE from 74.80 to 61.40) are real, but their significance is undermined by the baseline selection problem. Removed per the rule that weaknesses override conflicting strengths.
- **Harsh critic: "Training/inference mismatch."** The paper explicitly acknowledges this in Section 3.3 ("Our training and inference pipelines differ by design") and provides a reasoned justification (modularization allows CLIPort fine-tuning without retraining the HOI model). The critic's concern that the paper does not quantify the degradation is a reasonable improvement request but not a substantive flaw — moved to nice-to-haves.
- **Harsh critic: "Retargeting fidelity never measured."** The distillation step in Eq. (3) relies on retargeting quality, and the critic notes this is never measured independently. While fair, this is a methodological detail downstream of the main contribution and does not directly invalidate any result; demoted to a minor improvement suggestion.
- **Strength: "Decoupled perception and generation improves robustness."** The decoupling design is real but this is an architectural choice whose independent contribution is not measured. Removed as unverified by any ablation in the paper.
- **Strength: "Scalable language data annotation via GPT-4o."** Generic claim about using GPT-4o for annotation; not a distinguishing contribution of the paper. Removed as superficial.

---

## Novel Insights

The harsh critic raises an important but underemphasized observation: removing masked training in Table 4 produces substantially *higher* diversity scores (73.09 vs. 39.62 on DexYCB seen). This is the reverse of what one might expect if masked training simply improves quality. The implication is that the masking curriculum, while improving positional accuracy, substantially constrains the reachable output distribution — a diversity-accuracy tradeoff that is architecturally interesting and relevant to users who want a generative model that can produce varied manipulation strategies rather than converging to a single "safe" mode. This finding deserves explicit discussion.

---

## Suggestions

1. Replace or supplement the current baselines with at least one method from the dexterous manipulation literature (e.g., HOIGPT, Multi-GraspLLM, or even a retargeting-only baseline on the sequential prediction task) to demonstrate UniHM's advantage in its actual target domain.
2. Add a "per-hand independent VQ-VAE" ablation to isolate the contribution of the shared codebook and a cross-morphology transfer experiment (encode MANO → decode Shadow/Leap, measure joint error vs. direct retargeting) to substantiate Eq. (6).
3. Report the FID feature extractor used for each dataset (architecture, training set, normalization), and report trial counts and confidence intervals in Table 3.
4. Explicitly discuss the diversity-accuracy tradeoff surfaced by the masked training ablation.
5. Tighten the novelty claim relative to HOIGPT with a more precise technical comparison.

---

## Score and Decision

**Calibration Summary:**

**Round 1 Anchors:**
- `xcHIiZr3DT.md` (avg 2.50, Reject): Vision-based pseudo-tactile dexterous grasping — lower methodological rigor; clearly weaker than UniHM.
- `sXF5P4N7e8.md` (avg 3.00, Reject): Goal-conditioned masking for grasping — simpler, narrower contribution; weaker than UniHM.
- `twIPSx9qHn.md` (avg 5.00, Accept): Cross-embodiment dexterous grasping with RL — closely related topic; well-executed with proper domain-relevant comparisons.
- `VYOe2eBQeh.md` (avg 5.83, Accept): LAPA — VQ-VAE-based latent action pretraining for VLA models; stronger experimental design.
- `lFYj0oibGR.md` (avg 6.50, Accept): VLM-based robot imitation — cleaner and better validated VLA design.
- `Q6a9W6kzv5.md`, `KsUh8MMFKQ.md`, etc. (avg 8.00): Top-tier papers with stronger evaluation setups and broader impact.

**Round 1 bracket: 3.5 – 5.5.**

**Round 2 Anchors:**
- `Lr8IIc1rB8.md` (avg 4.00, Reject): Autoregressive action sequence learning — rejected due to limited novelty and non-rigorous real-world evaluation (10 trials, limited baselines). UniHM has a more ambitious and novel contribution, but also has more severe baseline selection problems.
- `twIPSx9qHn.md` (avg 5.00, Accept): Cross-embodiment dexterous grasping — directly comparable topic. This paper was accepted at 5.0 with proper domain-relevant comparisons but limited real-world trials (3 successful demonstrations). UniHM has more novel contributions but weaker experimental validation.
- `h7aQxzKbq6.md` (avg 6.00, Accept): HAMSTER hierarchical VLA — VLM-based open-world robot manipulation with proper baselines. Better experimental design than UniHM.
- `NxoFmGgWC9.md` (avg 5.50, Accept): Video generative pre-training for manipulation — accepted with good experimental validation.

**Positioning:** UniHM sits below `twIPSx9qHn.md` (5.0) due to the more fundamental baseline selection problem (wrong domain entirely) and the missing tokenizer evaluation, which together undermine both headline contributions. It sits clearly above the rejected `Lr8IIc1rB8.md` (4.0) because the system is more technically sophisticated and the contributions are more novel. The inconsistent treatment of baselines in real-world experiments and the unspecified FID extractor further reduce confidence in the claimed results. The paper lands between these two anchors, closer to the 4.0 Reject side because the core experimental claim rests on demonstrably out-of-domain comparisons and the second major contribution (tokenizer) has no direct validation.

**Final score: 4.0, Reject**

**Axis Assessment:**
- *Originality*: Moderate — the combination of VQ-VAE tokenizer, VLM, and physics refinement for dexterous manipulation is novel but individual components are adapted from existing work.
- *Importance of research question*: High — language-conditioned dexterous manipulation is a central challenge in embodied AI.
- *Claim support*: Weak — the main quantitative comparison uses out-of-domain baselines; the tokenizer's key claimed capability is unvalidated.
- *Soundness of experiments*: Poor — wrong-domain baselines, confounded baseline post-processing, unspecified FID extractor, missing trial counts.
- *Clarity of writing*: Good — the paper is clearly structured and the methodology is well described.
- *Value to research community*: Moderate — the physics-guided refinement formulation and masking curriculum have value, but the current evidence does not support the claimed state-of-the-art status.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>