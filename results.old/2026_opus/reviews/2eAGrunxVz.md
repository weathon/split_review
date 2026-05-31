Let me verify the algorithm and read the rest of the paper if relevant, then check the harsh critic's key claim about Theorem 3.1.Now I have enough understanding of the paper. Let me verify one key concern by analyzing the construction: with s=1, output z^(1)_{i,j} = m_j XOR r_{p(i,j)}. For 3-wise independence, every non-trivial F_2-linear combination must be uniform Bernoulli. The XOR of any k ≤ 3 outputs involves k message bits (with multiplicities) and k padding bits. For the XOR to be NON-uniform, all involved m_j AND all involved r_p must appear evenly. With k=3, total m-bit usage is 3 (odd), so at least one m_j appears an odd number of times → uniform. So Theorem 3.1 actually does hold under the default config; the harsh critic's central technical claim is wrong.

Now let me run calibration.Now I have enough calibration data. Let me write the final review.

**Round 1 bracket**: 3.75 (SuperMark rejected) — 6.0 (Shallow Diffuse rejected) — 7.6 (Lightweight watermarking rejected). Paper plausibly sits in 4.5–6.0.

**Round 2 narrowing**: Most relevant anchors are Hidden in the Noise (5.83 Accept, similar distortion-free initial-noise watermarking), PRC Watermark / "An undetectable watermark" (6.50 Accept, paper's own baseline with stronger cryptographic guarantees), Shallow Diffuse (6.00 Reject), SAT-LDM (5.50 Reject), A Recipe for Watermarking (5.33 Reject).

---

## Summary
The paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models that converts a binary watermark message into Gaussian-like latent noise via (i) XOR-mixing with random padding through an invertible matrix T, (ii) projection onto the unit sphere followed by an orthogonal rotation C, and (iii) scaling by a chi-distributed radius. The authors prove the construction matches a standard Gaussian up to the third moment (spherical 3-design) and demonstrate competitive extraction speed (~4 orders of magnitude faster than PRC), strong adversarial robustness, and near-chance detection by trained classifiers.

## Strengths
- **Genuinely novel and clean construction**: the polar-decomposition recipe (binary XOR → spherical 3-design → chi-scaling) is mathematically elegant and yields a moment-matching guarantee up to degree 3 (Theorems 3.1, 3.2, Lemmas 3.3, 3.4). I verified that the 3-wise independence of z^(1) actually does hold under the default config — for any 3 outputs, the F_2-linear combination always touches an odd number of m_j bits, making it uniform Bernoulli regardless of padding collisions.
- **Significant computational advantage over PRC**: Figure 4 documents extraction roughly four orders of magnitude faster than PRC Watermark, removing the belief-propagation decoding bottleneck. This is a concrete, measured engineering win.
- **Empirical undetectability vs. trained classifiers**: Figure 2 shows that both a two-layer MLP at latent level and a ResNet-18 at image level remain at ~50% on Spherical Watermark, while Tree-Ring and (fixed-key) Gaussian Shading hit 97–100%. Table 1 shows FID matches the unwatermarked baseline.
- **Better robustness than PRC under adversarial attacks**: Table 2 shows TPR (Adv.) of 99.83 vs. PRC's 95.38, and ACC (Adv.) of 98.12 vs. 97.69, with much larger margins as distortion grows (Figure 5, 6a).

## Weaknesses

### Fatal
None — the central technical claim (3-wise independence of z^(1) and the spherical 3-design of z^(2)) actually holds. The harsh critic's pigeonhole-collision argument against Theorem 3.1 is incorrect because the m_j bits supply additional independent randomness; the XOR of any k ≤ 3 outputs always touches at least one m_j an odd number of times and is therefore uniform.

### Major
- **The formal "undetectability" definition in §3.1 (Eq. 2) is stronger than what is actually proved.** Eq. 2 requires a cryptographic notion (negligible advantage for any PPT adversary in security parameter ρ). The construction only guarantees matching the first three moments of the uniform-on-sphere distribution (Theorem 3.2 → Lemma 3.3 → Lemma 3.4). Section 5 quietly concedes this ("higher-order moments may deviate from the true prior"). A degree-4 polynomial-time distinguisher could in principle break the 3-design guarantee. The two real baselines that meet a genuine cryptographic definition — PRC Watermark and per-image-keyed Gaussian Shading — are framed as the same kind of object as Spherical Watermark, but they are not. The framing should be the more honest "we match moments to degree 3, at much lower cost than PRC" rather than "we are lossless."
- **The Gaussian Shading baseline in Figure 2 is the handicapped variant.** §4.1 admits "with fixed keys, Gaussian Shading no longer achieves true losslessness," then uses 5 fixed keys across 100 users — i.e., precisely the configuration that breaks Gaussian Shading's lossless property — as the indistinguishability baseline. The fair comparison (per-image keys/nonces, which is Gaussian Shading's intended operating point and the property the paper claims to improve on) is omitted in Figure 2. The "Gaussian Shading is detectable" headline is therefore partially an artifact of the chosen configuration. The right framing is that Spherical Watermark eliminates per-image key/nonce *storage* relative to a per-image-keyed Gaussian Shading, not that Gaussian Shading is fundamentally detectable.

