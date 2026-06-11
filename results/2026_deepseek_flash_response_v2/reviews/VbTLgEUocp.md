Now let me compile the final review.

## Summary
This paper presents Calgacus, a protocol that uses an LLM to encode a secret text within a different, coherent cover text of the *same token length* by recording the token ranks of the secret message and using those ranks to select tokens during generation from a different prompt. The paper also discusses implications for AI safety, the nature of LLM knowledge, and reconceptualizes hallucination as absence of intention rather than factual inaccuracy.

## Strengths

1. **Full-capacity (same-length) encoding is a genuine differentiator.** The protocol achieves stegotext and secret message of equal length, a property explicitly contrasted with prior LLM-based steganography (Ziegler et al., 2019; Kaptchuk et al., 2021; Wu et al., 2024; Zamir, 2024). This prevents length-based detection and is a clean, novel idea.

2. **Quantitative evidence that stegotexts fall within the real-text distribution.** Figure 4 shows that for three source texts selected at μ, μ−2σ, and μ+2σ of a 1000-text Reddit distribution, 100 stegotexts each fall within the log-probability distribution of real texts, while random ASCII/English-word baselines do not.

3. **Clear mechanistic explanation of the probability gap.** The "Low entropy token choices" analysis (lines 134–146) explains *why* stegotexts are less probable than originals despite preserving ranks: rank-1 tokens occur at ~40% frequency in real text but many are "wasted" in low-entropy contexts where the model would predict with >95% probability.

4. **Honest treatment of limitations.** The paper acknowledges the hash counterexample, the detectability result, the dependence of quality on the choice of e and k, and the requirement that sender and receiver run identical LLM configurations.

5. **Cross-model validation.** The same probability shift is observable with Phi-3 3.8B (Figure 14), suggesting the phenomenon is not a single-model artifact.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation is too thin to support the scope of claims.** The quantitative evaluation rests on exactly 3 source texts, each truncated to 85 tokens, encoded using one model (Llama 3 8B), and evaluated only by LLM log-probability as a proxy for textual plausibility. There is no human evaluation of stegotext quality. While the paper acknowledges log-probability is only a proxy ("Measuring the meaningfulness of a text is a longstanding linguistic challenge," line 124), it nonetheless makes broad claims about "high-quality results" (abstract) and applicability to diverse scenarios (hiding critiques in praise, manuscripts in reviews, censored-platform communication) without testing any of these systematically. The same-length property is novel, but whether the method reliably produces texts that humans would judge as coherent, plausible, and on-topic is not established.

2. **No quantitative comparison against any other steganography method.** The paper surveys Ziegler et al. (2019), Kaptchuk et al. (2021), Wu et al. (2024), and Zamir (2024) in Related Work, but never compares against them—not on plausibility, detectability, capacity, or computational cost. While the paper states that its "main interest is to discuss the implications" (line 67) rather than to compete with prior methods, the reader cannot assess whether the same-length property comes at a meaningful cost (e.g., lower plausibility, higher detectability) or whether existing methods could achieve similar results with different trade-offs.

3. **Concrete AI safety scenario is proposed but not demonstrated.** The gas-meter tampering application (company covertly deploying an unfiltered LLM) is presented as a threat scenario, but the paper says it is shown in figures that reside in the appendix (Figures 11, 12). No working end-to-end result is demonstrated in the main text.

### Minor

1. **Detectability limits practical steganographic utility.** The paper shows that LLMs can generally distinguish stegotexts from originals by picking the more probable one. While the paper is transparent about this and discusses deniability, the framing ("LLMs CAN hide text in other text") underplays the fact that the method is detectable in principle—an adversary with access to an LLM could exploit the probability gap.

2. **Security analysis is preliminary.** The brute-force bound O(d^|k|) (line 154) assumes the attacker knows nothing about k, but the paper acknowledges k is expected to be a "sound instruction in natural language," making the effective search space much smaller. The suggestion that inserting a random string into k "nips [this attack] in the bud" (line 164) is stated without demonstration.

3. **Discussion is loosely tethered to the method.** The reconceptualization of hallucination as "lack of intention" and the analysis of LLM knowledge are philosophically interesting but could largely stand independently of the Calgacus protocol. The paper would benefit from making more explicit how the method *specifically* motivates these conclusions beyond being a vivid illustration.

### Trivial
None.

## Nice-to-Haves
- Human evaluation of stegotext plausibility (e.g., crowdsourced study comparing real texts vs. stegotexts)
- Evaluation on longer texts (200+ tokens) to test whether the method degrades with length
- Scaling experiments across model sizes (1B, 3B, 8B, 70B) to substantiate the "modest models" claim
- Systematic comparison against at least one prior steganography method on a shared metric

