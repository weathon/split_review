Now I have enough information to write the final consolidated review. Let me carefully construct it.

## Summary

This paper proves that decoder-only Transformer language models are almost surely injective: distinct prompts almost always yield distinct last-token representations. The proof uses a real-analyticity framework to show that collisions are confined to measure-zero parameter sets at initialization, and the paper argues (via a sketch of Theorem 2.3) that gradient-based training preserves this property. Building on this, the authors introduce SIFT, an algorithm that recovers the exact input prompt from per-position hidden states with provable linear-time guarantees and 100% empirical accuracy across tested models.

## Strengths

- **Elegant theoretical framework.** The use of real-analyticity and the analytic dichotomy (identically zero vs. measure-zero zero set) to analyze Transformer injectivity is mathematically creative and conceptually illuminating. The framing cleanly explains why collisions require deliberate non-analytic choices (tied embeddings, quantization, non-smooth activations).

- **Large-scale empirical collision search with zero collisions found.** The paper performs ~5 billion pairwise comparisons across six model families (GPT-2, Gemma-3, Llama-3.1-8B, Mistral-7B, Phi-4, TinyStories) and reports minimum distances far above the collision threshold (e.g., 0.620 for Llama-3.1-8B, 1.274 for Mistral-7B at the final layer in FP32). This provides strong correlational evidence supporting the injectivity claim.

- **SIFT is a clean, operational algorithm with strong results.** Theorem 3.1 guarantees recovery in at most \(T|\mathcal{V}|\) steps. In practice, SIFT achieves 100% accuracy while exploring less than 0.22% of the vocabulary on average and running in 28 seconds for 20-token prompts, versus 3890 seconds for brute force. The robustness guarantee (Theorem 3.2) with noise bounds is a nice addition.

- **Robustness validation across quantization and large-scale models.** Experiments with FP4 and INT8 quantization show that quantization preserves separation (often more than doubling minimum distances), and the results extend to models up to 70B parameters. This demonstrates the phenomenon is not an artifact of high precision or small scale.

- **Formal noise robustness guarantee.** Theorem 3.2 provides a precise noise bound (half the minimum separation distance) under which exact recovery remains provably guaranteed, and this is empirically validated with FP4 quantization noise.

## Weaknesses

### Major

- **The proof sketch of Theorem 2.3 (training preserves injectivity) is too compressed for the paper's strongest claim.** The argument that the GD update map \(\phi(\theta) = \theta - \eta\nabla\mathcal{L}(\theta)\) preserves absolute continuity relies on: (i) \(\det D\phi\) being real-analytic and not identically zero, (ii) the Inverse Function Theorem giving local invertibility away from the measure-zero singular set, and (iii) therefore pushforward of an absolutely continuous measure staying absolutely continuous. Step (iii) is asserted without justification of the technical machinery (area formula, Luzin N property). The critic's specific counterexample (\(\phi(x)=x^3-x\)) does *not* invalidate the claim — pushforward of an absolutely continuous measure under a smooth map with non-singular Jacobian a.e. is indeed absolutely continuous — but the paper's sketch does not make this clear. Furthermore, step (i) (non-identically-zero Jacobian determinant) is hand-waved as "one can check this by evaluating at a simple parameter setting" without demonstration, even in the sketch. Since the persistence-under-training claim is what distinguishes this work from prior results (Sutter et al., 2025, who proved injectivity only at initialization), this compression is a significant weakness. The full appendix may address this, but the main text does not give reviewers enough to assess the claim's validity.

- **The HARDPROMPTS baseline comparison in Table 5 is misaligned and adds little.** HARDPROMPTS is designed for *prompt optimization* (finding a discrete prompt that optimizes a downstream objective), not for exact prompt recovery from hidden states. Its 0% accuracy is expected and uninformative. The paper itself acknowledges that "these differences make them complementary but not directly comparable" (line 309–310), yet still features HARDPROMPTS in the main accuracy table as evidence of SIFT's efficiency. This does not invalidate SIFT's performance, but it weakens the experimental narrative. The BRUTEFORCE ablation already provides a meaningful efficiency baseline; HARDPROMPTS should be moved to the appendix or explicitly discussed as solving a different problem rather than presented as a comparative baseline.

### Minor

- **SIFT requires per-position hidden states, limiting practical applicability.** The theoretical injectivity result is about the *last-token* state, but SIFT requires the full sequence of hidden states at some layer to operate efficiently. The paper is transparent about this ("designing an efficient algorithm for that setting is nontrivial and left to future work," line 157–158). Nevertheless, the ambitious title ("Language Models are Injective and Hence Invertible") implies general practical invertibility, which is not yet demonstrated for the setting proven injective (last-token state only). A small-scale proof-of-concept experiment on last-token inversion (even with high computational cost or on short prompts) would substantially strengthen the paper.

- **The gradient-guided POLICY is referenced to appendices (Alg. 2 and 3) but not described in the main text.** The paper mentions "random order or gradient-guided search" qualitatively but does not specify the actual policy used in experiments. While the code release mitigates this, the main text should state the policy, especially since the algorithm's practical efficiency depends entirely on this heuristic.

- **The collision search (100k prompts) is finite relative to the combinatorial space of possible sequences.** While the paper correctly notes that the theoretical proof is the primary evidence, the claim that results "stabilize, making collisions unlikely at any sequence length" (line 299) slightly overstates what a finite-sample experiment can show. This is a minor presentational issue.