### Minor
- **Lemma 3.4 is applied via "≈" rather than equality.** The lemma's converse — n = r·u ~ N(0, I) — requires u to be *uniformly* distributed on the sphere, but z^(3) is only a spherical 3-design (a finite set, not a distribution). So z_w is not literally Gaussian; the paper writes "≈" in the runtime descriptions and acknowledges this in the limitations, but the central narrative still treats the output as Gaussian.
- **Lemma 3.3 statement is malformed.** As written it asserts that the marginal law of z_i^(3) "converges to N(0, 1/l_x) as l_x → ∞," which is a degenerate limit (variance → 0). The intended statement is presumably √l_x · z_i^(3) → N(0, 1).
- **"Encryption-free" understates the secret-management story.** (T, C) is a fixed, long-term secret with security properties analogous to a cryptographic key; the paper states it must be kept secret to prevent unauthorized removal. The genuine win is the elimination of *per-image* key/nonce storage, not the elimination of encryption. The introduction and motivation should make this distinction explicitly.
- **Per-user threat model not directly tested.** In deployment each user has a fixed m_u and only r varies. The classifier tests in Figure 2 mix samples across users, so they implicitly invoke randomness over m. A more convincing experiment would fix m, vary only r, and show that a distinguisher with many samples per user still fails. The current evaluation is reasonable but not maximally adversarial.

### Trivial
- The justification in §4.3 for "larger s improves indistinguishability" is qualitative — it would help to indicate which higher-order property is gained as s grows.

## Nice-to-Haves
- A fair, per-image-keyed Gaussian Shading row in Figure 2 and Table 1, even if it requires the storage overhead the paper criticizes — this would convert the framing dispute into a clean trade-off comparison.
- Quantify the leakage of the 3-design when probed by degree-4 statistics, both theoretically and empirically.
- Discuss the consequences of (T, C) leakage explicitly in the threat model.
- Test a stronger distinguisher than a 2-layer MLP / ResNet-18 (e.g., higher-order moment tests, or a classifier given many fixed-user samples).

## Removed Points
These points are flagged to be removed, treat them with caution:

- **(Harsh critic) "Theorem 3.1 is false under default settings."** Removed: verified false. The argument relies on viewing z^(1)_{i,j} ⊕ z^(1)_{i',j'} = m_j ⊕ m_{j'} as a violation of pairwise independence, but m_j ⊕ m_{j'} is itself a uniform Bernoulli — the pair is uniform on {0,1}^2. More generally, for any k ≤ 3 outputs, every non-trivial F_2-linear combination touches at least one m_j an odd number of times (because the total count of message-bit usages is k, which is odd when k=3 and the involved j-indices cannot all cancel), giving a uniform Bernoulli. Hence 2-wise and 3-wise independence both hold at any s ≥ 1, including the default s=1.
- **(Harsh critic) "Ablation on s contradicts the theory."** Removed: the critique was conditional on the (incorrect) claim that the theorem fails at small s. Since 3-wise independence holds at all s, the ablation pattern ("larger s improves indistinguishability beyond degree 3, at cost of error propagation") is internally consistent.
- **(Harsh critic) "FID metric distinguishes little."** Removed: noting that FID is uninformative among lossless methods is a fair caveat but not a real weakness — the paper reports it as a sanity check, not as the main evidence for undetectability.
- **(Strength finder) "Targets an important problem."** Removed: generic and not paper-specific.

