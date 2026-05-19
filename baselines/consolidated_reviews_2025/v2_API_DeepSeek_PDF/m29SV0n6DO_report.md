## Summary
# Final Review Report

## Summary

This paper presents **Toto**, a causal transformer for generative pre-training from videos via next-token prediction. The approach is conceptually straightforward: tokenize video frames into discrete dVAE tokens, arrange them in raster-scan order across frames, and train a decoder-only transformer to predict the next visual token using a standard autoregressive language modeling objective. Key design choices include RoPE relative positional embeddings (enabling coarse-to-fine resolution training), the use of discrete visual tokens from dVAE, and attention pooling for downstream feature extraction. The model is trained at three scales (120M, 280M, 1.1B parameters) on over 1 trillion visual tokens drawn from ImageNet, Kinetics-600, Ego4D, and HowTo100m.

The paper is best described as an **empirical benchmark study**: it does not claim a novel method (the abstract explicitly states "this paper does not describe a novel method"), but rather investigates whether an off-the-shelf autoregressive architecture can learn competitive visual representations when scaled to video data. The core value lies in (1) demonstrating that autoregressive next-token prediction can scale to video at >1 trillion tokens, (2) providing ablation studies on tokenization, probing methods, and resolution strategies, and (3) documenting scaling laws for visual next-token prediction.

**Key strengths:** The scale of pre-training (1T tokens, multiple video datasets, three model sizes) is substantial. The breadth of evaluation across image recognition, video classification, tracking, action anticipation, and robotic manipulation is commendable. The resolution fine-tuning experiment (low-res pre-train → high-res fine-tune) is a practical and insightful finding.

**Key weaknesses:** (1) Critical factual error: real-world robotics results (63%) are reported as "comparable" to the MVP baseline (75%), but the 12-point gap contradicts this characterization. (2) Multiple overclaims: "competitive across all tasks" is unsupported by the evidence (real-world robotics is worse; ImageNet trails MAE/AIM by 5.6-6.9 points). (3) The "first to show" novelty claim on K400 action recognition cannot be verified without external literature retrieval (deferred in this run). (4) The scaling law comparison with GPT-3 uses a different tokenizer (VQGAN vs dVAE) and is methodologically invalid. (5) Statistical rigor is limited: no variance, confidence intervals, or significance tests reported across any experiment.

## Strengths
1. **Large-scale empirical study with diverse evaluation.** The paper pre-trains models at three scales (120M, 280M, 1.1B) on over 1 trillion visual tokens from four complementary datasets (ImageNet, Kinetics-600, Ego4D, HowTo100m ≈97k hours of video). Downstream evaluation covers image classification (ImageNet), action recognition (Kinetics-400), action anticipation (Ego4D), video tracking (DAVIS), object permanence (CATER), simulated robotic manipulation (Franka/Kuka), and real-world robotics. This breadth provides a useful picture of where autoregressive video pre-training works well and where it struggles.

2. **Practical insight: coarse-to-fine resolution training.** The finding that low-resolution pre-training followed by one epoch of high-resolution fine-tuning outperforms full-resolution training from scratch (Table 4: 63.2% vs 61.2%, further improved to 64.4% with RoPE base increase) is practically valuable for resource-constrained training. The use of RoPE embeddings makes this possible, and the paper correctly identifies this as a cost-saving strategy.

3. **Systematic and informative tokenizer ablation.** Table 3 compares six tokenization strategies (VQGAN-16k, VQGAN-1k, dVAE-32x32, dVAE-16x16, patch-patch, patch-dVAE) under controlled conditions and finds that most methods perform similarly (60.6-61.3%). This is a useful reference result for researchers designing autoregressive vision models.

4. **Attention pooling vs average pooling analysis.** The paper shows a 7.9% improvement from attention pooling over average pooling for decoder-only models (Table 5). This confirms that naive averaging is suboptimal for autoregressive models due to skewed token attention patterns, and provides a practical recommendation for future work.

5. **Honest framing.** The abstract's admission that "this paper does not describe a novel method" is refreshingly candid and sets appropriate expectations. The paper is most valuable as a large-scale empirical study and benchmark, not as a methodological innovation.

6. **Scaling law documentation for visual next-token prediction.** Despite methodological concerns (tokenizer mismatch with main experiments), the attempt to characterize scaling laws for visual autoregressive models is a valuable contribution to the field's understanding of compute-efficient video pre-training.

