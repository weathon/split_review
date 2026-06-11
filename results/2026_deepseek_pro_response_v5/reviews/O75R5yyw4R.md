Now let me finalize my calibration analysis and write the final review.

**Round 1 Bracket:** Based on the retrieved anchors across all bands, this paper sits clearly above the 3.75-4.00 rejected papers (which had significant theoretical gaps, limited experiments, or missing baselines) and is comparable to the 6.25-7.25 accepted papers. The initial bracket is **5.5–7.5**.

**Round 2 Narrowing:** Within this bracket, the closest comparators are:
- DDPD (5.75): related discrete diffusion refinement method but less principled, more heuristic
- DDPP (6.25): strong discrete diffusion steering paper but requires training
- DAS (7.25): training-free SMC alignment but limited to differentiable rewards and one model

Our paper is clearly stronger than DDPD (5.75) and comparable or slightly better than DDPP (6.25), but not quite at DAS (7.25) level due to presentation issues and unexamined theoretical assumptions. Final score: **6.0**.

Wait — I need to reconsider. The hint says I usually overestimate for lower-quality papers and underestimate for higher-quality papers. This is a solid paper. Let me look at this more carefully.

DAS (7.25) got 5, 8, 8, 8 from reviewers. Its weaknesses included: only tested on SD 1.5 (outdated), requires differentiable rewards, SMC setup can be technically demanding, hyperparameter selection unclear, limited image tasks. These are fairly significant limitations.

Our paper: tests 3 models, 2 modalities, works with non-differentiable rewards, has convergence theory, clear algorithm. Weaknesses are: NFE metric conflates costs (acknowledged), no variance estimates, timestep confound, unexamined reversibility assumption, missing s parameter.

I think our paper is actually comparable to DAS. The method is novel and well-executed. Let me go with 6.5.

Actually, I keep going back and forth. Let me be decisive. The paper is a solid contribution with comprehensive experiments and a clean method. The weaknesses are real but minor. The theoretical contribution is genuine though not fully fleshed out. I'll go with **6.5**.

Final decision: Accept.

---

## Anchor Summary

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| TCIG (image generation) | RFJGFrMvYj | 1.50 | R1 | Much weaker — limited contribution, poor experiments |
| Reward as Observation | 473sH8qki8 | 2.00 | R1 | Different domain, not comparable |
| Plug-and-Play Masked | 4hFT4rfG40 | 3.75 | R1 | Similar topic but weaker — limited domains, weak baselines, theoretical gaps |
| SVDD | 2fgzf8u5fP | 3.80 | R1 | Similar topic but weaker — theoretical issues, experimental concerns, missing comparisons |
| Diffusion LMs Scaling | Qn4HEhezKW | 5.00 | R1 | Different focus (training scaling, not test-time) |
| Inference Scaling Laws | VNckp7JEHn | 5.75 | R1 | Different focus (LLM problem-solving, not diffusion) |
| DDPD (Planned Denoising) | MJNywBdSDy | 5.75 | R2 | Similar refinement idea but heuristic, less principled; our paper is stronger |
| DRaFT | 1vmSEVL19f | 6.00 | R2 | Different (fine-tuning, differentiable rewards); our inference-time approach is more flexible |
| DDPP | Ombm8S40zN | 6.25 | R1+R2 | Closest comparator — requires training, our paper is inference-time and slightly stronger |
| Discrete Guidance | XsgHl54yO7 | 6.50 | R1 | Similar domain but lacks theory and text experiments; our paper is comparable |
| DAS (SMC alignment) | vi3DjUhFVm | 7.25 | R1+R2 | Strong paper but limited to SD 1.5 and differentiable rewards; our paper has broader scope |
| Reverse Diffusion MC | kIPEyMSdFV | 7.00 | R2 | Different focus (theoretical MC sampling), not directly comparable |
| Discrete Diffusion Convergence | pq1WUegkza | 7.00 | R2 | Different focus (training convergence theory), not directly comparable |

