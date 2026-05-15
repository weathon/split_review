Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper introduces **Trustworthy Dataset Proof (TDP)**, a problem formalizing the verification that a model was trained on the *exact* claimed dataset (not just a distributionally similar one). The key technical contribution is **Data Probe** — a set of techniques that implant subtle statistical signatures in a small subset of training data (probes) so that the verifier can detect them by comparing output distributions between probe and non-probe samples. The integrity guarantee comes from binding probe selection to the dataset via a keyed hash: any modification to the dataset changes the hash, which changes which samples are selected as probes, causing detection to fail. The paper evaluates four probe types (Prominent, Absence, Untargeted, Targeted) across 4 datasets, 4 architectures, and 4 scoring methods.

---

## Strengths

- **Novel and well-motivated problem formulation.** The paper clearly distinguishes TDP from existing dataset *ownership* verification (watermarking, Dataset Inference) and from transcript-based approaches (PoTD). The formal threat model with defender goals G1–G4 (fidelity, low-invasiveness, harmlessness, efficiency) provides a rigorous foundation that prior work lacks.

- **Data Probe is a clever technical synthesis.** By replacing directed backdoor outputs (watermarking) with a requirement for only a *statistical difference* in output distributions, the method achieves watermarking-like usability (black-box verification, model-agnostic) while avoiding the security risks and performance degradation of backdoor-based approaches (Section 4.2, Definition 3).

- **Integrity is genuinely bound to the dataset via keyed hashing.** The probe selection mechanism (Section 5: "any minor modification of D will result in changes to the hash value, which in turn leads to changes in the selection of data probe") directly solves the integrity challenge that prior methods cannot address. This is a clean and well-reasoned cryptographic binding.

- **Extensive and convincing evaluation.** The paper tests 4 probe types × 4 scoring methods × 4 datasets (CIFAR-10, SVHN, CIFAR-100, Tiny-ImageNet-200) × 4 architectures (ResNet18, MobileNet, ShuffleNet, DenseNet). Table 2 shows that probes achieve high separation (PSA >> 0.5, pV << 0.1) for matched datasets while producing near-random results (PSA ≈ 0.5) for mismatched cases, with negligible accuracy impact (<±1%).

---

## Weaknesses

### Fatal
None.

### Major

- **Adaptive attack robustness is uneven and the key management tension is unresolved.** Table 3 shows that Prominent Probe (PP) is highly vulnerable to adaptive probe-forging attacks (ASR near 100% under some settings). The paper suggests hiding the key via a server API, but this conflicts with the protocol's requirement that the trainer submits the key as a certificate. If the trainer never learns the key, they cannot implant the probe during training; if they do learn it, they can forge it. The paper acknowledges this tension but does not resolve it. While UP, TP, and AP show better robustness, the PP vulnerability significantly limits the practical applicability of one of the four proposed probe types, and the overall security story for the framework is incomplete.