## Weaknesses
**W1. Critical data-narrative mismatch in real-world robotics (Severity: Critical).**  
Table 11 shows Toto-base achieves 63% success on real-world Franka cube-picking while the MVP baseline achieves 75%. The paper characterizes this as "on-par performance to state-of-the-art robot models" and "performs comparably." A 12-percentage-point gap (16% relative degradation) is not "comparable." This mismatch is the single most serious factual issue in the paper. The narrative must be corrected to honestly reflect the observed results. See annotation on Page 9 - Section 4.6 Robotics.

**W2. Broad overclaiming of results (Severity: Major).**  
The abstract, introduction, and conclusion repeatedly state that Toto achieves "competitive performance across all benchmarks" and "across all tasks." This is not supported:  
- Real-world robotics: 63% vs 75% (worse, not competitive)  
- ImageNet: 75.3% vs MAE 80.9% and AIM 82.2% (trails by 5.6-6.9 points)  
- K400 action recognition: 74.4% vs VideoMAE 79.8% and DINOv2 84.4% (trails by 5.4-10 points)  
- DAVIS tracking at matched resolution: Toto-base (42.0) vs DINO-base (54.3) — Toto is substantially worse at the same resolution
The paper should use bounded, comparative language that acknowledges where the method underperforms. See annotation on Page 7 - Section 4.2 Image Recognition and Page 9 - Section 4.6 Robotics.

**W3. Unverifiable novelty claims (Severity: Major).**  
The paper claims "first to show the competitive performance on K400 with autoregressive pre-training" (Section 4.3) and "highest accuracy on autoregressive modeling" (Table 7 caption). Since external literature retrieval is unavailable in this run (Retrieval-Disabled Mode), these claims cannot be independently verified. The AIM model (2024) uses autoregressive patch prediction and reports ImageNet results — the claim of "highest among autoregressive" should clarify that AIM uses continuous patch regression rather than discrete token classification. See annotation on Page 7 - Section 4.2 Image Recognition and Page 7 - Section 4.3 Action Recognition.

**W4. Methodology errors in scaling analysis (Severity: Major).**  
The scaling experiments (Section 4.8) use VQGAN tokenizer while all other experiments use dVAE. The scaling law is compared to GPT-3's despite different loss functions, tokenizers, and data modalities. The paper then draws the conclusion that "visual next token models scale at a slower rate than language only models" — an unsupported claim given the confounds. See annotation on Page 10 - Section 4.8 Compute Optimal Scaling.

**W5. Absence of statistical rigor (Severity: Major).**  
No variance, confidence intervals, or significance tests are reported across any experiment. Many comparisons involve small differences (Table 3: 61.3% vs 61.2%; Table 9: 2.70 vs 2.60) that could be noise. The DAVIS tracking comparison (Table 10) confounds resolution and model capacity. The Ego4D action anticipation results are all near chance (overall mAP ≤ 2.70). See annotations on Page 5 - Section 4.1 Design Choices (Table 3), Page 8 - Table 9, Page 8 - Table 10.

**W6. Tokenizer inconsistency claim without evidence (Severity: Minor).**  
The paper states VQGAN is "contaminated with ImageNet label information via perceptual loss" (Page 4). However, the results show VQGAN-16k (61.3%) and dVAE-32x32 (61.2%) are nearly identical, which weakens the contamination argument. If VQGAN's label leakage significantly biased representations, a larger performance gap would be expected. See annotation on Page 4 - Section 3.3 Data Set.

**W7. Formula notation issues (Severity: Minor).**  
The pre-training objective (Eq. 1-2) has ambiguous arrow notation and potential sign error. The forward equations (Eq. 3-5) reuse the same symbol for different intermediate variables, reducing reproducibility. See annotations on Page 3 - Section 3.1 Pre-training and Page 4 - Section 3.4 Downstream Transfer.

**W8. Missing limitations and analysis depth (Severity: Major).**  
The paper lacks: (a) any limitations section discussing when and why the method fails; (b) analysis of why autoregressive video pre-training underperforms masked modeling on several benchmarks; (c) discussion of the simulation-to-real gap in robotics; (d) sensitivity analysis of data mixing ratios; (e) variance reporting; (f) failure case analysis. See annotation on Page 10 - Conclusion.

**W9. Introduction narrative is too slow (Severity: Minor).**  
The first two paragraphs recount historical anecdotes (Shannon 1951, Attneave 1954) that delay the paper's core motivation. The research gap is not explicitly stated until the third paragraph, and the solution is introduced in the fourth. At ICLR paper length, this is too slow. See annotation on Page 1 - Introduction.