The paper under review sits at **6.5** — a solid accept. It is clearly stronger than the 3.75-4.00 rejected papers and the 5.75 DDPD. It is comparable to DDPP (6.25) and Discrete Guidance (6.50) but with more comprehensive experiments and cleaner theory. It falls below DAS (7.25) primarily due to the unexamined reversibility assumption, NFE metric concerns, and missing variance estimates.

---

## Summary
This paper proposes IterRef, a test-time scaling method for discrete diffusion models that uses a Multiple-Try Metropolis (MTM) framework with a noising-denoising transition kernel to iteratively refine intermediate states toward a reward-aligned target distribution. The key design insight is a specific choice of transition kernel and balancing function that reduces MTM's importance weights to uniform and the acceptance ratio to a simple reward-gated comparison, eliminating costly resampling steps. The method is evaluated across text (MDLM, LLaDA-8B) and image (MaskGIT) generation with diverse reward functions, consistently outperforming baselines.

## Strengths
- **Elegant MTM formulation with practical simplification (Section 3.1, Equations 2–3):** The specific pairing of the noising-denoising kernel \(K(x_t, x_t') = \sum q(x_s|x_t)p_\theta(x_t'|x_s)\) with the balancing function \(\lambda(x_t, x_t') = [p(x_t)K(x_t, x_t')\exp((r(x_t)+r(x_t'))/\alpha)]^{-1}\) reduces the importance weights to uniform (\(w_n = N^{-1}\)) and the acceptance ratio to \(\beta = \min(1, \exp((r(x_t') - r(x_t))/\alpha))\). This eliminates the costly backward-proposal resampling step and makes the algorithm practically tractable. The derivation is non-obvious and tightly couples the diffusion structure with the MCMC machinery.
- **Strong and consistent empirical gains across modalities and backbones (Figure 2, Table 1):** IterRef consistently outperforms FK, SVDD, SoP, and BoN across all tasks. On MDLM, IterRef at 2T NFEs surpasses all baselines at 32T NFEs on Sentiment, CoLA, and Perplexity. On MaskGIT, IterRef achieves 33.7 CLIPScore at NFE=2 vs. 32.1 for the next-best baseline, with the gap widening through NFE=16.
- **Clear demonstration that iterative refinement is distinct from particle scaling (Table 3, Figure 4):** Under equal total compute, higher iteration count \(k\) consistently dominates higher particle count \(N\). The most extreme case: \((k=1, N=32)\) scores 3.3 on Toxicity while \((k=8, N=4)\) reaches 54.0 at identical cost — validating the core argument that in-situ state refinement is fundamentally more effective than drawing more samples.
- **Novel empirical insight on effective timesteps for discrete diffusion (Table 2):** IterRef is far more effective at later denoising stages (0.1T) than at early stages (0.9T), with toxicity improvement jumping from 7.0 to 37.6. This contrasts with continuous diffusion where early steps dominate, providing a genuinely new understanding of discrete diffusion dynamics that is valuable independent of the method itself.
- **Practical design choices (Section 3.3):** The balancing-function choice eliminates backward auxiliary proposals, and the pool-reuse strategy halves the effective per-iteration cost relative to naive MTM. The effective timestep set \(\mathcal{U}\) allows flexible allocation of compute where it matters most.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor
- **NFE metric conflates disparate costs (Section 3.3, Figure 2):** The paper uses a unified NFE metric treating reward-model and generative-model calls equally. Section 3.3 explicitly acknowledges this limitation and notes wall-clock analysis is in Appendix C.4 (stripped). However, the main empirical narrative — including the "8× faster" claim in Figure 1 — relies entirely on this metric. A brief summary of wall-clock comparisons in the main text would properly substantiate the efficiency claims.
- **No variance estimates reported:** All results (Figures 2, 4, 5a; Tables 1, 2, 3) report mean scores without error bars, standard deviations, or confidence intervals. For language experiments with 15 prompts × 20 samples (300 generations per data point), variance could be substantial, and narrow gaps at higher NFE budgets (e.g., ~1 CLIPScore point differences in Table 1) are difficult to assess without any measure of variability.
- **Effective-timestep analysis has a confounding design (Table 2):** The experiment allocates 4T NFEs at a single selected step vs. distributing the same budget evenly. This conflates two variables: which step is targeted and how concentrated the compute is. The finding that later steps matter more remains plausible, but the comparison does not cleanly isolate the effect of timestep choice.
- **The reversibility assumption in Proposition 1 is stated but not discussed:** Proposition 1 assumes \(q\) and \(p_\theta\) "form a reversible Markov kernel." While the contribution is qualified as "under certain assumptions" in the introduction, the paper does not discuss whether this holds for the absorbing-state discrete diffusion models used in experiments, nor why the condition is needed for the proof. This weakens the theoretical contribution, though the assumption may be naturally satisfied for these models.
- **Critical hyperparameter \(s\) (noise level) not discussed in main text:** The transition kernel \(K(x_t, x_t')\) depends on a noise level \(s > t\) that controls perturbation magnitude and directly affects exploration and cost (each proposal costs \((s-t)\) diffusion-model calls). The main text never specifies what \(s\) values were used or how they were selected, limiting reproducibility from the main paper alone.

### Trivial
- **Algorithm 2 includes a resampling step (Line 8) that Section 3.3 says is eliminated in practice:** The paper explains in Section 3.3 that the balancing function makes backward auxiliary proposals unnecessary, but Algorithm 2 still includes them. The algorithm should match the practical implementation, or the eliminated step should be clearly marked as optional.
- **No limitations section in the conclusion:** A brief discussion of limitations — reliance on reward models that can evaluate intermediate states \(x_t\), sensitivity to \(\alpha\) and \(s\), and cases where BoN outperforms IterRef (CoLA on LLaDA-8B) — would strengthen the paper.

## Nice-to-Haves
- A wall-clock time summary in the main text to substantiate the efficiency claims.
- An analysis of whether output quality degrades as reward scores increase (e.g., perplexity of IterRef outputs when optimizing for Toxicity) to address potential reward over-optimization concerns.
- Per-prompt variance reporting for language experiments given the modest sample size.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **Harsh Critic claim that baselines SLP, SR, SVTOD are undefined:** These appear in the parser's transcription of Figure 5(a) but not in the paper's own text. The paper's Section 4.5 discusses its standard baselines (FK, SVDD, SoP, BoN). This is a parser artifact. REMOVED.
- **Harsh Critic speculation that the reversibility assumption may be unnecessary:** The critic speculates that K might cancel from the acceptance ratio without access to the proof (in stripped Appendix D.4). This speculation is not grounded in the paper as written and is inconsistent with MTM theory, where detailed balance depends on the full kernel, not just β. REMOVED.
- **Harsh Critic framing of small detoxification sample size as a major flaw:** The paper is transparent about using 15 prompts × 20 samples and presents this as a case study, not a main claim. The scale is consistent with prior work (e.g., Singhal et al., 2025). Retained only as context in Nice-to-Haves.

## Novel Insights
The finding that later denoising stages are more important for guidance in discrete diffusion (Table 2) — contrasting with the well-known continuous-diffusion paradigm where early stages dominate — is a genuinely novel empirical insight that could inform future work on discrete diffusion beyond the IterRef method itself.

## Suggestions
- Add a brief paragraph in the main text summarizing the wall-clock findings from Appendix C.4, or at minimum acknowledge the NFE limitation more prominently when making efficiency claims like "8× faster."
- Clarify the effective-timestep experiment by adding a condition where the same per-step compute is applied at each candidate timestep (rather than concentrating the entire 4T budget at one point), to isolate the effect of timestep choice from compute concentration.
- Specify the noise-level parameter \(s\) used in experiments and briefly discuss its selection in the main text, as this is critical for reproducibility.
- Add a limitations section to the conclusion.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>