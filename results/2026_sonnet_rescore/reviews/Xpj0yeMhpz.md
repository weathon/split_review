Now I have read the full paper. Let me write the meta-review based on my direct verification of the reviewer claims.

---

## Summary

This paper decouples the "class label" from the "target concept" in machine unlearning, formalizing three new mismatch settings beyond the conventional all-matched scenario: *target mismatch* (target concept is broader than forgetting data labels), *model mismatch* (model granularity differs from target), and *data mismatch* (both data and model granularity differ from target). The paper provides a representation-level theoretical analysis (Theorem 3.2) grounding a "gravity effect" where forgetting one subset affects nearby representations, and proposes TARF — a three-phase framework using annealed gradient ascent and selective gradient descent — demonstrating large improvements over baselines across CIFAR-10/100 and ImageNet benchmarks.

---

## Strengths

- **Novel and concrete problem taxonomy**: The four-way formalization of mismatch (Figure 1, Table 1) — using $\mathcal{L}_D$, $\mathcal{L}_M$, $\mathcal{L}_T$ to enumerate all combinations of subclass/superclass relations — is a genuine conceptual contribution. The taxonomy is operationalized directly through CIFAR-100's class/superclass structure, making it concrete and reproducible.

- **Principled representation-level analysis (Theorem 3.2, Figure 3)**: The paper derives a formal bound connecting the cross-subset loss divergence $\Delta L_{s_1,s_2}$ to representation distance $d_h(x_1, x_2)$ under gradient ascent, then validates the gravity co-movement with t-SNE visualizations and loss-curve dynamics. This analysis directly explains *why* standard methods fail in each mismatch setting and motivates TARF's identification phase.

- **Large, consistent empirical gains on mismatch settings**: Table 3 shows TARF achieves Gap ≤ 1.23% on CIFAR-10 target mismatch vs. next-best 20.80% (GA), and Gap = 0.21% vs. 8.86% (GA) on CIFAR-100 target mismatch. The improvements are consistent across data mismatch, model mismatch, and large-scale ImageNet-1k experiments (Table 4). Ablations in Figure 7 characterize the contributions of annealed schedule, model architecture robustness, and operation choice on identified data.

---

## Weaknesses

### Fatal
None.

### Major

- **No setting-aware (informed) baseline tested**: Baselines (FT, GA, L1-sparse, SCRUB, BS, SaUfn) are applied without any adaptation to the mismatch settings. TARF receives oracle information about the number of false-retaining classes (Section 2: *"we assume that the number of classes in $\mathcal{D}_{un}$ belonging to the target concept is known in target mismatch forgetting"*) and uses this to set threshold $\beta$ via the top-10% accuracy-drop criterion (Eq. 5). A minimally informed baseline — e.g., for target mismatch, identify the superclass of forgetting data and expand the forgetting set to include all subclasses, then run standard GA or SCRUB — would isolate what TARF's three-phase framework specifically contributes over any oracle-assisted adaptation. Without this, the reported gaps (20.80 → 1.23) prove that naïve application fails, but do not demonstrate that the full TARF machinery is *necessary*. This is the most important gap in the evaluation.

- **Table 5 (TOFU) has uninterpretable numerical coincidences**: In the first LLaMA3.2-1B-Instruct sub-table (lines 309–310), TARF (GA) and TARF (NPO) produce identical values across all six cells: 0.0762/0.0824/0.0095/0.0094/0.0095/0.0094. In the Representation Mismatch / Data Mismatch sub-table (lines 314–315), TARF (GA) and TARF (NPO) are again identical, and each setting pair (Representation Mismatch = Data Mismatch) shows the same values for all methods. In the third sub-table (lines 316–320), GA, TARF (GA), and TARF (NPO) all produce identical results (0.0002/0.1814/0.0000/.../0.0000). Different optimizer choices (GA vs NPO) should produce distinct loss trajectories; identical outputs across settings that should differ are difficult to explain as measurement-level coincidence. Whether this stems from a PDF parsing artifact or a data reporting issue, the LLM case study as presented does not constitute interpretable evidence of TARF's effectiveness in that domain. The paper directs readers to Appendix F.8 for more discussion, which was stripped from the parsed version.

