Now I have enough context from calibration to write the final review. Let me compose it.

---

## Summary

This paper proposes IRIS (Intrinsic Reward Image Synthesis), a framework that improves autoregressive text-to-image (T2I) models using reinforcement learning with only an intrinsic reward — negative self-certainty (NSC), defined as the forward KL divergence between the uniform distribution and the model's output distribution. The central observation is that self-certainty behaves oppositely for text and image generation: maximizing self-certainty helps text reasoning (e.g., math, code) but minimizing it benefits T2I generation. IRIS achieves results competitive with external-reward baselines (T2I-R1) on GenEval, T2I-CompBench, and WISE, without any human-labeled data or domain-specific verifiers.

## Strengths

1. **Empirical evidence that self-certainty exhibits task-dependent behavior**: Figure 2 directly shows that during external-reward training, text self-certainty of Qwen2.5-1.5B increases (as expected from the LLM literature), while image self-certainty of Janus-Pro-1B *decreases*. This observation — that maximizing self-certainty helps language reasoning but harms image generation — is a genuinely novel, modality-dependent finding that motivates the entire framework.

2. **Systematic ablations that cleanly validate the core design choices**: Figures 6–9 form a tightly connected set of controlled experiments. Figure 6 shows that minimizing image self-certainty outperforms maximizing it; Figure 7 does the same for text tokens; Figure 8 shows that the forward-KL formulation (self-certainty) beats the backward-KL formulation (entropy); Figure 9 justifies the use of RL (GRPO) over direct gradient-based optimization of NSC, which causes model collapse. These ablations are the strongest part of the empirical contribution — each isolates one design decision and provides clear evidence for the paper's choices.

3. **Competitive results across multiple benchmarks without external supervision**: Table 1 reports that Janus-Pro-1B + IRIS achieves 0.72 (GenEval), 0.3793 (T2I-CompBench Complex), and 0.37 (WISE), compared to T2I-R1's 0.75, 0.3820, and 0.38. The gaps are small (1–4%), and IRIS matches or slightly exceeds T2I-R1 on specific subcategories such as Physics (0.45 vs. 0.43) and Colors in GenEval (0.88 vs. 0.86). This demonstrates that an intrinsic reward can approach the effectiveness of carefully engineered external reward ensembles, which is the paper's central claim.

## Weaknesses

### Fatal
None.

### Major

None. The paper's core claims are supported by the evidence, and no identified flaw invalidates the main contribution.

### Minor

1. **Overstated "superior" and "reasoning" claims in the abstract and introduction**: The abstract claims IRIS achieves performance "competitive with or superior to external rewards." On aggregate metrics, IRIS is consistently ~1–4% *below* T2I-R1 on both model sizes and all three benchmarks (Table 1). While IRIS does lead on some subcategories (e.g., Physics, Colors), the aggregate picture is "competitive" but not "superior," and the paper's own body text correctly acknowledges this. Similarly, the paper frames improvements as "enhancing reasoning capabilities of T2I models." The benchmarks (GenEval, T2I-CompBench, WISE) measure compositional generation, attribute binding, and world knowledge — these are better described as improved compositional and semantic generation. The "reasoning" framing borrows from the LLM chain-of-thought literature but the paper provides no reasoning-specific evaluation (e.g., CoT relevance, factual accuracy). These overclaims are minor because the body text is more measured and the core contribution (intrinsic reward for T2I) does not depend on them.

2. **Training data not explicitly specified**: The paper states that experiments "primarily follow the protocol in T2I-R1 (Jiang et al., 2025)" (Sec. 4.1), which is a citable source for training details. However, the paper does not state what the training prompt distribution is, its size, or confirm that the GenEval/T2I-CompBench/WISE evaluation prompts are disjoint from training prompts. Since "primarily follow" may involve differences from the original protocol, the missing specification undermines full reproducibility. This is a minor issue because the reference provides the protocol baseline, but the authors should explicitly confirm prompt disjointness and state the training prompt source.

3. **Only tested on one model family (Janus-Pro)**: The paper claims IRIS is "agnostic to the model architecture" (Sec. 3), which is a claim about generality, but all experiments use Janus-Pro (1B and 7B). The paper discusses this limitation in Sec. 4.4, noting that T2I models have diverse architectures. Testing on even one additional autoregressive T2I model would substantially strengthen the generalizability claim. This is minor because the paper acknowledges the limitation and the method's core mechanism (intrinsic reward based on model's own output distribution) is architecture-agnostic in principle.

4. **Qualitative-only evidence for semantic CoT improvements**: Figure 4 shows one qualitative example comparing generation with and without semantic CoTs. The paper calls this "emergence of long-form reasoning," but no quantitative measure of CoT quality is provided (e.g., relevance to prompt, inclusion fidelity, diversity). The harsh critic's concern that the CoT example adds details not in the original prompt ("A photo of a bicycle") is somewhat misplaced — CoTs are intended to elaborate — but the lack of quantitative CoT evaluation is a real gap.

5. **No quantification of the chat-template correction's effect**: The paper identifies a chat-template bug in the official T2I-R1 implementation and claims to use the correct template (Sec. 4.1). However, it does not report the magnitude of the difference this correction makes. Readers cannot tell whether the baseline numbers in this paper are higher or lower than the original Jiang et al. (2025) numbers. A small comparison table would resolve this.

### Trivial
- The definition of KL(U∥π) as "forward KL" is technically nonstandard; the paper's ablation (Fig. 8) provides the empirical justification, so this is a notation preference.
- The paper has an ethics statement but no dedicated "Limitations" section. The architecture limitation and training-data omission are discussed elsewhere but not gathered in one place.

