Now I have enough information to write my review and assign a score. Let me synthesize everything.

## Summary

This paper introduces Insertion Language Models (ILMs), a new generative model class that generates sequences by inserting tokens at arbitrary positions one at a time, selecting both the insertion position and vocabulary element jointly. The approach is trained with a denoising objective on token subsequences and uses a stopping classifier to handle variable-length generation. The paper demonstrates strong advantages over ARMs and MDMs on synthetic planning tasks (star graphs and zebra puzzles) and shows competitive text generation with superior infilling flexibility compared to MDMs on LM1B and TinyStories.

## Strengths

- **Novel model class with compelling synthetic evidence**: The star graph experiments (Table 1) are the paper's standout contribution. ILM achieves 100% exact match on Star_medium and 99.1% on Star_hard, where MDM drops to 36.5% and 21.0% and ARM to 75.0% and 23.0%. The paper provides a clear explanation for MDM's failure (absolute vs. relative positions) and includes the Insertion Transformer baseline (35.2%, 22.1%, 17.5%) to show the specific design choices matter.

- **Clean formulation and training approach**: The paper presents a well-motivated training objective (Equation 2) with a tailored transformer parameterization (Equations 3-4) and a stopping classifier. The training diagram (Figure 2) and algorithms make the approach reproducible. The design of using relative positions (insertion between existing tokens) rather than absolute positions is a well-justified architectural choice.

- **Strong infilling results over MDMs**: Table 3 shows ILM consistently outperforms MDM on infilling across all three datasets and metrics (e.g., LM1B single-segment ΔNLL_inp: -3.57% vs -0.49%), demonstrating ILM's practical advantage in handling variable-length gaps without fixed mask constraints.

- **Competitive text generation with honest framing**: The paper is appropriately modest about text results, claiming ILMs are "competitive with ARMs" rather than superior. The Prometheus LLM judge scores (Figure 5) show ILM outperforming MDM on coherence and consistency across both datasets.

- **Insightful comparison against Insertion Transformer**: Table 1 shows IT significantly underperforming ILM on star graphs, and the qualitative analysis (Appendix C.0.2) of IT's tendency to over/undershoot sequence length validates the specific design of ILM's stopping classifier and normalized-count training target.

## Weaknesses

### Fatal

None.

### Major

- **Text experiments do not exercise the capabilities motivating ILMs** — The paper's central motivation is sequences with "sophisticated constraints" and non-left-to-right dependencies, yet the text experiments (Section 5.3) test only unconditional generation on LM1B and TinyStories—settings where left-to-right generation is perfectly adequate. ILM's NLL is 4.67 vs ARM's 3.94 on LM1B (Table 2), a substantial gap, and essentially tied on Stories (2.14 vs 2.11). The paper would be significantly strengthened by even one text experiment demonstrating ILM advantages on tasks requiring out-of-order generation (e.g., constrained generation, structured infilling with interacting constraints). This creates a gap between the paper's motivation and its text evidence that weakens the text-generation portion of the contribution.

- **Missing greedy-sequential MDM comparison** — The paper acknowledges in Section 1 that greedy unmasking (one token per forward pass) addresses MDM's simultaneous-unmasking limitation but generates slowly. All MDM comparisons use the default tau-leaping sampler with simultaneous unmasking. A comparison against greedy-sequential MDM would directly clarify whether ILM's advantage stems from the *model class* or from comparing against suboptimal MDM inference. The paper explicitly mentions this approach in the introduction (line 57-59), making its omission more conspicuous.

### Minor

- **ILM generates substantially shorter sequences than training data on Stories** — Table 2 shows ILM's mean generated length is 119 tokens vs. 205 in the training data (for Stories) and 21 vs. 28 on LM1B. While MDM's length problem (985 tokens on Stories) is more severe, ILM's stopping classifier appears systematically aggressive, which could affect downstream quality. This deserves some discussion.

- **The approximate training objective's bias is acknowledged but under-analyzed** — The paper notes the true denoising objective has "extremely high variance" (line 77) and substitutes a biased approximation (Equation 2). While this works empirically, a brief characterization of when this approximation is adequate vs. breaks down would strengthen the contribution. (Note: Appendix D may address this, but it was stripped from the review version.)

- **Infilling evaluation dataset may not be well-suited** — For TinyStories infilling (Table 3), both models show increased NLL relative to the input (+3.63 MDM, +1.79 ILM), and the paper acknowledges this is because "removing a sentence from the middle may not change the overall meaning too much." A dataset where removed segments are more consequential would provide a more informative test.

### Trivial

None.

## Nice-to-Haves

- A visualization or statistics of insertion positions chosen by ILM during inference would illuminate what ordering strategy the model learns, complementing the trajectory examples in Figure 7 (Appendix).
- The MDM's extreme length generation on Stories (985 vs 205 mean) deserves more prominent discussion, as it fundamentally distorts the NLL comparison and represents a significant quality failure.

## Removed Points

These points are flagged to be removed per the filtering discipline. Treat them with caution.