**W10. Related Work is a list rather than positioned comparison (Severity: Minor).**  
The Related Work section (Page 2) reads as a chronological summary rather than organizing around comparison axes. The specific technical differences with the closest prior work (iGPT, AIM) are not articulated with sufficient depth. See annotation on Page 2 - Related Work.

## Key Issues
The following are the top-priority issues ranked by severity and research-value impact:

### Key Issue #1 (Critical): Robotics results contradict narrative claims
**Location:** Page 9 - Section 4.6 Robotics, Table 11  
**Evidence:** Toto-base achieves 63% vs MVP 75% success on real-world cube-picking.  
**Mechanism:** The narrative says "on-par" and "comparable" while the data shows a 12-point gap. This is a factual error in the presentation, not a methodological flaw — the data itself is valid, but the claims about the data are wrong.  
**Impact:** If uncorrected, readers will distrust the paper's objectivity. The mismatch affects the credibility of all other "competitive" claims.  
**Fix:** Correct text to honestly report the results, add confidence intervals, discuss the simulation-to-real gap.

### Key Issue #2 (Major): Broad overclaiming across tasks
**Locations:** Abstract, Page 1 - Introduction, Page 10 - Conclusion  
**Evidence:** "Competitive across all benchmarks," "competitive performance across all tasks" — contradicted by real-world robotics (63% vs 75%), ImageNet (75.3% vs MAE 80.9%), and DAVIS at matched resolution (42.0 vs DINO 54.3).  
**Mechanism:** The paper uses absolute framing ("all") where comparative framing (e.g., "on several benchmarks") is warranted.  
**Fix:** Replace all instances of "competitive across all" with task-specific, evidence-linked claims.

### Key Issue #3 (Major): Methodologically invalid scaling comparison
**Location:** Page 10 - Section 4.8 Compute Optimal Scaling  
**Evidence:** Scaling law L(C)=7.42·C^{-0.0386} derived with VQGAN tokenizer, compared to GPT-3's L(C)=2.57·C^{-0.048} with BPE text tokenizer.  
**Mechanism:** Two different tokenizers (VQGAN vs BPE), different loss functions (visual token CE vs text CE), and different data distributions. The comparison is not apples-to-apples.  
**Fix:** Remove direct exponent comparison with GPT-3. Report scaling law with explicit caveat about tokenizer dependency.

### Key Issue #4 (Major): Pre-training objective notation errors
**Location:** Page 3 - Section 3.1 Pre-training, Eqs. (1)-(2)  
**Evidence:** Eq. (1) uses ambiguous arrow notation for conditioning; Eq. (2) has unclear sign (→ instead of -).  
**Mechanism:** These are not just cosmetic issues — ambiguous notation can lead to implementation errors and reproducibility failures.  
**Fix:** Adopt standard autoregressive notation with clear negative log-likelihood.

### Key Issue #5 (Major): Missing statistical rigor
**Locations:** Tables 3, 4, 5, 6, 7, 8, 9, 10, 11, 12  
**Evidence:** No variance, CI, or significance tests reported. Many comparisons involve marginal differences. Real-world robotics uses only 16 trials.  
**Fix:** Report mean±std over ≥3 seeds for all main experiments. Add confidence intervals for the robotics results.

## Actionable Suggestions
### S1 (Must): Correct the real-world robotics narrative
**Target:** Page 9 - Section 4.6 Robotics (paragraph and Table 11)  
**Action:** Replace all instances of "comparable" and "on-par" with accurate descriptions. The revised text should read: "Toto-base achieves 63% success rate over 16 trials, compared to MVP's 75% under the same setup. While Toto shows faster learning in simulation, its real-world performance trails the MVP baseline by 12 percentage points. With 16 trials, the 95% confidence intervals overlap considerably (Toto: 39-83%; MVP: 51-91%), indicating that additional trials are needed to establish a statistically significant difference."

### S2 (Must): Remove or bound all "competitive across all tasks" claims
**Target:** Abstract, Page 1 - Introduction, Page 10 - Conclusion  
**Action:** Replace every instance of "competitive across all benchmarks/tasks" with task-specific, evidence-linked statements. Example: "Toto achieves competitive results on image recognition (75.3%), action recognition (74.4%), and simulated robotic manipulation, while underperforming on real-world robotics (63% vs 75% for MVP) compared to state-of-the-art methods."

