## Summary

FeedSign proposes a federated fine-tuning method that reduces per-step communication to exactly 1 bit per client (uplink) regardless of model size. The key idea combines zeroth-order (ZO) optimization with shared pseudo-random number generators (PRNGs): the parameter server broadcasts a perturbation direction via seed, each client computes a binary vote indicating whether that direction reduces its local loss, and the server aggregates votes (e.g., majority) to determine the update. The paper provides theoretical convergence analysis (O(e⁻ᵗ) rate), experiments across models from 11M to 13B parameters (language + vision), and discusses byproducts including orbit-based model storage and differential privacy.

## Strengths

- **Genuinely novel communication architecture:** Reducing federated fine-tuning uplink to a single sign bit per step is a clever and well-motivated idea. The mechanism — combining ZO estimation, shared PRNG, and binary voting on random directions — is a clean, minimal design that pushes the seed-projection paradigm (FwdLLM, FedKSeed) to its logical extreme. Scaling to OPT-13B, the per-step uplink drops from 24 GB (full-model FO) to 1 bit, an improvement of roughly eleven orders of magnitude (Section 1, lines 24–25).

- **Empirical validation across a wide range of model scales and modalities:** Experiments span from 11M (ResNet-18) to 13B (OPT-13B) parameters, covering both vision (CIFAR-10/100, ViT-large) and language tasks (RoBERTa-large few-shot, OPT fine-tuning). On OPT-13B across 11 tasks, the mean gap to first-order methods is −6.0% (Section 4.1, line 51), demonstrating that extreme compression does not catastrophically degrade performance. The method is also tested under data heterogeneity (Section 4.2) and Byzantine attacks (Section 4.3), showing robustness advantages over ZO-FedSGD.

- **Orbit-based model storage and parameter security are interesting byproducts:** The observation that a 13B-parameter fine-tuning trajectory can be stored as seed-sign pairs (Section 5.1) is a genuine systems-level insight. The idea that the parameter server never holds model parameters (Section 5.2) has practical security implications beyond what standard FL offers.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Downlink communication claim is overstated.** The abstract (line 4) and conclusion (line 275) claim the client "downloads the global model of any size using exactly 1 bit per step." However, the method requires clients to know the random perturbation direction each step. If the parameter server broadcasts a new seed each step, this seed (at minimum 32–64 bits) constitutes downlink communication. The contribution list (line 20) more honestly states "per-step uplink communication overhead of 1 bit." The abstract's symmetric framing conflates uplink and downlink; the headline "1 bit per step" should be qualified to reflect the seed broadcast cost.

- **Convergence rate claim O(e⁻ᵗ) lacks necessary caveats.** The abstract (line 4) and contributions (line 22) assert convergence at "an exponential rate O(e⁻ᵗ), the same rate as in first-order (FO) methods can attain." FO methods achieve exponential (linear) convergence only under strong convexity or the Polyak-Łojasiewicz condition — assumptions that do not generally hold for large neural network fine-tuning. By not stating these assumptions alongside the claim, the paper implies a guarantee that is not standard in non-convex FL optimization. The claim should be qualified with the specific conditions under which it holds.

- **Byzantine robustness comparison is asymmetric and the inherent-advantage conclusion is overclaimed.** In Section 4.3 (lines 209–213), the Byzantine client in ZO-FedSGD "always transmits a random number" (unbounded, can arbitrarily corrupt any real-valued aggregate), whereas in FeedSign it "always transmits a reversed sign" (a bounded flip on a 1-bit signal). These are attacks of fundamentally different strength: an unbounded value vs. a single bit flip. With 4 honest and 1 Byzantine client, majority voting naturally tolerates a single flipped bit. The paper claims FeedSign has an "inherent advantage" (line 211), but the experiment does not calibrate attacks to be comparably strong. A fairer test would evaluate stronger coordinated attacks on FeedSign (e.g., sign-flipping in the gradient-aligned direction across steps). The asymmetric setup undermines the claimed generality of the robustness result.

- **"No obvious performance gap" language minimizes a real degradation.** Line 49 states FeedSign "manifests no obvious performance gap to MeZO," but lines 51–52 report a −5.5% to −6.0% mean gap to first-order methods on standard benchmarks. A 5–6% absolute gap is meaningful and should be characterized honestly rather than minimized. The paper would benefit from explicitly stating what constitutes an "obvious" or "acceptable" gap in its target deployment scenarios.

- **The orbit storage arithmetic is inconsistent.** Section 5.1 (line 231) claims a 10,000-step fine-tuning orbit for OPT-13B occupies "less than 200 bytes." Ten thousand 1-bit signs alone occupy ~1.25 KB, even before accounting for the initial seed or any metadata. This arithmetic discrepancy should be resolved.

### Trivial

- Some sentences are garbled in the extracted text (e.g., line 67: "vithth del faster tha"), which appears to be a parser artifact rather than a paper flaw.

## Nice-to-Haves

- Reporting standard deviations or confidence intervals across multiple random seeds would strengthen the reliability of the empirical results, though the authors note the computational expense of large-model ZO training.
- A formal description of the seed-sharing mechanism (broadcast each step vs. deterministic derivation) would clarify the actual downlink communication cost and help resolve the ambiguity in the "1 bit per step" claim.
- Clarifying what assumptions (strong convexity, PL condition, Lipschitz smoothness, etc.) drive the exponential convergence rate in Theorem 1 would help readers evaluate the claim without needing to infer from the missing section.

## Removed Points

- **Missing method section / Theorem 1 as a fatal weakness:** The harsh critic argued the absence of Section 3 (containing Algorithm 1 and Theorem 1) makes the paper unevaluable. However, this is a parser-induced omission, not a flaw in the submission. Removed per the instruction that parser artifacts do not reflect on the paper.
- **1/64 communication ratio is inconsistent:** The critic claimed the 1/64 ratio is implausible because ZO-FedSGD sends a "projection vector." ZO-FedSGD (FwdLLM/FedKSeed) sends a scalar projection per step; 1 bit vs. a 64-bit float yields a 1/64 per-step ratio, which is consistent. Removed as factually incorrect about the baseline.
- **Hyperparameters not reported / missing implementation details:** The critic noted the absence of learning rates, batch sizes, and β values. These details may reside in the missing Section 3 or appendix (parser-removed). Removed per the instruction on parser-induced content gaps.
- **"Standard FO methods do not converge at O(e⁻ᵗ)" framed as a fatal flaw:** Without Theorem 1's assumptions, this is a speculative claim about what the theorem may or may not prove. Demoted to Minor (the framing criticism above) rather than treated as a fatal methodological error.
- **Strength about "no obvious performance gap" being a strength:** The Strength Finder claimed this as evidence that compression doesn't degrade accuracy. However, the actual −6% gap is meaningful, so characterizing it as "no obvious gap" is the paper's spin, not an objective strength. Moved here to avoid inconsistency with the weakness about this language.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Qualify the communication claim throughout: clearly separate uplink (1 bit) from downlink (seed broadcast), and report the total per-step bits sent/received in both directions.
2. State the convergence assumptions explicitly alongside the O(e⁻ᵗ) claim in the abstract and contributions — ideally with a brief statement of which function class (e.g., strongly convex, PL) the bound applies to.
3. Redesign the Byzantine experiment with comparable attack strength across methods, or at minimum acknowledge the asymmetry and explain why it is inherent rather than a design choice.
4. Replace "no obvious performance gap" with a quantitative assessment of the trade-off (e.g., "FeedSign achieves performance within X% of FO at a communication reduction of factor Y").
5. Correct the orbit storage arithmetic and report the actual computation.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>