### Trivial

- The paper refers to the algorithm as both SIFT and SiPT/SIpIT with inconsistent capitalization across the text.

## Nice-to-Haves

- **Inversion from only the last-token state.** Even a proof-of-concept on short prompts with small vocabularies would substantially strengthen the connection between the theoretical injectivity result and practical invertibility, and better justify the title.

- **Analysis of why the gradient heuristic works.** The paper reports exploring ~0.2% of the vocabulary but does not analyze why gradient-guided search is effective. Is it because gradient magnitude correlates with token identity? Would a simpler heuristic (e.g., sorting by embedding similarity) achieve comparable results? Understanding this would deepen the contribution.

- **Reporting the number of candidates tested for BRUTEFORCE vs. SIFT.** The runtime comparison in Table 5 would be more informative if it reported the number of candidates evaluated, which directly validates the efficiency gain.

## Removed Points

- *Criticism that the Inverse Function Theorem argument cannot guarantee absolute continuity preservation.* The critic's specific objection (using φ(x)=x³−x as a counterexample) is factually incorrect: the pushforward of an absolutely continuous measure under a smooth map with non-singular Jacobian a.e. is indeed absolutely continuous, a standard result in geometric measure theory. The concern about proof rigor is retained in the Major weakness above, but re-framed as a compression issue rather than a logical gap.

- *Criticism about missing confidence intervals in Tables 1–3.* These tables report minimum distances from deterministic forward passes on fixed models; sampling variability is not applicable.

- *Criticism that the full proof in the appendix "cannot be fully assessed."* This reflects the reviewer's access limitations, not a flaw in the paper.

- *Requests to test deliberately engineered non-analytic collisions.* This would be a verification of a known failure case, not a novel contribution.

- *Strength about "clear connection to real-world privacy and regulatory implications."* This is a downstream implication, not a core scientific contribution of the paper.

## Novel Insights

The most interesting observation emerging from the reviews is that the paper essentially proves a *structural* property of Transformers that runs counter to widespread intuition. Many practitioners assume Transformer representations are lossy because components like LayerNorm, softmax attention, and residual connections are individually non-injective. This paper shows that when you compose these components into a full decoder-only architecture and view the map from *discrete sequences* to *continuous representations*, the overall function becomes injective almost surely. The insight that real-analyticity of the architecture forces collisions to be measure-zero exceptions is both mathematically elegant and practically meaningful — it means that failures to decode information from hidden states reflect algorithmic or computational limitations, not information-theoretic ones. This reframing has direct implications for interpretability, auditing, and privacy.

## Suggestions

1. **Strengthen the Theorem 2.3 presentation.** Add a brief justification in the main text about why the GD pushforward preserves absolute continuity — specifically citing the area formula or Luzin N property for C^1 maps. Also, provide at least an illustrative construction showing that \(\det D\phi\) is not identically zero (e.g., by evaluating at a parameter setting where the Hessian is diagonal or zero).

2. **Reconsider the HARDPROMPTS comparison.** Either move it to an appendix or explicitly label it as solving a different problem with a clear disclaimer that 0% accuracy is expected. The BRUTEFORCE ablation already serves as an adequate efficiency baseline.

3. **Describe the gradient-guided policy in the main text.** Even a brief description (e.g., "tokens are scored by the gradient norm of the reconstruction loss with respect to the token embedding") would make the algorithm self-contained without requiring readers to consult the appendix.

4. **Add a discussion (or small experiment) on last-token-only inversion.** Even if efficient inversion is left to future work, a discussion of why it is hard and what the bottleneck is would help calibrate reader expectations and better align the title with the results.

## Score and Decision

**Calibration anchors used (all from human_reviews_2026):**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `qOyF214xmg.md` (Transducing LMs) | 8.00 | Stronger theoretical rigor and clearer proofs; our paper has broader experiments but less airtight theory. |
| `TLSUIyBIfs.md` (Quantitative Bounds for Length Generalization) | 7.00 | Stronger quantitative theoretical results; our paper has a more surprising claim but sketchier proof presentation. |
| `CfFj68C9Cn.md` (Learning to Recall with Transformers) | 6.50 | Comparable theory+experiment balance; our paper covers more models and has more practical implications. |
| `MFDkLbcydi.md` (Taming Imperfect Process Verifiers) | 6.50 | Strong theory, limited experiments; our paper has broader experiments but less rigorous theory. |
| `SHidElLSVt.md` (Transformers Learn Latent Mixture Models) | 6.40 | Comparable quality; both papers combine theory with experiments, each with different scope limitations. |
| `wqwtDpPeEf.md` (InverseScope) | 5.50 | Weaker theoretical contribution; our paper's theory is more novel and the experiments are more extensive. |
| `CtwyBsbvOA.md` (Transformers as Multi-task Learners) | 4.00 | Our paper has stronger theory, clearer experiments, and more impactful results. |
| `I3spHvRHqo.md` (A Non-vacuous Test Error Guarantee) | 4.00 | Our paper's contribution is cleaner and better validated. |

This paper makes a genuinely novel theoretical contribution backed by extensive empirical validation. The main weakness is the compressed proof sketch for the training-persistence claim (Theorem 2.3), and the HARDPROMPTS comparison is not well-calibrated. These are addressable issues that do not undermine the paper's core contributions. The paper is stronger than rejected anchors at similar scores (~5.5) and comparable to accepted papers at ~6.0–6.5.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>