### Minor

- **Oracle assumption about the number of false-retaining classes deserves more prominence**: The assumption that the requester knows how many classes in $\mathcal{D}_{un}$ belong to the target concept (Section 2) is operationally non-trivial. TARF's Phase I identification relies on this (Eq. 5: $\beta$ = lowest value of top-$p$% accuracy drop). The paper mentions a weakly-supervised scenario in the appendix and discusses robustness in Appendix E, but the main text does not compare the weakly-supervised variant quantitatively to the full-information case. Surfacing this in the main text — even a single supplementary row in Table 3 — would clarify the practical regime of the method.

- **The Gap metric averages over qualitatively different failure modes**: Gap = $\frac{1}{4}\sum|\mathcal{R} - \mathcal{R}^*|$ equally weights UA, RA, TA, and MIA. In mismatch settings, UA and MIA directly measure whether the target concept was forgotten, while RA and TA reflect utility preservation. A method that preserves RA/TA by over-forgetting UA can produce the same Gap as one that precisely hits the retrained reference for different reasons. Table 2's fine-grained UA-F / UA-R split is the more informative reporting format; applying this to target and data mismatch settings in Table 3 would better characterize each method's failure mode.

- **Stable diffusion evaluation is qualitative only in the main paper**: Figure 6 presents visually plausible concept removal ("springer" and "tench") for a data mismatch scenario, but no quantitative metrics are reported in the main text (the paper defers full results to Appendix E.3). Established evaluation protocols for concept erasure in diffusion models (e.g., CLIP similarity, generation accuracy on erased vs. retained prompts) would strengthen the generative application claim.

- **Logical tension in Phase I under under-entangled representations is unaddressed**: Section 3.2 Remark 3.2 argues that false-retaining data is *hard* to affect via gradient ascent because its representation is distant from forgetting data (under-entangled). Yet Phase I relies on this same gradient propagating to identify false-retaining data. The paper observes empirically that the signal still works (Figure 5a — target classes show larger accuracy drops than remaining classes), and notes (line 128) that partial clustering exists. However, the seeming contradiction between the theoretical motivation for TARF (gravity is weak under under-entanglement) and its diagnostic use in Phase I (gravity is leveraged for identification) is not explicitly reconciled in the main text.

### Trivial

- **All-matched CIFAR-100 performance vs. SCRUB**: On the all-matched setting, TARF achieves Gap = 1.11 while SCRUB achieves 0.71 (Table 3). The discussion states TARF "generally performs better (or comparable with the best method)" without acknowledging this 56% performance gap in the all-matched baseline condition. This should be explicitly noted.

---

## Nice-to-Haves

- A systematic Phase I identification precision/recall curve as a function of $\beta$ (or equivalently the percentile cutoff) across different false-retaining fractions, rather than the single operating point shown in Figure 5(a), would substantially strengthen the representation gravity argument on its own terms.
- The computational cost of TARF is roughly 16–20× slower than GA (Table 3: TARF ~4.2–4.8 min vs. GA ~0.25 min), and comparable to FT/SCRUB. A brief discussion of the tradeoff relative to FT and SCRUB would help practitioners understand where TARF fits.
- For model mismatch, explicitly comparing TARF's fine-grained UA-F/UA-R to baselines in Table 3 (as done in Table 2 for CIFAR-10/100) would improve consistency.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Critic's claim that GA achieves Gap "close to" TARF on CIFAR-100 data mismatch**: The critic stated "GA achieves Gap=5.89 on CIFAR-100 data mismatch—close to TARF's 1.17." This is factually wrong. The 5.89 figure is from CIFAR-10, not CIFAR-100. On CIFAR-100 data mismatch, GA achieves Gap=2.43, while TARF achieves 1.17 — still a substantial and meaningful difference, not "close." Removed for factual inaccuracy.