## Removed Points
- *"Gas meter application not demonstrated"*: The paper states a real example is shown in Figures 11 and 12. The appendix is stripped by the parser; no conclusion about absence can be drawn.
- *"No confidence intervals / statistical significance"*: 100 samples per text provide reasonable coverage; this is nitpicking.
- *"Reproducibility details not specified"*: The paper acknowledges identical conditions are required (line 148) and describes the approach. Exact checkpoint/decoding details are implementation-level nitpicks.
- *Generic "evaluation lacks rigor" / "baselines may not be fair" type criticisms*: These were area-of-concern sweeps without specific concrete anchors to the paper.
- *"Missing related works"*: Not verifiable without external sources.
- *"Only 3 source texts" re-framed as fatal*: Legitimate weakness but not fatal—the method is clearly described and the three-point probe is a sensible minimal evaluation.
- *Strength Finder points about "important problem"*: These are generic and not specific to this paper's contribution.

## Novel Insights
The harsh critic's observation that the paper has "the structure and ambition of a full research contribution but the evaluation of a short workshop paper" captures the central tension. The strength finder's identification of the "low entropy token choices" analysis as a principled explanation for the probability gap is the review's most specific technical insight—it goes beyond reporting results to explain *why* the method behaves as it does. The merged review surfaces the fact that the paper's discussion ambitions (redefining hallucination, questioning LLM knowledge) are loosely coupled to the protocol itself, which is a useful structural observation the individual reviews did not fully articulate.

## Suggestions
1. **Expand the evaluation substantially**: Add human ratings of stegotext plausibility, test on more texts (30+), longer texts (200+ tokens), and multiple model sizes. This is the single highest-leverage improvement.
2. **Compare against at least one prior method** (e.g., Ziegler et al., 2019, or Meteor/Kaptchuk et al., 2021) on a shared plausibility metric to let readers assess the trade-offs of the same-length property.
3. **Either demonstrate the gas-meter scenario end-to-end or clearly label it as a proposed application** rather than a demonstrated one.
4. **Strengthen the security analysis**: address the reduced search space from natural-language keys, and provide evidence for the random-string mitigation.
5. **Tighten the connection between method and discussion**: show how the Calgacus protocol specifically constrains the philosophical conclusions, or consider separating the discussion into a shorter, more method-grounded section and a broader essay.

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Searched for papers on "LLM steganography hiding text in text" across three score bands.

| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| jbfDg4DgAk.md (Sparse Watermarking) | 3.00 | R1 | Lower band. Similar topic (LLM watermarking) but thin evaluation and missing baselines. Calgacus is stronger. |
| urQi0TgXFY.md (Hidden in Plain Text) | 5.00 | R1 | Middle band. Steganographic collusion with RL training, more thorough experiments. Calgacus has weaker evaluation but cleaner method. |
| 7suavRDxe8.md (Plausibly Deniable Encryption) | 4.80 | R1 | Middle band. Very related: uses LLMs for deniable encryption. Similar weaknesses (security model informality). Calgacus is comparable. |
| 6p8lpe4MNf.md (Semantic Invariant Robust Watermark) | 5.50 | R1 | Accepted. More thorough evaluation with theoretical results. Calgacus is below this. |
| 0koPj0cJV6.md (Black-Box Watermark) | 4.60 | R1 | More experiments but presentation issues. Calgacus is comparable or slightly below. |
| Bo62NeU6VF.md (Backtracking Safety) | 8.00 | R1 | Strong accept. Far above Calgacus in rigor and evaluation. |

**Round 1 bracket:** [3.5, 5.5]

**Round 2 (Narrowing):** Searched for LLM steganography papers with thin evaluation.

| Path | Score | Round | Comparison |
|------|-------|-------|------------|
| IQafqgqDzF.md (OD-Stega) | 3.50 | R2 | Very relevant: LLM steganography with weak evaluation and missing baselines. Calgacus has cleaner idea and better writing. **Calgacus is stronger.** |
| kRJNV8RCE3.md (Hiding Images in Diffusion Models) | 4.75 | R2 | Different domain but similar "hiding" framing. Rejected despite more experiments. Calgacus is comparable. |
| ecbRyZZmKG.md (Double-I Watermark) | 5.25 | R2 | Rejected. Watermarking for LLM copyright. More thorough evaluation. Calgacus is below. |

**Final bracket:** [3.5, 4.5]. Calgacus is clearly above OD-Stega (3.50) due to the cleaner idea, better writing, and honest treatment of limitations. It is below Hidden in Plain Text (5.00) and Plausibly Deniable Encryption (4.80) in evaluation thoroughness. The paper's primary weakness is the thin evaluation, which limits the credibility of its broader claims. The core idea is genuinely interesting and the writing is excellent, but the evidential basis is insufficient for a top conference venue.

**Score: 4.0** — The paper has a novel and well-described method with an engaging discussion, but the evaluation is too thin (3 texts, 85 tokens, 1 model, no human eval, no baseline comparison) to support the scope of claims. The core idea is promising and merits expansion.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>