## Novel Insights
None beyond the paper's own contributions. The polar-decomposition / 3-design framing is itself the paper's main intellectual contribution; the reviews surface its limitations (3 moments vs. cryptographic indistinguishability) but no new insight beyond what is implicit in the paper.

## Suggestions
- Replace the negligible-advantage formalism in §3.1 with a quantitative statement: e.g., "no degree-≤3 polynomial test can distinguish z_w from N(0, I)" and bound the higher-degree leakage.
- Rewrite the comparison to Gaussian Shading as a storage/compute trade-off rather than a losslessness gap, and include per-image-keyed Gaussian Shading as a baseline in Figure 2 and Table 1.
- Explicitly state that (T, C) is a long-term cryptographic key in the threat model section, and add a short discussion of leakage consequences.
- Fix Lemma 3.3's statement (use √l_x scaling) and either prove a tighter version of Lemma 3.4 for spherical 3-designs or be explicit that z_w is approximately, not exactly, Gaussian.
- Add a per-user undetectability experiment (fix m_u, vary r, give the classifier many samples).

## Axis Assessment
- **Originality**: Good. The 3-design construction via XOR mixing + sphere projection + chi-scaling is a fresh combination not seen in prior diffusion watermarking work.
- **Importance of question**: Moderate–high. Lossless diffusion watermarking is an active and meaningful sub-area.
- **Claims supported by evidence**: Mixed. Empirical claims (speed, robustness, classifier-resistance) are well-supported; the theoretical claim is over-stated (Eq. 2 vs. what Theorems actually prove).
- **Soundness of experiments**: Mostly solid, but the indistinguishability comparison against Gaussian Shading is handicapped, and undetectability is not tested per-user.
- **Clarity of writing**: Good — Figure 1 is informative, the modular three-stage decomposition is clean.
- **Value to community**: A useful engineering contribution (fast extraction, no per-image keys, good robustness), with a moderately novel theoretical lens, but the framing as cryptographically lossless will mislead some readers.

## Anchors retrieved (all rounds)
- Round 1, low band: vK8C37eHXM.md (3.20 reject; weakly related); W4djmqKZC6.md (3.00 reject); fkNsgI1nye.md (3.00 reject); rAZ3yCpc3K.md (3.00 reject) — all weaker than this paper.
- Round 1, mid band: T0ebbDO60R.md (SuperMark, 3.75 reject; weaker contribution depth); ll2nz6qwRG.md (Hidden in the Noise, 5.83 accept; comparable distortion-free initial-noise watermarking — read in full); HexshmBu0P.md (Recipe, 5.33 reject; different scope); 1IwoEFyErz.md (Shallow Diffuse, 6.00 reject; theoretically richer but rejected — read); ETFfXGM3e4.md (SAT-LDM, 5.50 reject; training-based — read).
- Round 1, high band: j7b4mm7Ec9.md (7.60 reject); CxXGvKRDnL.md (8.00 accept, compression); 84n3UwkH7b.md (8.00 accept, memorization); gU58d5QeGv.md (8.00 accept, T2I architecture) — clearly stronger than this paper.
- Round 2: ll2nz6qwRG.md (re-surfaced); HexshmBu0P.md (re-surfaced); ETFfXGM3e4.md (re-surfaced); uHdf9F1tY4.md (DiffusionShield, 5.50 reject); jlhBFm7T2J.md (undetectable watermark / PRC, 6.50 accept — read; this paper's own baseline, but with a genuine cryptographic guarantee that Spherical Watermark only approximates); LdIlnsePNt.md (SEAL text watermark, 6.00 reject); UchRjcf4z7.md (transfer attack, 6.50 accept); zqo2eKjSWH.md (Stable Signature attack, 4.50 reject); 9XEBFywIW7.md (Spread them Apart, 4.40 reject).

## Final positioning
Spherical Watermark is comparable to Hidden in the Noise (5.83 accept) in contribution depth — both are distortion-free initial-noise watermarking schemes — but the theoretical framing over-claims relative to PRC Watermark (6.50 accept) which actually meets the cryptographic definition. Empirical gains over PRC (speed, adversarial robustness) are real, but the Gaussian Shading comparison is handicapped. Better than rejected anchors at 5.33–5.50 (SAT-LDM, Recipe) due to a cleaner novel construction, but pulled down by the framing/comparison issues. Lands close to Shallow Diffuse (6.00 reject) and slightly below Hidden in the Noise (5.83 accept).

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>