- **Computation cost claim of "60–80×"**: The critic states TARF takes "roughly 60–80× more wall-clock time than GA." Table 3 shows TARF ~4.2–4.8 min and GA ~0.25 min, a ratio of ~17–20×, not 60–80×. Furthermore, TARF is comparable in time to FT, SCRUB, and L1-sparse. Removed for numerical inaccuracy; the computational cost is a minor note, not a substantial concern relative to comparable baselines.

- **"Fatal/structural" framing of the missing informed baseline**: The Harsh Critic calls this "structurally significant" and framed the performance gap as "largely reflect[ing] misconfiguration." While the concern about missing informed baselines is valid (retained as Major), calling it structural overstates the claim. TARF still requires three distinct algorithmic phases that a simple label-expansion baseline would not provide; it's an open question whether a simple adaptation closes the gap. The "fatal" framing is demoted to Major.

- **Claim about Stable Diffusion evaluation and "established quantitative evaluation protocols"**: The criticism assumes specific external benchmarks exist and were omitted. Given the paper defers to Appendix E.3, quantitative results may exist there. The point is retained only as a Minor weakness about main-text reporting, not a factual claim about absent methodology.

- **Strength: "Comprehensive and rigorous evaluation"** — This is largely generic. Retained as concrete evidence (ImageNet-1k, multiple architectures, ablations) but not as a standalone strength.

- **Strength: "Real-world applicability"** — This conflicts with the verified weakness about Table 5's reliability. Dropped as a standalone strength per conflict rule.

---

## Novel Insights

The paper's most insightful observation is the bidirectional nature of representation gravity: the same gravity effect that *causes* under-forgetting in under-entangled settings (false-retaining data is not dragged into the forgetting orbit) can be *exploited diagnostically* to identify which classes are within the target concept by measuring their differential response to early gradient ascent. This reframes a failure mode as a signal, which is the central intellectual move underlying TARF's Phase I. The three-phase framework makes explicit that different mismatch types require different interventions (identification for under-representation vs. separation for over-entanglement), which could generalize to other continual learning and representation-editing problems where semantic granularity mismatches arise.

---

## Suggestions

1. **Implement at least one setting-aware informed baseline per mismatch type**: For target mismatch, try a "superclass expansion" baseline that uses the known oracle class count to expand the forgetting set and applies standard GA or SCRUB. This is the most important revision to substantiate TARF's contribution.

2. **Repair or clearly explain Table 5**: Provide full per-run results or explicitly state in the main text whether the identical values reflect the TOFU benchmark's design (e.g., near-zero probabilities collapsing to machine epsilon) or experimental conditions. If it is a parser artifact, note explicitly in the appendix and include a summary statistic in the main text.

3. **Promote the weakly-supervised variant** from Appendix E to at least a supplementary table in the main paper, with direct comparison to the full-information case.

---

## Score and Decision

**Originality** (4/5): The mismatch taxonomy is genuinely novel; the algorithm builds on gradient ascent ideas but with a principled phased design.

**Importance** (3/5): Addresses a practically relevant gap in machine unlearning for real-world requests that span taxonomic boundaries.

**Claims Supported** (3/5): Core classification claims (Table 3, Table 4) are strongly supported. LLM case study (Table 5) is not reliably supported. Informed baseline gap prevents full attribution to TARF design.

**Soundness** (3/5): Theoretical analysis is motivating but the connection from Theorem 3.2 to Definition 3.3 is informal. Experiments are otherwise methodologically sound.

**Clarity** (3/5): Problem formalization and algorithm description are clear; Table 5 and the three-phase logical tension reduce clarity.

**Community Value** (4/5): The taxonomy and TARF framework are usable building blocks; the CIFAR/ImageNet benchmarks establish a concrete evaluation testbed for the community.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>3</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>4</community_value>
</subscores>