### S3 (Must): Fix pre-training objective notation (Eq. 1-2)
**Target:** Page 3 - Section 3.1  
**Action:** Replace Eq. (1) with standard autoregressive factorization:  
$$p(x^j) = \prod_{i=1}^n p(x^j_i \mid x^j_1, x^j_2, \dots, x^j_{i-1}; \omega)$$  
Replace Eq. (2) with proper negative log-likelihood:  
$$L_{\text{pre-train}} = -\mathbb{E}_{x^j \sim X} [\log p(x^j)]$$

### S4 (Must): Fix forward equation notation (Eq. 3-5)
**Target:** Page 4 - Section 3.4  
**Action:** Use distinct intermediate variables:  
$$H' = \text{LayerNorm}(H^\ell)$$  
$$H_{\text{attn}} = H' + \text{MHSA}(H')$$  
$$H^{\ell+1} = H_{\text{attn}} + \text{FFN}_{\text{SwiGLU}}(H_{\text{attn}})$$

### S5 (Must): Bound novelty claims and add qualifiers
**Target:** Page 7 - Section 4.2 (Table 7 caption: "highest accuracy on autoregressive modeling") and Section 4.3 ("first to show competitive performance")  
**Action:** Change to: "to our knowledge, the first demonstration of autoregressive next-token prediction transferring to action recognition at competitive levels" and "highest accuracy among autoregressive models operating on discrete visual tokens," explicitly noting that AIM uses continuous patch regression.

### S6 (Must): Remove or rephrase scaling law comparison with GPT-3
**Target:** Page 10 - Section 4.8  
**Action:** Replace the GPT-3 comparison with: "The measured exponent α=0.0386 applies to VQGAN-based training; the exponent may differ when using alternative tokenizers (e.g., dVAE) or data distributions. A direct comparison with language model scaling exponents is not meaningful due to differences in tokenization, loss functions, and modality."

### S7 (Nice-to-have): Add variance reporting
**Target:** All experiment tables  
**Action:** Report mean±std over ≥3 independent seeds for ImageNet, K400, and DAVIS experiments. For real-world robotics, report per-trial breakdown and confidence intervals. For Ego4D, note that all scores are low (mAP≤2.70) and add confidence estimates.

### S8 (Nice-to-have): Add limitations section
**Target:** New subsection after Conclusion  
**Action:** Write a 1-paragraph limitations section covering: (a) resolution gap between image (256x256) and video (128x128) evaluations; (b) absence of out-of-domain generalization tests; (c) the simulation-to-real gap in robotics; (d) the lack of data mixing sensitivity analysis; (e) the tokenizer dependency of scaling laws.

### S9 (Nice-to-have): Expand tokenizer contamination analysis
**Target:** Page 4 - Section 3.3  
**Action:** Add a sentence noting that while VQGAN uses perceptual loss with a VGG network pre-trained on ImageNet, the empirical results (Table 3) do not show a significant advantage for VQGAN over dVAE at matched resolution, suggesting the practical impact of label leakage is limited in this setting.

### S10 (Nice-to-have): Add DAVIS tracking with resolution-controlled comparison
**Target:** Page 8 - Section 4.5, Table 10  
**Action:** Report Toto-large results at 224x224 resolution for direct comparison with DINO-base at 224/8. Add DINO evaluated at 512x512 resolution if possible. Add a column for evaluation resolution and model capacity in the table.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
1. Historical anecdote: Shannon's guessing game (1951) → LLMs
2. Historical anecdote: Attneave's image analog (1954)
3. "Big Visual Data is in videos" → motivation
4. Method overview and contribution summary

**Problem:** The narrative arc (historical → motivational → technical) is too slow. The first 50% of the introduction builds context that, while interesting, does not directly advance the paper's core argument or establish the research gap. A conference paper introduction should establish stakes, gap, and solution within the first 1-2 paragraphs.

**Problem alignment check (FAIL):** The historical anecdotes do not map onto the paper's actual contribution. Shannon/Attneave are about modeling data distributions, while the paper's actual value is in scaling and ablations — not in advancing the theory of generative modeling.

**Variable alignment check (PARTIAL):** The introduction mentions "tokenization," "relative embeddings," and "attention pooling," which do appear as method variables. But the historical framing of "guessing games" is not reflected in any experimental variable.

**Contribution-evidence alignment check (PARTIAL):** The introduction claims "competitive performance across all benchmarks," which is contradicted by the evidence as noted in W1/W2.

### Recommended Storyline Candidate (Best)

