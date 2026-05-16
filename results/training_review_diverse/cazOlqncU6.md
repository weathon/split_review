Now I have a thorough understanding of the paper and can verify each criticism against the actual text. Here is my consolidated review.

---

## Summary

This paper introduces Trustworthy Dataset Proof (TDP), a problem formalizing the verification that a model was trained on a claimed dataset *in its entirety* (not just in distribution or with a few specific samples). The authors propose Data Probe, a technique that selects a small subset of probe samples via a keyed hash of the full dataset, implants them during training (via label flips, oversampling, etc.), and detects their presence through distribution-level differences in model outputs. The core claim is that the hash-based binding ensures any modification to the training data changes the probes, so only the complete original dataset can pass verification.

## Strengths

- **Novel problem formulation.** The paper is the first to formalize TDP as a distinct problem: verifying the *complete and authentic* use of a claimed dataset, as opposed to ownership verification (watermarking) or distribution-level similarity (dataset inference). The formalization in Section 3 (defender/attacker goals G1–G4) is clear and captures an important trust gap in deep learning.

- **Extensive empirical coverage across many settings.** The evaluations span four datasets (CIFAR-10/100, SVHN, Tiny-ImageNet), four architectures (ResNet-18, MobileNet, ShuffleNet, DenseNet), four probe types, and four score calculation methods. The results in Table 2 demonstrate that when the claimed and actual datasets match, most probe schemes produce PSA >> 0.5 and pV < 0.1, while mismatched cases yield near-0.5 PSA, with accuracy degradation consistently < ±1%.

- **Low-invasiveness and harmlessness are validated.** The paper convincingly shows that the proposed operations (oversampling, absence weighting, label flips) can be applied without modifying model architecture or training hyperparameters, and with negligible impact on model accuracy (< ±1%). This is a genuine usability advantage over methods like PoTD (which requires full training transcripts).

## Weaknesses

### Fatal

- **The integrity guarantee (G1) does not hold under the paper's own threat model.** The paper claims that binding probe selection to the dataset via a keyed hash ensures "successful probe implantation and detection can only occur when the dataset is used in its entirety for training" (Section 4.2, line 102) and that "any minor modifications to D will result in changes to the hash value, which in turn leads to changes in the selection of data probe x_p" (Section 5, line 120). **This reasoning assumes the trainer runs `ProbeSelect` on their actual training data.** A dishonest trainer can instead: (1) compute probes from the *claimed* dataset D using the key k (which they choose and submit), (2) train on a different dataset D* while *explicitly including those probe samples* from D, and (3) pass verification. The verifier recomputes the same probes from D, finds them present in the model, and outputs 1 — even though D was never used for training in its entirety. The protocol provides no mechanism to prevent this substitution. This is a **structural flaw** that collapses the core claim of the paper: the method reduces to verifying membership of a small known subset, not complete dataset usage.

  The paper's own adaptive attack experiment (RQ4, Section 6.2) tests a *different* and weaker scenario: post-hoc embedding of probes into a model already trained on D*. The most natural attack — including the D-probes in the training set from the start — is not tested anywhere (Section 7, Table 4; lines 261–271). The paper acknowledges that "keeping the user's key k hidden from the users, such as by implementing it through a server API, might be a solution" (line 246), but even verifier-provided keys do not prevent this attack: the trainer can still compute probes from D with the verifier's key and include them in D*'s training.

### Major

- **The experimental evaluation does not test the attack that matters.** The case studies (Section 7, Table 4) test scenarios where the dataset is modified (duplication, backdoor insertion) and `ProbeSelect` is implicitly run on the modified data — causing probes to change and verification to fail. This is expected behavior but does not test the attack described above, where the trainer *actively retains the original probe samples* while changing the rest of the data. RQ4 (Table 3) tests post-hoc probe forging after training on D*, which is a different (and arguably harder) attack vector. Without experiments where the attacker includes the D-computed probes during initial training on D*, the paper's claims of robustness are unsupported.

- **The protocol places key selection in the attacker's hands** (Section 5, line 111: "user-specific key k"). The trainer chooses and submits the key. This means the attacker controls the randomness used for probe selection, enabling probe choice that minimizes detectability or maximizes attack success. The paper does not discuss a verifier-chosen key protocol, which would be the natural starting point for a security scheme.

- **No formal security argument or proof for G1.** The paper offers only informal reasoning (Section 5) that the hash-binding ensures integrity. Given that the claim is a security guarantee against an active adversary, an informal argument that assumes honest behavior during the step the attacker would subvert is insufficient. A proper treatment would need to specify what cryptographic assumptions hold and prove that fidelity (G1) follows from them under the defined threat model.

### Minor

- **Probe types are largely re-implementations of existing techniques.** TP (targeted label flip to a fixed class) is a standard backdoor watermark; UP (random label flip) is untargeted poisoning; PP/AP (oversampling/undersampling) are standard class imbalance techniques. The paper frames these as a "weakened" backdoor requiring only distribution-level differences, but does not demonstrate that this weakening yields a concrete advantage over a well-designed clean-label backdoor watermark in a controlled comparison. A direct apples-to-apples comparison with a simple random-subset backdoor watermark would clarify the contribution.