## Nice-to-Haves
- A breakdown of how the chat-template correction affects the T2I-R1 baseline numbers.
- Quantitative evaluation of CoT quality (e.g., relevance scoring, attribute inclusion rate).
- A dedicated limitations paragraph collecting the scope caveats (single architecture, training data scope).

## Removed Points

These points are flagged to be removed — treat them with caution:

- *"The claim of 'superior' is not supported and the paper should remove the superiority claim"* — Retained as Minor Weakness #1 but scaled back. The abstract says "competitive with or superior to" and the body text qualifies this with subcategory analysis. It's an overstatement but not false on all readings.
- *"The self-certainty/self-uncertainty framing is confusing"* — The paper defines its terms clearly in Sec. 3.2. Removed as a misunderstanding.
- *"The approach is similar to entropy maximization"* — The paper explicitly compares forward KL with entropy (backward KL) in Fig. 8 and shows forward KL wins. This was addressed.
- *"Missing limitations section"* — Demoted to trivial, as Sec. 4.4 ("Further Discussions") acknowledges the architecture limitation.
- *"The theoretical motivation is thin for the KL definition"* — The paper cites prior work (Fang et al., 2024; Kang et al., 2025; Zhao et al., 2025b) for the self-certainty definition and provides the key empirical check (Fig. 8). This is a notation preference, not a weakness.
- *"The CoT example shows hallucination"* — The CoT adds contextually plausible details, consistent with the intended behavior of semantic CoTs (introduced by T2I-R1). Removed as a misinterpretation.
- *"Missing comparison to the original T2I-R1 numbers"* — Retained as Minor Weakness #5 but demoted from more severe framing.

## Novel Insights

The most interesting observation to emerge from the reviews is that the paper's strongest evidence is not in Table 1 but in the ablations (Figures 6–9). The marginal aggregate deficit of IRIS vs. T2I-R1 (1–4%) is less informative than the clean causal evidence that minimizing self-certainty is what drives improvement, while maximizing it causes rapid collapse. The contrast between Figures 2 (correlational observation) and 6 (causal intervention via ablation) forms a compelling empirical narrative that is more convincing than the benchmark numbers alone. A second insight: the paper inadvertently reveals that current external reward ensembles (HPSv2, DINO, GIT, ORM) are better at capturing aesthetic and spatial attributes than world-knowledge attributes (natural science in WISE), where the intrinsic reward actually matches or exceeds them. This suggests a complementary relationship between intrinsic and external rewards that the paper does not fully explore.

## Suggestions

1. Tone down the abstract and introduction claims: replace "superior to" with "competitive with" and "enhances reasoning capabilities" with "improves compositional and semantic generation" (or add a reasoning-specific evaluation to support the stronger framing).
2. Explicitly state the training prompt source, its size, and confirm that the three evaluation benchmarks are disjoint from the training prompts.
3. Add a small table quantifying the effect of the chat-template correction on the T2I-R1 baseline numbers.
4. Collect the architecture and data limitations into a single "Limitations" section.

## Score and Decision

**Calibration summary:**

**Round 1 (Bracketing):**
- Weak anchors (<3.5): Papers scoring 3.0–3.4 on T2I topics — much weaker papers (GAN-based methods, small-dataset T2I). IRIS is clearly above these.
- Middle anchors (3.5–7.5): Papers scoring 4.60–6.25 on autoregressive T2I and RL alignment topics. IRIS falls in this band.
- Strong anchors (>7.5): Papers scoring 8–10 — exceptional contributions with comprehensive evaluations. IRIS is not in this band.

**Initial bracket: 4.5–6.5**

**Round 2 (Narrowing):**
- Let8OMe20n (*Confidence-aware Reward Optimization*, avg 6.00, Accept) — Most directly comparable: both papers propose reward design improvements for T2I alignment. The Confidence-aware paper has a benchmark contribution plus a method; IRIS has stronger conceptual novelty (intrinsic reward vs. confidence calibration) but less evaluation breadth. IRIS's weaknesses (overclaiming, missing training data detail) are comparable in severity to what reviewers flagged for that paper.
- jQP5o1VAVc (*Fluid*, avg 5.75, Reject) — Scaling study of autoregressive T2I with continuous tokens. Stronger empirical results (SOTA FID) but limited conceptual novelty. IRIS has more novelty but weaker empirical results. Comparable overall quality.
- wryFCrWB0A (*DnD Transformer*, avg 6.20, Accept) — Architectural contribution with overclaiming issues ("spark of intelligence"). Mixed reviews ranging from 5 to 8. IRIS's overclaiming is less severe and the experimental design is cleaner.
- b9dBNNeDd3 (*SAR*, avg 4.60, Reject) — Unified framework for autoregressive image generation but suboptimal performance and critical reviews. IRIS is clearly stronger (cleaner ablations, novel observation, competitive results).
- sgAp2qG86e (*JetFormer*, avg 6.25, Accept) — Full-system architectural contribution. Stronger engineering contribution than IRIS but similar in having overclaiming issues and mixed reviewer scores.

IRIS sits between the 5.75 (Fluid, Reject) and 6.00 (Confidence-aware, Accept) anchors. It has a genuinely novel cross-modal observation (self-certainty's opposite behavior), a clean method, and well-designed ablations. However, it has minor overclaiming, an underspecified training setup, and limited architecture scope. The paper is stronger than the SAR paper (4.60), comparable to the Fluid paper (5.75), and slightly below the Confidence-aware paper (6.00) in terms of execution completeness.

**Final score: 5.5** — a solid borderline contribution with a novel core idea. The main issues are presentation overclaims and missing training data specification, both fixable.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>