- **No experimental comparison with Proof-of-Training-Data (PoTD).** PoTD (Choi et al., 2024) is identified as the most closely related work. The paper dismisses PoTD as failing to verify "subtle manipulations" (citing PoTD's own stated limitations), yet no direct experimental comparison is provided. Given the overlapping goals, an empirical head-to-head (e.g., testing both methods on the same minor dataset modifications) would substantially strengthen the claim that Data Probe offers an advantage over the closest prior work.

### Minor

- **The "mismatched" experimental setup in Table 2 is underspecified.** The paper reports PSA* and pV* for "mismatched declared and training models" but does not clearly describe how this mismatch was constructed — whether it uses a different dataset entirely (e.g., train on SVHN, claim CIFAR-10) or a different probe selection on the same dataset. The distinction matters for the integrity claim. The text says "probe-mismatch cases" (Table 2 caption) but also "mismatched declared and training models" (Section 6.2), creating ambiguity.

- **AP detection logic requires more explicit justification.** While the Absence Probe is not contradictory (as the harsh critic claimed — the verifier compares probe vs. non-probe score *distributions*, not absolute confidence levels, so the mechanism is sound), the paper could benefit from explicitly explaining why setting probe weight to 0 does not produce false positives when the claimed and actual datasets are different. The current description in Section 5 (lines 134–135) is too brief for readers to follow the security argument.

- **The case study (Table 4) shows results for PP only.** Given that PP is the most vulnerable probe type to adaptive attacks, evaluating all probe types in the case study would provide a more complete picture of when the method works and when it doesn't.

### Trivial
None worth noting separately.

---

## Nice-to-Haves
- An empirical test using a *completely different* dataset (e.g., train on SVHN while claiming CIFAR-10) with explicit results showing verification failure for all four probe types.
- Visualization of ROC curves or score distributions for a representative dataset-model-probe combination to qualitatively illustrate the separation strength.
- A diagram of the hash-binding mechanism showing how changing one sample cascades to changed probe selection and failed verification.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Absence Probe contradicts the core goal of TDP"** — Removed because this criticism misunderstands the detection mechanism. AP detection compares probe vs. non-probe score *distributions*, not absolute confidence. If a dishonest trainer uses a different dataset *D* ≠ *D*, the hash changes, different probes are selected, and both probe and non-probe samples (from the claimed dataset) are equally unseen by the model, yielding no separation (PSA ≈ 0.5). The mechanism is sound.

2. **"Baseline comparisons (watermarking, DI) are inappropriate for the TDP task"** — Removed because the paper's case study explicitly aims to show that *existing techniques fail at TDP*, which is a valid benchmarking approach for a new problem. The paper does not claim these are ideal baselines; it demonstrates that methods designed for different tasks cannot handle TDP, motivating the need for the proposed approach.

3. **"Probe mismatched evaluation does not test different datasets"** — Partially removed; the paper states it tests "mismatched declared and training models," which covers dataset mismatch. The real issue is underspecification of *how* the mismatch was generated (kept as a minor weakness above).

4. **"The paper claims 'first exploration' despite PoTD's existence"** — Removed because the paper acknowledges PoTD as related work (Section 2) and distinguishes TDP as a *different problem formulation* focusing on data-level integrity rather than transcript-based correspondence. The claim of "first exploration" is about the TDP problem specifically, not about dataset verification generally.

---

## Novel Insights
None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the authors themselves have not already made or implicitly addressed.

---

## Suggestions
1. **Resolve the key management tension** by either (a) providing a concrete protocol where a trusted third party generates and distributes *k* to both trainer and verifier without revealing it to the trainer's adversarial self, or (b) explicitly characterizing the security degradation when *k* is known to the trainer and providing mitigations (e.g., probe randomization, multiple keys).
2. **Add an empirical comparison with PoTD** under the same experimental settings (minor modifications to CIFAR-10) to substantiate the claimed advantage over the closest prior work.
3. **Clarify the mismatched evaluation setup** in Table 2: specify whether PSA*/pV* are computed from a different dataset entirely (e.g., train on SVHN, verify on CIFAR-10) or from a different probe selection on the same dataset.
4. **Evaluate all probe types in the case study (Table 4)** rather than only PP, since the results for UP/TP/AP could differ substantially.
5. **Provide an explicit security argument for AP** showing why setting probe weight to 0 does not create false positives when datasets differ (even though, as analyzed, it does not — the reasoning is worth spelling out).

---

## Score and Decision

The paper introduces a well-motivated new problem, proposes a creative and technically sound solution (Data Probe with hash-binding), and supports it with a comprehensive evaluation across 16+ experimental configurations. However, the unresolved adaptive-attack robustness of PP, the tension in key management, and the absence of an empirical comparison with PoTD prevent the current version from being a fully mature contribution. The paper's core ideas are promising and likely replicable, but the security analysis needs completion before the claims can be fully trusted.

**Originality:** High — TDP is a genuinely new problem framing, and Data Probe is a novel synthesis of ideas from watermarking and membership inference.  
**Importance of question:** High — verifying authentic dataset use is practically relevant given lawsuits and regulatory scrutiny around training data.  
**Claims support:** Moderate — core claims are supported for non-adaptive settings, but adaptive robustness claims are only partially validated.  
**Soundness of experiments:** Moderately strong — comprehensive along most axes, but the mismatched evaluation setup is underspecified and PoTD is not compared.  
**Clarity of writing:** Good — clear definitions, threat model, and protocol description, though some experimental details could be expanded.  
**Value to community:** Moderate to high — the problem framing alone could stimulate follow-up work, and the Data Probe techniques are practically usable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>