- **Missing FIM-ARM baselines in infilling** — The paper explicitly addresses this at Section 5.3.2: "we only compare MDMs and ILMs as ARMs are not capable of performing infilling without specialized training." The paper also discusses FIM's limitation (single-gap infilling only) in Section 4. This is a justified scope decision rather than an omission. The harsh critic's point about FIM-ARM in infilling is reasonable in principle but the paper's exclusion is well-motivated given FIM's inability to handle multi-gap infilling.

- **Training approximation under-analyzed (fatal variant)** — The harsh critic's concern about the training objective's bias is valid but the Appendix (stripped) likely addresses it. The strong empirical results suggest the approximation works. This is demoted from a potential fatal flaw to a minor weakness.

- **Missing diversity metrics beyond entropy** — This is a reasonable nice-to-have but does not undermine the paper's core claims.

- **Figure 6 caption should note ARM with KV cache** — The figure explicitly labels "ARM (w/o KV cache)" and the limitations section discusses this. Minor presentation issue.

- **Section 3 train-test mismatch with uniform distribution over n** — This parallels similar issues in diffusion models and is speculative rather than empirically demonstrated.

## Novel Insights

The paper's most genuinely novel observation is that MDMs fail on variable-length planning tasks not because of insufficient model capacity but because of their reliance on absolute token positions—predicting absolute positions of junction/target nodes when arm lengths vary is essentially equivalent to solving the puzzle itself. ILM overcomes this through relative-position insertion, which is a meaningful architectural insight for the non-autoregressive generation community. The comparison against Insertion Transformer further isolates that the stopping classifier and normalized-count objective are the critical design choices, not merely the insertion mechanism.

## Suggestions

1. Add at least one text experiment that exercises out-of-order generation capability (e.g., constrained generation with global constraints, or multi-span infilling where fill positions interact). This is more impactful than scaling existing experiments.
2. Include a greedy-sequential MDM baseline to distinguish model-class advantages from inference-procedure advantages.
3. More prominently discuss ILM's shorter-than-training sequence lengths and the MDM's extreme length generation in the main text, not as footnotes.

## Calibration Report

**Round 1 anchors:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| FiLM: Fill-in Language Models (UbOzNf6hGq) | 4.25 | 1 | Similar topic (insertion-based generation) but less technically novel; ILM introduces a new model class vs. changing masking ratios |
| Diffusion LMs Can Perform Many Tasks (Qn4HEhezKW) | 5.00 | 1 | Broader scope but less focused contribution; ILM has cleaner motivation and experiments |
| Scaling up Masked Diffusion Models (WNvvwK0tut) | 6.50 | 1 | Comprehensive scaling study; ILM has comparable novelty but smaller scale |
| Energy-Based Diffusion LMs (sL2F9YCMXf) | 6.75 | 1 | Strong technical novelty + results; ILM is comparable in novelty |
| Beyond Autoregression: DD for Planning (NRYgUzSPZz) | 6.25 | 1 | Very similar structure: strong planning results, limited generalization; comparable quality |
| Interpolating AR and DD (tyEyYT267x) | 8.00 | 1 | Clearly stronger all around |

**Round 2 anchors:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Diffusion LMs Can Perform Many Tasks (Qn4HEhezKW) | 5.00 | 2 | ILM is clearly stronger: more novel, cleaner experiments |
| A Reparameterized Discrete Diffusion (1pTlvxIfuV) | 5.50 | 2 | Novel contribution but less motivated than ILM |
| Simple and Controllable Uniform DD (i5MrJ6g5G1) | 5.25 | 2 | More focused contribution; ILM's planning experiments are more convincing |
| Think while You Generate: DD with Planned Denoising (MJNywBdSDy) | 5.75 | 2 | Introduces planner+denoiser separation; ILM's overall contribution is comparable |
| Beyond Autoregression (NRYgUzSPZz) | 6.25 | 2 | Most directly comparable; ILM's model class is more novel, planning results similar strength, text experiments similarly limited |
| PlaSma: Planning with Small LMs (dFcXJgnrGB) | 6.50 | 2 | Different approach to planning; not directly comparable |
| Retrieval is Accurate Generation (oXYZJXDdo7) | 7.00 | 2 | Stronger overall; ILM is below this |

**Round 1 bracket:** 4.5–7.0
**Round 2 narrowing:** The paper is clearly above the 5.0-5.75 range (FiLM, reparameterized DD, simple uniform DD) due to its stronger motivation, cleaner experiments, and more novel model class. It is comparable to "Beyond Autoregression" (6.25), which has similar structure (strong planning results, limited text generalization) but slightly less architectural novelty. It is below the Energy-Based DL (6.75) and Interpolating AR/DD (8.00) anchors which have both stronger technical contributions and broader validation.

**Final positioning:** 6.0 — the paper introduces a genuinely novel model class with compelling synthetic planning evidence and competitive text results, but the text experiments don't exercise ILM's specific advantages and some important comparisons are missing.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>