- **No calibration of false positive rates.** The paper uses a p-value threshold of 0.1 and a PSA threshold of 0.51, but does not analyze the false positive rate of honest training under these thresholds. The natural variation in model output distributions across seeds could produce false alarms. For a deployment-ready verification scheme, this calibration is essential.

- **Missing discussion of probe overlap with non-probe samples.** When probe samples are included in training on D* (the attack scenario), the non-probe samples from D* may also differ from the claimed dataset's non-probe distribution, potentially making the probe/non-probe distinction harder to detect. The paper does not analyze how the attack's detection difficulty depends on the similarity between D and D*.

### Trivial

- None that survive filtering — the parser-extracted text is clean of formatting artifacts.

## Nice-to-Haves

- A protocol variant where the verifier provides the key *after* the trainer commits to D (e.g., by publishing a hash) would be a natural and potentially effective mitigation, though it would require the trainer to be able to re-train if probes cannot be precomputed. Discussing this tradeoff would strengthen the paper.
- Exploring implicit probes whose behavior emerges only from the full dataset distribution (e.g., data-dependent features that cannot be simulated with isolated samples) would address the structural flaw at a deeper level.

## Removed Points

These points were flagged by the reviewer or strength finder but are removed or downgraded with justification:

1. **"The 100% blocking success in Table 4 is an artifact"** — Removed. The 100% success rate in Table 4 is expected behavior: if the dataset is modified and `ProbeSelect` is run on the modified data, the probes change, so verification correctly fails. The real issue is that this tests a different scenario than the attack. The criticism is kept in the *Major* section but rephrased.

2. **"Strength: Data Probe technique with integrity-guaranteeing probe selection ensures only the complete claimed dataset passes verification"** — Removed (conflicts with verified fatal weakness). The hash-binding does not prevent the trainer from computing probes from the claimed dataset and training on a different dataset that includes those probes.

3. **"Strength: Comprehensive threat model and goal-driven design"** — Removed (conflicts with verified weakness). While the threat model is formally defined, the protocol does not actually achieve G1 (fidelity) against the defined attacker, so the design does not meet its own goals.

4. **"The paper would benefit from a clearer security model: specify who chooses the key"** — The reviewer's point about the key is valid and kept in Major. The rest of this criticism (about auditing, computational resources) is too vague to retain.

## Novel Insights

The key insight that emerges from the critique is that the paper's hash-based binding solves a *different* problem from the one it claims. The hash ensures that if the trainer runs `ProbeSelect` on their actual training data, any modification to that data changes the probes. This is useful for *detecting accidental or passive* tampering but does not prevent an *active* adversary who can selectively compute probes from a claimed dataset and include them in a different training set. This distinction — passive tamper-detection vs. active adversary verification — is fundamental and suggests that the TDP problem, as defined, requires either (a) cryptographic commitment enforced before key revelation, or (b) a fundamentally different approach where probe behavior is implicitly induced by the full dataset distribution rather than by explicit sample inclusion.

## Suggestions

1. **Acknowledge the structural limitation explicitly.** Reframe the method as a *dataset membership proof* (certifying that specific samples from the claimed dataset were used in training) rather than as a full integrity guarantee. This would be an honest and still-useful contribution.

2. **Test the relevant attack.** Run experiments where the attacker computes probes from the claimed dataset D (with the known key), then trains on a modified/different dataset D* with those probe samples included from the start. Report how detection metrics change as D and D* diverge.

3. **Consider a commitment-based protocol.** Discuss a variant where the trainer commits to D (publishes its hash) before receiving the key from the verifier. Analyze whether this prevents or mitigates the attack, and under what assumptions.

4. **Compare directly with a simple random-subset backdoor watermark.** Training a model with a small set of randomly selected samples from D whose labels are flipped to a fixed target class, and measuring detection via output behavior on those samples, would provide a clean baseline for evaluating whether the "weakened" probe design offers any advantage.

## Score and Decision

The paper addresses an important problem and demonstrates careful experimental methodology across diverse settings. However, the core claim — that Data Probe can certify the *complete and authentic* use of a claimed dataset — is not supported. The protocol has a structural bypass: a dishonest trainer can compute probes from the claimed dataset and include them in training on a different dataset, passing verification. This is not a minor oversight or missing ablation; it is a fundamental gap between what the protocol achieves and what it claims. The experimental evaluation does not test this most relevant attack. While the problem formulation has value, the proposed solution does not solve it under its own threat model.

**Score: 4.0 / 10** — The paper has non-trivial merit in problem formulation and experimental scope, but the central contribution (the integrity guarantee) is invalid, and fixing it would require a major redesign of the protocol or a significant relaxation of the claims.

**Decision: Reject**

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>