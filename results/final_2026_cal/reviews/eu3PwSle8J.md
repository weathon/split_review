Now I have enough information to synthesize the final review. Let me write it.

**Round 1 Bracket:** The paper clearly sits above weak/withdrawn papers (scores 2.0–3.2) and well below the 8+ papers (which are on completely different topics). This places it in the 4–7 range.

**Round 2 Narrowing:** Compared to directly relevant anchors — ASIDE (4.67), Sysformer (5.00), Intent-FT (5.00) — the AIR paper has more thorough evaluation (3 model sizes × 2 training methods × multiple attacks), cleaner results, and consistent performance. Compared to SEAM (6.50), the AIR paper lacks a comparable theoretical contribution but has comparably thorough empirical work. Final score: **6.0**.

---

## Summary

This paper proposes Augmented Intermediate Representations (AIR), a method for injecting instruction hierarchy (IH) signals into *every* decoder layer of an LLM, rather than only at the input layer as prior work does. The core idea is to add small, learnable privilege-level embeddings to the intermediate token representations at each layer. Across three base models (3B–8B), two training paradigms (SFT and DPO), and multiple attack types, AIR reduces attack success rate (ASR) on gradient-based prompt injection attacks by ~1.6× to 9.2× compared to the best prior IH mechanism (Delim or ISE), while maintaining utility and adding only ~0.4M parameters (0.005% increase).

## Strengths

- **Consistent and large ASR reductions across diverse settings.** Table 1 shows AIR outperforms Delim and ISE on essentially every model × training × attack combination. Examples: Llama-3.2-3B SFT GCG ASR drops from 38.0% (Delim) to 4.1% (AIR); Qwen-2.5-7B DPO GCG drops from 7.7% (ISE) to 1.6% (AIR). The 1.6×–9.2× reduction range in the abstract is concretely supported by the table.

- **Principled motivation and clean method.** The paper identifies a genuine limitation of input-only IH signals (degradation across layers), supports it with a cosine-similarity analysis (Figure 3), and proposes a straightforward fix: layer-specific learnable privilege embeddings. The analogy to RoPE (positional info in all layers vs. only the input) is apt and grounds the design in a known successful precedent.

- **Minimal overhead.** Section 4 computes that for Llama-3.1-8B, AIR adds only 0.4M parameters (0.005% increase). The inference cost is negligible. This makes the method practical for deployment.

- **Thorough evaluation.** The paper spans three model sizes (3B, 7B, 8B), two training methods (SFT, DPO), static and gradient-based attacks (Naive, Ignore, Completion, Escape Sep., GCG with momentum, Astra), and the SEP separation benchmark. Utility is measured on AlpacaEval 2.0. The evaluation is more comprehensive than most prior work in this area.

- **Good utility preservation.** Figure 6 shows that AIR models suffer at most ~2% degradation in AlpacaEval win rate compared to a non-adversarially trained baseline, and often match or exceed it.

## Weaknesses

### Major
None.

### Minor

- **ASR numbers reported without variance.** The ASR results in Table 1 are point estimates from what appears to be a single run. Gradient-based attacks like GCG are stochastic (initial token choice, optimization path), and the paper would be strengthened by reporting mean/variance over multiple seeds. Figure 7 does provide loss curves with standard-deviation shading, which helps, but the headline ASR numbers lack this companion information. Given the large improvements, the trends are likely robust, but without variance the reader cannot fully assess reliability.

- **Cosine similarity analysis (Figure 3) is on a model not trained for IH.** The analysis uses the base pre-trained Llama-3.2-3B model, where the Delim tokens and ISE/AIR embeddings have not been trained. The resulting similarity trajectories may partly reflect the model treating unknown tokens naively rather than demonstrating fundamental degradation of learned IH signals through layers. This does **not** affect the paper's main empirical results (which are on trained models), and the paper frames it as a hypothesis ("We hypothesize that this limits the effectiveness…"), but the motivating argument would be cleaner if this limitation were acknowledged or if the analysis were repeated on instruction-tuned models.