A tighter, more effective introduction would follow this arc:

**P1 — Big Picture + Gap (2-3 sentences):**
"Autoregressive next-token prediction has become the dominant paradigm for pre-training large language models, producing representations that transfer effectively across diverse tasks without task-specific architectural modifications. While analogous approaches have been explored for images (iGPT, AIM), video autoregressive pre-training at scale remains largely unexplored — existing video representation learning is dominated by masked modeling (VideoMAE, ST-MAE) and contrastive objectives."

**P2 — Specific Gap + Proposed Solution (3-4 sentences):**
"Scaling autoregressive pre-training to video introduces three challenges: (i) the number of visual tokens per video is orders of magnitude larger than per image; (ii) existing discrete tokenizers (VQGAN, dVAE) have different trade-offs between reconstruction quality and label contamination; (iii) decoder-only architectures lack the asymmetric encoder-decoder design of masked models, requiring alternative downstream feature extraction strategies. This paper investigates whether a straightforward causal transformer, trained to predict the next visual token from video, can learn generalizable representations competitive with these more specialized approaches."

**P3 — Method Overview + Key Findings (3-4 sentences):**
"We present Toto, a causal transformer pre-trained via next-token prediction on over 1 trillion visual tokens from diverse video datasets. Key design choices include dVAE tokenization with discrete token prediction, RoPE relative positional embeddings enabling coarse-to-fine resolution training, and attention pooling for feature extraction. Through systematic ablation, we find that tokenization choice has limited impact on representation quality, and that low-resolution pre-training followed by high-resolution fine-tuning outperforms full-resolution training from scratch."

**P4 — Empirical Results + Contribution Summary (3-4 sentences):**
"Empirically, Toto achieves competitive results on image recognition (75.3% on ImageNet-1k), action recognition (74.4% on Kinetics-400), and simulated robotic manipulation, while showing mixed results on real-world robotics (63% vs 75% for MVP). We document scaling laws for visual next-token prediction, showing a power-law relationship with compute. These findings establish autoregressive video pre-training as a viable alternative to masked modeling, while identifying areas where further innovation is needed."

### Abstract Outline (Complete)

**S1 (Problem + Domain):** "We study generative pre-training from videos via next-token prediction, an approach that has been highly effective in language and image domains but remains under-explored for video."

**S2 (Challenge/Gap):** "A key challenge is scaling to video data, which requires orders of magnitude more tokens than images and different considerations for position encoding, tokenization, and downstream feature extraction."

**S3 (Proposed Method):** "We present Toto, a causal transformer pre-trained autoregressively on over 1 trillion visual tokens from diverse video and image datasets, using dVAE discrete tokenization and RoPE relative positional embeddings."

**S4 (Key Results):** "Toto achieves competitive performance on image classification (75.3%), action recognition (74.4% on Kinetics-400), and simulated robotic manipulation, with scaling laws showing a power-law loss-compute relationship."

**S5 (Bounded Claim):** "These results demonstrate that autoregressive video pre-training is a viable approach for learning transferable visual representations, while the gap with state-of-the-art masked modeling on several benchmarks highlights directions for future improvement."

### Introduction Outline (Complete)

**P1 (Establish Territory + Gap):** "Autoregressive pre-training dominates NLP and has been explored for images (iGPT, AIM), but video autoregressive pre-training at scale is largely unexplored. The dominance of masked modeling (VideoMAE) in video representation learning motivates investigating whether next-token prediction can also scale to video and produce competitive representations."

