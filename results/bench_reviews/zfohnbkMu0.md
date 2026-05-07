Now I have a thorough understanding of the paper and calibration anchors. Let me compose my final review.

## Summary

The paper argues that the open ML model ecosystem faces urgent supply-chain risks—including model tampering, malware injection, and training data issues—and that transparency mechanisms adapted from software supply chain security (specifically Sigstore) can and should be deployed now. It proposes two solutions: (1) model signing via Sigstore transparency logs, implemented as an open-source library with benchmarks on models up to Llama-3.1-405B; and (2) a zero-knowledge set construction for privacy-preserving dataset (non-)inclusion proofs, evaluated up to 100M entries.

## Strengths

- **Model signing is actionable and deployable (Section 5)**: Unlike many position papers that identify problems without offering working interventions, this paper ships a 4500-line open-source library and is actively integrating it with Kaggle. Benchmarks on actual large models (Table 1) show feasible overheads (0.03%–35% signing overhead, 6ms verification), making the urgency argument concrete rather than aspirational.

- **Systematic threat mapping using the SLSA framework (Section 3, Figure 1)**: The paper maps eight attack categories (A–H) from the software supply chain onto ML, documenting real incidents for nearly every category (malware on Hugging Face, namesquatting, PyTorch compromises, leaked API tokens, pickle deserialization attacks). This provides a useful organizing framework and demonstrates the breadth of the problem beyond the commonly discussed data provenance concerns.

- **Honest framing of transparency as detection, not prevention (Section 4)**: The paper explicitly draws the analogy to Certificate Transparency, which "does not prevent misissuance" but enables detection and accountability. This is a nuanced and technically informed framing that avoids overselling what transparency mechanisms achieve.

- **Thoughtful comparison of signing alternatives**: Section 4 justifies the Sigstore choice over PGP (which has <2% adoption on Hugging Face and was removed from PyPI), Sigsum, Notary, and SCITT based on maturity, transparency log architecture, and key management flexibility—rather than simply defaulting to a familiar tool.

- **Clean cryptographic construction for ZKS (Section 6.2–6.3)**: The construction adapting SEEMless-style verifiable data structures to dataset commitments is well-specified and draws on established primitives (VRFs, Merkle trees) in a sensible way, with ms-scale prove/verify times (Figure 4).

## Weaknesses

### Fatal
None.

### Major

- **The dataset commitment scheme (Section 6) provides only the format of transparency without the substance, and this gap is not adequately reckoned with**: Section 6.4 explicitly acknowledges "This does not prove, however, that the commitment accurately represents the data that was actually used in training the model." A malicious model creator can commit to any dataset and produce valid proofs of (non-)inclusion. The paper lists three paths forward (trusted regulator, ZK proofs of training, TEEs) as "interesting future work," but the ZK proof literature cited in Section 3 is itself acknowledged as not yet scalable to large models (Section 3: "there is thus currently no proof system that has demonstrated the ability to scale to large models"). This creates a circular dependency: the commitment scheme's meaningfulness depends on proof-of-training, which is currently infeasible. While partial transparency (accountability through commitment) still has value—similar to how CT works—the paper does not adequately analyze what guarantees remain when the commitment cannot be validated, nor discuss the risk of "transparency theater" in depth.

- **The gap between threats identified and threats addressed is significant, and the paper's urgency argument outpaces what its solutions deliver**: The paper maps eight attack categories (A–H) and documents real incidents across several. Model signing addresses attacks F and G; dataset commitments conditionally address a narrow aspect of attack D. Attacks A, B, C, E, and H—including some of the most frequently demonstrated like dependency poisoning (E) and namesquatting (H)—receive no proposed mitigation. While Section 4 notes some attacks are "difficult, if not impossible" to prevent, the paper states in Section 2 that "solutions urgently need to be designed and deployed." The paper should more explicitly reconcile the scope of the problem it identifies with the narrower scope of what it proposes to address, rather than implying its two proposals substantially address the threats it catalogs.

### Minor

- **Why would Sigstore adoption succeed where PGP failed?**: The paper documents that Hugging Face's GPG signing has <2% adoption and PyPI removed PGP support entirely. While Sigstore's architectural differences (ephemeral keys, no key management, identity-based certificates) provide implicit reasons, the paper does not explicitly analyze whether these differences overcome the adoption barriers that doomed PGP—particularly since both require active effort from publishers.

- **The software–ML analogy breaks down precisely at the point most relevant to dataset commitments**: In software, source code is inspectable and builds are deterministic, enabling reproducible builds that verify the binary corresponds to the source. In ML, the "source" (training data + code + hyperparameters) relates to the "output" (model weights) through a nondeterministic process, so there is no equivalent of a reproducible build. The paper briefly alludes to this at the end of Section 6.4 but does not analyze how this limits transparency in ML versus software. This is less of an issue for model signing (which signs an artifact regardless of how it was produced) but is central to the dataset commitment proposal.