- **No evaluation against adaptive attacks targeting AIR's multi-layer mechanism.** The paper evaluates against strong white-box attacks (GCG with momentum, Astra), but these are not specifically designed to counteract per-layer IH embeddings. An adversary with white-box access could potentially craft an attack that explicitly cancels or overrides the added IH vectors (e.g., optimizing a prefix that forces hidden states toward a common representation regardless of privilege level). This is a limitation shared with much of the literature, and the paper does not claim otherwise, but it is worth noting.

### Trivial
- The reported range "1.6× to 9.2× reduction" for GCG is very slightly optimistic: one data point (Llama-3.1-8B DPO GCG: AIR 2.8% vs. ISE 4.0%) yields a 1.43× reduction, just below 1.6×. This does not change the overall picture but the bound is slightly off.

## Nice-to-Haves

- An adaptive attack (e.g., augmenting the GCG objective with a term that penalizes differences between hidden states of different privilege levels) would further strengthen the robustness claim.
- Reporting ASR over 3–5 random seeds with standard deviation would address the most common concern about stochastic optimization attacks.

## Removed Points

- **"Training datasets and procedures are relegated to the appendix"** (Harsh Critic, Missing Parts): The appendix is stripped by the parser. The original submission contains these details. REMOVED per hard rules.
- **"SEP utility score limitation (witness might appear coincidentally)"**: This is a limitation of the benchmark, not the paper's method. The paper uses SEP as proposed by Zverev et al. REMOVED as a weakness against the paper.
- **"Limited discussion of potential overfitting to specific attack setup"**: Speculative; the paper uses standard attack configurations. REMOVED.
- **"Missing related works"** and **"formatting nitpicks"**: REMOVED per hard rules.
- **Strength from Strength Finder about "empirical validation of IH signal degradation hypothesis"**: Kept but noted as a minor concern — the analysis is on an untrained model, which weakens the strength but doesn't eliminate it entirely.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions

1. Add variance reporting (mean ± std over multiple seeds) for the ASR numbers in Table 1, especially for GCG and Astra.
2. Clarify in Section 3 / Figure 3 caption that the cosine similarity analysis is performed on the base pre-trained model (not yet trained for IH), and briefly discuss whether the trends are expected to hold post-training.
3. Add a limitations paragraph discussing adaptive attacks as a direction for future work.
4. Correct the claim about the lower bound of the reduction factor (1.43× vs. 1.6× for one cell).

## Score and Decision

Calibration anchors used:

| Anchor ID | Avg Score | Round | Comparison to this paper |
|---|---|---|---|
| dOS3e1kC5u | 2.50 | R1 | Much weaker; rejected/withdrawn paper on soft-prompt extraction |
| PKrYc2nyO4 | 3.20 | R1 | Weaker; withdrawn paper on self-activating internal defense |
| bIJkCBVSgd | 3.00 | R1 | Weaker; rejected paper on distractor injection |
| gMajoi2xsq | 4.67 | R1 | Related topic (instruction hierarchy toolkit); this paper has more methodological novelty and cleaner evaluation |
| 44xt30V679 | 5.00 | R1 | Related (jailbreak defense); this paper is more thorough empirically |
| C81TnwHiRM | 4.67 | R2 | Most directly comparable (prompt injection via embedding separation); AIR has lower ASR and more thorough evaluation |
| EbgCEd8gyN | 5.00 | R2 | Adaptive system prompts for safety; AIR has more principled approach and cleaner results |
| ERNpUGr8M5 | 6.50 | R2 | Self-destructive defense; stronger theoretical contribution but similar empirical thoroughness; AIR slightly below this level |
| BLOIB8CwBI | 6.50 | R2 | Different topic (world model verification); not directly comparable |

Round 1 bracket: 4–7.  
Round 2 narrowing: compared to ASIDE (4.67) and Sysformer (5.00), this paper is stronger; compared to SEAM (6.50), it has less theoretical depth but comparable empirical breadth. Final score: **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>