**P2 (Concrete Challenges + This Paper's Response):** "Scaling to video introduces challenges in token volume, position encoding, and downstream evaluation. We address these through discrete token prediction, RoPE embeddings enabling coarse-to-fine training, and attention pooling for feature extraction."

**P3 (Method Overview):** "Toto is a causal transformer with RMSNorm, SwiGLU activations, and RoPE. Pre-trained on 1T tokens from ImageNet, Kinetics-600, Ego4D, and HowTo100m at three scales (120M, 280M, 1.1B)."

**P4 (Results Preview + Contribution Claims):** "We show competitive results on ImageNet, K400, Ego4D, DAVIS tracking, CATER object permanence, and robotic manipulation. Three contributions: (C1) first demonstration of autoregressive next-token prediction scaling to video with competitive transfer; (C2) systematic ablation of design choices; (C3) scaling laws for visual next-token prediction."

### Alternative Storyline Option 2 (Results-First)

For a paper primarily valued as an empirical study, consider a "results-first" structure:

Title: "Autoregressive Video Pre-training at Scale: An Empirical Study"

P1: State that this paper studies whether next-token prediction can scale to video.
P2: Present the main finding upfront: it can, achieving competitive results on several benchmarks, but with important caveats.
P3: Method details (compressed).
P4: Key ablations and scaling laws.

This structure works well for empirical benchmark papers and would align better with the abstract's honest framing ("this paper does not describe a novel method").

### Alternative Storyline Option 3 (Benchmark + Design Guide)

Frame the paper as a "design guide for autoregressive video pre-training":

P1: Prior work has explored autoregressive image pre-training but not video.
P2: We provide the first systematic study of what design choices matter.
P3: Three actionable findings: (a) tokenizer choice matters less than expected; (b) coarse-to-fine resolution training saves compute and improves accuracy; (c) attention pooling is essential for decoder-only models.
P4: Scaling laws for compute-efficient video pre-training.

## Priority Revision Plan
The following revision actions are ordered by priority (P0 = must fix before resubmission, P1 = important, P2 = nice-to-have).

### P0 — Publication-Critical (Must Fix)

| # | Action | Target | Effort | Expected Impact |
|---|--------|--------|--------|-----------------|
| P0.1 | Correct real-world robotics narrative: replace "comparable/on-par" with accurate description of 63% vs 75% gap. Add confidence intervals. | Page 9, Table 11 | Low | Restores factual integrity; prevents immediate rejection on credibility grounds |
| P0.2 | Replace all "competitive across all tasks/benchmarks" claims with bounded, evidence-linked statements. | Abstract, Introduction, Conclusion | Low | Prevents overclaim detection and trust loss |
| P0.3 | Fix pre-training objective notation (Eq. 1-2) with standard autoregressive factorization and proper negative log-likelihood. | Page 3, Section 3.1 | Low | Improves reproducibility |
| P0.4 | Fix forward equation notation (Eq. 3-5) with distinct intermediate variables. | Page 4, Section 3.4 | Low | Eliminates symbol ambiguity |
| P0.5 | Add limitations section covering resolution gap, simulation-to-real transfer, data mixing sensitivity, and tokenizer dependency of scaling laws. | New subsection after Conclusion | Medium | Demonstrates scientific maturity; pre-empts reviewer concerns |

### P1 — Important (Should Fix for Strong Resubmission)

| # | Action | Target | Effort | Expected Impact |
|---|--------|--------|--------|-----------------|
| P1.1 | Bound novelty claims: qualify "first to show" with explicit scope (autoregressive next-token prediction on video, to our knowledge). | Sections 4.2, 4.3 | Low | Prevents unfalsifiable novelty claims |
| P1.2 | Remove or rephrase GPT-3 scaling comparison; add tokenizer-dependency caveat. | Section 4.8 | Low | Methodologically sound presentation |
| P1.3 | Add variance/confidence intervals for all main experiments. | Tables 3, 7, 8, 9, 10, 11 | Medium | Enables meaningful statistical inference |
| P1.4 | Add resolution-controlled DAVIS comparison (Toto at 224x224). | Section 4.5, Table 10 | Low | Fair comparison with DINO |
| P1.5 | Restructure Introduction to follow recommended storyline (gap → solution → evidence → bounded claims). | Page 1, Introduction | Medium | Reader engagement; clearer contribution positioning |

### P2 — Quality Improvement (Nice-to-Have)

| # | Action | Target | Effort | Expected Impact |
|---|--------|--------|--------|-----------------|
| P2.1 | Add data mixing ratio sensitivity analysis. | Section 3.3 | High | Strengthens empirical contribution |
| P2.2 | Add failure case analysis for DAVIS tracking and robotics. | Sections 4.5, 4.6 | Medium | Provides actionable insights |
| P2.3 | Compute scaling exponents for both VQGAN and dVAE tokenizers. | Section 4.8 | High | Validates scaling law generality |
| P2.4 | Add Ego4D frozen-feature evaluation (without fine-tuning or pyramid network). | Section 4.4 | Medium | Consistent protocol across tasks |
| P2.5 | Restructure Related Work around comparison axes. | Page 2, Section 2 | Medium | Improved positioning depth |
| P2.6 | Run real-world robotics with more trials (>30) to establish statistical significance. | Section 4.6 | Medium | Conclusive results |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (Data/Protocol) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-----------------------|---------|--------------|-----------------|-------------------|
| E1 | Tokenizer ablation: does tokenizer choice affect representation quality? | ImageNet-1k, Large model, 400 epochs, linear probing at optimal layer | ImageNet Top-1 | All tokenizers similar (60.6-61.3%), dVAE-16x16 worse (53.2%) | Yes, partially | No variance reported; VQGAN "contamination" claim not empirically validated |
| E2 | Probing method: does attention pooling outperform average pooling? | ImageNet-1k, Large model, same layer | ImageNet Top-1 | Attention pooling 7.9% better (61.1 vs 53.2) | Yes | Only tested at one layer; not tested on video tasks |
| E3 | Resolution: does coarse-to-fine training work? | ImageNet-1k, dVAE tokens | ImageNet Top-1 | 16→32 (63.2%) > 32-only (61.2%); +RoPE tuning 64.4% | Yes | Mechanism not explained; compute savings not quantified |
| E4 | Architecture comparison | ImageNet-1k, dVAE tokens, linear probing | ImageNet Top-1 | Toto (53.2%) > GPT2 (48.5%) > Mamba (40.7%) | Yes | Only one model size; Mamba not optimized for vision |
| E5 | ImageNet classification | Three model sizes, attention probing + fine-tuning | ImageNet Top-1 | 64.7/71.1/75.3% for base/large/1b | Partially | Trails MAE (80.9%) and AIM (82.2%); attention probing ≠ linear probing |
| E6 | K400 action recognition | Three model sizes, 16 frames, 128x128 | K400 Top-1 | 59.3/65.3/74.4% | Partially | Trails VideoMAE (79.8%); low resolution; unverifiable "first" claim |
| E7 | Ego4D action anticipation | Large model, fine-tuned + pyramid network | Overall mAP | 2.70 (highest among compared) | Partially | All scores near chance (mAP≤2.70); different protocol (fine-tuned vs frozen) |
| E8 | DAVIS video tracking | Three model sizes, label propagation, various resolutions | J&F, J, F | Best J&F 62.4 at 512/8 | Partially | Confounds resolution and capacity; at matched resolution Toto-base (42.0) < DINO-base (54.3) |
| E9 | Simulated robotic manipulation | Toto-base, frozen features, DAgger, 4 tasks | Mean success rate | Faster learning than MVP baseline | Yes | Only one baseline (MAE-based MVP); no error bars |
| E10 | Real-world robotic manipulation | Toto-base, frozen features, behavior cloning, 16 trials | Success rate | 63% (vs MVP 75%) | Partially/Negatively | Narrative contradicts results; small trial count; no confidence intervals |
| E11 | CATER object permanence | Toto-large, fine-tuned, 16/32 frames | Localization accuracy | 62.8/72.9% (beats V3D, TFC) | Yes | Single task; limited comparison set |
| E12 | Scaling laws | VQGAN tokenizer, a1-a6 models, µ-Param | Validation loss vs MACs | L(C)=7.42·C^{-0.0386} | Partially | Uses different tokenizer than main experiments; GPT-3 comparison invalid |

### Research-Theme Gap Diagnosis

**New Knowledge:** The paper's primary research value is in establishing a baseline for autoregressive video pre-training. The claim that "this works at scale" is supported by the scaling trends and the fact that three model sizes show consistent improvement. However, the paper does not provide new knowledge about *why* autoregressive video pre-training works or fails — it lacks mechanism-level analysis.

**Reproducibility/Reusability:** The paper commits to releasing models, training, and evaluation code, which is commendable. However, key details are missing: exact training steps per model, learning rate schedules for each model size, GPU-hours consumed, and data preprocessing pipeline details.

**Impact on Practice/Understanding:** The most impactful findings are: (a) coarse-to-fine resolution training saves compute; (b) attention pooling is critical for decoder-only models; (c) autoregressive video pre-training scales but at a shallower rate than language. However, these insights would be stronger with the proposed additional experiments.

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiments (Publication-Critical)

| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Expected Gain |
|-------------|-----------|---------------|----------|---------|-------------------|------|---------------|
| Real-world robotics: Toto is competitive with MVP | Toto is not competitive (null hypothesis) | Run 30+ additional trials for Toto and MVP on cube-picking; add 2 more task variants | Same demonstrations, same behavior cloning setup | Success rate ±95% CI | If Toto CI overlaps MVP CI, claims can be softened; if Toto is significantly worse, must rephrase | 2-3 days | Restores factual accuracy |
| Variance reporting across all experiments | Reported single-run results are reproducible | Re-run 3 seeds for ImageNet (base), K400 (large), DAVIS (large) | Same hyperparameters | Mean±std Top-1 | std < 0.5% for image tasks, < 1% for video tasks | 1-2 weeks | Statistical credibility |

#### P1 Experiments (Important)

| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Expected Gain |
|-------------|-----------|---------------|----------|---------|-------------------|------|---------------|
| Scaling law is tokenizer-independent | Scaling exponent differs by tokenizer | Repeat a1-a6 scaling with dVAE tokenizer | Same architecture, same training data | Validation loss vs MACs, exponent α | If α_dVAE differs from α_VQGAN by >0.01, add tokenizer-dependent caveat | 2-3 weeks | Validates scaling generality |
| DAVIS tracking: Toto is competitive at matched resolution | Resolution confounds comparison | Evaluate Toto-large at 224/8 and DINO at 512/8 | Same patch size, same evaluation protocol | J&F, J, F | If Toto-large at 224/8 < DINO-base at 224/8, add explicit comparison caveat | 1-2 days | Fair comparison |
| Data mixing ratio impact | Mixing ratio affects downstream performance | Compare 3 mixing ratios: current (20/10/10/60), uniform (25/25/25/25), ImageNet-heavy (50/16/16/18) | Same model, same token count | ImageNet Top-1, K400 Top-1 | If performance varies by >2%, add sensitivity discussion | 1 week | Empirical rigor |

#### P2 Experiments (Nice-to-Have)

| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Cost | Expected Gain |
|-------------|-----------|---------------|----------|---------|-------------------|------|---------------|
| Video pre-training helps more than image-only | Video data provides temporal signal missing from images | Pre-train Toto-large on ImageNet-only (same token count) vs video mixture | Same architecture, same optimizer | ImageNet Top-1, K400 Top-1, DAVIS J&F | If video-mixture outperforms image-only on DAVIS/K400 but not ImageNet, supports temporal transfer | 2-3 weeks | Core contribution evidence |
| Context length scaling | Longer context improves video understanding | Train Toto-large with 2K, 4K, 8K token contexts | Same data, same model size | Validation loss, K400 Top-1 | If 8K > 4K > 2K, add context scaling analysis | 2-3 weeks | Guides architecture decisions |
| Out-of-domain generalization | Toto features generalize beyond training distribution | Evaluate frozen features on 4 domain-shifted benchmarks | Same probing protocol | Accuracy drop relative to in-domain | Report relative drop; expected ≤15% | 1 week | Robustness evidence |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 5.5 / 10**

**Rationale:** The paper's primary value is as a large-scale empirical study establishing a baseline for autoregressive video pre-training. The scale of pre-training (1T tokens, three model sizes, diverse evaluation) is substantial and the ablation studies on tokenization, probing, and resolution are informative. However, the score is constrained by:

- **Research value:** Moderate. The paper does not claim a novel method and its main findings (autoregressive video pre-training works at scale) are confirmatory rather than surprising. The most novel findings (coarse-to-fine resolution training, attention pooling advantage) are individually useful but not transformative.
- **Novelty:** Low to moderate. The paper explicitly states it does not describe a novel method. The novelty lies in the scale and breadth of the empirical study rather than methodological invention. External literature verification is deferred (Retrieval-Disabled Mode).
- **Validity risk:** Moderate to high. The critical factual error in the robotics section (narrative claiming "comparable" for 63% vs 75%) undermines credibility. Multiple overclaims ("competitive across all tasks") weaken trust. The scaling law comparison with GPT-3 is methodologically invalid.
- **Reproducibility:** Moderate. The method is straightforward to implement (standard causal transformer + dVAE tokenization), but variance reporting is absent, and key details (exact training steps, GPU budget, data preprocessing pipeline) are missing.
- **Fixability:** High. The critical issues (correcting narrative, bounding claims, fixing notation) are low-effort corrections. The deeper issues (variance reporting, scaling law validation, resolution-controlled comparisons) require additional experiments but are well-scoped.

**Post-Revision Target: [6.5, 7.5] / 10**

If the authors complete all P0 and P1 revision items (correcting the robotics narrative, bounding claims, adding variance, fixing notation, adding limitations section, and improving the scaling law analysis), the paper could achieve a score in the 6.5-7.5 range. The paper would then be a solid empirical contribution — useful as a benchmark and design reference for autoregressive video pre-training — without claiming more than it delivers. The upper bound is limited by the inherent lack of methodological novelty, which is by the authors' own admission.