### Trivial
None.

## Nice-to-Haves

- Analysis of what model signing guarantees when the hub itself is the adversary (attack G): Section 5.3 suggests hubs act as OIDC providers, creating a trust concentration in entities the threat model identifies as potential adversaries. The transparency log provides some accountability, but this scenario deserves explicit discussion.

- Adversarial adaptation analysis: If model signing becomes widespread, attackers may shift to unaddressed attack vectors (e.g., compromising training infrastructure, dependency poisoning). Discussion of how the threat landscape might shift would strengthen the paper.

- Presentation: The two proposals have very different maturity levels (deployable vs. speculative). The paper could benefit from more clearly foregrounding model signing as the near-term actionable contribution and treating dataset commitments as a longer-term research direction with clearly stated prerequisites.

## Removed Points

*These points were flagged to be removed; treat them with caution.*

- **"The paper is not truly a position paper / looks like two separate papers"**: This conflates presentation with substance. Position papers can and should include concrete proposals alongside their arguments; the combination of an actionable near-term proposal with a longer-term direction is appropriate for a position paper format.

- **"Lack of empirical evidence/proof"**: This is a position paper. The model signing section has substantial empirical evaluation, and the ZKS section has benchmarks. Demanding further empirical proof of a position argued from reasoning is not appropriate for position paper evaluation criteria.

- **"Overclaiming" about urgency**: Position papers are expected to make strong, debatable claims. The urgency framing is the paper's central position and is meant to spark discussion; it is not a factual overclaim.

- **"Transparency theater" counterargument not addressed**: The paper's impact statement explicitly states: "We stress that the solutions offered in this paper do not yet achieve this potential, and that achieving the full potential will require careful consideration to ensure that further solutions provide meaningful information rather than becoming onerous or a check-box exercise that provides a false sense of transparency." The concern is therefore addressed, even if briefly.

- **Criticism about missing related works**: Per instructions, do not mention missing related works without external sources to confirm their existence.

- **Formatting/style nitpicks and typos**: These are parser artifacts, not author errors.

## Novel Insights

The paper makes an underappreciated distinction between model integrity and data provenance as separate supply-chain concerns for ML. While data provenance has received extensive attention, the paper demonstrates that model integrity—ensuring the model you download is the one the publisher intended—is an overlooked but tractable first step. The key insight is that model signing is the "low-hanging fruit" of ML supply chain security: it requires no changes to how models are trained, imposes minimal overhead, and can be deployed at the hub level. This reframing—from trying to solve the harder provenance problem first to securing the model artifact itself—has practical implications for how the community should prioritize supply-chain interventions.

## Suggestions

- Explicitly quantify what model signing detects and under what assumptions. Walk through 2–3 concrete attack scenarios (e.g., compromised HF account, malicious insider at hub, supply-chain poisoning) and show step-by-step what model signing lets the publisher, consumer, and auditor detect.

- In Section 6.4, be more upfront about the severity of the commitment validity gap. Acknowledge that without commitment validity, the ZKS is an accountability mechanism (committing the trainer to a claim) rather than a verification mechanism, and discuss what enforcement or regulatory structures could make this accountability meaningful.

- Consider restructuring to foreground model signing (Section 5) as the primary actionable contribution and framing dataset commitments as a longer-term research direction with clearly stated prerequisites, rather than presenting them as equal contributions.

## Score and Decision

**Calibration anchors:**
- **Model Atlas** (BzFMBNqg7R, avg 7.0, Accept): Similar topic (model provenance/transparency) but less concrete implementation; our paper surpasses it in deployability.
- **Data Deals** (mdKzkjY1dM, avg 6.0, Accept): Similar topic (ML value chain, data provenance) with empirical analysis of 73 deals but less technical implementation; comparable but our paper has more concrete technical contribution.
- **LACP** (o3M9ibtZWV, avg 4.33, Reject): Proposes a protocol with shallow technical detail and no implementation; our paper is significantly stronger with real code and benchmarks.
- **Blockchain AI** (8Ow7kh78fk, avg 2.33, Reject): Vague, buzzword-heavy, no clear position; our paper is vastly better.

The paper under review is stronger than the Model Atlas (which scored 7.0) in terms of concrete implementation and evaluation, but weaker in that the Model Atlas presented a cohesive broad vision while this paper's second major proposal (dataset commitments) has a significant acknowledged gap. Relative to the Data Deals paper (6.0), this paper is more technically concrete with working code and benchmarks. The LACP and Blockchain AI papers are clearly below. Given the strong actionable contribution of Section 5 tempered by the incomplete nature of Section 6, I place this paper at 7.0—strong for a position paper due to its deployable contribution, but not exceptional given the gap between its urgency framing and what its solutions cover.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>